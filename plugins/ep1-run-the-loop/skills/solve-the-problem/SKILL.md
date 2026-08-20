---
name: solve-the-problem
description: Move 1 of the GTM Loop, Solve. Pick the GTM workflow that costs you the most and frame the problem as a workflow, not a role. Stops you from solving a stretched team by adding headcount. Fire on "what should I fix first", "where is my GTM leaking", "do I need a GTM Engineer", "which workflow to redesign", "name the problem", or the start of any GTM redesign.
---

# Solve the Problem: build the workflow, not the org chart

## What this does
Finds the one workflow worth fixing first and writes the problem as a workflow instead of a headcount. The reflex when a GTM team is stretched is to add a role. That names a hire, not a problem. This move points you at the work.

## What you'll need
A list of where work moves between your GTM functions. No connectors. You can do this from memory or a whiteboard: the handoffs and shared jobs across marketing, sales, CS, and RevOps.

## The method
1. List the crossings, not the org chart. Walk the revenue lifecycle end to end and write down every place work passes between functions or is shared by more than one. Those are your workflows.
2. Find the leaks two fast ways. Follow the spreadsheets: every recurring manual export, copy-paste, or cleanup job is a workflow with no system. Follow the "whoever has five minutes" work: anything that falls to whoever is free is unowned by definition.
3. Size each in cost, not annoyance. Hours per week, pipeline leaked, or churn. Rank them.
4. Pick the single most expensive one. That is the only workflow worth a project this quarter.
5. Write the problem as a workflow sentence. "Inbound leaks between marketing and sales" is a workflow. "We need a GTM Engineer" is a headcount. If your sentence names a person, rewrite it until it names the work.

## Failure points
- Naming a role instead of a problem. A job req is not a fix.
- Ranking by what is loudest instead of what is most expensive.
- Trying to fix the whole funnel at once and learning nothing.

## The receipt
[the one workflow you picked, and what it costs you per week today]

## Example chat

**You:** We're stretched thin across GTM. Feels like we need a GTM Engineer. Where should we actually start?

**Claude:** Let's walk the crossings before we name a hire.
```
CROSSING                          COST
Inbound lead -> sales handoff     ~6 hrs/week, hand-copied into CRM
Trial signup -> CS onboarding     ~4 hrs/week, no owner, whoever's free
Renewal data -> forecast roll-up  ~3 hrs/week, spreadsheet export
```
Inbound handoff is the most expensive and the most exposed, it is blocking pipeline, not just annoying someone. The workflow sentence: "Inbound leaks between marketing and sales." Not "we need a GTM Engineer." Key insight: naming a role is not naming a problem, it just moves the problem onto someone's job description. One sharpener: bring actual logged hours next time instead of estimates, so the ranking is real cost, not gut feel.

## Go further
Naming the workflow is step one. Here is where an operator takes it once the pick is made.

- **Track the crossings automatically.** Wire a scheduled Claude task to pull weekly time-in-stage from Salesforce and flag which handoff is slipping, so the ranking updates itself instead of a quarterly guess.
- **Catch the leak the day it happens.** Have Slack ping the workflow owner the moment a lead sits unrouted past your SLA, instead of finding it in next month's audit.
- **Feed the pick straight into the next move.** Hand the ranked workflow to a scheduled task that drafts the signal list automatically, so Solve and Stack the Tech run back to back without re-typing the brief.

Name the workflow once, and the system keeps pointing you at the next one.


## Next move
Hand the workflow to Stack the Tech. Built GTM. Approach, not receipts.
