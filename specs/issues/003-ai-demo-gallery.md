# Build: AI demo gallery page

## Problem

The site has several demo pages, but there is no single high-signal gallery that makes the offer feel concrete and easy to scan.

## User story

As a buyer, I want one page where I can see the types of AI systems Ferre Torres B.V. can implement, so I can choose the most relevant demo for my company.

## Scope

- Create `/ai-demo-gallery.html`.
- Add cards for Company Brain, RAG evaluation, finance intelligence, AI PM assistant, agentic workflow, and AI-first software engineering.
- Each card should include a synthetic visual preview, business value, technical angle, and CTA.
- Link the gallery from homepage and relevant service pages.
- Add gallery page to sitemap and `llms.txt`.

## Acceptance criteria

- Gallery page exists and is indexable.
- Each demo card links to the correct guided demo or future placeholder.
- CTA is clear: request a guided demo or start a project brief.
- Page includes SEO title, description, canonical URL, OG metadata, and JSON-LD if useful.
- Sitemap and internal links are updated.

## Verification

- Static metadata checks pass.
- Sitemap coverage passes.
- Browser desktop and mobile checks pass.
- Live HTTPS check returns 200 after deployment.
