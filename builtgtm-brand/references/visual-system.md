# The Sales Operator Visual System · Blueprint (v3, Aug 2026)

The full token, typography, and component spec for any rendered Sales Operator
document. This replaced the amber editorial system on Aug 22 2026. If a
document uses Construction Amber `#F26A24`, Forest `#2D5F4F`, soft shadows, or
the bracket-only `[ Built GTM ]` or `[ The Sales Operator ]` wordmark, it is the OLD brand: rebuild it.

The live specimen is https://thesalesoperator.ai/brand/brand-specimen.html — if a
document does not look like that page, it is off-brand.

## Tokens

| Token | Hex | Use |
| --- | --- | --- |
| Blueprint Cobalt | `#2B5CE7` | The one accent: block logo, rules, numbers, CTAs, links |
| Cobalt Deep | `#1E44B8` | Hover states, links on paper |
| Warm Ink | `#101014` | Text, 2px borders, hard shadows |
| Warm Paper | `#F6F5EF` | The page ground (never plain white) |
| Safety Orange | `#FF6B2C` | Rare signal accent ONLY (replaced Forest) |
| Mid Neutral | `#6B6B6B` | Secondary text |
| Border Light | `#D6D4CC` | Hairlines inside cards |
| Surface White | `#FFFFFF` | Card surfaces |

Cobalt tint fill: `rgba(43,92,231,.07)`; cobalt tint border: `rgba(43,92,231,.30)`.

## The ground

Paper with the faint cobalt blueprint grid:

```css
background:#F6F5EF;
background-image:linear-gradient(rgba(43,92,231,.05) 1.5px,transparent 1.5px),
                 linear-gradient(90deg,rgba(43,92,231,.05) 1.5px,transparent 1.5px);
background-size:44px 44px;
```

## The mark

The `[THE_SALES_OPERATOR]` block logo, drawn inline (never the bracket-only wordmark; it read `[SALES_OPERATOR]` until Oct 2026):
Geist Mono 700, white, on a cobalt block, 2px ink border, 3px hard shadow,
6px radius. Header AND footer of every document. On dark grounds use the
inverted block: paper block, cobalt type, cobalt border + shadow.

```css
.block{font-family:'Geist Mono',monospace;font-weight:700;color:#fff;
background:#2B5CE7;border:2px solid #101014;border-radius:6px;
box-shadow:3px 3px 0 #101014;padding:2px 9px;}
```

## Typography

Geist for everything; Geist Mono for labels, numbers, and the logo. Import:
`https://fonts.googleapis.com/css2?family=Geist:wght@400;500;700;800&family=Geist+Mono:wght@500;700&display=swap`
H1 3.4rem/800/-.035em. H2 1.6rem/800. Body 15.5px/1.65 in ink. Headlines are
sentence case; the only all-caps is mono labels.

## Components

- **Sticker label (the eyebrow on everything):** mono 700 uppercase, ink text
  in a white chip, `border:2px solid #101014; box-shadow:2px 2px 0 #101014;
  padding:3px 10px; transform:rotate(-1deg);` no border-radius.
- **Section card:** white surface, `border:2px solid #101014; border-radius:
  10px; box-shadow:6px 6px 0 #101014; padding:32px 36px;` Nothing floats; no
  blurred shadows anywhere.
- **Cobalt rule:** 64x6px solid cobalt bar, square corners, under the H1.
- **Section number:** `01 /` in Geist Mono 700 cobalt, above the H2.
- **Facts grid:** 1px `#D6D4CC` gaps between white cells, wrapped in a 2px ink
  border, 8px radius. Mono uppercase key, 600 ink value.
- **Numbered steps:** `01` `02` in mono cobalt left of each item.
- **Callout:** cobalt tint fill, `border:2px solid #2B5CE7; border-radius:8px;`
  with a mono uppercase cobalt kicker line.
- **Signal tag (rare):** Safety Orange text on `rgba(255,107,44,.08)` with a
  1.5px `rgba(255,107,44,.4)` border, 4px radius. Use for at-risk / caution /
  the one highlighted signal. Never as a second accent.
- **Primary CTA:** cobalt fill, white text, 2px ink border, 4px hard shadow,
  6px radius; on hover translate(-2px,-2px) and grow the shadow. Secondary:
  same but white fill, ink text.
- **Pill:** cobalt text on cobalt tint, 1.5px cobalt-tint border, 4px radius,
  mono uppercase. Used for a collection or version tag next to the eyebrow.

## Rules

1. One accent. Cobalt does all the accent work; orange appears only when
   something is genuinely a signal.
2. Hard shadows only: ink offsets, no blur, no glow, no gradient.
3. Borders are 2px ink. Hairlines (1px `#D6D4CC`) live only inside cards.
4. The block logo appears top and bottom. Never recolored, never borderless.
5. Paper ground with the grid; white is reserved for card surfaces.
6. Copy caps near 640px measure inside cards. Mobile collapses to one column.
7. No em dashes anywhere in the copy. No emojis.
8. Start from `assets/template.html`; never build the scaffold from memory.
