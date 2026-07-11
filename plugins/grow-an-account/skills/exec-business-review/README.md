# Executive Business Review

> Prep an executive business review that earns the C-level room, not another QBR nobody remembers. Build the value narrative tied to their strategic goals, the ROI story with the math, and the one ask worth their time. Built for B2B customer success teams, customizable to your product and your buyer. Trigger on "prep an EBR", "executive business review", "C-level review deck", "value narrative for the exec", "ROI story for the renewal", or any executive-review prep.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/exec-business-review && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/exec-business-review/SKILL.md -o ~/.claude/skills/exec-business-review/SKILL.md && echo "Installed exec-business-review. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/exec-business-review/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Executive Business Review

## What this does
Prepares an executive business review that flies higher than a QBR. Not a usage recap. A value story tied to the goals the executive actually owns, backed by the ROI math, ending in a single ask that moves the relationship forward. The room is short on time and long on skepticism. This gives you the narrative that survives both.

## What you'll need
You do not need to connect anything to get value today. Bring what you know about the account and the skill runs now. Connect the tools below and it pulls the evidence automatically and adds signals you cannot paste by hand.

- Works today with: what you can describe. The executive's stated goals, what the account has achieved with you, the usage story, the renewal or expansion context, and the outcome you want from the meeting.
- More powerful connected to a CRM: pulls the account value, the renewal date, the history, and past commitments.
- Sharper with a product-analytics tool: turns "they use it a lot" into the specific adoption and outcome numbers behind the ROI.
- Sharper with a meeting or email tool: surfaces what was promised in past reviews, so this one shows follow-through.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents an ROI number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: describe the account, the exec's goals, and the outcome you want. The skill builds the full narrative today on your real picture. No connection required.
- **Connect your tools**: the same skill pulls value, adoption, and history automatically and adds signals you cannot paste by hand (real usage depth, achieved outcomes, prior commitments). Same output, less effort, sharper.
- **Just exploring**: no account yet? Get the framework, the narrative structure, and a worked example on sample data, so you can see the shape before you build.

Every run ends with the one thing that would make the next run sharper, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org selling into an executive buyer. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | your CRM of choice |
| ANALYTICS | your product-analytics connector | a product-usage tool of your choice |
| EXEC_GOALS | the strategic goals the buyer owns | cost, growth, risk, efficiency |
| VALUE_METRICS | how you prove impact | time saved, revenue influenced, cost avoided |
| ROI_INPUTS | the numbers behind the math | baseline, current state, price |
| ASK | the one outcome you want | multi-year renewal, expansion, exec reference |
| ALTITUDE | how high the story sits | outcomes, not features |

Run any value model you like. The skill ties usage to outcomes to the exec's goals, so point it at their strategic language, not anyone else's.

## The method

### Altitude check (EBR, not QBR)
A QBR reports on the quarter. An EBR speaks to strategy. If a line is about a feature or a ticket count, it does not belong in this room. Every point ladders up to a goal the executive is measured on. Cut anything that does not.

### Value narrative tied to their goals
Start from what the executive is trying to do this year, then show how your product moved it. Not "you used these features." Instead "here is the outcome you wanted, and here is the proof you got closer to it." Their goal is the headline. Your product is the supporting evidence.

### The ROI story with the math
Show the return, and show the arithmetic under it. Baseline, current state, the delta, the cost. An ROI claim with no visible math is a slide the CFO ignores. Keep the exact figures in an evidence layer and round to human scale in the headline.

### The one ask
End with a single, specific ask that matches the value shown. A multi-year renewal, an expansion, an executive reference, a joint plan. One ask. A room given three asks grants none. Earn it with the story, then make it easy to say yes.

### Objection pre-empt
Name the one thing the executive is most likely to push on, and have the answer ready before they ask. Usually it is price, a competitor, or a gap they remember. Walk in with it handled.

## Quality gates
- Every point ladders to a stated executive goal. No orphan features.
- No ROI claim without the math visible behind it.
- Exactly one ask. Specific, matched to the value shown.
- Numbers presented as achieved are sourced, never asserted. Estimates are labeled as estimates.
- The deck reads in the language of outcomes, not the language of the product.

## Output (example)
```
EXECUTIVE BUSINESS REVIEW, prep
Exec goal on the line: cut manual ops time 20% this year

Value narrative
  Goal:     reduce manual handling across the ops team
  Proof:    the team automated the workflow that was eating their week
  Outcome:  ~30% fewer manual steps on that workflow (illustrative)

ROI story (math shown)
  Baseline:  ~X hours/week manual
  Now:       ~Y hours/week
  Value:     (X - Y) hours x loaded rate, vs annual price
  Result:    payback in well under a year (illustrative)

The one ask
  A two-year renewal, in exchange for an executive-sponsored roadmap review.

Pre-empt: they will ask about the competitor's new feature. Answer ready.
```
(All numbers are illustrative.)

## Where the numbers come from
The value metrics and ROI inputs are yours to define. The example figures are illustrative, not benchmarks. Real math comes from your baseline and your price, sourced from the account. The structure does not change. The numbers are yours.

## Make it yours
Fork it. Change the goal framework, the value metrics, the ask. The point is not to run someone else's playbook. It is to run yours, faster, in the room that decides the renewal. Built by an operator. Customize it, break it, make it better.
