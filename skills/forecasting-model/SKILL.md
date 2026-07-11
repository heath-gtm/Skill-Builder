---
name: forecasting-model
description: Build a forecast you can defend in the room. Category definitions that mean something, coverage math against quota, blended historical conversion, and a range instead of a single hero number. Built for B2B RevOps and sales leaders, customizable to your CRM and your forecast categories. Trigger on "build my forecast", "what are we going to close", "is my coverage enough", "what's commit vs best case", "give me a forecast range", or any forecast diagnostic.
---

# Forecasting Model

## What this does
Reads your open pipeline and builds a forecast that survives scrutiny. It pins what each category actually means, computes coverage against the number you have to hit, applies your own historical conversion instead of a hopeful guess, and reports a range with a low, likely, and high case rather than one number that is wrong to the dollar. The output tells you not just what you will close but how much to trust it.

## What you'll need
You do not need to connect anything to get value today. Bring your pipeline and the skill runs now. Connect the tools below and it reads history automatically and grounds the conversion rates in your real close data.

- Works today with: a paste or CSV of open deals with amount, stage, forecast category, close date, and owner, plus your quota or target for the period.
- More powerful connected to a CRM: it reads the live pipeline and category assignments automatically, across every rep.
- Sharper with a data warehouse: it pulls historical close rates by category and stage so the model runs on your numbers, not a benchmark.
- Sharper with a BI tool: pushes the range and coverage into a dashboard leadership can watch move.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a conversion rate it cannot ground. A thin history is a wider range, not a fake precision.

- **Bring your data**: paste or upload your open pipeline and your target. The skill runs the full forecast today on your real deals. No connection required.
- **Connect your tools**: the same skill pulls the pipeline and the close history automatically and grounds the model in your actual conversion (by category, by stage, by segment). Same output, less effort, defensible.
- **Just exploring**: no data yet? Get the framework, the category definitions, the coverage math, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a history to connect or a category to clean up.

## Customize this for yourself
This was built for a B2B SaaS org forecasting a quarter on a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | a CRM (Salesforce, HubSpot, Pipedrive) |
| WAREHOUSE | optional history source | a data warehouse (Snowflake, BigQuery) |
| CATEGORIES | your forecast categories | Commit, Best Case, Pipeline, Omitted |
| CATEGORY rules | what qualifies a deal for each | your entry criteria per category |
| TARGET | the number for the period | quota, per rep and rolled up |
| PERIOD | the forecast window | current quarter |
| HISTORY window | how far back conversion is drawn | trailing 4 quarters |

Pin your category rules first. A commit that means "rep feels good" and a commit that means "verbal yes, paper in legal" produce very different forecasts from the same pipeline.

## The method

### Category definitions
State what each category means as an entry rule, not a vibe. Commit is deals meeting the commit criteria. Best Case is upside that could close with things breaking right. Pipeline is everything else still live. Omitted is out. Every deal lands in exactly one, and the rule is printed.

### Coverage math
Divide open pipeline for the period by the target to get coverage. Report it overall and per rep. A team needing the number with 1.5x coverage is in a different reality than one with 4x, and the forecast should say which. State the coverage ratio, do not bury it.

### Historical conversion
Apply your own trailing close rate by category and stage, not a benchmark and not 100 percent of commit. If commit historically closes at 85 percent, the model says so. Where history is too thin to trust, widen the range instead of pretending precision.

### The range, not the number
Report three cases. Low is roughly commit at its historical rate. Likely blends commit and a slice of best case at their rates. High is commit plus best case landing well. A single number is a false promise. A range with its assumptions printed is a forecast.

### Gap to target
Set the range against the target and name the gap or the cushion. If the likely case lands short, say by how much and what category would have to overperform to close it. That is the sentence leadership actually needs.

## Quality gates
- Every category prints its entry rule. No undefined commit.
- Conversion rates are historical and sourced, never assumed at 100 percent.
- The forecast is always a range. Any single number is labeled as one case within it.
- Thin history widens the range. The model never fakes precision it has not earned.

## Output (example)
```
FORECAST · current quarter · target $2.40M · coverage 2.8x
Category     Open $      Hist. close   Weighted
Commit       $1.10M      85%           $0.94M
Best Case    $0.90M      42%           $0.38M
Pipeline     $1.80M      14%           $0.25M

Range for the quarter:
  Low     $0.98M   commit at rate, best case misses
  Likely  $1.55M   commit + partial best case at historical rates
  High     $2.05M   commit + best case land well

Gap: likely case is $0.85M short of target. Best Case would need to nearly double its close rate to close it.
```
Illustrative figures. Your run reports your real numbers.

## Where the numbers come from
The history window (trailing 4 quarters) and the blend that builds the likely case are defaults, not laws. They suited a mid-market SaaS quarter. If your cycle is longer or your volume thinner, widen the history and the range. The category rules and close rates are yours.

## Make it yours
Fork it. Change the categories, the entry rules, the history window, the way the range is blended. The point is not to run someone else's forecast. It is to run yours, grounded in your close history, defensible in the room. Built by an operator. Customize it, break it, make it better.