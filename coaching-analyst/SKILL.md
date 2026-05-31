---
name: coaching-analyst
description: Your rep gap analyst. Connect Salesforce + Mixmax — turns any "who needs help and on what?" question into per-rep coaching priorities: PLAN-completeness rate per rep, activity quality per rep, deal velocity per rep, win rate by segment, time-in-stage outliers, dark-deal concentration. Different from QA Agent (watches the system) — Coaching watches the people. Sales Manager + Sales Leader companion. Trigger on "who needs coaching?", "rep gap analysis", "coaching priorities this week", "{AE}'s coaching plan", "where is {rep} struggling?", "team-level coaching themes", "show me PLAN-completion outliers", "who's working their pipeline?", "activity quality by rep", "who's the lowest performer?", or any rep-level coaching question. Also fire before a 1:1 or a forecast call.
---

# Coaching Analyst — your rep gap companion

**Required:** Salesforce + Mixmax. **Optional:** Amplitude (PQA leverage by rep), Octave / Aero (ICP-fit-of-rep-book scoring).

## What this analyst answers

- "Who needs coaching this week?" — ranked list with named topic per rep
- "Rep gap analysis on {AE}" — full per-rep diagnostic
- "Where is {rep} struggling?" — specific deal patterns / activity types they're below average on
- "Team-level coaching themes" — pattern across the team (e.g., "3 of 5 reps below PLAN-completion target")
- "Pre-1:1 brief" — surgical coaching prep for a manager about to walk into a 1:1
- "Pre-forecast brief" — which reps are reliable vs unreliable on this forecast call

## What it owns internally

- **PLAN-completeness rate per rep** (the BS detector at rep level)
- **Activity quality scoring**: meeting count × meeting quality (transcript-summarized) × follow-up cadence
- **Deal velocity per rep**: avg days in each stage, surface stage-stickers
- **Win rate by segment**: where each rep wins vs loses (segment, channel, deal size)
- **Time-in-stage outliers**: deals stuck longer than rep's own median
- **Dark-deal concentration**: % of rep's book that's ghost / stale
- **Coaching theme detector**: surfaces patterns across the team

## Quality gates

**Per-rep gap is specific.** Not "Karan needs help with PLAN." Instead, "Karan: PLAN completeness 14% (1 of 7 opps), missing field most often = Address_Decision_Dynamics__c."

**Coaching themes are team-level + statistically meaningful.** Doesn't surface "everyone needs to do better" — surfaces "3 of 5 AEs have win rate <40% in mid-market — investigate ICP fit or messaging."

**Pre-1:1 brief is forecast-aware.** Knows the next forecast call is Thursday and what the rep called last week, so the brief is "what should the manager press on?"

## Output format example

```
🧠 COACHING PRIORITIES · Week of June 1

TOP COACHING PRIORITY: Karan
  PLAN completeness: 14% (1 of 7 opps) — lowest on team
  Most-missing field: Address_Decision_Dynamics__c (5 of 7 opps)
  Stage-stickers: 3 opps in Solution Validation > 21 days (his median is 9)
  Activity quality: avg 1.3 meetings/wk (team avg 3.1)
  Win rate this Q: 22% mid-market, 67% SMB
  → 1:1 focus: PLAN + multi-thread + activity cadence

ISABELLE — strong, but watch:
  PLAN completeness: 87% (highest on team)
  Activity quality: avg 3.8 meetings/wk
  Win rate this Q: 71% (highest, but small sample n=7)
  Concern: book is 96% covered but pipeline is below quota → 
           she's working hard but pipeline math doesn't get there
  → 1:1 focus: pipeline-creation strategy, not execution

FELIPE — bottom-of-funnel issue:
  PLAN completeness: 67%
  Activity quality: avg 1.1 meetings/wk (lowest)
  Coverage: 40% of book engaged (lowest)
  → 1:1 focus: top-of-funnel coverage, not deal-level coaching

TEAM-LEVEL THEMES THIS WEEK:
  1. PLAN-completion target is 80%; team avg is 56%. Group training needed.
  2. 3 of 5 AEs have <40% mid-market win rate. ICP fit or messaging investigation.
  3. Multi-thread coverage averaging 1.4 contacts/deal (target 3+). Sequencing needs work.

Pre-forecast call brief (Thursday):
  • Karan called Commit on Vortex.io — actually SLIP_RISK (Champion went dark)
  • Isabelle called Best Case on Acme — actually MOMENTUM (5 meetings this week)
  • Felipe has 2 deals in Commit that just slid from Best Case last week (Commit Creep)
  Recommend: press Karan on Vortex, push Isabelle to upgrade Acme to Commit,
  challenge Felipe on commit-creep pattern
```

## Used by

- **Sales-leader-weekly-report** workflow (coaching priorities section)
- **Pre-1:1 brief** workflow (manager prep)
- **Pre-forecast call brief** workflow
- **Daily-Sales-Assistant** workflow (leader mode)
- Standalone for Sales Manager / Sales Leader weekly review

## When NOT to use

- For system-level QA on the analyst system itself (use QA Agent)
- For deal-by-deal diagnosis (use Deal-Health Analyst directly)
- For top-of-funnel coverage gaps (use Pipeline-Creation Analyst)

## Inheritance from LOCKED_DESIGN.md

Lock-ins #8 (deal-risk taxonomy), #16 v9.1 (4-source activity), #26 (PLAN Selling — never MEDDIC), #28 (Deal Health Summary).

## Make.com / API packaging

**Input:** `{ mode: "team_priorities | per_rep | pre_1_1 | pre_forecast | themes", rep_email: string | null }`

**Output:** `{ top_priorities, per_rep_gaps, team_themes, pre_1_1_brief, pre_forecast_brief }`

**Failure modes:** No Mixmax → activity quality cannot be measured (falls back to SFDC activity count only).

## Shippable as

Standalone connector-gated SKU. Make.com node. The Sales Manager's weekly coaching companion + Sales Leader's pre-1:1 brief generator.
