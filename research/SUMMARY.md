# Opera Concrete & Pavers: keyword and question research

Prepared 2026-10-01 for operaconcretepavers.com (Orlando unit and Sarasota unit). Files in this folder:

- `keywords.csv`: 239 keywords, each with exactly one owner page
- `questions.csv`: 182 questions with IDs Q001 to Q182; near-duplicate variants are merged into the rationale
- `blog-plan.csv`: 68 blog posts
- `compare-plan.csv`: 12 comparison pages
- `cost-pages.csv`: 12 cost guides, each with its keyword cluster and question IDs

## Method

- **Search**: I ran about 35 web searches covering cost-guide SERPs, People-Also-Ask-style questions, competitor FAQ and blog pages in Orlando and Sarasota, county and city permit pages, HOA/ARC manuals, the Florida turf statute, UF/IFAS, and forum threads on Houzz, River Dave's, DISboards and the Golden Retriever forum.
- **Demand**: `demand_estimate` is a **relative estimate, not a search volume**. No keyword tool was available.
  - High: the term has its own national cost-guide page on Angi, HomeGuide or HomeAdvisor and many competing local pages.
  - Medium: Florida- or city-modified, or covered by several FL competitors.
  - Low: long-tail, local or niche.
  - Validate later with Google Search Console and Keyword Planner.
- **Ownership**: each keyword cluster and each question has exactly one `owner_page`.
  - City x service URL pattern: `/<city>-fl/<service>/`.
  - Questions under about 150 words go into FAQ blocks: 5 to 7 per service page, plus 5 FAQ hubs.
  - Topics that need 1,200+ words become blog posts.
- **Extra placement value**: `compare_page` was added to `placement` for 5 questions whose natural owner is a /compare/ page. An `id` column was added to questions.csv so cost-pages.csv can reference rows.
- **Price figures** in notes come from public cost guides and competitors. They are *market references*, not Opera's prices. Replace them with your own bid data before publishing.

## Site architecture implied

| Page type | Count | URLs |
|---|---|---|
| Home + regional hubs | | `/`, `/orlando-fl/`, `/sarasota-fl/` |
| City hubs | 46 | `/<city>-fl/` (30 Orlando unit + 16 Sarasota unit) |
| Service pages | 13 | |
| Cost guides | 12 | |
| Compare pages | 12 | |
| FAQ hubs | 5 | |
| Blog posts | 68 | |
| City x service pages | rest of the ~450 | only where unique local content exists |

## Sources consulted

- Angi: https://www.angi.com/articles/how-much-does-concrete-driveway-cost.htm ; https://www.angi.com/articles/brick-paver-patio-cost/fl/orlando ; https://www.angi.com/articles/how-much-does-stamped-concrete-patio-cost/fl/orlando ; https://www.angi.com/articles/how-much-does-it-cost-build-retaining-wall/fl/orlando ; https://www.angi.com/articles/cracks-concrete-driveway-repair-vs-replace/fl/orlando ; https://www.angi.com/articles/concrete-slab-cost/fl/orlando ; https://www.angi.com/articles/how-much-does-concrete-walkway-cost/fl/orlando ; https://www.angi.com/articles/travertine-pavers-cost.htm
- HomeGuide: https://homeguide.com/costs/concrete-driveway-cost ; https://homeguide.com/costs/concrete-slab-cost ; https://homeguide.com/costs/concrete-retaining-wall-cost
- HomeAdvisor: https://www.homeadvisor.com/cost/garages/install-a-concrete-driveway/ ; https://www.homeadvisor.com/cost/landscape/install-a-retaining-wall/
- Fixr: https://www.fixr.com/costs/retaining-wall-building ; Forbes Home: https://www.forbes.com/home-improvement/outdoor-living/retaining-wall-cost/
- FL cost guides / competitors: https://linkedconcrete.com/concrete-driveway-cost-florida/ ; https://linkedconcrete.com/stamped-concrete-cost-florida/ ; https://www.chcconcrete.net/2026/03/10/stamped-concrete-driveway-cost/ ; https://daydreamoutdoor.com/post/paver-installation-cost-orlando ; https://handys.now/paver-cost-in-sarasota-2026-7-materials-real-installed-prices-and-what-nobody-tells-you-about-the-base/ ; https://www.tuscanpavingstone.com/home/search/pavers-cost-sarasota/ ; https://wellbuiltflorida.com/travertine-pool-deck-cost/ ; https://craft-pavers.com/pricing/ ; https://goldenoutdoorsolutions.com/paver-driveway-cost-florida/ ; https://www.castlecleanandseal.com/articles/paver-sealing-cost-central-florida ; https://artificialturftampa.com/artificial-turf-installation-cost-florida-2026-guide/ ; https://magnoliaturf.com/how-much-is-turf-per-square-foot/ ; https://concretesolutionsfl.com/blog/pool-deck-resurfacing-cost-south-florida-2026/ ; https://linkedconcrete.com/pool-deck-resurfacing-options-florida/
- Orlando competitors/FAQ: https://www.localpaversllc.com/post/blog-paver-permits-orange-county-orlando ; https://www.localpaversllc.com/post/blog-pavers-over-concrete-pool-deck-orlando ; https://www.localpaversllc.com/post/blog-travertine-vs-concrete-pavers-pool-deck ; https://www.groundsource.pro/blog/comparing-concrete-vs-paver-patios-driveways-fl ; https://orlandoconcretecrew.com/resurfacing-vs-replacing-a-driveway/ ; https://ocoeeconcrete.com/blog/concrete-cost-orlando/
- Sarasota competitors: https://sarasotaconcretecompany.com/ ; https://theconcretetruck.com/concrete-services ; https://lwrconcretepavers.com/ ; https://www.manasotaonline.com/blog/articles/how-to-fix-sunken-pavers-in-venice-fl-causes-solutions ; https://magnoliaturf.com/artificial-grass-in-sarasota/ ; https://tropicalgardenslandscape.com/blog/will-i-need-permits-for-landscaping-sarasota-fl
- Permits / government: https://www.orangecountyfl.net/PermitsLicenses/DoINeedaPermit.aspx ; https://www.orlando.gov/Building-Development/Permits-Inspections/Other/Apply-for-an-Engineering-Permit ; https://ocoee.org/Faq.aspx?QID=181 ; https://www.seminolecountyfl.gov/core/fileparse.php/3293/urlt/residential_driveway_permit_application.pdf ; https://www.mymanatee.org/media/docs/default-source/development-services-department-documents/development-services-department-documents/permitting/inspections-required-for-paver-driveways-102821.pdf ; https://www.mymanatee.org/media/docs/default-source/development-services-department-documents/development-services-department-documents/permitting/driveway-appl-pdf-2022.pdf ; https://www.districtgov.org/wp-content/uploads/2024/06/District-three-ARCManual.pdf (Lakewood Ranch ARC)
- HOA / turf law: https://www.floridacondohoalawblog.com/2023/11/29/the-effect-of-section-720-3045-florida-statute-on-homeowner-association/ ; https://www.theorlandolawgroup.com/blog/all/astroturf-your-backyard/ ; https://moderngroundsfl.com/artificial-turf-installation-florida-hb-683-what-florida-homeowners-need-to-know/
- UF/IFAS (turf heat/environment): https://blogs.ifas.ufl.edu/news/2025/07/30/scorching-temps-from-california-turf-raises-questions-about-artificial-turf-xeriscaping-in-humid-states-like-florida/ ; https://blogs.ifas.ufl.edu/orangeco/2025/04/15/synthetic-turf-and-the-environment/
- Florida problems: https://puppaversinc.com/paver-knowledge-base/why-pavers-sink-in-south-florida-and-how-to-prevent-it/ ; https://pandapavers.com/blog/florida-soil-and-paver-installation/ ; https://swflpaverguide.com/how-often-should-pavers-be-sealed/ ; https://www.alliancepavers.com/blog/how-florida-climate-affects-your-pavers-and-hardscaping ; https://www.hdsurfacesolutions.com/blog/polymeric-sand-vs-regular-joint-sand-for-fl-pavers/ ; https://swpavers.com/travertine-pool-deck-care-guide-sw-florida/ ; https://croftconcrete.com/pour-concrete-in-rain/ ; https://concretesolutionsfl.com/blog/concrete-curing-florida-heat/ ; https://linkedconcrete.com/fix-cracked-concrete-florida/ ; https://concretesolutionsfl.com/blog/best-concrete-driveway-finishes-florida/ ; https://www.concretenetwork.com/concrete/concrete_driveways/how-long-before-you-can-drive-on-concrete.html
- Forums/discussions (phrasing): https://www.riverdavesplace.com/forums/threads/stamped-concrete-for-pool-decking-vs-travertine.206497/ ; https://www.riverdavesplace.com/forums/threads/tavertine-vs-cooldeck.233752/ ; https://www.houzz.com/discussions/3740278/pool-deck-travertine-or-brick-pavers ; https://www.disboards.com/threads/anybody-here-have-stamped-concrete.3271057/ ; https://www.goldenretrieverforum.com/threads/pros-cons-of-artificial-turf-in-the-backyard.514043/

## Top 100 keywords by estimated demand

Ranked by estimate tier, then commercial before informational. The order inside a tier is judgment, not volume.

| # | Keyword | Intent | Demand (est.) | Owner page |
|---|---|---|---|---|
| 1 | concrete driveway | commercial | High | `/concrete-driveways/` |
| 2 | concrete patio | commercial | High | `/concrete-patios/` |
| 3 | pool deck resurfacing | commercial | High | `/concrete-pool-decks/` |
| 4 | stamped concrete | commercial | High | `/stamped-concrete/` |
| 5 | stamped concrete patio | commercial | High | `/stamped-concrete/` |
| 6 | concrete slab | commercial | High | `/concrete-slabs/` |
| 7 | concrete repair | commercial | High | `/concrete-repair/` |
| 8 | paver driveway | commercial | High | `/paver-driveways/` |
| 9 | paver patio | commercial | High | `/paver-patios/` |
| 10 | pool deck pavers | commercial | High | `/pool-deck-pavers/` |
| 11 | paver sealing | commercial | High | `/paver-sealing/` |
| 12 | retaining wall | commercial | High | `/retaining-walls/` |
| 13 | artificial turf installation | commercial | High | `/artificial-turf/` |
| 14 | artificial grass installers near me | commercial | High | `/artificial-turf/` |
| 15 | concrete contractor near me | local | High | `/` |
| 16 | concrete contractors near me | local | High | `/` |
| 17 | concrete company near me | local | High | `/` |
| 18 | paver installers near me | local | High | `/` |
| 19 | paver contractors near me | local | High | `/` |
| 20 | concrete contractor orlando | local | High | `/orlando-fl/` |
| 21 | concrete contractors orlando fl | local | High | `/orlando-fl/` |
| 22 | concrete contractor sarasota | local | High | `/sarasota-fl/` |
| 23 | concrete contractors sarasota fl | local | High | `/sarasota-fl/` |
| 24 | concrete driveway cost | informational | High | `/concrete-driveway-cost/` |
| 25 | how much does a concrete driveway cost | informational | High | `/concrete-driveway-cost/` |
| 26 | concrete driveway cost per square foot | informational | High | `/concrete-driveway-cost/` |
| 27 | concrete patio cost | informational | High | `/concrete-patio-cost/` |
| 28 | stamped concrete cost | informational | High | `/stamped-concrete-cost/` |
| 29 | stamped concrete cost per square foot | informational | High | `/stamped-concrete-cost/` |
| 30 | concrete slab cost | informational | High | `/concrete-slab-cost/` |
| 31 | concrete slab cost per square foot | informational | High | `/concrete-slab-cost/` |
| 32 | paver driveway cost | informational | High | `/paver-driveway-cost/` |
| 33 | paver patio cost | informational | High | `/paver-patio-cost/` |
| 34 | paver patio cost per square foot | informational | High | `/paver-patio-cost/` |
| 35 | paver patio ideas | informational | High | `/blog/paver-patio-ideas-florida/` |
| 36 | retaining wall cost | informational | High | `/retaining-wall-cost/` |
| 37 | artificial turf cost | informational | High | `/artificial-turf-cost/` |
| 38 | artificial turf cost per square foot | informational | High | `/artificial-turf-cost/` |
| 39 | pavers vs concrete driveway | informational | High | `/compare/pavers-vs-concrete-driveway/` |
| 40 | stamped concrete vs pavers | informational | High | `/compare/stamped-concrete-vs-pavers/` |
| 41 | how long before you can drive on new concrete | informational | High | `/concrete-driveways/` |
| 42 | residential concrete contractor | commercial | Medium | `/` |
| 43 | concrete driveway installation | commercial | Medium | `/concrete-driveways/` |
| 44 | concrete driveway contractors | commercial | Medium | `/concrete-driveways/` |
| 45 | concrete driveway replacement | commercial | Medium | `/concrete-driveways/` |
| 46 | new concrete driveway | commercial | Medium | `/concrete-driveways/` |
| 47 | driveway extension concrete | commercial | Medium | `/blog/driveway-widening-and-extensions-florida/` |
| 48 | concrete patio installation | commercial | Medium | `/concrete-patios/` |
| 49 | concrete patio contractors near me | commercial | Medium | `/concrete-patios/` |
| 50 | concrete patio extension / extend lanai slab | commercial | Medium | `/concrete-patios/` |
| 51 | concrete pool deck | commercial | Medium | `/concrete-pool-decks/` |
| 52 | kool deck / cool deck resurfacing | commercial | Medium | `/concrete-pool-decks/` |
| 53 | pool deck repair | commercial | Medium | `/concrete-pool-decks/` |
| 54 | stamped concrete driveway | commercial | Medium | `/stamped-concrete/` |
| 55 | stamped concrete pool deck | commercial | Medium | `/stamped-concrete/` |
| 56 | stamped concrete contractors near me | commercial | Medium | `/stamped-concrete/` |
| 57 | concrete sidewalk installation | commercial | Medium | `/concrete-walkways/` |
| 58 | concrete walkway | commercial | Medium | `/concrete-walkways/` |
| 59 | concrete slab for shed | commercial | Medium | `/concrete-slabs/` |
| 60 | concrete pad for shed near me | commercial | Medium | `/concrete-slabs/` |
| 61 | concrete driveway repair | commercial | Medium | `/concrete-repair/` |
| 62 | concrete resurfacing | commercial | Medium | `/concrete-repair/` |
| 63 | driveway resurfacing | commercial | Medium | `/concrete-repair/` |
| 64 | concrete crack repair | commercial | Medium | `/concrete-repair/` |
| 65 | concrete leveling / sunken slab repair | commercial | Medium | `/concrete-repair/` |
| 66 | paver driveway installation | commercial | Medium | `/paver-driveways/` |
| 67 | brick paver driveway | commercial | Medium | `/paver-driveways/` |
| 68 | paver driveway contractors near me | commercial | Medium | `/paver-driveways/` |
| 69 | paver patio installation | commercial | Medium | `/paver-patios/` |
| 70 | paver walkway | commercial | Medium | `/paver-patios/` |
| 71 | paver patio contractors near me | commercial | Medium | `/paver-patios/` |
| 72 | backyard pavers / lanai pavers | commercial | Medium | `/paver-patios/` |
| 73 | travertine pool deck | commercial | Medium | `/pool-deck-pavers/` |
| 74 | travertine pavers installation | commercial | Medium | `/pool-deck-pavers/` |
| 75 | pavers over pool deck | commercial | Medium | `/pool-deck-pavers/` |
| 76 | paver sealing near me | commercial | Medium | `/paver-sealing/` |
| 77 | paver cleaning and sealing | commercial | Medium | `/paver-sealing/` |
| 78 | paver repair | commercial | Medium | `/paver-sealing/` |
| 79 | retaining wall contractors near me | commercial | Medium | `/retaining-walls/` |
| 80 | paver retaining wall / block retaining wall | commercial | Medium | `/retaining-walls/` |
| 81 | synthetic turf | commercial | Medium | `/artificial-turf/` |
| 82 | pet turf / artificial grass for dogs | commercial | Medium | `/artificial-turf/` |
| 83 | putting green installation | commercial | Medium | `/artificial-turf/` |
| 84 | best concrete contractor sarasota | commercial | Medium | `/blog/how-to-choose-a-concrete-contractor-sarasota/` |
| 85 | best paver company orlando | commercial | Medium | `/blog/how-to-choose-a-paver-contractor-orlando/` |
| 86 | hardscape contractor near me | local | Medium | `/` |
| 87 | concrete contractor central florida | local | Medium | `/orlando-fl/` |
| 88 | paver company orlando | local | Medium | `/orlando-fl/` |
| 89 | concrete contractor kissimmee | local | Medium | `/kissimmee-fl/` |
| 90 | concrete contractor clermont fl | local | Medium | `/clermont-fl/` |
| 91 | concrete contractor winter garden fl | local | Medium | `/winter-garden-fl/` |
| 92 | pavers sarasota fl | local | Medium | `/sarasota-fl/` |
| 93 | concrete contractor bradenton | local | Medium | `/bradenton-fl/` |
| 94 | concrete contractor lakewood ranch | local | Medium | `/lakewood-ranch-fl/` |
| 95 | concrete contractor venice fl | local | Medium | `/venice-fl/` |
| 96 | concrete driveway orlando | local | Medium | `/orlando-fl/concrete-driveways/` |
| 97 | concrete driveway sarasota | local | Medium | `/sarasota-fl/concrete-driveways/` |
| 98 | stamped concrete orlando | local | Medium | `/orlando-fl/stamped-concrete/` |
| 99 | paver driveway orlando | local | Medium | `/orlando-fl/paver-driveways/` |
| 100 | paver patio orlando | local | Medium | `/orlando-fl/paver-patios/` |

## Top 100 questions

Ordered by placement priority: cost and service-page FAQs first (closest to revenue), then compare pages, blog posts and FAQ hubs.

| # | ID | Question | Owner | Placement |
|---|---|---|---|---|
| 1 | Q114 | How much does a concrete driveway cost in Florida? | `/concrete-driveway-cost/` | cost_page |
| 2 | Q115 | How much does it cost to replace a 2-car driveway? | `/concrete-driveway-cost/` | cost_page |
| 3 | Q116 | Is a concrete driveway cheaper in Orlando or Sarasota? | `/concrete-driveway-cost/` | cost_page |
| 4 | Q117 | How much does a 12x12 concrete patio cost? | `/concrete-patio-cost/` | cost_page |
| 5 | Q118 | Is a concrete patio cheaper than a paver patio? | `/concrete-patio-cost/` | cost_page |
| 6 | Q119 | How much does stamped concrete cost per square foot in Florida? | `/stamped-concrete-cost/` | cost_page |
| 7 | Q120 | Why does stamped concrete cost more than plain concrete? | `/stamped-concrete-cost/` | cost_page |
| 8 | Q121 | How much does a travertine pool deck cost? | `/pool-deck-cost/` | cost_page |
| 9 | Q122 | How much does it cost to resurface a pool deck in Florida? | `/pool-deck-cost/` | cost_page |
| 10 | Q123 | How much does it cost to put pavers over an existing pool deck? | `/pool-deck-cost/` | cost_page |
| 11 | Q124 | How much does a 12x12 concrete slab cost? | `/concrete-slab-cost/` | cost_page |
| 12 | Q125 | How much does a yard of concrete cost in Florida? | `/concrete-slab-cost/` | cost_page |
| 13 | Q126 | How much does a concrete sidewalk or walkway cost per square foot? | `/concrete-walkway-cost/` | cost_page |
| 14 | Q127 | How much does it cost to repair a cracked concrete driveway? | `/concrete-repair-cost/` | cost_page |
| 15 | Q128 | How much does concrete leveling cost? | `/concrete-repair-cost/` | cost_page |
| 16 | Q129 | How much does a paver driveway cost in Florida? | `/paver-driveway-cost/` | cost_page |
| 17 | Q130 | Are paver driveways more expensive than concrete? | `/paver-driveway-cost/` | cost_page |
| 18 | Q131 | How much does a 400 sq ft paver patio cost? | `/paver-patio-cost/` | cost_page |
| 19 | Q132 | How much do pavers cost per square foot installed? | `/paver-patio-cost/` | cost_page |
| 20 | Q133 | How much does it cost to seal pavers? | `/paver-sealing-cost/` | cost_page |
| 21 | Q134 | Is sealing pavers worth the money? | `/paver-sealing-cost/` | cost_page |
| 22 | Q135 | How much does a retaining wall cost per linear foot? | `/retaining-wall-cost/` | cost_page |
| 23 | Q136 | How much does artificial turf cost in Florida? | `/artificial-turf-cost/` | cost_page |
| 24 | Q137 | How much does a backyard putting green cost? | `/artificial-turf-cost/` | cost_page |
| 25 | Q138 | Are there rebates for replacing grass with artificial turf in Florida? | `/artificial-turf-cost/` | cost_page |
| 26 | Q001 | How long before I can drive on a new concrete driveway? | `/concrete-driveways/` | faq_on_service_page |
| 27 | Q002 | How thick should a concrete driveway be in Florida? | `/concrete-driveways/` | faq_on_service_page |
| 28 | Q003 | How long does a concrete driveway last in Florida? | `/concrete-driveways/` | faq_on_service_page |
| 29 | Q004 | Do you use rebar, wire mesh or fiber in driveways? | `/concrete-driveways/` | faq_on_service_page |
| 30 | Q005 | How long does it take to replace a concrete driveway? | `/concrete-driveways/` | faq_on_service_page |
| 31 | Q006 | Do you remove and haul away the old driveway? | `/concrete-driveways/` | faq_on_service_page |
| 32 | Q007 | Can you extend my existing concrete patio or lanai slab? | `/concrete-patios/` | faq_on_service_page |
| 33 | Q008 | How thick should a concrete patio be? | `/concrete-patios/` | faq_on_service_page |
| 34 | Q009 | Can a concrete patio hold a hot tub, pergola or outdoor kitchen? | `/concrete-patios/` | faq_on_service_page |
| 35 | Q010 | What finishes can I choose for a concrete patio? | `/concrete-patios/` | faq_on_service_page |
| 36 | Q011 | How do you make sure water drains away from the house? | `/concrete-patios/` | faq_on_service_page |
| 37 | Q012 | What is Kool Deck and can it be resurfaced? | `/concrete-pool-decks/` | faq_on_service_page |
| 38 | Q013 | How long does pool deck resurfacing last in Florida? | `/concrete-pool-decks/` | faq_on_service_page |
| 39 | Q014 | Can a cracked pool deck be resurfaced, or does it need replacing? | `/concrete-pool-decks/` | faq_on_service_page |
| 40 | Q015 | Do I need to drain the pool for pool deck work? | `/concrete-pool-decks/` | faq_on_service_page |
| 41 | Q016 | How soon can we use the pool deck after resurfacing? | `/concrete-pool-decks/` | faq_on_service_page |
| 42 | Q017 | Can you replace the pool coping at the same time? | `/concrete-pool-decks/` | faq_on_service_page |
| 43 | Q018 | Is stamped concrete slippery when wet? | `/stamped-concrete/` | faq_on_service_page |
| 44 | Q019 | Does stamped concrete crack? | `/stamped-concrete/` | faq_on_service_page |
| 45 | Q020 | How often does stamped concrete need resealing in Florida? | `/stamped-concrete/` | faq_on_service_page |
| 46 | Q021 | Can stamped concrete be installed over my existing slab? | `/stamped-concrete/` | faq_on_service_page |
| 47 | Q022 | How long does stamped concrete last? | `/stamped-concrete/` | faq_on_service_page |
| 48 | Q023 | Which stamped concrete colors stay coolest around a pool? | `/stamped-concrete/` | faq_on_service_page |
| 49 | Q024 | How wide should a front walkway be? | `/concrete-walkways/` | faq_on_service_page |
| 50 | Q025 | Can you build a walkway from the driveway to the backyard or side gate? | `/concrete-walkways/` | faq_on_service_page |
| 51 | Q026 | How far apart should joints be in a concrete walkway? | `/concrete-walkways/` | faq_on_service_page |
| 52 | Q027 | Can you replace just one cracked section of my walkway? | `/concrete-walkways/` | faq_on_service_page |
| 53 | Q028 | Can a concrete walkway be colored or stamped to match my patio? | `/concrete-walkways/` | faq_on_service_page |
| 54 | Q029 | What size slab do I need for my shed? | `/concrete-slabs/` | faq_on_service_page |
| 55 | Q030 | Can you pour a slab for a detached garage or carport? | `/concrete-slabs/` | faq_on_service_page |
| 56 | Q031 | Do you pour pads for generators, AC units and pool equipment? | `/concrete-slabs/` | faq_on_service_page |
| 57 | Q032 | How do you keep a slab from settling in sandy Florida soil? | `/concrete-slabs/` | faq_on_service_page |
| 58 | Q033 | Do you pour house foundations or room additions? | `/concrete-slabs/` | faq_on_service_page |
| 59 | Q034 | What is the smallest slab or job you will take? | `/concrete-slabs/` | faq_on_service_page |
| 60 | Q035 | Can you repair just the cracked part of my driveway? | `/concrete-repair/` | faq_on_service_page |
| 61 | Q036 | Does crack filler work on concrete driveway cracks? | `/concrete-repair/` | faq_on_service_page |
| 62 | Q037 | How long does concrete resurfacing last on a driveway? | `/concrete-repair/` | faq_on_service_page |
| 63 | Q038 | Can you fix a trip hazard where a slab has lifted? | `/concrete-repair/` | faq_on_service_page |
| 64 | Q039 | Can you level a sunken concrete slab? | `/concrete-repair/` | faq_on_service_page |
| 65 | Q040 | Will the repaired section match my old concrete? | `/concrete-repair/` | faq_on_service_page |
| 66 | Q041 | Are pavers strong enough for a driveway? | `/paver-driveways/` | faq_on_service_page |
| 67 | Q042 | How thick are driveway pavers compared with patio pavers? | `/paver-driveways/` | faq_on_service_page |
| 68 | Q043 | Do paver driveways need edge restraints? | `/paver-driveways/` | faq_on_service_page |
| 69 | Q044 | Can you add pavers just to the apron or as a border on my concrete driveway? | `/paver-driveways/` | faq_on_service_page |
| 70 | Q045 | How long does a paver driveway installation take? | `/paver-driveways/` | faq_on_service_page |
| 71 | Q046 | Will new pavers change the height at my garage door? | `/paver-driveways/` | faq_on_service_page |
| 72 | Q047 | How long does it take to install a paver patio? | `/paver-patios/` | faq_on_service_page |
| 73 | Q048 | Can you match new pavers to my existing driveway or pool deck pavers? | `/paver-patios/` | faq_on_service_page |
| 74 | Q049 | How deep is the base under a paver patio in Florida? | `/paver-patios/` | faq_on_service_page |
| 75 | Q050 | Will a paver patio drain during heavy rain? | `/paver-patios/` | faq_on_service_page |
| 76 | Q051 | Do pavers fade in the Florida sun? | `/paver-patios/` | faq_on_service_page |
| 77 | Q052 | Can you install a paver walkway around the side of the house? | `/paver-patios/` | faq_on_service_page |
| 78 | Q053 | Will pavers over my existing pool deck end up higher than the coping? | `/pool-deck-pavers/` | faq_on_service_page |
| 79 | Q054 | Is travertine a good choice for a saltwater pool? | `/pool-deck-pavers/` | faq_on_service_page |
| 80 | Q055 | Is travertine slippery when wet? | `/pool-deck-pavers/` | faq_on_service_page |
| 81 | Q056 | Can you install new paver or travertine coping? | `/pool-deck-pavers/` | faq_on_service_page |
| 82 | Q057 | What size travertine pavers are best for a pool deck? | `/pool-deck-pavers/` | faq_on_service_page |
| 83 | Q058 | Can pavers be installed inside a screen enclosure without removing it? | `/pool-deck-pavers/` | faq_on_service_page |
| 84 | Q059 | Does a travertine pool deck have to be sealed? | `/pool-deck-pavers/` | faq_on_service_page |
| 85 | Q060 | How often should pavers be sealed in Florida? | `/paver-sealing/` | faq_on_service_page |
| 86 | Q061 | How long should I wait to seal new pavers? | `/paver-sealing/` | faq_on_service_page |
| 87 | Q062 | How long after sealing can I walk or drive on my pavers? | `/paver-sealing/` | faq_on_service_page |
| 88 | Q063 | Can sunken pavers be re-leveled without new pavers? | `/paver-sealing/` | faq_on_service_page |
| 89 | Q064 | Can you replace a few cracked or stained pavers? | `/paver-sealing/` | faq_on_service_page |
| 90 | Q065 | Does sealing pavers stop weeds and ants? | `/paver-sealing/` | faq_on_service_page |
| 91 | Q066 | Why did my pavers turn white or cloudy after sealing? | `/paver-sealing/` | faq_on_service_page |
| 92 | Q067 | Does a retaining wall need drainage behind it? | `/retaining-walls/` | faq_on_service_page |
| 93 | Q068 | How tall can a retaining wall be before it needs an engineer? | `/retaining-walls/` | faq_on_service_page |
| 94 | Q069 | Can you build a seat wall around a patio or fire pit? | `/retaining-walls/` | faq_on_service_page |
| 95 | Q070 | What is the difference between a retaining wall and a seat wall? | `/retaining-walls/` | faq_on_service_page |
| 96 | Q071 | Do you build seawalls? | `/retaining-walls/` | faq_on_service_page |
| 97 | Q072 | How long does a block retaining wall last? | `/retaining-walls/` | faq_on_service_page |
| 98 | Q073 | How long does artificial turf last in the Florida sun? | `/artificial-turf/` | faq_on_service_page |
| 99 | Q074 | Does artificial turf drain during heavy rain? | `/artificial-turf/` | faq_on_service_page |
| 100 | Q075 | What goes under artificial turf in Florida? | `/artificial-turf/` | faq_on_service_page |

## Cannibalization map

| Pages at risk | How the split was decided |
|---|---|
| /concrete-driveways/ vs /concrete-repair/ | Driveways owns new pours and full replacement (tear-out). Repair owns cracks, section fixes, resurfacing, leveling. Decision content (resurface vs replace) sits on /compare/resurface-vs-replace-concrete/ and both pages link to it. |
| /concrete-repair/ vs /concrete-pool-decks/ | Pool-deck resurfacing (Kool Deck, spray, overlays) is owned by /concrete-pool-decks/. /concrete-repair/ mentions pool decks only in one link line. |
| /stamped-concrete/ vs /concrete-patios/ and /concrete-driveways/ | Any query containing 'stamped' goes to /stamped-concrete/ (patio, driveway, pool deck). Patio and driveway pages cover plain/broom/salt finishes and link out for stamped. |
| /paver-patios/ vs /paver-driveways/ vs /pool-deck-pavers/ | Split by surface: patio + walkways / driveways / pool decks (travertine, shellstone, coping). The generic query 'cost of pavers installed' goes to /paver-patio-cost/. |
| /pool-deck-pavers/ vs /concrete-pool-decks/ | Split by material family (pavers/travertine vs poured/resurfaced). Both pool deck price sets live on ONE /pool-deck-cost/ page so cost never splits. The choice between them is /compare/pavers-vs-concrete-pool-deck/ and, for owners of existing Kool Deck, /compare/cool-deck-vs-pavers-vs-travertine/. |
| /paver-sealing/ vs /blog/why-pavers-sink-in-florida/ and related blog posts | Service page owns commercial fix intent (re-leveling, re-sanding, sealing). Blog posts own the 'why' (sinking, efflorescence, mold, ants) and link to the service page. FAQ 'why did my sealer turn cloudy' (blushing) is different from the efflorescence post. |
| Service page vs cost page (e.g. /paver-driveways/ vs /paver-driveway-cost/) | Every 'cost/price/per square foot' query goes to the cost page. Service pages show one short 'typical range' line linking to the cost page, and have no cost H2. |
| Cost page vs city x service page | Rule: cost queries for the two anchor cities (Orlando, Sarasota) stay on the cost page (regional table). Cost queries for smaller cities (e.g. 'concrete driveway price kissimmee') go to the city x service page's local price block. Low volume, so the split rarely matters. |
| City hub (/orlando-fl/) vs city x service (/orlando-fl/paver-patios/) | Hub owns '<trade> contractor <city>' (concrete contractor orlando, paver company orlando). City x service owns '<service> <city>'. The hub lists services with one paragraph each and no service-level FAQ. |
| City x service pages vs one another (e.g. /orlando-fl/concrete-driveways/ vs /winter-garden-fl/concrete-driveways/) | Near-duplicate risk across about 450 pages. Each needs unique local facts: permit jurisdiction, HOA/ARC, soil/terrain (Clermont hills, coastal salt), neighborhoods, real project photos. Where nothing unique exists, do not publish that city x service page; let the city hub cover it. Kissimmee turf overlaps the owner's sibling site kissimmeeartificialturf.com, so write different copy or noindex one of them. |
| Homepage vs /paver-patios/ for 'paver installers near me' | Homepage owns the trade-level near-me queries (concrete and pavers). Turf near-me goes to /artificial-turf/ because the homepage can't hold three trades. |
| /compare/pavers-vs-concrete-driveway/ vs /compare/stamped-concrete-vs-pavers/ | Driveway framing vs patio/outdoor-living framing. Titles and H1s must carry 'driveway' vs 'patio'. The cost-only question 'is concrete cheaper than pavers' sits on the cost pages. |
| /blog/best-pavers-for-florida/ vs the /compare/ material pages | The blog post is a five-material buyer's guide that links to each head-to-head page. It does not target any 'X vs Y' query. |
| /blog/how-hot-do-pool-decks-get-florida/ vs /compare/ pool pages | Heat is the only criterion on the blog post. The compare pages weigh cost, upkeep and look, and link to it for temperature. |
| /blog/pavers-over-existing-concrete/ vs /pool-deck-pavers/ | The blog post owns 'pavers over concrete' (how and when it works) across all surfaces. The pool page keeps only the coping-height FAQ and the commercial offer. |
| Hiring posts (4 regional + turf) | Separated by trade (concrete vs pavers vs turf) and region (Orlando vs Sarasota). Each uses region-specific criteria (county licensing, ARC, coastal), so the same text doesn't repeat. Posts are framed as criteria and make no 'we are the best' claims. |
| County permit posts (6) vs /faq/cost-and-permits/ | The FAQ hub gives the statewide 'it depends' answer and links to the six county posts. Each county post owns only its own jurisdictions. |
| /blog/hoa-approval-for-pavers-and-concrete/ vs /blog/lakewood-ranch-arc-approval-hardscape/ vs /blog/florida-hoa-artificial-turf-law/ | Generic hardscape HOA process vs LWR district manuals vs the turf statute. Three different intents. |
| /concrete-slabs/ vs /blog/shed-slab-guide-florida/ vs /blog/concrete-pad-for-rv-or-boat-parking/ | The service page sells pads. The shed post owns thickness, tie-downs and permits for sheds. The RV post owns RV/boat pad rules. The slab page FAQ only answers sizing and scope. |

## Caveats for the content team

- **Permits.** Permit facts (fees, which city needs what) change. Each county post must cite and link the official page and carry a 'verified on' date. Seminole's $45 ROW fee and Orange County's fee bands come from secondary sources and need confirming.
- **Turf rebates.** Many Florida utility programs pay for Florida-friendly plantings and may exclude synthetic turf. Don't promise rebates.
- **Turf law.** For FS 720.3045 and the 2025 HB 683 changes, quote the statute text and add 'not legal advice'.
- **Credentials.** License, insurance, warranty and financing answers must use Opera's real facts. Never invent addresses, license numbers or reviews. The /faq/ trust answers are placeholders until the owner provides them.
- **Scope.** Leveling (foam or mudjacking) and putting greens are listed as 'if offered'. Confirm with the owner and delete those rows if the service isn't sold.
- **Sibling site.** The owner's existing kissimmeeartificialturf.com competes for 'artificial turf kissimmee'. Decide which domain owns that query.
