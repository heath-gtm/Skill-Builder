---
name: sfdc-field-library
description: Canonical Salesforce field reference for Mixmax GTM. Single source of truth for every SFDC field name, definition, query pattern, operational definition. Load FIRST anytime you answer a question touching Salesforce data — gives you the 22 GTM custom fields, the PLAN-stage matrix, the 4-source activity formula (lock-in #16 v9.1), channel classification rules, canonical SOQL snippets. Trigger on "Salesforce", "SFDC", "account", "opportunity", "deal", "pipeline", "renewal", "PLAN", "forecast", "rep performance", "channel", "activity", "stage", "Commit", "Best Case", "ARR", "what's happening with {account}", "review {account}", "is {deal} real", "pipeline review", "deal review", "Aero", "PES", "ICP fit", "book of business", "CSM book", "decision maker", "champion", "multi-thread", "days dark", "ghost deal", "stuck deal", "Account_Notes", "Decision_Maker__c", or any field-name reference. Fire AGGRESSIVELY — better to load once unnecessarily than answer with the wrong field reference.
---

# SFDC Field Library — canonical reference for every Salesforce-related question

**Purpose.** This skill IS the field library. Whenever you're answering ANY question that touches Salesforce data — account health, deal review, pipeline analysis, renewal prep, rep coaching, ICP fit, channel attribution, anything — you should have this content in context BEFORE responding. Always reference canonical field names + canonical interpretations. Apples-to-apples consistency across every output.

**Source of truth.** `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` is the canonical file. This skill mirrors its content. When the library updates, both update together.

---

## Object hierarchy

```
Account  ──┬──► Opportunity ──► OpportunityContactRole ──► Contact
           │
           ├──► Contact (Account-direct)
           ├──► Task   (WhatId = Account.Id)
           └──► Event  (WhatId = Account.Id)

Opportunity ──┬──► Task   (WhatId = Opportunity.Id)
              └──► Event  (WhatId = Opportunity.Id)
```

---

## 1. Account custom fields (the 22 GTM fields you actually care about)

### ARR + customer type (warehouse-sourced, authoritative)

| Field | Definition | Notes |
|---|---|---|
| `DWH_DS_Customer_ARR__c` | Direct Sales customer ARR | Use for sales-led deal sizing |
| `DWH_SS_Customer_ARR__c` | Self-Serve customer ARR | Stripe-billed monthly→annual |
| `DWH_Customer_Type__c` | Customer / Prospect / Churned / Free / Paused | **Authoritative — overrides standard Type field** |
| `DWH_Forecasted_ARR__c` | CRO-locked forecast ARR | Used by Pipeline-Creation |

### The 4 PLAN fields (NEVER MEDDIC — PLAN Selling is Mixmax-built)

| Field | PLAN Letter | Required by stage |
|---|---|---|
| `Problems_Account__c` | **P**roblems | Discovery |
| `Leverage_Alignment__c` | **L**everage Alignment | Solution Validation |
| `Address_Decision_Dynamics__c` | **A**ddress Decision Dynamics | Proposal |
| `Next_Steps_Account__c` | **N**ext Steps | Negotiation |

**The BS detector (PLAN-vs-stage):**
```
if Stage = 'Discovery'           and Problems_Account__c           is null → PLAN_GAP
if Stage = 'Solution Validation' and Leverage_Alignment__c         is null → PLAN_GAP
if Stage = 'Proposal'            and Address_Decision_Dynamics__c  is null → PLAN_GAP
if Stage = 'Negotiation'         and Next_Steps_Account__c         is null → PLAN_GAP
if ForecastCategoryName = 'Commit' and ANY of 4 PLAN fields is null → COMMIT_RISK
```

When PLAN is incomplete, ALWAYS name the missing field. Never just "PLAN incomplete."

### Decision maker

| Field | Definition |
|---|---|
| `Decision_Maker__c` | Named decision maker contact |
| `Decision_Maker_Title__c` | Their title |

### Account notes (the rep's narrative)

| Field | Definition |
|---|---|
| `Account_Notes__c` | Free-text rep narrative |
| `Account_Notes_Last_Updated__c` | Timestamp of last update — **>180 days = stale** |

### Growth + upsell intent

| Field | Definition |
|---|---|
| `Growth_Potential__c` | Picklist: Low / Medium / High |
| `Upsell_Plan_Account__c` | Free-text upsell motion |

### Tech stack + competitive intel

| Field | Definition |
|---|---|
| `Email_Provider__c` | Outlook / Gmail |
| `CRM__c` | Salesforce / HubSpot / Other |
| `Sales_Acceleration_Tool__c` | Outreach / SalesLoft / Apollo / Yesware / Cursor — **3+ tools = consolidation displacement target** |
| `Conversational_Intelligence_Competitor__c` | Gong / Chorus / etc. |
| `Data_Enrichment_Competitor__c` | ZoomInfo / Apollo / Lusha / etc. |
| `Secondary_Competitor_Used__c` | Other competitive products |

### Common Room enriched fields

| Field | Definition |
|---|---|
| `CR_Number_of_Employees__c` | **Use this over standard NumberOfEmployees** (fresher) |
| `CR_CS_Team__c` | Estimated CS team size |
| `CR_of_Sales_Team__c` | Estimated sales team size |
| `CR_Sales_Team_Hiring__c` | Sales hires in last 90d — **≥3 = top-of-funnel ICP scream** |

### Aero scoring fields

| Field | Definition |
|---|---|
| `Aero_Account_Fit_Score__c` | 0-100 |
| `Aero_Account_Fit_Score_Tier__c` | A / B / C / D |
| `Aero_Blended_Score_Tier__c` | Composite (fit + engagement) |
| `Aero_Product_Engagement_Score__c` | 0-100 — has **two known failure modes**: Aero False-Negative + Ghost-Active |

### Product Engagement Story (Amplitude Analyst writebacks)

| Field | Definition |
|---|---|
| `Product_Engagement_Verdict__c` | Power / Established / Emerging / Dormant / Untouched / Ghost-Active / Aero-False-Negative |
| `Product_Engagement_Last_Run__c` | ISO datetime |
| `Product_Engagement_Active_Latest__c` | Latest week's `_active` count |
| `Aero_False_Negative__c` | Boolean override |

### Account brief URL

| Field | Definition |
|---|---|
| `Account_Brief_URL__c` | Deep link to canonical brief on GitHub Pages |
| `Account_Tier__c` | Tier 1 / 2 / 3 prioritization |

### Renewal fields

| Field | Definition |
|---|---|
| `Open_Renewal_ARR__c` | ARR locked into current open renewal opp |
| `RP_Renewal_Period_Start__c` | Renewal period start date |
| `RP_Renewal_Period_End__c` | Renewal period end date (THE renewal day) |
| `Past_Renewals__c` | Count of prior renewals (tenure proxy) |
| `Last_Renewal_Touch__c` | Date of last renewal-track activity |
| `Days_Since_Last_Renewal_Touch__c` | `>30` = renewal-track ghost |
| `All_Purchased_Seats__c` | Paid seat count (expansion math denominator) |
| `Stripe_Subscription_Start_Date__c` / `End_Date__c` | Stripe sub tenure |
| `Implementation_Status__c` | Onboarding state |
| `CSM__c` / `CSM_Text__c` | Assigned CSM (record ref + text fallback) |

### Channel attribution (source of the lead) — CANONICAL

| Field | Definition |
|---|---|
| `Channel_Source__c` | **THE canonical channel attribution field.** Formula (text) on Account = the source of the lead. Values: `Inbound` / `Outbound` / `Product`. See § 5. Channel is attributed at the **account** level; an opportunity inherits its account's channel. **Never** use `Opportunity.Channel__c` for attribution (see § 2). Formula field — non-groupable in SOQL: filter on it, never `GROUP BY`. |

---

## 2. Opportunity fields

### Standard
`Id`, `Name`, `AccountId`, `Account.Name`, `Account.Website`, `StageName`, `Amount`, `CloseDate`, `IsClosed`, `LastActivityDate`, `LastModifiedDate`, `OwnerId`, `Owner.Email`, `Type`, `Probability`

### Custom
`ForecastCategoryName`, `Loss_Reason__c`, `Competitor__c`, `Channel__c`

⚠️ **`Opportunity.Channel__c` is NOT the channel attribution field.** It is a separate legacy formula whose values (`Direct`, `Virality & Product`, `Other/Unknown`, …) do not map to the lead source and routinely disagree with the account's true channel. For channel attribution always use `Account.Channel_Source__c` (Inbound / Outbound / Product — see § 5).

### Opportunity stage canonical values

```
Discovery
Solution Validation
Proposal
Negotiation
Closed Won
Closed Lost — Pass
Closed Lost — Lost
Closed Lost — Churn  (renewal-specific)
```

### ForecastCategoryName interpretation

| Category | Meaning |
|---|---|
| `Commit` | AE will hit it. Miss = forecast accuracy issue. |
| `Best Case` | Can close but conditions still needed. |
| `Pipeline` | Real deal, uncertain timing. |
| `Omitted` | Closed or excluded. |

**Commit Creep Watch:** any deal that moved `Commit → Best Case` in trailing 14 days = surface to Sales Leader.

---

## 3. Contact fields

`Id`, `Name`, `FirstName`, `LastName`, `Email` (primary join key), `Phone`, `MobilePhone`, `Title`, `AccountId`, `LeadSource`, `LastActivityDate`

Default order: `ORDER BY LastActivityDate DESC NULLS LAST LIMIT 25`

---

## 4. The 4-source activity formula (lock-in #16 v9.1) — CRITICAL

**Never use `LastActivityDate` alone.** Reps log activity at Account/Contact level — single-field reads systematically misclassify active accounts as silent.

```sql
canonical_last_activity = MAX(
  Account.LastActivityDate,
  Opportunity.LastActivityDate,
  (SELECT MAX(ActivityDate) FROM Task
     WHERE Status = 'Completed'
       AND (WhatId = '{account_or_opp_id}'
            OR WhoId IN (SELECT Id FROM Contact WHERE AccountId = '{account_id}'))),
  (SELECT MAX(ActivityDate) FROM Event
     WHERE WhatId = '{account_or_opp_id}'
        OR WhoId IN (SELECT Id FROM Contact WHERE AccountId = '{account_id}'))
)

days_dark = today - canonical_last_activity
```

In Vercel runtime, this is wrapped by `salesforce_query_activities()`. NEVER inline a single-source query.

---

### Funnel-stage qualification dates (channel-specific) — CANONICAL

The lead/account qualification stage for each channel lives in a different Account date field. These are the join keys for any MQA/OQA/PQA → SQO funnel analysis. (Verified 2026-06-05.)

| Field | Stage | Channel | Notes |
|---|---|---|---|
| `MQA_Date_2024__c` | **MQA** (Marketing Qualified Account) | Inbound | **The populated inbound stamp.** Use this — NOT the Lead `MQL__c`/`MQL_Date__c` fields, which are **empty** in the live org (inbound auto-creates opps and bypasses lead-level MQL stamping). Populated from 2024 Q4 onward. |
| `OQA_Date__c` | **OQA** (Outbound Qualified Account) | Outbound | Tracking began Jan 2026 — small population, too new to trend QoQ. No "OQL" field exists. |
| `Sales_PQA_Date_Account__c` | **PQA** (Product Qualified Account) | Product | Clean history from 2025. Also `PQA_Date_Initial__c`, `PQA_Date_Most_Recent__c`, `CR_PQA_Score__c`. |

**MQA/OQA/PQA → SQO conversion** = join the account-stage date to its New-Business opps where `SQL__c = true` (the SQO marker, see § 2), time-bounded with `SQO_Date__c` on/after the qualification date to exclude pre-stage SQOs.

⚠️ **Lead MQL fields are EMPTY** — `Lead.MQL__c`, `MQL_Date__c`, `MQL_Assigned_Date_Time__c` returned 0 rows (trailing 18mo, verified 2026-06-05). Do not use them; use `Account.MQA_Date_2024__c` for the inbound funnel.

---

---

## 5. Channel classification (canonical — used by every channel-aware analyst)

**Canonical attribution field: `Account.Channel_Source__c`** — a formula (text) field = the source of the lead. This is the SINGLE source of truth for channel. Read it directly; do not reconstruct channel from heuristics when this field is populated.

```
INBOUND      Account.Channel_Source__c = 'Inbound'    (lead came to us — web form, demo request, MQA)
OUTBOUND     Account.Channel_Source__c = 'Outbound'   (we went to them — SDR/AE sourced, OQA)
PRODUCT      Account.Channel_Source__c = 'Product'    (self-serve signup / PQA — product-led)
```

**Channel is attributed at the Account level (the source of the lead). An Opportunity inherits the channel of its Account — read `Opportunity.Account.Channel_Source__c`. Never derive channel from the Opportunity alone.**

**How the formula works (empirically verified 2026-06-07, 0 counterexamples):**
`Channel_Source__c` = channel of the EARLIEST qualification date on the account:
`MQA_Date_2024__c` → Inbound · `OQA_Date__c` → Outbound · `Sales_PQA_Date_Account__c` → Product.
Ties resolve to Inbound (MQA evaluated first). **If NO qualification date exists → defaults to
'Outbound'** — verified across the full org (every no-date account reads Outbound; every Inbound
account has an MQA date; every Product account has a PQA date; 51/51 dual-stamped accounts follow
earliest-wins). Three caveats: (1) 'Outbound' is overloaded — it includes the entire unqualified
account universe (~88K no-date accounts), not just OQA-qualified accounts; (2) `MQA_Date_2024__c`
exists only since Q4 2024 and `OQA_Date__c` only since Jan 2026, so accounts qualified before
those fields existed fall to the Outbound default regardless of true origin; (3) it is a live
formula — stamping a date retroactively re-attributes the account and all its historical opps.

⚠️ **Do NOT use `Opportunity.Channel__c`.** It is a separate legacy formula whose values (`Direct`, `Virality & Product`, `Other/Unknown`, …) do not map to the lead source and frequently disagree with the account's true channel (e.g. an `Outbound` account shows `Virality & Product` on the opp). It is not the channel attribution field.

`Channel_Source__c` is a formula field — **non-groupable in SOQL. Filter on it (`WHERE Channel_Source__c = 'Outbound'`); never `GROUP BY Channel_Source__c`.**

### Two-layer attribution model (Heath-canonical 2026-06-07)

Attribution is tracked at TWO layers. Never mix them up:

**Layer 1 — LEAD attribution (Account level, set before any opp exists):**

| What | Field |
|---|---|
| Channel Source | `Account.Channel_Source__c` (formula; Inbound/Outbound/Product) |
| Inbound qualification | `Account.MQA_Date_2024__c` (MQA date) |
| Product qualification | `Account.Sales_PQA_Date_Account__c` (PQA date) |
| Outbound qualification | `Account.OQA_Date__c` (OQA date; populated since Jan 2026) |

**Layer 2 — OPPORTUNITY SOURCE attribution (once an opp is created):**

| What | Field | Notes |
|---|---|---|
| Opportunity record type | `RecordTypeId` / `RecordType.Name` | lifecycle gate (Net New / Conversion / Renewal / Expansion) |
| Type | `Type` | picklist: New Business / Convert SS to DS / Expansion / Renewal / … |
| Opportunity Source | `Opportunity_Source__c` | **Formula (Text)** — computed FROM `Opportunity_Source_Details__c`. Non-groupable, NOT directly writable. To change Source, change Details. |
| Opportunity Source Details | `Opportunity_Source_Details__c` | **Restricted picklist (writable)** — the driver field. Value sets are record-type-scoped (the Renewal record type does NOT allow `Product - *` values). |

**Hard rule (Heath, 2026-06-07):** any opportunity with `RecordType.DeveloperName =
'Mixmax_Conversion_Direct_Sales'` (RT Id `012VS000005ln5fYAA`) OR `Type = 'Convert SS to DS'`
must carry `Opportunity_Source_Details__c = 'Product - SS Customer'` so `Opportunity_Source__c`
rolls to **Product**. Conversions tagged `Inbound - Marketing` or `Outbound - *` are
misclassifications. A Salesforce automation (record-triggered flow or validation rule) should
enforce this going forward — spec drafted 2026-06-07, pending admin deployment.

⚠️ **Picklist traps when correcting records:** `Opportunity_Source_Details__c` is a restricted,
dependency-constrained picklist — (a) the `Mixmax - Renewal` record type's value set blocks all
`Product - *` values; (b) `Type` controls availability too (e.g. `Type='InApp Expansion'` blocks
Product values — set `Type='Convert SS to DS'` in the SAME update).

**Bookings-by-channel reporting basis (Heath-canonical 2026-06-07):** when reporting bookings
by channel against the master performance tracker, filter to `RecordTypeId IN
('0121R000001QF50QAG' /*Net New - DS*/, '012VS000005ln5fYAA' /*Conversion - DS*/)` — new
business + conversions ONLY. Expansion (DS + Organic), Renewal, and all other record types are
excluded even when they carry a `Product`/`Inbound`/`Outbound` Opportunity Source (e.g. 24 won
Product-source deals / $69,019 since 2024 sit on Expansion - Organic — excluded by design:
already-converted customers).

**Cleanup record (2026-06-07):** audited all 97 conversions created since 2024-01-01; 55 were
misclassified (43 Inbound - Marketing, 10 Outbound - SDR/AE/Hybrid, 2 In+Out Hybrid) including
26 won deals / **$185,559** wrongly credited to Inbound/Outbound. 54 corrected to
`Product - SS Customer`. 1 outstanding: Checkr `006VS0000050nlpYAA` (Closed Lost, record type
`Mixmax - Renewal` blocks Product picklist values — also a Type/RecordType contradiction; left
flagged). Null `Opportunity_Source_Details__c` exists ONLY on Renewal-type opps (389 since 2024) — by design.
**Sweep 2 (same day):** all opps on RT `Mixmax - Conversion - Direct Sales` regardless of Type —
3 more fixed (Citrus Patrimonial, SumUp won $4,854, Truckbase.io incl. Type correction
InApp Expansion→Convert SS to DS). Conversion RT now 0 non-Product.
**Sweep 3 (same day, Heath expanded scope to all-time on Net New DS + Conversion DS RTs):**
339 of 346 pre-2024 legacy conversions on Net New DS corrected — including ALL 182 won deals
($1,264,596 all-time bookings moved to Product). 7 unfixable, all Closed Lost ($0 won impact):
blocked by the "Please choose a specific Product Gap" validation rule (null `Product_Gaps__c`
on 2017–2022 records; do not fabricate a value — admin can bypass if ever needed). Post-sweep
all-time Product won = 363 deals / $2,071,131. Remaining known non-Product conversions sit on
Expansion - Organic (138) and Expansion - DS (28) RTs + 1 Renewal (Checkr) — out of rule scope.

### ⚠️ PRODUCT-CHANNEL OVERRIDE — SS→DS conversions (Heath-confirmed 2026-06-06)

**Every `Opportunity.Type = 'Convert SS to DS'` belongs to the PRODUCT channel** for any
channel/motion/funnel analysis — **regardless of the account's `Channel_Source__c` value.**

Why: a self-serve→direct-sales conversion is the product-led motion by definition, but the
account keeps its *original* lead-source stamp (usually `Inbound` — how the self-serve signup
first arrived). A naive `Channel_Source__c = 'Product'` filter therefore misses the product
motion almost entirely (found 1 win where the real number was **16 wins / $79.9K**, Jan 2025 →
May 2026 — which reconciles to the team's ~$80K product bookings figure).

Canonical motion definitions for new-logo funnel work:

```
INBOUND  motion = Type = 'New Business'      AND Account.Channel_Source__c = 'Inbound'
OUTBOUND motion = Type = 'New Business'      AND Account.Channel_Source__c = 'Outbound'
PRODUCT  motion = Type = 'Convert SS to DS'  (ANY channel stamp)
                  OR (Type = 'New Business' AND Account.Channel_Source__c = 'Product')
```

The three motions are mutually exclusive (a conversion is Product even on an Inbound-stamped
account). Exclude Expansion / Upsell / Cross-sell / Renewal types from new-logo channel analysis.

**Fallback heuristics (use ONLY when `Channel_Source__c` is null — which, as of 2026-06-05, is never on new-business opps).**

⚠️ The enum values below were refreshed 2026-06-05 to the **actual live-org `LeadSource` picklist**. The prior values (`'Inbound Web Form'`, `'Demo Request'`, `'SDR Sourced'`, `'Cold Outreach'`, `'Self-Serve Signup'`) **do not exist** in the org. Note `LeadSource` is messy — `Direct` is a ~70% catch-all — so this fallback is coarse; prefer `Channel_Source__c` always.

```
INBOUND   LeadSource IN (
            'Direct', 'Website', 'Organic Search', 'Google - Organic',
            'Sign-up', 'Referral', 'Employee Referral', 'Partner',
            'Webinar', 'Sponsorship', 'Other', 'Intercom', 'Capterra'
          )
OUTBOUND  LeadSource IN (
            'Outbound', 'Practical Prospecting', 'List Import', 'Linkedin'
          )
          OR Mixmax sequence enrollment exists on primary contact
PRODUCT   LeadSource IN ('Product', 'Virality')
          OR (Amplitude `_active` > 0 trailing 30d AND PQA threshold met)
```

The 3 channels are mutually exclusive at the account level. If a fallback heuristic produces multiple matches, priority is **Product > Inbound > Outbound** (lock-in #11 v5). NOTE: this LeadSource fallback under-counts Outbound (agency/SDR leads are often logged `Direct`); `Channel_Source__c` is authoritative and should be used whenever populated.

---

## 6. Glossary — operational definitions

| Term | Definition |
|---|---|
| **Active account** | `canonical_last_activity` (4-source) within last 30 days |
| **Ghost deal** | Open Opp with 4-source activity > 47 days |
| **Stuck deal** | Days in current stage > 2× rep's median for that stage |
| **Stale account note** | `Account_Notes_Last_Updated__c` > 180 days ago |
| **PLAN complete** | All 4 PLAN fields populated for current stage requirement |
| **Multi-thread** | ≥ 2 `OpportunityContactRole` records with `Contact.LastActivityDate` in last 30d |
| **Single-thread risk** | Multi-thread = false on Opp in Solution Validation or later |
| **Champion drop-off** | `OpportunityContactRole.IsPrimary` contact has no activity in 21+ days |
| **PQA threshold** | `_active` events at `gp:domain` ≥ 5 unique users in trailing 30d |
| **Ghost-Active** | Aero PES > 0 but **every** capability adoption tier = 'Never-adopted' |
| **Aero False-Negative** | Aero PES at floor (0 or 1) but ≥ 2 capabilities at 'Established' or higher |
| **Commit creep** | Opp moved `Commit → Best Case` in trailing 14 days |
| **3-tool consolidation target** | Account has 3+ tools in `Sales_Acceleration_Tool__c` |
| **Top-of-funnel ICP scream** | `CR_Sales_Team_Hiring__c >= 3` |

---

## 7. Canonical SOQL snippets

### Full account (all 22 GTM fields)

```sql
SELECT
  Id, Name, Website, Type, OwnerId, Owner.Email, LastActivityDate,
  DWH_DS_Customer_ARR__c, DWH_SS_Customer_ARR__c, DWH_Customer_Type__c, DWH_Forecasted_ARR__c,
  Problems_Account__c, Leverage_Alignment__c, Address_Decision_Dynamics__c, Next_Steps_Account__c,
  Decision_Maker__c, Decision_Maker_Title__c,
  Account_Notes__c, Account_Notes_Last_Updated__c,
  Growth_Potential__c, Upsell_Plan_Account__c,
  Email_Provider__c, CRM__c, Sales_Acceleration_Tool__c,
  Conversational_Intelligence_Competitor__c, Data_Enrichment_Competitor__c, Secondary_Competitor_Used__c,
  CR_Number_of_Employees__c, CR_CS_Team__c, CR_of_Sales_Team__c, CR_Sales_Team_Hiring__c,
  Aero_Account_Fit_Score__c, Aero_Account_Fit_Score_Tier__c, Aero_Blended_Score_Tier__c, Aero_Product_Engagement_Score__c,
  Product_Engagement_Verdict__c, Product_Engagement_Last_Run__c, Product_Engagement_Active_Latest__c, Aero_False_Negative__c,
  Account_Brief_URL__c, Account_Tier__c,
  Open_Renewal_ARR__c, RP_Renewal_Period_Start__c, RP_Renewal_Period_End__c,
  Past_Renewals__c, Last_Renewal_Touch__c, Days_Since_Last_Renewal_Touch__c,
  All_Purchased_Seats__c, Stripe_Subscription_Start_Date__c, Stripe_Subscription_End_Date__c,
  Implementation_Status__c, CSM__c, CSM_Text__c,
  Channel_Source__c
FROM Account WHERE {filter}
```

### Open opps for an AE with full PLAN

```sql
SELECT
  Id, Name, AccountId, Account.Name, Account.Website,
  StageName, ForecastCategoryName, Amount, CloseDate, Probability,
  LastActivityDate, LastModifiedDate, Owner.Email, Type,
  Problems_Account__c, Leverage_Alignment__c, Address_Decision_Dynamics__c, Next_Steps_Account__c,
  Loss_Reason__c, Competitor__c, Account.Channel_Source__c
FROM Opportunity
WHERE IsClosed = false AND Owner.Email = '{ae_email}'
ORDER BY CloseDate ASC
```

### Renewal pipeline (per CSM, days-out window)

```sql
SELECT Id, Name, AccountId, Account.Name, StageName, ForecastCategoryName,
       Amount, CloseDate, Owner.Email, Type
FROM Opportunity
WHERE Type = 'Renewal' AND IsClosed = false
  AND CloseDate <= NEXT_N_DAYS:{days_out}
  AND Owner.Email = '{csm_email}'
ORDER BY CloseDate ASC
```

### Closed-Won cohort (Pattern Analyst — Won mode)

```sql
SELECT Id, AccountId, Account.Name, Account.Website, Account.Type,
       Account.CR_Number_of_Employees__c, Account.Industry,
       Account.Email_Provider__c, Account.CRM__c, Account.Sales_Acceleration_Tool__c,
       Amount, CloseDate, Account.Channel_Source__c, Type, Probability, Owner.Email
FROM Opportunity
WHERE IsClosed = true AND IsWon = true AND CloseDate = LAST_N_MONTHS:6
```

### Closed-Lost cohort (Pattern Analyst — Lost mode)

```sql
SELECT Id, AccountId, Account.Name, Account.Website, Amount, CloseDate,
       StageName, Account.Channel_Source__c, Loss_Reason__c, Competitor__c, Owner.Email
FROM Opportunity
WHERE IsClosed = true AND IsWon = false
  AND StageName LIKE 'Closed Lost%' AND CloseDate = LAST_N_MONTHS:6
```

### Churn cohort (Pattern Analyst — Churn mode)

```sql
SELECT Id, AccountId, Account.Name, Account.Website,
       Account.DWH_DS_Customer_ARR__c, Account.DWH_SS_Customer_ARR__c,
       Account.CSM__c, Account.RP_Renewal_Period_End__c,
       Amount, CloseDate, Account.Channel_Source__c, Loss_Reason__c, Competitor__c
FROM Opportunity
WHERE Type = 'Renewal' AND IsClosed = true AND IsWon = false
  AND StageName = 'Closed Lost — Churn'
  AND CloseDate = LAST_N_MONTHS:12
```

---

## 8. Join patterns

### Cross-system: Account.Website → Amplitude `gp:domain`

Strip protocol + path → canonical "acme.com" → `gp:domain` filter in Amplitude.

`Account.Website = "https://www.acme.com/products"` → `acme.com`

### Cross-system: Contact.Email → Mixmax meeting + sequence APIs

The Contact's `Email` is the primary join key for cross-system queries.

---

## 9. What to do when a field is missing

If the question references a field that's not documented in this library:

1. **Do not invent a field name.** Salesforce orgs vary; what looks intuitive may not exist.
2. **Tell the user** — "That field isn't in the canonical library. Either it's an org-specific field I shouldn't assume exists, or the library needs an amendment."
3. **Ask** which field they actually mean OR offer to run a SFDC schema probe to discover it.
4. **If the field really exists and should be canonical**, propose adding it via Evolution Agent (PR to this library).

---

## 10. Source

This skill mirrors `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` (and `heath-gtm/Skill-Builder/SFDC_FIELD_LIBRARY.md`). When the library updates, this skill body updates with it.
