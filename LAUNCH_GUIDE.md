# Ferre Torres B.V. launch guide

This file is for manual launch tasks that cannot be completed from the static GitHub Pages repo.

## 1. Google Search Console

1. Go to https://search.google.com/search-console
2. Add a Domain property: `ferretorres.eu`
3. Copy the TXT verification record Google provides.
4. In Hostinger DNS, add:
   - Type: `TXT`
   - Host/name: `@`
   - Value: Google verification value
   - TTL: default or `3600`
5. Verify in Search Console.
6. Submit sitemap: `https://ferretorres.eu/sitemap.xml`
7. In Catalan UI, use:
   - `Mapes del web` to submit only `sitemap.xml`.
   - `Inspeccio d'URL` to request indexing for individual pages.
8. If Search Console says the sitemap is HTML, the wrong URL was submitted as a sitemap. Remove that submitted entry and submit only `https://ferretorres.eu/sitemap.xml`.
9. Use URL Inspection and request indexing for:
   - `https://ferretorres.eu/`
   - `https://ferretorres.eu/ai-consultancy.html`
   - `https://ferretorres.eu/ai-opportunity-assessment.html`
   - `https://ferretorres.eu/ai-integration-roadmap.html`
   - `https://ferretorres.eu/ai-consultancy-netherlands.html`
   - `https://ferretorres.eu/ai-consultancy-rotterdam.html`
   - `https://ferretorres.eu/ai-consultancy-amsterdam.html`
   - `https://ferretorres.eu/ai-transformation-netherlands.html`
   - `https://ferretorres.eu/ai-consulting-for-ceos.html`
   - `https://ferretorres.eu/ai-consulting-for-cfos.html`
   - `https://ferretorres.eu/ai-consulting-for-ctos.html`
   - `https://ferretorres.eu/ai-consulting-for-enterprises.html`
   - `https://ferretorres.eu/company-brain-for-companies.html`
   - `https://ferretorres.eu/rag-consultant-netherlands.html`
   - `https://ferretorres.eu/ai-automation-consulting-europe.html`
   - `https://ferretorres.eu/ai-solutions.html`
   - `https://ferretorres.eu/ai-mvp-poc.html`
   - `https://ferretorres.eu/ai-demo-gallery.html`
   - `https://ferretorres.eu/ai-architecture.html`
   - `https://ferretorres.eu/delivery-patterns.html`
   - `https://ferretorres.eu/regulated-knowledge-assistant-pattern.html`
   - `https://ferretorres.eu/finance-reporting-automation-pattern.html`
   - `https://ferretorres.eu/industrial-intelligence-pattern.html`
   - `https://ferretorres.eu/project-intelligence-assistant-pattern.html`

## 2. Form capture

Recommended first provider: Formspree.

1. Go to https://formspree.io
2. Create a form for `jferre@ferretorres.eu`.
3. Copy the endpoint. It will look like `https://formspree.io/f/xxxxxxx`.
4. Send the endpoint to Codex.
5. Codex will add it to `window.FERRE_SITE_CONFIG.formEndpoint` and the form will submit automatically with email fallback.

## 3. Analytics

Recommended first provider: Plausible or Simple Analytics.

For Plausible:

1. Go to https://plausible.io
2. Add site: `ferretorres.eu`
3. Copy the tracking script.
4. Send the script to Codex.

Do not add Google Analytics by default unless there is a strong reason. Privacy-friendly analytics fits the B2B/GDPR positioning better.

## 4. Public profiles

Add the site URL to:

- LinkedIn profile website field: `https://ferretorres.eu/`
- GitHub profile: `https://ferretorres.eu/`
- Email signature
- Any consulting/freelance profiles
- Partner or vendor pages where appropriate

## 5. Proof collection template

For each anonymized project, write:

```text
Industry:
Problem:
What we built:
Time to first MVP:
Data/tools involved:
Users:
Outcome:
Reusable system:
What can be public:
What must stay confidential:
```

Send two or three completed notes to Codex. They can become approved proof pages.

## 6. First LinkedIn posts

### Post 1: AI consultancy

Most companies do not need another AI brainstorm.

They need one workflow where AI can prove value quickly:

- repeated manual work
- accessible company context
- clear users
- measurable operating impact
- a realistic path from MVP to production

That is the way we are positioning Ferre Torres B.V.: AI consultancy and AI-first implementation for companies that want working systems, not slide decks.

https://ferretorres.eu/ai-consultancy.html

### Post 2: Company Brain

The most useful AI system in a company is not always a chatbot.

Often it is a private operational memory:

- documents
- decisions
- metrics
- tickets
- meetings
- policies
- workflow context

That is what I mean by a Company Brain: a governed AI-ready core that can support assistants, dashboards, RAG, and agentic workflows.

https://ferretorres.eu/company-brain-for-companies.html

### Post 3: RAG implementation

RAG quality is not about connecting documents to a chat interface.

The real work is:

- source quality
- metadata
- permissions
- retrieval evaluation
- answer grounding
- feedback loops
- production monitoring

I created a short guided preview of how companies should think about RAG evaluation before rollout.

https://ferretorres.eu/demo-rag-evaluation.html

### Post 4: Finance intelligence

Dashboards are useful until every important question still requires manual interpretation.

AI finance intelligence should help explain:

- margin movement
- cash variance
- pricing signals
- forecast changes
- anomalies
- follow-up actions

Synthetic guided preview:

https://ferretorres.eu/demo-finance-intelligence.html

### Post 5: Agentic workflows

The safest useful agents are not fully autonomous.

They operate inside a workflow:

- retrieve context
- draft the next action
- use tools
- respect approval gates
- escalate exceptions
- leave an audit trail

That is where agentic AI becomes useful for companies.

https://ferretorres.eu/agentic-ai-workflows.html

### Post 6: Technical architecture

AI demos are useful, but technical buyers need to understand the operating architecture:

- data connectors
- permissions
- retrieval and vector search
- evaluation
- orchestration
- approval gates
- monitoring
- audit trails

I published the high-level architecture patterns we use when scoping AI systems for companies.

https://ferretorres.eu/ai-architecture.html

### Post 7: Proof patterns

Not every project can become a named public case study.

But buyers still need to understand implementation patterns:

- regulated knowledge assistants
- finance reporting automation
- industrial intelligence
- project intelligence assistants

These anonymized pages describe the problem, workflow, data, governance, MVP path, and reusable system without exposing confidential client work.

https://ferretorres.eu/delivery-patterns.html

### Post 8: AI opportunity assessment

Most companies have too many AI ideas and not enough clarity on which one should become a funded system.

The useful first step is an AI opportunity assessment:

- where is the workflow pain repeated?
- which data and tools are already available?
- who owns the business result?
- what would prove value in an MVP?
- what should not be built yet?

That is the gap between AI pressure and a buildable plan.

https://ferretorres.eu/ai-opportunity-assessment.html

### Post 9: AI integration roadmap

AI integration is not about adding a chatbot to every department.

The real question is how AI connects to the company operating system:

- workflows
- data sources
- dashboards
- permissions
- retrieval
- agents
- evaluations
- monitoring
- governance

A practical roadmap should tell the company what to build first, what to validate, and what becomes reusable infrastructure.

https://ferretorres.eu/ai-integration-roadmap.html
