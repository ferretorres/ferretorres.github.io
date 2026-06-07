# Ferre Torres B.V. site completion tracker

Last updated: 2026-06-07

Purpose: keep track of manual inputs, missing proof, and future improvements that should not block the current site but matter before pushing harder to enterprise buyers.

## Current status

- Public site: deployed at `https://ferretorres.eu/`.
- GitHub Pages: active with custom domain and HTTPS.
- Core positioning: AI consultancy for companies, AI-first transformation, Company Brain, RAG, agents, finance intelligence, AI-native internal software.
- Entity scope: Ferre Torres B.V. only.
- Contact email: `jferre@ferretorres.eu`.
- Contact path: static form creates an email draft; no automatic form endpoint is connected yet.
- Discovery files: `sitemap.xml`, `robots.txt`, and `llms.txt` exist.
- SEO pages: homepage, AI consultancy, AI implementation services, AI consulting process, AI capability statement, AI readiness checklist, enterprise AI RFP checklist, Netherlands/city pages, enterprise/CEO/CFO/CTO pages, AI opportunity assessment, AI integration roadmap, AI MVP/PoC, AI architecture, AI delivery model, AI security/GDPR, solution/demo/proof pages.
- Demo state: synthetic guided preview pages and a guided-demo meeting page exist; production demo apps or live walkthrough videos are not embedded yet.
- Proof state: anonymized implementation pattern pages exist; named client case studies, testimonials, logos, and quantified outcomes are not approved yet.
- Owner actions: `OWNER_ACTIONS.md` lists manual account, proof, analytics, form, booking, pricing, and rollout decisions.
- Sales enablement: `SALES_PLAYBOOK.md`, `PROPOSAL_TEMPLATES.md`, and `LEAD_INTAKE_CHECKLIST.md` exist for outreach, first calls, qualification, follow-up, and proposal drafting.

## Fix now

None known. Current site is shippable as a professional v1 assuming the latest deployed build remains healthy.

## Manual owner tasks

### 1. Google Search Console indexing

- Category: SEO / indexing
- Status: owner action needed
- Why not done: requires Google account UI access.
- Risk if left: Google may discover pages slower and may not prioritize the new SEO pages.
- Revisit trigger: after every new important page or monthly until pages are indexed.
- Affected area/files: `sitemap.xml`, `LAUNCH_GUIDE.md`.
- Dependencies/blockers: Google Search Console access.
- Acceptance criteria:
  - Domain property verified.
  - Only `https://ferretorres.eu/sitemap.xml` submitted under Sitemaps.
  - URL Inspection requested for priority pages.
  - Search Console shows sitemap read successfully.
- Verification:
  - Search Console sitemap status is success.
  - Pages start appearing under indexed/discovered URLs.

Priority URL list:

- `https://ferretorres.eu/`
- `https://ferretorres.eu/ai-consultancy.html`
- `https://ferretorres.eu/ai-implementation-services.html`
- `https://ferretorres.eu/ai-consulting-process.html`
- `https://ferretorres.eu/ai-readiness-checklist.html`
- `https://ferretorres.eu/ai-opportunity-assessment.html`
- `https://ferretorres.eu/ai-integration-roadmap.html`
- `https://ferretorres.eu/ai-mvp-poc.html`
- `https://ferretorres.eu/ai-security-gdpr.html`
- `https://ferretorres.eu/ai-consulting-for-enterprises.html`
- `https://ferretorres.eu/enterprise-ai-rfp-checklist.html`
- `https://ferretorres.eu/ai-consulting-for-ceos.html`
- `https://ferretorres.eu/ai-consulting-for-cfos.html`
- `https://ferretorres.eu/ai-consulting-for-ctos.html`
- `https://ferretorres.eu/ai-consultancy-netherlands.html`
- `https://ferretorres.eu/company-brain-for-companies.html`
- `https://ferretorres.eu/rag-consultant-netherlands.html`
- `https://ferretorres.eu/ai-demo-gallery.html`
- `https://ferretorres.eu/guided-ai-demo.html`
- `https://ferretorres.eu/ai-architecture.html`
- `https://ferretorres.eu/delivery-model.html`
- `https://ferretorres.eu/delivery-patterns.html`

### 2. Contact form endpoint

- Category: conversion / lead capture
- Status: owner decision needed
- Why not done: requires choosing a provider and creating an endpoint.
- Risk if left: mailto fallback works, but some visitors may not complete the email draft.
- Revisit trigger: before sending the site to a high-value campaign or after the first missed/uncertain lead.
- Affected area/files: `index.html`, `privacy.html`, `LAUNCH_GUIDE.md`.
- Dependencies/blockers: Formspree, Basin, Tally, HubSpot, or another approved form provider.
- Acceptance criteria:
  - Provider selected.
  - Endpoint configured in `window.FERRE_SITE_CONFIG.formEndpoint`.
  - Test submission reaches `jferre@ferretorres.eu`.
  - Privacy page updated with provider and purpose.
- Verification:
  - Submit a test brief from the live site.
  - Confirm success page or fallback behavior.
  - Confirm no console errors.

### 3. Privacy-friendly analytics

- Category: SEO / conversion measurement
- Status: owner decision needed
- Why not done: requires choosing a provider and accepting tracking tradeoffs.
- Risk if left: no visibility into traffic, search landing pages, or conversion path.
- Revisit trigger: before active LinkedIn/outbound/SEO campaign.
- Affected area/files: `index.html` and all static pages if script is global, `privacy.html`.
- Dependencies/blockers: Plausible, Simple Analytics, Fathom, or another privacy-friendly provider.
- Acceptance criteria:
  - Provider selected.
  - Analytics script added consistently.
  - Privacy page updated.
  - Core events defined: contact click, project brief generation, demo page visits, role page visits.
- Verification:
  - Live pageview appears in analytics dashboard.
  - No layout or console regressions.

### 4. Proof and credibility inputs

- Category: sales trust
- Status: owner content needed
- Why not done: requires approved project facts and confidentiality decisions.
- Risk if left: site reads professional but lacks hard external proof for conservative enterprise buyers.
- Revisit trigger: before sending to enterprise procurement, recruiters, partners, or C-level warm intros.
- Affected area/files: `proof.html`, `delivery-patterns.html`, pattern pages, homepage trust section.
- Dependencies/blockers: permission to name clients or approved anonymized facts.
- Acceptance criteria:
  - 3-5 anonymized project notes completed using the template in `LAUNCH_GUIDE.md`.
  - Each note has industry, problem, what was built, time to MVP, tools/data, users, outcome, reusable system, and confidentiality boundary.
  - At least 2 quantified outcomes are approved for public wording.
- Verification:
  - Review pages for false claims and confidentiality.
  - Browser and SEO checks pass after content update.

### 5. Team and delivery network credibility

- Category: sales trust / company positioning
- Status: owner content needed
- Why not done: requires names, roles, bios, or preferred anonymity for freelancers/partners.
- Risk if left: buyers may still infer the company is only one person despite current company/team wording.
- Revisit trigger: before pitching larger implementation projects.
- Affected area/files: homepage trust section, `ai-consulting-for-enterprises.html`, optional future team/delivery page.
- Dependencies/blockers: approval from collaborators if named.
- Acceptance criteria:
  - Delivery model wording clearly explains founder-led senior network.
  - If public, each collaborator has role, capability, and optional LinkedIn/profile.
  - If private, public wording explains capacity without naming people.
- Verification:
  - Review for overclaiming.
  - Confirm wording stays BV-only.

Autonomous progress: `delivery-model.html` now explains the founder-led senior delivery model without naming collaborators or overstating capacity. Owner input is still needed if named profiles, bios, LinkedIn links, or explicit delivery capacity should be public.

### 6. Guided demo assets

- Category: conversion / sales enablement
- Status: future asset work
- Why not done: current pages use synthetic static previews, not live demos or videos.
- Risk if left: visitors can understand the offer, but high-intent buyers may still need a meeting to see depth.
- Revisit trigger: before a demo-led outreach campaign or after repeated buyer requests for examples.
- Affected area/files: `ai-demo-gallery.html`, all `demo-*.html`, possible future `/assets/demo-*`.
- Dependencies/blockers: chosen demo scenarios, screenshots/videos, or lightweight interactive mockups.
- Acceptance criteria:
  - Each core solution has either a stronger static screenshot, short walkthrough video, or interactive static mock.
  - All assets are synthetic/anonymized.
  - Pages clearly invite a guided demo meeting.
- Verification:
  - Browser desktop/mobile checks.
  - Performance check after adding media.

### 7. Booking flow

- Category: conversion
- Status: owner decision needed
- Why not done: requires choosing whether to expose calendar availability publicly.
- Risk if left: email flow is professional but higher friction than direct scheduling.
- Revisit trigger: when outreach volume starts or if prospects ask for scheduling links.
- Affected area/files: homepage contact section, demo pages, enterprise page.
- Dependencies/blockers: Cal.com, Calendly, SavvyCal, or manual email-only preference.
- Acceptance criteria:
  - Booking policy chosen.
  - If added, CTA is `Request demo or project discussion` plus booking link.
  - Privacy page updated if provider uses cookies/tracking.
- Verification:
  - Test booking link on desktop/mobile.
  - Confirm no intrusive third-party embed unless intentionally approved.

### 8. Search positioning expansion

- Category: SEO
- Status: deferred
- Why not done: current English SEO footprint is broad enough for v1; more pages should follow evidence.
- Risk if left: ranking for competitive keywords like `AI consultancy Netherlands` will take time.
- Revisit trigger: after Search Console has 2-4 weeks of query data.
- Affected area/files: service pages, sitemap, `llms.txt`.
- Dependencies/blockers: Search Console query data.
- Acceptance criteria:
  - Identify queries with impressions but low CTR or low average position.
  - Add/adjust pages only around real query evidence.
  - Avoid duplicate thin pages.
- Verification:
  - Metadata, sitemap, internal links, browser checks.

### 9. Dutch-language SEO decision

- Category: SEO / localization
- Status: decision needed later
- Why not done: current site is English-only by design.
- Risk if left: Dutch-language searches may be harder to win in the Netherlands.
- Revisit trigger: Search Console shows Dutch queries or Netherlands impressions that English pages do not capture.
- Affected area/files: possible future Dutch landing pages, hreflang, sitemap.
- Dependencies/blockers: decision on whether to support Dutch copy.
- Acceptance criteria:
  - Decide whether to keep English-only or add limited Dutch pages.
  - If adding Dutch, use clean canonical/hreflang and do not machine-translate blindly.
- Verification:
  - SEO metadata checks plus manual copy review.

### 10. Pricing and packaging

- Category: sales enablement
- Status: owner decision needed
- Why not done: public pricing may not be desirable for high-ticket enterprise work.
- Risk if left: buyers may not know expected engagement size; too much ambiguity can reduce qualified leads.
- Revisit trigger: after 3-5 inbound conversations or before outbound campaign.
- Affected area/files: `ai-opportunity-assessment.html`, `ai-integration-roadmap.html`, `ai-mvp-poc.html`, proposal templates.
- Dependencies/blockers: target deal size, minimum engagement, whether to publish ranges.
- Acceptance criteria:
  - Decide public vs private pricing.
  - Define packages: assessment, roadmap, MVP/PoC, production build, advisory retainer.
  - Add ranges only if strategically useful.
- Verification:
  - Review wording for enterprise positioning and no unwanted anchoring.

## Autonomous build backlog

These are safe for Codex to tackle independently unless they cross a manual decision above.

| Item | Status | Notes |
|---|---|---|
| Add lightweight Open Graph preview image variants for key pages. | Done | Key sales, solution, demo, proof, security, architecture, finance, and RAG pages now use dedicated 1200x630 social cards. |
| Add a small `README.md` section pointing to `LAUNCH_GUIDE.md` and this tracker. | Done | `README.md` now links the operating docs. |
| Add a repeatable static QA script so the long validation commands live in one place. | Done | `scripts/check_site.py` validates metadata, JSON-LD, links, sitemap coverage, and basic accessibility markers. |
| Add stronger internal links from demo pages back to `ai-mvp-poc.html`, `ai-security-gdpr.html`, and `index.html#contact` where relevant. | Done | Demo pages now connect previews to MVP/PoC, security/GDPR, and contact paths. |
| Improve `proof.html` with a clearer "what evidence we need next" section while staying anonymized. | Done | Proof page now separates current public-safe proof from owner-approved evidence needed later. |
| Add a short LinkedIn post for the new `ai-security-gdpr.html` page in `LAUNCH_GUIDE.md`. | Done | Launch guide includes the security/GDPR post draft. |

## Next recommended sequence

1. Owner: submit sitemap and request indexing for priority URLs.
2. Owner: choose form endpoint provider or decide to stay email-only.
3. Owner: choose analytics provider or decide to stay analytics-free.
4. Owner: provide 2-3 anonymized proof notes.
5. Codex: add real demo assets when owner has screenshots/videos or approves synthetic interactive mockups.
6. Codex: expand SEO pages only after Search Console query data shows which terms have impressions.

## Notes

- Do not publish named client logos, named case studies, or quantified outcomes without explicit approval.
- Do not claim certifications, regulatory approvals, or legal advice.
- Keep the site BV-only unless the UAE company is intentionally introduced in a separate context.
- Keep public demos synthetic or anonymized.
