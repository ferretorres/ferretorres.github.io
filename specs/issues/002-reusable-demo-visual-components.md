# Build: Reusable synthetic demo visual components

## Problem

Each demo page needs product-like visuals, but maintaining unrelated one-off HTML structures will make the site inconsistent and harder to iterate.

## User story

As a visitor, I want all demo previews to feel like parts of the same professional delivery system, so the company feels coherent and mature.

## Scope

- Add reusable HTML/CSS patterns for synthetic dashboards, control panels, workflow timelines, KPI rows, source cards, approval gates, and architecture panels.
- Keep implementation static and dependency-free.
- Ensure components work inside the existing design system.
- Support desktop and mobile without horizontal overflow.

## Acceptance criteria

- Shared CSS classes exist for demo screens and product panels.
- At least one demo page uses the new component system.
- Components are responsive at 375px and 1280px widths.
- Visuals are labeled as synthetic where needed.
- No new JavaScript dependency is added.

## Verification

- Run static checks.
- Open the upgraded demo page locally.
- Verify no horizontal overflow on mobile.
- Verify text does not overlap inside visual panels.
