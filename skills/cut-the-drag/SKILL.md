---
name: cut-the-drag
description: Move 3 of the GTM Loop, the Cut half of Split. Take the non-selling drag off your reps so their time goes to selling. Not automation for its own sake: it is about protecting selling time and clearing the busywork between the steps. Fire on "what is pulling reps off selling", "take the busywork off", "free up my reps", "cut the drag", "what should come off their plate", or any move to protect rep selling time in a workflow.
---

# Cut the Drag: give reps their selling time back

## What this does
Takes the non-selling drag off the rep's plate so their time goes to actual selling. The drag is the execution between the steps: scoring, enrichment, pulling history, drafting the prep. On most teams reps grind that by hand and sell in whatever time is left. This move flips it: the drag runs before the rep starts, so they open the account ready to sell.

## What you'll need
One workflow, stacked with the right tech and signals (the output of Stack the Tech). No connectors required to plan it.

## The method
1. List the non-selling drag. Every repeatable execution task that is not selling: score the account, enrich it, pull the last touches, draft the brief. Be specific: "pull the last three touches and summarize" is drag, "run the sales conversation" is not.
2. Ask one question per task: does a rep have to do this to sell, or does it just have to be done before they sell? If it only has to be done, it is drag, and it should not cost a rep an hour.
3. Take the drag off the rep. The stacked workflow runs it, scoring, enrichment, history, first-draft prep, before the rep opens the account. Start with one, prove it, then the next.
4. Flag the not-yet. Where a task is not safe to run unattended, like auto-sending to a top account, say so and route it through a human check first.
5. Protect the selling time you freed. If the freed hours get eaten by new busywork, you cut the wrong thing. The measure is hours back to selling, not tasks automated.

## Failure points
- Automating for its own sake instead of asking what frees a rep to sell.
- Taking a task off the plate that carried context the rep needed to sell.
- Freeing hours that quietly refill with new drag.

## The receipt
[the non-selling drag you took off the reps, and the selling hours it gave back per week]

Example (illustrative):
- Cut: reps hand-building account research before every first call, now an auto-brief from CRM plus web, about 3 hrs/week back.
- Cut: copy-pasting call notes into the CRM, now auto-logged from the recording, about 2 hrs/week back.
- Kept with the rep: the discovery conversation and the qualification call.
Selling time returned: roughly a day a week per rep.

## Example chat
Here is the skill running on a real workflow, start to finish.

**You:** We built out the stacked workflow for outbound prospecting. What's still eating rep time that shouldn't be?

**Claude:** Walked the workflow step by step and asked the one question: does a rep have to do this to sell, or does it just have to be done before they sell?
```
Task                          Rep does it now    Verdict
Score + enrich the account    Yes, ~20 min       Drag. Move before rep opens it.
Pull last 3 touches           Yes, ~10 min       Drag. Move before rep opens it.
Draft the outreach angle      Yes, ~15 min       Drag. First-draft it, rep edits.
Run the actual call           Yes                Not drag. Keep with rep.
```
Three of four tasks are drag, and none of them require rep judgment, just execution before the rep opens the account. That is about 45 minutes back per account touched.

**You:** Good. What about auto-sending the outreach once it's drafted?

**Claude:** Flagging that one, not cutting it. Auto-send on a first-draft outreach to a net-new account is exactly the not-yet case: the message needs a human read before it goes out, at least until the draft quality is proven over a few weeks. Route it to a review queue instead of straight to send. One sharpener: connect the CRM so I can pull real hours-logged-per-task instead of estimates, so the receipt is measured, not guessed.

## Go further
The read is step one. Here is where an operator takes it once the manual version proves out.

- **Run the drag nightly, not on demand.** Point a scheduled Claude task at the CRM overnight so every account is scored, enriched, and pre-briefed before reps log in.
- **Watch for drag creeping back.** Have Slack ping the team lead whenever a quick manual task shows up three times in a week, before it hardens into new busywork.
- **Wire the not-yet queue to a human gate.** Send anything flagged for review, like the auto-send case, into a Slack approval thread so a person still owns the risky sends.

The cut is only real if the freed hours stay freed. That is the thing to watch.

## Next move
Hand the cleared workflow to Keep the Judgment. Built GTM. Approach, not receipts.
