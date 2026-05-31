---
name: deal-health-analyst
description: Your active-deal analyst. Connect Salesforce + Mixmax — turns any "is this deal real?" question into a deal-by-deal risk verdict: deal-risk taxonomy (AT_RISK / SLIP_RISK / GHOST / CHAMPION_DROP / STUCK / STALE / MOMENTUM / HEALTHY), PLAN-vs-stage validation, multi-thread coverage check, days-dark per deal, quarter pacing math, commit creep watch. Sales Leader's daily companion. Trigger on "how are my deals?", "deal health on {opp}", "is {deal} going to close?", "which deals are stuck?", "what's at risk this month?", "rep is BSing me on {deal}", "forecast accuracy by AE", "commit watch", "show me ghost deals", "multi-thread check on {account}", or any open-deal diagnostic. Also fire when a Sales Leader walks into a 1:1 and asks "review {AE}'s open opps" or "what should I press {AE} on?"
---

# Deal-Health Analyst — your active-deal companion

**Required:** Salesforce. **Optional:** Mixmax (multi-thread + conversation depth), Amplitude (product-side momentum).

## What this analyst answers

- "Is this deal real?" — per-opp deal-risk verdict with rationale
- "Which deals are at risk this month?" — book-scan with surfacing of AT_RISK / SLIP_RISK opps
- "Is the rep BSing me on {deal}?" — PLAN-vs-stage gap detector
- "Multi-thread check on {account}" — is the rep talking to one person or many?
- "Commit creep watch" — which Commit-Cat deals quietly slid to Best Case?
- "Forecast accuracy by AE" — how often does {AE} hit Commit?

## What it owns internally

- **8-state deal-risk taxonomy** (lock-in #8): AT_RISK / SLIP_RISK / GHOST / CHAMPION_DROP / STUCK / STALE / MOMENTUM / HEALTHY
- **4-source activity check** (lock-in #16 v9.1): MAX(Account, Opportunity, Task, Event) LastActivityDate
- **PLAN-vs-stage validator** (lock-in #26): if Stage=Solution Validation but Address_Decision_Dynamics__c=null → BS flag
- **Multi-thread classifier**: <2 contacts in last 30 days = single-thread risk
- **Quarter pacing math** + Commit Creep Watch (movement from Commit→Best Case in trailing 14 days)

## Quality gates

**No deal verdict without 4-source activity proof.** If the analyst reports a deal as GHOST, it must show all 4 source dates that confirm no activity.

**PLAN gap surfaces field-by-field.** When PLAN is incomplete for current stage, the analyst names exactly which of the 4 fields (Problems_Account__c, Leverage_Alignment__c, Address_Decision_Dynamics__c, Next_Steps_Account__c) is missing.

**Forecast accuracy is trailing-quarter, never trailing-week.** Avoids small-sample noise.

## Output format example

```
🎯 KARAN'S ACTIVE DEAL HEALTH · 7 open opps

┌──────────────────┬──────────────┬──────────┬───────────┬─────────────────────┐
│ Account          │ Stage / ARR  │ Risk     │ Days-Dark │ Why                 │
├──────────────────┼──────────────┼──────────┼───────────┼─────────────────────┤
│ Acme Corp        │ Sol Val/$45K │ HEALTHY  │ 2         │ Multi-thread + PLAN │
│ Vortex.io        │ Prop/$67K    │ SLIP     │ 12        │ Champion went dark  │
│ Blend Labs       │ Sol Val/$28K │ STUCK    │ 23        │ No PLAN Next Steps  │
│ Datadog Trial    │ Eval/$112K   │ GHOST    │ 47        │ Zero activity 4-src │
│ Whip Around      │ Disc/$22K    │ AT_RISK  │ 7         │ Single-thread       │
│ ...              │              │          │           │                     │
└──────────────────┴──────────────┴──────────┴───────────┴─────────────────────┘

Forecast accuracy (trailing Q): Karan = 67% (team avg 73%)
Commit creep watch: 1 deal slid from Commit → Best Case (Vortex.io, -$67K)

Next moves (named):
  1. Vortex.io — re-engage Sarah Chen via Karan; offer demo of Smart Send AI
  2. Blend Labs — Karan needs to add Next Steps to PLAN before next pipeline review
  3. Datadog Trial — declare lost or run final outreach this week
```

## Used by

- **Sales-leader-weekly-report** workflow (full team rollup)
- **AE-pipeline-analysis** workflow (per-AE deep dive)
- **Daily-Sales-Assistant** workflow (leader mode)
- Standalone for ad-hoc deal review prep

## When NOT to use

- For renewals (use Renewal-Health Analyst)
- For top-of-funnel pipeline coverage (use Pipeline-Creation Analyst)
- For per-rep coaching priorities (use Coaching Analyst)

## Inheritance from LOCKED_DESIGN.md

Lock-ins #8 (deal-risk taxonomy), #16 v9.1 (4-source activity), #26 (PLAN Selling terminology — never MEDDIC), #28 (Deal Health Summary card spec).

## Make.com / API packaging

**Input:** `{ mode: "single_deal | rep_book | team_book", target_id: string, include_actions: bool }`

**Output:** `{ deals: [{ id, risk_state, days_dark, plan_gap, multi_thread, recommended_action }], forecast_accuracy: number, commit_creep: [...] }`

**Failure modes:** No Salesforce connected → "Connect Salesforce." Mixmax disconnected → degrades to 2-source activity check + flags reduced confidence.

## Shippable as

Standalone connector-gated SKU. Make.com node. Standalone API. The Sales Leader's daily companion.
