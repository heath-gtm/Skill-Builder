---
name: cs-leader-weekly-runbook
description: >
  Reference runbook for generating, regenerating, or troubleshooting the
  Mixmax CS Leader Weekly report. Use whenever the user asks "how do I run
  the CS Leader Weekly", "what goes in the must-save section", "regenerate
  just the canary list", "how do I pick the Must-Renew accounts this week",
  or "the CSM book health dashboard is wrong". Also use for ad-hoc one-off
  generations outside the scheduled task.
---

# CS Leader Weekly — Runbook

This skill documents the CS Leader Weekly workflow for ad-hoc generation, troubleshooting, and single-section regeneration. For end-to-end automated runs, fire the registered `cs-leader-weekly-report` scheduled task.

## Where everything lives

- **Spec:** `Revenue Reviews/specs/cs_leader_weekly_spec.md`
- **Output folder:** `Revenue Reviews/Leader Weekly/CS/`
- **Filename:** `CS_Leader_Weekly_{YYYY-MM-DD}.html`
- **Published path:** `${GITHUB_PAGES_URL}/reports/leader-weekly/cs/{YYYY-MM-DD}.html`

## Selection heuristics

### Must-Save Top 3
Score each open at-risk account:
- +3 if renewal date within next 30 days
- +2 if renewal date within next 60 days
- +3 if Amplitude shows silent (no events in last 30 days)
- +2 if Mixmax MCP shows no meeting in last 45 days
- +2 if ARR ≥ top-quartile of CS book
- +1 if sponsor change detected (CRM contact churn)
Pick top 3. Each row needs a named save play this week (exec call, business review, escalation), NEVER "monitor".

### Must-Renew This Month
Filter: renewal date in current calendar month, status not yet Confirmed. Sort by ARR descending. Action this week column must specify a concrete next step (renewal proposal sent, call booked, exec sponsor engaged).

### Renewal Pipeline 31-60 / 61-90
Filter: renewal date in next 31–60 days (table 1) and 61–90 days (table 2). Same shape as Must-Renew but action column is "engagement plan in flight" rather than "this week".

### Top 3 Expansion Plays
Score each customer:
- +3 if Amplitude shows usage above expansion threshold (e.g., seat utilization >85%)
- +2 if support ticket volume up week-over-week (often a feature-gap signal that maps to upsell)
- +3 if customer raised an exec ask in a recent meeting
- +1 if hit a renewal milestone (year 1 anniversary)
Pick top 3. Trigger signal column must be from THIS WEEK.

### Canary List (preventive)
Filter: NOT currently at-risk, but shows ≥2 of:
- Usage decline week-over-week >25%
- No meeting in last 30 days (where there used to be regular cadence)
- Sponsor change detected
- NPS drop in last 60 days
- Support ticket spike with low CSAT
These are pre-at-risk. The point is intervention BEFORE they hit Must-Save.

## Status badge thresholds (CSM Book Health)

- HEALTHY — NRR (90d) ≥ 100% AND no STRESSED accounts
- WATCH — NRR 90–100% OR 1–2 at-risk accounts
- STRESSED — NRR <90% OR ≥3 at-risk accounts

## Account Deep-Dive Protocol

For every named account in sections 2, 3, 4, 5, 8:
1. Mixmax MCP — recent meetings, sentiment, last-touch date.
2. `account-amplitude-crossref` — usage classification (heavy / moderate / silent) + specific events in the last 30 days.
3. `octave-messaging-suggestions` — recommended outreach if re-engagement is needed.

## Single-section regeneration

1. Read current `CS_Leader_Weekly_{date}.html`.
2. Replace the `<h2 id="...">` block (and content up to the next `<h2>`) for that section.
3. Re-validate the QA gate items applicable to that section.
4. Show diff before publishing.

## Publishing

Use `mixmax-publishing-core`'s `publishing-config-reference` skill to load the config, then publish via the GitHub Contents API. Wait 30–90s for Pages rebuild.

## Common failure modes

- **Must-Save accounts have no Amplitude usage read** → MUST regenerate. Save plays without usage context are useless.
- **Coaching notes too vague** → regenerate with specific account names + specific behaviors. "Heather should coach Sara on QBRs" is not acceptable. "Sara has skipped 2 consecutive QBRs with Acme — re-establish cadence this week and coach on prep template" is acceptable.
- **Canary list duplicates Must-Save accounts** → those don't belong in Canary. Canary is preventive (pre-at-risk).
- **Churn autopsy includes save actions** → it shouldn't. Autopsy is closed-loop / educational.
