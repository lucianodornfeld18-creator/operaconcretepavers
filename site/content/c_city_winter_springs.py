# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "winter-springs"

WS_CODE_URL = "https://www.zoneomics.com/code/winter-springs-FL/chapter_5"
WS_SITEWORK_URL = "https://www.winterspringsfl.org/DocumentCenter/View/326/Site-Work-Permit-Application"
WS_CD_URL = "https://www.winterspringsfl.org/cd/page/building-permits"
TUSCAWILLA_ACC_URL = "https://countryclubvillageattuscawilla.com/acc-request"
WS_WIKI_URL = "https://en.wikipedia.org/wiki/Winter_Springs,_Florida"
LAKE_JESUP_WIKI = "https://en.wikipedia.org/wiki/Lake_Jesup"
CENTRAL_WINDS_URL = "https://playorlandonorth.com/facilities/central-winds-park/"
CENSUS_REPORTER_WS = "https://censusreporter.org/profiles/16000US1278325-winter-springs-fl/"

SRC = [
    "census-pep-v2025", "sjrwmd-watering", "fl-dos-state-soil", "dep-rule", "fs125572",
    ("City of Winter Springs Code of Ordinances §20-439, Parking Areas on Residential Lots (via Zoneomics)", WS_CODE_URL),
    ("City of Winter Springs, Site Work Permit Application", WS_SITEWORK_URL),
    ("City of Winter Springs, Building & Permits", WS_CD_URL),
    ("Country Club Village at Tuscawilla, ACC Request (Bylaws Exhibit IX, Driveway Pavers)", TUSCAWILLA_ACC_URL),
    ("Wikipedia, Winter Springs, Florida", WS_WIKI_URL),
    ("Wikipedia, Lake Jesup", LAKE_JESUP_WIKI),
    ("Play Orlando North, Central Winds Park", CENTRAL_WINDS_URL),
    ("Census Reporter, Winter Springs, FL (ACS 2024 5-yr, B25035)", CENSUS_REPORTER_WS),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Who signs off on a new driveway or paver job in Winter Springs?",
        f"<p>Community Development, the department that runs permitting out of 1126 East State Road 434 and answers at 407-327-5963, reviews it ({ext(WS_CODE_URL, 'Winter Springs Code §20-439')}). The city's own zoning code puts the trigger plainly: a driveway construction permit is required “whenever impervious materials are used to construct a driveway or designated parking area, or whenever a new designated parking area is constructed on any residential lot” (Code §20-439(f)). That line doesn't mention a dollar figure, which matters once Florida's 2026 small-job exemption enters the conversation below.</p>"),
    sec("Does the 2026 permit exemption let a Winter Springs homeowner skip that review?",
        f"<p>House Bill 803 waives a <em>building</em> permit for qualifying single-family work under $7,500 starting July 1, 2026, but Winter Springs' driveway rule doesn't live in the building code; it's written into the zoning chapter that governs parking areas on residential lots ({ext(WS_CODE_URL, 'Code §20-439')}). Because that section triggers on the material, not the price tag, a $4,000 apron replacement still needs the same driveway construction permit a $14,000 one does. {svc('concrete-driveways', 'A new driveway')} or {svc('paver-driveways', 'a paver driveway')} both fall under it the same way.</p>"),
    sec("What can a Winter Springs driveway actually be built from, and how wide?",
        f"<p>For any residential lot developed or redeveloped after August 11, 2009, the code lists the approved materials by name: “concrete, asphalt, decorative pavers, brick, Eco-brick, crushed rock, gravel, geo-web with gravel, or turf block” ({ext(WS_CODE_URL, 'Code §20-439(e)')}). Width is tied to the garage rather than a flat number: a driveway “shall not exceed the width of the garage or carport,” and a lot gets at most one separate designated parking area, capped at 12 feet wide. Worth flagging on the {svc('artificial-turf', 'artificial-turf')} side: “turf block” on that list is an open-cell concrete paver meant to be planted with grass, a different product from the synthetic lawn turf covered further down this page, so the two shouldn't be confused when reading the ordinance.</p>"),
    sec("Does a golf-course neighborhood like Tuscawilla add its own review?",
        f"<p>It can. Country Club Village at Tuscawilla, one of the HOAs inside the larger Tuscawilla community, spells out in its bylaws that redoing a driveway in new pavers, or laying thin pavers over the existing slab, “would need to be approved by the ACC with respect to color, style and configuration,” under an exhibit of its governing documents titled Driveway Pavers ({ext(TUSCAWILLA_ACC_URL, 'Country Club Village at Tuscawilla, ACC Request')}). That association review sits on top of, not instead of, the city's own permit; a homeowner inside that HOA budgets time for both approvals before pallets show up.</p>"),
    sec("How does sitting on Lake Jesup change where a project's water goes?",
        f"<p>Winter Springs holds the only piece of city-owned, developed shoreline on the lake, inside Central Winds Park, a 103-acre complex that “includes sparkling Lake Jesup and a nature trail” and has run since 1992 ({ext(CENTRAL_WINDS_URL, 'Central Winds Park')}). Lake Jesup itself covers roughly 16,000 acres as part of the St. Johns River's middle basin, averaging only about 6 feet deep ({ext(LAKE_JESUP_WIKI, 'Lake Jesup')}). No published number in either the driveway code or the Site Work Permit guidance sets how far back a {svc('retaining-walls', 'retaining wall')} or a {svc('concrete-pool-decks', 'pool deck')} has to sit from that shoreline; on a lot that slopes toward the park, figuring out where the fill and runoff end up is something a crew works out by walking the yard, not something printed in an ordinance.</p>"),
    sec("What does a median 1989 build year tell a crew about the ground?",
        f"<p>The city grew from a settlement first known as “Tuskawilla” around 1865 into the incorporated “City of North Orlando” in 1959, then took its current name in 1972 once officials realized the old name confused people about where it actually sat relative to Orlando ({ext(WS_WIKI_URL, 'Wikipedia, Winter Springs, Florida')}). Census Bureau estimates put the city's population at 39,585 as of July 1, 2025 ({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}), and the typical home dates to 1989 (Census Reporter, ACS 2024 5-yr estimate, {ext(CENSUS_REPORTER_WS, 'B25035')}). That puts a meaningful share of original driveways and pool decks past the three-and-a-half-decade mark, old enough that a resurfacing or overlay conversation is common rather than unusual.</p>"),
    sec("Does Winter Springs sit on the same flatwoods ground as the rest of Seminole County?",
        f"<p>Much of it does. Myakka fine sand, the flatwoods soil typical across Seminole County, became Florida's official state soil by legislative designation in 1989 and underlies more than 1.5 million acres statewide ({src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}); on a lot carrying that kind of ground, the base for {svc('concrete-slabs', 'a slab')} or a {svc('paver-patios', 'paver patio')} gets priced after a look at the yard, not assumed from the plan alone. The district that governs irrigation here, SJRWMD, actually runs two separate calendars depending on the time of year: a two-day split by address during Daylight Saving Time, collapsing to a single assigned day per address, Saturday for odd and no-number homes, Sunday for even ones, once clocks fall back to Eastern Standard Time ({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}).</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Winter Springs require a permit for a paver driveway the same way it does for concrete?",
        "Yes. Code §20-439(f) requires a driveway construction permit whenever impervious materials go into a driveway or designated parking area, and decorative pavers are named on the approved-materials list the same as concrete and asphalt."),
    faq("Does Florida's 2026 small-project exemption cover a Winter Springs driveway?",
        "Not on its own. HB 803 waives a building permit for qualifying work under $7,500, but Winter Springs' driveway requirement sits in the zoning code and triggers on the material used rather than the project's value, so it applies regardless of price."),
    faq("Is Tuscawilla's HOA review the same across the whole community?",
        "No single answer covers every Tuscawilla association; Country Club Village at Tuscawilla's own bylaws specifically require ACC approval of color, style and configuration for driveway pavers, and a different HOA inside the broader Tuscawilla area may run its own separate process."),
    faq("Do Winter Springs' watering days change once Daylight Saving Time ends?",
        "Yes. SJRWMD runs a two-day schedule by address during Daylight Saving Time, but once clocks fall back to Eastern Standard Time, each address drops to a single assigned day, Saturday for odd and no-number homes, Sunday for even-numbered ones."),
    faq("What's worth checking before hiring a concrete or paver contractor in Winter Springs?",
        f"Confirm the contractor on the state's license-lookup tool, and make sure the written quote already assumes Community Development's driveway construction permit rather than treating it as optional or bundled in later. {post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} covers the rest of what a solid estimate should include, including how to judge the best fit for a given project."),
]

HUB = page("/winter-springs-fl/", "city", "Concrete, Pavers & Turf Contractor in Winter Springs, FL",
           "Opera pours concrete, sets pavers and installs turf in Winter Springs, FL, where Code §20-439 requires a driveway permit by material, not price, as of October 2026.",
           "Concrete, Pavers and Artificial Turf Built for Winter Springs Homes",
           capsule(f"Opera pours concrete, sets pavers and installs artificial turf for homeowners in Winter Springs, a Seminole County city of about 39,585 residents whose zoning code requires a driveway construction permit for any impervious material, independent of project cost. "
                   f"As of October 2026, a new concrete driveway here runs {price('concrete-driveway')} per {per('concrete-driveway')}, with the Orlando unit's base roughly {str(__import__('_data').CITIES['winter-springs']['miles'])} miles south."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Winter Springs",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Driveway and patio permits in Seminole County"),
                    ("/oviedo-fl/", "Concrete, pavers and turf in Oviedo"),
                    ("/sanford-fl/", "Concrete, pavers and turf in Sanford"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Winter Springs, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Winter Springs, FL",
    "meta": "Concrete driveway contractors in Winter Springs, FL: why Code §20-439 requires a permit for any impervious driveway, regardless of job value, October 2026.",
    "h1": "Pouring a Concrete Driveway in Winter Springs",
    "lede": capsule(f"A new or replacement concrete driveway in Winter Springs runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "The city's zoning code requires a driveway construction permit whenever impervious material goes down, a rule written around the material rather than the dollar amount, so it reaches small jobs the same way it reaches large ones."),
    "sections": [
        ("A driveway permit here is triggered by the material, not the price tag",
         f"<p>Winter Springs Code §20-439(f) requires a driveway construction permit “whenever impervious materials are used to construct a driveway or designated parking area, or whenever a new designated parking area is constructed on any residential lot” ({ext(WS_CODE_URL, 'Winter Springs Code §20-439')}). Florida's 2026 small-job exemption waives a <em>building</em> permit under $7,500, but that exemption doesn't touch a zoning-code trigger built around the material itself; Community Development, reachable at 407-327-5963, reviews a concrete apron the same way whether the contract runs $3,000 or $13,000.</p>"),
        ("Width is measured against the garage, not a flat number",
         f"<p>Rather than publish a fixed maximum, the code ties driveway width to the house: a driveway “shall not exceed the width of the garage or carport, whichever is greater.” Concrete is named directly among the approved materials for any lot developed or redeveloped since August 11, 2009 ({ext(WS_CODE_URL, 'Code §20-439(e)')}), so a two-car garage with a 20-foot door opening sets the ceiling for how wide the slab in front of it can legally run.</p>"),
    ],
    "scenario": ("A driveway sized to a two-car garage opening, worked out in square feet",
                 f"<p>Picture a home with a 20-foot-wide garage door and a driveway running 24 feet back to the street, 480 sq ft total, replacing a cracked original slab. At {price('concrete-driveway')} per {per('concrete-driveway')}, that lands between roughly $2,880 and $7,200 before any demolition is added. "
                 "Because the new slab matches the garage width rather than widening the throat, the project clears Code §20-439's width rule without a variance; the driveway construction permit still applies, since the job replaces an impervious surface regardless of how modest the contract price comes in.</p>"),
    "faqs": [
        faq("Does a small concrete driveway repair skip Winter Springs' permit under the 2026 exemption?",
            "Not automatically. The city's driveway construction permit triggers on the use of impervious material, not on project cost, so Florida's 2026 small-job building-permit waiver doesn't reach it the way it would a different kind of interior work."),
        faq("How wide can a concrete driveway be in Winter Springs?",
            "The code ties it to the garage: a driveway can't exceed the width of the garage or carport, whichever is greater, rather than a single citywide number."),
        faq("Who reviews a Winter Springs driveway permit application?",
            "Community Development, out of 1126 East State Road 434, reachable at 407-327-5963."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Winter Springs, FL",
    "meta": "Paver driveway installers in Winter Springs, FL: the city's approved-materials list and Tuscawilla's own ACC review for driveway pavers, October 2026.",
    "h1": "Paver Driveways in Winter Springs: Two Layers of Review",
    "lede": capsule(f"Expect {price('paver-driveway')} per {per('paver-driveway')} for a paver driveway in Winter Springs as of October 2026. "
                     "Decorative pavers sit on the city's own approved-materials list for driveways, but a golf-course neighborhood like Tuscawilla can add its own architectural review on top of that city permit."),
    "sections": [
        ("Decorative pavers are named on the city's materials list",
         f"<p>Winter Springs' zoning code spells out which surfaces qualify for a residential driveway or designated parking area built since August 11, 2009: “concrete, asphalt, decorative pavers, brick, Eco-brick, crushed rock, gravel, geo-web with gravel, or turf block” ({ext(WS_CODE_URL, 'Code §20-439(e)')}). Pavers clear that list without an exception, but the same section's permit trigger still applies: any impervious material, including pavers, needs the driveway construction permit from Community Development before installation starts.</p>"),
        ("Tuscawilla's Country Club Village layers its own ACC sign-off on top",
         f"<p>Inside Country Club Village at Tuscawilla, one HOA within the larger Tuscawilla community, the governing bylaws carry an exhibit specifically titled Driveway Pavers: redoing the whole driveway in new pavers, or laying thin pavers over the existing slab, “would need to be approved by the ACC with respect to color, style and configuration” ({ext(TUSCAWILLA_ACC_URL, 'Country Club Village at Tuscawilla, ACC Request')}). That review is separate from, and in addition to, the city's own permit; {cs('winter-springs', 'concrete-driveways', 'a plain concrete driveway')} in the same HOA would still need ACC sign-off on its finish even though it isn't a paver product.</p>"),
    ],
    "scenario": ("A paver overlay inside an HOA that reviews color and pattern",
                 f"<p>Say a home inside Country Club Village at Tuscawilla has a 440 sq ft driveway and wants thin pavers set over the existing concrete rather than a full tear-out. At {price('paver-driveway')} per {per('paver-driveway')}, that overlay runs roughly $5,280 to $8,800 depending on the paver chosen. "
                 "Before ordering material, the homeowner submits the proposed color, style and configuration to the ACC under the bylaws' Driveway Pavers exhibit, and separately files for Community Development's driveway construction permit; one approval doesn't substitute for the other.</p>"),
    "faqs": [
        faq("Are decorative pavers an approved driveway material in Winter Springs?",
            "Yes. The zoning code's approved-materials list for driveways and designated parking areas names decorative pavers directly, alongside concrete, asphalt, brick and several other surfaces."),
        faq("Does every Tuscawilla HOA require ACC approval for driveway pavers?",
            "Country Club Village at Tuscawilla's bylaws do, under an exhibit specifically covering driveway pavers; other HOAs inside the broader Tuscawilla community may run a different process, so check the specific association's documents rather than assume one rule covers all of Tuscawilla."),
        faq("Does a paver overlay over existing concrete still need the city's driveway permit?",
            "Yes. The permit trigger is the use of impervious material for the driveway, which an overlay satisfies the same way new construction does."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Winter Springs, FL",
    "meta": "Concrete patio contractors in Winter Springs, FL: the city's Site Work Permit for paving and drainage, and flatwoods soil, October 2026.",
    "h1": "Building a Concrete Patio in Winter Springs",
    "lede": capsule(f"A concrete patio in Winter Springs falls between {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "The city's Site Work Permit covers “Paving, Grading, and Drainage” as one of its listed work types, and the flatwoods soil under much of Seminole County shapes how that patio needs to be pitched."),
    "sections": [
        ("A patio pour falls under the city's paving-and-drainage permit category",
         f"<p>Winter Springs' Site Work Permit application, revised May 2024, lists “Paving, Grading, and Drainage” as one of the project types a homeowner checks off alongside clearing and grubbing or a temporary construction fence ({ext(WS_SITEWORK_URL, 'City of Winter Springs, Site Work Permit Application')}). Work has to start within 60 days of the permit being issued and finish within one year, or the permit expires, the same clock the city puts on its driveway permits. A backyard {svc('concrete-patios', 'patio')} addition is paving work in the plainest sense, so it falls inside that category rather than skating past permitting because it sits on private ground.</p>"),
        ("On flatwoods ground, the base gets built thicker, not just graded differently",
         f"<p>Myakka fine sand, the flatwoods soil common across Seminole County, became Florida's official state soil in 1989 ({src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}). Industry guidance for paver bases (ICPI Tech Spec 2) calls for adding 2 to 4 extra inches of compacted aggregate specifically on continually wet or weak soils, the category flatwoods ground with a shallow water table falls into; the same logic carries over to how much fill a crew compacts under a concrete patio before the forms go up, even though the finished slab looks identical either way once it's poured.</p>"),
    ],
    "scenario": ("An outdoor-kitchen pad off a lanai, priced by the square foot",
                 f"<p>A homeowner wants a 220 sq ft pad for an outdoor kitchen built onto the side of an existing lanai, on a lot where the backyard holds water a day or two after a hard summer storm. Quoted at {price('concrete-patio')} per {per('concrete-patio')}, the pour comes to roughly $1,320 to $2,860 before any counter or grill structure is added on top. "
                 "Because this is new paved surface, the Site Work Permit's paving-and-drainage category applies the same as it would to a driveway, and the extra base thickness that flatwoods soil calls for gets built into the quote rather than discovered mid-pour.</p>"),
    "faqs": [
        faq("What permit covers a new concrete patio in Winter Springs?",
            "The city's Site Work Permit, which lists “Paving, Grading, and Drainage” as one of its project types, covers a patio addition along with other paving and grading work."),
        faq("How long is a Winter Springs Site Work Permit valid for?",
            "Work must commence within 60 days of issuance and be completed within one year, or the permit expires."),
        faq("Does flatwoods soil change how a Winter Springs patio gets built, not just how it looks?",
            "It can change the base thickness. Industry guidance adds 2 to 4 extra inches of compacted aggregate under paving on continually wet or weak soils, a category that includes the flatwoods ground common across Seminole County, even though the finished slab on top looks no different."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Winter Springs, FL",
    "meta": "Paver patio installers in Winter Springs, FL near Lake Jesup and Central Winds Park, about a dozen miles from Orlando, October 2026.",
    "h1": "Paver Patios and Walkways for Winter Springs Yards",
    "lede": capsule(f"A paver patio in Winter Springs runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     f"The city sits roughly {str(__import__('_data').CITIES['winter-springs']['miles'])} miles from the Orlando unit's base and holds the only developed, city-owned shoreline on Lake Jesup, inside Central Winds Park, so a lot anywhere near that side of town drains toward one of the largest lakes in the St. Johns River system."),
    "sections": [
        ("Lake Jesup sets the drainage backdrop for lots on that side of town",
         f"<p>Lake Jesup covers roughly 16,000 acres as part of the St. Johns River's middle basin, with a maximum depth of only about 10 feet and an average around 6 ({ext(LAKE_JESUP_WIKI, 'Lake Jesup')}). Central Winds Park, the city's 103-acre complex that “includes sparkling Lake Jesup and a nature trail,” has sat on that shoreline since 1992 ({ext(CENTRAL_WINDS_URL, 'Central Winds Park')}). Neither the city's Site Work Permit guidance nor its driveway code publishes a fixed setback from the lake for a {svc('paver-patios', 'paver patio')}; a yard that slopes toward it gets its grading worked out on site instead.</p>"),
        ("The same paving-and-drainage permit covers a patio whether it's concrete or pavers",
         f"<p>Winter Springs' Site Work Permit application groups “Paving, Grading, and Drainage” under one checkbox, so a paver patio goes through the identical review {cs('winter-springs', 'concrete-patios', 'a poured concrete patio')} does, with work required to start within 60 days of issuance and wrap within a year ({ext(WS_SITEWORK_URL, 'City of Winter Springs, Site Work Permit Application')}).</p>"),
    ],
    "scenario": ("A paver patio on a lot a short walk from the Lake Jesup shoreline, worked out in square feet",
                 f"<p>Take a home a few streets from Central Winds Park adding a 18 by 16 ft paver patio, 288 sq ft, off the side of the house where the yard slopes gently toward the park's tree line. At {price('paver-patio')} per {per('paver-patio')}, that job runs roughly $3,456 to $4,608 depending on the paver pattern. "
                 "Before the base goes down, the crew checks where that slope already carries water, since nothing in the city's published guidance sets a specific setback from Lake Jesup itself, only the general expectation that water keeps moving away from the house.</p>"),
    "faqs": [
        faq("Is there a published setback from Lake Jesup for a paver patio in Winter Springs?",
            "Not in the city's Site Work Permit guidance or its driveway code. The practical question is grading, since a lot sloping toward the lake has less natural fall to shed water than one farther from it."),
        faq("How far is Winter Springs from the Orlando unit's base?",
            f"Roughly {str(__import__('_data').CITIES['winter-springs']['miles'])} miles. The city holds the only city-owned, developed shoreline on Lake Jesup, inside Central Winds Park."),
        faq("Does a paver patio need a different permit than a concrete one in Winter Springs?",
            "No. Both fall under the same Site Work Permit category for paving, grading and drainage."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Winter Springs, FL",
    "meta": "Concrete pool deck builders in Winter Springs, FL: original late-1980s decks and the city's paving-permit category, October 2026.",
    "h1": "Concrete Pool Decks for Winter Springs Homes",
    "lede": capsule(f"A concrete pool deck in Winter Springs runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} in the Florida market as of October 2026. "
                     "With the city's typical home dating to 1989, a share of the original pool decks are old enough that a resurfacing decision is more common than a first installation."),
    "sections": [
        ("A deck from the city's median build year has logged nearly four decades of Florida sun",
         f"<p>Census Reporter's latest ACS estimate puts Winter Springs' median year structure built at 1989 (Census 2024 5-yr, table B25035, {ext(CENSUS_REPORTER_WS, 'Census Reporter, Winter Springs FL')}), a period when the city's population was still climbing fast after its 1972 renaming from the City of North Orlando ({ext(WS_WIKI_URL, 'Wikipedia, Winter Springs, Florida')}). A pool deck poured around that time has had close to four decades of heat cycling and UV exposure, long enough for a worn cool-deck coating or a network of hairline cracks to call for a resurfacing decision rather than another spot patch.</p>"),
        ("The paving-and-drainage permit covers a deck replacement, not just new construction",
         f"<p>Winter Springs' Site Work Permit groups paving, grading and drainage work under one application type, which covers a pool deck resurfacing or tear-out the same way it covers a brand-new pour ({ext(WS_SITEWORK_URL, 'City of Winter Springs, Site Work Permit Application')}). The 60-day start clock and one-year completion window apply either way, so scheduling the resurfacing crew after the permit is issued, not before, keeps the project inside that window.</p>"),
    ],
    "scenario": ("Weighing resurfacing against a tear-out on a 1989-era deck, worked out in square feet",
                 f"<p>Picture a 600 sq ft pool deck original to a home built around the city's 1989 median, with a chalky cool-deck coating and a few hairline cracks radiating from the coping. Resurfacing it at {price('concrete-pool-deck')} per {per('concrete-pool-deck')} lands between roughly $3,000 and $7,200, cheaper for a plain broom finish and pricier for a decorative overlay. "
                 "A full tear-out and repour costs more up front once demolition and disposal are added, and makes more sense once cracking has worked its way past the surface coating and into the slab itself.</p>"),
    "faqs": [
        faq("Should an original Winter Springs pool deck from the late 1980s be resurfaced or replaced?",
            "Often resurfaced, if the cracking is limited to the surface coating rather than the slab underneath. With the city's median home dating to 1989, hairline cracking and a worn coating on flatwork that age is common wear, not necessarily a structural problem."),
        faq("What permit covers a pool deck replacement in Winter Springs?",
            "The Site Work Permit, under its paving, grading and drainage category, the same application used for a new deck or a patio."),
        faq("How long does a Winter Springs Site Work Permit stay valid once issued?",
            "Work has to start within 60 days and be completed within one year, or the permit expires."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Winter Springs, FL",
    "meta": "Pool deck paver overlays in Winter Springs, FL for decks nearing the city's 1989 median build year, with HOA review inside Tuscawilla, October 2026.",
    "h1": "Pool Deck Pavers in Winter Springs: Overlays and New Builds",
    "lede": capsule(f"Pool deck pavers for a Winter Springs backyard run {price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026, set fresh over a new shell or layered over a deck that's already cracking. "
                     "A 1989 median build year puts a sizable share of the city's cool-deck surfaces at an age where an overlay gets priced alongside demolition rather than skipped."),
    "sections": [
        ("1989 is the pivot point for a lot of cool-deck coatings here",
         f"<p>Census Reporter's ACS 2024 5-yr estimate puts Winter Springs' median year structure built at 1989 ({ext(CENSUS_REPORTER_WS, 'Census Reporter, Winter Springs FL')}); a pool built around that time has had roughly three and a half decades for its spray-texture coating to chalk, pit and crack along the coping line. Whether that surface still holds a {svc('pool-deck-pavers', 'paver overlay')} comes down to how far the cracking has traveled into the slab underneath, not just how the deck looks from the lanai.</p>"),
        ("One permit covers both a first pour and a resurfacing job",
         f"<p>The city doesn't run a separate paperwork track for new construction versus resurfacing work; its Site Work Permit groups paving, grading and drainage under one application, and a pool deck overlay qualifies as paving the same way a brand-new deck does ({ext(WS_SITEWORK_URL, 'City of Winter Springs, Site Work Permit Application')}). Inside Country Club Village at Tuscawilla specifically, the HOA's published exhibit on ACC review names driveway pavers, not pool decks, so a homeowner there confirms with the association directly rather than guess whether that same clause reaches the backyard ({ext(TUSCAWILLA_ACC_URL, 'Country Club Village at Tuscawilla, ACC Request')}).</p>"),
    ],
    "scenario": ("Deciding between a thin overlay and a full demolition",
                 f"<p>A 480 sq ft deck around an in-ground pool, poured in the late 1980s, has gone chalky and shows a scatter of hairline cracks near the skimmer. Setting pavers over it at {price('pool-deck-pavers')} per {per('pool-deck-pavers')} works out to roughly $6,720 for standard concrete paver and nearer $14,500 if travertine goes down instead. "
                 "Demolition adds to the total if the crew opts for a full rebuild rather than an overlay, which tends to be the better call once a crack has worked down through the original slab rather than sitting in the coating alone.</p>"),
    "faqs": [
        faq("Does a cracked Winter Springs pool deck need a tear-out before pavers go down?",
            "Not always. If the cracking stays in the surface coating rather than the slab itself, an overlay set under the city's Site Work Permit is often the less expensive route than full demolition."),
        faq("Does Tuscawilla's ACC review extend to pool deck pavers, not just driveways?",
            "The published exhibit in Country Club Village at Tuscawilla's bylaws names driveway pavers specifically; confirm with the association directly before assuming the same clause governs a backyard pool deck."),
        faq("Why do so many Winter Springs pool decks need attention around the same age?",
            "The city's median home was built in 1989, which puts a cluster of original pool decks at roughly the same point in their service life, where a coating that chalked years ago finally starts cracking."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Winter Springs, FL",
    "meta": "Stamped concrete contractors in Winter Springs, FL: how the city's driveway code treats decorative finishes and flatwoods subgrade, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Winter Springs",
    "lede": capsule(f"Stamped concrete work in Winter Springs falls between {price('stamped-concrete')} per {per('stamped-concrete')} as of October 2026, moving with the pattern and number of colors. "
                     "The city's driveway code names “concrete” as an approved material without separating plain gray from a decorative finish, so a stamped slab clears the same bar a broom-finish one does."),
    "sections": [
        ("The approved-materials list doesn't single out a finish",
         f"<p>Winter Springs Code §20-439(e) names “concrete” among the approved driveway surfaces for any lot developed or redeveloped since August 11, 2009, without distinguishing a plain pour from a stamped, stained or exposed-aggregate one ({ext(WS_CODE_URL, 'Code §20-439(e)')}). A slate-pattern stamped driveway files for the same driveway construction permit a flat gray one would, triggered by the use of impervious material rather than by how it's finished.</p>"),
        ("Flatwoods subgrade matters more for a decorative slab than the pattern choice does",
         f"<p>Myakka fine sand, typical of Seminole County's flatwoods ground, became Florida's state soil in 1989 ({src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}). A stamped finish adds depth to how much base work pays off, since a slab that settles unevenly on soft, poorly compacted subgrade shows that movement more visibly in a patterned surface than it would in plain gray concrete, where a hairline settlement crack reads less noticeably against the uniform color.</p>"),
    ],
    "scenario": ("An ashlar-pattern pool patio extension, sized out",
                 f"<p>A homeowner is extending a cracked 340 sq ft side patio into an ashlar-slate stamped pour with two blended earth tones. Figured at {price('stamped-concrete')} per {per('stamped-concrete')}, the job runs somewhere around $4,080 on the plain end and climbs to roughly $5,440 once the second color pass and a border band are added. "
                 "Because it's still an impervious surface under Code §20-439 regardless of texture, Community Development reviews it through the same driveway-and-paving process a plain gray slab would use, so the decorative choice doesn't add a separate approval step.</p>"),
    "faqs": [
        faq("Is a stamped finish reviewed any differently than a plain pour under Winter Springs' code?",
            "No. Code §20-439 names concrete as an approved material without carving out a separate category for a decorative texture, so a stamped surface goes through the identical permit review a broom finish would."),
        faq("Why might a stamped pattern crack more visibly than plain concrete on Seminole County flatwoods ground?",
            "Uneven subgrade compaction on flatwoods soil can let a slab settle in spots, and that settlement tends to read more clearly in a textured, multi-color pattern than it would against a uniform gray surface, where the same movement is easier to miss."),
        faq("Does Tuscawilla's HOA treat a stamped driveway the way it treats paver driveways?",
            "The Country Club Village ACC exhibit that's been published specifically addresses driveway pavers as a product; a stamped concrete finish is a different material, so that community's residents check with the association rather than assume the paver clause carries over."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Winter Springs, FL",
    "meta": "Artificial turf installers in Winter Springs, FL: the state's 10-foot water-body setback near Lake Jesup, and the city's own “turf block” paver, October 2026.",
    "h1": "Artificial Turf for Winter Springs Yards",
    "lede": capsule(f"Artificial turf in Winter Springs runs {price('artificial-turf')} per {per('artificial-turf')} in the Florida market as of October 2026. "
                     "On a lot near Lake Jesup or Central Winds Park, state rule keeps synthetic grass at least 10 feet from the water unless a seawall sits in between, a different question from the city's own “turf block” driveway paver, which is a separate product entirely."),
    "sections": [
        ("Don't confuse the city's “turf block” with the lawn product installed here",
         f"<p>Winter Springs' own driveway code lists “turf block” among the materials approved for a residential driveway or designated parking area ({ext(WS_CODE_URL, 'Code §20-439(e)')}), but that's an open-cell concrete paver meant to be planted with grass through its gaps, not the synthetic lawn turf covered on this page. {svc('artificial-turf', 'Artificial turf')} for a backyard or pet area falls under Florida's statewide turf rule instead, not the driveway materials list.</p>"),
        ("Rule 62-308.100 draws the line at 10 feet from open water",
         f"<p>A homeowner backing up to Central Winds Park or any part of the Lake Jesup shoreline works under Florida's statewide synthetic-turf standard, Rule 62-308.100, which took effect May 19, 2026 ({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). The short version for a lot like that: turf stops 10 feet short of the water unless a seawall stands between the panel and the shoreline, the subgrade underneath has to be washed stone rather than unwashed fill, the infill has to be a natural material, and no sprinkler line gets buried under the finished lawn. Florida Statutes §125.572, passed in 2025, keeps Winter Springs from writing a tighter local version of that standard without state authority to do so ({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Converting a bare strip along the back fence line",
                 f"<p>A rear yard that backs onto a retention pond has struggled to hold St. Augustine for years, and the owner is ready to swap 420 sq ft of thin, bare grass for turf, with the pond's edge sitting roughly 18 feet from where the lawn ends. At {price('artificial-turf')} per {per('artificial-turf')}, that build runs around $4,200 to $7,560 depending on pile height and backing. "
                 "Eighteen feet already clears Rule 62-308.100's 10-foot minimum with room to spare, so the layout doesn't need to pull back any further; a yard where the pond sits closer than 10 feet would need the panel edge moved back or a seawall confirmed first.</p>"),
    "faqs": [
        faq("Does the city's “turf block” driveway material count as artificial turf under the state rule?",
            "No. Turf block is a concrete grid paver meant to be planted with live grass through its openings; it's listed as a driveway surface in Code §20-439(e), separate from the synthetic lawn turf Rule 62-308.100 governs."),
        faq("What's the closest artificial turf can sit to a retention pond or Lake Jesup itself?",
            "10 feet, under the state's May 2026 synthetic-turf rule, unless a seawall or comparable barrier already separates the panel from the water."),
        faq("Can Winter Springs require a wider turf setback than the state's 10-foot minimum?",
            "Only within limits. A 2025 state law restricts how far a local government can tighten its own turf standard past the floor the state rule already sets."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
