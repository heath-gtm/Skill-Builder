---
name: book-of-business-analyst
description: Your portfolio analyst. Connect a CRM and a product-analytics tool, then turn any "what's the state of my book?" question into a portfolio rollup: per-account health composite, renewal pipeline at 90/120/180-day horizons, multi-product penetration view, expansion candidates, accounts going dark, and revenue-retention contribution per account. Use it for rollup views, not per-deal depth. Trigger on "how's my book?", "review my portfolio", "show me at-risk accounts", "expansion candidates in my book", "where am I leaking?", "who's gone dark?", "retention by account", "multi-product opportunities", or any portfolio rollup question.
---

# Book-of-Business Analyst

## What this does
This skill turns your customer book into one rollup view. It pulls every account you own, scores each on a health composite, lays out the renewals coming due, shows which products each account has adopted and which it has not, flags accounts going quiet, and ranks the best expansion plays. It is built for the start of the week, when you need to know where to spend your time. It is a rollup, not a per-deal deep dive.

## What you'll need
You do not need to connect anything to start. Bring your book and the skill runs today. Connect the tools below and it pulls the accounts automatically and adds usage signals you cannot paste by hand.

- Works today with: your account list with owner, ARR or contract value, and renewal date. Paste or upload a CSV.
- More powerful connected to a CRM: the whole book with owners, value, and renewal dates, live.
- More powerful connected to a product-analytics tool: per-account usage and active users, which power the health composite and the going-dark detector.
- Sharper with a sales-activity tool (outreach overlay) and a support tool (sentiment overlay).

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload what you have (a CSV or an export). The skill runs the full analysis today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and adds signals you cannot paste by hand (live activity, product usage, history). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.
## Customize this for yourself
| Set this | What it is | Default / Example |
|---|---|---|
| CRM | Where accounts, owners, and contract values live | Salesforce, HubSpot, or your CRM |
| Renewal date field | The field the renewal queue reads | A "renewal end date" field |
| Product lines | The set of products you check penetration against | Core, Add-on A, Add-on B, Add-on C |
| Health-score inputs | The signals that combine into the composite | Engagement tier, active users, champion stability, support sentiment |
| Dark-days threshold | Trailing window of no activity that flags an account | 30 days |

Map your portfolio first. Tell the skill which owner field equals "my book," which contract-value field is the source of truth for ARR, and what your product line names are. The method runs against those placeholders.

## The method
1. Pull the book. Every account where the owner field matches the portfolio owner, with contract value, renewal date, and product lines.
2. Score the health composite per account. Combine the inputs you mapped into one of four bands: HEALTHY, WATCH, AT-RISK, GHOST. Every band carries the reasons that produced it.
3. Build the renewal queue. Bucket open renewals into 90, 120, 180-day horizons, each with a verdict.
4. Build the multi-product penetration view. Per product line, count adopted vs total. The largest gap is the biggest opportunity.
5. Run the going-dark detector. Flag accounts past the dark-days threshold or with falling active users. Pair each with contract value and renewal date.
6. Compute retention contribution per account. Year-over-year value delta net of churn and downgrades, rolled to a portfolio figure.
7. Rank expansion candidates. Single-product accounts at an adoption ceiling carrying the signals to take the next product.
8. Close with named next moves tied to specific accounts.

## Quality gates
- The health composite is sourced. Never "Acme is at risk," always "at risk because engagement dormant, zero activity in 30 days, champion left in March."
- The renewal queue carries a risk overlay (HEALTHY / WATCH / SAVE_NEEDED).
- Book comparisons are honest. Surface book mix, not just headline numbers. One owner may hold the harder accounts.
- If a query needs a signal you have not mapped, the skill stops and says what to connect.

## Output (example)
```
PORTFOLIO ROLLUP  ·  47 accounts  ·  $4.2M ARR

Health composite:
  HEALTHY:  31 ($2.8M)   WATCH: 9 ($820K)
  AT-RISK:   5 ($412K)   GHOST: 2 ($168K)

Renewal pipeline:
  Next 90d:  6 renewals · $678K · 4 HEALTHY · 1 WATCH · 1 SAVE_NEEDED
  Next 120d: 11 renewals · $1.2M

Multi-product penetration:
  Core:     42 of 47 (89%)
  Add-on C:  8 of 47 (17%)  (34 expansion candidates, biggest gap)

Going-dark this week:
  - Account One   (-87% active users, $42K ARR, renewing 2026-08)

Retention contribution YTD: +$340K net · 108% net retention

Top expansion candidates:
  1. Account Four ($187K), Core only, ready for Add-on C
```

## Where the numbers come from
The defaults are illustrative. Re-tune to your book: the four health bands and their inputs, the 90/120/180-day renewal horizons, the 30-day dark threshold, the product lines and what counts as adopted, and the retention math (the year-over-year delta and what you net out). Match each to your own retention reality.

## Example chat
**You:** How's my book looking this week? Here's my account export. [pastes CSV]

**Claude:** Rolled it up.
```
PORTFOLIO ROLLUP  ·  47 accounts  ·  $4.2M ARR
Health composite:
  HEALTHY:  31 ($2.8M)   WATCH: 9 ($820K)
  AT-RISK:   5 ($412K)   GHOST: 2 ($168K)

Going-dark this week:
  - Account One   (-87% active users, $42K ARR, renewing 2026-08)

Top expansion candidates:
  1. Account Four ($187K), Core only, ready for Add-on C
```
The one to move on first: Account One isn't just AT-RISK, it's going dark with a renewal five months out, which is exactly the window where a save attempt still works. Wait until the renewal call and it's too late to matter.

**You:** What's dragging the AT-RISK bucket?

**Claude:** Every AT-RISK account in this run is flagged for a named reason (dormant engagement, zero activity in 30 days, or a departed champion), never just "at risk" with no evidence behind it. One sharpener: connect your product-analytics tool and the going-dark detector runs on real usage trend instead of the single snapshot you pasted.

## Go further
A weekly rollup by hand catches this week's fires. Here's the version that never lets one slip.

- **Run it every Monday automatically.** Connect Salesforce and your product-analytics tool to a scheduled Claude task that regenerates the rollup before your week starts, no manual export required.
- **Alert the moment an account goes dark.** Wire Amplitude usage drops into a Slack DM to the account owner the day the threshold trips, not the week you happen to run the report.
- **Push expansion candidates to the AE.** Feed the ranked list into Salesforce as a task or a Clay enrichment trigger so a single-product account at the adoption ceiling becomes a warm handoff, not a line item nobody actions.

The rollup is the read. The system is what makes sure nobody has to remember to ask for it.

## Make it yours
Map your CRM, your renewal field, your product lines, and your health inputs, and this becomes your book, not a template. Built by an operator. Customize it, break it, make it better.
