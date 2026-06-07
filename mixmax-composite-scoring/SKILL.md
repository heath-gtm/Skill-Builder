---
name: mixmax-composite-scoring
description: Self-contained orchestrator that computes the Mixmax composite ICP score (v5.3 — layered, evidence-weighted) for one or many accounts and returns a stack-ranked priority list. v5 replaces blended pools with a layered model — gates, then an external-signal base rank computed for EVERY account, then product/intent escalators as bounded additive boosts. Three models read one signal library: Model A prospect acquisition, Model B customer expansion, Model C win-back. Weights are locked to a 100-won/60-lost truth-cohort backtest (2026-06-06). Trigger on "composite score", "score these accounts", "rescore", "rank by composite", "stack rank", "ICP score for X", "is this an Aero false negative", "prioritize these leads", or any multi-source account qualification. Canonical methodology: https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-signal-stack-v5-blueprint-2026-06-06.html
---

# Mixmax Composite Scoring v5.4 — Layered Signal Library

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


## v5.3.1 delivery layer — Plays + per-account evidence (2026-06-07)

Scores rank; **plays decide the motion.** One account = one play, evaluated top-down (canonical doc section 06d):
Competitor-exclude > In-Flight (open opp) > Expansion (`DWH_DS_Customer_ARR__c` > 0 or RT=Customer) > SS->DS (`DWH_SS_Customer_ARR__c` > 0, DS=0) > Win-Back (RT=Fall Off, no ARR) > PQA Re-Engage (RT=Prospect + PQA date) > Net-New.

**Hard rules:**
- `Account.RecordTypeId` is the lifecycle gate — never derive cohorts from field filters alone. Re-pull on every refresh (drift is real week-to-week).
- ARR truth = `DWH_DS/SS_Customer_ARR__c` + `DWH_Customer_Type__c`. Never read ARR from derived sheets. Self-serve payers keep RT=Prospect by design.
- Channel (`Channel_Source__c`) segments WITHIN a play; it is never a model input or play gate. (2026-06-07 product-channel remap in SFDC: model + plays unaffected; channel cuts in downstream reports have a break-in-series at that date.)

**Per-account evidence contract ("Why this score"), in order:**
1. Escalators first (live product usage + buyer-intent) — the rep's outreach context.
2. Fit case: CRM-in-stack (Salesforce/HubSpot = the strongest correlated stack signal), hiring count, displaceable competitor, talk-to-sales CTA.
3. Gmail as qualifier ("they qualify for our motion"), never as the win driver. Microsoft = the cap explained.
4. Caveats stated plainly: Octave DQ cap, coverage cap, unknown email stack haircut.
Plus per account: Amplitude capability breakdown (what they use / don't, from `amplitude-event-taxonomy`; flag ghost-active), Octave play (native assignment where scored; rule-based fallback marked *), SFDC deep link, and for Win-Back the loss story (last lost renewal CloseDate + Amount + `Loss_Reason__c` + `Main_Competitor__c`, `Past_Renewals__c` tenure, still-active users).

**Proposed v5.4 (not yet weighted):** capability breadth (uses x/6 tracked capabilities) as a bounded escalator. Requires backtest per the discipline loop.

**Field/event fixes (verified live 2026-06-07):** Opportunity competitor field is `Main_Competitor__c` (`Competitor__c` does not exist). Amplitude `Template` filter is `action = "Create"` (capitalized). `followup created` returned zero volume in 90d — taxonomy needs the current AI-followups event name.


## v5.4 (sample-validated 2026-06-07) — pipeline changes

Validated on an 18-account stratified sample (3 per play, full enrichment rebuild, byte-identical re-run). Weights unchanged pending re-fit; these are STRUCTURAL changes:

1. **People component (.10) = DM findability, not committee depth.** FullEnrich database search (search_people, zero credits): sales-leadership title found at the domain = 100, not found = 0. Found 12/18 on sample; misses correctly identify non-ICP motion (nonprofits, VCs, consumer). Waterfall enrichment (email+mobile) only fires on play entry.
2. **Product escalator reads Amplitude ONLY** (never Aero PES): +6 = >=5 active users 30d at gp:domain; +12 = >=2 capabilities with >=3 users (or paying + active). Read order: SFDC Product_Engagement_Verdict__c (fresh) -> existing Customer Strategy Brief (same taxonomy — apples-to-apples) -> fresh Amplitude pull last.
3. **DQ accounts: flagged, never ranked.** They exit play work queues; capped score retained for audit/grading only.
4. **Model selection by commercial state, never play:** DWH ARR > 0 -> Model B; else Model A. (In-Flight prospects = A; In-Flight payers = B.)
5. **Octave reframed: validated qualifier.** Flat-within-closed-deals (1.03x) is the expected result for a gate — every tested deal already passed ICP. The DQ boundary is the validated part; keep gate + weight, revisit at re-fit with this framing.
6. **Shadow signals (computed, not weighted):** capability breadth (x/6) and team whitespace (teams sold / DWH teams present, fields: Sold_to_SDRs/AEs/full_cycle_AE_team/Success/Partner_Manager_Team/Recruiting/Other__c over DWH_of_Teams__c + DWH_of_AE/SDR/CS_Users__c). Promote per the discipline loop only.
7. **SS->DS play gate:** a paying SS account with no findable sales-titled DM cannot run a conversion motion — route to usage-expansion touch instead.

Field name corrections (verified live): `Sold_to_AEs__c`, `Sold_to_full_cycle_AE_team__c` (not Sold_to_full_cycle_AE__c); Opportunity competitor = `Main_Competitor__c`; channel context = `Channel_Source__c` for prospects without an open opp, `Opportunity_Source__c` on new-business/conversion deals.


## Model close-out (2026-06-07) — all open questions resolved

- **History: OUT of the score.** Echo test: prior-won accounts won at 84% vs 82% baseline (1.02x) within engaged accounts — flat + circular. History is context-grade: evidence text + routing only. Weights renormalize over remaining filled components.
- **PES-M v1 built** (the Mixmax Product Engagement Score, separate model): `0.25*activity + 0.35*breadth + 0.40*depth` from the Amplitude capability matrix; GHOST_ACTIVE/NO_DATA overrides; verdicts Power/Established/Emerging/Dormant. Validated 9.0x: 34% of paying accounts >=Established vs 4% non-paying. Artifact: Revenue Reviews/specs/pesm_v1_2026-06-07.csv. The product escalator and Model B adoption component read PES-M. SFDC mapping: Product_Engagement_Verdict__c + PESM_Score__c (RevOps to create).
- **Team whitespace validated on the full paying book:** computable 495/777; median coverage 0.00; 280 zero-Sold_to accounts (partly flag hygiene — on the DQ list); 185 addressable targets (>=3 users on unsold teams) on $3.25M ARR. Stays shadow until the forward expansion-outcome lift test; target list ships into the Expansion play now.
- **T8 forward test registered + baselined:** 173 strike vs 173 size-matched 50-79 controls; outcome = new opp or external meeting 2026-06-07 -> 2026-09-04; pass >=2.0x; baseline opp counts snapshotted. Register: Revenue Reviews/specs/t8_forward_test_register.json.

## Cross-references
Canonical v5.3 doc (above, incl. section 06d play mapping) · v4 methodology (superseded) · `sfdc-field-library` · `product-engagement-story` · `strike-zone-analyst`
