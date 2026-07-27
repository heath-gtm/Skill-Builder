---
name: closed-won-analysis
description: Turn a pile of won deals into the repeatable reason you win. Reads your closed-won deals, extracts the signals, motions, personas, and competitive situations that keep showing up, then builds a target profile and a ranked list of active lookalikes to work. Built for B2B revenue teams, customizable to your CRM and your sales process. Trigger on "why do we win", "what do our best deals have in common", "build me an ICP from wins", "find lookalikes to my closed-won", "which open deals look like winners", or any won-deal pattern pull.
---

# Closed-Won Analysis

## What this does
Reads your closed-won deals and finds what they have in common: the segments you win, the personas who sign, the motions that work, and the competitive spots where you come out ahead. It turns that into one target profile you can hand a rep, then ranks your active pipeline by how closely each open deal matches your winners. The point is not a nice chart. It is a shorter list of accounts that look like the ones you already closed.

## What you'll need
You do not need to connect anything to get value today. Bring your won deals and the skill runs now. Connect the tools below and it pulls them automatically and adds signals you cannot paste by hand.

- Works today with: a list of your closed-won deals, with segment or size, industry, win date, deal size, sales cycle length, primary contact title, source, and (if you have it) the competitor and the primary use case. Paste it or upload a CSV.
- More powerful connected to a CRM: it reads all of the above automatically, across every won deal in the window you pick.
- Sharper with a meeting or transcript tool: pulls the actual words buyers used, so the pattern is "why they said yes," not just the fields.
- Sharper with a product-analytics tool: adds which features the winners adopted first, so the profile includes real behavior.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a pattern it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your won-deal list (a CRM export, a closed-won CSV). The skill runs the full analysis today on your real deals. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and adds signals you cannot paste by hand (buyer language, first-adopted features, full history). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| WON filter | how you mark a win | Stage = Closed Won |
| WINDOW | the win-date range to analyze | trailing 4 quarters |
| SEGMENT fields | how you group accounts | industry, employee count, region |
| PERSONA field | the title that signs | primary contact role or title |
| MOTION fields | inbound vs outbound, source | lead source, channel |
| COMPETITOR field | who you displaced or beat | competitor on the deal |
| USE_CASE field | the problem you solved | primary use case or product |
| MIN_SAMPLE | fewest wins before a pattern counts | 5 (raise if you close a lot) |

Run any segmentation you like. The skill reports the patterns that actually repeat in your wins, so point it at your fields, not anyone else's.

## The method

### Pattern extraction (what repeats)
Group every won deal across your segment, persona, motion, competitive, and use-case fields. Report only the patterns that clear MIN_SAMPLE, so one lucky whale never becomes a "profile." For each pattern, show the share of wins, the average deal size, and the average cycle length, so a common-but-small pattern is not confused with a rare-but-huge one.

### Win-signal ranking
Rank the patterns by lift, not raw count. A signal earns its place when won deals show it far more often than the base rate of all your deals. "Half our wins are mid-market" means nothing if half your pipeline is mid-market. The signals that matter are the ones over-represented in wins.

### Target profile (the ICP you actually close)
Fold the top signals into one plain-language profile: the segment, the persona who signs, the motion that lands them, the use case that resonates, and the competitive setup where you win. This is not the ICP on the website. It is the ICP your win data votes for.

### Lookalike ranking (active pipeline)
Score every open deal by how many profile signals it hits. Return a ranked list, best matches first, with the signals each one shares with your winners and the ones it is missing. This is the payoff: a shorter list of open accounts that look like deals you already won.

## Quality gates
- No pattern reported below MIN_SAMPLE. Small samples lie, and one big logo is not a trend.
- Signals ranked by lift over base rate, never by raw count alone.
- Every lookalike shows the specific signals it matches, never just a score.
- Competitive and use-case claims come from a field or a transcript, never invented.

## Output (example)
```
CLOSED-WON PATTERNS · 34 wins, trailing 4 quarters

Top win signals (by lift over base rate)
Signal                        Share of wins   Avg size   Avg cycle
Mid-market, 200-800 staff     62%             $41K       38 days
Champion = Head of Ops        55%             $44K       35 days
Inbound demo request          48%             $39K       29 days
Displaced a manual/DIY setup  44%             $47K       33 days

Target profile (what you actually close):
  Mid-market ops leader, inbound, replacing a manual process.
  Fast cycle, above-average deal size.

Active lookalikes (open pipeline, best match first)
Account      Signals matched            Missing
Haledon      3 of 4 (seg, persona, mo)  no competitor read
Brightsea    3 of 4 (seg, persona, uc)  outbound, not inbound
Corverin     2 of 4 (seg, use case)     enterprise size

Next move:
  1. Work Haledon and Brightsea first. They match your winners on 3 of 4.
  2. Add a competitor field to your next 10 wins. It is your thinnest signal.
```

## Where the numbers come from
MIN_SAMPLE (5) and the trailing-4-quarter window are defaults, not laws. They suited a mid-market SaaS cycle with steady volume. If you close a handful of large deals a year, widen the window and lower the floor with your eyes open. If you close hundreds, raise the floor so only strong patterns survive. Lift is always measured against your own base rate, so the profile is yours, not a benchmark.

## Example chat
Here is the skill running on a real won-deal export.

**You:** Pull the pattern out of our Q2 wins, 34 deals, and tell me who in open pipeline looks like them.

**Claude:** Read's done. Your website ICP and your win data don't agree.
```
Signal                        Share of wins   Lift vs base
Mid-market, 200-800 staff     62%             1.4x
Champion = Head of Ops        55%             1.8x
Displaced a manual/DIY setup  44%             2.1x
```
"Displaced a manual setup" is your strongest signal by lift, not your biggest by share. It's rare in your total pipeline (21%) but shows up in nearly half your wins. That's the profile that actually predicts a close, not the mid-market segment everyone already assumes. One sharpener: add a competitor/incumbent field to more deals, it's your thinnest signal right now.

**You:** Score my open pipeline against that profile.

**Claude:** Ranked, best match first.
```
Account      Signals matched          Missing
Haledon      3 of 4 (seg, persona, mo) no incumbent read
Brightsea    3 of 4 (seg, persona, uc) outbound not inbound
```
Haledon and Brightsea are your two best bets this quarter, both hit 3 of 4 win signals. One sharpener: connect your CRM so this scoring re-runs automatically as new deals open, instead of a one-time snapshot on today's list.

## Go further
The read is step one. Here's where an operator takes it once the manual version proves out.

- **Rescore the pipeline weekly, not once.** Point a scheduled Claude task at Salesforce nightly and write the lookalike score back to a custom field on the opportunity.
- **Hand the profile to the SDR team.** Feed the top win signals into Clay to re-rank the outbound target list so reps prospect the accounts that already look like winners.
- **Alert on a new lookalike the day it appears.** DM the account owner in Slack the moment an open deal crosses the match threshold, instead of waiting for the next QBR.

You built the read once; now it runs itself.


## Make it yours
Fork it. Change the signals, the segments, the sample floor. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
