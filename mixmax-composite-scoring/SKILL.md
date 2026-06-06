---
name: mixmax-composite-scoring
description: Self-contained orchestrator that computes the Mixmax composite ICP score (v5.3 — layered, evidence-weighted) for one or many accounts and returns a stack-ranked priority list. v5 replaces blended pools with a layered model — gates, then an external-signal base rank computed for EVERY account, then product/intent escalators as bounded additive boosts. Three models read one signal library: Model A prospect acquisition, Model B customer expansion, Model C win-back. Weights are locked to a 100-won/60-lost truth-cohort backtest (2026-06-06). Trigger on "composite score", "score these accounts", "rescore", "rank by composite", "stack rank", "ICP score for X", "is this an Aero false negative", "prioritize these leads", or any multi-source account qualification. Canonical methodology: https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-signal-stack-v5-blueprint-2026-06-06.html
---

# Mixmax Composite Scoring v5.3 — Layered Signal Library

**Canonical (locked 2026-06-06, QA-verified):** https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-signal-stack-v5-blueprint-2026-06-06.html
Supersedes v4. Three models, one library: **A** prospect acquisition · **B** customer expansion · **C** win-back.

## Architecture — layered, never blended

The v4/v3 lesson: components with different fill rates cannot share one weighted pool — the highest-fill signal dominates regardless of weights. v5 layers:

1. **Layer 0 — gates:** email stack multiplier (Gmail 1.00 / Microsoft 0.55 / unknown 0.90); Octave disqualifier -> cap 40; zero sales-motion fingerprints -> cap 55.
2. **Layer 1 — base rank** from EXTERNAL signals, renormalized over filled components (`score = SUM(wi*Fi*filledi)/SUM(wi*filledi)`), with a Coverage stamp (cap 65 when <0.5). Missing enrichment is never scored as zero.
3. **Layer 2 — escalators**, bounded ADDITIVE boosts (multiplicative saturates the ceiling): product usage +6 (PES>=40 / free seats / trial) or +12 (PES>=75 / paid usage); first-party buyer intent +8 (1 person, CR ls_464 >=75pct) or +15 (>=2 people). DQ accounts: boosts capped at +4.

## Model A locked base weights (truth-cohort evidence)

| w | Component | Evidence |
|---|---|---|
| .24 | Octave ICP (x10; disqualifier caps at 40) | qualitative anchor |
| .18 | SFDC history gradient: won-lapsed 85 / closed-lost 65 / open 50 / cold 20 | pending echo test; routing-grade |
| .14 | Sales hiring <=90d, **presence-flattened** (>=1 posting=100, 0=40) | **1.55x won/lost** — volume >=3 falsified (0.91x) |
| .13 | Competitor sales-engagement tool in stack (NO COMPETITION=40) | displacement targeting |
| .10 | CR committee depth gradient (20+:100 / 10+:75 / 5+:50 / 1+:25) | |
| .08 | Contact-sales/demo CTA on website | **1.22x** + DQ-tier separation (17% vs ~50%) |
| .07 | CRM in stack | qualifier-grade (1.12x) |
| .06 | Size band (25-2000 FTE=100) | won median 108 vs lost 46 FTE |

**Weight ZERO (falsified or unproven — do not reintroduce without a new backtest):** sales-role presence 0.96x · sales-headcount magnitude ~1.15x · hiring volume >=3 0.91x · YoY headcount growth 1.18x (retest quarterly) · Bombora/third-party topic intent 0.57x (inverse) · **Aero: weight zero, graded** — compute it, emit an accuracy report, never weight it.

**Tiers:** >=80 Hot · 65-79.9 Warm · 50-64.9 Watch · <50 DQ. The action list is the **>=90 strike band**.

## Model B (customer expansion) — per-domain
Adoption/PES .30 · seat-whitespace (seats/employees; *denominator upgrade: Crustdata sales headcount*) .25 · sales-hiring timing .20 · ARR headroom .15 · utilization (used/purchased) .10. **Rule: utilization <40% AND PES <40 -> SAVE-FIRST flag — retention play before any expansion pitch.**

## Execution

1. **SFDC-first reads.** Check signal stamps + `*_Refreshed_At__c`; only pull a provider when stale (volatile weekly: hiring, intent; slow monthly: CTA, headcount, tech). Write-back field spec: canonical doc section 06c.
2. **Universe + channel:** `Channel_Source__c` validated by PQA/MQA/OQA stamps (Product > Inbound > Outbound).
3. **SFDC baseline (one bulk SOQL):** Id, Website, `Email_Provider__c`, `CRM__c`, `Sales_Acceleration_Tool__c`, `Channel_Source__c`, opp history (StageName/IsClosed/IsWon/CloseDate), contacts/titles.
4. **Deepline enrichment (managed billing, all verified live):**
   - Hiring: `theirstack_job_search`, `company_domain_or` batches of 40, `job_title_pattern_or` as separate plain patterns ["sdr","bdr","sales development","account executive","account manager","revenue operations","head of sales","sales manager","vp sales"], `posted_at_max_age_days` 90.
   - CTA: `predictleads_company_website_evolution` per domain (limit 100); regex `(?i)(contact[ -]sales|talk[ -]to[ -]sales|book[ -]a[ -]demo|request[ -]a?[ -]?demo|get[ -]a[ -]demo|schedule[ -]a[ -]demo|speak (to|with) (sales|an expert))` over subpage text+urls; Firecrawl fallback for the ~3% misses.
   - Headcount (gate + Model B denominator only): `crustdata_v2_enrich_company`, `company_domain` 25/batch, `fields:"headcount"` -> `linkedin_headcount_by_role_absolute.Sales`, totals, growth timeseries. PDL premium NOT required.
5. **Common Room:** `commonroom_list_objects` Contact grain per domain -> committee count + buyer-intent people (`memberLeadScorePercentile >=75`, scoreId `ls_464`).
6. **Octave:** `qualify_company` on the base-rank shortlist (expensive calls go where the cheap signals point).
7. Score per layer math, stack rank, deliver with per-component transparency + Coverage + Aero grade report.

## Discipline (the AI-native loop)
New signals enter at weight zero -> shadow-score -> won/lost lift test (promotion >=~1.5x; <1.2x stays qualifier) -> promote/retire. Quarterly re-fit on the grown cohort; every re-fit ships as a versioned, QA-verified canonical page. Tests are pre-registered before data is seen (canonical doc section 06b falsification protocol).

## Cross-references
Canonical v5.3 doc (above) · v4 methodology (superseded) · `sfdc-field-library` · `product-engagement-story` · `strike-zone-analyst`
