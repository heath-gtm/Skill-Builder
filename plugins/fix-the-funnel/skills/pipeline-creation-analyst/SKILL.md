---
name: pipeline-creation-analyst
description: Your top-of-funnel coverage analyst. Connect a CRM and a product-analytics tool, then turn any "do I have enough at-bats?" question into a pipeline-coverage diagnosis: per-channel coverage math, account engagement velocity per rep, a hot-account ranking, a daily prioritized work plan, and under-prospected segment surfacing. Trigger on "do I have enough pipeline?", "pipeline coverage by channel", "who should we go after this week?", "run the daily drop", "top accounts to engage", "where are we under-prospected?", "hot accounts this week", "rep-by-rep coverage check", "pipeline gap analysis", or any account-level coverage question.
---

# Pipeline-Creation Analyst

## What this does
This skill answers the top-of-funnel coverage question: do you have enough at-bats to hit next quarter's number, and where are the gaps? It reads your CRM and a product-analytics tool, runs forward-looking coverage math per channel and per rep, ranks the hottest accounts to work, builds a daily prioritized account drop with a named owner per account, and surfaces the segments you are under-prospecting. It is built for the person who runs the pipeline review, not the person who works a single lead.

## What you'll need
- A CRM. The system of record for accounts, owners, channel attribution, and forecasted value.
- A product-analytics tool. The source of product-usage and active-user signal. Optional, but it powers the product channel and the new-user signal.
- An account-fit score (optional overlay). Any model that ranks accounts by ICP fit.
- A hiring-intent or firmographic-signal source (optional). Powers the "why now" line.

No CRM connected? The skill says what to connect and stops. It does not guess.

## Customize this for yourself
| Set this | What it is | Default / Example |
|---|---|---|
| CRM connector | System of record for accounts, owners, pipeline | A CRM |
| Product-analytics connector | Source of product usage and active-user counts | A product-analytics tool |
| Channel field | The account field that classifies channel | A "channel source" field; never the opportunity-level channel field |
| Fit-score field | Account-level ICP fit score | An "account fit score" field, 0-100 |
| Forecast / target field | Account-level forecasted value used in coverage math | A "forecasted value" field |
| Channels | Your acquisition channels | Inbound, Outbound, Product |
| Coverage targets | Per-channel pipeline target for the period | Set from your quota plan |
| Activity sources | The signals that count as "engaged" | Calls, emails, tasks, product events, weighted by recency |
| Daily drop size | Accounts surfaced per day | 10 |

To use your own channels, replace the channel list with whatever your business runs. To use your own targets, set a per-channel pipeline number and the coverage math re-bases against it.

## The method
1. Classify every account by channel. Read the channel field and group accounts into your channels.
2. Run forward-looking coverage math per channel. Project the pipeline needed to hit the period target using win rate and cycle time, then compare projected against needed. Output a covered-percentage and a health flag (healthy, under, over) per channel.
3. Score account engagement velocity per rep. Count accounts engaged in a trailing window using your activity sources, weighted by recency, against book size.
4. Rank hot accounts. A composite of recent signal, account-fit score, and product engagement.
5. Detect the new-user signal. Flag accounts showing fresh active users as a distinct work item.
6. Surface under-prospected segments. Cross fit score against coverage. Name the gap as segment plus channel, with target and current percentages.
7. Build the daily drop. Top N prioritized accounts, each with a recommended owner and a one-line "why now."
8. Compute the coverage gap. Target, current projection, dollar gap, and the math to close it. End with the single point of leverage.

## Quality gates
- Coverage math is forward-looking. It projects pipeline needed for the next period, not just open opps.
- The daily drop names a recommended owner, with the account fact that justifies the routing.
- Under-prospected surfacing is segment plus channel, with target and current percentages.
- Fail loud on missing fields. Never invent a field name or definition.

## Output (example)
```
TEAM PIPELINE COVERAGE  ·  Period target: 1.8M new revenue

Per-channel coverage:
  INBOUND:    890K projected vs 900K needed · 99% covered · HEALTHY
  OUTBOUND:   310K projected vs 720K needed · 43% covered · UNDER
  PRODUCT:    202K projected vs 180K needed · 112% covered · OVER

THE DAILY DROP, Monday
  1. Account One   Recent funding + sales hiring spike   Owner: Rep A   Fit 87
  2. Account Two   Cost-consolidation trigger            Owner: Rep C   Fit 73
  3. Trial Account 3 active users, 1 power user          Owner: Rep B   Fit 68

Under-prospected segments:
  - Mid-market, Outbound: 22% of target, 8% current coverage
  - Existing accounts with new-user signups in last 30d: 12 ignored

Coverage gap math:
  Needs 1.8M. Current projection 1.4M (gap 400K).
  To close: 18 more opps at avg 22K + 60% win rate = 30 more meetings.
  Leverage point: Rep C plus the outbound segment.
```

## Where the numbers come from
The coverage targets, win rate, cycle time, average deal size, and the daily-drop size are defaults. Re-tune them to your plan. The thresholds that drive healthy, under, over are defaults too. Set them where your team draws the line. The activity-source weighting is a starting point; adjust which signals count and how recency decays.

## Make it yours
Map your connectors and fields, set your channels and targets, and this becomes your coverage companion. Built by an operator. Customize it, break it, make it better.
