import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {test} from 'node:test';

const home = await readFile(new URL('../index.html', import.meta.url), 'utf8');
const contact = await readFile(new URL('../contact.html', import.meta.url), 'utf8');
const form = html => html.match(/<form id="enquiry-form"[\s\S]*?<\/form>/)?.[0];

test('homepage embeds the complete established enquiry form', () => {
  assert.equal((home.match(/id="enquiry-form"/g)||[]).length, 1);
  assert.equal(form(home), form(contact));
});

test('homepage loads the shared form module and stylesheet', () => {
  assert.match(home, /<script type="module" src="assets\/contact\.mjs\?v=/);
  assert.match(home, /<link rel="stylesheet" href="assets\/enquiry\.css\?v=/);
});
