# Conversation Analyst

> Your conversation analyst. Connect a meeting/conversation tool and a CRM, then turn any "what's been said / what's happening with this relationship?" question into a conversation pulse: meeting timeline, email reply tracking, last positive signal, champion drop-off detection, meeting digest, follow-up drafting. Trigger on "what's happening at {account}?", "summarize my meetings this week", "draft a follow-up for {account}", "is the champion still engaged?", "when did we last hear from {contact}?", "QBR prep for {customer}", "conversation pulse on {account}", "did {champion} go dark?", or any communication-history or relationship-state question.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/conversation-analyst && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/conversation-analyst/SKILL.md -o ~/.claude/skills/conversation-analyst/SKILL.md && echo "Installed conversation-analyst. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/conversation-analyst/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Conversation Analyst

## What this does
This skill turns the scattered history of a relationship into one readable pulse. It pulls meetings, email replies, and sequence activity, lays them on a timeline, tracks who is still replying and who has gone quiet, flags when a champion drops off, summarizes recent meetings, and drafts a grounded follow-up. It answers the question you ask before you reach out: what has actually been said, and where did we leave off.

## What you'll need
- A meeting/conversation tool, for meeting history, email reply timelines, and sequence enrollments.
- A CRM, for the activity sync layer (logged tasks and events), contact roles, and account context.
Both matter. The meeting tool sees conversations the CRM never logged. The CRM sees logged activity the meeting tool never tracked. Optional: a full email source for thread context, and a cross-channel signal source.

No meeting tool or CRM connected? The skill says what to connect and stops. It does not guess.

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

## Make it yours
Set the two connectors, match the champion field, tune the thresholds to your cycle, and the pulse is yours. Built by an operator. Customize it, break it, make it better.
