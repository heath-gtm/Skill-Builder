---
name: escalation-runbook
description: Turn a customer on fire into a runbook, not a scramble. Triage the severity, name the internal owners and the comms cadence, write the customer-facing message, and set the post-mortem that stops a repeat. Built for B2B customer success teams, customizable to your severity model and your org. Trigger on "customer escalation", "account is on fire", "how do I handle this escalation", "who owns this", "what do I tell the customer", or any escalation-response need.
---

# Escalation Runbook

## What this does
Takes a live customer escalation and turns panic into a sequence. It grades how bad this actually is, assigns the internal owners, sets how often everyone hears an update, drafts the message the customer receives, and schedules the post-mortem that prevents the same fire twice. A calm customer is not a lucky customer. It is a managed one.

## What you'll need
You do not need to connect anything to get value today. Bring the situation and the skill runs now. Connect the tools below and it pulls context automatically and adds signals you cannot paste by hand.

- Works today with: what is happening, in your words. What broke, since when, who is affected, what the customer has said, and how big the account is. Paste the thread or describe it.
- More powerful connected to a CRM: pulls the account value, the renewal date, and the owner, so the severity reflects the stakes.
- Sharper with a meeting or email tool: reads what was already promised and when the customer last heard from you.
- Sharper with a support or product tool: adds the ticket history and whether this issue is a repeat.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a fact it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: describe the escalation. What broke, who is hit, what was said. The skill runs the full triage today on your real situation. No connection required.
- **Connect your tools**: the same skill pulls account value, renewal date, and history automatically and adds signals you cannot paste by hand (ticket age, repeat pattern, last touch). Same output, less effort, sharper.
- **Just exploring**: no live fire? Get the framework, the severity model, and a worked example on a sample incident, so the runbook is ready before you need it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org with a tiered severity model. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | your CRM of choice |
| SEVERITY_MODEL | how you grade an incident | Sev1 / Sev2 / Sev3 |
| OWNERS | the roles that get pulled in | CSM, Support, Eng, Exec sponsor |
| CADENCE | how often you update per severity | Sev1 hourly, Sev2 daily, Sev3 on change |
| ACCOUNT_VALUE field | where the stakes live | ARR, renewal date, strategic flag |
| COMMS_CHANNEL | where updates go | the customer thread + an internal channel |
| POSTMORTEM_SLA | when the review must happen | within 5 business days of resolution |

Run any severity model you like. The skill grades impact against blast radius, so point it at your definitions, not anyone else's.

## The method

### Severity triage
Grade the escalation on two axes: how much is broken and how many it hits. A full outage on a top account is not the same as a cosmetic bug for one user. Assign a severity and state the reason in one line. The severity sets the cadence and the owners. Everything downstream follows from this call.

### Owners and RACI
Name the people, not the departments. Who drives the fix, who talks to the customer, who decides, who just needs to know. One accountable owner per escalation. A fire with two owners has none.

### Comms cadence
Set the heartbeat. How often the customer hears from you and how often the internal room syncs, both keyed to severity. Silence is what turns a bug into a churn risk. An update that says "still working it, next update at 3pm" beats a fix delivered in silence.

### Customer-facing message
Draft what the customer actually reads. Acknowledge, own it without over-promising, state what you know, state the next update time. No blame, no jargon, no false certainty. Give them the next checkpoint, not a guess at the finish.

### Post-mortem that prevents a repeat
Schedule the review before the fire is even out. Capture the root cause, the timeline, what the customer experienced, and the one change that stops a recurrence. An escalation you do not learn from is one you have agreed to have again.

## Quality gates
- No severity grade without the one-line reason behind it.
- Exactly one accountable owner. Named, not a team.
- The customer message states a specific next-update time, never "soon."
- Every resolved escalation has a scheduled post-mortem before it closes.
- No blame language in anything the customer sees.

## Output (example)
```
ESCALATION RUNBOOK
Severity: SEV1  (core workflow down, top-20 account, renewal in 60 days)

Owners
  Drive fix:      Eng on-call
  Customer comms: the CSM
  Decision:       Support lead
  Informed:       Exec sponsor

Cadence: customer update every hour, internal sync every 30 min

Customer message (draft):
  "We are aware the X workflow is failing for your team and we have
   engineers on it now. This is our top priority. Next update by 2:00pm
   your time, whether or not it is resolved by then."

Post-mortem: scheduled within 5 business days. Owner: the CSM.
Prevent-a-repeat: add a monitor on the workflow that failed silently.
```
(Details are illustrative.)

## Where the numbers come from
The cadences (hourly, daily) and the post-mortem SLA (5 days) are defaults, not laws. They suited a mid-market SaaS support model. If your customers expect tighter or looser contact, change them. The logic does not change. The thresholds are yours.

## Example chat
**You:** Acme's integration broke for their whole team an hour ago, they're furious in the shared Slack channel. What do I do?

**Claude:** Graded it SEV1: core workflow down, top-20 account, renewal in 60 days.
```
Owners
  Drive fix:      Eng on-call
  Customer comms: You (the CSM)
  Decision:       Support lead
  Informed:       Exec sponsor

Cadence: customer update every hour, internal sync every 30 min
```
Draft customer message is ready to send, and a post-mortem is scheduled for 5 business days out so this doesn't quietly repeat. The real risk here isn't the outage, it's the renewal clock running while the account is mad.
One sharpener: connect your CRM so the severity call pulls the actual ARR and renewal date instead of me asking you for them.

## Go further
The runbook works from what you paste in the moment. Here is the version that catches the fire before you open a laptop.

- **Auto-triage from the alert.** Wire a scheduled Claude task to a PagerDuty or Slack alert so severity, owners, and the first customer message draft exist before anyone joins the call.
- **Pull the stakes automatically.** Connect Salesforce so every escalation opens with real ARR and renewal date, not a guess at how much this account matters.
- **Close the loop in writing.** Have the post-mortem write itself into a shared doc tagged to the account, so the next escalation on the same account starts with the last one's lesson already loaded.

A fire you learn from is the only kind worth having.

## Make it yours
Fork it. Change the severity model, the roles, the cadence. The point is not to run someone else's playbook. It is to run yours, faster, when the account is on fire and there is no time to think. Built by an operator. Customize it, break it, make it better.
