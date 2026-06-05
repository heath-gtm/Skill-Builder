---
name: deal-intelligence
description: >
  Full 360-degree deal intelligence for Mixmax AEs. Reads the Open Deals tab, then runs
  the complete enrichment protocol on every deal: company research (Octave), Amplitude
  product usage deep dive (active users, power users, feature adoption, WAU trends),
  Mixmax meeting history with commitments and open items, contact intelligence with
  engagement mapping, and synthesized verdicts with specific multi-step action plans.
  Trigger on: "review my deals", "how are my deals looking", "deal review", "what's at
  risk", "which deals need attention", "stuck deals", "deal health", "pipeline review",
  "how's my pipeline", "deal risk", "what's closing this month", "forecast review", or
  any request to assess, prioritize, or triage open opportunities. Also trigger when a
  rep names a specific deal or account in a deal context ("how's the Acme deal", "what's
  happening with the Datadog opp", "is the Stripe deal on track").
---

# Deal Intelligence

Full 360-degree deal review. Every deal the rep surfaces gets the complete workup:
company research, product usage deep dive, meeting history, contact intelligence, and
a synthesized verdict with specific next moves. The rep walks away knowing exactly
what's happening inside each account and what to do about it.

## References to Load

Before executing, load these references:
1. `references/sheet-schema.md` — column layout for the Open Deals tab
2. `references/360-view-protocol.md` — the standard enrichment protocol (5 layers)
3. `references/octave-engagement-engine.md` — Octave tools for generating engagement materials

The 360-view protocol gives you intelligence. The Octave engine turns it into action.

## Execution Flow

### Step 1 — Read the Open Deals Tab & Build the Pipeline Map

Read the Open Deals tab from the rep's Google Sheet (URL in project instructions).
Parse all rows into a structured deal list.

Produce the pipeline map:
- Total open deals, total pipeline ARR
- Deals by forecast category (Commit / Best Case / Pipeline / Omitted)
- Deals closing this month, next month
- Average days in stage across all deals

### Step 2 — Auto-Flag Risk Signals

For every deal, check derived risk signals:

- **Stalled**: Days in Stage > 21 AND not Closed Won/Lost
- **No champion access**: Champion Email is blank
- **Single-threaded**: No Economic Buyer listed
- **Slipping**: Close Date within 14 days AND stage is Discovery or Evaluation
- **Missing next step**: Next Step is blank AND not Closed Won/Lost
- **Pushed**: Rep flagged "Pushed close date" in Risk Flag column
- **Competitor threat**: Rep flagged "Competitor" in Risk Flag

Combine rep's manual Risk Flag with auto-detected signals. A deal can have multiple.

Rank deals by urgency: 🔴 (2+ flags or Commit with declining usage), 🟡 (1 flag),
🟢 (no flags + healthy signals).

### Step 3 — Run the 360-View Protocol on Each Deal

Follow the protocol in `references/360-view-protocol.md`. Depth depends on mode:

**Full pipeline review (all deals):**
- **Every deal** gets Layers 2A + 2D (active user count + WAU trend) and Layer 3A (meeting search)
- **Top 3 highest-risk or highest-ARR deals** get the FULL protocol — all 5 layers at maximum depth

**Single-deal review:**
- Run ALL 5 layers at full depth on the one deal. Leave nothing out.

#### Layer 1: Company Research (Octave)
For priority deals, use `enrich_company` with the domain. Pull company overview,
recent news, funding, leadership changes, competitive landscape. A rep who opens with
"I saw you just brought on a new CRO" sounds like a partner. Don't skip this.

#### Layer 2: Amplitude Product Usage Deep Dive
For every deal's domain, run the Amplitude query sequence from the protocol:

1. **Active user census**: Total active users (30d) vs prior 30d → growth/decline %
2. **Power user identification**: Top users by event count — names, emails, primary features.
   These are your champions, expansion advocates, and churn canaries.
3. **Feature adoption matrix**: For each feature category (email tracking, sequences,
   templates, calendar, Meeting Copilot, tasks, rules) — user count, % adoption, trend.
   Highlight the top feature gap (highest-value untouched feature).
4. **WAU trend (12 weeks)**: Growing / stable / declining / churning
5. **Expansion signals**: New workspace members, feature breadth expanding, paid feature
   usage on free plan

Query construction:
- Filter: `gp:email contains [domain]`
- Exclude test users: `userdata_cohort is not vbyym9zo`
- If zero results, try domain variations (see protocol for fallback sequence)
- NEVER leave Amplitude empty. Try 3+ query variations before reporting "no data."

**Critical insight for deals:** If Amplitude shows declining usage on a Commit or Best Case
deal, that's the #1 risk signal. A deal can't be "Commit" if the product champions are
going dark. Surface this directly.

#### Layer 3: Mixmax Meeting & Sequence Intelligence

**Meetings:**
1. `search_events` with the domain
2. `search_meeting_summaries` with champion/contact emails
3. For the 3 most recent meetings, pull full summaries

Extract and synthesize:
- Last meeting date and topic
- Key discussion points across all meetings
- **Commitments made** by either side — what was promised?
- **Open action items** — what's unresolved?
- **Pain points** the customer articulated
- **Competitive mentions** — did they name alternatives?
- **Buying signals** — timeline mentions, budget discussions, stakeholder intros
- **Red flags** — missed meetings, declining attendance, vague next steps

**Sequences:**
For every known contact at the deal (Champion, EB, power users from Amplitude, meeting
attendees), use `sequences` MCP with action `find_contact_in_sequences`:
- Check which sequences each contact is currently enrolled in or has completed
- For active sequences, note the stage they're on and enrollment date

For each sequence with contacts from this deal, use `sequences` MCP with action
`get_sequence_insights` to pull per-stage performance:
- Open rate, click rate, reply rate, bounce rate per stage
- Which stage(s) generated replies — this tells you what messaging resonated
- Drop-off points — where engagement died

Produce the sequence read for the deal:
- **Active enrollments:** Who is currently in what sequence, what stage, what's the engagement?
- **Past sequences:** What was tried, did it work, which angle got a response?
- **Channel responsiveness:** Based on stage types and reply patterns, what channels
  and messaging approaches work with this account?
- **Sequence conflicts:** If the deal is active AND contacts are in unrelated sequences,
  flag it — the rep needs to coordinate.
- **Never sequenced:** Contacts with no sequence history — fresh engagement opportunities.

**Critical deal signal:** If a Commit or Best Case deal has contacts enrolled in sequences
with zero replies across multiple stages, the deal may be more at risk than the forecast
suggests. Surface this alongside Amplitude declining usage as a compound risk signal.

Identify the **top 3 must-address items** before the next interaction (from meetings
AND sequences combined).

#### Layer 4: Contact Intelligence
Build the people map from all sources:

- **From sheet**: Champion, Economic Buyer (named by the rep)
- **From Amplitude**: Power users (highest event counts) — these may be champions
  the rep doesn't know about yet
- **From Mixmax**: Meeting attendees, speakers from transcripts
- **From Octave**: `enrich_person` on champion and EB — LinkedIn, role, tenure

For each key person:
- Name, title, email
- Role in the deal (Champion? Blocker? EB? End User? Power User?)
- Engagement level (active in product? attending meetings? responding to emails?)
- Recommended approach — what to say to THIS person based on their role and data

Produce the engagement map:
1. **Must engage** — the person whose action moves the deal forward
2. **Should engage** — supporters who amplify internally (often Amplitude power users)
3. **Watch** — stakeholders who could block if ignored

#### Layer 5: Synthesis & Verdict
For each deal, synthesize all four layers into:

**The Verdict** — one sentence capturing the real story. Not "they have 15 active
users" but "Champion is engaged and usage is growing, but you're single-threaded —
the new VP of Sales (hired 3 weeks ago) hasn't been brought in yet and she controls
budget."

**The Action Plan** — 3-5 specific, sequenced actions:
1. "Email Alex Chen (power user, 847 events/month) Tuesday — reference the workflow
   automation they built in Q1 and ask for 15 minutes to show Meeting Copilot"
2. "Ask Alex to intro you to the new VP of Sales, Sarah Kim (hired March 15 per
   LinkedIn) — this is your multi-threading play to de-risk the single-thread flag"
3. "Send the ROI deck Wednesday with personalized data: their team sent 4,200
   tracked emails last month and booked 18 meetings via scheduling links"

**The Outreach Angle** — if a touch is needed, provide the specific angle: what to
reference (usage data, meeting commitments, company news), what to offer, what tone.

### Step 4 — Generate Engagement Materials (Octave)

For the top 3 priority deals (🔴 first, then highest ARR 🟡), generate ready-to-use
engagement materials using the Octave Engagement Engine:

#### CRM Context Pull
For each priority deal, run `generate_crm_context`:
- `companyDomain`: the deal's domain
- `objective`: "Deal review — assessing deal health and planning next engagement"
- `guidance`: "Focus on deal progression, recent activity, competitor mentions, and any
  internal notes about risk or blockers"
- `includeRelatedContacts`: true

#### Draft Next Touch
For the #1 recommended action on each priority deal, generate the actual message:

**If the action is "email the champion":**
Use `generate_email` with WARM_OUTBOUND, 1 email, full 360 context in `allEmailsContext`.

**If the action is "reach out to a new stakeholder" (multi-threading):**
Use `generate_email` with COLD_OUTBOUND, 2-3 emails. Inject context about the existing
relationship: "Your colleague [champion] and I have been discussing [topic]..."

**If the next meeting is scheduled:**
Use `generate_call_prep` with the full 360 context packed into `meetingContext`.

**If the rep needs talking points (not a send-ready email):**
Use `generate_content` with instructions for internal talking points.

#### Knowledge Base & Playbook Check
- `search_knowledge_base` for case studies matching the deal's industry/use case
- Check for relevant playbooks: `list_entities` for playbooks, then `list_value_props`
  for persona-specific messaging

#### Qualification Cross-Check
For deals where the rep's data seems optimistic (Commit but usage declining, Best Case
but single-threaded), run `qualify_company` to get an Octave-independent assessment.

### Step 5 — Produce the Deal Review Output

```
# Deal Review — [Rep Name] | [Date]

## Pipeline Summary

| Metric | Value |
|--------|-------|
| Total Open Deals | [X] |
| Total Pipeline ARR | $[X] |
| Commit | $[X] ([N] deals) |
| Best Case | $[X] ([N] deals) |
| Pipeline | $[X] ([N] deals) |
| Closing This Month | [X] deals, $[ARR] |

---

## 🔴 [Deal Name] — $[ARR] | [Stage] | Close: [Date]

**Risk signals:** [Stalled 23 days, Single-threaded — no EB listed]

**Company context:** [1-2 sentences from Octave — what they do, recent news, size]

**Product usage:**
- [X] active users (30d), [trend] from [Y] prior period
- Power users: [Name] ([X] events/mo, primary: sequences), [Name] ([X] events/mo, primary: email tracking)
- Feature adoption: Heavy on [features]. Gap: [untouched feature] — conversation starter
- WAU trend: [Growing/Stable/Declining] over 12 weeks

**Meeting history:**
- Last meeting: [date] — [topic]
- Key commitment: [what was promised by whom]
- Open items: [unresolved action items]
- Must address: [top item that can't wait]

**Sequence history:**
- Active: [Name] in "[Sequence Name]" — stage [X]/[Y], [open/reply status]
- Past: [Name] completed "[Sequence Name]" — [replied at stage X / no reply]
- Best channel: [email/LinkedIn/phone based on reply patterns]
- ⚠️ [Conflict/overlap warning if applicable]

**People map:**
- Champion: [Name, Title] — [engagement status]
- Must engage: [Name, Title] — [why and what to say]
- Power user not in deal: [Name] — [opportunity to bring them in]

**Verdict:** [One sentence — the real story]

**Action plan:**
1. [Specific action with person, timing, and message]
2. [Specific action]
3. [Specific action]

**Ready-to-use engagement (from Octave):**

📧 **Draft email to [champion/stakeholder]:**
> Subject: [subject line]
> [Full email body — ready to copy-paste and send]

📞 **Call prep for next meeting (if scheduled):**
> Key questions: [2-3 discovery questions tailored to this deal's situation]
> Objection to expect: [most likely objection + data-backed response]

📋 **Proof point:** [relevant case study from knowledge base]

---

## 🟡 [Deal Name] — $[ARR] | [Stage] | Close: [Date]
[Same structure, slightly condensed for Watch deals]

---

## 🟢 [Deal Name] — $[ARR] | [Stage] | Close: [Date]
**Why it's on track:** [brief — healthy usage, recent meeting, clear next step]
**Keep momentum:** [one specific action]

---

## This Week's Top 5 Actions (across all deals)

1. **[Action]** — [Deal Name] — [Why now, grounded in data]
2. **[Action]** — [Deal Name] — [Why now]
3. **[Action]** — [Deal Name] — [Why now]
4. **[Action]** — [Deal Name] — [Why now]
5. **[Action]** — [Deal Name] — [Why now]
```

## Writing Style

- Lead with the verdict, not the data. The data exists to support the verdict.
- Every deal MUST end with specific, named, timed actions — not "follow up" but
  "email Jane Smith by Wednesday with the ROI deck, then ask her to intro you to
  the VP of Sales by Friday"
- Use real names from Amplitude, meetings, and enrichment. "Your power user Alex Chen"
  not "a power user at the account."
- If Amplitude shows declining usage on a Commit deal, say so directly and urgently.
  This is the single biggest disconnect in any pipeline.
- Reference specific product usage in recommendations: "They sent 4,200 tracked emails
  last month" gives the rep ammunition for conversations.
- The Top 5 Actions are the most important section. Everything above builds the case
  for these actions.
