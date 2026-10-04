"""Run your judges over the test set and report how far each one can be trusted.

    python scripts/run_judges.py --judges example/judges.py --out judge-run
    python scripts/run_judges.py --judges example/judges.py --out judge-run --repeats 5 --only no_outreach_copy

Your judges file defines:
    JUDGES        {"name": DiscreteMetric, ...}  each prompt uses the variable {output}
    JUDGE_MODELS  {"name": "model id"}           optional; default Claude Haiku 4.5
    view(name, text)                             optional; what each judge is shown
    script_check(name, text)                     optional; True if your format checker
                                                 already catches this rule on this text

The report (in <out>/results/<time>/) lists, per judge:
    false alarms   clean outputs it failed. each one needs a person to read it
    caught         planted and held out mistakes it failed on every repeat
    checker        the same mistakes your format checker caught, if you gave one
    consistency    the share of cases with the same verdict on every repeat
then every disagreement with the judge's reason.

Reads ANTHROPIC_API_KEY from the environment. Never prints it.
"""
import argparse
import asyncio
import json
import os
import sys
import time
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anthropic.resources.messages import AsyncMessages  # noqa: E402
from build_set import load  # noqa: E402
from claude_judge import DEFAULT_MODEL, claude_judge  # noqa: E402

USAGE = {"in": 0, "out": 0}
_create = AsyncMessages.create


async def _counted(self, *a, **kw):
    r = await _create(self, *a, **kw)
    if getattr(r, "usage", None):
        USAGE["in"] += r.usage.input_tokens
        USAGE["out"] += r.usage.output_tokens
    return r

AsyncMessages.create = _counted


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judges", required=True)
    ap.add_argument("--out", required=True, help="the folder build_set.py wrote to")
    ap.add_argument("--repeats", type=int, default=2)
    ap.add_argument("--only", nargs="*", help="judge names to run")
    ap.add_argument("--model", help="one model for every judge, overriding JUDGE_MODELS")
    ap.add_argument("--concurrency", type=int, default=8)
    args = ap.parse_args()

    mod = load(args.judges)
    judges = mod.JUDGES
    names = args.only or list(judges)
    view = getattr(mod, "view", lambda name, text: text)
    script_check = getattr(mod, "script_check", None)
    models = {n: args.model or getattr(mod, "JUDGE_MODELS", {}).get(n, DEFAULT_MODEL) for n in names}
    llms = {m: claude_judge(m) for m in set(models.values())}

    rows = [json.loads(l) for l in open(os.path.join(args.out, "judge-set.jsonl"), encoding="utf-8")]
    sem = asyncio.Semaphore(args.concurrency)
    jobs = [(r, n, k) for r in rows for n in names if n in r["expected"] for k in range(args.repeats)]

    async def one(r, n, k):
        async with sem:
            base = {"id": r["id"], "kind": r["kind"], "judge": n, "repeat": k, "expected": r["expected"][n]}
            try:
                res = await judges[n].ascore(llm=llms[models[n]], output=view(n, r["text"]))
                return {**base, "got": res.value, "reason": res.reason}
            except Exception as e:  # recorded, never counted as a verdict
                return {**base, "got": "error", "reason": f"{type(e).__name__}: {e}"[:300]}

    t0 = time.time()
    results = await asyncio.gather(*(one(*j) for j in jobs))
    secs = time.time() - t0

    stamp = time.strftime("%Y-%m-%d-%H%M%S")
    outdir = os.path.join(args.out, "results", stamp)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "verdicts.jsonl"), "w", encoding="utf-8") as f:
        for x in results:
            f.write(json.dumps(x) + "\n")

    by = defaultdict(list)
    for x in results:
        by[(x["judge"], x["id"])].append(x)
    text = {r["id"]: r["text"] for r in rows}

    lines = [f"# Judge trust report, {stamp}", "",
             f"{len(results)} judge calls, {args.repeats} repeat(s), {secs:.0f}s. "
             f"Tokens: {USAGE['in']:,} in, {USAGE['out']:,} out.", "",
             "Models: " + ", ".join(f"`{n}` {models[n]}" for n in names), "",
             "| Judge | False alarms on clean | Caught, planted | Caught, held out | Checker caught | Consistency |",
             "|---|---|---|---|---|---|"]
    detail = []
    for n in names:
        groups = {k: [v for (j, _), v in by.items() if j == n and v[0]["kind"] == k]
                  for k in ("clean", "planted", "holdout")}
        every = groups["clean"] + groups["planted"] + groups["holdout"]
        errors = sum(x["got"] == "error" for v in every for x in v)
        alarms = [v for v in groups["clean"] if any(x["got"] == "fail" for x in v)]
        caught = {k: [v for v in groups[k] if all(x["got"] == "fail" for x in v)] for k in ("planted", "holdout")}
        missed = [v for k in ("planted", "holdout") for v in groups[k] if v not in caught[k]]
        bad = groups["planted"] + groups["holdout"]
        checker = (f"{sum(bool(script_check(n, text[v[0]['id']])) for v in bad)} of {len(bad)}"
                   if script_check else "n/a")
        steady = sum(len({x["got"] for x in v}) == 1 for v in every) / max(1, len(every))
        lines.append(f"| `{n}` | {len(alarms)} of {len(groups['clean'])} | "
                     f"**{len(caught['planted'])} of {len(groups['planted'])}** | "
                     f"**{len(caught['holdout'])} of {len(groups['holdout'])}** | {checker} | {steady:.2f} |"
                     + (f" {errors} errors" if errors else ""))
        for v in alarms:
            detail.append(f"- **{n}**, clean `{v[0]['id']}` failed ({'/'.join(x['got'] for x in v)}): "
                          f"{v[0]['reason'][:400]}")
        for v in missed:
            detail.append(f"- **{n}**, {v[0]['kind']} `{v[0]['id']}` missed ({'/'.join(x['got'] for x in v)}): "
                          f"{v[0]['reason'][:400]}")
    lines += ["", "A mistake counts as caught only if every repeat failed it. A clean output counts as a "
              "false alarm if any repeat failed it.", "",
              "## Every disagreement, for a person to read", "",
              "For each one, decide: the judge is wrong (fix the rubric or the view), the earlier review "
              "was wrong (count it as a catch), or the contract is vague (a person rules, then the rubric "
              "follows the contract).", ""]
    lines += detail or ["None."]
    report = "\n".join(lines) + "\n"
    with open(os.path.join(outdir, "report.md"), "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    print("saved:", outdir)


if __name__ == "__main__":
    asyncio.run(main())
