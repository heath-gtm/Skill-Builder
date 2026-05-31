---
name: evolution-agent
description: The AI-native capstone. Watches QA Agent's audit + reads implicit feedback (emoji reactions, click-through, outcome attribution) + explicit feedback (👍/👎, structured reasons) — then generates pull requests to heath-gtm/Skill-Builder + LOCKED_DESIGN.md that evolve the system — tightens scoring rubrics, updates trigger phrases, amends lock-ins, proposes new workflows when usage patterns suggest them, retires unused analysts. Closes the loop QA Agent surfaces. Heath approves PR → system mutates itself. Trigger on "evolve the system", "apply this week's QA recommendations", "PR the scoring update", "amend lock-in #X", "propose a new workflow", "retire unused analysts", "what should we improve?", or any system-evolution / self-learning question. Also fires automatically after every QA Agent weekly digest.
---

# Evolution Agent — the AI-native capstone

**Required:** File system access (Revenue Reviews) + GitHub (Skill-Builder write access). **Optional:** Slack (for digest engagement signal), Salesforce (for outcome attribution closing the loop).

## What this analyst answers

- "Evolve the system" — full audit + PR-generation pass
- "Apply this week's QA recommendations" — turn QA Agent's digest into reviewable system changes
- "PR the scoring update" — generate a Skill-Builder PR that adjusts a scoring rubric based on accuracy data
- "Amend lock-in #X" — generate a LOCKED_DESIGN.md PR for a lock-in update
- "Propose a new workflow" — when usage patterns suggest a bundle, draft the workflow spec
- "Retire unused analysts" — surface analysts that haven't been called in 90 days + propose deprecation

## What it owns internally — the AI-native flywheel

```
                   QA Agent surfaces drift
                            ↓
              Implicit signals collected
              (emoji reactions, click-through,
               re-asks, outcome attribution)
                            ↓
              Explicit signals collected
              (👍/👎 + structured reasons)
                            ↓
              Evolution Agent reads both streams
                            ↓
   ┌────────────────────────┴────────────────────────┐
   ↓                                                  ↓
PR to heath-gtm/Skill-Builder              PR to LOCKED_DESIGN.md
(modifies SKILL.md files)                   (amends lock-ins)
   ↓                                                  ↓
Heath reviews + approves                   Heath reviews + approves
   ↓                                                  ↓
System mutates itself                      Architecture updates
   ↓                                                  ↓
Next week's analyst outputs are smarter   Workflows compose differently
```

## What it owns internally — concretely

- **Implicit feedback collector**: reads `Revenue Reviews/comms_audit/*.tsv`, `daily_drop_audit/*.tsv`, and Slack reaction counts to derive output-quality signals
- **Explicit feedback collector**: reads `Revenue Reviews/feedback/*.tsv` (rep-submitted 👍/👎 + structured reasons)
- **Outcome attribution engine**: cross-references analyst predictions to actual outcomes (did flagged AT_RISK deals slip? Did STRONG_FIT verdicts convert?)
- **PR generator**: writes GitHub PRs to Skill-Builder + LOCKED_DESIGN.md with surgical changes + rationale
- **Workflow pattern detector**: finds recurring analyst-call sequences in user activity + proposes them as new workflow specs
- **Deprecation surfacer**: flags analysts with low invocation rate or persistently poor accuracy

## Quality gates

**Every PR has rationale tied to data.** Not "tighten this scoring rubric." Instead, "Tighten this scoring rubric — over the trailing 90 days, STRONG_FIT verdicts converted at 82% but FIT verdicts converted at 79% (delta too small). Recommend collapsing FIT and STRONG_FIT into single tier."

**Heath approves before any merge.** The Evolution Agent NEVER auto-merges. Every change is a reviewable PR with diff + rationale.

**Outcome attribution honest.** Doesn't claim "we improved win rate by 5%" without controlling for cohort confounds (window size, segment mix, etc.).

## Output format example

```
🧬 EVOLUTION AGENT WEEKLY · Week of May 25

PROPOSED CHANGES — 4 PRs ready for review

1. tighten-icp-composite-rubric.md (Skill-Builder PR)
   ──────────────────────────────────────────────────
   Rationale: Trailing 90d outcome attribution shows STRONG_FIT (82% conv)
   and FIT (79% conv) too close to differentiate. Collapse to single tier
   "FIT" + add explicit override flag for "ABOVE_BASELINE_SIGNAL".
   Affects: icp-analyst/SKILL.md (composite score breakdown section)
   PR diff: 23 lines changed
   Outcome math:
     • Pre-change: 2-tier classifier, 82% / 79% conversion
     • Post-change: 1-tier + override, projected 85% precision
   → Review: github.com/heath-gtm/Skill-Builder/pull/47

2. amend-lock-in-26-add-Cursor-to-stack.md (LOCKED_DESIGN PR)
   ──────────────────────────────────────────────────
   Rationale: Trailing 30d Mixmax transcripts mention "Cursor" in
   12 calls (vs 4 last quarter). Add Cursor to Sales_Acceleration_Tool__c
   enumeration + the 26-field tech-stack-as-displacement scoring.
   Affects: LOCKED_DESIGN.md lock-in #26
   → Review: github.com/heath-gtm/Skill-Builder/pull/48

3. propose-new-workflow-customer-renewal-prep.md
   ──────────────────────────────────────────────────
   Rationale: Last 8 weeks, "renewal prep for {account}" requests
   triggered Renewal-Health → Conversation → Comms in that order
   17 times. Pattern detected. Propose new workflow spec
   "W7: Customer Renewal Prep" that bundles them.
   Affects: new file at Revenue Reviews/specs/workflows/W7_renewal_prep.md
   → Review: github.com/heath-gtm/Skill-Builder/pull/49

4. retire-deepline:workflow-hello-world.md
   ──────────────────────────────────────────────────
   Rationale: Analyst invoked 2x in last 180 days. Both invocations
   were user-test, not real use. Recommend deprecation.
   Affects: deepline plugin manifest
   → Review: github.com/heath-gtm/Skill-Builder/pull/50

ACCURACY SCORES (trailing 90d):
  ICP Analyst:        82% precision on STRONG_FIT
  Deal-Health:        78% precision on AT_RISK (deals actually slipped)
  Renewal-Health:     91% precision on RENEW verdicts
  Pattern Analyst:    67% precision on predictive churn (low — investigate)

THE ONE THING TO REVIEW FIRST:
  Pattern Analyst predictive churn at 67% precision is below 75% threshold.
  Either tighten the model or surface lower-confidence claims more cautiously.
  → Investigate the 8 false-positive churn flags from last quarter.

Next pass: Sunday 2026-06-06 (after next QA Agent digest)
```

## Used by

- **Weekly system maintenance** (scheduled Sundays after QA Agent)
- **Quarterly architecture review** (deep pattern detection over 90-day windows)
- **Heath manual ad-hoc** ("what should we improve?")
- Standalone — this is the system's self-improvement engine

## When NOT to use

- For real-time decision-making (Evolution Agent runs weekly + on-demand for retrospective improvement)
- For pulling data from connectors (uses other analysts as upstream — never queries directly)
- For autonomous decisions — every change requires Heath's PR approval

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- No direct SFDC reads — consumes audit logs from other analysts + outcome attribution data.
- Generates GitHub PRs that may amend this library file when field changes are needed.

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

Lock-in #33 (QA Agent — Evolution is the next layer on top). This skill's existence locks-in #34 (the AI-native flywheel). All lock-ins and SKILL.md files are downstream targets for Evolution Agent PRs.

## Make.com / API packaging

**Input:** `{ mode: "full_evolution_pass | proposed_PRs_only | accuracy_audit | deprecation_surfacer", trailing_days: 90 }`

**Output:** `{ proposed_PRs: [...], accuracy_scores, top_priority, next_pass_date }`

**Failure modes:** No GitHub write access → cannot generate PRs (falls back to "proposed changes report"). No audit logs → returns "no signal to evolve from."

## Shippable as

Standalone — the meta-meta-layer that turns a productized analyst suite into a self-improving system. Pairs naturally with QA Agent (which surfaces issues) — Evolution Agent generates the change-control actions.

This is the AI-native capstone. Without it, the system is a productized SaaS that improves manually. With it, the system compounds.
