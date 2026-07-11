# Account Brief Prompt

> Build a reusable prompt that turns any account's raw notes, CRM export, or research into a one-page account brief. Trigger on "account brief prompt", "build me an account brief template", "prompt to research an account", "turn my notes into a brief", "one-pager prompt for accounts", or any request to standardize account prep.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/account-brief-prompt && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/account-brief-prompt/SKILL.md -o ~/.claude/skills/account-brief-prompt/SKILL.md && echo "Installed account-brief-prompt. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/account-brief-prompt/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Account Brief Prompt

## What this does
Builds a reusable prompt that turns whatever you have on an account (pasted notes, a CRM export, a few links) into a consistent one-page brief. Run it on any account and get the same shape every time: the verdict, the why, the people, the next move. You are building the template once and reusing it forever, no connectors required.

## What you'll need
An AI chat tool to run the brief prompt in, and whatever raw material you have on an account to paste in. No connectors. The prompt does the structuring.

## Customize this for yourself
| Set this | What it is | Example |
|---|---|---|
| Your brief sections | The fixed shape every brief follows | Verdict, why, people, competitive flag, next move |
| Your verdict scale | The labels your verdict uses | Reach out / Monitor / Nurture / Pass |
| Your house rules | What to do with thin input | "If a section has no evidence, write 'unknown.' Do not invent." |

## The method
1. Fix the sections. Decide the handful of blocks every brief always has, in order.
2. Fix the verdict scale. A short set of labels so two briefs are comparable.
3. Write the prompt so it reads the pasted material, fills each section from it, and marks anything it cannot find as unknown rather than guessing.
4. Add the named-recipient rule: the brief must name one specific person to contact, not "the team."
5. Add the honesty rule: thin input produces a thin brief that says what is missing, never a confident brief built on nothing.
6. Save the prompt. Reuse it on every account.

## Output (example)
The reusable prompt it builds:
```
You are an account researcher. Turn the material below into a one-page brief.

Output exactly these sections:
- Verdict: one of Reach out / Monitor / Nurture / Pass, plus one sentence why
- Why: 3 bullets, each a fact from the material, no adjectives without a number
- People: the named contacts and their roles; mark the one to reach out to first
- Competitive flag: any competitor named in the material, else "none found"
- Next move: one sentence, naming the person and the angle

Rules: use only what is in the material. If a section has no evidence, write
"unknown." Name one specific person in Next move, never "the team."

Material:
[paste notes, CRM export, links]
```

## Make it yours
Set your sections, your verdict scale, and your house rules. The skill hands you a prompt you paste once into a Project or a saved prompt and run on every account from then on. Built by an operator. Customize it, break it, make it better.
