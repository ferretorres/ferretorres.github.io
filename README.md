# Ferre Torres B.V. GitHub Page

Static landing page for Ferre Torres B.V., the Dutch B.V. for European AI-first transformation work.

## Publish on GitHub Pages

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
