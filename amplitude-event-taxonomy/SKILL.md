---
name: amplitude-event-taxonomy
description: >-
  Canonical Amplitude event + capability reference for Mixmax — the single source of truth for which events mean what, how they roll up into the 11 product capabilities at gp:domain grain, and how events→groups→adoption-tier produce the product-engagement narrative. Load FIRST on any Amplitude / product-usage question. Defines the Mixmax prod project (130895), gp:domain grain, universal filters, the Tier 1/2/3 event registry with traps, the 11-capability rubric and its raw-event mapping, adoption tiers (Power/Established/Emerging/Dormant/Untouched/Never-adopted), the 12-week trend classifier, Ghost-Active + Aero-False-Negative detectors, the conversion funnel + aha moments, and paid productIds. Trigger on Amplitude, product usage, product engagement, events, event taxonomy, 'what event should I use', 'is this event reliable', gp:domain, 11-capability rubric, adoption tier, ghost active, Aero false negative, WAU, DAU, activation, aha moment, signups, conversion to paid, or any product-analytics question.
---

# Amplitude Event Taxonomy — Single Source of Truth

The Amplitude counterpart to `sfdc-field-library`. Every product-usage analyst,
brief, and report reads event meaning from THIS file. No skill makes its own
event decisions. The goal is apples-to-apples consistency: the same event always
means the same thing, the same capability always rolls up the same raw events,
and the same counts always produce the same narrative.

Skills that inherit from this canonical: `amplitude-analyst`, `product-engagement-story`,
`amplitude-guide`, `account-health-monitor`, and every report that reads product usage
(`weekly/monthly/quarterly-gtm-report` STEP 0 load this file).

---

## 1. Project + grain conventions (fixed)

- **Project:** Mixmax production, `projectId 130895`. Always confirm with `get_context` at session start.
- **Account grain:** `gp:domain` (group-property domain). An "account's" usage = the `gp:domain` segment equal to the account's `Account.Website`-derived domain (lower-cased, protocol/path stripped). Cross-walk to SFDC via `sfdc-field-library` § 10.
- **Default window:** Last 12 Weeks, `interval: 7` (weekly buckets).
- **Default metric:** `uniques`, `countGroup: "User"` (unique users per capability per week).
- **Tooling:** `query_dataset` for custom funnels / event segmentation; `query_chart` / `query_charts` to inspect existing charts.

## 2. Universal filters (apply to EVERY analysis — no exceptions)

| Filter | How | Why |
|---|---|---|
| Exclude Mixmax test users | `userdata_cohort is not vbyym9zo` | Test accounts pollute every metric |
| Exclude auto-connected integrations | on `Connected Third-Party Integration`, exclude `google` + `microsoft` | These are auth methods, not real integrations |

## 3. The method — events → groups → narrative (this is the thing we keep)

This is the durable methodology the whole product-usage layer is built on. Do not deviate from it.

1. **Events** — pull raw instrumented events (§6 registry), each with its required filter (unfiltered events are noise).
2. **Groups** — roll raw events up into the **11 capabilities** (§4) at **gp:domain** grain, weekly uniques over 12 weeks.
3. **Tier** — classify each capability into an **adoption tier** (§5) using `adoption_rate = UA_latest / _active_latest`.
4. **Trend** — classify each capability's **12-week trend** (§5): last-4-week avg vs prior-8-week avg.
5. **Overrides** — run the two detectors (§5): **Ghost-Active** and **Aero False-Negative**.
6. **Narrative + verdict** — synthesize the tiers/trends into a plain-English story a rep trusts (because the counts are visible) and a verdict picklist value. Lead with what's adopted + rising, name the onboarding gap (Untouched/Never), and surface new-user activation.

The narrative's credibility comes from the counts being inspectable — never assert a tier without the underlying weekly uniques.

## 4. The 11-capability rubric (canonical roll-up)

Each capability is a group of one or more raw events at gp:domain grain. Mapping to the instrumented events (§6); where the exact event is not yet codified it is marked **(confirm)** — fill from the live project rather than guessing.

| # | Capability | Raw event(s) + required filter |
|---|---|---|
| 1 | **Email sends** (baseline activity) | `Sent email on server` (always filtered; plain sends are noise) |
| 2 | **Sequences** | `SequenceServer_ActivateRecipients_Activated` + `Sequences_Sequence_Created` (creation ≠ activation) |
| 3 | **Templates** | `Template` with `action = "create"`, and/or `Sent email on server` with `withTemplate = true` |
| 4 | **AI follow-ups** | `Sent email on server` with `relatedMixmaxInsights` ≠ `[]` (Todo / Smart Follow-up) |
| 5 | **AI Compose** | AI-drafted outbound **(confirm exact event/property)** |
| 6 | **Calendar enhancements** | `Sent email on server` where `calendarEnhancementTypes` contains `calendarlink`/`availability`/`event`/`groupscheduling`. **Trap:** `default_calendarlink_in_signature` alone is passive — NOT a real enhancement. Also `Calendar_Meeting_Confirmed` (outcome) and `meeting templates` with `action = updated` (setup done) |
| 7 | **Meeting Copilot — recording** | `MeetingCopilot_Summary_Attempt` |
| 8 | **Meeting Copilot — transcripts** | `MeetingCopilot_Summary_Accessed` / `MeetingCopilot_Summary_SharedEmail_Sent` |
| 9 | **Smart Send AI** (send-time optimization) | **(confirm exact event/property)** |
| 10 | **Sequence-server activations** | `SequenceServer_ActivateRecipients_Activated` (automated rep activation) |
| 11 | **Baseline `_active`** | any product engagement at all — the denominator for adoption_rate and the Ghost-Active comparator |

> Capabilities 5 and 9 are named in the rubric but their exact instrumented events are not in the registry yet (the original `RUBRIC.md` / `AMPLITUDE_QUERY.md` companion files were never committed). Confirm against the live project and update this table — this canonical is where that mapping should live.

## 5. Tiers, trend, overrides, verdict

**Per-capability adoption tier** (from `adoption_rate = UA_latest / _active_latest`):
`Power` · `Established` · `Emerging` · `Dormant` · `Untouched` · `Never-adopted`.
> Exact numeric cutoffs lived in the un-committed `RUBRIC.md`. **Set + record the cutoffs here** so every skill tiers identically; until then, tiers are qualitative (Power = heavy/consistent, Established = regular, Emerging = recent/growing, Dormant = was-active-now-decaying, Untouched = zero this window but adopted before, Never-adopted = never seen).

**12-week trend:** `Rising` / `Flat` / `Declining` / `Collapsed` (and `Zero` when all weeks are 0). Classifier: compare last-4-week average to prior-8-week average.

**Override detectors (locked — inherited by amplitude-analyst & product-engagement-story):**
- **Ghost-Active** — `_active` baseline is healthy but every other capability is ~zero. Seats log in; no value created. → play = `activation_rescue`; force the ghost-active banner.
- **Aero False-Negative** — `Aero_Product_Engagement_Score__c` at floor (e.g. 0.33 / 28.05) but real sustained capability adoption present. → `promote_in_queue`; tag "AERO FALSE NEGATIVE"; force into the rep's top-N regardless of composite.

Both overrides append a row to `Revenue Reviews/aero_feedback_queue/{YYYY-MM}.tsv` (lock-in #8).

**Verdict picklist** (writeback to `Account.Product_Engagement_Verdict__c`): Healthy / Established / Emerging / `GHOST_ACTIVE` / `AERO_FALSE_NEGATIVE` / `NO_DATA` / `Truly Dead`. `NO_DATA` when `_active` has zero non-zero weeks in the window (return explicitly, never guess).

## 6. Event registry

### Tier 1 — Core funnel events (reliable, curated)
| Event | Meaning | Key properties |
|---|---|---|
| `Signup (server)` | User signed up | `isFirstWorkspaceAdmin`, `leadSource`, `viralSource`, `jobRole`, `experimentVariant`, `signupPrimaryService` |
| `Plan changed` | Payment / plan change | `productId` (paid values in §7) |
| `ShoppingCart_ProductComparison_PageLoaded` | Viewed pricing/comparison | 29% of buyers hit this before any feature |
| `ShoppingCart_Summary_PageLoaded` | Viewed checkout summary | purchase-intent |
| `ShoppingCart_PayNow_Clicked` | Clicked pay | direct purchase-intent |
| `Billing - purchase` / `Billing - purchased for` | Purchase confirmed | final conversion |

### Tier 2 — Activation & feature events (need specific filters)
| Event | Meaning | Trap |
|---|---|---|
| `Sent email on server` | Email sent via Mixmax | MUST filter (sequence/template/calendar/insight). Never analyze unfiltered. |
| `SequenceEditor_ConfirmActivateSequence_Clicked` | Sequence activated | Aha #1 — strongest payment predictor |
| `SequenceServer_ActivateRecipients_Activated` | Server-side sequence activation | pair with above |
| `Sequences_Sequence_Created` | Sequence created | creation ≠ activation |
| `Connected Third-Party Integration` | 3rd-party connected | exclude google/microsoft (universal); signal: linkedin, salesforce, hubspot, zoom |
| `Template` | Template used | filter `action = "create"` for real creation |
| `meeting templates` | Calendar setup done | MUST filter `action = updated` |
| `MeetingCopilot_Summary_Attempt` / `_Accessed` / `_SharedEmail_Sent` | Meeting Copilot usage | low volume / niche |
| `Workspace_Member_Added` | Team member added | expansion signal |
| `Tasks` | Tasks usage | filter `action = "completed task"` |
| `Rules` | Automation rules | filter `action = 'activate'` |
| `Calendar_Meeting_Confirmed` | Meeting booked via Mixmax | value/outcome signal |
| `Installed extension` / `Clicked install extension` | Extension install (confirmed / proxy) | setup moment |
| `Viewed message tracking details` | Checks tracking in Gmail | engagement signal |
| `App_Navigation_PageLoaded` | Navigation | journey only, NOT conversion |

### Tier 3 — Noise (warn or exclude)
`Onboarding_Step_Shown`/`_Finished`, `OnboardingHub_*`, `Dashboard onboarding finished`, `Created profile` (exception: `hasExtensionInstalled = true` = setup moment), `Created workspace`, `Message sent via Mixmax Lite`, `Calendar inserted`, `User_Levers_Changed`, `Sent email on server` (unfiltered), `Shared conversations`/`Sent sidechat message` (filter `action = "added comment"` for real usage), Gmail UI performance events, `LayoutMigration_*`, `ImportContacts_*`.

## 7. Conversion funnel, aha moments, paid plans

**Aha moments (predict payment):**
- Aha #1 — Sequence activation: `SequenceEditor_ConfirmActivateSequence_Clicked` or `SequenceServer_ActivateRecipients_Activated` — **31% conversion**, strongest predictor.
- Aha #2 — Action taken (Todo / Smart Follow-up): instrumented from **Feb 18, 2026** onward (no data before).
- Aha #3 — Email with calendar enhancement (see §4 cap 6 trap).

**Self-serve funnel:** `Signup (server)` (filter `isFirstWorkspaceAdmin = True` for first-admins) → pricing/cart Tier-1 events → `Plan changed` / `Billing - purchase`.

**Paid `productId` values** (count as paid on `Plan changed`): `[gen1-inbox-copilot]`, `[gen1-engagement-copilot]`, `[gen1-meeting-copilot]`, `[gen1-bundle]`, and their `custom-branding-addon` combinations; legacy `mixmaxEnterpriseAnnualOct2017`, `mixmaxProfessionalAnnualOct2017`, `mixmaxProfessionalMonthlyOct2017`. **Exclude** trials (`[gen1-bundle-trial]`, `[gen1-inbox-copilot-trial]`), free/downgrades (`[gen1-free]`, `Free`, `[]`), and direct-sales (`[gen1-copilots-for-teams, gen1-custom-branding-addon]`) when measuring self-serve paid conversion.

## 8. New-user signals (lock-in #18)
`new_users_14d`, `new_users_30d` per gp:domain via first-seen analysis. Used by the Daily Drop (lead ranking) and onboarding-gap outreach: surface new signups at customer accounts and whether each activated within 7 days.

## 9. Inheritance + lock-ins
This file is the canonical; it inherits nothing and is inherited by everything product-usage. Related lock-ins: #8 (aero_feedback_queue row format), #14 (play-type override contract — Ghost-Active / Aero-False-Negative), #18 (new-user signal). SFDC field cross-walk (Website→gp:domain, PES + writeback fields) lives in `sfdc-field-library`.

## 10. When NOT to use
- For SFDC field meaning → `sfdc-field-library`.
- For the rendered per-account card / verdict flow → `product-engagement-story` (this file is the reference it reads).
- For running a specific account's story → `amplitude-analyst`.
- For ad-hoc funnel/recipe analysis → `amplitude-guide`.
