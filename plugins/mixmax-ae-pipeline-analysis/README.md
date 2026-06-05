# Mixmax AE Pipeline Analysis

On-demand analysis of any AE's full open pipeline.

## What it does

Run this for any AE name and get a comprehensive HTML report with:
- Pipeline overview (deals, value, stage distribution, coverage ratio)
- Deals tiered as Must-Win, Should-Win, Long-Shot
- Stuck deal detection with specific unstick strategies
- Amplitude trial/evaluation usage per deal
- Top 2 most engaged contacts per deal (from Gmail + Mixmax meetings)
- Octave-generated strategic plays per deal (close, accelerate, advance, unstick)
- Full meeting intelligence with objections and competitive mentions

## Skills

- **ae-pipeline-setup** — One-time setup: verify MCPs, register the scheduled task
- **ae-pipeline-runbook** — Reference guide for running and troubleshooting

## Data Sources

- Gen 1 AE Forecast tab (via snapshot)
- Amplitude (trial usage, 6-month trends)
- Mixmax meetings (transcripts, objections, buying signals)
- Gmail (email threads, contact engagement)
- Mixmax sequences (enrollment status)
- Octave (strategic plays, company enrichment, contact discovery)
- Web research (company news, funding, urgency signals)

## Usage

1. Install plugin
2. Run `ae-pipeline-setup` to connect tools and register the task
3. Trigger `ae-pipeline-analysis-report` manually
4. Specify the AE name when prompted
5. Review at 4 checkpoints, then publish to GitHub Pages
