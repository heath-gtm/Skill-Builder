---
name: prospecting-analyst
description: Your lead-level analyst. Connect Salesforce + Mixmax — turns any "which leads should I work?" question into a lead-by-lead work plan: per-lead status (never-touched / engaged-not-replied / gone-cold / hot), days-dark per lead, last-touch quality, re-engagement candidate ranking, recommended next action per lead. Different from Pipeline-Creation (account-level coverage) — this is lead-by-lead work assignment. SDR-facing. Trigger on "which leads should I work?", "who haven't I touched?", "show me cold leads", "hot leads to follow up on", "who's gone dark?", "re-engagement candidates", "lead status check", "next action per lead", "who replied but I didn't follow up?", or any lead-level work-assignment question. Also fire when an SDR opens Monday morning unsure what to work.
---

# Prospecting Analyst — your lead-level companion

**Required:** Salesforce + Mixmax. **Optional:** Octave (Aero score per lead), Common Room (signal overlay).

## What this analyst answers

- "Which leads should I work right now?" — prioritized lead-by-lead work plan
- "Who haven't I touched?" — never-touched leads ranked by ICP score
- "Show me cold leads" — engaged historically, gone dark, re-engagement candidates
- "Hot leads to follow up on" — replied / clicked / opened in last 7 days
- "Who replied but I didn't follow up?" — the most expensive miss surface
- "Next action per lead" — specific recommended motion for each lead

## What it owns internally

- **Per-lead status classifier**: never-touched / engaged-not-replied / gone-cold / hot
- **Days-dark per lead** + last-touch quality scoring (email open + click + reply weights)
- **Re-engagement ranker**: cold leads scored by ICP × time-since-last-touch × prior-engagement-depth
- **Hot lead surfacer**: replies in last 7d + clicks in last 14d + meeting-asks in last 30d
- **Next-action recommender**: per-lead recommended motion (cold sequence / reply / direct outreach / book meeting)

## Quality gates

**Status classification uses Mixmax + SFDC, never one source.** A lead that replied in Mixmax but has stale SFDC last-touch is HOT, not COLD.

**Re-engagement candidates name the trigger.** Not "follow up with Sarah." Instead, "Sarah replied positively in March, no contact since — recent layoff round at her company could reopen the conversation."

**Hot leads decay.** A reply from 6 days ago is more urgent than a reply from 2 days ago — the analyst sorts by urgency.

## Output format example

```
🎯 KARAN'S LEAD WORK PLAN · 47 leads, ranked by priority

🔥 HOT — work today (5)
  1. Sarah Chen @ Acme — replied "yes interested" 2d ago, no follow-up
  2. Mike Rodriguez @ Vortex — booked meeting via Calendly 1d ago, prep
  3. Jim Coulon @ Datadog — opened 4 emails in last 3d, no reply yet
  4. Petra Lovric @ Blend — clicked pricing page yesterday
  5. Linda Park @ PGA — replied "send more info" 5d ago, no follow-up

♻️ RE-ENGAGE — work this week (12 candidates ranked)
  1. Tim Lee @ Halborn — last reply March, layoff round announced, fresh trigger
  2. Anna Kim @ Whip Around — engaged Q4, switched roles to VP RevOps
  ...

🥶 COLD — work when hot queue is clear (8 candidates)
  ...

❄️ NEVER TOUCHED — start fresh sequences (22)
  Sorted by ICP composite score:
  1. Adam Bell @ Stripe (ICP: 91, signal: 14 sales hires)
  2. Maria Gonzalez @ Brex (ICP: 88, signal: Series E)
  ...

📊 The most expensive miss this week:
  Sarah Chen (#1 above) replied 2 days ago. Every day she waits is -23% reply rate.

Recommended order:
  1. Reply to Sarah Chen NOW (under 2 minutes)
  2. Prep for Mike Rodriguez tomorrow (15 min)
  3. Run the re-engage sequence for Tim Lee + Anna Kim
  4. Start 5 new sequences from "never touched" top of list
```

## Used by

- **Daily Drop** workflow (the daily 10-lead Slack message)
- **Daily-Sales-Assistant** workflow (rep mode)
- **AE-pipeline-analysis** (top-of-funnel section)
- Standalone for SDR / AE Monday-morning planning

## When NOT to use

- For account-level coverage (use Pipeline-Creation Analyst)
- For active deals already in pipeline (use Deal-Health Analyst)
- For pre-funnel ICP qualification (use ICP Analyst first)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Contact.Email, LeadSource, LastActivityDate (lead-level status classifier)
- Account.Aero_Account_Fit_Score__c (hot lead ranking)
- Mixmax sequence enrollment via mixmax_query_sequence_enrollment (cross-system)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

Lock-ins #11 (channel classifier), #16 v9.1 (4-source activity), #25 (Daily Drop format).

## Make.com / API packaging

**Input:** `{ rep_email: string, mode: "full | hot_only | re_engage | never_touched | next_action", limit: number }`

**Output:** `{ hot: [...], re_engage: [...], cold: [...], never_touched: [...], next_action_per_lead: [...], expensive_misses: [...] }`

**Failure modes:** No Mixmax → status classification is SFDC-only, hot/cold detection degraded. No SFDC → cannot proceed.

## Shippable as

Standalone connector-gated SKU. Make.com node. The SDR's Monday morning companion.
