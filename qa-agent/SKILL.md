---
name: qa-agent
description: The 7th analyst — the meta-analyst. Monitors every other analyst's audit log + feedback queue, surfaces scoring blind spots, CRM hygiene gaps, enrichment gaps, workflow drift, and Daily Drop engagement decline. Generates weekly QA report (HTML) + Slack digest (Sundays, DMs Heath) + improvement recommendations. First stepping stone of AI-native GTM — every override, every missing CRM field, every enrichment miss becomes a training signal. Use to ask "what's broken in the system?", "show me CRM hygiene issues", "is the Daily Drop working?", "are scoring models drifting?", "what should we coach on this week?". Trigger on "run QA", "weekly QA report", "system health check", "where are our scoring blind spots?", "show me coaching priorities from data", "audit our workflow performance", "Daily Drop engagement check", "where's the system getting things wrong?", or any system-level health / improvement / feedback-loop question. Also fires automatically Sundays 7pm CT.
---

# QA Agent — the meta-analyst

**Required:** Read access to `Revenue Reviews/` (where all the audit TSVs live).

**Optional:** Slack (post weekly digest to Heath's DM + critical alerts to #revops-alerts) · GitHub (verify brief manifest integrity + check published-brief health).

## What this agent does

The QA Agent is unlike the other 6 analysts. It doesn't pull data from a SaaS connector. It reads the audit trails the OTHER analysts leave behind + derives system-level patterns. Then it tells you where to invest improvement effort.

This is the feedback layer. Without it, every analyst run is a one-shot — produce work, ship it, move on, no learning. With it, every override + every gap + every disagreement becomes a signal that compounds into a smarter system next week.

## What this agent answers

In plain English:

- "What's broken in the system this week?" → Weekly QA report with scoring misfires + CRM gaps + workflow drift
- "Where are we BS'ing ourselves on the deal review?" → Cross-rep PLAN-completeness audit + opp-vs-stage mismatches across the entire pipeline
- "Show me CRM hygiene issues" → Per-rep audit: stale PLAN Account_Notes (>180 days), null Decision_Maker__c, opps with null LastActivityDate, accounts with low custom-field coverage
- "Is the Daily Drop working?" → Engagement audit: claim rate (🎯 reactions) / first-touch rate (🔥) / meeting-book rate (✅) by AE + by day-of-week. Streak watch + decline detection.
- "Are our scoring models drifting?" → Aero override hit rate over time (did our False-Negative calls turn out to be right?). ICP composite score drift vs Aero + Octave. Deal-risk classifier accuracy (did flagged AT_RISK deals actually slip?).
- "What should we coach on this week?" → Data-driven coaching priorities: which rep has the lowest PLAN-completeness rate, which AE's deals have the most days-dark concentration, who's not using the Daily Drop, etc.
- "Audit our workflow performance" → Per-workflow success/failure rate + connector availability + failure-mode breakdown
- "Where is the system getting things wrong?" → Cross-analyst disagreement detection (e.g., SFDC Analyst says HEALTHY but Conversation Analyst says Champion-Drop-Off → reconcile + add to a "calibration queue")

## The audit streams it reads

```
Revenue Reviews/
├── aero_feedback_queue/                  ← Ghost-Active + Aero False-Negative overrides
│   ├── 2026-05.tsv
│   └── sfdc_gaps.tsv                     ← SFDC custom fields not yet provisioned
├── sfdc_analyst_audit/2026-05.tsv        ← every account analyzed + verdict + rep follow-through
├── amplitude_analyst_audit/2026-05.tsv   ← override fires + downstream verification
├── conversation_analyst_audit/2026-05.tsv ← Champion-Drop-Off calls + verification
├── icp_override_queue/2026-05.tsv        ← ICP composite vs Aero/Octave disagreements
├── enrichment_audit/2026-05.tsv          ← provider not_found rate + cost per field
├── comms_audit/2026-05.tsv               ← every SFDC write + Slack post + verification
├── daily_drop_audit/2026-05.tsv          ← Daily Drop emoji-reaction engagement
└── workflow_run_log/2026-05.tsv          ← per-workflow success/failure + duration
```

Plus cross-cutting:

- `mixmaxhq/GTM-account-briefs/reports.json` — manifest shape + entry-count drift
- GitHub Pages CDN deploy state — verifies briefs render after publish
- Slack message history — reaction counts on Daily Drop posts (counts 🎯 🔥 ✅ 🚀)

## The 6 sections of the weekly QA report

### 🎯 1. Scoring Accuracy

- Aero override hit rate ("We called Aero False-Negative on 23 accounts last month; 19 became active deals = 82% precision")
- ICP composite score drift vs Aero / Octave over the trailing 30 days
- Deal-risk classifier accuracy (did flagged AT_RISK/SLIP_RISK opps actually slip? % accuracy)
- Outliers: accounts where our analysts disagreed with each other (SFDC says HEALTHY, Conversation says Champion-Drop) → calibration queue

### 🧠 2. CRM Hygiene

- Stale PLAN per rep: accounts where `Account_Notes_Last_Updated > 180 days`
- Null Decision_Maker__c per rep
- Opps with PLAN incomplete for current stage (cross-pipeline)
- SFDC custom field population rate per rep (the field-by-field % filled)
- Trend: getting better or worse vs last week

### 💧 3. Enrichment Gaps

- Per-provider not_found rate trends (FullEnrich, Common Room, Octave)
- Cost per verified field by provider
- Contacts that have been not_found in 3+ runs (manual sourcing needed)
- Domain types where Common Room fails most often (industry / segment / region patterns)

### 📡 4. Workflow Performance

- Per-workflow success rate trend (W1, W2, W3, W6, etc.)
- Connector availability per workflow run (when did Amplitude MCP drop out, etc.)
- Failure mode breakdown (connector missing / data not found / classifier disagreement / SFDC validation failure)
- Top workflows by usage + top workflows by failure rate

### 🔥 5. Daily Drop Engagement

- Claim rate per AE per day (🎯 reactions / 10 leads)
- First-touch rate per AE (🔥 reactions / 🎯 reactions)
- Meeting-book rate per AE (✅ reactions / 🔥 reactions)
- Streak watch (top reps by consecutive-day 100% action rate)
- Week-over-week trend: is engagement rising or declining?

### 🚨 6. System Health

- Broken brief links count (must be zero — if not, surface immediately)
- Manifest entry drift detection (reports.json should have ~283 entries)
- Lock-in violations: anyone non-reconciler writing to `reports.json` (should be zero)
- GitHub Pages CDN deploy lag

## Output: the actual improvement recommendations

These are the concrete asks the QA Agent generates. They're surgical + actionable:

- "5 accounts in HM's book have Account_Notes > 180 days old: Blend Labs, Whip Around, Galvanize, PGA, Halborn. Schedule PLAN refresh in next 1:1."
- "Karan's PLAN-completeness rate is 14% (1 of 7 opps). Highest-priority coaching session this week."
- "Aero False-Negative override fired 8 times this month, 7 became active deals. Email Aero with the list — they're under-scoring Series-D B2B SaaS at 100-500 employees."
- "FullEnrich not_found rate jumped to 31% last week (baseline 12%). Worth investigating their data freshness."
- "Daily Drop claim rate dropped to 47% this week from 71% baseline. Karan was OOO Tuesday (claim rate 0). Adjust for OOO or pre-roster the Drop next time he's out."
- "Isabelle is the #1 PLAN-completer (87%) but #2 by deal count. Pair her with Karan for a peer-coaching session."

## The AI-native GTM flywheel this enables

```
            ┌──────────────────┐
            │  6 Analysts run  │
            │  → Output work   │ ────┐
            └──────────────────┘     │
                                     │
       ↑ Each loop closes             ▼
       ↑ system gets smarter         ┌──────────────────────┐
       │                             │   QA Agent monitors  │
       │                             │   audit logs         │
       │                             └──────────────────────┘
       │                                     │
       │                                     ▼
       │                             ┌──────────────────────┐
       │                             │ Surfaces:            │
       │                             │ - scoring misfires   │
       │                             │ - CRM hygiene gaps   │
       │                             │ - enrichment gaps    │
       │                             │ - workflow drift     │
       │                             └──────────────────────┘
       │                                     │
       │                                     ▼
       │                             ┌──────────────────────┐
       │                             │ Specific recs feed:  │
       │                             │ - lock-in updates    │
       │                             │ - scoring models     │
       │                             │ - workflow specs     │
       │                             │ - rep coaching       │
       │                             └──────────────────────┘
       │                                     │
       └─────────────────────────────────────┘
```

Every recommendation that lands means next week's analyst outputs are better. The system compounds. That's the AI-native GTM thesis — not "use AI to do stuff faster," but "use AI to build a system that learns from itself."

## Output format example (weekly digest)

For Sunday-evening DM to Heath:

```
📊 Weekly QA Digest — Week of May 25

🎯 SCORING ACCURACY
   Aero override precision: 82% (19 of 23 calls correct — strongest data point yet)
   ICP composite drift: +4 pts vs Aero in trailing 30d (we're scoring tighter; expect Aero recalibration)
   Deal-risk classifier: 8 of 11 flagged SLIP_RISK deals actually slipped (73%)

🧠 CRM HYGIENE — top 3 issues
   1. 17 of 24 cross-rep deals have PLAN incomplete for current stage (71%). Same number as last week — NO improvement.
   2. Karan: 14% PLAN-completeness (1 of 7 opps). Lowest on the team. Top coaching priority.
   3. 12 customer accounts have Account_Notes > 180 days. Suggest PLAN refresh in next CSM 1:1s.

💧 ENRICHMENT
   FullEnrich not_found jumped 31% (baseline 12%). Worth investigating data freshness.
   Octave hit rate on LinkedIn URLs holding strong at 91%.

🔥 DAILY DROP ENGAGEMENT
   Average claim rate: 67% (above 60% target).
   Top picker: Isabelle, 4 days at 100% (longest streak this quarter).
   Concern: Felipe's claim rate is 23%. Onboarding issue or signal something more?

🚨 SYSTEM HEALTH
   Zero broken brief links. Zero manifest violations. All systems green.

🎯 TOP RECOMMENDATIONS THIS WEEK
   1. Karan: 1:1 focused on PLAN completion — biggest team-level coaching priority
   2. Email Aero with the Series-D B2B SaaS over-coverage data — they should recalibrate that segment
   3. Investigate FullEnrich data freshness with their team
   4. Felipe: schedule check-in on Daily Drop engagement + onboarding state

Full report: [link to HTML]
```

## Used by (what consumes this agent)

- **Heath (weekly direct usage)** — Sunday digest before Monday review
- **RevOps team** — for the SFDC gap sheet + custom-field provisioning queue
- **The Aero team (external feedback loop)** — gets the curated False-Negative/False-Positive list monthly
- **The system itself** — recommendations land back as lock-in amendments + scoring rubric updates

## When NOT to use this agent

- For real-time decisions (the QA Agent runs weekly — for real-time use the underlying analysts)
- For pulling SFDC / Amplitude / Mixmax data directly (use the read analysts)
- For one-off questions about a single account (use SFDC + Amplitude + Conversation analysts directly)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- No direct SFDC reads — consumes the audit TSVs that other analysts write.
- Reads salesforce_analyst_audit, comms_audit, etc. for drift detection.

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

The QA Agent reads the audit-trail outputs of every other analyst. It doesn't have its own lock-in dependencies beyond the file-system layout. Lock-in #2 (single-writer manifest rule), #8 (Aero feedback queue), and the auditability requirements of every other lock-in are what makes this agent possible.

## Make.com / API packaging

**Input schema:**
```json
{
  "mode": "weekly_full | spot_check | scoring_audit | engagement_audit",
  "window_days": 7,
  "include_recommendations": true,
  "post_digest_to_slack": true,
  "slack_target": "user:U07CAK8C0CW"
}
```

**Output schema:**
```json
{
  "report_url": "https://psychic-adventure-p3jj6y9.pages.github.io/qa-reports/2026-05-29.html",
  "scoring_accuracy": {...},
  "crm_hygiene": {...},
  "enrichment_gaps": {...},
  "workflow_performance": {...},
  "daily_drop_engagement": {...},
  "system_health": {...},
  "top_recommendations": [{...}, ...],
  "slack_digest_url": "https://mixmax.slack.com/..."
}
```

**Failure modes:**
- Audit TSVs missing: surfaces which streams couldn't be read + degrades gracefully
- File-system access denied: returns "Connect file system to enable QA monitoring"

## Shippable as

**Standalone QA SaaS:** customer adds this agent to their Make.com scenario as the final-of-the-week node. Once-a-week QA digest, posted to their preferred channel. Tells them how to improve everything else.

**Bundled with the analyst suite:** included free with any 2+ analyst purchase. It's the layer that makes the analysts get smarter over time.

This is the first stepping stone for AI-native GTM. Without this loop, the analysts produce one-shot outputs. With this loop, the system compounds.

## Scheduled run

`qa-agent-weekly` — runs every Sunday at 7:00 PM CT — generates the full weekly QA + posts the digest to Heath's DM by 7:30 PM. Ready for Monday review.

---

## Context Integrity Audit (Built GTM / Re:Built)

A second meta-check beyond the scoring and CRM audits above: is the brand and show context referenced from one source, or has it forked? This is the eval gate for the AI-native context loop. "Looked good once" is not an eval. Run this before anything that uses brand or show context ships, and on the weekly QA run.

**Canonical source of truth:** `get-built-gtm/context/`. Read `get-built-gtm/context/README.md` first.

**Run it:**

```
bash get-built-gtm/context/sync/audit-context.sh [root-to-scan]
```

**What it checks, and why each matters:**

1. **Dead session-scoped context paths.** Agents must read a stable repo path, never a `/sessions/.../memory/` scratch path. That bug left the dispatch agent with no voice file.
2. **References to superseded sources.** No skill, page, or prompt should pull from "GTM Tactical", the GTM-Show-Series docx, or the stale GTM Building Blocks copy.
3. **Forked brand copies.** Any file carrying the brand voice rules must be GENERATED from canon via `build-context.sh`, not hand-maintained. Hand copies drift.
4. **Derived vs canon sync.** If canon changed but the derived artifacts (brand SKILL, system prompt, dispatch voice) were not regenerated, the deployed agents are stale.

**Output:** PASS/FAIL per check, exit 1 on drift. Wire it into the build/test step so nothing referencing brand or show ships without it.

**When to fire:** before publishing any Built GTM content or show surface, after any context edit, and on the weekly QA run alongside the sections above.
