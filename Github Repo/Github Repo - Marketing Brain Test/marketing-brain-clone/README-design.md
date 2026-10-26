# Design team review: brand content in the marketing brain

**For:** CIQ Brand and Design (Jarrod, Ola, and anyone they loop in)
**From:** Marketing Ops (Darrell Wu), drafted with Claude
**Status:** asking for review · **Date:** 2026-10-22

## What this is and why it matters

This repo is a shared "brain" that marketing teammates and their AI assistants read
before they write or design anything. We turned the **CIQ Brand Manual & Style Guide
2.0 (Sept 2026)** into short markdown files in [`brand/`](brand/), plus a skill,
[`skills/apply-brand/`](skills/apply-brand/SKILL.md), that checks an HTML email,
dashboard, or draft against those files and fixes what it can.

Once this ships, **assistants will follow these files literally.** If a value or rule
is wrong here, it will be wrong in every asset an assistant produces, at scale. So we
need your eyes on three kinds of content:

1. **Where the manual was ambiguous or had errors,** and we had to choose (§2, §3).
2. **What we wrote ourselves** because the manual didn't cover it (§4).
3. **What the skill enforces** on your behalf (§5).

Everything under `brand/` ships as `status: draft`. Assistants tell readers it's a
draft until you sign off.

### If you have 15 minutes

Answer the **8 decisions in §1**. Those change what assistants produce today. The rest
can follow.

### How to give feedback

Comment inline on the PR, or reply in Slack with the item number (for example
"§3.4: use 663 C"). Each item links to the file it changes. You don't need git. We'll
make the edits.

---

## 1. Decisions we need first

These shape most of what assistants will make. Our current assumption is in
**bold**. Tell us if it's wrong.

| # | Question | What we assumed for now | Where |
| --- | --- | --- | --- |
| 1.1 | **Internal HTML dashboards:** brand palette or Quotient product colors? Dashboards look like product UI, but the manual says Quotient colors are product-only, and we don't have Quotient values. | **Use the brand palette, light theme, on a Taupe 1 or white base.** | [SKILL.md → dashboards](skills/apply-brand/SKILL.md) |
| 1.2 | **Chart colors fail contrast on white.** Most step-2 colors are under the 3:1 WCAG minimum for non-text elements on white: Hedge 2 1.35:1, Lagoon 2 2.0:1, Violet 2 2.4:1, Citrus 2 1.1:1. Only Violet 3 (5.3:1), Lagoon 3 (4.2:1), and Cirrus 4 (3.1:1) pass. Can you give us an approved, accessible chart series order? | **No fixed order.** The skill flags low-contrast fills as a "fix". | [visual/imagery.md → Charts](brand/visual/imagery.md) |
| 1.3 | **Button corner radius:** the site's CTA uses 14px, but the manual's rounding system is 4 / 8 / 16 / 24px. Which is the standard for marketing buttons and cards? | **Flag 14px as an open question.** Recommend 8px or 16px. | [visual/color.md Q8](brand/visual/color.md#open-questions-for-brand) |
| 1.4 | **Primary CTA spec:** Hedge 2 `#B5EF71` background with Almost Black text. This comes from the live site, not the manual. Is it the approved CTA? | **Yes. Used in email and HTML.** | [visual-identity.md](brand/visual-identity.md) |
| 1.5 | **HTML email:** clients drop blur, gradients, and web fonts. Is a flat light base (Taupe 1, Cirrus 1, or 50% tints) plus a pre-rendered gradient image an acceptable on-brand email? | **Yes. Flat bases, with fonts falling back to Arial and Georgia.** | [SKILL.md → HTML email](skills/apply-brand/SKILL.md) |
| 1.6 | **Body font:** the manual says **Fakt** is body and **Manrope is legacy**. Our earlier draft, based on the live site, had Manrope as body. Is the site migrating to Fakt? | **The manual wins. Fakt body, with Public Sans as the free alternate.** | [visual/typography.md](brand/visual/typography.md) |
| 1.7 | **Product lockups use Manrope Light,** the typeface being phased out. Will lockups change? | **Lockups unchanged.** Assistants never rebuild them anyway. | [visual/logo.md Q3](brand/visual/logo.md#open-questions-for-brand) |
| 1.8 | **Source of truth.** When the PDF, the Notion Brand Portal, and this repo disagree, which wins? And who reviews changes to `brand/`? | **The PDF wins.** Brand is listed as owner of `brand/` in [OWNERS.md](OWNERS.md). | [brand/README.md](brand/README.md) |

---

## 2. Assumptions we made where the manual was unclear

Please confirm or correct each one.

| # | Ambiguity | What we did | Where |
| --- | --- | --- | --- |
| 2.1 | P. 50 labels Hedge's Dark swatch `#074F37` "Hedge 4", and Citrus Dark `#C64444` "Citrus 4". | **Treated both as the "Dark" swatch,** as p. 49 labels them. The real Hedge 4 is `#338B4E` and the real Citrus 4 is `#FF6969`. | [visual/color.md](brand/visual/color.md#open-questions-for-brand) |
| 2.2 | P. 50 labels the Cirrus tints "Tint of Lagoon 1". | **Followed p. 49,** which says "Tint of Cirrus 1". | same |
| 2.3 | The RGB values disagree with the hex for Lagoon 3 and Citrus 1. | **Treated hex as authoritative** everywhere. | same |
| 2.4 | The text on the Agents pattern page (p. 90) maps green to Catalyst and orange to Incentives. The palettes say the opposite. | **Followed the palettes:** Incentives is green, Catalyst is orange (Apricot). | [visual/product-palettes.md](brand/visual/product-palettes.md#open-questions-for-brand) |
| 2.5 | The p. 32 "expressive" wordmark swatch is visibly violet but labeled `#0A2028`. | **Listed it as "Violet (unconfirmed)".** We assume Violet 3 `#7F3BFF`. | [visual/logo.md Q2](brand/visual/logo.md#open-questions-for-brand) |
| 2.6 | Wordmark pairings use near-palette values (`#B6F071`, `#A7D841`, `#E8F3FC`, `#C0FFA1`, `#E5E3E1`). | **Kept them as listed** for wordmark use only. We didn't add them to the tokens, so the checker flags them anywhere else. | same, Q1 |
| 2.7 | Layering examples use one-digit-off values (`#9967FF`, `#F5FFCC`, `#E5FF0C`, `#F6D0BC`). | **Treated them as typos** of `#9867FF`, `#F6FFCD`, `#E6FF0C`, and `#F7D1BD`. | [visual/color.md Q6](brand/visual/color.md#open-questions-for-brand) |
| 2.8 | Berry 3.5 `#DD88CD` (Planning) doesn't match the full-spectrum Berry bridge `#E891DB`. | **Kept both:** `#DD88CD` for Planning only. | [visual/product-palettes.md](brand/visual/product-palettes.md#open-questions-for-brand) |
| 2.9 | The Brand Star "in tension with" pairs appear only in the diagrams. | **Read them from the star's arrows,** for example Confident in tension with Unorthodox and Approachable. | [foundations.md](brand/foundations.md#personality-the-brand-star-pp-1220) |
| 2.10 | The equalizer on p. 20 shows bar heights with no legend. | **Read it as a 4-step scale** (Unorthodox 4, Grounded 3, Empowering 2, Confident 2, Approachable 1) and labeled it an illustration, not a default mix. | same |
| 2.11 | Vision, Mission, and Promise are marked "work in progress", with 2024 versions shown. | **Included the 2024 lines as reference only.** Assistants are told not to present them as current. | [foundations.md](brand/foundations.md#vision-mission-promise-pp-810) |
| 2.12 | "Neue Haas Grotesk Pro" (manual) vs. "Neue Haas Grotesk **Display** Pro" at weight 200 (live site). | **Assumed they're the same licensed cut.** | [visual/typography.md Q2](brand/visual/typography.md#open-questions-for-brand) |

---

## 3. Errata to fix in the manual itself

These are probable errors in the PDF. They're worth fixing at the source so the next
version agrees with this repo.

1. **Accessibility page (p. 59):** white on Violet 3 `#7F3BFF` is labeled WCAG AAA but
   measures **5.3:1**, which is AA and only AAA for large text. All other pairs on the
   page pass AAA.
2. **Pantone duplicates (p. 50):** Berry 1 and Taupe 1 are both **663 C**. Citrus 1 and
   Berry 2 are both **475 C**. Please don't send these to a printer until corrected.
3. **RGB typos (p. 50):** Lagoon 3 lists Hedge 2's RGB (182/240/113). Citrus 1 lists
   250/232/222.
4. **Copy-paste captions:** the Incentives pattern (p. 66) begins "To represent CIQ
   Planning…", and the Catalyst palette (p. 81) is captioned "Planning gradient
   spectrum".
5. **The Agents pattern description (p. 90)** swaps the Incentives and Catalyst colors
   (see 2.4).
6. **Catalyst example (p. 83):** one base is malformed (`F9F9F8 7`), and another pairs
   the Apricot Dark base with Hedge green layers.
7. **The duplicate "Hedge 4" and "Citrus 4" labels** and the Cirrus tint label (see
   2.1–2.2).
8. **The violet wordmark swatch label** (see 2.5).
9. **Minor:** "Brant team" (p. 134), "anthing" (p. 60), and a showcase page still
   marked "VERSION 1.75 … pg X" (p. 170).

---

## 4. Content we wrote that isn't in the manual

The manual didn't cover these, but assistants need them. They're marked in the files
as MOps-authored. Please approve, edit, or strike each one.

| # | What | Why we added it | Where |
| --- | --- | --- | --- |
| 4.1 | **Tone by situation** (social, thought leadership, support, sales, product UI → which traits to turn up or down) | The manual says to adjust tone but gives no table, so assistants need a starting point. | [voice-and-tone.md](brand/voice-and-tone.md#dialing-tone-by-situation) |
| 4.2 | **"In writing, that looks like…"** for each personality trait | It translates trait definitions into writing behavior. | [voice-and-tone.md](brand/voice-and-tone.md#the-voice) |
| 4.3 | **Web and email font fallback stacks** (`Neue Haas → Public Sans → Helvetica Neue → Arial`, and so on) | The manual names fonts but not CSS stacks. | [visual/typography.md](brand/visual/typography.md#fallback-stacks-for-html-and-email) |
| 4.4 | **Machine-readable color tokens,** including every bridge and legacy color plus product gradients | Lets the skill validate hex values automatically. Please spot-check against the Figma variables. | [visual/color-tokens.yaml](brand/visual/color-tokens.yaml) |
| 4.5 | **"The ten rules"** summary | A one-screen digest for quick work. It's our compression of the manual, so check that the emphasis is right. | [visual-identity.md](brand/visual-identity.md#the-ten-rules) |
| 4.6 | **Name rules:** don't write "Captivate IQ", "CaptivateIq", or "Captivate". Keep "Quotient", "Calcy", and "IQ Bug" out of customer copy. | Common errors, inferred from how the manual uses the names. | [word-list.md](brand/word-list.md) |
| 4.7 | **Email build rules:** no blur or gradients, a bulletproof Hedge 2 button, the logo as an image ≥116px wide, a dark-mode check | Email realities the manual doesn't address. | [SKILL.md → HTML email](skills/apply-brand/SKILL.md) |

### Deliberately left out

- **`examples.md` (before and after rewrites).** This is the fastest way to teach an
  assistant the voice, but we didn't want to invent examples you haven't approved.
  **Could Brand or Content give us 5–10 real before/after pairs?**
- **A use / avoid / never-say word list.** The manual only gives general guidance.
- **Writing mechanics the manual doesn't set:** headline case (sentence or title),
  numbers and percentages, dates and time zones, em-dash spacing, abbreviations on
  first use. Assistants currently "follow house practice and flag", which means
  inconsistent output.
- **Quotient product colors,** which we don't have (see 1.1).

### Terms to confirm (with PMM)

"CIQ Eclipse" (appears only in showcase videos), "BPM" (p. 145, undefined), and
whether running text should say "CIQ Incentives" or "CaptivateIQ Incentives".

---

## 5. What the `apply-brand` skill enforces for you

The skill reviews an asset and sorts findings into three levels. Please check that the
levels match how you'd judge.

| Severity | Triggers |
| --- | --- |
| **Blocking** | Logo misuse (live text instead of the file, recoloring, below minimum size, smaller than a partner logo), text contrast under 4.5:1, an off-brand company description, real customer data, unapproved claims or stats |
| **Fix** | Off-palette color, wrong font, text in an accent color, name or mechanics errors, a corner radius outside 4/8/16/24 |
| **Suggestion** | Color proportion, layering, white space, tone |

**Guardrails:**

- **It never publishes or sends anything.** It writes a corrected copy beside the
  original.
- It never invents colors, fonts, taglines, or logo variants.
- It warns that product pillar palettes need Brand approval.
- It hands **photography quality, logo-file authenticity, and claims** to a human.

**Known limits worth knowing:**

- **Questionable nearest-color suggestions.** The color checker suggests the nearest
  token, which can be a legacy or bridge shade (marked "use sparingly") instead of a
  core color. For example, it suggested legacy `#A6D741` instead of Hedge 2 for a
  lime green. We plan to prefer core steps.
- **Taste calls are judgment.** Layering, blur, and how a composition *feels* are left
  to the model's judgment, and those findings are only "suggestions".
- **The shareable build is a snapshot.** `skills/apply-brand/build_standalone.py` makes
  a zip of the skill plus a copy of `brand/` for people outside the repo. **When you
  change `brand/`, someone has to rebuild and redistribute the zip.**

---

## 6. Housekeeping

- **The manual PDF isn't in git.** At 126 MB it's over GitHub's file limit, so the
  files cite its page numbers and point to the copy in the Notion Brand Portal
  (Notion → General → Brand).
- **Contacts in [brand/resources.md](brand/resources.md)** list names and roles from
  p. 208, and point to the manual for email addresses. Is that the right level of
  detail?
- **Review cadence:** each file says `review_every: 90d`. Does that match your
  release rhythm for the manual?

Thank you. Even a partial pass on §1 lets us start a small pilot with confidence.
