# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "apopka"

FEE_URL = "https://www.apopka.gov/256/Fees"
ENG_URL = "https://www.apopka.gov/268/Engineering-Division"
BLDGFAQ_URL = "https://www.apopka.gov/faq.aspx?TID=18"
PERMITTING_URL = "https://www.apopka.gov/253/Permitting"
TYPES_URL = "https://www.apopka.gov/264/Types"
FESTIVAL_URL = "https://www.apopka.gov/m/newsflash/Home/Detail/740?arc=1283"
ACS_URL = "https://censusreporter.org/profiles/16000US1201700-apopka-fl/"
WIKI_URL = "https://en.wikipedia.org/wiki/Apopka,_Florida"
WEKIWA_URL = "https://en.wikipedia.org/wiki/Wekiwa_Springs_State_Park"
KELLY_URL = "https://www.orangecountyfl.net/CultureParks/Parks.aspx?m=dtlvw&d=22"

SRC = [
    "census-pep-v2025", "sjrwmd-watering", "fl-senate-2011-104", "dep-rule", "fs125572", "orange-res-plan-guide",
    "nrcs-candler-osd", "nrcs-tavares-osd", "nrcs-astatula-osd", "nrcs-myakka-osd", "nrcs-smyrna-osd",
    ("City of Apopka, Building Permit FAQs", BLDGFAQ_URL),
    ("City of Apopka, Permitting Fees", FEE_URL),
    ("City of Apopka, Engineering Division", ENG_URL),
    ("City of Apopka, Permitting", PERMITTING_URL),
    ("City of Apopka, Permit Types", TYPES_URL),
    ("City of Apopka, Apopka Art & Foliage Festival Proclamation", FESTIVAL_URL),
    ("Census Reporter, Apopka FL (ACS 2020-2024 5-yr, B25035/B01003)", ACS_URL),
    ("Wikipedia, Apopka, Florida", WIKI_URL),
    ("Wikipedia, Wekiwa Springs State Park", WEKIWA_URL),
    ("Orange County Parks & Recreation, Kelly Park/Rock Springs", KELLY_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("What triggers a building permit for a driveway, patio or pavers in Apopka?",
        f"<p>Apopka's own FAQ keeps the trigger broad, covering work to \"enlarge, alter, repair, move\" or otherwise change a structure "
        f"({ext(BLDGFAQ_URL, 'the city\'s Building Permit FAQ')}), wording that reaches a new driveway, a patio slab or a paver installation the same way it reaches a room addition. The Building-Safety Department reviews the application at City Hall, 120 E Main Street, second floor, 407-703-1713, and anything calling for a state-registered architect or engineer, typically structural work rather than ordinary flatwork, goes through a separate plan review "
        f"({ext(BLDGFAQ_URL, 'the city\'s Building Permit FAQ')}). Pricing starts at the going Florida range of {price('concrete-driveway')} per {per('concrete-driveway')} for a new concrete driveway, current this October 2026.</p>"),
    sec("How does Apopka calculate a permit fee?",
        f"<p>The city's own fee schedule sets the formula plainly: permits run \"$7.50 per $1,000 of actual contracted cost or construction cost/value, whichever is greater,\" with a $75 floor and, on new construction, a separate $50 non-refundable administrative charge "
        f"({ext(FEE_URL, 'Apopka Permitting Fees')}). A $6,000 driveway replacement, for example, lands at roughly $75 under that formula before any plan-review add-on, while a larger job scales up with the contract price rather than a flat per-square-foot number. Applications route through the OpenGov online portal, open to homeowners and registered contractors alike "
        f"({ext(PERMITTING_URL, 'Apopka Permitting')}).</p>"),
    sec("Who reviews the paving, drainage and right-of-way side of the job?",
        f"<p>Apopka's Engineering Division, also at 120 E Main Street, handles excavation permits, plan review and right-of-way permitting, plus review of stormwater drainage improvements tied to a project "
        f"({ext(ENG_URL, 'Apopka Engineering Division')}). That matters most for {svc('concrete-driveways', 'a driveway')} that widens an apron toward the street or for {svc('retaining-walls', 'a retaining wall')} cut into a sloped lot, since either one can touch city-maintained drainage. The Building Division's own permit-type list separately confirms that building permits, electrical, mechanical, plumbing and gas work are each tracked on their own, so a paver job that also moves a hose bib or an outdoor outlet can pull in more than one application "
        f"({ext(TYPES_URL, 'Apopka Permit Types')}).</p>"),
    sec("Why does Apopka call itself the Indoor Foliage Capital of the World, and does that touch outdoor projects?",
        f"<p>A 2026 city proclamation marking the Apopka Art and Foliage Festival states plainly that \"the City of Apopka has long been known as the 'Indoor Foliage Capital of the World,'\" a title tied to the greenhouse nursery industry that grew up here over the past century "
        f"({ext(FESTIVAL_URL, 'the 2026 festival proclamation')}). The nursery trade itself doesn't set a rule for a homeowner's driveway or patio, but it does mean shade cloth frames, greenhouse slabs and nursery access roads show up on local permit counters alongside ordinary residential work, and a {svc('concrete-slabs', 'slab')} poured for a backyard greenhouse or potting shed goes through the same building-permit review as any other accessory structure.</p>"),
    sec("How fast is Apopka growing, and what does that mean for new driveways and patios?",
        f"<p>The Census Bureau's own population estimates put Apopka at 65,552 residents on July 1, 2025, up from a 2020 base of 54,892, a gain of nearly 20 percent in five years that makes it Orange County's second-largest city "
        f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}). Wikipedia's entry on the city, citing Census figures, describes Apopka as \"a fast-growing city\" that is \"expanding in all directions\" "
        f"({ext(WIKI_URL, 'Wikipedia, Apopka, Florida')}), and the Census Reporter profile puts the median year a home here was built at 2002 "
        f"({ext(ACS_URL, 'Census Reporter, Apopka FL')}). That pace means a share of {svc('paver-driveways', 'paver driveways')} and {svc('concrete-pool-decks', 'pool decks')} going in around the city today are first installs on recently platted lots rather than replacements of an older slab.</p>"),
    sec("What do Wekiwa Springs and Kelly Park add to the picture for a backyard project?",
        f"<p>Apopka sits at the edge of a spring-fed system that defines a lot of how water moves through the area. Wekiwa Springs State Park, just outside the city, covers about 7,000 acres and discharges roughly 42 million gallons of water a day into the Wekiva River, the park holding the river's headwaters "
        f"({ext(WEKIWA_URL, 'Wikipedia, Wekiwa Springs State Park')}). A few miles north, Orange County's own Kelly Park, 380 acres built around Rock Springs, keeps a spring that runs 68 to 72 degrees year-round, a feature the county's park page highlights for tubing and swimming "
        f"({ext(KELLY_URL, 'Orange County Parks & Recreation, Kelly Park/Rock Springs')}). The limestone that feeds those springs sits under much of north Orange County, which is part of why the state's own sinkhole-claims data lists Orange among the counties that generated the bulk of Florida's claims from 2006 through 2009 "
        f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}); a dip in a driveway near that geology is worth a second look before assuming it's ordinary settlement.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Apopka require a permit for pavers on private property?",
        f"Yes. The city's permit trigger covers any work that constructs, alters or repairs a structure, and a paver driveway or patio application goes through the Building-Safety Department the same way a slab or an addition would "
        f"({ext(BLDGFAQ_URL, 'the city\'s Building Permit FAQ')})."),
    faq("How much does a driveway permit cost in Apopka?",
        f"The city calculates fees at $7.50 per $1,000 of the contracted cost, with a $75 minimum, plus a separate $50 administrative fee on new construction; a modest driveway job can land near that $75 floor "
        f"({ext(FEE_URL, 'Apopka Permitting Fees')})."),
    faq("Does a driveway apron that reaches the street go through a separate review in Apopka?",
        f"Work touching city right-of-way or drainage, including a widened apron, routes through the Engineering Division rather than the Building Division alone, since that office handles right-of-way permitting and stormwater review "
        f"({ext(ENG_URL, 'Apopka Engineering Division')})."),
    faq("Is Apopka's nursery industry still active today?",
        f"The \"Indoor Foliage Capital of the World\" title traces back to the fern and foliage trade that built up here over the past century, and the city still marks it each spring with the Apopka Art and Foliage Festival "
        f"({ext(FESTIVAL_URL, 'the 2026 festival proclamation')})."),
    faq("How do you pick the best concrete contractor near Apopka?",
        f"Check the contractor's status on the state's license-verification tool, confirm the bid already accounts for both a Building Division permit and, if the work touches the street, an Engineering Division review, and ask how the quote handles demolition of an existing slab. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} covers the rest."),
]

HUB = page("/apopka-fl/", "city", "Concrete, Pavers & Turf Contractor in Apopka, FL",
           "Opera builds concrete driveways, pavers and turf in Apopka, FL, where the city's permit fee runs $7.50 per $1,000 of contract value, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Apopka, Florida Homes",
           capsule(f"Opera's crews pour concrete and set pavers and artificial turf across Apopka, Orange County's second-largest city with 65,552 residents as of mid-2025, roughly "
                   f"{str(__import__('_data').CITIES['apopka']['miles'])} miles from Orlando. Budget {price('concrete-driveway')} per {per('concrete-driveway')} for a new concrete driveway under the current October 2026 Florida market range, plus the city's own permit fee, calculated at $7.50 per $1,000 of contract value rather than off square footage."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Apopka",
           related=[("/central-florida/", "The Orlando-unit coverage area"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Driveway and patio permits in Orlando and Orange County"),
                    ("/winter-garden-fl/", "Concrete, pavers and turf in Winter Garden"),
                    ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Apopka, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Apopka, FL – Permits",
    "meta": "Concrete driveway installers in Apopka, FL: the city's $7.50-per-$1,000 permit formula and when Engineering Division review applies, Oct. 2026.",
    "h1": "Pouring a Concrete Driveway in Apopka",
    "lede": capsule(f"Pricing for a new or replacement concrete driveway in Apopka sits at {price('concrete-driveway')} per {per('concrete-driveway')} this October 2026, the going Florida market figure. "
                     "Apopka treats the slab as a structure for permit purposes, so the fee tracks the contract value rather than square footage, and work that widens the apron toward the street adds a second review."),
    "sections": [
        ("The permit fee scales with the contract, not the slab's size",
         f"<p>Apopka's fee schedule sets the formula without exception: \"$7.50 per $1,000 of actual contracted cost or construction cost/value, whichever is greater,\" with a floor of $75 "
         f"({ext(FEE_URL, 'Apopka Permitting Fees')}). That means two driveways of the same square footage can carry different permit fees if their finishes, and therefore their contract prices, differ, a detail worth asking a contractor to confirm before the number gets written into a quote for {svc('concrete-driveways', 'a driveway')}.</p>"),
        ("A widened apron adds the Engineering Division to the paperwork",
         f"<p>Where a new or wider driveway meets the street, that section falls to the Engineering Division rather than the Building Division alone, since that office covers right-of-way permitting, plan review and drainage review for work in the public strip "
         f"({ext(ENG_URL, 'Apopka Engineering Division')}). A driveway that stays inside its existing footprint on private ground skips that second review; one that widens toward the curb typically doesn't.</p>"),
    ],
    "scenario": ("Replacing a two-car driveway, worked out in square feet",
                 f"<p>A 22 by 24 ft two-car driveway comes to 528 sq ft. At {price('concrete-driveway')} per {per('concrete-driveway')}, the pour alone lands between roughly $3,168 and $7,920, before demolition of the old slab is added. "
                 "Running a $5,500 contract for that job through the city's fee formula puts the permit itself at roughly $75, since $5,500 falls under the $75 floor on the $7.50-per-$1,000 scale; a larger, higher-end contract for the same footprint would push the fee closer to, or past, that floor depending on the finish chosen.</p>"),
    "faqs": [
        faq("Is Apopka's driveway permit fee based on square footage?",
            "No. The city calculates it off the contracted cost or construction value, $7.50 per $1,000, with a $75 minimum, so two driveways the same size can carry different fees depending on price."),
        faq("Does a concrete driveway in Apopka need Engineering Division sign-off?",
            "Only the part that touches the street or city drainage. The Engineering Division reviews right-of-way and drainage work; a driveway staying within its existing private footprint typically stays with the Building Division alone."),
        faq("Where is Apopka's Building Division located?",
            "City Hall, 120 E Main Street, second floor, reachable at 407-703-1713 for driveway and other structure permits."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Apopka, FL – New Subdivisions",
    "meta": "Paver driveway installers in Apopka, FL: why the city's structure-wide permit rule covers pavers, and what nearly 20% growth means, Oct. 2026.",
    "h1": "Paver Driveways for Apopka's Growing Subdivisions",
    "lede": capsule(f"Figure {price('paver-driveway')} per {per('paver-driveway')} for a paver driveway in Apopka heading into the last quarter of 2026. "
                     "Orange County's second-largest city added nearly 11,000 residents between 2020 and mid-2025, and a meaningful share of the paver driveways going in today are first installs on recently built lots rather than a swap for a cracked original."),
    "sections": [
        ("Pavers don't get a lighter permit path than poured concrete",
         f"<p>Apopka's own trigger for a building permit covers altering, repairing or adding any structure on the lot without carving out an exception for material "
         f"({ext(BLDGFAQ_URL, 'the city\'s Building Permit FAQ')}). A {svc('paver-driveways', 'paver driveway')} goes through the Building-Safety Department's review the same as a poured one, with the fee again set at $7.50 per $1,000 of contract value against a $75 floor "
         f"({ext(FEE_URL, 'Apopka Permitting Fees')}).</p>"),
        ("A fast-growing city means more first installs than replacements",
         f"<p>The Census Bureau's latest estimate puts Apopka's population at 65,552 as of July 1, 2025, up from 54,892 in 2020, a jump of close to 20 percent in five years "
         f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}). Wikipedia describes the city, citing Census data, as \"expanding in all directions\" "
         f"({ext(WIKI_URL, 'Wikipedia, Apopka, Florida')}), which tracks with what a paver crew sees on the ground: more driveways poured onto fresh fill for the first time than pulled out and replaced.</p>"),
    ],
    "scenario": ("A paver driveway on a newly platted lot, worked out in square feet",
                 f"<p>A 24 by 24 ft paver driveway on a new-construction lot comes to 576 sq ft. At {price('paver-driveway')} per {per('paver-driveway')}, that job runs roughly $5,760 to $17,280 depending on the paver and base depth chosen. "
                 "On a freshly graded lot, the base crew is usually working with fill that hasn't settled through a full wet season yet, so compaction gets checked carefully before the bedding sand and pavers go down, a step that matters less on an older, already-settled lot nearby.</p>"),
    "faqs": [
        faq("Does a paver driveway in Apopka need a different permit than a concrete one?",
            "No. The city's permit trigger applies to any structure regardless of material, so a paver driveway goes through the same Building-Safety Department review and fee formula a poured driveway would."),
        faq("Is most paver driveway work in Apopka new construction or replacement?",
            "A larger share than in many older Central Florida cities is new construction, since the city's population grew nearly 20 percent between 2020 and mid-2025 on a wave of new subdivisions."),
        faq("Does fresh fill on a new Apopka lot change how a paver base gets built?",
            "It can. Soil on a recently graded lot hasn't always settled through a full wet season, so a crew checks compaction more carefully there than on an older, already-settled lot."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Apopka, FL – 2002 Homes",
    "meta": "Concrete patio contractors in Apopka, FL: the city's permit trigger and what a 2002 median build year means for a patio addition, Oct. 2026.",
    "h1": "Building a Concrete Patio in Apopka",
    "lede": capsule(f"Expect {price('concrete-patio')} per {per('concrete-patio')} for a concrete patio in Apopka, the Florida range current for this October. "
                     "With the city's typical home dating to 2002, a lot of patio work here means adding onto a yard with an established driveway and walkway already in place, rather than building out a brand-new lot from scratch."),
    "sections": [
        ("A patio slab counts as a structure for permit purposes",
         f"<p>Apopka's building-permit FAQ doesn't carve patios or other outdoor slabs out of its general rule, and \"which building permits require plan review\" notes that structural work, rather than ordinary flatwork, is what pulls in a state-registered engineer or architect for a closer look "
         f"({ext(BLDGFAQ_URL, 'the city\'s Building Permit FAQ')}). An ordinary backyard {svc('concrete-patios', 'patio')} addition typically clears that review without needing an engineer's stamp, though the building-permit application itself still applies.</p>"),
        ("A 2002 median build year means the yard around it is often already finished",
         f"<p>Census Reporter's profile of Apopka puts the median year a home here was built at 2002 "
         f"({ext(ACS_URL, 'Census Reporter, Apopka FL')}), a generation of houses old enough that the driveway, walkway and often a first patio are already in place by the time a homeowner is planning an addition or an expansion. That changes the planning question from \"where does everything go\" to \"how much room is actually left,\" since the slab has to fit around an existing layout rather than start from bare dirt.</p>"),
    ],
    "scenario": ("A patio addition on an established lot, worked out in square feet",
                 f"<p>A 16 by 20 ft patio off the back of the house comes to 320 sq ft, and at {price('concrete-patio')} per {per('concrete-patio')}, that pour runs roughly $1,920 to $4,160 before a decorative finish is added. "
                 "On a lot built out around the city's 2002 median, that 320 sq ft usually has to tie into an existing lanai slab or work around mature landscaping already in place, which is a different planning problem than laying out a patio on a lot where nothing has been poured yet.</p>"),
    "faqs": [
        faq("Does a concrete patio need a permit in Apopka?",
            "Yes. The city's general permit trigger covers any structure, including a patio slab, and the application goes through the Building-Safety Department the same way a driveway or addition would."),
        faq("Does an Apopka patio addition need an engineer's stamp?",
            "Usually not for ordinary flatwork. The city reserves plan review requiring a state-registered architect or engineer mainly for structural work, which a typical backyard patio slab doesn't trigger."),
        faq("Why does an Apopka patio project often work around existing landscaping?",
            "Because the city's typical home dates to 2002, a lot of lots already have a mature yard, driveway and walkway in place, so a patio addition has to fit into that existing layout rather than start from an empty lot."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Apopka, FL – Spring-Fed Ground",
    "meta": "Paver patio installers in Apopka, FL: the karst geology feeding Wekiwa Springs and what it means for drainage near a patio base, Oct. 2026.",
    "h1": "Paver Patios and Walkways for Apopka Backyards",
    "lede": capsule(f"A paver patio built in Apopka this October runs {price('paver-patio')} per {per('paver-patio')}, within the broader Florida range contractors are quoting. "
                     "The city sits on ground shaped by the same limestone system that feeds Wekiwa Springs, and the soils under a typical backyard here range from fast-draining ridge sand to wetter flatwoods pockets within a short distance of each other."),
    "sections": [
        ("A spring-fed landscape sits just outside the city limits",
         f"<p>Wekiwa Springs State Park, bordering Apopka, covers roughly 7,000 acres and its spring feeds about 42 million gallons of water a day into the Wekiva River, which the park holds the headwaters of "
         f"({ext(WEKIWA_URL, 'Wikipedia, Wekiwa Springs State Park')}). That volume of water moving through limestone conduits is a reminder that the ground under much of north Orange County isn't uniform, and a {svc('paver-patios', 'paver patio')} base that assumes one soil type across the whole yard can run into a surprise a few feet from where a test hole was dug.</p>"),
        ("Ridge sand and flatwoods soil can trade places within the same yard",
         f"<p>Candler and Tavares soils, both excessively to moderately well drained with the water table well below the surface, show up across much of the sand-ridge ground common in north and west Orange County, while Myakka and Smyrna, both poorly drained flatwoods soils, hold water within 18 inches of the surface for months at a time in lower spots "
         f"({src('nrcs-candler-osd', 'NRCS Official Series Description, Candler')}; {src('nrcs-myakka-osd', 'NRCS Official Series Description, Myakka')}). On a lot where the back half of the yard sits lower than the front, a paver base crew sometimes finds both conditions on the same property, which is why a soil check at the actual patio location matters more than a general assumption about the neighborhood.</p>"),
    ],
    "scenario": ("A paver patio checked against two different corners of the same lot, worked out in square feet",
                 f"<p>Picture an 18 by 18 ft paver patio, 324 sq ft, planned for the back corner of a yard that slopes gently from the house toward a drainage swale. At {price('paver-patio')} per {per('paver-patio')}, that job runs roughly $3,240 to $5,508 depending on the paver and base depth. "
                 "If that low corner tests out as wetter flatwoods soil while the rest of the lot drains like ridge sand, the crew typically adds a few extra inches of compacted base under just that section rather than deepening the whole patio uniformly.</p>"),
    "faqs": [
        faq("Does Apopka's limestone geology affect a paver patio base?",
            "Indirectly. The same limestone system that feeds Wekiwa Springs underlies much of the area, and while it doesn't set a specific paver spec, it's part of why soil conditions can vary noticeably within a single yard."),
        faq("Can one yard in Apopka have two different soil types?",
            "Yes. Fast-draining ridge sand and wetter flatwoods soil both occur in north Orange County, and a sloped lot can carry both, which is why a base crew checks the actual patio footprint rather than assuming one soil type for the whole property."),
        faq("Is Wekiwa Springs close enough to Apopka to affect a backyard project?",
            "The park borders the city, and while there's no setback rule tied to the spring itself for an ordinary residential patio, the groundwater system it belongs to is part of the reason local soil can be unpredictable over short distances."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Apopka, FL – Growth",
    "meta": "Concrete pool deck builders in Apopka, FL: new pools on recently platted lots and the city's structure-wide permit rule, Oct. 2026.",
    "h1": "Concrete Pool Decks for Apopka Homes",
    "lede": capsule(f"A concrete pool deck in Apopka falls between {price('concrete-pool-deck')} per {per('concrete-pool-deck')} under current October 2026 Florida pricing. "
                     "With the city's population up nearly 20 percent since 2020, a larger share of pool decks going in now are poured alongside a brand-new pool shell than resurfaced over an older one."),
    "sections": [
        ("New construction is driving a lot of first-time pool deck pours",
         f"<p>Apopka's population climbed from 54,892 in 2020 to an estimated 65,552 by mid-2025 "
         f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}), growth that Wikipedia, drawing on Census figures, describes as the city \"expanding in all directions\" "
         f"({ext(WIKI_URL, 'Wikipedia, Apopka, Florida')}). That pace of building means a {svc('concrete-pool-decks', 'pool deck')} poured this fall is more likely to be going in around a pool shell set the same month than replacing a deck that's spent two decades in the Florida sun.</p>"),
        ("The same building-permit trigger applies whether the pool is new or the deck is a redo",
         f"<p>Apopka's permit rule doesn't distinguish between a deck poured with a new pool and one added later to an existing pool, since both count as a structure under the city's own definition "
         f"({ext(BLDGFAQ_URL, 'the city\'s Building Permit FAQ')}). The fee still runs off the contract value at $7.50 per $1,000 with a $75 floor "
         f"({ext(FEE_URL, 'Apopka Permitting Fees')}), so a larger decorative deck carries a higher permit fee than a plain broom-finish one of the same footprint simply because the contract price is higher.</p>"),
    ],
    "scenario": ("A new pool deck sized to a freshly set shell, worked out in square feet",
                 f"<p>A newly built home pouring a 550 sq ft deck around a just-installed pool shell prices out between roughly $2,750 and $8,250 once the {price('concrete-pool-deck')} per {per('concrete-pool-deck')} range is applied, trending toward the higher end for a cool-touch decorative finish. "
                 "Because that deck and the pool itself are going in together, the pour schedule usually works around the pool contractor's own timeline rather than fitting into an already-landscaped yard the way a deck replacement would.</p>"),
    "faqs": [
        faq("Are most new Apopka pool decks poured with a new pool or added to an old one?",
            "A growing share are poured alongside a brand-new pool shell, since the city's rapid growth means more first-time installs than deck replacements compared with older, slower-growing Central Florida cities."),
        faq("Does Apopka's permit process treat a new pool deck differently from a replacement?",
            "No. Both fall under the same structure-wide permit trigger and the same $7.50-per-$1,000 fee formula; the fee itself tracks the contract price rather than whether the deck is new or a redo."),
        faq("What's the price range for a concrete pool deck in Apopka?",
            f"Figure {price('concrete-pool-deck')} per {per('concrete-pool-deck')} heading into the last part of 2026, with a plain broom finish toward the lower end and a cool-touch decorative texture pushing it higher."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Apopka, FL – Watering Rules",
    "meta": "Pool deck paver installers in Apopka, FL: how Orange County's normal watering schedule compares to Lake County's stricter order next door, Oct. 2026.",
    "h1": "Travertine and Paver Pool Decks in Apopka",
    "lede": capsule(f"A travertine or concrete-paver pool deck in Apopka costs {price('pool-deck-pavers')} per {per('pool-deck-pavers')} this fall, under current Florida contractor rates. "
                     "A yard on Apopka's west side and one a few miles over the Lake County line can look identical, but one answers to a stricter sprinkler schedule than the other, a distinction worth knowing before landscaping goes in around a new deck."),
    "sections": [
        ("Orange County runs the ordinary St. Johns schedule, not the tighter one",
         f"<p>Apopka sits in Orange County, which the St. Johns River Water Management District states plainly \"is to follow the St. Johns restrictions,\" its standard year-round, twice-a-week calendar rather than any emergency order "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}). That's a meaningfully lighter rule than the district's Phase III Extreme Water Shortage order, which currently covers parts of neighboring Lake County under a stricter one-day-a-week schedule with an 8 a.m. to 6 p.m. no-watering window "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}).</p>"),
        ("New sod around a freshly built deck gets a grace period either way",
         f"<p>Under the district's normal rule that covers Apopka, newly planted sod or landscaping can be watered daily for its first 30 days, then every other day for the next 30, before dropping onto the ordinary twice-a-week calendar "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}). That matters for the grass or ground cover planted around a freshly set {svc('pool-deck-pavers', 'paver pool deck')}, which often needs more frequent watering than the mature lawn it's replacing during its first month in the ground.</p>"),
    ],
    "scenario": ("Timing new sod around a freshly paved deck, worked out in square feet",
                 f"<p>Take a 500 sq ft travertine deck poured around a brand-new pool shell, with the strip of disturbed yard around it resodded the same week. Pricing the deck itself against {price('pool-deck-pavers')} per {per('pool-deck-pavers')} puts that portion at roughly $6,500 to $15,000 depending on the stone chosen. "
                 "That resodded strip qualifies for the district's 30-day daily watering window, stepping down to every other day for 30 more days before it settles onto Orange County's standard twice-a-week calendar, a schedule that wouldn't carry over the same way for a lot a few miles west under Lake County's tighter order.</p>"),
    "faqs": [
        faq("Is Apopka under the same strict watering limits as parts of Lake County?",
            "No. Orange County, which includes Apopka, follows the St. Johns district's ordinary twice-a-week schedule, while the district's Phase III Extreme Water Shortage order currently applies a stricter one-day-a-week rule to parts of neighboring Lake County."),
        faq("How long can new sod around a pool deck be watered daily in Apopka?",
            "Up to 30 days under the district's new-landscape exemption, then every other day for 30 more days, before the lawn moves onto the normal twice-a-week schedule."),
        faq("Why choose travertine over a concrete paver for an Apopka pool deck?",
            "Mainly comfort underfoot and look, since travertine stays noticeably cooler in direct sun than a dark concrete paver, though the budget difference between the two materials is usually the deciding factor for most homeowners."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Apopka, FL – Permit Basics",
    "meta": "Stamped concrete contractors in Apopka, FL: how the city's fee formula treats a decorative finish and its own permit-type list, Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Apopka",
    "lede": capsule(f"Stamped concrete work in Apopka currently prices between {price('stamped-concrete')} per {per('stamped-concrete')}, swinging with how many colors and how deep a texture the pattern calls for. "
                     "A decorative finish doesn't change which permit applies here, but it does change the contract price the city's own fee formula is built around."),
    "sections": [
        ("A higher contract value on a decorative pour means a higher permit fee",
         f"<p>Because Apopka's permit fee runs off \"actual contracted cost or construction cost/value,\" at $7.50 per $1,000 with a $75 floor "
         f"({ext(FEE_URL, 'Apopka Permitting Fees')}), a multi-color stamped pattern with a custom border carries a higher permit fee than a plain gray pour of the identical footprint, simply because the job itself costs more. The permit-type list the Building Division publishes tracks building, electrical, mechanical, plumbing and gas work separately, so a {svc('stamped-concrete', 'stamped concrete')} job that also adds exterior lighting around a new patio can touch more than one of those categories "
         f"({ext(TYPES_URL, 'Apopka Permit Types')}).</p>"),
        ("The review process itself doesn't single out decorative work",
         f"<p>Apopka's general permit trigger covers construction, alteration or repair of a structure without naming finish type, and plan review requiring an outside architect or engineer is reserved mainly for structural work rather than surface treatment "
         f"({ext(BLDGFAQ_URL, 'the city\'s Building Permit FAQ')}). A stamped driveway or walkway clears the same Building-Safety Department review a plain broom-finish pour would, with the pattern and color choice left entirely to the homeowner.</p>"),
    ],
    "scenario": ("Pricing a stamped walkway and comparing the resulting permit fee",
                 f"<p>Take a running-bond, single-color stamped front walkway, 180 sq ft, priced against the {price('stamped-concrete')} per {per('stamped-concrete')} range: roughly $1,440 to $2,880 for the pour itself. A $2,200 contract for that job keeps the city's permit fee right at the $75 floor. "
                 "Add a second integral color and a deeper release texture, and the same 180 sq ft job might run closer to $4,000, which under the $7.50-per-$1,000 formula pushes the permit fee to around $30 above that floor, a small but real difference tied directly to the finish chosen.</p>"),
    "faqs": [
        faq("Does a stamped concrete driveway cost more to permit than a plain one in Apopka?",
            "It can, slightly. Since the city's fee formula is based on contract value, a pricier decorative job generates a somewhat higher permit fee than a plain pour of the same size, even though both go through the identical review."),
        faq("Does stamped concrete need plan review by an outside engineer in Apopka?",
            "Generally not. The city reserves that step mainly for structural work; an ordinary stamped driveway or patio clears the standard Building-Safety Department review without it."),
        faq("Can a stamped concrete project in Apopka involve more than one type of permit?",
            "It can if the job includes other trades, such as new exterior lighting or an electrical run to a water feature, since the city tracks building, electrical and other permit types separately."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Apopka, FL – Karst Ground",
    "meta": "Artificial turf installers in Apopka, FL: the state's turf rule, the spring-fed water system nearby, and the sinkhole-claims list, Oct. 2026.",
    "h1": "Artificial Turf for Apopka Yards",
    "lede": capsule(f"Turf installers are pricing Apopka jobs at {price('artificial-turf')} per {per('artificial-turf')} this fall. "
                     "The state's 2026 synthetic-turf rule sets the same base, drainage and water-body buffer here as anywhere else in Florida, and Orange County's place on the state's own sinkhole-claims list is a reason a washed, well-drained base matters more here than the turf material itself."),
    "sections": [
        ("The statewide base and buffer rules apply the same way in Apopka as anywhere else",
         f"<p>Florida's synthetic turf rule, effective May 19, 2026, requires a washed, permeable subgrade, bars buried irrigation lines under the turf, and keeps the panel at least 10 feet back from a pond, lake or canal edge unless a seawall already stands between the two "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A companion 2025 law caps how far a city or county can push its own turf rule past that state floor "
         f"({src('fs125572', 'Florida Statutes §125.572')}). On a lot near one of the ponds or drainage canals common in Apopka's newer subdivisions, that 10-foot line is worth measuring from the water's actual edge before a {svc('artificial-turf', 'turf')} layout is finalized.</p>"),
        ("A well-drained base matters more here than elsewhere in Orange County",
         f"<p>Florida Senate figures tied to a 2010 interim report place Orange among the counties that generated the bulk of the state's sinkhole insurance claims filed between 2006 and 2009 "
         f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}), geology connected to the same limestone system that feeds Wekiwa Springs and Rock Springs nearby "
         f"({ext(WEKIWA_URL, 'Wikipedia, Wekiwa Springs State Park')}). That doesn't make a settling patch of yard a sinkhole, but it is a reason the washed, compacted stone base the state's turf rule already requires gets built to spec rather than skipped, since a poorly draining base on ground like this can pond water the turf itself was supposed to shed.</p>"),
    ],
    "scenario": ("Working a pond setback into a backyard turf layout",
                 f"<p>Picture a 420 sq ft stretch of backyard that runs down to a retention pond on a newer Apopka lot: pulling the layout back the required 10 feet from the water's edge trims off about 50 sq ft, leaving roughly 370 sq ft to actually turf. At {price('artificial-turf')} per {per('artificial-turf')}, that comes to somewhere between $3,700 and $9,250 once pile height and backing are chosen. "
                 "Measuring from the pond's actual waterline, rather than from a fence set back from it, is what sets the real number before material gets ordered.</p>"),
    "faqs": [
        faq("How close to a retention pond can artificial turf go in Apopka?",
            "No closer than 10 feet from the water's actual edge under the statewide turf rule, unless a seawall or similar barrier already separates the lawn from the water."),
        faq("Does Orange County's sinkhole history mean turf shouldn't go on certain Apopka lots?",
            "Not as a rule, but it is a reason the washed, well-compacted base the state's turf standard already requires gets built properly, since a soft or poorly draining base is more likely to show a problem on ground tied to this kind of limestone geology."),
        faq("Can a homeowners association near Apopka still restrict artificial turf?",
            "An HOA's own architectural rules operate separately from the state law that limits city and county turf restrictions, so checking a specific community's guidelines is still worth doing before ordering material."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
