---
name: Dutchplanners Legal
description: A well-set legal dossier for searching omgevingsrecht uitspraken down to the rechtsoverweging.
colors:
  dp-red: "#dc3b40"
  primary: "#b82e33"
  primary-hover: "#99282c"
  primary-foreground: "#ffffff"
  dp-navy: "#000050"
  navy-light: "#152266"
  navy-100: "#dee3f4"
  navy-200: "#bfc8e9"
  navy-800: "#0b1242"
  background: "#ffffff"
  foreground: "#1a1a1a"
  hairline: "#eceae9"
  surface-hover: "#fafafa"
  muted: "#54595f"
  input-border: "#d8d1cf"
  control-border: "#8a7f7b"
  selected-bg: "#fdf3f3"
  selected-border: "#b82e33"
  selected-foreground: "#99282c"
  warm-gray-200: "#ecece9"
  warm-gray-250: "#e2dfde"
  warm-gray-500: "#a49995"
  charcoal-700: "#2a3036"
  highlighter: "#fde68a"
  alert-bg: "#fdf3f3"
  alert-border: "#ff8e90"
  dark-background: "#151217"
  dark-foreground: "#f1ecf2"
  dark-surface: "#211d24"
  dark-hairline: "#3c353f"
  dark-surface-hover: "#2b262f"
  dark-accent: "#8d9bfb"
  dark-accent-hover: "#aab5fc"
  dark-muted: "#a59cac"
  dark-input-border: "#453d49"
typography:
  wordmark:
    fontFamily: "Oxanium, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 800
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "IBM Plex Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.4
  title:
    fontFamily: "IBM Plex Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 600
    lineHeight: 1.5
  body:
    fontFamily: "IBM Plex Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.43
  data:
    fontFamily: "IBM Plex Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: "1.25rem"
    fontFeature: "\"tnum\""
  label:
    fontFamily: "IBM Plex Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.33
  passage:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.375
  reference:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.33
    fontFeature: "\"tnum\""
rounded:
  sm: "2px"
  full: "9999px"
spacing:
  "1": "4px"
  "1.5": "6px"
  "2": "8px"
  "3": "12px"
  "4": "16px"
  "6": "24px"
  "8": "32px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-foreground}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0 16px"
    height: "36px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-outline:
    backgroundColor: "{colors.background}"
    textColor: "{colors.foreground}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "32px"
  button-outline-hover:
    backgroundColor: "{colors.surface-hover}"
  button-ghost:
    textColor: "{colors.muted}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "32px"
  button-ghost-hover:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.foreground}"
  button-sm:
    typography: "{typography.label}"
    padding: "0 8px"
    height: "28px"
  input-search:
    backgroundColor: "{colors.background}"
    textColor: "{colors.foreground}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0 36px"
    height: "36px"
  chip-filter:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.foreground}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 0 0 8px"
    height: "24px"
  chip-aspect:
    backgroundColor: "{colors.background}"
    textColor: "{colors.foreground}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 6px"
    height: "20px"
  counter:
    backgroundColor: "{colors.navy-100}"
    textColor: "{colors.navy-800}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "0 6px"
  dictum-gegrond:
    backgroundColor: "{colors.navy-light}"
    textColor: "{colors.primary-foreground}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 6px"
    height: "20px"
  dictum-bestuurlijke-lus:
    backgroundColor: "{colors.navy-100}"
    textColor: "{colors.navy-light}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 6px"
    height: "20px"
  dictum-ongegrond:
    backgroundColor: "{colors.warm-gray-200}"
    textColor: "{colors.charcoal-700}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 6px"
    height: "20px"
  app-header:
    backgroundColor: "{colors.dp-navy}"
    textColor: "{colors.primary-foreground}"
    height: "48px"
  nav-item:
    textColor: "{colors.navy-200}"
    typography: "{typography.body}"
    padding: "0 12px"
    height: "48px"
  nav-item-active:
    textColor: "{colors.primary-foreground}"
  coverage-bar:
    backgroundColor: "{colors.warm-gray-200}"
    height: "4px"
    width: "56px"
---

# Design System: Dutchplanners Legal

## Overview

**Creative North Star: "De Griffie"**

The interface is a well-set legal dossier. White paper, warm-grey hairlines, navy text, and nothing that competes with the uitspraak itself. A planner comes here mid-dossier to find a citable rechtsoverweging and copy it back into a ruimtelijke onderbouwing; the screen behaves like a clerk's file, ordered and quiet, with every number aligned and every source one click away.

Density is professional, not cramped: a full-width table of uitspraken in 13px type on 20px lines, sections separated by whitespace and single hairlines rather than boxes. Colour is rationed. The navy header bar is the brand anchor; below it the page is paper and ink. Red, the house colour, appears exactly where a decision is made (the one primary action of the screen) and where you are (the active nav underline). Status colour belongs to the dictum and to errors, nowhere else.

Two devices carry the identity. The **r.o.-marge** sets rechtsoverweging numbers in mono in a narrow left margin beside serif passages, like randnummers in a law journal: it tells you where to cite from. The **dekkingsstreep** replaces a bare relevance score with a thin bar, so closeness to the search or the report reads at a glance.

**Key Characteristics:**
- White canvas, warm-grey hairlines, navy text; red only for the primary action, the active nav and a chosen filter.
- Flat in-flow content; only floating layers lift.
- Near-square 2px corners everywhere; full rounding only for counters, dots and markers.
- Three voices of type: Plex Sans for the UI, Source Serif 4 for uitspraak text, Plex Mono for ECLI and r.o.-numbers.
- Tabular figures for every number, date and count.
- Light and dark themes switch through semantic tokens on `data-theme`, never through the OS alone.

## Colors

A restrained paper-and-ink palette built on the binding house colours, with red held back for decisions and position.

### Primary
- **Griffie Red** (primary, dp-red-700): the one primary action per screen, such as *Zoek* next to the search field. Chosen over the raw house red because white text on it holds 5.6:1. Hover deepens to **Deep Griffie Red** (primary-hover).
- **House Red** (dp-red): the brand red. Used for the active nav underline on the navy bar, the "p" and the "Legal" suffix in the wordmark, and the sandglass loader. Never as text on white, never as a border on content.

### Secondary
- **Dossier Navy** (dp-navy): the header bar and brand chrome. In light mode it is also the accent: links, focus outlines, the hover edge on table rows, the filled part of the dekkingsstreep, `accent-color`, the caret and the tinted text selection.
- **Lifted Navy** (navy-light): link hover (deepens the navy, never turns red) and the filled GEGROND/TOEWIJZING dictum badge.
- **Pale Navy** (navy-100) with **Ink Navy** (navy-800): counters such as the active-filter count, and the BESTUURLIJKE_LUS dictum badge (navy-100 with navy-light text).
- **Muted Navy** (navy-200): inactive nav labels on the navy bar.

### Neutral
- **Paper** (background): the canvas, card surface and input fill in light mode.
- **Ink** (foreground): body text and data.
- **Griffie Hairline** (hairline, `--card-border` = `dp-light-bg`): every divider, table rule, chip border and floating-layer border.
- **Hover Wash** (surface-hover): row hover, outline and ghost button hover, filter-chip fill, skeleton bars.
- **Clerk Grey** (muted): secondary text, table head labels, placeholders, the r.o.-marge, ghost button text.
- **Field Edge** (input-border): resting border of inputs; on hover it darkens to **Stone** (warm-gray-500).
- **Control Edge** (control-border, #8a7f7b; dark #7a7080): resting border of outline buttons, ≥3:1 on the canvas (WCAG 1.4.11) so a clickable control reads as clickable at rest.
- **Chosen Red** (selected-bg dp-red-50, selected-border primary, selected-foreground dp-red-800; dark #2c1618 / #e0666b / #ffb4b7): a chosen filter (a select or the gemeente field with a value, an active aspect chip, the Kenmerken count).
- **Coverage Track** (warm-gray-200): the unfilled dekkingsstreep and the neutral dictum badges (ONGEGROND, AFWIJZING) with **Charcoal** (charcoal-700) text. Charcoal also sets the serif snippet text.
- **Highlighter** (highlighter, amber-200): `<mark>` behind query terms; its text stays dark (#1a1e22) in both themes.
- **Alert Blush** (alert-bg, alert-border, with primary-hover text): the error banner. Status colour, not decoration.

### Dark theme
A warm-charcoal canvas (dark-background), raised surfaces (dark-surface, dark-surface-hover) and hairlines (dark-hairline), with a single periwinkle accent (dark-accent, hover dark-accent-hover) replacing navy for links, focus and the dekkingsstreep. The header stays Dossier Navy. Warm-grey and charcoal ranges are remapped to warm-neutral tiers so pills and tracks never tint blue.

### Named Rules
**The Three Reds Rule.** Red appears in three places only: the single primary action of a screen, the active nav underline, and a chosen filter in Chosen Red (user decision 2026-10-17: a selection must be visible at a glance). No red eyebrows, red icons or red hover states, and no red borders beyond a chosen filter. Dictum and error colours are status, and keep their own palette.

**The Clickable Rule.** A clickable element reads as clickable at rest: outline buttons carry the Control Edge and turn accent on hover, ghost buttons speak in the accent colour, and text links carry a faint accent underline (40% of the link colour, 3px offset) that turns solid on hover.

**The Navy Is Ink Rule.** Navy colours text, links, focus and thin accents. It never fills a table head, panel or section; the only navy fields are the header bar and the GEGROND/TOEWIJZING badge.

**The Semantic Token Rule.** Colour comes from the semantic tokens (`foreground`, `muted`, `accent`, `card-border`, `card-hover`, `primary`), which switch with `data-theme`. Tailwind `dark:` variants are not used: they follow the OS, not the in-app theme choice.

## Typography

**Display Font:** none; the UI has no display tier.
**Body Font:** IBM Plex Sans (with ui-sans-serif, system-ui)
**Passage Font:** Source Serif 4 (with Georgia, serif)
**Label/Mono Font:** IBM Plex Mono (with ui-monospace)
**Wordmark:** Oxanium, in the header wordmark only.

**Character:** A neutral, engineered sans for the instrument, a book serif for the law itself, and a mono for the references you cite. The serif marks the boundary between the tool and the source.

### Hierarchy
- **Wordmark** (Oxanium 800, 1.125rem, tight tracking): "Dutchplanners" in the header, with the "Legal" suffix (600, 0.75rem, uppercase, wide tracking, dp-red) as part of the lockup.
- **Headline** (600, 1.25rem): the page title on pages that carry their own h1.
- **Title** (600, 1rem): section headings, such as the result count and empty-state headings.
- **Body** (400, 0.875rem): running UI text, buttons, inputs, descriptions.
- **Data** (400, 0.8125rem on 20px lines, tabular figures): table cells and dense lists.
- **Label** (500, 0.75rem, muted): table head labels, sub-labels, chips, range and sort lines. Sentence case.
- **Passage** (Source Serif 4, 400, 0.875rem, line-height 1.375, max ~75-80ch): snippets and quoted uitspraak text; query terms marked with the highlighter at weight 500.
- **Reference** (Plex Mono, 500, 0.75rem): ECLI numbers and r.o.-numbers.

### Named Rules
**The Three Voices Rule.** Sans for the tool, serif for the source, mono for the citation. Uitspraak text is never set in sans; ECLI and r.o.-numbers are never set in serif or sans.

**The Tabular Rule.** Every number, date, count and duration uses tabular figures (`tabular-nums`) so columns align.

**The No Eyebrow Rule.** No uppercase, letter-spaced labels above headings. Labels are 0.75rem, weight 500, muted, sentence case. The wordmark's "Legal" suffix is part of the logo, not a pattern to reuse.

**The Floor Rule.** Nothing smaller than 0.75rem; no arbitrary 10px or 11px text.

## Layout

One shared frame for every route: content is centred at max 1536px (`max-w-screen-2xl`) with 16px side padding, 24px from 640px up (`PAGE_CONTAINER` in [web/src/components/layout/page-container.ts](web/src/components/layout/page-container.ts)). The header uses the same frame, so header and body share edges and switching pages never shifts the content.

The page is a single column: the navy header (48px from 640px; 44px nav targets below), then one scroll area (`<main>`) that holds input and output together. On /zoeken a toolbar line (search field, Filters, Wis alle filters, summary) sits above a full-width table; active filters wrap as chips below it; filters themselves live in a drawer.

The result table appears from 1024px (`lg`); below that the same results render as a hairline-separated list, because a cut-off table hides the key columns. The table head is sticky against `<main>`, which is why the table has no overflow wrapper.

Spacing rhythm: tight inside groups (gaps of 6-12px), generous between sections (24-32px), more space above a heading than below it. Table cells pad 12px horizontally and 8px vertically. Empty states centre with 48px of air.

## Elevation & Depth

The system is flat. In-flow content (tables, lists, sections, chips, banners) has no drop shadow; Tailwind's `shadow-xs` through `shadow-md` are reset to `none` in the theme. Depth comes from hairlines, whitespace and the Hover Wash. Two inset shadows are drawing techniques, not elevation: a 1px inset hairline under the sticky table head (a border would scroll away under `border-collapse`) and the 2px inset accent edge on a hovered or focused result row.

### Shadow Vocabulary
- **Floating layer** (`box-shadow: 0 8px 24px rgba(0,0,0,0.12)`): dialogs, popovers, dropdowns and map overlay controls, always with a 1px hairline border.
- **Drawn hairline** (`box-shadow: inset 0 -1px 0 var(--card-border)`): sticky table head cells.
- **Row edge** (`box-shadow: inset 2px 0 0 var(--accent)`): first cell of a result row (data row and snippet row) on hover and focus-within.

### Named Rules
**The Paper Rule.** In-flow content lies flat on the page. Only layers that float above the page (dialog, popover, dropdown, map control) lift, with a hairline border plus the one floating shadow.

**The Hairline Rule.** Sections are separated by a single hairline and whitespace, not boxed in cards. A coloured border wider than 1px on a card or callout is forbidden; the 2px accent row edge is the one sanctioned exception.

## Shapes

Near-square everywhere: every corner is 2px, enforced by mapping all Tailwind radius steps (`xs` through `2xl`) to 2px. Buttons, inputs, chips, badges, banners, skeleton bars, floating layers and `<mark>` all share it. Full rounding is reserved for counters, status dots, map markers and avatars. Borders are 1px hairlines; the only thicker strokes are the 2px active nav underline and the 2px row edge.

**The Two Pixel Rule.** Corners are 2px. Pills are for things you count, not things you click.

## Components

Components are refined and restrained: quiet at rest, a clear hairline or wash on hover, a navy outline on focus.

### Buttons
- **Shape:** near-square (2px); one vocabulary for buttons and links via `buttonClass(variant, size, iconOnly)` in [web/src/components/shared/button-styles.ts](web/src/components/shared/button-styles.ts).
- **Sizes:** sm 28px (inside tables and dense lists, 0.75rem text), md 32px (default), lg 36px (next to the search field). Icon-only buttons are square at the same heights and always carry an aria-label.
- **Primary:** Griffie Red fill, white text, weight 500; at most one per screen. Hover deepens to Deep Griffie Red.
- **Outline:** Paper fill, Control Edge border, Ink text; hover turns border and text accent and washes the fill; pressed fills with the hairline tone.
- **Ghost:** no fill, accent text; hover washes the fill and deepens the text to accent-hover; pressed fills with the hairline tone.
- **Focus / Disabled:** 2px accent outline at 2px offset on `focus-visible`; disabled at 45% opacity with a not-allowed cursor.

### Chips
- **Active filter chip:** 24px high, Hover Wash fill, hairline border, label type; its own remove button keeps a 24px hit area (WCAG 2.5.8).
- **Aspect chip:** 20px high, Paper fill, hairline border; clicking filters on the aspect; hover darkens the border and washes the fill. Aspects are neutral: colour is for status only.
- **Counter:** fully rounded Pale Navy pill with Ink Navy tabular figures, e.g. the active-filter count inside the Filters button.

### Dictum badges
20px, 2px corners, label type at weight 600. GEGROND and TOEWIJZING are the strong navy fill with white text; BESTUURLIJKE_LUS is Pale Navy; ONGEGROND and AFWIJZING sit on the Coverage Track with Charcoal text; NIET_ONTVANKELIJK and ONBEVOEGD are lighter still. The explanation travels in the title and in screen-reader text.

### Inputs / Fields
- **Style:** 36px, Paper fill, Field Edge border, 2px corners, leading search icon in Clerk Grey, placeholder in Clerk Grey.
- **Hover / Focus:** hover darkens the border to Stone; focus turns the border accent and adds a 2px ring at 25% accent.
- **Clear:** a ghost icon button (sm) inside the field's right edge when it has a value.

### Navigation
- **Header:** sticky (in flow, not fixed) Dossier Navy bar at 48px, z-index above map controls and below dialogs.
- **Items:** icon plus label in body type at weight 500, Muted Navy at rest, white on hover. The active item is white with a 2px House Red underline, the only colour in the bar. Focus is a white outline drawn inside.
- **Mobile:** nav wraps to its own row under the wordmark with short labels and 44px targets.

### Result table
- **Head:** Paper background, label type in Clerk Grey, sticky, a drawn hairline below; sortable heads are buttons with a chevron that appears on hover and turns Ink when active.
- **Rows:** each uitspraak is its own `<tbody>`: data row plus snippet row share one bottom hairline and one hover state (Hover Wash plus the 2px accent row edge).
- **Cells:** data type, ECLI as a mono accent link, dates and counts tabular, empty values as a muted em dash with screen-reader text.
- **Ghost row actions:** icon actions (rechtspraak.nl) are hidden until row hover or focus, and always visible on devices without hover.
- **States:** a table-shaped skeleton with 2px bars (pulse off under reduced motion); an error banner with `role="alert"` and *Opnieuw proberen*; an empty state with a next step (*Wis alle filters*).

### r.o.-marge (signature)
The snippet row starts with a 72px right-aligned margin in Plex Mono, 0.75rem, Clerk Grey, holding "r.o. 4.2" (screen readers hear "Rechtsoverweging"). Beside it the passage runs in Source Serif 4 in Charcoal, clamped to two lines and at most 80ch, with query terms on the Highlighter. Wherever a rechtsoverweging is quoted (snippets, the uitspraakpagina, PDF references), its number sits in this margin.

### Dekkingsstreep (signature)
A 4px by 56px bar on the Coverage Track, filled from the left in the accent colour, square-ended. It replaces a bare score: relevance relative to the best hit on the page, or in rapportmodus the shared aspects with a tabular value beside it ("18/52"). The full meaning is in the title and screen-reader text.

### Motion
State changes (colour, border, background, opacity, shadow) transition at 150ms ease; all transitions drop to 0ms under `prefers-reduced-motion`. No hover lifts or translations; any transform or animation carries a reduced-motion guard.

## Do's and Don'ts

### Do:
- **Do** use `buttonClass` for every button and button-like link, with at most one primary per screen.
- **Do** wrap every page body in `PAGE_CONTAINER` so it aligns with the header.
- **Do** separate sections with a single hairline (`border-card-border`) and 24-32px of whitespace.
- **Do** set uitspraak text in Source Serif 4 and put r.o.-numbers in the mono r.o.-marge beside it.
- **Do** show relevance or overlap as a dekkingsstreep, with the exact value in the title and screen-reader text.
- **Do** use tabular figures for every number, date and count, and mono for ECLI.
- **Do** give every interactive element the 2px accent `focus-visible` outline at 2px offset, and keep hit areas at least 24px.
- **Do** give floating layers a hairline border plus `0 8px 24px rgba(0,0,0,0.12)`.

### Don't:
- **Don't** use red anywhere but the one primary action, the active nav underline and a chosen filter.
- **Don't** fill table heads, panels or sections with navy.
- **Don't** put drop shadows on in-flow content or box sections in shadowed cards.
- **Don't** use coloured borders wider than 1px on cards or callouts.
- **Don't** use corners other than 2px, or pill shapes for buttons, chips and badges.
- **Don't** put uppercase, letter-spaced eyebrows above headings, or use Oxanium outside the wordmark.
- **Don't** use text smaller than 0.75rem.
- **Don't** use Tailwind `dark:` variants; use the semantic tokens that follow `data-theme`.
- **Don't** add hover lifts or transforms without a reduced-motion guard.
