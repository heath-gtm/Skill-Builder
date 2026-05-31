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

---

## 2. Opportunity fields

### Standard
`Id`, `Name`, `AccountId`, `Account.Name`, `Account.Website`, `StageName`, `Amount`, `CloseDate`, `IsClosed`, `LastActivityDate`, `LastModifiedDate`, `OwnerId`, `Owner.Email`, `Type`, `Probability`

### Custom
`ForecastCategoryName`, `Loss_Reason__c`, `Competitor__c`, `Channel__c`

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

## 5. Channel classification (canonical)

```
INBOUND      LeadSource IN ('Inbound Web Form', 'Demo Request',
                            'Content Download', 'Pricing Page', 'Sales Inquiry')
              OR Opportunity.Channel__c = 'Inbound'

OUTBOUND     LeadSource IN ('SDR Sourced', 'AE Sourced', 'Cold Outreach',
                            'List Import')
              OR Mixmax sequence enrollment exists on primary contact
              OR Opportunity.Channel__c = 'Outbound'

PRODUCT      Account.Website domain has Amplitude `_active` > 0 in trailing 30d
              AND (LeadSource = 'Self-Serve Signup' OR PQA threshold met)
              OR Opportunity.Channel__c = 'Product'
```

If multiple criteria match, **priority is Product > Inbound > Outbound** (lock-in #11 v5). The 3 channels are mutually exclusive at the Opportunity level.

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
  Implementation_Status__c, CSM__c, CSM_Text__c
FROM Account WHERE {filter}
```

### Open opps for an AE with full PLAN

```sql
SELECT
  Id, Name, AccountId, Account.Name, Account.Website,
  StageName, ForecastCategoryName, Amount, CloseDate, Probability,
  LastActivityDate, LastModifiedDate, Owner.Email, Type,
  Problems_Account__c, Leverage_Alignment__c, Address_Decision_Dynamics__c, Next_Steps_Account__c,
  Loss_Reason__c, Competitor__c, Channel__c
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
       Amount, CloseDate, Channel__c, Type, Probability, Owner.Email
FROM Opportunity
WHERE IsClosed = true AND IsWon = true AND CloseDate = LAST_N_MONTHS:6
```

### Closed-Lost cohort (Pattern Analyst — Lost mode)

```sql
SELECT Id, AccountId, Account.Name, Account.Website, Amount, CloseDate,
       StageName, Channel__c, Loss_Reason__c, Competitor__c, Owner.Email
FROM Opportunity
WHERE IsClosed = true AND IsWon = false
  AND StageName LIKE 'Closed Lost%' AND CloseDate = LAST_N_MONTHS:6
```

### Churn cohort (Pattern Analyst — Churn mode)

```sql
SELECT Id, AccountId, Account.Name, Account.Website,
       Account.DWH_DS_Customer_ARR__c, Account.DWH_SS_Customer_ARR__c,
       Account.CSM__c, Account.RP_Renewal_Period_End__c,
       Amount, CloseDate, Channel__c, Loss_Reason__c, Competitor__c
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
