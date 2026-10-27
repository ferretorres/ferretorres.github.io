export const FORM_ENDPOINT = 'https://submit-form.com/Gkeicb6LW';
const RECIPIENT = 'jferre@ferretorres.eu';
const SUBJECT = 'AI project enquiry';

export function buildDraft(fields) {
  const name = fields.name.trim();
  const email = fields.email.trim();
  const message = fields.message.trim() || 'I would like to discuss an AI project.';
  const text = ['Hello Josep,', '', message, '', 'Best,', name, email].filter((line, index) => index < 5 || line).join('\n');
  const mailto = `mailto:${RECIPIENT}?subject=${encodeURIComponent(SUBJECT)}&body=${encodeURIComponent(text)}`;
  const gmail = new URL('https://mail.google.com/mail/');
  gmail.search = new URLSearchParams({view: 'cm', fs: '1', to: RECIPIENT, su: SUBJECT, body: text});
  return {mailto, gmail: gmail.href, text};
}

export async function submitEnquiry(fields, fetchImpl = fetch) {
  const payload = {
    name: fields.name.trim(),
    email: fields.email.trim(),
    message: fields.message.trim(),
    _honeypot: fields._honeypot || '',
  };
  if (!payload.name || !payload.email || !payload.message || payload._honeypot || payload.name.length > 120 || payload.email.length > 254 || payload.message.length > 2000) return 'failed';
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 20_000);
  try {
    const response = await fetchImpl(FORM_ENDPOINT, {
      method: 'POST',
      headers: {'Content-Type': 'application/json', Accept: 'application/json'},
      body: JSON.stringify(payload),
      signal: controller.signal,
      credentials: 'omit',
      referrerPolicy: 'strict-origin-when-cross-origin',
    });
    return response.ok ? 'accepted' : 'failed';
  } catch {
    return 'uncertain';
  } finally {
    clearTimeout(timer);
  }
}

if (typeof document !== 'undefined') {
  const form = document.querySelector('#enquiry-form');
  if (form) {
    const fields = ['name', 'email', 'message'].map(name => form.elements.namedItem(name));
    const status = form.querySelector('[data-contact-status]');
    const submit = form.querySelector('[type=submit]');
    const copy = form.querySelector('[data-copy-message]');
    const emailApp = form.querySelector('[data-email-app]');
    const gmail = form.querySelector('[data-gmail]');
    const values = () => Object.fromEntries(['name', 'email', 'message', '_honeypot'].map(name => [name, form.elements.namedItem(name).value]));
    const updateDrafts = () => {
      const draft = buildDraft(values());
      emailApp.href = draft.mailto;
      gmail.href = draft.gmail;
    };
    form.addEventListener('input', () => {
      fields.forEach(field => field.setCustomValidity(''));
      updateDrafts();
    });
    updateDrafts();
    copy.hidden = false;
    copy.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(buildDraft(values()).text);
        status.textContent = 'Message copied. You can paste it into your email app.';
      } catch {
        status.textContent = 'Copy unavailable. Select your message above to copy it manually.';
      }
    });
    form.addEventListener('submit', async event => {
      event.preventDefault();
      if (submit.disabled) return;
      for (const field of fields) {
        field.setCustomValidity(field.value.trim() ? '' : 'Please complete this field.');
      }
      if (!form.reportValidity()) return;
      const enquiry = values();
      submit.disabled = true;
      fields.forEach(field => { field.readOnly = true; });
      form.dataset.state = 'pending';
      submit.setAttribute('aria-busy', 'true');
      status.textContent = 'Sending your enquiry…';
      const outcome = await submitEnquiry(enquiry);
      form.dataset.state = outcome;
      submit.removeAttribute('aria-busy');
      fields.forEach(field => { field.readOnly = false; });
      submit.disabled = outcome === 'accepted';
      if (outcome === 'accepted') {
        submit.textContent = 'Enquiry submitted';
        status.textContent = 'Your enquiry was submitted. Thank you — we’ll reply by email.';
      } else if (outcome === 'uncertain') {
        status.textContent = 'We couldn’t confirm submission. It may have arrived. Your message is still here; check before sending again.';
      } else {
        status.textContent = 'Your enquiry wasn’t accepted. Your message is still here. Retry, or use Email app or Gmail below.';
      }
      status.focus();
    });
  }
}
