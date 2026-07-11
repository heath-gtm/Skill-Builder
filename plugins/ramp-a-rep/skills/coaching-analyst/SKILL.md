---
name: coaching-analyst
description: Your rep gap analyst. Connect a CRM and a meeting/activity tool, then turn any "who needs help and on what?" question into per-rep coaching priorities: sales-methodology completeness per rep, activity quality per rep, deal velocity per rep, win rate by segment, time-in-stage outliers, and stale-deal concentration. It watches the people, not the system. Trigger on "who needs coaching?", "rep gap analysis", "coaching priorities this week", "{rep}'s coaching plan", "where is {rep} struggling?", "team-level coaching themes", "who's working their pipeline?", "activity quality by rep", or any rep-level coaching question. Also fire before a 1:1 or a forecast call.
---

# Coaching Analyst

## What this does
This skill turns rep data into per-rep coaching priorities. It reads each rep's pipeline, activity, and win history, then surfaces a specific gap for each person plus the team-level patterns underneath them. It answers "who needs help and on what?" with a named topic per rep, not a vague verdict. It watches the people, not the system.

## What you'll need
- A CRM. The source of opportunities, stages, forecast categories, close dates, and account notes.
- A meeting and activity tool. The source of meeting counts, transcripts, and follow-up cadence.
- Optional: a product-usage tool and an account-scoring tool.
- A defined sales methodology with a completeness check, and a win-rate segmentation.

No CRM connected? The skill says what to connect and stops. It does not guess.

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

## Make it yours
Map your CRM, your methodology, your segments, and your targets, and the method runs against your numbers. Built by an operator. Customize it, break it, make it better.
