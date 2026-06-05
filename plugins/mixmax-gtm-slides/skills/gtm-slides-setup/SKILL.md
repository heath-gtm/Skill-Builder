---
name: gtm-slides-setup
description: >
  Set up the GTM Slides workflow. Use when the user says "set up GTM Slides",
  "configure GTM slides", "install GTM slides", "create the GTM slides task",
  "how do I run the GTM slides", or "I just installed the mixmax-gtm-slides plugin".
  Guides the user through connecting required tools, verifying the spec files,
  and registering the scheduled task.
---

# GTM Slides — Setup (v5.3.0)

## What This Skill Does

Installs and configures the `leader-ceo-updates` scheduled task (GTM Slides workflow) that produces the **v5.3.0 HTML content workbench** — a 34-slide single-file artifact with universal 7-block skeleton, cover Data Accuracy banner, universal visual picker, collapse-all sidebar, and inline-editable K/S/S drivers on D1–D5. The workbench feeds the Mixmax CEO's board deck workflow (copy-paste into Google Slides).

## Prerequisites Check

Before setup, verify these tools are connected:

1. **Google Sheets MCP** (or Chrome MCP) — for reading Gen 1 Quarterly / Monthly Lookback snapshots
2. **GitHub publishing config** — `Revenue Reviews/specs/github_publishing_config.md` with valid PAT (managed by `mixmax-publishing-core` plugin)
3. **Notion MCP** — for posting to the GTM Team page
4. **Slack MCP** — for DM notifications (optional — workflow degrades gracefully)
5. **Python 3.10+** with `matplotlib`, `openpyxl`, `playwright` installed
6. **`mixmax-publishing-core` plugin** installed (provides git data API push)
7. **`mixmax-report-accuracy` plugin** installed (provides the pre-publish QA gate)

## Setup Steps

### Step 1 — Verify Spec Files (v5.3.0)

Check that these files exist in the user's workspace or in the plugin's `references/` folder:

- `references/gtm_slides_spec.md` — **v5.3.0** — 34-slide layout, 7-block skeleton, DA banner §0, visual picker, QA regex gate
- `references/gtm_slides_task_prompt.md` — **v5.3.0** — LLM-facing workflow prompt
- `references/cover_page_spec.md` — **v2.0.0** — cover with §0 Data Accuracy banner
- `references/universal_report_addendum.md` — universal QA + ARR + Slack rules
- `Revenue Reviews/specs/github_publishing_config.md` — GitHub publishing credentials (set up once via `mixmax-publishing-core:publishing-config-setup`)

If any `references/*.md` files are missing, reinstall the plugin from the latest bundle.

### Step 2 — Verify Publishing Config

Invoke `mcp__mixmax-publishing-core__publishing-config-reference` (or read `Revenue Reviews/specs/github_publishing_config.md` directly) and check:
- `GITHUB_PAT` is not a placeholder
- `GITHUB_OWNER` and `GITHUB_REPO` are set
- The PAT has repo write access
- `PATH_GTM_SLIDES` resolves (default: `reports/gtm-slides/`)

If invalid, run the `mixmax-publishing-core:publishing-config-setup` skill first.

### Step 3 — Verify Snapshot Script

The unified snapshot Apps Script (`apps_script_unified_snapshot.gs`) must capture all 13 tabs the v5.3 task prompt reads, including:
- Monthly / Quarterly Revenue Summary
- Monthly / Quarterly Bookings Summary
- CS Summary
- Renewals - This Year (GID: 2085621475)
- Rev Ops - SQLs - This Year (GID: 1374581498)
- Rev Ops AE Forecast - This Year
- Total Prospect Account Engaged - Year
- Meetings (AE Roles ONLY) - This Year (GID: 1101943570)

If the script is older / smaller than the canonical version, update it from the workspace copy (`Revenue Reviews/apps_script_unified_snapshot_v2.gs`).

### Step 4 — Create Output Directory

```
Revenue Reviews/Leader Weekly/GTM Slides/
Revenue Reviews/Leader Weekly/GTM Slides/charts/
Revenue Reviews/Leader Weekly/GTM Slides/qa/
```

### Step 5 — Register Scheduled Task

Register the `leader-ceo-updates` scheduled task with:
- **Task ID:** `leader-ceo-updates`
- **Schedule:** Manual only (no cron)
- **Description:** `GTM Slides — HTML Content Workbench (v5.3.0) with 34-slide 7-block universal skeleton + cover Data Accuracy banner + universal visual picker + collapse-all + inline-editable K/S/S drivers. Manual trigger after base revenue report is approved.`
- **Prompt:** Contents of `references/gtm_slides_task_prompt.md` (v5.3.0)

### Step 6 — Verify (dry run)

Ask the user if they want a dry run:
1. Point to any existing approved monthly or quarterly report
2. Run through STEP 0 → STEP 2c (spec load + data extraction + DA banner extraction + Data QA checkpoint) only
3. Confirm the 12 DA banner metrics extract correctly from the snapshot
4. Confirm stat card values populate for a sample of slides (e.g., 01, D1, 20, GAL)
5. Do NOT generate HTML or publish

### Post-Setup

After setup completes, tell the user:
- The GTM Slides v5.3.0 workflow is ready
- Trigger the `leader-ceo-updates` task after any approved Monthly or Quarterly Revenue Report
- Output: single-file HTML workbench published to `{GITHUB_PAGES_URL}/reports/gtm-slides/GTM_{period}_Workbench_v5.3.0.html`
- This plugin supersedes the old `mixmax-leader-update-slides` plugin (v1.x) — uninstall that if still present
