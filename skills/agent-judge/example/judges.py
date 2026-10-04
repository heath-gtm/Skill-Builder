"""Example judges for an account research brief. Copy this file and make it yours.

The agent behind these briefs writes one page for a sales rep: a verdict, a person line,
a *Because* line (why reach out now), proof material, and the evidence. Two of its rules
need meaning, so each gets a judge:

    because_names_cause_and_problem   the Because names a real cause and a real problem
    no_outreach_copy                  nothing in the brief is a message to the prospect

Everything else about the brief (word caps, required lines, valid links) belongs in a
format checker, not here.
"""
import re

from ragas.metrics import DiscreteMetric

PREAMBLE = (
    "You are grading one rule of a contract for an account research brief. A sales rep "
    "reads the brief, then writes their own message to the prospect. Judge only the rule "
    "below. Ignore length, formatting, style, and every other rule.\n\n"
)

BECAUSE = DiscreteMetric(
    name="because_names_cause_and_problem",
    allowed_values=["pass", "fail"],
    prompt=PREAMBLE + (
        "RULE: the *Because* line connects a cause to a problem.\n"
        "You are shown only the *Because* line, on purpose: whatever is not in it does not count.\n"
        "Pass if the line does one of these:\n"
        "(a) names a specific cause AND a specific business problem the person likely owns. "
        "A cause is a dated or observed signal (an acquisition, a new location, a hiring wave), "
        "or, when there is no signal, the person's role at a company that fits the customer "
        "profile. A problem is a named operational problem, such as dispatch chaos or "
        "technician productivity.\n"
        "(b) says in words that no problem maps to this company.\n"
        "Starting with 'Low fit:' or 'Problem-led, no trigger:' is allowed.\n"
        "Fail if it names a problem with no cause, a cause with no problem, or a vague stand-in "
        "for a problem (such as 'the decision', 'the timing', or 'growth'). Also fail if it only "
        "restates the fit or the size: that is not the same as saying no problem maps.\n\n"
        "Because line:\n{output}\n\nAnswer pass or fail."
    ),
)

NO_COPY = DiscreteMetric(
    name="no_outreach_copy",
    allowed_values=["pass", "fail"],
    prompt=PREAMBLE + (
        "RULE: the brief never contains outreach copy.\n"
        "Fail if any part of the brief contains words written to be sent or said to the "
        "prospect: an email, a DM, a greeting, a subject line, a sign-off, a call script, or a "
        "ready-to-send opening line, quoted or not. Copy is addressed to the prospect: a "
        "sentence to them in the second person, or a request for their time. Suggesting a "
        "subject line or a script counts as copy even when it is framed as a tip to the rep.\n"
        "These are allowed and are not copy: the *Ask* line (one question for the rep to test, "
        "in quotes); a proof point in *Open with* stated as a fact about a customer and a "
        "result, even though the rep may repeat it; advice that tells the rep what to talk "
        "about.\n\n"
        "Brief:\n{output}\n\nAnswer pass or fail."
    ),
)

JUDGES = {m.name: m for m in (BECAUSE, NO_COPY)}

# Start every judge small. In the build this kit came from, the copy judge was the one that
# needed a larger model: the small one read the "Open with" label as an order to send.
JUDGE_MODELS = {
    "because_names_cause_and_problem": "claude-haiku-4-5-20251001",
    "no_outreach_copy": "claude-sonnet-5-5",
}


def view(name, text):
    """Show each judge only what its rule covers."""
    if name == "because_names_cause_and_problem":
        line = next((l for l in text.splitlines() if l.startswith("*Because*")), "")
        return line.replace("*Because*", "", 1).strip() or "(no Because line)"
    return text


def script_check(name, text):
    """What a regex would catch of the same rule. Shows what the judge adds."""
    if name == "no_outreach_copy":
        return bool(re.search(r"(?im)^(hi|hey|dear) |^subject:", text))
    if name == "because_names_cause_and_problem":
        line = next((l for l in text.splitlines() if l.startswith("*Because*")), "")
        return not re.search(r"likely owns|no problem .* maps", line)
    return False


# ---- planters: each breaks exactly one rule, so the right verdict is known ----

def _set(text, label, new):
    out, n = re.subn(r"(?m)^\*" + re.escape(label) + r"\*.*$", lambda _: new, text, count=1)
    return out if n else None


def _first(text):
    person = next(l for l in text.splitlines()[1:] if l.strip())
    return person.split(",")[0].split()[0]


def _company(text):
    return text.splitlines()[0].split(" · ", 1)[-1].rstrip("*")


def because_no_cause(text):
    return _set(text, "Because", f"*Because* {_first(text)} likely owns dispatch chaos right now.")


def because_vague_problem(text):
    return _set(text, "Because", f"*Because* {_company(text)} is growing fast, so {_first(text)} "
                                 "likely owns the decision right now.")


def because_restates_fit(text):  # held out: added after the first run
    return _set(text, "Because", f"*Because* Low fit: {_company(text)} sits outside our size range.")


def copy_open_with(text):
    return _set(text, "Open with", f"*Open with* \"{_first(text)}, saw the news about {_company(text)}. "
                                   "Shops your size lose hours a week to this. Worth 15 minutes Thursday?\"")


def copy_subject_line(text):
    return _set(text, "Check first", f"*Check first* Use subject line: {_company(text)} and your busy season")


def copy_spoken_script(text):  # held out: added after the first run
    return _set(text, "Open with", f"*Open with* Tell {_first(text)}: we help shops like yours stop "
                                   "losing billable hours, then ask for 15 minutes this week.")


PLANTS = {
    "because_names_cause_and_problem": [(because_no_cause, 2), (because_vague_problem, 2)],
    "no_outreach_copy": [(copy_open_with, 2), (copy_subject_line, 2)],
}
HOLDOUT = {
    "because_names_cause_and_problem": [(because_restates_fit, 2)],
    "no_outreach_copy": [(copy_spoken_script, 2)],
}
