# Evolution Agent

> Close the loop on your own skills. Reads what your quality checks flagged plus the feedback signals coming back (thumbs up and down, click-through, what actually happened to the accounts you scored), then proposes concrete, reviewable changes: tighten a scoring rubric, update a trigger phrase, retire a skill nobody uses, add a workflow a usage pattern is begging for. You approve each change; nothing edits itself. Built for anyone running a library of AI skills, customizable to your feedback sources. Trigger on "what should we improve", "apply the QA findings", "propose the scoring update", "retire unused skills", "evolve the system", or any self-improvement question.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/evolution-agent && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/evolution-agent/SKILL.md -o ~/.claude/skills/evolution-agent/SKILL.md && echo "Installed evolution-agent. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/evolution-agent/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Evolution Agent

## What this does
Turns the signals your system is already producing (quality-check findings, feedback reactions, and real outcomes) into a short list of concrete proposed changes to your own skills, scores, and workflows. Each one arrives as a reviewable proposal with the data behind it. You approve; the system updates. It never edits itself. This is the layer that makes a library of skills improve over time instead of drifting.

## What you'll need
You do not need to connect anything to get value today. Paste your findings and the skill runs now. Connect the tools below and it reads the feedback and outcome streams automatically.

- Works today with: your quality-check findings and any feedback you have collected (thumbs, notes, outcomes). Paste them and the skill drafts the changes.
- More powerful connected to your feedback log: it reads reactions, click-through, and re-asks automatically instead of you summarizing them.
- Sharper with outcome data: cross-references what a skill predicted against what actually happened (did the AT_RISK deals slip, did the high-fit accounts convert).
- Sharper with a version-control connector: writes each proposed change as a reviewable diff you can approve in one click.

## How this runs at your connection level
This skill is never reliant on a connector. It runs on the findings and feedback you paste today and gets sharper as you connect the streams it reads. It never claims an improvement it cannot show in the data, and it never merges a change on its own.

- **Bring your data**: paste your QA findings and feedback. The skill drafts the proposed changes today, each with its rationale. No connection required.
- **Connect your tools**: the same skill reads the feedback log and outcome data automatically and turns proposals into ready-to-review diffs. Same output, less effort, sharper.
- **Just exploring**: nothing collected yet? Get the framework, the four change types, and a worked example, so you can see the shape before you feed it signal.

Every run ends with the one thing to review first: the single highest-priority change, and why it matters now.

## Customize this for yourself
This was built to evolve a suite of GTM skills. Set these to your stack:

| Set this | What it is | Default / Example |
|---|---|---|
| FEEDBACK SOURCES | where signal comes from | thumbs up/down, reactions, click-through, written notes |
| OUTCOME SOURCE | how you attribute results | CRM outcomes, win/loss, renewal result |
| SKILL LIBRARY | what it proposes changes to | your SKILL.md files, scoring rubrics, workflow specs |
| APPROVAL GATE | who signs off | you, always; nothing auto-merges |
| RETIRE_DAYS | unused window before a deprecation proposal | 90 |
| ACCURACY_FLOOR | precision below which a skill gets flagged | 75% |

## The method

### Read both feedback streams
Implicit signals (reactions, click-through, re-asks, outcome attribution) and explicit signals (thumbs plus structured reasons). Neither alone is enough. A single thumbs-down is noise; the same pattern across both streams is a signal worth acting on.

### Attribute outcomes honestly
Cross-reference each skill's predictions to what actually happened, controlling for cohort confounds (window size, segment mix, sample size). Never claim a lift without accounting for what else moved. Small samples lie, and a self-improving system that believes its own inflated numbers gets worse, not better.

### Propose, never merge
Every change ships as a reviewable proposal with a diff and a rationale tied to data. Four kinds:
- **Tighten a rubric**: when two tiers converge on the same outcome, collapse or re-cut them.
- **Update a trigger or definition**: when language in the field has shifted (a new tool named in calls, a new phrase reps use).
- **Propose a new workflow**: when the same sequence of skills fires together often enough to bundle.
- **Retire a skill**: when it is unused past RETIRE_DAYS or persistently below ACCURACY_FLOOR.

### Name the one thing to review first
Every pass ends by surfacing the single highest-priority change, usually the skill whose accuracy dropped below the floor, with the specific cases to investigate.

## Quality gates
- Every proposal has a rationale tied to data. Not "tighten this rubric" but "STRONG_FIT converted at 82% and FIT at 79%, too close to differentiate. Collapse to one tier plus an above-baseline override."
- Nothing auto-merges. Every change is a reviewable proposal you approve before anything updates.
- Outcome claims are honest. No "we improved win rate by 5%" without controlling for cohort confounds.
- A skill is retired only on evidence: low invocation past the window, or precision below the floor, never a hunch.

## Output (example)
```
EVOLUTION PASS - week of May 25
4 proposed changes ready for review

1. Tighten the fit rubric
   STRONG_FIT converted 82%, FIT 79% (too close). Collapse to one tier
   plus an "above-baseline" override.
2. Add a term to the tech-stack list
   A tool showed up in 12 calls this month vs 4 last quarter.
3. Propose a new workflow: renewal prep
   The same 3 skills fired in the same order 17 times. Bundle them.
4. Retire an unused skill
   Invoked twice in 180 days, both tests. Deprecate.

Accuracy (trailing 90 days):
  Fit scoring     82%
  Deal health     78%
  Churn predict   67%   <- below the 75% floor

Review first: churn prediction at 67%. Tighten it or lower its confidence.
```

## Where the numbers come from
RETIRE_DAYS (90), the 75% accuracy floor, and the trailing-90-day window are defaults from one team's cadence, not laws. A fast-moving library wants a shorter unused window; a high-stakes one wants a higher accuracy floor. Re-tune them to how much risk you carry. The loop (read both streams, attribute honestly, propose, approve) does not change. The thresholds are yours.

## Make it yours
Fork it. Change the feedback sources, the floors, the windows, the change types. The point is not to run someone else's improvement loop. It is to make your own skills compound instead of rot, with a human on every merge. Built by an operator. Customize it, break it, make it better.
