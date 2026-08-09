---
name: resume-tailor
description: Given a job description, generate a tailored two-page ATS resume AND a cover letter for Heath Barnett, built strictly from the locked master, then publish it through the Job Engine so the real PDFs render. Trigger on "tailor my resume for", "generate a resume for this JD", "build a resume for this role", "write a cover letter for", "apply to this", or any pasted job description where Heath wants application materials. Never fabricates: the master is the only source of facts.
---

# Resume Tailor

Turns a job description into a tailored, two-page, ATS-clean resume plus a cover letter for Heath, from his locked master. Built for the Built-gtm Lab.

## The one rule (non-negotiable)

The master is the ONLY source of facts. You may reorder, reword, select, cut, and rewrite to tell the right story for the JD. You may NOT invent a number, company, logo, date, or claim that is not in the master. If the JD wants something Heath cannot truthfully support, leave it out. No keyword-stuffing with unsupported claims.

There are no role variants and no Gen 1 / Gen 2. One flexible master, role-agnostic headline.

Heath is a teacher and force-multiplier, NOT an individual closer. Never frame him as personally carrying a bag or closing deals (the only IC facts are early-career Accenture and founder-led Partake). Use coach / teach / develop / build-people language. Running discovery and win-loss himself IS on-brand.

## Where the master actually lives (read this before touching anything)

There are TWO copies and they are not interchangeable:

- `career/resume.json` in the Built-gtm repo. The human source of truth. What Heath edits.
- `storage.ats_career.resume_json` in the Lab database. The DB master. This is what the Job Engine's materials generator actually reads when it builds a tailored application.

They drift. Push the repo file to the DB, then stamp the shared fields onto every unapplied tailored copy:

```
POST https://builtgtm.ai/api/career-sync   Authorization: Bearer <AGENT_TEST_SECRET>
{"action":"read"}                       -> current DB master + tailored-copy count
{"action":"write","resume_json":{...}}   -> replace the DB master (auto-backs-up first)
{"action":"propagate"}                   -> copy shared fields onto every UNAPPLIED tailored copy
{"action":"pages"}                       -> page counts + anything over two pages
{"action":"jd_status"}                   -> which confirmed roles are still missing a real JD
```

`propagate` never touches `title`, `tagline`, or `summary`, which are per-role tailored, and defaults to unapplied roles only: a role Heath already applied to keeps the resume exactly as submitted.

## Structure of a role (the Built / Operationalized / XFN arc)

Every role in `experience` carries, in this order:

1. `company`, `location`, `dates`, `title`
2. `chapter`: the one-word arc of the role (TURNAROUND, SCALE-UP, STARTUP, ENTERPRISE & M&A)
3. `scope`: `<ARR band>  |  <org shape>`. The ARR band and the layers of management. Postings screen on both, and 7 of 9 senior postings want a manager-of-managers, so org shape always names the LAYERS, not just headcount. Where the band is a subset of the company, the scope is named in front ("Americas:", "15 markets:") so the band is not misread as company revenue.
4. `summary`: two or three sentences: what he walked into and what he owned.
5. `bullets`: grouped by the arc. A bullet beginning `### ` is a GROUP LABEL, not a bullet. Exactly these three, in order:
   - `### What I built`
   - `### How I operationalized it`
   - `### How I partner cross-functionally`

That arc is not decoration. It is the answer to the three things Heath is screened on: a build that became a system or process, building and enabling sales organizations, and cross-functional partnership driving outcomes. Every bullet lives under the label it proves.

"How I Operate" as a standalone section is RETIRED. The arc inside each role carries it. Do not reintroduce it.

## Numbers

Read `context/numbers-rules.md` in the repo and follow it exactly. The short version:

- Result metrics publish as rounded floors with a plus, never precise figures. 94% becomes 90%+, 335% becomes 300%+, 52% becomes 50%+.
- No NRR, GRR, or retention-rate figures in any form. Retention reads as DRIVING EXPANSION REVENUE, never a defensive percentage.
- The `%` symbol only, never the word "percent" spelled out.
- Always simplify. The shortest true phrasing wins.
- No em dashes anywhere.
- Structural counts keep their exact number (150-person hub, 15 reps promoted, 45-day ramp).
- Retired and not to be resurrected: Rule of 40, LTV/CAC, CAC payback.

The ARR bands in the scope lines are the ONE place a company's revenue range appears. Everywhere else, growth publishes as a multiple or a percentage.

## Titles Heath will not consider

Director-level seats of any flavor and Account Executive seats are out. Do not source them, do not tailor for them.

## Inputs
- The job description (pasted, or captured onto the role via `{"action":"set_jd","role_key":"...","jd_text":"..."}`).

Ground everything in the real JD. With `jd_text` empty the generator falls back to an inferred problem hypothesis, which is what produces presumptuous "here is your problem" copy. Capture the real JD first: Greenhouse `boards-api.greenhouse.io/v1/boards/{board}/jobs/{id}` returns `content`; Ashby `api.ashbyhq.com/posting-api/job-board/{board}` returns `descriptionHtml`.

## Procedure

1. **Read the JD.** Extract the real title and company, seniority, the 6-10 competencies it leans on, the top 3 priorities, industry and stage, and any hard requirements (motion, region, team size, ARR band taken through).
2. **Set the title to match the posting.** On a tailored application, `title` is the JD's exact role title (ATS best practice). The master stays role-agnostic; the tailored copy mirrors the posting.
3. **Rewrite the summary** into the JD's story: open with the role they are hiring, lead with the proof that matches their top priorities. Keep it under about 1,000 characters; the two-page gate has headroom but the top of the page is the most expensive real estate on the document.
4. **Reorder and match competencies** to the JD's language where Heath truthfully has it. 8-13 items.
5. **Tailor the experience** without breaking the arc. Keep all six roles and keep the three group labels in every role. Reorder and reword bullets inside a label so the most JD-relevant proof surfaces first. Cut the weakest bullets from the oldest roles before touching the recent ones. Never move a bullet under a label it does not prove.
6. **Write the cover letter** in Heath's voice: plain, specific, operator, discovery posture rather than assumed problems. One opening that names the role and the single most relevant proof, one middle that maps two or three receipts to their stated needs, one close on why this company and stage. 350-400 words. No em dashes, no arrows, no emojis, never "excited" or "passionate", no bow-tied ending.

## Render and publish

The apply kits ship through the Job Engine, not by hand-editing a JSON file.

1. Confirm the role in the Job Engine so it lands in `storage.ats_tracking` with `status='confirmed'`.
2. Generate materials: `POST /api/worker-run {"role_key":"Company|Job Title"}`. This writes `resume_json` (the DB master plus the tailored title, tagline, and summary) and `cover_letter_md`.
3. The nightly `applications-sync` GitHub Action renders every confirmed role's PDFs into `site/public/resume/` and writes back `resume_url`, `cover_url`, `resume_pages`, and `resume_overlength`. To ship sooner, render locally and write back with `{"action":"set_render_meta","items":[...]}`.
4. Verify with `{"action":"pages"}`. `over_two_pages` must be 0.

`career/applications.json` is OVERWRITTEN by that nightly job. Do not hand-append tailored applications to it: the next CI run wipes them. The legacy `career/render_resume.py` path that reads it is kept only for the master PDF.

## The two-page gate

Enforced in code, not by eyeballing it. `site/scripts/render-applications.py` walks a density ladder starting at the canonical 9.1pt layout and only tightens whitespace and secondary type if a copy runs long. Body text never drops below the readable floor. If even the tightest rung overflows, the role is flagged `resume_overlength=true` and logged loud so it gets a manual trim instead of silently shipping a three-pager.

Headroom today: a tailored summary can run about 1,200 characters longer than the master's before the ladder starts working at all. Every current kit sits on the canonical rung.

## Layout lives in exactly two files

- `career/resume_layout.py`: the Python layout, imported by BOTH `career/render_resume.py` and `site/scripts/render-applications.py`.
- `site/lib/resumeHtml.ts`: the TypeScript layout, imported by the Job Engine, the tailored-apps list, the shareable brief, and the private resume view.

These two must stay in step. Do NOT re-fork the layout into a component or a script. That fork is exactly how the arc restructure reached the master PDF while all 63 apply kits printed "### What I built" as a literal bullet and ran to three pages.

## Files
- Repo master: `career/resume.json`
- DB master: `storage.ats_career.resume_json` (via `/api/career-sync`)
- Numbers rules: `context/numbers-rules.md`
- ICP and title rules: `context/job-search-icp.md`
- Receipts: `career/receipts.md`
- Shared layout: `career/resume_layout.py`, `site/lib/resumeHtml.ts`
- Renderers: `career/render_resume.py` (master), `site/scripts/render-applications.py` (all tracked roles, CI)
- Page: `site/app/private/resume/`
