---
name: resume-tailor
description: Given a job description, generate a tailored two-page ATS resume AND a cover letter for Heath Barnett, built strictly from the locked master (career/resume.json), then render PDFs and publish to the Lab at /private/resume. Trigger on "tailor my resume for", "generate a resume for this JD", "build a resume for this role", "write a cover letter for", "apply to this", or any pasted job description where Heath wants application materials. Never fabricates: the master is the only source of facts.
---

# Resume Tailor

Turns a job description into a tailored, two-page, ATS-clean resume + a cover letter for Heath, from his locked master. Built for the Built-gtm Lab.

## The one rule (non-negotiable)

`career/resume.json` is the ONE flexible master and the ONLY source of facts. There are no role variants and no Gen 1 / Gen 2; this single master is it. The master headline is role-agnostic ("Revenue & GTM Leadership"). You may reorder, reword, select, cut, and rewrite to tell the right story for the JD and keep it to two pages. You may NOT invent a number, company, logo, date, or claim that is not in the master. If the JD wants something Heath cannot truthfully support, leave it out. No keyword-stuffing with unsupported claims.

Heath is a teacher and force-multiplier, NOT an individual closer. Never frame him as personally carrying a bag or closing deals (the only IC facts are early-career Accenture and founder-led Partake). Use coach / teach / develop / build-people language. Running discovery and win-loss himself IS on-brand.

Numbers note: the resume is a private application document, so real figures are fine. The public builtgtm.ai surfaces stay relative (Airwallex = "over 5x"). Keep the resume consistent with how Heath speaks in the Lab talk tracks.

## Inputs
- The job description (pasted).
- Optional: which master base fits best (cro / vpgtm / vpsales). If not given, infer from the JD's level and scope.

## Procedure

1. **Read the JD.** Extract: the real title + company, seniority, the 6-10 competencies/keywords it leans on, the top 3 priorities, the industry/stage, and any hard requirements (e.g. specific motion, region, team size).
2. **Set the title to match the posting.** On a tailored application, set `title` to the JD's exact role title (ATS best practice). The master stays role-agnostic; the tailored copy mirrors the posting.
3. **Rewrite the summary** into the JD's story: open with the role they're hiring, lead with the proof that matches their top priorities. 3-4 lines.
4. **Reorder + match competencies** to the JD's language (use the JD's exact phrasing where Heath truthfully has it; e.g. "net revenue retention" vs "NRR"). 8-10 items.
5. **Tailor the experience** to tell the right story in two pages:
   - Keep all six roles (chronology intact) unless space forces trimming the oldest.
   - Reorder/select/reword bullets so the most JD-relevant proof surfaces first per role.
   - Cut the least relevant bullets to hold two pages. Recent + most-relevant roles keep more bullets; older roles compress to 1-2.
6. **Write the cover letter** in Heath's authentic voice (plain, specific, operator, not corporate; no em dashes, no arrows, no emojis). Structure: one opening that names the role and the single most relevant proof; one middle that maps 2-3 of his receipts to their stated needs; one close on why this company/stage specifically. ~250-320 words, one page.
7. **Two-page check.** The resume must render to exactly two pages. If page 3 appears, cut the weakest bullets (oldest roles first) and re-render.

## Render + publish

1. Build a tailored application object and append it to `career/applications.json`:
   ```json
   { "slug": "company-role", "company": "Acme", "role": "VP Revenue", "date": "YYYY-MM-DD",
     "title": "VP Revenue (matches the posting)", "summary": "<tailored summary>",
     "competencies": ["..."], "experience": [ <tailored roles, same shape as resume.json experience> ],
     "coverLetter": ["para 1","para 2","para 3"],
     "resumeFile": "applications/company-role/resume.pdf",
     "coverFile": "applications/company-role/cover-letter.pdf" }
   ```
   Omit `experience` to fall back to the master roles unchanged.
2. Render: `python3 career/render_resume.py` in a weasyprint env (`pip install weasyprint --break-system-packages`). This regenerates the master `Heath-Barnett-Resume.pdf` and every application's resume.pdf + cover-letter.pdf into `site/public/resume/applications/<slug>/`.
3. Verify each tailored `resume.pdf` is 2 pages (pypdf).
4. `node site/scripts/sync-content.mjs` (ingests applications.json -> generated.json.applications).
5. Commit + push to Built-GTM/Built-gtm main (token `GITHUB_PAT_BUILT_GTM`), fire the Vercel deploy hook, verify READY.
6. Present the resume + cover letter PDFs to Heath in chat; they also appear on /private/resume under "Tailored applications".

## Reuse by Clay
This same procedure + the master is the brain for Heath's Clay workflow. If/when an API endpoint is stood up, it takes `{ jobDescription, master, base }` and returns the tailored application object above. The render + publish steps stay here.

## Files
- Master facts: `career/resume.json`
- Applications: `career/applications.json`
- Renderer: `career/render_resume.py`
- Page: `site/app/private/resume/` (ResumeView lists applications)
