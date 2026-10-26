---
title: Agents
owner: pmm
status: draft            # Availability checked against the internal release tracker 2026-10-22; needs PMM + Product sign-off
last_reviewed: 2026-10-22
review_every: 30d
source: "Oct. Agents Launch Campaign Strategy Brief (mod 2026-10-21); PR Newswire release 'CaptivateIQ Brings Trusted AI Agents to Incentive and Sales Planning' (2026-10-21); PR Newswire 'CaptivateIQ Launches CaptivateIQ Agents' (2026-05-14); captivateiq.com/ai-agents; internal Unified Product Roadmap + EPD Releases tracker (read 2026-10-22). Not read: Conway Launch Day Keynote; Agents Click-to-Accept Addendum."
---

# Agents

AI agents that build, explain, and change comp and planning logic on the customer's own
data, with an admin approving every change. Announced at Captivate 2026 (May 14, limited
beta) and **launched GA on October 21, 2026** (press release and
[captivateiq.com/ai-agents](https://www.captivateiq.com/ai-agents)).

## What's available

The public status is what we've announced. The internal status is the EPD release
tracker as of 2026-10-22. Where they differ, use the public status in copy and check
with Product before anything contractual.

| Agent | Public status | Internal tracker | What it does |
| --- | --- | --- | --- |
| **Comp Builder** | GA (Oct 21, 2026) | Beta. The GA date is set to 10/21 but the stage hadn't been flipped. | "You describe intent, the agent builds, and it shows you what moves before it moves." Explains formulas, debugs calculations, builds new logic from plain language. |
| **Rev Planning** | GA (Oct 21, 2026); the Sept 2026 "What's New" blog also lists it | MVP+ GA Sep 9, 2026. **Proactive Intelligence** (flags gaps before you ask) is still Beta. | Flags unassigned accounts, quota gaps, and coverage problems, models the change, and builds it when you approve. |
| **Catalyst Forecasting** | Not called out in launch messaging | GA Jun 10, 2026 | Forecasting inside Catalyst. See [catalyst.md](catalyst.md). |
| **Comp Ops** (rep inquiries) | **Not GA.** But a public "Meet the Comp Ops Agent" webinar page exists. | Beta | Drafts answers to rep pay questions; payout prep and QA. Launch brief: "behind on accuracy and should be excluded from GA claims." |
| **MCP Server** | Announced May 14, 2026 | Alpha | Connect your own AI tools to CaptivateIQ data. |
| Account Dealer, territory geo-carving, payee-facing agents | Not announced | Alpha or not released | — |

> **Rules for copy:**
> - Say **Comp Builder and Rev Planning are GA**, because that's what we announced. Don't
>   claim Rev Planning's proactive "tells you before you ask" behavior as GA until
>   Product flips it.
> - **Don't claim Comp Ops or the MCP Server as available.** V6 messaging and its
>   flywheel mention both, so cut them or mark them "coming soon" with PMM approval.
> - Don't put roadmap dates in customer-facing material.

## Message

- Value prop: "Make the change your strategy calls for, without a consultant and
  without breaking what's underneath."
  - See how your own plans work, traced to source, in plain English.
  - Make the change yourself: the agent writes the logic, shows it, and waits for approval.
  - Coverage and comp move together: one change updates both.
- Public headline: "Planning and incentives agents that simply work."
- POV: every SPM vendor announced an agent this year and shipped a demo, while comp
  admins kept pasting plan logic into ChatGPT. Ours run on live, governed data with
  humans in the loop.
- Keynote lines: "You orchestrate. Agents execute." · "Your logic. Your rules." ·
  "Nothing gets the GA label until it works on your data and is trustworthy." ·
  "Two are GA today, more on the way."
- Creative direction: real AI solving real problems, no hype, no sci-fi robots.

## Governance

Enterprise buyers ask for these. The launch brief states them as **buyer requirements,
not confirmed product facts**, so check each against the Agents addendum before
claiming it: data stays isolated; customer data never trains a shared model; every
agent action records the approving admin; nothing reaches production without approval;
we disclose which model runs.

Safe to say now: agents work from the same live, governed dataset as everyone else;
they leave the same audit trail as a person; nothing moves without an admin approving
it. The roadmap's enterprise-governance work supports this: audit logs to customer
SIEMs, access controls, approval routing, and 2FA are all GA. See
[incentives.md](incentives.md#controls-and-governance-ga).

## Who it's for

- Primary: the comp or RevOps practitioner/leader who builds and maintains plans.
  Secondary: CRO and CFO.
- Mid-market: comp is one of five jobs, one person can run the tool, they already use
  ChatGPT, and they want value in week one without a consultant.
- Enterprise: logic buried in a build by people who left, services dependency, finance
  scrutiny at renewal, an exec AI mandate. Security and legal review is "the long pole".

## Proof (status in [positioning/proof-points.md](../../positioning/proof-points.md))

- ClickUp (Garrett Kraudy, Senior FP&A Partner): an hour of copy-paste work "now takes
  10-15 minutes across different plans". Public testimonial on /ai-agents; no case study page yet.
- Vercel: logo on the homepage and /ai-agents. No public quote or case study yet,
  although the launch brief planned one.
- "The agents cut a 4-hour job down to 30 minutes" appears on the public webinar page,
  attributed to ClickUp.
