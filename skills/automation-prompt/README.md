# Automation Prompt

> Turn a "when X happens, do Y" idea into a precise build prompt for an automation platform (n8n, Make, Zapier, and others). Trigger on "build an automation", "n8n prompt", "Make scenario", "Zapier prompt", "automate this workflow", "when X happens do Y", or any request to wire up a no-code or low-code workflow.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/automation-prompt && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/automation-prompt/SKILL.md -o ~/.claude/skills/automation-prompt/SKILL.md && echo "Installed automation-prompt. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/automation-prompt/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Automation Prompt

## What this does
Takes a workflow idea in plain words and returns a build prompt structured for an automation platform: the trigger, the steps in order, the data that moves between them, the branches, and the error handling. Automations break on the details. This pins them down before you build.

## What you'll need
An automation platform to build in (n8n, Make, Zapier, or similar). No connectors here; the prompt describes the workflow you then assemble. Bring the "when X, do Y."

## Customize this for yourself
| Set this | What it is | Example |
|---|---|---|
| Target platform | The tool you will build in | n8n, Make, Zapier |
| Your apps | The services in your stack the workflow will touch | Your CRM, your email, your sheet |
| Error policy | What should happen when a step fails | "Log it and notify me, do not retry silently" |

## The method
1. State the trigger precisely: what event starts this, and how often it can fire.
2. List the steps in order, each as "take this, do that, pass this along."
3. Name the data that moves between steps. The field that step 2 needs from step 1 is where automations break.
4. Add the branches: "if the record already exists, update it; if not, create it."
5. Add error handling: what happens when a step fails or returns nothing.
6. Add a test plan: the one input you will run through it to confirm it works end to end.

## Output (example)
Idea: "when a lead fills the form, add them to the CRM and Slack me."
Built prompt:
```
Platform: n8n.

Trigger: webhook, fires when the website form is submitted. Expect { name,
email, company, message }.

Steps:
1. Look up the email in the CRM (search by email).
2. Branch:
   - If found: update the record, append the message to notes.
   - If not found: create a new lead with the form fields.
3. Post to Slack #leads: "New lead: {name} at {company}. {message}"

Error handling: if the CRM step fails, post to Slack #alerts with the error and
the raw payload. Do not drop the lead silently.

Test: submit one form with a known email and one with a new email. Confirm one
updates and one creates.
```

## Make it yours
Set your platform, your apps, and your error policy. Then describe any "when X, do Y" and get a build prompt with the data flow and the failure cases already mapped. Built by an operator. Customize it, break it, make it better.
