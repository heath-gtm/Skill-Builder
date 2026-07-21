---
name: builtgtm-skill-publisher
description: Turn a private skill you built for your own stack into a clean public version anyone can install and customize, while preserving your personal copy untouched. Strips the company-specific wiring (connectors, CRM field names, proprietary scores, IDs, tuned thresholds, internal vocabulary) and abstracts it into a documented "Customize this for yourself" setup block, keeping the method intact. Trigger on "publish this skill", "make a public version of", "genericize this skill", "share-ready version of", "turn my skill into a community version", "add this to the Built GTM Skills page".
---

# Built GTM Skill Publisher

You built a skill for your own stack. It works because it is wired to your CRM, your fields, your scores, your thresholds. That wiring is exactly what stops anyone else from using it. This skill takes the private one and produces a public twin: same method, generic wiring, plus a setup block that teaches a stranger to make it theirs in ten minutes. Your personal copy is never touched.

## The one rule
The value you share is the METHOD. The thing you protect is the DATA: the field names, the thresholds tuned on your numbers, the customer and rep names, the IDs. Share the how. Strip the who and the what-we-measured.

## Step 1: Binding inventory
Read the source skill and every file it bundles. Tag each company-specific binding into one of seven types, and decide KEEP, ABSTRACT, or STRIP.

1. Connectors and tools. Named MCP or connector (Salesforce, Amplitude, a meeting tool). ABSTRACT to a role.
2. Data fields. Proprietary CRM or schema field names. ABSTRACT to a concept plus a field map.
3. Proprietary frameworks and scores. Your scoring model, methodology, or rubric. KEEP the concept, ABSTRACT the brand name, let the user plug their own.
4. IDs, secrets, project numbers. Project IDs, sheet IDs, tokens, internal URLs. STRIP. Replace with "set your own."
5. Tuned thresholds. Numbers fit on your data. KEEP as defaults, label "re-tune on your data."
6. Internal vocabulary and names. Product names, rep names, team names, internal doc references, "shippable as SKU," automation-platform packaging, lock-in numbering. STRIP or generalize.
7. Business taxonomy. Your channels, stages, segments. ABSTRACT to "your channels," "your stages."

Output a one-screen binding report: each item, its type, the decision, the replacement. Show it before you transform.

## Step 2: Transform
- KEEP the analysis logic, the verdict format, the quality gates, the "what good looks like." This is why anyone wants the skill.
- ABSTRACT connectors, fields, framework names, and taxonomy into documented placeholders with a default and an example.
- STRIP IDs, secrets, internal doc references, private names, packaging notes, and lock-in numbering. Gone.

## Step 3: The public skill shape
Every public skill ships these sections, in order:
1. Frontmatter. Generic name and description. No internal trigger names, no private workflow references.
2. What this does. One short paragraph, plain language, no jargon.
3. What you'll need. The connector roles and data prerequisites.
4. Customize this for yourself. The setup contract. A table of placeholders the user sets, covering connector swaps, the field map, the framework swap, and the tunable thresholds. Write it so a stranger makes it work on their stack in ten minutes. This is the most important section.
5. The method. The preserved logic, written against the placeholders.
6. Where the numbers come from. Which numbers are defaults, what to re-tune, what the method assumes.
7. Make it yours. One line inviting the user to fork and break it. Built GTM footer.

## The Customize contract (template)
```
## Customize this for yourself
This skill was built for a B2B SaaS sales org. Set these to match your stack:

| Set this        | What it is                          | Default / Example                 |
|-----------------|-------------------------------------|-----------------------------------|
| CRM             | your CRM connector                  | Salesforce, HubSpot, Pipedrive    |
| STAGE field     | your opportunity stage              | Opportunity.StageName             |
| QUALIFICATION   | your methodology's fields           | MEDDIC, BANT, your custom fields  |
| CHANNEL         | how you segment source              | Inbound / Outbound / Product      |
| DARK_DAYS       | no-activity days = at risk          | 14 (re-tune on your cycle)        |

No CRM connector? The skill says what to connect and stops. It does not guess.
```

## Step 4: Confidentiality gate (hard stop)
Before any public output, scan the draft for: real customer or account names, real person names, real dollar figures, field names that leak your schema, project IDs, tokens, internal doc paths, and any threshold described as tuned or validated on private data. If one survives, stop and flag it for the owner. When unsure, strip it.

## Step 5: Store, do not publish
- Personal copy. Leave the source skill exactly where it lives. Never edit the original. If it is not already in the owner's private repo, archive an exact copy to personal-skills/<name>/.
- Public draft. Write to public-skills/<name>/SKILL.md in the private repo. This is staging. It is NOT public until the owner explicitly says to push it to the public distribution repo.
- Include the one-line install command and the "make it yours" note.

## Process
1. Read the source skill and bundled files.
2. Run the binding inventory. Show the report.
3. Apply KEEP, ABSTRACT, STRIP.
4. Draft the public skill in the seven-section shape with the Customize contract.
5. Run the confidentiality gate. Flag anything uncertain.
6. Write to public-skills/<name>/. Confirm with the owner before anything goes public.

The method travels. The wiring gets documented. The owner stays in control of what ships.
