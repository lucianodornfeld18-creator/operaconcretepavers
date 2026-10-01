# Writing guide — operaconcretepavers.com

Internal. Never rendered. Read all of it before writing a content module.

## Who is speaking

**Opera Concrete & Pavers** is a locally run concrete, pavers and artificial-turf contractor with **two crews / service units**:

- **Orlando unit** (Greater Orlando / Central Florida): Orange, Osceola, Seminole, Lake and Polk counties — Orlando, Kissimmee, Clermont, Oviedo, Winter Garden, Windermere and nearby towns.
- **Sarasota unit** (Suncoast): Sarasota and Manatee counties — Sarasota, Lakewood Ranch, Bradenton, Venice and nearby towns.

First person plural ("we"). Service-area business: **no street address, no showroom**. Each unit will get its own phone number later; until then, never print a phone number — use `tel("orlando")` / `tel("sarasota")` (they fall back to the estimate form automatically) or `contact()`. Never print an e-mail address.

**Never mention or link** ocoeeconcrete.com, lakewoodranchconcretefl.com, sarasotaconcrete.com, windermereconcrete.com, grovelandconcrete.com, kissimmeeconcrete.com, kissimmeeartificialturf.com, GCM Best Services, or any "sister", "partner" or "network" company. Do not cite any of those sites as a source either.

Public text is American English, written the way an estimator who has poured and laid a lot of this explains it to a homeowner standing on the driveway: plain, specific, a little opinionated, never salesy.

## Never invent (hard rule — a page with an invented fact gets deleted)

No street address, license number, insurance carrier, years in business, founding year, number of projects, reviews, star ratings, awards, staff names, owner name, brand of pavers/turf we "carry" or are "certified" by (ICPI/CMHA certification, Belgard/Tremron/Pavestone "authorized installer" — do not claim), warranty length or terms, financing partners, prices presented as "our price", photos described as our work, testimonials, "as seen in", response-time promises ("same day", "24 hours"), "licensed" (unverified — do not say licensed or unlicensed about us), "insured", "family-owned", "veteran-owned".

What you may say instead: market ranges with a source and date; what a good contractor does and why; what we do as a **method** ("we cut control joints the same day", "we compact the base in 2-inch lifts", "we pull a permit when the city requires one"). Methods are fine. Track records are not.

Do not describe the site's own production: no "keyword", "SEO", "search volume", "answer engine", "tier", "lead", "network", "sister", "partner contractors", "pipeline", "benchmark", "word count", "owner input", "pending", "TODO", "placeholder", "lorem", "stock photo".

## Verified facts you can use

**Only facts in `research/facts.md` (with their source ids in `research/sources.json`, loaded into `_data.SOURCES`)** plus the prices in `site/_prices.json` (use `price("concrete-driveway")`, `per("concrete-driveway")`, `price_note()`). Cite with `src("id")` inline or ids in `sources=[...]`. Anything local you add (permit rules, HOA/ARC process, soils, flood zones, housing age, community names) must be researched on the web **and cited** with `ext(url, "label")` inline or `(label, url)` tuples in `sources=[...]`. Prefer primary sources (city/county sites, flsenate.gov, floridabuilding.org, floridadep.gov, UF/IFAS, USDA NRCS, NOAA, FEMA, Census, ACI, CMHA/ICPI). If a jurisdiction publishes no rule, write that and point to the department. Never guess.

Prices: **never write a different price for a different city**. Price does not change by ZIP; access, demolition, soil, drainage, permits and HOA rules do. Say "market range", never "our price".

## Page mechanics

Every content module lives in `site/content/` as `c_<name>.py`, imports from `_helpers`, and exposes `get_pages()` returning a list of `page(...)` dicts. Read `site/_helpers.py` and `site/_data.py` first.

```python
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext, price, per, price_note, tel, contact, photo
```

- `lede` is the **answer capsule**: 40–70 words, stands alone if quoted by an AI system, contains a number with a unit, a date ("as of October 2026") and the place.
- Body is HTML built with `sec("H2", "<p>…</p>")`. Use H3 inside sections where it helps (`<h3>…</h3>`). H2s that answer a question are written as the literal question and open with a 40–70 word direct answer paragraph, then detail, then a table, list or steps where it helps.
- Tables: `table(caption, headers, rows, note)` — clear headers with units. AI systems quote tables.
- FAQs: `faqs=[faq("Question?", "Answer.")]` — 5–7 per commercial page, each answer 35–80 words, **never repeating a question owned by another page** (see `research/questions.csv`, column owner_page).
- Links only with the helpers (`svc("paver-patios")`, `city("sarasota")`, `cs("sarasota", "paver-patios")`, `post("slug", "anchor")`, `compare("slug", "anchor")`, `a("/cost/", "anchor")`). Descriptive, varied anchors; the same anchor at most twice per page. Every page links to at least 6 other internal pages in running text. Only link to routes that exist in `_data.py` / `_posts.py` (a link to a page not yet written renders as plain text, which is fine).
- Titles ≤ 60 characters where possible (65 max), keyword first, no "Best" on commercial pages. Meta 120–160 characters with a concrete fact. H1 differs from the title.

## Word counts (visible main text, measured by QA)

Home 3,000–4,500 · pillar 1,200–2,000 · service 1,800–2,800 · city×service 850–1,400 · city hub 800–1,600 · unit hub 1,000–1,800 · cost page 1,800–3,000 · permit 700–1,500 · post 1,200–2,500 · compare 1,000–1,800 · FAQ page 1,000+.

## Keywords without stuffing

The page's primary phrase goes in the title, H1, first 100 words, one H2 and the meta — then stop counting and write. Rotate synonyms naturally: "pavers / brick pavers / paving stones / interlocking pavers", "concrete / cement" (homeowners say cement; we can say "people call it a cement driveway" once), "pool deck / pool patio", "artificial turf / artificial grass / synthetic turf". Hard limits checked by QA: exact primary phrase ≤ 1.5% of words; no sentence of 8+ words repeated anywhere else on the site.

### "best … contractor" / "near me"

Never as a claim about ourselves ("we are the best", "#1", "top-rated", "leading"). Only as the customer's question or as criteria: *"How do you pick the best concrete contractor in Orlando?"*, *"Searching for paver installers near me? Check these five things first."* Frequency: home 2; service page 1; city hub 1 with the city name; city×service at most 1; FAQ hub 3.

## Style (QA fails the build on the banned list)

Banned: in today's, whether you're, look no further, it's important to note, it's worth noting, in conclusion, ultimately, at the end of the day, when it comes to, elevate, seamless, unlock, delve, robust, leverage, game-changer, transform your, dream yard, oasis, paradise, lush, pristine, we understand that, our team of experts, top-notch, state-of-the-art, cutting-edge, meticulous, comprehensive, hassle-free, peace of mind, stand the test of time, a testament to, nestled, vibrant, boasts, tapestry, one-stop shop, we've got you covered, utilize, in order to, let's dive in, here's the thing, say goodbye to, second to none, unparalleled. Track-record phrases are also banned: most of our, many of our, our customers, our clients, we've installed/built/done, years of experience, hundreds of, our portfolio. No emojis. No exclamation marks. No "Conclusion" or generic "Why choose us" sections. Em dashes: at most two per page. "ensure" at most once per page. No rhetorical-question openers. Not every section ends with a call to action.

Required: contractions; varied sentence and paragraph lengths; one specific checkable fact (number with unit, code section, soil series, temperature, depth, date, community name) every 120–150 words; concrete examples written as illustrations ("say you have a 24 × 20 ft two-car driveway in a 1990s Kissimmee subdivision…"), never as a job we completed; installer opinions with a reason ("we don't pour when the evaporation rate is high without a curing compound, because the surface dries before the slab underneath and crazes").

## Florida building facts worth using (details and sources in research/facts.md)

Residential flatwork is typically 4 in thick (Florida's residential code minimum for slabs is 3½ in) at 3,000–4,000 psi; driveways that see trucks, RVs or boat trailers go 5–6 in. Control joints at 24–36 times the slab thickness (8–12 ft for a 4 in slab; NRMCA CIP 6), cut to a quarter of the depth. Hot-weather concreting (ACI 305): concrete placed above 95 °F or with an evaporation rate over 0.2 lb/ft²/h cracks early — early starts, evaporation retarder, curing compound, wet curing; NRMCA says cure at least 3 days (do not cite "7 days / 70%" as a rule). Pavers (ICPI/CMHA Tech Spec 2): residential driveway base about 6 in of compacted aggregate on well-drained soil, 2–4 in more on wet/poorly drained soils, compacted to 98% standard Proctor; patios and walks thinner; 1 in bedding sand; edge restraint; 60 mm (2⅜ in) pavers are acceptable for residential driveways, 80 mm for heavier loads; no fixed resealing interval in Tech Spec 5. Soils: flatwoods (Myakka — the state soil — Smyrna, Immokalee, EauGallie, Pomona, Felda, Basinger) hold water within 0–18 in part of the year; ridge sands (Candler, Astatula, Tavares) drain excessively. Rainfall (NOAA 1991–2020): Orlando airport 51.45 in/yr, Sarasota–Bradenton airport 49.05 in/yr; rainy season roughly late May–mid October. Watering: in 2026 SWFWMD (Sarasota, Manatee, Polk) and SJRWMD Lake County are under emergency once-a-week orders — check facts.md for the exact orders and dates before writing about sod vs. turf. Sinkhole claims concentrate in west-central counties (Hernando, Pasco, Hillsborough); Orange is on the high-claims list; Sarasota/Manatee are not. Travertine and shell stone stay cooler underfoot than dark concrete pavers; no measured degree figures are verified, so don't print temperatures for deck materials. Coastal Sarasota/Manatee: salt air, flood zones (AE/VE), high water table. Live oaks: roots lift slabs; Orlando, Winter Park and Sarasota protect larger trees by ordinance (see facts.md).

## Florida law, carefully (see facts.md part 2)

- Licensing: F.S. 489.117(4)(a)1 lists "driveway or tennis court installation" and "decorative stone installation" among jobs for which no state or local license may be required. Structural concrete (foundations, slabs, footers, walls) falls under the state "structural masonry specialty contractor" certificate. Never say Opera is licensed or unlicensed; you may tell homeowners how to check any contractor on DBPR.
- Lien law: Notice of Commencement is required for improvements over $2,500 (F.S. 713.13 / 713.02(5)); write it exactly.
- Artificial turf: HB 683 (2025, ch. 2025-140) created F.S. 125.572, which limits local governments only; DEP Rule 62-308.100 effective May 19, 2026 sets the standard (natural infill, washed base, 10 ft from waterbodies unless seawall, no in-ground irrigation on turf, outside tree drip lines unless an arborist certifies, lots ≤ 1 acre). F.S. 720.3045 protects only turf not visible from the frontage/adjacent parcel. In 2026, F.S. 720.3035(1)(c) bars an HOA from requiring a building permit before it reviews a project.
