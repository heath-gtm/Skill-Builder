# Vibecode Prompt

> Turn an app idea into a precise build prompt for an AI app builder (Lovable, v0, Bolt, Replit, and others). Trigger on "build me an app", "prompt for Lovable", "v0 prompt", "vibecode this", "I want to build a tool that", "prompt to build a web app", or any request to spin up an app with an AI builder.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/vibecode-prompt && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/vibecode-prompt/SKILL.md -o ~/.claude/skills/vibecode-prompt/SKILL.md && echo "Installed vibecode-prompt. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/vibecode-prompt/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Vibecode Prompt

## What this does
Takes an app idea in plain words and returns a build prompt structured the way AI app builders want it: the one-sentence product, the pages, the data model, the core interactions, the styling, and what to build first. A vague prompt gives you a vague app. This one gives the builder a spec.

## What you'll need
An AI app builder to paste the result into (Lovable, v0, Bolt, Replit, or similar). No connectors. Bring the idea; the skill builds the prompt.

## Customize this for yourself
| Set this | What it is | Example |
|---|---|---|
| Target builder | The tool you will paste into | Lovable, v0, Bolt, Replit |
| Stack preference | Any framework or service you want it to use | Next.js, Supabase, Tailwind |
| Look and feel | Your default visual direction | "Clean, lots of whitespace, one accent color" |

## The method
1. Name the product in one sentence: what it is and who it is for.
2. List the pages or screens, each with its job in a phrase.
3. Define the data model: the few objects and their fields. Builders go sideways without this.
4. Spell out the core interactions: what happens when the user clicks the main button.
5. Set the styling: the visual direction and the one or two brand colors.
6. Sequence the build: "Start with the data model and the main page. Get that working before anything else." This stops the builder from trying to do everything at once and breaking.
7. Add guardrails: no auth in v1, mock the data, keep it one page until it works.

## Output (example)
Idea: "a tracker for my outreach experiments."
Built prompt:
```
Build a single-page web app: an outreach-experiment tracker for a salesperson.

Pages: one main page, a table of experiments with an "add experiment" form.

Data model:
- Experiment { name, channel, hypothesis, sent, replies, status, notes }

Interactions:
- "Add experiment" opens a form, saves a row to the table
- Each row shows a computed reply rate (replies / sent)
- A status pill: running, won, killed

Styling: clean, lots of whitespace, one orange accent, system font.

Build order: first the data model and the table with mock rows. Get that
rendering. Then the add form. Then the computed reply rate. No auth in v1.
```

## Make it yours
Set your target builder, your stack, and your look. Then describe any tool you want and get a prompt the builder can actually execute. Built by an operator. Customize it, break it, make it better.
