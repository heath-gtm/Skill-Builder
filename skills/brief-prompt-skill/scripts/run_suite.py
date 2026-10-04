#!/usr/bin/env python3
"""
run_suite.py: run brief_eval across many role configs and produce ONE branded
cross-team scorecard. This is the stress test for 'is the harness universal':
if every config runs through the same check types with no code changes, it is.

Usage:
  python run_suite.py --mock cfg_sdr.json cfg_ae.json cfg_csm.json cfg_mktg.json ...
  python run_suite.py --runs 5 cfg_*.json          # live, needs ANTHROPIC_API_KEY
"""
import argparse, glob, html, json, os, statistics, sys, time
import brief_eval as be

def eval_config(path, runs, api_key, mock_mode):
    cfg = json.load(open(path))
    mock = cfg.get("_mock") if mock_mode else None
    brief = be.eval_prompt(cfg["prompt"], "BRIEF", cfg, runs, api_key, True, mock)
    naive = None
    if cfg.get("baseline_prompt"):
        naive = be.eval_prompt(cfg["baseline_prompt"], "NAIVE", cfg, runs, api_key, True, mock)
    return {"cfg": cfg, "brief": brief, "naive": naive,
            "role": cfg.get("role_label", cfg.get("name"))}

def color(pct):
    return ("var(--good)" if pct >= .85 else
            "var(--mid)" if pct >= .6 else "var(--bad)")

def write_suite_html(rows, path):
    ts = time.strftime("%B %-d, %Y")
    # summary facts
    briefs = [r["brief"]["overall"] for r in rows]
    naives = [r["naive"]["overall"] for r in rows if r["naive"]]
    avg_brief = statistics.mean(briefs)
    avg_naive = statistics.mean(naives) if naives else 0
    avg_consist = statistics.mean([r["brief"]["consistency"] for r in rows])

    def role_card(r):
        b = r["brief"]; n = r["naive"]
        crits = "".join(
            f'<div class="crit"><div class="crit-top"><span class="crit-name">{html.escape(c)}</span>'
            f'<span class="crit-pct">{v*100:.0f}%</span></div>'
            f'<div class="track"><div class="fill" style="width:{v*100:.0f}%;background:{color(v)}"></div></div></div>'
            for c, v in b["by_criterion"].items())
        delta = ""
        if n:
            d = (b["overall"] - n["overall"]) * 100
            delta = f'<span class="delta">+{d:.0f} vs naive</span>'
        oc = color(b["overall"])
        return (f'<div class="card"><div class="card-h">'
                f'<span class="card-label">{html.escape(r["role"])}</span>'
                f'<span class="card-sub">{html.escape(r["cfg"]["name"])}</span></div>'
                f'<div class="bignums"><div><div class="bn" style="color:{oc}">{b["overall"]*100:.0f}%</div>'
                f'<div class="bn-l">Pass rate</div></div><div class="vr"></div>'
                f'<div><div class="bn">{b["consistency"]*100:.0f}%</div><div class="bn-l">Consistency</div></div>'
                f'<div class="vr"></div><div><div class="bn-badge">{delta}</div></div></div>'
                f'<div class="crits">{crits}</div></div>')

    cards = "".join(role_card(r) for r in rows)
    tpl = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BRIEF Across GTM | Eval Suite | Built GTM</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700;800&family=Geist+Mono:wght@500;700&display=swap');
.bg-root{ --accent:#2B5CE7; --good:#2B5CE7; --mid:#8a8a92; --bad:#FF6B2C; --ink:#101014; --body:#33333b; --sub:#33333b; --muted:#8a8a92; --line:#e4e2da; --pillbg:rgba(43,92,231,.07); --pillbd:rgba(43,92,231,.30); --paper:#F6F5EF;
  background:var(--paper); background-image:linear-gradient(rgba(43,92,231,.05) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(43,92,231,.05) 1.5px,transparent 1.5px); background-size:44px 44px; color:var(--body); min-height:100vh; font-family:'Geist',Inter,ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif; -webkit-font-smoothing:antialiased; line-height:1.5; }
.bg-root *{ box-sizing:border-box; }
.bg-head{ display:flex; align-items:center; justify-content:space-between; gap:16px; padding:16px 40px; border-bottom:2px solid var(--ink); background:rgba(246,245,239,.92); flex-wrap:wrap; }
.bg-wordmark{ font-family:'Geist Mono',monospace; font-weight:700; font-size:14px; letter-spacing:-.02em; color:#fff; background:var(--accent); border:2px solid var(--ink); border-radius:6px; box-shadow:3px 3px 0 var(--ink); padding:2px 9px; }
.bg-x{ color:var(--muted); } .bg-doctype{ font-family:'Geist Mono',monospace; font-weight:500; color:var(--ink); letter-spacing:.02em; }
.bg-view{ font-family:'Geist Mono',monospace; font-size:12px; letter-spacing:.1em; color:var(--ink); text-decoration:none; border-bottom:1px solid var(--ink); padding-bottom:2px; }
.bg-wrap{ max-width:900px; margin:0 auto; padding:60px 40px 96px; }
.bg-eyebrow{ display:flex; align-items:center; gap:12px; margin-bottom:20px; flex-wrap:wrap; }
.bg-k{ display:inline-block; font-family:'Geist Mono',monospace; font-size:12px; font-weight:700; letter-spacing:.12em; color:var(--ink); background:#fff; border:2px solid var(--ink); box-shadow:2px 2px 0 var(--ink); padding:3px 10px; transform:rotate(-1deg); }
.bg-pill{ font-family:'Geist Mono',monospace; font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--accent); background:var(--pillbg); border:1.5px solid var(--pillbd); border-radius:4px; padding:4px 10px; }
.bg-h1{ font-size:3.2rem; font-weight:800; letter-spacing:-.035em; line-height:1; color:var(--ink); margin:0; }
.bg-rule{ width:64px; height:6px; background:var(--accent); border-radius:0; margin:22px 0 0; }
.bg-lede{ font-size:17px; color:var(--body); line-height:1.6; max-width:660px; margin:18px 0 0; }
.bg-lede b{ color:var(--ink); font-weight:600; }
.summary{ display:grid; grid-template-columns:repeat(3,1fr); gap:2px; background:var(--ink); border:2px solid var(--ink); border-radius:10px; box-shadow:5px 5px 0 var(--ink); overflow:hidden; margin-top:36px; }
.sum{ background:#fff; padding:20px 22px; }
.sum-v{ font-size:34px; font-weight:800; letter-spacing:-.03em; color:var(--ink); line-height:1; }
.sum-l{ font-family:'Geist Mono',monospace; font-size:10px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); margin-top:8px; }
.snum{ font-family:'Geist Mono',monospace; font-size:12.5px; letter-spacing:.06em; color:var(--muted); margin:44px 0 14px; padding-top:32px; border-top:1px solid var(--line); }
.cards{ display:grid; grid-template-columns:1fr 1fr; gap:16px; }
.card{ background:#fff; border:2px solid var(--ink); border-radius:10px; box-shadow:5px 5px 0 var(--ink); padding:20px; }
.card-h{ margin-bottom:14px; }
.card-label{ font-family:'Geist Mono',monospace; font-size:12px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; color:var(--accent); display:block; }
.card-sub{ font-size:14px; font-weight:700; color:var(--ink); }
.bignums{ display:flex; align-items:center; gap:16px; padding:4px 0 16px; border-bottom:1px solid var(--line); margin-bottom:14px; }
.bn{ font-size:30px; font-weight:800; letter-spacing:-.03em; color:var(--ink); line-height:1; }
.bn-l{ font-family:'Geist Mono',monospace; font-size:9px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); margin-top:6px; }
.bn-badge .delta{ font-family:'Geist Mono',monospace; font-size:11px; font-weight:700; color:var(--accent); background:var(--pillbg); border:1.5px solid var(--pillbd); border-radius:4px; padding:4px 9px; white-space:nowrap; }
.vr{ width:1px; height:38px; background:var(--line); }
.crit{ margin-bottom:11px; }
.crit-top{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:4px; }
.crit-name{ font-family:'Geist Mono',monospace; font-size:11px; color:var(--body); }
.crit-pct{ font-family:'Geist Mono',monospace; font-size:11px; font-weight:700; color:var(--ink); }
.track{ height:6px; background:var(--paper); border:1px solid var(--line); border-radius:999px; overflow:hidden; }
.fill{ height:100%; border-radius:999px; }
.bg-callout{ margin-top:30px; padding:16px 18px; background:var(--pillbg); border:2px solid var(--accent); border-radius:8px; font-size:14.5px; color:var(--ink); line-height:1.6; }
.bg-callout .ck{ font-family:'Geist Mono',monospace; font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:var(--accent); margin-bottom:8px; }
.bg-foot{ margin-top:50px; padding-top:26px; border-top:2px solid var(--ink); font-size:14px; color:var(--sub); line-height:1.65; }
.bg-sig{ font-family:'Geist Mono',monospace; font-size:12px; text-transform:uppercase; letter-spacing:.14em; color:var(--muted); margin-top:16px; }
@media(max-width:760px){ .cards{ grid-template-columns:1fr; } .summary{ grid-template-columns:1fr; } }
@media(max-width:640px){ .bg-head{ padding:18px 22px; } .bg-wrap{ padding:44px 22px 72px; } .bg-h1{ font-size:2.2rem; } }
</style></head><body class="bg-root">
<header class="bg-head"><div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
<span class="bg-wordmark">[BUILT_GTM]</span>
<span class="bg-x">|</span><span class="bg-doctype">Eval suite</span></div>
<a class="bg-view" href="https://builtgtm.ai">BUILTGTM.AI &rarr;</a></header>
<main class="bg-wrap">
<div class="bg-eyebrow"><span class="bg-k">EVAL SUITE</span><span class="bg-pill">BRIEF across GTM</span></div>
<h1 class="bg-h1">One harness.<br>Every seat.</h1><div class="bg-rule"></div>
<p class="bg-lede">The same eval engine, run against __N__ role-specific BRIEF prompts. No code changed between them, only the config. <b>That is the test of universal.</b> Each card is one GTM seat: its pass rate, its run-to-run consistency, and the lift over the naive ask.</p>
<div class="summary">
<div class="sum"><div class="sum-v" style="color:__BC__">__AVGBRIEF__%</div><div class="sum-l">Avg BRIEF pass rate</div></div>
<div class="sum"><div class="sum-v">__AVGCON__%</div><div class="sum-l">Avg consistency</div></div>
<div class="sum"><div class="sum-v" style="color:var(--bad)">__AVGNAIVE__%</div><div class="sum-l">Avg naive pass rate</div></div>
</div>
<div class="snum">01 / Per-seat scorecards</div>
<div class="cards">__CARDS__</div>
<div class="bg-callout"><div class="ck">What this proves</div>
The check types (contains, ordered, regex, hard-stop, judge) held across SDR, AE, CSM, and Marketing without a single code change. Different seat, different rubric, same engine. That is the signal it is ready to lock as a skill.</div>
<footer class="bg-foot">Every seat runs its own brief. The harness does not care which. Point it at a config, get a receipt.
<div class="bg-sig">[BUILT_GTM] &middot; eval suite &middot; __TS__</div></footer>
</main></body></html>"""
    out = (tpl.replace("__N__", str(len(rows)))
              .replace("__AVGBRIEF__", f"{avg_brief*100:.0f}")
              .replace("__AVGNAIVE__", f"{avg_naive*100:.0f}")
              .replace("__AVGCON__", f"{avg_consist*100:.0f}")
              .replace("__BC__", color(avg_brief))
              .replace("__CARDS__", cards)
              .replace("__TS__", ts))
    open(path, "w").write(out)
    return path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("configs", nargs="+")
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--out", default="brief_suite_scorecard.html")
    a = ap.parse_args()
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not a.mock and not key:
        sys.exit("Set ANTHROPIC_API_KEY or use --mock.")
    paths = []
    for pat in a.configs:
        paths.extend(sorted(glob.glob(pat)) or [pat])
    rows = []
    for p in paths:
        print(f"\n=== {p} ===")
        rows.append(eval_config(p, a.runs, key, a.mock))
    out = write_suite_html(rows, a.out)
    print(f"\nSuite scorecard: {out}")
    for r in rows:
        n = f" | naive {r['naive']['overall']*100:.0f}%" if r["naive"] else ""
        print(f"  {r['role']:24s} brief {r['brief']['overall']*100:5.0f}%  "
              f"consist {r['brief']['consistency']*100:.0f}%{n}")

if __name__ == "__main__":
    main()
