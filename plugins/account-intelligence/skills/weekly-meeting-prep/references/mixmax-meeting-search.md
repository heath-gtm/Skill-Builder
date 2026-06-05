# Mixmax Historical Meeting Search — Reference Guide

This file details how to use the Mixmax MCP to pull historical meeting context for each
external customer identified in Step 2 of the weekly prep workflow.

## Search Methodology

Run TWO searches for each external customer domain:

### Search 1: Events by Domain

Use the Mixmax `meetings` tool with `action: "search_events"`:

```
action: "search_events"
domain: "[customer-domain.com]"
after: "[6 months ago, ISO format]"
expand: "mixmax:summary"
limit: 25
```

The `expand: "mixmax:summary"` parameter includes AI-generated summaries inline where
available, saving round trips.

### Search 2: Meeting Summaries by Attendee Email

For each external attendee's email address, use:

```
action: "search_meeting_summaries"
attendee: "[attendee@domain.com]"
isExternal: true
from: "[6 months ago, ISO format]"
to: "[today, ISO format]"
owner: "me"
limit: 25
```

Run this for each unique external attendee email found in Step 2. Deduplicate results across
attendees — the same meeting may appear for multiple attendees.

## Pull Full Summaries & Transcripts

For each meeting found that has an AI summary available:

1. **Full summary** — Use `action: "get_meeting_summary"` with the `meetingKey` (the `id`
   returned by `search_meeting_summaries`). This gives you topics discussed, decisions made,
   action items, and sentiment.

2. **Transcripts for key meetings** — Use `action: "get_meeting_transcript"` with the
   `meetingKey`. Only pull transcripts for the **3 most recent or most strategically important**
   meetings. Prioritize:
   - QBRs or business reviews
   - Escalation or complaint meetings
   - Onboarding kickoffs
   - The most recent meeting (regardless of type)

   Transcripts are large — pulling more than 3 will bloat the briefing without proportional value.

## Synthesis Framework

From all meetings found, synthesize into these five categories:

### 1. Meeting History Overview

- Total number of historical meetings found
- Date range: first meeting → most recent meeting
- Meeting cadence pattern: weekly? monthly? ad hoc? clustered around events?
- Other Mixmax team members who've attended (besides Heath)

### 2. Key Topics & Themes

- Recurring topics across meetings (sequence performance, CRM integration, onboarding, billing, etc.)
- Features or products discussed most frequently
- Interest expressed in capabilities they're not yet using
- Any product feedback or feature requests mentioned

### 3. Problems & Escalations

- Issues, bugs, or complaints raised in previous meetings
- Unresolved problems flagged but not yet closed
- Escalation patterns — same issue recurring across multiple meetings is a red flag
- For each problem: when raised, severity, current status if known

### 4. Commitments & Action Items

- Action items assigned to Mixmax team members — especially any potentially still open
- Promises made to the customer (feature requests logged, timeline commitments, follow-ups)
- Action items assigned to the customer that Heath should follow up on
- **Items older than 60 days without resolution should be flagged as urgent**

### 5. Relationship Trajectory

- Trending positive, neutral, or concerning?
- Signals of expansion interest, churn risk, or deepening engagement
- Notable quotes or sentiments — pull verbatim from summaries/transcripts when available
- Changes in engagement frequency (meeting more often? less often? stopped for a while then restarted?)

## Flag Critical Items

Based on the full historical analysis, flag the **Top 3 things Heath MUST address** in the
upcoming meeting:

1. **Most important unresolved issue or open action item** — with full context on when it was
   raised, who owns it, and why it matters
2. **Biggest opportunity** — based on expressed interest from the customer in previous meetings
3. **Relationship risk or commitment needing follow-through** — anything that could erode trust
   if not addressed

These three items feed directly into the briefing's "Recommended Conversation Angles" section.
At least one conversation angle in the final briefing must reference historical meeting context.

## When Data Is Missing

| Scenario | What to report |
|----------|---------------|
| Zero summaries AND zero events | "No historical meeting data found in Mixmax for [domain]. This may be a first meeting, or Meeting Copilot may not have been active for previous calls. Check your email thread history manually before the meeting." |
| Events found but no summaries | Report the event history (dates, titles, attendees). Note that AI summaries were not available. Suggest Heath review personal notes or email threads. |
| Summaries exist but are thin | Report what's there, supplement with transcript pulls for the most important meetings. |
| Mixmax MCP errors or is unavailable | Skip this entire step. Note in the briefing: "Historical meeting context unavailable — Mixmax MCP returned an error." Add a manual action item for Heath to review email threads. Continue with Steps 4-6. |

Always note the date range of data found — don't imply completeness if data only goes back a
few months.
