---
name: csm-book-runbook
description: >
  Reference runbook for generating, regenerating, or troubleshooting the
  Mixmax CSM Book of Business Analysis report. Use whenever the user asks
  "how do I run the CSM book analysis", "regenerate the book of business",
  "what goes in the at-risk section", "how are accounts categorized",
  "run a book review for Edwin", "show me Edwin's book", "what's in
  Edwin's portfolio", or any question about the CSM book methodology,
  account deep-dive protocol, engagement scoring, or output format.
---

# CSM Book of Business Analysis — Runbook

Reference guide for generating and troubleshooting the CSM Book of Business Analysis.

---

## Quick Start

1. Trigger the `csm-book-of-business-report` scheduled task
2. When prompted, provide the **CSM name** (e.g., "Edwin", "Heather")
3. The workflow runs through 4 checkpoints — review and approve at each
4. Report publishes to GitHub Pages at `csm-book/{CSM_Name}_Book_of_Business_{date}.html`

---

## The 4 Checkpoints

### Checkpoint 1 — Account List Verification
**After:** Data pull from Renewals tab
**Shows you:** All accounts in the CSM's book with ARR, renewal dates, health status
**You confirm:** Account list is complete and correct

### Checkpoint 2 — Deep-Dive Summary
**After:** Amplitude, meetings, Gmail, sequences, web research completed
**Shows you:** Summary table — Account | ARR | Usage | Trend | Meetings | Top Contact | Engagement Score | News
**You confirm:** Data looks right, no domains to retry, no re-investigations needed

### Checkpoint 3 — Section Assignments & Strategic Plays
**After:** Accounts categorized + Octave plays generated
**Shows you:** Which accounts are At-Risk, Growth, Most Engaged, Renewing 90d — plus 1-line play summaries
**You confirm:** Categorizations and strategic plays are appropriate

### Checkpoint 4 — Report Review
**After:** HTML report generated
**Shows you:** Local file link to the complete report
**You confirm:** Report is ready to publish

---

## Account Sections

### At-Risk Accounts
Accounts with ANY of:
- Risk Status flagged in the sheet
- Amplitude usage declining or silent
- No meetings in 60+ days
- No active sequence enrollments
- Negative company news (layoffs, M&A)

### Growth & Expansion Opportunities
Accounts with ANY of:
- Amplitude usage growing (especially feature adoption)
- Seat count growth signals
- Executive engagement in recent meetings
- Positive company news (funding, hiring)
- Product-qualified signals (hitting limits, exploring premium)

### Most Engaged
Top 5–10 accounts by composite engagement score:
- Score = (meetings × 3) + (emails × 1) + (sequence replies × 2)

### Renewing Next 90 Days
All accounts with renewal date within 90 days. Readiness badges:
- **READY:** Healthy usage + recent engagement + no risk flags
- **AT RISK:** Declining usage OR no engagement 30d+ OR risk flagged
- **NEEDS ATTENTION:** Mixed signals

---

## Top 2 Most Engaged Contacts

Every account card includes the 2 most engaged contacts identified from:
1. **Gmail threads** — search for `from:@domain.com OR to:@domain.com`, count messages per contact
2. **Mixmax meetings** — search by account name and attendee domain, count appearances per contact

**Scoring:** (meeting appearances × 3) + (email thread count × 1)

**Role assessments:** Champion / Power User / Executive Sponsor / Day-to-Day Contact

---

## Deep-Dive Card Format

Each account card contains:
1. **Header** — Account name, ARR badge, health badge, renewal countdown
2. **Meta bar** — CSM, ARR, contract start, renewal date, Aero Fit, health score
3. **Top 2 contacts** — Name, title, last interaction, engagement score, role
4. **Amplitude usage** — 6-month trend, classification, feature adoption
5. **Sequence status** — Active enrollments or gap flag
6. **Meeting intelligence** — Themes, sentiment, action items, exec engagement
7. **Web research** — Company news, M&A, funding, leadership changes
8. **Strategic play** — Octave-generated outreach (save / expand / renew angle)

---

## Octave Strategic Play Types

| Account Type | Play | Octave Tools |
|-------------|------|-------------|
| At-Risk | Save conversation + re-engagement email | `generate_call_prep` + `generate_email` |
| Growth | Expansion pitch + upsell conversation | `generate_email` + `generate_call_prep` |
| Renewing | Renewal conversation starter | `generate_call_prep` |

All plays are grounded in: Amplitude usage data, meeting conversation history, company research, and contact role.

---

## Troubleshooting

### "No accounts found for this CSM"
- Check the CSM name matches exactly (case-sensitive match on CSM Owner column)
- Try first name only, then full name
- Check the Renewals tab directly to see how CSM names are formatted

### "Amplitude returned zero results"
- Try alternate domain variations (e.g., companyname.com, company.io)
- Some accounts use parent company domains in Amplitude
- Check if the account is self-serve (may have individual user emails, not company domain)

### "Gmail search returned no threads"
- Verify the domain spelling
- The CSM may communicate through a different channel (Slack, Mixmax sequences)
- Check Mixmax sequences for the account as an alternative engagement signal

### "Octave play feels generic"
- Provide more context to the Octave tools: include specific Amplitude metrics, meeting themes, and company news
- Request regeneration with a specific angle (e.g., "focus on their declining sequence usage")

---

## Output

- **Local file:** `Revenue Reviews/CSM Book of Business/{CSM_Name}_Book_of_Business_{YYYY-MM-DD}.html`
- **GitHub Pages:** `${GITHUB_PAGES_URL}/csm-book/{filename}`
- **Archive:** Previous reports stored in same directory for historical comparison
