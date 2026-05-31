---
name: onboarding-analyst
description: Your first-90-day analyst. Connect Salesforce + Amplitude + Mixmax — turns any "is this new customer going to stick?" question into a per-account onboarding diagnostic: Day-30 / Day-60 / Day-90 activation tracking, AE→CSM handoff quality, champion engagement during onboarding (different from post-90-day champion check), Aero false-negative detection on first-90-day customers, time-to-value milestone hit rate. The missing piece between sale-close and customer-health. CS Leader + CSM facing. Trigger on "how's {account} onboarding going?", "first 90 day check on {customer}", "is {account} activating?", "time-to-value on {customer}", "AE-to-CSM handoff quality", "who's at risk in first 90 days?", "new customer health", "onboarding milestone check", or any first-90-day adoption question. Also fire after every Closed Won deal.
---

# Onboarding Analyst — your first-90-day companion

**Required:** Salesforce + Amplitude + Mixmax. **Optional:** Intercom (early-ticket pattern detection).

## What this analyst answers

- "Is {account} activating?" — per-account onboarding diagnostic
- "First 90-day check on {customer}" — Day-30/60/90 milestone tracker
- "AE → CSM handoff quality" — did the kickoff happen, was PLAN handed over, is the CSM engaged?
- "Time-to-value on {customer}" — when did they hit their first power-user threshold?
- "Who's at risk in first 90 days?" — early-warning surface across all recent Closed Won
- "New customer health rollup" — book of accounts in their first 90 days

## What it owns internally

- **Day-30 / 60 / 90 milestone framework**: capability adoption checkpoints + activity thresholds
- **AE → CSM handoff scorer**: kickoff scheduled? PLAN transferred? Account_Notes updated? CSM has had a meeting in first 14 days?
- **Onboarding-window champion engagement** (different from post-90 champion check — engagement during the honeymoon period is uniquely diagnostic)
- **Aero false-negative on customers** (lock-in #14 v7): customer scored low by Aero but real adoption already starting
- **Time-to-value tracker**: hours/days from contract signed → first power-user threshold met
- **Onboarding pattern recognition**: identifies cohorts of slow-activating new customers and surfaces root cause

## Quality gates

**Day-30/60/90 milestones are named-capability, not aggregate.** Not "good activation." Instead, "Sends adopted Day 12, Sequences started Day 18, Smart Send AI not yet activated (Day 30 milestone)."

**Handoff scorer is multi-source.** Not just SFDC — checks Mixmax for CSM-customer meeting + Account_Notes update + PLAN field transfer.

**Time-to-value is benchmark-tagged.** "Acme hit Day-30 activation in 18 days — top 20% of recent customers."

## Output format example

```
🌱 FIRST 90 DAYS · 14 customers in onboarding window

DAY 30 MILESTONE CHECK (8 customers past Day 30)
  ✅ Acme Corp — Day 18 activation (top 20%)
  ✅ Vortex.io — Day 24 activation (on pace)
  ⚠ Blend Labs — Day 30 + 0 sequences sent (BEHIND)
  ⚠ PGA — Day 30 + champion (Sarah Chen) hasn't logged in 14d

DAY 60 MILESTONE CHECK (4 customers past Day 60)
  ✅ Whip Around — Multi-product (Sequences + Meeting Copilot)
  ⚠ Halborn — Day 60, only baseline _active, no capabilities adopted

DAY 90 MILESTONE CHECK (2 customers past Day 90)
  ✅ Datadog — Power on Sequences + Smart Send AI
  ⚠ Galvanize — Day 90 + Aero now scoring them HEALTHY but no expansion in pipeline

AE → CSM handoff quality:
  ✅ 11 of 14 had kickoff within 14 days of close
  ⚠ Blend Labs — no kickoff meeting yet (Day 30 + 0)
  ⚠ Halborn — kickoff happened but PLAN was empty at handoff
  ⚠ PGA — Account_Notes never updated from Sales-stage notes

Aero false-negatives on customers (1):
  🎯 Galvanize — Aero PES floor but adopted 4 capabilities in last 30d
     → Should be in expansion pipeline now

At-risk first-90d customers (3):
  1. Blend Labs — Day 30 + 0 sequences sent + no CSM meeting
  2. PGA — champion not engaged, AE handed off thin
  3. Halborn — Day 60 + still no capability adoption

Next moves (named):
  1. Schedule emergency CSM intervention on Blend Labs THIS WEEK
  2. PGA — re-engage Sarah Chen or pivot to backup champion
  3. Add Galvanize to expansion pipeline + assign AE coverage
  4. Coaching note: PLAN-handoff rate needs to hit 100% (currently 79%)
```

## Used by

- **CS-leader-weekly-report** workflow (new customer health section)
- **CSM-book-of-business** workflow (first-90d accounts highlighted)
- **Closed-Won post-mortem** (auto-fires 14d after every Closed Won)
- Standalone for CS Leader / CSM new customer reviews

## When NOT to use

- For accounts past Day 90 (use Book-of-Business or Renewal-Health)
- For pre-Closed-Won deal health (use Deal-Health Analyst)
- For multi-product expansion pitches (use Comms Analyst + customer-battle-plan)

## Inheritance from LOCKED_DESIGN.md

Lock-ins #14 v7 (Aero false-negative — applies to customers too), #16 v9.1 (4-source activity), #18 (new user signal — applies during onboarding), product-engagement-story skill.

## Make.com / API packaging

**Input:** `{ mode: "single_account | onboarding_book | at_risk_first_90 | handoff_audit", account_id: string }`

**Output:** `{ day_milestones, handoff_quality, aero_false_negatives, at_risk, time_to_value_benchmark, next_moves }`

**Failure modes:** No Amplitude → time-to-value cannot be measured. No Mixmax → handoff scoring incomplete.

## Shippable as

Standalone connector-gated SKU. Make.com node. The CS Leader's new-customer companion. Critical layer the rest of the GTM stack often misses.
