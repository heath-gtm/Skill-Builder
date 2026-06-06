---
name: mixmax-composite-scoring
description: Self-contained orchestrator that computes the Mixmax composite ICP score (v4 — two-stage, channel-aware) for one or many accounts and returns a stack-ranked priority list. v4 replaces the v3 flat 10-component blend with a gate -> fit -> intent spine, weights fit to real won/lost outcomes, and channel-specific profiles (Product > Inbound > Outbound). Reads canonical Salesforce fields; enriches the Gmail gate via Deepline/BuiltWith. ONE skill call returns the fully enriched, stack-ranked list. Use whenever a workflow needs to rank, qualify, or compare accounts. Trigger on "composite score", "score these accounts", "rescore", "rank by composite", "stack rank", "ICP score for X", "is this an Aero false negative", "prioritize these leads", or any multi-source account qualification. Canonical v4 methodology (2026-06-05): https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-composite-scoring-v4-methodology-2026-06-05.html
---

# Mixmax Composite Scoring v4 — Self-Contained Orchestrator

**Purpose.** Compute a stack-ranked priority list using a two-stage, channel-aware model. One skill call: accounts in, fully enriched stack-ranked list out.

**Published methodology (canonical):** https://psychic-adventure-p3jj6y9.pages.github.io/operational/mixmax-composite-scoring-v4-methodology-2026-06-05.html
**Spec mirror (working folder):** `Revenue Reviews/specs/composite_scoring_v4_spec.md`

---

## What changed from v3 (and why)

v3 was a flat additive 10-component blend. A won/lost + convert-cohort backtest (June 2026) showed:
- **Gmail/Workspace = 2.67x lift** (gate); **Microsoft email = 0.34x** (disqualifier). Best predictor — was 0% of v3.
- **CRM presence (1.12x), sales-hiring (0.96x), generic fit scores (CR ICP 1.13x) are FLAT** — qualifiers, not differentiators.
- **First-party buyer-intent = 3.22x (11x at ≥2 people)** — the self-serve differentiator. Bombora third-party = 0.57x (excluded).
- Fit is flat among signups; **intent predicts self-serve conversion.**

So v4 = **gate → fit differentiator → intent ranker**, channel-weighted, dropping AE-activity artifacts (recency, ownership) and never giving the Aero-False-Negative flag a flat bonus (score intent on REAL usage).

---

## Execution Orchestration

### STEP 1 — Resolve universe + channel
Channel = `Channel_Source__c` (Product / Inbound / Outbound), validated by stamps `Sales_PQA_Date_Account__c` (Product), `MQA_Date_2024__c` (Inbound), `OQA_Date__c` (Outbound). Multi-stamp → priority Product > Inbound > Outbound.

### STEP 2 — SFDC baseline (one bulk query)
```sql
SELECT Id, Name, Website, OwnerId, Channel_Source__c,
  Sales_PQA_Date_Account__c, MQA_Date_2024__c, OQA_Date__c,
  Email_Provider__c, CRM__c, Sales_Acceleration_Tool__c,
  CR_of_Sales_Team__c, CR_Sales_Team_Hiring__c,
  Aero_Account_Fit_Score__c, Product_Engagement_Verdict__c, Aero_Product_Engagement_Score__c,
  DWH_Customer_Type__c, Account_Tier__c,
  (SELECT Title FROM Contacts LIMIT 200)
FROM Account WHERE Id IN (...)
```

### STEP 3 — Fill gaps (parallel subagents)
- **Gmail gate** — if `Email_Provider__c` null, Deepline `builtwith_domain_lookup` (Google Apps/Workspace vs Microsoft 365/Outlook), batch 16/call, write back.
- **Buyer-intent** — Common Room Contact at `companyWebsite=<domain>`, filter `memberLeadScorePercentile >= 75, scoreId "ls_464"` → count of high-intent people.
- **Product usage** — `Product_Engagement_Verdict__c` / Amplitude PES + active users.
- **Committee depth** — CR contacts count.

### STEP 4–5 — Score (see §Math), stack rank + tier, deliver.

---

## The Math (v4)

```
gmail_gate  = 1.00 Gmail · 0.55 Microsoft/Outlook · 0.90 unknown
intent_pes  = POWER 100 / ESTABLISHED 85 / EMERGING 55 / DORMANT 25 / UNTOUCHED 10 / NO_DATA 0
              AERO_FALSE_NEGATIVE → by REAL active users (au>=20:90,>=10:75,>=5:60,>=2:45,else 30)
intent_buyer= CR Buyer-Intent ls_464: >=2 people 100 / 1 person 70 / else 0
intent_comm = CR contacts: >=20:100 / >=10:80 / >=5:60 / >=2:40 / >=1:20 / else 0
fit_octave  = Octave ICP x10
fit_aero    = Aero_Account_Fit_Score__c     # correlated -> low weight
fit_title   = buying title 100 / manager 50 / else 0

Channel profiles (sum 1.0):  pes  buyer comm | octave aero title
  PRODUCT  (intent-led)      .35  .15   .10  | .15    .05  .20
  INBOUND  (balanced)        .20  .15   .10  | .20    .10  .25
  OUTBOUND (fit-led)         .05  .05   .10  | .30    .15  .35

raw       = Σ(profile_weight × component)
composite = gmail_gate × raw
if Octave disqualifier OR anti-signal DWH_Customer_Type__c: composite = min(composite,50)
```
**Tiers:** ≥80 "1 Hot" · 65–79.9 "2 Warm" · 50–64.9 "3 Watch" · <50 "4 Disqualify".
**Dropped from v3:** recency, ownership (AE-activity artifacts).

---

## Salesforce field map (verified live)
`Email_Provider__c` (gate; backfill BuiltWith) · `CRM__c` · `Sales_Acceleration_Tool__c` · `CR_Sales_Team_Hiring__c`/`CR_of_Sales_Team__c` · `Aero_Account_Fit_Score__c` · `Product_Engagement_Verdict__c`/`Aero_Product_Engagement_Score__c` · buyer-intent via CR `ls_464` · `Channel_Source__c` + PQA/MQA/OQA stamps · `Account_Tier__c`.
> Library corrections: channel = `Channel_Source__c` (not `Channel__c`); add the three qualification stamps.

## Honest limitations
Weights fit to one snapshot (n≈99 + 80) — re-fit quarterly. BuiltWith detection positive-only. Buyer-intent/committee partly engagement-confounded. Tier thresholds tunable.

## Cross-references
v4 methodology (published) · `mixmax-analyst-suite:sfdc-field-library` · `product-engagement-story` · `deepline:niche-signal-discovery`
