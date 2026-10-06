"""Did retrieval find the passage that holds the answer? A script, not a judge.

    python scripts/retrieval_check.py --questions example/questions.jsonl --answers rag-run/answers

Each answerable question in the questions file carries "evidence": a short phrase that
appears in the passage holding the answer. For each saved answer file, this checks
whether any source the answerer was shown contains that phrase. Finding the right
document is not enough: the passage with the answer has to be among the chunks shown.

It also flags answers that cite nothing, and unanswerable questions (no evidence) that
were answered instead of declined, so a person can look before any judge runs.
"""
import argparse
import json
import os
import re

NOT_FOUND = "Not in the sources."


def sections(text):
    parts = dict(re.findall(r"(?ms)^## (Question|Sources|Answer)\n(.*?)(?=^## |\Z)", text))
    return {k: v.strip() for k, v in parts.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", required=True)
    ap.add_argument("--answers", required=True)
    args = ap.parse_args()
    rows = [json.loads(l) for l in open(args.questions, encoding="utf-8") if l.strip()]
    hit = total = uncited = guessed = 0
    for r in rows:
        path = os.path.join(args.answers, f"{r['id']}.md")
        if not os.path.exists(path):
            print(f"{r['id']}: no answer file")
            continue
        s = sections(open(path, encoding="utf-8").read())
        ans = s.get("Answer", "")
        declined = ans.startswith(NOT_FOUND)
        notes = []
        if r.get("evidence"):
            total += 1
            found = r["evidence"].lower() in s.get("Sources", "").lower()
            hit += found
            notes.append("passage found" if found else "PASSAGE MISSED")
        elif not declined:
            guessed += 1
            notes.append("ANSWERED AN UNANSWERABLE QUESTION")
        if not declined and not re.search(r"\[[^\]]+#\d+\]", ans):
            uncited += 1
            notes.append("NO CITATION")
        print(f"{r['id']}: " + ", ".join(notes or ["declined, as expected"]))
    print(f"\nPassage found for {hit} of {total} answerable questions. "
          f"Uncited answers: {uncited}. Unanswerable questions answered: {guessed}.")


if __name__ == "__main__":
    main()
