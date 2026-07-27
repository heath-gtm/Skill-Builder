---
name: pipeline-report
description: Build the pipeline report a review actually needs: coverage vs target, creation vs goal, movement since last time, aging, and the deals that need a decision this week. Built for B2B revenue teams, customizable to your CRM and your sales process. Trigger on "pipeline report", "do we have enough pipeline", "coverage check", "what's aging", "prep for the pipeline review", or any pipeline diagnostic.
---

# Pipeline Report

## What this does
Reads your open pipeline and answers the four questions a review asks: do we have enough coverage, are we creating enough, is it moving, and which deals need a decision now. It ends with a short list of deals to act on, not a wall of rows.

## What you'll need
You do not need to connect anything to get value today. Bring your pipeline and the skill runs now. Connect the tools below and it pulls it automatically and adds signals you cannot paste by hand.

- Works today with: a list of open deals, with stage, amount, close date, created date, and last activity date. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads the whole pipeline automatically, plus history for creation and movement.
- Sharper with a BI tool or a sheet: pulls the target and the coverage ratio without a copy-paste.
- Sharper with a meeting or email tool: tightens the aging and gone-quiet checks.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your pipeline (a deal export, a stage CSV). The skill runs the full analysis today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the pipeline automatically and adds signals you cannot paste by hand (creation history, stage movement, live activity). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| STAGE field | the opportunity stage | Opportunity.StageName |
| TARGET source | the number pipeline must cover | quota, plan, a BI tool |
| COVERAGE ratio | healthy pipeline-to-target multiple | 3x (re-tune to your win rate) |
| CREATION goal | new pipeline you need per period | your per-period target |
| AGING basis | days in stage that mean aging | 30 (re-tune) |
| DECISION window | close date that means act now | this week / this period |

Run any process you like. The skill reads coverage, creation, movement, and aging against your own targets, so point it at your numbers, not anyone else's.

## The method

### Coverage vs target
Open pipeline in the period divided by the target it must cover. State the ratio and whether it clears your bar. Below coverage is the first thing a review needs to know, so it leads.

### Creation vs goal
New pipeline created this period against what you needed to create. Coverage can look fine while creation quietly dries up. This is the leading indicator, so it gets its own line.

### Movement
What changed since last time: deals that advanced, deals that slipped a stage, deals that pushed their close date. Movement is the difference between a live pipeline and a parked one.

### Aging
Deals sitting in one stage past the aging basis. An old deal is not a bad deal, but an old deal nobody has touched is. Show days in stage and days dark side by side.

### Deals that need a decision
The short list. Deals inside the decision window, deals that are stuck, deals that are aging and quiet. Each one gets a next move, not just a flag.

## Quality gates
- Coverage is always shown as a ratio against a named target, never a raw dollar total alone.
- Creation is measured against a goal, not reported as a number floating on its own.
- "Aging" cites days in stage. A deal is not old because it feels old.
- The decision list is short and every entry has a move.

## Output (example)
```
PIPELINE REPORT · This period
Coverage      $1.8M open vs $600K target  ·  3.0x, at bar
Creation      $210K created vs $250K goal  ·  84%, behind
Movement      4 advanced, 2 slipped a stage, 3 pushed close date
Aging         5 deals over 30 days in stage, 2 of them dark 14+ days

Decide this week
  1. Vertex ($67K, close Thu): champion quiet 12 days. Re-engage or slip it.
  2. Blend Labs ($28K, in stage 34d): no next step. Set one or disqualify.
  3. Northwind ($112K, dark 21d): last outreach or mark it lost.
```
(Figures illustrative.)

## Where the numbers come from
The coverage ratio (3x), the aging basis (30 days), and the creation goal are defaults, not laws. They suited a mid-market SaaS cycle with a roughly one-in-three win rate. If yours differs, re-tune the multiple to your close rate. The logic does not change. The thresholds are yours.

## Example chat

**You:** Build the pipeline report for this week's review. Target's $600K. [pastes deal export]

**Claude:** Here's the read, four questions in order.
```
Coverage      $1.8M open vs $600K target  ·  3.0x, at bar
Creation      $210K created vs $250K goal  ·  84%, behind
Movement      4 advanced, 2 slipped a stage, 3 pushed close date
Aging         5 deals over 30 days in stage, 2 of them dark 14+ days
```
Coverage looks fine at 3.0x, but creation is quietly behind at 84%. That's the leading indicator, and it's the one a coverage number alone would hide until next quarter.

**You:** Give me the short list to actually act on.

**Claude:**
```
1. Vertex ($67K, close Thu): champion quiet 12 days. Re-engage or slip it.
2. Northwind ($112K, dark 21d): last outreach or mark it lost.
```
Every entry gets a move, not just a flag. Sharpener: connect a meeting or email tool so "champion quiet 12 days" comes from real activity data instead of the last-activity field you pasted in, which tends to lag.

## Go further
The weekly pull proves the four questions are the right ones. Here's the version that's ready before the review starts.

- **Generate it the morning of the review.** A scheduled Claude task pulls the CRM Monday at 6am and has the report waiting before the meeting, no manual export.
- **Catch the aging deals as they cross the line.** Connect Slack so a deal crossing 30 days in stage posts to the owner the day it happens, instead of surfacing a week later in the report.
- **Tighten the dark-deal read.** Connect a meeting or email tool so "champion quiet" reflects real last-touch data across email and calls, not just the CRM activity field.

Four questions, asked the same way every week, is what makes the review fast.

## Make it yours
Fork it. Change the ratio, the aging window, the fields. The point is not to run someone else's report. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
