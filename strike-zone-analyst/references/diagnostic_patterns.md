# Diagnostic Patterns — Strike Zone Math

For each leaky gate, the most common failure modes, the queries that disambiguate them, and the typical intervention. Read the pattern that matches the symptom, then run the disambiguating query before recommending action.

The reason for the disambiguation step: the same symptom often has 2–4 plausible causes. Recommending the wrong fix wastes a quarter. The five extra minutes to confirm pays for itself.

---

## Gate 1 — Cohort → Meeting Booked

**Symptom:** Meeting-booked rate is low (< channel baseline by 10pts+).

### Failure mode 1A: Touchpoint volume too low
- **Disambiguator:** Run touchpoint query (SOQL Q7). If median touchpoints < 5 for Outbound or < 2 for Inbound on accounts that didn't book, this is it.
- **Action (leader):** Cadence rewrite. Specify how many additional steps, what channels (call vs. LinkedIn vs. email), and over what time window.
- **Action (rep):** Pull the rep's accounts where touches < team median and re-engage with the missing channel.

### Failure mode 1B: Touchpoint volume fine, but quality is low
- **Disambiguator:** Compare reply rate on accounts that didn't book vs. accounts that did. If volume is matched but reply rate diverges, it's a copy/personalization problem.
- **Action:** Sequence audit. Run sequence-performance-analyst skill on the channel's top 3 sequences. Identify the step with worst reply rate, rewrite it.

### Failure mode 1C: Wrong-fit accounts entering the cohort
- **Disambiguator:** Pull cohort accounts grouped by `Aero_Account_Score_Date__c` and `Aero_Upsell_Fit_Tier__c`. If a disproportionate share of non-booking accounts are low-fit, the lead-scoring filter is broken upstream.
- **Action:** Tighten the cohort gate. Raise the score floor that triggers MQA/OQA/PQA. This is RevOps work, not rep work.

### Failure mode 1D (Product channel only): PQA fired but the user never returned to product
- **Disambiguator:** Pull Amplitude WAU for the cohort accounts in the 14 days post-PQA. If most accounts didn't return, the PQA is firing on a single-session signal that doesn't predict commercial intent.
- **Action:** PQA model rework. Add a retention requirement (e.g., 3+ sessions in 14d) before the PQA fires.

---

## Gate 2 — Meeting Booked → Meeting Completed (Show Rate)

**Symptom:** Show rate < 60% for Inbound, < 50% for Outbound, < 70% for Product.

### Failure mode 2A: Booking-to-meeting gap too long
- **Disambiguator:** Compute median days between `CreatedDate` of the Opp (or Meeting_Set_Date__c) and the actual meeting datetime. If > 5 days, no-shows climb steeply.
- **Action:** Shrink the booking window. Inbound: book within 48h of MQA. Outbound: book within 7 days. Add a confirmation Mixmax sequence between booking and meeting.

### Failure mode 2B: No confirmation/reminder workflow
- **Disambiguator:** Pull sequences associated with the channel — is there a "meeting confirmation" Mixmax sequence active for booked meetings? Check sequence enrollment rates on cohort accounts.
- **Action:** Install (or fix) a 2-touch confirmation sequence: T-24h reminder, T-1h "see you soon" with the link.

### Failure mode 2C: Meetings booked with wrong stakeholder (champion only, not decision-maker)
- **Disambiguator:** Cross-reference no-show accounts with FullEnrich or LinkedIn — were the booked contacts ICs vs. decision-makers? IC-booked meetings have higher no-show because the IC's calendar is less protected.
- **Action:** Update the qualification rubric — require a manager or above to book the meeting, or book the meeting with the champion + manager paired.

---

## Gate 3 — Meeting Completed → SQL (Stage 0)

**Symptom:** Of meetings completed, < 40% convert to `'0 - Qualification'`.

### Failure mode 3A: AE qualification is too loose at booking, too strict at SQL handoff
- **Disambiguator:** Compare meeting completion rate to SQL conversion across AEs. If a few AEs convert at 70% and others at 20% with similar meeting volume, it's individual qualification discipline.
- **Action:** Coaching call with the bottom-quartile AEs. CHAMP review (Challenges, Authority, Money, Prioritization). Pull 3 of their disqualified meetings and audit the discovery questions.

### Failure mode 3B: The "meeting" wasn't actually a sales meeting
- **Disambiguator:** Pull `Event.Subject` for completed-but-not-SQL meetings. If many are "Mixmax Demo Request" auto-bookings without a discovery component, the booking workflow is conflating product demos with sales-qualified meetings.
- **Action:** Split the workflow — auto-booked demos go to a self-serve track unless they hit a separate qualification gate. Sales-qualified meetings get a discovery-first agenda.

### Failure mode 3C: Discovery rubric is unclear
- **Disambiguator:** Read the SQL definition in the AE handbook. If it's vague ("AE judges it a real opportunity"), reps will diverge.
- **Action:** Crisp SQL rubric. CHAMP + SPRINT + PLAN — what is the minimum bar? Document, then audit a sample of recent SQLs against it.

---

## Gate 4 — SQL → SQO (Stage 0 → Stage 1, Discovery)

**Symptom:** Of opps that hit `'0 - Qualification'`, < 60% reach `'1 - Discovery'`.

### Failure mode 4A: Discovery meeting can't be scheduled
- **Disambiguator:** Days from SQL to next scheduled meeting. If > 14 days median, the prospect has cooled.
- **Action:** Service-level commitment — discovery within 7 days of SQL. Calendar holds on AE calendars. Maybe move SDR-to-AE handoff earlier.

### Failure mode 4B: Discovery happened but didn't qualify forward
- **Disambiguator:** Pull `Discovery_Completed__c = TRUE` opps that didn't move past Stage 0. Read the SFDC notes — what's the most common disqualifier (budget, timing, fit)?
- **Action:** If it's budget, push the budget question earlier (CHAMP M). If it's timing, build a nurture path. If it's fit, the cohort filter upstream is wrong (loop back to Gate 1C).

### Failure mode 4C: Stage definition mismatch
- **Disambiguator:** Spot-check 5 opps stuck in `'0 - Qualification'`. Are they actually discovery-stage in practice but never advanced in SFDC?
- **Action:** SFDC hygiene push. Stage update at end of each meeting is non-negotiable. RevOps audit weekly.

---

## Gate 5 — SQO → Closed Won (Win Rate)

**Symptom:** Of opps that hit `'1 - Discovery'` and closed, win rate < 25%.

### Failure mode 5A: Pricing pressure / late-stage discount creep
- **Disambiguator:** Compare `Amount` at SQO_Date vs. `Amount` at CloseDate for won and lost opps. If lost opps had bigger discount asks, pricing is the killer.
- **Action:** Discount-approval threshold. Above X%, requires manager approval. Surface the data in pipeline reviews.

### Failure mode 5B: Single-threaded deals losing the buyer
- **Disambiguator:** Count contacts on each Opp with `Contact.AccountId = Opp.AccountId`. Lost deals with 1 contact = single-threaded. If > 50% of losses are single-threaded, that's the pattern.
- **Action:** Multi-thread requirement at SQO. Three contacts minimum, including one decision-maker and one user.

### Failure mode 5C: Competitive losses
- **Disambiguator:** Search meeting transcripts (Mixmax meetings MCP) for competitor names in lost opps. Outreach, Apollo, Salesloft, Smartlead.
- **Action:** Competitive playbook refresh. Top-3 objection responses, latest battlecard. Train AEs on the specific competitor showing up most.

### Failure mode 5D: Wrong-fit accounts making it to SQO
- **Disambiguator:** Pull `Aero_Upsell_Fit_Tier__c` for lost opps. If most lost opps are low-tier, the qualification gates earlier in the funnel are too loose.
- **Action:** Re-tighten Gate 3 or Gate 4. This is a multi-gate fix — surface it as such.

---

## Gate 6 — Closed Won → Average Deal Size & Cycle Time

**Symptom:** Average deal size dropping, or cycle time stretching.

### Failure mode 6A: Segment mix shifting toward SMB
- **Disambiguator:** Pull `Account.Segment__c` for Closed Won across the comparison window. If SMB share rose, that's the cause.
- **Action:** Either accept it (volume strategy) or rebalance pipeline targets toward MM/ENT. Pipeline goals by segment, not just overall.

### Failure mode 6B: Discount creep
- **Disambiguator:** Compare list ARR vs. booked ARR over time. Use `ARR__c` and any list-price reference.
- **Action:** Discount-approval matrix. Floor pricing by segment.

### Failure mode 6C: Cycle time stretching late-stage
- **Disambiguator:** Use SOQL Q8 to decompose cycle time into the 3 sub-windows. Find the sub-window with the largest growth.
- **Action:** Address that specific sub-window. Usually it's SQO → Close (procurement, legal, security review). Standard MSAs and faster legal pre-clears.

---

## Multi-gate compounds

Sometimes the data shows two gates degrading simultaneously. The common patterns:

- **Gate 1 + Gate 3 both leaking** → The upstream cohort filter is too loose. Tighten lead scoring (1C and 5D treatments overlap).
- **Gate 2 + Gate 4 both leaking** → The handoff workflow is broken. Same booking-to-discovery friction shows up twice.
- **Gate 5 + Gate 6 both leaking** → Late-stage execution problem (pricing, competition, multi-threading discipline).

When you see a compound, the first action is to confirm it's actually one root cause and not two coincidental problems. Pull a few specific opps and trace them end-to-end.

---

## Reporting the diagnosis

Always frame the diagnosis as:
1. **Symptom** — which gate, what the delta is, against what baseline
2. **Most likely cause** — which failure mode, with the disambiguating evidence
3. **Recommended action** — Who / What / By when
4. **What we'd see if this works** — the metric that should move and by how much, in what timeframe

If you can't fill in #4, the action is too vague. Sharpen it before recommending.
