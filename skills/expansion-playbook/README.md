# Expansion Playbook

> Find the next expansion inside an account and build the pitch that lands it. It reads the signals that say ready, picks the right play (seats, tiers, or a new use case), and writes the ask tied to an outcome the customer already values. Built for B2B customer success and account teams, customizable to your CRM and product analytics. Trigger on "where can I expand this account", "is this account ready to grow", "build an upsell", "cross-sell play", "expansion pitch", or any grow-the-account move.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/expansion-playbook && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/expansion-playbook/SKILL.md -o ~/.claude/skills/expansion-playbook/SKILL.md && echo "Installed expansion-playbook. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/expansion-playbook/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Expansion Playbook

## What this does
Looks inside an account you already own and finds the next dollar: more seats, a higher tier, or a new use case. It reads the signals that say the account is ready, picks the play that fits those signals, and writes a pitch tied to an outcome the customer has already felt. It only recommends the expansion the data supports, and it says when there is none.

## What you'll need
You do not need to connect anything to get value today. Bring what you know about the account and the skill runs now. Connect the tools below and it pulls the rest and adds signals you cannot paste by hand.

- Works today with: current seats and tier, who uses what, the outcomes delivered so far, and any teams or use cases not yet on the product. Paste it or upload a doc.
- More powerful connected to a CRM: it reads the account, current ARR, products owned, and contacts automatically.
- Sharper with a product-analytics tool: turns "they seem active" into which teams and features are actually maxed out.
- Sharper with an enrichment tool: sizes the untapped teams and roles inside the company you have not reached.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste seats, usage, and outcomes. The skill finds and pitches the expansion today on your real account. No connection required.
- **Connect your tools**: the same skill pulls products owned, usage, and org size automatically and adds signals you cannot paste by hand. Same play, less effort, sharper.
- **Just exploring**: no account yet? Get the framework, the exact signals it reads, and a worked example on a sample account, so you can see the shape before you feed it.

Every run ends with the one signal that would most sharpen the play, a field to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS org growing named accounts. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| CRM | your CRM connector | Salesforce, HubSpot, Pipedrive |
| PRODUCTS owned | what the account already has | seats, tier, modules |
| USAGE source | where adoption lives | product analytics, a usage export |
| READY signals | what says expansion-ready | seats maxed, feature-limited, new team appearing |
| EXPANSION types | the plays available | more seats, tier upgrade, new use case, cross-sell |
| ORG map source | how you size untapped teams | enrichment tool, org chart, LinkedIn |
| OUTCOME proof | the win you pitch from | hours saved, revenue influenced, cycle time |

Pitch from an outcome the customer already values. An expansion tied to a felt win closes; an expansion tied to your quota does not.

## The method

### Read the ready signals
Expansion-ready looks like: seats fully active and bumping the limit, a feature or tier the account keeps hitting the ceiling of, a new team showing up in usage, a second use case emerging on its own, a strong health score with a happy sponsor. If none of these are present, the honest answer is "not yet," and the skill says so.

### Pick the play
Match the play to the signal. Maxed seats point to more seats. Ceiling-hitting points to a tier upgrade. A new team in usage points to a land-and-expand into that team. A second use case points to a cross-sell. Do not stack every play at once; lead with the one the signals most support.

### Size it
Estimate the expansion: how many seats, which tier, what the new team is worth. Use enrichment or the org map to size the untapped part of the company. Mark the size an estimate when you cannot see it, and name the input that would make it firm.

### Write the pitch
Anchor on the outcome already delivered, then extend it. "One team cut its cycle time this much; the next team runs the same motion and is not on it yet." Name the buyer, the ask, and the proof. One clear ask beats a menu.

### Time it
Tie the ask to a moment: a QBR, a hit milestone, a renewal, a new-team launch. An expansion pitched at the right moment feels like help; the same pitch at the wrong moment feels like a shakedown.

## Quality gates
- No expansion recommended without a ready signal to back it. "Not yet" is a valid, honest output.
- The pitch anchors on a delivered outcome, never on your quota.
- Any expansion size that cannot be measured is marked an estimate with the input that would firm it.
- One primary play per account, not a menu of five.

## Output (example)
```
EXPANSION READ · sample account · current 9 seats, mid tier
READY SIGNALS                          PLAY
9/9 seats active, 2 waitlisted         +5 seats
Hitting the reporting ceiling monthly  tier upgrade
New ops team appearing in usage        land the ops team

Primary play: +5 seats.
Proof: the current team is fully adopted and turning people away.
Ask: add 5 seats now, revisit the tier at the next review.
Buyer: the sponsor who owns the team.
Timing: pitch at the QBR in 3 weeks, off the adoption win.

Estimated expansion: ~55% of current ARR (illustrative, confirm seat price).
```

## Where the numbers come from
The seat counts, sizes, and percentages come from the data you paste or the tools you connect. Nothing above is a real customer number; it is illustrative. When the skill cannot size an expansion, it marks it an estimate and names the input, a seat price or an org map, that would make it real.

## Make it yours
Fork it. Change the ready signals, the plays, the way you size and time the ask. The point is not to run someone else's upsell script. It is to grow the accounts you already earned, on outcomes they already feel. Built by an operator. Customize it, break it, make it better.
