---
name: icp-analyst
description: Your ICP qualifier. Connect Salesforce + a scoring system (Aero, Octave, or any account scoring vendor) — turns any "is this account real ICP?" question into a stacked verdict: composite score from every signal, breakdown by source, override flags when scoring systems are wrong, channel classification, written rationale. Use when a rep is starting prospecting, a marketer is scoring inbound, RevOps is building a TAM model, or a sales manager is vetting an outbound list. Trigger on "is {account} a real ICP fit?", "score this list against our ICP", "find lookalikes to {winning customer}", "why is Aero wrong about {account}?", "validate this prospect list", "what's our ICP coverage in {segment}?", "is this PQA worth pursuing?", "find accounts that match our top customers", "qualify these leads", or any account / list / segment qualification. Also fire when a leader is debating whether to invest a rep cycle on an account vs pass.
---

# ICP Analyst — your fit qualifier

**Required connectors:** Salesforce + at least one scoring source (Aero, Octave, or any account-scoring vendor).

**Optional connectors:** Common Room (for hiring intent + employee count) · Amplitude (for product-side ICP signal via PQA detection) · FullEnrich (for technographic confirmation).

## What this analyst answers

In plain English, the ICP Analyst answers questions like:

- "Is acme.com a real ICP fit?" → Composite 0-100 score with source breakdown
- "Score this list of 50 prospects against our ICP" → Per-row verdict with rationale, sortable by score
- "Find lookalikes to Datadog and Vortex" — our two highest-ARR customers" → Search for accounts matching their technographic + employee count + industry + funding-stage profile
- "Why is Aero scoring this 30 when the hiring signal is screaming?" → Override detection: surface accounts where Aero's score conflicts with leading-indicator signals (hiring 14 sales reps + uses Outreach = displacement target Aero missed)
- "What's our Q2 ICP coverage in mid-market SaaS?" → Pipeline pull filtered by segment + scored against ICP, surface coverage gaps
- "Validate this prospect list from the SDR team" → Run the full ICP analyzer over a CSV / pasted list, flag duplicates, surface mis-targeted accounts
- "Is this PQA worth Karan's cycles?" → Single-account qualifier with explicit "yes / no / nurture" verdict + reasoning

## What it owns internally

The ICP Analyst is the product layer over these atomic skills:

- **Multi-source ICP scoring** — Aero Account Fit Score + Octave Fit + Common Room enrichment + PLAN-completeness signal
- **A4 — Channel Classifier** (lock-in #11) — Inbound / Product / Outbound
- **Override detection** for Aero False-Negative and Aero False-Positive (lock-in #14 v7 + product-engagement-story skill)
- **Tech-stack-as-displacement-target scoring** (lock-in #26) — accounts using Outreach + Gong + Apollo are 3-tool consolidation candidates
- **Hiring intent scoring** — `CR_Sales_Team_Hiring__c >= 3` is a top-of-funnel ICP signal

## The quality gates this analyst guarantees

**No single-source ICP claims.** When the analyst outputs an ICP score, it MUST show the breakdown by source — Aero contribution, Octave contribution, Common Room contribution, signal contribution. If a source is unavailable, the analyst declares it ("Octave not connected — score derived from Aero + Common Room + signals only").

**Override visibility.** When the analyst's composite verdict disagrees with Aero or Octave, it explicitly says so and logs the disagreement to `Revenue Reviews/icp_override_queue/{YYYY-MM}.tsv` for the scoring-vendor team to review. This is how we feed back into the Aero feedback loop.

**Channel-tagged outputs.** Every ICP verdict comes with a channel classification — is this account being qualified for Inbound (came to us), Product (self-served signup), or Outbound (we go to them)? The play type and outreach strategy differs by channel.

## Composite ICP score breakdown

```
Composite ICP Score 0-100 (the headline number)
  = 35% × Account Fit (employees + industry + funding + region)
  + 25% × Product-side signal (Amplitude PQA + Aero PES if connected)
  + 20% × Hiring + intent signals (Common Room hiring + recent funding + LinkedIn growth)
  + 15% × Tech-stack-displacement signal (Outreach, Gong, Apollo, SalesLoft, Yesware in their stack)
  + 5% × PLAN-completeness (proxy for rep-confirmed qualification — bonus if a rep has already done the homework)

Penalties (subtract from total):
  - Sub-50 founder-led (-30 unless overridden by other signals)
  - Already a customer at full saturation (-100)
  - Recently churned cooling-off period (-40 if churned within 90 days)
  - In an active deal cycle by another rep (-25 to avoid double-tap)
```

## Output format example

For "Is acme.com a real ICP fit?":

```
🎯 ACME CORP — ICP Score: 87 / 100 · STRONG FIT

Source breakdown:
  Aero Account Fit Score:        78 / 100  (B+ score, marketing approved)
  Octave Fit:                    "GOOD FIT" (qualified)
  Common Room enrichment:        805 employees, 22 sales reps, 14 hiring
  Tech stack displacement:       3 tools — Outreach + Gong + Apollo
  PLAN completeness:             4/4 — rep has done the homework
  Channel classification:        Outbound + Product (hybrid)

Composite signals:
  ✅ Account fit: SaaS + 500+ employees + Series D + N. America
  ✅ Hiring 14 sales reps = top-of-funnel ICP scream
  ✅ Tech stack consolidation play: 3-tool displacement = strong messaging hook
  ✅ Karan has built the full PLAN already — qualification confirmed

Verdict: STRONG FIT — pursue with full outbound investment. Channel suggests
hybrid play: cold sequence into RevOps role (typical entry point) + watch
for any signups from acme.com that would trigger inbound handoff.

Recommended play: COLD OUTBOUND — Aero is correct that this is ICP. The
hiring intent + tech stack consolidation make it Karan's top-3 worth-the-time
outbound target this week.

[Open in CRM ↗]
```

## Used by (workflows that compose this analyst)

- **W1 Per-Account Brief Pipeline** — every brief reports the ICP composite verdict
- **W2 Leader Brief Generator** — Top Leads section uses ICP score as primary sort
- **W3 Daily Drop** — daily hot-lead ranking uses ICP composite
- **W6 Customer Interview Prioritizer** — uses ICP score as a signal for "should this customer be in our reference roster?"
- **W7 Reference Customer Finder** — anchors lookalike search on ICP-validated customers
- **W11 Lost-Deal Reopener** — surfaces deals that scored high ICP but lost, with re-qualification

## When NOT to use this analyst

- For deal-stage analysis (use Salesforce Analyst — deal-risk classifier lives there)
- For "have they used the product" questions (use Amplitude Analyst)
- For pure CRUD of ICP scores in SFDC (use the Salesforce MCP directly)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.* (Aero scoring, CR_* enrichment, tech-stack-as-displacement fields per § 1)
- Account.LeadSource + Opportunity.Channel__c (canonical channel classification, § 5)
- Writes to icp_override_queue audit when composite disagrees with Aero/Octave

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

This analyst inherits lock-ins #11 (channel classifier), #14 v7 (play type taxonomy + Aero override contract), #18 (new user signal), #26 (tech stack + hiring fields), and the Aero False-Negative override logic from the `product-engagement-story` skill. Read `Account Brief Pipeline/LOCKED_DESIGN.md` before any invocation.

## Make.com / API packaging

**Input schema:**
```json
{
  "mode": "single | batch",
  "account_id": "string (when mode=single)",
  "account_list": [{"id": "string", "domain": "string"}] (when mode=batch),
  "include_override_log": true,
  "channel_hint": "Inbound | Product | Outbound | null"
}
```

**Output schema:**
```json
{
  "verdict": "STRONG_FIT | FIT | NEUTRAL | WEAK_FIT | NOT_ICP",
  "composite_score": 0-100,
  "breakdown": {
    "account_fit": 0-100,
    "product_signal": 0-100,
    "hiring_intent": 0-100,
    "tech_stack_displacement": 0-100,
    "plan_completeness": 0-100
  },
  "penalties_applied": [...],
  "channel_classification": "Inbound | Product | Outbound | Hybrid",
  "override_flag": "AERO_FALSE_NEGATIVE | AERO_FALSE_POSITIVE | null",
  "recommended_play": "ACTIVATE | CONVERT | EXPANSION | RECOVERY | RENEWAL_DEFENCE | COLD_OUTBOUND | NURTURE | PASS",
  "rationale": "string"
}
```

**Failure modes:**
- No SFDC connected: "Connect Salesforce to enable ICP scoring."
- No scoring source connected: "Connect at least one scoring source (Aero, Octave, or vendor) to enable ICP scoring."
- Account not found in SFDC: returns null verdict + "Account not in CRM — enrich first via Enrichment Analyst, then re-score."

## Shippable as

**Standalone connector-gated SKU:** customer connects Salesforce + one scoring vendor → ICP Analyst becomes available. The override-detection logic is what's unique — most ICP tools just report their own score; this one tells you when the score is wrong + why.

**Make.com sub-agent module:** ships as a discrete node — input is account_id or account_list, output is structured ICP verdict JSON. Chains naturally with Enrichment Analyst (enrich-then-score pipeline) and Comms Analyst (score-then-notify-rep).
