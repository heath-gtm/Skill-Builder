"""Build a pairwise test set: old vs new on the same inputs, plus pairs that test the judge.

    python scripts/build_pairs.py --judges example/judges.py --old example/old --new example/new \
        --reviewed example/reviewed --inputs example/inputs.jsonl --out pair-run

--old and --new are folders of outputs (.md or .txt, one per file). A file with the same
name in both folders is the same input run on the two prompt versions.
--reviewed is a folder of outputs a person already reviewed and trusts. They can come from
either version or from other inputs. They are the raw material for the trust test.
--inputs is optional: a .jsonl file with {"id": "<file name without extension>", "input": "..."}
so the judge sees what was asked. Without it the judge sees "(not given)".

Three kinds of trust pairs are built from the reviewed outputs:
    planted    a reviewed output vs a copy with one mistake planted by your planter.
               the judge must pick the clean side in both orders
    holdout    the same, with mistake styles you add after the first run (HOLDOUT)
    identical  a reviewed output vs itself. the judge must call it a tie in both orders

Your judges file defines the planters, the same way agent-judge does:
    PLANTS  = {"criterion": [(planter_function, how_many), ...]}
    HOLDOUT = {...}

Writes <out>/pair-set.jsonl.
"""
import argparse
import importlib.util
import json
import math
import os
import sys


def load(path):
    spec = importlib.util.spec_from_file_location("judges", path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(os.path.abspath(path)))
    spec.loader.exec_module(mod)
    return mod


def read_folder(folder):
    files = sorted(f for f in os.listdir(folder) if f.endswith((".md", ".txt")))
    return {os.path.splitext(f)[0]: open(os.path.join(folder, f), encoding="utf-8").read() for f in files}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judges", required=True, help="your judges file")
    ap.add_argument("--old", required=True, help="outputs from the old prompt")
    ap.add_argument("--new", required=True, help="outputs from the new prompt, same file names")
    ap.add_argument("--reviewed", required=True, help="outputs a person reviewed and trusts")
    ap.add_argument("--inputs", help="optional .jsonl of {id, input}")
    ap.add_argument("--identical", type=int, default=2, help="how many identical pairs to build")
    ap.add_argument("--out", required=True, help="folder for the pair set and results")
    args = ap.parse_args()

    mod = load(args.judges)
    names = list(mod.JUDGES)
    old, new, reviewed = read_folder(args.old), read_folder(args.new), read_folder(args.reviewed)
    inputs = {}
    if args.inputs:
        for line in open(args.inputs, encoding="utf-8"):
            if line.strip():
                row = json.loads(line)
                inputs[row["id"]] = row["input"]

    both = sorted(set(old) & set(new))
    if not both:
        sys.exit("No file name appears in both --old and --new. Name each output after its input.")
    for only in sorted(set(old) ^ set(new)):
        print(f"note: {only} is in one folder only, so it is not compared")
    if not reviewed:
        sys.exit(f"No .md or .txt files in {args.reviewed}")

    rows = [{"id": cid, "kind": "real", "input": inputs.get(cid, "(not given)"), "old": old[cid], "new": new[cid],
             "expected": {n: None for n in names}} for cid in both]

    clean = list(reviewed.items())
    for cid, text in clean[:args.identical]:
        rows.append({"id": f"{cid}=itself", "kind": "identical", "input": inputs.get(cid, "(not given)"),
                     "old": text, "new": text, "expected": {n: "tie" for n in names}})

    plan = [(m, p, "planted") for m, p in getattr(mod, "PLANTS", {}).items()]
    plan += [(m, p, "holdout") for m, p in getattr(mod, "HOLDOUT", {}).items()]
    step = next(s for s in (3, 5, 7, 2, 1) if math.gcd(s, len(clean)) == 1)  # reaches every output once
    slot = 0
    for i, (metric, planters, kind) in enumerate(plan):
        if metric not in mod.JUDGES:
            sys.exit(f"Planters name a criterion that doesn't exist: {metric}")
        cursor = i * 2
        for fn, want in planters:
            made = tried = 0
            while made < want and tried < len(clean):
                cid, text = clean[cursor % len(clean)]
                cursor += step
                tried += 1
                bad = fn(text)
                if bad is None or bad == text:
                    continue
                # alternate which slot holds the clean output, so the slot name carries no signal
                clean_slot = "new" if slot % 2 == 0 else "old"
                slot += 1
                pair = {"new": text, "old": bad} if clean_slot == "new" else {"old": text, "new": bad}
                rows.append({"id": f"{cid}+{fn.__name__}", "kind": kind, "input": inputs.get(cid, "(not given)"),
                             **pair, "expected": {metric: clean_slot}})
                made += 1
            if made < want:
                print(f"note: {fn.__name__} planted {made} of {want} (not enough outputs it applies to)")

    os.makedirs(args.out, exist_ok=True)
    path = os.path.join(args.out, "pair-set.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    count = {k: sum(r["kind"] == k for r in rows) for k in ("real", "planted", "holdout", "identical")}
    print(f"{count['real']} old vs new, {count['planted']} planted, {count['holdout']} held out, "
          f"{count['identical']} identical -> {path}")


if __name__ == "__main__":
    main()
