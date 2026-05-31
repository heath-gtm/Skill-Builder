---
name: book-of-business-analyst
description: Your portfolio analyst. Connect Salesforce + Amplitude — turns any "what's the state of my book?" question into a CSM portfolio rollup: per-account health composite, renewal pipeline 90/120/180-day visibility, multi-product penetration heatmap, expansion candidates, accounts going dark, NRR contribution per account. The CSM's Monday morning agent. Different from Renewal-Health (per-deal depth) — this is rollup view. Trigger on "how's my book?", "review my portfolio", "what's the state of {CSM}'s book?", "show me at-risk accounts", "expansion candidates in my book", "where am I leaking?", "who's gone dark?", "NRR by account", "multi-product opportunities", or any portfolio rollup question. Also fire when a CS Leader asks to review a CSM's whole book or compare CSMs.
---

# Book-of-Business Analyst — your portfolio companion

**Required:** Salesforce + Amplitude. **Optional:** Mixmax (activity overlay), Intercom (support sentiment overlay).

## What this analyst answers

- "How's my book this week?" — portfolio rollup with health composite per account
- "What renewals are coming in the next 90/120/180 days?" — renewal queue visibility
- "Who's at risk?" — accounts trending red across health composite
- "Who's going dark?" — accounts with declining activity + adoption
- "Expansion candidates in my book?" — multi-product penetration gaps surfaced
- "Compare CSMs" — book-by-book comparison for CS Leader

## What it owns internally

- **Per-account health composite**: PES tier × activity (4-source) × champion stability × support sentiment
- **Renewal queue rollup** at 90 / 120 / 180-day horizons
- **Multi-product penetration heatmap** (which accounts have Sequences but not Meeting Copilot, etc.)
- **Going-dark detector**: trailing-30-day activity decline + WAU/DAU drop
- **NRR contribution math per account** (year-over-year value delta)
- **Expansion candidate ranking** (single-product accounts with adoption ceilings hit)

## Quality gates

**Health composite is sourced.** Never "Acme is at risk." Always "Acme is at risk because: PES Dormant, activity 0 in 30d, champion left in March."

**Renewal queue includes risk overlay.** Every renewal in the queue gets a brief verdict (HEALTHY / WATCH / SAVE_NEEDED) so the CSM knows where to invest time.

**Compare-CSMs honest.** When CS Leader asks "compare HM vs Diana," the analyst surfaces book mix (not just headline numbers) — HM might have harder accounts.

## Output format example

```
📊 HM'S BOOK · 47 accounts · $4.2M ARR · 28% of company

Health composite distribution:
  HEALTHY:      31 accounts ($2.8M ARR)
  WATCH:         9 accounts ($820K ARR)
  AT-RISK:       5 accounts ($412K ARR)  ← needs save-play
  GHOST:         2 accounts ($168K ARR)  ← run verify-or-churn protocol

Renewal pipeline:
  Q3 (90d):     6 renewals · $678K · 4 HEALTHY · 1 WATCH · 1 SAVE_NEEDED
  Q4 (120d):   11 renewals · $1.2M · 8 HEALTHY · 2 WATCH · 1 SAVE_NEEDED
  Q1'27 (180d): 9 renewals · $890K · all WATCH or later

Multi-product penetration heatmap:
  Sequences:           42 of 47 (89%)
  Meeting Copilot:     23 of 47 (49%) ← 19 expansion candidates
  Smart Send AI:       18 of 47 (38%) ← 24 expansion candidates
  Calendar Enhancements: 8 of 47 (17%) ← 34 expansion candidates ★

Going-dark this week (trailing 30d activity decline):
  • Blend Labs (-87% WAU, $42K ARR, renewing 2026-08)
  • Whip Around (-71% WAU, $28K ARR, renewing 2026-09)
  • Halborn (-54% WAU, $67K ARR, renewing 2026-11)

NRR contribution YTD: +$340K (net of churn) · 108% NRR

Top expansion candidates (single-product → multi-product play):
  1. Acme Corp ($187K) — Sequences only, ready for Calendar
  2. Vortex.io ($112K) — Sequences + Meeting Copilot, ready for Smart Send
  3. PGA ($89K) — Sequences only, has all signals for Calendar

Next moves (named):
  1. Blend Labs — schedule activity check + run save play before week ends
  2. Acme Corp — book Calendar Enhancement demo before Q3 renewal
  3. HM 1:1 with Diana to compare WAU recovery tactics
```

## Used by

- **CS-leader-weekly-report** workflow (CSM book health dashboard)
- **CSM-book-of-business** workflow (full portfolio runbook)
- **Daily-Sales-Assistant** workflow (CSM mode)
- Standalone for Monday-morning book review

## When NOT to use

- For per-renewal depth (use Renewal-Health Analyst)
- For specific at-risk save plays (use customer-battle-plan skill)
- For new-business pipeline (use Pipeline-Creation Analyst)

## Inheritance from LOCKED_DESIGN.md

Lock-ins #14 v7 (play types — RENEWAL_DEFENCE + EXPANSION), #16 v9.1 (4-source activity), #28 (Deal Health Summary), product-engagement-story skill.

## Make.com / API packaging

**Input:** `{ csm_email: string, mode: "rollup | renewal_queue | at_risk | expansion_candidates | compare", compare_with: string | null }`

**Output:** `{ health_distribution, renewal_queue, multi_product_heatmap, going_dark, nrr_ytd, expansion_candidates, next_moves }`

**Failure modes:** No Amplitude → composite is SFDC-only (lower confidence). No Intercom → support sentiment omitted.

## Shippable as

Standalone connector-gated SKU. Make.com node. The CSM's Monday morning companion.
