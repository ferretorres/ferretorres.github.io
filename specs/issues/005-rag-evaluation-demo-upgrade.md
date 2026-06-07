# Upgrade: RAG evaluation guided demo visual

## Problem

RAG buyers often underestimate retrieval quality, evaluation, permissions, and monitoring. The demo should show that Ferre Torres B.V. treats RAG as a production system, not a chat UI.

## User story

As a technical buyer, I want to see how RAG quality is evaluated, so I can trust that the implementation will not be a brittle document chatbot.

## Scope

- Upgrade `demo-rag-evaluation.html`.
- Add a synthetic evaluation console with test questions, retrieved sources, answer quality, citation checks, permission checks, and reviewer feedback.
- Show common failure modes: stale source, weak retrieval, missing permission, unsupported answer.
- Add technical questions for scoping.

## Acceptance criteria

- Page visually communicates RAG evaluation and source grounding.
- Synthetic data is clearly labeled.
- Buyer can see the difference between retrieval, generation, citation, and review.
- CTA points to guided demo or project brief.

## Verification

- Browser desktop and mobile checks.
- Internal link check.
- SEO metadata check.
