---
name: account-intelligence-orchestrator
description: >
  The conversational entry point for Mixmax AE Account Intelligence. Routes rep intent to
  the right specialized skill, ensuring every output delivers a full 360-degree view with
  company research, Amplitude product usage, power user identification, meeting history,
  contact intelligence, and specific action plans. Handles open-ended requests like "what
  should I focus on", "review my week", "how are my deals", "who should I prospect", or
  any account/deal/meeting question. Trigger on: "what should I work on", "what needs my
  attention", "review my week", "morning briefing", "daily briefing", "what's on my plate",
  "help me prioritize", "what's happening with my accounts", "give me a rundown", "catch
  me up", or any broad request about the rep's book of business. This is the DEFAULT skill.
---

# Account Intelligence Orchestrator

The front door for AE Account Intelligence. Reps talk naturally; this skill interprets
their intent and dispatches to the right specialized skill.

**Core principle:** Every skill in this plugin delivers a full 360-degree view. Company
research, Amplitude product usage, power user identification, Mixmax meeting history,
contact enrichment, and specific action plans. There are no "light" outputs. When a rep
asks for anything, they get the complete picture.

## References

Load `sheet-schema.md` for the Google Sheet column layout.
Load `360-view-protocol.md` for the standard enrichment protocol that every skill follows.

## Intent Detection & Routing

When a rep sends a message, classify their intent and route:

### → Deal Intelligence
**Signals:** "deals", "pipeline", "forecast", "what's at risk", "stuck deals", "deal
review", "how's my pipeline", "what's closing", specific deal or account name in a deal
context ("how's the Acme deal")
**Invoke:** `deal-intelligence` skill
**What they get:** Full pipeline review with every deal enriched — company research,
Amplitude usage (active users, power users, feature matrix, WAU trend), Mixmax meeting
history with commitments and open items, contact intelligence with engagement mapping,
and synthesized verdicts with specific multi-step action plans.

### → Prospect Finder
**Signals:** "who should I go after", "prospect", "new accounts", "outbound targets",
"inbound", "product leads", "PQLs", "pipeline creation", "cold accounts"
**Invoke:** `prospect-finder` skill
**What they get:** Prioritized target list with every recommended account fully enriched —
company research, Amplitude usage (free users, power users, conversion signals), contact
enrichment with role mapping, competitive landscape, and specific outreach angles grounded
in all the data.

### → Weekly Meeting Prep
**Signals:** "meetings this week", "prep my week", "prep me for [company]", "who am I
meeting with", "calendar", "upcoming calls", "product research on [company]"
**Invoke:** `weekly-meeting-prep` skill
**What they get:** Full briefing per meeting — company background, Mixmax meeting history
with must-address items, Amplitude deep dive (users, features, trends), top contacts
with engagement levels, health assessment, and conversation angles.

### → Account Health Monitor
**Signals:** "is [account] healthy", "check health", "at risk", "churn signals", "usage
declining", "how's [domain] doing" (in a product usage context)
**Invoke:** `account-health-monitor` skill
**What they get:** 5-dimension health scorecard, specific users at risk, what changed
narrative, and recommended intervention actions.

### → Call Prep
**Signals:** "prep me for my call", "call prep for", "get me ready for my meeting",
"talking points for", "discovery questions for", "what should I ask", "objection
handling for", "how to handle objections with", "prep for my demo", "meeting in 30
minutes with [company]", "I have a call with [person]"
**Invoke:** `call-prep` skill
**What they get:** 60-second brief, account intelligence, recommended agenda, tailored
discovery questions (SPIN), objection handling table, data-backed talking points, attendee
profiles, case studies, and red flag watch list — all grounded in 360 intelligence.

### → Outreach Drafting
**Signals:** "draft outreach", "write an email to", "draft the next touch", "what should
I say to", "email to [person]", "email sequence for", "LinkedIn message for"
**Invoke:** `octave-outreach-drafter` skill
**What they get:** Full multi-channel engagement package: email sequences (cold/warm/inbound),
LinkedIn messages, call prep, internal talking points — all grounded in 360 account data.

### → Post-Meeting Follow-Up
**Signals:** "follow up", "recap email", "I just got off a call", "write a follow-up"
**Invoke:** `meeting-followup-generator` skill
**What they get:** Personalized follow-up email + structured action items from meeting.

### → Enrollment Check
**Signals:** "is [person] in a sequence", "check enrollment", "am I already emailing"
**Invoke:** `prospect-enrollment-check` skill
**What they get:** Sequence enrollment status + meeting history context.

### → Weekly Digest
**Signals:** "summarize my meetings", "what happened this week", "weekly digest"
**Invoke:** `weekly-meeting-digest` skill
**What they get:** Full week roll-up with themes, action items, accounts needing attention.

### → Daily Briefing (broad/multi-area requests)
**Signals:** "what should I focus on", "what needs my attention", "morning briefing",
"catch me up", "give me a rundown", "what's on my plate"
**Handle directly** using the Daily Briefing Flow below.

## Daily Briefing Flow

When a rep asks for a broad overview, produce a briefing that touches all areas with
enough depth to be actionable — then make it easy to drill deeper.

### Step 1 — Read all three sheet tabs

Load `sheet-schema.md`. Read the rep's Google Sheet (all three tabs).

Quick counts:
- **Deals**: Total count, total ARR, any with risk flags, any closing this week/next
- **Renewals**: Any within 60 days, any At Risk or Critical, total upcoming ARR
- **Prospects**: Total count, hot product leads (Channel=Product, Aero>70, Stage=Cold/Engaged),
  high-fit untouched (Aero>80, Cold, Tier 1), re-engage targets

### Step 2 — Check this week's calendar

Pull this week's calendar (Monday-Friday). Identify external customer meetings using
the domain exclusion logic from weekly-meeting-prep.

### Step 3 — Run quick Amplitude checks on flagged items

For any deal with risk flags or any meeting with an at-risk account, run a quick
Amplitude check (Layer 2A from the protocol): active users (30d) and WAU trend.
This adds the "product truth" layer to the sheet data.

For any hot product leads from the prospect tab, check active free user count.

### Step 4 — Produce the Daily Briefing

```
# Good morning — here's your day | [Date]

## 🗓️ Meetings Today
- **[Company]** — [time] | [X] active Mixmax users, WAU [trend] | [deal context if exists]
- **[Company]** — [time] | [context]
[If none: "No external meetings today."]

## 🔴 Deals Needing Attention ([count])
- **[Deal]** — $[ARR] | [Stage] | [Risk flag] | [X] active users, WAU [trend]
  → [One-line recommended action]
- **[Deal]** — $[ARR] | [Stage] | [Risk flag]
  → [Action]
[If none: "All deals tracking clean."]

## 🔄 Renewals Watch
- **[Account]** — $[ARR] | Renews [date] ([X] days) | [Health status]
  → [Action if At Risk]
[If none: "No urgent renewals."]

## 🔥 Hot Prospects
- **[Account]** — [Channel] | Aero [score] | [X] free users, [signal]
  → [One-line angle]
- **[Account]** — [Channel] | Aero [score] | [signal]
  → [Angle]
[If none: "No new hot leads this week."]

## ✅ Today's Top 5 Actions
1. **[Specific action]** — [Account/Deal] — [Why now: grounded in data]
2. **[Action]** — [Account/Deal] — [Why now]
3. **[Action]** — [Account/Deal] — [Why now]
4. **[Action]** — [Account/Deal] — [Why now]
5. **[Action]** — [Account/Deal] — [Why now]

---
*Go deeper:*
*"Review my deals" → full 360 on every deal*
*"Who should I go after?" → prospect intelligence with outreach angles*
*"Prep me for my call with [company]" → full meeting briefing*
*"How healthy is [domain]?" → Amplitude health diagnostic*
```

### Brevity Rules for Daily Briefing

The briefing is a 60-second scan that leads to action. Rules:
- Maximum 400 words total
- One line per item with the key data point and one recommended action
- The Amplitude quick-check (active users + WAU trend) appears on every flagged item —
  this is the minimum product truth layer
- The Top 5 Actions are the payoff. Everything above is evidence for them.
- End with drill-in prompts so the rep knows every line can become a full 360 deep dive

## Conversation Continuity

After routing to a skill, stay in the conversation. Common chains:

- Daily briefing → "tell me more about the Acme deal" → `deal-intelligence` (single deal)
- Deal review → "draft outreach to the champion" → `octave-outreach-drafter`
- Deal review → "prep me for my call with them" → `call-prep`
- Deal review → "is Jane in a sequence?" → `prospect-enrollment-check`
- Prospect finder → "draft outreach to #1" → `octave-outreach-drafter`
- Meeting prep → "write the follow-up" → `meeting-followup-generator`
- Meeting prep → "what questions should I ask?" → `call-prep`
- Any skill → "how healthy is [domain]?" → `account-health-monitor`
- Any skill → "prep me for my call with [company]" → `call-prep`

When routing a follow-up, pass the context from the prior skill output. If the rep says
"draft outreach to the champion on that deal" after a deal review, the outreach drafter
should already know who the champion is, what the deal context is, and what angle to use.

## When in Doubt

If intent is ambiguous, don't interrogate. Make your best guess, state what you're doing
("I'll pull your deal review — let me know if you meant something else"), and proceed.
Reps want speed and depth, not clarifying questions.
