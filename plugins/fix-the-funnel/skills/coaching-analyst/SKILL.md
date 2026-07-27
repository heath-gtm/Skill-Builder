---
name: coaching-analyst
description: Your rep gap analyst. Connect a CRM and a meeting/activity tool, then turn any "who needs help and on what?" question into per-rep coaching priorities: sales-methodology completeness per rep, activity quality per rep, deal velocity per rep, win rate by segment, time-in-stage outliers, and stale-deal concentration. It watches the people, not the system. Trigger on "who needs coaching?", "rep gap analysis", "coaching priorities this week", "{rep}'s coaching plan", "where is {rep} struggling?", "team-level coaching themes", "who's working their pipeline?", "activity quality by rep", or any rep-level coaching question. Also fire before a 1:1 or a forecast call.
---

# Coaching Analyst

## What this does
This skill turns rep data into per-rep coaching priorities. It reads each rep's pipeline, activity, and win history, then surfaces a specific gap for each person plus the team-level patterns underneath them. It answers "who needs help and on what?" with a named topic per rep, not a vague verdict. It watches the people, not the system.

## What you'll need
You do not need to connect anything to start. Bring your rep data and the skill runs today. Connect the tools below and it pulls it automatically and adds signals you cannot paste by hand.

- Works today with: per-rep open deals and activity counts, plus your qualification framework's fields. Paste or upload.
- More powerful connected to a CRM: opportunities, stages, forecast categories, close dates, and notes, live.
- More powerful connected to a meeting or activity tool: meeting quality from transcripts and real follow-up cadence, not just counts.
- Sharper with product-usage and account-scoring tools.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload your list (a deal export, a stage CSV). The skill runs the full analysis today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and adds signals you cannot paste by hand (live activity, product usage, history). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
| Set this | What it is | Default / Example |
|---|---|---|
| CRM | Where opportunities, stages, and notes live | Any CRM with opportunity and activity objects |
| Methodology fields | The fields or steps your completeness check counts | Your qualification framework's required fields |
| Activity sources | Where meetings, calls, and follow-ups are logged | Meeting tool + CRM tasks/events |
| Win-rate segments | How you split wins to find where a rep wins vs loses | Segment, channel, deal size |
| Completeness target | The team bar for methodology completeness | 80% |
| Win-rate flag threshold | Win rate below which a segment gets flagged | 40% |
| Multi-thread target | Contacts per deal you expect | 3+ |
| Stage-sticker rule | When a deal counts as stuck | Longer than the rep's own median in that stage |

Map your own methodology to the completeness check. If your framework has named steps or required fields, list them as the methodology fields and the skill counts completeness against those. The method does not assume any one framework.

## The method
Per rep, the skill computes:
- Methodology completeness rate. The share of open opps that pass your check, plus the field the rep misses most.
- Activity quality. Meeting count times meeting quality (from transcripts) times follow-up cadence. High count of low-quality touches does not score well.
- Deal velocity. Average days in each stage. Surfaces deals sitting longer than the rep's own median.
- Win rate by segment. Where the rep wins and loses. Small samples flagged as small.
- Stale-deal concentration. The share of the book going dark or stale.
- Coaching theme detection. Patterns that hold across the team, not one rep.

The team view rolls these up against your targets and names the reps outside the band.

## Quality gates
- Per-rep gap is specific. Not "needs help with methodology," but "completeness 14% (1 of 7 opps), most-missing step is the decision-dynamics field."
- Coaching themes are team-level and statistically meaningful. "3 of 5 reps below 40% mid-market win rate" beats "everyone needs to do better."
- Pre-1:1 brief is forecast-aware. It knows the next forecast call and what the rep called last week.
- Small samples are labeled with their n.

## Output (example)
```
COACHING PRIORITIES, Week of June 1

TOP PRIORITY: Rep A
  Methodology completeness: 14% (1 of 7 opps), lowest on team
  Most-missing step: decision-dynamics (5 of 7 opps)
  Stage-stickers: 3 opps in Solution Validation past 21 days (median 9)
  1:1 focus: methodology + multi-thread + activity cadence

Rep B, strong but watch:
  Completeness 87% (highest), win rate 71% (small sample n=7)
  Concern: working hard, but pipeline math does not get there
  1:1 focus: pipeline-creation strategy, not execution

TEAM THEMES:
  1. Completeness target 80%, team avg 56%. Group training.
  2. 3 of 5 reps below 40% mid-market win rate. ICP or messaging check.
  3. Multi-thread averaging 1.4 contacts/deal (target 3+).
```

## Where the numbers come from
Defaults to re-tune: completeness target 80%, win-rate flag 40%, multi-thread target 3+, stage-sticker rule judged per rep against their own median. Any win rate carries its n so a hot streak is not mistaken for a trend. Activity quality depends on the meeting tool; with none connected, the skill falls back to CRM activity counts and says so.

## Example chat
Here is the skill running on a real rep roster ahead of 1:1s.

**You:** Who on the team needs coaching this week, and on what specifically?

**Claude:** Read's done. Your top priority isn't your lowest performer, it's your busiest one.
```
Rep A: methodology completeness 14% (1 of 7 opps), lowest on team
       most-missing step: decision-dynamics field (5 of 7 opps)
Rep B: completeness 87% (highest), win rate 71% (n=7, small sample)
```
Rep A's gap is specific and fixable: they're skipping decision-dynamics on almost every deal, not "struggling generally." Rep B looks like your best rep by win rate, but the sample is only 7 deals, so that number could flip next quarter. One sharpener: connect your meeting tool so activity quality comes from real transcripts instead of raw call counts, which currently can't tell a good call from a long one.

**You:** What's the team-level theme underneath these two?

**Claude:** One pattern holds across more than one rep, which is what makes it a theme instead of a coincidence.
```
3 of 5 reps below 40% mid-market win rate
Team avg methodology completeness: 56% vs 80% target
```
That's not an individual coaching problem, it's a segment problem. Worth a group training on mid-market messaging, not five separate 1:1 conversations repeating the same fix. One sharpener: add product-usage data so the team theme can separate "messaging is off" from "we're selling to the wrong accounts."

## Go further
The read is step one. Here's where an operator takes it once the manual version proves out.

- **Refresh the board before every 1:1, automatically.** Point a scheduled Claude task at Salesforce and Gong the morning of 1:1 day and post each rep's brief to their manager in Slack.
- **Catch a stalling rep mid-quarter, not at the QBR.** Have the task re-run weekly and flag any rep whose completeness or win rate drops two weeks running.
- **Turn team themes into a training calendar.** Feed recurring gaps into a content-brief skill to spin up the enablement session the data is actually asking for.

You built the read once; now it runs itself.


## Make it yours
Map your CRM, your methodology, your segments, and your targets, and the method runs against your numbers. Built by an operator. Customize it, break it, make it better.
