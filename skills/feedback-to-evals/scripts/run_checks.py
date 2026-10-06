"""Trust-test your script checks the same way you trust-test a judge. Free: no model calls.

    python scripts/run_checks.py --judges example/judges.py --clean example/outputs --out feedback-run

Some feedback is about shape, not meaning: a missing owner, a word cap, a banned character.
That goes to a script check, not a judge. A script check can still be wrong, so it gets the
same test: it should pass your clean outputs and fail copies with the mistake planted.

Your judges file defines:
    CHECKS         {"name": function(text) -> None if it passes, or a reason string if it fails}
    CHECK_PLANTS   {"name": [(planter_function, how_many), ...]}
    CHECK_HOLDOUT  {...}   same shape; new mistake styles added after the first run

Writes <out>/checks-report.md and prints it.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_set import load  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judges", required=True, help="your judges file")
    ap.add_argument("--clean", required=True, help="folder of trusted outputs")
    ap.add_argument("--out", required=True, help="folder for the report")
    args = ap.parse_args()

    mod = load(args.judges)
    checks = getattr(mod, "CHECKS", {})
    if not checks:
        sys.exit("No CHECKS in your judges file.")
    files = sorted(f for f in os.listdir(args.clean) if f.endswith((".md", ".txt")))
    clean = [(os.path.splitext(f)[0], open(os.path.join(args.clean, f), encoding="utf-8").read()) for f in files]

    lines = ["# Script check trust report", "",
             "| Check | False alarms on clean | Caught, planted | Caught, held out |", "|---|---|---|---|"]
    detail = []
    for i, (name, fn) in enumerate(checks.items()):
        alarms = [(cid, fn(text)) for cid, text in clean if fn(text)]
        counts = {}
        for kind, plan in (("planted", getattr(mod, "CHECK_PLANTS", {})), ("holdout", getattr(mod, "CHECK_HOLDOUT", {}))):
            made = caught = 0
            cursor = i * 3
            for planter, want in plan.get(name, []):
                n = tried = 0
                while n < want and tried < len(clean):
                    cid, text = clean[cursor % len(clean)]
                    cursor += 1
                    tried += 1
                    out = planter(text)
                    if out is None or out == text:
                        continue
                    n += 1
                    if fn(out):
                        caught += 1
                    else:
                        detail.append(f"- **{name}**, {kind} `{cid}+{planter.__name__}` missed: the check passed it")
                made += n
            counts[kind] = f"{caught} of {made}"
        lines.append(f"| `{name}` | {len(alarms)} of {len(clean)} | **{counts['planted']}** | **{counts['holdout']}** |")
        for cid, why in alarms:
            detail.append(f"- **{name}**, clean `{cid}` failed: {why}")
    lines += ["", "## Every disagreement, for a person to read", ""] + (detail or ["None."])
    report = "\n".join(lines) + "\n"
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "checks-report.md"), "w", encoding="utf-8") as f:
        f.write(report)
    print(report)


if __name__ == "__main__":
    main()
