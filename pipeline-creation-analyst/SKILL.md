---
name: pipeline-creation-analyst
description: Your top-of-funnel analyst. Connect Salesforce + Amplitude — turns any "do I have enough at-bats?" question into pipeline coverage diagnosis: per-channel (Inbound / Outbound / Product) coverage, account engagement velocity per AE, hot-account ranking, Daily Drop generation, SDR coverage health, under-prospected segments. SDR Manager + VP Sales companion. Trigger on "do I have enough pipeline?", "pipeline coverage by channel", "who should we go after this week?", "run the Daily Drop", "top accounts to engage", "where are we under-prospected?", "hot accounts this week", "AE-by-AE coverage check", "pipeline gap analysis", or any account-level coverage question. Also fire when an SDR Manager preps for a pipeline review or a VP Sales asks about coverage going into the quarter.
---

# Pipeline-Creation Analyst — your top-of-funnel companion

**Required:** Salesforce + Amplitude. **Optional:** Octave / Aero (account fit scoring overlay), Common Room (hiring intent), FullEnrich (decision-maker enrichment).

## What this analyst answers

- "Do I have enough at-bats for next quarter?" — coverage math at channel + AE level
- "Pipeline coverage by channel" — Inbound / Outbound / Product split + relative health
- "Who should we go after this week?" — account-level prioritized work plan
- "Run the Daily Drop" — daily 10-account Slack drop generation
- "Hot accounts this week" — PQA signal + Aero score + engagement velocity
- "AE-by-AE coverage check" — per-rep account-engagement velocity

## What it owns internally

- **Channel-coverage math** (lock-in #11): Inbound vs Outbound vs Product splits + per-channel pipeline health
- **Account engagement velocity scoring**: 4-source activity weighted by recency
- **Daily Drop generation** (lock-in #25): 10 prioritized accounts per day with picker recommendations
- **PQA detection** (lock-in #18): new-user signal at customer accounts
- **Under-prospected segment surfacing**: ICP fit × current pipeline coverage gap
- **Hot account ranker**: composite of recent signal + Aero score + product engagement

## Quality gates

**Coverage math is forward-looking.** Doesn't just count open opps — projects pipeline needed for next-quarter target based on win rate × cycle time.

**Daily Drop has named recommended picker.** Not "good account" — instead, "Karan owns Acme territory but Felipe has bandwidth and Acme has 14 sales hires."

**Under-prospected surfacing is segment + channel.** Names exact gaps: "Mid-market SaaS Inbound: 22% of pipeline target, 8% of pipeline current."

## Output format example

```
📡 TEAM PIPELINE COVERAGE · Q3 target $1.8M new ARR

Per-channel coverage:
  INBOUND:    $890K projected vs $900K needed · 99% covered · HEALTHY
  OUTBOUND:   $310K projected vs $720K needed · 43% covered · UNDER ★
  PRODUCT:    $202K projected vs $180K needed · 112% covered · OVER

Per-AE engagement velocity (trailing 30d):
  Karan:     47 accounts engaged (book is 73) · 64% coverage · HEALTHY
  Isabelle:  68 accounts engaged (book is 71) · 96% coverage · STRONG
  Felipe:    23 accounts engaged (book is 58) · 40% coverage · LOW ⚠

🔥 THE DAILY DROP — Monday, June 1

  1. Acme Corp — Series D, 14 sales hires · Recommended: Karan ★
     Aero: 87 · ICP: 91 · Signal: Hiring spike + Outreach in stack
  2. Vortex.io — Layoff round just announced · Recommended: Felipe
     Aero: 73 · ICP: 88 · Signal: Cost consolidation play
  3. Datadog Trial — 3 active free users, 1 power user · Recommended: Isabelle
     Aero: 68 · ICP: 82 · Signal: PQA threshold met
  ... 7 more ...

Under-prospected segments:
  • Mid-market SaaS Outbound: 22% of pipeline target, 8% current coverage
  • Series C+ B2B with Outreach in stack: 35 accounts unworked
  • Customer accounts with new-user signups in last 30d: 12 ignored

Coverage gap math:
  Q3 needs $1.8M new ARR
  Current projection: $1.4M (-$400K gap)
  To close gap: 18 additional opps at avg $22K + 60% win rate = 30 more meetings
  → Felipe + outbound segment is the leverage point

Next moves (named):
  1. Felipe — block 4 hours/day for outbound through end of June
  2. Re-route Daily Drop heavier to Felipe for next 2 weeks
  3. Schedule SDR Manager 1:1 on Inbound→Outbound rebalance
```

## Used by

- **Daily Drop** workflow (the 7am CT Slack drop)
- **Sales-leader-weekly-report** (coverage dashboard)
- **Strike-Zone Analyst** as upstream input (funnel-leak diagnosis builds on coverage)
- **Daily-Sales-Assistant** workflow (leader mode pipeline section)
- Standalone for VP Sales / SDR Manager coverage reviews

## When NOT to use

- For lead-level work assignment (use Prospecting Analyst)
- For active deal health (use Deal-Health Analyst)
- For funnel-stage leakage (use Strike-Zone Analyst)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.Website (canonical → channel classification + Amplitude join, § 5 + § 10)
- Account.Channel_Source__c (canonical channel attribution, § 5; `Account.LeadSource` is fallback only — never `Opportunity.Channel__c`)
- Account.Aero_Account_Fit_Score__c + CR_Sales_Team_Hiring__c (top-of-funnel signal)
- Account.DWH_Forecasted_ARR__c (Q-target coverage math)
- 4-source activity check for engagement velocity per AE (§ 8)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

Lock-ins #11 (channel classifier), #14 v7 (play types — ACTIVATE / CONVERT / COLD OUTBOUND), #16 v9.1 (4-source activity), #18 (new user signal), #25 (Daily Drop format), #26 (tech stack + hiring fields).

## Make.com / API packaging

**Input:** `{ mode: "team_coverage | daily_drop | hot_accounts | under_prospected | per_ae_velocity", channel: "Inbound | Outbound | Product | All" }`

**Output:** `{ coverage_per_channel, ae_velocity, daily_drop: [{account, picker, signal}], under_prospected, hot_accounts, coverage_gap_math }`

**Failure modes:** No Amplitude → product signal omitted (Outbound + Inbound still work). No Aero → ICP scoring degrades to SFDC-only signal.

## Shippable as

Standalone connector-gated SKU. Make.com node. The SDR Manager / VP Sales coverage companion.
