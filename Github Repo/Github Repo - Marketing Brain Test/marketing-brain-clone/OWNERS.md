# Owners

**Status:** first pass · **Maintainer:** Darrell Wu · **Last updated:** 2026-10-06

Who owns each part of the brain. The owner approves changes, keeps files current,
and signs off before a file moves from `status: draft` to `status: approved`.
Directories follow the tree in [PROPOSAL.md](PROPOSAL.md#3-proposed-tree).

Indented rows (`├─`, `└─`) are paths inside the folder above them. To indent a
row, start its other cells with `&emsp;` (one per level). An owner marked
*(inherited)* is the parent folder's owner. Replace it with a name to hand that
piece to someone else. Anything inside a folder that isn't listed belongs to the
folder's owner.

| Path | What's in it | Owner |
| --- | --- | --- |
| `product/` | Product overview, capabilities, integrations, packaging, launches | Product Marketing |
| `├─ capabilities/` | &emsp;One file per product area |  |
| `├─ packaging.md` | &emsp;Editions and tiers, externally sayable only |  |
| `└─ launches/` | &emsp;One file per launch: what, who, key messages, date |  |
| `positioning/` | Messaging framework, competitors, proof points, objections | Product Marketing |
| `├─ messaging-framework.md` | &emsp;Positioning statement, pillars, value props |  |
| `├─ competitors/` | &emsp;One file per competitor, plus spreadsheets and build-it-ourselves |  |
| `├─ proof-points.md` | &emsp;Approved stats, customer quotes, logos |  |
| `├─ icp-and-segments.md` | &emsp;ICP, segments, industries, disqualifiers | &emsp;Daniel McFarland (Sales Enablement) |
| `└─ personas/` | &emsp;One file per buyer persona | &emsp;Daniel McFarland (Sales Enablement) |
| `brand/` | Voice and tone, writing style, word list, visual identity, examples | Jarrod (Design) |
| `├─ voice-and-tone.md` | &emsp;Who we sound like, tone by channel and audience |  |
| `├─ word-list.md` | &emsp;Use, avoid, never-say |  |
| `└─ visual-identity.md` | &emsp;Colors, type, logo rules, link to the asset library |  |
| `library/` | Core reusable content assets, as files or links: research, analyst reports, case studies | Product Marketing |
| `├─ research/` | &emsp;Our own research, e.g. "State of Incentive Compensation" | |
| `├─ analyst-reports/` | &emsp;Gartner, Forrester, etc.: summary and link | |
| `└─ case-studies/` | &emsp;Full customer stories | |
| `marketing-ops/` | Systems map, funnel, campaigns, UTMs, data dictionary, reporting | Darrell Wu (Marketing Ops) |
| `├─ campaigns.md` | &emsp;Campaign types, naming convention, member statuses |  |
| `├─ utm-standards.md` | &emsp;UTM taxonomy and rules, plus `utm-taxonomy.yaml` |  |
| `└─ data-dictionary.md` | &emsp;Key fields, meanings, picklist values |  |
| `setup/` | Getting started, connectors, Salesforce CLI, MCP config | Darrell Wu (Marketing Ops) |
| `├─ getting-started.md` | &emsp;Clone, open in your assistant, starter prompts |  |
| `├─ connectors.md` | &emsp;Which connectors to enable and why |  |
| `└─ salesforce-cli.md` | &emsp;Install `sf` CLI, SSO login, troubleshooting |  |
| `skills/<name>/` | One procedure per folder | The skill's author, set in its frontmatter |
| `templates/<name>.md` | Fill-in-the-blank docs | The template's author, set in its frontmatter |
| `company/` | Overview, glossary | |
| `├─ overview.md` | &emsp;What CaptivateIQ does and who we sell to, in one page | |
| `└─ glossary.md` | &emsp;ICM, SPIFF, MQL, SAL and other terms, one definition each | |
| Root files and `.github/` | README, AGENTS, CONTRIBUTING, CHANGELOG, CODEOWNERS | |
