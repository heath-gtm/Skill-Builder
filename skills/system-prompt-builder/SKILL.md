---
name: system-prompt-builder
description: Build a durable system prompt or project instruction set for an AI assistant (a Claude Project, a GPT, a custom agent). Trigger on "write a system prompt", "build a Claude project", "custom GPT instructions", "agent instructions", "give my AI a persona", or any request to set up a reusable assistant.
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

## Example chat

**You:** I want to set up a Claude Project for first-pass support replies. Can you write the system prompt?

**Claude:** Here's the standing brief.
```
You are a first-pass support assistant for a B2B software product. You draft
replies for a human to review and send. You do not send anything yourself.

Knowledge: treat the linked product docs as ground truth. If an answer is not
in the docs, say so and draft your best guess clearly labeled as unconfirmed.

Boundaries: never promise a refund, a timeline, or a feature. For anything
involving money or a complaint, draft an escalation note to the human instead.
```
Key insight: the boundaries section is the part most people skip, and it's the one that keeps the assistant from making a promise nobody authorized. One sharpener: add a second worked example that shows how it declines an out-of-scope request, right now it only shows the happy path.

## Go further
The prompt is written. Here is where an operator takes it once the manual version proves out.

- **Keep the assistant current without a rewrite.** Point the knowledge section at a live doc (Notion) instead of pasted text, so ground truth updates without touching the prompt.
- **Test it before it goes live.** Run the finished prompt through a small eval, a dozen realistic requests, and check it holds the boundaries before the team starts relying on it.
- **Give it a place to escalate to.** Wire the refusal line to open a Slack thread with a human instead of just declining, so an out-of-scope request does not dead-end.

The prompt sets who it is once; the connections keep it accurate after that.


## Make it yours
Set the assistant's job, its reference material, and its hard rules. Then any AI you stand up starts every conversation already knowing who it is. Built by an operator. Customize it, break it, make it better.
