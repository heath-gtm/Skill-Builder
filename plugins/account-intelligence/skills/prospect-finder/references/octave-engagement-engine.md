# Octave Engagement Engine — Reference

The complete toolkit for turning 360 intelligence into ready-to-use rep actions.
Every skill that produces engagement recommendations should use these tools.

---

## Tool Catalog

### 1. Email Sequences — `generate_email`

Generates 1-4 step personalized email sequences. This is not a template filler —
Octave uses its knowledge base (your product, personas, playbooks, proof points) to
craft contextual messaging.

**Parameters:**
- `person` (required): firstName, lastName, email, title, companyName, companyDomain, linkedInProfile
- `sequenceType`: COLD_OUTBOUND (default), WARM_OUTBOUND, INBOUND, CUSTOM
- `numEmails`: 1-4 (default 4)
- `allEmailsContext`: Context for ALL emails — THIS IS WHERE YOU INJECT 360 INTELLIGENCE
- `allEmailsInstructions`: Tone, format, length guidance for all emails
- `step1Context` through `step4Context`: Per-email context
- `step1Instructions` through `step4Instructions`: Per-email instructions

**How to inject 360 intelligence:**
Pass the synthesized account context into `allEmailsContext`. Include:
- Amplitude usage data: "They have 15 active users, 3 power users using sequences daily, WAU growing 12%"
- Meeting history: "Last meeting April 10 — discussed workflow automation, committed to ROI review"
- Company research: "Just raised Series C, hired new VP of Sales last month"
- Deal context: "In Evaluation stage, $48K ARR, champion is Jane Smith"

**Sequence type selection:**
- `COLD_OUTBOUND`: First-time outreach, no prior relationship
- `WARM_OUTBOUND`: Re-engage, follow-up on past interaction, product lead with usage
- `INBOUND`: Responding to inbound demo request or content download
- `CUSTOM`: Any other context (specify in instructions)

**Example call:**
```
generate_email({
  person: {
    firstName: "Sarah",
    lastName: "Kim",
    email: "sarah@gammatech.com",
    title: "Head of Revenue Ops",
    companyDomain: "gammatech.com"
  },
  sequenceType: "WARM_OUTBOUND",
  numEmails: 3,
  allEmailsContext: "Gamma Tech has 12 active free users on Mixmax. 3 use sequences daily. Sarah visited the pricing page 3x this month. Their team sent 2,800 tracked emails last month. WAU is growing 15%. They're a 450-person SaaS company that just hired a new VP of Sales.",
  allEmailsInstructions: "Strategic partner tone. Lead with their usage data. Reference the pricing page visits as a signal. Each email should be under 100 words. CTA: book a 15-minute call to show how paid features would help their SDR team.",
  step1Context: "First touch. Lead with usage acknowledgment.",
  step2Context: "Follow-up. Reference a specific feature they're not using (Meeting Copilot).",
  step3Context: "Break-up style. Give a concrete ROI number based on their volume."
})
```

### 2. Saved Email Agents — `run_email_agent`

Run pre-configured email agents your team has built in Octave. These agents have
built-in personas, playbooks, and writing styles.

**Parameters:**
- `agent` (required): Agent name or oId. Use `list_agents` with type 'EMAIL' to discover available agents.
- `person`: Same as generate_email
- `allEmailsContext`, per-step context/instructions: Same as generate_email

**When to use:** When the team has a proven agent for the use case. Check `list_agents`
first. If a relevant agent exists, prefer it over raw `generate_email` — agents carry
institutional knowledge.

### 3. Call Prep — `generate_call_prep`

Generates comprehensive call preparation: discovery questions, person/company briefs,
objection handling, and relevant case studies from the Octave knowledge base.

**Parameters:**
- `person` (required): firstName, lastName, email, title, companyDomain, companyName, linkedInProfile
- `meetingContext`: Meeting type (discovery/demo/follow-up), topics, previous conversations, special considerations

**How to inject 360 intelligence:**
Pack the `meetingContext` with everything from the 360 view:
- Amplitude data: user counts, feature adoption, power users, trends
- Meeting history: prior commitments, pain points, open items
- Deal context: stage, ARR, risk flags, champion status
- Company research: recent news, competitive landscape

**Example call:**
```
generate_call_prep({
  person: {
    firstName: "Jane",
    lastName: "Smith",
    email: "jane@acme.com",
    title: "Director of Sales Ops",
    companyDomain: "acme.com"
  },
  meetingContext: "Follow-up meeting. Jane is our champion on a $48K deal in Evaluation stage. Last meeting (April 10): discussed workflow automation and committed to ROI review. Their team has 22 active users, WAU stable. Power user Alex Chen sends 500+ tracked emails/month. They're NOT using Meeting Copilot or Rules — demo opportunities. Risk: single-threaded through Jane only, no EB engagement. The economic buyer is John Doe (VP Sales). We need Jane to introduce us to John this meeting."
})
```

### 4. Saved Call Prep Agents — `run_call_prep_agent`

Run pre-configured call prep agents. Use `list_agents` with type 'CALL_PREP' to discover.

### 5. Content Generation — `generate_content`

Generates any content type: LinkedIn messages, intro paragraphs, talking points,
one-pagers, custom content. The Swiss Army knife.

**Parameters:**
- `instructions` (required): What to generate — be specific about type, tone, length, key points
- `person` (optional): For personalization
- `company` (optional): For account-based content
- `customContext`: Additional context (360 intelligence goes here)
- `url`: Optional URL to scrape for additional context

**Best use cases:**
- LinkedIn connection request messages (personalized with usage data)
- Internal briefing notes for managers
- One-pagers for specific accounts
- Talking points for specific personas
- Competitive battle cards for specific accounts

**Example — LinkedIn message:**
```
generate_content({
  instructions: "Write a LinkedIn connection request message. Under 300 characters. Reference their Mixmax usage without being creepy. Warm, peer-to-peer tone.",
  person: {
    firstName: "Alex",
    lastName: "Chen",
    title: "SDR Manager",
    companyDomain: "acme.com"
  },
  customContext: "Alex is a Mixmax power user — 847 events/month, primarily sequences and email tracking. We have no direct relationship yet but his colleague Jane Smith is our champion on a $48K deal. We want Alex as a second thread into the account."
})
```

### 6. CRM Context — `generate_crm_context`

Synthesizes a narrative from CRM data (Salesforce/HubSpot). Pulls contact info,
account details, deal/opportunity status, and activity history, then produces a
contextual summary.

**Parameters:**
- Identification: `email`, `firstName`/`lastName` + `companyDomain`, or explicit CRM record IDs
- `objective`: Why you need this context (e.g., "call prep", "deal review", "outreach planning")
- `guidance`: What to focus on (e.g., "focus on recent deal activity and competitor mentions")
- `includeRelatedContacts`: Pull in other contacts at the account
- `activityLookbackDays`: How far back to look (default 90)

**When to use:** Before generating any outreach or call prep. The CRM context gives
you the relationship history that Amplitude and Mixmax don't capture — internal notes,
call logs, email exchanges, deal progression.

**Example:**
```
generate_crm_context({
  companyDomain: "acme.com",
  objective: "Preparing for deal review and next outreach",
  guidance: "Focus on deal progression, competitor mentions, and any commitments logged in notes. Flag if there are contacts we're not engaging.",
  includeRelatedContacts: true,
  activityLookbackDays: 180
})
```

### 7. Playbooks & Value Props — `get_playbook` + `list_value_props`

Retrieve persona-specific messaging playbooks with value propositions, objection
handling, and discovery frameworks.

**`get_playbook`:** Retrieves a full playbook with linked personas and value props.
**`list_value_props`:** Lists value props for a playbook, grouped by persona.

**When to use:** Before drafting outreach, check if there's a relevant playbook.
Playbooks contain tested messaging that aligns with the team's positioning.

Use `list_entities` with type filtering to find available playbooks, then `get_playbook`
to retrieve the full content.

### 8. Knowledge Base — `search_knowledge_base`

Search Octave's knowledge base for relevant case studies, proof points, competitive
intelligence, and reference materials.

**When to use:** When crafting outreach for a specific industry, use case, or
competitive situation. The knowledge base contains the evidence that makes messaging
credible.

### 9. Qualification — `qualify_company` + `qualify_person`

Score how well a company or person matches your ICP.

**When to use:** During prospect prioritization. Adds an Octave qualification score
alongside the Aero fit score from the sheet.

---

## Engagement Playbook — How Skills Should Use These Tools

### For Deal Intelligence (after 360 view):

1. `generate_crm_context` — pull CRM narrative for the deal
2. `search_knowledge_base` — find relevant case studies for the account's industry/use case
3. For each recommended action involving outreach:
   - `generate_email` with WARM_OUTBOUND + full 360 context → draft email to champion
   - `generate_content` → talking points for the next conversation
   - If a meeting is coming up: `generate_call_prep` with full context

### For Prospect Finder (after 360 view):

1. `qualify_company` — get Octave qualification alongside Aero score
2. For each top prospect:
   - `generate_email` with sequence type based on channel:
     - Product leads → WARM_OUTBOUND (they're already using the product)
     - Inbound → INBOUND
     - Outbound → COLD_OUTBOUND
     - Re-engage → WARM_OUTBOUND
   - `generate_content` → LinkedIn connection message for the primary contact
   - If Meeting Set: `generate_call_prep` for the upcoming meeting

### For Meeting Prep (after 360 view):

1. `generate_crm_context` — CRM narrative for the account
2. `generate_call_prep` — full call prep with discovery questions, objection handling
3. `search_knowledge_base` — relevant proof points for the meeting topics
4. `generate_content` → pre-meeting email to attendees (agenda-setting touch)

### For Account Health (after health assessment):

1. If intervention needed:
   - `generate_email` with WARM_OUTBOUND → re-engagement email to at-risk users
   - `generate_content` → internal escalation brief for the CSM/manager
   - `generate_call_prep` → prep for a save conversation

---

## Context Injection Formula

The key to great Octave output is rich context. For every Octave call, construct the
context string from the 360 view:

```
CONTEXT TEMPLATE:

Company: [name] ([domain]) — [industry], [employee count] employees
Recent news: [funding, hires, product launches]
Mixmax usage: [X] active users (30d), WAU [trend]. Power users: [names + activity].
Features used: [list]. Features NOT used: [list] — demo opportunity.
Deal context: [stage], $[ARR], [forecast category]. Champion: [name]. EB: [name].
Risk: [flags].
Meeting history: Last meeting [date] — [topic]. Commitments: [list]. Open items: [list].
Sequence history: [Name] was in "[Sequence Name]" — [replied at stage X / no reply].
  Best-performing angle: [subject/approach that got engagement].
  Angles that failed: [approaches with zero engagement — AVOID these in new messaging].
  Channel responsiveness: [email/LinkedIn/phone based on reply patterns].
  Currently enrolled: [yes/no — if yes, coordinate, don't duplicate].
CRM context: [synthesized narrative from generate_crm_context]
Competitive intel: [any competitor mentions from meetings or research]
```

Pack this into `allEmailsContext`, `meetingContext`, or `customContext` depending on
which Octave tool you're calling. The richer the context, the better the output.
