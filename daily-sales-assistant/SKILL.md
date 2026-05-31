---
name: daily-sales-assistant
description: Your daily companion workflow. Composes Deal-Health + Pipeline-Creation + Coaching + Conversation Analysts into one morning brief — rep mode (your accounts today — deal-risk flags, hot leads, follow-up drafts, today's priorities) OR leader mode (your team today — coaching priorities, must-win deal status, rep-by-rep PLAN gaps). Connect Salesforce + Mixmax + Amplitude (full functionality) or any subset (degraded brief). Trigger on "morning brief", "what should I work on today?", "daily sales assistant", "today's priorities", "run my morning", "team morning brief", "leader morning brief", "what does my team need today?", "pre-1:1 brief", "daily companion", or any rep/leader morning-priorities request. Auto-fires 7am CT daily for Heath + opted-in users. Posts to user's DM or to designated channel.
---

# Daily-Sales-Assistant — your daily companion workflow

**This is a workflow, not an analyst.** It composes other agents (Deal-Health, Pipeline-Creation, Renewal-Health, Coaching, Conversation, Prospecting) into one morning brief — different output per persona.

**Required connectors:** depends on mode (see below).

## Two modes, one workflow

### REP MODE — "your accounts today"

**Audience:** AE / SDR / CSM

**Connectors needed:** Salesforce + Mixmax. Optional: Amplitude.

**Composition:**
- **Prospecting Analyst** → today's hot leads + cold re-engagement candidates
- **Deal-Health Analyst** → at-risk opps + multi-thread gaps in your book
- **Conversation Analyst** → meetings today + people you haven't followed up with
- **Comms Analyst** → drafts follow-ups for highest-priority gaps

**Output sections:**
1. 🎯 Top 3 priorities today (specific actions, named)
2. 🔥 Hot leads (Prospecting Analyst pulls)
3. ⚠ At-risk deals (Deal-Health flags)
4. 📅 Meetings today + prep links
5. 📝 Drafted follow-ups (one-click send)
6. 🎁 Bonus: account that needs attention this week

### LEADER MODE — "your team today"

**Audience:** Sales Manager / VP Sales / CS Leader / CRO

**Connectors needed:** Salesforce + Mixmax. Optional: Amplitude (multi-product expansion signal).

**Composition:**
- **Coaching Analyst** → today's coaching priorities + 1:1 prep
- **Deal-Health Analyst** → must-win deal status across team
- **Pipeline-Creation Analyst** → coverage health
- **Book-of-Business Analyst** (CS leaders) → portfolio at-risk
- **Renewal-Health Analyst** (CS leaders) → renewals this week

**Output sections:**
1. 🎯 Top 3 things to know today
2. 🧠 Coaching priorities (named rep + named issue)
3. 💰 Must-win deals — status + flags
4. 📡 Pipeline coverage health
5. 📅 1:1s today + pre-1:1 briefs
6. 🚨 Anything that needs leadership escalation

## Configuration

```yaml
# In your scheduled task config

DAILY_SALES_ASSISTANT_CONFIG:
  mode:              "rep | leader"
  audience:          "{user_email}"
  fire_time:         "07:00 CT"  # adjustable per user
  delivery_channel:  "dm | channel"
  channel_id:        "{slack_channel_id if delivery_channel=channel}"
  include_drafts:    true   # rep mode only — auto-draft follow-ups
  include_meetings:  true   # require Mixmax connector
```

## Quality gates

**Prioritization is forecast-aware.** Knows today is forecast call → "press on these 3 deals first."

**Drafts are review-first.** Follow-up drafts go to user's drafts folder, not auto-sent (unless user explicitly opted-in to autosend per workflow).

**Empty days surface honestly.** If user has nothing critical → "No critical items today, focus on Top 5 from Prospecting Analyst."

## Output format example (REP MODE)

```
☀️ KARAN — Monday June 1, 2026

🎯 TOP 3 PRIORITIES TODAY:
  1. Reply to Sarah Chen (Acme) — replied "yes interested" 2d ago, every day = -23% reply rate
  2. Prep for Mike Rodriguez (Vortex) — meeting at 2pm, deal at $67K SLIP risk
  3. Unstick Blend Labs — Day 30 + 0 sequences sent, your customer + Day 30 milestone missed

🔥 HOT LEADS (5):
  Sarah Chen @ Acme — replied 2d ago, no follow-up
  Mike Rodriguez @ Vortex — booked meeting yesterday  
  Jim Coulon @ Datadog — opened 4 emails in last 3d
  Petra Lovric @ Blend — clicked pricing yesterday
  Linda Park @ PGA — replied "send more info" 5d ago

⚠ AT-RISK DEALS IN YOUR BOOK (3):
  Vortex.io — SLIP, champion went dark (today's meeting is the test)
  Blend Labs — STUCK, no PLAN Next Steps + onboarding issue
  Datadog Trial — GHOST, 47 days zero activity (declare lost?)

📅 MEETINGS TODAY:
  10:00 AM — Internal pipeline review (Gabrielle)
  2:00 PM — Vortex.io (Mike Rodriguez) — prep link: [Brief]
  4:30 PM — Blend Labs CSM intro (HM joining)

📝 DRAFTED FOLLOW-UPS (in your drafts folder, review + send):
  • To Sarah Chen — "Quick demo this week?" (2 lines)
  • To Linda Park — "Sending the resources I mentioned" (1-pager attached)
  • To Tim Lee — re-engagement "Saw the layoff news, hope you're well"

🎁 BONUS — account that needs you this week:
  Halborn — champion just changed jobs at LinkedIn. Need re-thread or risk
  the renewal in November. Suggest reaching out to backup contact this week.
```

## Output format example (LEADER MODE)

```
☀️ TEAM MORNING — Monday June 1 · Karan + Isabelle + Felipe

🎯 TOP 3 THINGS TO KNOW:
  1. Karan needs PLAN-completion coaching this week (14% — lowest on team)
  2. Felipe has 2 deals quietly slid Commit → Best Case (commit creep)
  3. Pipeline coverage is at 78% for Q3 — Outbound is the gap

🧠 COACHING PRIORITIES THIS WEEK:
  Karan      — PLAN completeness + multi-thread (1:1 Tue 11am)
  Isabelle   — pipeline strategy (working hard but math gap, 1:1 Wed 2pm)
  Felipe     — top-of-funnel coverage (1:1 Mon 4pm — TODAY)

💰 MUST-WIN DEALS · 5 named:
  Acme Corp (Karan, $187K, HEALTHY, multi-thread good)
  Vortex.io (Karan, $67K, SLIP, champion gone — today's meeting is test)
  Datadog (Isabelle, $112K, MOMENTUM, ready for proposal)
  Stripe POC (Felipe, $89K, AT_RISK, single-thread)
  Brex Expansion (HM/Karan, $48K, HEALTHY)

📡 PIPELINE COVERAGE:
  Inbound:    99% covered (HEALTHY)
  Outbound:   43% covered (UNDER ★ — this is the lever)
  Product:    112% covered (OVER)
  Action: Felipe owns Outbound gap closing this week

📅 YOUR 1:1S TODAY:
  4:00 PM — Felipe — pre-brief: pipeline coverage + commit creep

🚨 LEADERSHIP ESCALATION:
  None today. Forecast call is Thursday — Karan/Vortex needs ground-truthing.
```

## Used by

- Standalone for daily morning briefs (this is the primary use)
- Slack-triggered ("morning brief" command)
- Scheduled task `daily-sales-assistant-rep-{user}` + `daily-sales-assistant-leader-{user}`

## When NOT to use

- For deep deal review (use Deal-Health Analyst directly)
- For book-wide CSM review (use Book-of-Business Analyst)
- For weekly retrospective (use Sales-Leader-Weekly or CS-Leader-Weekly reports)

## Salesforce field reference

This analyst inherits from `Revenue Reviews/specs/SFDC_FIELD_LIBRARY.md` —
the single source of truth for every field name, definition, and canonical
interpretation. Specifically, this analyst reads:

- Composes other analysts — does not query SFDC directly.
- Inherits field consistency through the agents it calls.

If a query needs a field not in the library, FAIL LOUD and request a library
amendment via Evolution Agent — never invent ad-hoc field names or definitions.
Apples-to-apples consistency across every analyst output is the goal.

## Inheritance from LOCKED_DESIGN.md

This workflow is locked-in #35 (proposed). Composes Deal-Health, Pipeline-Creation, Prospecting, Coaching, Renewal-Health, Book-of-Business, Conversation, and Comms Analysts. Reads all relevant lock-ins through them.

## Make.com / API packaging

This is a workflow — Make.com scenario chains the constituent analysts. The Daily-Sales-Assistant node accepts:

**Input:** `{ user_email: string, mode: "rep | leader", delivery: "dm | channel | inline" }`

**Output:** `{ brief_url: string, top_priorities: [...], sections: {...} }` — also delivers to Slack/email per delivery setting.

## Shippable as

Standalone connector-gated SKU bundling the underlying analysts. The flagship customer-facing product that demonstrates the analyst suite working together. Per-seat pricing tied to which connectors are wired up.

The Daily-Sales-Assistant is the first true compose-multiple-analysts workflow. It's the demo that sells the suite.
