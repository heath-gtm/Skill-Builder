# Positioning Brief

> Turn what you do, who it is for, and why you win into a crisp positioning statement and a full message house. Produces a category frame, value pillars, proof points, and objection reframes your whole team can repeat. Trigger on "help me position this", "write our positioning", "build a message house", "what's our value prop", "how do we describe this", or "our messaging is all over the place".

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/positioning-brief && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/positioning-brief/SKILL.md -o ~/.claude/skills/positioning-brief/SKILL.md && echo "Installed positioning-brief. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/positioning-brief/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Positioning Brief

## What this does
Takes the raw pieces of your story and turns them into positioning the whole team can say the same way twice. It writes one positioning statement, then a message house underneath it: the category you compete in, the two-to-four value pillars that carry the story, the proof under each pillar, and the reframe for every objection you keep hearing. The output is meant to be pasted into a deck, a site, or a rep's mouth.

## What you'll need
You do not need to connect anything to get value today. Bring the three answers below and the skill runs now. Connect the tools and it pulls live language to pressure-test what you wrote.

- Works today with: three inputs pasted in plain text. What you do, who it is for, and why you win against the alternative (including "do nothing"). Add any existing tagline, a competitor name, and two customer quotes if you have them.
- More powerful connected to a web-analytics tool: it sees which of your current pages hold attention, so the pillars follow real interest, not guesses.
- Sharper with a CRM or a call tool: it pulls the objections and win reasons your buyers actually say, so the reframes are theirs, not yours.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the three answers you give it today and gets sharper as you connect tools. It never invents a proof point it cannot see. A missing proof is a labeled gap, not a fabricated stat.

- **Bring your data**: paste your three answers plus any quotes. The skill returns the full statement and message house today. No connection required.
- **Connect your tools**: the same skill pulls win reasons, lost reasons, and live page language automatically, and grounds the pillars in what buyers already respond to.
- **Just exploring**: no answers yet? Get the framework, the exact prompts it asks, and a worked example on a sample product, so you can see the shape before you fill it.

Every run ends with the one thing that would sharpen the next one, a proof point to add or a source to connect.

## Customize this for yourself
This was built for a B2B product sold to a defined buyer. Set these to your situation:

| Set this | What it is | Example |
|---|---|---|
| PRODUCT | the thing you are positioning | a scheduling app, a data platform |
| AUDIENCE | the one buyer this brief speaks to | RevOps lead, Head of Support |
| ALTERNATIVE | what they use if not you | a spreadsheet, a legacy tool, nothing |
| CATEGORY | the frame you want to own | "pick a lane you can win" |
| PILLAR_COUNT | how many value pillars | 3 (use 2 to 4, never 5) |
| PROOF sources | where evidence lives | quotes, case studies, product facts |
| OBJECTIONS | the pushback you keep hearing | "too expensive", "we built it ourselves" |

Position for one audience per brief. A statement that speaks to everyone speaks to no one. Run it again for the next buyer.

## The method

### Positioning statement (one sentence, four parts)
For [AUDIENCE] who [need], [PRODUCT] is the [CATEGORY] that [single differentiated value], unlike [ALTERNATIVE]. If any part is fuzzy, the skill names which part and asks for it rather than guessing.

### Category frame
Name the lane you want to be measured in. A strong frame makes your strengths look like the standard and the alternative look dated. The skill flags a frame that is too broad to win or too narrow to matter.

### Value pillars (2 to 4)
Each pillar is a claim the buyer cares about, not a feature. Two to four only. A fifth pillar is a sign two of them are the same idea wearing different words, and the skill will say so.

### Proof points
Every pillar carries at least one piece of evidence: a customer quote, a hard product fact, or an outcome. A pillar with no proof is labeled UNPROVEN so you can go get the receipt before you ship it.

### Objection reframes
For each objection you keep hearing, the skill writes the one-line reframe that turns the concern into your strength. It reframes, it does not dodge.

## Quality gates
- No pillar ships without at least one proof point, or it is labeled UNPROVEN.
- No fabricated metric. Illustrative numbers are marked as examples, never presented as yours.
- The statement names a real ALTERNATIVE, including "do nothing." Positioning against no one is not positioning.

## Output (example)
```
POSITIONING BRIEF · audience: RevOps lead

Statement:
For RevOps leads drowning in manual pipeline hygiene, [Product] is the
pipeline-automation layer that keeps every deal current without a single
manual update, unlike the spreadsheets and reminders they use today.

Category: pipeline-automation layer (not "CRM add-on")

Pillars:
  1. Always-current pipeline   proof: quote, "we stopped Friday cleanup"
  2. Zero rep data entry       proof: product fact, auto-capture
  3. Trustworthy forecast      proof: UNPROVEN (get a customer outcome)

Objection reframes:
  "We already have a CRM."   -> The CRM stores the deal. It does not keep
                                it honest. That is the gap you feel Fridays.
  "Too expensive."           -> Price it against the hour a day per rep
                                you spend keeping the CRM true.

Next: pillar 3 has no proof. Pull one renewal story to close it.
```

## Where the inputs come from
The three answers (what you do, who it is for, why you win) come from you. PILLAR_COUNT (3) and the two-to-four range are defaults, not laws. Proof points come from your quotes, product facts, and outcomes, or from a connected CRM and call tool. Objections come from your team's memory today and from lost-reason data once a tool is connected. The thresholds are yours to move.

## Make it yours
Fork it. Change the category, the pillar count, the reframes. The point is not to sound like a positioning textbook. It is to say your story the same way twice, everywhere, this quarter. Built by an operator. Customize it, break it, make it better.
