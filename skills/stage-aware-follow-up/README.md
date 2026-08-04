# Stage-Aware Follow-Up

> Write the buyer-facing follow-up a live deal actually owes, keyed to its stage and exit criteria instead of a generic cadence. After discovery, after the demo, after the proposal, and through procurement, each follow-up has a different job, one ask, and a dated next step. Trigger on "follow up after the demo", "what do I send after discovery", "stage-aware follow-up", "next-step email for this deal", "my deal went quiet after the proposal".

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/stage-aware-follow-up && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/stage-aware-follow-up/SKILL.md -o ~/.claude/skills/stage-aware-follow-up/SKILL.md && echo "Installed stage-aware-follow-up. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/stage-aware-follow-up/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Stage-Aware Follow-Up

## What this does
Writes the follow-up email a deal owes after each real interaction, keyed to the stage the deal is in. The stage's exit criteria decide the ask in the email, not a cadence template. Where trigger-outreach converts an external buying signal into a touch before the pipeline exists, this skill works inside the live deal: the buyer-facing message after each real interaction, driven by the stage and the exit criteria it still owes. It is not meeting-recap, which produces internal notes. This produces the thing the buyer reads.

## What you'll need
You do not need to connect anything to get value today. Bring the deal and the skill runs now. Connect the tools below and it pulls the context automatically.

- Works today with: the deal's stage, what happened in the last interaction (paste the notes or transcript), and who was in the room.
- More powerful connected to conversation intelligence (Gong, Fathom, Fireflies): it quotes what the buyer actually said, not what you remember.
- Sharper with a CRM: it reads the stage and exit criteria fields itself.
- Sharper with email connected: it checks when your last send went out and whether it got a reply.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a quote or a commitment the buyer did not make. A gap is a prompt, not a guess.

- **Bring your data**: paste the stage, the meeting notes or transcript, and the attendee list. The skill drafts the stage-correct follow-up today. No connection required.
- **Connect your tools**: the same skill pulls the transcript, the stage, and your send history automatically. Same output, less effort, sharper quotes.
- **Just exploring**: no live deal yet? Get the method, the per-stage jobs, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org running a staged pipeline. Set these to your process:

| Set this | What it is | Default / Example |
|---|---|---|
| STAGE names | your pipeline's actual stages | Discovery, Demo, Proposal, Negotiation, Procurement |
| EXIT CRITERIA per stage | what must be true to advance | Discovery: problem confirmed + next meeting booked with the right people |
| FOLLOW-UP SLA | how fast the follow-up goes out | Same day, before end of business |
| ESCALATION threshold | unanswered follow-ups before you change the play | 2 |

Map your own stage names and exit criteria. The skill asks for the exit criterion the deal has not met yet, because that criterion becomes the ask in the email.

## The method

### After discovery: confirm the problem, earn the room
The job: play the problem back in the buyer's words, not yours, and earn the next meeting with the right people in it. The exit criterion is a confirmed problem and a booked meeting with the people who feel it. So the email quotes what they said, states what you heard the cost to be, and asks for one thing: the next meeting, with the names you need in the room.

### After the demo: arm the champion
The job: give the champion a recap they can forward without editing. They will resell this internally whether you help them or not. So the email is written for the person who was not in the room: the problem, what they saw, what it changes for them, and the one open question. Forwardable is the test. If your champion has to rewrite it, you failed.

### After the proposal: surface the unspoken objection
The job: name the thing they are not saying and keep the economic buyer warm. Silence after a proposal is an objection that has not been spoken yet. So the email offers the objection on their behalf ("if the sticking point is the rollout timeline, here is what that actually looks like") and includes a reason for the economic buyer to stay in the thread.

### In negotiation and procurement: momentum with dates
The job: keep every open item attached to a name and a date. Never "just checking in." Every send restates where the process stands, what is owed by whom, and the next dated step. If legal has the redlines, the email says who has them, since when, and when you will reconvene.

### Timing and escalation
Same day, while the context is hot. Every send closes with a dated next step, never an open loop. When two follow-ups go unanswered: change the channel (call instead of email), change the person (go around or above with your champion's cover), or call the risk honestly in your forecast. A third identical email is not a strategy.

## Quality gates
- Every follow-up contains exactly one ask. Two asks is zero asks.
- A follow-up with no dated next step does not send.
- Never "just checking in" or "bumping this." If the email has no new information and no dated step, do not send it.
- The ask must map to the stage's unmet exit criterion. If it does not, the stage is wrong or the ask is.
- Quotes come from the notes or transcript. No invented buyer statements.

## Output (example)
```
SAMPLE FOLLOW-UP · Meridian Freight (fictional)
Stage: Post-demo
Exit criterion driving the ask: champion has what she needs to resell internally

Subject: What your ops team saw today, in one page

Dana,

Recap you can forward as-is:

The problem your team named: dispatch spends ~2 hours a day
reconciling load boards by hand ("we re-key the same load three
times," your words from today).

What you saw: one intake, no re-keying, exceptions flagged for a
human instead of buried.

Open question from your side: whether IT signs off on the TMS
connection. I'll bring our integration lead to answer it live.

One ask: 30 minutes Thursday with you and Marcus from IT.
Holding 2pm. Does that work?

Heath
```

## Example chat
Here is the skill running on a real deal, start to finish.

**You:** I demoed to Meridian Freight this morning. Champion is Dana, ops director. Her boss wasn't there. Here are my notes. [pastes notes]

**Claude:** Stage is post-demo, so the job is arming Dana to resell internally, and the unmet exit criterion is getting her boss into the process. Drafted the forwardable recap above: her problem in her words, what she saw, the one open question, and a single ask for Thursday with IT. It goes today while the demo is fresh. One sharpener: connect Fathom and I can quote the transcript instead of your notes.

**You:** She never replied to that or the nudge I sent Friday. Do I bump it again?

**Claude:** No. Two unanswered follow-ups means the play changes, not the wording. Three options in order: change the channel and call her Tuesday morning, change the person and ask the AE who knows Marcus in IT to open that thread, or call the risk and move this out of your commit. A third email that says the same thing softer is the one move off the table.

## Go further
The draft is step one. Here is where an operator takes it once the manual version proves out.

- **Pull what was actually said.** Connect Gong or Fathom so every follow-up quotes the buyer's real words from the transcript, not your memory of them.
- **Let the stage drive the template.** Read the stage field from Salesforce so the skill picks the right job automatically and flags when the ask does not match the stage.
- **Send from where you work.** Connect your email tool so the draft lands ready to send, and the skill can see whether the last one got a reply before writing the next.
- **Catch the silent ones.** Schedule a Claude task to scan open deals for follow-ups past your SLA and post the misses to your Slack DM each morning.

The follow-up is only as good as the hours between the meeting and the send. Automate the gap.

## Make it yours
Fork it. Change the stage names, the exit criteria, the SLA, the escalation threshold. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
