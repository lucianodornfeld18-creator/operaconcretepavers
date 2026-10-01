# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "minneola"

MINNEOLA_BUILDING_URL = "https://www.minneola.us/building-department"
WIKI_MINNEOLA_URL = "https://en.wikipedia.org/wiki/Minneola,_Florida"
WIKI_CHAINOFLAKES_URL = "https://en.wikipedia.org/wiki/Clermont_chain_of_lakes"
WIKI_TURNPIKE_URL = "https://en.wikipedia.org/wiki/Florida%27s_Turnpike"
WIKI_SOUTHLAKETRAIL_URL = "https://en.wikipedia.org/wiki/South_Lake_Trail"
CLICKORLANDO_MINNEOLA_URL = "https://www.clickorlando.com/news/local/2023/10/02/we-spend-as-we-go-how-minneola-handles-rapid-growth-without-raising-taxes/"
CENSUS_MINNEOLA_URL = "http://censusreporter.org/profiles/16000US1245900-minneola-fl/"

SRC = [
    "census-pep-v2025", "sjrwmd-watering", "dep-rule", "fs125572", "lake-exempt",
    "nrcs-candler-osd", "nrcs-tavares-osd",
    ("City of Minneola, Building Department", MINNEOLA_BUILDING_URL),
    ("Wikipedia, Minneola, Florida", WIKI_MINNEOLA_URL),
    ("Wikipedia, Clermont chain of lakes", WIKI_CHAINOFLAKES_URL),
    ("Wikipedia, Florida Turnpike", WIKI_TURNPIKE_URL),
    ("Wikipedia, South Lake Trail", WIKI_SOUTHLAKETRAIL_URL),
    ("ClickOrlando, How Minneola handles rapid growth without raising taxes", CLICKORLANDO_MINNEOLA_URL),
    ("Census Reporter, Minneola FL (ACS 2020-2024 5-yr, B25035)", CENSUS_MINNEOLA_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("A single Turnpike exit changed what Minneola is",
        f"<p>Exit 278 on Florida's Turnpike, at Hancock Road in Minneola, opened to traffic in June 2017 as an all-electronic toll interchange "
        f"({ext(WIKI_TURNPIKE_URL, 'Wikipedia, Florida Turnpike')}). Mayor Pat Kelley later described the effect in blunt terms: \"All of a sudden we became a bedroom community for Orlando\" "
        f"({ext(CLICKORLANDO_MINNEOLA_URL, 'ClickOrlando, Minneola growth coverage')}). Acreage along that corridor that once sat as rolling pasture is now platted for new subdivisions, and {svc('concrete-driveways', 'a driveway')} or {svc('concrete-patios', 'a patio')} going in near Hancock Road today is almost always tied to one of those new builds rather than a replacement.</p>"),
    sec("The growth itself shows up clearly in the numbers",
        f"<p>Minneola's population estimate went from 13,848 in April 2020 to 21,064 by July 2025, a 52 percent jump in five years "
        f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}). Even with that pace of new building, the city's median home still dates to 2007, meaning a meaningful share of the housing stock is approaching an age where the original driveway or patio starts showing its first real cracks "
        f"({ext(CENSUS_MINNEOLA_URL, 'Census Reporter, Minneola FL')}).</p>"),
    sec("Minneola runs its own Building Department, separate from the county",
        f"<p>Being incorporated changes the paperwork: Lake County's exemption that waives a building permit for a low driveway or sidewalk applies only outside city limits, so it has no bearing on a Minneola address "
        f"({src('lake-exempt', 'Lake County, Residential Work Exempt from Permits')}). Instead, Minneola's own Building Department, at 800 N. US Highway 27, reviews construction, enlargement, alteration, repair and demolition work directly, with the permitting counter open weekdays from 8 a.m. to 5 p.m. and the customer-service line at 352-394-3598 ext. 180 "
        f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}). {post('lake-and-polk-county-driveway-permits', 'Our Lake and Polk County permit guide')} walks through how that compares to Clermont and the unincorporated county next door.</p>"),
    sec("Lake Minneola gives the city its name and its waterfront",
        f"<p>Lake Minneola covers about 1,888 acres, making it the third largest of the thirteen lakes in the Clermont chain and, at roughly 18 feet deep with pockets near downtown closer to 30, also the deepest "
        f"({ext(WIKI_CHAINOFLAKES_URL, 'Wikipedia, Clermont chain of lakes')}). An 1884 settler, George W. Hull, is credited with giving the lake its current name, borrowed from a Dakota phrase for \"much water.\" {svc('paver-patios', 'A lakefront patio')} or {svc('pool-deck-pavers', 'a pool deck')} built close to that shoreline still answers to setback and erosion questions a lot a few streets back from the water never has to consider.</p>"),
    sec("The region's rail-trail runs straight through town",
        f"<p>The South Lake Trail, a paved path a little over 12.5 miles long, passes through Clermont, Minneola and Groveland, and is the largest trail in Lake County "
        f"({ext(WIKI_SOUTHLAKETRAIL_URL, 'Wikipedia, South Lake Trail')}). It runs over hilly ground on its way between those three towns, a reminder that Minneola sits on the same undulating terrain as its neighbors even without a single peak as famous as the ones just south of it.</p>"),
    sec("The state's current watering order leaves Minneola with one day a week",
        f"<p>Lake County falls under SJRWMD's Phase III Extreme Water Shortage Order, Order 2026-017, which pulled affected counties down from the normal twice-weekly schedule to a single irrigation day: odd-numbered addresses water Saturday, even-numbered addresses water Sunday, nonresidential irrigation runs Tuesday, and nothing may run between 8 a.m. and 6 p.m. any day "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). A yard that was already struggling to establish new sod before that order has even less room now, which is part of why {svc('artificial-turf', 'artificial turf')} keeps coming up in conversations about a Minneola backyard.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is Minneola the same town as Clermont?",
        f"No, they're separate incorporated cities that happen to share a shoreline along Lake Minneola and the South Lake Trail. Each city runs its own Building Department and permit process, so confirming which office covers a given address matters before work starts "
        f"({ext(WIKI_CHAINOFLAKES_URL, 'Wikipedia, Clermont chain of lakes')})."),
    faq("What caused Minneola's population to grow so fast?",
        f"A Florida Turnpike interchange at Hancock Road, Exit 278, opened in June 2017 and gave the area direct highway access it hadn't had before, which the mayor has credited with turning Minneola into a bedroom community for Orlando almost overnight "
        f"({ext(CLICKORLANDO_MINNEOLA_URL, 'ClickOrlando, Minneola growth coverage')})."),
    faq("Does Minneola require a permit for a driveway or paver patio?",
        f"Generally yes. The city's Building Department reviews work to construct, enlarge, alter, repair or demolish a structure, and Lake County's own low-driveway exemption for unincorporated areas does not extend inside Minneola's city limits "
        f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}; {src('lake-exempt', 'Lake County, Residential Work Exempt from Permits')})."),
    faq("What's Lake County's watering schedule right now?",
        f"One day a week under the state's current emergency order: odd addresses Saturday, even addresses Sunday, nonresidential irrigation Tuesday, with nothing allowed between 8 a.m. and 6 p.m. ({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')})."),
    faq("How old is a typical Minneola home?",
        f"The median home here was built in 2007, even though the population has grown fastest since the Turnpike interchange opened a decade later; a lot of the newest construction sits alongside driveways and patios that are now old enough for their first serious maintenance ({ext(CENSUS_MINNEOLA_URL, 'Census Reporter, Minneola FL')})."),
]

HUB = page("/minneola-fl/", "city", "Concrete, Pavers & Turf Contractor in Minneola, FL",
           "Concrete, pavers and turf in Minneola, FL: the Turnpike interchange behind its growth, Lake Minneola's shoreline and the state's watering order, Oct. 2026.",
           "Concrete, Pavers and Artificial Turf for Minneola, Florida Homes",
           capsule(f"Minneola, a Lake County city about 22 miles from Orlando, grew from an estimated 13,848 residents in 2020 to 21,064 by mid-2025, much of it after a Florida Turnpike interchange opened at Hancock Road in 2017. "
                   f"We pour driveways, patios and pool decks in concrete and pavers, and build artificial turf, for houses on both sides of that corridor; a new concrete driveway prices at {price('concrete-driveway')} per {per('concrete-driveway')} on the current, October 2026 Florida market."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Minneola",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/lake-and-polk-county-driveway-permits/", "Driveway and patio permits in Lake and Polk counties"),
                    ("/clermont-fl/", "Concrete, pavers and turf in Clermont"),
                    ("/groveland-fl/", "Concrete, pavers and turf in Groveland"),
                    ("/artificial-turf-cost/", "Artificial turf cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Minneola, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Minneola, FL – Permits",
    "meta": "Concrete driveway installers in Minneola, FL: why the city's own Building Department, not the county, reviews the job, as of October 2026.",
    "h1": "Pouring a Concrete Driveway in Minneola",
    "lede": capsule(f"A new or replacement concrete driveway in Minneola costs {price('concrete-driveway')} per {per('concrete-driveway')} under current, October 2026 Florida pricing. "
                     "Because Minneola is its own incorporated city rather than part of unincorporated Lake County, the driveway permit goes to the city's Building Department, which does not offer the county's low-height exemption for a new pour."),
    "sections": [
        ("City limits mean city rules, not the county's exemption",
         f"<p>Lake County waives a building permit for a driveway or sidewalk under 30 inches above grade, but that exemption is written for unincorporated land, and it stops applying the moment an address sits inside Minneola "
         f"({src('lake-exempt', 'Lake County, Residential Work Exempt from Permits')}). Minneola's own Building Department instead reviews a driveway as construction work in its own right, through the permitting counter at 800 N. US Highway 27, open weekdays 8 a.m. to 5 p.m., 352-394-3598 ext. 180 "
         f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}).</p>"),
        ("New subdivisions near the Turnpike interchange are driving a lot of this work",
         f"<p>Growth along the Hancock Road corridor, tied back to the 2017 opening of the Turnpike's Exit 278, means a sizable share of the {svc('concrete-driveways', 'driveways')} going in around Minneola right now are first pours for homes that didn't exist a few years ago "
         f"({ext(WIKI_TURNPIKE_URL, 'Wikipedia, Florida Turnpike')}). A driveway on one of those lots is being measured against a fresh survey rather than an older plat, which usually makes the setback review more straightforward than it is on an established street.</p>"),
    ],
    "scenario": ("A new driveway near the Turnpike corridor, by the math",
                 f"<p>Picture a 20 by 44 foot driveway serving a new two-story house off Hancock Road: 880 square feet before any walkway tie-in. Figured against {price('concrete-driveway')} per {per('concrete-driveway')}, that comes out to roughly $5,280 on the low side and $13,200 on the high side. "
                 "Because the lot is new construction, the city's review is checking that figure against a current plat rather than an older survey that might not match what's actually on the ground.</p>"),
    "faqs": [
        faq("Does Lake County's driveway exemption apply inside Minneola?",
            "No. That exemption only covers unincorporated Lake County; inside Minneola's city limits, the Building Department reviews driveway work on its own terms regardless of height."),
        faq("Why are so many Minneola driveways brand new?",
            "A Turnpike interchange that opened at Hancock Road in 2017 opened up a corridor of new subdivisions, and a lot of the driveway work going on today is tied to those recently platted lots rather than older streets."),
        faq("Who handles a driveway permit in Minneola?",
            "The city's own Building Department, at 800 N. US Highway 27, rather than Lake County's building office. The customer-service line is 352-394-3598 ext. 180."),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Minneola, FL – Base & Permits",
    "meta": "Paver driveway installers in Minneola, FL: building a base on the Lake Wales Ridge's ground and getting a city permit, as of October 2026.",
    "h1": "Paver Driveways for Minneola Homes",
    "lede": capsule(f"Paver driveways in Minneola run {price('paver-driveway')} per {per('paver-driveway')}, current Florida contractor figures for this fall. "
                     "Minneola sits on the same chain of sand ridges that gives neighboring Clermont its hills, and on a lot graded for a new subdivision along the Hancock Road corridor, that terrain shapes the base more than any permit rule does."),
    "sections": [
        ("The ground under a new Minneola subdivision drains fast",
         f"<p>Tavares soil, mapped widely across this part of Lake County, is moderately well drained with a seasonal high water table sitting 42 to 72 inches down for much of the year, a different profile from the heavier, wetter ground common on the flatwoods side of the Orlando unit "
         f"({src('nrcs-tavares-osd', 'USDA, Tavares soil series')}). On a freshly graded lot along the Turnpike corridor, that means the base crew is less worried about a shallow water table undermining the pavers and more focused on simple, thorough compaction of loose sand.</p>"),
        ("A paver driveway on private land still goes through Minneola's own review",
         f"<p>Because the city is incorporated, Lake County's permit-free threshold for a low driveway doesn't carry over, and {svc('paver-driveways', 'a paver driveway')} here is reviewed by Minneola's Building Department rather than the county office "
         f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}). Calling the department before ordering material confirms what documentation a specific lot needs, since a brand-new plat near the interchange and an older lot closer to downtown don't always ask for the same paperwork.</p>"),
    ],
    "scenario": ("A paver driveway on a new lot, run through the numbers",
                 f"<p>A paver driveway measuring 16 by 40 feet on a newly platted Minneola lot comes to 640 square feet. At {price('paver-driveway')} per {per('paver-driveway')}, the job falls between roughly $6,400 and $19,200 depending on the paver chosen. "
                 "That range doesn't shift because of the local soil; what shifts is how the crew spends its prep time, leaning on compaction rather than on drainage work a wetter lot elsewhere in the unit would demand.</p>"),
    "faqs": [
        faq("What soil is typically under a new Minneola driveway?",
            "A lot of the newer subdivisions sit on Tavares soil, which is moderately well drained with the seasonal high water table sitting several feet down for most of the year, different from the wetter flatwoods ground common elsewhere in the Orlando unit."),
        faq("Does a paver driveway in Minneola skip the city's permit process?",
            "Not automatically. Minneola's Building Department reviews paver work inside city limits regardless of Lake County's exemption for unincorporated land, so confirming the requirement for a specific lot before ordering material is worth the call."),
        faq("Is base prep different for a Minneola driveway than for one in Clermont?",
            "Not dramatically, since both towns sit on similar ridge-adjacent ground, but the exact soil series and water table depth can vary lot to lot, which is why a site-specific check still matters more than assuming the neighboring city's conditions apply."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Minneola, FL – Aging Slabs",
    "meta": "Concrete patio contractors in Minneola, FL: why a 2007-era patio is reaching the age for its first real repair, as of October 2026.",
    "h1": "Concrete Patios for Minneola Homes",
    "lede": capsule(f"A concrete patio in Minneola is priced at {price('concrete-patio')} per {per('concrete-patio')}, the current Florida range for late 2026. "
                     "With the median home here dating to 2007, a good number of Minneola's original patio slabs are old enough now that resurfacing, not a fresh pour, is the more common call."),
    "sections": [
        ("A median build year nearly two decades old changes the typical request",
         f"<p>Minneola's population has nearly doubled since 2020, but the city's median home was still built back in 2007 "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {ext(CENSUS_MINNEOLA_URL, 'Census Reporter, Minneola FL')}). A patio poured around that time has had close to twenty years of Central Florida sun and summer rain to work on it, long enough for joint sealant to fail and for the surface to start pitting, which is a different conversation than the first-pour work going in on a brand-new lot off Hancock Road.</p>"),
        ("Patio work still answers to the city's own permit desk",
         f"<p>A patio slab, new or replaced, falls under Minneola's Building Department rather than Lake County's office, the same as a driveway "
         f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}). On an older lot, the department may ask to see what's already there before approving a full tear-out, since a patio that's settled unevenly sometimes needs more than a simple resurfacing to fix.</p>"),
    ],
    "scenario": ("Resurfacing an aging patio, added up by the square foot",
                 f"<p>A 16 by 18 foot patio poured around 2007, now showing surface pitting and a hairline crack along one edge, covers 288 square feet. At {price('concrete-patio')} per {per('concrete-patio')}, a full replacement lands between $1,728 and $3,744, while a resurfacing overlay on the same footprint typically comes in under that range. "
                 "Deciding between the two usually comes down to whether the slab underneath has settled enough to need a fresh pour instead of just a new face.</p>"),
    "faqs": [
        faq("Is a 2007 concrete patio in Minneola due for replacement?",
            "Not automatically, but it's at an age where pitting, faded color and failing joint sealant are common enough that a close look is worth it before assuming a simple cleaning will fix the surface."),
        faq("Does Minneola treat patio repairs differently from a new patio permit?",
            "The same Building Department reviews both, though a repair on an older, unevenly settled slab sometimes needs more documentation than a straightforward new pour on a vacant lot."),
        faq("Are most Minneola patios newer or older than the city's median home age?",
            "It varies by neighborhood. Streets built up before the Turnpike interchange opened in 2017 tend to track closer to the city's 2007 median build year, while subdivisions along the newer corridor skew much younger."),
    ],
    "sources": SRC,
}

# 4. paver-patios -----------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Minneola, FL – Lake Minneola",
    "meta": "Paver patio installers near Minneola, FL: what building close to Lake Minneola's shoreline changes about a backyard project, Oct. 2026.",
    "h1": "Paver Patios and Walkways Near Lake Minneola",
    "lede": capsule(f"Paver patios near Minneola price between {price('paver-patio')} per {per('paver-patio')}, Florida figures current for October 2026. "
                     "Lake Minneola itself, the 1,888-acre lake the city takes its name from, sits close enough to a meaningful share of local backyards that shoreline distance, not just square footage, often decides how a paver patio gets laid out."),
    "sections": [
        ("A deep, historic lake right at the edge of town",
         f"<p>Lake Minneola runs about 1,888 acres and, at roughly 18 feet deep with pockets near downtown closer to 30 feet, is both the third largest and the deepest of the thirteen lakes making up the Clermont chain "
         f"({ext(WIKI_CHAINOFLAKES_URL, 'Wikipedia, Clermont chain of lakes')}). A backyard that backs up to that shoreline is laying pavers over ground that can shift with seasonal water levels, which is a different planning question than a patio set well back from any open water.</p>"),
        ("A lakefront patio still goes through the same city review as any other",
         f"<p>Proximity to the water doesn't exempt a {svc('paver-patios', 'paver patio')} from Minneola's own Building Department process; if anything, a lot that touches the shoreline is more likely to draw questions about grading and runoff during that review "
         f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}). Checking with the department early, before pavers are ordered, is worth it on any lot within sight of the water.</p>"),
    ],
    "scenario": ("A lakefront patio addition, sized up front",
                 f"<p>A 22 by 18 foot paver patio built along the back of a Lake Minneola-facing lot comes to 396 square feet. Figuring that against {price('paver-patio')} per {per('paver-patio')} puts the job between $3,960 and $6,732. "
                 "On a lot this close to the shoreline, that estimate often needs a grading plan folded in alongside it, since water running off the patio has somewhere specific it needs to go rather than simply spreading across an open yard.</p>"),
    "faqs": [
        faq("How big is Lake Minneola?",
            f"About 1,888 acres, making it the third largest of the thirteen lakes in the Clermont chain and, at up to roughly 30 feet deep near downtown, also the deepest ({ext(WIKI_CHAINOFLAKES_URL, 'Wikipedia, Clermont chain of lakes')})."),
        faq("Does a patio near Lake Minneola need extra permitting?",
            "Not a separate permit category, but the city's review on a shoreline-adjacent lot is more likely to focus on grading and where runoff goes than it would on a lot farther from the water."),
        faq("Where did Lake Minneola get its name?",
            "An 1884 settler named George W. Hull is credited with naming it, borrowing a Dakota-language phrase that translates roughly to \"much water.\""),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Minneola, FL – New Builds",
    "meta": "Concrete pool deck builders in Minneola, FL: pouring on fast-draining ridge soil for homes going up along the Hancock Road corridor, Oct. 2026.",
    "h1": "Concrete Pool Decks for Minneola Homes",
    "lede": capsule(f"A concrete pool deck in Minneola runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, the current Florida range for this fall. "
                     "A large share of the pools going into new Minneola subdivisions sit on Tavares or Candler soil, ground that drains well enough that the deck's base work focuses on compaction rather than on keeping water away from the slab."),
    "sections": [
        ("Fast-draining ground changes the base, not the mix",
         f"<p>Tavares soil, common on the newer side of Minneola near the Turnpike corridor, keeps its seasonal high water table 42 to 72 inches down for most of the year, while Candler soil nearby drains even more aggressively, with saturation staying below 80 inches "
         f"({src('nrcs-tavares-osd', 'USDA, Tavares soil series')}; {src('nrcs-candler-osd', 'USDA, Candler soil series')}). Underneath a new pool deck, that means the crew isn't managing standing water the way a flatwoods lot would require; the job is packing that loose sand into a grade that holds steady under the deck's weight.</p>"),
        ("New pools are going in alongside new houses more often than not",
         f"<p>With Minneola's population growing from 13,848 to 21,064 between 2020 and 2025, much of it tied to development along Hancock Road since the Turnpike interchange opened in 2017, a meaningful share of {svc('concrete-pool-decks', 'pool decks')} here are poured at the same time as the pool shell rather than retrofitted years later "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {ext(WIKI_TURNPIKE_URL, 'Wikipedia, Florida Turnpike')}).</p>"),
    ],
    "scenario": ("A new pool deck, broken down by the square foot",
                 f"<p>A 540 square foot deck poured around a freshly set pool shell on a new Minneola lot comes out to between $2,700 and $8,100 at {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, with a decorative or cool-touch finish landing toward the top of that range. "
                 "Because the pool and the surrounding deck go in together, the elevation gets set once against the contractor's own layout instead of being measured against something already in the ground.</p>"),
    "faqs": [
        faq("Does Minneola's soil affect how a new pool deck is built?",
            "It shifts the emphasis toward compaction. Tavares and Candler soils both drain well, so the crew spends less effort managing groundwater and more effort packing the base into a stable grade under the deck."),
        faq("Are most new Minneola pool decks poured alongside the pool itself?",
            "Often, yes, especially in subdivisions built since the Turnpike interchange opened in 2017, where the pool and its deck are typically part of the same new-construction project rather than a later addition."),
        faq("What's the going rate for a concrete pool deck in Minneola?",
            f"{price('concrete-pool-deck')} per {per('concrete-pool-deck')} as of October 2026, with the finish chosen, plain broom versus a decorative or cool-touch surface, moving the total within that range."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers --------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Minneola, FL – Lakefront",
    "meta": "Travertine and paver pool deck installers in Minneola, FL: building near Lake Minneola's shoreline and on fast-draining ridge sand, Oct. 2026.",
    "h1": "Travertine and Paver Pool Decks in Minneola",
    "lede": capsule(f"Pool decks finished in travertine or pavers near Minneola price between {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, tracking current Florida contractor rates. "
                     "On a lot close to Lake Minneola's shoreline, the deck's layout has to account for the water as much as for the pool itself, while a lot farther inland is usually dealing with fast-draining ridge sand instead."),
    "sections": [
        ("Two very different sites, both common around Minneola",
         f"<p>A home near Lake Minneola's roughly 1,888-acre shoreline sits on different ground than one in a new subdivision off Hancock Road "
         f"({ext(WIKI_CHAINOFLAKES_URL, 'Wikipedia, Clermont chain of lakes')}). Near the water, grading the deck so runoff doesn't carry straight toward the shoreline matters more than soil type; farther inland, on Tavares or Candler sand, the bigger question is compacting a base that holds steady under {svc('pool-deck-pavers', 'pavers or travertine')} without a shallow water table to fight "
         f"({src('nrcs-tavares-osd', 'USDA, Tavares soil series')}).</p>"),
        ("Which site a project sits on changes the conversation before the first paver is set",
         f"<p>A deck going in along the lake typically needs the layout checked against drainage and setback questions the Building Department raises during review "
         f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}), while a deck on a new inland lot is more often a straightforward compaction and elevation exercise tied to the pool contractor's own shell survey.</p>"),
    ],
    "scenario": ("A travertine deck on an inland lot, figured by the square foot",
                 f"<p>A 600 square foot travertine deck around a new pool on a Hancock Road-area lot comes to somewhere between $7,200 and $18,000 once {price('pool-deck-pavers')} per {per('pool-deck-pavers')} is applied, depending on the stone pattern chosen. "
                 "Set that same footprint along Lake Minneola instead, and the price range holds, but the base crew spends more of its time on the grading plan than it would a few miles inland.</p>"),
    "faqs": [
        faq("Does building near Lake Minneola change how a paver pool deck is laid out?",
            "Yes, mainly around drainage and setback. A deck close to the shoreline is graded so runoff doesn't head straight for the water, a consideration that doesn't come up the same way on a lot well away from the lake."),
        faq("Is the soil the same all over Minneola for a pool deck base?",
            "No. Tavares and Candler soils, common on the newer inland side of the city, drain fast and need thorough compaction, while a lakefront lot's planning leans more on grading and setbacks than on soil type."),
        faq("What's the price difference between a lakefront and an inland Minneola pool deck?",
            f"The {price('pool-deck-pavers')} per {per('pool-deck-pavers')} material and labor range doesn't change by location, though a lakefront project often carries added grading or drainage work that an inland lot doesn't need."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ----------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Minneola, FL – New Builds",
    "meta": "Stamped concrete contractors in Minneola, FL: picking a pattern for the city's wave of new construction along Hancock Road, as of October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Minneola",
    "lede": capsule(f"Expect to pay {price('stamped-concrete')} per {per('stamped-concrete')} for stamped concrete in Minneola, tracking the current Florida market heading into late 2026. "
                     "With so much of the city's growth concentrated along the Hancock Road corridor since the Turnpike interchange opened, a stamped driveway or patio here is usually the first finish a new house has ever had rather than a redo of something older."),
    "sections": [
        ("A decade of rapid building means more first choices than second opinions",
         f"<p>Minneola's population climbed from 13,848 in 2020 to 21,064 by 2025, growth concentrated heavily along the corridor that opened up once the Turnpike's Exit 278 went in at Hancock Road "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {ext(WIKI_TURNPIKE_URL, 'Wikipedia, Florida Turnpike')}). A homeowner on one of those newer streets is picking a stamped pattern and color from scratch, without an existing driveway anywhere on the block to match or avoid clashing with.</p>"),
        ("The same Building Department reviews a stamped finish as a plain one",
         f"<p>Choosing a decorative stamp over plain gray concrete doesn't change which office signs off on the work; Minneola's Building Department reviews the driveway or patio itself, not the surface treatment "
         f"({ext(MINNEOLA_BUILDING_URL, 'City of Minneola, Building Department')}). On an older lot closer to downtown, by contrast, matching an existing stamped walkway or an adjacent patio sometimes becomes part of the design conversation in a way it rarely is on a brand-new street.</p>"),
    ],
    "scenario": ("A stamped driveway apron, run through the math",
                 f"<p>A stamped border section covering 260 square feet along a new driveway's edge, done in a single integral color, comes out to between $2,080 and $4,940 at {price('stamped-concrete')} per {per('stamped-concrete')}, with a multi-color release pushing the total higher. "
                 "Because the house next door likely hasn't been built yet either, the color and pattern decision here is rarely about matching the neighbors, which is a different starting point than a stamped job in an older part of town.</p>"),
    "faqs": [
        faq("Does a stamped patio need a different permit than plain concrete in Minneola?",
            "No, the Building Department reviews the underlying driveway or patio work the same way regardless of whether the finish is plain or decorative."),
        faq("Is it easier to pick a stamped pattern on a new Minneola street than an older one?",
            "In one sense, yes, since a brand-new street along the Hancock Road corridor usually has no existing finish nearby to match or avoid, unlike an older block where a neighboring driveway or patio can shape the decision."),
        faq("What stamped finish suits a new-construction Minneola home?",
            "A single, integral color in a straightforward pattern is a common first choice on new builds, since there's rarely an established neighborhood look yet to match against."),
    ],
    "sources": SRC,
}

# 8. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Minneola, FL – Watering Order",
    "meta": "Artificial turf installers in Minneola, FL: Lake County's one-day order under SJRWMD and the lake-setback rule in the 2026 state turf law, Oct. 2026.",
    "h1": "Artificial Turf for Minneola Yards",
    "lede": capsule(f"Installing artificial turf in Minneola runs {price('artificial-turf')} per {per('artificial-turf')} under current, fall-2026 Florida pricing. "
                     "Lake County's emergency watering order has cut irrigation to one day a week, and on a lot anywhere near Lake Minneola's shoreline, the state's 2026 turf rule adds its own distance requirement from the water on top of that."),
    "sections": [
        ("One watering day, split into two allowed windows",
         f"<p>Under SJRWMD's Order 2026-017, Lake County addresses water once in a seven-day stretch: odd-numbered houses on Saturday, even-numbered houses on Sunday, nonresidential irrigation on Tuesday, with nothing running between 8 a.m. and 6 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). New sod planted under that schedule has far less room to recover between waterings than it did under the district's old twice-a-week rule, which is a big part of why turf comes up for a yard that just will not hold a green lawn right now.</p>"),
        ("Near Lake Minneola, the state's turf rule adds a water-setback rule of its own",
         f"<p>DEP Rule 62-308.100, effective since May 2026, sets a statewide floor for turf construction: a washed, draining aggregate base, anchored seams and edges, and turf held back a minimum of 10 feet from any lake, pond or canal, except where a seawall is already doing that job "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). On a Lake Minneola-adjacent lot, that buffer trims the usable turf footprint right along the water, something a backyard set well away from the lake never has to plan around. A separate statute caps how far a city can tighten residential turf rules past that floor, though an individual community's own design standards aren't affected by it "
         f"({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Turf for a yard that can no longer hold sod, by the numbers",
                 f"<p>Take a 420 square foot backyard where sod has thinned out under the current one-day watering schedule. Installing turf there costs between $4,200 and $10,500 at {price('artificial-turf')} per {per('artificial-turf')}, depending on pile height and backing. "
                 "On a lot backing up to Lake Minneola instead, trimming that same footprint back from the required 10-foot water buffer might shave off a corner of usable turf area, which is worth measuring before a final quote is drawn up.</p>"),
    "faqs": [
        faq("How often can a Minneola lawn be watered under the current order?",
            f"Once a week: odd-numbered addresses on Saturday, even-numbered on Sunday, nonresidential irrigation on Tuesday, and never between 8 a.m. and 6 p.m. ({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')})."),
        faq("How close to Lake Minneola can artificial turf be installed?",
            f"At least 10 feet back from the shoreline under the state's 2026 turf rule, unless a seawall already separates the yard from the water ({src('dep-rule', 'Rule 62-308.100')})."),
        faq("Does Minneola's watering order explain why so many lawns look thin right now?",
            "It's a major factor. A single watering day a week gives sod far less chance to recover from Central Florida heat and foot traffic than the district's normal twice-weekly schedule did, which is why so many homeowners are asking about turf instead."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
