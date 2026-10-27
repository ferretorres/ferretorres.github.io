import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';

const page = new URL('https://ferretorres.eu/contact.html');
const request = url => fetch(url, {cache: 'no-store', signal: AbortSignal.timeout(15000)});
const response = await request(page);
assert.equal(response.status, 200, 'Contact page must load');
assert.ok(response.headers.get('content-type')?.startsWith('text/html'), 'Contact page must be HTML');
const html = await response.text();
const expectedPage = await readFile(new URL('../contact.html', import.meta.url), 'utf8');
assert.equal(html, expectedPage, 'Published contact page must match the release, including its module version');
const scripts = [...html.matchAll(/<script\b(?=[^>]*type="module")[^>]*src="([^"]+)"/g)];
assert.ok(scripts.length, 'Contact page must load its enhancement module');
for (const [, src] of scripts) {
  const url = new URL(src, page);
  assert.equal(url.origin, page.origin, 'Contact modules must be self-hosted');
  const module = await request(url);
  assert.equal(module.status, 200, 'Contact module must load');
  const mime = module.headers.get('content-type')?.split(';')[0];
  assert.ok(['text/javascript', 'application/javascript'].includes(mime), `Contact module MIME is ${mime}; browsers will refuse a non-JavaScript module`);
  const expected = await readFile(new URL('../' + url.pathname.slice(1), import.meta.url), 'utf8');
  assert.equal(await module.text(), expected, 'Published module must match the release');
  console.log(`PASS: ${url.pathname} served as ${mime}, matching release bytes`);
}
