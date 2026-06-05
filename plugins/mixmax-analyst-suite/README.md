# Mixmax Analyst Suite v1.2.1

21 skills covering every stage of the customer lifecycle + the AI-native self-learning meta layer + compute-aware refresh orchestration.

## v1.2.1 — what's new
- **PLAN Selling everywhere.** `salesforce-analyst` no longer uses "MEDDIC-equivalent" phrasing — it reads as a PLAN-based strategic read (lock-in #26: never MEDDIC).
- **`gtm-design-analyst`** content/messaging hand-off now points only to `heath-voice-humanizer` (the standalone `humanizer` skill was retired/merged).
- Built reproducibly from this repo via `scripts/build_plugin.py` (manifest + skill list now live in-repo).

## v1.2 — what's new
- **refresh-orchestrator** (NEW) — compute-aware gating layer. Decides before any expensive workflow runs whether to SKIP / PARTIAL / RECYCLE / FULL regenerate. Saves ~50% of GTM compute spend.
- Every artifact-generating workflow in the Vercel runtime now consults the orchestrator FIRST.

## The complete suite
```
READ      prospecting · pipeline-creation · strike-zone · deal-health
          onboarding · book-of-business · renewal-health
          salesforce · amplitude · conversation
AUGMENT   icp · enrichment · pattern · coaching
WRITE     comms
DESIGN    gtm-design
META      qa-agent · evolution-agent
WORKFLOW  daily-sales-assistant
REFERENCE sfdc-field-library (auto-loads on every SFDC question)
GATING    refresh-orchestrator (compute-aware caching)
```

## Source
[heath-gtm/Skill-Builder](https://github.com/heath-gtm/Skill-Builder) — built with `python3 scripts/build_plugin.py mixmax-analyst-suite`
