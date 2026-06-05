---
name: leader-update-slides-runbook
description: >
  Reference runbook for generating Mixmax Leader Update Slides (the
  slide-by-slide HTML briefs the CEO uses to write his monthly/quarterly board
  deck). Use whenever the user asks "how do I run the Update Slides", "what
  goes in each slide", "what's the spec for the leader-ceo-updates workflow",
  "how do I tweak a slide", "the slide brief is wrong", or "regenerate just
  the {Sales|CS} Update Slides for {period}". Also use for ad-hoc one-off
  generations outside the scheduled task.
---

# Leader Update Slides — Runbook

This skill documents the Update Slides workflow at a level useful for ad-hoc generation, troubleshooting, or single-slide regeneration. For end-to-end automated runs, use the registered `leader-ceo-updates` scheduled task.

## Where everything lives

- **Spec (canonical):** `Revenue Reviews/specs/CEO_Update_Addendum.md`
- **Output folders:** `Revenue Reviews/Leader Weekly/Update Slides/{Sales,CS}/`
- **Filename convention:** `{YYYY-MM}.html` for monthly, `{YYYY-QN}.html` for quarterly
- **Published path roots** (from the publishing config): `PATH_UPDATE_SLIDES_SALES` and `PATH_UPDATE_SLIDES_CS`

## When to invoke this skill instead of the task

- The user wants to **regenerate one slide** (not the whole brief).
- The user wants to **render a back-period** (e.g., a January 2026 monthly brief that wasn't generated at the time).
- The CEO requested a **format tweak** that needs to be tested before running the full workflow.
- The base report changed and you need to **re-publish** without re-deriving anything.

## Core principles (do not violate)

1. **Inherit, never re-derive.** All numbers come from the approved base report. Never re-query the Gen 1 sheet.
2. **Format reference is the most recent prior live artifact.** Read `2026-03.html` (or whatever is most recent) and match its layout exactly.
3. **Spec wins over style guesses.** When in doubt about slide structure, color, or content, defer to `CEO_Update_Addendum.md`.
4. **Five slides monthly, six slides quarterly.** No exceptions.
5. **Takeaway-style titles.** "Q1 closed at 92% of plan" — not "Bookings".
6. **Writing Guidance callout is mandatory.** Every slide. Italic, in the right column under the bullets.
7. **Current period highlighted.** Green for positive, amber for mixed, red for negative, per the spec's color palette.

## Single-slide regeneration recipe

When the user wants only one slide rebuilt:

1. Read the current `{period}.html` file.
2. Read the spec section for the slide in question (Slides 1–6 are clearly labeled in `CEO_Update_Addendum.md`).
3. Read the relevant subset of the base report (e.g., for Slide 4 Bookings, read only the bookings + channel mix sections).
4. Replace the `<section class="slide-brief">` block for that slide. Leave all other slide sections untouched.
5. Re-validate the QA gate items for that slide (takeaway title, chart with current period highlighted, ≥3 bullets, Writing Guidance, numbers reconcile).
6. Show the diff (or just the new slide rendered alone) to the user before publishing.

## Publishing a regenerated file

Use the `publishing-config-reference` skill from `mixmax-publishing-core` to load the config. Then:

1. GET `${GITHUB_API_BASE}/contents/${PATH_*}{period}.html?ref=${GITHUB_BRANCH}` to fetch the existing SHA.
2. PUT to the same URL with the new base64 content + the SHA.
3. Wait 30–90 seconds, verify Pages URL returns 200.

## Common failure modes

- **Numbers drifted from base report** → revert and re-extract from base report verbatim. Never paper over a discrepancy.
- **Slide cannot be filled (missing data)** → render with chart + `[needs leader input]` placeholder bullet + Writing Guidance. Do not skip.
- **CEO format changed mid-cycle** → update the spec first, then regenerate. Never let a one-off format change drift the spec.
