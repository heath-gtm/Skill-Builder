# Forecast Call Prep

> Walk into the forecast call with a number you can defend. Sorts every deal into commit, best-case, or pipeline, flags the one risk that could sink each, and scripts the exact question to press each rep on. Built for B2B sales teams and managers, customizable to your CRM and forecast categories. Trigger on "prep my forecast call", "is this number real", "what do I ask each rep", "which commits are soft", "sandbag check", or any pre-forecast review.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/forecast-call-prep && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/forecast-call-prep/SKILL.md -o ~/.claude/skills/forecast-call-prep/SKILL.md && echo "Installed forecast-call-prep. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/forecast-call-prep/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Forecast Call Prep

## What this does
Takes your open deals and builds the forecast call for you, deal by deal. It sorts each one into commit, best-case, or pipeline based on what the evidence supports, not what the category says. It flags the single biggest risk on each deal. Then it hands you the exact question to ask the rep so the call moves the number instead of narrating it.

## What you'll need
You do not need to connect anything to get value today. Bring your deals and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a list of the deals in the forecast, with stage, amount, close date, forecast category, and last activity date. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads all of the above automatically, plus category history so it can see what moved.
- Sharper with a meeting or email tool: confirms the last real touch and who is actually engaged.
- Sharper with a product-analytics tool: adds trial usage momentum on deals that ride on a pilot.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your forecast list (a pipeline export, a category CSV). The skill runs the full prep today on your real deals. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and adds signals you cannot paste by hand (live activity, category movement, usage). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample deals, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline and a weekly forecast call. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| STAGE field | the opportunity stage | Opportunity.StageName |
| FORECAST field | commit / best-case / pipeline category | ForecastCategoryName |
| AMOUNT field | the number that rolls up | Opportunity.Amount, ARR |
| CLOSE field | the committed close date | Opportunity.CloseDate |
| ACTIVITY sources | where "last touch" lives | Account, Opportunity, Task, Event dates |
| PERIOD | the forecast window | this month, this quarter |
| THIN_DAYS | no-activity days that make a commit soft | 10 (re-tune to your cycle) |

Run any qualification method you like. The skill checks "does the evidence support the category this deal claims," so point it at your fields, not anyone else's.

## The method

### Category sort (three buckets, evidence-based)
Every deal lands in COMMIT, BEST_CASE, or PIPELINE based on what the evidence supports, then that is compared to the category the rep set.
- COMMIT: close date in the period, recent two-way activity, more than one contact engaged, next step set. A deal missing any of these is a soft commit and gets called out.
- BEST_CASE: real but not locked. A credible path to close in the period with at least one open risk.
- PIPELINE: possible, not this period. Named as upside, not counted on.
The gap between the evidence bucket and the rep's category is the whole point. A COMMIT the evidence rates BEST_CASE is where the number breaks.

### One risk per deal
Every deal gets exactly one flagged risk, the one most likely to sink it: single-thread, no next step, close date already slipped once, champion quiet, thin activity, or legal/procurement not started. One risk, named, so the call is about that risk and nothing else.

### The question to press
Each deal gets one scripted question for the rep, aimed at the flagged risk. Not "how's it going." Something like "who besides your champion has said yes, and when did they say it?" The question is designed to surface the truth, not confirm the hope.

### Soft-commit watch
Flag any COMMIT where the evidence is thin: no activity in THIN_DAYS, a single thread, a close date that already moved, or a next step that is blank. These are the deals that quietly miss. Surface them before the call, not after the quarter.

## Quality gates
- No deal called a soft commit without naming the specific thing that is missing.
- Every deal carries exactly one scripted question, tied to its one flagged risk.
- Close-date slips are shown with the prior date, never asserted.
- The number is presented three ways: rep-committed, evidence-supported, and the gap between them.

## Output (example)
```
FORECAST CALL PREP · 6 deals in the period
Account     Category   Evidence     Amount   Risk               Press the rep on
Acme Corp   Commit     Commit       $45K     Clean              Confirm signature date
Vertex      Commit     Best-case    $67K     Single-thread      Who else has said yes?
Blend Labs  Best-case  Best-case    $28K     No next step       What is the next date?
Northwind   Commit     Pipeline     $112K    Close slipped 2x   Why is this month real?

Number three ways:
  Rep-committed:      $224K
  Evidence-supported: $73K
  Gap to defend:      $151K (Vertex, Northwind)

Walk in with:
  1. Vertex. Get a second yes on record or move it to best-case.
  2. Northwind. Third slip. Make the rep prove the date or push it out.
```

## Where the numbers come from
THIN_DAYS (10) and the "more than one contact engaged" cutoff are defaults, not laws. They suited a mid-market SaaS cycle with a weekly call. If your deals run longer or your call is monthly, raise them. The buckets do not change. The thresholds are yours.

## Make it yours
Fork it. Change the buckets, the thresholds, the questions. The point is not to run someone else's forecast discipline. It is to run yours, faster, so the number you say out loud is the number you can defend. Built by an operator. Customize it, break it, make it better.
