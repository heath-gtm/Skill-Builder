---
name: offboarding-audit
description: Score the experience a customer has when they leave, the moment most companies treat as a cancel button. Grades the exit on whether you burn the bridge or build the boomerang, finds where a leaving customer gets punished or ghosted, and hands back a scored audit with fixes. Built for any post-sale team, customizable to your product and cancel flow. Trigger on "audit our offboarding", "score our cancel flow", "what happens when a customer leaves", "do we burn bridges on churn", "how do we say goodbye", "can we win these back later", or any offboarding-experience question.
---

# Offboarding Audit

## What this does
Grades the experience a customer has on the way out, the moment almost every company treats as a cancel button and nothing more. It walks the exit step by step, scores whether each moment builds a bridge or burns one, and finds the places a leaving customer gets punished, ghosted, or guilt-tripped. The premise: a customer who leaves feeling respected is a boomerang, and a customer who leaves feeling trapped is gone for good. Software is commoditized, so the goodbye is a growth channel, and this measures it.

## What you'll need
You do not need to connect anything to get value today. Describe your offboarding and the skill scores it now. Connect your tools and it grades against what leaving customers actually hit.

- Works today with: a walk-through of your exit flow, the cancel path, the emails, the data offboarding, the last human interaction. Paste it and go.
- More powerful connected to your billing or product tool: it sees the real cancel path a customer walks, including the dark patterns you forgot were there.
- Sharper with a CRM or CS tool: it reads whether a human reached out at the exit or the customer left in silence.
- Sharper with churn-reason or survey data: it hears why they left in their own words, and whether you listened.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on what you describe today and gets sharper as you connect tools. It never scores a courtesy that did not happen, and never assumes an exit was graceful because the flow looks clean. A gap is a prompt, not a guess.

- **Bring your data**: walk through your cancel flow and the last 30 days of a leaving customer. The skill scores the full exit today.
- **Connect your tools**: the same skill grades the real path, including friction and dark patterns, and whether a human showed up at the end.
- **Just exploring**: no exit flow to show yet? Get the rubric, the moments it grades, and a worked example, so you see the shape before you audit.

Every run ends with the one thing that would sharpen the next audit, a moment to instrument or a tool to connect.

## Customize this for yourself
This was built to be motion-agnostic. Set these to your exit:

| Set this | What it is | Default / Example |
|---|---|---|
| EXIT_MOMENTS | the steps of leaving | cancel request, retention offer, data export, last touch |
| CANCEL_PATH | how hard it is to leave | one click vs a maze |
| HUMAN_EXIT | where a person shows up at the end | a real goodbye vs silence |
| DATA_DIGNITY | how you hand back their data | clean export vs hostage-taking |
| REASON_CAPTURE | how you learn why they left | asked and listened vs a required dropdown |
| DOOR_LEFT_OPEN | how easy it is to come back | a warm door vs a cold wall |

The rubric is yours. The point is to grade the goodbye you actually give, and whether it leaves a door open or slams one.

## The method

### Score the exit moment by moment
Walk the leaving customer's path: the moment they decide, the cancel flow, the retention attempt, the data handoff, the final word. Each moment scores on one question: does this build a bridge or burn one. A cancel maze burns. A clean export with a warm note builds.

### Find the punishment
Name where leaving gets punished: the hidden cancel button, the guilt-trip copy, the retention offer that should have been the price all along, the data held hostage. Every punishment is a scored miss, because it converts a maybe-later into a never.

### Grade the last human moment
Score whether a real person says goodbye, or the customer vanishes into an automated "sorry to see you go." The last interaction is the one they remember. A high-value customer offboarded in silence is the clearest miss there is.

### Check the door
Score how easy it is to come back. Is their data recoverable, is their config saved, does anyone plan to reach out in 90 days, or is the door a cold wall. The boomerang lives or dies on whether the door was left open.

### Turn the score into fixes
Every burned bridge ends in a specific move: the dark pattern to remove, the human to insert at the exit, the 90-day win-back to schedule. Not "improve retention." The exact place you burned it and how to stop.

## Quality gates
- Every exit moment scores the one question: bridge or bridge burned.
- Punishments and dark patterns are named specifically, never softened to "friction."
- The last human moment is scored on its own, never blended into the flow score.
- The door-left-open check is explicit: could this customer come back easily, yes or no.
- Every burned bridge ends in a specific fix, never a generic recommendation.

## Output (example)
```
OFFBOARDING AUDIT · [your product] · the exit

Moment              Bridge or burned                  Score
Decision to leave   no human noticed the warning       1/5
Cancel flow         4 screens, hidden confirm button   1/5
Retention offer     50% off (should've been the price) 2/5
Data export         manual, 5-day wait                 2/5
Last human touch    none, just a "sorry to see you go" 0/5

BURNED BRIDGES: the cancel maze and the silent exit. This customer
leaves feeling trapped then ignored. That is a never, not a later.

DOOR LEFT OPEN: no. Data is a hassle to get, config is deleted,
no one plans to reach back out.

FIXES:
  1. Kill the cancel maze. One clear button. Respect earns returns.
  2. Insert a real human goodbye for accounts over [threshold].
  3. Keep their config warm for 90 days and schedule a win-back.

Offboarding experience score: 1.2 / 5 (bridge burned)
```

## Example chat
Here is the skill grading an exit that looks fine and is not.

**You:** Audit our offboarding. To cancel, they email support, we send a 40%-off save offer, then we process it in 3-5 days and delete the account. Standard stuff.

**Claude:** Standard is the problem. Scored as the leaving customer feels it:
```
Cancel via email       makes them ask permission to leave   2/5
40% save offer         reads as "we were overcharging you"  2/5
3-5 day processing     limbo, feels like foot-dragging      2/5
Delete the account     door slammed, config gone            1/5
```
The burned bridge is the ending: you delete everything, so even if they want to come back in six months, they start from zero. And the save offer backfires. Dropping 40% at the exit tells them the price was never real, which makes the relationship feel transactional right when you want it to feel human. Nobody said a genuine goodbye.

**You:** Huh. So what's the boomerang version?

**Claude:** Flip the ending. Make cancel one honest click, no maze, because respect is what earns the return. Skip the desperation discount and instead have the CSM send a real note: "totally understand, here's your clean data export, and we'll keep your setup warm for 90 days in case anything changes." Then actually schedule the 90-day reach-back. You just turned a deletion into an open door. One sharpener: connect your billing tool and I'll map the real cancel path a customer walks, so I can catch the dark patterns you have stopped noticing.

## Go further
The audit is step one. Here is where an operator takes it once the score is real.

- **Schedule the boomerang automatically.** Have a Claude task log every churned account and, at 90 days, surface the ones worth a warm reach-back to the CSM in Slack, with the win-back context ready.
- **Kill dark patterns before they cost you.** Feed the cancel-path findings to whoever owns the flow so the maze gets removed, and re-audit to confirm the score moved.
- **Pair it with the onboarding audit.** Score the welcome and the goodbye together: if you onboard like a five-star hotel and offboard like a parking ticket, the gap is the finding, and closing it is the whole play.

You grade the goodbye once, then leave the door open on purpose.

## Where the inputs come from
The exit moments, the thresholds, and the door-open window are yours to set. The examples here suited a subscription SaaS cancel flow. A usage-based or enterprise contract exits differently. The logic, score bridge-or-burned, name the punishment, leave the door open, does not change.

## Make it yours
Fork it. Change the exit moments, the rubric, the win-back window, the voice. The point is not to grade someone else's cancel flow. It is to measure whether your customers leave as a never or a later, and to turn the goodbye into a door. Built by an operator. Customize it, break it, make it better.
