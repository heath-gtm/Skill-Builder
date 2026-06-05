# Scoring Audit Methodology — Mode 3

The method for cross-referencing signals to find where Aero (or any internal scoring model) is failing. Output is a list of named accounts the model misclassified, with the signal that disagrees.

## The premise

Aero is one signal among many. When it disagrees with Octave + Amplitude + Common Room + Salesforce, the disagreement IS the finding — there's a scoring gap to investigate.

This method is what produced the answer to "why are we not driving pipeline from Product?" in the Mixmax 2026 PQA cohort. The answer wasn't "rep execution" — it was "16% of the cohort (43 accounts) had a scoring miss that masked real opportunity."

## Two patterns that surface most often

### Pattern A: Aero False-Negatives (engagement miss)
**Definition:** Amplitude shows real, sustained product engagement at the account, but Aero PES sits at floor (28.04 in Mixmax's current model).

**Why it happens:**
- Aero's PES model bins low-engagement accounts together at a single floor value. Real engagement that doesn't cross a threshold doesn't register.
- The floor is opaque to reps — they see "low PES" and de-prioritize, not knowing the model is mis-binning.

**How to detect:**
```
flag = (amplitude_verdict in [POWER, ESTABLISHED]) 
   AND (sfdc.Aero_Product_Engagement_Score__c <= 28.04 OR null)
```

**Example from Mixmax cohort:** Quantum Metric — 19.9 active users/week, 13.9 senders (Power tier), Aero PES = 28.04.

### Pattern B: Aero-Missed ICPs (firmographic miss)
**Definition:** An independent ICP qualifier (Octave) scores the account high (≥7/10) but Aero Account Fit is low (<40) or null.

**Why it happens:**
- Aero has limited firmographic enrichment. When usage data is sparse, it produces "No Score" silently — reps see that as low fit.
- Aero doesn't appear to apply a firmographic-only fallback when usage signal is absent.

**How to detect:**
```
flag = (octave_score >= 7) 
   AND (sfdc.Aero_Account_Fit_Score__c < 40 OR null)
```

**Example from Mixmax cohort:** Toddle — Octave 9 (strong fit), Aero Account Fit 38 (low). Schneps Media — Octave 9, Aero null.

## Three more patterns worth checking

### Pattern C: Buying-title silence
**Definition:** A buying-title role (VP+ in Sales/RevOps/CS) fires the PQA, but the model doesn't weight the trigger user's title.

**Why it matters:** A VP of Sales firing a PQA reads identical to an IC firing one in the current model. The signal of who triggered the event is lost.

**How to detect:** Cross-reference `Account.Last_PQA_Trigger_User__c` (or equivalent) against `Contact.Title` and flag VP+ / Head of / Chief.

**Example from Mixmax cohort:** Contentful — Brett McNay (VP of Sales) was the active user firing the PQA. The brief found him; Aero didn't surface him.

### Pattern D: Trend velocity blindness
**Definition:** An account collapsing from 700 → 50 events scores the same as an account flat at 50. Aero's PES doesn't appear to decay over time.

**How to detect:** Compute 4-week rolling delta from Amplitude. Flag accounts where current-week activity is <30% of 4-week average AND PES hasn't moved.

**Example from Mixmax cohort:** Workato — 701 events week 1 → 48 events week 6, Aero PES unchanged.

### Pattern E: Penetration-ratio blindness
**Definition:** "2 active users" reads the same regardless of whether the account has 3 ICP contacts or 30. ICP penetration (active / mapped) is missing from the model.

**How to detect:** Compute `active_user_count / sfdc_icp_contact_count`. Flag low penetration (<15%) on accounts that look engaged in raw counts.

**Example from Mixmax cohort:** Workato — 2 active / 21 mapped ICP contacts = 9.5% penetration. Aero reads "some engagement"; reality is "one IC trying it solo."

## How to run the audit

### Inputs needed
- Cohort definition (which accounts to audit)
- Per-account: Aero scores, Amplitude PES, Octave qualify result, Common Room org match, SFDC contacts

If you've just run Mode 2 (Sprint Planning), the v2_scored_cohort.json already has everything needed.

### The audit query

For each pattern, scan the cohort:

```python
false_negatives = [a for a in cohort
                   if a.amplitude_verdict in ("POWER", "ESTABLISHED")
                   and (a.aero_pes or 0) <= 28.04]

missed_icps = [a for a in cohort
               if (a.octave_score or 0) >= 7
               and (a.aero_account_fit_score or 0) < 40]
```

### The output

For each pattern, produce:
- Total count + % of cohort
- Top 10 by composite score
- 2-3 specific named examples with full context (the signal that disagrees + recommended action)

If the audit is for a vendor conversation (e.g., showing Aero where their model is failing), tone matters: collaborative, not accusatory. Bring the signal, the examples, and the ask. Don't bring opinions.

## What good output looks like

In the Mixmax 2026 PQA cohort audit:

| Pattern | Count | % of cohort | Top example |
|---|---|---|---|
| Aero False-Negatives | 34 | 13.0% | Quantum Metric (19.9 active users/wk, Aero PES floored) |
| Aero-Missed ICPs | 9 | 3.4% | Toddle (Octave 9, Aero 38) |
| **Combined** | **43** | **16.5%** | — |

The combined number tells you the rough volume of accounts the model is mis-classifying. The named examples make the pattern concrete enough to discuss with the vendor or to override manually in the queue.

## How to share the findings

Three output formats depending on audience:

1. **Internal RevOps brief** — markdown doc with the patterns, counts, examples, and a "what we'd change in the model" section. For the team that owns the model.
2. **Vendor conversation primer** — Slack message or email to the model vendor with the patterns + 1-2 examples each + technical asks. Collaborative tone.
3. **Sprint backlog override** — list of false-negative + missed-ICP accounts to manually promote in the rep queue, regardless of what Aero says.

## Caveats

- **Audit a stable cohort, not a moving one.** Use a snapshot of the cohort taken on a specific date. Don't audit "all accounts as of today" — the data shifts.
- **Make sure your independent signals are independent.** Octave and Aero shouldn't both be reading from the same upstream firmographic provider; if they are, "agreement" is fake.
- **A small false-negative rate isn't a failure.** Every model has misses. The question is whether the rate is acceptable for your conversion economics. 16% is meaningful at Mixmax's price point; at a higher-ACV product, a smaller rate would matter.
- **Caveat your findings with what's not in the data.** If Common Room didn't match 27 of 261 accounts, those are unscored, not validated. Be honest about coverage gaps.
