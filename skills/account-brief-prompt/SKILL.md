---
name: account-brief-prompt
description: Build a reusable prompt that turns any account's raw notes, CRM export, or research into a one-page account brief. Trigger on "account brief prompt", "build me an account brief template", "prompt to research an account", "turn my notes into a brief", "one-pager prompt for accounts", or any request to standardize account prep.
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

## Example chat
**You:** I want a prompt I can reuse to turn my messy account notes into a one-page brief every time.

**Claude:** Built it. Five fixed sections, a four-label verdict scale, and a hard rule against guessing.
```
Output exactly these sections:
- Verdict: Reach out / Monitor / Nurture / Pass, plus one sentence why
- Why: 3 bullets, each a fact from the material
- People: named contacts; mark the one to reach out to first
- Competitive flag: any competitor named, else "none found"
- Next move: one sentence, naming the person and the angle

Rules: use only what is in the material. If a section has no evidence, write "unknown."
```
The part that actually saves you: it writes "unknown" instead of inventing a contact when your notes are thin, so a bad brief looks bad instead of looking confident.

**You:** Run it on this account. [pastes notes]

**Claude:**
```
Verdict: Monitor. Real interest but no economic buyer named yet.
Why: - Champion (Dana, Ops Lead) opened pricing page twice
     - Team of 40, matches ICP size band
     - No stated timeline in the notes
People: Dana (Ops Lead), reach out first. Economic buyer: unknown.
Competitive flag: none found
Next move: Ask Dana who signs off on tools over $10K.
```
One sharpener: paste in your last three account briefs that felt right, and I'll tighten the verdict scale to match how you actually talk about deals, not the default four labels.

## Go further
Running the prompt by hand proves the shape works. Here's how it scales.

- **Turn it into a Project.** Save the prompt as a Claude Project with your CRM notes format pinned, so every rep on the team gets the same brief shape without re-explaining the rules.
- **Trigger it from the CRM.** Wire a Salesforce or HubSpot workflow so any account crossing a stage automatically drops its notes into the prompt and posts the brief to Slack.
- **Batch it weekly.** Point a scheduled Claude task at your whole active pipeline every Monday morning and get one brief per account waiting before standup.

One prompt, reused on every account, is worth more than one perfect brief.

## Make it yours
Set your sections, your verdict scale, and your house rules. The skill hands you a prompt you paste once into a Project or a saved prompt and run on every account from then on. Built by an operator. Customize it, break it, make it better.
