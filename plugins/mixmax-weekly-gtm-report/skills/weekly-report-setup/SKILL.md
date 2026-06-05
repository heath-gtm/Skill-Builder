---
name: weekly-report-setup
description: >
  Set up the Weekly GTM Revenue Report workflow. Use when the user says
  "set up weekly report", "configure weekly revenue report", "install weekly
  GTM report", "create the weekly report task", or "how do I run the weekly
  report". Guides the user through connecting required tools and creating
  the scheduled task.
---

# Weekly GTM Report — Setup Guide

Walk the user through setting up the automated Weekly GTM Revenue Report workflow. This is a one-time setup process.

## Prerequisites Check

Before setup, verify these MCP connections are available:

1. **Google Drive** — for finding weekly snapshots
2. **Chrome extension** — for data extraction via gviz CSV endpoint
3. **Notion** — for publishing report summaries
4. **Slack** — for distributing reports to channels
5. **GitHub** — for hosting HTML reports on GitHub Pages (requires a PAT with repo scope)

For any missing connection, guide the user to install it from the Cowork connectors panel.

## Setup Steps

### Step 1: Verify Gen 1 Sheet Access

Ask the user to confirm:
- They have access to the Weekly RevOps Report (Gen 1) Google Sheet
- The Apps Script "RevOps Tools > Create Weekly Snapshot" menu is installed
- They know the Google Drive folder where snapshots are saved

### Step 2: Verify GitHub Pages Repository

Ask the user:
- What is the GitHub repository for hosting reports? (e.g., `username/mixmax-revenue-reports`)
- Do they have a GitHub Personal Access Token with repo scope?
- Is GitHub Pages enabled on the repository?

### Step 3: Verify Notion Pages

Ask the user to provide or confirm:
- The Notion page ID for the CRO Report page
- The Notion page ID for the GTM Report page
- The parent page/workspace where these live

### Step 4: Verify Slack Channels

Ask the user to confirm:
- The Slack channel ID for #gtm-central (org-wide distribution)
- The Slack channel ID for #gtm-leadership
- How the CRO Report should be delivered (DM or private channel)

### Step 5: Create the Scheduled Task

Use the `create_scheduled_task` tool to create an ad-hoc (manual trigger) task with ID `weekly-revenue-report`. The task prompt should follow the 12-step workflow documented in the mixmax-revenue-reporting skill.

Key elements of the task prompt:
- Step 0: Interactive intake (3 questions — focus areas, context, data caveats)
- Steps 1-5: Load skills, find snapshot, extract 9 tabs, verify period, run specialist analysis
- Steps 6-7: Generate Mixmax GTM Report (org-wide, no rep names, team attack plan, Top 10 with WHY) and CRO Report (full detail, rep performance)
- Steps 8-9: QA spot-check and user approval
- Steps 10-12: Publish to GitHub Pages, update Notion, draft Slack messages

### Step 6: Test Run

After creating the task, recommend the user:
1. Create a fresh weekly snapshot from the Gen 1 sheet
2. Click "Run Now" on the weekly-revenue-report task
3. Walk through the full workflow to verify all connections work
4. Review both reports before approving distribution

## How to Run (Weekly Process)

Once set up, the weekly process is:

1. Open the Gen 1 Google Sheet
2. Click **RevOps Tools > Create Weekly Snapshot**
3. In Claude Cowork, go to the weekly-revenue-report scheduled task
4. Click **Run Now**
5. Answer the 3 intake questions
6. Review and approve at each gate
