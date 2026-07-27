---
name: conversation-analyst
description: Your conversation analyst. Connect a meeting/conversation tool and a CRM, then turn any "what's been said / what's happening with this relationship?" question into a conversation pulse: meeting timeline, email reply tracking, last positive signal, champion drop-off detection, meeting digest, follow-up drafting. Trigger on "what's happening at {account}?", "summarize my meetings this week", "draft a follow-up for {account}", "is the champion still engaged?", "when did we last hear from {contact}?", "QBR prep for {customer}", "conversation pulse on {account}", "did {champion} go dark?", or any communication-history or relationship-state question.
---

# Conversation Analyst

## What this does
This skill turns the scattered history of a relationship into one readable pulse. It pulls meetings, email replies, and sequence activity, lays them on a timeline, tracks who is still replying and who has gone quiet, flags when a champion drops off, summarizes recent meetings, and drafts a grounded follow-up. It answers the question you ask before you reach out: what has actually been said, and where did we leave off.

## What you'll need
You do not need to connect anything to start. Bring what you have on the relationship and the skill runs today. Connect the tools below and it pulls the full history automatically, including conversations you would never reconstruct by hand.

- Works today with: what you know about recent contact, a timeline of meetings and email replies, the contacts involved, and when each last responded. Paste it.
- More powerful connected to a meeting or conversation tool: meeting history, email reply timelines, and sequence enrollments, live. It sees conversations the CRM never logged.
- More powerful connected to a CRM: the logged activity layer, contact roles, and account context.
- Sharper with a full email source (thread context) and a cross-channel signal source.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or upload what you have (a CSV or an export). The skill runs the full analysis today on your real numbers. No connection required.
- **Connect your tools**: the same skill pulls the data automatically and adds signals you cannot paste by hand (live activity, product usage, history). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact fields it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.
## Customize this for yourself
| Set this | What it is | Default / Example |
| --- | --- | --- |
| Meeting tool | The connector for meeting + email + sequence history | Any meeting/conversation platform |
| CRM | The connector for activity sync, contact roles, account context | Any CRM |
| Champion field | The CRM field that marks the primary contact on a deal | Primary contact role flag |
| Dark-days threshold | Days of silence before a contact is flagged dropped off | 21 days |

Swapping tools is a matter of pointing the two roles at different connectors. If your CRM names the primary-contact flag differently, set the champion field to match.

## The method
1. Meeting timeline. The last 90 days of meetings: date, type, attendees, topics, decisions, action items with owner and status.
2. Email reply tracking. Per contact: last reply date, reply count in the window, baseline cadence. Compare current behavior to baseline.
3. Last positive signal. The most recent forward-moving reply or commitment across all contacts.
4. Champion drop-off detection (locked rule below).
5. Sequence enrollment. Active sequences, touches delivered, reply state.
6. Pulse summary. A short read of the relationship's current state.
7. Suggested next move. The contact, the action, and the open commitments to close.

## Quality gates
- Cross-source completeness. The skill never reports "no activity" from a single source. It cross-references meeting-tool meetings and emails, CRM tasks and events, and any email thread context.
- Champion drop-off, locked rule. A primary contact is flagged "dropped off" only when their last reply is older than the dark-days threshold AND they have at least 3 historical replies in the prior 90 days. Without that baseline the skill says the signal is insufficient. This prevents flagging a brand-new contact who never replied.
- Meeting digest quality. Every digest names attendees, topics, decisions, action items with owner and deadline, and open questions. If a meeting has no transcript, the skill says so rather than fabricating.

## Output (example)
```
NORTHWIND, Conversation Pulse  ·  last 90 days
   Source: meeting tool + CRM activity layer

Meeting timeline
   May 27, Renewal touchbase, Rep + Primary Contact, 30 min
       Decisions: confirmed June 15 renewal date
       Action: Rep to send SOW by May 30 (sent May 29)
   May 12, QBR, Rep + Primary Contact + Finance Lead, 60 min
       Action: Primary Contact to share rollout plan (open, 17 days)

Email cadence
   Primary Contact:  last reply yesterday, 6 in 7 days, baseline 1-2/wk, HEALTHY
   Finance Lead:     last reply 12 days ago, baseline weekly, SLOWING
   Former Champion:  last reply 47 days ago, 8 historical replies, DROPPED OFF

Suggested next move
   Rep: 1:1 with Former Champion by Friday, reference past advocacy
   Open commitments: Primary Contact's rollout plan (17 days open)
```

## Where the numbers come from
Defaults tuned for a typical B2B cadence: a 90-day window, a 21-day dark threshold, and a 3-reply baseline minimum below which "dropped off" has no meaning. Widen the window for slow enterprise cycles, tighten the dark threshold for high-velocity motions, and raise the baseline if your contacts reply often. Re-tune the window and the dark threshold to your sales cycle before trusting the drop-off flags.

## Example chat
Here is the skill running on a real account pulse check.

**You:** What's happening at Northwind? Give me the conversation pulse.

**Claude:** Pulse built, and one contact just crossed the drop-off line.
```
Primary Contact:  last reply yesterday, 6 in 7 days, HEALTHY
Finance Lead:     last reply 12 days ago, baseline weekly, SLOWING
Former Champion:  last reply 47 days ago, 8 historical replies, DROPPED OFF
```
The Former Champion flag is real, not noise, because they had 8 replies in the prior 90 days before going quiet, that baseline is what makes "dropped off" mean something instead of just "never replied." The Primary Contact looks fine on the surface, but the Finance Lead slowing down is the earlier warning sign most reps miss because the loudest contact is still talking. One sharpener: connect a full email thread source so the digest quotes what the Finance Lead actually said in their last reply, not just the date.

**You:** Draft the follow-up to win the Former Champion back.

**Claude:** Drafted, grounded in the last real thing they said, not a generic check-in.
```
Subject: following up from the QBR
"Hi [name], it's been a bit since we connected, last I heard
you were championing the rollout plan internally. Curious where
that landed, happy to jump on a quick call if useful."
```
Referencing the QBR and the rollout plan keeps this from reading as a cold re-engagement, it shows you remember what they were actually working on. One sharpener: connect your CRM so this draft can also check whether the rollout plan action item ever got marked done before you send it.

## Go further
The read is step one. Here's where an operator takes it once the manual version proves out.

- **Catch every drop-off the week it happens.** Point a scheduled Claude task at your meeting tool and CRM weekly and flag any champion crossing the dark-days threshold before the renewal conversation.
- **Route the flag to the right owner instantly.** DM the account owner in Slack the moment a champion drop-off fires, instead of surfacing it at the next QBR prep.
- **Chain the read into the write.** Hand the pulse straight to comms-agent so the drafted follow-up ships as a real email draft, not a copy-paste step.

You built the read once; now it runs itself.


## Make it yours
Set the two connectors, match the champion field, tune the thresholds to your cycle, and the pulse is yours. Built by an operator. Customize it, break it, make it better.
