---
name: stack-the-tech
description: Move 2 of the GTM Loop, Stack. Stack the right tech and signals to give one workflow the context it needs to run. Not a buy-or-build shopping trip: it is the tools that carry the data and the signals that tell the workflow what matters. Fire on "what does this workflow need", "what tech and signals", "stack the tech", "what tools for this workflow", "what data do we need here", or any move to assemble the stack for a GTM workflow.
---

# Stack the Tech: the right tech and the right signals

## What this does
Assembles the stack for one workflow: the tech that carries the data and the signals that give it context. The point is not to shop for tools or to rebuild infrastructure. It is to give this specific workflow the right inputs, so it runs on real context instead of a lone tool guessing.

## What you'll need
One workflow with its steps and its crux named (the output of Solve the Problem). No connectors required to plan the stack.

## The method
1. Walk the steps and name the context each one needs. For account prep: which account, what fit, what timing, what history. Context is the signal a step needs to do its job.
2. For each step, name the signal first, then the tech that carries it. Fit is a signal (your ICP model). Timing is a signal (intent, product usage). The CRM, the enrichment vendor, the dialer are tech that carry data. Signal first, tech second.
3. Buy the plumbing, build the thin edge. Buy the commodity tech you would be crazy to rebuild. Build only the small layer that is your advantage: the scoring logic, the rules, the view. Most of the edge is signal logic, not infrastructure.
4. Assemble the context, do not just connect tools. A stack of tools with no signals is plumbing with nothing flowing through it. The output of this move is the workflow running on the right signals.
5. Decide per workflow. The signals and tech that fit this workflow may be wrong for the next. The unit is the workflow, not the contract.

## Failure points
- Buying a platform and calling it context. A tool is not a signal.
- Wiring up tools with no signal flowing through them.
- Rebuilding infrastructure because building feels productive.

## The receipt
[the signals you stacked, the tech that carries them, and the context the workflow now runs on]

## Example chat

**You:** We picked "inbound leaks between marketing and sales" as the workflow. What does it actually need to run?

**Claude:** Let's walk the steps and name the signal each one needs before we touch any tools.
```
STEP            SIGNAL NEEDED         TECH THAT CARRIES IT
Lead qualifies  fit + timing          CRM (Salesforce) + enrichment (Clay)
Route to rep    territory match       CRM routing rules
Rep follow-up   intent + urgency      product usage (Amplitude), Slack alert
```
Signal first, tech second: most of these steps only need a rule layered on tools you already own, the routing logic is the one thing worth building. Key insight: a stack of connected tools with nothing flowing through them is plumbing, not context. One sharpener: name the one signal you do not have yet (timing) and go find where it already lives before buying anything new.

## Go further
The stack is planned. Here is where an operator takes it once the manual version proves out.

- **Wire the routing rule into the CRM.** Build the thin scoring layer as a Salesforce flow so fit and timing route the lead automatically, no rep has to notice it happened.
- **Surface the signal where the rep already lives.** Push the Amplitude intent spike into Slack as a DM the moment it crosses your threshold, instead of a dashboard nobody checks.
- **Enrich before it ever hits a human.** Run new leads through Clay on intake so fit and timing are already on the record when the rep opens it.

The stack is only as good as what is flowing through it, wire the signal, not just the tool.


## Next move
Hand the stacked workflow to Split: start with Cut the Drag, then Keep the Judgment. Built GTM. Approach, not receipts.
