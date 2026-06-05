# mixmax-sales-leader-weekly

Weekly cross-period Sales Leader brief for Mixmax (Heath, private).

## What this plugin produces

A single private HTML brief, generated weekly. Synthesizes the most recent approved quarterly report, the quarter-ahead artifact, and the freshest Gen 1 weekly snapshot into a Monday-morning leverage read for the Sales Leader.

Sections:
1. Monday Morning Headline
2. This Week's Must-Win Deals (Top 5)
3. Rep Health Dashboard
4. Coaching Notes (Private)
5. Top 10 Accounts This Week
6. Stuck + Pull-In Deals
7. Quarter-Ahead Red Flags
8. Monday Meeting Talking Points
9. Base Report Link

File lands at `Revenue Reviews/Leader Weekly/Sales/Sales_Leader_Weekly_{YYYY-MM-DD}.html` and is published to GitHub Pages + DM'd to Heath.

## Skills

- **`sales-leader-weekly-setup`** — one-time installer. Bundles the spec into your working folder and registers the `sales-leader-weekly-report` scheduled task.
- **`sales-leader-weekly-runbook`** — reference for ad-hoc generation, single-section regeneration, selection heuristics, and status-badge thresholds.

## Dependencies

- **`mixmax-publishing-core`** — required.
- **`mixmax-weekly-gtm-report`** — provides `deal-management`, `pipeline-building`, `mixmax-revenue-reporting` skills used during section generation.
- **`account-amplitude-crossref`** + **`octave-messaging-suggestions`** — installed as standalone Cowork skills (already shipped in your account). Used in the Account Deep-Dive Protocol.
- A previously-approved Mixmax Quarterly + Quarter-Ahead artifact, plus a freshly-cut weekly snapshot.

## Install

1. Install `mixmax-publishing-core` and run `publishing-config-setup`.
2. Install this plugin.
3. Run `sales-leader-weekly-setup`.
4. Cut a fresh weekly snapshot from the Gen 1 sheet (RevOps Tools → Create Weekly Snapshot).
5. Trigger `sales-leader-weekly-report` from the Cowork scheduled-tasks panel. Recommended cadence: every Friday afternoon or Monday before the sales standup.
