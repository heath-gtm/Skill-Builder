# Briefing Template — Exact Output Format

Use this template for every customer briefing. Write in a conversational analyst voice — like
a smart RevOps person briefing a colleague over coffee. Use specific numbers, call out trends,
and make interpretive observations. Direct, opinionated, actionable.

---

## [Company Name] — Product Usage Summary

**Meeting:** [Title] | [Date/Time CT]
**Attendee(s):** [Names + emails]

---

### Company Background

[2-3 paragraph narrative from company research. Include what the company does, their business
model, how they make money, and the Mixmax fit analysis. This should read like a natural
briefing, not a data sheet.]

---

### Historical Meeting Context

**Meeting History:** [X] previous meetings found over the last [timeframe]. Last meeting was
[date]. Cadence: [pattern]. Other Mixmax attendees: [names].

**What's Been Discussed:**
[2-3 paragraph narrative synthesizing key topics, themes, and feature discussions from
historical meetings. Be specific: "Last time you spoke with them in [month], the conversation
centered on..." / "This has been a recurring theme across your last 3 meetings..."
Reference specific dates and topics.]

**Open Issues & Commitments:**
[Bullet each unresolved problem or open action item with context:]
- [Date] — Customer reported [issue]. Assigned to [person]. Status: [open/unknown/resolved].
- [Date] — Heath committed to [action]. Follow-up needed.
- [Date] — Customer asked about [feature/capability]. No resolution noted.

**Relationship Signal:**
[1-2 sentences on trajectory. Pull a verbatim quote from a summary/transcript if one is
particularly telling. E.g., "In the March 12 meeting, their VP of Sales said verbatim:
'We're looking at expanding to the whole team next quarter' — that's a strong signal worth
following up on."]

**⚠️ Top 3 Must-Address Items:**
1. [Most important unresolved issue/action item — with context]
2. [Biggest opportunity based on expressed interest]
3. [Relationship risk or commitment needing follow-through]

[If no historical meeting data is available, write: "No historical meeting data found in
Mixmax for this customer. This may be a first meeting, or Meeting Copilot may not have been
active for previous calls. Review email threads manually before the meeting."]

---

### Account Overview

**Account Size:** [X] active users in the last 30 days. Identified users include [list first
names with @domain shorthand, e.g., "eliza@, cathy@, marla@"], showing up to ~20 names then
"and more" if needed.

**User Trend:** [Narrative interpretation of WAU over the last 6 months — is it stable,
growing, declining? Call out specific recent weeks and what they suggest.]

### User Roster

| User | Profile | Emails (30d) | Seq. Emails | Seq. Activations | Tracking Views | Calendar |
|------|---------|--------------|-------------|------------------|----------------|----------|
| [user@] | [Power/Active/Light/Passive] | [count] | [count] | [count] | [count] | [count] |

Sort by emails sent descending. Include every user on the account.

**Profile breakdown:** [X] Power Users, [X] Active Users, [X] Light Users, [X] Passive/No Usage.

**Plan/Billing:** [State plan info if available. If not: "Plan and billing cycle data not
available in Amplitude — pull from Salesforce or Stripe before the meeting."]

---

### Email Volume

**Total emails sent:** [range per week over last 90 days]. [Narrative interpretation.]

**Sequence emails:** [range and pattern]. [Interpretation — steady-state vs. bursty,
campaign-driven vs. always-on, who's driving volume.]

**Sequence activations:** [X unique users per week]. [Interpretation — single power user
or distributed across team.]

---

### Feature Adoption (90-Day Uniques)

| Feature | Unique Users |
|---------|-------------|
| Email tracking (viewed details) | [count] |
| Templates (emails with template) | [count] |
| Sequence activations | [count] |
| Emails with calendar enhancements | [count] |
| Calendar meetings confirmed | [count] |
| Tasks completed | [count] |
| Rules/Automation activated | [count] |
| Meeting Copilot | [count] |

[Narrative interpretation. Calculate adoption percentages against active user count. Identify
anchor features vs. gaps. E.g.: "Email tracking is the anchor — 68 unique users, that's 85%
of their base. Sequences at 26 users (81%) is exceptional. But zero Rules adoption despite
high sequence volume is a missed opportunity."]

**Workspace expansion:** [X members added in 90 days — interpret growth trajectory.]

---

### Integrations

[Narrative on which third-party integrations are connected, excluding Google/Microsoft auth.
If zero: "Zero third-party integrations connected (excluding Google/Microsoft auth). No
Salesforce, no LinkedIn, no HubSpot, no Zoom, no Slack." If some exist, list them and
note what's missing.]

---

### Top 3 People to Reach Out To

**#1 — [Role label, e.g., "Highest-value champion"]**
**[Name]**
[2-3 sentences explaining WHY this person is the priority. Reference their specific data AND
any historical meeting participation. What makes them strategically important?]

**#2 — [Role label, e.g., "Expansion advocate"]**
**[Name]**
[2-3 sentences with data-backed reasoning. Include historical meeting context if available.]

**#3 — [Role label, e.g., "Underutilized potential"]**
**[Name]**
[2-3 sentences with data-backed reasoning.]

---

### Health Assessment

**Strengths:**
- [Each strength references specific data. E.g.:]
- Very stable, growing user base (32 active, trending up)
- High email volume (~1,000+/week)
- Exceptional sequence adoption (81% of users)
- Strong meeting engagement — X previous meetings over Y months shows active relationship

**Risks/Opportunities:**
- [Each risk explains WHY it matters + the opportunity. Incorporate historical context:]
- Zero integrations — biggest gap. No CRM means no activity sync, no sidebar, no LinkedIn.
  Major expansion and stickiness opportunity.
- Open action item from [date] still unresolved — customer raised [issue]. Risk of trust
  erosion if not followed up.
- No Tasks, Rules, or Meeting Copilot — three entire feature categories untouched.

---

### Recommended Conversation Angles

3 specific, data-driven angles. Each needs: a clear title, specific data reference, a
suggested opening line Heath can use naturally, and the strategic opportunity. **At least one
must tie back to historical meeting context.**

**1. [Angle Title]**
[2-3 sentences with data + suggested talk track in quotes. If tied to history: "Last time in
your March meeting, they mentioned X — this is your opening to..."]

**2. [Angle Title]**
[2-3 sentences.]

**3. [Angle Title]**
[2-3 sentences.]

---

### Bottom Line

[2-3 sentence synthesis of EVERYTHING — company context, historical relationship, product
health, key gaps, and the single most important thing Heath should know going in. This is
the "if you read nothing else, read this" paragraph. Must incorporate both product data AND
historical meeting intelligence to be forward-looking.]
