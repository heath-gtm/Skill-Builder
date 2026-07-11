# Comms Agent

> Turn a piece of analysis into the thing that ships it. Takes the output of a read (an account verdict, a usage story, a ranked list) and drafts the CRM update, the Slack post, the follow-up email, and the next touch, draft-first and fully logged. Built for any GTM team, customizable to your CRM, your channel tool, and your outreach stack. Trigger on "draft the CRM update for this", "post this to a channel", "write a follow-up to this person", "update the qualification fields on this account", "send this recommendation to a teammate", "draft an outreach sequence", or any write, send, or notify step at the end of a workflow.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/comms-agent && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/comms-agent/SKILL.md -o ~/.claude/skills/comms-agent/SKILL.md && echo "Installed comms-agent. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/comms-agent/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Comms Agent

## What this does
This is the write-side. The other skills read and analyze; this one ships the result. Hand it an account verdict, a usage story, or a ranked list and it drafts what goes out: the CRM field update, the channel post, the personalized follow-up email, the next-touch sequence. Everything is a draft first and everything is logged, so nothing leaves the loop without your eyes on it.

## What you'll need
You do not need to connect anything to get a draft today. Paste the analysis and the target, and the skill writes the copy now. Connect your tools and it writes the update straight into the record or the channel instead of handing you text to paste.

- Works today with: the analysis output plus where it should go (a field, a channel, a person). The skill returns ready-to-paste copy and the exact record or field to drop it in.
- More powerful connected to a CRM: it writes the field update and the contact record directly, with duplicate checking.
- More powerful connected to a channel tool: it posts or drafts the message in the right place.
- Sharper with an outreach tool: drafts a multi-touch sequence in your voice from a style guide you provide.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never writes silently and it never fakes a send.

- **Bring your data**: paste the analysis and the destination. The skill returns the drafted update, post, or email and tells you exactly where it goes. No connection required.
- **Connect your tools**: the same skill writes the field, posts the message, or creates the draft directly, with an audit row every time. Same output, less copy-paste.
- **Just exploring**: no data yet? Get the framework, the operation types it supports, and a worked example, so you can see the shape before you wire it in.

Every run ends with the one thing that would make the next run sharper, a connector to add or a voice sample to feed.

## Customize this for yourself
This was built for a B2B GTM stack. Set these to your tools:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | where field and contact writes go | Salesforce, HubSpot, Pipedrive |
| CHANNEL tool | where posts and DMs go | Slack, Teams, a channel export |
| OUTREACH tool | where sequences and sends go | your sequencing tool, an email client |
| VOICE tool | your playbook and writing style | Octave, a pasted style guide |
| DRAFT_FIRST | draft or autosend by default | draft (opt in per workflow to autosend) |
| AUDIT log | where every write is recorded | a log file or sheet you control |

Wire in one tool or all of them. Each connector unlocks a slice: CRM alone gives you writebacks, a channel tool alone gives you posts.

## The method

### Operation types
One of: crm_field_update, crm_contact_writeback, channel_post, channel_draft, direct_message, outreach_draft, sequence. The skill routes each request to the right operation and returns a structured confirmation.

### Draft-first by default
Email drafts and channel messages are created as DRAFTS, not sends, so the person can review before it goes out. Autosend is an explicit, per-workflow opt-in, never the default.

### Idempotent CRM writes
Before creating a contact, the skill checks for a duplicate. If one exists, it updates instead of creating, so you never pollute the CRM with duplicate records. Field updates capture the before and after value.

### Full auditability
Every write logs a row: timestamp, operation type, target (record and field, or channel and message), before and after values, and which workflow called it. No silent writes, ever.

### Honest connector failure
If a step asks to post to a channel but the channel tool is not connected, the skill says so and aborts that operation. It never fabricates a success.

## Quality gates
- Draft-first is the default. Autosend requires an explicit opt-in.
- No silent writes. Every operation logs an audit row with before and after values.
- Idempotency on contact writes. Check for a duplicate, update instead of creating.
- Honest failure. A missing connector returns "not connected, operation aborted," never a fake success.

## Output (example)
```
CRM WRITE-BACK COMPLETE · 12 contacts processed

Name             Operation        Notes
Contact A         CREATED          verified email + phone written
Contact B         UPDATED          existed, added mobile + profile
Contact C         UPDATED          existed, updated title
Contact D         EXISTING (skip)  all fields already populated
Contact E         SKIPPED          email not found, not written

Summary: 4 created · 6 updated · 1 unchanged · 1 skipped
Audit trail: 12 rows appended to your log

---

CHANNEL POST (DRAFT) · #gtm-pipeline
Mode: draft (autosend off) - review and send when ready
Message: THE DAILY DROP - Friday... [full copy ready to post]
Audit: 1 row appended
```

## Where the numbers come from
There are no thresholds here, only defaults you control: draft-first is on until you opt a workflow into autosend, and the audit log goes wherever you point it. The one rule that does not move is that nothing sends silently and nothing fakes success. Everything else is yours.

## Make it yours
Fork it. Add operation types, change the draft-first rule, point the audit log at your own store. The point is not to run someone else's write layer. It is to ship your own work, reviewed and logged, faster. Built by an operator. Customize it, break it, make it better.
