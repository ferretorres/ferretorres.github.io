# Immersive website redesign

Source: owner request, 27 October 2026. Extends [demo visual system](demo-visual-system.md).

## Problem and solution

The homepage makes buyers read repeated service descriptions before understanding the offer. Replace it with a visual journey: business problem → example workflow → implementation approach → credible delivery → contact. Reference TinyFish's visual explanations and Kore.ai's outcome-led browsing, with original artwork and copy.

## Scope and decisions

- Keep static GitHub Pages, existing English SEO URLs, canonical tags, service schema, and internal discovery paths.
- Warm ivory / forest green identity, custom phi-inspired vector mark, glass navigation and restrained motion. Retain the readable company name.
- Homepage: succinct value proposition, bespoke system illustration, three selectable workflows, architecture diagram, three engagement steps, delivery credibility, visible FAQs, direct email contact, useful service links.
- Shared identity, navigation, typography and accessibility refinements across existing pages.
- Explicitly illustrative synthetic examples. No invented customers, results, certifications, integration availability or delivery guarantees.
- No new dependencies, tracking, form providers, data storage or automatic email sends.
- Preserve pre-existing working-directory changes. Local preview and validation precede publication.

## User stories and acceptance criteria

1. Buyers understand AI consulting and implementation for European companies at a glance. **AC1**: one descriptive H1, concise copy, contact CTA and workflow illustration at desktop and mobile sizes.
2. Buyers explore knowledge, operations and finance examples. **AC2**: each explains input, AI processing, human control and output; mouse, touch and arrow/Home/End keyboard navigation work; links reach existing demos.
3. Buyers understand how work starts. **AC3**: discovery, working MVP, and production are distinct linked steps; no invented timeline or price.
4. Search visitors retain service content. **AC4**: existing indexable URLs stay in sitemap, assets and internal links resolve, metadata/schema remain valid, visible FAQs match homepage schema.
5. Visitors navigate comfortably. **AC5**: mobile menu works by keyboard/touch; visible focus, reduced motion and high contrast; no overflow at 375, 768 and 1440 pixels; useful without JavaScript.
6. Buyers can contact the company. **AC6**: project/demo links open correctly addressed drafts; clipboard success is reported only after a successful copy, with an honest failure state.
7. Branding is consistent. **AC7**: vector mark/favicon work small; shared header/footer and social previews match.

## Slices and verification

1. Brand assets, shared styling and homepage structure (AC1, AC3, AC7).
2. Workflow selection, mobile menu, contact behavior and progressive enhancement (AC2, AC5, AC6).
3. SEO/schema, social cards and regression checks (AC4, AC7).

Gate: `python3 scripts/check_site.py`, JavaScript syntax, changed-lines whitespace, desktop/mobile/tablet browser inspection, workflow and keyboard tests, contact-link inspection, JavaScript-disabled and reduced-motion/high-contrast checks, representative subpages, console/network. Record results in `specs/qa/immersive-redesign.md`.

## Challenge, risks and rollout

- Glass readability: strong text contrast and opaque surfaces; blur is decorative.
- Motion: no autoplay carousel, scroll hijacking or indefinite animations; respect reduced motion.
- Discovery: all examples are in initial HTML, visible without JavaScript; enhancement adds tab semantics.
- Header regression: verify long-title service, solution, demo and legal pages at narrow widths.
- Phi is a graphic inspiration, not a claim that Latin F belongs to Greek. Keep the company name.
- Rollback: local changes are reviewable; starting working-tree files preserved under `tmp/site-redesign-baseline/`. Use existing hosting only when authorized.
- Lead-provider, booking, analytics and approved case studies retain their completion-tracker revisit triggers. No backend expansion.

## Refinement and publication, 27 October 2026

The owner requested slightly more immersion, more workflow images, simplicity,
loading-time care, and direct publication. Publication is explicitly authorized.

- **AC8:** Three original SVG workflow illustrations explain discovery, MVP validation and production; each has meaningful alt text, intrinsic dimensions and lazy loading.
- **AC9:** Section entrances run once as they enter view; menu and workflow transitions are subtle. The hero heading is immediately readable. Reduced-motion users get static content, and content remains useful without JavaScript or IntersectionObserver.
- **AC10:** Remove the unused legacy stylesheet from the homepage while retaining it on secondary pages. Keep the homepage's complete local resource budget below 100 KB decoded, new workflow illustrations below 12 KB combined, and JavaScript below 8 KB. No animation library, font download, autoplay video or pointer/scroll polling.
- **AC11:** Recheck desktop/mobile/tablet behavior, keyboard tabs/menu, illustrations, source/SEO checks, and measured page bytes before publication. Push only an explicit website-file allowlist, use a reviewed feature-branch PR and rebase merge, then verify the live HTTPS site and new assets. Private accounting directories, temporary evidence and unrelated existing edits must not be published.

Release risks to check: stale mixed CSS/HTML assets (version the changed assets),
hidden or moving content (progressive enhancement and reduced-motion fallback),
accidentally included workspace files (inspect staged-file allowlist). Rollback is
the preceding public commit via a reviewed revert; no history rewrite.

Live verification identified Hostinger as the active custom-domain host. Keep
the GitHub Pages release as a mirror and publish a targeted website-file overlay
to Hostinger. Preserve the separate application and existing legal pages; restore
direct service URLs, retain old section entry points and version the favicon.

## Plum identity refinement

The owner asked to replace the familiar green/blue AI palette and common
typography with a pleasing purplish direction. Use warm ivory, muted plum,
dusty lilac and a structured humanist display face. Replace the large italic
serif treatment while retaining the visual workflow hierarchy and motion.

- Apply the palette consistently to shared styles, homepage, vector identity,
  workflow illustrations and social previews. Preserve content, URLs and behavior.
- Use one original, unmodified IBM Plex Sans Medium Latin1 WOFF2 file (21,960
  bytes, SIL OFL 1.1) for headings and brand text. Body text uses local humanist
  system fonts. This supersedes the earlier no-font-download constraint; retain
  the 100 KB homepage resource budget, now counting the preloaded font.
- Verify readable contrast, loaded font, no desktop/mobile overflow, workflow
  selection and menu behavior, and valid versioned SEO image URLs.
- Continue the authorized direct-publication workflow after review. Use only
  the active-host file overlay; retain the protected application and legal files.

## FT monogram refinement

The owner requested a more distinctive, professional and simple logo matching
plum colours, with direct publication. Replace the phi glyph with a custom solid
FT monogram: shared top bar, open counters and one diagonal terminal. Keep the
company name and existing typography. This supersedes the earlier phi direction.

- Apply one consistent silhouette to the header/footer, hero, workflow graphics,
  favicon, manifest and social cards. Keep the palette and page behaviour.
- Check recognition at 16/24/36 pixels, inverse use on plum, and loaded desktop
  and mobile layouts. Keep all assets vector except existing social JPEG cards;
  retain the 100 KB homepage budget. No dependencies or new font requests.
- Version changed asset references, retain SEO metadata, and run the static site
  gate, scoped Python checks and independent review. Publish committed public
  files through the existing overlay, preserving live legal/privacy/application
  paths. Risks: stale logos, small-size legibility, and unrelated-file overwrite.
  Mitigations: version keys, rendered size checks and an explicit file allowlist.
  Rollback: reviewed revert and the same overlay without deleting directories.
