# mixmax-cs-leader-weekly

Weekly cross-period CS Leader brief for Mixmax (Heather, private).

## What this plugin produces

A single private HTML brief, generated weekly. Synthesizes the most recent approved quarterly + quarter-ahead artifacts + freshest Gen 1 weekly snapshot into a Monday-morning leverage-and-prevention read for the CS Leader.

Sections:
1. Monday Morning Headline
2. Must-Save Top 3 (named, owner, $ exposure, usage read, play)
3. Must-Renew This Month
4. Renewal Pipeline — 31-60 / 61-90 Lookout
5. Top 3 Expansion Plays of the Week
6. CSM Book Health Dashboard
7. CSM Coaching Notes (Private)
8. Canary List — trending toward at-risk (preventive)
9. Churn / Downgrade Autopsy — recent quarter (closed)
10. Quarter-Ahead Red Flags (Top 3)
11. Monday Stand-Up Talking Points
12. Base Report Link

File lands at `Revenue Reviews/Leader Weekly/CS/CS_Leader_Weekly_{YYYY-MM-DD}.html` and is published to GitHub Pages + DM'd to Heather.

## Skills

- **`cs-leader-weekly-setup`** — one-time installer. Bundles the spec into your working folder and registers the `cs-leader-weekly-report` scheduled task.
- **`cs-leader-weekly-runbook`** — reference for ad-hoc generation, single-section regeneration, selection heuristics, and status-badge thresholds.

## Dependencies

- **`mixmax-publishing-core`** — required.
- **`mixmax-monthly-gtm-report`** — provides `renewals-management`, `customer-success`, `mixmax-revenue-reporting` skills.
- **`account-amplitude-crossref`** + **`octave-messaging-suggestions`** — standalone Cowork skills used in the Account Deep-Dive Protocol. Required for sections 2, 3, 4, 5, 8.
- A previously-approved Mixmax Quarterly + Quarter-Ahead artifact, plus a freshly-cut weekly snapshot.

## Install

1. Install `mixmax-publishing-core` and run `publishing-config-setup`.
2. Install this plugin.
3. Run `cs-leader-weekly-setup`.
4. Cut a fresh weekly snapshot from the Gen 1 sheet.
5. Trigger `cs-leader-weekly-report` from the Cowork scheduled-tasks panel. Recommended cadence: every Friday afternoon or Monday morning.
