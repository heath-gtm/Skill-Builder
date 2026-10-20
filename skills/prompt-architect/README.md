# Prompt Architect

> Turn a rough task into a precise, ready-to-paste prompt for any AI platform (Claude, GPT, Gemini, and others) using SCRIPT, the six-line structure for a single prompt. Supply the material, Cast the role, Request one thing, Ideal answer, Permissions, Talk to me first. Trigger on "write me a prompt for", "I need an AI to", "help me prompt engineer", "structure this prompt", "use SCRIPT", "turn this into a prompt", "make this prompt better", "optimize my prompt", "write me the prompt to build my ICP Cortex", or any prompt-building request. For more than one seat, or anything that runs without you, hand off to brief-prompt-skill.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/prompt-architect && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/prompt-architect/SKILL.md -o ~/.claude/skills/prompt-architect/SKILL.md && echo "Installed prompt-architect. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/prompt-architect/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Prompt Architect

## What this does
Takes a rough description of what you want an AI to do and returns a precise, structured prompt you can paste into any model. It follows SCRIPT, six lines in the order the model reads best, so the material comes first, the ask is one thing, the model sees an answer that is already right, and it knows what to do when it does not know. One seat, one SCRIPT.

## What you'll need
Any AI chat tool to paste the result into. No connectors. Bring the task and whatever the model has to read; the skill builds the prompt.

## Customize this for yourself
| Set this | What it is | Example |
|---|---|---|
| Target model | The platform you will paste into | Claude, GPT, Gemini |
| Your defaults | House style for every output | "Plain language, no preamble, cite sources" |
| Reusable context | Facts the model should always have | Your company, your audience, your product |
| Standing permissions | What it may never do, every time | "Never invent a number. Never name a price." |

## The method
SCRIPT. Six lines, in this order, and the order is the point.

1. **S, Supply the material.** Paste what it needs to read, first, at the top. Long material before the ask is the one ordering rule with a measured gain behind it. If you have nothing to paste, that is why the answer will be generic.
2. **C, Cast the role.** One line. Who it is, and who it is writing for. Never "an assistant."
3. **R, Request one thing.** The one job, and one line on why it matters. Two jobs is two prompts.
4. **I, Ideal answer.** One example that is already right. Three if tone matters. The shape of the answer, if the example does not show it. An example steers format and tone better than any instruction.
5. **P, Permissions.** What it must do when it does not know: say so, do not guess. Then what it may never do: invent a number, name a price, send anything. Undecided beats invented.
6. **T, Talk to me first.** Before it starts, it lists what it needs from you, then stops. You cannot know your open questions until it has tried and found the gaps.

**For an agent that runs without you**, two changes and nothing else. The steps in order go between I and P, because an unattended run needs the sequence written down. And T becomes stop and escalate, because there is nobody to talk to at 2am. For more than one seat, write a BRIEF first and give each seat its own SCRIPT (see brief-prompt-skill).

**The test it has to pass.** Hand the six lines to a colleague with no context and ask them to write a prompt from it. If they ask what a letter means, the gloss is wrong, not the colleague.

## Output (example)
Rough ask: "summarize customer calls."
Built prompt, S C R I P T in order:
```
[S] TRANSCRIPT
<transcript>
[paste the call here]
</transcript>

[C] You are a customer-research analyst writing for a product team that has
not heard the call.

[R] Summarize this one call so the product team can act on it without
listening. They are deciding what to build next quarter, so what the customer
asked for matters more than how the call felt.

[I] Return exactly these four sections. Here is one done right:
- Verdict: Struggled. Three blockers, no workaround found on the call.
- Quotes: "We tried the export twice and it timed out both times" (admin)
- Feature request: scheduled exports, so nobody has to click
- Next step: rep sends the API workaround by Friday

[P] Quote the customer's own words, never paraphrase a quote. If a section has
no evidence in the transcript, write "none stated." Do not infer sentiment the
words do not support. Never invent a feature name that was not said.

[T] Before you write, list anything in the transcript you cannot place in one
of the four sections, then stop and wait for me.
```
The bracketed letters are there so the prompt is auditable. Drop them if the model you paste into does not need them.

## Example chat

**You:** I need a prompt that summarizes customer calls for the product team. They haven't heard the call.

**Claude:** Built it as a SCRIPT, material first.
```
<transcript>
[paste the call here]
</transcript>

You are a customer-research analyst writing for a product team that has not
heard the call.

Summarize this one call so the team can act on it without listening. They are
deciding what to build next quarter, so what was asked for matters more than
how the call felt.

Return exactly these four sections. One done right:
- Verdict: Struggled. Three blockers, no workaround found on the call.
- Quotes: "We tried the export twice and it timed out both times" (admin)
- Feature request: scheduled exports, so nobody has to click
- Next step: rep sends the API workaround by Friday

Quote the customer's own words, never paraphrase. If a section has no evidence,
write "none stated." Do not infer sentiment the words do not support.

Before you write, list anything you cannot place in a section, then stop.
```
The two lines doing the real work are the permission to write "none stated" and the stop at the end. Without the first, the model invents a verdict from tone. Without the second, it files the one odd thing the customer said under the wrong heading and you never see it.

**You:** Write me the prompt to turn my ICP document into the ICP Cortex. Four files: what we sell, who buys from us, who we say no to, how we score.

**Claude:** One seat, so one SCRIPT. The line doing the work is T: it finds where your document contradicts itself and stops before writing anything, because the conflicts are the actual problem and you have never seen the list.
```
<documents>
[attach every document that describes who you sell to]
</documents>

You are a GTM operator turning one company's scattered ICP material into
four plain documents the whole team and every AI tool read from.

Produce four documents: what we sell, who buys from us, who we say no to,
how we score. Plain prose, no tables, one labeled claim per line.

Each document uses exactly four sections. One done right:
## The short answer (three sentences a new hire could repeat)
## What we believe (one claim per line)
## What we do not know yet (explicitly undecided)
## What this changes downstream (what breaks when this changes)

Never resolve a contradiction yourself; mark it undecided. Never invent a
claim the documents do not support. Never fill a gap to look finished.

Before you write anything, list every place these documents contradict
each other, quoting both versions. Then stop and wait for my decisions.
```
That is the whole ICP Cortex build prompt. The `icp-cortex-builder` skill carries the long form with the three pile sort and the templates.

**You:** Can you make it work for GPT instead of Claude?

**Claude:** Same six lines, same order. The example and the permissions travel across models unchanged; only the framing at the top shifts slightly for how GPT reads instructions. Sharpener: tell me your standing permissions once, the things it must never do on any prompt, and every prompt after this one starts from that line instead of being rebuilt.

## Go further
One well-built prompt is a single task solved. Here is what it looks like running as infrastructure.

- **Turn it into a repeatable column.** Feed the prompt into Clay as an enrichment column so every new call transcript gets summarized the same way automatically, not one at a time.
- **Run it on a schedule.** A scheduled Claude task applies the prompt to every call logged that day and posts the summaries to Slack for the product team each morning. That is an agent, so the steps go in and T becomes stop and escalate.
- **Version it like code.** Keep the prompt in a shared doc or repo with a changelog, so when the output drifts, you can see exactly which line changed and roll it back.

A good prompt gets the same answer twice. The system is what gets it a thousand times without you watching, and that system is a BRIEF.

## Make it yours
Set your target model, your defaults and your standing permissions once. Then describe any task and get a SCRIPT that leaves nothing to chance. Built by an operator. Customize it, break it, make it better.
