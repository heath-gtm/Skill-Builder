# Enablement Plan

> Turn a new rep's start date into a ramp that ends in quota, not confusion. Builds a 30/60/90 onboarding plan with milestones at each gate, a certification bar they have to clear before they carry full load, and the manager touchpoints that catch a slow ramp early. Built for B2B sales managers and enablement, customizable to your role and motion. Trigger on "build an onboarding plan", "30/60/90 for a new AE", "how do I ramp this rep", "certification checklist", "onboarding milestones", or any new-hire ramp.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/enablement-plan && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/enablement-plan/SKILL.md -o ~/.claude/skills/enablement-plan/SKILL.md && echo "Installed enablement-plan. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/enablement-plan/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Enablement Plan

## What this does
Takes a new hire and builds the ramp: a 30/60/90 plan where each gate has milestones the rep must hit, a certification bar they clear before they carry a full book, and the manager touchpoints that surface a slow ramp in week three instead of month three. It turns "figure it out" into a path with checkpoints, so a struggling rep is caught early and a strong one is turned loose sooner.

## What you'll need
You do not need to connect anything to get value today. Bring the role and the start date and the skill runs now. Connect the tools below and it grounds the milestones in real activity.

- Works today with: the role, the motion, the start date, and what "fully ramped" means for this seat. Paste it or describe it.
- More powerful connected to a CRM: it tracks the rep's real activity and pipeline against the milestones, so ramp is measured, not assumed.
- Sharper with a meeting or call tool: it can check discovery and demo reps against the certification bar with real calls.
- Sharper with an LMS or content tool: it can map the learning path to your existing modules instead of generic ones.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the role you give it today and gets more powerful as you connect tools. It never invents a milestone hit it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: describe the role, motion, and ramp definition. The skill builds the full 30/60/90, the cert bar, and the touchpoints today. No connection required.
- **Connect your tools**: the same skill tracks real activity and pipeline against the milestones so ramp is measured. Same output, less effort, sharper.
- **Just exploring**: no hire yet? Get the framework, the milestone library, and a worked example on a sample AE ramp, so you can see the shape before you fill it in.

Every run ends with the one thing that would make the next run sharper, a milestone to define or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org onboarding quota-carrying and support roles. Set these to your role:

| Set this | What it is | Default / Example |
|---|---|---|
| ROLE | the seat being ramped | AE, SDR, CSM, Sales Engineer |
| MOTION | what they run | inbound, outbound, expansion, renewal |
| FULLY_RAMPED | the definition of done | full quota, full book, solo on deals |
| CERT_BAR | what they must pass to go solo | pitch, discovery, demo, objection pass |
| MILESTONES | the gate checkpoints | pick from the library, or add yours |
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| LMS | your learning system | your content or module library |
| TOUCHPOINT_CADENCE | manager check-in rhythm | daily wk 1, then 2x/wk, then weekly |

Set FULLY_RAMPED for your motion. An outbound SDR is ramped when they are self-sourcing meetings. A CSM is ramped when they own renewals solo. Different seats, different finish line.

## The method

### 30/60/90 with a theme per gate
Each gate has one job. Day 30 is learn: product, ICP, pitch, tools. Day 60 is do-with-support: real activity under supervision, first live calls, shadow-to-solo. Day 90 is own: full load, self-sourced, forecasting their own deals. One theme per gate keeps the ramp from becoming a firehose.

### Milestones at each gate
Each gate carries 3 to 5 milestones written as observable results, not attendance. "Passed the pitch cert," not "watched the pitch training." "Sourced first 5 qualified meetings," not "did some prospecting." A milestone you cannot observe is not a milestone.

### The certification bar
Before the rep carries a full book, they clear the CERT_BAR: a live pass on the pitch, a discovery call, a demo, and objection handling, graded against a rubric by the manager or a peer. The bar is pass or not-yet, and not-yet means more reps, not a lower bar. This is the gate that protects your pipeline from an unready rep.

### Manager touchpoints
The plan schedules the manager's check-ins at TOUCHPOINT_CADENCE, front-loaded because week one is where a bad ramp starts. Each touchpoint has a purpose: unblock, coach, or assess against the nearest milestone. The point is to catch a slow ramp while there is still time to fix it.

### Early-warning signals
The plan names the signals that a ramp is slipping: milestone missed at a gate, activity below the expected curve, cert not passed on the first attempt. Each has a response, so a slow start triggers coaching instead of a surprise at day 90.

## Quality gates
- Every milestone is an observable result, never attendance or "completed training."
- The certification bar is pass or not-yet, graded against a rubric, before full load.
- Manager touchpoints are front-loaded, each with a purpose, not just a recurring invite.
- Every gate has an early-warning signal with a defined response.
- FULLY_RAMPED is defined for the specific motion, not borrowed from another seat.

## Output (example)
```
ENABLEMENT PLAN · Mid-Market AE · outbound motion
Fully ramped = full quota, self-sourcing, forecasting own deals

DAY 30 · LEARN
  [ ] Pitch cert passed (live, rubric-graded)
  [ ] ICP + qualification framework quiz passed
  [ ] Tools and CRM hygiene checklist signed off
DAY 60 · DO WITH SUPPORT
  [ ] 15 self-sourced qualified meetings booked
  [ ] Discovery cert passed
  [ ] First 3 opps created, manager co-piloting
DAY 90 · OWN
  [ ] Demo + objection cert passed -> solo on deals
  [ ] Pipeline at 2x ramp-quota, self-sourced
  [ ] Forecasting own deals in the weekly call

Manager touchpoints: daily wk1, 2x/wk wks 2-6, weekly after.
Early warnings:
  - Pitch cert not passed by day 30 -> extra reps, re-cert day 37
  - Under 8 meetings by day 45 -> prospecting coaching block
```

## Where the numbers come from
The 30/60/90 gates, the meeting counts, and the 2x pipeline target are illustrative, not benchmarks. They suited a mid-market outbound AE. A longer sales cycle or an enterprise seat needs longer gates and different milestones. Set the finish line and the counts to your own motion. The framework does not change. The ramp is yours.

## Make it yours
Fork it. Change the gates, the milestones, the cert bar. The point is not to ramp a rep against someone else's onboarding. It is to run yours, so a slow start is caught in week three and a strong rep is carrying load sooner. Built by an operator. Customize it, break it, make it better.
