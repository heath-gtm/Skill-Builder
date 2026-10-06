"""Judge every pair in both orders and report: can the judge be trusted, and did the change help?

    python scripts/run_pairs.py --judges example/judges.py --out pair-run
    python scripts/run_pairs.py --judges example/judges.py --out pair-run --only no_outreach_copy --model claude-sonnet-5-5

Your judges file defines:
    JUDGES        {"criterion": DiscreteMetric, ...}  allowed_values ["A", "B", "tie"]; each prompt
                                                     uses {input}, {output_a} and {output_b}
    RULES         {"criterion": {"kind": "must-never" | "must-always" | "quality",
                                 "zero_tolerance": True or False}}      optional
    JUDGE_MODELS  {"criterion": "model id"}           optional; default Claude Haiku 4.5
    view(name, text)                                  optional; what each judge is shown

Every pair runs twice per criterion: old as A, then new as A. A winner counts only when it
wins in both orders. Opposite winners (a flip) and a winner in one order with a tie in the
other (a split) both count as a tie and as a position inconsistency.

The report (in <out>/results/<time>/) has:
    trust test      planted and held out: the clean side won in both orders
                    identical: a tie in both orders
                    position consistency: the same verdict in both orders
    old vs new      per criterion: new wins, old wins, ties
    regression list every must-never criterion where old won, even if new wins overall,
                    and every zero-tolerance criterion where old won in even one order
then every miss and every loss with the judge's reason.

Reads ANTHROPIC_API_KEY from the environment. Never prints it.
"""
import argparse
import asyncio
import json
import os
import sys
import time
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Ragas sends a usage ping with a blocking HTTP call inside the event loop. When its endpoint
# stalls, every judge call stalls with it. Turn it off.
os.environ.setdefault("RAGAS_DO_NOT_TRACK", "true")
from anthropic.resources.messages import AsyncMessages  # noqa: E402
from build_pairs import load  # noqa: E402
from claude_judge import DEFAULT_MODEL, claude_judge  # noqa: E402

PRICE = {"claude-haiku-4-5-20251001": (1, 5), "claude-sonnet-5-5": (2, 10)}  # $ per million tokens, in and out
USAGE = defaultdict(lambda: {"in": 0, "out": 0})
_create = AsyncMessages.create


async def _counted(self, *a, **kw):
    r = await _create(self, *a, **kw)
    if getattr(r, "usage", None):
        USAGE[kw.get("model", "?")]["in"] += r.usage.input_tokens
        USAGE[kw.get("model", "?")]["out"] += r.usage.output_tokens
    return r

AsyncMessages.create = _counted


def combine(a, b):
    """The two orders' verdicts (old, new, or tie) -> (outcome, agreement)."""
    if "error" in (a, b):
        return "error", "error"
    if a == b:
        return a, "consistent"
    return "tie", ("split" if "tie" in (a, b) else "flip")


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judges", required=True)
    ap.add_argument("--out", required=True, help="the folder build_pairs.py wrote to")
    ap.add_argument("--only", nargs="*", help="criteria to run")
    ap.add_argument("--kinds", nargs="*", default=["real", "planted", "holdout", "identical"])
    ap.add_argument("--model", help="one model for every criterion, overriding JUDGE_MODELS")
    ap.add_argument("--concurrency", type=int, default=8)
    args = ap.parse_args()

    mod = load(args.judges)
    judges = mod.JUDGES
    names = args.only or list(judges)
    rules = getattr(mod, "RULES", {})
    view = getattr(mod, "view", lambda name, text: text)
    models = {n: args.model or getattr(mod, "JUDGE_MODELS", {}).get(n, DEFAULT_MODEL) for n in names}
    llms = {m: claude_judge(m) for m in set(models.values())}

    rows = [json.loads(l) for l in open(os.path.join(args.out, "pair-set.jsonl"), encoding="utf-8")]
    rows = [r for r in rows if r["kind"] in args.kinds]
    sem = asyncio.Semaphore(args.concurrency)
    jobs = [(r, n, o) for r in rows for n in names if n in r["expected"] for o in ("old_first", "new_first")]

    async def one(r, n, order):
        a, b = ("old", "new") if order == "old_first" else ("new", "old")
        base = {"id": r["id"], "kind": r["kind"], "criterion": n, "order": order, "expected": r["expected"][n]}
        err = ""
        async with sem:
            for attempt in range(3):
                try:
                    res = await asyncio.wait_for(judges[n].ascore(llm=llms[models[n]], input=r["input"],
                                                 output_a=view(n, r[a]), output_b=view(n, r[b])), timeout=120)  # a hung call is retried, not waited on forever
                    return {**base, "said": res.value, "side": {"A": a, "B": b}.get(res.value, "tie"),
                            "reason": res.reason}
                except Exception as e:  # recorded, never counted as a verdict
                    err = f"{type(e).__name__}: {e}"[:300]
                    await asyncio.sleep(2 * (attempt + 1))
        return {**base, "said": "error", "side": "error", "reason": err}

    t0 = time.time()
    results = await asyncio.gather(*(one(*j) for j in jobs))
    secs = time.time() - t0

    stamp = time.strftime("%Y-%m-%d-%H%M%S")
    outdir = os.path.join(args.out, "results", stamp)
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "verdicts.jsonl"), "w", encoding="utf-8") as f:
        for x in results:
            f.write(json.dumps(x) + "\n")

    by = defaultdict(dict)
    for x in results:
        by[(x["criterion"], x["id"])][x["order"]] = x
    pairs = []
    for (n, cid), d in by.items():
        a, b = d["old_first"], d["new_first"]
        outcome, agree = combine(a["side"], b["side"])
        pairs.append({"criterion": n, "id": cid, "kind": a["kind"], "expected": a["expected"],
                      "outcome": outcome, "agree": agree, "a": a, "b": b})

    def sel(n, kind):
        return [p for p in pairs if p["criterion"] == n and p["kind"] == kind]

    cost = sum(u["in"] / 1e6 * PRICE.get(m, (0, 0))[0] + u["out"] / 1e6 * PRICE.get(m, (0, 0))[1]
               for m, u in USAGE.items())
    tokens_in = sum(u["in"] for u in USAGE.values())
    tokens_out = sum(u["out"] for u in USAGE.values())
    lines = [f"# Prompt judge report, {stamp}", "",
             f"{len(results)} judge calls, both orders, {secs:.0f}s. Tokens: {tokens_in:,} in, {tokens_out:,} out. "
             f"Cost about ${cost:.2f}.", "",
             "Models: " + ", ".join(f"`{n}` {models[n]}" for n in names), ""]

    misses = []
    lines += ["## Can the judge be trusted?", "",
              "| Criterion | Planted: clean side won both orders | Held out: same | Identical: tie both orders | Same verdict both orders | Flips |",
              "|---|---|---|---|---|---|"]
    for n in names:
        pl, ho, ident = sel(n, "planted"), sel(n, "holdout"), sel(n, "identical")
        every = [p for p in pairs if p["criterion"] == n]
        errors = sum(p["agree"] == "error" for p in every)
        lines.append(f"| `{n}` | **{sum(p['outcome'] == p['expected'] for p in pl)} of {len(pl)}** | "
                     f"**{sum(p['outcome'] == p['expected'] for p in ho)} of {len(ho)}** | "
                     f"{sum(p['outcome'] == 'tie' and p['agree'] == 'consistent' for p in ident)} of {len(ident)} | "
                     f"{sum(p['agree'] == 'consistent' for p in every)} of {len(every)} | "
                     f"{sum(p['agree'] == 'flip' for p in every)} |" + (f" {errors} errors" if errors else ""))
        for p in pl + ho:
            if p["outcome"] != p["expected"]:
                misses.append(f"- **{n}**, {p['kind']} `{p['id']}`: the clean side is {p['expected']}. Got "
                              f"{p['a']['side']} with old as A, {p['b']['side']} with new as A. "
                              f"Judge: {p['b']['reason'][:400]}")
        for p in ident:
            if not (p["outcome"] == "tie" and p["agree"] == "consistent"):
                misses.append(f"- **{n}**, identical `{p['id']}`: said {p['a']['said']} / {p['b']['said']}. "
                              f"Judge: {p['a']['reason'][:300]}")
    lines += ["", "A judge counts toward a decision only after it picks the clean side of every planted "
              "pair in both orders and calls identical pairs a tie.", ""]

    regress, losses = [], []
    lines += ["## Did the change help?", "",
              "| Criterion | Kind | New wins | Old wins | Ties | of which splits | of which flips |",
              "|---|---|---|---|---|---|---|"]
    for n in names:
        rule = rules.get(n, {})
        kind = rule.get("kind", "quality") + (", zero tolerance" if rule.get("zero_tolerance") else "")
        rp = sel(n, "real")
        c = Counter(p["outcome"] for p in rp)
        lines.append(f"| `{n}` | {kind} | {c['new']} | {c['old']} | {c['tie']} | "
                     f"{sum(p['agree'] == 'split' for p in rp)} | {sum(p['agree'] == 'flip' for p in rp)} |")
        for p in rp:
            why = p["b"]["reason"] if p["b"]["side"] == "old" else p["a"]["reason"]
            leans_old = p["agree"] == "split" and "old" in (p["a"]["side"], p["b"]["side"])
            if p["outcome"] == "old" and rule.get("kind") == "must-never":
                regress.append(f"- **{n}**, `{p['id']}`: old won in both orders. Judge: {why[:400]}")
            elif (p["outcome"] == "old" or leans_old) and rule.get("zero_tolerance"):
                regress.append(f"- **{n}**, `{p['id']}`: old won in one order, a tie in the other. "
                               f"Read it. Judge: {why[:400]}")
            elif p["outcome"] == "old":
                losses.append(f"- **{n}**, `{p['id']}`: {why[:400]}")
    lines += ["", "## Regression list", "",
              "Every case where the new version is worse on a must-never rule, even if it wins overall.", ""]
    lines += regress or ["None."]
    lines += ["", "## Other losses, for a person to read", ""] + (losses or ["None."])
    lines += ["", "## Trust-test misses, for a person to read", "",
              "For each one, decide: the judge is wrong (fix the rubric or the view), the planted mistake "
              "is not really a mistake (fix the planter), or the rule is vague (a person rules, then the "
              "rubric follows).", ""] + (misses or ["None."])

    report = "\n".join(lines) + "\n"
    with open(os.path.join(outdir, "report.md"), "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    print("saved:", outdir)


if __name__ == "__main__":
    asyncio.run(main())
