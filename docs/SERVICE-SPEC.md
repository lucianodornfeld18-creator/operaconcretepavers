# Service, pillar and unit pages (internal, never rendered)

Read docs/WRITING-GUIDE.md, docs/AGENT-BRIEF.md and research/facts.md first. Finished examples of the mechanics: site/content/c_home.py and site/content/c_hubs.py.

## Service page (kind "service")

```python
# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext, price, per, price_note, tel, contact, photo, offer
from _photos import for_service

def driveways():
    K = "concrete-driveways"
    pids = for_service(K, 3)
    body = "".join([
        sec("…", "<p>…</p>" + photo(pids[1], "caption describing only what is visible") if len(pids) > 1 else ""),
        …,
        "<!--AUTO:service-cities-->",      # the build inserts the list of town pages for this service here
        …,
    ])
    return page("/concrete-driveways/", "service", "<title ≤60, primary keyword first>", "<meta 120–160>", "<H1 ≠ title>",
                capsule("…40–70 words with the price range, a Florida fact, 'as of October 2026'…"), body,
                faqs=[…5–7 faq() — the questions research/questions.csv assigns to this URL…],
                sources=[…ids from research/sources.json and (label, url) tuples…],
                related=[(cost page route, "…"), (compare route, "…"), (post route, "…"), …],
                crumbs=[("Concrete", "/concrete/")], crumb="Concrete driveways", service=K,
                hero_photo=pids[0] if pids else None, offer=offer(SERVICES[K]["price"]), eyebrow="Concrete · Greater Orlando & Sarasota")

def get_pages():
    return [driveways(), …]
```

- 1,800–2,800 words of visible text. The page must stand on its own as the best answer on the web for the service in Florida: what it is, when to choose it, how we build it (spec table: thickness/base/joints/finish or paver/turf spec), the process step by step (`steps()` — also pass `howto=("How a … is built", [(step, text), …])` to page() for HowTo schema), Florida-specific problems and how the build avoids them, cost summary (one short section with the market range and a link to the cost guide — the cost page owns the detailed cost questions), permits/HOA summary with links to the county permit posts, care, and "how to choose a contractor" criteria (one "best … near me" phrasing allowed, as the customer's question).
- Use the questions research/questions.csv assigns to this URL (owner_page) as FAQ or as H2 questions. Don't answer questions owned by other pages beyond a linking sentence.
- At least 2 photos from `for_service(K, n)` inside the body if available (`photo(pid, caption)`; captions describe only what is visible — never "our project", never a city).
- Link to: the pillar, the cost guide (`_posts.cost_for(K)`), 1–2 compare pages, 3–5 posts from `_posts.POSTS` whose services include K, 2–3 sibling services, both unit pages (`/central-florida/`, `/sarasota-manatee/`), and 3–4 city×service pages via `cs("orlando", K)`, `cs("sarasota", K)` etc. (only cities whose tier includes K: tier 1 has all services; tier 2 has driveways, patios, pool decks, stamped, turf; tier 3 has concrete driveways, paver patios, turf).

## Pillar page (kind "pillar") — /concrete/ and /pavers/

1,200–2,000 words: what the family of services covers, how to choose among them (table), shared engineering facts (concrete: thickness, psi, joints, curing in heat; pavers: base, bedding sand, edge restraint, joint sand, sealing), a card grid of the services (use the same card markup as c_home._cards or a `<ul class="grid">`), links to every service in the family, the related cost guides, compares and posts. FAQ 4–6 not owned elsewhere. crumbs=[]; `form=True` is the default for pillars. `/artificial-turf/` is a service page, not a pillar.

## Unit page (kind "unit", unit="orlando" or "sarasota") — /central-florida/ and /sarasota-manatee/

1,000–1,800 words: the counties and towns this crew covers, the soils and weather of that region (from facts.md), the permit desks of that region in a table (from facts.md part 3a/3b), the HOAs and master-planned communities common there (only the ones with sources), the services with links to the city×service pages of the main towns, water restrictions in force in 2026, and "<!--AUTO:unit-cities-->" where the town list should appear. Pass `unit="orlando"` / `unit="sarasota"` so the form routes the lead to that crew. FAQ 4–6 about that region.
