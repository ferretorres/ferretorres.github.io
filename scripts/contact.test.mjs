import assert from 'node:assert/strict';
import {test} from 'node:test';
import {buildDraft, submitEnquiry, FORM_ENDPOINT} from '../assets/contact.mjs';

const enquiry = {name: 'Alex Example', email: 'alex@example.com', message: 'A useful AI workflow for our team.', _honeypot: ''};

test('drafts preserve Unicode, punctuation and newlines with a fixed recipient', () => {
  const draft = buildDraft({...enquiry, name: 'Alex & Co', message: 'Café + invoices? #1\nA second line: <review>'});
  const mail = new URL(draft.mailto);
  const gmail = new URL(draft.gmail);
  assert.equal(mail.pathname, 'jferre@ferretorres.eu');
  assert.equal(gmail.origin + gmail.pathname, 'https://mail.google.com/mail/');
  assert.equal(gmail.searchParams.get('to'), 'jferre@ferretorres.eu');
  assert.equal(mail.searchParams.get('body'), draft.text);
  assert.equal(gmail.searchParams.get('body'), draft.text);
  assert.ok(draft.text.includes('Café + invoices? #1\nA second line: <review>'));
  assert.ok(draft.text.includes('Alex & Co'));
  assert.equal(mail.searchParams.get('bcc'), null);
});

test('drafts cannot turn field values into recipients or mail headers', () => {
  const draft = buildDraft({...enquiry, name: 'Name?bcc=other@example.com', message: '&to=other@example.com\nBcc: other@example.com'});
  assert.equal(new URL(draft.gmail).searchParams.get('to'), 'jferre@ferretorres.eu');
  assert.equal(new URL(draft.mailto).searchParams.get('bcc'), null);
});

test('a full long message remains available for copying', () => {
  const message = 'é'.repeat(2000);
  const draft = buildDraft({...enquiry, message});
  assert.ok(draft.text.includes(message));
  assert.equal(new URL(draft.gmail).searchParams.get('body'), draft.text);
});

test('direct submission uses only the established provider and expected fields', async () => {
  let body;
  const outcome = await submitEnquiry(enquiry, async (url, options) => {
    assert.equal(url, 'https://submit-form.com/Gkeicb6LW');
    assert.equal(url, FORM_ENDPOINT);
    assert.equal(options.method, 'POST');
    assert.equal(options.headers['Content-Type'], 'application/json');
    body = JSON.parse(options.body);
    return {ok:true, status:200};
  });
  assert.equal(outcome, 'accepted');
  assert.deepEqual(body, enquiry);
});

for (const status of [400,403,429,500]) {
  test(`provider HTTP ${status} never reports acceptance`, async () => {
    assert.equal(await submitEnquiry(enquiry, async () => ({ok:false,status})), 'failed');
  });
}

test('network and timeout failures report uncertainty', async () => {
  assert.equal(await submitEnquiry(enquiry, async () => {throw new TypeError('network');}), 'uncertain');
  assert.equal(await submitEnquiry(enquiry, async () => {const error = new Error('timeout'); error.name='AbortError'; throw error;}), 'uncertain');
});

test('blank required text and a filled honeypot never send a request', async () => {
  const forbidden = async () => {assert.fail('No request expected');};
  assert.equal(await submitEnquiry({...enquiry,name:' '}, forbidden), 'failed');
  assert.equal(await submitEnquiry({...enquiry,message:' '}, forbidden), 'failed');
  assert.equal(await submitEnquiry({...enquiry,_honeypot:'spam'}, forbidden), 'failed');
});
