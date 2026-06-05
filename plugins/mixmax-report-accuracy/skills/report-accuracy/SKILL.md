---
name: report-accuracy
description: "Conduct a full accuracy audit of any Mixmax revenue report before publishing. Runs universal QA checks (data completeness, math accuracy, snapshot freshness, section coverage, cross-reference consistency, HTML integrity) plus report-specific checks. Produces a structured pass/warning/fail result with individual check details that feed into the cover page QA badge. Trigger on 'QA this report', 'run accuracy check', 'verify report', 'is this report ready to publish', 'report audit', 'check the numbers', 'validate before publishing', or any request to verify report accuracy before publishing."
---

# Report Accuracy Skill — Full QA Protocol

## Purpose

This skill is the **single source of truth** for report quality assurance across all Mixmax revenue reports. Its entire job is to conduct a comprehensive accuracy audit of any report before it is published.

**When to invoke:** After the HTML report is generated and before publishing to GitHub Pages. This skill runs between the final HTML generation step and the publish step in every workflow.

**Output:** A structured QA result object that feeds into the cover page QA badge, plus a human-readable summary for the user at the checkpoint.

---

## STEP 1 — Identify the Report Type

Determine which report is being audited. The report type dictates which checks to run.

**Supported report types:**
- `weekly` — Weekly GTM Revenue Report
- `monthly` — Monthly GTM Revenue Report
- `quarterly` — Quarterly GTM Revenue Report
- `churn` — Churn Analysis
- `closed-won` — Closed Won Analysis
- `closed-lost` — Closed Lost Analysis
- `ae-pipeline` — AE Pipeline Analysis
- `csm-book` — CSM Book of Business
- `sales-leader-weekly` — Sales Leader Weekly
- `cs-leader-weekly` — CS Leader Weekly
- `leader-update-slides` — Leader Update Slides

Read the generated HTML file to extract the report content for validation.

---

## STEP 2 — Run Universal Checks

These 6 checks apply to EVERY report regardless of type.

### Check 1: Data Completeness
**What:** Verify all expected rows/accounts/deals are present in the report.
**How:**
1. Read the source data (snapshot tab or Gen 1 sheet) and count the filtered rows
2. Count the items in the report (deal cards, account cards, rows in the summary table)
3. Compare: report count must equal source count
**Pass:** Counts match exactly
**Fail:** Any discrepancy — report the delta (e.g., "Expected 14 deals, found 12 — missing 2")
**Severity:** Critical

### Check 2: Math Accuracy
**What:** Verify all totals, subtotals, and computed metrics reconcile.
**How:**
1. Sum all individual line items in the report (per-deal amounts, per-account ARR, etc.)
2. Compare against the reported totals in the executive summary
3. Verify any computed metrics (weighted pipeline, coverage ratios, NRR/GRR, percentages)
4. Allow ±$1 rounding tolerance on dollar amounts, ±0.1% on percentages
**Pass:** All totals reconcile within tolerance
**Fail:** Any discrepancy beyond tolerance — report the exact variance
**Severity:** Critical

### Check 3: Snapshot Freshness
**What:** Verify the snapshot data is recent enough to be trustworthy.
**How:**
1. Extract the snapshot filename and date from the report metadata
2. Calculate days since snapshot
3. Apply threshold:
   - Weekly reports: ≤3 days
   - Monthly reports: ≤7 days
   - Quarterly reports: ≤7 days
   - On-demand (AE Pipeline, CSM Book): user-confirmed (always pass if user confirmed at checkpoint)
   - Leader weeklies: ≤3 days
   - Leader Update Slides: matches the base report's snapshot
**Pass:** Within threshold
**Warning:** Exceeds threshold but user confirmed usage at snapshot confirmation step
**Fail:** Exceeds threshold with no user confirmation
**Severity:** Warning (can be overridden by user)

### Check 4: Section Coverage
**What:** Verify all required sections of the report are populated.
**How:**
1. Check that every required section exists in the HTML (by section ID or heading)
2. Verify no section is empty or contains only placeholder text
3. For card-based reports (AE Pipeline, CSM Book): verify every item has all required card sections
**Pass:** All required sections present and populated
**Warning:** Optional sections missing (acceptable)
**Fail:** Required sections empty or missing
**Severity:** Warning

### Check 5: Cross-Reference Consistency
**What:** Verify numbers cited in different sections of the report agree with each other.
**How:**
1. Extract the executive summary metrics (total ARR, deal count, etc.)
2. Extract the same metrics from section headers, subtotals, and the full table
3. Compare: all instances of the same metric must show the same value
4. Check that tier/category subtotals sum to the grand total
**Pass:** All cross-references consistent
**Fail:** Any discrepancy — report which values disagree and where
**Severity:** Critical

### Check 6: HTML Integrity
**What:** Verify the report renders correctly with no visual errors.
**How:**
1. Check that all SVG elements have valid viewBox attributes and contain visible content
2. Verify no empty card containers (div with class but no content)
3. Check that all internal links (#anchors) have corresponding targets
4. Verify all Salesforce links follow the correct pattern (`https://mixmax.lightning.force.com/lightning/r/...`)
5. Verify external links (Google Drive, Gen 1 sheet) are properly formed
6. Check that the sidebar TOC entries all have matching section IDs
**Pass:** No structural HTML issues found
**Warning:** Minor issues (e.g., an optional link missing) that don't affect readability
**Fail:** Broken SVG, missing cards, orphaned links
**Severity:** Warning

---

## STEP 3 — Run Report-Specific Checks

Based on the report type identified in Step 1, run the additional checks below.

### Weekly Revenue Report
- [ ] **Rep count match:** Number of reps in Rep Summary = number of reps in source tab
- [ ] **Channel bookings sum:** Inbound + Outbound + Product + Expansion = Total Bookings
- [ ] **NRR/GRR validity:** NRR and GRR calculations are mathematically correct (GRR ≤ 100%, NRR can exceed 100%)
- [ ] **WoW comparison:** If prior week data is cited, verify the delta calculations

### Monthly Revenue Report
- [ ] **Monthly-to-weekly reconciliation:** Monthly totals should be reconcilable against the weekly reports from that month (if available — flag if weeklies are not referenced)
- [ ] **Risk register completeness:** Every risk entry has owner + dollar exposure + severity
- [ ] **Quarter-pacing math:** QTD actual + monthly forecast = quarterly projection (verify arithmetic)

### Quarterly Revenue Report
- [ ] **Quarterly-to-monthly reconciliation:** Quarterly totals reconcile against the 3 monthly reports
- [ ] **YTD calculations:** Year-to-date numbers are correct sums of quarterly actuals
- [ ] **Board-readiness:** Numbers are presented at appropriate precision for board consumption

### Churn Analysis
- [ ] **Churn account completeness:** All churned accounts from the Churn Analysis tab are present
- [ ] **Thematic categorization sum:** Sum of thematic category ARR = total churn ARR
- [ ] **Root cause coverage:** Every account has a root cause classification
- [ ] **Preventability verdicts:** Every account has a preventability assessment

### Closed Won Analysis
- [ ] **Deal completeness:** All closed-won deals in the period are present
- [ ] **Win pattern evidence:** Winning patterns are supported by actual deal data
- [ ] **Competitive intelligence sourcing:** Competitive mentions cite specific meeting transcripts or data

### Closed Lost Analysis
- [ ] **Deal completeness:** All closed-lost deals in the period are present
- [ ] **Loss pattern evidence:** Loss patterns are supported by actual deal data
- [ ] **Preventability verdicts:** Every deal has a preventability assessment
- [ ] **Competitive intelligence sourcing:** Competitive mentions cite specific data

### AE Pipeline Analysis
- [ ] **Deal filter verification:** All open deals for the AE are present (not closed-won, not closed-lost)
- [ ] **Tier assignment validity:** Every tier assignment follows the spec criteria (Must-Win/Should-Win/Long-Shot thresholds)
- [ ] **Octave play coverage:** Every Must-Win and Should-Win deal has an Octave strategic play
- [ ] **Amplitude coverage:** Every deal has an Amplitude usage classification
- [ ] **Stuck detection:** Stuck deals correctly flagged (>14 days in stage, overdue close, no meetings 30d+)
- [ ] **Top 2 contacts:** Every deal card has a Top 2 Most Engaged Contacts section (or explicit "No contacts found")
- [ ] **Salesforce links:** Every deal has both Account + Opportunity Salesforce links that follow the correct URL pattern

### CSM Book of Business
- [ ] **Account filter verification:** All accounts for the CSM are present
- [ ] **ARR total match:** Sum of per-account ARR = reported total ARR
- [ ] **Amplitude coverage:** Every account has an Amplitude usage classification
- [ ] **At-risk save plays:** Every at-risk account has a strategic save play
- [ ] **Renewal readiness badges:** Every renewing-next-90d account has a readiness badge (READY/AT RISK/NEEDS ATTENTION)
- [ ] **Top 2 contacts:** Every account card has a Top 2 Most Engaged Contacts section
- [ ] **Salesforce links:** Every account has a Salesforce Account link following the correct URL pattern

### Sales Leader Weekly
- [ ] **Rep badge justification:** Every rep badge (🟢🟡🔴) is supported by data in the card
- [ ] **Must-Win deal coverage:** All Must-Win deals have next actions
- [ ] **Pipeline/bookings source match:** Numbers match the Gen 1 source data

### CS Leader Weekly
- [ ] **NRR/GRR source match:** NRR and GRR numbers match the source data
- [ ] **Must-Save coverage:** Every Must-Save account has a save strategy
- [ ] **CSM book health badges:** Badge assignments are justified by underlying data

### Leader Update Slides
- [ ] **Source report match:** All numbers match their source reports exactly (slide briefs never override base data)
- [ ] **Named entity links:** All named accounts/deals have Salesforce links
- [ ] **No conflicting numbers:** Numbers in Sales slides don't contradict CS slides

---

## STEP 4 — Compile QA Result

Aggregate all check results into a structured QA result:

```
QA Result:
  Report Type: {type}
  Report File: {filename}
  QA Timestamp: {datetime}
  
  Overall Status: {PASS | WARNING | FAIL}
  
  Universal Checks:
    1. Data Completeness: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
    2. Math Accuracy: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
    3. Freshness: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
    4. Coverage: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
    5. Cross-Reference: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
    6. HTML Integrity: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
  
  Report-Specific Checks:
    7. {Check name}: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
    8. {Check name}: {✅ PASS | ⚠️ WARNING | ❌ FAIL} — {detail}
    ... (all report-specific checks)
  
  Overall Status Logic:
    - PASS: All checks pass (no warnings, no failures)
    - WARNING: No critical failures, but one or more warnings
    - FAIL: One or more critical failures (blocks publishing)
  
  Critical Failures (if any):
    - {Check N}: {description of failure}
  
  Warnings (if any):
    - {Check N}: {description of warning}
  
  Recommendation:
    - PASS: "Report is ready to publish."
    - WARNING: "Report has warnings. Review the flagged items and confirm with user before publishing."
    - FAIL: "Report has critical issues. Fix the following before publishing: {list}"
```

---

## STEP 5 — Present to User

Show the user a clean summary of the QA results at the checkpoint:

```
🔍 **Report Accuracy Audit — {Report Type}**

Overall: {✅ ALL CHECKS PASSED | ⚠️ PASSED WITH WARNINGS | ❌ FAILED — FIX REQUIRED}

{List each check with its status and a one-line description}

{If FAIL: "The following issues must be fixed before publishing:"}
{If WARNING: "The following items are flagged but can be overridden:"}
{If PASS: "All checks passed. Ready to publish."}
```

Ask the user: "QA is complete. {Recommendation}. Should I proceed to publish?"

---

## STEP 6 — Embed in Cover Page

Pass the QA result to the cover page generator, which uses it to render the QA badge:
- `PASS` → green badge with all check marks
- `WARNING` → yellow badge with warning indicators
- `FAIL` → red badge (this state should not be published — the workflow should have stopped)

If the user overrides warnings, note the override: "User override: Approved with warnings by {user name}"

---

## Troubleshooting

### "I can't access the source data to verify"
If the source snapshot or Gen 1 sheet is not accessible during QA:
- Flag the Data Completeness and Math Accuracy checks as ⚠️ WARNING with note "Source data not accessible for verification"
- Proceed with all other checks
- Note in the QA badge that source verification was not possible

### "The count is off by 1–2 items"
Before failing:
1. Check if the discrepancy is due to closed-won/closed-lost deals that changed status between snapshot and report generation
2. Check if it's a header row being counted
3. If explainable, mark as ⚠️ WARNING with explanation rather than ❌ FAIL

### "The HTML has minor rendering issues"
Minor issues (e.g., slightly off SVG alignment, optional section missing) → ⚠️ WARNING
Critical issues (missing cards, broken charts, missing Salesforce links) → ❌ FAIL

### "Numbers don't match but the difference is small"
Apply tolerance thresholds:
- Dollar amounts: ±$1 (rounding)
- Percentages: ±0.1%
- Counts: must be exact (no tolerance)
- Dates: must be exact

---

## Integration with Report Workflows

Every report task prompt should include a step that invokes this skill:

```
## STEP N — Report Accuracy Audit

Before publishing, run the Report Accuracy Skill:
1. Identify the report type
2. Run all universal checks against the generated HTML + source data
3. Run all report-specific checks
4. Compile the QA result
5. Present the summary to the user
6. If PASS or user-approved WARNING: embed the QA badge in the cover page and proceed to publish
7. If FAIL: stop and fix the identified issues before re-running QA
```
