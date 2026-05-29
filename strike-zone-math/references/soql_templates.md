# SOQL Templates — Strike Zone Math

All field names verified against the Mixmax Salesforce org on 2026-05-27. Do not substitute alternates without re-verifying.

## Conventions

- `<COHORT_START>` and `<COHORT_END>` are date literals like `2026-02-01` and `2026-05-01`
- `<CHANNEL>` is one of `'Inbound'`, `'Outbound'`, `'Product'`
- `Account.Channel_Source__c` is a formula field and **non-groupable** in SOQL — filter on it, don't GROUP BY it
- New-business filter: always include `Opportunity.Type IN ('New Business', 'Convert SS to DS')` to exclude renewal-ladder stages
- The cohort anchor date field varies by channel:
  - Inbound → `Account.MQA_Date_2024__c`
  - Outbound → `Account.OQA_Date__c`
  - Product → `Account.Sales_PQA_Date_Account__c`

## Query 1 — Cohort size by channel

Per-channel cohort size for a given window. Run three times (one per channel) and combine.

```sql
-- Inbound cohort
SELECT COUNT(Id), CALENDAR_MONTH(MQA_Date_2024__c) m, CALENDAR_YEAR(MQA_Date_2024__c) y
FROM Account
WHERE MQA_Date_2024__c >= <COHORT_START>
  AND MQA_Date_2024__c < <COHORT_END>
  AND Channel_Source__c = 'Inbound'
GROUP BY CALENDAR_MONTH(MQA_Date_2024__c), CALENDAR_YEAR(MQA_Date_2024__c)
ORDER BY y, m
```

Outbound: swap `MQA_Date_2024__c` → `OQA_Date__c`, filter `Channel_Source__c = 'Outbound'`.
Product: swap to `Sales_PQA_Date_Account__c`, filter `Channel_Source__c = 'Product'`.

## Query 2 — Meeting booked from cohort

Count of cohort accounts where a new-business Opp exists with `Meeting_Set_Date__c` populated.

```sql
SELECT Account.Id accId, Account.Name, Account.MQA_Date_2024__c cohortDate,
       MIN(Meeting_Set_Date__c) firstMeeting
FROM Opportunity
WHERE Account.MQA_Date_2024__c >= <COHORT_START>
  AND Account.MQA_Date_2024__c < <COHORT_END>
  AND Account.Channel_Source__c = 'Inbound'
  AND Type IN ('New Business', 'Convert SS to DS')
  AND Meeting_Set_Date__c != NULL
  AND CreatedDate >= Account.MQA_Date_2024__c
GROUP BY Account.Id, Account.Name, Account.MQA_Date_2024__c
```

Meeting rate = `count(accounts with a meeting) / cohort_size`.

## Query 3 — Show rate

Of meetings that have happened, what fraction completed.

```sql
SELECT Meeting_Status__c, COUNT(Id)
FROM Opportunity
WHERE Account.MQA_Date_2024__c >= <COHORT_START>
  AND Account.MQA_Date_2024__c < <COHORT_END>
  AND Account.Channel_Source__c = <CHANNEL>
  AND Type IN ('New Business', 'Convert SS to DS')
  AND Meeting_Status__c IN ('Completed', 'No Show', 'Cancelled', 'Rescheduled')
GROUP BY Meeting_Status__c
```

Show rate = `Completed / (Completed + No Show + Cancelled + Rescheduled)`. Exclude `Pending Schedule` and `Scheduled` — they haven't happened yet.

## Query 4 — SQL count from cohort (Stage 0 reached)

```sql
SELECT COUNT_DISTINCT(AccountId)
FROM Opportunity
WHERE Account.MQA_Date_2024__c >= <COHORT_START>
  AND Account.MQA_Date_2024__c < <COHORT_END>
  AND Account.Channel_Source__c = <CHANNEL>
  AND Type IN ('New Business', 'Convert SS to DS')
  AND (StageName = '0 - Qualification' OR SQL__c = TRUE)
```

Meeting → SQL rate = `count(SQL accounts) / count(accounts with a meeting)`.

## Query 5 — SQO count from cohort (Stage 1 reached)

```sql
SELECT COUNT_DISTINCT(AccountId)
FROM Opportunity
WHERE Account.MQA_Date_2024__c >= <COHORT_START>
  AND Account.MQA_Date_2024__c < <COHORT_END>
  AND Account.Channel_Source__c = <CHANNEL>
  AND Type IN ('New Business', 'Convert SS to DS')
  AND (StageName = '1 - Discovery' OR SQO__c = TRUE OR SQO_Date__c != NULL)
```

SQL → SQO rate = `count(SQO accounts) / count(SQL accounts)`.

## Query 6 — Closed Won / Lost and win rate

```sql
SELECT IsWon, IsClosed, COUNT(Id), SUM(Amount), SUM(ARR__c), AVG(Amount)
FROM Opportunity
WHERE Account.MQA_Date_2024__c >= <COHORT_START>
  AND Account.MQA_Date_2024__c < <COHORT_END>
  AND Account.Channel_Source__c = <CHANNEL>
  AND Type IN ('New Business', 'Convert SS to DS')
  AND (SQO__c = TRUE OR StageName = '1 - Discovery' OR
       StageName LIKE '2 -%' OR StageName LIKE '3 -%' OR StageName LIKE '4 -%' OR
       StageName LIKE '5 -%' OR StageName IN ('Closed Won', 'Closed Lost'))
GROUP BY IsWon, IsClosed
```

Win rate (SQO → Won) = `Closed Won / (Closed Won + Closed Lost)`. In-flight opps (`IsClosed = FALSE`) shown separately.

## Query 7 — Touchpoints to first meeting

For each account in the cohort that booked a meeting, count distinct outbound activity events between cohort anchor date and first meeting date.

```sql
SELECT AccountId, COUNT_DISTINCT(Id) touchpoints,
       MIN(ActivityDate) firstTouch, MAX(ActivityDate) lastTouch
FROM Task
WHERE AccountId IN :cohort_account_ids
  AND ActivityDate >= :cohort_anchor_date_for_account
  AND ActivityDate <= :first_meeting_date_for_account
  AND (Type IN ('Email Sent', 'Call', 'LinkedIn Connect', 'LinkedIn InMail', 'SMS')
       OR MixmaxInsights__Is_Mixmax_Sequence_Activity__c = TRUE)
GROUP BY AccountId
```

This is parameterized — run per-account in a loop, or build a cohort table first and join. Skip inbound replies (`Type = 'Replied'` or `'Received'`) — those are prospect actions, not Mixmax touchpoints.

Avg touchpoints to meeting = `AVG(touchpoints)` across the cohort. Heath cares about the median too — Outbound has a long right tail.

## Query 8 — Cycle time decomposition

```sql
SELECT Id, AccountId,
       Account.MQA_Date_2024__c cohortDate,
       Meeting_Set_Date__c,
       SQO_Date__c,
       CloseDate,
       IsWon,
       Amount
FROM Opportunity
WHERE Account.MQA_Date_2024__c >= <COHORT_START>
  AND Account.MQA_Date_2024__c < <COHORT_END>
  AND Account.Channel_Source__c = <CHANNEL>
  AND Type IN ('New Business', 'Convert SS to DS')
  AND IsClosed = TRUE
  AND IsWon = TRUE
```

Compute in code:
- Days cohort → meeting = `Meeting_Set_Date__c - cohortDate`
- Days meeting → SQO = `SQO_Date__c - Meeting_Set_Date__c`
- Days SQO → close = `CloseDate - SQO_Date__c`
- Days cohort → close = `CloseDate - cohortDate`

## Query 9 — Per-rep drill (rep mode)

When the user names a rep, pull their cohort.

```sql
SELECT Id, AccountId, Account.Name, Account.Channel_Source__c,
       StageName, Amount, CreatedDate, CloseDate, IsWon, IsClosed,
       Meeting_Set_Date__c, Meeting_Status__c, SQO_Date__c
FROM Opportunity
WHERE OwnerId = '<rep_user_id>'
  AND Type IN ('New Business', 'Convert SS to DS')
  AND CreatedDate >= LAST_N_DAYS:90
ORDER BY CreatedDate DESC
```

Then compute the rep's per-gate conversion rates and compare to team baseline from queries 1–6.

## Query 10 — Segment breakdown (when leak might be segment-driven)

```sql
SELECT Segment__c, COUNT(Id)
FROM Account
WHERE MQA_Date_2024__c >= <COHORT_START>
  AND MQA_Date_2024__c < <COHORT_END>
  AND Channel_Source__c = <CHANNEL>
GROUP BY Segment__c
```

Note: `Segment__c` is also a formula field — same non-groupable caveat applies. If this errors, pull rows and group client-side.
