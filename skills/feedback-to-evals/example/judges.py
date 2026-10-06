"""What the sample feedback (feedback.md) turned into. Copy this file and make it yours.

The agent behind these outputs writes a call recap for an account executive. Two of its rules
need meaning, so each gets a judge. Two need only shape, so each gets a script check.

    no_overstated_commitment   line 3. New judge, from FB1.
    written_to_the_rep         line 4. Existed before the feedback. FB2 added a planter.
    owner_and_date (script)    line 2. From FB3.
    no_dashes (script)         line 5.

FB4 (a contract gap), FB5 (a preference), and FB6 (needs the transcript) have no gate here
on purpose. See feedback.md.
"""
import re

from ragas.metrics import DiscreteMetric

PREAMBLE = (
    "You are grading one rule of the contract for a call recap. After a customer call, an "
    "agent writes the recap for the account executive who ran the call. Judge only the rule "
    "below. Ignore length, formatting, style, and every other rule.\n\n"
)

COMMITMENT = DiscreteMetric(
    name="no_overstated_commitment",
    allowed_values=["pass", "fail"],
    prompt=PREAMBLE + (
        "RULE (line 3): never state a commitment the customer did not make. A maybe stays a maybe.\n"
        "Work in two steps.\n"
        "1. Find every statement that the customer agreed, approved, confirmed, chose, signed, "
        "or will do something.\n"
        "2. For each, check the customer's own words in the recap (the quotes under 'What they "
        "said'). Fail if the recap states a firmer commitment than the quotes support: a "
        "'consider' or 'take it to my boss' written as 'agreed', a budget, a decision, or a date "
        "nobody stated, or a plan written as already done.\n"
        "Pass if every commitment matches what the customer said. A customer who really did "
        "commit ('the budget is approved, I sign') is a pass. A next step the rep owns is not a "
        "customer commitment.\n\n"
        "Recap:\n{output}\n\nAnswer pass or fail."
    ),
)

TO_THE_REP = DiscreteMetric(
    name="written_to_the_rep",
    allowed_values=["pass", "fail"],
    prompt=PREAMBLE + (
        "RULE (line 4): the recap is written to the rep. Nothing in it is addressed to the customer.\n"
        "Fail if any part of the recap is written to be sent to the customer: a greeting, a "
        "sign-off, a sentence to them in the second person, or a ready to send email or message, "
        "quoted or not.\n"
        "These are allowed: the customer's own words quoted under 'What they said'; next steps "
        "that tell the rep what to send, without writing the message.\n\n"
        "Recap:\n{output}\n\nAnswer pass or fail."
    ),
)

JUDGES = {m.name: m for m in (COMMITMENT, TO_THE_REP)}

# Start every judge on Claude Haiku 4.5. Move one only when a rerun shows it failing.
JUDGE_MODELS = {name: "claude-haiku-4-5-20251001" for name in JUDGES}


def script_check(name, text):
    """What a regex would catch of the same rule. Shows what each judge adds."""
    if name == "no_overstated_commitment":
        return bool(re.search(r"\b(agreed|signed|confirmed)\b", text))
    if name == "written_to_the_rep":
        return bool(re.search(r"(?im)^(hi|hey|dear) |^best,", text))
    return False


# ---- script checks (run_checks.py runs these for free) ----

def owner_and_date(text):
    """Line 2: every next step names an owner and a due date. Returns a reason if it fails."""
    steps = re.search(r"(?ms)^## Next steps\n(.*?)(?=^## )", text)
    for line in (steps.group(1) if steps else "").splitlines():
        if line.startswith("- ") and not re.match(r"- Owner: \S.* · Due: \d{4}-\d{2}-\d{2} · ", line):
            return f"next step without an owner and a date: {line[:80]}"
    return None


def no_dashes(text):
    """Line 5: no em dashes or en dashes."""
    return "has an em or en dash" if re.search("[\u2014\u2013]", text) else None


CHECKS = {"owner_and_date": owner_and_date, "no_dashes": no_dashes}


# ---- planters: each one reproduces a piece of feedback on a clean output ----

def _first(text):
    return re.search(r"With: (\w+)", text).group(1)


def _company(text):
    return text.splitlines()[0].replace("# Call recap: ", "")


def _sub(text, pattern, new):
    out = re.sub(pattern, new, text, count=1, flags=re.M)
    return out if out != text else None


def maybe_to_yes(text):  # FB1
    return _sub(text, r"^(## Decisions\n)", f"\\1- {_first(text)} agreed to the three-year term.\n")


def invented_budget(text):  # FB1, a second style of the same mistake
    if "budget is approved" in text:
        return None  # this customer really did say it, so the edit would not be a mistake
    return _sub(text, r"^(## Summary\n.*?)$", f"\\1 {_first(text)} confirmed the budget is approved for this quarter.")


def done_not_planned(text):  # held out: a plan written as already done
    if "budget is approved" in text:
        return None
    return _sub(text, r"^(## Decisions\n)", f"\\1- {_company(text)} has chosen us and starts in November.\n")


def next_steps_as_email(text):  # FB2
    return _sub(text, r"^(## Next steps\n)",
                f"\\1Send this today:\n\"Hi {_first(text)}, great talking with you. I'll send pricing by Friday. "
                "Does Tuesday work for a follow up? Best, Casey\"\n\n")


def greeting_in_summary(text):  # held out: addressed to the customer in the summary
    return _sub(text, r"^(## Summary\n)", f"\\1Thanks for your time today, {_first(text)}. ")


def drop_owner(text):  # FB3
    return _sub(text, r"^- Owner: [^·]+· (Due: [^·]+· )", "- \\1")


def vague_due_date(text):  # held out: an owner with no real date
    return _sub(text, r"^(- Owner: [^·]+· )Due: \d{4}-\d{2}-\d{2}", "\\1Due: soon")


def dash_in_summary(text):
    return _sub(text, r"^(## Summary\n.*?)\. ", "\\1 \u2014 ")


def en_dash_in_header(text):  # held out: an en dash, not an em dash
    return _sub(text, r" · Rep:", " \u2013 Rep:")


PLANTS = {
    "no_overstated_commitment": [(maybe_to_yes, 2), (invented_budget, 2)],
    "written_to_the_rep": [(next_steps_as_email, 2)],
}
HOLDOUT = {
    "no_overstated_commitment": [(done_not_planned, 2)],
    "written_to_the_rep": [(greeting_in_summary, 2)],
}
CHECK_PLANTS = {
    "owner_and_date": [(drop_owner, 2)],
    "no_dashes": [(dash_in_summary, 2)],
}
CHECK_HOLDOUT = {
    "owner_and_date": [(vague_due_date, 2)],
    "no_dashes": [(en_dash_in_header, 2)],
}
