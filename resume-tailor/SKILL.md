---
name: resume-tailor
description: Given a job description, generate a tailored two-page ATS resume AND a cover letter for Heath Barnett, built strictly from the locked master (career/resume.json), then render PDFs and publish to the Lab at /private/resume. Trigger on "tailor my resume for", "generate a resume for this JD", "build a resume for this role", "write a cover letter for", "apply to this", or any pasted job description where Heath wants application materials. Never fabricates and never mirrors the posting's wording: the master is the only source of facts.
---

# Resume Tailor

Turns a job description into a tailored, two-page, ATS-clean resume and cover letter for Heath, from his locked master.

## The three rules (non-negotiable)

Rewritten Aug 13 2026 after a tailoring pass invented a claim and over-cut its best evidence. The old version of this skill told you to "use the JD's exact phrasing where Heath truthfully has it." That instruction is retired and is the direct cause of the failure. Replace it with these.

**1. TRACE.** `career/resume.json` and the `career/<company>/receipts.md` files are the ONLY sources of facts. You may reorder, reword, select, cut and reweight. You may NOT invent a number, company, logo, title, date, buyer, cadence or claim that is not in a source. If a requirement has no supporting fact, leave it unanswered. The invented line is always the one that gets checked, and it is usually the most load-bearing line in the document.

Before shipping, run the trace test: for every phrase not in the master, name the receipts file it came from. No source, no line.

**2. NO MIRRORING.** Never reuse the posting's distinctive phrasing. If a phrase appears in the job description, do not put it in the document. Say the same thing in Heath's own words. A reader recognises their own posting read back to them, and it reads as a candidate performing rather than reporting.

Before shipping, run the mirror test: search the variant for the posting's distinctive phrases. Any six-word run shared verbatim was chosen from the spec, not from memory. `checkJdMirroring()` in `site/lib/jobs/worker.ts` does this automatically for generated materials.

**3. NO OVER-CUTTING.** Tailoring deletes as dangerously as it adds. Never drop a named logo, an absolute dollar figure or a hard metric because it sits under a heading that looks less relevant. A real pass once cut Airbnb from a resume going to a short-term-rental company. Diff the variant against the master and justify every deletion, not just every addition.

## Locked content rules (these override anything in the source material)

- **Mixmax revenue does not publish, in any form.** It is not a growth story: roughly $10M on arrival, down to nearly $8M, back to roughly $10M. Never write a Mixmax revenue figure, range, band, multiple, or the words grew or growth about Mixmax revenue. What publishes is the swing and the efficiency: inherited a go-to-market at about -$1M in net ARR a year, took the new-business unit to net positive on 60% less spend and about 80% fewer selling heads.
- **The Mixmax frame is two jobs at once:** built an enterprise motion from zero WHILE making the existing commercial engine profitable, with one 15-person team covering inbound, outbound and product-led.
- **Cycle times are per channel.** Inbound 29 days, product-led 45, outbound 67 down from about 140. The 140-to-67 figure is OUTBOUND only and must never be published as the blended cycle.
- **Never write Heath as a solo builder.** He prototypes hands-on, then builds with Product, the data team and RevOps, and tunes with the reps who run on it. "I built it myself" is true only at Partake, where he co-founded with a CTO.
- **Motion mix beats the deal-size multiple.** Airwallex and Mixmax were product-led companies, so blended deal sizes were low by design. Do not publish or chase absolute ACV for either. The claim is that he builds a strategic enterprise layer on top of a product-led base, which he has now done twice.
- **Numbers publish as floors** with a plus, rounded down to a multiple of 5. Never publish a retention rate in any form; reframe retention as driving expansion revenue. Use the % symbol, never the word.
- No em dashes, no arrows, no emojis, anywhere.

## Procedure

1. **Read the JD.** Extract the real title and company, seniority, the competencies it leans on, its top three priorities, the industry and stage, and any hard requirements.
2. **Score the fit before writing.** If the posting gates on something Heath does not have, say so rather than papering over it. Absolute ACV at the strategic-enterprise end, an SVP tenure bar, a $100M+ ARR SaaS bar, or a required onsite location outside Remote-US / Dallas / Austin / Nashville are all reasons to advise against applying rather than to tailor harder.
3. **Reweight, do not rewrite.** Start from the master. Decide which roles carry this posting and give them the space; cut the least relevant role back rather than trimming everything evenly.
4. **Rewrite the summary and tagline in Heath's voice,** leading with the proof that matches their top priorities. Never with their sentence.
5. **Match competencies to the posting's subject matter,** not its wording. 6 to 8 items.
6. **Write the cover letter:** one story told deep, not an inventory. 240 to 420 words, at most two bullets, a 120-to-180-word narrative paragraph, names the company at least twice, and closes without "I would welcome" or any variant.

   Five hard rules, set by Heath on 25 Aug 2026 and enforced as guards in `site/lib/jobs/worker.ts` (`COVER_OVERRIDES` and `checkCover`). This skill and that generator must not disagree; the generator is the executable copy and wins on any conflict.

   1. **No closing question.** Not a soft one, not "one thing I would want to dig into on a call". The last sentence carries no question mark. This overrides the closing-question section of the shared thesis rule, which still applies to the brief and to outreach emails.
   2. **Uber Eats and Airwallex carry the opening proof.** Both named, with a concrete result attached to each, before Mixmax or Notch appears anywhere. Mixmax and Notch layer in after, as the closer analogue in size. Band-matching still decides which climb the thesis rests on; this decides the order the names appear in.
   3. **Open on why this role specifically.** The first paragraph names the company and one concrete thing from their posting or their business, and connects it to something Heath has actually done. An opener that would survive another company being pasted over it has failed.
   4. **Never assert a company fact the posting does not contain.** Their customers, customer count, headcount, revenue, funding, executives and reporting lines only appear if the job description says them. Research notes are a hypothesis, not a citable source. A Bitmovin draft claimed "over 400 customers, from the BBC to Hulu and Discovery"; the count appears nowhere and two of the three logos are not their customers.
   5. **Close on curiosity, never on a plan.** Name the one thing Heath genuinely cannot resolve from outside, say plainly he cannot see it from there, and say he would want to understand it. Written as a statement, so rule 1 still holds. Never "where I would start", "the first thing I would do", or "what they need is". Removing the closing question does not license a closing prescription.

## Render, gate, publish

1. Append the tailored application object to `career/applications.json` with `slug`, `company`, `role`, `date`, and any of `title`, `tagline`, `summary`, `competencies`, `experience`, `coverLetter`. Omit `experience` to inherit the master roles unchanged.
2. Render: `python3 career/render_resume.py` in a weasyprint env.
3. **Gate it. Do not skip this.**
   - `python3 career/eval_resume.py site/public/resume/applications/<slug>/resume.pdf` must return 0 fail. It checks the parse layer, field detection, the recruiter first screen, content rules, contradictions and shape.
   - `python3 career/verify_resume.py <same path>` must return PASS. It is the copy-paste test: page budget, fill, unmappable glyphs, probe strings.
   - Two pages, body type at 9.4pt or above, last page at least 80% full.
4. `node site/scripts/sync-content.mjs`, then commit and push to Built-GTM/Built-gtm main and confirm the Vercel deploy reaches READY.
5. Present the PDFs to Heath in chat. They also appear at /private/resume under Tailored applications.

## Files
- Master facts: `career/resume.json` (mirror `career/resume/resume.md` is GENERATED by `career/gen_resume_md.py`, never hand-edit it)
- Receipts: `career/<company>/impact.md` and `receipts.md`, `career/company-matrix.json`
- Applications: `career/applications.json`
- Renderer and layout: `career/render_resume.py`, `career/resume_layout.py`
- Gates: `career/eval_resume.py`, `career/verify_resume.py`
- Generation guards: `site/lib/jobs/worker.ts` (`checkCover`, `checkTailoredResume`, `checkJdMirroring`, `checkSoloBuilder`, `checkMixmaxRevenue`)
- Full spec: `career/TAILORING-WATERFALL.md`
