# Contact enquiry choices

Source: owner request, 27 October 2026. Extends immersive-redesign.md.

## Outcome and brownfield delta

Visitors can fill a short project enquiry and choose direct submission, their
email app, or Gmail. Email-app/Gmail routes let them retain sent-mail history.
Current marketing site exposes mailto links only; the prior live site had an
existing Formspark action https://submit-form.com/Gkeicb6LW, already disclosed
in the preserved live privacy policy. Reuse and verify that established delivery
connection. No new backend, SMTP credentials, account, package or tracking.

Add an indexable contact.html with visible contact details, relevant service
links, canonical/ContactPage structured data and sitemap entry. A form supports
enquiries; it does not promise better search rankings. Keep homepage under
100 KB by loading form styling/script only on the contact page.

## Acceptance criteria

- AC1: Name (120 chars), email (254), message (2000) have visible labels, native
  required/type validation, autocomplete and clear privacy guidance. Three
  choices explain website submission versus a draft the visitor must send.
- AC2: Direct submit POSTs only name/email/message plus honeypot/control fields
  to the existing HTTPS Formspark endpoint. No credentials in public code. No
  attachments, autoresponder to unverified recipients or new storage.
- AC3: In the JavaScript-enhanced flow, pending prevents duplicate sends. Success
  appears only after provider
  acceptance; failures, rejection and timeouts preserve input, enable retry and
  offer email choices. Timeout says delivery is uncertain, avoiding false claims.
- AC4: Email app and Gmail receive the same fixed recipient, subject and current
  Unicode/newline-safe message. They send nothing automatically. Gmail opens
  only by user click, with noopener/noreferrer. Values stay local until a chosen
  action; no localStorage, autosave, logs or analytics for enquiry content.
- AC5: Native form works without JS with distinct success/error redirects and
  _append=false so enquiry content never enters redirect query strings. Native
  cross-origin navigation does not promise retained input or duplicate protection;
  the error page explains retry/email recovery. Verify a script-free submission.
- AC6: Keyboard/mobile/desktop layouts, readable focus/status, invalid/pending/
  success/failure states and original homepage menu/workflows pass. New page
  has one H1, valid metadata/schema/internal links and sitemap coverage.
- AC7: Verify a synthetic direct submission reaches jferre@ferretorres.eu.
  Opening a draft is never presented as sending it. Existing live legal/privacy
  and separate app remain unchanged on Hostinger. Update contradictory local
  privacy source and old email-draft success copy for the GitHub mirror. Publish
  via reviewed committed-file overlay excluding the active privacy/legal files.

## Boundaries, data and threats

Name/email/message are visitor personal/business enquiry data. Direct route:
visitor browser -> existing Formspark -> business inbox. Formspark manages spam
filtering, provider quota and storage. Keep existing honeypot. Frontend validation
helps users; it is not claimed as server enforcement. No account settings or
provider protections changed. Draft routes: browser -> chosen mail app or Gmail
only on click. Recipient is fixed; no dynamic action URL, injection or HTML
rendering from input. Build URLs with encoding and status with textContent.

Existing live privacy policy names Hostinger and Formspark, name/email/message,
no tracking/cookies and 24-month enquiry retention. Preserve it; link clearly and
name Formspark beside direct submission. Provider dashboard retention cannot be
verified from a public endpoint; owner retains mailbox/provider retention duties.
Residual risk: external service availability, spam false positives and long mail
URI handling. Show honest errors, keep input and offer a full-message copy action.
No raw message data in screenshots/evidence except clearly synthetic fixtures.

## Slices and validation

1. Contact UI and email draft composition: contact.html, assets/contact.css,
   assets/contact.mjs; failing Node tests for Unicode/fixed recipient/encoding.
2. Formspark submission: tested local fake HTTP boundary for accepted/rejected/
   timeout states; live synthetic delivery separately. Native redirect controls
   statically checked. No test mocks on public production.
3. Discovery/release: homepage and navigation links, sitemap, success/error
   pages, operating docs and completion tracker. Static checker across all pages,
   JS syntax, Node tests, browser at375/768/1440, independent review and live
   delivery gate. Existing PHP investigation is unused; no PHP dependency added.

Rollout risks: lost messages, misleading Sent history, stale scripts/redirects.
Mitigations: real delivery check, explicit draft wording and versioned new assets.
Release before linking new pages: assets/new pages, then changed navigation,
index last. Rollback: reviewed revert plus explicit overlay; preserve protected
paths and all unrelated/private working files.

## Challenge reconciliation

Independent challenge found no provider blocker after verified inbox delivery.
Scoped input retention/duplicate guarantees to the enhanced flow; native failure
recovery is explicit. Update mirror privacy and old success copy, while preserving
the active Hostinger privacy document already describing Formspark enquiries.

## Homepage form, 27 October 2026

The owner now requests the same form directly on the homepage with all three
sending choices and direct publication. This supersedes the contact-page-only
loading decision above. The existing provider, payload, protection and privacy
boundaries remain unchanged.

- AC8: Exactly one homepage form has the same name/email/message constraints,
  endpoint, native redirect controls and three sending choices as contact.html.
  Reuse the existing module, extracting shared form styles without a library.
- AC9: Keep the complete homepage local-resource budget below100,000 decoded
  bytes, including the module, shared stylesheet and font. Compact structured
  data without changing values, trim source indentation, and remove superseded
  contact CTA styles/clipboard code. No deferred-resource accounting loophole.
  No request to Formspark or Gmail occurs until a visitor chooses an action.
- AC10: Homepage desktop/tablet/mobile form, draft values/copy, validation, native
  and enhanced submission work; menu/workflows and contact-page layout remain
  healthy. Verify module MIME and exact source bytes for both live pages and
  actual homepage submission reaching the business inbox.

Validation: new homepage/contact parity regression observed RED first; existing
10 Node tests, static54-page/100KB gate, syntax, browser375/768/1440 and live HTTP
checks. Publish explicit committed files via reviewed rebase merge and existing
Hostinger overlay, assets before HTML/index last. Preserve private working files,
active legal/privacy and separate application. Rollback is reviewed revert plus
targeted overlay. Risks: style collisions on plum, stale CSS/module, hidden size
regression. Controls: ivory form card/dark focus token, version keys, full budget
counting and loaded browser checks.
