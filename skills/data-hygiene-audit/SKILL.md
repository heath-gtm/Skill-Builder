---
name: data-hygiene-audit
description: Turn a messy CRM export into a prioritized cleanup list. Finds the hygiene problems that quietly break reporting: missing fields, stale records, duplicates, bad stages, orphaned deals, and no-owner accounts. Built for B2B RevOps teams, customizable to your CRM and your data model. Trigger on "audit my CRM data", "why is my reporting off", "find the duplicates", "which records are stale", "clean up the pipeline", or any data-quality diagnostic.
---

# Data-Hygiene Audit

## What this does
Reads your CRM records and returns a straight verdict on the data that reporting depends on. It finds the records with missing required fields, the ones that have gone stale, the likely duplicates, the deals sitting in impossible stages, and the accounts and opportunities with no owner. Then it ranks the problems by how much they distort the numbers, so you fix the leaks that matter before the cosmetic ones.

## What you'll need
You do not need to connect anything to get value today. Bring an export and the skill runs now. Connect the tools below and it reads them automatically and checks records you would never paste by hand.

- Works today with: a CSV or paste of your accounts, contacts, and open deals, with owner, stage, close date, created date, last activity date, and the fields your reports rely on.
- More powerful connected to a CRM: it reads every object automatically, across the whole database, not just the rows you exported.
- Sharper with a data warehouse: it can compare CRM values against a source of truth and catch fields that silently drifted.
- Sharper with an activity or email tool: tightens the stale-record check with real last-touch dates.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a count it cannot see. A blank field is a finding, not a guess.

- **Bring your data**: paste or upload your export. The skill runs the full audit today on your real records. No connection required.
- **Connect your tools**: the same skill pulls the objects automatically and checks records you cannot paste by hand (every account, dedupe across the whole base, warehouse cross-checks). Same output, less effort, wider net.
- **Just exploring**: no data yet? Get the framework, the exact fields it checks, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline in a standard CRM. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | a CRM (Salesforce, HubSpot, Pipedrive) |
| WAREHOUSE | optional source of truth | a data warehouse (Snowflake, BigQuery) |
| REQUIRED fields | fields your reports cannot work without | owner, stage, close date, amount, segment |
| STAGE model | your legal stage list and order | your opportunity stages |
| STALE_DAYS | no-update days that mean stale | 90 for accounts, 30 for open deals |
| DEDUPE keys | what makes two records the same | email + domain, company name + domain |
| ROLL-UP grain | the level your reports summarize at | account, segment, owner |

Point it at your required fields and your stage model, not anyone else's. The audit is only as strict as the rules you give it.

## The method

### Missing-field scan
For every record, check the REQUIRED fields and report the fill rate field by field, named. A report that groups by segment is a lie if a third of accounts have no segment. Show the percentage empty and the raw count, not "some records are incomplete."

### Stale-record check
Flag any record whose last meaningful update is older than STALE_DAYS. Use last activity date where you have it, created or modified date where you do not, and say which one you used. An open deal with no touch in 30 days and a close date next week is the loudest kind of stale.

### Duplicate detection
Group records that match on the DEDUPE keys and surface the clusters, not just a count. Show which record looks like the survivor (most complete, most recent activity) so the merge decision is already half made.

### Bad-stage and orphan check
Flag deals in a stage that does not exist in your model, deals past their close date still marked open, and any account or opportunity with no owner. No-owner records are invisible to every rep-level report, so they distort every roll-up silently.

### Priority ranking
Rank findings by blast radius: a missing field on the grain your reports group by outranks a typo in a record no dashboard reads. The output is a cleanup list ordered by how much each fix straightens the numbers.

## Quality gates
- No "incomplete" without the named field and the exact fill rate.
- No duplicate flag without showing the cluster and the suggested survivor.
- Stale always states which date drove the flag, so nobody argues the definition.
- Counts are counts. The audit never estimates a number it can read directly.

## Output (example)
```
DATA-HYGIENE AUDIT · 4,120 accounts · 8,660 contacts · 310 open deals
Finding                     Scope        Severity   Detail
Segment field empty         38% of accts HIGH       1,566 accts drop out of segment reports
No-owner accounts           212 accts    HIGH       Invisible to every rep roll-up
Likely duplicate accounts   96 clusters  MED        Matched on domain, survivors flagged
Open deals past close date  41 deals     MED        Still open, close date in the past
Stale open deals            57 deals     MED        No activity in 30+ days

Cleanup order:
  1. Backfill segment on the 1,566 accounts. It breaks every segment report.
  2. Assign owners to the 212 orphan accounts before the next roll-up.
  3. Work the 96 duplicate clusters. Survivors already suggested.
```
Illustrative figures. Your run reports your real counts.

## Where the numbers come from
STALE_DAYS (90 for accounts, 30 for open deals) and the DEDUPE keys are defaults, not laws. They suited a mid-market SaaS base. If your sales cycle runs longer or your data model keys on something else, change them. The logic does not move. The thresholds and keys are yours.

## Example chat
Here is the skill running on a real export, start to finish.

**You:** Audit this CRM export, something's off with our segment reporting. [uploads CSV]

**Claude:** Ran the missing-field scan first, since that is usually the loudest problem.
```
Finding                     Scope        Severity   Detail
Segment field empty         38% of accts HIGH       1,566 accts drop out of segment reports
No-owner accounts           212 accts    HIGH       Invisible to every rep roll-up
```
The catch: your segment report is not wrong, it is just silently missing over a third of the base. That is why the numbers looked low.

**You:** What about duplicates? We merged two lists last quarter.

**Claude:** Found 96 likely clusters matched on domain, each with a suggested survivor (most complete, most recent activity), so the merge decision is already half made.
```
Cluster: "Acme Corp" x3 -> survivor: record with most fields filled, most recent activity
```
One sharpener: connect the CRM directly so I can check every account, not just the 4,120 in this export. Dedupe only catches what is in front of it.

## Go further
The read is step one. Here is where an operator takes it once the manual version proves out.

- **Run the audit weekly, automatically.** Point a scheduled Claude task at Salesforce every Monday and post the top 5 findings to the RevOps Slack channel.
- **Block bad data at the source.** Wire required-field validation into Salesforce so segment cannot go blank on a new account instead of catching it after the fact.
- **Cross-check against the warehouse.** Connect Snowflake as a source of truth so fields that silently drifted between systems get flagged, not just fields that are empty.

Catching it once is a cleanup. Catching it weekly is hygiene.

## Make it yours
Fork it. Change the required fields, the stale windows, the dedupe keys, the priority weighting. The point is not to run someone else's rulebook. It is to run yours, on your data, so the numbers your team trusts are actually true. Built by an operator. Customize it, break it, make it better.