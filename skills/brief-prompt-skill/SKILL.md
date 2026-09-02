---
name: brief-prompt-skill
metadata:
  version: "1.0.0"
description: >
  Heath's BRIEF prompting framework plus its eval harness. Use to WRITE a
  structured prompt for any go-to-market use case (SDR research, AE deal reads,
  CSM renewal calls, marketing lead scoring, RevOps analysis, win/loss, outreach,
  enrichment columns) and to MEASURE whether that prompt actually works by running
  an eval that reports a pass rate. BRIEF = Brief the goal, Role, Inputs,
  Execution, Finish line. Trigger on "write a prompt for", "build a BRIEF",
  "structure this prompt", "turn this into a prompt", "make this prompt better",
  "eval this prompt", "test this prompt", "what's the success rate of this prompt",
  "score this prompt", "is this prompt reliable", "A/B this prompt", or any request
  to author or evaluate a prompt. especially a repeatable one meant to run across
  many rows, deals, or accounts. Also fire when someone references SPICE and wants
  something more complete, or wants a prompt that produces the same quality every run.
license: MIT
compatibility: cowork claude-code
---

# BRIEF: the prompt framework and the eval harness

Two jobs: **write** a structured prompt with the BRIEF framework, and **prove it
works** with the eval harness. Most prompt tools stop at writing. The reason
prompts fail in production is that nobody measures them, so the second half is
the point.

---

## Part 1. The BRIEF Framework

BRIEF is the house structure for any prompt Heath runs. It keeps the parts SPICE
(Clay's framework) got right and adds the four an agent needs. Every block below
maps to a real failure it prevents.

**B. Brief the goal.** One line on the objective, then the context that makes it
matter. State what counts and what does not; rank the priorities. The model cannot
prioritize what you never ranked. (This is SPICE's Context, sharpened with "why.")

**R. Role.** Name the expert. Not "an assistant." A specific seat ("a skeptical
RevOps analyst who never states a cause he can't tie to deals") changes every word
that follows. SPICE has no role block; this is the cheapest quality upgrade there is.

**I. Inputs.** The data, in its own block, separated from the logic. Use
`{variables}` for anything that changes per run. Dynamic values tangled into
instructions is where prompts rot. (This is SPICE's variable separation, kept.)

**E. Execution.** The steps, in order, with decision branches, and the tool to
use at each step. "Check for X. If none, check Y. If none, check Z." Write the
steps or the model writes them for you, with mixed results.

**F. Finish line.** What "correct" looks like: the output format/schema, the
success criteria, the stopping condition, and one labeled example of a finished
output. This is the block SPICE stops short of. and it doubles as the eval
rubric (see Part 2). If you can't write the Finish line, you don't yet know what
you're asking for.

### Writing a BRIEF prompt

1. Interview only for what's missing. Most requests already imply the goal, the
   inputs, and the constraints. extract those, ask only for the gaps (2-3
   questions max).
2. Draft all five blocks. Label them in the prompt (`[ROLE]`, `[BRIEF]`,
   `[INPUTS]`, `[EXECUTION]`, `[FINISH LINE]`). the labels help the model and
   make the prompt auditable.
3. Make the Finish line verifiable. Every requirement should be answerable
   yes/no against an output ("has 4 named blocks", "every claim cites a count").
   Vague Finish lines can't be evaluated. that's the tell they're too soft.
4. Deliver the prompt clean, ready to paste into Clay, a Claude system prompt,
   an agent, or a one-off ask.

If the user wants content produced *through* the prompt (a post, an email, a
brief), apply Heath's voice via `builtgtm-brand`. BRIEF governs structure, the
brand skill governs the words.

---

## Part 2. The Eval Harness

A prompt without an eval is an opinion. The harness runs a prompt N times across
test cases, scores each output against a rubric built from the Finish line, and
reports a pass rate plus run-to-run consistency. Consistency is the number that
matters: it says whether you get the same quality every run or just got lucky once.

### How it works

The prompt-specific parts live in a JSON **config**, never in the Python. That's
what makes the harness universal. swap the config, eval a different use case, same
engine. It has been validated across SDR, AE, CSM, Marketing, and win/loss configs
with no code changes.

Two kinds of checks, both derived from the Finish line:

- **Structural** (deterministic, no API, 100% reliable). parsed from the output
  by generic check types: `contains_all`, `ordered`, `regex_min`, `regex_absent`,
  `absent_after` (hard-stop), `present_after`.
- **Judge** (LLM-as-judge). a second model call grades the subjective parts
  (is every claim supported by the data, is the recommendation actionable) strict
  yes/no against rubric questions.

### Writing a config

Read `references/example_config.json` for a complete working example (the SDR
research use case). The shape:

```json
{
  "name": "Use case name",
  "model": "claude-sonnet-4-6",
  "prompt": "the full BRIEF prompt, with {data} where inputs go",
  "baseline_prompt": "optional naive one-liner for the A/B, also uses {data}",
  "datasets": [ {"name": "..", "data": "the input string"} ],
  "structural_checks": [
    {"id": "all_blocks", "type": "contains_all", "values": ["BLOCK A", "BLOCK B"]},
    {"id": "order", "type": "ordered", "values": ["BLOCK A", "BLOCK B"]},
    {"id": "cites", "type": "regex_min", "pattern": "\\d+\\s+deal", "min": 3},
    {"id": "stop", "type": "absent_after", "anchor": "LAST BLOCK",
     "values": ["in summary", "in conclusion"]}
  ],
  "judge_checks": [
    {"id": "supported", "question": "Is every claim backed by the input data?"}
  ]
}
```

To build a config from a BRIEF prompt: turn each Finish-line requirement into one
check. Format/order/citation requirements → structural checks. Judgment
requirements (supported, actionable, distinct, not-inflated) → judge checks. Add
one `baseline_prompt` (the naive version of the ask) to get the A/B delta.

### Running it

```bash
# one use case
python scripts/brief_eval.py --config my_config.json --runs 5 --compare
# many use cases on one board
python scripts/run_suite.py --runs 5 cfg_a.json cfg_b.json cfg_c.json
# no API key. verify the scorer against baked-in _mock outputs
python scripts/brief_eval.py --config my_config.json --mock
```

`--compare` runs the baseline too and reports the point delta. `--runs 5` is the
floor for a trustworthy read; one run tells you nothing. Live runs need
`ANTHROPIC_API_KEY`. Both scripts write a branded HTML scorecard (`brief-prompt-skill`
uses the `builtgtm-brand` amber system). pass rate and consistency per prompt,
a bar per criterion, and the BRIEF-vs-naive delta.

### Reading the result

- **Pass rate** = average fraction of checks passed across all runs.
- **Consistency** = 1 minus the spread across datasets. Low consistency means the
  prompt is unreliable even if its average looks fine. tighten the Finish line.
- **Per-criterion bars** show *which* requirement leaks. A low `hard_stop` bar
  means the model keeps adding summaries; a low `claims_supported` bar means it's
  fabricating. Fix the specific block, rerun, watch the bar move.

This is the same loop as a code test suite: define success (Finish line), run the
suite (eval), fix the weakest part, rerun.

---

## How to Apply This Skill

1. **Author request** ("write a prompt for X") → run the BRIEF framework, deliver
   the five-block prompt clean.
2. **Eval request** ("does this prompt work", "what's the success rate") → write a
   config from the prompt's Finish line, run `brief_eval.py`, deliver the scorecard.
3. **Both** → write the BRIEF, then offer to eval it. A prompt that's about to run
   across many rows, deals, or accounts should always be evaluated before it ships.
