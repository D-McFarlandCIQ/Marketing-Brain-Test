---
title: Product overview
owner: pmm
status: draft            # MOps first pass from sales and messaging decks; needs PMM + Product review
last_reviewed: 2026-10-22
review_every: 90d
source: "Internal Unified Product Roadmap + EPD Releases tracker (GA status and themes only, read 2026-10-22); 2025_SPM_Narrative First Call Deck (mod 2026-10-13); Messaging Framework V6 (WIP); Partner Listing Boilerplate (Oct 2026); Oct. Agents Launch Campaign Strategy Brief (mod 2026-10-21); Catalyst Pitch and Talk Track (Dec 2025)"
---

# Product overview

CaptivateIQ is a sales performance management (SPM) platform. It runs **incentive
compensation** and **sales planning** on one live calculation layer, **SmartGrid**, with
predictive modeling (**Catalyst**) and **AI agents** on top. **Financial Planning
(EPM)** is the next product line.

> **The portfolio story is still open.** The PMM Resource Directory notes it's undecided
> whether to tell a *platform* or a *portfolio* story (approver: Conway, CEO). The
> working view: a portfolio can graduate to a platform, but not the reverse. V6
> messaging tells one connected-platform story. Don't pitch the products as separate
> tools.

## How the pieces fit

```text
            ┌─────────────────────────── Agents ───────────────────────────┐
            │  Comp Builder (GA)   Rev Planning (GA)   Comp Ops (beta)      │
            ├──────────────── Catalyst (predictive models) ────────────────┤
            │      Planning                      Incentives                │
            │  capacity · quota ·         commissions · bonuses ·          │
            │  territory & accounts       ASC 606 · rep statements         │
            ├──────────────────────── SmartGrid ───────────────────────────┤
            │   live calculation layer: data connectors → models → payouts  │
            └──────────────────────────────────────────────────────────────┘
                 Integrations: CRM (Salesforce), HRIS (Workday), ERP, more
```

The V6 flywheel describes the same platform as a cycle: **Plan → Pay → Monitor → Adapt**
(see [positioning/messaging-framework.md](../positioning/messaging-framework.md#growth-flywheel-plan--pay--monitor--adapt)).

## Product lines

| Product | What it does | PMM point person | Detail |
| --- | --- | --- | --- |
| **Incentives** (ICM) | Calculates and pays commissions and bonuses; rep statements; reporting; ASC 606 | Chelsea McClure (ICM) | [capabilities/incentives.md](capabilities/incentives.md) |
| **Planning** (Sales Planning) | Capacity planning, quota setting, territory and account carving | John Houston | [capabilities/planning.md](capabilities/planning.md) |
| **SmartGrid** | The live modeling and calculation layer under everything | — | [capabilities/smartgrid.md](capabilities/smartgrid.md) |
| **Catalyst** | Modeling workspace for forecasting, payout checks, scenarios, predictive ML | John Houston | [capabilities/catalyst.md](capabilities/catalyst.md) |
| **Agents** | AI agents that build, explain, and change plans with admin approval | John Houston | [capabilities/agents.md](capabilities/agents.md) |
| **Financial Planning** (EPM) | Forecasting, planning, and budgeting for the CFO | Ben (PMM) | **Not released and not announced.** The V6 brief says it soft-launched in Aug 2026, but the release tracker shows it unreleased as of 2026-10-22. Don't mention it externally until it's announced. |

PMM point people come from the PMM Resource Directory and the Notion PMM hub. Confirm
coverage with the PMM team charter (Vijay).

## Names

Brand spellings are in [brand/word-list.md](../brand/word-list.md): **CIQ Incentives,
CIQ Planning, CIQ Catalyst, CIQ Agents, SmartGrid**. Older names you'll still see in
sources: "Sales Planning Module", "Planning module", "SmartGRID", "SmartGrid ELT",
"SmartGrid modeling engine", "Assist AI" / "AI Assist", "AI Admin Co-Pilot", "AI Payee
Coach", "AI Plan Advisor". Ask PMM which older AI feature names survive the Agents launch.

## Gaps

- **Product overview and capability map** (PMM + Product) is listed in the directory
  with no doc. This file is assembled from sales decks, so verify features against
  Product before external use.
- No ICM-only one-pager (the PMM hub marks it as a gap).
- The internal roadmap is Product-owned and confidential. This repo uses it only to
  check what is **GA today**. Planned features and target dates are deliberately left out.

## Where the platform is heading (themes only)

From the internal roadmap, at a level that's safe to reflect in messaging. These are
directions, not commitments; don't attach dates or feature names to them externally.

- **Agents across every product**, all on the same governed data.
- **One platform:** planning and incentives converging on a shared modeling foundation,
  which supports V6's "one live system" story.
- **Enterprise governance** as table stakes: approvals, access controls, audit, security.
- **Easier data onboarding:** more self-service connectors and bigger data volumes.
- **Payee experience:** mobile, plan documents, statements, notifications.
- **A new admin UI** (internal codename Eclipse; the brand manual shows "CIQ Eclipse" in
  product video examples). It's in beta, so don't name it externally.

The roadmap also tags customer value with six outcomes: compliance, operational scale,
revenue performance, cost reduction, forecast accuracy, and seller experience. Those are
a useful cross-check for the V6 pillars.
