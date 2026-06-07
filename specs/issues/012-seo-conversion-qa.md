# Verify: SEO, conversion, accessibility, and deployment QA

## Problem

After adding visuals and pages, the site needs a final QA pass so it remains fast, indexable, responsive, and conversion-oriented.

## User story

As the company owner, I want the upgraded site to be polished and technically clean, so I can send it to enterprise prospects with confidence.

## Scope

- Run static HTML checks.
- Validate JSON-LD.
- Validate SEO metadata for indexable pages.
- Validate sitemap coverage.
- Validate internal links.
- Browser-test key pages on desktop and mobile.
- Spot-check live HTTPS URLs after deployment.
- Confirm CTAs are clear and not too scattered.
- Confirm synthetic demo labels are visible.

## Acceptance criteria

- All checks pass or documented exceptions exist.
- Sitemap and `llms.txt` include the new pages.
- No horizontal overflow on tested mobile pages.
- Contact path remains clear.
- The site can be sent as the current professional version.

## Verification

- Record the commands/checks run.
- Confirm GitHub Pages build is successful.
- Confirm representative live URLs return 200.
