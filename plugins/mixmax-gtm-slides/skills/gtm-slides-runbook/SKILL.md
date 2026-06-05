---
name: gtm-slides-runbook
description: Reference runbook for generating, regenerating, or troubleshooting the Mixmax GTM Slides HTML content workbench (v5.3.0). Use whenever the user asks "how do I run the GTM workbench", "what goes in each slide card", "regenerate just the Sales section", "how do I add a custom visual", "the chart export is broken", "what should the Q&A say", "how do I publish the workbench", "where is the Data Accuracy banner", "how do I edit K/S/S inline", "why is the sidebar collapsed", "what are the keyboard shortcuts", "how does decided tracking work", "what is the verdict pill", or any question about the v5.3.0 methodology — 34-slide layout, universal 7-block skeleton, cover Data Accuracy banner, universal visual picker, collapse-all sidebar, inline-editable K/S/S drivers, decided state tracking, keyboard navigation, sticky mini-header, or output format. Also use for ad-hoc one-off generations outside the scheduled task.
---

# GTM Slides Runbook — v5.3.0

This is the reference runbook for the **`leader-ceo-updates`** scheduled task. It describes the current state of the HTML content workbench and how to regenerate, troubleshoot, or tweak a specific part.

---

## Current state (v5.3.0)

- **34 slide cards** in the canonical order: `01, 02, 03, 04, D1, DS1, 05, 06, D2, SS1, D3, 18, D4, 13, 14, D5, 17, 07, 16, 15, E1, 08, 09, 10, 19, 11, 12, 23, R1, 20, 21, 22, GAL, 24`
- **13 Parts** × **21 sidebar Sections** taxonomy (Intro → Scorecard → Revenue → Direct Sales → Self-Serve → Customer Success → Pipeline → Expansion → Risks → Plan → Appendix → Q&A → Close)
- **Universal 7-block skeleton** on every slide — no exceptions
- **Cover Data Accuracy banner §0** at the very top of the cover (4 cards × 3 metrics = 12 rows)
- **Universal visual picker** (3 tabs: Cards only · Cards + K/S/S · Chart + Cards) replaces the old narrative-angle picker
- **Collapse-all-on-load** sidebar — every group starts collapsed except `sidebar-group-data-accuracy`
- **Inline-editable K/S/S drivers** on D1–D5 — each `<li>` is `contenteditable`, per-column Reset button restores rendered default
- **State-aware verdict pills** — `verdict-ok` (green), `verdict-watch` (amber), `verdict-risk` (red)
- **Decided state tracking** — per-slide toggle, sidebar chips, cover dashboard dots, session-scoped (no localStorage)
- **All-navy chrome** — `--mx-navy: #1D1D53` is the dominant header tone; magenta `#C53FDF` is the accent
- **Lazy-loaded charts** — `loading="lazy" decoding="async"` on every `<img>`

## The 7-block skeleton (memorize this)

```
1. Compact header        → slide-head slide-head-compact
2. 3 Stat cards row      → STAT_CARDS[slide_id] × 3
3. Visual picker         → 3 tabs, active drives Copy Template
4. Primary visual        → chart <img> OR K/S/S drivers card
5. Anticipated Q&A       → <details>, collapsed
6. Custom bullets box    → contenteditable scratchpad
7. Slide divider         → purple→lime gradient <hr>
```

If a slide is missing a block, that's a regression. Run the QA regex gate before assuming otherwise.

## Versioning history (short)

| Version | Key change |
|---|---|
| 4.3.0 | Decided-state tracking, narrative picker, 22 slides |
| 5.0.0 | 13-Part taxonomy, Custom Bullets box, Expansion slide E1 |
| 5.1.0 | 21-Section sidebar, new IDs (D1–D5 / DS1 / SS1 / R1 / GAL), unified bullet picker, chart picker tabs with YoY/QoQ variants |
| 5.2.0 | Universal 7-block skeleton, compact header, state-aware verdict pill, 3-stat-card row, all-navy chrome |
| **5.3.0** | **Cover DA banner §0, universal visual picker, collapse-all-on-load, inline K/S/S drivers, 34-slide QA gate** |

---

## Troubleshooting — common questions

### "Where is the Data Accuracy banner?"

Top of the cover page, above the AI summary. It's a 4-card grid: **ARR Contribution · Bookings · Pipeline · Renewals** — each card shows 3 metrics (actual · delta · segment split). The banner has its own sidebar entry (`sidebar-group-data-accuracy`) pinned open at the top of the TOC.

If it's missing from the cover, the task prompt didn't execute STEP 3b correctly — re-read `references/cover_page_spec.md` (v2.0.0) and re-run. The QA regex gate should have caught this: `assert "class=\"data-accuracy-banner\"" in html`.

### "Why is the narrative picker gone?"

Replaced in v5.3 with the **universal visual picker** (3 tabs: Cards only · Cards + K/S/S · Chart + Cards). Every slide now exposes the same picker shape; the active tab drives `data-copy-image` destination when the CEO clicks Copy Slide Template. Tab default per slide family:

| Slide family | Default tab |
|---|---|
| D1–D5 (Drivers) | `cards-kss` |
| Chart-bearing slides | `chart-cards` |
| Text-only (01, 19, 24) | `cards-only` (single-tab, picker collapsed to no-op) |

If you see narrative-angle tabs (Candid/Momentum/Action/Board) in the output, the task prompt is using an outdated spec version. Upgrade to v5.3.0 and regenerate.

### "How do I edit K/S/S drivers inline?"

On D1–D5 with the `cards-kss` tab active, every bullet `<li>` in the 3-column drivers card is `contenteditable="true"`. Click into a bullet, type, and then use Copy Slide Template to copy your edited version into Google Slides. If you want to revert to the rendered default, click the **Reset** button in the column toolbar — it swaps `innerHTML` back to the `data-default-html` snapshot captured at build time.

Edits are session-scoped — no persistence. Refreshing the page resets all columns.

### "Why is my sidebar collapsed when I load the workbench?"

v5.3 collapses every sidebar group on load. The CEO expands what he wants. `sidebar-group-data-accuracy` is the only exception — pinned open. The CSS gate is:

```css
aside.toc .sidebar-group[data-collapsed="true"] .sidebar-group-list { display: none; }
aside.toc .sidebar-group.sidebar-group-data-accuracy .sidebar-group-list { display: block !important; }
```

Click any group's header to toggle it open. Every group header shows `{decided}/{total}` chip that updates live.

### "How do I regenerate just the Sales section?"

You can't regenerate "just a section" in v5.3 — the workbench is a single-file HTML artifact built by one pass of the task prompt. Re-run the full `leader-ceo-updates` task; in STEP 2c Data QA you can flag only the Sales card values and accept the rest unchanged.

If the regeneration is truly surgical (e.g., fixing a typo in one slide's verdict text), edit the local HTML file directly in the working folder and re-publish via `mcp__3fa8b410...` Drive publish or the git data API. Skip the task prompt.

### "How do I add a custom visual?"

Custom visuals go in slots 16–21. During STEP 1 Context Intake, when asked "Custom visuals?", say yes and the prompt routes to STEP 1b, which collects:
1. The data (paste / describe / point to file or tab)
2. Chart type preference (bar / line / pie / waterfall / scatter) or let Claude recommend
3. The story — what should this chart convey?
4. Labels, colors, annotations

The generated chart is embedded on the target slide and follows the same 7-block skeleton as every other slide.

### "The chart export is broken — Copy Image produces a blank clipboard."

Three common causes:
1. **Browser blocks `ClipboardItem`.** Firefox requires HTTPS; Safari requires user-initiated gesture. Test in Chrome first.
2. **Active tab is `cards-only`.** The Cards-only picker tab has no chart to copy. Switch to `chart-cards` or `cards-kss`.
3. **PNG not found.** If the chart image 404'd at load, `fetch(img.src)` fails. Check the Network tab, confirm `chart_assets/{period}/{slide_id}.png` exists.

### "What should the Q&A say on each slide?"

3–5 anticipated board questions + answers per slide, collapsed by default. Target: the questions a board member would actually ask, not FAQ filler. Example for slide 03 (Revenue vs target):

- **Q:** Why did Direct Sales miss plan by $363.5K?
- **A:** Concentrated in 3 deals slipping out of Q1 (Acme, Globex, Initech — $287K combined). Attribution detail on slide D1.

The task prompt generates these from the base report; you can hand-tune in STEP 2c before the workbench is built.

### "How do I publish the workbench?"

STEP 8a: git data API push (blob → tree → commit → PATCH ref). The Contents API is 5 MB-capped and the workbench is 10–18 MB. Never use `PUT /repos/.../contents/...` for GTM Slides.

Target path: `reports/gtm-slides/GTM_{period}_Workbench_v5.3.0.html`
Target URL: `https://heath-gtm.github.io/mixmax-revenue-reports/reports/gtm-slides/GTM_{period}_Workbench_v5.3.0.html`

### "Why doesn't copy preserve formatting in Google Slides?"

Copy Slide Template uses `navigator.clipboard.write(new ClipboardItem({...}))` with `text/html` + `text/plain`. Google Slides paste picks up the HTML fragment and rebuilds it with styled text (bold, italic, colors preserved). If Slides is stripping formatting, check the Chrome paste menu for "Keep source formatting" — the default sometimes flips to "Match destination."

### "How do I copy the chart as an image?"

Click Copy Slide Template while the `chart-cards` tab is active. The JS reads the chart's `<img src>`, fetches the PNG blob, and writes `image/png` + `text/html` to the clipboard via `ClipboardItem`. Paste into Slides → you get both the image (as an image) and the surrounding HTML (as text).

### "What are the keyboard shortcuts?"

| Key | Action |
|---|---|
| `j` / `k` | Next / previous slide |
| `gg` | Jump to cover |
| `G` | Jump to last slide |
| `c` | Copy Slide Template (active picker tab) |
| `d` | Toggle decided on current slide |
| `b` | Toggle Board-only view |
| `/` | Focus sidebar search |
| `1` / `2` / `3` | Switch visual picker tab |
| `?` | Open shortcuts overlay |
| `Esc` | Dismiss overlay / exit focus |

No angle-switching keys — the narrative picker is gone in v5.3.

### "How does decided tracking work?"

Each slide's compact header has a `<button class="decided-toggle">Mark decided</button>`. Click toggles `data-decided="true"` on the `<section class="slide">`. Live updates propagate to:
- Sidebar group chip (`{decided}/{total}`)
- Cover dashboard dot (fills in with magenta)
- Progress meter at the top of the cover (if rendered)

Session-scoped. No localStorage. Refresh resets everything.

### "Why doesn't the sidebar show progress after I mark slides decided?"

Usually one of:
1. **The sidebar group is collapsed.** The chip updates either way, but the list underneath is hidden.
2. **The `data-decided-for` wiring dropped.** Check the per-slide toggle has `data-decided-for="{slide_id}"` and the sidebar anchor carries a matching `href="#slide-{slide_id}"`.
3. **The chart in the cover dashboard didn't bind.** Confirm the cover dashboard renders 21 dots (one per Section) and each dot carries `data-dashboard-section="{section_id}"`.

### "What is the verdict pill?"

A state-aware pill rendered in Block 1 of every slide (next to the slide number + section label). Three states:

| State | Class | When |
|---|---|---|
| OK / Hit | `verdict-ok` (green) | Metric at/above target |
| Watch | `verdict-watch` (amber) | Within 10% of target, trending risky |
| Risk / Miss | `verdict-risk` (red) | Below target or negative signal |

The pill's tint (background + border) is driven by the state class. The `verdict-label` ("Hit", "Watch", "Miss") + `verdict-text` (one-liner with dollar impact) give the CEO a 2-word read at the top of the slide before he scrolls.

### "Why does every slide have the same shape?"

That's the point of v5.2's universal 7-block skeleton. Legacy slides (01–24) were rewritten in place via `rewrite_legacy_slide_verdict` + `rewrite_new_slide_header` so they conform to the same 7-block layout as v5.x-native slides (D1–D5, DS1, SS1, R1, E1, GAL). The CEO reads every slide the same way, top-to-bottom, without re-orienting.

If a slide has an outlier shape (extra hybrid-pane composer, stacked 4-pack, narrative tabs), it's a v4.x leftover that didn't get rewritten. Re-run the task prompt against v5.3.0.

---

## Visual QA checklist

Before approving the workbench for publish:

- [ ] Cover page renders with **§0 Data Accuracy banner** at the top
- [ ] DA banner has **4 cards × 3 metrics** = 12 rows; all values populated (no `—` or empty)
- [ ] DA banner source citation footer present and cites the Gen 1 Quarterly Lookback tabs
- [ ] `sidebar-group-data-accuracy` renders at the top of the TOC and is **open** (not collapsed)
- [ ] Every other sidebar group starts **collapsed**
- [ ] **34 slides** in canonical order (spot-check IDs: `01 → 02 → 03 → 04 → D1 → DS1 → 05 → 06 → D2 → SS1 …`)
- [ ] Every slide has the **compact header** with verdict pill + action bar + decided toggle
- [ ] Every slide has **3 stat cards** (labels + values + signed deltas + arrows)
- [ ] Every slide has a **visual picker** with 3 tabs (or single-tab for text-only slides)
- [ ] D1–D5 K/S/S columns are `contenteditable` and have a **Reset** button
- [ ] Slide dividers render between every slide (purple→lime gradient)
- [ ] Copy Slide Template works on at least one slide per family
- [ ] Decided toggle updates the sidebar chip live
- [ ] Keyboard shortcut `?` opens the overlay; `j`/`k` navigate; `c` copies
- [ ] No console errors in DevTools

## QA regex gate (STEP 5)

```python
assert len(re.findall(r'<section class="slide[^"]*"', html)) == 34
assert len(re.findall(r'class="slide-head slide-head-compact"', html)) == 34
assert len(re.findall(r'class="verdict-pill', html)) == 34
assert len(re.findall(r'class="slide-action-bar"', html)) == 34
assert len(re.findall(r'class="decided-toggle"', html)) == 34
assert len(re.findall(r'class="custom-bullets-wrap"', html)) == 34
assert len(re.findall(r'class="slide-step slide-step-visual-picker"', html)) == 34
assert len(re.findall(r'class="slide-divider"', html)) >= 34
assert len(re.findall(r'class="sidebar-group ', html)) == 21
assert 'sidebar-group-data-accuracy' in html
assert 'class="data-accuracy-banner"' in html
assert html.count('class="da-tile') == 4
assert html.count('class="da-metric-row') == 12
assert 'Total ARR as % to target' not in html
```

Any failure blocks publish.

---

## References

- `references/gtm_slides_spec.md` v5.3.0 — canonical spec
- `references/gtm_slides_task_prompt.md` v5.3.0 — LLM-facing prompt
- `references/cover_page_spec.md` v2.0.0 — cover with §0 DA banner
- `references/universal_report_addendum.md` — ARR rule, QA, Cover Page, Slack rules
- `skills/gtm-slides-setup/SKILL.md` — setup & scheduled-task registration

**End of runbook.**
