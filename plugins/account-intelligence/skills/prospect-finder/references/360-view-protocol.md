# 360-View Protocol — Standard Account Enrichment

Every skill in Account Intelligence follows this protocol when analyzing an account.
The sheet gives you the "what." This protocol gives you the "so what." Run all five
layers for every account you surface to the rep.

---

## Layer 1: Company Research (Octave)

Use `enrich_company` with the domain. Extract:

- **Company overview**: What they do, market position, recent news
- **Size & segment**: Employee count, estimated revenue, funding stage
- **Tech stack signals**: What tools they use (competitors? complements?)
- **Recent news**: Funding rounds, leadership changes, product launches, layoffs
- **Competitive landscape**: Are they using or evaluating Mixmax competitors?

If Octave returns thin data, supplement with `find_company` for additional context.

**Why this matters for reps:** A rep who opens with "I saw you just raised your Series C"
or "Congrats on the new VP of Sales hire" sounds like a strategic partner. A rep who opens
with "I noticed you're on our free plan" sounds like a salesperson.

---

## Layer 2: Product Usage Deep Dive (Amplitude)

All queries use project ID `130895`. Filter by `gp:email contains [domain]`.
Exclude test users: `userdata_cohort is not vbyym9zo`.

### 2A: Active User Census (30-day)

Query: Count unique users active in last 30 days at this domain.

Report:
- **Total active users (30d)**
- **Total active users (prior 30d)** — for trend
- **Growth/decline %** — the single most important health signal

### 2B: Power User Identification

Query: Top users by total event count in last 30 days at this domain.

For each power user, capture:
- **Name / email**
- **Total events (30d)** — proxy for engagement depth
- **Primary features used** — what they do most in Mixmax
- **Role inference** — from email prefix, title if available, or feature patterns
  (e.g., heavy sequence user = likely SDR/BDR, heavy calendar user = likely AE)

**Why this matters:** Power users are your best champions, expansion advocates, and
churn canaries. If a power user goes dark, that's a red flag. If a non-user at the
same account starts showing up, that's an expansion signal.

### 2C: Feature Adoption Matrix

Query: For each feature category, count unique users at this domain (30d).

Feature categories:
- **Email tracking** (opens, clicks, link tracking)
- **Sequences** (sequence sends, sequence activations)
- **Templates** (template usage, template creation)
- **Calendar** (scheduling links, availability)
- **Meeting Copilot** (meeting recordings, summaries)
- **Tasks** (task creation, task completion)
- **Rules** (automation rules, triggers)

Report as a matrix:
| Feature | Users (30d) | % of Active Users | Trend (vs prior 30d) |
|---------|-------------|-------------------|---------------------|

Highlight:
- **Heavily adopted** (>60% of users): This is sticky. Reference in outreach.
- **Partially adopted** (20-60%): Expansion opportunity — who's using it and who isn't?
- **Untouched** (<20% or 0): Either they don't need it or they don't know about it.
  The "top feature gap" — the highest-value untouched feature — is a conversation starter.

### 2D: Engagement Trend (60-90 day view)

Query: Weekly active users over the last 12 weeks at this domain.

Classify the trend:
- **Growing**: WAU up >10% over 60d — healthy, lean into expansion
- **Stable**: WAU flat (±10%) — okay but watch for plateau
- **Declining**: WAU down >10% — intervention needed, find out why
- **Churning**: WAU down >25% or multiple power users dropped — escalate

### 2E: Conversion & Expansion Signals

Query: New workspace members added in last 30 days at this domain.

- **New users appearing**: Organic growth signal — someone invited them
- **Feature breadth expanding**: Users trying new features = deepening investment
- **Paid feature usage on free plan**: They're hitting limits — conversion opportunity

### Amplitude Query Sequence (follow this order)

1. Start with `query_amplitude_data` — simple active user count by domain
2. If that returns data, run the power user query (top users by event count)
3. Then feature adoption matrix (events grouped by feature category)
4. Then 12-week WAU trend
5. If step 1 returns zero, try domain variations:
   - Try without subdomain (e.g., `company.com` instead of `app.company.com`)
   - Try `gp:domain` filter instead of `gp:email contains`
   - Try `get_users` to find any users at the domain
6. Only report "no Amplitude data" after 3+ query attempts

---

## Layer 3: Meeting & Sequence Intelligence (Mixmax)

### 3A: Search for meetings

1. `search_events` with the domain — finds all Mixmax events related to the account
2. `search_meeting_summaries` with attendee emails — finds summarized meetings
3. For the 3 most recent/important meetings, pull full summaries with `get_meeting_summary`

### 3B: Synthesize meeting history

From the meeting data, extract:
- **Last meeting date** and topic
- **Key discussion points** across all meetings — what keeps coming up?
- **Commitments made** (by either side) — what was promised?
- **Open action items** — what's unresolved?
- **Pain points expressed** — what problems did the customer articulate?
- **Competitive mentions** — did they name any competitors?
- **Buying signals** — timeline mentions, budget discussions, stakeholder introductions
- **Red flags** — missed meetings, declining attendance, vague next steps

### 3C: Sequence Intelligence

Check whether anyone at the account has been or is currently being sequenced. This
tells you what outreach has already been attempted, what worked, and what didn't.

**Step 1 — Find enrolled contacts:**
For every known contact at the domain (from the sheet, Amplitude power users, meeting
attendees), run `find_contact_in_sequences` with their email. This returns:
- Which sequences they're currently enrolled in (active)
- Which sequences they've completed or been removed from (past)
- Their enrollment status per sequence

**Step 2 — Pull sequence performance:**
For each sequence that has contacts from this account, run `get_sequence_insights` with
the sequenceId. Extract per-stage metrics:
- **Open rate** per stage — are they reading?
- **Click rate** per stage — are they engaging with content?
- **Reply rate** per stage — did they respond? Which stage got the reply?
- **Bounce rate** — are the email addresses valid?
- **Drop-off point** — at which stage do recipients stop engaging?

**Step 3 — Synthesize sequence history:**
Produce the sequence read:

- **Currently in sequence:** [Name] enrolled in "[Sequence Name]" — stage [X] of [Y],
  last activity: [date]. Open rate: [X]%, reply rate: [X]%.
- **Previously sequenced:** [Name] completed "[Sequence Name]" — [outcome: replied /
  completed no reply / removed]. Best-performing stage: [stage X] with [X]% reply rate.
- **Never sequenced:** [Names] — no prior sequence touches. Fresh contacts.
- **Channel responsiveness:** Based on sequence data, this account responds best to:
  [email / LinkedIn / phone] — grounded in which stages and message types got engagement.
- **Messaging that worked:** If a reply came from a specific stage, note the subject line
  and angle that landed — this tells the rep what resonates with this account.
- **Messaging that didn't work:** If sequences completed with no reply, note what was
  tried so the rep doesn't repeat the same angle.

**Why this matters for reps:** Knowing that "Sarah was sequenced 3 months ago on a
cold outbound play and replied to the case study email but went dark after" is infinitely
more useful than treating her as a fresh cold contact. The rep can reference the prior
conversation, use the angle that got engagement, and skip the angles that fell flat.

**Critical signals from sequences:**
- **Active enrollment + deal review:** If a contact is currently in a sequence AND the
  rep is reviewing that deal, flag it. The sequence may be helping or conflicting with
  the deal motion.
- **Multiple contacts sequenced, zero replies:** The messaging isn't landing. Time to
  change the angle, try a different persona, or go in through a different door.
- **Reply but no meeting:** They engaged but didn't convert to a conversation. Follow up
  with a more specific ask or a different CTA.
- **Sequence overlap:** If multiple reps or sequences are touching the same account,
  flag it immediately — this creates a terrible customer experience.

### 3D: Critical items

Identify the **top 3 must-address items** — things the rep needs to handle before
or during the next interaction. These could be:
- Unfulfilled commitments from prior meetings
- Pain points that haven't been addressed
- Competitive threats that need countering
- Stakeholders who were promised follow-ups
- Active sequence enrollments that need coordination with deal motion
- Prior sequence angles that failed (don't repeat them)

---

## Layer 4: Contact Intelligence (Octave + Amplitude)

### 4A: Identify the key people

From all sources, build a people map:

- **From the sheet**: Champion, Economic Buyer, Primary Contact (named in the rep's data)
- **From Amplitude**: Power users (by event count), new users (recently added)
- **From Mixmax meetings**: Attendees from recent meetings, speakers in transcripts
- **From Octave**: `find_person` and `enrich_person` for named contacts

### 4B: For each key person, build a profile

- **Name and title**
- **Email**
- **Role in the deal/account** (Champion? Blocker? Economic Buyer? End User?)
- **Engagement level** — are they active in the product? Attending meetings? Responding to emails?
- **LinkedIn context** (from Octave enrichment) — tenure, background, connections
- **Recommended approach** — what to say to this person based on their role and engagement

### 4C: Who to engage

Produce a ranked list:
1. **Must engage** — the person whose action is needed to move things forward
2. **Should engage** — supporters who can amplify your message internally
3. **Watch** — stakeholders who could become blockers if ignored

---

## Layer 5: Synthesis & Action

After running Layers 1-4, synthesize everything into:

### The Verdict

One sentence: what's the real story with this account right now?
Not "they have 15 active users" but "They're a growing account with strong sequence
adoption but their champion just went dark — you need to multi-thread before renewal."

### The Recommended Actions

3-5 specific, sequenced actions. Not "follow up" but:
1. "Email Alex Chen (power user, 847 events/month) to schedule a check-in — reference
   the workflow automation they built last quarter"
2. "Ask Alex to intro you to their new VP of Sales (hired 3 weeks ago per LinkedIn) —
   this is your multi-threading play"
3. "Send a 'what's changed' email to Sarah Kim who went dark 6 weeks ago — Amplitude
   shows she stopped using sequences on March 1"

### The Outreach Angle

If the rep needs to reach out, provide the specific angle grounded in data:
- What to reference (usage data, meeting history, company news)
- What to offer (feature demo, business review, case study)
- What tone to strike (strategic partner, not salesperson)

---

## When to Go Deep vs. Light

- **Deal review (all deals)**: Run Layers 2A-2D + Layer 3A + 3C for every deal. Go full
  depth (all 5 layers) on the top 3 highest-risk or highest-ARR deals.
- **Deal review (single deal)**: Run all 5 layers at full depth including full sequence history.
- **Prospect finder (list)**: Run Layers 1 + 2A-2C + 3C for every recommended prospect.
  Sequence data is critical for prospects — you MUST check before recommending outreach.
  Go full depth on the top 5.
- **Prospect finder (single)**: Run all 5 layers at full depth.
- **Daily briefing**: Run Layer 2A only (active user count + trend) for flagged items.
  The briefing is a scan — drill-ins go deep.
- **Meeting prep**: Already runs all 5 layers by design. Include sequence history so the
  rep knows what outreach has been attempted before the meeting.
- **Account health**: Runs Layers 2A-2E at full depth, plus Layer 3 (meetings + sequences)
  for context.
- **Outreach drafting**: ALWAYS run Layer 3C first. Never draft outreach without checking
  sequence enrollment and history — the rep needs to know what was tried and what worked.
