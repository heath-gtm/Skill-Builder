---
name: feedback-to-evals
description: Turn real feedback on your agent, prompt, or skill into test cases, so your eval set grows from the misses users actually hit instead of the ones you imagined. Each thumbs down, rejected proposal, or reviewer note gets sorted into a broken rule, a gap in your written rules, or a preference. A broken rule gets a scripted edit that reproduces the same mistake on outputs you trust, plus a script check or a Claude judge that has to catch every copy before it joins your gate. Starter kit and a fictional sample included. Trigger on "turn this feedback into evals", "add this miss to my eval set", "my users keep thumbs-downing the same thing", "make sure this never happens again", "grow my eval set from real feedback", "what do I test after a bad review", "turn complaints into test cases", or any time a piece of feedback should become a check.
---

# Feedback to Evals: every real miss becomes a test

## What this does
Your eval set was written before anyone used the agent. Your users have been writing the real one since.

Every thumbs down with a reason is a test case someone handed you for free. Most teams fix the prompt, maybe rerun that one input, and move on. The next version breaks the same way on a different input and nobody notices until another thumbs down.

This skill takes each piece of feedback and asks three questions before it builds anything:
1. **Which rule did it break?** Map it to a line in your written rules. If no line covers it, that is a gap in the rules, and the skill drafts the missing line for a person to approve. It never adds one quietly.
2. **How do I make many of these?** A planter: a small scripted edit that puts the same kind of mistake into outputs you already trust. One complaint becomes ten or twenty cases.
3. **What catches it?** A script check if a regex can settle it. A Claude judge if it needs meaning. An existing judge if one already covers the rule.

Then the proof: the check has to catch every planted copy and pass every clean output before it counts toward your gate.

**Taste is not a rule.** "I'd prefer paragraphs" gets logged, not gated. A gate built on one person's taste blocks good outputs forever.

## Where this came from
Built in October 2026 on the real feedback log of a research agent that had been live for a few weeks: thumbs down from the people using it, notes from a reviewer, and changes its owner approved, then later reverted. The agent writes a brief a person reads before making a call.

The log was more useful than the eval set written before launch, and it taught the method:
- **The fixes went into the prompt and stopped there.** Several rules that came out of feedback lived in the system prompt and the skills, but never made it back into the written contract. Classing each item against the contract is what surfaced the drift.
- **Some feedback was later overruled.** A reviewer flagged a missing check, it became a rule, and the owner removed it a few versions later. Built as a gate, it would have failed outputs the owner wanted. Feedback that the owner overrules is a preference.
- **The saved outputs were older than the rules.** The "clean" outputs were saved before some rules existed, so they failed checks written from later feedback. Those flags were real misses in stale outputs, not broken checks.
- **The planters were wrong more often than the judges.** When a judge missed a plant, the plant was usually the problem: an edit that left an attribution in place, or landed in a line that already said the right thing. Read one plant of each style before you pay for a run.
- **Feedback without the output is half a test case.** The live runs saved the verdict and the comment, not the output. Those items could only be reproduced from their description, and some could not be tested at all.

What is still unsolved: a judge sees the output, not what the agent should have found. Feedback like "it named the wrong decision maker" needs the transcript or source passed in next to the output. That part is not in this kit yet.

## Try it in 60 seconds
A fictional sample ships with this skill: four call recaps, six pieces of feedback on them in `example/feedback.md`, and the judges and checks that feedback turned into.

1. Copy the `scripts/` and `example/` folders from this skill somewhere you can run Python 3.10 or newer.
2. Install and set your key:
   ```
   python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
   export ANTHROPIC_API_KEY=...
   ```
3. Read `example/feedback.md` first. It is the ledger: each piece of feedback, its class, and what it turned into.
4. Test the script checks (free), then build the test set and run the judges:
   ```
   .venv/bin/python scripts/run_checks.py --judges example/judges.py --clean example/outputs --out feedback-run
   .venv/bin/python scripts/build_set.py --judges example/judges.py --clean example/outputs --out feedback-run
   .venv/bin/python scripts/run_judges.py --judges example/judges.py --out feedback-run
   ```
5. Open `feedback-run/checks-report.md` and `feedback-run/results/<time>/report.md`. Read the tables, then every disagreement under them.

The sample is about 40 judge calls and costs a few cents.

**Your first exercise is already in the report.** On the run before this was published, the commitment judge failed the Oakmoor recap, the one clean recap where the customer really did commit ("The budget is approved. Anything under it, I sign."). The rubric names that exact near miss as a pass, and the judge still read it as conditional. Decide who is right. If the judge is wrong, try narrowing what it sees or moving it up a model, and rerun. If the recap overstated it, fix the recap. That loop is the whole skill in miniature.

## What you'll need
- **Works today with**: a pile of real feedback (thumbs down with reasons, review notes, rejected changes), the outputs that feedback was about if you saved them, and 10 or more outputs you trust.
- **Written rules**: a contract, a system prompt, or a list. Feedback is classed against them. If you have none, run `agent-contract` first.
- **An Anthropic API key and Python**: the judges are Claude models called through Ragas and the Anthropic SDK. Script checks need neither.
- **Better with agent-judge**: it covers how to write and trust-test a judge in depth. This skill decides which feedback deserves one.

## How this runs at your connection level
The skill never depends on a connector. It runs on feedback and outputs you paste or point it at.

- **Bring your data**: a feedback export (a spreadsheet, a Slack thread, a review doc) and a folder of outputs. You get a classified ledger, drafted rules, planters, checks, and a trust report.
- **Connect your tools**: if thumbs up and down already land in a database or a channel, point the skill there and run it on every new batch. Save the output next to each piece of feedback; that one habit makes every later step possible.
- **Just exploring**: run the sample, then change one piece of feedback in the ledger and follow it through to a check.

Every run ends with three lists: what joined the gate, the rule drafts waiting on a person, and the feedback that could not be tested and what is missing to test it.

## Customize this for yourself

| Set this | What it is | Default / Example |
|---|---|---|
| FEEDBACK_SOURCE | where feedback comes from | thumbs down with a reason, review notes, rejected or reverted changes |
| CONTRACT | the written rules feedback is classed against | your contract, else the system prompt |
| CLEAN_SET | outputs that passed a review | 10 or more, from the current version |
| STYLES | planter styles per piece of feedback | 2 to 3 from the feedback's own wording |
| HOLDOUT | new styles added after the first run, never used to tune | 2 per rule |
| JUDGE_MODEL | the model each judge runs on | start on Claude Haiku 4.5, move up only when a rerun shows it |
| REPEATS | runs per judgment | 2 to tune, 5 for a gate |
| GATE_BAR | what a check must clear to join the gate | every plant caught on a zero tolerance rule, 90% or more otherwise, false alarms under 5% |
| PREFERENCE_BAR | when a logged preference becomes a contract question | the same preference from 3 different people |
| RULE_OWNER | who approves drafted rules | the agent's owner. never the skill |

**RULE_OWNER does not move.** A drafted rule is a proposal. Until a person approves it, nothing is gated on it.

## The method

### Step 1: Collect feedback with its output
Pull every piece of feedback with the output it was about, the version that produced it, and who said it. Feedback with no saved output can still be classed, but it can only be reproduced from its description. Note which items are missing their output.

### Step 2: Class every item
One row per item in a ledger (`example/feedback.md` shows the format).

| Class | Test | Becomes |
|---|---|---|
| Rule broken | a written rule already says the output was wrong | a planter, plus a script check or a judge |
| Gap | no written rule covers it, or it lives in the prompt but not the contract | a drafted rule for RULE_OWNER. no gate until approved |
| Preference | taste, a one-off, or something the owner later overruled | a line in the ledger. never a gate |

Two traps. Feedback that the agent followed a bad rule is a gap, not a broken rule: the fix is the rule. And a reviewer's note is not automatically a rule: check whether the owner kept it.

### Step 3: Script or judge
If a regex can settle it (a missing field, a word cap, a banned character, a number next to a word), it goes to a script check. Free, exact, and it runs first. If it needs meaning (was this commitment real, is this addressed to the customer), it goes to a judge. If a judge already covers the rule, the feedback becomes a new planter style for that judge, not a new judge.

### Step 4: Write the planters
A planter takes one clean output and returns it with the same mistake the feedback named, or nothing if it cannot apply. Write 2 to 3 styles from the feedback's own wording. Make the planter refuse outputs where the edit would be true: planting "confirmed the budget" on a recap where the customer really did confirm it is not a mistake.

Read one plant of each style before the first paid run. Planters are code, and code has bugs.

### Step 5: Prove it
Run the clean outputs and the plants, twice. Then add held-out styles the rubric never saw and run again. Read every disagreement. There are four kinds:
- **The judge or check is wrong.** Fix the rubric, the view, or the regex, and rerun.
- **The clean output really breaks the rule.** Often because the output is older than the rule. Count it as a catch.
- **The rule is vague.** RULE_OWNER decides, the rule is rewritten, the judge follows.
- **The plant is wrong.** Fix the planter.

### Step 6: Join the gate, keep the ledger
A check joins the gate once it clears GATE_BAR. Its row in the ledger names the feedback it came from, so anyone can trace a gate back to the person who asked for it. Each new batch of feedback starts at Step 1, and the set grows. It never restarts.

## Quality gates
- Every piece of feedback has a ledger row with a class.
- No drafted rule is gated until a person approves it.
- No preference became a gate.
- Every rule broken maps to a named rule.
- Nothing a regex can check went to a judge.
- Every planter was read on at least one output before a paid run.
- Every check was run on clean, planted, and held-out cases before it joined the gate.
- Held-out styles were added after the first run and never used to tune.
- Every disagreement was read and sorted into one of the four kinds.
- The report names what could not be tested and what is missing.
- No em dashes anywhere.

## Output (example)
From the fictional sample in this skill, run before publishing.

```
FEEDBACK LEDGER                         6 items: 4 rule broken, 1 gap, 1 preference

FB1  "says she agreed to the three year term"   rule broken, line 3   new judge
FB2  "next steps are a ready to send email"     rule broken, line 4   existing judge, new planter
FB3  "next step has nobody on it"               rule broken, line 2   script check
FB4  "missed the six week legal review"         gap                   rule drafted, waiting
FB5  "too many bullets"                         preference            logged
FB6  "named the wrong decision maker"           rule broken, line 3   needs the transcript. open

SCRIPT CHECKS                       free
check            false alarms   planted    held out
owner_and_date   0 of 4         2 of 2     2 of 2
no_dashes        0 of 4         2 of 2     2 of 2

JUDGES                              2 repeats, 36 judge calls, about 5 cents, Claude Haiku 4.5
judge                      false alarms   planted   held out   regex caught   consistency
no_overstated_commitment   1 of 4         4 of 4    2 of 2     5 of 6         1.00
written_to_the_rep         0 of 4         2 of 2    2 of 2     0 of 4         1.00

DISAGREEMENTS, for a person to read
  no_overstated_commitment, clean oakmoor-property: judge fail.
    the customer said "the budget is approved, I sign". the rubric lists this as a pass.
    open: judge too strict, or recap too firm? decide before this judge joins the gate.

GATE
  joins now: owner_and_date, no_dashes, written_to_the_rep (with the new FB2 planter)
  waiting: no_overstated_commitment (one false alarm to settle)
  waiting on a person: the FB4 rule draft
  not testable yet: FB6, until the transcript is passed in next to the recap
```

The regex column flatters the regex. It matches "agreed", "confirmed", or "signed" anywhere, so it would also fire on two of the clean recaps: one says "No pricing was agreed", and Oakmoor's customer really did confirm. One of its 5 catches is that same "agreed" in a sentence about nothing being agreed. The held out style, a plan written as already done, uses none of those words. That is the case the judge is for.

## Example chat

**You:** Our recap agent got five thumbs down this week. Can you make sure these don't come back?

**Claude:** Paste the five with their reasons, the recaps they were about, and the agent's rules.

**You:** Here they are.

**Claude:** Two break rules you already have: one recap says the customer agreed to a term she only said she'd consider, and one has a next step with no owner. One is a gap: "it missed that legal review takes six weeks" breaks nothing you've written down, so I drafted a rule for you to approve. One is taste ("too many bullets"), logged. The fifth needs the transcript to judge, so I can't test it from the recap alone.

**You:** What do the two rule breaks become?

**Claude:** The missing owner is a regex, so a free script check. The overstated commitment needs meaning, so a judge. I wrote two ways to plant each mistake into recaps you already trust. The judge caught every plant and passed every clean recap, so it can join the gate. Approve or reword the legal review rule and I'll build its planter next.

## Go further
- **Run it on every batch.** Weekly feedback, weekly ledger rows. The gate grows with the agent.
- **Save the output with the feedback.** If your thumbs down button stores only the reason, change it to store the output too.
- **Pair it with a coach.** If something proposes fixes from feedback, every approved fix should arrive with its planter and check, and every rejected one should land in the ledger as a preference so it is not proposed again.
- **Pass the source in.** For feedback about what the agent should have found, give the judge the transcript or pages next to the output.

## Make it yours
Point it at your own feedback, set your bars, and name the person who approves new rules. Keep the order: class it, then script or judge, then plant, then prove. Built by an operator. Customize it, break it, make it better.
