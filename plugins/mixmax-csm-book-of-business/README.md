# Mixmax CSM Book of Business Analysis

On-demand analysis of any CSM's full account portfolio.

## What it does

Run this for any CSM name and get a comprehensive HTML report with:
- Full book overview (accounts, ARR, health distribution)
- At-risk accounts with Amplitude decay signals and save plays
- Growth & expansion opportunities with usage spike evidence
- Most engaged accounts by meeting + email activity
- Accounts renewing in next 90 days with readiness assessments
- Top 2 most engaged contacts per account (from Gmail + Mixmax meetings)
- Octave-generated strategic outreach per account

## Skills

- **csm-book-setup** — One-time setup: verify MCPs, register the scheduled task
- **csm-book-runbook** — Reference guide for running and troubleshooting

## Data Sources

- Gen 1 Renewals tab (via snapshot)
- Amplitude (product usage, 6-month trends)
- Mixmax meetings (transcripts, themes, action items)
- Gmail (email threads, contact engagement)
- Mixmax sequences (enrollment status)
- Octave (strategic plays, company enrichment)
- Web research (company news, M&A, funding)

## Usage

1. Install plugin
2. Run `csm-book-setup` to connect tools and register the task
3. Trigger `csm-book-of-business-report` manually
4. Specify the CSM name when prompted
5. Review at 4 checkpoints, then publish to GitHub Pages
