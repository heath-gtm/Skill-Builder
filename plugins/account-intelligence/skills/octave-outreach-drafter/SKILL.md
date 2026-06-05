---
name: octave-outreach-drafter
description: >
  Full messaging engine for Mixmax AEs. Generates personalized multi-channel engagement:
  email sequences (cold/warm/inbound), LinkedIn messages, call prep with discovery questions
  and objection handling, CRM context narratives, and playbook-aligned value propositions —
  all grounded in 360 account intelligence from Amplitude, Mixmax, and company research.
  Trigger on: "draft outreach", "write an email to", "email sequence for", "draft the
  next touch", "what should I say to", "LinkedIn message for", "messaging for", "write
  something to send", "turn this into outreach", "help me reach out", "cold email",
  "follow-up email", "re-engage email", "sequence for", or any request to create
  engagement messaging for a specific person or account. Also trigger after a deal review,
  prospect recommendation, or meeting prep when the rep says "now draft the email", "write
  the outreach", or "what should I send".
---

# Octave Outreach Drafter — Full Messaging Engine

Turns 360 account intelligence into ready-to-use, multi-channel engagement. Not just
one email — full sequences, LinkedIn messages, call prep, and playbook-aligned value
props, all grounded in real data.

## References to Load

Before executing, load:
1. `references/octave-engagement-engine.md` — the full Octave tool catalog and usage patterns

## Execution Flow

### Step 1 — Gather Context

Before generating any messaging, you need the full picture. Check what's already in the
conversation from a prior skill (deal review, prospect finder, meeting prep). If context
exists, use it. If not, build it.

**If coming from a prior skill output:**
Extract from the conversation: company domain, contact info, Amplitude usage data,
meeting history, deal context, risk flags, recommended angle.

**If standalone (rep just says "draft outreach to Sarah at Acme"):**
Run a mini 360-view:
1. `enrich_company` with the domain — company overview, news, size
2. `enrich_person` or `find_person` on the contact — LinkedIn, role, background
3. Quick Amplitude check — active users at domain, power user status, feature adoption
4. Quick Mixmax meeting check — `search_events` by domain for prior meetings
5. **Sequence check (MANDATORY):** Use `sequences` MCP with `find_contact_in_sequences`
   for the contact's email. If they're currently enrolled, STOP and warn the rep before
   generating new outreach. If previously sequenced, pull `get_sequence_insights` to see
   what worked and what didn't — use this to inform the messaging angle.
6. `generate_crm_context` — CRM narrative for relationship history

**Sequence intelligence feeds directly into messaging:**
- If a prior sequence got a reply at a specific stage, use that angle as the lead.
- If sequences completed with zero engagement, explicitly avoid those approaches.
- If the contact was previously sequenced by a different rep, reference the prior
  relationship: "Your team has been in touch with my colleague..."
- If currently enrolled, offer to update the existing sequence instead of creating a new one.

### Step 2 — Determine Engagement Type

Based on context, select the right approach:

| Situation | Sequence Type | Primary Channel | Supporting Channels |
|-----------|--------------|-----------------|-------------------|
| Cold prospect, no prior touch | COLD_OUTBOUND | Email (3-4 step) | LinkedIn connect |
| Product lead with free usage | WARM_OUTBOUND | Email (2-3 step) | LinkedIn message |
| Inbound demo request | INBOUND | Email (1-2 step) | Call prep |
| Re-engage (went dark 30+ days) | WARM_OUTBOUND | Email (2-3 step) | LinkedIn message |
| Active deal, next touch needed | CUSTOM | Email (1 step) | Call prep |
| Post-meeting follow-up | CUSTOM | Email (1 step) | — |
| Champion ask (need intro to EB) | CUSTOM | Email (1 step) | LinkedIn to EB |
| At-risk account, re-engagement | WARM_OUTBOUND | Email (2-3 step) | Call prep |

### Step 3 — Pull Playbook & Knowledge Base

Before generating, check for relevant resources:

1. **Check for saved email agents:** `list_agents` with type 'EMAIL'. If a relevant agent
   exists, use `run_email_agent` — agents carry institutional messaging knowledge.

2. **Check for saved call prep agents:** `list_agents` with type 'CALL_PREP'. Same logic.

3. **Search knowledge base:** `search_knowledge_base` for case studies, proof points, or
   competitive intel relevant to the account's industry, use case, or competitor situation.

4. **Check playbooks:** If you know the persona (from enrichment), check for relevant
   playbooks via `list_entities`. Pull value props with `list_value_props`.

### Step 4 — Generate Messaging

Construct the context string from the 360 view (see octave-engagement-engine.md for
the full template). Then generate:

#### A. Email Sequence (always)

Use `generate_email` or `run_email_agent`:

- Inject the full context string into `allEmailsContext`
- Set `allEmailsInstructions`: "Strategic partner tone. Lead with data that shows you
  understand their world. Each email under 100 words. Every email needs one clear CTA."
- Per-step instructions should vary the angle:
  - Step 1: Lead with the primary insight (usage data, company news, or meeting reference)
  - Step 2: Different angle (feature gap, peer comparison, case study)
  - Step 3: Value-forward (specific ROI or outcome based on their usage patterns)
  - Step 4: Break-up or soft close (if 4-step sequence)

#### B. LinkedIn Message (when contact has LinkedIn)

Use `generate_content`:
- Instructions: "LinkedIn connection request. Under 300 characters. Reference one specific
  data point. Warm, peer-to-peer, no pitch."
- Inject person context and 360 data into `customContext`

#### C. Call Prep (when a meeting exists or is being booked)

Use `generate_call_prep` or `run_call_prep_agent`:
- Pack `meetingContext` with the full 360 context + specific meeting objectives

#### D. Internal Talking Points (for ammo, not a send-ready message)

Use `generate_content`:
- Instructions: "Internal talking points. Bullet format. Opening hook, 3 value points
  grounded in usage data, anticipated objections with responses, close/next-step ask."

### Step 5 — Produce the Engagement Package

```
# Engagement Package — [Contact Name] at [Company]

## Context Snapshot
**Company:** [1-2 sentences — what they do, size, recent news]
**Product usage:** [X] active users, WAU [trend], power users: [names]
**Relationship:** [CRM/meeting summary — where do we stand?]
**Deal:** [stage, ARR, risk flags — if applicable]

---

## 📧 Email Sequence ([X] steps, [sequence type])

### Email 1 — [Angle: e.g., "Usage acknowledgment"]
**Subject:** [subject line]
**Body:**
[full email body from Octave]

### Email 2 — [Angle: e.g., "Feature gap"]
**Subject:** [subject line]
**Body:**
[full email body]

### Email 3 — [Angle: e.g., "ROI play"]
...

---

## 💬 LinkedIn Message
[connection request or InMail — under 300 chars]

---

## 📞 Call Prep (if meeting exists)
**Discovery Questions:**
[from generate_call_prep]

**Objection Handling:**
[from generate_call_prep]

**Talking Points:**
[key value points grounded in their data]

**Case Studies:**
[relevant case studies from knowledge base]

---

## 🎯 Engagement Strategy
**Primary play:** [the main angle and why]
**Sequence:** [what to send when — email day 1, LinkedIn day 2, follow-up day 5]
**Success signal:** [what response or action means it's working]
**If no response:** [pivot plan after sequence completes]

---

## Value Props for This Persona
[from playbook, if available — persona-specific value propositions]
```

## Engagement Quality Rules

- **Never send without context.** Every email must reference something specific — usage
  data, meeting history, company news, or a named person.
- **Match the tone to the relationship.** Cold = peer curiosity. Warm = strategic partner.
  Inbound = grateful + fast-track. Re-engage = "what's changed" with new angle.
- **Lead with THEIR data, not YOUR product.** "Your team sent 4,200 tracked emails last
  month" beats "Mixmax helps teams send more emails."
- **Every email gets one CTA.** Book a call, watch a video, reply with a time, forward
  to the right person. Not three asks.
- **Sequence spacing:** Cold: Day 1, 3, 7, 14. Warm: Day 1, 4, 10. Re-engage: Day 1, 5, 12.
- **LinkedIn supplements, never replaces.** LinkedIn message goes Day 2 after first email.
- **If Octave has a saved agent for this scenario, use it.** Always check `list_agents` first.
