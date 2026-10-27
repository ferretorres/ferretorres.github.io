import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';

const request = url => fetch(url, {cache: 'no-store', signal: AbortSignal.timeout(15000)});
const hash = value => createHash('sha256').update(value).digest('hex');
for (const path of ['', 'contact.html']) {
  const page = new URL(path, 'https://ferretorres.eu/');
  const response = await request(page);
  assert.equal(response.status, 200, 'Contact page must load');
  assert.ok(response.headers.get('content-type')?.startsWith('text/html'), 'Contact page must be HTML');
  const html = await response.text();
  const expectedPage = await readFile(new URL('../' + (path || 'index.html'), import.meta.url), 'utf8');
  assert.equal(hash(html), hash(expectedPage), `Published ${page.pathname} must match the release, including its module version`);
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
}
