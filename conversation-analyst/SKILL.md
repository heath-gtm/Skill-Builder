---
name: conversation-analyst
description: Your conversation analyst. Connect Mixmax + Salesforce — turns any "what's been said / what's happening with this relationship?" question into a conversation pulse: meeting timeline, email reply tracking, last positive signal, champion drop-off detection, meeting digest, follow-up drafting. Use when a rep needs to know what's been said before reaching out, a leader is prepping for a 1:1, or a CSM is preparing for a QBR. Trigger on "what's happening at {account}?", "summarize my meetings this week", "draft a follow-up for {account}", "is the champion still engaged?", "when did we last hear from {contact}?", "QBR prep for {customer}", "what did we discuss with {prospect}?", "conversation pulse on {account}", "did {champion} go dark?", or any communication-history / relationship-state question. Also fire when an AE walks into a meeting cold and needs the 60-second "where we left off" read.
---

# Conversation Analyst — your CRM history analyst

**Required connectors:** Mixmax (for meeting + email + sequence history) AND Salesforce (for Task/Event activity sync, contact roles, and account context).

**Optional connectors:** Gmail (for full email thread context beyond Mixmax-tracked sends) · Common Room (for cross-channel signals like LinkedIn engagement).

## What this analyst answers

In plain English, the Conversation Analyst answers questions like:

- "What's been happening with Acme Corp?" → 90-day conversation timeline with meetings, replies, sequence enrollments, last positive signal
- "Summarize my meetings this week" → Per-meeting digest with action items, decisions made, open commitments
- "Draft a follow-up for the call I just had with Sarah at Acme" → Pulls the transcript / summary, references specific conversation points, drafts a personalized email
- "Is the champion still engaged?" → Champion drop-off detection: Sarah's last reply was 23 days ago vs typical 3-day cadence → 🚨 dropped off
- "When did we last hear from Mike at Vortex?" → Per-contact last positive signal date
- "QBR prep for Acme — give me everything from the last 90 days" → Full conversation context: meetings, attendees, key decisions, open items, current state of every committee member
- "What did we discuss with Datadog last call?" → Meeting transcript summary + action items from the most recent meeting
- "Give me a conversation pulse on Halborn" → Activity timeline + reply rate + sentiment of last 3 interactions
- "Did Linda go dark?" → Single-contact silence detection with reply-cadence baseline

## What it owns internally (the micro skills it composes)

The Conversation Analyst is the product layer over these atomic skills:

- **D3 — Mixmax Conversation History** — meetings, sequences, reply timelines, activity logs via Mixmax MCP
- **D1 cross-reference** (SFDC side of activity) — Tasks + Events tied to the account
- Meeting digest generation (the `meeting-followup-generator` skill in the account-intelligence plugin)
- Champion drop-off detection (custom heuristic — see quality gates below)
- Follow-up email drafting (the `octave-outreach-drafter` skill when Octave is connected, fallback to native draft)

## The quality gates this analyst guarantees

**Cross-source completeness.** The analyst NEVER reports "no activity" based on a single source. It cross-references Mixmax meetings + Mixmax emails + SFDC Tasks + SFDC Events + any provided email thread context to produce the real picture. This is the same 4-source activity check the Salesforce Analyst uses, expanded to include conversation-level signal beyond just date.

**Champion drop-off detection — locked rule:**
A primary contact is flagged as "dropped off" when their last reply is > 21 days ago AND they have ≥3 historical replies in the prior 90 days (so we know what their normal cadence looks like). Without that historical baseline, the analyst says "insufficient signal — primary contact has < 3 historical replies, dropping doesn't have meaning yet."

This prevents the false positive where a brand-new contact who hasn't replied to a single email gets flagged as "dropped off."

**Meeting digest quality.** Every digest includes: who attended, key topics, decisions made, action items with owner + deadline, open questions. Pulled from Mixmax meeting transcripts or summaries. If the meeting has no transcript or summary, the analyst says so rather than fabricating context.

## Output format example

For "Give me a conversation pulse on Acme Corp":

```
💬 ACME CORP — Conversation Pulse · last 90 days
   Source: Mixmax + SFDC activity layer

📅 Meeting timeline
   May 27 — Renewal touchbase · HM ↔ Megan Botting · 30 min
       Topics: pricing, seat count, AI Compose adoption
       Decisions: Confirmed June 15 contract renewal date
       Action items: HM to send updated SOW by May 30 ✅ (sent May 29)
   
   May 12 — QBR · HM ↔ Megan + Jim Coulon (CFO) · 60 min
       Topics: Q1 usage review, expansion play for sales team, Meeting Copilot rollout
       Decisions: Expand 25 seats in Q3
       Action items: Megan to share rollout plan ⏳ (still open, 17 days)
   
   Apr 30 — Pricing call · HM ↔ Jim · 45 min

📧 Email cadence
   Megan Botting:  last reply YESTERDAY · 6 replies in last 7 days · baseline cadence 1-2/week · ✅ HEALTHY
   Jim Coulon:     last reply 12 days ago · 4 replies in last 90 days · baseline cadence ~weekly · ⚠️ SLOWING
   Sarah Chen:     last reply 47 days ago · 8 historical replies · baseline daily/weekly · 🚨 DROPPED OFF

🎯 Last positive signal: Today — Megan's reply "great, sending you my SOW review by Friday"

📊 Sequence enrollment
   Active: "Q3 expansion ladder" — Sarah Chen + Mike R · 3 of 5 touches delivered · 0 replies · soft start

🧠 Pulse summary
   Renewal is on track (May 27 call locked the date). Megan is fully engaged. Jim is slowing — likely deferring details to Megan, which is normal for a CFO at this stage but worth watching. Sarah has gone silent after Q1 — she championed last year's renewal so we need to re-engage her before the Q3 expansion conversation. Sequence to her is in a soft-start phase; HM should consider a direct 1:1 instead.

📝 Suggested next move
   HM: 1:1 with Sarah by Friday — reference her Q1 advocacy + soft-ask on Q3 expansion role
   Open commitments to close: Megan's rollout plan share (17 days open)
```

## Used by (workflows that compose this analyst)

- **W1 Per-Account Brief Pipeline** (required — conversation timeline feeds the brief's "Conversation" card)
- **W2 Leader Brief Generator** (required — Champion Risk Watch + Deals to Unstick depend on this)
- **W4 Customer Strategy Suite** (required)
- **W5 Pipeline Analysis Manual** (required)
- **W6 Customer Interview Prioritizer** (required — relationship depth scoring)
- **W8 Win-Back Targeting** (required — recent inbound signal detection)
- **W10 Expansion Opportunity Scanner** (required — recent conversation context)
- **W12 Champion Migration Tracker** (required — tracks where former champions ended up)
- **W13 Quiet Quitting Detector** (required — replies spacing out is the early signal)

## When NOT to use this analyst

- For deal-risk classification (use Salesforce Analyst — the risk taxonomy lives there)
- For product usage questions (use Amplitude Analyst — capability data is its domain)
- For pure email send/automation (use Mixmax directly)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.Id, Account.Website
- Contact.Email, Contact.LastActivityDate
- OpportunityContactRole.IsPrimary (champion identification)
- Task / Event via salesforce_query_activities() (4-source activity, § 8)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

This analyst inherits lock-in #16 v9.1 (multi-source activity check — same rule, but applied at the conversation-detail layer not just the date-flag layer). Read `Account Brief Pipeline/LOCKED_DESIGN.md` and the existing `account-intelligence` plugin skills (`meeting-followup-generator`, `weekly-meeting-prep`, `weekly-meeting-digest`) before any invocation — those are the inheritance source for meeting digest and follow-up drafting patterns.

## Shippable as

A connector-gated capability requiring BOTH Mixmax and Salesforce. Customer connects both → Conversation Analyst becomes available. With Mixmax alone, the analyst can see meetings/emails/sequences but loses the SFDC activity-sync layer (some Tasks/Events not tracked in Mixmax will be missed). With Salesforce alone, the analyst can see Tasks/Events but loses the meeting transcript / sequence enrollment layer. Both required for full quality.

If only one is available, the analyst responds: "Connect {missing connector} to enable full conversation analysis. With {connected only} I can see [list of capabilities] but not [list of missing capabilities]."
