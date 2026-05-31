---
name: enrichment-analyst
description: Your data-fill agent. Connect FullEnrich (contact-level) or Common Room (company-level) — or both for full waterfall — fills gaps on any list. Given name + company, find email + phone + LinkedIn + title. Given a domain, find headcount + funding + technographic profile + hiring intent. Use when a rep builds a target list, an SDR needs phone numbers, a CSM needs decision-maker identity, or RevOps hygienizes CRM data. Trigger on "enrich these contacts with emails", "find LinkedIn URLs for {list}", "get phone numbers for {contacts}", "who are the decision makers at {company}?", "complete this prospect list", "find personal emails for {list}", "enrich this CSV", "get the technographic stack for {company}", "fill in missing data on {list}", or any data-completion / list-enrichment / contact-lookup question. Also fire inside any workflow needing richer contact data than CRM has.
---

# Enrichment Analyst — your data-fill agent

**Required connector:** FullEnrich OR Common Room. Either alone works at reduced quality; both together unlock the full waterfall pattern.

**Optional connectors:** Octave (for `find_person` + `qualify_person` + LinkedIn URL identity validation) · Apollo / Lusha / ZoomInfo (additional providers in the waterfall) · LinkedIn scraper (for profile data beyond URL).

## What this analyst answers

In plain English, the Enrichment Analyst answers questions like:

- "Enrich these 50 contacts with email + phone" → Per-row enriched data with source-confidence tags
- "Find LinkedIn URLs for {list of names + companies}" → URL resolution with strict identity validation (no false positives)
- "Get the technographic stack for {company}" → Software-in-use profile (CRM, sales tools, conversational intelligence, data enrichment vendor)
- "Who are the decision makers at acme.com?" → Buying committee discovery — typical 5-7 senior roles per account with confidence-tagged identifiers
- "Complete this prospect list — half of them are missing emails" → Bulk waterfall with cost-per-credit awareness (cheapest provider first)
- "Find personal emails for these {list}" → Personal-email enrichment (work emails the system already has)
- "Get the CFO at {company}" → Single-role + company lookup
- "Fill in the missing phone numbers for these enrolled contacts" → Mid-sequence enrichment so callable contacts get a call task

## What it owns internally

The Enrichment Analyst is the product layer over these atomic skills:

- **D5 — Common Room Enrichment** — company-level signals (CR_Number_of_Employees, CR_of_Sales_Team, CR_Sales_Team_Hiring, technographic profile)
- **D6 — FullEnrich Contact Waterfall** — 11-provider waterfall for email + mobile + LinkedIn + title with `verified_2_source` / `verified_1_source` / `inferred` / `not_found` confidence per field
- **D7 — Octave Research** — `find_person`, `qualify_person`, LinkedIn URL identity validation (the strict-validation pattern that prevents false positives)
- The LinkedIn URL lookup pattern from the `deepline:linkedin-url-lookup` skill (when DeepLine is connected)

## The quality gates this analyst guarantees

**Confidence-tagged outputs.** Every enriched field is returned with its source confidence — never bare values. Reps can filter by confidence in their workflow ("only use verified_2_source for personal emails I'm about to dial").

**Identity validation on LinkedIn URLs.** When the analyst returns a LinkedIn URL for a name + company, it has cross-checked the name + company on the profile against the input — preventing the classic false positive of returning a different person's profile with a similar name. This is the strict-validation rule from the `linkedin-url-lookup` skill in the DeepLine plugin.

**Cost-aware waterfall.** When multiple providers can answer the same question, the analyst tries cheapest-first by default. Credit consumption per provider is logged so you can audit + optimize spend over time.

**Honest "not found"** — never fabricates. If a contact's email cannot be found across the entire waterfall, the analyst returns `null` + `not_found` rather than guessing.

## Output format example

For "Enrich these 5 prospects":

```
✅ Enrichment Complete · 5 contacts processed

┌────────────────┬──────────────────────────────┬────────────────┬──────────────────────────┬─────────────────────┐
│ Name           │ Email                        │ Phone          │ LinkedIn                 │ Title               │
├────────────────┼──────────────────────────────┼────────────────┼──────────────────────────┼─────────────────────┤
│ Sarah Chen     │ sarah@acme.co (✓ verified_2) │ +1503-555-1234 │ linkedin.com/in/sarahc   │ VP Sales (✓ verif)  │
│ Mike Rodriguez │ mike@acme.co (✓ verified_1)  │ — (not_found)  │ linkedin.com/in/miker    │ CRO (inferred)      │
│ Jim Coulon     │ jcoulon@acme.co (✓ verified_2)│ +1503-555-5678 │ linkedin.com/in/jimcoulon│ CFO (✓ verif)       │
│ Petra Lovric   │ petra@vortex.io (✓ verified_2)│ +44-20-7946-1111│ linkedin.com/in/petralovic│ CS Manager (✓ verif)│
│ Linda Park     │ — (not_found)                │ — (not_found)  │ linkedin.com/in/lindap   │ — (not_found)       │
└────────────────┴──────────────────────────────┴────────────────┴──────────────────────────┴─────────────────────┘

Audit:
  Provider credits used: FullEnrich × 4, Octave × 1
  Confidence breakdown: 8 verified_2, 4 verified_1, 1 inferred, 3 not_found
  Total cost: $1.12 (4× FullEnrich @ $0.25 + 1× Octave @ $0.12)

Recommended next action: Pass the 12 enriched contacts to Comms Analyst for SFDC write-back (lock-in #13). Skip Linda Park — manually source her LinkedIn before reaching out.
```

## Used by (workflows that compose this analyst)

- **W1 Per-Account Brief Pipeline** — every brief's buying committee is enriched
- **W6 Customer Interview Prioritizer** — used to find decision makers if PLAN Decision_Maker field is empty
- **W7 Reference Customer Finder** — used to identify the right contact at each reference candidate
- **W11 Lost-Deal Reopener** — used to find new champions if old champion has left the company
- **W12 Champion Migration Tracker** — used to track champions' new companies via LinkedIn lookup
- Used by Make.com scenarios as a standalone enrichment node

## When NOT to use this analyst

- For pure CRUD against your CRM (use Salesforce Analyst or the Salesforce MCP)
- For scoring whether a contact is worth enriching (use ICP Analyst first to triage, then enrich the qualifying subset)
- For mass list builds from scratch (use a TAM build tool — Apollo, ZoomInfo, etc. directly — the Enrichment Analyst optimizes per-contact, not whole-population)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Account.Website (for company-level enrichment)
- Contact.Email + Name + Account.Name (for contact-level enrichment join)
- Writes back: Contact.MobilePhone, Contact.LinkedIn (via Comms Analyst — lock-in #13)

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

This analyst inherits lock-in #13 (SFDC Contact write-back contract — FullEnrich beats stale CRM for `MobilePhone`, never overwrites `Email` unless explicitly told to) + the FullEnrich waterfall rules from `spec-inproduct.md` + the LinkedIn identity-validation rules from the `linkedin-url-lookup` skill.

## Make.com / API packaging

**Input schema:**
```json
{
  "mode": "contact_enrich | company_enrich | role_lookup | list_complete",
  "contacts": [{"name": "string", "company": "string", "existing_email": "string | null"}],
  "company": "string (when mode=company_enrich or role_lookup)",
  "role": "string (when mode=role_lookup, e.g. 'CFO' or 'VP Sales')",
  "fields_required": ["email", "phone", "linkedin", "title"],
  "max_cost_usd": 5.00,
  "min_confidence": "verified_1 | inferred"
}
```

**Output schema:**
```json
{
  "enriched": [
    {
      "name": "string",
      "company": "string",
      "email": {"value": "string | null", "confidence": "verified_2 | verified_1 | inferred | not_found"},
      "phone": {...},
      "linkedin": {...},
      "title": {...}
    }
  ],
  "audit": {
    "providers_used": {"FullEnrich": 4, "Octave": 1},
    "total_cost_usd": 1.12,
    "confidence_breakdown": {"verified_2": 8, "verified_1": 4, "inferred": 1, "not_found": 3}
  }
}
```

**Failure modes:**
- No enrichment provider connected: "Connect FullEnrich or Common Room to enable enrichment."
- Cost cap exceeded mid-run: returns partial results + flag "Cost cap reached at $5.00 — 23 of 50 contacts enriched. Increase max_cost_usd or retry remainder."
- All providers return not_found: returns `null` for the field + confidence `not_found` rather than guessing.

## Shippable as

**Standalone connector-gated SKU:** customer connects FullEnrich → contact-level enrichment. Connects Common Room → company-level enrichment. Connects both → full waterfall.

**Make.com sub-agent module:** discrete node, input is contacts array, output is enriched array. Chains naturally with ICP Analyst (qualify list → enrich qualifying) and Comms Analyst (enrich → SFDC writeback).

**Standalone API endpoint:** could be packaged as a per-enriched-contact pricing model — `$X.XX per verified_2 email, $Y.YY per verified phone` — much cleaner unit economics than monthly seat-based pricing.
