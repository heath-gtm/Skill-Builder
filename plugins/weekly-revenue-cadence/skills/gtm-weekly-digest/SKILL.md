---
name: gtm-weekly-digest
description: One screen, whole funnel. A weekly GTM digest across marketing, pipeline, deals, and retention: the three numbers that matter, what changed since last week, and what needs attention now. Built for B2B revenue teams, customizable to your data and your stack. Trigger on "weekly digest", "GTM update", "what happened this week", "give me the one-screen summary", "Monday number", or any cross-funnel weekly recap.
---

# GTM Weekly Digest

## What this does
Pulls the whole go-to-market funnel onto one screen: what marketing generated, what pipeline did, how deals moved, and where retention stands. It surfaces the three numbers that matter this week, what changed since last week, and the handful of things that need attention, so a team starts the week aligned instead of digging.

## What you'll need
You do not need to connect anything to get value today. Bring your numbers and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a few numbers per stage of the funnel, this week and last, from wherever you track them. Paste them or upload a CSV.
- More powerful connected to a CRM: it reads pipeline, deals, and retention automatically.
- Sharper with a BI tool or a sheet: pulls the trend and the prior weeks without a copy-paste.
- Sharper with a marketing or product tool: adds top-of-funnel and usage signals cleanly.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your weekly numbers (a metrics sheet, a few exports). The skill writes the full digest today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the numbers automatically and adds signals you cannot paste by hand (live pipeline, week-over-week trend, usage). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org tracking a full funnel. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| FUNNEL stages | the stages you report | leads, pipeline, deals, retention |
| TOP THREE | the numbers that lead the digest | your three most-watched metrics |
| MARKETING source | where top-of-funnel lives | a marketing tool, a sheet |
| RETENTION source | where renewals and churn live | a CRM, a CS platform |
| CHANGE flag | week-over-week move worth naming | +/- 15% (re-tune) |
| ATTENTION rule | what earns an attention flag | off plan, slipping, or gone quiet |

Report on any funnel you like. The skill reads your stages and your top three against last week, so point it at your metrics, not anyone else's.

## The method

### The three numbers that matter
Pick the three that decide the week and put them first. Each with its value, its target, and the week-over-week move. If everything is a headline, nothing is. Three, chosen on purpose.

### Across the funnel
One line per stage: marketing generated, pipeline created and covered, deals moved, retention held. A digest is one screen. If it scrolls, it is a report, and it will not get read on a Monday.

### What changed
Week over week, not since the start of time. Name the moves that cross the change flag, up or down, and tie each to a cause you can see. A change with no cause is noise.

### What needs attention
The short list. Anything off plan, slipping, or going quiet, across any stage. Each item names the owner and the move. Attention without an owner is a shrug.

## Quality gates
- Exactly three headline numbers. A fourth headline means none of them is.
- The whole digest fits one screen. Length is a bug here, not thoroughness.
- Every change ties to a cause you can show, never an unsourced "up nicely."
- Attention items are owned. No owner, no action, no point.

## Output (example)
```
GTM WEEKLY DIGEST · Week of the 7th

The three
  New ARR      $110K wk  vs $125K plan   -12% wk/wk
  Pipeline     $210K created            +18% wk/wk
  Net retention 98%                      flat

Across the funnel
  Marketing    240 MQLs (+8%), 34 SQLs
  Pipeline     $210K created, 3.0x coverage
  Deals        4 advanced, 2 slipped, 1 closed
  Retention    1 renewal booked, 1 account gone quiet

Needs attention
  1. Sales: two deals slipped the week, ~$90K. Pull to a decision.
  2. CS: Delta Co dark 30d with a renewal in 75d. Re-engage.
```
(Figures illustrative.)

## Where the numbers come from
The change flag (+/- 15%) and the choice of three headline numbers are defaults, not laws. They suited a weekly SaaS cadence. If your week is noisier, widen the flag. If your funnel turns on different metrics, swap the three. The logic does not change. The thresholds are yours.

## Make it yours
Fork it. Change the three, the stages, the flags. The point is not to run someone else's digest. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
