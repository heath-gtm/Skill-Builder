---
name: prospect-finder
description: >
  Full 360-degree prospect intelligence for Mixmax AEs. Reads the Prospect Accounts tab,
  then runs the complete enrichment protocol on recommended targets: company research
  (Octave), Amplitude product usage deep dive (active free users, power users, feature
  adoption, conversion signals), Mixmax sequence/meeting history, contact enrichment with
  role mapping, and synthesized outreach angles grounded in real data. Trigger on: "who
  should I go after", "prospect recommendations", "find me accounts", "which accounts to
  target", "outbound targets", "inbound accounts", "product leads", "PQLs", "who's hot",
  "prospect prioritization", "new accounts", "cold accounts to re-engage", "pipeline
  creation", "who should I prospect", "accounts by channel", or any request to identify,
  prioritize, or recommend target accounts for outreach. Also trigger when a rep specifies
  a channel ("who should I go after in outbound", "any hot product leads").
---

# Prospect Finder

Full 360-degree prospect intelligence. Every recommended account gets the complete workup:
company research, product usage deep dive, contact enrichment, competitive landscape, and
a specific outreach angle grounded in all the data. The rep walks away with a ready-to-
execute target list, not a spreadsheet to stare at.

## References to Load

Before executing, load these references:
1. `references/sheet-schema.md` — column layout for the Prospect Accounts tab
2. `references/360-view-protocol.md` — the standard enrichment protocol (5 layers)
3. `references/octave-engagement-engine.md` — Octave tools for generating engagement materials

## Execution Flow

### Step 1 — Read the Prospect Accounts Tab & Map the Landscape

Read the Prospect Accounts tab from the rep's Google Sheet (URL in project instructions).
Parse all rows.

Produce the landscape map:
- Total prospect accounts
- By channel: Inbound / Outbound / Product / Expansion / Partner
- By GTM stage: Cold / Engaged / Meeting Set / Qualified / Disqualified
- By ICP tier: Tier 1 / Tier 2 / Tier 3
- Already in sequence (skip these for outreach recs)

### Step 2 — Score & Rank Every Account

Apply prioritization signals from the schema:

**Tier A — Go now (highest priority):**
- Hot product leads: Channel = Product AND Aero > 70 AND Stage = Cold/Engaged
- High-intent inbound: Channel = Inbound AND Last Activity Date < 7 days
- High-fit untouched: Aero > 80 AND Stage = Cold AND ICP = Tier 1

**Tier B — Go this week:**
- Re-engage targets: Last Activity > 30 days ago AND Stage = Engaged AND Not in sequence
- Mid-fit with signal: Aero 50-80 AND has a Product Usage Signal noted

**Tier C — Backlog:**
- Everything else not disqualified or already in sequence

**Skip entirely:**
- Sequence Enrolled = Yes (already in motion)
- Stage = Disqualified
- Stage = Meeting Set or Qualified (already progressing — not a prospecting target)

If the rep asks about a specific channel, filter to that channel before scoring.

### Step 3 — Run the 360-View Protocol on Top Prospects

Follow `references/360-view-protocol.md`. Depth:

**Full prospect list:** Every Tier A account gets Layers 1 + 2A-2C + 4A (company research +
active users + power users + feature adoption + contact identification).

**Top 5 prospects:** Get the FULL 5-layer protocol at maximum depth.

**Single prospect:** If the rep asks about one specific prospect, run all 5 layers.

#### Layer 1: Company Research (Octave)

For every Tier A prospect, use `enrich_company`:
- What they do, market position, company size, funding stage
- Recent news: funding rounds, leadership hires, product launches, layoffs
- Tech stack: are they using Mixmax competitors? Which ones?
- Industry and use case fit: why would they need Mixmax specifically?

**For outbound prospects:** Company research is your opening. "I saw you just raised
your Series B" or "Congrats on hiring a new Head of Revenue Ops" — this is how reps
sound like strategic partners instead of cold callers.

**For product prospects:** Company research gives context to the usage data. "A 400-person
SaaS company with 12 free users and growing" tells a different story than just "12 users."

#### Layer 2: Amplitude Product Usage Deep Dive

Run the full Amplitude query sequence for every Tier A prospect's domain:

1. **Active user census (30d)**: How many people are using Mixmax? Free or paid?
2. **Power user identification**: Top users by event count — names, emails, what they do.
   These are your warm contacts. A cold email to someone already using your product
   isn't really cold.
3. **Feature adoption matrix**: What are they using? Email tracking only? Full sequences?
   Calendar? Meeting Copilot? The features they USE tell you what they value. The features
   they DON'T use tell you what to demo.
4. **WAU trend**: Is their usage growing (great — ride the wave), stable (good — give them
   a reason to expand), or declining (act fast — they might be evaluating alternatives)?
5. **Conversion signals**: Hitting paid feature limits? Inviting new members? These are
   buying signals hiding in the data.

**Critical for Product channel:** This is the whole game. A product lead with 12 active
free users, 3 using sequences daily, and the Head of Rev Ops visiting the pricing page —
that's not a cold prospect. That's a warm deal waiting for a conversation.

Query construction:
- Filter: `gp:email contains [domain]`
- Exclude test users: `userdata_cohort is not vbyym9zo`
- NEVER leave Amplitude empty. Try 3+ query variations before reporting "no data."

#### Layer 3: Meeting & Sequence History (Mixmax)

**Meetings:**
1. `search_events` by domain — any past meetings or touches?
2. If meetings exist, pull the most recent summary — what was discussed? What happened?

**Sequences — CRITICAL for prospect prioritization:**
For every known contact at the prospect (from the sheet + Amplitude power users), use
`sequences` MCP with action `find_contact_in_sequences` to check enrollment status.

Then for any sequences with contacts from this account, use `get_sequence_insights`
to pull per-stage open/click/reply/bounce rates.

Produce the sequence read:
- **Currently enrolled:** [Name] in "[Sequence Name]" stage [X]/[Y] — [engagement status].
  If actively enrolled, the rep should NOT start a new sequence. Coordinate.
- **Previously sequenced:** [Name] went through "[Sequence Name]" — outcome: [replied at
  stage X / completed no reply / bounced / removed]. If they replied, what stage and
  subject line got the response? That's your proven angle.
- **Never sequenced:** Fresh contacts with no prior outreach — these are clean plays.
- **Channel that worked:** Based on reply data, this account responds to [angle/format].
- **Angles that failed:** [Sequence name] tried [approach] with zero engagement — don't
  repeat this.

**Why this matters:** A prospect who was sequenced 3 months ago and replied to the case
study email is NOT a cold prospect. A prospect who completed two sequences with zero
replies needs a fundamentally different approach, not the same playbook again. The
sequence history tells you whether to warm-touch, cold-touch, or try a completely
different door.

**Critical for Tier scoring:** If a prospect is currently enrolled in an active
sequence, they should be flagged as "in motion" and excluded from new outreach
recommendations unless the current sequence is failing.

#### Layer 4: Contact Intelligence

Build the target contact profile:

- **From sheet**: Key Contact, Title, Email (rep's starting point)
- **From Amplitude**: Power users at the domain — these may be better contacts than
  whoever the rep has listed. A power user who sends 500 tracked emails/month is more
  likely to champion than a VP who's never logged in.
- **From Octave**: `find_person` / `enrich_person` on the key contact — LinkedIn profile,
  tenure, background, role context. Also `find_person` to discover OTHER contacts at the
  company (look for sales leaders, rev ops, SDR managers).

For each identified contact:
- Name, title, email
- Engagement level: are they using Mixmax? How heavily?
- LinkedIn context: tenure (new hires = opportunity), background, connections
- **Recommended as primary target?** The best target is someone who (a) has authority
  or influence, (b) is already using the product or has a clear pain point, and
  (c) is reachable.

Produce the "Who to contact" ranking:
1. **Primary target** — the person most likely to convert. Usually the intersection of
   "has authority" and "already engaged with the product."
2. **Warm intro path** — if a power user exists, they can intro you up. Map this path.
3. **Backup contact** — if primary is unreachable, who's the alternative?

#### Layer 5: Synthesis — The Outreach Brief

For each top prospect, synthesize everything into an actionable outreach brief:

**The Opportunity** — one sentence: what makes this account worth pursuing right now?
Not "they have a high Aero score" but "400-person SaaS company with 12 active free
users, growing WAU, and a newly hired VP of Sales who needs to ramp an SDR team — 
they're ready for a paid conversation."

**The Angle** — the specific approach grounded in data:
- **For product leads**: Lead with their usage. "Your team sent 2,800 tracked emails
  last month through Mixmax — I'd love to show you how [feature they're not using]
  could save your SDRs 3 hours/week."
- **For outbound**: Lead with company research. "I saw you just brought on a new Head
  of Revenue Ops — when teams go through that transition, sequence automation usually
  becomes a priority."
- **For inbound**: Lead with their intent. "You checked out our pricing page and
  requested a demo — I pulled some data on how your team is already using Mixmax and
  I think there's a clear path to [specific value]."
- **For re-engage**: Lead with what changed. "When we last connected in February, you
  were evaluating tools. Since then, your team's Mixmax usage actually grew 40% — 
  seems like the product is sticking. Worth a fresh conversation?"

**The Action Plan**:
1. Specific email to send (or offer to draft via octave-outreach-drafter)
2. Who to send it to (primary target with reasoning)
3. Enrollment check (verify not already in a sequence)
4. Backup play if no response in 5 days

### Step 4 — Generate Engagement Materials (Octave)

For the top 5 Tier A prospects, generate ready-to-use engagement using the Octave
Engagement Engine. The rep shouldn't have to ask "now write the email" — it's already there.

#### Qualification Cross-Check
For each top prospect, run `qualify_company` with the domain to get an Octave-independent
ICP assessment alongside the Aero score from the sheet. If Octave's qualification diverges
significantly from Aero (e.g., Aero 85 but Octave says poor fit), surface the discrepancy.

#### Email Sequence per Prospect
For each of the top 5, generate an email sequence with `generate_email`. Match sequence
type to the prospect's channel:

| Channel | Sequence Type | Emails | Lead With |
|---------|--------------|--------|-----------|
| Product | WARM_OUTBOUND | 3 | Their usage data — "your team sent X tracked emails" |
| Inbound | INBOUND | 2 | Their intent signal — "you requested a demo" |
| Outbound | COLD_OUTBOUND | 4 | Company research — news, hiring, market context |
| Re-engage | WARM_OUTBOUND | 3 | What changed since last touch — usage growth, new hire |
| Expansion | CUSTOM | 2 | Existing relationship + new opportunity |

**Context injection:** Pack `allEmailsContext` with the full 360 intelligence from Steps 2-3:
Amplitude usage (user counts, power users, feature adoption, WAU trend), company research
(industry, size, news), meeting/sequence history, contact enrichment, and the specific
outreach angle from the synthesis.

**Per-step instructions:**
- Step 1: Lead with the primary angle (data-driven for product leads, research-driven for
  outbound, intent-driven for inbound)
- Step 2: Different value angle — reference a feature gap, case study, or peer comparison
- Step 3: ROI play grounded in their usage numbers, or break-up email
- Step 4 (cold only): Soft close with value offer

**allEmailsInstructions:** "Strategic partner tone. Lead with data that shows preparation.
Each email under 100 words. One CTA per email. Never pitch features without connecting
to their specific situation."

#### LinkedIn Messages
For the primary contact at each top prospect, generate a LinkedIn connection request
using `generate_content`:
- Instructions: "LinkedIn connection request. Under 300 characters. Reference one specific
  data point about their company or usage. Warm, peer-to-peer, no pitch."
- Inject person context + 360 data into `customContext`

#### CRM Context
For prospects with any prior CRM history, run `generate_crm_context` to pull the
relationship narrative. Inject into the outreach context.

#### Knowledge Base
`search_knowledge_base` for case studies matching each prospect's industry, company size,
or use case. Attach the strongest proof point to the outreach package.

#### Call Prep (for Meeting Set prospects)
For any Tier A prospect that already has a meeting scheduled (Stage = Meeting Set),
generate full call prep using `generate_call_prep` with the 360 context packed into
`meetingContext`.

### Step 5 — Produce the Prospect Brief

```
# Prospect Intelligence — [Rep Name] | Week of [Date]

## Landscape

| Channel | Total | Tier A (go now) | Tier B (this week) | In Sequence |
|---------|-------|-----------------|-------------------|-------------|
| Product | [X] | [X] | [X] | [X] |
| Inbound | [X] | [X] | [X] | [X] |
| Outbound | [X] | [X] | [X] | [X] |
| Expansion | [X] | [X] | [X] | [X] |

---

## 🔥 #1: [Account Name] — [Channel] | Aero: [Score] | [ICP Tier]

**Company:** [2-3 sentences — what they do, size, recent news, why they're a fit]

**Product usage:**
- [X] active users (30d), WAU [trend]
- Power users: [Name] ([X] events/mo, uses: sequences, email tracking), [Name] ([events/mo])
- Feature adoption: Heavy on [features]. Not using: [features] — demo opportunity
- Conversion signal: [hitting limits / inviting members / pricing page visits]

**Prior history:**
- Meetings: [Any prior meetings? Last one: date, topic, outcome]
- Sequences: [Who was sequenced? Which sequences? Reply at stage X / no reply / never touched]
- Best channel: [What messaging approach got engagement, if any]
- ⚠️ [Currently enrolled — coordinate / Previously failed — new angle needed / Clean slate]

**Who to contact:**
- Primary: [Name, Title] — [why them: power user + authority / new hire + pain fit]
- Warm intro: [Power user who can intro to primary]
- LinkedIn: [Key context — tenure, background]

**The opportunity:** [One sentence — the real story]

**The angle:** [Specific outreach approach grounded in data]

**Action plan:**
1. [Specific action — email, call, sequence]
2. [Follow-up play]

**Ready-to-use engagement (from Octave):**

📧 **Email sequence ([X] steps, [sequence type]):**

> **Email 1 — [Angle]**
> Subject: [subject line]
> [Full email body — ready to copy-paste]

> **Email 2 — [Angle]**
> Subject: [subject line]
> [Full email body]

> **Email 3 — [Angle]**
> Subject: [subject line]
> [Full email body]

💬 **LinkedIn connection request:**
> [Under 300 chars — personalized with data]

📋 **Proof point:** [Relevant case study from knowledge base]

🎯 **Octave qualification:** [ICP fit assessment — aligns with / diverges from Aero score]

---

## 🔥 #2: [Account Name] — [Channel] | Aero: [Score] | [ICP Tier]
[Same depth — full 360 + ready-to-use engagement]

---

[Continue for top 5]

---

## 🔄 Re-engage Targets

### [Account Name] — last touched [X] days ago | [Channel]
**What happened before:** [brief history from meetings/sequences]
**What's changed:** [new signal — usage growth, new hire, company news]
**New angle:** [specific re-approach]

---

## This Week's Prospecting Actions

1. **[Action]** — [Account] — [Why now, grounded in data]
2. **[Action]** — [Account] — [Why now]
3. **[Action]** — [Account] — [Why now]
4. **[Action]** — [Account] — [Why now]
5. **[Action]** — [Account] — [Why now]

---
*"Draft outreach to [person] at [company]" to generate a ready-to-send email*
*"Is [person] already in a sequence?" to check before sending*
```

## Writing Style

- Be opinionated. "Go after this account THIS WEEK because..." not "This account
  scores well on several dimensions."
- Every recommendation needs a specific person to contact, a specific angle, and a
  specific action. Not "consider reaching out" but "email Sarah Kim Tuesday morning
  with a usage-based value prop referencing their 2,800 tracked emails."
- Product usage data is ammunition. "Your team sent X emails" and "3 of your SDRs
  use sequences daily" give the rep something concrete to open with.
- Power users are warm contacts, not cold leads. Calling someone who already uses
  your product every day is fundamentally different from cold outreach. Frame it that way.
- If an account has zero Amplitude data and no meeting history, be honest: "This is a
  pure cold play — here's the company research angle, but there's no product signal yet."
- The Top 5 Prospecting Actions are the payoff. The rest is evidence.
