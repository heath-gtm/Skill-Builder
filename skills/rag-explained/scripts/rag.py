"""A small RAG you can read in one sitting: chunk your docs, find the right chunks, answer from them.

    python scripts/rag.py index --docs example/docs --out rag-run
    python scripts/rag.py ask   --out rag-run "How many days of leave do new hires get?"
    python scripts/rag.py batch --out rag-run --questions example/questions.jsonl

index   splits every .md or .txt file in --docs into chunks of about CHUNK_WORDS words
        (on headings first, then paragraphs) and saves them to <out>/chunks.jsonl.
ask     finds the TOP_K chunks that share the most rare words with the question (BM25,
        the keyword ranking search engines used for decades, no embeddings needed), then
        asks Claude to answer from those chunks only, citing them, or to say the answer
        is not in the sources.
batch   runs ask for every line of a questions file and saves one .md per question in
        <out>/answers/: the question, the chunks it was shown, and the answer. That is
        exactly what the rag-judge skill grades.

Reads ANTHROPIC_API_KEY from the environment. Never prints it.
"""
import argparse
import json
import math
import os
import re
import sys
from collections import Counter

CHUNK_WORDS = 220
TOP_K = 4
MODEL = "claude-opus-5-5"
NOT_FOUND = "Not in the sources."

STOP = set("""a an and are as at be but by for from has have how i if in into is it its of on or
that the their them then there these they this to was were what when where which who why will
with you your do does did can could should would not no so than too very just about over""".split())


def words(text):
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]


# ---- index ----------------------------------------------------------------------------
def split_doc(name, text):
    """Headings first, then paragraphs, packed up to CHUNK_WORDS. Each chunk keeps its heading."""
    text = re.sub(r"^---\n[\s\S]*?\n---\n", "", text)  # drop frontmatter
    sections = re.split(r"(?m)^(?=#{1,3} )", text)
    chunks = []
    for sec in sections:
        lines = sec.strip().splitlines()
        if not lines:
            continue
        heading = lines[0].lstrip("#").strip() if lines[0].startswith("#") else ""
        body = "\n".join(lines[1:] if heading else lines).strip()
        buf = []
        for para in re.split(r"\n\s*\n", body):
            if buf and len(" ".join(buf).split()) + len(para.split()) > CHUNK_WORDS:
                chunks.append((heading, "\n\n".join(buf)))
                buf = []
            buf.append(para.strip())
        if buf and " ".join(buf).strip():
            chunks.append((heading, "\n\n".join(buf)))
    return [{"id": f"{name}#{i + 1}", "doc": name, "heading": h, "text": t} for i, (h, t) in enumerate(chunks)]


def index(docs_dir, out):
    files = sorted(f for f in os.listdir(docs_dir) if f.endswith((".md", ".txt")))
    if not files:
        sys.exit(f"No .md or .txt files in {docs_dir}")
    chunks = []
    for f in files:
        chunks += split_doc(os.path.splitext(f)[0], open(os.path.join(docs_dir, f), encoding="utf-8").read())
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "chunks.jsonl"), "w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps(c) + "\n")
    print(f"{len(files)} docs -> {len(chunks)} chunks -> {os.path.join(out, 'chunks.jsonl')}")


# ---- retrieve ---------------------------------------------------------------------------
def load_chunks(out):
    path = os.path.join(out, "chunks.jsonl")
    if not os.path.exists(path):
        sys.exit(f"Run index first: no {path}")
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def retrieve(question, chunks, k=TOP_K, k1=1.5, b=0.75):
    """BM25: a chunk scores high when it contains the question's rarer words, a few times."""
    docs = [words(c["heading"] + " " + c["text"]) for c in chunks]
    avg = sum(map(len, docs)) / max(1, len(docs))
    df = Counter(w for d in docs for w in set(d))
    n = len(docs)
    q = words(question)
    scored = []
    for c, d in zip(chunks, docs):
        tf = Counter(d)
        s = 0.0
        for w in q:
            if w in tf:
                idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * tf[w] * (k1 + 1) / (tf[w] + k1 * (1 - b + b * len(d) / avg))
        scored.append((s, c))
    scored.sort(key=lambda x: -x[0])
    return [c for s, c in scored[:k] if s > 0]


# ---- answer -----------------------------------------------------------------------------
SYSTEM = (
    "You answer questions using only the numbered sources you are given. Every sentence "
    "of your answer must be supported by a source, and you cite it in square brackets, "
    "like [doc#2]. Do not use anything you know that the sources do not say. If the "
    f"sources do not contain the answer, reply with exactly: {NOT_FOUND} "
    "Keep answers under 120 words."
)


def answer(question, hits, model=MODEL):
    import anthropic

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY first.")
    sources = "\n\n".join(f"[{c['id']}] {c['heading']}\n{c['text']}" for c in hits) or "(no sources found)"
    client = anthropic.Anthropic(timeout=120.0)  # fail loudly instead of hanging; the SDK retries twice
    r = client.messages.create(
        model=model, max_tokens=2000, system=SYSTEM,
        messages=[{"role": "user", "content": f"Sources:\n\n{sources}\n\nQuestion: {question}"}],
    )
    text = "".join(b.text for b in r.content if b.type == "text").strip()
    return text, r.usage


def as_markdown(question, hits, text):
    src = "\n\n".join(f"[{c['id']}] {c['heading']}\n{c['text']}" for c in hits) or "(no sources found)"
    return f"## Question\n{question}\n\n## Sources\n{src}\n\n## Answer\n{text}\n"


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("index"); p.add_argument("--docs", required=True); p.add_argument("--out", required=True)
    p = sub.add_parser("ask"); p.add_argument("--out", required=True); p.add_argument("question")
    p.add_argument("--model", default=MODEL)
    p = sub.add_parser("batch"); p.add_argument("--out", required=True); p.add_argument("--questions", required=True)
    p.add_argument("--model", default=MODEL)
    args = ap.parse_args()

    if args.cmd == "index":
        return index(args.docs, args.out)

    chunks = load_chunks(args.out)
    if args.cmd == "ask":
        hits = retrieve(args.question, chunks)
        text, _ = answer(args.question, hits, args.model)
        print(as_markdown(args.question, hits, text))
        return

    adir = os.path.join(args.out, "answers")
    os.makedirs(adir, exist_ok=True)
    tin = tout = 0
    rows = [json.loads(l) for l in open(args.questions, encoding="utf-8") if l.strip()]
    for row in rows:
        hits = retrieve(row["question"], chunks)
        text, usage = answer(row["question"], hits, args.model)
        tin += usage.input_tokens
        tout += usage.output_tokens
        with open(os.path.join(adir, f"{row['id']}.md"), "w", encoding="utf-8") as fh:
            fh.write(as_markdown(row["question"], hits, text))
        shown = " ".join(c["text"] for c in hits).lower()
        if row.get("evidence"):
            got = "passage found" if row["evidence"].lower() in shown else "PASSAGE MISSED"
        else:
            got = "no answer expected"
        print(f"{row['id']}: {got} | {'declined' if text.startswith(NOT_FOUND) else 'answered'}")
    print(f"{len(rows)} answers -> {adir}. Tokens: {tin:,} in, {tout:,} out.")


if __name__ == "__main__":
    main()
