# Renewal-Health Analyst

> Your per-renewal analyst. Connect a CRM plus a product-analytics tool (and optionally a meeting tool) and turn any "will this renewal happen?" question into a per-deal verdict: renew yes/no, value, and conditions, a champion-stability check, an adoption story for the pitch, a commercial-lever inventory, and save-play prerequisites. Built for per-renewal depth, not portfolio rollups. Trigger on "will {account} renew?", "renewal verdict on {account}", "is {customer}'s renewal real?", "prep for {account} renewal", "what should I offer {account}?", "save play for {account}", "commercial levers on {customer}", "champion check on {account}", or any single-renewal question.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/renewal-health-analyst && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/renewal-health-analyst/SKILL.md -o ~/.claude/skills/renewal-health-analyst/SKILL.md && echo "Installed renewal-health-analyst. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/renewal-health-analyst/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Renewal-Health Analyst

## What this does
This skill reads one customer and returns a renewal verdict you can act on. It combines product adoption, champion stability, support sentiment, and any competitive signals into a single per-deal call: will this renew, at what value, and under what conditions. It then hands you the pitch material: the adoption story, the commercial levers you can pull, and the checklist of things that must happen before the renewal call. It is built for depth on one renewal at a time, not portfolio rollups.

## What you'll need
- A CRM (required). The account, renewal dates and value, contacts, and the renewal opportunity.
- A product-analytics tool (required). Which features the customer actually uses, and how often.
- A meeting tool (optional). Champion-conversation depth and recent engagement.
- A support tool (optional). A support-sentiment pulse.

No CRM and product-analytics tool connected? The skill says what to connect and stops. It does not guess.

## Customize this for yourself
| Set this | What it is | Default / Example |
| --- | --- | --- |
| CRM | The system of record for the account and the renewal | A CRM with account, contact, opportunity objects |
| Renewal date field | The field holding the renewal close or period-end date | A "renewal end date" field |
| Renewal value field | The current ARR up for renewal | An "open renewal ARR" field |
| Product-usage signal | The adoption read per feature or capability | A per-feature usage tier from your analytics tool |
| Champion field | The contact marked as the primary relationship owner | A "primary champion" field |
| Renew threshold | Confidence floor above which you call it a likely renewal | 70% |
| Champion-stale threshold | Days of champion silence that downgrade the verdict | 90 days |
| Engagement-floor threshold | Active weeks below which the relationship reads thin | Customer median |

Your product-usage signal is the part most worth mapping carefully. Decide how your analytics tool expresses adoption per feature, and name the features the way your customers would recognize them.

## The method
- Per-renewal verdict. Combine product adoption, champion stability, support sentiment, and competitive intel into a verdict and a confidence number: renew yes/no, a predicted value (flat, upsell, downgrade), and the conditions attached.
- Champion-stability check. Confirm the named champion is still active: record valid, title still a buyer, recent engagement. Flag single-thread risk when the only real relationship runs through one person.
- Adoption story for the pitch. Group product usage by depth: deeply used, established, emerging, untouched. State it in features the customer recognizes. The untouched group becomes the expansion narrative.
- Commercial-lever inventory. Term length, discount headroom, expansion add-ons, multi-year incentives, prepay. Attach a number to each and mark the strongest.
- Save-play prerequisites. A sequenced checklist of what must happen before the renewal call, with branch logic for responds, ghosts, and rejects.

## Quality gates
- No renewal verdict without a champion check. If the champion left or has not engaged within the stale threshold, the verdict downgrades automatically.
- The adoption story is named-capability, not "good usage."
- Save plays are sequenced (Day 0 / Day 7 / Day 14) with branch logic for responds, ghosts, rejects.

## Output (example)
```
EXAMPLE CO RENEWAL  ·  Closes 2026-08-15

VERDICT: RENEW + EXPANSION POSSIBLE  ·  Confidence 78%

Champion stability:
  - Champion still at the company (profile verified this month)
  - Engaged 6 of the last 12 weeks (above customer median)
  - Second-thread contact left in March, single-thread risk

Adoption story (for the pitch):
  Deeply used: Sequencing, Smart Send
  Established: Templates, Meeting Recording
  Emerging:    AI Compose
  Untouched:   Calendar features, Auto Follow-ups
  Story: "Core outreach is fully adopted. Calendar is your next step."

Commercial levers:
  - Multi-year at flat rate (strongest)
  - Add calendar bundle (expansion)

Save-play prerequisites:
  [ ] Re-thread to a second champion
  [ ] Run a calendar-feature demo
  [ ] Pre-position the multi-year offer 30 days out
```

## Where the numbers come from
The thresholds are defaults, not laws. The renew threshold (70%) is the confidence floor for calling a renewal likely. The champion-stale threshold (90 days) is the silence window that downgrades a verdict. The engagement floor defaults to your own customer median, so it self-calibrates once you have enough accounts. Re-tune all three after you watch a few renewals land against the verdicts the skill gave you.

## Make it yours
Map the roles to your stack, set your thresholds, and name your features the way your customers do. Built by an operator. Customize it, break it, make it better.
