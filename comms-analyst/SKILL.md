---
name: comms-analyst
description: Your write-side agent. Takes outputs of the read + augment analysts and ships them — writes back to Salesforce, posts to Slack, drafts outreach, sends DMs, updates CRM fields, schedules follow-ups. Connect Salesforce (SFDC writes), Slack (messaging), and/or Mixmax (outreach sending) — each connector unlocks a slice; all three unlock everything. Use when a workflow's output needs to GO somewhere — into CRM, into a channel, into a rep's inbox. Trigger on "write these enriched contacts back to SFDC", "post the daily drop to {channel}", "draft a follow-up to {person} referencing {meeting}", "update PLAN fields on {account}", "send a save play recommendation to {CSM} in Slack", "notify the team about {event}", "draft an Octave sequence for {prospect}", "DM Heath the top 10 customer interview candidates", or any output/write/send/notify operation. Also fire inside any workflow needing to materialize results outside the analysis loop.
---

# Comms Analyst — your write-side agent

**Required connector:** Salesforce OR Slack OR Mixmax. Each unlocks a slice of capability; all three together unlock everything.

**Optional connector:** Octave (for outreach drafting using your company's playbook + writing style).

## What this analyst answers

In plain English, the Comms Analyst answers the WRITE side of questions:

- "Write back these enriched committee members to SFDC" → SFDC Contact create/update with the FullEnrich data
- "Post the Daily Drop to `#gtm-pipeline`" → Formatted Slack message + audit row
- "Draft a follow-up email to Sarah Chen referencing yesterday's meeting" → Personalized draft pulling meeting context from Conversation Analyst
- "Update the PLAN fields on Acme Corp based on the transcript I just shared" → SFDC Account update of `Problems_Account__c`, `Leverage_Alignment__c`, etc. — with the rep's draft for confirmation before write
- "Send a save play recommendation to HM in Slack" → DM to HM with the suggested play + brief link
- "Notify the team that Karan just closed Millennium" → Channel post with celebration formatting
- "Draft an Octave sequence for {prospect}" → Multi-touch sequence using Octave's content engine + the company's voice
- "DM Heath the top 10 customer interview candidates" → Format the W6 output + post as draft for review

## What it owns internally

The Comms Analyst is the product layer over these atomic skills:

- **O2 — Slack Post / Drop / Leaderboard** — channel posts, DMs, draft creation, EOD leaderboard format
- **O4 — SFDC Contact Write-Back** (lock-in #13) — Contact create/update with FullEnrich beats stale CRM
- **SFDC Account field updates** — `Account_Brief_URL__c`, `Product_Engagement_Verdict__c`, the 4 PLAN fields, Account_Notes update with timestamp
- The `octave-outreach-drafter` skill — email content via Octave when connected
- The `meeting-followup-generator` skill — follow-up drafts from meeting context
- Mixmax sequence creation when connected (handoff to Mixmax for actual send)

## The quality gates this analyst guarantees

**Full auditability.** Every write operation is logged to `Revenue Reviews/comms_audit/{YYYY-MM}.tsv` with:
- Timestamp (UTC)
- Operation type (SFDC_contact_create / SFDC_account_update / Slack_post / Slack_draft / Octave_draft / etc.)
- Target (record ID + field, or channel ID + message URL)
- Before / after values for field updates
- Cost (Slack count toward Slack API limits; Octave token cost if used; etc.)
- Caller (workflow ID + invocation ID for traceability)

No silent writes — ever.

**Draft-first by default for outbound copy.** Email drafts and Slack messages are posted as DRAFTS by default (using `slack_send_message_draft` instead of `slack_send_message`) so the rep / leader can review before sending. Explicit opt-in required for autosend.

**Idempotency on SFDC writes.** Before creating an SFDC Contact, the analyst queries to confirm no duplicate exists. If a duplicate exists, the analyst UPDATES instead of creating — preventing duplicate Contact pollution.

**Honest connector failure.** If a workflow requests "post to Slack" but Slack isn't connected, the analyst returns "Slack not connected — operation aborted" rather than silently failing or fabricating success.

## Output format example

For "Write these 12 enriched committee members to SFDC":

```
✅ SFDC Write-Back Complete · 12 contacts processed

┌────────────────┬─────────────────┬──────────┬─────────────────────────────────┐
│ Name           │ Operation       │ SF ID    │ Notes                           │
├────────────────┼─────────────────┼──────────┼─────────────────────────────────┤
│ Sarah Chen     │ CREATED         │ 003abc.. │ Verified email + phone written  │
│ Mike Rodriguez │ UPDATED         │ 003def.. │ Existed; added Mobile + LinkedIn │
│ Jim Coulon     │ UPDATED         │ 003ghi.. │ Existed; updated Title          │
│ Petra Lovric   │ EXISTING (skip) │ 003jkl.. │ All fields already populated    │
│ Linda Park     │ SKIPPED         │ —        │ Email = not_found, skipped per #13│
│ ... 7 more ... │                 │          │                                 │
└────────────────┴─────────────────┴──────────┴─────────────────────────────────┘

Summary:
  Created:   4  · new SFDC Contact records
  Updated:   6  · existing records with new fields
  Existing:  1  · already complete, no change
  Skipped:   1  · failed enrichment, not written

Audit trail: Revenue Reviews/comms_audit/2026-05.tsv (12 rows appended)
SF record IDs: [003abc..., 003def..., 003ghi..., ...12 total]
```

For "Post the Daily Drop to #gtm-pipeline":

```
✅ Slack Post Complete

Channel: #gtm-pipeline (C0ADW3Z8M7C)
Message: 🔥 THE DAILY DROP — Friday, May 29...
Mode: sent (not draft — autosend enabled for daily-drop workflow per its task config)
Slack URL: https://mixmax.slack.com/archives/C0ADW3Z8M7C/p1780123456789
Message TS: 1780123456.789

Audit: Revenue Reviews/comms_audit/2026-05.tsv (1 row appended)
Reaction counter scheduled: EOD leaderboard at 17:00 CT (counts 🎯 🔥 ✅ 🚀 reactions)
```

## Used by (workflows that compose this analyst)

- **W1 Per-Account Brief Pipeline** — SFDC Contact writeback + SFDC Account field update with brief URL
- **W3 Daily Drop** — Slack post + EOD leaderboard
- **W4 Customer Strategy Suite** — SFDC writeback + optional Slack notification
- **W6 Customer Interview Prioritizer** — Slack draft to Heath
- **Daily Drop EOD leaderboard** — counts emoji reactions + posts results
- Used by any workflow that has output to ship

## When NOT to use this analyst

- For pure READS (use SFDC / Amplitude / Conversation Analyst)
- For scoring / qualification (use ICP Analyst)
- For data enrichment / discovery (use Enrichment Analyst)
- The Comms Analyst is ONLY for write / send / notify operations

## Inheritance from LOCKED_DESIGN.md

This analyst inherits lock-in #2 (single-writer manifest rule — never writes to `reports.json`), lock-in #12 (clickable gap tags + #brief-requests channel), lock-in #13 (SFDC Contact write-back contract), lock-in #25 (Daily Drop format + EOD leaderboard mechanics), and the Slack channel registry (`C0ADW3Z8M7C` Daily Drop, `C0B6MD314MR` brief requests, `C085CP9QXB7` GTM Central). Read `Account Brief Pipeline/LOCKED_DESIGN.md` before any invocation.

## Make.com / API packaging

**Input schema:**
```json
{
  "operation_type": "sfdc_contact_writeback | sfdc_account_update | slack_post | slack_draft | slack_dm | octave_draft | mixmax_sequence",
  "payload": {... operation-specific ...},
  "draft_first": true,
  "autosend_override": false,
  "audit_log": true
}
```

**Output schema:**
```json
{
  "status": "completed | partial | failed",
  "operations_performed": [
    {
      "type": "string",
      "target_id": "string (SF record ID or Slack message TS)",
      "target_url": "string (link to the SF record or Slack message)",
      "before": {...},
      "after": {...},
      "cost": "string (credits, tokens, API calls)"
    }
  ],
  "audit_rows_written": N,
  "audit_file": "Revenue Reviews/comms_audit/2026-05.tsv"
}
```

**Failure modes:**
- No required connector: "Connect {connector} to enable {operation_type}."
- Duplicate detection on SFDC: skips the duplicate + logs in audit, doesn't fail the batch.
- Slack rate limit hit: pauses + retries with backoff, surfaces in output.
- Octave draft fails: returns the un-Octaved draft + flag "Octave unavailable — review draft manually."

## Shippable as

**Standalone connector-gated SKU:** customer connects Salesforce alone → SFDC writebacks. Connects Slack alone → Slack messaging. Each unlocks a slice.

**Make.com sub-agent module:** discrete node, input is operation type + payload, output is structured confirmation + audit trail. Chains naturally as the FINAL step in any workflow — every workflow that needs to ship outputs goes through Comms Analyst.

**Standalone API endpoint:** could be packaged as a write-API for AI agents that don't want to implement Salesforce / Slack / Mixmax integrations themselves — they call the Comms Analyst endpoint with intent, the analyst handles the connector + auditability + idempotency.

This is the "ship the work" analyst. Without it, no workflow output ever leaves the analysis loop.
