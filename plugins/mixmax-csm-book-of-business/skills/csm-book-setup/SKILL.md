---
name: csm-book-setup
description: >
  Set up the Mixmax CSM Book of Business Analysis workflow. Use when the user says
  "set up CSM book of business", "configure CSM book analysis", "install CSM book",
  "create the CSM book task", "how do I run a book of business analysis", or
  "I just installed the mixmax-csm-book-of-business plugin".
  Guides the user through connecting required tools, verifying the
  Renewals tab, and registering the scheduled task.
---

# CSM Book of Business Analysis Setup

One-time setup skill for the Mixmax CSM Book of Business Analysis workflow.

---

## What this does

1. Verifies all required MCP connections are active
2. Confirms the Renewals tab exists in Gen 1
3. Drops the canonical spec and task prompt into the user's working folder
4. Registers a manual-trigger scheduled task: `csm-book-of-business-report`

---

## Prerequisites

Before running setup, the user MUST have:

- **Google Sheets MCP** or **Chrome MCP** — to read Gen 1 data
- **Amplitude MCP** — to pull product-usage data (project 130895)
- **Mixmax MCP** — to search meeting transcripts and check sequence enrollments
- **Gmail MCP** — to search email threads and identify engaged contacts
- **Octave MCP** — to generate strategic outreach plays and enrich companies
- **GitHub publishing config** — `Revenue Reviews/specs/github_publishing_config.md` must exist with valid PAT

---

## Setup Steps

### Step 1 — Verify MCP connections

Check that the following tools respond:
- `query_amplitude_data` (Amplitude)
- `meetings` or `search_meeting_summaries` (Mixmax)
- `gmail_search_messages` (Gmail)
- `generate_email` and `enrich_company` (Octave)
- Chrome MCP `javascript_tool` OR Google Drive MCP (for sheet reading)

If any are missing, tell the user which connector to install and stop.

### Step 2 — Verify the Renewals tab

Read a sample from Gen 1 Sheet ID `1ikq0APBWkPcaaDUKx4nbdy0QNYVK30Tvb3_reeChpCY` Renewals tab to confirm:
- The tab exists and has data
- CSM Owner column is populated
- Account Name, ARR, and Renewal Date columns have values

### Step 3 — Copy specs to working folder

Copy from the plugin's `references/` folder:
- `csm_book_of_business_spec.md` → `Revenue Reviews/specs/`
- `csm_book_of_business_task_prompt.md` → `Revenue Reviews/specs/`

If files already exist, ask the user if they want to overwrite.

### Step 4 — Verify publishing config

Read `Revenue Reviews/specs/github_publishing_config.md`. Confirm:
- `GITHUB_PAT` is set (not placeholder)
- `GITHUB_OWNER` and `GITHUB_REPO` are set
- Test with a lightweight API call if possible

If missing, tell the user to run the `publishing-config-setup` skill first.

### Step 5 — Register the scheduled task

Create a manual-trigger scheduled task:
- **taskId:** `csm-book-of-business-report`
- **description:** "CSM Book of Business Analysis — on-demand deep-dive into any CSM's full account portfolio with Amplitude usage, meeting intel, Gmail engagement, sequence status, and Octave strategic plays. Published to GitHub Pages."
- **prompt:** (see task prompt file for full content)
- No cron — manual trigger only

### Step 6 — Create output directory

Ensure `Revenue Reviews/CSM Book of Business/` exists.

### Step 7 — Confirm setup

Print:
- All MCP connections verified
- Renewals tab confirmed
- Specs copied to working folder
- Scheduled task registered
- Output directory ready
- "Setup complete. To run: trigger `csm-book-of-business-report` and specify the CSM name."
