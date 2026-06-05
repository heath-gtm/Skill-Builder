---
name: account-health-monitor
description: >
  On-demand account health check that flags declining usage, user churn, and engagement
  shifts for a specific Mixmax customer account. The canary in the coal mine — catches
  problems between meetings. Trigger on: "how healthy is [account]", "check health for
  [domain]", "is [company] at risk", "account health", "usage declining at [company]",
  "churn signals for [domain]", "are we losing [company]", "engagement check on [account]",
  or any request to assess whether a customer account's product usage is trending positively
  or negatively. Also trigger when Heath asks about "risk" or "churn" alongside an account
  name or domain. Fire proactively when Amplitude data in a meeting prep briefing shows
  declining WAU or feature adoption — suggest running a full health check.
---

# Account Health Monitor

Produces a focused health assessment for a single customer account by analyzing Amplitude
usage trends, identifying churn signals, and surfacing intervention opportunities.

## What This Skill Does (and Doesn't)

**Does:** Answers "Is this account healthy, and if not, what specifically is declining?"
with numbers, trends, and named users who are at risk.

**Doesn't:** Generate meeting prep, draft outreach, or produce the full 7-section briefing.
For those, use `weekly-meeting-prep`. This skill is a quick diagnostic, not a deep briefing.

## Data Sources

All data comes from Amplitude (project ID `130895`). No Mixmax meeting history, no web
research, no Octave drafts. This is pure product analytics.

## Health Check Framework

For the given domain, run these analyses and score each dimension:

### 1. User Retention (Weight: 35%)

Compare active users in the last 30 days vs. the prior 30 days (days 31-60).

| Signal | Score |
|--------|-------|
| Active users grew >10% | Green |
| Active users stable (±10%) | Yellow |
| Active users declined >10% | Red |
| Active users declined >25% | Critical |

Also identify: which specific users dropped off? List names that were active 31-60 days
ago but NOT active in the last 30 days. These are your churn candidates.

### 2. Engagement Depth (Weight: 25%)

Compare feature breadth — how many feature categories does the average user touch?
Features: email tracking, sequences, templates, calendar, tasks, rules, Meeting Copilot.

| Signal | Score |
|--------|-------|
| Average user touches 3+ feature categories | Green |
| Average user touches 2 feature categories | Yellow |
| Average user touches 1 or fewer | Red |

Also check: is feature breadth expanding or contracting over 90 days?

### 3. Email Volume Trend (Weight: 20%)

Compare weekly email volume (last 4 weeks vs. prior 4 weeks).

| Signal | Score |
|--------|-------|
| Volume grew >15% | Green |
| Volume stable (±15%) | Yellow |
| Volume declined >15% | Red |
| Volume declined >30% | Critical |

### 4. Sequence Health (Weight: 15%)

Are sequences still being activated? Compare unique sequence activators (last 30d vs. prior 30d).

| Signal | Score |
|--------|-------|
| Activators grew or stable | Green |
| Activators declined but >0 | Yellow |
| Zero sequence activations in last 30d | Red |

### 5. Expansion Signal (Weight: 5%)

New workspace members added in last 30 days.

| Signal | Score |
|--------|-------|
| 2+ new members | Green |
| 1 new member | Yellow |
| Zero new members | Neutral (not scored negatively — some accounts are stable) |

## Overall Health Score

Compute a weighted score: Green = 3, Yellow = 2, Red = 1, Critical = 0.
Weight by the percentages above.

| Overall Score | Verdict |
|---------------|---------|
| 2.5 - 3.0 | Healthy — no action needed |
| 2.0 - 2.4 | Watch — monitor weekly |
| 1.5 - 1.9 | At Risk — intervention recommended |
| Below 1.5 | Critical — escalate immediately |

## Output Format

```
## [Company] — Account Health Check

**Overall: [Healthy / Watch / At Risk / Critical]** (score: X.X/3.0)

### Scorecard

| Dimension | Score | Signal |
|-----------|-------|--------|
| User Retention | [Green/Yellow/Red] | [X] active users (30d) vs [Y] prior 30d ([+/-Z%]) |
| Engagement Depth | [Green/Yellow/Red] | Avg [X] features/user, [trend] over 90d |
| Email Volume | [Green/Yellow/Red] | [X]/week (30d avg) vs [Y]/week prior ([+/-Z%]) |
| Sequence Health | [Green/Yellow/Red] | [X] activators (30d) vs [Y] prior |
| Expansion | [Green/Yellow/Neutral] | [X] new members (30d) |

### Users at Risk

[List specific users who were active 31-60 days ago but dropped off in last 30 days]

- [user@domain] — was [profile tier], sent [X] emails/month, now inactive
- [user@domain] — was [profile tier], last seen [date]

### What Changed

[2-3 sentence narrative interpreting the signals. What's the story? Is this seasonal?
Did a power user leave? Did sequence usage dry up? Connect the dots.]

### Recommended Action

[1-2 specific actions based on the signals:]
- If user churn: "Reach out to [specific person] — they were a power user sending [X]
  emails/month and went dark [Y] weeks ago."
- If feature contraction: "Schedule a feature re-enablement session focused on [feature]."
- If volume decline: "Check if they've adopted a competing tool — volume drops this steep
  usually mean a tool switch, not a usage change."
```

## Amplitude Query Patterns

Follow the same query construction guide as `weekly-meeting-prep`:
- Filter by `gp:email contains [domain]`
- Exclude test users: `userdata_cohort is not vbyym9zo`
- For the 30d vs. prior 30d comparison, run the same query twice with different date ranges
- For dropped users: get unique users in days 31-60, then check which are NOT in days 1-30

If queries fail, follow fallback strategies (try domain variations, try `gp:domain`, try
`get_users`). Only report "no data" after 3+ attempts.
