# Book-of-Business Analyst

> Your portfolio analyst. Connect a CRM and a product-analytics tool, then turn any "what's the state of my book?" question into a portfolio rollup: per-account health composite, renewal pipeline at 90/120/180-day horizons, multi-product penetration view, expansion candidates, accounts going dark, and revenue-retention contribution per account. Use it for rollup views, not per-deal depth. Trigger on "how's my book?", "review my portfolio", "show me at-risk accounts", "expansion candidates in my book", "where am I leaking?", "who's gone dark?", "retention by account", "multi-product opportunities", or any portfolio rollup question.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/book-of-business-analyst && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/book-of-business-analyst/SKILL.md -o ~/.claude/skills/book-of-business-analyst/SKILL.md && echo "Installed book-of-business-analyst. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/book-of-business-analyst/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Book-of-Business Analyst

## What this does
This skill turns your customer book into one rollup view. It pulls every account you own, scores each on a health composite, lays out the renewals coming due, shows which products each account has adopted and which it has not, flags accounts going quiet, and ranks the best expansion plays. It is built for the start of the week, when you need to know where to spend your time. It is a rollup, not a per-deal deep dive.

## What you'll need
- A CRM that holds your accounts, owners, ARR or contract value, and renewal dates. The spine of the book.
- A product-analytics tool that reports per-account usage and active users. Powers the health composite and the going-dark detector.
- Optional: a sales-activity tool for an outreach overlay, and a support tool for a sentiment overlay.

No CRM connected? The skill says what to connect and stops. It does not guess.

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

## Make it yours
Map your CRM, your renewal field, your product lines, and your health inputs, and this becomes your book, not a template. Built by an operator. Customize it, break it, make it better.
