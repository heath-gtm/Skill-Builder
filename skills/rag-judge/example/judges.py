"""Judges for a RAG answer: one file per question with ## Question, ## Sources, ## Answer.

Two rules need meaning, so each gets a judge:
    grounded                every claim in the answer is supported by the sources shown
    answers_when_it_can     answers when the sources hold the answer, declines when not
Whether retrieval found the right passage is a script (retrieval_check.py), not a judge.

The planters below work on any answer file in that format, so this file runs unchanged
on your own RAG's answers.
"""
import re

from ragas.metrics import DiscreteMetric

NOT_FOUND = "Not in the sources."

PREAMBLE = (
    "You are grading one rule for an answer produced by a retrieval system. The system was "
    "shown the numbered sources below and had to answer from them only. Judge only the rule "
    "below. Ignore style, length, and every other rule.\n\n"
)

GROUNDED = DiscreteMetric(
    name="grounded",
    allowed_values=["pass", "fail"],
    prompt=PREAMBLE + (
        "RULE: every factual claim in the Answer is supported by the Sources shown.\n"
        "Work in steps. 1. List each factual claim in the Answer. 2. For each, find the "
        "source text that says it. 3. Fail if any claim has no supporting source text.\n"
        "Supported means the sources say it, not that it is true or commonly known. A claim "
        "that is true in the world but absent from the sources is unsupported. A citation "
        "pointing at a source that does not say the claim does not count as support. A "
        "faithful paraphrase is supported. Extra context is fine when a shown source says "
        "it, even if it describes something different from the main answer, such as a "
        "related item or a conflict between two sources. An answer that says it is not in "
        "the sources passes.\n\n"
        "{output}\n\nAnswer pass or fail."
    ),
)

ANSWERS = DiscreteMetric(
    name="answers_when_it_can",
    allowed_values=["pass", "fail"],
    prompt=PREAMBLE + (
        "RULE: the Answer answers when the Sources contain what the Question asks, and "
        "declines when they do not.\n"
        "1. Decide whether the Sources contain what the Question asks for. If you think they "
        "do, quote the exact source text that holds it before deciding.\n"
        "2. If any source states what was asked, the Answer must answer it. Saying it is not "
        "in the sources is then a fail, however the question is worded.\n"
        "3. If they do not, the Answer must say so and stop. Guessing, estimating, or "
        "answering from general knowledge is a fail, even when hedged with words like "
        "'probably' or 'the sources do not say exactly, but'.\n"
        "Partly answerable questions pass if the Answer gives the part the sources hold and "
        "says what they do not. An answer that answers and then adds a caveat or notes a "
        "conflict between sources still answered.\n\n"
        "{output}\n\nAnswer pass or fail."
    ),
)

JUDGES = {m.name: m for m in (GROUNDED, ANSWERS)}
# Both judges start on Haiku in your own trust test. In the build this kit came from, Haiku
# was close but flip-flopped on a few clean answers, and Sonnet 5.5 held on both rules, so
# the sample ships on Sonnet. Measure on your own answers before you settle.
JUDGE_MODELS = {"grounded": "claude-sonnet-5-5", "answers_when_it_can": "claude-sonnet-5-5"}


def script_check(name, text):
    """What a regex catches: an answer with no citation at all."""
    ans = text.split("## Answer", 1)[-1].strip()
    return not ans.startswith(NOT_FOUND) and not re.search(r"\[[^\]]+#\d+\]", ans)


# ---- planters: each breaks exactly one rule ----

def _answer(text):
    return text.split("## Answer\n", 1)[-1].strip()


def _with_answer(text, new):
    return text.split("## Answer\n", 1)[0] + "## Answer\n" + new.strip() + "\n"


def _first_source(text):
    m = re.search(r"(?m)^\[([^\]]+#\d+)\]", text)
    return m.group(1) if m else None


def _answered(text):
    return not _answer(text).startswith(NOT_FOUND)


def add_unsupported_number(text):
    src = _first_source(text)
    if not (_answered(text) and src):
        return None
    return _with_answer(text, _answer(text) + f" Teams that follow this see about a 40% lift in the first quarter [{src}].")


def change_a_number(text):
    if not _answered(text):
        return None
    ans = _answer(text)
    m = re.search(r"(?<![#\w])(\d+)(?![\w#])", ans)
    if not m:
        return None
    n = int(m.group(1))
    return _with_answer(text, ans[:m.start()] + str(n * 2 + 1) + ans[m.end():])


def add_outside_knowledge(text):  # held out: true-sounding, not in the sources
    src = _first_source(text)
    if not (_answered(text) and src):
        return None
    return _with_answer(text, _answer(text) + f" This follows the MEDDIC qualification framework used by most enterprise sales teams [{src}].")


def guess_when_missing(text):
    if _answered(text):
        return None
    return _with_answer(text, "Based on the sources, the answer is about 20 percent, which is the usual benchmark.")


def decline_when_present(text):
    if not _answered(text):
        return None
    return _with_answer(text, NOT_FOUND)


def hedged_guess(text):  # held out: a guess wearing a disclaimer
    if _answered(text):
        return None
    return _with_answer(text, "The sources do not say exactly, but it is probably around 20 percent for most teams.")


# Sized for the 11-answer sample. On your own answers, aim for 8 to 12 planted per judge.
PLANTS = {
    "grounded": [(add_unsupported_number, 3), (change_a_number, 3)],
    "answers_when_it_can": [(guess_when_missing, 2), (decline_when_present, 3)],
}
HOLDOUT = {
    "grounded": [(add_outside_knowledge, 2)],
    "answers_when_it_can": [(hedged_guess, 1)],
}
