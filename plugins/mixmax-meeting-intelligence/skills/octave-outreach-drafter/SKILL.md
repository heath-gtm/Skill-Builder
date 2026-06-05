---
name: octave-outreach-drafter
description: >
  Drafts persona-specific outreach messaging for contacts identified in a meeting prep briefing.
  Takes the Top 3 People, conversation angles, and account context from a weekly-meeting-prep
  briefing and generates ready-to-send emails via Octave. Trigger on: "draft outreach for
  [person] at [company]", "write the email to [person]", "draft the next touch", "Octave
  message for [account]", "turn this briefing into outreach", or any request to translate
  meeting prep intelligence into sendable copy. Also trigger after a weekly-meeting-prep
  briefing when Heath says "now draft the email", "write something to send", or "what should
  I say to them". Works standalone or as the natural follow-up to a meeting prep briefing.
---

# Octave Outreach Drafter

Generates one opinionated outreach email per contact using the SMART framework, powered by
Octave's content engine and grounded in the data from a meeting prep briefing.

## When This Skill Fires

This skill activates in two contexts:

1. **After a meeting prep briefing** — Heath has just run a weekly-meeting-prep (any mode)
   and wants to turn the insights into an actual email. The briefing's Top 3 People,
   conversation angles, and Amplitude data are already in context.

2. **Standalone** — Heath names a person and company and asks for outreach. In this case,
   gather context first (use web search + Amplitude if needed) before drafting.

## The SMART Framework

Every draft follows this structure. Each section is 1-2 sentences max.

**S — Show Me You Know Me**
Reference something specific about the recipient's world — their company's recent news,
their role's typical pain, or (best) their actual Mixmax usage data from the briefing.
Not generic flattery. Something that proves you did homework.

**M — Map the Facts**
State the specific data point that makes this outreach relevant. Pull from Amplitude:
"Your team has 136 active Mixmax users sending 2,100+ emails/week" or from meeting history:
"Last time we spoke, you mentioned exploring Salesforce integration."

**A — Acknowledge the Cracks**
Name the gap or risk honestly. "But none of that activity is syncing to Salesforce" or
"Your sequence adoption is concentrated in just 15% of users." This builds credibility —
you're not pretending everything is perfect.

**R — Reveal the Impact**
Connect the gap to a business outcome they care about. "That means your CRM is blind to
your team's most active selling channel" or "You're leaving 4-5x sequence volume on the
table." Keep it quantified when possible.

**T — Take Action**
One clear, low-friction CTA. Not "let's schedule a call." Something specific:
"Would a 15-minute walkthrough of the Salesforce sync make sense this week?" or
"I put together a quick view of your team's adoption — want me to share it?"

## Draft Specifications

- **Length:** 75-120 words. Not a word more. Shorter is better.
- **Tone:** Strategic partner, not sales rep. You're a peer sharing insight, not pitching.
- **Recipients:** One email per person. Never batch multiple people into one email.
- **CTA:** Exactly one. Specific and low-commitment.
- **Subject line:** Include a suggested subject line. Short, specific, no clickbait.

## How to Use Octave

If the Octave MCP tools are available (`generate_email`, `generate_content`, etc.):

1. Use `generate_email` with the recipient context, company context, and the SMART framework
   as the structural guide
2. Pass the conversation angle from the briefing as the email's strategic focus
3. Set tone to "strategic-partner" (not "sales-rep" or "marketing")

If Octave tools are NOT available, draft the email yourself following the SMART framework
using the briefing data as source material. The framework is the important part, not the
tool.

## Output Format

For each contact:

```
### Draft for [Name] — [Title at Company]

**Subject:** [suggested subject line]

[Full email body — 75-120 words, SMART framework]

---
**Why this person:** [1 sentence from the briefing explaining the data-backed reason]
**Angle used:** [which conversation angle from the briefing this maps to]
**Data referenced:** [specific metrics cited in the email]
```

## What NOT to Do

- Don't write generic outreach that could be sent to anyone at any company
- Don't mention Mixmax features by name unless the recipient already uses them
- Don't use phrases like "I wanted to reach out" or "I hope this finds you well"
- Don't include multiple CTAs or vague next steps
- Don't exceed 120 words — ruthlessly cut
- Don't draft for people at companies where the briefing says there's zero Amplitude data
  (prospect with no usage = different playbook, not this skill)
