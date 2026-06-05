---
name: quarterly-report-setup
description: >
  Set up the Mixmax Quarterly Revenue Report workflow. Use when the user says
  "set up quarterly report", "configure quarterly revenue report", "install quarterly
  GTM report", "create the quarterly report task", "how do I run the quarterly report",
  or similar. Guides the user through connecting required tools (Google Sheets,
  Chrome MCP, Notion, Slack, GitHub), verifying the Quarterly Snapshots folder,
  installing the quarterly Apps Script alongside the existing weekly + monthly scripts,
  creating the scheduled task, and running a dry-run. Authoritative source for the
  pre-run snapshot protocol (user takes BOTH Lookback + Lookahead snapshots before
  triggering the task).
---

# Quarterly Report Setup

This skill gets the Mixmax Quarterly Revenue Report workflow installed and running. It's the onboarding companion to the scheduled task prompt — run through this once per fresh Cowork and you're ready to close any quarter.

---

## Prerequisites checklist

Before running the first quarterly report, confirm all of the following are in place. If any item fails, the workflow will fail mid-run.

1. **Weekly and Monthly workflows are installed and healthy.** The quarterly report is a fresh cut from Gen 1, but monthly retrospective HTMLs provide optional cross-reference context. Confirm both `mixmax-weekly-gtm-report` and `mixmax-monthly-gtm-report` plugins are installed.

2. **Three monthly reports exist for the closing quarter** (strongly recommended). At `Revenue Reviews/Monthly Report/`, look for `Mixmax_Monthly_Report_{YYYY-MM}.html` and `CRO_Monthly_Report_{YYYY-MM}.html` for each of the 3 months. If 0–1 monthlies exist, the quarterly can still run but the First Flagged field in the risk register will degrade.

3. **Quarterly snapshot infrastructure (Apps Script + Drive folder).** The quarterly workflow reads from values-only Google Sheet snapshots produced by the Gen 1 Apps Script. Two menu items drive the workflow — **both are snapshot-only; neither writes to any cells**:
   - `RevOps Tools — Quarterly > Create Quarterly Lookback Snapshot` — run AFTER the final month of the quarter closes, while quarter-selection cells (if any) still point at the closed quarter. Creates `Gen1_Quarterly_Lookback_Snapshot_{QN YYYY}_{date}` in the Quarterly Snapshots Drive folder.
   - `RevOps Tools — Quarterly > Create Quarterly Lookahead Snapshot` — run AFTER the user has manually updated the Gen 1 dropdowns (monthly C2 cells, Rep/CS date ranges, and any Quarterly Summary quarter selectors) to the first month of the new quarter. Creates `Gen1_Quarterly_Lookahead_Snapshot_{QN YYYY}_{date}`.

   Both snapshots live in a dedicated **Quarterly Snapshots** Drive folder (parallel to the weekly + monthly snapshots folders). On first setup the user creates this folder and pastes its ID into `QCONFIG.QUARTERLY_SNAPSHOT_FOLDER_ID` in the Apps Script.

4. **Chrome MCP connected.** Used to click Apps Script menu items and fetch gviz CSVs from the snapshots.

5. **Notion MCP connected.** The quarterly workflow updates a Quarterly Notion hub page.

6. **Slack MCP connected.** Distributes to `#gtm-central`, `#gtm-leadership`, CRO DM, and (for the Board Snapshot) a dedicated Board/Exec channel or DM.

7. **GitHub PAT configured.** The quarterly task prompt uses the same PAT as weekly + monthly. Confirm write access to `heath-gtm/mixmax-revenue-reports`.

8. **Weekly RevOps Report Google Sheet is live.** Sheet ID: `1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY`. User must have edit access.

9. **Prior-quarter targets file exists** (optional). Located at `Revenue Reviews/Quarterly Report/{PriorQuarter}_Targets.md`. If this is the first quarterly run, the file won't exist yet — it'll be created at the end of this run.

---

## Connector list

| Connector | Used In | Required? |
|---|---|---|
| Chrome MCP | Menu clicks, gviz CSV extraction | Required |
| Notion MCP | Update Quarterly Notion hub | Required |
| Slack MCP | Distribute 4 reports | Required |
| Google Calendar MCP | Useful for scheduling board/review prep | Optional |
| Gmail MCP | Optional board-email handoff | Optional |

---

## Pre-run snapshot protocol (user takes BOTH snapshots before triggering the task)

Starting in v1.0.0, the quarterly workflow has no mid-run sheet handoff. Heath takes BOTH the Quarterly Lookback and Quarterly Lookahead snapshots BEFORE clicking Run Now on the scheduled task. Claude verifies both snapshots at Checkpoint 1 and then runs straight through without another sheet handoff.

**Division of responsibility:**
- **Heath (before running the task):** takes the Quarterly Lookback snapshot with dropdowns on the final month of the closing quarter (and any quarter-selection cells on the closed quarter). Then manually flips the 6 monthly dropdowns to the first month of the new quarter (plus any quarter-selection cells to the new quarter) and takes the Quarterly Lookahead snapshot.
- **Claude (during the task):** confirms both snapshots are present and fully populated at Checkpoint 1, then reads from them for retrospective + forward-looking analysis. Claude does NOT click any Apps Script menu items during the run and does NOT write dropdown cells.

### The dropdowns Heath flips between snapshots

Before taking the Quarterly Lookahead snapshot, Heath updates these cells to reflect the first month of the new quarter:
- Monthly Revenue Summary · C2 → "Month Year" label (e.g., "April 2026" for Q2 open)
- Monthly Bookings Summary · C2 → same "Month Year" label
- Rep Summary · E3 (start date) → 1st of new quarter's first month (e.g., 2026-04-01)
- Rep Summary · F3 (end date) → last day of new quarter's first month (e.g., 2026-04-30)
- CS Summary · E3 (start date) → same as Rep Summary E3
- CS Summary · F3 (end date) → same as Rep Summary F3

If the Quarterly Revenue Summary / Quarterly Bookings Summary tabs have a "For the Quarter of" selector (e.g., cell B2), Heath flips that to the new quarter too.

### Pre-run sequence

1. With dropdowns on the final month of the closing quarter, open Gen 1 and click `RevOps Tools — Quarterly > Create Quarterly Lookback Snapshot`. Confirm `Gen1_Quarterly_Lookback_Snapshot_{QN-YYYY}_{date}` appears in the Quarterly Snapshots folder.
2. Update all applicable dropdowns (monthly C2 + Rep/CS date ranges + any quarterly selectors) to the new quarter.
3. Click `RevOps Tools — Quarterly > Create Quarterly Lookahead Snapshot`. Confirm `Gen1_Quarterly_Lookahead_Snapshot_{QN-YYYY}_{date}` appears.
4. Trigger the `quarterly-revenue-report` scheduled task (Run Now).

### What Claude verifies at Checkpoint 1

Claude reads both snapshots' Manifest tabs via gviz CSV and confirms:
- **Lookback Manifest:** Snapshot Type = "Quarterly Lookback (retrospective)", Quarter Label matches the quarter Heath said he's closing, all 9 tabs OK with row counts > 0, plus spot-checks on key cells in Quarterly Revenue Summary + Quarterly Bookings Summary + CS Summary.
- **Lookahead Manifest:** Snapshot Type = "Quarterly Lookahead (forward-looking targets)", Quarter Label matches the new quarter, all 9 tabs OK, anchor cells show dropdowns on the new quarter's first month, target cells populated.

If anything looks off, Claude surfaces it at Checkpoint 1 and waits — no sheet writes, no re-snapshots from Claude's side.

### Extracting new-quarter targets from the Lookahead snapshot

Once the Lookahead snapshot is verified at Checkpoint 1, Claude extracts new-quarter targets via gviz CSV. For each tab, fetch:

```
https://docs.google.com/spreadsheets/d/{SNAPSHOT_ID}/gviz/tq?tqx=out:csv&gid={GID}
```

(The snapshot GIDs are per-file — read them from the snapshot's Manifest tab or by opening the snapshot in Chrome.)

**Targets to extract (Quarterly Revenue Summary + Quarterly Bookings Summary):**
- Net ARR Contribution targets for the new quarter: Total Net ARR, DS, SS
- DS channel targets: New Business, Expansion, Downgrade, Churn
- Self-Serve targets: Net New SS, Reactivation, Upgrade, Seat Exp/Contraction, Downgrade, Churn
- Bookings targets: Total, New Business, Expansion
- Pipeline targets by channel: Total, Inbound, Outbound, Product, Expansion
- Activity targets: Accounts Engaged, Meetings Booked, SQLs, SQOs
- Renewals targets for the new quarter: Forecasted ARR, NRR, GRR

Save captured targets to `Revenue Reviews/Quarterly Report/{NewQuarter}_Targets.md`. Include a `Source Snapshot:` line with the Lookahead snapshot URL so future runs can trace targets back.

---

## Step-by-step setup

### 1. Confirm Weekly + Monthly workflows are running

Ask: *"Have you run at least one monthly report for each of the 3 months in the quarter you want to close?"*

If no: send them to the monthly setup skill first. The quarterly can technically run without the monthlies, but the First Flagged column in the risk register will degrade and reconciliation against monthly reports won't be possible.

### 2. Install the quarterly Apps Script on the Gen 1 sheet

The quarterly script (`apps_script_quarterly_snapshot.gs`) is a STANDALONE addition — it does NOT replace the existing weekly + monthly script. It adds a new `RevOps Tools — Quarterly` menu with two items.

1. Open the Weekly RevOps Report (Gen 1) Google Sheet.
2. Extensions → Apps Script.
3. Create a new script file in the same project (File → New → Script). Name it `quarterly.gs`.
4. Paste the contents of `apps_script_quarterly_snapshot.gs`.
5. In the existing `onOpen()` function (from the weekly + monthly script), add a call to `addQuarterlyMenu_()` at the end. Save.
6. Reload the sheet — the new `RevOps Tools — Quarterly` menu should appear alongside the existing `RevOps Tools` menu.

### 3. Create the Quarterly Snapshots Drive folder and wire it up

1. In Google Drive, create a folder named **Quarterly Snapshots** (sibling to the existing Weekly + Monthly snapshot folders).
2. Open the folder and copy its folder ID from the URL (the string after `/folders/`).
3. In the Apps Script, set `QCONFIG.QUARTERLY_SNAPSHOT_FOLDER_ID` to that ID. Save.

### 4. Authorize the quarterly Drive scope

1. In Apps Script, open `quarterly.gs`.
2. Select `authorizeQuarterlyDrive` in the function dropdown and click Run.
3. Accept the Drive + Spreadsheet scopes in the OAuth prompt.
4. Confirm the Logger shows `Quarterly Snapshots folder: Quarterly Snapshots (OK)`.

### 5. Do a dry-run snapshot pair

1. Take a Lookback snapshot against whatever state the sheet is currently in. Confirm it lands in the Quarterly Snapshots folder and the Manifest tab has Snapshot Type, Quarter Label, all 9 tabs OK.
2. Take a Lookahead snapshot. Same verification.
3. Delete both dry-run snapshots before the real run.

### 6. Create the scheduled task

The task is created manually from Cowork:
- Task ID: `quarterly-revenue-report`
- Trigger: Manual (Run Now only) — no cron
- Prompt: the contents of `task_prompt.md` from this plugin

### 7. First real run

1. Take both quarterly snapshots (Lookback first, then flip dropdowns and take Lookahead).
2. Click Run Now on the `quarterly-revenue-report` task.
3. Answer the intake questions at Checkpoint 1.
4. Work through all 5 checkpoints.

---

## Troubleshooting

**`RevOps Tools — Quarterly` menu item missing.** The quarterly script wasn't installed or `addQuarterlyMenu_()` wasn't called from `onOpen()`. Reload the sheet after adding the call. If still missing, check the Apps Script execution log.

**Lookback or Lookahead snapshot fails on click.** Likely `QCONFIG.QUARTERLY_SNAPSHOT_FOLDER_ID` is still the placeholder. Set it to the real folder ID and re-run.

**Manifest shows "sheet not found" for a tab.** A tab was renamed or deleted in the Gen 1 sheet. Either restore the tab or update `QCONFIG.QUARTERLY_TABS` to match.

**gviz CSV returns empty from the snapshot.** The snapshot GIDs are per-file (new each run). Open the snapshot's Manifest tab in Chrome to read the correct GIDs.

**Monthly reports missing for a month of the quarter.** If only 1–2 monthlies exist, the quarterly still runs but First Flagged degrades. Note in the run log that cross-reference was partial. If 0 monthlies exist, recommend running the monthlies first before the quarterly.

**Prior-quarter targets file missing.** Not a blocker. Note in the run log that baseline targets were unavailable for QoQ comparison. Targets for the new quarter will still be captured and saved.

---

## First-run checklist

On first setup:
- [ ] Weekly + Monthly workflows confirmed healthy
- [ ] At least 2 monthlies exist for the closing quarter
- [ ] Quarterly Snapshots Drive folder created + ID wired
- [ ] Apps Script installed + `addQuarterlyMenu_()` called from `onOpen()`
- [ ] OAuth authorized via `authorizeQuarterlyDrive`
- [ ] Dry-run Lookback + Lookahead snapshots succeed
- [ ] Chrome + Notion + Slack MCPs verified
- [ ] Scheduled task `quarterly-revenue-report` created

Once all boxes are checked, you're ready to close your first quarter.
