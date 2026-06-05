---
name: pipeline-building
description: Trigger on phrases about pipeline creation, pipeline coverage, pipeline by channel, accounts engaged, meetings booked, SQLs, SQOs, account prioritization, GTM stage analysis, cold accounts, new accounts, inbound/outbound/product accounts, Aero fit scores, "which accounts to go after", re-engagement, account engagement velocity, activity metrics, pipeline health, or any mention of the Total Prospect Account Engaged tab or the pipeline/activity sections of the Monthly Bookings Summary.
---

# Pipeline Building & Account Engagement Analysis

This skill analyzes pipeline creation metrics, account engagement velocity, and GTM stage distribution to help the Mixmax sales team prioritize accounts and optimize channel-based account engagement.

## Data Sources

- **Monthly Bookings Summary tab** (GID: 1201655554) — pipeline created by channel, activity metrics (Accounts Engaged, Meetings Booked, SQLs, SQOs), coverage ratios
- **Quarterly Bookings Summary tab** (GID: 1160215217) — quarterly pipeline context
- **Total Prospect Account Engaged - Year tab** (GID: 43784651) — all prospect accounts with Channel Source, Account GTM Stage, Account Status, Aero: Account Fit Score Tier, Aero: Product Fit Score Tier, Prospecting Notes, Website, Account ID

## Salesforce Account Links

Every account must link to: https://mixmax.lightning.force.com/lightning/r/Account/{AccountID}/view

## Account GTM Stage Definitions

- **New** — New account, not yet worked by an AE
- **Engaged** — AE activity in the last 14 days
- **Cold** — No AE activity in the last 14 days (re-engagement opportunity)
- **Nurture** — In nurture cycle, not actively worked
- **Disqualified** — Removed from active pipeline

## Account Status Definitions

- **New**
- **Qualified** — Qualified, ready to work
- **Attempting Contact** — Trying to contact
- **Disqualified / 1. Bad company fit**
- **Disqualified / 2. SPAM**
- **Nurture / 1. Too small (SS)** — route to Self-Serve
- **Nurture / 3. Product gaps**
- **Nurture / 7. No Interest**

## Analysis Framework

### 1. Pipeline Coverage & Health

Analyze pipeline creation across channels and assess overall pipeline health:

- **Total Pipeline Created:** Current vs Target
- **Pipeline by Channel:** Inbound, Outbound, Product, Expansion — each with Current, Target, Variance
- **Coverage Ratio:** total pipeline / remaining bookings target (healthy = 3x+, concerning = below 2x)
- **Channel Mix Assessment:** Is pipeline creation balanced or over-reliant on one channel?

### 2. Activity Metrics

Compare actual activity against targets to identify bottlenecks:

- **Accounts Engaged:** Current vs Target vs % to Target
- **Meetings Booked:** Current vs Target vs % to Target (break out by Inbound, Outbound, Product)
- **SQLs:** Current vs Target vs % to Target (break out by channel)
- **SQOs:** Current vs Target vs % to Target (break out by channel)
- **Activity-to-Pipeline Conversion:** Are activities converting at expected rates?

### 3. GTM Stage Distribution Analysis

From the Total Prospect Account Engaged tab:

- Count accounts by GTM Stage: New, Engaged, Cold, Nurture, Disqualified
- Break down by Channel Source within each stage
- Flag red flags:
  - If Cold > Engaged = re-engagement problem
  - If New accounts piling up without moving to Engaged = activation problem
  - If too many in Nurture = potential pipeline sitting idle

### 4. Account Engagement Velocity

Track how quickly accounts move through stages:

- How quickly are New accounts converting to Engaged?
- What % of Engaged accounts have moved to an opportunity?
- Are Cold accounts being re-engaged or just accumulating?

### 5. Top 10 Accounts to Go After (Unified Priority List)

Build ONE unified Top 10 list that pulls from ALL 700+ prospect accounts regardless of channel or GTM stage. This is the single, org-wide priority list. No separate lists by channel — just the 10 best accounts to focus on RIGHT NOW.

#### Scoring Methodology

Accounts are ranked on a composite score across four dimensions:

1. **Fit** — Aero Account Fit Score + Aero Product Fit Score (combined weight). Excellent/Excellent = highest, Low/Low = lowest.
2. **Engagement** — GTM Stage recency (Engaged > New > Cold), days since last touch, recent meeting/email volume, website visits in the last 30 days.
3. **Opportunity** — Revenue potential: estimated deal size based on company size/industry, expansion ARR from existing deployment, competitive displacement opportunity.
4. **Timing** — Urgency signals: contract renewal approaching, recent inbound interest (form fill, demo request), product usage spike (for Product channel accounts), pricing page visits.

The Top 10 are the accounts with the highest composite score. Each account's WHY must reference the specific signals that earned its spot.

#### Required Fields for Each Account

- **Account Name** (Salesforce link)
- **Channel Source** (Inbound, Outbound, Product, or Expansion)
- **Aero Account Fit Score Tier**
- **Aero Product Fit Score Tier**
- **GTM Stage**
- **Account Status**
- **WHY This Account** (mandatory, 2-3 sentences)

#### WHY Justification Requirements

Every account MUST include a "WHY" that answers the question: **"Out of 700+ prospect accounts, why did THIS one make the Top 10?"**

The WHY must combine ALL four scoring signals:

- **Fit Signal** — Which Aero scores (Account + Product) make this account a strong fit?
- **Engagement Signal** — What recent activity shows interest? (GTM Stage, days since last touch, meetings/emails, site visits)
- **Revenue Opportunity Signal** — What's the deal size potential, expansion ARR, or competitive displacement opportunity?
- **Timing Signal** — Why NOW? (Contract renewal coming up, recent inbound interest, product usage spike, pricing page visits)

**Good WHY Example:** "Excellent Aero fit (Account + Product), engaged 3x in last 7 days via Inbound, $45K expansion potential based on current 50-seat deployment, and pricing page visited twice this week. This account is actively evaluating — if we don't move now, a competitor will."

**Bad WHY Example:** "High fit score, looks like a good account."

#### Building the WHY

- Visit the account's Website to gather intelligence (industry, size, recent news, tech stack)
- For Product channel accounts: **ALWAYS invoke the `amplitude-guide` skill** to pull live usage data (active users, feature adoption, usage velocity, aha-moment progression). Timing signals for Product-channel accounts must be grounded in real Amplitude events (e.g. "usage jumped 3x in last 14 days", "pricing page hit twice this week", "team expanded from 2 to 8 active seats") — not guessed from CRM fields.
- Connect observed signals to specific Mixmax value props relevant to this account
- Be specific: reference actual engagement dates, deal sizes, product usage trends, competitive context
- Make it clear why THIS account, out of 700+, deserves attention RIGHT NOW — reps won't act on vague justifications

## Output Guidelines

### For Mixmax GTM Report (Org-Wide)

Show the full Top 10 with WHY justifications — this is org-wide and transparent:
- **Top 10 Accounts** list with Salesforce links, Aero scores, and mandatory WHY justifications
- Pipeline coverage numbers
- Activity metrics vs targets
- GTM Stage distribution summary
- Channel-level insights
- **No rep names**, but account names YES (this is org-wide accountability)

### For CRO Report (Direct to CRO)

Provide full detail beyond the Top 10:
- **Top 10 Accounts** list with Salesforce links, Aero scores, and mandatory WHY justifications
- Rep assignment for each Top 10 account
- Full GTM Stage breakdown by channel
- Activity detail by rep (meetings, emails, calls by rep)
- Specific pipeline gaps and re-engagement opportunities
- Channel-level performance vs targets

### Formatting

- **Color coding for Aero scores:** Excellent = green, Good = blue, Moderate = yellow, Low = red
- **Currency:** Format as $X,XXX
- **Percentages:** Include 1 decimal place
- **Account links:** Always use Salesforce URL format for clickable account references
