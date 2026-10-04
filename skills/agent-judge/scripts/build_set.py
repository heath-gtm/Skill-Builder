"""Build a judge test set: your clean outputs, plus copies with one mistake planted.

    python scripts/build_set.py --judges example/judges.py --clean example/clean --out judge-run

--clean is a folder of outputs you already reviewed and trust (.md or .txt, one per file).
Your judges file defines the planters:

    PLANTS  = {"judge_name": [(planter_function, how_many), ...]}
    HOLDOUT = {...}   # same shape; new mistake styles added after the first run

A planter takes one clean output and returns it with exactly one rule broken, or None
if it can't apply to that output. Because you wrote the edit, the right verdict is known
without anyone labelling failures by hand.

Writes <out>/judge-set.jsonl.
"""
import argparse
import importlib.util
import json
import os
import sys


def load(path):
    spec = importlib.util.spec_from_file_location("judges", path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(os.path.abspath(path)))
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judges", required=True, help="your judges file")
    ap.add_argument("--clean", required=True, help="folder of trusted outputs")
    ap.add_argument("--out", required=True, help="folder for the test set and results")
    args = ap.parse_args()

    mod = load(args.judges)
    names = list(mod.JUDGES)
    files = sorted(f for f in os.listdir(args.clean) if f.endswith((".md", ".txt")))
    if not files:
        sys.exit(f"No .md or .txt files in {args.clean}")
    clean = [(os.path.splitext(f)[0], open(os.path.join(args.clean, f), encoding="utf-8").read()) for f in files]

    rows = [{"id": cid, "kind": "clean", "variant": None, "text": text,
             "expected": {n: "pass" for n in names}} for cid, text in clean]

    plan = [(m, p, "planted") for m, p in getattr(mod, "PLANTS", {}).items()]
    plan += [(m, p, "holdout") for m, p in getattr(mod, "HOLDOUT", {}).items()]
    for i, (metric, planters, kind) in enumerate(plan):
        if metric not in mod.JUDGES:
            sys.exit(f"Planters name a judge that doesn't exist: {metric}")
        cursor = i * 3  # spread plants across the clean outputs
        for fn, want in planters:
            made = tried = 0
            while made < want and tried < len(clean):
                cid, text = clean[cursor % len(clean)]
                cursor += 1
                tried += 1
                out = fn(text)
                if out is None or out == text:
                    continue
                rows.append({"id": f"{cid}+{fn.__name__}", "kind": kind, "variant": fn.__name__,
                             "text": out, "expected": {metric: "fail"}})
                made += 1
            if made < want:
                print(f"note: {fn.__name__} planted {made} of {want} (not enough outputs it applies to)")

    os.makedirs(args.out, exist_ok=True)
    path = os.path.join(args.out, "judge-set.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    n_plant = sum(r["kind"] == "planted" for r in rows)
    n_hold = sum(r["kind"] == "holdout" for r in rows)
    print(f"{len(clean)} clean, {n_plant} planted, {n_hold} held out -> {path}")


if __name__ == "__main__":
    main()
