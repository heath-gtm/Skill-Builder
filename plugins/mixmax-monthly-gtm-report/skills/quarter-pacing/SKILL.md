---
name: quarter-pacing
description: The save-or-exceed-the-quarter math for the Mixmax Monthly Report. Uniquely monthly — too granular for quarterly, too big for weekly. Produces the QTD scorecard, catch-up requirement, Commit Creep Watch, Forecast Confidence Index, and the 30-Day Intervention Window. Use whenever the monthly analysis needs to answer "are we on track to hit the quarter, and if not, what specifically has to happen in the next 30 days?" Trigger on phrases like "save the quarter", "exceed the quarter", "QTD pacing", "catch-up math", "commit creep", "commit trajectory", "forecast confidence", "intervention window", "what has to happen this month", "quarter-to-date vs plan", "pacing scorecard", "can we hit the quarter", or any request for mid-quarter intervention.
---

# Quarter Pacing — The Save-or-Exceed-the-Quarter Engine

The monthly report's most important section. Weekly is too noisy to do quarter pacing; quarterly is too late. Monthly is the ONLY cadence where intervention can still change the outcome. This skill produces the math and the specific plays that let the CRO walk into the next week knowing exactly what to do.

## Core mandate

1. **Pacing math must be explicit.** Not "we're tracking well" — exact numbers, exact gap, exact catch-up requirement.
2. **Intervention list has a hard cap of 5.** If everything is a priority, nothing is. The 30-Day Intervention Window is 5 items. Max.
3. **Commit Creep Watch is mandatory.** Track Commit at Month 1 vs Month 2 vs Month 3 of quarter. Shrinking Commit is the #1 silent killer of quarters.
4. **Forecast Confidence Index has a single rollup score** — green / yellow / red + one sentence. The CEO should be able to read just that number and know the state.

## Inputs

Sheet tabs (Monthly snapshot):
- **Monthly Revenue Summary** — MTD, QTD, vs Target, vs Plan
- **AE Forecast** — Commit, Best Case, Pipeline by rep (both current snapshot AND prior monthly snapshots if available)
- **Monthly Bookings Summary** — bookings by channel, segment
- **Rep Summary** — attainment MTD and QTD per rep

Cross-skill references:
- `revenue-analysis` — underlying ARR math
- `deal-management` — deal-level context on Commit/Best Case population
- `direct-sales` (monthly) — rep-level pacing diagnosis
- `mixmax-revenue-reporting` — source-of-truth cells

## Required sections

### 1. QTD Scorecard

Three-column table by metric. Compute for: Total ARR, Total Bookings, New Biz, Expansion, Churn, Net New ARR.

| Metric | QTD Actual | QTD Plan (pro-rated) | Variance ($ + %) |

Pro-rate the plan based on fraction of quarter elapsed (e.g. end of Month 2 = 66.67% of quarter target). Flag any line with variance worse than -10%.

**Output:** one-sentence state-of-the-quarter per the aggregate — "at end of Month 2, we're tracking $X ahead / behind plan on a $Y quarter."

### 2. Catch-Up Requirement (THE MATH)

Explicit math, not vibes:

```
Quarter Target: $Q
QTD Actual: $A
Remaining Gap: $Q - $A = $G
Weeks Remaining in Quarter: W
Required Weekly Run-Rate: $G ÷ W = $R/week
Historical Weekly Run-Rate (last 3 months average): $H/week
Catch-Up Multiplier: $R ÷ $H = Mx

Required Pipeline (at historical win rate): $G ÷ (win rate %)
Current Qualified Pipeline for remaining weeks: $P
Pipeline Coverage for catch-up: $P ÷ required = coverage ratio
```

**Output:** honest assessment. If Catch-Up Multiplier > 1.5x and Pipeline Coverage < 3x, the quarter is in trouble and must be stated plainly.

### 3. Commit Creep Watch

Table: Commit $ at start of Month 1 | Month 2 | Month 3. QoQ trend comparison.

**Interpret:**
- Shrinking Commit month-over-month = reps are pulling back as the quarter matures. This is almost always a bad sign — either deals slipping or initial forecast was inflated.
- Growing Commit = reps gaining confidence, deals firming up. Healthy.
- Flat Commit = neutral, but dig into whether the COMPOSITION is changing (new deals coming in, old ones dropping out).

**Output:** per-rep Commit trajectory for any rep whose Commit shrank >15% MoM. These reps need conversations this week.

### 4. Forecast Confidence Index (FCI)

Blend of four signals into one rollup score (0–100, mapped to green / yellow / red):

1. **Forecast accuracy history** (40% weight) — how accurate was our Commit at start of last quarter vs what closed? If we were within 5%, score 40. Within 15%, score 25. Worse, score 10.
2. **Pipeline coverage** (25% weight) — current qualified pipeline ÷ remaining quarter gap. >3x = 25, 2–3x = 15, <2x = 5.
3. **Stage distribution health** (20% weight) — % of Commit deals in late stage (SQO / Negotiation / Proposal). >70% late = 20, 50–70% = 12, <50% = 5.
4. **Stuck-deal penalty** (15% weight) — % of Commit deals that have been in current stage >14 days. <10% stuck = 15, 10–25% = 8, >25% = 0.

Map total: 75–100 = green. 50–74 = yellow. <50 = red.

**Output:** the number, the color, and a one-sentence "why" that names the weakest sub-signal. E.g. "FCI: 58 (Yellow) — pipeline coverage is healthy at 3.2x, but 38% of Commit deals are stuck >14 days."

### 5. 30-Day Intervention Window — THE HEART

**Exactly 5 items. No more.** These are the things that MUST happen in the next 30 days or the quarter is compromised.

Each item follows the Action Item Format:

```
#{1-5}. {Headline} — Owner: {name} — $ at stake: ${amount}

What specifically must happen: {≤25 words, with calendar-date specificity where possible}

Why this one makes the list: {evidence — cell refs, deal names, rep names, whatever makes it undeniable}

Consequence if it doesn't happen: ${dollar miss or $ risk created}

Confirmation check at next monthly: {how we'll know if it actually happened}
```

**Rule:** items must be weighted toward **CONTROLLABLE, NAMED actions.** "Market conditions improve" does not make the list. "Close WidgetCo by May 10 — AE Sarah has exec alignment this Thursday, needs legal to turn redlines in 48 hours" does.

**Rule:** items must collectively address the quarter gap. If the gap is $200K and the 5 items add up to $50K of upside, that's a broken intervention plan — flag it explicitly.

### 6. Projection + Recommendation

Given QTD pacing, FCI, and the 30-day intervention list:

- **Projected EOQ outcome** at current trajectory (ignore interventions): $X
- **Projected EOQ outcome** if 3 of 5 interventions land (realistic case): $Y
- **Projected EOQ outcome** if all 5 land (best case): $Z

State which of these three the report is recommending leadership communicate to the board / company. Usually this is (2) — realistic case, with transparency on what it depends on.

## Output modes

**Mixmax Monthly (org-wide):** sections 1, 2 (summary only — hide the raw math), 3 (if material), 4 (FCI + one-sentence state), 5 (full 5-item list), 6 (recommendation only).

**CRO Monthly:** everything. Full pacing math, per-rep Commit Creep, full FCI breakdown, full 5-item intervention plan with per-deal detail.

**Month-Ahead report:** section 5 becomes the spine of Month-Ahead — those 5 interventions become the month's priority list for the GTM team.

## When the math says the quarter is lost

Be honest. If Catch-Up Multiplier is >2x, Pipeline Coverage is <2x, and the 5 interventions collectively cover less than half the gap — say so clearly. The report's job is to inform decisions, not protect feelings. Phrase it as: "At current trajectory and with realistic intervention assumptions, we project landing the quarter at X% of plan. Recommend leadership align on communications and on structural plays for next quarter rather than heroic mid-quarter compression."

Never soft-pedal a miss. The CRO needs the honest read to make the right call.
