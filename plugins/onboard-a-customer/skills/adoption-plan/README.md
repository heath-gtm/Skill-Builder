# Adoption Plan

> Turn "they bought it but nobody uses it" into a plan to fix it. Reads what is unused inside an account, picks the one habit to build next, and writes the enablement plan that gets there. Built for B2B customer success teams, customizable to your product and your onboarding. Trigger on "drive adoption", "which features are unused", "why aren't they using it", "seats sitting idle", "build an enablement plan", or any account-adoption diagnostic.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/adoption-plan && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/adoption-plan/SKILL.md -o ~/.claude/skills/adoption-plan/SKILL.md && echo "Installed adoption-plan. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/adoption-plan/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Adoption Plan

## What this does
Reads how an account actually uses your product, finds the gap between what they bought and what they touch, and picks the single next habit worth building. Then it writes the enablement plan to get there: who to reach, what to show them, and how you will know it worked. One habit at a time, because adoption is a sequence, not a launch.

## What you'll need
You do not need to connect anything to get value today. Bring what you know about the account and the skill runs now. Connect the tools below and it pulls usage automatically and adds signals you cannot paste by hand.

- Works today with: what you can describe or paste. The seats sold, the features in the plan, which ones you have seen them use, who the users are, and where they got stuck. A usage export or a CSV works too.
- More powerful connected to a product-analytics tool: it reads real feature and seat usage automatically, across the whole account.
- Sharper with a CRM: pulls the entitlement, the plan tier, and the account owner so the plan lands on the right desk.
- Sharper with a meeting or email tool: shows what was already promised in onboarding, so the plan does not repeat a training they ignored.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the data you give it today and gets more powerful as you connect tools. It never invents a usage number it cannot see. A gap is a prompt, not a guess.

- **Bring your data**: paste or describe the account. Seats, features, who uses what, where they stalled. The skill runs the full analysis today on your real picture. No connection required.
- **Connect your tools**: the same skill pulls usage and entitlement automatically and adds signals you cannot paste by hand (idle seats, feature depth, the trend over weeks). Same output, less effort, sharper.
- **Just exploring**: no data yet? Get the framework, the exact signals it reads, and a worked example on sample data, so you can see the shape before you feed it.

Every run ends with the one thing that would make the next run sharper, a signal to add or a tool to connect.

## Customize this for yourself
This was built for a B2B SaaS product with multiple features and per-seat licensing. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| ANALYTICS | your product-analytics connector | a product-usage tool of your choice |
| CRM | your CRM connector | your CRM of choice |
| CORE_FEATURES | the features that define value | your top 5 to 10 capabilities |
| ACTIVATION_EVENT | the action that means "adopted" | first workflow completed, first invite sent |
| SEAT field | where entitlement lives | licensed seats vs active seats |
| IDLE_DAYS | no-login days that mean a seat is idle | 30 (re-tune to your cycle) |
| ADOPTION_TIER | how you rank a user's depth | Power / Established / Emerging / Dormant |

Run any adoption model you like. The skill measures "what did they buy versus what do they touch," so point it at your core features, not anyone else's.

## The method

### Adoption gap (bought vs touched)
List what the account is entitled to. List what they actually use. The gap between the two is the whole job. Name the specific unused feature or the count of idle seats. Never say "low adoption" without the line item behind it.

### Pick the one next habit
Do not hand an account a ten-item training plan. Rank the unused features by value-to-effort: high value, low friction, adjacent to something they already do. The winner is the next habit. One. The rest wait their turn.

### Depth tiers per user
Sort the named users into tiers by how deeply they use the product (for example Power, Established, Emerging, Dormant). A Dormant user needs a different push than a Power user missing one feature. The plan targets the tier, not the average.

### Enablement plan (who, what, proof)
For the chosen habit, write the play: the named user or role to reach, the specific thing to show them, the reason it matters to their job, and the usage signal that will prove it stuck. If a champion drives adoption, name them.

### Momentum check
Adoption is a trend, not a snapshot. Compare usage over the trailing weeks. A feature used once and dropped is not adopted. Flag the difference between a spike and a habit.

## Quality gates
- No "low adoption" verdict without the named feature or idle-seat count that proves it.
- Exactly one next habit per plan. If everything is urgent, nothing gets adopted.
- A feature counts as adopted only on a repeated signal, never a single event.
- Idle-seat claims show the last-login evidence, never a guess.

## Output (example)
```
ADOPTION PLAN, one account
Entitled: 40 seats, 9 core features
In use:   26 active seats, 4 features touched
Gap:      14 idle seats, 5 features never opened

Next habit: shared templates (high value, low friction, next to what they already do)
Target:     the ops lead + 3 Emerging users
Show them:  one 15-min walkthrough on their own workflow
Proof:      3+ templates saved and reused within 2 weeks

Then, not now:
  - Reporting module (needs the template habit first)
  - The 14 idle seats (re-provision after the ops team is live)
```
(Numbers are illustrative.)

## Where the numbers come from
IDLE_DAYS (30) and the tier cutoffs are defaults, not laws. They suited a product with a monthly usage rhythm. If your product is touched daily, tighten them. If it is a quarterly tool, loosen them. The logic does not change. The thresholds are yours.

## Make it yours
Fork it. Change the tiers, the activation event, the one-habit rule if you dare. The point is not to run someone else's playbook. It is to run yours, faster. Built by an operator. Customize it, break it, make it better.
