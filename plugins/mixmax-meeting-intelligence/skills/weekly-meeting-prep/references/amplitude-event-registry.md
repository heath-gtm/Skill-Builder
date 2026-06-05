# Amplitude Event Registry & Analysis Guide

Authoritative reference for all Amplitude queries in the weekly meeting prep workflow.
Project ID: `130895`.

## Universal Configuration

Apply these to EVERY query:

| Setting | Value |
|---------|-------|
| Project ID | `130895` |
| User property for domain filtering | `gp:email` contains `[customer-domain]` |
| Exclude test users | `userdata_cohort is not vbyym9zo` |
| Integration event exclusions | On `Connected Third-Party Integration`: exclude `google` and `microsoft` |

Other useful user properties:
- `gp:domain` — user domain
- `gp:workspaceId` — workspace identifier
- `gp:plan` — current plan type
- `gp:jobRole` — user's job role

## Event Definitions & Required Filters

### Email Events

**`Sent email on server`** — Email volume. NEVER analyze this event unfiltered — raw sends
are noise. Always apply one of these feature-specific filters:

| Filter | What it captures |
|--------|-----------------|
| `withSequence = true` | Sequence emails |
| `withTemplate = true` | Template emails |
| `calendarEnhancementTypes` contains `calendarlink`, `availability`, `event`, or `groupscheduling` | Calendar-enhanced emails |
| `relatedMixmaxInsights` is not `[]` | Insight-driven emails (Todo/Smart Follow-up) |

**Calendar enhancement exclusion:** Always EXCLUDE `default_calendarlink_in_signature` from
calendar enhancement analysis. It's passive/auto-added and doesn't represent intentional
feature usage.

### Sequence Events

| Event | What it means | Notes |
|-------|--------------|-------|
| `SequenceEditor_ConfirmActivateSequence_Clicked` | Sequence activations | Strongest value signal and payment predictor |
| `SequenceServer_ActivateRecipients_Activated` | Server-side activation confirmation | Backup verification of activations |
| `Sequences_Sequence_Created` | New sequences created | Creation ≠ activation — don't confuse these |

### Feature Events

| Event | Filter | What it captures |
|-------|--------|-----------------|
| `Connected Third-Party Integration` | Exclude google/microsoft | Real integrations (linkedin, salesforce, hubspot, zoom) |
| `Template` | `action = "create"` | Actual template creation (without filter, includes views/uses) |
| `meeting templates` | `action = "updated"` | Calendar template completion |
| `MeetingCopilot_Summary_Attempt` | — | Meeting Copilot attempted |
| `MeetingCopilot_Summary_Accessed` | — | Meeting Copilot summary viewed |
| `MeetingCopilot_Summary_SharedEmail_Sent` | — | Meeting Copilot summary shared via email |
| `Workspace_Member_Added` | — | Team expansion signal |
| `Tasks` | `action = "completed task"` | Actual task completions |
| `Rules` | `action = "activate"` | Successful rule activation |
| `Calendar_Meeting_Confirmed` | — | Meetings booked via Mixmax calendar |
| `Installed extension` | — | Extension installation |
| `Viewed message tracking details` | — | User checks email tracking in Gmail (engagement signal) |

### Conversion Events

| Event | Property | What it captures |
|-------|----------|-----------------|
| `Plan changed` | Check `productId` | Payment or plan change — productId tells you what plan |
| `App_Navigation_PageLoaded` | Check `page` | Which product areas the user visits |

## Analysis Framework

### A. User Roster & Activity (30-day window)

For every unique user from the customer domain, determine:

| Metric | Source |
|--------|--------|
| Active today (Y/N) | Any event today |
| Active last 30 days (Y/N) | Any event in 30d |
| Emails sent (30d) | `Sent email on server` (any filter) |
| Sequence emails (30d) | `Sent email on server` where `withSequence = true` |
| Sequence activations (30d) | `SequenceEditor_ConfirmActivateSequence_Clicked` |
| Tracking views (30d) | `Viewed message tracking details` |
| Calendar meetings (30d) | `Calendar_Meeting_Confirmed` |

**User profile tiers:**

| Tier | Criteria |
|------|----------|
| Power User | High email volume + multiple feature types active (sequences + tracking + calendar or templates) |
| Active User | Regular email volume + 1-2 features active |
| Light User | Some activity but minimal feature usage |
| Passive / No Feature Usage | On the account but zero meaningful product activity |

### B. Email Volume Trends (weekly, 90-day window)

- Total emails sent per week
- Sequence emails per week
- Unique users activating sequences per week

### C. Feature Adoption (90-day uniques)

Query unique users for each feature over 90 days. Order the results table from highest
adoption to lowest:

1. Email tracking (`Viewed message tracking details`)
2. Templates (`Sent email on server` where `withTemplate = true`)
3. Sequence activations (`SequenceEditor_ConfirmActivateSequence_Clicked`)
4. Calendar-enhanced emails
5. Calendar meetings confirmed (`Calendar_Meeting_Confirmed`)
6. Tasks completed (`Tasks` where `action = "completed task"`)
7. Rules activated (`Rules` where `action = "activate"`)
8. Meeting Copilot (any of the 3 events)

Calculate adoption percentages against the active user base for each feature.

### D. Integrations (90-day window)

`Connected Third-Party Integration` — exclude google/microsoft. Report which integrations
exist and which are missing. Key integrations to check for: Salesforce, HubSpot, LinkedIn,
Zoom, Slack.

### E. Team Expansion (90-day window)

`Workspace_Member_Added` — count and interpret: growing, stable, or shrinking?

### F. Plan/Billing

`Plan changed` — check `productId` for current plan type. If no data: "Plan and billing
cycle data not available in Amplitude — pull from Salesforce or Stripe before the meeting."

### G. WAU Trend (6-month window, weekly granularity)

Weekly active users over time. Look for: stability, growth, decline, anomalous dips,
seasonal patterns.

---

## Query Construction Guide

This section is critical — follow it precisely to ensure Amplitude queries return data.

### How to Query Amplitude

Use the Amplitude MCP tools. The primary query tool is `query_chart` or `query_amplitude_data`.
If one tool fails or returns empty, try the other. Do NOT give up after a single failed query.

### Recommended Query Sequence

Run queries in this order for each customer domain. This sequence is designed to build up
from simple to complex, ensuring you get at least basic data even if advanced queries fail.

**Query 1 — Active Users (simple, validates the domain works):**
Start with any active event filtered by `gp:email contains [domain]` over the last 30 days.
This confirms there are users from this domain in Amplitude. If this returns zero results,
the domain may be wrong — try variations (e.g., `datadoghq.com` vs `datadog.com`).

**Query 2 — User List:**
Get unique users by `gp:email` containing the domain. Use `get_users` or a segmentation
query grouped by `gp:email`. This gives you the full roster of emails.

**Query 3 — Email Volume:**
Query `Sent email on server` with `gp:email contains [domain]`, grouped by week, over 90 days.
Then repeat with `withSequence = true` for sequence emails.

**Query 4 — Feature Adoption:**
For each feature event in the registry, query 90-day uniques filtered by domain. You can
batch these or run them individually.

**Query 5 — WAU Trend:**
Query any active event by `gp:email contains [domain]`, grouped by week, over 6 months.

### Fallback Strategies

If Amplitude queries fail or return unexpected results:

1. **Try `get_users` with email filter** — sometimes the user lookup is more reliable than
   event queries for finding who exists on an account.
2. **Try `gp:domain` filter instead of `gp:email contains`** — some accounts may have the
   domain property set differently.
3. **Check for domain variations** — e.g., `datadoghq.com` (corporate) vs `datadog.com`,
   `gong.io` vs `gong.com`.
4. **If the Amplitude MCP tool errors**, note the specific error and try a different query
   structure. Do NOT skip Amplitude entirely after one failure.
5. **If all queries return zero**, report it clearly: "Zero Amplitude data found for [domain].
   This may indicate: (a) the account uses a different email domain, (b) they are a prospect
   with no Mixmax activation, or (c) the domain filter doesn't match their user properties.
   Try searching by individual attendee emails if known."

### Important: Never Leave Amplitude Empty

The Amplitude deep dive is the most valuable part of the briefing — it's what makes this
prep data-driven rather than just a web search summary. Exhaust all fallback strategies
before reporting "no data available." If you tried 3+ query approaches and none returned
data, document which approaches you tried and why they failed so Heath knows what to
investigate manually.
