# Contact enquiry verification

Source: [contact scope](../contact-enquiry.md), 27 October 2026.

| Acceptance | Evidence |
|---|---|
| AC1 | Visible labels, native required/email validation, length limits, privacy disclosure. Empty name and invalid email focus the invalid field. |
| AC2 | Existing Formspark connection recovered from original site. Synthetic API preflight returned200 and matching full message reached business INBOX UID151. No new provider credentials/dependencies/backend. |
| AC3 | Local isolated browser endpoints verified pending, accepted, failed503 and disconnected-network uncertainty. Failed/uncertain input retained and retry enabled; pending readonly/disabled; accepted duplicate button disabled. |
| AC4 | Ten Node tests cover Unicode/newlines, fixed recipient, query/header injection, full2000-character copy and provider outcomes. Browser hrefs/copy action verified. Gmail opens only on visitor action in a new tab; drafts must be sent by the visitor. External mail-client delivery is not claimed as tested. |
| AC5 | Script-free native browser submission through actual Formspark delivered (INBOX UID152), redirected to success with empty query. A synthetic honeypot submission redirected to error, also without query data. Native failure recovery makes no input-retention guarantee. |
| AC6 | Contact at375/768/1440: no overflow/header collision, all required controls visible with readable labels. Keyboard Tab and purple focus ring checked. Static checker covers54 pages, sitemap and JSON-LD; contact has canonical and ContactPage data. Homepage remains below100KB and loads no contact module/style. |
| AC7 | Actual provider/inbox delivery proven. Production module MIME/CORS and a final live enhanced submission are post-upload release checks. Protected legal/privacy/app responses must remain unchanged. |

## Review corrections and limits

- Spec challenge reconciled enhanced versus native preservation/duplicate guarantees
  and corrected mirrored privacy/success copy. Active Hostinger privacy already
  discloses Formspark, name/email/message and the established retention policy;
  it stays outside the overlay. No tracking, cookies or application storage added.
- Input/action borders darkened to #977d9e:3.66:1 on white,3.53:1 on the card.
- aria-busy belongs to the submit button, leaving pending live status outside its
  busy subtree. No HTML interpolation or enquiry-content logging.
- Provider dashboard retention/quota settings are unverified owner duties; the
  application does not make a new deletion or delivery guarantee. Provider spam
  filtering/honeypot and availability remain operational boundaries.
- Full OS forced-color/reduced-motion emulation is unavailable; shared guards and
  contact-specific system borders remain. Actual sending in a visitor's mail
  app/Gmail is a visitor action; URL data round trips and copy fallback are tested.
- Public release is an explicit committed-file overlay, new assets/pages before
  navigation and homepage last. Exclude live privacy/legal, app/assets and all
  unrelated private working files. Rollback uses a reviewed revert and overlay.

Commands: node --test scripts/contact.test.mjs; node --check assets/contact.mjs;
python3 scripts/check_site.py; scoped git diff --check. Ten tests were observed
RED before implementation and then GREEN; evidence stays locally under tmp/.
