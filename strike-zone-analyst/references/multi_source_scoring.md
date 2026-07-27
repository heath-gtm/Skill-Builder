> **Note.** This is the internal reference rubric for strike-zone Mode 2 (Sprint Planning) and Mode 3 (Scoring Audit). To design a fresh account score for your own business, use the `account-scoring-model-builder` skill.

# Multi-Source Composite Scoring — v2 Rubric

The scoring rubric for Mode 2 (Sprint Planning) and Mode 3 (Scoring Audit). Composite score is 0-100, computed as a weighted sum of 10 sub-scores. Each sub-score is independently 0-100 so weights are transparent.

## Why a composite

No single source is enough. Salesforce knows what's in the CRM. Aero scores firmographic + product fit but has documented blind spots. Amplitude knows actual product engagement. Octave knows ICP qualification independently. Common Room knows community/intent + extra contacts. FullEnrich verifies and adds phones.

Combining them with explicit weights:
1. Surfaces disagreement (an account scoring high in Octave but low in Aero = a signal worth investigating)
2. Rewards signal-richness (an account with 5+ sources agreeing is more confident than one with 1)
3. Forces honesty about where each source contributes — the weights are auditable

## The 10 components and their weights

| # | Component | Weight | Computation |
|---|---|---|---|
| 1 | Octave ICP Score | 20% | `octave_score * 10` (0-100). If `disqualifier_triggered=true`, cap at 10. If `octave_status != "success"`, default to 40. |
| 2 | Octave Playbook Match | 8% | `playbook_score * 10`. If null, default to 40. |
| 3 | Amplitude PES | 15% | Verdict mapping (see below) |
| 4 | Common Room Engagement | 12% | If CR matched: `max(cr_lead_scores percentile)` if present, else 50. If not_found: 30. |
| 5 | Common Room Buying Committee Depth | 8% | `cr_contacts_count`: ≥50→100, 20-49→80, 10-19→60, 5-9→40, 1-4→20, 0 or unmatched→0 |
| 6 | SFDC Aero Account Fit | 10% | `Aero_Account_Fit_Score__c` (0-100). If null: firmographic fallback (see below) |
| 7 | SFDC Buying-Title Signal | 10% | Best title score across contacts (see title rubric below) |
| 8 | SFDC Account Engagement | 8% | GTM stage mapping + recent-opp bonus (see below) |
| 9 | Recency | 4% | Days since cohort anchor: ≤30→100, 31-60→75, 61-90→50, 91-120→35, >120→25 |
| 10 | Ownership clarity | 5% | Named owner = 80. +20 if Growth AE (Karan, Isabelle, Felipe). Null/default → 0. |

**Composite formula:**
```
composite = 0.20*octave_icp + 0.08*octave_playbook + 0.15*amplitude_pes
          + 0.12*cr_engagement + 0.08*cr_buying_depth + 0.10*sfdc_aero
          + 0.10*sfdc_buying_title + 0.08*sfdc_engagement + 0.04*recency
          + 0.05*ownership
```

## Sub-score logic

### Amplitude PES verdict mapping

Pulled from the `product-engagement-story` skill's tier framework:

| Verdict | Score |
|---|---|
| POWER | 100 |
| ESTABLISHED | 85 |
| AERO_FALSE_NEGATIVE | 100 *(override)* |
| EMERGING | 65 |
| DORMANT | 35 |
| UNTOUCHED | 15 |
| GHOST_ACTIVE | 25 *(override)* |
| NO_DATA | 50 |

The two overrides exist because they're cases where the standard tier alone misleads:
- **AERO_FALSE_NEGATIVE** scores 100 because the Amplitude data already proves the account is engaged; the score reflects "high signal regardless of what Aero says."
- **GHOST_ACTIVE** scores 25 because `_active` events fire but no actual capability is being used; not actually engaged.

### Firmographic fallback (when Aero Account Fit is null)

Start at 0, then:
- Industry includes "Software & Services" / "Technology" / "Software" / "Internet" → +30
- Industry includes "Financial" / "Health Care" / "Media" → +15
- NumberOfEmployees 100-5000 → +30
- NumberOfEmployees 30-99 → +20
- NumberOfEmployees 5000+ → +15 (huge enterprises are often competitor or out-of-fit)
- NumberOfEmployees <30 → -10
- Industry is null → -10
- Cap fallback at 70 (never as high as a real Aero score)

### Buying-title rubric (apply to `Contact.Title`, take the MAX across all contacts at the account)

| Title pattern (case-insensitive contains) | Score |
|---|---|
| "Chief Revenue" / "CRO" / "VP Sales" / "VP Revenue" | 100 |
| "Chief Marketing" / "CMO" / "VP Marketing" | 95 |
| "Chief Customer" / "VP CS" / "VP Customer Success" | 95 |
| "Chief Operating" / "COO" / "VP Operations" | 90 |
| "Head of Sales" / "Head of Revenue" / "Head of Growth" / "Head of GTM" | 90 |
| "Head of Marketing" / "Head of Customer Success" | 85 |
| "Director" + ("Sales" / "Revenue" / "GTM" / "Marketing" / "CS") | 80 |
| "Director" + ("Operations" / "RevOps" / "Sales Operations") | 80 |
| "Manager" + ("Sales" / "RevOps" / "GTM" / "Marketing") | 60 |
| "Account Executive" / "AE" / "SDR" / "BDR" / "Sales Development" | 50 |
| Any title present but doesn't match above | 30 |
| No mapped contacts | 0 |

### SFDC Account Engagement

Map `Account_GTM_Stage__c`:
- Engaged → 100
- Customer → 80
- New → 60
- Nurture → 50
- Cold → 40
- Disqualified → 10
- Null/other → 30

Plus +20 (capped at 100) if any Opportunity has `CreatedDate >= today - 365 days`.

## Signal richness bonus

Count how many of the 5 enrichment sources contributed a non-default signal:
1. Octave returned a real score (not 40 default)
2. Amplitude returned a verdict (not NO_DATA)
3. Common Room matched
4. SFDC Aero Account Fit is non-null
5. SFDC has at least one buying-title contact mapped

Bonus:
- 5+ sources → +5 to composite
- 3-4 sources → +3
- <3 sources → -3

Final composite capped at 100.

## Tier assignment

| Tier | Score range | Meaning |
|---|---|---|
| **Tier 1 (Hot)** | 75+ | Sprint now |
| **Tier 2 (Warm)** | 60-74 | Next sprint |
| **Tier 3 (Watch)** | 45-59 | Monitor, may improve |
| **Tier 4 (Disqualify)** | <45 | Remove from cohort |

## Flags

Set boolean flags per account for filtering:

| Flag | Trigger condition |
|---|---|
| `aero_missed` | Octave score ≥7 AND (Aero_Account_Fit_Score__c < 40 OR null) |
| `aero_false_negative` | Amplitude verdict = "AERO_FALSE_NEGATIVE" |
| `cr_adds_committee_depth` | cr_contacts_count > SFDC contact count by 5+ |
| `octave_disqualifier` | Octave disqualifier_triggered=true OR octave_score ≤ 2 |

## "Why" generation per account

For the user-facing output, generate three short phrases:

**Top + signal** = highest-contributing component × weight. Format:
- `"Octave 10/10 — ideal prospect"`
- `"Amplitude POWER — 18 active users, 8 senders"`
- `"Aero False-Negative — Amplitude shows real engagement, Aero PES floored"`
- `"CR depth — 33 contacts vs 25 SFDC"`
- `"VP Sales mapped: Brett McNay"`

**Secondary + signal** = second-highest contributor

**Top − signal** = lowest contributor that dragged score down:
- `"Amplitude NO_DATA — no product usage visibility"`
- `"No buying-title contact mapped"`
- `"Cold stage, 90+ days quiet"`
- `"Octave disqualifier: Non-NA HQ"`

## When to recalibrate weights

The weights above are illustrative defaults. Recalibrate against your own won/lost cohort when:
- Aero ships a meaningful model update (reduce Octave weight; increase Aero weight)
- Common Room data quality changes materially (e.g., new lead-score model deployed)
- The cohort definition changes (e.g., moving from PQA to a new gate)
- A new source comes online

Document weight changes inline in the rubric file with the date and rationale.
