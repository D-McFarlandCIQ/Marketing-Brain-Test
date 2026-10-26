# PMM review: what we need from you

**For:** the CaptivateIQ Product Marketing team · **From:** Marketing Ops (Darrell Wu) ·
**Date:** 2026-10-22

We've done a first pass at the PMM-owned parts of the marketing brain: `product/`,
`positioning/`, and `library/`. The marketing brain is the shared folder that teammates'
AI assistants read before drafting copy, building decks, or answering "what do we say
about X?". Whatever these files say is what those assistants will repeat. Each file is
marked `status: draft` until a PMM owner signs off.

Sources for this pass:
- the PMM Resource Directory sheet and the docs it links to
- the PMM Notion hub and the win/loss pages
- the internal product roadmap and release tracker, used only to check what's GA
- captivateiq.com and the public press releases

**Start here:**
- [positioning/README.md](positioning/README.md): maps every row of the Resource
  Directory to a file here, or marks it missing.
- [library/public-links.md](library/public-links.md): every public asset with a verified
  link, safe to send externally.

## Decisions only PMM can make

These block other work. Each one changes what the assistant tells people.

| # | Decision | Why it matters | Where |
| --- | --- | --- | --- |
| 1 | **Which messaging framework is current?** V6 ("one live system for growth") is marked NOT FINAL, but its language already shipped in the Oct 2026 partner boilerplate, and the first-call deck still uses FY27 ("planning and incentives in sync"). | We default to V6 and list the FY27 phrases it retires ("AI-infused", agility-led). Confirm or correct. | [messaging-framework.md](positioning/messaging-framework.md) |
| 2 | **Customer count:** 800+ or 1,000+? | Both are in live assets. | [proof-points.md](positioning/proof-points.md) |
| 3 | **Comp Builder GA status.** We announced it GA on Oct 21, but on Oct 22 the release tracker still showed it in Beta. Rev Planning's "tells you before you ask" proactive layer is also still Beta. | Sales will claim what the press release says. Product should flip the stage, or we soften the claim. | [agents.md](product/capabilities/agents.md) |
| 4 | **Comp Ops agent and MCP Server** appear in V6 copy and the flywheel, and there's a public "Meet the Comp Ops Agent" webinar page. Both are pre-GA (beta and alpha). | Risk of over-claiming. We've told the assistant not to claim either as available. | [agents.md](product/capabilities/agents.md) |
| 5 | **EPM / Financial Planning.** The V6 brief says it soft-launched in Aug 2026; the release tracker says it hasn't been released. | We've told the assistant to keep EPM out of external copy until it's announced. Confirm, and say who owns EPM positioning. | [overview.md](product/overview.md) |
| 6 | **Platform or portfolio story?** Still open per the directory (approver: Conway). | Decides how product pages and the deck are structured. | [overview.md](product/overview.md) |
| 7 | **SmartGrid vocabulary.** It's an open item in V6, and exec feedback says it's becoming a blanket word. | We use "unified modeling workspace" until you decide. | [smartgrid.md](product/capabilities/smartgrid.md) |
| 8 | **Gated content: should sellers send direct PDF links?** Most /resources pages are gated, but the PDF links sit in the page source and open without the form. | Direct links skip HubSpot attribution. The link index uses landing pages only. Say if you want direct links for analyst reprints or case-study PDFs. | [public-links.md](library/public-links.md) |

## Claims that need sign-off before anyone reuses them

- **Nothing in [proof-points.md](positioning/proof-points.md) is approved.** The
  directory row "Approved stats, claims & proof points" has no doc behind it. Please
  mark each row `approved`, fix it, or kill it.
- **Unsourced deck stats:** "90% reduction in incentives errors", "10% increase in
  seller attainment", "6X faster plan changes" (in three wordings), ">150K sellers".
  The FY27 framework's own proof section is marked [TO BE UPDATED].
- **"91% are adjusting incentive strategy, only 12% can change a plan in under two
  weeks"** is in the Agents brief with no source. It might come from the 2026 State of
  ICM report. Please confirm.
- **The research stat cited in the directory** ("46% adjust comp plans quarterly; 39%
  take 1–2 months") isn't in the 2025 tracker. Which wave is it from?
- **Stale claims still in compete assets:** "80+ features last year", "8 trillion
  calculations a month", "7,000+ plans", "Cut comp processing time by 50%+" (Xactly
  outreach play). These need a date and source, or retirement.
- **The safest stats to use today** are the public case-study headlines (Gong 60x,
  Intercom 30% fewer inquiries, and so on). They're already on our site.

## Content that's out of date or missing

| Area | Issue |
| --- | --- |
| Personas | The 2026 GTM Personas deck isn't shared with the assistant's Drive account, so there are **no persona files yet**. Share it or export it. |
| Value framework | Value Framework Slides aren't shared either. There's no value map. |
| Agents keynote and the Project Neutron deck | Not shared. The Agents content comes from the campaign brief and press release instead. |
| Battlecards | The current cards live in Aligned (teamaligned.com), which the assistant can't read. The competitor files use the Aug 2026 compete slides, Forrester, win/loss notes, and 2022–23 Notion cards (marked stale). The Agents GA, EPM, and Spiff battlecard refreshes are open Notion tasks. |
| Forrester narrative | Forrester's Q1 2025 weaknesses (no mobile app, weak controls and compliance) are **fixed**: the payee mobile app went GA in Feb 2026, and audit logs to SIEM, access controls, approval routing, and 2FA all shipped. Use this in the next briefing and in competitive responses. |
| Research | The **2026 State of ICM** report is public and supersedes the 2025 tracker the directory links to. That 2025 tracker is a vendor draft with an empty executive summary. |
| Workday | The native integration went GA in July 2026 and the partner boilerplate drafts a Marketplace listing, but **no CaptivateIQ listing is live**, while Xactly and Varicent are listed. |
| Case studies | There's no Agents case study yet. ClickUp has a testimonial only and Vercel a logo only. Enterprise proof is thin; we lost CBRE in 2025 partly on F500 logos and scale. |
| Win/loss | Interview notes in Notion stop at Feb 2025, although the process runs weekly. |
| Launch process | Launch Framework 2.0 is from Oct 2024. Is there a newer one? The directory asks whether a release process exists. |
| Web | The Oct 21 Agents webinar page still reads as upcoming. There's no newsroom or press kit on captivateiq.com. |
| Missing docs | No source doc exists for: ICP and segments, enterprise buying committee, legacy displacement narrative, competitor pricing intel, packaging, demo script, ROI/business case kit, public roadmap narrative, reference customer list. |

## Governance flags

- **Personal Gmail ownership.** Several core PMM docs are owned by a personal Gmail
  account (ben.thiefels@gmail.com) rather than a company account: Messaging Framework V6,
  the Partner Listing Boilerplate, the upsell framework, the CSM cheat sheet, and the
  pre-call guide. Please transfer them to a captivateiq.com owner or a shared drive.
- **Forrester copy.** The Forrester PDF linked from the directory and the Notion hub is a
  personal analyst copy marked "Distribution and reproduction are prohibited". Link to
  the public landing page instead.
- **Battlecards are internal only.** Per Legal's competitive intel guidelines (Feb 2025),
  written battlecards are never shared outside the company. The competitor files say so
  at the top.
- **How the roadmap is handled.** We read the internal roadmap to check what's GA. The
  repo records shipped features and broad themes only. Target dates, planned features,
  and slipped items are deliberately left out, because these files feed assistants that
  draft customer-facing copy. If PMM wants a fuller internal roadmap summary, it needs an
  explicit confidential home and Product's agreement. Two things for Product: the
  roadmap's status field is stale on many rows, and "Payee AI agents" were made
  available to sell (Nov 2025) before they reached alpha.

## Suggested order of review

1. **Decisions 1–5 above.** They change what the assistant says this week.
2. **[proof-points.md](positioning/proof-points.md)**: approve or kill each row.
3. **Share the four unreadable decks** (Personas, Value Framework, Agents keynote,
   Project Neutron) and the Aligned battlecards, so we can run a second pass.
4. **File owners:** add a named owner to each file's frontmatter. Then review your files
   and change `status: draft` to `status: approved`.

## How to give feedback

Comment on the files directly (PR review), or reply in the thread with the file and the
fix. Corrections go into the knowledge files, not into prompts, so every teammate's
assistant gets the fix at once.
