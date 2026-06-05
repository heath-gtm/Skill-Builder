---
name: monthly-report-setup
description: >
  Set up the Mixmax Monthly Revenue Report workflow. Use when the user says 
  "set up monthly report", "configure monthly revenue report", "install monthly 
  GTM report", "create the monthly report task", "how do I run the monthly report", 
  or similar. Guides the user through connecting required tools (Google Sheets, 
  Chrome MCP, Notion, Slack, GitHub), verifying snapshot infrastructure, creating 
  the scheduled task, and running a dry-run. Also contains the sheet-reset 
  protocol executed during the monthly workflow.
---

# Monthly Report Setup

This skill gets the Mixmax Monthly Revenue Report workflow installed and running. It's the onboarding companion to the scheduled task prompt — run through this once per fresh Cowork and you're ready to close any month.

---

## Prerequisites checklist

Before running the first monthly report, confirm all of the following are in place. If any item fails, the workflow will fail mid-run.

1. **Weekly workflow is installed and healthy.** The monthly report consumes weekly reports as inputs. Confirm the `mixmax-weekly-gtm-report` plugin is installed and at least 4 weekly reports exist for the target month at `Revenue Reviews/Weekly Report/` or published to GitHub Pages.

2. **Monthly snapshot infrastructure (Apps Script + Drive folder).** The monthly workflow mirrors the weekly pattern: it reads from values-only Google Sheet snapshots produced by the Gen 1 Apps Script. Two menu items drive the workflow — **both are snapshot-only; neither writes to any cells**:
   - `RevOps Tools > Create Monthly Lookback Snapshot` — run AFTER the month closes, while dropdowns still point at the closed month. Creates `Gen1_Monthly_Lookback_Snapshot_{YYYY-MM}_{date}` in the Monthly Snapshots Drive folder.
   - `RevOps Tools > Create Monthly Lookahead Snapshot` — run AFTER the user has manually updated the 6 dropdowns to the new month. Creates `Gen1_Monthly_Lookahead_Snapshot_{YYYY-MM}_{date}` capturing the new-month targets. The script does NOT write dates — this avoids timezone/date-parsing drift. The user is the source of truth for the dropdowns.

   Both snapshots live in a dedicated **Monthly Snapshots** Drive folder (parallel to the weekly snapshots folder). On first run, the user creates this folder and pastes its ID into `CONFIG.MONTHLY_SNAPSHOT_FOLDER_ID` in the Apps Script. The script source is at `Revenue Reviews/Monthly Report/apps_script_monthly_snapshot.gs`.

3. **Chrome MCP connected.** Chrome MCP is used to click the two Apps Script menu items. Verify by running `mcp__Claude_in_Chrome__tabs_context_mcp` — if it errors, ask the user to install the Chrome extension.

4. **Notion MCP connected.** Step 12 updates the Monthly Notion page. Verify with `mcp__notion-fetch`.

5. **Slack MCP connected.** Step 8 and Step 11 send to `#gtm-central`, `#gtm-leadership`, and CRO DM.

6. **GitHub PAT configured.** The monthly task prompt contains the PAT. Confirm it still has write access to `heath-gtm/mixmax-revenue-reports`.

7. **Weekly RevOps Report Google Sheet is live.** Sheet ID: `1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY`. User must have edit access.

8. **Prior-month targets file exists** (optional but recommended). Located at `Revenue Reviews/Monthly Report/[Prior_Month]_[Year]_Targets.md`. If this is the first monthly run, the file won't exist yet — it'll be created at the end of this run.

---

## Connector list

These are the connectors/MCPs the monthly workflow uses:

| Connector | Used In | Required? |
|---|---|---|
| Chrome MCP | Sheet reset, gviz CSV extraction | Required |
| Notion MCP | Update monthly hub page | Required |
| Slack MCP | Distribute reports | Required |
| Google Calendar MCP | Not used directly, but useful for scheduling review meetings | Optional |
| Gmail MCP | Not used directly | Optional |

---

## Step-by-step setup

### 1. Confirm Weekly workflow is running

Ask the user: *"Have you run at least one weekly report for the month you want to close? The monthly report uses those weeklies as inputs."*

If no, send them to the weekly setup skill first. Don't proceed until they have weekly reports for the target month.

### 2. Install the combined Apps Script on the Gen 1 sheet

The combined `apps_script_monthly_snapshot.gs` file (in `Revenue Reviews/Monthly Report/`) is a drop-in replacement for the current weekly-only bound script. It preserves every weekly function and adds the two monthly menu items.

1. Open the Weekly RevOps Report (Gen 1) Google Sheet.
2. Extensions → Apps Script.
3. Replace the contents of `Code.gs` with the combined file.
4. Save. The `onOpen` trigger will refresh the `RevOps Tools` menu on the next sheet reload.

### 3. Create the Monthly Snapshots Drive folder and wire it up

1. In Google Drive, create a folder named **Monthly Snapshots** (sibling to the existing weekly snapshots folder).
2. Open the folder and copy its folder ID from the URL (the string after `/folders/`).
3. In the Apps Script, set `CONFIG.MONTHLY_SNAPSHOT_FOLDER_ID` to that ID. Save.

### 4. Smoke-test both menu items

1. Reload the Gen 1 sheet. `RevOps Tools` should now show:
   - Create Weekly Snapshot (existing)
   - Create Monthly Lookback Snapshot (new)
   - Create Monthly Lookahead Snapshot (new)
2. With the dropdowns on the closed month you want to lookback, run `Create Monthly Lookback Snapshot`. Confirm a file named `Gen1_Monthly_Lookback_Snapshot_{YYYY-MM}_{date}` appears in the Monthly Snapshots folder.
3. Open the snapshot's Manifest tab and verify "Snapshot Type" = "Monthly Lookback (retrospective)".
4. You can optionally smoke-test `Create Monthly Lookahead Snapshot` too — it's read-only and safe to run anytime. It snapshots whatever month the dropdowns are currently on. During a real monthly close, you run it AFTER updating the 6 dropdowns to the new month.

### 5. Create the scheduled task

Use `mcp__scheduled-tasks__create_scheduled_task` with:
- **Name:** `mixmax-monthly-revenue-report`
- **Prompt:** contents of the monthly task prompt
- **Schedule:** on-demand (no automatic interval — monthly reports run when the user is ready, typically in the first week of the new month)

Confirm creation with `mcp__scheduled-tasks__list_scheduled_tasks`.

### 6. Dry-run

Before the first real run, offer the user a dry-run:
- Pick a closed month with weeklies already in place
- Run the full workflow but STOP at Approval Gate #1 (do not publish)
- Review the draft reports together

This lets us catch setup issues before leadership sees a report.

### 7. Document the run

Create `Revenue Reviews/Monthly Report/README.md` with:
- Which months have been closed
- Link to each month's GitHub Pages report
- Any known issues or adjustments

---

## Pre-run snapshot protocol (user takes BOTH snapshots before triggering the task)

Starting in v1.0.7, the monthly workflow no longer does a mid-run sheet reset. Heath takes BOTH the Lookback and Lookahead snapshots BEFORE clicking Run Now on the scheduled task. Claude verifies both snapshots at Checkpoint 1 and then runs straight through look-behind and look-ahead analysis without another sheet handoff.

**Division of responsibility:**
- **Heath (before running the task):** takes the Lookback snapshot with dropdowns on the closing month, then manually flips the 6 dropdowns to the new month and takes the Lookahead snapshot.
- **Claude (during the task):** confirms both snapshots are present and fully populated at Checkpoint 1, then reads from them for retrospective + forward-looking analysis. Claude does NOT click any Apps Script menu items during the run and does NOT write dropdown cells.

The script deliberately does not write date cells — timezone/date-parsing drift in prior versions rolled dropdowns back one day. Keeping dates user-authored eliminates that class of bug.

### The 6 dropdowns Heath flips between snapshots

Before taking the Lookahead snapshot, Heath updates these 6 cells on the Gen 1 sheet:
- Monthly Revenue Summary · C2 → "Month Year" label (e.g., "April 2026")
- Monthly Bookings Summary · C2 → "Month Year" label
- Rep Summary · E3 (start date) → 1st of new month (e.g., 2026-04-01)
- Rep Summary · F3 (end date) → last day of new month (e.g., 2026-04-30)
- CS Summary · E3 (start date) → same as Rep Summary E3
- CS Summary · F3 (end date) → same as Rep Summary F3

### Pre-run sequence

1. With dropdowns still on the closing month, open Gen 1 and click `RevOps Tools > Create Monthly Lookback Snapshot`. Confirm `Gen1_Monthly_Lookback_Snapshot_{YYYY-MM}_{date}` appears in the Monthly Snapshots folder.
2. Update all 6 dropdowns to the new month.
3. Click `RevOps Tools > Create Monthly Lookahead Snapshot`. Confirm `Gen1_Monthly_Lookahead_Snapshot_{YYYY-MM}_{date}` appears.
4. Trigger the `mixmax-monthly-revenue-report` scheduled task (Run Now).

### What Claude verifies at Checkpoint 1

Claude reads both snapshots' Manifest tabs via gviz CSV and confirms:
- **Lookback Manifest:** Snapshot Type = "Monthly Lookback (retrospective)", Closed Month matches the month Heath said he's closing, all 9 tabs OK with row counts > 0, plus spot-checks on key cells.
- **Lookahead Manifest:** Snapshot Type = "Monthly Lookahead (forward-looking targets)", New Month matches the new month, all 9 tabs OK, Dropdown State section shows all 6 dropdowns on the new month, plus target cells populated.

If anything looks off, Claude surfaces it at Checkpoint 1 and waits — no sheet writes, no re-snapshots from Claude's side.

### Extracting new-month targets from the Lookahead snapshot

Once the Lookahead snapshot is verified at Checkpoint 1, Claude extracts new-month targets from it via gviz CSV endpoint. For each tab, fetch:
   ```
   https://docs.google.com/spreadsheets/d/1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY/gviz/tq?tqx=out:csv&gid={GID}
   ```

   | Tab | GID |
   |---|---|
   | Monthly Revenue Summary | 586801175 |
   | Monthly Bookings Summary | 1201655554 |
   | Rep Summary | 1461552329 |
   | CS Summary | 1594569652 |

   Use JavaScript fetch via Chrome MCP's `javascript_tool`. Store large CSVs in `window.__` variables and retrieve in chunks via `.substring()` if truncated.

4. **Extract these targets** (from the Lookahead snapshot, not the live sheet):

   From Monthly Revenue Summary (contribution targets, NOT Total ARR targets):
   - Net ARR Contribution targets: Total Net ARR, Total Net DS Contribution, Total Self-Serve ARR Contribution
   - DS Channel targets: Net New Business, Expansion, Downgrade (budget), Churn (budget)
   - Self-Serve targets: Net New SS, Reactivation, Upgrade, Seat Expansion, Seat Contraction, Downgrade, Churn

   From Monthly Bookings Summary:
   - Bookings targets: Total Bookings, New Business Bookings, Expansion Bookings
   - Pipeline targets by channel: Total, Inbound, Outbound, Product, Expansion
   - Activity targets: Accounts Engaged, Meetings Booked, SQLs, SQOs

   From CS Summary:
   - Renewals Overview for All / CSM Owned / VSB Owned: # Accounts, At Risk, Forecasted ARR, NRR %, GRR % (ARR Retention), GRR % (Client Retention)
   - Renewals Summary: Previous Contract, Current ARR, Forecasted ARR, ARR Impact ($), NRR Target

5. **Save captured targets** to `Revenue Reviews/Monthly Report/[New_Month]_[Year]_Targets.md`. Include a `Source Snapshot:` line with the Lookahead snapshot URL so future runs can trace targets back.

---

## Troubleshooting

**`RevOps Tools > Create Monthly Lookahead Snapshot` menu item missing.** The combined Apps Script wasn't installed (or the sheet needs a reload). Reload the sheet — `onOpen` rebuilds the menu. If still missing, reinstall the script per Step 2.

**Lookahead snapshot fails on click.** Likely `CONFIG.MONTHLY_SNAPSHOT_FOLDER_ID` is still set to the placeholder. Set it to the real folder ID and re-run. (The script no longer prompts for a month — it reads whatever is currently in Monthly Revenue Summary C2.)

**Lookahead snapshot missing after menu click.** Check the Apps Script execution log (Extensions → Apps Script → Executions). The most common cause is Drive permission issues — reauthorize the script.

**gviz CSV returns empty from the snapshot.** The snapshot GIDs are per-file (new each run). Open the Lookahead snapshot's Manifest tab in Chrome and read the GIDs from the URL when each tab is selected.

**Dropdown-change log shows errors.** The Manifest tab records each `setValue()` call. If any shows "ERROR", the underlying tab may have had data-validation removed. Manually re-apply validation and re-run.

**Weekly reports missing for a week of the month.** If only 2–3 weeklies exist, reconciliation is still possible but noted. If 0–1 weeklies exist, recommend the user run the outstanding weekly first.

**Prior-month targets file missing.** Not a blocker. Note in the run log that baseline targets were unavailable for MoM comparison.

---

## First-run checklist

On first setup:
- [ ] Weekly workflow confirmed healthy
- [ ] Combined `apps_script_monthly_snapshot.gs` installed on Gen 1
- [ ] Monthly Snapshots Drive folder created; folder ID pasted into `CONFIG.MONTHLY_SNAPSHOT_FOLDER_ID`
- [ ] `RevOps Tools > Create Monthly Lookback Snapshot` smoke-tested (Lookback snapshot visible in Drive folder)
- [ ] All 4 MCPs connected (Chrome, Notion, Slack, + GitHub PAT)
- [ ] Scheduled task `mixmax-monthly-revenue-report` created
- [ ] Monthly Notion hub page created (or placeholder)
- [ ] Dry-run completed to Approval Gate #1
- [ ] README created at `Revenue Reviews/Monthly Report/README.md`

On every subsequent run: confirm Chrome MCP is still connected (this is the most common failure point), confirm the Apps Script is still healthy by checking the `RevOps Tools` menu is present, and that a Lookback snapshot has been captured for the closing month before starting.
