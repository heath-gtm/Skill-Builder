# Pipeline Review Runbook

> Run a pipeline review that finds problems instead of reciting the pipeline. Checks coverage against target, ages every stage, tracks week-over-week movement, isolates the stuck deals, and hands you the exact question to ask on each one. Built for B2B sales managers, customizable to your CRM and stages. Trigger on "run my pipeline review", "do we have enough coverage", "what moved this week", "which deals are aging", "prep the pipeline meeting", or any pipeline health check.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/pipeline-review-runbook && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/pipeline-review-runbook/SKILL.md -o ~/.claude/skills/pipeline-review-runbook/SKILL.md && echo "Installed pipeline-review-runbook. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/pipeline-review-runbook/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Pipeline Review Runbook

## What this does
Turns your open pipeline into a review with an agenda. It measures coverage against the target, ages each deal in its current stage, shows what moved since last week and what did not, isolates the deals that are stuck, and gives you the specific question to ask on each one. You run the meeting off findings, not off a scroll through the CRM.

## What you'll need
You do not need to connect anything to get value today. Bring your pipeline and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a list of your open deals, with stage, amount, close date, stage-entry date, and last activity date, plus your period target. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads all of the above automatically and can compare to last week without you keeping a snapshot.
- Sharper with a meeting or email tool: confirms which stuck deals are actually cold versus quietly progressing.
- Sharper with a product-analytics tool: adds trial momentum on deals gated by a pilot.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your pipeline (a stage export, an open-deal CSV) and your target. The skill runs the full review today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and tracks week-over-week movement for you. Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the runbook, the exact fields it reads, and a worked example on sample pipeline, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline and a weekly team review. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| STAGE field | the opportunity stage | Opportunity.StageName |
| AMOUNT field | the number that rolls up | Opportunity.Amount, ARR |
| STAGE_ENTRY field | when the deal entered its stage | last stage-change date |
| ACTIVITY sources | where "last touch" lives | Account, Opportunity, Task, Event dates |
| TARGET | the period quota to cover | your team or rep target |
| COVERAGE_RATIO | pipeline-to-target you expect | 3x (re-tune to your win rate) |
| AGING_DAYS | days in stage that count as aged | per-stage, e.g. 21 (re-tune) |

Run any process you like. The skill checks movement and age against your stages, so point it at your fields, not anyone else's.

## The method

### Coverage vs target
Open pipeline for the period divided by the target, compared to your expected COVERAGE_RATIO. Shown as a ratio and as a gap in currency. If coverage is below the ratio, the review is a pipeline-generation conversation, not a deal-by-deal one. Say which it is up front.

### Stage aging
Every deal is aged against the day it entered its current stage, not the day it was created. Deals past the AGING_DAYS threshold for their stage are flagged. Aging is per-stage because a week in negotiation is not a week in discovery.

### Week-over-week movement
Three lists: what advanced a stage, what slipped or pushed a close date, and what did not move at all. The did-not-move list is the one most reviews skip and the one that predicts the miss.

### Stuck-deal isolation
A deal is stuck if it is past AGING_DAYS in stage with no forward step and no recent activity. These get pulled out of the roll-up and reviewed on their own, because averaging them into the total hides them.

### The question per deal
Each stuck or slipping deal gets one scripted question aimed at the reason it is stuck: no next step, single-thread, close date drift, or a stage it does not qualify for. The question makes the rep commit to a date or a decision.

## Quality gates
- Coverage is stated as a ratio and a currency gap, never a vibe.
- Aging is per-stage and measured from stage-entry, never from create date.
- The did-not-move list is always shown, even when it is uncomfortable.
- Every stuck deal carries one scripted question, not a general "let's discuss."

## Output (example)
```
PIPELINE REVIEW · period target $600K
Coverage: $1.42M open / $600K target = 2.4x (below 3x, short ~$360K)

Stage aging (flagged past threshold):
  Vertex     Negotiation   34 days   no next step
  Blend Labs Discovery     28 days   single-thread

Week-over-week:
  Advanced (2):  Acme -> Proposal, Cirrus -> Negotiation
  Slipped (1):   Northwind close pushed to next month
  Did not move (3): Vertex, Blend Labs, Delta

Ask on the stuck ones:
  1. Vertex. 34 days in negotiation. What single thing closes this, and when?
  2. Blend Labs. One contact for 4 weeks. Who else needs to be in the room?
  3. Coverage. Below 3x. Where do the next 5 deals come from?
```

## Where the numbers come from
COVERAGE_RATIO (3x), and the per-stage AGING_DAYS defaults are starting points, not laws. They suited a mid-market SaaS cycle with a healthy win rate. If your win rate is higher, a lower ratio covers you. If your stages run long, raise the aging thresholds. The runbook does not change. The thresholds are yours.

## Make it yours
Fork it. Change the ratio, the aging cutoffs, the questions. The point is not to run someone else's review. It is to run yours, faster, so the meeting ends with commitments instead of a recap. Built by an operator. Customize it, break it, make it better.
