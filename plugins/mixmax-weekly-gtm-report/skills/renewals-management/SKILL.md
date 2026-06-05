---
name: renewals-management
description: Should trigger on phrases about renewals, NRR, GRR, net revenue retention, gross revenue retention, churn, downgrade, at-risk accounts, CS summary, CSM renewals, VSB renewals, renewal pipeline, "how are renewals looking", customer success, retention, or any mention of the Renewals tab or CS Summary tab.
---

# Renewals Management Analysis

Analyze Mixmax customer success renewals, retention metrics, and at-risk accounts to inform weekly GTM reporting and CS strategy.

## Data Sources

- **CS Summary tab (GID: 1594569652)** — aggregated NRR/GRR metrics, renewals overview by segment (All, CSM Owned, VSB Owned), at-risk accounts
- **Renewals - This Year tab (GID: 1335996078)** — individual renewal records with Account Name, Account Record Type, # Past Renewals, Customer Account Tier, Account Owner, CSM, renewal dates, Previous Contract, Current ARR, Forecasted ARR, ARR Impact

## Salesforce Links

Every account referenced must link to Salesforce:
```
https://mixmax.lightning.force.com/lightning/r/Account/{AccountID}/view
```

## Key Metrics

### NRR (Net Revenue Retention)

- NRR % for All accounts, CSM Owned, VSB Owned
- NRR measures retention INCLUDING expansion — NRR > 100% means expansion outpaces churn
- Flag any segment with NRR below 80%

### GRR (Gross Revenue Retention)

- GRR % (ARR Retention) for All, CSM Owned, VSB Owned
- GRR % (Client Retention) for All, CSM Owned, VSB Owned
- GRR measures retention EXCLUDING expansion — always ≤ 100%
- ARR Retention = dollar-weighted, Client Retention = logo-weighted

### Renewals Overview

For each segment (All, CSM Owned, VSB Owned):
- # Accounts up for renewal
- # At Risk
- Forecasted ARR
- Previous Contract ARR
- ARR Impact ($ change)

## Analysis Framework

### 1. Retention Health Check

- Is NRR above or below 100%? By how much?
- Is GRR trending down? Compare to target.
- Which segment (CSM vs VSB) is driving retention issues?

### 2. At-Risk Identification

- List all accounts flagged as "At Risk" with:
  - Account name (linked to Salesforce)
  - Current ARR
  - Forecasted ARR
  - ARR Impact if lost/downgraded
  - CSM/Account Owner
  - Reason for risk (if available in notes)
- Sort by ARR Impact descending — biggest dollar risk first

### 3. Churn & Downgrade Analysis

- Total churn $ this period vs target/budget
- Total downgrade $ this period vs target/budget
- Are churn/downgrade running above or below plan?
- Identify specific accounts driving churn/downgrade

### 4. Renewal Timeline

- Which renewals are closing this month?
- Which are closing next month?
- Are any overdue (past renewal date but not yet processed)?
- What's the total ARR up for renewal in the next 30/60/90 days?

### 5. CSM Workload Distribution

- How many renewals per CSM?
- Any CSM with a disproportionate share of at-risk accounts?
- Flag capacity issues

## Output Guidelines

- **For Mixmax GTM Report (Org-Wide):** NRR/GRR headline numbers, total at-risk count, total ARR at risk. No individual account names or CSM names.
- **For CRO Report (Direct to CRO):** Full detail with individual accounts linked to Salesforce, CSM names, ARR impact, and risk reasons.
- **Color coding:**
  - Red = NRR below 80% or accounts at risk with >$10K ARR impact
  - Yellow = NRR 80-95% or accounts with any risk flag
  - Green = NRR above 95% and on track
- **Currency format:** $X,XXX
- **Percentage format:** 1 decimal place (e.g., 95.2%)
