---
title: Incentives (ICM)
owner: pmm
status: draft
last_reviewed: 2026-10-22
review_every: 90d
source: "2025_SPM_Narrative First Call Deck appendix (mod 2026-10-13); Messaging Framework V6; Battlecard: Spreadsheets (mod 2026-03-13); internal EPD Releases tracker, GA items only (read 2026-10-22)"
---

# Incentives (incentive compensation management)

Calculates and pays commissions and bonuses, gives reps live visibility into their pay,
and gives finance an auditable record. The product CaptivateIQ was founded on, by
"comp professionals, for comp professionals".

## Capabilities (from the first-call deck)

| Area | Promise | Features |
| --- | --- | --- |
| **Automate** | Improve efficiency with automation | Data integrations · data management · plan design · workflow automation · ASC 606/340 · AI admin co-pilot |
| **Motivate** | Boost motivation with transparency | Rep statements · what-if calculator · leaderboards · task management · manager views · AI payee coach · plan documents |
| **Captivate** | Support company strategy | Out-of-the-box reports and dashboards · advanced reporting · custom dashboards · reporting API · AI plan advisor |

The V6 framework describes the same product in growth terms:
- Build any plan (splits, accelerators, exceptions) and change it in days.
- Live rep statements show deal pay, accelerator progress, and a what-if calculator.
- Trace every payout and accrual to its source, with a built-in audit trail and SOX-compliant controls.
- Automated workflows for payouts, plan administration, and plan agreements.
- Excel-like formulas, with no proprietary syntax.

## Shipped in the last year (internal release tracker, GA only)

| GA date | Release |
| --- | --- |
| 2026-02-11 | **Payee mobile app** (Tier 1). Forrester's Q1 2025 "no mobile app" weakness no longer applies. |
| 2026-02-11 | Automated plan assignments; multi-product global navigation |
| 2026-05-06 | Charts in statement PDFs |
| 2026-07-29 | Payee statement links; custom payee email templates |
| 2026-09-09 | **Native plan document management** (Tier 2) |
| 2026-10-21 | Inquiries enhancements; plan document follow-ups |

### Controls and governance (GA)

The roadmap frames these as table stakes that remove enterprise trust objections so
the AI story can land. They also answer Forrester's low score on
controls/compliance/administration.

| GA date | Release |
| --- | --- |
| 2025-10-22 | Sandbox management upgrades; report model access export; column tracing |
| 2026-02-11 | User segmentation and sub-resource access controls |
| 2026-03-25 | Audit logs shipped to customer SIEM tools |
| 2026-05-06 | Configurable link expiration; approver auto-assignment; approval routing by calculated field |
| 2026-06-17 | Email-based 2FA; contextual audit log links |
| 2026-07-29 | Audit log CSV exports; SFTP with customer-provided public key |

Still in beta, so don't claim them: enterprise payout approval workflows, custom email
sender domain, extra SSO restrictions for sandbox, SFTP encryption at rest.

## Why it's different

- **Modeling-centric.** "Our product was built knowing commissions is a modeling
  problem." Admins build and adapt plans themselves, in real time, on SmartGrid.
- **Self-serve.** Plan changes don't wait on IT or professional services.
- **Analyst view (Forrester Q1 2025):** strong on plan creation, modeling, data
  transformation, and time to value. Weaker on controls/compliance/administration and
  dispute resolution, and it had no mobile app. Both have since been addressed (see
  above), which is worth raising in the next Forrester briefing. See
  [library/analyst-reports/forrester-wave-spm-ic-q1-2025.md](../../library/analyst-reports/forrester-wave-spm-ic-q1-2025.md).

## Verify with Product

- The "ASC 606/340*" asterisk in the deck has a footnote that didn't come through.
- Whether the AI co-pilot, payee coach, and plan advisor names are current after the Agents launch.
- "Payee AI agents" were made available to sell in Nov 2025 but hadn't been released as of
  Oct 2026, per the release tracker. Check what's been sold or promised.
