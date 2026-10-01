# Tier-2 and tier-3 city modules (internal)

Same mechanics as docs/CITY-AND-BANK-SPEC.md section 2, smaller scope:

- Tier 2 city: hub (800–1,200 words) + LOCAL for the 8 services in `_data.TIER_SERVICES[2]`.
- Tier 3 city: hub (800–1,000 words) + LOCAL for the 3 services in `_data.TIER_SERVICES[3]`.
- One file per city: `site/content/c_city_<slug_with_underscores>.py`, `SLUG = "<slug>"`.
- Unit and hub crumbs: Orlando-unit towns → `[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")]`; Sarasota-unit towns → `[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")]` (unit is derived from the county in `_data.CITIES`).
- Six verifiable local facts per city across hub + LOCAL, each cited: who issues the driveway/right-of-way permit (city vs. county — check whether the place is incorporated; CDPs and communities like Lake Nona, Dr. Phillips, Horizon West, Celebration, Parrish, Osprey, Nokomis, Siesta Key, Englewood are unincorporated or part of a bigger city), county rules from research/facts.md parts 3a/3b, Census population/housing age, a real community/HOA/historic district only with a cited document, soils/water/flood/salt, water-management-district rules, distance via `_data.CITIES[slug]["miles"]`.
- Research the web for local facts beyond research/facts.md and cite them with `ext()`.

Hard-won rules (earlier writers had to rewrite whole modules for breaking these):
- Never reuse another city module's sentences, sentence shapes, lede template, price-arithmetic skeleton or scenario sizes. Write each lede and each scenario in a fresh shape. Generic facts (DEP turf rule, sinkhole lists, FEMA zones, watering orders) must be phrased differently from every existing page — `qa/cross_check.py` fails any shared run of 14+ words.
- `per()` already returns the full unit ("sq ft installed", "sq ft of wall face"); never append "installed" or "of wall face".
- Give `src()` calls short custom anchor text (`src("dep-rule", "the state turf rule")`) — default SOURCES labels contain em dashes and repeat across pages.
- At most 2 em dashes per page; "best" at most once; title ≠ H1; meta 120–160 chars; H1s must be unique site-wide (include the town name).
- Prices never differ by town; don't call price_note(); never claim track records, licenses, addresses or phones.
- Checks, from the project root, until clean: `python qa/check_module.py c_city_<slug>` and `python qa/cross_check.py c_city_<slug>`. Don't run site/build.py; don't edit other files.
