# Enrichment Analyst

> Your data-fill agent. Connect a contact-enrichment tool (contact-level) or a company-enrichment tool (company-level), or both for the full waterfall, to fill gaps on any list. Given a name plus a company, find email, phone, LinkedIn, and title. Given a domain, find headcount, funding, technographic profile, and hiring intent. Trigger on "enrich these contacts with emails", "find LinkedIn URLs for {list}", "get phone numbers for {contacts}", "who are the decision makers at {company}", "complete this prospect list", "enrich this CSV", "get the technographic stack for {company}", "fill in missing data on {list}", or any data-completion, list-enrichment, or contact-lookup question.

## Install

Paste this into your terminal (Claude Code):

```bash
mkdir -p ~/.claude/skills/enrichment-analyst && curl -fsSL https://raw.githubusercontent.com/heath-gtm/Skill-Builder/main/skills/enrichment-analyst/SKILL.md -o ~/.claude/skills/enrichment-analyst/SKILL.md && echo "Installed enrichment-analyst. Restart Claude Code."
```

Or download `SKILL.md` from this folder and drop it into `~/.claude/skills/enrichment-analyst/`, then restart Claude Code.

This skill runs on the data you paste, with nothing connected, and gets sharper as you connect your tools. Browse the full library at **[builtgtm.ai/tools](https://builtgtm.ai/tools)**.

---

# Enrichment Analyst

## What this does
This is your data-fill agent. Give it a name and a company, and it finds the email, phone, LinkedIn URL, and title. Give it a domain, and it returns headcount, funding, a technographic profile, and hiring intent. It works one contact at a time or across a whole list, tries the cheapest provider first, and tags every value it returns with how confident it is. It never invents a value it could not find.

## What you'll need
- A contact-enrichment tool (contact-level: email, phone, LinkedIn, title). Drives the contact waterfall.
- A company-enrichment tool (company-level: headcount, funding, hiring signals, technographic profile).
- Either one alone works at reduced quality. Both connected run the full waterfall.
- Optional: a people-search tool for LinkedIn URL identity validation, and a CRM to read records as input or write enriched values back.

No enrichment tool connected? The skill says what to connect and stops. It does not guess.

## Customize this for yourself
| Set this | What it is | Default / Example |
| --- | --- | --- |
| Contact-enrichment tool | Resolves email, phone, LinkedIn, title from a name plus company | Any contact-waterfall provider |
| Company-enrichment tool | Returns headcount, funding, hiring intent, tech profile from a domain | Any company-data provider |
| Identity-validation tool | Cross-checks a returned LinkedIn URL against the input name plus company | Optional people-search tool |
| CRM | System of record you read from and write enriched fields back to | Optional |
| Waterfall order | The sequence providers are tried in for the same field | Cheapest provider first |
| Confidence tags | The labels attached to every returned value | verified_2_source, verified_1_source, inferred, not_found |
| Minimum confidence | The lowest confidence you accept for a given use | verified_1 for dialing, inferred for research |
| Maximum spend | A per-run cost cap that stops the waterfall when reached | Set a dollar ceiling per run |

To swap a provider, point the contact or company role at a different tool. The method does not change. Only the connector behind the role changes.

## The method
The core pattern is a cost-aware waterfall. For any field, try providers in order, cheapest first, and stop the moment you get a confident answer.
1. Read the input. For each row you need a name plus a company (contact mode) or a domain (company mode). Note fields already present so they are not re-bought.
2. Run the contact waterfall. For email, phone, LinkedIn, and title, try providers in order. Take the first confident hit. Tag each field with its confidence.
3. Run the company pass. For a domain, return headcount, funding, hiring signals, and the technographic profile.
4. Discover the buying committee. For a "who are the decision makers" request, return the senior roles per account, each with confidence-tagged identifiers.
5. Validate every LinkedIn URL. Cross-check the name and company on the profile against the input. If they do not match, do not return the URL.
6. Track spend. Log credits per provider. If the run hits the cap, stop and return partial results with a note.
7. Return confidence-tagged rows plus an audit of providers used, the confidence breakdown, and total cost.

## Quality gates
- Confidence-tagged outputs. Every enriched field comes back with its source confidence, never a bare value.
- Identity validation on LinkedIn URLs before they ship. This blocks returning the wrong person.
- Cost-aware waterfall. The cheapest provider is tried first. Per-provider credit use is logged.
- Honest "not found." If a value cannot be found, return null plus not_found rather than guessing.

## Output (example)
```
Enrichment Complete  ·  5 contacts processed

Name       | Email                     | Phone        | Title
-----------|---------------------------|--------------|-------------------
Contact A  | a@example.co (verified_2) | +1-555-0101  | VP Sales (verified)
Contact B  | b@example.co (verified_1) | not_found    | CRO (inferred)
Contact C  | c@example.co (verified_2) | +1-555-0102  | CFO (verified)
Contact E  | not_found                 | not_found    | not_found

Audit:
  Confidence breakdown: 8 verified_2, 4 verified_1, 1 inferred, 3 not_found
  Total cost: within run cap
  Skip Contact E: source the LinkedIn URL manually before reaching out.
```

## Where the numbers come from
By default the waterfall tries providers cheapest-first and stops at the first confident hit, so the same field is never paid for twice. Confidence tags come from the providers: two independent sources is verified_2, one is verified_1, a pattern-derived guess is inferred, and a value no provider could confirm is not_found. Cost figures are the per-provider credit prices of the tools you connect. To change the economics, reorder the waterfall, swap in a cheaper provider, or lower the maximum spend.

## Make it yours
Set your two connector roles, your waterfall order, and your confidence floor, then run a small list to confirm the costs and tags read the way you expect. Built by an operator. Customize it, break it, make it better.
