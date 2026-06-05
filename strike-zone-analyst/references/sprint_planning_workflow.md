# Sprint Planning Workflow

The staged enrichment process for Mode 2: taking a PQA (or MQA/OQA) cohort and turning it into a ranked sprint backlog with verified contacts.

## When to use this workflow

Trigger phrases: "PQA sprint planning", "score our PQAs", "build a PQA backlog", "rank our PQA cohort", "give me the sprint list", "which accounts should we work this sprint".

If the user is asking a single-gate diagnostic question ("why is our show rate dropping"), that's Mode 1, not this. If they're asking about a single account, use `customer-strategy-brief` instead. This workflow is specifically for ranking a cohort.

## Workflow at a glance

```
Step 1 — Define cohort                (1 SOQL query, ~5 sec)
Step 2 — Parallel enrichment fan-out  (3 sources, ~15-20 min wall)
   ├─ Octave qualify (1 call/account)
   ├─ Amplitude PES (cohort-level batch)
   └─ Common Room org lookup (1 call/account)
Step 3 — Composite scoring            (Python, ~30 sec)
Step 4 — FullEnrich top tier          (credit-gated, ~5-10 min)
Step 5 — Build xlsx                   (5 tabs, ~1 min)
Step 6 — Hand off                     (present file + summary)
```

## Step 1 — Define the cohort

Always confirm with the user before running. Default cohort definition:

- All accounts with `Sales_PQA_Date_Account__c >= <start>` AND `<= today`
- Channel filter optional — sometimes the cohort is intentionally cross-channel
- Typical windows: trailing 90 days, year-to-date, last full quarter

Query (chunked if results exceed 25K tokens):

```sql
SELECT Id, Name, Website, NumberOfEmployees, Industry,
       Aero_Account_Fit_Score__c, Aero_Upsell_Fit_Score__c, Aero_Upsell_Fit_Tier__c,
       Account_GTM_Stage__c, Channel_Source__c, OwnerId, Owner.Name,
       Sales_PQA_Date_Account__c, MQA_Date_2024__c, OQA_Date__c,
       All_Purchased_Seats__c, Aero_Product_Engagement_Score__c
FROM Account
WHERE Sales_PQA_Date_Account__c >= <COHORT_START>
  AND Sales_PQA_Date_Account__c <= <COHORT_END>
ORDER BY Sales_PQA_Date_Account__c DESC
```

Save the cohort master to a JSON file. The enrichment subagents will read it.

## Step 2 — Parallel enrichment

Spawn three subagents in parallel. Each handles all accounts in the cohort.

### Subagent A — Octave qualify

Per account: call `qualify_company` with `companyDomain` (NOT "domain" — the schema requires that exact field name). Extract:
- `data.score` (0-10 ICP fit)
- `data.rationale` (first sentence only)
- `data.playbook.name` and `data.playbook.score`
- `data.disqualifierSummary.triggered` and `firstQuestion`

**Critical guardrail:** Octave returns ~10K tokens per call (product description is bulky). Subagent must process silently — DON'T echo or summarize each response in chat. Cap batch size at ~50 accounts per subagent or it'll hit context limits. For 260+ accounts, spawn 5 subagents in parallel, each handling ~50.

Save output as JSON array per subagent (e.g., `octave_part_A.json` through `octave_part_E.json`), then merge.

### Subagent B — Amplitude PES

Use the `product-engagement-story` skill's 11-event framework. Either:
- One cohort-level groupBy query per event (11 queries total, ~30 sec — efficient)
- Or one per-account query (261 × ~3 sec = 13 min — slower but clearer)

The cohort-level pattern is much faster and produces the same per-account verdict. Use it when the cohort is large.

Output per account: verdict (POWER/ESTABLISHED/AERO_FALSE_NEGATIVE/EMERGING/DORMANT/UNTOUCHED/GHOST_ACTIVE/NO_DATA), trend, active_users_latest_week.

### Subagent C — Common Room

Per account: `commonroom_list_objects` filtered on `companyWebsite = <domain>` for Organization. Extract:
- `cr_org_id`
- `cr_contacts_count`
- `cr_lead_scores` (highest percentile)
- `cr_sub_industry`, `cr_employees`, `cr_revenue_range_max`
- `cr_recent_job_openings_count`, `cr_recent_news_count`
- `cr_has_sfdc_profile`, `cr_has_opp_profile`

Common Room typically responds in ~1 sec/call. Whole cohort in ~5 min.

If pulling rich fields per account is too slow, use a bulk OR filter on companyWebsite — trades depth for speed.

## Step 3 — Composite scoring

After all three enrichment files are ready, merge with the cohort master and compute composite scores per `references/multi_source_scoring.md`.

Done in a single subagent. Reads the 5 input files (cohort_master + 3 enrichment + v1 xlsx for buying-title backfill), produces:
- `v2_scored_cohort.json` — all accounts ranked, with sub-scores, tier, why-signals, flags
- `v2_top50_for_fullenrich.json` — top 50 by composite, for the FullEnrich step

## Step 4 — FullEnrich top tier (credit-gated)

**Always check credits first.** `mcp__63157928-2125-4a53-b8f6-c0881c12ac2e__get_credits` → balance. ~8.7 credits per contact for work email + mobile phone.

Cost math: 50 accounts × 5 contacts/account = 250 contacts × 8.7 = ~2,200 credits. Adjust scope to fit credit budget:
- Top 50 enriched (250 contacts, ~2,200 credits)
- Top 25 enriched (125 contacts, ~1,100 credits)
- Top 10 enriched (50 contacts, ~440 credits)

**Strategy per account:**
- If account has 5+ senior SFDC contacts → enrich existing
- If account has <5 senior SFDC contacts → use `search_people` to discover net-new VPs/Directors at the company, then enrich

Output per account: buying_committee array with name, title, email + verification status, phone + type, source, enrichment status.

## Step 5 — Build the xlsx

Use the `xlsx` skill. Five tabs:

1. **Sprint Ranking** — all cohort accounts × ~32 columns. Tier-colored rows. Auto-filter. Frozen header. Sorted by composite DESC.
2. **Top Buying Committee** — FullEnriched contacts (1 row per contact, grouped by account). The sprint execution tab — reps work this top-down.
3. **Scoring Rubric** — methodology, weights, tier thresholds, flag definitions.
4. **Cohort Summary** — COUNTIF rollups: by tier, by channel, by owner, by Octave score, by Amplitude verdict, by flag.
5. **Aero Scoring Gaps** — Section A: 34 Aero False-Negatives. Section B: 9 Aero-Missed ICPs (or whatever the run produced). Both sorted by composite DESC.

Recalc formulas before saving: `python scripts/recalc.py <output>.xlsx`. Confirm zero errors.

## Step 6 — Hand off

Save the .xlsx to the user's workspace folder. `present_files` makes it openable.

Summary message should include:
- Total accounts scored, tier distribution
- Top 5 accounts by composite
- Count of `aero_false_negative` and `aero_missed` flags
- FullEnrich coverage (# phones, # verified emails, credits used vs balance)
- Sanity check results (a known good account in Tier 1, a known bad account in Tier 4)

## Time + cost budgets

| Step | Wall time | Token cost | $ cost |
|---|---|---|---|
| 1. Cohort definition | ~5 sec | minimal | 0 |
| 2. Parallel enrichment (3 subagents) | ~15-20 min | ~1M tokens total | 0 |
| 3. Composite scoring | ~30 sec | ~100K | 0 |
| 4. FullEnrich top 50 | ~5-10 min | ~200K | ~$22 (2,200 credits @ ~$0.01/credit) |
| 5. xlsx build | ~1 min | ~100K | 0 |
| **Total** | **~25-35 min** | **~1.4M tokens** | **~$22** |

Adjust FullEnrich scope to control the only $ cost. Everything else is sunk.

## Failure modes to handle gracefully

- **Octave subagent context overflow** — split into smaller batches or rerun the failed range
- **Amplitude returns NO_DATA for many accounts** — that's a real finding, not a failure; surface it as a data-coverage caveat
- **Common Room non-match** — 10-15% of accounts won't match; OK to leave unmatched and zero those components
- **FullEnrich credits exhausted mid-run** — stop, report what was enriched, ask user before refilling

## When NOT to run this workflow

- Single-account question → use `customer-strategy-brief`
- Funnel-gate diagnostic without a cohort to rank → Mode 1, not this
- Closed-lost analysis → `closed-lost-runbook`
- Renewal book → `csm-book-of-business`
