# Champion-Move Detection

> Turn "my champion changed jobs" into two motions run the same day. Verify the move is real, score the risk on the account they left, score the opportunity at the company they joined, then write both plays, the internal risk flag with an owner and the door-opener to their new inbox. Built for B2B sales and CS teams, customizable to your CRM and enrichment stack. Trigger on "my champion just left", "champion changed jobs", "contact moved companies", "champion move play", "turn a job change into a deal".

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/champion-move-detection && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/champion-move-detection/SKILL.md -o ~/.claude/skills/champion-move-detection/SKILL.md && echo "Installed champion-move-detection. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/champion-move-detection/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Champion-Move Detection

## What this does
Runs the play for one detected job change. When a champion at a customer account or a key contact on an open deal moves companies, this skill verifies the move is real, scores both sides of it, and produces two outputs: an internal risk flag on the account or deal they left, with a named owner, and a door-opener message to the company they joined. Someone who already knows your product just landed somewhere new. That is the warmest first touch you will ever get, and it expires fast.

This is the play, not the system. If you want the standing monitor that watches all your contacts and feeds detections into this play, that is the job-change-watchlist skill, its upstream. And if you want to build a champion inside a live deal, that is champion-plan. This skill starts the moment one move is detected.

## What you'll need
You do not need to connect anything to get value today. Bring one detected move, or a contact list to sweep, and the skill runs now. Connect the tools below and it pulls signals automatically.

- Works today with: a contact list export (name, title, account, role on deal, last-engaged date) plus a manual LinkedIn check on the person who moved. Paste it or upload a CSV.
- Does more connected to a CRM: it reads account status, open deals, and contact roles automatically (Salesforce, HubSpot).
- Sharper with an enrichment tool: Clay, Common Room, or FullEnrich confirms the new company and title without a manual check.
- Sharper with Slack: routes the risk flag to the account owner the moment it is written.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets sharper as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste the contact who moved, or upload your contact export and name the person. The skill runs verification questions, both scores, and both drafts today. No connection required.
- **Connect your tools**: the same skill pulls CRM context and enrichment confirmation automatically, and routes the flag to Slack. Same output, less effort, sharper.
- **Just exploring**: no move detected yet? Get the verification checklist, the two scoring rubrics, and a worked example on sample data, so you know the play before you need it.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org with a customer book and a staged pipeline. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot |
| ENRICHMENT | who confirms the move | Clay, Common Room, FullEnrich |
| ALERT channel | where the risk flag lands | Slack #churn-risk, #deal-alerts |
| CONTACT ROLES | how you see who is on a deal | OpportunityContactRole |
| ENGAGEMENT depth | what "knew the product well" means | logins, sequences run, QBRs attended |
| BOUNCE tripwire | where email bounces surface | your sequencer's bounce report |
| STALE_DAYS | days since last engagement before depth decays | 90 (re-tune to your motion) |
| TOUCH window | how fast the door-opener ships after verification | 5 business days |

The scoring rubrics care about behavior, not titles. Point ENGAGEMENT depth at real usage and interaction data, whatever that is in your stack.

## The method

### Detect the move
Three tripwires, cheapest first. An email hard bounce from a previously good address is the earliest and cheapest signal, treat every bounce on a key contact as a possible move. Second, an enrichment lookup: run the contact through Clay, Common Room, or FullEnrich and compare current company against your CRM. Third, a manual LinkedIn check on your top contacts on a set cadence, monthly for champions at customer accounts, weekly for key contacts on open deals. If you run the job-change-watchlist skill, detections arrive from there and you skip straight to verification.

### Verify it is real
A profile update is not a move. Confirm both title AND company changed. A new title at the same company is a promotion, which is a different play entirely (congratulate them, then re-map reporting lines). Require two of three before acting: LinkedIn shows the new company, enrichment confirms it, or the old email bounces. One source alone triggers a check, not the play.

### Score both sides
Every verified move gets two scores, because every move is two events.

- Old-account risk score. Higher when: the account is a customer up for renewal inside two quarters, the mover was the only engaged contact, they were the economic buyer or day-to-day power user, and no successor is named. A champion leaving a multi-threaded account with a named successor is LOW. A champion leaving a single-threaded renewal is CRITICAL.
- New-account opportunity score. Driven by prior engagement depth, not by the new company's firmographics. Did they use the product weekly or just sign the contract? Did they attend QBRs, open your emails, expand the account? Deep behavioral history scores HIGH even if the new company looks like a stretch fit. This weighting is deliberate: when we backtested a win-scoring model against real won and lost deals, the strongest predictor of a win was a behavioral signal at 3.56x lift, against 1.13x for the firmographic fit score. What they did with your product beats where they landed.

Engagement older than STALE_DAYS decays. A power user from three years ago is a warm lead, not a hot one. Say so in the score.

### Write the two motions
Motion one, the internal flag. One paragraph in the CRM and the alert channel: who left, what they owned, the risk score with its reasons, and a named owner with a dated next step. "Champion left" with no owner is not a flag, it is a shrug. If the mover was on an open deal, the flag includes a re-map: who inside the account now owns the problem the deal was solving, and which remaining contact can tell you.

Motion two, the door-opener. A short message to the mover at their new company, sent inside the TOUCH window. Rules: congratulate the move specifically, reference the shared history in one concrete line (a project shipped, a result they drove, a problem they solved with your product), then a soft ask, not a pitch. Never reference how you found out beyond LinkedIn. Never mention the old account's renewal, their old colleagues' status, or anything that reads as surveillance. You are a familiar name saying congratulations, with a door behind it.

## Quality gates
- No play runs on an unverified move. Two of three sources, or it stays a check.
- No risk flag ships without a named owner and a dated next step.
- No opportunity score without the engagement evidence behind it, listed. "They liked us" is not evidence.
- The door-opener references at most one piece of shared history and zero facts the mover has not made public.
- A promotion (title change, same company) never triggers this play.

## Output (example)
```
CHAMPION MOVE · sample data
Mover: Dana Reyes · was VP Ops at Northwind (customer) · now COO at Vertex Labs
Verified: LinkedIn + enrichment agree · old email hard-bounced 07/28

Side          Score      Why
Northwind     RISK HIGH  Renewal in Q4, Dana was 1 of 2 engaged
                         contacts, no successor named
Vertex Labs   OPP HIGH   Dana ran 14 sequences/wk, attended 3 QBRs,
                         drove the seat expansion last year

Motion 1 (internal): Flag Northwind churn-risk HIGH. Owner: account
  CSM. Next step by Fri: call remaining contact, ask who inherits
  Dana's workflows, start successor map.
Motion 2 (door-opener): Congrats note to Dana at Vertex Labs
  referencing the reporting workflow she built. Ship within 5 days.
```

## Example chat
Here is the skill running on a single detected move, start to finish.

**You:** My champion at Northwind just left. Dana Reyes, she was our power user there. Here's my contact export. [pastes CSV]

**Claude:** Verified first: LinkedIn shows Dana as COO at Vertex Labs and her Northwind email hard-bounced last week. Two sources agree, this is a real move, not a promotion. Scored both sides on sample thresholds:
```
Northwind     RISK HIGH   Q4 renewal, Dana was 1 of 2 engaged contacts
Vertex Labs   OPP HIGH    Weekly usage, 3 QBRs, drove last expansion
```
The Northwind flag needs an owner today. Who runs that account now?

**You:** The CSM is Marcus. Draft both motions.

**Claude:** Motion one, for Marcus and the #churn-risk channel: Northwind flagged HIGH, Dana owned the reporting workflows and the renewal relationship, next step is a call to the remaining contact by Friday to map her successor. Motion two, the door-opener to Dana at Vertex Labs: a two-line congratulations referencing the reporting workflow she built, with a soft offer to compare notes once she is settled. No mention of Northwind's renewal, nothing she has not posted publicly. One sharpener: connect your enrichment tool so the next move gets confirmed automatically instead of by hand.

## Go further
The single play is step one. Here is where an operator takes it once the manual version proves out.

- **Stand up the watchlist.** Run the job-change-watchlist skill, or UserGems-style tracking via your enrichment tool, so every key contact is monitored and detections arrive without a manual LinkedIn pass.
- **Wire the tripwires.** Connect Clay or Common Room to re-enrich your champion list monthly, and pipe your sequencer's hard bounces on key contacts into the same detection queue.
- **Route flags automatically.** Connect Salesforce and Slack so a verified move writes the risk flag to the account record and pings the owner in the same minute.
- **Work the network view.** Use LinkedIn Sales Navigator alerts on your top 50 champions so the move surfaces the day it is announced, not the month the email bounces.

The door-opener window is short. Automate the detection so the play starts on day one, not day forty.

## Make it yours
Fork it. Change the scores, the tripwires, the touch window, the message rules. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
