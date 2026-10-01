# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "davenport"

DAVENPORT_BUILDING_URL = "https://www.mydavenport.org/index.asp?SEC=54C1C62E-BE5B-43DE-AF31-EF135278CEAD"
POLK_FAQ_URL = "https://www.polkfl.gov/services/building/faqs/"
WIKI_DAVENPORT_URL = "https://en.wikipedia.org/wiki/Davenport,_Florida"
WIKI_FOURCORNERS_URL = "https://en.wikipedia.org/wiki/Four_Corners,_Florida"
WIKI_LWRNWR_URL = "https://en.wikipedia.org/wiki/Lake_Wales_Ridge_National_Wildlife_Refuge"
CENSUS_DAVENPORT_URL = "http://censusreporter.org/profiles/16000US1216450-davenport-fl/"

SRC = [
    "census-pep-v2025", "fs713-13", "fs713-135", "fl-senate-2011-104", "swfwmd-restrictions",
    "nrcs-candler-osd", "nrcs-astatula-osd", "dep-rule", "fs125572",
    ("City of Davenport, Building Department", DAVENPORT_BUILDING_URL),
    ("Polk County, Building FAQ", POLK_FAQ_URL),
    ("Wikipedia, Davenport, Florida", WIKI_DAVENPORT_URL),
    ("Wikipedia, Four Corners, Florida", WIKI_FOURCORNERS_URL),
    ("Wikipedia, Lake Wales Ridge National Wildlife Refuge", WIKI_LWRNWR_URL),
    ("Census Reporter, Davenport FL (ACS 2020-2024 5-yr, B25035 & B25004)", CENSUS_DAVENPORT_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Davenport sits at the edge of an area the Census Bureau calls Four Corners",
        f"<p>Lake, Orange, Osceola and Polk counties all meet a few miles northeast of downtown Davenport, in a census-designated place officially named Citrus Ridge but almost universally called Four Corners, and ChampionsGate sits inside that same overlap "
        f"({ext(WIKI_FOURCORNERS_URL, 'Wikipedia, Four Corners, Florida')}). U.S. 27, which runs along the place's western edge, is the road most of that growth was built around, and the 2020 census counted 56,381 residents there, more than double the 26,116 counted in 2010 "
        f"({ext(WIKI_FOURCORNERS_URL, 'Wikipedia, Four Corners, Florida')}). {svc('concrete-driveways', 'A driveway or paver job')} anywhere along that stretch of US-27 is worth checking against both a city address and the county line before a permit application goes in.</p>"),
    sec("Davenport itself is growing about as fast as any town the Orlando unit covers",
        f"<p>Davenport's own population estimate climbed from 9,297 in April 2020 to 18,110 by July 2025, just short of doubling in five years "
        f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}). The typical Davenport home dates to 2015, the newest median build year of any city the Orlando unit tracks "
        f"({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). Most of the {svc('concrete-driveways', 'driveways')} and {svc('concrete-pool-decks', 'pool decks')} going in around town right now are first pours tied to new construction rather than a replacement for something decades old.</p>"),
    sec("A lot of that new housing stock sits empty between guests, not between owners",
        f"<p>Census survey data puts 630 housing units in Davenport as vacant, and 343 of those, about 54 percent, are marked \"for seasonal, recreational, or occasional use\" rather than for sale or for rent "
        f"({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). That category is the Census Bureau's catch-all for a second home or a short-term rental, and it is a meaningfully higher share than a typical year-round Orlando-unit suburb. {svc('pool-deck-pavers', 'A pool deck')} or {svc('paver-patios', 'a backyard patio')} built for a house that turns over guests every few days still answers to the same permit and impervious rules as a full-time residence.</p>"),
    sec("Two different building departments cover a Davenport-area address",
        f"<p>Inside the city limits, Davenport's own Building Department asks for a drawing that marks the distance from every property line for \"sheds, pavers, slabs,\" filed along with a signed, notarized permit application; the Permit Manager's line is 863-419-3300 ext. 142 "
        f"({ext(DAVENPORT_BUILDING_URL, 'City of Davenport, Building Department')}). Step outside the city into unincorporated Polk County and the office changes to the county's own Building Division, which publishes a narrower list of what skips a building permit: some driveway sections inside the right-of-way or within the minimum setback, sidewalks, and slabs that do not support a structure, with the caveat that drainage and land-development code rules still apply regardless "
        f"({ext(POLK_FAQ_URL, 'Polk County, Building FAQ')}). Confirming which office actually covers a specific lot, at 863-534-6080 for the county or 863-419-3300 for the city, comes before the site plan is drawn, not after.</p>"
        f"<p>{post('lake-and-polk-county-driveway-permits', 'Our Lake and Polk County permit guide')} covers Clermont, Minneola, Groveland and this stretch of Polk County side by side.</p>"),
    sec("Polk County answers to the same water district as the Suncoast, not to Orlando's rules",
        f"<p>Lawns in Davenport fall under the Southwest Florida Water Management District rather than St. Johns River, and the district's Modified Phase III order, in force until March 31, 2027, has cut every county it covers, Polk included, down to a single irrigation day picked by the final digit of the house number "
        f"({src('swfwmd-restrictions', 'SWFWMD, District Water Restrictions')}). Sprinklers can only run late at night into the small hours or again for a few hours after dark, not at any point in between. A lawn here answers to the same district and the same calendar as Sarasota and Manatee, even though Davenport itself sits squarely in the Orlando unit rather than near the coast, which is one reason {svc('artificial-turf', 'artificial turf')} gets asked about for a patch of yard that struggles to recover on one watering day.</p>"),
    sec("Polk County's sand ridge drains fast, and its sinkhole history is real where Lake County's isn't",
        f"<p>Scattered tracts of the Lake Wales Ridge National Wildlife Refuge sit east of US-27 between Davenport and Sebring, the southern stretch of the same sand-hill formation that runs north into Lake County "
        f"({ext(WIKI_LWRNWR_URL, 'Wikipedia, Lake Wales Ridge National Wildlife Refuge')}). Candler, one of the soil series mapped across that ridge, is excessively drained with saturation never reaching within 80 inches of the surface "
        f"({src('nrcs-candler-osd', 'USDA NRCS, Candler soil series')}), loose enough underfoot that a base crew earns its keep through compaction passes rather than through drainage design. Polk County itself carries a different distinction from its northern neighbor: a 2010 Florida Senate report names it among eleven counties responsible for over 88 percent of Florida's sinkhole insurance claims between 2006 and 2009, a list Lake County does not appear on "
        f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). A crack showing up fast on a new Davenport driveway is still usually just fill settling under freshly graded ground, but it's one of the few places on the Orlando unit's map where ruling out the rarer cause is worth the extra question.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is the City of Davenport the same place as Four Corners?",
        f"Not exactly. Four Corners, officially the Citrus Ridge census-designated place, is the broader area where Lake, Orange, Osceola and Polk counties meet, and ChampionsGate sits inside it; Davenport is the incorporated city whose own limits sit at that area's western edge along US-27 "
        f"({ext(WIKI_FOURCORNERS_URL, 'Wikipedia, Four Corners, Florida')})."),
    faq("Does a short-term rental home near Davenport follow different pool deck or patio rules?",
        "Not under the permit process itself. Whether a house turns over renters weekly or houses the same family year-round, a pool deck, patio or driveway built for it still goes through the same building department, the same site-plan and setback review, and the same impervious-surface math as any other house on the same street."),
    faq("What permit covers a driveway in unincorporated Polk County near Davenport?",
        f"Polk County's Building Division handles it rather than the city, and its own FAQ lists some driveway sections in the right-of-way or minimum setback as skipping a building permit, though drainage and land-development rules still apply either way "
        f"({ext(POLK_FAQ_URL, 'Polk County, Building FAQ')}). Confirming the specific scope with the county at 863-534-6080 before pricing a job avoids assuming an exemption that may not fit."),
    faq("Why does so much of Davenport's concrete look brand new?",
        f"Because most of it is. The typical home here was built in 2015, and the city's population nearly doubled between 2020 and 2025, so a large share of the driveways, patios and pool decks going in right now are first pours on freshly graded lots rather than replacements "
        f"({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}; {src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')})."),
    faq("Is Polk County more prone to sinkholes than the rest of the Orlando unit?",
        f"By the state's own count, yes, more than most. A 2010 Florida Senate report names Polk as one of eleven counties behind over 88 percent of Florida's sinkhole insurance claims from 2006 to 2009; Orange County also makes that list, while Lake, Osceola and Seminole do not "
        f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')})."),
]

HUB = page("/davenport-fl/", "city", "Concrete, Pavers & Turf Contractor in Davenport, FL",
           "Concrete, pavers and turf in Davenport, FL: Four Corners' growth, Polk County's permit split and the state's one-day watering order, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Davenport, Florida Homes",
           capsule(f"Davenport, a Polk County city roughly 29 miles south of Orlando, had an estimated 18,110 residents by mid-2025, nearly double its 9,297 count in 2020. "
                   f"Opera builds concrete driveways, patios, pool decks and artificial turf here; a new concrete driveway runs {price('concrete-driveway')} per {per('concrete-driveway')} under current, October 2026 Florida pricing, and whether Davenport's own Building Department or Polk County's reviews a permit depends on exactly which side of the city line an address falls on."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Davenport",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/lake-and-polk-county-driveway-permits/", "Driveway and patio permits in Lake and Polk counties"),
                    ("/celebration-fl/", "Concrete, pavers and turf in Celebration"),
                    ("/kissimmee-fl/", "Concrete, pavers and turf in Kissimmee"),
                    ("/pool-deck-cost/", "Pool deck cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Davenport, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Davenport, FL – Permits",
    "meta": "Concrete driveway installers in Davenport, FL: the city's setback site plan versus Polk County's narrower exemption, as of October 2026.",
    "h1": "Pouring a Concrete Driveway in Davenport",
    "lede": capsule(f"A new or replacement concrete driveway in Davenport runs {price('concrete-driveway')} per {per('concrete-driveway')}, current Florida pricing heading into late 2026. "
                     "Which office signs off on it depends on the address: inside the city, a site plan showing setbacks is the standard submission, and just outside it, in unincorporated Polk County, a narrower set of driveway sections can skip the building permit entirely."),
    "sections": [
        ("Davenport's own permit asks for setbacks first, square footage second",
         f"<p>The City of Davenport's Building Department wants a drawn plan marking how far driveway, paver or slab work sits off each property line, submitted alongside a signed, notarized permit application; the Permit Manager, Aleeta Hall, can be reached at 863-419-3300 ext. 142 "
         f"({ext(DAVENPORT_BUILDING_URL, 'City of Davenport, Building Department')}). That review doesn't publish a numeric impervious-surface cap the way some Orange County cities do, so a new driveway's width mostly comes down to clearing those setback lines on the survey rather than hitting a percentage ceiling.</p>"),
        ("Polk County's exemption is narrower than it sounds",
         f"<p>Once a lot sits outside Davenport's city limits, Polk County's own Building Division FAQ lists only certain driveway sections, inside the right-of-way or within the minimum setback, as skipping a building permit, alongside sidewalks and slabs that don't support a structure; every one of those still has to meet the land development code's drainage rules "
         f"({ext(POLK_FAQ_URL, 'Polk County, Building FAQ')}). Treating that as a blanket exemption for a whole driveway is the mistake the county's own FAQ is trying to head off; a call to the Building Division at 863-534-6080 before the forms go up settles which section, if any, actually qualifies.</p>"),
    ],
    "scenario": ("Sizing a three-car driveway for new construction",
                 f"<p>An 18 by 50 foot driveway built alongside new construction on a Four Corners-area lot comes to 900 square feet before any turnaround pad is added. Running that against the {price('concrete-driveway')} per {per('concrete-driveway')} range puts the pour between $5,400 and $13,500, not counting the site-plan review itself. "
                 "Whether that plan goes to Davenport's Building Department or to Polk County's instead changes which setback figures the survey has to clear, but it doesn't change the square-footage math behind the price.</p>"),
    "faqs": [
        faq("Does Davenport publish a maximum driveway width?",
            "Not in the Building Department's own permit guidance; the submission focuses on marking how far the work sits off each property line rather than meeting a published width or impervious-surface cap. Confirming any lot-specific limit with the department before finalizing a design is still worth doing."),
        faq("Can a driveway section in unincorporated Polk County skip the building permit?",
            "Sometimes. The county's FAQ lists sections in the right-of-way or within the minimum setback, along with sidewalks and non-structural slabs, as exempt, but drainage and land-development rules still apply, and the county recommends confirming the specific scope before assuming it qualifies."),
        faq("Who do I call for a driveway permit near Four Corners?",
            "It depends on the address. Inside Davenport's city limits, the Building Department at 863-419-3300 handles it; just outside the line, in unincorporated Polk County, the Building Division at 863-534-6080 does instead."),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Davenport, FL – Ridge Sand",
    "meta": "Paver driveway installers near Davenport, FL: Polk County's permit exemption gap and the fast-draining sand under much of the Four Corners area.",
    "h1": "Paver Driveways for Davenport and the Four Corners Area",
    "lede": capsule(f"A paver driveway near Davenport runs {price('paver-driveway')} per {per('paver-driveway')}, per October 2026 Florida contractor figures. "
                     "Much of the ground on this side of Polk County belongs to the same sand-hill formation that extends north into Lake County, and that history is what a compacted base under a paver driveway is actually responding to here."),
    "sections": [
        ("A sand-hill chain that starts south of Lake County and runs through here",
         f"<p>Scattered parcels of the Lake Wales Ridge National Wildlife Refuge lie just east of US-27 between Davenport and Sebring, the far southern end of the same formation that gives Lake County its hills farther north "
         f"({ext(WIKI_LWRNWR_URL, 'Wikipedia, Lake Wales Ridge National Wildlife Refuge')}). Candler soil, mapped widely across that ridge, keeps groundwater from reaching within 80 inches of the surface "
         f"({src('nrcs-candler-osd', 'USDA NRCS, Candler soil series')}). None of that moisture ever threatens a paver base here the way it would on wetter flatwoods ground; instead, the crew's real job is packing loose, free-draining sand tight enough that it won't rut under a parked car.</p>"),
        ("One FAQ answer covers only a slice of the driveway, not the whole thing",
         f"<p>Polk County's own Building Division FAQ carves out driveway sections that fall inside the right-of-way or within the required setback as not needing a building permit; it does not say the same about the stretch of driveway on private property behind that line, and every section still has to satisfy the land development code's drainage standard "
         f"({ext(POLK_FAQ_URL, 'Polk County, Building FAQ')}). {svc('paver-driveways', 'A paver driveway')} spanning both sides of that boundary line is effectively two filings bundled into one job, which is worth budgeting time for before pavers are ordered.</p>"),
    ],
    "scenario": ("Pricing a paver driveway by the numbers",
                 f"<p>A 16 by 42 foot paver driveway on an unincorporated Polk County lot comes to 672 square feet. At {price('paver-driveway')} per {per('paver-driveway')}, that job falls somewhere between $6,720 and $20,160 depending on the paver chosen. "
                 "None of that estimate changes because of the sand underneath; what changes is the labor mix, since a crew here spends a larger share of the schedule on compaction passes and a smaller share on the drainage detailing a flatwoods lot farther east would need.</p>"),
    "faqs": [
        faq("Why does a paver base near Davenport lean so heavily on compaction?",
            "Because the native sand drains too well to hold water against the base in the first place. With nothing to manage on the drainage side, the crew's attention goes into packing that loose sand into a dense, stable layer that won't shift under vehicle weight."),
        faq("Is the whole driveway permit-exempt in unincorporated Polk County?",
            "No, only the sections inside the right-of-way or within the required setback, according to the county's own FAQ. The private-property portion of the same driveway is a separate question, and drainage rules apply to every section regardless."),
        faq("Does the Lake Wales Ridge actually reach as far south as Davenport?",
            "Yes. Separate tracts of the Lake Wales Ridge National Wildlife Refuge sit along US-27 between Davenport and Sebring, confirming that the ridge's sandy, fast-draining geology extends well south of its better-known high points in Lake County."),
    ],
    "sources": SRC,
}

# 3. concrete-patios ------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Davenport, FL – New Construction",
    "meta": "Concrete patio contractors in Davenport, FL: why most patios here are first pours on new homes built since the mid-2010s, as of October 2026.",
    "h1": "Concrete Patios for Davenport Homes",
    "lede": capsule(f"A new concrete patio in Davenport is pricing between {price('concrete-patio')} per {per('concrete-patio')}, current Florida figures for this fall. "
                     "With the typical home here dating to 2015 and the city's population nearly doubling since 2020, a lot of patio work right now means pouring alongside new construction rather than replacing a cracked original slab."),
    "sections": [
        ("The newest median build year the Orlando unit tracks",
         f"<p>Davenport's population estimate went from 9,297 in 2020 to 18,110 by mid-2025, and the median home here was built in 2015, newer than any other city this unit covers "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). On a lot that recent, a lanai or back patio is more often specified at the same time as the house than added years later to a worn yard, which changes the conversation from \"match the existing finish\" to \"pick a finish before the slab goes in.\"</p>"),
        ("The patio still goes through its own site-plan review",
         f"<p>Inside the city, a patio slab follows the same path as a driveway: a drawing that marks the distance off each property line, pulled from a current survey, filed with a signed and notarized application through Davenport's Building Department "
         f"({ext(DAVENPORT_BUILDING_URL, 'City of Davenport, Building Department')}). Outside the city, in unincorporated Polk County, a patio slab that doesn't support a structure may fall under the county's narrower exemption list, though the office recommends confirming that before assuming it applies "
         f"({ext(POLK_FAQ_URL, 'Polk County, Building FAQ')}).</p>"),
    ],
    "scenario": ("A new-construction lanai patio, added up in square feet",
                 f"<p>An 18 by 22 foot lanai patio poured alongside a new Davenport house comes to 396 square feet. At {price('concrete-patio')} per {per('concrete-patio')}, that prices out between $2,376 and $5,148, before a stamped or decorative finish moves the number higher. "
                 "Because the house and patio are going in together, the crew sets the patio's elevation against the builder's own grading plan rather than against an existing slab, the reverse of how a resurfacing job in an older subdivision would start.</p>"),
    "faqs": [
        faq("Is a Davenport patio usually new construction or a replacement?",
            "More often new construction. With the median home here built in 2015 and the population nearly doubling since 2020, a large share of patio work goes in alongside a new house rather than replacing an older, cracked slab."),
        faq("Does a patio in Davenport need the same permit as a driveway?",
            "Inside the city limits, yes, the same site-plan and setback review applies to both. In unincorporated Polk County, a patio slab that doesn't support a structure may qualify for the county's narrower exemption, which is worth confirming before assuming it does."),
        faq("Does a patio need to match an existing finish in a new Davenport subdivision?",
            "Not usually, since most patios here are specified at the same time as the house rather than added to match something already built. The bigger planning question is the patio's elevation against the builder's own grading plan."),
    ],
    "sources": SRC,
}

# 4. paver-patios ----------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Davenport, FL – Rental Backyards",
    "meta": "Paver patio installers in Davenport, FL: what the Census Bureau's seasonal-housing count says about backyard use here, as of October 2026.",
    "h1": "Paver Patios and Walkways for Davenport Homes",
    "lede": capsule(f"Paver patios in Davenport price between {price('paver-patio')} per {per('paver-patio')}, Florida figures current for October 2026. "
                     "Census survey data shows a meaningfully higher share of Davenport housing marked for seasonal or occasional use than a typical year-round suburb, which is part of why so many backyard paver patios here are built around guest turnover rather than a single family's routine."),
    "sections": [
        ("A higher share of \"seasonal, recreational, or occasional use\" housing than most Orlando-unit towns",
         f"<p>Of the 630 housing units the Census Bureau's survey counted as vacant in Davenport, 343 of them, about 54 percent, fall into the \"seasonal, recreational, or occasional use\" category rather than for-sale or for-rent housing sitting empty between tenants "
         f"({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). That category covers both a snowbird's second home and a managed short-term rental, and it points to a backyard layout built around turning the space over to a new set of guests every week or two rather than a yard one family uses the same way all year.</p>"),
        ("The permit and setback rules don't change based on who is using the backyard",
         f"<p>Whether a house is occupied by its owner every night or by a rotating set of renters, a {svc('paver-patios', 'paver patio')} addition still goes through the same site-plan and setback review Davenport or Polk County applies to any other backyard project "
         f"({ext(DAVENPORT_BUILDING_URL, 'City of Davenport, Building Department')}). What changes is the layout brief more than the paperwork: a fire-pit seating area or a second dining zone built for groups of eight or ten shows up more often here than it would on a quieter residential street.</p>"),
    ],
    "scenario": ("Extending the patio for a crowd, square foot by square foot",
                 f"<p>A 24 by 20 foot paver patio extension off the back of a Davenport-area house, built to seat a larger group than a typical family patio would, comes to 480 square feet. At {price('paver-patio')} per {per('paver-patio')}, that addition falls somewhere between $4,800 and $8,160. "
                 "Sizing that patio for turnover-driven use, enough seating and walking space for a full house of guests rather than a nightly routine for two or three people, is often the detail that changes the layout more than the budget does.</p>"),
    "faqs": [
        faq("Does the Census Bureau track how many Davenport homes are vacation rentals?",
            f"Not by that exact label, but its survey category for housing \"for seasonal, recreational, or occasional use\" captures both second homes and short-term rentals, and it covers about 54 percent of the vacant housing units counted in Davenport ({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')})."),
        faq("Does a backyard built for rental guests need a different paver permit?",
            "No. The site-plan and setback review that Davenport or Polk County applies to a backyard paver project is the same regardless of whether the house is owner-occupied or managed as a rental."),
        faq("Why are Davenport-area paver patios often larger than a typical family patio?",
            "A lot of the backyard work here is built around groups of renters rather than a single household's daily routine, so seating and walking space get sized for eight or ten people instead of two or three."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks ----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Davenport, FL – Rentals",
    "meta": "Concrete pool deck builders in Davenport, FL: why new-construction pools and heavier guest turnover both shape deck sizing, Oct. 2026.",
    "h1": "Concrete Pool Decks for Davenport Homes",
    "lede": capsule(f"A concrete pool deck in Davenport runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, current Florida pricing for late 2026. "
                     "Between the city's new-construction boom and a vacation-home market that puts more feet on a deck in a given week than a typical owner-occupied pool sees, deck sizing here skews larger than the Orlando-unit average."),
    "sections": [
        ("A pool deck built for a full house of guests, not just a family of four",
         f"<p>With roughly half of Davenport's counted vacant housing marked for seasonal or occasional use, a meaningful share of the pools going in around town are built into homes designed to sleep and entertain a large group at once rather than a single household "
         f"({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). A deck sized only for a couple of lounge chairs on a house like that gets crowded fast once eight or ten guests are using the pool at the same time, which is why decks on these homes tend to run wider than the plans a straight owner-occupied build would call for.</p>"),
        ("New construction means the deck's elevation is set once, against the pool shell",
         f"<p>Because so much of Davenport's housing stock is recent, built since a median year of 2015, most pool decks here are poured fresh against a newly set pool shell rather than retrofitted around an older one "
         f"({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). That sequencing matters on this part of the ridge: the Candler and Astatula sand common here drains fast and compacts differently than flatwoods soil, so the base crew checks compaction against the pool contractor's elevation survey before the deck forms go up "
         f"({src('nrcs-candler-osd', 'USDA NRCS, Candler soil series')}).</p>"),
    ],
    "scenario": ("A pool deck built for a full house of guests",
                 f"<p>A new-construction home built for short-term rental use, pouring a 650 square foot deck around a freshly set pool shell, sits between $3,250 and $9,750 at the {price('concrete-pool-deck')} per {per('concrete-pool-deck')} rate, with a cool-touch decorative finish pushing toward the higher end. "
                 "That figure runs larger than a typical two-person household's deck would need, which tracks with how many of these Davenport-area pools are designed from the start to host a full house rather than a couple.</p>"),
    "faqs": [
        faq("Are Davenport pool decks usually bigger than elsewhere in the Orlando unit?",
            "Often, yes, since a meaningful share of local pools go into homes designed for large groups of short-term guests rather than a single family, and the deck's seating and walking space gets sized accordingly."),
        faq("Does Davenport's sandy soil affect a new pool deck's base?",
            "It changes the compaction work more than the drainage plan. Ridge soils here drain fast with a deep water table, so the base is checked for stable compaction against the pool shell's elevation rather than built to manage standing water."),
        faq("Is a pool deck for a rental home inspected any differently than for a full-time residence?",
            "No, the same permit, site-plan and inspection process applies either way, through Davenport's Building Department inside the city or Polk County's Building Division outside it."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers -------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Davenport, FL – Ridge Soil",
    "meta": "Travertine and paver pool deck installers in Davenport, FL: building on excessively drained Polk County ridge sand, as of October 2026.",
    "h1": "Travertine and Paver Pool Decks in Davenport",
    "lede": capsule(f"Pool decks finished in travertine or pavers near Davenport price between {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, tracking current Florida contractor rates. "
                     "A lot of this part of Polk County sits on the same excessively drained ridge sand that runs up through Lake County, and on a new pool build, getting that base compacted right matters more here than managing a shallow water table does."),
    "sections": [
        ("Ridge sand under a new pool deck needs real compaction, not drainage planning",
         f"<p>Davenport sits near the southern tracts of the Lake Wales Ridge National Wildlife Refuge, east of US-27 between Davenport and Sebring, part of the same ancient sand-hill formation that defines much of inland Polk County "
         f"({ext(WIKI_LWRNWR_URL, 'Wikipedia, Lake Wales Ridge National Wildlife Refuge')}). The Astatula soil common on that ridge is excessively drained, with saturation more than 60 inches below the surface, so a {svc('pool-deck-pavers', 'paver or travertine pool deck')} base here compacts loose, dry sand into a stable layer rather than fighting standing water the way a flatwoods lot would "
         f"({src('nrcs-astatula-osd', 'USDA NRCS, Astatula soil series')}).</p>"),
        ("Most of these decks are going in on brand-new pools, not replacing old ones",
         f"<p>With the median Davenport home built in 2015, a paver or travertine pool deck here is more often part of a new pool build than a resurfacing job on a deck that's already cracked or faded "
         f"({ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). Setting the paver layout against the pool contractor's own shell elevation before the base is cut avoids a mismatch at the coping line, a step that matters more on a new build than it does on a deck being re-laid around a pool that's been in the ground for years.</p>"),
    ],
    "scenario": ("A new travertine deck, priced out by the square foot",
                 f"<p>A newly built pool on a Four Corners-area lot calling for 720 square feet of travertine instead of plain concrete comes to somewhere between $8,640 and $21,600, running that footage against the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} figure, the exact total swinging on the stone and pattern picked. "
                 "Because the pool shell goes in at the same time as the deck, the crew sets the paver base to that shell's own elevation from day one instead of chasing an older deck's existing height.</p>"),
    "faqs": [
        faq("Does Polk County's ridge sand affect how a paver pool deck is built?",
            "Mostly in how much of the schedule goes to compaction. Since Astatula and nearby ridge soils sit excessively drained year-round, the crew isn't managing a water table at all; the work instead goes into tamping that loose sand into a grade that won't shift under the pavers."),
        faq("Are most Davenport-area pool decks new builds or resurfacing jobs?",
            "More often new builds, since the median home here was constructed in 2015 and a lot of pools and their decks go in together on freshly graded lots rather than replacing an aging original surface."),
        faq("What's the price range for a travertine pool deck near Davenport?",
            f"{price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026, moving with the stone, pattern and whether the job is a new build or an overlay on an existing deck."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ----------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Davenport, FL – New Builds",
    "meta": "Stamped concrete contractors in Davenport, FL: picking a pattern for a brand-new driveway or pool deck rather than matching an old one, Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Davenport",
    "lede": capsule(f"Stamped-concrete work in Davenport is budgeted at {price('stamped-concrete')} per {per('stamped-concrete')}, the current Florida range for this fall. "
                     "With most driveways and patios here going in on new construction rather than replacing something older, the design question is usually picking a fresh pattern and color from scratch instead of matching an existing slab."),
    "sections": [
        ("A new-construction market means a blank slate, not a color match",
         f"<p>Davenport's population estimate nearly doubled between 2020 and 2025, and the median home here dates to 2015, newer than any other city the Orlando unit tracks "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {ext(CENSUS_DAVENPORT_URL, 'Census Reporter, Davenport FL')}). On a lot that recent, a stamped driveway or pool-deck surround is almost always a first-time choice rather than an attempt to match a pattern poured a decade earlier, which opens up more pattern and color combinations than a resurfacing job typically allows.</p>"),
        ("The same site-plan review applies whether the finish is plain or decorative",
         f"<p>A stamped slate or ashlar pattern doesn't move a driveway or patio into a different permit category inside Davenport's city limits; the submission is still a drawing that marks the distance off each property line, filed with the Building Department "
         f"({ext(DAVENPORT_BUILDING_URL, 'City of Davenport, Building Department')}). Outside the city, the same holds for whichever section of the job unincorporated Polk County's Building Division ends up reviewing.</p>"),
    ],
    "scenario": ("A stamped pool-deck border, tallied by the square foot",
                 f"<p>A 300 square foot stamped border around a new pool, done in a travertine-look pattern with a single integral color, comes to somewhere between $2,400 and $5,700 at the {price('stamped-concrete')} per {per('stamped-concrete')} rate, with a multi-color release pushing it higher. "
                 "Because the pool itself is new, the pattern and color get chosen once against the house's own finishes rather than reverse-engineered to match an existing stamped surface somewhere else on the property.</p>"),
    "faqs": [
        faq("Does a stamped driveway need a different permit than plain concrete in Davenport?",
            "No, the same site-plan and setback review applies either way inside the city limits. The decorative finish is a design choice, not a different permit category."),
        faq("Is it harder to match a stamped pattern on an older Davenport home?",
            "Less of a concern here than elsewhere, since most Davenport homes are recent enough, built since around 2015, that a stamped project is usually a first-time pattern choice rather than a match to something poured years earlier."),
        faq("What stamped pattern works well for a new-construction pool deck?",
            "A travertine-look or ashlar pattern in a single integral color is a common first choice on a new pool, since it reads as a deliberate design decision rather than an attempt to tie into an older, already-poured surface."),
    ],
    "sources": SRC,
}

# 8. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Davenport, FL – Watering Order",
    "meta": "Artificial turf installers in Davenport, FL: SWFWMD's once-a-week order for Polk County and the 2026 state turf base rule, as of October 2026.",
    "h1": "Artificial Turf for Davenport Yards",
    "lede": capsule(f"Installing artificial turf around a Davenport home runs {price('artificial-turf')} per {per('artificial-turf')} under current, fall-2026 Florida pricing. "
                     "Polk County now falls under SWFWMD's once-a-week watering order, the same rule covering Sarasota and Manatee, which is a tighter calendar for new sod than the district's normal twice-weekly schedule and part of why turf keeps coming up here."),
    "sections": [
        ("One irrigation day, and a short list of hours to use it",
         f"<p>Polk County properties answer to SWFWMD's Modified Phase III order, in force until March 31, 2027, which pares irrigation down to a single day each week, chosen by the final digit of the house number, and confines it to two narrow stretches: shortly after midnight until 4 a.m., or from 8 p.m. until just before midnight "
         f"({src('swfwmd-restrictions', 'SWFWMD, District Water Restrictions')}). New sod trying to take root under that calendar struggles more than it would under the district's old twice-weekly allowance, and on a yard that absorbs daily foot traffic from a rotating set of guests, the bare, trampled patches show up within weeks rather than months.</p>"),
        ("Florida's 2026 turf standard treats a Davenport yard no differently than one on the coast",
         f"<p>DEP Rule 62-308.100, in force since May 19, 2026, is what actually governs the build: a washed aggregate base that drains, edges and seams anchored down, and a 10-foot buffer kept between the turf and any pond, lake or canal, dropped only where a seawall is doing that separating job instead "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A separate 2026 statute caps how aggressively a city or county can tighten residential turf rules on top of that floor, though it has no bearing on what a homeowners' association chooses to require "
         f"({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Turf for a worn side yard, run through the numbers",
                 f"<p>Take a 480 square foot side yard that gets crossed on foot every day by a rotating set of short-term guests, the kind of traffic that keeps sod from ever fully recovering on a single watering day. At {price('artificial-turf')} per {per('artificial-turf')}, installing turf there comes to somewhere between $4,800 and $12,000 depending on pile height and backing. "
                 "A family using that same strip of yard at a normal, steady pace would put far less wear on sod, which is the real difference driving the request here, not the square footage itself.</p>"),
    "faqs": [
        faq("How often can a Davenport-area lawn legally be watered right now?",
            f"Once in a seven-day stretch, on whichever day the last digit of the house number lines up with, and only in one of two windows: shortly after midnight to 4 a.m., or 8 p.m. to just before midnight ({src('swfwmd-restrictions', 'SWFWMD, District Water Restrictions')})."),
        faq("Does Florida's 2026 turf rule treat Polk County differently from Orange County?",
            f"No. DEP Rule 62-308.100 sets a single statewide minimum for base material, drainage, anchoring and setbacks from water, and any city or county may tighten that minimum but never loosen it ({src('dep-rule', 'Rule 62-308.100')})."),
        faq("Does guest turnover wear out a lawn faster than everyday family use?",
            "It tends to, since a rental yard sees fresh feet crossing it almost daily rather than the lighter, more predictable use a single household puts on the same space, and that extra traffic lines up poorly with a once-a-week watering limit."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
