---
name: trigger-outreach
description: Turn a buying signal into a timely, relevant touch. Read the trigger (funding, a new hire, a product launch, a job posting, a tech change), pick the angle it earns, and write the outreach while it is still fresh. Built for B2B outbound teams, customizable to your signals and your voice. Trigger on "someone just raised, what do I send", "they posted a job, draft outreach", "new VP started, reach out", "write a touch off this news", or any signal-to-message task.
---

# Trigger Outreach

## What this does
Takes a buying signal and turns it into a message worth reading. It reads what the trigger actually means, picks the one angle the signal earns, and writes a short, specific touch that lands while the event is still fresh. No spray. No "congrats on the round" with a pitch stapled to it. A reason to reach out, and a message built around that reason.

## What you'll need
You do not need to connect anything to get value today. Paste the signal and the account, and the skill runs now. Connect the tools below and it reads the signals for you and drops the drafts where you send from.

- Works today with: the trigger (what happened, when, at which company) and who you want to reach. Paste the headline, the job post, or the note, plus a name and title.
- More powerful connected to a signal source: it watches for funding, hiring, launches, and tech changes, so you catch the trigger the day it fires, not a week late.
- Sharper with a CRM: it checks whether the account is already owned or in a deal, so the touch fits the relationship you actually have.
- Sharper with a sequencer or email tool: it drops the drafted touch straight into your outreach, ready to review and send.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the signal you paste today and gets more powerful as you connect tools. It never invents a trigger it cannot see, and it never claims freshness it cannot date. A missing detail is a prompt, not a guess.

- **Bring your data**: paste the signal and the target. The skill reads the trigger, picks the angle, and writes the touch today. No connection required.
- **Connect your tools**: the same skill watches your signal source, checks the CRM for context, and drops drafts into your sequencer. Same output, caught sooner, sent faster.
- **Just exploring**: no signal in hand? Get the framework, the angle each trigger type earns, and a worked example, so you can see the shape before a real one fires.

Every run ends with the one thing that would sharpen the next run, a signal source to connect or a detail to add to the trigger.

## Customize this for yourself
This was built for a B2B team working signals into outbound. Set these to your motion:

| Set this | What it is | Default / Example |
|---|---|---|
| SIGNAL sources | where triggers come from | funding, hiring, launch, tech change, news |
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| SEQUENCER | where the touch gets sent | any email or sequence tool |
| FRESHNESS window | how old a trigger can be and still count | 14 days (retune to your motion) |
| ANGLE map | which angle each trigger type earns | funding to capacity, hire to mandate |
| VOICE | your tone and length rules | short, plain, one ask, no flattery |
| VALUE hook | the problem you tie the trigger to | what the signal implies they now need |

Point it at your signals and your voice. The skill writes in the register you set, tied to the problem you actually solve, not a generic pitch.

## The method

### Read the trigger
Name what actually happened and what it implies. A funding round means new capacity and pressure to deploy it. A senior hire means a new mandate and a window to shape it. A product launch means a go-to-market push and new load on a team. A job posting names a gap in words the company chose. A tech change means a stack in motion. The read is the work. The message is downstream.

### Freshness gate
A trigger has a half-life. Check the date before you write. Inside the freshness window, the event is a live reason to reach out. Past it, the touch reads as late and the angle is weaker. If a signal is stale, say so and pick a different reason, or wait for the next one.

### Pick the angle (one, not three)
Each trigger earns one angle. Funding earns a capacity or scaling angle. A new leader earns a mandate or first-90-days angle. A launch earns a load or growth angle. A job post earns a "you named this gap" angle. A tech change earns a fit-with-your-new-stack angle. Pick the one the signal actually supports. Do not stack all of them into one message. One reason, said well, beats three reasons said fast.

### Write the touch
Short. Specific to the trigger. One ask. Open with the event as the reason you are reaching out, tie it to the problem it implies, and make one clear next step. No flattery-then-pivot. The signal is not a warm-up line, it is the whole reason the message exists, so the message should not survive with the trigger removed.

### Relevance test
Read it back and ask: could this exact message be sent to any other company? If yes, it is not signal outreach, it is a template with a name swapped in. Rewrite until the trigger is load-bearing.

## Quality gates
- Every touch names the specific trigger. No generic opener dressed up as timely.
- The freshness date is checked. A stale trigger is flagged, not sent as if fresh.
- One angle per message. No stacking funding plus hiring plus launch into one touch.
- The message fails the relevance test if it could be sent to any other account. Rewrite it.
- Any metric used to illustrate is clearly illustrative, never presented as a real number about the target.

## Output (example)
```
TRIGGER OUTREACH · Northwind (illustrative)
Signal:     Series B raise, 9 days ago (inside freshness window)
Angle:      New capacity, pressure to deploy the team fast
Persona:    VP Sales

Draft:
  Subject: your Series B and the next 20 reps

  Saw the round close last week. Rounds like this usually mean a
  hiring plan that outpaces the process that has to support it.
  When a team doubles, the outbound motion is often the first thing
  that cracks. Worth 20 minutes to compare notes on what tends to
  break at that size?

Why it works: the raise is the whole reason for the touch. Remove it
and the message has nothing to stand on. That is the test.
```

## Example chat
Here is the skill turning one real signal into a touch worth sending.

**You:** Northwind just closed a Series B, 9 days ago. VP Sales is Dana Cole. What do I send?

**Claude:** Good timing. Nine days is well inside the freshness window, so the raise is still a live reason to reach out.

One angle, not three. A Series B is new capacity and pressure to deploy it fast, so I'm playing the scaling angle, not "congrats on the round."

```
Subject: your Series B and the next 20 reps

Dana, saw the round close last week. Rounds this size usually
mean a hiring plan that outpaces the process meant to support it.
When a team doubles, the outbound motion is often the first thing
to crack. Worth 20 minutes to compare notes on what tends to break
at that size?
```

Relevance test: pull the raise out of that email and it has nothing to stand on. That's the bar, so it passes. I skipped the "love what you're building" opener on purpose; the signal is the whole reason, not a warm-up line.

**You:** They're already an open opp in Salesforce. Does that change it?

**Claude:** It does. This isn't a cold touch, it's a reason to re-engage an active deal, so I'd drop the introduction framing and reference where you left off:

```
Subject: the Series B changes the timeline we talked about

Dana, the round probably moves up the hiring you mentioned on our
last call. If the team's about to scale, the follow-up gap we
scoped gets more expensive fast. Want to pick the thread back up
this week?
```

One sharpener for next time: connect your signal source and I'll catch triggers like this the day they fire instead of nine days later, and check the CRM myself so I know it's an open opp before I write.

## Where the inputs come from
The freshness window (14 days) and the angle map are defaults, not laws. They suited a fast outbound motion where signals decay quickly. If your buyers move slower, widen the window. If your product ties to a different implication, remap the angles. The logic does not change. The thresholds and the mapping are yours.

## Go further
One good touch is the start. Here is where an operator takes it once the manual version works.

- **Watch the signals so you don't have to.** Wire a signal source into a scheduled Claude task that drafts the touch the day a trigger fires and drops it in your sequencer for review. You react to a ready draft, not a news alert.
- **Check the CRM before it writes.** Have the task read Salesforce or HubSpot first, so an owned account or open deal gets a relationship-aware touch instead of a cold intro to someone you already know.
- **Route by freshness automatically.** Fresh triggers go straight to a draft; stale ones get parked with a note. You never send "congrats on the round" three weeks late, and the good ones never sit.

The stack stays simple: a signal source fires it, Claude reads and writes it, the CRM keeps it honest about the relationship, your sequencer sends it. You set the angle map once; it runs on every trigger after that.

## Make it yours
Fork it. Change the signal sources, the freshness window, the angle map, the voice. The point is not to send someone else's template. It is to turn a real event into a real reason, in your words, faster. Built by an operator. Customize it, break it, make it better.
