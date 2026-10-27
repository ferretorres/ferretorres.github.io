# Immersive redesign verification

Date: 27 October 2026. Source: [redesign spec](../immersive-redesign.md).

## Result

Local review gate: **Green**. The owner explicitly authorized direct publication in the refinement request. Publication is the next release step.

Green = required local checks passed; Red = a required check failed; Blocked = required proof is unavailable. There are no outstanding local failures. Live deployment and cross-browser/OS-specific checks remain outside the verified result.

## Automated checks

- `python3 scripts/check_site.py`: pass across 52 HTML pages. Metadata, canonicals, local assets/links, sitemap, JSON-LD, social images and basic document accessibility. The checker now also compares the homepage's visible FAQ with its FAQPage schema.
- `node --check assets/site.js`: pass.
- `git diff --check`: pass.
- Additional local fragment/duplicate-ID check: pass across 52 pages.
- All 52 pages include the shared brand stylesheet, common navigation and deferred enhancement script. Original secondary-page content preserved relative to the initial dirty working tree.
- Ten social preview images regenerated and inspected as 1200 × 630 JPEGs.
- Complete homepage resource budget: **75,228 bytes**, including HTML, referenced CSS/JavaScript, all SVG images, favicon and manifest. Baseline: 106,200 bytes. The checker enforces a 100,000-byte ceiling. Three new lazy SVG illustrations total 4,966 bytes; JavaScript is 4,814 bytes. No new project dependencies, fonts, tracking or third-party UI requests.

## Rendered browser checks

Target: `http://127.0.0.1:8010/`, Codex in-app browser.

| Width | Homepage | Consulting | Solutions | Company Brain demo | Privacy |
| --- | --- | --- | --- | --- | --- |
| 375 px | Pass | Pass | Pass | Pass | Pass |
| 768 px | Pass | Pass | Pass | Pass | Pass |
| 1440 px | Pass | Pass | Pass | Pass | Pass |

All fifteen layout checks found no document horizontal overflow, broken images or H1/header overlap. Representative screenshots were visually inspected. A legacy mobile header grid conflict and an inherited architecture-grid selector conflict were found and fixed during rendered review.

- Operations and finance selection show exactly one corresponding panel.
- ArrowRight changes selection and focus, wraps to the first tab, and shows a solid focus ring.
- Home and End select first/last examples; Space preserves the selected tab without following the anchor.
- Direct `#workflow-finance` navigation selects its matching panel.
- Mobile menu opens/closes; Escape closes it and returns focus; choosing Contact closes it and navigates to contact.
- FAQ disclosure opens and exposes the matching answer.
- Clipboard copy succeeds and announces success. Failure wording is present and success is set only after the clipboard promise resolves; permission-denial behavior was reviewed in source, not injected into the browser.
- Project and demo links have the correct `mailto:` recipient, subject and context. No actual email was sent.
- A script-free QA snapshot renders all three workflow examples and expanded navigation, with no hero/header overlap or horizontal overflow.
- Reduced-motion and forced-colors safeguards were confirmed in loaded CSS rules. OS media emulation is not exposed by the connected browser; actual forced-colors mode and a reduced-motion OS setting were not exercised.
- Browser console returned no errors or warnings on the inspected final service pages.

## Review and limitations

No fabricated clients, metrics or certifications. Workflow surfaces are explicitly illustrative/synthetic; existing service URLs and search discovery are retained. The homepage follows problem → workflow → architecture → engagement → delivery → FAQ → contact. The logo uses an original phi-inspired vector with the company name kept legible.

Local evidence: `tmp/redesign-browser-results.json`, `tmp/redesign-desktop.png`, `tmp/redesign-mobile.png`, and full-page variants. Starting website files are preserved in `tmp/site-redesign-baseline/`; unrelated accounting and pre-existing working-tree changes were left intact.

Not verified: live HTTPS publication, search ranking/indexing outcomes, Safari/Firefox rendering, actual OS high contrast/reduced-motion settings, email delivery. Contact remains the existing email-draft model. The owner authorized publication directly; the release uses the existing GitHub Pages source, a feature-branch PR and rebase merge.


## Refinement release gate

- Source: owner follow-up requesting slightly more immersion, improved transitions, more workflow visuals, simplicity and direct publication.
- The homepage now omits the 39,494-byte legacy stylesheet; secondary pages retain it. Shared header foundations are explicit in the brand stylesheet.
- The hero heading is visible from first paint. Entrances use transform/opacity only, run once with IntersectionObserver, and remain static under reduced-motion settings. No scroll/pointer polling or animation dependency.
- Three original 640 × 320 SVG images illustrate discovery, validation and production. Intrinsic dimensions reserve layout; lazy loading defers download below the fold.
- Fifteen current-candidate layout checks across 375/768/1440 px passed with clear headings, no overflow and no broken images. Mobile menu Enter/Tab/Escape paths, workflow selection and Home navigation passed.
- Local browser instrumentation observed initial decoded resources fall from 106,485 to 70,428 bytes (six initial requests to five), with zero observed layout shift in both samples. Instrumentation is QA-only and is not published. These are localhost observations, not real-network speed guarantees.
- `ruff check`, `ruff format --check`, `ty check`, JavaScript syntax, SVG XML, site metadata/link/schema checks and whitespace checks pass. The two changed Python scripts were made executable to match their shebangs; Pillow annotation mismatches were corrected.
- Independent change scan, adversarial review and rule audit found no remaining code blocker. The existing English-only static marketing site is an inherited mismatch with the generic Lingui localization policy; no translation compliance is claimed or localization stack introduced.
- Private accounting directories, temporary QA artifacts and unrelated existing `PROPOSAL_TEMPLATES.md` / `llms.txt` changes are excluded from the explicit staged-file allowlist.
- Release source: existing GitHub Pages legacy build from `main`, repository root. Base verified as `b045565`, matching `origin/main` before branching. Release branch: `feature/immersive-site-refinement`.
- Rollback: reviewed revert of the release commit, without a force push. Risks and mitigations are recorded in the source spec.


## Active hosting correction

Live verification after PR #13 showed the custom domain is served by Hostinger,
not the repository's GitHub Pages mirror. The mirror release built successfully
at `235ccf1`, but was not yet a successful custom-domain publication.

- Active host: Hostinger shared/cloud static website. Root also contains the
  separate `iih` application. Whole-root replacement is outside this release.
- Preserve the existing `iih/`, `_astro/`, `og/`, `legal.html` and `privacy.html`.
  The current legal/privacy pages and their assets remain available.
- Replace obsolete `.htaccess` redirects so restored service/demo pages resolve
  directly. Retain extensionless route handling. Public-site fixed-name assets
  revalidate after one hour; the inherited immutable policy for other hosts is
  retained. HTML continues to revalidate. Favicon references get a version key.
- Keep the former `#work`, `#services`, `#about` and `#how-we-work` entry points as
  aliases into the new sections, including links from preserved legal pages.
- Update through File Manager with an explicit website-only overlay, rather than
  the whole-site deploy operation. No directory deletion, DNS change, auth change,
  or database operation. Backups of the public entry, favicon, discovery and legal
  pages and the original server rules are saved locally under `tmp/`.
- Publication gate: merged source plus live HTTPS content/asset hash checks,
  direct service routes, preserved legal routes, and unchanged subdomain health.
