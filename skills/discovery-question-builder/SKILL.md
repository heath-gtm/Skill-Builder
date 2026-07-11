---
name: discovery-question-builder
description: Turn a persona and a problem into a discovery plan that actually qualifies. Tailored questions sequenced from problem to impact to next step, mapped to MEDDPICC, MEDDIC, BANT, or your own framework. Built for B2B AEs and SDRs, customizable to your persona, framework, and CRM. Trigger on "build discovery questions", "MEDDIC questions for this persona", "what should I ask on this call", "qualify this deal", or any first-call prep.
---

# Discovery-Question-Builder

## What this does
Takes a persona and the problem you think they have, and returns a sequenced set of discovery questions that move from surfacing the problem, to sizing its impact, to agreeing a next step. Each question is mapped to the qualification field it fills, so a good call also fills your framework instead of leaving you to backfill it later.

## What you'll need
You do not need to connect anything to get value today. Give the skill a persona and a problem and it runs now. Connect the tools below and it grounds the questions in the real account and writes back the answers.

- Works today with: a persona, the problem hypothesis, and the framework you qualify against. Paste it and go.
- More powerful connected to a CRM: it reads the open opportunity and the qualification fields already filled, so it only asks what is still missing.
- Sharper with a meeting or call tool: it can pull prior-call notes so you do not re-ask what you already learned.
- Sharper with an enrichment tool: pulls the role and context so the questions land in the prospect's world, not a generic one.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on what you give it today and gets sharper as you connect tools. It never assumes an answer the prospect has not given. An unknown is a question to ask, not a field to guess.

- **Bring your data**: name the persona, the problem, and the framework. The skill builds the sequenced question set now.
- **Connect your tools**: the same skill reads the open deal and the fields already filled, so it targets the gaps and can write the answers back after the call.
- **Just exploring**: no deal yet? Get the sequence, the field map, and a worked example on a sample persona, so you see the shape before the call.

Every run ends with the one thing that would make the next call sharper, a field to map or a tool to connect.

## Customize this for yourself
This was built for B2B AEs running staged discovery. Set these to your motion:

| Set this | What it is | Default / Example |
|---|---|---|
| PERSONA | who is on the call | economic buyer, champion, end user |
| PROBLEM | the hypothesis you are testing | stated as a business pain |
| FRAMEWORK | how you qualify | MEDDPICC, MEDDIC, BANT, your own |
| DEPTH | how many questions per stage | 2 to 3 (re-tune to call length) |
| NEXT_STEP | the exit you want to earn | a scoped next meeting or action |
| CRM | your CRM connector | a CRM you already run |
| QUALIFICATION fields | your framework's fields in the CRM | the fields you actually track |

Qualify with any framework you like. The skill maps its questions to your fields, not anyone else's letters.

## The method

### Problem to impact to next step
Questions run in three passes. First surface and confirm the problem in the prospect's words. Then quantify what it costs them, in time, money, or risk. Then agree the next step. Impact questions before you have confirmed a problem land flat; this order keeps them earned.

### Map every question to a field
Each question is tagged with the framework field it fills, Metrics, Economic Buyer, Decision Criteria, Pain, and so on for your framework. A discovery call is not done because time ran out; it is done when the fields that gate the next stage are filled.

### Layered, not interrogation
Questions layer: an open question, then a follow-up that goes one level deeper on the answer. The plan gives you the follow-up so you are not caught flat when they say "it's a problem." No rapid-fire checklist feel.

### Impact quantification
At least one question forces a number or a consequence, "what does that cost you a quarter," "what happens if this is still true next year." A pain with no size does not survive a deal review. Any example figure is illustrative, drawn from the prospect, never asserted by you.

### Earn the next step
The plan ends by scripting the transition to the next step, tied to what they just told you, so the ask feels like their logic, not your quota.

## Quality gates
- Every question maps to a named framework field. No orphan questions.
- Impact questions come after a confirmed problem, never before.
- At least one question forces a quantified consequence.
- The next-step ask references the prospect's own stated pain, not a generic close.

## Output (example)
```
DISCOVERY PLAN · economic buyer · framework: MEDDPICC

Pass 1 - Problem (fills: Pain, Metrics)
  Q: How is [process] handled today, start to finish?
    follow-up: Where does it break most often?
  Q: What made this worth looking at now?

Pass 2 - Impact (fills: Metrics, Economic Buyer)
  Q: When it breaks, what does that cost, roughly, per quarter?
  Q: Who else feels that cost? Who signs off on fixing it?

Pass 3 - Next step (fills: Decision Process, Champion)
  Q: If we showed this solved, what is your process to move on it?
  Ask: "Based on the [cost] you mentioned, worth a working session
  with [role] next week to map it?"
```

## Where the inputs come from
PERSONA, PROBLEM, and FRAMEWORK are yours to set; the three-pass order and the 2-to-3-per-stage depth are defaults that suited a 30-minute first call, not laws. A longer discovery can go deeper per pass. The order holds. The inputs are yours.

## Make it yours
Fork it. Change the persona, the framework, the depth, the next step you aim for. The point is not to run someone else's qualification. It is to run yours, and fill it while you talk. Built by an operator. Customize it, break it, make it better.
