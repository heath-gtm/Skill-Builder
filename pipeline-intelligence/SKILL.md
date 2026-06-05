---
name: pipeline-intelligence
description: >-
  Unified pipeline, account-prioritization, and ICP-quality engine for Mixmax GTM. Three modes: (1) PIPELINE COVERAGE & ACTIVITY — pipeline by channel, coverage ratios, activity metrics (Accounts Engaged, Meetings Booked, SQLs, SQOs), GTM stage distribution, engagement velocity; (2) ACCOUNT PRIORITIZATION — five top-10 lists (New, Cold/re-engage, Inbound, Outbound, Product) with Aero fit tiers and engagement angles; (3) MONTHLY ICP QUALITY — SQL/SQO opp cohorts scored with Aero + Octave composite, Aero False-Negative/False-Positive detection, L3M baseline, 9-section leadership HTML report. Trigger on pipeline creation, pipeline coverage, pipeline by channel, accounts engaged, meetings booked, SQLs, SQOs, account prioritization, GTM stage analysis, cold/new accounts, inbound/outbound/product accounts, Aero fit scores, Aero vs Octave, 'which accounts to go after', 're-engage', 'pipeline ICP quality', 'monthly pipeline analysis', 'how good is our pipeline', or the Total Prospect Account Engaged tab.
---

# Pipeline Intelligence

The single source of truth for pipeline creation, account prioritization, and
monthly ICP-quality analysis at Mixmax. This skill consolidates three previously
separate skills (`pipeline-building`, `account-pipeline-analysis`,
`pipeline-icp-analysis`) into one engine with three modes.

| Mode | Question it answers | Output |
|---|---|---|
| **A · Pipeline Coverage & Activity** | Do we have enough pipeline, and is it converting? | Coverage + activity + GTM-stage read by channel |
| **B · Account Prioritization** | Which accounts should we go after, and why? | Five top-10 lists with Aero tiers + engagement angles |
| **C · Monthly ICP Quality** | How good is THIS MONTH's pipeline? | Aero+Octave composite, FN/FP flags, L3M trend, 9-section HTML report |

Pick the mode that matches the question. Modes A and B usually run together off
the weekly snapshot; Mode C is a monthly leadership deliverable off live
Salesforce + Octave.

---

## Shared reference (all modes)

### Data sources

- **Monthly Bookings Summary tab** (GID: 1201655554) — pipeline created by channel, activity metrics (Accounts Engaged, Meetings Booked, SQLs, SQOs), coverage ratios
- **Quarterly Bookings Summary tab** (GID: 1160215217) — quarterly pipeline context
- **Total Prospect Account Engaged - Year tab** (GID: 43784651) — every prospect account with Channel Source, Account GTM Stage, Account Status, Aero: Account Fit Score Tier, Aero: Product Fit Score Tier, Prospecting Notes, Website, Account ID. In weekly snapshot context this tab is exported as a values-only sheet.
- **Salesforce + Octave (live)** — required for Mode C. Optional Amplitude (Product-channel deep dive) and Common Room (hiring-signal enrichment).

### Total Prospect Account Engaged — key fields

| Field | What it tells you |
|---|---|
| **Account Name** | Company name |
| **Account ID** | Salesforce ID — use for linking |
| **Channel Source** | Inbound, Outbound, Product, or Expansion |
| **Account GTM Stage** | Current motion stage (see below) |
| **Account Status** | Salesforce status (finer grain than GTM Stage) |
| **Aero: Account Fit Score Tier** | AI company fit: Excellent, Good, Moderate, Low |
| **Aero: Product Fit Score Tier** | AI product fit: Excellent, Good, Moderate, Low |
| **Prospecting Notes** | AE notes on the account |
| **Website** | Company URL — use for research when crafting angles |

### Salesforce account links

Every account referenced must link to its Salesforce record:

`https://mixmax.lightning.force.com/lightning/r/Account/{AccountID}/view`

Account IDs appear in the Rep Summary (Deals by Forecast Category), AE Forecast, Renewals, and Total Prospect Account Engaged tabs.

### Account GTM Stage definitions

- **New** — New account, not yet worked by an AE
- **Engaged** — AE activity in the last 14 days
- **Cold** — No AE activity in the last 14 days (re-engagement opportunity)
- **Nurture** — In nurture cycle, not actively worked
- **Disqualified** — Removed from active pipeline

### Account Status definitions

- **New** — New account
- **Qualified** — Qualified, ready to work
- **Attempting Contact** — Trying to contact
- **Disqualified / 1. Bad company fit** — Does not fit ICP
- **Disqualified / 2. SPAM** — Spam account
- **Nurture / 1. Too small (SS)** — Too small for Direct Sales, route to Self-Serve
- **Nurture / 3. Product gaps** — Product doesn't meet their needs currently
- **Nurture / 7. No Interest** — No interest at this time

### Formatting conventions

- **Aero score color coding:** Excellent = green, Good = blue, Moderate = yellow, Low = red
- **Currency:** $X,XXX
- **Percentages:** 1 decimal place
- **Account links:** always the Salesforce URL format above, e.g.
  `<a href="https://mixmax.lightning.force.com/lightning/r/Account/{ACCOUNT_ID}/view" target="_blank">{Account Name}</a>`

---

## Mode A — Pipeline Coverage & Activity

Analyze pipeline creation, coverage health, activity throughput, and GTM-stage flow.

### 1. Pipeline coverage & health

- **Total Pipeline Created:** Current vs Target
- **Pipeline by Channel:** Inbound, Outbound, Product, Expansion — each with Current, Target, Variance
- **Coverage Ratio:** total pipeline / remaining bookings target (healthy = 3x+, concerning = below 2x)
- **Channel Mix Assessment:** balanced creation, or over-reliant on one channel?

### 2. Activity metrics

Compare actual activity against targets to find bottlenecks:

- **Accounts Engaged:** Current vs Target vs % to Target
- **Meetings Booked:** Current vs Target vs % to Target (break out by Inbound, Outbound, Product)
- **SQLs:** Current vs Target vs % to Target (by channel)
- **SQOs:** Current vs Target vs % to Target (by channel)
- **Activity-to-Pipeline Conversion:** are activities converting at expected rates?

### 3. GTM stage distribution

From the Total Prospect Account Engaged tab:

- Count accounts by GTM Stage: New, Engaged, Cold, Nurture, Disqualified
- Break down by Channel Source within each stage
- Red flags:
  - Cold > Engaged → re-engagement problem
  - New accounts piling up without moving to Engaged → activation problem
  - Too many in Nurture → pipeline sitting idle

### 4. Account engagement velocity

- How quickly are New accounts converting to Engaged?
- What % of Engaged accounts have moved to an opportunity?
- Are Cold accounts being re-engaged or just accumulating?

---

## Mode B — Account Prioritization (the five priority lists)

Turn the Total Prospect Account Engaged tab into prioritized, actionable lists.
Every weekly report should produce these five lists. Each contains the **top 10
accounts**, and for each account provide: Account Name (Salesforce link), Channel
Source, Aero Account Fit Score Tier, Aero Product Fit Score Tier, Account Status,
Prospecting Notes, and a **Suggested Engagement Angle** (1–2 sentences from
visiting the account's website; for Product accounts also reference Amplitude
usage).

#### List 1: Top 10 New Accounts to Go After
**Filter:** GTM Stage = New. **Sort:** Aero Account Fit (Excellent → Good → Moderate), then channel diversity.
**Why:** Fresh accounts nobody has touched. Best-fit first = highest-probability first conversations.

#### List 2: Top 10 Cold Accounts to Re-Engage
**Filter:** GTM Stage = Cold. **Sort:** Aero Account Fit, then how recently they went cold.
**Why:** They showed interest then fell off. Re-engagement beats cold outreach because context exists.

#### List 3: Top 10 Inbound Accounts to Prioritize
**Filter:** Channel Source = Inbound. **Sort:** Aero Account Fit, then GTM Stage (Engaged → New → Cold).
**Why:** They raised their hand. Best-fit first maximizes inbound conversion.

#### List 4: Top 10 Outbound Accounts to Prioritize
**Filter:** Channel Source = Outbound. **Sort:** Aero Account Fit, then GTM Stage (New → Engaged → Cold).
**Why:** Outbound costs more effort per account; spend it on the highest-fit accounts.

#### List 5: Top 10 Product Accounts to Prioritize
**Filter:** Channel Source = Product. **Sort:** BOTH Aero Product Fit AND Account Fit (a great product fit with poor company fit is still a poor bet).
**Why:** Product-sourced accounts already use Mixmax. The angle is expansion — reference actual Amplitude usage (use `amplitude-guide`) to craft a relevant upsell.

### Deterministic Top-10 selector (when run off a snapshot)

When prioritizing from a snapshot for reproducible output, filter to
`GTM Stage ∈ {Engaged, New}` then sort: (1) Aero Blended Score desc,
(2) # Open Opps asc, (3) days_since_last_activity asc. Cap at 3 per channel to
prevent single-channel dominance. Two runs against the same snapshot produce the
same Top 10.

### Crafting engagement angles

Visit the account's Website and write a 1–2 sentence angle that:

- References something specific (industry, size, recent news, tech stack)
- Connects it to a relevant Mixmax value prop
- For Product accounts: also references Amplitude usage (which features they use, activation status, expansion openings)

**Good:** "Mid-market recruiting firm with 200+ employees running high-volume outreach — position Mixmax sequences as a way to scale candidate engagement without adding headcount."
**Bad:** "They might benefit from Mixmax."

### GTM stage distribution summary

Alongside the lists, summarize overall distribution: total accounts by GTM Stage, breakdown by Channel Source within each stage, and flag Cold > Engaged (re-engagement problem) or New piling up (activation problem).

---

## Mode C — Monthly Pipeline + ICP Quality Analysis

**Required connectors:** Salesforce + Octave. **Optional:** Amplitude (product channel), Common Room (hiring signal).

Once a month a GTM leader needs to answer three questions about the pipeline just
created: *(1) Is the volume real? (2) Is it good ICP? (3) What's improving / keep
doing / fix?* This mode answers all three with a single HTML artifact built from
Salesforce ground truth, cross-scored by Aero + Octave, compared to an L3M
trailing baseline, laid out as a leadership-meeting talking script.

### Methodology — fixed and non-negotiable

**Cohort definition.** Two parallel cohorts, both filtered to `Type != 'Renewal'`:

- **SQL cohort** = Opportunities with `AE_SQL_Contact__c` in the target month. This field is inconsistently populated; if it returns zero, fall back to `CreatedDate` in the target month and document the fallback in the methodology section.
- **SQO cohort** = Opportunities with `SQO_Date__c` in the target month. This is the primary cohort key and the headline.

The SQL cohort exists to (a) sanity-check funnel movement and (b) catch opps created late-month that haven't reached SQO.

**Channel attribution.** Use `Opportunity_Source__c` as the canonical channel field (rolls up to Inbound / Outbound / Product / Expansion). Do NOT use `Channel__c` (free-text, mostly "Other/Unknown") or `LeadSource` alone (informational, inconsistent with the dashboard).

**ICP composite scoring.** Two independent signals, both required.

- **Aero** (Salesforce, Account-level): `Aero_Account_Fit_Score__c` (0-100), `Aero_Account_Fit_Score_Tier__c` (High/Medium/Low/No Score), `Aero_Blended_Score_Tier__c`, `Aero_Product_Engagement_Score__c`
- **Octave** (live API per Account.Website domain): `mcp__012b2f88-c19c-41ca-a2e8-18c61394ad53__qualify_company` with `companyDomain` → headline verdict (Strong/Moderate/Weak/Bad), 1-9 score, segment match, reasoning

**Composite grading:**
- **A-Grade** = Octave Strong (8-9) regardless of Aero
- **B-Grade** = Octave Moderate (5-7) OR Octave Strong + Aero No Score
- **Off-ICP** = Octave Weak (3-4) or Bad (1-2) at any Aero score

**Override flags — the highest-value outputs:**
- **Aero False Negative (FN)** = Aero Low + Octave Strong (8-9). We almost passed on a real fit.
- **Aero False Positive (FP)** = Aero High + Octave Weak/Bad (1-4). We prioritized a non-fit.

**L3M trailing baseline.** Same cohort definition, range `(target_month - 3 months)` through `(target_month - 1 day)`. Report per-month detail AND the 3-month average. Flag any anomalously low month (e.g., 1-opp month) and offer a "trimmed baseline" alternative.

**Deal-health overlay on open opps.** For every target-month opp still open: compute days since SQO, check PLAN-vs-stage on the Account (Problems / Leverage / Decision Dynamics / Next Steps — fields on Account, see `sfdc-field-library`), surface concentration risk (which AE owns >40% of cohort by $). Skip the 4-source activity check unless requested.

**Velocity reality-check.** Compare target-month Closed Won $ vs Pipeline Created $. If Closed Won grew much slower than pipeline, flag it in the Cover and note expected forward-quarter conversion (trailing win rate × cycle time).

### Report structure (9 sections, in order)

The HTML report MUST follow this order — it is the leadership talking script.

1. **At a glance** — 4 metric cards: Pipeline $, Closed Won $, Strong-Fit %, Aero-misclassified $.
2. **What the month proved** — two side-by-side callouts: "Keep doing this" (green) and "Fix this immediately" (amber); both name specific accounts and dollars.
3. **Channel breakdown** — 4 channel cards (Inbound/Outbound/Product/Expansion) each with ARR, opp count, Strong-Fit count, Weak/Bad $, Aero alignment, median Aero, avg deal size, Closed Won; plus a "Reading the channels" narrative.
4. **Aero vs Octave** — the defining section. Table of every account where Aero and Octave disagree, flagged FN or FP; below it a red callout summarizing the systemic finding. This is the report's headline insight.
5. **Every opp ranked by composite** — full sortable table: Account, Channel, Owner, ARR, Stage, Aero, Octave, Composite grade; override flags inline.
6. **AE breakdown** — per-AE pipeline cards + a coaching callout naming the highest-leverage save or post-mortem candidate.
7. **vs L3M trailing avg** — numeric table with per-month detail + L3M average row + Target Month row + Delta row; amber callout if velocity drops despite volume rising.
8. **Action plan** — numbered 5-7 specific actions, each with named owner and due date ("tell leadership tomorrow"). No abstractions.
9. **Methodology** — reproduce cohort definition, channel attribution, scoring formulas, L3M definition, and an explicit reconciliation block if dashboard total differs from report total.

### Data pulls — exact SOQL templates

**SQL date cohort:**

```sql
SELECT Id, Name, AccountId, Account.Name, Account.Website,
       StageName, ForecastCategoryName, Type, LeadSource,
       Channel__c, Opportunity_Source__c,
       ARR__c, Amount, CreatedDate, SQO_Date__c, AE_SQL_Contact__c,
       CloseDate, Probability, IsClosed, IsWon, Owner.Name
FROM Opportunity
WHERE AE_SQL_Contact__c >= {MONTH_START}
  AND AE_SQL_Contact__c < {MONTH_END}
  AND Type != 'Renewal'
ORDER BY ARR__c DESC NULLS LAST
```

If this returns 0 rows, fall back to:

```sql
... WHERE CreatedDate >= {MONTH_START}T00:00:00Z
       AND CreatedDate < {MONTH_END}T00:00:00Z
       AND Type != 'Renewal'
```

**SQO date cohort:**

```sql
... WHERE SQO_Date__c >= {MONTH_START}
       AND SQO_Date__c < {MONTH_END}
       AND Type != 'Renewal'
```

**Account ICP fields (one batched query):**

```sql
SELECT Id, Name, Website, Type, DWH_Customer_Type__c,
       Aero_Account_Fit_Score__c, Aero_Account_Fit_Score_Tier__c,
       Aero_Blended_Score_Tier__c, Aero_Product_Engagement_Score__c,
       CR_Number_of_Employees__c, CR_of_Sales_Team__c,
       CR_Sales_Team_Hiring__c, Sales_Acceleration_Tool__c, Industry
FROM Account
WHERE Id IN ({ACCOUNT_IDS_FROM_COHORT})
```

**L3M baseline aggregate** (record-level pull then aggregate locally because `Opportunity_Source__c` is not GROUP BY-able):

```sql
... WHERE SQO_Date__c >= {MONTH_START - 3MO}
       AND SQO_Date__c < {MONTH_START}
       AND Type != 'Renewal'
ORDER BY SQO_Date__c
```

**Octave per-domain call:**

```
mcp__012b2f88-c19c-41ca-a2e8-18c61394ad53__qualify_company({ companyDomain: "..." })
```

Run all unique domains in parallel batches of 5-7 via a subagent to keep main-context clean. Subagent returns a compact table: Domain | Verdict | Score | Segment | Reason.

### Output & publishing (Mode C)

- HTML report at `Revenue Reviews/specs/{YYYY-MM}-pipeline-icp-analysis.html` in the user's workspace folder
- Published to GitHub Pages at `monthly/{YYYY-MM}-pipeline-icp-analysis.html` via the publishing config workflow
- `reports.json` manifest entry: `id: "pipeline-icp-analysis-{YYYY-MM}"`, `type: "analysis"`, `roles: ["revops", "sales", "leadership"]`
- Run `Revenue Reviews/specs/html_publish_validator.py` BEFORE publish. Requires `<script src="/nav.js">` and `<script src="/theme.js">` near top of body, NO hardcoded theme toggle/handler, all colors via CSS custom properties.

### Quality gates (Mode C)

- **No ICP claim without two-source breakdown.** Every Strong-Fit label shows the Aero verdict AND the Octave verdict. If only one is available, declare it.
- **Every FN/FP gets a deal-level call-out.** Name the account, the dollar amount, and what the disagreement implies for action.
- **Reconciliation block is mandatory** when the user's dashboard totals differ from SOQL totals. State the SOQL ground-truth figure first, then explain the difference.
- **L3M baseline includes a "trimmed" alternative** when one month had <2 opps.

### Make.com / API packaging (Mode C)

**Input:**
```json
{
  "target_month": "2026-05",
  "include_sql_cohort": true,
  "include_deal_health_overlay": false,
  "publish_to_pages": true,
  "audience_notes": "leadership meeting tomorrow"
}
```

**Output:**
```json
{
  "report_url": "...",
  "github_pages_url": "...",
  "headline_verdict": "Strong Volume / Scoring System Needs Work",
  "pipeline_arr_total": 317015,
  "pipeline_arr_by_channel": { "inbound": 194922, "outbound": 46440, "product": 18490, "expansion": 58164 },
  "strong_fit_pct": 0.74,
  "aero_fn_dollars": 61822,
  "aero_fp_dollars": 25056,
  "l3m_baseline_avg_arr": 70090,
  "vs_l3m_pct": 3.52,
  "action_count": 6
}
```

**Failure modes:** No Salesforce → hard fail. No Octave → degrade to Aero-only composite + warn override-detection unavailable. `AE_SQL_Contact__c` returns 0 → silent fallback to CreatedDate, documented in methodology. Publishing config missing → build HTML, save to workspace, skip GitHub push, note to run `publishing-config-setup`.

### Suggested cadence (Mode C)

Run on the last business day of each month, or the morning before the first leadership meeting of the new month. Pair with the monthly Closed Won analysis for the rear-view + forward-view picture.

---

## Output guidelines (Modes A & B)

**TL;DR / company-level report:** pipeline coverage numbers, activity vs targets, GTM stage distribution summary, channel-level insights, list names with account counts. NO individual account names.

**GTM Leadership report:** full detail — all five top-10 lists with Salesforce links, Aero scores, and engagement angles; full GTM stage breakdown by channel; activity detail by rep if available; specific pipeline gaps and re-engagement opportunities.

---

## When NOT to use this skill

- "Is this deal real" / per-deal forecast call → `deal-health-analyst` or `deal-intelligence`
- Per-rep pipeline review / AE coaching → `mixmax-ae-pipeline-analysis:ae-pipeline-runbook`
- Single-account strategic deep dive → `customer-strategy-brief` / `customer-strategy-deep-dive`
- Weekly cadence revenue read → `mixmax-weekly-gtm-report`
- Funnel-leak conversion diagnosis by channel → `strike-zone-analyst`

---

## Inheritance and lock-ins

Inherits from `sfdc-field-library` (canonical field reference — the 22 GTM custom fields), `mixmax-gtm-brand-guidelines` (HTML output standards), `publishing-config-reference` (GitHub Pages publishing), `icp-analyst` (composite ICP scoring framework), and `salesforce-analyst` (PLAN-vs-stage validation for the deal-health overlay). For Product-channel angles, calls `amplitude-guide` / `product-engagement-story`.

Lock-ins: #11 (channel classifier), #14 v7 (play type taxonomy + Aero override contract), #16 v9.1 (4-source activity if doing deal-health overlay), #26 (22 custom fields).

---

## Example invocation (Mode C)

> "Analyze the pipeline we created in May 2026. I need to walk into our leadership meeting tomorrow saying this is what we did, here's what's improving, what we need to keep doing. Aero+Octave ICP cross-check please, vs L3M trailing avg, publish to GTM Pages."

Produces the full report in one pass: SOQL pulls (SQO non-renewal + L3M + Account ICP), parallel Octave calls per domain via subagent, channel rollup, Aero-vs-Octave reconciliation, deal-health overlay if requested, full HTML against brand guidelines, validator gate, GitHub Pages publish, reports.json update, and a one-line summary with the GitHub URL.
