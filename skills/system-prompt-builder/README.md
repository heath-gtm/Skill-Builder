# System Prompt Builder

> Build a durable system prompt or project instruction set for an AI assistant (a Claude Project, a GPT, a custom agent). Trigger on "write a system prompt", "build a Claude project", "custom GPT instructions", "agent instructions", "give my AI a persona", or any request to set up a reusable assistant.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/system-prompt-builder && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/system-prompt-builder/SKILL.md -o ~/.claude/skills/system-prompt-builder/SKILL.md && echo "Installed system-prompt-builder. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/system-prompt-builder/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# System Prompt Builder

## What this does
Builds the standing instructions for an AI assistant you will reuse: a Claude Project, a custom GPT, or an agent. Not a one-off prompt. The durable brief that defines who the assistant is, what it knows, how it behaves, and what it must never do, so every conversation starts aligned.

## What you'll need
An assistant to configure (a Claude Project, a custom GPT, an agent framework). No connectors. Bring the job you want the assistant to own.

## Customize this for yourself
| Set this | What it is | Example |
|---|---|---|
| The assistant's job | The one thing it exists to do | "Draft first-pass support replies" |
| Reference material | Docs or facts it should always have | Your product docs, your tone guide |
| Hard rules | The lines it must never cross | "Never promise a refund. Escalate instead." |

## The method
1. Define the role in one paragraph: who the assistant is and the single job it owns.
2. Set the knowledge: what it should treat as ground truth, and what to do when it does not know.
3. Set the behavior: tone, format, how long answers run, when to ask versus when to act.
4. Set the boundaries: the hard rules, the things it must never do, what to escalate.
5. Give a worked example: one ideal exchange, input and output, so the model has a target.
6. Add the refusal line: how it declines gracefully when a request is out of scope.

## Output (example)
```
You are a first-pass support assistant for a B2B software product. You draft
replies for a human to review and send. You do not send anything yourself.

Knowledge: treat the linked product docs as ground truth. If an answer is not in
the docs, say "I am not certain, a human should confirm" and draft your best guess
clearly labeled as unconfirmed.

Behavior: warm, plain, under 120 words. Lead with the answer, then the steps.
Never open with "Great question." Ask a clarifying question only if the issue is
genuinely ambiguous.

Boundaries: never promise a refund, a timeline, or a feature. For anything
involving money or a complaint, draft an escalation note to the human instead.

Example:
User: "The export button is greyed out."
You: "That usually means the report is still generating. Give it about a minute,
then refresh. If it is still greyed out, tell me your plan tier and I will check
the export limits."
```

## Make it yours
Set the assistant's job, its reference material, and its hard rules. Then any AI you stand up starts every conversation already knowing who it is. Built by an operator. Customize it, break it, make it better.
