---
name: rep-operating-standards
description: Canonical Mixmax rep operating standards (Heath-set 2026-06-07) — the constants every rep-target, capacity, meeting-goal, pipeline-blend, or quota-math model MUST start from. $50K/mo quota = NEW BUSINESS ONLY (expansion = overattainment); Inbound 2.0 meetings/SQO is a SET STANDARD (era actuals 5.2–7.0 — always label); target SQO blend 45/40/15 (IB/P/OB, product triple-down); 60/25/15 is TIME management, never pipeline blend; rep ritual = 1 sourced meeting/day. Includes the quota→wins→SQOs→meetings math chain (8.8/wk → 7.3/wk), the meetings ladder, the capacity model + hiring trigger (>6 IB mtgs/wk sustained), and agent instructions. Trigger on: rep targets, rep quota, meetings per week, meetings target, capacity model, hiring trigger, pipeline coverage, channel blend, 60/25/15, SQO blend, quota math, rep scorecard, "how many meetings", "what should a rep book", or any per-rep performance modeling.
---

# Rep Operating Standards — Canonical (Heath-set 2026-06-07)

**Status:** canonical. Any agent, skill, or report modeling rep targets, meetings, capacity, pipeline blend, or quota math MUST start from these constants. Synced to `heath-gtm/Skill-Builder/rep-operating-standards/SKILL.md`.
**Evidence base:** Pipeline Diagnosis rev 2.7 (`analysis/pipeline-diagnosis-2026-06-05.html`, QA badge 85 claims / 0 open flags) and the Rep Scorecard (`analysis/rep-scorecard-2026-06-08.html`).

---

## 1. The standards

1. **Quota: $50K/rep/month on NEW BUSINESS ONLY** (new logo + SS→DS conversions, `Opportunity_Source__c` channel, NB + Conversion record types). Expansion is overattainment — never in the quota base.
2. **Inbound = 2.0 meetings/SQO — a SET STANDARD, not a trailing actual** (era actuals ran 5.2–7.0). Meeting #1 is the SQL event; verdict in ≤2 meetings. Never present 2.0 as historical fact; label it "standard."
3. **Target SQO blend = Inbound 45 / Product 40 / Outbound 15.** Product is the triple-down channel: 47.2% SQO→win, most productive meetings (2.5× inbound), under-engaged PQA supply.
4. **60/25/15 is TIME (60% customers + active deals · 25% building pipeline · 15% admin) — never a pipeline blend.** Do not conflate.
5. **The rep ritual: source 1 meeting/day** (~5.1/wk product + outbound). Inbound is demand — gated, not chased.

## 2. The math chain (per rep · per month, $50K)

| Step | Current win rates | IB at 41% era best |
|---|---|---|
| Wins (ASP $11.0K / $5.2K / $10.8K) | 6.3 (2.3 IB · 3.3 P · 0.6 OB) | 6.0 (2.7 · 2.8 · 0.5) |
| SQOs = wins ÷ SQO→win (29.3 / 47.2 / 24.2%) | 17.7 (8.0 · 7.1 · 2.7) | 14.7 (6.6 · 5.9 · 2.2) |
| Meetings = SQOs × mtgs/SQO (2.0 / 2.4 / 2.0†) | ~38/mo | ~32/mo |
| **Booked per week** | **8.8** | **7.3** |
| SQO pipeline created | ~$154K/mo ≈ 3.1× coverage | ~$127K ≈ 2.5× |

† Outbound 2.0 mtgs/SQO is a planning assumption (window n = 12 SQOs / 7 wins; method range 1.9–5.4). Product 2.4 and all win rates / ASPs are Jan'25→May'26 window actuals.

## 3. The meetings ladder (same $50K)

Today's funnel (IB 5.2–7.0): 15–18/wk (calendar breaks) → **2.0 standard: 8.8** → +IB 41% SQO→win: 7.3 → +10% deal size: 6.6 → +10% win rate everywhere: **6.0**.

## 4. Capacity model + hiring trigger

Optimal week: ~3.7 inbound (demand) + ~5.1 sourced (1/day) + 2–3 customer ≈ 12 held ≈ 18h inside the 60% block.
**Neglect mechanism:** every inbound meeting above ~4/wk displaces a sourced meeting or eats the 25% block (2025 precedent: product wins 26→11 while inbound surged).
**Hiring trigger:** rep sustained >~6 inbound meetings/wk for a month, or team meeting blend >65% inbound → capacity is the constraint; rebalance routing or hire. Check: team inbound meeting demand ÷ ~4 per rep = required headcount.

## 5. Agent instructions (for any analyst/skill build)

1. Load these constants before modeling rep targets, meeting goals, coverage, or channel blend; cite "Heath operating standards 2026-06-07."
2. Channel attribution: `Opportunity_Source__c` + RT IN (Net New - DS `0121R000001QF50QAG`, Conversion - DS `012VS000005ln5fYAA`). Lead-grain (`Account.Channel_Source__c`) only for lead-source analysis — label which grain is in use (see SFDC_FIELD_LIBRARY §5).
3. In any QA badge, label IB 2.0 as **standard**, OB 2.0 as **planning assumption**, everything else as window actuals.
4. Coverage rule of thumb: ~3× SQO-pipeline-to-quota.
5. When reporting a rep's performance: lead with conversion (SQO→win, mtgs/SQO, ASP) and blend vs 45/40/15 — not activity volume.
6. Expansion revenue is reported as overattainment, never as quota progress.

## Changelog
- 2026-06-08: created; standards from Pipeline Diagnosis rev 2.4–2.7 session decisions.
