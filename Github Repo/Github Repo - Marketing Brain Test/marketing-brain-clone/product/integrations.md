---
title: Integrations
owner: pmm
status: draft            # Thin: only the Workday connector is documented in the sources read
last_reviewed: 2026-10-22
review_every: 90d
source: "Internal EPD Releases tracker (read 2026-10-22); Workday Marketplace search (2026-10-22); Partner Listing Boilerplate, Workday Marketplace listing draft (Oct 2026); Cross-Sell/Upsell framework; competitive docs (2024–26). Directory row 'Architecture, integrations & scale' (Product + SE) has no doc."
---

# Integrations

CaptivateIQ pulls data from CRM, HRIS, ERP, and data warehouses into SmartGrid.
Forrester (Q1 2025) called out our wide range of preconfigured integrations as a
strength. Older assets claim "20+ pre-built integrations (CRM, ERP, HRIS, and more)";
check the current number with Product.

## Workday (HCM) connector

**Native Workday Integration went GA on 2026-07-29** (internal release tracker, Tier 3).
The partner boilerplate drafts a Workday Marketplace listing called **CaptivateIQ
Workday Connector**, but as of 2026-10-22 **no CaptivateIQ listing is live** on the
marketplace, while Xactly's and Varicent's are. The public page,
[captivateiq.com/integration-partners/workday](https://www.captivateiq.com/integration-partners/workday),
is thin. Ask PMM whether the end-date generation scope shipped; the roadmap rows for it
were never updated.

Draft listing copy:

> Run incentive compensation and planning on live Workday employee data with the
> CaptivateIQ Workday Connector.

- Pulls employee data from Workday HCM, so plans, quotas, and payouts run on the worker
  data HR manages, with Workday as the source of truth.
- Admins write **Workday Query Language (WQL)** queries from inside CaptivateIQ, using a
  schema explorer that lists the tables, fields, data types, and required filters the
  integration user can see.
- Previews sample rows, maps a unique ID, and creates worksheet columns automatically.
- On-demand syncs in insert, upsert, or delete mode, with record counts and errors logged per job.
- OAuth authentication (Workday API client ID, client secret, refresh token).
- Works with CaptivateIQ Incentives and CaptivateIQ Planning. Requires Workday Core HCM.
  Self-service or services setup. Global.

## Salesforce (CRM)

- Syncs with Salesforce so plans and quotas match CRM data. Territory and quota design
  runs on live CRM data.
- Multiple import modes per connector (e.g. overwrite), plus Workato for complex
  imports. Older battlecards contrast this with Spiff, where deleted Salesforce records persist.

## Other

- NetSuite: a "CIQ for NetSuite" partner battlecard exists in Notion (Oct 2025, not read).
- Data workbooks and CSV upload (Catalyst and SmartGrid).

## In beta (don't claim as available)

Self-service managed connectors (e.g. Google Sheets, BigQuery, HubSpot), the
overhauled connector management UI, and Data Prep.

## To fill in

Full connector list, data-flow diagram, API, and scale proof (payee counts, plan
complexity, calculation times). The directory assigns these to Product and Solutions Engineering.
