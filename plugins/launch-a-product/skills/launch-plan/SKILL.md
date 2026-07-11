---
name: launch-plan
description: Build a tiered go-to-market launch plan for a product or feature: the audiences, the channels, the assets, the timeline, the owners, and the metrics that call it a win. Sizes the launch to what it deserves, so a small feature gets a small plan and a big bet gets the full push. Trigger on "plan a launch", "build a GTM launch plan", "we're shipping X, how do we launch it", "launch checklist", "go-to-market plan for this feature", or "what's the launch timeline".
---

# Launch Plan

## What this does
Turns "we are shipping something" into a plan someone can run. It sizes the launch to a tier, then fills in the audiences to reach, the channels to reach them, the assets each channel needs, a timeline with a real launch day, the owner for every piece, and the handful of metrics that decide whether it worked. No orphaned tasks, no launch day where the assets are not done.

## What you'll need
You do not need to connect anything to get value today. Describe what you are shipping and the skill runs now. Connect the tools and it grounds the plan in your real audiences and past launches.

- Works today with: what you are shipping, who it is for, why it matters, and the date you want to launch. Paste it and the skill returns the tiered plan now.
- More powerful connected to a CRM or a marketing tool: it sizes real audience segments and picks the channels that reached them last time.
- Sharper with a web-analytics tool: it sets baseline metrics from your real traffic, so the win condition is grounded, not guessed.
- Sharper with a content or social tool: it can slot the assets into a real publishing calendar instead of a static list.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on your description today and gets sharper as you connect tools. It never invents an audience size or a baseline it cannot see. An unknown number is labeled unknown, not fabricated.

- **Bring your data**: describe the launch and the target date. The skill returns the full tiered plan today. No connection required.
- **Connect your tools**: the same skill sizes real segments, picks proven channels, and sets baselines from past launches automatically.
- **Just exploring**: nothing to ship yet? Get the tiering rubric, the plan template, and a worked example, so you see the shape before you fill it.

Every run ends with the one thing that would sharpen the next launch, a segment source to connect or a metric baseline to set.

## Customize this for yourself
This was built for a B2B product team shipping features and products. Set these to your stack:

| Set this | What it is | Example |
|---|---|---|
| WHAT | the thing you are launching | a feature, a product, a rebrand |
| TIER | the size of the push | T1 major, T2 standard, T3 minor |
| AUDIENCES | who needs to hear it | existing users, prospects, press |
| CHANNELS | where you will reach them | email, blog, social, in-app, sales |
| CRM | your audience-data connector | a CRM, a marketing tool |
| ANALYTICS | your web-analytics connector | a web-analytics tool |
| LEAD_TIME | days from kickoff to launch | 14 (re-tune to the tier) |

Pick the tier honestly. A T3 feature dressed as a T1 launch burns the team and the audience's attention. The skill recommends a tier and tells you why.

## The method

### Tier the launch (T1 / T2 / T3)
First decision, everything follows from it. T1 is a major bet: full channel push, sales enablement, press. T2 is a standard feature: email, blog, social, in-app. T3 is a minor update: changelog and one in-app note. The skill recommends a tier from WHAT and lets you override.

### Audiences
Names who needs to hear it, in priority order: existing users who benefit today, prospects it unblocks, and internal teams (sales, support) who field the questions. Real segment sizes when a CRM is connected, named segments when not.

### Channels and assets
Maps each audience to the channels that reach them, and each channel to the exact asset it needs: the email, the blog post, the social thread, the in-app note, the sales one-pager. Every asset has a channel and every channel has an audience. Nothing floats.

### Timeline and owners
Back-plans from launch day across LEAD_TIME: asset drafts, reviews, a go or no-go, launch, and follow-up. Every item has a named owner. An unowned task is flagged before it becomes a launch-day surprise.

### Win metrics
Two or three metrics that decide success, matched to the tier and the goal: adoption of the feature, signups from the campaign, pipeline influenced. Baselines come from a connected analytics tool, or are labeled "set a baseline" when none is connected. A launch with no win condition is just noise.

## Quality gates
- Every asset has a channel, an owner, and a due date before launch day. No orphans.
- The tier is stated and justified. A T3 does not get a T1 budget.
- Win metrics are named up front, with a baseline or a clear "set a baseline" flag.
- Illustrative audience sizes and metric targets are marked as examples, never presented as your real data.

## Output (example)
```
LAUNCH PLAN · shipping: bulk-export feature · recommended tier: T2

Audiences (priority):
  1. Existing power users (benefit today)
  2. Prospects who asked for export
  3. Support + sales (will field questions)

Channels -> assets -> owner -> due:
  Email      release note to power users     PMM    L-2
  Blog       how-to with screenshots         PMM    L-3
  In-app     tooltip on the export button    PM     L-1
  Social     3-post thread                   PMM    L-day
  Sales      one-pager + talk track          PMM    L-2

Timeline (LEAD_TIME 14):
  L-14 kickoff  ->  L-5 drafts done  ->  L-2 review + go/no-go
  ->  L-day ship  ->  L+7 follow-up post

Win metrics (T2):
  - Feature adoption among power users (set a baseline)
  - Export-related tickets down (set a baseline)

Next: connect a CRM to size the power-user segment for real.
```

## Where the inputs come from
WHAT, the audiences, and the target date come from you. TIER is recommended by the skill and confirmed by you. LEAD_TIME (14) is a default, not a law, tune it to the tier. Segment sizes come from a connected CRM or marketing tool, and metric baselines from a connected web-analytics tool. The thresholds and the tier are yours to move.

## Make it yours
Fork it. Change the tiers, the channels, the lead time, the win metrics. The point is not to run a launch by the book. It is to ship the thing with the assets done, the owners named, and a clear read on whether it worked. Built by an operator. Customize it, break it, make it better.
