---
name: call-prep
description: >
  Generate complete call preparation for any meeting: discovery questions tailored to the
  account's situation, objection handling based on competitive landscape and deal risk,
  talking points grounded in Amplitude usage data, person/company briefs, and relevant
  case studies — all powered by Octave's call prep engine plus 360 account intelligence.
  Trigger on: "prep me for my call", "call prep for", "get me ready for my meeting",
  "talking points for", "discovery questions for", "what should I ask", "objection
  handling for", "how to handle objections with", "prep for my demo", "prep for
  discovery", "meeting talking points", or any request to prepare for a specific
  upcoming conversation. Also trigger when a rep says "I have a call with [person] in
  an hour" or "meeting in 30 minutes with [company]" — these are urgent call prep requests.
---

# Call Prep — Full Meeting Preparation Engine

Generates comprehensive meeting preparation by combining 360 account intelligence with
Octave's call prep engine. The rep walks into every meeting knowing the account cold:
usage data, relationship history, the right questions to ask, how to handle objections,
and the specific value props that resonate with this persona.

## References to Load

Before executing, load:
1. `references/octave-engagement-engine.md` — Octave tool catalog, especially `generate_call_prep`
   and `run_call_prep_agent` sections

## Execution Flow

### Step 1 — Identify the Meeting & Contact

From the rep's request, extract:
- **Who:** Contact name, title, email, company, domain
- **When:** Meeting date/time (check calendar if needed)
- **What type:** Discovery, demo, follow-up, negotiation, QBR, save call
- **What's the goal:** What does the rep want to achieve?

If the rep is vague ("prep me for my Acme call"), check the calendar for the next
meeting with that account and pull attendee details.

### Step 2 — Build 360 Context

Run the full enrichment protocol. You need all of this for quality call prep:

**Company research (Octave):**
- `enrich_company` — company overview, news, size, funding, tech stack

**Product usage (Amplitude):**
- Active users (30d) with trend
- Power users by name — are any of them in this meeting?
- Feature adoption matrix — what they use heavily, what they don't
- WAU trend — growing, stable, or declining?

**Meeting history (Mixmax):**
- Prior meetings with this account — topics, commitments, open items
- Specifically: what was promised last time? What's unresolved?

**Sequence history (Mixmax):**
- For every meeting attendee, use `sequences` MCP with `find_contact_in_sequences`
- Check if any attendee has been sequenced — what worked, what didn't?
- If an attendee replied to a specific sequence stage, note the subject/angle that landed
  — reference this in the meeting to show continuity
- If an attendee was sequenced with zero engagement, know that going in — they may be
  skeptical or disengaged, and the rep should adjust their approach
- Channel responsiveness: which message types got opens/clicks/replies?

**Contact enrichment (Octave):**
- `enrich_person` on every attendee — role, background, LinkedIn, tenure
- Map each attendee's role: decision-maker, influencer, end user, blocker?

**CRM context (Octave):**
- `generate_crm_context` — deal history, activity notes, competitor mentions
- Include related contacts to see the full relationship map

**Knowledge base (Octave):**
- `search_knowledge_base` for case studies in their industry
- Relevant proof points for the topics likely to come up

### Step 3 — Generate Call Prep via Octave

First check for saved agents: `list_agents` with type 'CALL_PREP'. If a relevant
agent exists (e.g., "Discovery Call Prep", "Demo Prep"), use `run_call_prep_agent`.

Otherwise, use `generate_call_prep`:

```
generate_call_prep({
  person: {
    firstName: "[from enrichment]",
    lastName: "[from enrichment]",
    email: "[contact email]",
    title: "[from enrichment]",
    companyDomain: "[domain]",
    linkedInProfile: "[from enrichment]"
  },
  meetingContext: "[FULL 360 CONTEXT STRING — see template below]"
})
```

**Meeting context template:**

```
Meeting type: [discovery / demo / follow-up / negotiation / QBR / save call]
Meeting goal: [what the rep wants to achieve]

Company: [name] ([domain]) — [industry], [size], [recent news]

Product usage: [X] active users (30d), WAU [trend]. Power users: [names + activity].
Features heavily used: [list]. Features NOT used: [list].
Engagement trend: [growing/stable/declining] over [timeframe].

Deal context: [stage], $[ARR], [forecast category]. Days in stage: [X].
Champion: [name, title]. Economic buyer: [name, title].
Risk flags: [stalled, single-threaded, competitor, etc.]

Prior meetings: Last meeting [date] — [key topic].
Commitments made: [list].
Open action items: [list].
Must address: [top 3 items from meeting history].

Sequence history: [Name] was sequenced in "[Sequence Name]" — [replied at stage X
with subject "[subject]" / completed no reply / currently in stage X].
Channel responsiveness: [best-performing message type from sequence data].
Angles that worked: [subject lines/approaches that got engagement].
Angles that failed: [approaches with zero engagement — avoid repeating].

CRM notes: [synthesized narrative from generate_crm_context].

Attendees in this meeting:
- [Name, Title] — [role in deal, engagement level, product usage, sequence status]
- [Name, Title] — [role, engagement, usage, sequence status]

Competitive landscape: [competitor mentions from research/meetings].
```

### Step 4 — Enhance with Intelligence-Driven Prep

Octave produces great call prep. Now layer on the 360 intelligence to make it specific:

**Usage-based discovery questions:**
Take Octave's generic discovery questions and sharpen them with data:
- Generic: "How is your team handling email outreach?"
- Data-enhanced: "Your team sent 4,200 tracked emails last month through Mixmax — that's
  strong volume. Are the SDRs hitting their activity targets, or is there pressure to
  scale further?"

**Data-backed talking points:**
For every value point, attach the account's own numbers:
- Generic: "Mixmax saves teams time on sequences"
- Data-backed: "Alex Chen on your team runs 12 active sequences — if Meeting Copilot
  auto-generated his follow-ups, that's roughly 3 hours/week back."

**Meeting-history-aware objection handling:**
If prior meetings surfaced objections, address them proactively:
- "Last time, Jane mentioned concern about data privacy. Here's our updated SOC 2
  compliance documentation + the case study from [similar company]."

**Power-user leverage:**
If a meeting attendee is a power user in Amplitude, that's your ally:
- "Alex has 847 events/month — he's your internal proof point. Reference his workflows
  when talking to the VP."

### Step 5 — Produce the Call Prep Package

```
# Call Prep — [Company] | [Meeting Type] | [Date/Time]

## Meeting Overview
**Attendees:** [names, titles, roles in deal]
**Goal:** [what you're trying to achieve]
**Duration:** [if known]

---

## The 60-Second Brief
[3-4 sentences: who they are, where we stand, what matters in this meeting.
This is what the rep reads walking into the room.]

---

## 📊 Account Intelligence

**Product usage:** [X] active users, WAU [trend]
**Power users in this meeting:** [name — X events/mo, uses: features]
**Top feature gap:** [untouched feature = demo opportunity]
**Recent change:** [any notable shift in usage, new users, feature adoption]

**Deal status:** [stage, ARR, days in stage, risk flags]
**Last meeting:** [date] — [key outcome/commitment]
**Unresolved from last time:** [open items that need addressing]

---

## 🎯 Meeting Agenda (Recommended)

1. **Open** (2 min): [specific opener — reference their data or recent news]
2. **Address open items** (5 min): [prior commitments to resolve]
3. **Discovery / demo / discussion** (15-20 min): [the core of the meeting]
4. **Handle objections** (5 min): [anticipated objections with responses]
5. **Close / next steps** (3 min): [specific ask — what's the next milestone?]

---

## ❓ Discovery Questions (tailored to this account)

**Situation:**
[2-3 questions grounded in their current usage and company context]

**Pain:**
[2-3 questions exploring gaps identified in the feature adoption matrix]

**Impact:**
[2-3 questions connecting their usage patterns to business outcomes]

**Decision:**
[2-3 questions about timeline, process, and stakeholders]

---

## 🛡️ Objection Handling

| Likely Objection | Why They'd Say It | Response |
|-----------------|-------------------|----------|
| [objection 1] | [context from meetings/deal] | [data-backed response] |
| [objection 2] | [context] | [response with proof point] |
| [objection 3] | [context] | [response] |

---

## 💬 Talking Points (data-backed)

1. **[Value point]** — grounded in: [their specific usage data]
2. **[Value point]** — grounded in: [their specific pain from meetings]
3. **[Value point]** — grounded in: [competitive/market context]

---

## 👥 Attendee Profiles

### [Name] — [Title]
**Role in deal:** [Champion / EB / Influencer / End User / Unknown]
**Product engagement:** [active user? power user? never logged in?]
**Background:** [from enrichment — tenure, prior roles, LinkedIn]
**Approach:** [how to engage this specific person]

### [Name] — [Title]
...

---

## 📋 Case Studies & Proof Points
[from search_knowledge_base — relevant to their industry, size, use case]

---

## ⚠️ Watch For (Red Flags)
[things to listen for that signal risk: competitor mentions, budget hesitancy,
timeline push, stakeholder absence, enthusiasm drop]
```

## Quality Rules

- The 60-Second Brief is the most important section. It's what the rep reads 2 minutes
  before the call. Make it perfect.
- Discovery questions must reference their actual data. "How are you using sequences?"
  is lazy. "Your team has 12 active sequences — which ones are driving the most pipeline?"
  shows preparation.
- Objection handling should anticipate objections based on deal stage, prior meetings,
  and competitive landscape — not generic objections.
- Always identify which attendee is the power user in Amplitude. That person is your
  ally in the room.
- If this is a follow-up meeting, the first agenda item MUST be resolving prior commitments.
  Nothing kills trust faster than ignoring what you promised.
