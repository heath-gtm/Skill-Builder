# SFDC Field Library — Single Source of Truth

**Purpose.** Every analyst, every workflow, every connector wrapper reads from this document. When a query needs a Salesforce field, the field name + meaning + canonical interpretation lives here. No analyst makes its own field decisions. Apples-to-apples consistency across every output the GTM team sees.

**Inheritance.** Every `SKILL.md` references this file by name. The `lib/connectors/salesforce.ts` in `heath-gtm/agent-runtime` reads field lists from this document (mirrored). When a field is added or its meaning shifts, **edit this file only** — every downstream analyst picks up the change.

**Versioning.** This document is git-tracked. Material changes require a PR (Evolution Agent generates them when it detects drift between analyst behavior and the library spec).

---

## Object hierarchy reference

```
Account  ──┬──► Opportunity ──► OpportunityContactRole ──► Contact
           │
           ├──► Contact (Account-direct)
           │
           ├──► Task   (WhatId = Account.Id)
           └──► Event  (WhatId = Account.Id)

Opportunity ──┬──► Task   (WhatId = Opportunity.Id)
              └──► Event  (WhatId = Opportunity.Id)

Contact ──┬──► Task   (WhoId = Contact.Id)
          └──► Event  (WhoId = Contact.Id)
```

The 4-source activity check (lock-in #16 v9.1) walks all 4 leaves whenever asking "is this account/opp active?"

---

## 1. Account object

### Standard fields

| Field | Purpose | Notes |
|---|---|---|
| `Id` | 18-char Account ID | Always preferred over Name for joins |
| `Name` | Display name | Not reliable for matching — use Website + DWH_Customer_Type__c |
| `Website` | Account domain | Strip protocol + path → canonical "acme.com" for cross-system join |
| `Type` | Customer / Prospect / etc. | Cross-check with `DWH_Customer_Type__c` (warehouse source of truth) |
| `OwnerId` / `Owner.Email` | AE who owns the account | Maps to `karan@mixmax.com` etc. for per-rep filtering |
| `Industry` | Industry tag | Use only with `CR_Number_of_Employees__c` for ICP filtering |
| `NumberOfEmployees` | SFDC headcount | **Stale** — prefer `CR_Number_of_Employees__c` (Common Room refresh) |
| `CreatedDate` | When the Account was added | For "first 90 days" milestone calc |
| `LastActivityDate` | Last logged activity on the Account | **Part of 4-source check — never read alone** (see § 8) |

### DWH-sourced ARR + customer type (warehouse → SFDC sync)

| Field | Definition | Used by |
|---|---|---|
| `DWH_DS_Customer_ARR__c` | Direct Sales customer ARR (sales-led contracts) | Book-of-Business, Renewal-Health, Customer Success agents |
| `DWH_SS_Customer_ARR__c` | Self-Serve customer ARR (Stripe-billed monthly→annual) | Book-of-Business, Self-Serve attribution |
| `DWH_Customer_Type__c` | Customer / Prospect / Churned / Free / Paused | **Authoritative** — overrides standard `Type` field |
| `DWH_Forecasted_ARR__c` | CRO-locked forecast ARR for the account | Pipeline-Creation, Sales Leader briefings |

### The 4 PLAN fields (Mixmax-built methodology, NEVER MEDDIC — lock-in #26)

| Field | PLAN Letter | When required |
|---|---|---|
| `Problems_Account__c` | **P**roblems | Required by Discovery stage |
| `Leverage_Alignment__c` | **L**everage Alignment | Required by Solution Validation |
| `Address_Decision_Dynamics__c` | **A**ddress Decision Dynamics | Required by Proposal |
| `Next_Steps_Account__c` | **N**ext Steps | Required by Negotiation + Commit |

**Validation rule (the BS detector — lock-in #26):**
```
if Stage = 'Discovery'           and Problems_Account__c           is null → PLAN_GAP
if Stage = 'Solution Validation' and Leverage_Alignment__c         is null → PLAN_GAP
if Stage = 'Proposal'            and Address_Decision_Dynamics__c  is null → PLAN_GAP
if Stage = 'Negotiation'         and Next_Steps_Account__c         is null → PLAN_GAP
if ForecastCategoryName = 'Commit' and ANY of the 4 PLAN fields is null → COMMIT_RISK
```

When PLAN is incomplete, **always name the missing field** in output, never just "PLAN incomplete."

### Decision maker fields

| Field | Definition |
|---|---|
| `Decision_Maker__c` | Named decision maker contact (text or contact ref) |
| `Decision_Maker_Title__c` | Their title at the account |

A null `Decision_Maker__c` at Proposal stage = CRM hygiene flag (Coaching Analyst surfaces).

### Account notes (the "rep's narrative")

| Field | Definition |
|---|---|
| `Account_Notes__c` | Free-text rep narrative on the account |
| `Account_Notes_Last_Updated__c` | Timestamp of last update |

**Staleness rule:** Account Notes >180 days old = stale (Coaching Analyst surfaces; Book-of-Business flags).

### Growth + upsell intent

| Field | Definition |
|---|---|
| `Growth_Potential__c` | Picklist: Low / Medium / High — CSM-set growth potential |
| `Upsell_Plan_Account__c` | Free-text upsell motion plan |

### Tech stack + competitive intel

| Field | Definition |
|---|---|
| `Email_Provider__c` | Outlook / Gmail — needed for product fit |
| `CRM__c` | Salesforce / HubSpot / Other — competitive context |
| `Sales_Acceleration_Tool__c` | Outreach / SalesLoft / Apollo / Yesware / Cursor — **3-tool displacement target** when 3+ tools listed (lock-in #26) |
| `Conversational_Intelligence_Competitor__c` | Gong / Chorus / etc. |
| `Data_Enrichment_Competitor__c` | ZoomInfo / Apollo / Lusha / etc. |
| `Secondary_Competitor_Used__c` | Any other competitive product in use |

### Common Room enriched fields (CR_*)

| Field | Definition |
|---|---|
| `CR_Number_of_Employees__c` | **Use this over standard NumberOfEmployees** — Common Room refresh |
| `CR_CS_Team__c` | Estimated CS team size |
| `CR_of_Sales_Team__c` | Estimated sales team size |
| `CR_Sales_Team_Hiring__c` | Count of sales hires in last 90d — **≥3 = top-of-funnel ICP signal** (lock-in #26) |

### Aero scoring fields

| Field | Definition |
|---|---|
| `Aero_Account_Fit_Score__c` | 0-100 fit score |
| `Aero_Account_Fit_Score_Tier__c` | A / B / C / D tier |
| `Aero_Blended_Score_Tier__c` | Composite tier (fit + engagement) |
| `Aero_Product_Engagement_Score__c` | 0-100 product engagement score — **has two known failure modes:** Aero False-Negative + Ghost-Active (lock-in #14 v7) |

### Product Engagement Story writeback fields (managed by Amplitude Analyst)

| Field | Definition | Written by |
|---|---|---|
| `Product_Engagement_Verdict__c` | Picklist: Power / Established / Emerging / Dormant / Untouched / Ghost-Active / Aero-False-Negative | `amplitude-analyst` (gated writeback) |
| `Product_Engagement_Last_Run__c` | ISO datetime of last Product Engagement Story run | `amplitude-analyst` |
| `Product_Engagement_Active_Latest__c` | Latest week's `_active` user count for the domain | `amplitude-analyst` |
| `Aero_False_Negative__c` | Boolean — true when Aero PES floor + real adoption present | `amplitude-analyst` |

### Account brief URL (one-stop deep link)

| Field | Definition |
|---|---|
| `Account_Brief_URL__c` | Stable URL to the canonical account brief on `mixmaxhq/GTM-account-briefs` GitHub Pages |

### Account tiering

| Field | Definition |
|---|---|
| `Account_Tier__c` | Tier 1 / 2 / 3 — used for prioritization workflows |

### Renewal-related fields (read by Renewal-Health + Book-of-Business)

| Field | Definition |
|---|---|
| `Open_Renewal_ARR__c` | ARR locked into the current open renewal opportunity |
| `RP_Renewal_Period_Start__c` | Renewal period start date |
| `RP_Renewal_Period_End__c` | Renewal period end date (the renewal day) |
| `Past_Renewals__c` | Count of prior renewals — proxy for tenure |
| `Last_Renewal_Touch__c` | Date of last renewal-conversation activity |
| `Days_Since_Last_Renewal_Touch__c` | Computed days since last touch — `>30` = renewal-track ghost |
| `All_Purchased_Seats__c` | Total paid seats — denominator for expansion math |
| `Stripe_Subscription_Start_Date__c` | When the Stripe sub started (subscription tenure) |
| `Stripe_Subscription_End_Date__c` | When the Stripe sub ends (for Self-Serve churn timing) |
| `Implementation_Status__c` | New customer onboarding state (Onboarding Analyst reads) |
| `CSM__c` / `CSM_Text__c` | Assigned CSM (record ref + text fallback) |

### Channel attribution (source of the lead) — CANONICAL

| Field | Definition |
|---|---|
| `Channel_Source__c` | **THE canonical channel attribution field.** Formula (text) on Account = the source of the lead. Values: `Inbound` / `Outbound` / `Product` (see § 5). Channel is attributed at the **account** level; an opportunity inherits its account's channel via `Opportunity.Account.Channel_Source__c`. **Never** use `Opportunity.Channel__c` for attribution. Formula field — non-groupable in SOQL: filter on it, never `GROUP BY`. |

---

## 2. Opportunity object

### Standard fields

| Field | Purpose |
|---|---|
| `Id` | 18-char Opp ID |
| `Name` | Display name |
| `AccountId` | Parent account |
| `Account.Name` | Joined account name |
| `Account.Website` | Joined domain |
| `StageName` | Current stage (see § 3) |
| `Amount` | Opp value (USD) |
| `CloseDate` | Expected close date |
| `IsClosed` | true for Closed Won / Closed Lost |
| `LastActivityDate` | Opp-level last activity — **part of 4-source check, never read alone** |
| `LastModifiedDate` | Last record update (any field) |
| `OwnerId` / `Owner.Email` | AE owner |
| `Type` | Opportunity type — New Business / Renewal / Expansion / etc. |
| `Probability` | Stage-derived close probability |

### Custom Opportunity fields

| Field | Definition |
|---|---|
| `ForecastCategoryName` | Commit / Best Case / Pipeline / Omitted — see § 4 |
| `Loss_Reason__c` | Why we lost (when Closed Lost) — feeds Pattern Analyst |
| `Competitor__c` | Who we lost to (when Closed Lost) — feeds Pattern Analyst |
| `Channel__c` | ⚠️ **Legacy formula — NOT the channel attribution field.** Values (`Direct` / `Virality & Product` / `Other/Unknown`) do not map to the lead source and disagree with the account's true channel. Use `Account.Channel_Source__c` for channel attribution — see § 5 |

### Opportunity Contact Roles

`OpportunityContactRole` is the join object that tracks which contacts are on the deal + their role. Read via:
```
SELECT ContactId, Contact.Name, Contact.Email, Contact.Title, Contact.MobilePhone, Role, IsPrimary
FROM OpportunityContactRole WHERE OpportunityId = '{opp_id}'
```

**Multi-thread rule:** `< 2 contact roles` in last 30 days = single-thread risk flag.

---

## 3. Opportunity stage canonical values

```
Discovery
Solution Validation
Proposal
Negotiation
Closed Won
Closed Lost — Pass
Closed Lost — Lost
Closed Lost — Churn  (for renewal opportunities that churn)
```

**Mappings:**

| Stage | PLAN field required for COMMIT | Deal-Health threshold |
|---|---|---|
| Discovery | Problems_Account__c | OK to be Pipeline category |
| Solution Validation | + Leverage_Alignment__c | Should be Best Case at this point |
| Proposal | + Address_Decision_Dynamics__c | Commit-eligible — full PLAN required |
| Negotiation | + Next_Steps_Account__c | Commit-default — full PLAN + Decision_Maker__c |

---

## 4. ForecastCategoryName interpretation

```
Commit       AE will hit it. If they miss, it's a forecast accuracy issue.
Best Case    AE believes it can close but conditions still needed.
Pipeline     Real deal but uncertain timing.
Omitted      Closed Won, Closed Lost, or excluded by rep judgment.
```

**Commit Creep Watch (Deal-Health Analyst):** any deal that moved Commit → Best Case in trailing 14 days = surface to Sales Leader.

---

## 5. Channel classification (canonical — used by every channel-aware analyst)

**Canonical attribution field: `Account.Channel_Source__c`** — a formula (text) field = the source of the lead. This is the SINGLE source of truth for channel. Read it directly; do not reconstruct channel from heuristics when this field is populated.

```
INBOUND      Account.Channel_Source__c = 'Inbound'    (lead came to us — web form, demo request, MQA)
OUTBOUND     Account.Channel_Source__c = 'Outbound'   (we went to them — SDR/AE sourced, OQA)
PRODUCT      Account.Channel_Source__c = 'Product'    (self-serve signup / PQA — product-led)
```

**Channel is attributed at the Account level (the source of the lead). An Opportunity inherits the channel of its Account — read `Opportunity.Account.Channel_Source__c`. Never derive channel from the Opportunity alone.**

⚠️ **Do NOT use `Opportunity.Channel__c`.** It is a separate legacy formula whose values (`Direct`, `Virality & Product`, `Other/Unknown`, …) do not map to the lead source and frequently disagree with the account's true channel (e.g. an `Outbound` account shows `Virality & Product` on the opp). It is not the channel attribution field.

`Channel_Source__c` is a formula field — **non-groupable in SOQL. Filter on it (`WHERE Channel_Source__c = 'Outbound'`); never `GROUP BY Channel_Source__c`.**

**Fallback heuristics (use ONLY when `Channel_Source__c` is null):**
```
INBOUND   LeadSource IN (
            'Inbound Web Form', 'Demo Request', 'Content Download',
            'Pricing Page', 'Sales Inquiry'
          )
OUTBOUND  LeadSource IN (
            'SDR Sourced', 'AE Sourced', 'Cold Outreach', 'List Import'
          )
          OR Mixmax sequence enrollment exists on primary contact
PRODUCT   Account.Website domain has Amplitude `_active` > 0 in trailing 30d
          AND (LeadSource = 'Self-Serve Signup' OR PQA threshold met)
```

The 3 channels are mutually exclusive at the account level. If a fallback heuristic produces multiple matches, priority is **Product > Inbound > Outbound** (lock-in #11 v5).

---

## 6. Contact object

| Field | Purpose |
|---|---|
| `Id` | Contact ID |
| `Name` / `FirstName` / `LastName` | Display |
| `Email` | **Primary key for cross-system join** with Mixmax + FullEnrich |
| `Phone` | Office phone |
| `MobilePhone` | Direct dial — FullEnrich enrichment overwrites stale CRM (lock-in #13) |
| `Title` | Role at company |
| `AccountId` | Parent account |
| `LeadSource` | How the contact entered the system — see § 5 for canonical values |
| `LastActivityDate` | Last logged activity on the contact — **part of 4-source check** |

**Default contact query order:**
```
ORDER BY LastActivityDate DESC NULLS LAST
LIMIT 25
```

Contacts with no `LastActivityDate` after enrichment = ghost-contact (rep should reach out or remove from book).

---

## 7. Task + Event objects

Used **only** for the 4-source activity check (§ 8). Never read alone for "is this active?" decisions.

### Task

| Field | Purpose |
|---|---|
| `WhatId` | Account.Id OR Opportunity.Id |
| `WhoId` | Contact.Id (when contact-level) |
| `ActivityDate` | When the task happened |
| `Status` | Filter to `Status = 'Completed'` — drafts don't count |
| `Subject` | Brief description (audit only) |
| `Type` | Call / Email / etc. (audit only) |

### Event

| Field | Purpose |
|---|---|
| `WhatId` | Account.Id OR Opportunity.Id |
| `WhoId` | Contact.Id (when contact-level) |
| `ActivityDate` | Event date |
| `Subject` | Event title (audit only) |

---

## 8. The 4-source activity check (canonical formula — lock-in #16 v9.1)

**THE RULE.** Every "days since last activity" claim — for any account, opportunity, or contact — must be computed as the MAX of all four sources below. Reading `Account.LastActivityDate` or `Opportunity.LastActivityDate` alone systematically misclassifies real activity as silence (because reps log emails/meetings at the Account or Contact level, not the Opp level).

### Formula

```sql
canonical_last_activity = MAX(
  Account.LastActivityDate,
  Opportunity.LastActivityDate,
  (SELECT MAX(ActivityDate) FROM Task
     WHERE Status = 'Completed'
       AND (WhatId = '{account_or_opp_id}' OR WhoId IN (SELECT Id FROM Contact WHERE AccountId = '{account_id}'))),
  (SELECT MAX(ActivityDate) FROM Event
     WHERE (WhatId = '{account_or_opp_id}' OR WhoId IN (SELECT Id FROM Contact WHERE AccountId = '{account_id}')))
)

days_dark = today - canonical_last_activity
```

### Failure modes the rule prevents

```
1. Account-level email logged → Opp.LastActivityDate stays null →
   single-field read says "no activity" but Account.LastActivityDate is yesterday.

2. Meeting logged on Contact, not on Opp → Opp.LastActivityDate stays null →
   single-field read says "ghost" but Event on Contact shows fresh meeting.

3. Discovery call held without subsequent Opp logging → Opp shows null but
   a Task with Subject='Demo' was completed 3 days ago.
```

**The Daily Drop bug (May 2026) was caused by single-field reads.** Lock-in #16 v9.1 mandates the 4-source check. Every analyst must implement it via `salesforce_query_activities()` (the canonical tool) — never inline a single-source query.

---

## 9. Canonical SOQL snippets (battle-tested — every analyst uses these)

### A. Get the full account record with all 22 GTM fields

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
FROM Account
WHERE {account_filter}
```

### B. Get open opportunities for an AE with full PLAN

```sql
SELECT
  Id, Name, AccountId, Account.Name, Account.Website,
  StageName, ForecastCategoryName, Amount, CloseDate, Probability,
  LastActivityDate, LastModifiedDate, Owner.Email, Type,
  Problems_Account__c, Leverage_Alignment__c, Address_Decision_Dynamics__c, Next_Steps_Account__c,
  Loss_Reason__c, Competitor__c, Account.Channel_Source__c
FROM Opportunity
WHERE IsClosed = false
  AND Owner.Email = '{ae_email}'
ORDER BY CloseDate ASC
```

### C. Get all contacts on an account (for multi-thread + decision-maker checks)

```sql
SELECT Id, Name, FirstName, LastName, Email, Phone, MobilePhone, Title, LeadSource, AccountId, LastActivityDate
FROM Contact
WHERE AccountId = '{account_id}'
ORDER BY LastActivityDate DESC NULLS LAST
LIMIT 25
```

### D. Opportunity Contact Roles (multi-thread check)

```sql
SELECT
  OpportunityId, ContactId, Role, IsPrimary,
  Contact.Name, Contact.Email, Contact.Title, Contact.MobilePhone
FROM OpportunityContactRole
WHERE OpportunityId IN ({opp_id_list})
```

### E. 4-source activity check (the canonical formula from § 8)

Use the `salesforce_query_activities()` tool in agent-runtime — never inline.

### F. Renewal pipeline (per CSM, days-out window)

```sql
SELECT
  Id, Name, AccountId, Account.Name, StageName, ForecastCategoryName,
  Amount, CloseDate, Owner.Email, Type
FROM Opportunity
WHERE Type = 'Renewal'
  AND IsClosed = false
  AND CloseDate <= NEXT_N_DAYS:{days_out}
  AND Owner.Email = '{csm_email}'
ORDER BY CloseDate ASC
```

### G. Closed-Won cohort (for Pattern Analyst — Won mode)

```sql
SELECT
  Id, AccountId, Account.Name, Account.Website, Account.Type,
  Account.CR_Number_of_Employees__c, Account.Industry,
  Account.Email_Provider__c, Account.CRM__c, Account.Sales_Acceleration_Tool__c,
  Amount, CloseDate, Account.Channel_Source__c, Type, Probability,
  Owner.Email,
  (SELECT Role, IsPrimary, Contact.Title FROM OpportunityContactRoles)
FROM Opportunity
WHERE IsClosed = true AND IsWon = true
  AND CloseDate = LAST_N_MONTHS:6
```

### H. Closed-Lost cohort (Pattern Analyst — Lost mode)

```sql
SELECT
  Id, AccountId, Account.Name, Account.Website,
  Amount, CloseDate, StageName, Account.Channel_Source__c,
  Loss_Reason__c, Competitor__c,
  Owner.Email
FROM Opportunity
WHERE IsClosed = true AND IsWon = false
  AND StageName LIKE 'Closed Lost%'
  AND CloseDate = LAST_N_MONTHS:6
```

### I. Churn cohort (Pattern Analyst — Churn mode)

```sql
SELECT
  Id, AccountId, Account.Name, Account.Website,
  Account.DWH_DS_Customer_ARR__c, Account.DWH_SS_Customer_ARR__c,
  Account.CSM__c, Account.RP_Renewal_Period_End__c,
  Amount, CloseDate, Account.Channel_Source__c, Loss_Reason__c, Competitor__c
FROM Opportunity
WHERE Type = 'Renewal' AND IsClosed = true AND IsWon = false
  AND StageName = 'Closed Lost — Churn'
  AND CloseDate = LAST_N_MONTHS:12
```

---

## 10. Join patterns

### Account → Opp → Contact (full deal context)

```
1. Pull Account with the 22 GTM fields (Snippet A)
2. Pull all open Opps for AccountId (Snippet B)
3. Pull all OpportunityContactRoles for the opp set (Snippet D)
4. Pull all Contacts on the Account (Snippet C)
5. Compute 4-source activity per opp + per account (use canonical tool, § 8)
```

### Cross-system: Account.Website → Amplitude `gp:domain`

```
Account.Website (strip protocol + path) → canonical "acme.com"
                                       ↓
                                       gp:domain filter in Amplitude
```

Acme `Website = "https://www.acme.com/products"` → canonical domain = `acme.com`.

### Cross-system: Contact.Email → Mixmax + FullEnrich

The Contact's primary `Email` is the canonical join key. Mixmax sequence enrollment + meeting history queries use email arrays. FullEnrich identity validation uses email + LinkedIn.

---

## 11. Decisions glossary

| Term | Operational definition |
|---|---|
| **Active account** | `canonical_last_activity` (4-source) within last 30 days |
| **Ghost deal** | Open Opp with 4-source activity > 47 days |
| **Stuck deal** | Days in current stage > 2× rep's median for that stage |
| **Stale account note** | `Account_Notes_Last_Updated__c` > 180 days ago |
| **PLAN complete** | All 4 PLAN fields populated for current stage requirement |
| **Multi-thread** | ≥ 2 OpportunityContactRoles with `Contact.LastActivityDate` in last 30d |
| **Single-thread risk** | Multi-thread = false on an Opp in Solution Validation or later |
| **Champion drop-off** | OpportunityContactRole.IsPrimary contact has no activity in 21+ days |
| **PQA threshold met** | `_active` events at `gp:domain` ≥ 5 unique users in trailing 30d |
| **Ghost-Active** | Aero PES > 0 but **every** capability adoption tier = 'Never-adopted' |
| **Aero False-Negative** | Aero PES at floor (0 or 1) but ≥ 2 capabilities at 'Established' or higher |
| **Commit creep** | Opp moved from `ForecastCategoryName = 'Commit'` → 'Best Case' in trailing 14 days |
| **3-tool consolidation target** | Account has 3+ tools in `Sales_Acceleration_Tool__c` |
| **Top-of-funnel ICP scream** | `CR_Sales_Team_Hiring__c >= 3` |

---

## 12. Inheritance contract for SKILL.md files

Every analyst SKILL.md includes this block in its body, before the output-format example:

```markdown
## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:
- {list fields used}
- {note any computed values via canonical tool, e.g., "canonical_last_activity
  via salesforce_query_activities() — never inline single-source"}

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
```

---

## 13. Inheritance contract for the runtime connector code

`heath-gtm/agent-runtime/lib/connectors/salesforce.ts` mirrors every field listed in this document inside its SOQL queries. The `description:` strings on each tool spec reference this file by name.

When a field is added to this library, the corresponding connector tool gets a 1-line PR adding it to the SELECT clause. Evolution Agent generates these PRs.

---

## 14. Adding a new field (the process)

1. New field gets defined here first (with definition + business intent + downstream usage)
2. Salesforce.ts SELECT clause gets the field added
3. Any analyst that needs the field updates its SKILL.md inheritance block
4. Evolution Agent monitors usage; flags drift if an analyst starts reading a field not declared

Never invent fields in a SKILL.md or in code without amending this document first. Drift here = analyst inconsistency downstream = re-teaching session = wasted Heath time.

---

## 15. Adding a new picklist value (the process)

For picklist fields (`StageName`, `ForecastCategoryName`, `Type`, `DWH_Customer_Type__c`, `Product_Engagement_Verdict__c`):

> Note: channel is **not** a picklist — it is the `Account.Channel_Source__c` formula (Inbound / Outbound / Product, see § 5). Its values change only if the underlying formula is edited in Salesforce, not via this process.


1. Add the new value to the canonical list here
2. Document its meaning + the analyst rules that change for it
3. PR Evolution Agent's recommendation matrix if rules change

---

## 16. Field deprecation

When SFDC retires a field:

1. Mark it `~~deprecated~~` in this document with the date + reason
2. Remove from `salesforce.ts` SELECT clause
3. Audit every SKILL.md inheritance block — remove the field from each analyst's "reads" list
4. Notify the team in `#gtm-central` before merging

---

## Audit trail

| Date | Change |
|---|---|
| 2026-05-31 | Initial canonical library shipped — all 22 GTM custom fields + 4 PLAN fields + Aero scoring + PES writeback + renewal fields + 4-source activity formula + canonical channel classification + 9 reusable SOQL snippets + glossary |
