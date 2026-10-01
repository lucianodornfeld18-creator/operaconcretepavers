# City modules and the block bank (internal, never rendered)

City × service pages (`/<city>-fl/<service>/`, e.g. `/kissimmee-fl/paver-driveways/`) are assembled by `site/_cityservice.py` from two hand-written sources:

1. **The city module** `site/content/c_city_<slug_with_underscores>.py` — everything that is true only of that town, written for each service separately, plus the city hub page `/<slug>-fl/`.
2. **The block bank** `site/bank/b_<service_with_underscores>.py` — technical blocks about the service, in several variants, so that two towns rarely show the same wording.

Read `docs/WRITING-GUIDE.md` and `docs/AGENT-BRIEF.md` first. Everything there applies.

## 1. Block bank

`site/bank/b_concrete_driveways.py` etc.:

```python
# -*- coding: utf-8 -*-
BLOCKS = {
  "base":    [("H2 variant 1", "<p>…</p>"), … N variants …],
  "build":   [ … N … ],
  "process": [ … N … ],
  "risks":   [ … N … ],
  "care":    [ … N … ],
}
```

- **N = 8** variants for: concrete-driveways, paver-driveways, concrete-patios, paver-patios, concrete-pool-decks, pool-deck-pavers, stamped-concrete, artificial-turf. **N = 5** for: concrete-walkways, concrete-slabs, concrete-repair, paver-sealing, retaining-walls.
- 80–120 words each, **each variant making a different point or using a different example**, not a reworded copy. H2s differ too and read like real headings ("Why a 4-inch slab isn't enough for a boat trailer").
- Placeholders `{city}` and `{county}` are replaced at build time; use `{city}` once or twice per variant so the sentence reads naturally ("On a typical {city} lot…"). Write so the text is true in BOTH regions (Greater Orlando sand ridges and flatwoods; coastal Sarasota/Manatee flatwoods with salt air and flood zones) — or phrase region-specific points conditionally ("if the lot sits in a coastal flood zone…", "on the sandy ridge soils west of Orlando…"), never asserting something about {city} that might be false for one of the 46 towns.
- Block meanings: **base** = what goes under it and why on Florida soil (subgrade, compaction, aggregate base, fill, drainage, water table); **build** = the spec (thickness, psi, reinforcement, joints, finish; or paver type, thickness, pattern, edge restraint, joint sand; or turf/infill/backing); **process** = how the job runs, day by day, and how long, including curing/inspection; **risks** = what goes wrong when it's done badly, and Florida-specific traps (heat and evaporation, afternoon storms, roots of live oaks, sinkholes vs. settlement, salt, hurricanes, irrigation overspray, HOA/permit missteps); **care** = upkeep for this service in Florida.
- Plain HTML strings (no helper calls inside the bank, so no links). Facts must come from `research/facts.md` or the writing guide; no prices except the published ranges in `site/_prices.json`, and only if useful; no invented numbers.
- No sentence of 8+ words may repeat anywhere in your file or any other bank file.

Check with `python qa/check_bank.py b_<service_with_underscores>` until it reports 0 issues.

## 2. City module

```python
# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, cs, post, compare, src, ext, price, per, tel, contact
from _cityservice import cityservice_pages

SLUG = "kissimmee"                       # must exist in _data.CITIES
SRC = [("City of Kissimmee — Building Division", "https://…"), …]   # every local source you used

HUB = page("/kissimmee-fl/", "city", "<title ≤60>", "<meta 120–160>", "<H1>", capsule("…40–70 words…"),
           "".join([sec("…", "…"), …, "<!--AUTO:city-services-->"]),
           faqs=[faq("…", "…"), …4–6…], sources=SRC, city=SLUG, crumbs=[("Service areas", "/service-areas/"), ("<unit name>", "<unit route>")], crumb="Kissimmee",
           related=[…unit hub, permit post for the county, 2 nearby city hubs, cost guide…], eyebrow="Concrete · Pavers · Turf in Kissimmee, FL")

LOCAL = {
  "concrete-driveways": {
     "title": "Concrete Driveways in Kissimmee, FL – <local angle>",     # ≤ 65 chars, unique
     "meta":  "…120–160 chars with a local fact…",
     "h1":    "…different from the title…",
     "lede":  capsule("…40–70 words: what it is here, the {price('concrete-driveway')} per sq ft market range, one local fact, 'as of October 2026'…"),
     "sections": [("H2 …", "<p>…</p>"), ("H2 …", "<p>…</p>")],   # two local sections, 120–180 words each
     "scenario": ("H2 …", "<p>Say you have a … sq ft … in <neighborhood type> …</p>"),      # 100–150 words, illustrative, with sq ft and the market price range arithmetic
     "faqs": [faq("…local question…", "…"), faq("…", "…"), faq("…", "…")],               # 3, unique to this page
     "sources": SRC,
  },
  …   # one entry per service in _data.TIER_SERVICES[tier of this city]
}

def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
```

### What "local" has to mean (the uniqueness gate)

Across the hub and the LOCAL entries, work in at least **six verifiable local facts**, each cited, spread so different services lean on different facts:

- which jurisdiction reviews permits (city vs. unincorporated county) for driveways / right-of-way aprons, patios, pool decks, walls — department name and link (see `research/facts.md` permits section); link our county permit post from `_posts.py`
- the water management district and the current watering rules (SJRWMD / SWFWMD — note the 2026 emergency orders in facts.md), which matter for turf vs. sod and for curing
- one or two real communities, HOAs, CDDs or historic districts and what their published architectural rules say about driveways, pavers, colors or turf — only if you can cite the document; otherwise describe the housing type without naming a rule
- the dominant soil series (USDA) and what it means for subgrade and drainage; flood zones for coastal towns (FEMA)
- when most homes were built (Census ACS or the city's history) and what that implies (original 1980s driveways cracking, narrow 1990s aprons, pool cages, live oaks)
- coastal salt air, lakes, canals, golf courses, conservation land, sinkhole-prone karst, slopes on the ridge
- distance from the unit's base city: use `_data.CITIES[slug]["miles"]` ("about N miles from Orlando/Sarasota") — never invent a drive time

Per service, make the local sections about *that service in that town*. Never the same paragraph with the service name swapped. No sentence of 8+ words may repeat between any two of your pages.

Prices never differ by town. Use `price("<key>")` / `per("<key>")` and do arithmetic inside the published range.

City hub word floor 800 (tier 1: aim 1,200+). City × service pages need ≥ 850 words including the bank blocks.

**Two checks, both mandatory, from the project root:** `python qa/check_module.py c_city_<slug>` and then `python qa/cross_check.py c_city_<slug>` (fails on a pair over 12% or a shared run of 14+ words with any page already built).
