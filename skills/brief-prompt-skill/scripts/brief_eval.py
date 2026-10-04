#!/usr/bin/env python3
"""
brief_eval.py: a universal eval harness for BRIEF prompts.

Point it at ANY prompt + rubric config and it measures the success rate:
runs the prompt N times per test case, scores every output against your
rubric (deterministic checks + LLM-as-judge), and writes a branded HTML
scorecard.

The prompt-specific stuff lives in a JSON config, NOT in this file. That is
what makes it universal: swap the config, eval a different use case, same
harness. Once you trust it across a few use cases, it locks in as a skill.

CONFIG SHAPE (see references/example_config.json):
{
  "name": "Closed Won / Lost Analysis",
  "model": "claude-sonnet-4-6",
  "prompt": "the full BRIEF prompt, with {data} where the input goes",
  "baseline_prompt": "optional naive prompt for the A/B, also uses {data}",
  "datasets": [ {"name": "...", "data": "...the input string..."} ],
  "structural_checks": [
     {"id": "all_blocks", "type": "contains_all",
      "values": ["WHY WE WIN", "WHY WE LOSE"], "desc": "..."},
     {"id": "order", "type": "ordered", "values": [...]},
     {"id": "counts", "type": "regex_min", "pattern": "\\d+\\s+deal",
      "min": 3},
     {"id": "no_summary", "type": "absent_after", "anchor": "NEXT MOVE",
      "values": ["in summary", "in conclusion"]}
  ],
  "judge_checks": [
     {"id": "supported", "question": "Is every claim backed by the data?"}
  ]
}

STRUCTURAL CHECK TYPES (deterministic, no API):
  contains_all   - all `values` appear in the output
  ordered        - `values` appear in this order
  regex_min      - `pattern` matches at least `min` times
  regex_absent   - `pattern` never matches
  absent_after   - none of `values` appear after `anchor` (hard-stop check)
  present_after  - a regex `pattern` appears after `anchor`

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  python brief_eval.py --config my_config.json --runs 5 --compare
  python brief_eval.py --config my_config.json --mock          # no API
  python brief_eval.py --config my_config.json --no-judge      # structural only
Output:
  brief_scorecard.html   (branded)  +  console summary
"""

import argparse, html, json, os, re, statistics, sys, time

# ---------------------------------------------------------------- model calls

def call_model(prompt, model, api_key, max_tokens=1500):
    import urllib.request
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=body,
        headers={"content-type": "application/json", "x-api-key": api_key,
                 "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read())
    return "".join(b.get("text", "") for b in data.get("content", []))

# ---------------------------------------------------------- structural checks

def run_structural(out, checks):
    up = out.upper()
    results = {}
    for c in checks:
        t = c["type"]
        if t == "contains_all":
            ok = all(v.upper() in up for v in c["values"])
        elif t == "ordered":
            pos = [up.find(v.upper()) for v in c["values"]]
            ok = all(p >= 0 for p in pos) and pos == sorted(pos)
        elif t == "regex_min":
            ok = len(re.findall(c["pattern"], out, re.I)) >= c.get("min", 1)
        elif t == "regex_absent":
            ok = not re.search(c["pattern"], out, re.I)
        elif t == "absent_after":
            i = up.find(c["anchor"].upper())
            tail = up[i:] if i >= 0 else up
            ok = i >= 0 and not any(v.upper() in tail for v in c["values"])
        elif t == "present_after":
            i = up.find(c["anchor"].upper())
            ok = i >= 0 and bool(re.search(c["pattern"], out[i:], re.I))
        else:
            ok = False
        results[c["id"]] = ok
    return results

# --------------------------------------------------------------- judge checks

def run_judge(out, data, checks, model, api_key):
    rubric = "\n".join(f'- {c["id"]}: {c["question"]}' for c in checks)
    prompt = (f"You are grading an output against a rubric. Be strict.\n\n"
              f"INPUT THE OUTPUT WAS GIVEN:\n{data}\n\n"
              f"OUTPUT TO GRADE:\n{out}\n\n"
              f"RUBRIC, strict yes/no each:\n{rubric}\n\n"
              f"Return ONLY JSON: keys = criterion ids, values = true/false.")
    raw = call_model(prompt, model, api_key)
    raw = re.sub(r'^```(?:json)?|```$', '', raw.strip(), flags=re.M).strip()
    try:
        parsed = json.loads(raw)
        return {c["id"]: bool(parsed.get(c["id"], False)) for c in checks}
    except Exception:
        return {c["id"]: False for c in checks}

# --------------------------------------------------------------------- runner

def eval_prompt(prompt_tpl, label, cfg, runs, api_key, use_judge, mock):
    rows, per_ds = [], []
    struct = cfg.get("structural_checks", [])
    judge = cfg.get("judge_checks", []) if use_judge else []
    model = cfg.get("model", "claude-sonnet-4-6")
    for ds in cfg["datasets"]:
        ds_frac = []
        for i in range(runs):
            if mock:
                out = mock[label][i % len(mock[label])]
            else:
                out = call_model(prompt_tpl.format(data=ds["data"]), model, api_key)
                time.sleep(0.4)
            row = run_structural(out, struct)
            if judge and not mock:
                row.update(run_judge(out, ds["data"], judge, model, api_key))
            elif judge and mock:
                row.update(mock.get(label + "_judge", [{}])[i % len(mock.get(label + "_judge", [{}]))])
            rows.append(row)
            ds_frac.append(sum(row.values()) / len(row) if row else 0)
            print(f"  [{label}] {ds['name']} run {i+1}/{runs}: "
                  f"{sum(row.values())}/{len(row)}")
        per_ds.append(statistics.mean(ds_frac))
    crit = list(rows[0].keys())
    by_c = {c: sum(r[c] for r in rows) / len(rows) for c in crit}
    overall = statistics.mean([sum(r.values()) / len(r) for r in rows])
    consistency = 1 - (statistics.pstdev(per_ds) if len(per_ds) > 1 else 0)
    return {"label": label, "overall": overall, "by_criterion": by_c,
            "consistency": consistency, "n": len(rows)}

# ---------------------------------------------------------------- console out

def print_report(results):
    print("\n" + "=" * 60)
    for r in results:
        print(f"\n  {r['label']}  ({r['n']} runs)")
        print(f"  overall {r['overall']*100:5.1f}%   consistency {r['consistency']*100:5.1f}%")
        for c, v in r["by_criterion"].items():
            print(f"    {c:24s} {v*100:5.1f}%  {'#'*int(v*20)}")
    if len(results) == 2:
        d = (results[0]["overall"] - results[1]["overall"]) * 100
        hi, lo = (results[0], results[1]) if d >= 0 else (results[1], results[0])
        print(f"\n  DELTA: {hi['label']} beats {lo['label']} by {abs(d):.1f} pts")
    print("=" * 60)

# ------------------------------------------------------- branded HTML report

def bar(pct):
    if pct >= 0.85: color = "var(--good)"
    elif pct >= 0.6: color = "var(--mid)"
    else: color = "var(--bad)"
    return (f'<div class="track"><div class="fill" style="width:{pct*100:.0f}%;'
            f'background:{color}"></div></div>')

def write_html(results, cfg, path):
    name = html.escape(cfg.get("name", "BRIEF Prompt"))
    ts = time.strftime("%B %-d, %Y")
    primary = results[0]
    delta_html = ""
    if len(results) == 2:
        d = (results[0]["overall"] - results[1]["overall"]) * 100
        hi, lo = (results[0], results[1]) if d >= 0 else (results[1], results[0])
        delta_html = (f'<div class="bg-callout"><div class="ck">The delta</div>'
                      f'<b>{html.escape(hi["label"])}</b> beats '
                      f'<b>{html.escape(lo["label"])}</b> by '
                      f'<b>{abs(d):.1f} points</b> on overall pass rate. Same model, '
                      f'same data. The difference is the brief.</div>')

    def scorecard(r):
        rows = "".join(
            f'<div class="crit"><div class="crit-top">'
            f'<span class="crit-name">{html.escape(c)}</span>'
            f'<span class="crit-pct">{v*100:.0f}%</span></div>{bar(v)}</div>'
            for c, v in r["by_criterion"].items())
        oc = ("var(--good)" if r["overall"] >= .85 else
              "var(--mid)" if r["overall"] >= .6 else "var(--bad)")
        return (f'<div class="card"><div class="card-h">'
                f'<span class="card-label">{html.escape(r["label"])}</span>'
                f'<span class="card-n">{r["n"]} runs</span></div>'
                f'<div class="bignums">'
                f'<div><div class="bn" style="color:{oc}">{r["overall"]*100:.0f}%</div>'
                f'<div class="bn-l">Overall pass rate</div></div>'
                f'<div class="vr"></div>'
                f'<div><div class="bn">{r["consistency"]*100:.0f}%</div>'
                f'<div class="bn-l">Run-to-run consistency</div></div>'
                f'</div><div class="crits">{rows}</div></div>')

    cards = "".join(scorecard(r) for r in results)
    tpl = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(name)s | Eval Scorecard | Built GTM</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700;800&family=Geist+Mono:wght@500;700&display=swap');
.bg-root{ --accent:#2B5CE7; --good:#2B5CE7; --mid:#8a8a92; --bad:#FF6B2C; --ink:#101014; --body:#33333b; --sub:#33333b; --muted:#8a8a92; --line:#e4e2da; --pillbg:rgba(43,92,231,.07); --pillbd:rgba(43,92,231,.30); --paper:#F6F5EF;
  background:var(--paper); background-image:linear-gradient(rgba(43,92,231,.05) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(43,92,231,.05) 1.5px,transparent 1.5px); background-size:44px 44px; color:var(--body); min-height:100vh; font-family:'Geist',Inter,ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif; -webkit-font-smoothing:antialiased; line-height:1.5; }
.bg-root *{ box-sizing:border-box; }
.bg-head{ display:flex; align-items:center; justify-content:space-between; gap:16px; padding:16px 40px; border-bottom:2px solid var(--ink); background:rgba(246,245,239,.92); flex-wrap:wrap; }
.bg-wordmark{ font-family:'Geist Mono',monospace; font-weight:700; font-size:14px; letter-spacing:-.02em; color:#fff; background:var(--accent); border:2px solid var(--ink); border-radius:6px; box-shadow:3px 3px 0 var(--ink); padding:2px 9px; }
.bg-x{ color:var(--muted); }
.bg-doctype{ font-family:'Geist Mono',monospace; font-weight:500; color:var(--ink); letter-spacing:.02em; }
.bg-view{ font-family:'Geist Mono',monospace; font-size:12px; letter-spacing:.1em; color:var(--ink); text-decoration:none; border-bottom:1px solid var(--ink); padding-bottom:2px; }
.bg-wrap{ max-width:860px; margin:0 auto; padding:60px 40px 96px; }
.bg-eyebrow{ display:flex; align-items:center; gap:12px; margin-bottom:20px; flex-wrap:wrap; }
.bg-k{ display:inline-block; font-family:'Geist Mono',monospace; font-size:12px; font-weight:700; letter-spacing:.12em; color:var(--ink); background:#fff; border:2px solid var(--ink); box-shadow:2px 2px 0 var(--ink); padding:3px 10px; transform:rotate(-1deg); }
.bg-pill{ font-family:'Geist Mono',monospace; font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--accent); background:var(--pillbg); border:1.5px solid var(--pillbd); border-radius:4px; padding:4px 10px; }
.bg-h1{ font-size:3.2rem; font-weight:800; letter-spacing:-.035em; line-height:1; color:var(--ink); margin:0; }
.bg-rule{ width:64px; height:6px; background:var(--accent); border-radius:0; margin:22px 0 0; }
.bg-lede{ font-size:17px; color:var(--body); line-height:1.6; max-width:640px; margin:18px 0 0; }
.bg-lede b{ color:var(--ink); font-weight:600; }
.cards{ display:grid; grid-template-columns:1fr; gap:18px; margin-top:40px; }
.card{ background:#fff; border:2px solid var(--ink); border-radius:10px; box-shadow:5px 5px 0 var(--ink); padding:24px; }
.card-h{ display:flex; align-items:center; gap:10px; margin-bottom:18px; }
.card-label{ font-family:'Geist Mono',monospace; font-size:13px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; color:var(--ink); }
.card-n{ font-family:'Geist Mono',monospace; font-size:11px; color:var(--muted); margin-left:auto; }
.bignums{ display:flex; align-items:center; gap:28px; padding:6px 0 22px; border-bottom:1px solid var(--line); margin-bottom:20px; }
.bn{ font-size:40px; font-weight:800; letter-spacing:-.03em; color:var(--ink); line-height:1; }
.bn-l{ font-family:'Geist Mono',monospace; font-size:10px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); margin-top:7px; }
.vr{ width:1px; height:44px; background:var(--line); }
.crit{ margin-bottom:14px; }
.crit-top{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:5px; }
.crit-name{ font-family:'Geist Mono',monospace; font-size:12px; color:var(--body); }
.crit-pct{ font-family:'Geist Mono',monospace; font-size:12px; font-weight:700; color:var(--ink); }
.track{ height:7px; background:var(--paper); border:1px solid var(--line); border-radius:999px; overflow:hidden; }
.fill{ height:100%; border-radius:999px; }
.bg-callout{ margin-top:26px; padding:16px 18px; background:var(--pillbg); border:2px solid var(--accent); border-radius:8px; font-size:14.5px; color:var(--ink); line-height:1.6; }
.bg-callout .ck{ font-family:'Geist Mono',monospace; font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:var(--accent); margin-bottom:8px; }
.bg-foot{ margin-top:50px; padding-top:26px; border-top:2px solid var(--ink); font-size:14px; color:var(--sub); line-height:1.65; }
.bg-sig{ font-family:'Geist Mono',monospace; font-size:12px; text-transform:uppercase; letter-spacing:.14em; color:var(--muted); margin-top:16px; }
@media(max-width:640px){ .bg-head{ padding:18px 22px; } .bg-wrap{ padding:44px 22px 72px; } .bg-h1{ font-size:2.3rem; } }
</style></head><body class="bg-root">
<header class="bg-head"><div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
<span class="bg-wordmark">[BUILT_GTM]</span>
<span class="bg-x">|</span><span class="bg-doctype">Eval scorecard</span></div>
<a class="bg-view" href="https://builtgtm.ai">BUILTGTM.AI &rarr;</a></header>
<main class="bg-wrap">
<div class="bg-eyebrow"><span class="bg-k">EVAL SCORECARD</span><span class="bg-pill">%(name)s</span></div>
<h1 class="bg-h1">The receipt on<br>the prompt.</h1><div class="bg-rule"></div>
<p class="bg-lede">Pass rate across <b>%(n)s runs</b>. Structural checks are parsed from the output. Judge checks are graded by a second model. <b>Consistency is the number that matters</b>: it says whether you get the same quality every run, or just got lucky once.</p>
<div class="cards">%(cards)s</div>
%(delta)s
<footer class="bg-foot">An eval is a test suite for a prompt. The Finish line wrote the rubric. This ran it.
<div class="bg-sig">[BUILT_GTM] &middot; eval scorecard &middot; %(ts)s</div></footer>
</main></body></html>"""
    out = (tpl.replace("%(name)s", name)
              .replace("%(n)s", str(primary["n"]))
              .replace("%(cards)s", cards)
              .replace("%(delta)s", delta_html)
              .replace("%(ts)s", ts))
    open(path, "w").write(out)
    return path

# --------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--no-judge", action="store_true")
    ap.add_argument("--out", default="brief_scorecard.html")
    a = ap.parse_args()

    cfg = json.load(open(a.config))
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not a.mock and not key:
        sys.exit("Set ANTHROPIC_API_KEY, or run with --mock.")
    mock = cfg.get("_mock") if a.mock else None
    use_judge = not a.no_judge

    print(f"\nEval: {cfg.get('name')}  (runs={a.runs}, mock={a.mock})")
    results = [eval_prompt(cfg["prompt"], "BRIEF", cfg, a.runs, key, use_judge, mock)]
    if (a.compare or a.mock) and cfg.get("baseline_prompt"):
        results.append(eval_prompt(cfg["baseline_prompt"], "NAIVE", cfg, a.runs, key, use_judge, mock))
    print_report(results)
    p = write_html(results, cfg, a.out)
    print(f"\nScorecard written: {p}")

if __name__ == "__main__":
    main()
