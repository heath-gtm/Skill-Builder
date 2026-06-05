---
name: ae-pipeline-runbook
description: >
  Reference runbook for generating, regenerating, or troubleshooting the
  Mixmax AE Pipeline Analysis report. Use whenever the user asks
  "how do I run the AE pipeline analysis", "regenerate the pipeline report",
  "what goes in the must-win section", "how are deals tiered",
  "run a pipeline review for Jordan", "show me Jordan's pipeline",
  "what deals does Jordan have", or any question about the AE pipeline
  methodology, deal deep-dive protocol, tier assignments, Octave plays,
  or output format.
---

# AE Pipeline Analysis — Runbook

Reference guide for generating and troubleshooting the AE Pipeline Analysis.

---

## Quick Start

1. Trigger the `ae-pipeline-analysis-report` scheduled task
2. When prompted, provide the **AE name** (e.g., "Jordan", "Mike")
3. The workflow runs through 4 checkpoints — review and approve at each
4. Report publishes to GitHub Pages at `ae-pipeline/{AE_Name}_Pipeline_Analysis_{date}.html`

---

## The 4 Checkpoints

### Checkpoint 1 — Deal List & Tier Verification
**After:** Data pull from AE Forecast tab
**Shows you:** All open deals with amount, stage, close date, and proposed tier
**You confirm:** Deal list is complete and tier assignments are correct

### Checkpoint 2 — Deep-Dive Summary
**After:** Amplitude, meetings, Gmail, sequences, web research completed
**Shows you:** Summary table — Account | Amount | Stage | Tier | Usage | Meetings | Top Contact | Stuck? | Key Signal
**You confirm:** Data looks right, no domains to retry, no re-investigations needed

### Checkpoint 3 — Strategic Plays Review
**After:** Octave plays generated for all Must-Win/Should-Win/Stuck deals
**Shows you:** Per-deal play summaries and email subject lines
**You confirm:** Priorities and messaging angles are appropriate

### Checkpoint 4 — Report Review
**After:** HTML report generated
**Shows you:** Local file link to the complete report
**You confirm:** Report is ready to publish

---

## Deal Priority Tiers

### Must-Win (Tier 1) — green badge
Any deal matching:
- Forecast Category = "Commit" or "Best Case" AND Amount ≥ $10K
- OR: Stage ≥ 3 (Proposal/Negotiation) AND Amount ≥ $25K
- OR: Close Date within 30 days AND Stage ≥ 2

### Should-Win (Tier 2) — yellow badge
Any deal matching:
- Stage 2+ AND Amount ≥ $5K
- OR: Forecast Category = "Pipeline" AND Close Date within 60 days
- OR: Strong Aero Fit (≥70) AND active trial usage in Amplitude

### Long-Shot (Tier 3) — gray badge
Any deal matching:
- Stage 1 (Early Discovery) regardless of amount
- OR: Close Date > 90 days out
- OR: No meetings in 30+ days AND no sequence enrollment
- OR: Weak Aero Fit (<50) AND no trial usage

---

## Stuck Deal Detection

A deal is flagged "stuck" if ANY of:
- Close date is in the past (overdue)
- >14 days in current stage with no forward movement
- No meetings in 30+ days
- No email replies in 21+ days
- Sequence enrollment stalled (all stages exhausted, no reply)
- Prospect usage declining or silent in Amplitude

**Unstick potential ratings:**
- **High:** Signals still warm, specific play available
- **Medium:** Some signals, needs creative approach
- **Low:** Likely dead, consider disqualifying

---

## Top 2 Most Engaged Contacts

Every deal card includes the 2 most engaged contacts identified from:
1. **Gmail threads** — search for `from:@domain.com OR to:@domain.com`, count messages per contact
2. **Mixmax meetings** — search by account name and attendee domain, count appearances per contact

**Scoring:** (meeting appearances × 3) + (email thread count × 1)

**Role assessments:** Economic Buyer / Champion / Technical Evaluator / Coach / Blocker / Unknown

---

## Deep-Dive Card Format

Each deal card contains:
1. **Header** — Account name, amount badge, stage badge, tier badge, stuck indicator
2. **Meta bar** — Owner, Amount, Stage, Close Date, Forecast, Record Type, Source, Aero Fit
3. **Top 2 contacts** — Name, title, last interaction, engagement score, role assessment
4. **Amplitude usage** — 6-month trial trend, classification, key features tried
5. **Sequence status** — Active enrollments or gap flag
6. **Meeting intelligence** — Objections, buying signals, competitive mentions, next steps
7. **Web research** — Company news, funding, leadership changes, urgency signals
8. **Strategic play** — Octave-generated email + call prep

---

## Octave Strategic Play Types

| Tier | Play Type | Octave Tools |
|------|----------|-------------|
| Must-Win | CLOSE or ACCELERATE | `generate_email` + `generate_call_prep` |
| Should-Win | ADVANCE or VALIDATE | `generate_email` |
| Stuck | UNSTICK or DISQUALIFY | `generate_email` + alternate contact strategy |
| Long-Shot | INVEST / PARK / DISQUALIFY | Brief recommendation (INVEST gets 1 email) |

All plays are grounded in: Amplitude trial data, meeting conversation history, company research, contact role, and deal stage.

---

## Troubleshooting

### "No open deals found for this AE"
- Check the AE name matches the Opportunity Owner column exactly
- Try first name only, then full name, then last name
- Check the AE Forecast tab directly to see how owner names are formatted

### "Amplitude returned zero results"
- Use the Website column (Col X) as the primary domain
- Try alternate domain variations
- Some prospect accounts haven't started a trial — that's valid data (classify as "No Trial Activity")

### "Gmail search returned no threads"
- Verify the domain spelling
- The AE may communicate through Mixmax sequences rather than direct email
- Check sequence enrollment as an alternative engagement signal

### "Tier assignment feels wrong"
- Override at Checkpoint 1 — tell the workflow which deals to re-tier
- Tiers are based on Stage + Amount + Close Date + Forecast Category
- Real-world context (champion relationship, verbal commit, etc.) should override formula

### "Octave play feels generic"
- Provide more context: specific Amplitude metrics, meeting objections, company news
- Request regeneration with a specific angle (e.g., "focus on the competitive threat from Outreach")

---

## Output

- **Local file:** `Revenue Reviews/AE Pipeline Analysis/{AE_Name}_Pipeline_Analysis_{YYYY-MM-DD}.html`
- **GitHub Pages:** `${GITHUB_PAGES_URL}/ae-pipeline/{filename}`
- **Archive:** Previous reports stored in same directory for historical comparison
