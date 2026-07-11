# Deal-Health Analyst

> Turn "is this deal real?" into a deal-by-deal risk verdict. An 8-state risk taxonomy, a qualification-vs-stage gap check, multi-thread coverage, days-dark per deal, and a commit-creep watch. Built for B2B sales teams, customizable to your CRM and your sales process. Trigger on "how are my deals", "which deals are stuck", "what's at risk this month", "is the rep sandbagging", "multi-thread check", or any open-deal diagnostic.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/deal-health-analyst && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/deal-health-analyst/SKILL.md -o ~/.claude/skills/deal-health-analyst/SKILL.md && echo "Installed deal-health-analyst. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/deal-health-analyst/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Deal-Health Analyst

## What this does
Reads your open opportunities and gives each one a straight verdict: healthy, slipping, stuck, or dead. It checks whether a deal has real activity behind it, whether the rep actually qualified it, and whether they are talking to more than one person. Then it names the next move on the deals that need one.

## What you'll need
- Required: a CRM connector (deals, stages, amounts, close dates, activity dates, contact roles).
- Optional: a meeting or email tool, which sharpens the multi-thread and gone-dark checks.
- Optional: a product-analytics tool, which adds usage momentum for trials.
No CRM connected? The skill says what to connect and stops. It does not guess.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| STAGE field | the opportunity stage | Opportunity.StageName |
| FORECAST field | commit / best-case category | ForecastCategoryName |
| QUALIFICATION fields | your methodology's fields | MEDDIC, BANT, your custom fields |
| ACTIVITY sources | where "last touch" lives | Account, Opportunity, Task, Event dates |
| CONTACT ROLES | how you see who is on a deal | OpportunityContactRole |
| DARK_DAYS | no-activity days that mean at risk | 14 (re-tune to your cycle) |
| STUCK_DAYS | days in one stage that mean stuck | 21 (re-tune) |

Run any methodology you like. The skill checks "is this deal qualified for the stage it claims," so point it at your qualification fields, not anyone else's.

## The method

### Deal-risk verdict (8 states)
Every open deal gets exactly one: HEALTHY, MOMENTUM, AT_RISK, SLIP_RISK, STUCK, STALE, CHAMPION_DROP, GHOST.
- GHOST: no activity across any activity source for DARK_DAYS or more. Must show the source dates that prove it.
- STUCK: same stage past STUCK_DAYS with no forward step.
- SLIP_RISK: close date inside the period, but activity or qualification is thin.
- CHAMPION_DROP: your main contact has gone quiet, no touches in 30 days.
- AT_RISK: single-threaded, fewer than 2 contacts engaged in 30 days.
- MOMENTUM and HEALTHY: real activity, multi-threaded, qualified for stage.

### Activity check (multi-source)
Days dark is today minus the most recent touch across ALL your activity sources, not one. A deal is GHOST only if every source is cold. Show the dates.

### Qualification-vs-stage gap
If a deal claims a late stage but the qualification fields for that stage are empty, flag it and name the exact field that is missing. This is the "is the rep sandbagging" check. It is only as good as the fields you map.

### Multi-thread check
Fewer than 2 contacts engaged in 30 days is single-thread risk. One champion is one point of failure.

### Commit-creep watch
Flag deals that quietly moved from Commit to Best Case in the trailing two weeks. That movement is the forecast telling on itself.

## Quality gates
- No GHOST verdict without showing the activity dates that prove it.
- Qualification gaps surface field by field, named, never "incomplete."
- Forecast accuracy is trailing-quarter, never trailing-week. Small samples lie.

## Output (example)
```
ACTIVE DEAL HEALTH · 7 open opps
Account     Stage / ARR    Risk      Days-Dark   Why
Acme Corp   Sol Val/$45K   HEALTHY   2           Multi-thread + qualified
Vertex      Prop/$67K      SLIP      12          Champion went quiet
Blend Labs  Sol Val/$28K   STUCK     23          No next step set
Northwind   Eval/$112K     GHOST     47          Zero activity, all sources

Next moves:
  1. Vertex. Re-engage the champion. The deal has no second thread.
  2. Blend Labs. Add the missing next step before the next review.
  3. Northwind. Declare it lost or run one final outreach this week.
```

## Where the numbers come from
DARK_DAYS (14), STUCK_DAYS (21), and the multi-thread cutoff (2 contacts in 30 days) are defaults, not laws. They suited a mid-market SaaS cycle. If your deals run longer, raise them. The logic does not change. The thresholds are yours.

## Make it yours
Fork it. Change the states, the thresholds, the fields. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
