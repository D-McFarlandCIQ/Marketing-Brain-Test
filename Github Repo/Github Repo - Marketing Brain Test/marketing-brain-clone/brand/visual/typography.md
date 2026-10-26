---
title: Typography
owner: brand
status: draft            # MOps first pass; needs Brand sign-off
last_reviewed: 2026-10-06
review_every: 90d
source: "CIQ Brand Manual & Style Guide 2.0, CIQ Typography (pp. 94–103)"
---

# Typography

Three families: a modern sans for headlines (**Neue Haas Grotesk Pro**), a classic
serif accent (**IvyPresto Headline**), and a neutral workhorse for body text
(**Fakt**). Pairing a humanist sans with a classic serif is what makes CIQ type
distinctive.

## Licensed brand fonts (brand team, website, marketing materials)

| Family | Role | Licensed weights |
| --- | --- | --- |
| **Neue Haas Grotesk Pro** | Headlines, subheads | 35 Extra Light, 36 Extra Light Italic, 55 Roman, 56 Italic |
| **IvyPresto Headline** | Accent words in headlines, quotes, large callouts | Thin, Thin Italic, Light, Light Italic |
| **Fakt** | Body copy, sub-headers, charts | Whole family licensed. Use Light, Normal, Medium, and Semibold, each with its italic |

These fonts are **licensed only to brand-team design seats and to the website and
marketing materials.** Ask the brand team about licenses case by case.

## Free alternates (everyone else, and Google Slides)

Use these for company materials made outside Brand and Marketing, such as the company
Google Slides template:

| Use | Font | Source |
| --- | --- | --- |
| Headlines and subheaders | **Public Sans** | Google Fonts |
| Headlines, subheaders, and quotes (serif accent) | **Newsreader** | Google Fonts |
| Body | **Public Sans**, or **Manrope** | Google Fonts |

**Manrope is a legacy brand typeface and is being phased out** because it has no
italics. Prefer Public Sans for body text in new work.

## Type hierarchy (p. 99)

| Level | Print | Web | Typeface |
| --- | --- | --- | --- |
| Extra-large header | Extra-large headline | **H1** | Neue Haas Grotesk Pro **Extra Light** + IvyPresto Headline **Thin Italic** |
| Large header | Large headline | **H2** | Neue Haas Grotesk Pro **Roman** + IvyPresto Headline **Light Italic** |
| Medium header | Medium headline | **H3** | Neue Haas Grotesk Pro **Roman** |
| Sub-header | Sub-header | **H4** | **Fakt Medium** |
| Body | Body | Body | **Fakt Regular** |

- **When in doubt, use Fakt Regular** and create contrast with size, not weight or
  color.
- Use **Fakt Medium or Semibold** sparingly, for sub-headers and highlights.
- **The serif-italic accent:** in H1 and H2, set an emphasis phrase in IvyPresto
  italic inside a Neue Haas Grotesk headline. The homepage's "*A Leader in* Sales
  Performance Management" is an example.
- Other combinations are possible, but share them with the brand team for approval.

## Type color

- Sans headlines and body: **Almost Black** `#0C1728`, or **White** on dark
  backgrounds.
- Serif headlines: **Taupe 4** `#585858`.
- Brand colors (Lagoon, Violet, Hedge) are for small moments of emphasis only. See
  [color.md](color.md#type-color-pp-5253).

## Fallback stacks for HTML and email

MOps suggestions. The manual doesn't specify web stacks.

```css
--font-display: "Neue Haas Grotesk Display Pro", "Public Sans", "Helvetica Neue", Arial, sans-serif;
--font-serif:   "IvyPresto Headline", "Newsreader", Georgia, serif;
--font-body:    "Fakt", "Public Sans", "Helvetica Neue", Arial, sans-serif;
```

In email, assume none of the brand fonts load. Design so the Arial or Georgia
fallback still looks right.

## Open questions for Brand

1. **The intro (p. 94)** names the three families but not Manrope, yet the product
   lockups use Manrope Light ([logo.md](logo.md)). Will lockups move off Manrope?
2. **Display versus Text cut.** captivateiq.com loads "Neue Haas Grotesk *Display* Pro"
   at weight 200, while the manual names "Neue Haas Grotesk Pro" 35 Extra Light. Are
   these the same licensed cut?
3. **Legacy web fonts.** The site still loads Akkurat and Poppins. Are they retired?
