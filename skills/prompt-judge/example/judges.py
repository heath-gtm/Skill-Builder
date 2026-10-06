"""Example pairwise judges for an account research brief. Copy this file and make it yours.

The prompt behind these briefs was rewritten: the old version wrote long Why paragraphs and
put the verdict at the bottom; the new version puts the decision first. Did that help, and
did it break anything? Three rules need meaning, so each gets a pairwise judge:

    decision_up_top                   a rep can act on the top of the brief alone (quality)
    because_names_cause_and_problem   the Because names a real cause and a real problem (must-always)
    no_outreach_copy                  nothing in the brief is a message to the prospect (must-never,
                                      zero tolerance)

Each judge sees output A and output B for the same input and answers A, B, or tie.
run_pairs.py asks twice, with the order swapped, and only a winner in both orders counts.
Anything a script can check (word caps, required lines, valid links) stays in a script.
"""
import re

from ragas.metrics import DiscreteMetric

PREAMBLE = (
    "You are comparing two outputs, A and B. Two versions of the same prompt produced them "
    "for the same input. Each output is an account research brief: a sales rep reads it, "
    "decides whether to reach out, and then writes their own message.\n"
    "Judge only the criterion below. Ignore length, layout, formatting, tone, and every "
    "other rule. Do not favor an output for coming first or second, or for being longer.\n"
    "Answer A if A is clearly better on this criterion, B if B is clearly better, and tie if "
    "they are equally good, equally bad, or the difference would not change what a rep does. "
    "When both outputs meet the rule, the answer is tie.\n"
    "Your answer names the BETTER output: the one that follows the rule more closely. If B "
    "breaks the rule and A does not, the answer is A.\n\n"
)

TAIL = (
    "\n\nInput (what was asked for):\n{input}\n\n"
    "Output A:\n{output_a}\n\n"
    "Output B:\n{output_b}\n\n"
    "Answer A, B, or tie, where the letter names the output that is better on this criterion."
)


def _judge(name, criterion):
    return DiscreteMetric(name=name, allowed_values=["A", "B", "tie"], prompt=PREAMBLE + criterion + TAIL)


DECISION = _judge("decision_up_top", (
    "CRITERION: a rep can act on the top of the brief alone.\n"
    "You are shown only the first 60 words of each output, on purpose: that is what a busy "
    "rep reads before deciding. Whatever is cut off does not count.\n"
    "Better: from those words alone the rep knows whether to reach out, the specific reason "
    "to do it now, and what to open with or ask.\n"
    "Worse: the rep would have to keep reading to find the decision, the reason, or the "
    "question; or the words are there but generic, so they give the rep nothing to act on."
))

BECAUSE = _judge("because_names_cause_and_problem", (
    "CRITERION: the Because line connects a cause to a problem.\n"
    "You are shown only the Because line of each output, on purpose: whatever is not in it "
    "does not count.\n"
    "A line meets the rule if it (a) names a specific cause AND a specific business problem "
    "the person likely owns, or (b) says in words that no problem maps to this company. A "
    "cause is a dated or observed signal (an acquisition, a new location, a hiring wave), or, "
    "when there is no signal, the person's role at a company that fits the customer profile. "
    "A problem is a named operational problem, such as dispatch overload or crew routing. "
    "'Low fit:' or 'Problem-led, no trigger:' at the start is allowed.\n"
    "A line breaks the rule if it names a problem with no cause, a cause with no problem, a "
    "vague stand-in for a problem ('the decision', 'the timing', 'growth'), or only restates "
    "the fit or the size.\n"
    "If one line meets the rule and the other breaks it, the one that meets it wins. If both "
    "meet it, tie."
))

NO_COPY = _judge("no_outreach_copy", (
    "CRITERION: the brief never contains outreach copy.\n"
    "Copy is words written to be sent or said to the prospect: an email, a DM, a greeting, a "
    "subject line, a sign-off, a call script, or a ready-to-send opening line, quoted or not. "
    "Copy is addressed to the prospect: a sentence to them in the second person, or a request "
    "for their time. Suggesting a subject line or a script counts as copy even when it is "
    "framed as a tip to the rep.\n"
    "Not copy: the Ask line (one question for the rep to test, in quotes); a proof point "
    "stated as a fact about a customer and a result, even though the rep may repeat it; "
    "advice that tells the rep what to talk about.\n"
    "If one output contains copy and the other does not, the one without copy wins. If "
    "neither contains copy, tie. If both do, tie."
))

JUDGES = {m.name: m for m in (DECISION, BECAUSE, NO_COPY)}

RULES = {
    "decision_up_top": {"kind": "quality"},
    "because_names_cause_and_problem": {"kind": "must-always"},
    "no_outreach_copy": {"kind": "must-never", "zero_tolerance": True},
}

# Start every judge small. On the build this kit came from, the small model on the copy rule
# kept naming the side that broke the rule instead of the better side, in one order only.
# That judge moved up a model; the others stayed small.
JUDGE_MODELS = {
    "decision_up_top": "claude-haiku-4-5-20251001",
    "because_names_cause_and_problem": "claude-haiku-4-5-20251001",
    "no_outreach_copy": "claude-sonnet-5-5",
}


def view(name, text):
    """Show each judge only what its rule covers."""
    if name == "decision_up_top":
        words = text.split()
        return " ".join(words[:60]) + (" [cut]" if len(words) > 60 else "")
    if name == "because_names_cause_and_problem":
        line = next((l for l in text.splitlines() if l.startswith("*Because")), "")
        return re.sub(r"^\*Because\*\s*", "", line).strip() or "(no Because line)"
    return text


# ---- planters: each breaks exactly one rule in a reviewed brief, so the right answer is known ----

def _set(text, label, new):
    out, n = re.subn(r"(?m)^\*" + re.escape(label) + r"\*.*$", lambda _: new, text, count=1)
    return out if n else None


def _first(text):
    return text.splitlines()[1].split(",")[0].split()[0]


def _company(text):
    return text.splitlines()[0].split(" · ", 1)[-1].rstrip("*")


def call_buried(text):
    lines = text.splitlines()
    filler = (f"{_company(text)} has served its area for years and competes with several local firms on "
              "price, service, and reliability. The market is fragmented, owners wear many hats, and "
              "software choices range from spreadsheets to dedicated platforms.")
    return "\n".join(lines[:1] + ["", filler, ""] + lines[1:]) + "\n"


def call_defers(text):
    out = _set(text, "Because", "*Because* See _Why now_ below.")
    return out and _set(out, "Open with", "*Open with* See the sources below.")


def call_generic(text):  # held out: added after the first run
    out = _set(text, "Open with", "*Open with* Our platform helps companies like theirs run better.")
    return out and _set(out, "Ask", "*Ask* \"What are your top priorities this year?\"")


def because_no_cause(text):
    return _set(text, "Because", f"*Because* {_first(text)} likely owns dispatch overload right now.")


def because_vague_problem(text):
    return _set(text, "Because", f"*Because* {_company(text)} is growing fast, so {_first(text)} "
                                 "likely owns the decision right now.")


def because_restates_fit(text):  # held out
    return _set(text, "Because", f"*Because* Low fit: {_company(text)} sits outside our size range.")


def copy_open_with(text):
    return _set(text, "Open with", f"*Open with* \"{_first(text)}, saw the news about {_company(text)}. "
                                   "Shops your size lose hours a week to this. Worth 15 minutes Thursday?\"")


def copy_subject_line(text):
    return _set(text, "Check first", f"*Check first* Use subject line: {_company(text)} and your busy season")


def copy_spoken_script(text):  # held out
    return _set(text, "Open with", f"*Open with* Tell {_first(text)}: we help shops like yours stop "
                                   "losing billable hours, then ask for 15 minutes this week.")


PLANTS = {
    "decision_up_top": [(call_buried, 1), (call_defers, 1)],
    "because_names_cause_and_problem": [(because_no_cause, 1), (because_vague_problem, 1)],
    "no_outreach_copy": [(copy_open_with, 1), (copy_subject_line, 1)],
}
HOLDOUT = {
    "decision_up_top": [(call_generic, 1)],
    "because_names_cause_and_problem": [(because_restates_fit, 1)],
    "no_outreach_copy": [(copy_spoken_script, 1)],
}
