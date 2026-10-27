# Ferre Torres B.V. GitHub Page

Static landing page for Ferre Torres B.V., the Dutch B.V. for European AI-first transformation work.

## Publish on GitHub Pages

Production `ferretorres.eu` is currently hosted on Hostinger; GitHub Pages is a
mirror. Reuse `.hostinger/site.json`. Publish an explicit static-file overlay,
preserving the separate `iih/` application and existing `_astro/`, `og/`,
`legal.html` and `privacy.html`. Never upload this entire working directory:
it also contains private, untracked accounting files. Include `.htaccess` so
service URLs resolve directly and extensionless legal URLs remain available.

1. Push this repository to GitHub.
2. In the repository settings, open **Pages**.
3. Set the source to **Deploy from a branch**.
4. Select the default branch and `/ (root)`.

Custom domain: `ferretorres.eu`.
Public contact email: `jferre@ferretorres.eu`.

## Operating docs

- Manual launch and indexing tasks: `LAUNCH_GUIDE.md`
- Short owner action checklist: `OWNER_ACTIONS.md`
- Owner completion tracker: `specs/site-completion-tracker.md`
- Outreach and first-call sales guide: `SALES_PLAYBOOK.md`
- Proposal templates: `PROPOSAL_TEMPLATES.md`
- Lead qualification checklist: `LEAD_INTAKE_CHECKLIST.md`

## QA

The October 2026 visual refresh uses `assets/brand.css` across all pages,
`assets/home.css` for the visual homepage, and dependency-free `assets/site.js`
for navigation, workflow tabs, one-time section entrances, and email copying.
Three small `assets/workflow-*.svg` illustrations load lazily. The homepage uses
only the two dedicated stylesheets; secondary pages also retain `styles.css`. The custom vector identity
lives in `assets/ferre-torres-mark.svg` and `favicon.svg`.

Design scope: [immersive redesign spec](specs/immersive-redesign.md).
Verification: [redesign QA](specs/qa/immersive-redesign.md).

The homepage and contact page offer direct submission through the existing Formspark form,
an email-app draft, and Gmail composition. The two draft options send only when
the visitor presses Send in their own account, preserving their Sent history.
See [contact scope](specs/contact-enquiry.md). Run `node --test scripts/contact.test.mjs`
for message encoding, provider outcomes and error-state contracts. The live
Hostinger privacy document already discloses Formspark; keep it preserved when
deploying. The repository privacy page reflects the same contact data flow.
`assets/.htaccess` declares the JavaScript MIME type for `.mjs` on Hostinger.
After publication, run `node scripts/check_contact_http.mjs` to verify module
headers and release bytes for both pages; a successful static check cannot prove server MIME.

For a local preview, run `python3 -m http.server 8010 --bind 127.0.0.1` and
open `http://127.0.0.1:8010/`. No build or dependency installation is needed.

Run static site checks before publishing changes:

```bash
python3 scripts/check_site.py
```

The QA script also checks for insecure `http://` asset URLs and required
referrer-policy metadata. For the public site, use `https://ferretorres.eu/`.
The local preview URL `http://127.0.0.1:8010/` can appear as "Not secure" in
the browser because it is a local HTTP development server.

Regenerate social preview cards after changing the visual direction:

```bash
python3 scripts/generate_og_images.py
```
