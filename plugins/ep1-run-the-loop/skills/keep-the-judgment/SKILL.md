---
name: keep-the-judgment
description: Hand a redesigned GTM workflow to a named owner with the four threads that keep it running: context, tooling, ownership, and rhythm. The keep move of the GTM Loop's Split, so the workflow does not fall apart in a month. For any operator rolling out a workflow change. Fire on "how do I roll this out", "who owns this", "enable my team", "make this stick", "keep the judgment", or the last step of any GTM workflow redesign.
---

# Keep the Judgment: leave the calls to the people

## What this does
Hands the redesigned workflow to a human who owns it, with the four threads that keep it from falling apart. Cutting the drag is not the finish line. A workflow with no owner and no rhythm tears again in a month.

## What you'll need
One workflow that has been solved, stacked, and had its drag cut. No connectors required.

## The method
1. Name the human judgment. The calls in this workflow that need context, judgment, or the relationship. That is what the person keeps.
2. Thread 1, context. Write the shared brain for this one workflow: the ICP, the rules, the definitions, the messaging. The human and the AI pull from the same source, or the AI guesses confidently.
3. Thread 2, tooling. Stand up the one automation that runs the drag. One workflow, not the whole stack.
4. Thread 3, ownership. Put one name on the workflow. They own the human judgment and the system's output. No orphan workflows.
5. Thread 4, rhythm. Set the recurring review where the owner checks the output and fixes drift. On the calendar, weekly or biweekly. A standing review, not a Slack channel.

## Failure points
- Cutting the drag and walking away. No owner means it tears again.
- Keeping the judgment with a doc nobody keeps current. Context rots.
- Reviewing in a Slack thread instead of a standing meeting. Drift wins.

## The receipt
[one owner, one context doc, one running automation, one recurring review, on one workflow]

## Example chat
Here is the skill running on a real handoff, start to finish.

**You:** We just cut the drag on our lead-routing workflow. How do I make sure it doesn't fall apart in a month?

**Claude:** Here's the handoff, the four threads named.
```
Context doc:  routing-rules.md (ICP, SLA timers, fallback logic)
Tooling:      one automation, the round-robin assignment
Owner:        RevOps lead, named, not "the team"
Rhythm:       biweekly review, calendar hold, not a Slack channel
```
The failure mode this catches: you were about to keep the judgment in a Slack thread, which is exactly how drift wins. A standing review is the difference between an owner and an orphan. One sharpener: name the actual person for the rhythm review right now, before this doc goes stale waiting on a decision nobody's made.

## Go further
The handoff is step one. Here is where an operator takes it once the manual version proves out.

- **Put the rhythm on the calendar for real.** Use a scheduled Claude task to generate the biweekly review agenda from the last two weeks of routing exceptions, so the owner walks in with the drift already surfaced.
- **Catch context rot automatically.** Flag the context doc in Slack if it hasn't been touched in 60 days, so nobody's running rules that quietly went stale.
- **Track ownership across every workflow you've cut.** Log each workflow's owner and last-review date in a Notion or Airtable table, so "no orphan workflows" is a fact you can check, not a hope.

You handed off the judgment once, now the system checks that it's still being kept.


## Next move
Repeat the loop on the next most expensive workflow. Built GTM. Receipts only.
