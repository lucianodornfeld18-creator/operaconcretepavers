# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "altamonte-springs"

AS_DRIVEWAY_PERMIT_URL = "https://www.altamonte.org/DocumentCenter/View/27/Driveway-Construction-Permit-Application"
AS_BUILDING_CHECKLIST_URL = "https://www.altamonte.org/DocumentCenter/View/23/Building-Permit-Application-and-Checklist"
AS_ZONING_URL = "https://www.zoneomics.com/code/altamonte-springs-FL/chapter_7"
AS_FLU_URL = "https://www.altamonte.org/DocumentCenter/View/65/Section-II---Chapter-1-Future-Land-Use-Element-DIA"
AS_APRICOT_URL = "https://www.altamonte.org/953/Project-APRICOT"
AS_WIKI_URL = "https://en.wikipedia.org/wiki/Altamonte_Springs,_Florida"
CENSUS_REPORTER_AS = "https://censusreporter.org/profiles/16000US1200950-altamonte-springs-fl/"

SRC = [
    "census-pep-v2025", "sjrwmd-watering", "fl-dos-state-soil", "dep-rule", "fs125572",
    ("City of Altamonte Springs, Driveway Construction Permit Application (rev. 3/1/2024)", AS_DRIVEWAY_PERMIT_URL),
    ("City of Altamonte Springs, Building Permit Application and Checklist (rev. 3/1/2024)", AS_BUILDING_CHECKLIST_URL),
    ("City of Altamonte Springs Land Development Code §3.7.8, R-1 Lot Coverage (via Zoneomics)", AS_ZONING_URL),
    ("City of Altamonte Springs, Future Land Use Element, Data Inventory and Analysis, City Plan 2030", AS_FLU_URL),
    ("City of Altamonte Springs, Project APRICOT", AS_APRICOT_URL),
    ("Wikipedia, Altamonte Springs, Florida", AS_WIKI_URL),
    ("Census Reporter, Altamonte Springs, FL (ACS 2024 5-yr, B25035)", CENSUS_REPORTER_AS),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Which office reviews a new driveway in Altamonte Springs?",
        f"<p>The Building and Fire Safety Department, answering at (407) 571-8433, handles it through a dedicated Driveway Construction Permit Application rather than folding it into the general building-permit form ({ext(AS_DRIVEWAY_PERMIT_URL, 'City of Altamonte Springs, Driveway Construction Permit Application')}). The form itself asks for a contract with the job's valuation, since the fee is based on that number, plus a survey showing the distance to the nearest driveway or intersection, the house's location relative to the street, and existing sidewalks, storm inlets and manholes in the right-of-way. A Notice of Commencement is required once the job passes $5,000.</p>"),
    sec("What does the driveway application actually spell out about construction?",
        f"<p>The form checks off a driveway's construction type against a short, specific list: “3000 Concrete,” “Asphalt Concrete,” or “Other,” along with the design, single, double or circular, and how it ties into the street, curb and gutter, straight curb, or an unimproved edge ({ext(AS_DRIVEWAY_PERMIT_URL, 'City of Altamonte Springs, Driveway Construction Permit Application')}). New construction needs a compaction test run between the existing street and the property line before anything is poured, and a replacement driveway built in asphalt needs its own base, depth, compaction and prepour inspections in that order. The permit itself expires 60 days after approval, and starting work without one doubles the fee.</p>"),
    sec("Does a patio or pool deck fall under a different form than the driveway?",
        f"<p>Yes. A patio, porch or pool deck goes through the city's general Building Permit Application rather than the driveway-specific form, and that checklist asks the site plan to show “Location and Size of Porches, Patios, Steps, Driveways, Sidewalks, etc.” along with lot coverage calculations for single-family and duplex lots ({ext(AS_BUILDING_CHECKLIST_URL, 'City of Altamonte Springs, Building Permit Application and Checklist')}). Any project that adds paved surface or changes how a lot drains also needs a drainage plan showing the existing and proposed patterns, and the checklist calls for a signed homeowner or condominium association approval letter before the city will process the application.</p>"),
    sec("How much of a lot can concrete, pavers and a house legally cover?",
        f"<p>The city's R-1 single-family district caps total lot coverage at 45 percent for a detached house, duplex or zero-lot-line home, rising to 55 percent for a townhouse, under Land Development Code §3.7.8 ({ext(AS_ZONING_URL, 'Altamonte Springs LDC §3.7.8')}). A {svc('paver-patios', 'patio')} or a wide {svc('paver-driveways', 'paver driveway')} eats into that ceiling the same way an addition to the house itself would, which is part of why the lot coverage worksheet shows up on the building-permit checklist well before the first inspection.</p>"),
    sec("Why do some Altamonte Springs addresses actually belong to the county instead?",
        f"<p>The city's own Future Land Use Element describes “enclaves,” pockets of unincorporated Seminole County “completely surrounded” by the city on all four sides, mostly built-out single-family subdivisions along the city's fringe ({ext(AS_FLU_URL, 'City of Altamonte Springs, Future Land Use Element DIA')}). A homeowner inside one of those pockets files a driveway or paver permit with the county's Development Review Division instead of the Building and Fire Safety Department, even though the mailing address reads Altamonte Springs the same as a property two streets over inside the city limits.</p>"),
    sec("What does the Little Wekiva River mean for grading on this side of Seminole County?",
        f"<p>Altamonte Springs has no coastal shoreline of its own, and most of the city sits above the 100-year flood plain on naturally sandy, well-drained soil the city's own plan calls “marginally undulating” ({ext(AS_FLU_URL, 'City of Altamonte Springs, Future Land Use Element DIA')}). The exception runs along the Little Wekiva River, where a handful of structures sit inside the 100-year flood plain though not its floodway, and erosion along the riverbanks has become serious enough that the St. Johns River Water Management District keeps a standing Little Wekiva River Flood Management Plan aimed at it. A {svc('retaining-walls', 'retaining wall')} or {svc('concrete-pool-decks', 'pool deck')} near that corridor gets its grading checked against that erosion history before anything is dug.</p>"),
    sec("What does a median 1983 build year and Project APRICOT add up to for a yard here?",
        f"<p>Census Bureau estimates put the city's population at 48,000 as of July 1, 2025 ({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}), and most of that growth traces to the 1970s and 1980s, when Altamonte Springs turned from a small suburban town into a commercial hub anchored by Interstate 4 ({ext(AS_FLU_URL, 'City of Altamonte Springs, Future Land Use Element DIA')}). The typical home dates to 1983 (Census Reporter, ACS 2024 5-yr, {ext(CENSUS_REPORTER_AS, 'B25035')}), the same decade the city built out Project APRICOT, a reclaimed-water irrigation system that now reaches more than 99 percent of its residential, commercial and public properties ({ext(AS_APRICOT_URL, 'City of Altamonte Springs, Project APRICOT')}). A yard that age is old enough that an original driveway or pool deck is a common resurfacing candidate, and it's also old enough to likely already run on reclaimed water for its sprinklers rather than the drinking-water system.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Altamonte Springs use the same form for a driveway and a patio?",
        "No. Driveways go through a dedicated Driveway Construction Permit Application with its own survey and inspection requirements; patios, porches and pool decks go through the general Building Permit Application instead."),
    faq("What happens if construction starts in Altamonte Springs before the driveway permit is approved?",
        "The permit fee doubles, according to the application itself, and failing to build the driveway after a permit is issued forfeits the fee entirely."),
    faq("Does a paver patio count against my lot coverage limit in Altamonte Springs?",
        "Yes. The R-1 district's lot coverage cap, 45 percent for most single-family homes, factors into the same application that reviews a patio or driveway addition, which is why the checklist asks for lot coverage calculations up front."),
    faq("How do I know if my Altamonte Springs address is actually in unincorporated Seminole County?",
        "Check for one of the enclaves the city's own planning documents describe, pockets of county land completely surrounded by the city; a driveway or paver permit there goes to the county's Development Review Division instead of Building and Fire Safety."),
    faq("What's worth confirming before hiring a concrete or paver contractor in Altamonte Springs?",
        f"Verify the license through the state's lookup tool, and make sure the estimate already separates the driveway-specific permit from the general building permit a patio or pool deck would need, since the city doesn't treat them as the same application. {post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} covers what else belongs in a solid, best-practice estimate."),
]

HUB = page("/altamonte-springs-fl/", "city", "Concrete, Pavers & Turf Contractor in Altamonte Springs, FL",
           "Opera pours concrete, sets pavers and installs turf in Altamonte Springs, FL, where driveways and patios use two separate city permit forms, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Altamonte Springs Homes",
           capsule(f"Opera builds concrete driveways, pavers and artificial turf for homeowners in Altamonte Springs, a Seminole County city of about 48,000 residents where driveways and patios are reviewed on two separate city permit forms. "
                   f"As of October 2026, a new concrete driveway runs {price('concrete-driveway')} per {per('concrete-driveway')}, and the city's own application requires a compaction test before a new driveway is poured."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Altamonte Springs",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Driveway and patio permits in Seminole County"),
                    ("/winter-springs-fl/", "Concrete, pavers and turf in Winter Springs"),
                    ("/sanford-fl/", "Concrete, pavers and turf in Sanford"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Altamonte Springs, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Altamonte Springs, FL",
    "meta": "Concrete driveway contractors in Altamonte Springs, FL: the city's compaction test, inspection order and 60-day permit window, October 2026.",
    "h1": "Pouring a Concrete Driveway in Altamonte Springs",
    "lede": capsule(f"A new or replacement concrete driveway in Altamonte Springs runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "The city's own Driveway Construction Permit Application checks the job as “3000 Concrete” construction and requires a compaction test between the street and the property line before any new driveway gets poured."),
    "sections": [
        ("The permit form tracks the build step by step, not just the paperwork",
         f"<p>Altamonte Springs' Driveway Construction Permit Application, revised March 2024, has the applicant check a construction-type box, “3000 Concrete,” “Asphalt Concrete,” or “Other,” and a design, single, double or circular ({ext(AS_DRIVEWAY_PERMIT_URL, 'City of Altamonte Springs, Driveway Construction Permit Application')}). New driveway construction requires a compaction test run between the existing street and the property line before concrete goes down, a step the form calls out directly rather than leaving to a general inspection. The permit expires 60 days after approval, and the fee doubles if construction starts before that approval comes through.</p>"),
        ("Documentation leans on a survey more than a floor plan",
         f"<p>Instead of asking for architectural drawings, the application wants a property survey marking the distance to the nearest driveway or intersection, the house's position relative to the street, and existing sidewalks, storm inlets and manholes already sitting in the right-of-way ({ext(AS_DRIVEWAY_PERMIT_URL, 'City of Altamonte Springs, Driveway Construction Permit Application')}). The fee itself is based on the contract's stated valuation, so the signed contract has to accompany the application rather than follow later, and a Notice of Commencement is required once that value passes $5,000.</p>"),
    ],
    "scenario": ("A double-wide driveway replacement, worked out against the survey requirement",
                 f"<p>Picture a double-design driveway replacement, 22 by 26 ft, 572 sq ft, tying into the street with an existing concrete curb and gutter. At {price('concrete-driveway')} per {per('concrete-driveway')}, that job runs roughly $3,432 to $8,580 before demolition of the old slab is added. "
                 "Before the new concrete is placed, the compaction test between the street and the property line has to pass, and the survey submitted with the application has to show the measured distance to the neighbor's driveway, since the form asks for that figure directly rather than leaving it to be checked later.</p>"),
    "faqs": [
        faq("Does a replacement concrete driveway need a compaction test in Altamonte Springs?",
            "New driveway construction does, run between the existing street and the property line before concrete is placed. A replacement driveway built in asphalt instead needs base, depth, compaction and prepour inspections."),
        faq("How long does an Altamonte Springs driveway permit stay valid?",
            "60 days from the approval date; the fee doubles if construction starts before the permit is approved."),
        faq("What survey details does the city's driveway application require?",
            "Distance to the nearest driveway or intersection, the house's location relative to the street paving, existing sidewalks, storm inlets and manholes in the right-of-way, the lot lines, and lot coverage calculations."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Altamonte Springs, FL",
    "meta": "Paver driveway installers in Altamonte Springs, FL: lot coverage limits under LDC §3.7.8, and the county enclaves that skip the city permit, October 2026.",
    "h1": "Paver Driveways in Altamonte Springs",
    "lede": capsule(f"Expect {price('paver-driveway')} per {per('paver-driveway')} for a paver driveway in Altamonte Springs as of October 2026. "
                     "A wide paver driveway pushes against the city's 45 percent lot coverage cap faster than a narrower concrete one does, and a property sitting inside one of the city's unincorporated enclaves files with the county instead."),
    "sections": [
        ("Pavers count toward the same lot coverage ceiling as the house itself",
         f"<p>Altamonte Springs' R-1 single-family district caps lot coverage at 45 percent for a detached house, duplex or zero-lot-line home under Land Development Code §3.7.8 ({ext(AS_ZONING_URL, 'Altamonte Springs LDC §3.7.8')}). Because a paver driveway typically runs wider than a poured-concrete one to accommodate a circular or double design, it's worth running the lot coverage math before ordering material, especially on a smaller R-1AAA or R-1AA lot where the percentage ceiling drops rather than rises.</p>"),
        ("An enclave address files with the county, not the city",
         f"<p>The city's own land-use planning document describes “enclaves,” islands of unincorporated Seminole County “completely surrounded” by Altamonte Springs on every side, mostly built-out single-family subdivisions along the city's perimeter ({ext(AS_FLU_URL, 'City of Altamonte Springs, Future Land Use Element DIA')}). A paver driveway on one of those lots goes through the county's own Development Review Division rather than the city's Driveway Construction Permit Application, even with an Altamonte Springs mailing address.</p>"),
    ],
    "scenario": ("Checking a circular paver driveway against the lot coverage cap",
                 f"<p>Say a 9,000 sq ft R-1 lot already carries a 2,400 sq ft house and wants a circular paver driveway adding 950 sq ft of new paved surface. At {price('paver-driveway')} per {per('paver-driveway')}, that comes to roughly $9,500 to $28,500 depending on the paver and base. "
                 "Added to the house, that driveway brings total lot coverage to about 37 percent, inside the R-1 district's 45 percent ceiling; a smaller lot carrying the same house and driveway size could run up against that cap and need the design trimmed before the permit clears.</p>"),
    "faqs": [
        faq("Does a paver driveway count differently than concrete toward lot coverage in Altamonte Springs?",
            "No, the Land Development Code's lot coverage cap applies to the paved surface generally; a wider paver driveway simply tends to add more square footage against that same percentage limit than a narrower concrete one would."),
        faq("How do I know if a property is inside one of the city's unincorporated enclaves?",
            "The city's planning documents describe these as pockets of Seminole County completely surrounded by city limits; confirming the parcel with the county property appraiser or the Building and Fire Safety Department settles which permit desk applies."),
        faq("What's the lot coverage cap for a detached home in Altamonte Springs' R-1 district?",
            "45 percent, under Land Development Code §3.7.8, rising to 55 percent for a townhouse unit."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Altamonte Springs, FL",
    "meta": "Concrete patio contractors in Altamonte Springs, FL: the building-permit checklist's drainage plan and HOA letter requirement, October 2026.",
    "h1": "Building a Concrete Patio in Altamonte Springs",
    "lede": capsule(f"A concrete patio in Altamonte Springs falls between {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "Unlike a driveway, a patio goes through the city's general Building Permit Application, which asks for a drainage plan on any job that adds impervious area and, in a deed-restricted neighborhood, a signed HOA approval letter."),
    "sections": [
        ("A patio triggers the general checklist, not the driveway form",
         f"<p>The Building Permit Application Checklist lists “Location and Size of Porches, Patios, Steps, Driveways, Sidewalks, etc.” as a required item on the site plan, alongside lot coverage calculations for single-family and duplex properties ({ext(AS_BUILDING_CHECKLIST_URL, 'City of Altamonte Springs, Building Permit Application and Checklist')}). That's a different track from the driveway-specific form covered on {cs('altamonte-springs', 'concrete-driveways', 'the concrete driveway page for this city')}, even though both ultimately run through the same Building and Fire Safety Department.</p>"),
        ("Adding paved surface pulls in a drainage plan and an association letter",
         f"<p>“For all projects involving the addition of impervious area or affecting lot drainage,” the checklist requires a drainage plan showing existing and proposed drainage patterns along with the proposed finished floor elevation ({ext(AS_BUILDING_CHECKLIST_URL, 'City of Altamonte Springs, Building Permit Application and Checklist')}). The same checklist also calls for a Homeowner Association or Condominium Association approval letter before the city processes the permit, which matters on any lot inside a deed-restricted subdivision.</p>"),
    ],
    "scenario": ("A side-yard patio addition, checked against the drainage-plan trigger",
                 f"<p>A homeowner is pouring a 260 sq ft patio along the side of the house, in a neighborhood governed by an HOA, where the yard currently sheets water toward the back fence line. Pricing that at {price('concrete-patio')} per {per('concrete-patio')} runs roughly $1,560 to $3,380 before any decorative finish is added. "
                 "Because the new slab adds impervious area, a drainage plan showing the existing and proposed flow accompanies the building permit application, and the signed HOA approval letter has to be on file before the city will move the application forward.</p>"),
    "faqs": [
        faq("Does a concrete patio in Altamonte Springs need a drainage plan?",
            "Yes, if the project adds impervious area or affects how the lot drains, the building-permit checklist requires a plan showing both the existing and proposed drainage patterns."),
        faq("Does Altamonte Springs require HOA sign-off before approving a patio permit?",
            "The building-permit checklist lists a Homeowner Association or Condominium Association approval letter as a required item, which applies on a lot inside a deed-restricted community."),
        faq("Is a patio reviewed under the same form as a driveway in Altamonte Springs?",
            "No. A patio goes through the general Building Permit Application; a driveway uses its own dedicated Driveway Construction Permit Application."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Altamonte Springs, FL",
    "meta": "Paver patio installers in Altamonte Springs, FL on sandy ridge soil near the Little Wekiva River floodway, October 2026.",
    "h1": "Paver Patios and Walkways for Altamonte Springs Yards",
    "lede": capsule(f"A paver patio in Altamonte Springs runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "Most of the city sits on sandy, well-drained ridge soil above the 100-year flood plain, with the main exception running along the Little Wekiva River, where erosion has become serious enough for a standing state flood management plan."),
    "sections": [
        ("Ridge soil drains fast almost everywhere except the river corridor",
         f"<p>The city's own land-use plan describes its natural ground as sandy and well drained, with “marginally undulating” topography left over from a landscape once covered in citrus groves ({ext(AS_FLU_URL, 'City of Altamonte Springs, Future Land Use Element DIA')}). That drains faster than the flatwoods soil common elsewhere in Seminole County, which is good news for a {svc('paver-patios', 'paver patio')}'s base, though a lot backing onto the Little Wekiva River corridor is a different story, since the riverbanks there have seen erosion serious enough that SJRWMD maintains a dedicated Little Wekiva River Flood Management Plan.</p>"),
        ("The patio permit still runs through the drainage-plan checklist",
         f"<p>A paver patio falls under the same Building Permit Application Checklist a concrete one does, with a drainage plan required whenever the project adds impervious area ({ext(AS_BUILDING_CHECKLIST_URL, 'City of Altamonte Springs, Building Permit Application and Checklist')}). On a lot near the Little Wekiva, that drainage plan carries more weight than it would farther from the river, since it has to account for how the new paved area interacts with ground that's already prone to erosion nearby.</p>"),
    ],
    "scenario": ("A paver patio set back from the Little Wekiva River corridor",
                 f"<p>A home backing onto a greenbelt along the Little Wekiva adds a 240 sq ft paver patio well clear of the riverbank itself, on sandy soil that drains quickly after rain. Figured at {price('paver-patio')} per {per('paver-patio')}, the job runs about $2,880 to $3,840 depending on the paver pattern. "
                 "Because the lot sits near, but not inside, the areas the city flags for flood-plain structures, the drainage plan submitted with the permit focuses mainly on keeping new runoff from adding to the erosion already documented along that stretch of riverbank.</p>"),
    "faqs": [
        faq("Does Altamonte Springs' soil drain well for a paver patio base?",
            "Generally, yes. The city's own planning documents describe its natural soil as sandy and well drained outside the Little Wekiva River corridor, which is better-draining ground than the flatwoods soil common across much of the rest of Seminole County."),
        faq("Is there a flood plan specific to the Little Wekiva River in Altamonte Springs?",
            "Yes. The St. Johns River Water Management District maintains a Little Wekiva River Flood Management Plan addressing erosion along the riverbanks, which the city coordinates with on nearby projects."),
        faq("Does a paver patio near the Little Wekiva need extra permitting?",
            "Not a separate permit, but the drainage plan required for any project adding impervious area gets more scrutiny on a lot near documented erosion than it would on one farther from the river."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Altamonte Springs, FL",
    "meta": "Concrete pool deck builders in Altamonte Springs, FL: decks from the city's 1983 median build year and the 1970s-80s growth era, October 2026.",
    "h1": "Concrete Pool Decks for Altamonte Springs Homes",
    "lede": capsule(f"Pricing a concrete pool deck in Altamonte Springs lands in the {price('concrete-pool-deck')} per {per('concrete-pool-deck')} range as of October 2026. "
                     "With the city's typical home dating to 1983, a meaningful share of original pool decks have logged more than four decades of Central Florida sun."),
    "sections": [
        ("The city's building boom lines up with a lot of aging pool decks today",
         f"<p>Census Reporter's ACS 2024 5-yr estimate puts Altamonte Springs' median year structure built at 1983 ({ext(CENSUS_REPORTER_AS, 'Census Reporter, Altamonte Springs FL')}), squarely inside the 1970s and 1980s stretch when the city's own planning documents describe it growing rapidly from a small suburban town into a commercial center built around Interstate 4 ({ext(AS_FLU_URL, 'City of Altamonte Springs, Future Land Use Element DIA')}). A deck poured during that building wave has had more than 40 years of heat cycling, long enough that a chalky cool-deck coating or a network of hairline cracks near the coping is ordinary wear rather than a surprise.</p>"),
        ("A pool deck replacement still routes through the drainage-plan checklist",
         f"<p>Whether it's a first installation or a resurfacing job, a pool deck project falls under the city's general Building Permit Application, with its site plan requirement for “Location and Size of Porches, Patios, Steps, Driveways, Sidewalks, etc.” and a drainage plan once the project adds or changes impervious area ({ext(AS_BUILDING_CHECKLIST_URL, 'City of Altamonte Springs, Building Permit Application and Checklist')}).</p>"),
    ],
    "scenario": ("Resurfacing a deck original to the city's 1980s building boom",
                 f"<p>Take a 520 sq ft deck wrapped around an in-ground pool, original to an early-1980s build, now showing a pitted, discolored cool-deck surface. Quoted for resurfacing, that job falls between roughly $2,600 and $6,240 at {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, cheaper for a plain broom finish and pricier once a decorative overlay is specified. "
                 "Since the job changes the deck's surface rather than its footprint, the drainage plan mainly confirms that the resurfaced area still sheds water the way the original slab did, rather than requiring a new grading layout from scratch.</p>"),
    "faqs": [
        faq("Why are so many Altamonte Springs pool decks showing their age around the same time?",
            "The city's median home dates to 1983, right in the middle of the 1970s-80s building boom that turned Altamonte Springs into a commercial hub; a large share of original pool decks are now past four decades old."),
        faq("Does resurfacing an existing pool deck need the same permit as a new one in Altamonte Springs?",
            "Yes, both fall under the general Building Permit Application, with a drainage plan required once the project adds or changes impervious area."),
        faq("Should an original 1980s Altamonte Springs pool deck be resurfaced or torn out?",
            "Often resurfaced, if the cracking stays in the surface coating rather than reaching into the slab; a crack that runs deep enough to show through a new overlay points toward a full tear-out instead."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Altamonte Springs, FL",
    "meta": "Pool deck paver overlays and new builds in Altamonte Springs, FL, near Lake Orienta, where Project APRICOT runs reclaimed water citywide, October 2026.",
    "h1": "Pool Deck Pavers in Altamonte Springs",
    "lede": capsule(f"Pool deck pavers in Altamonte Springs run {price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026, whether they're set new or layered over an aging slab. "
                     "A city built out around Lake Orienta's shoreline more than a century ago now irrigates almost every yard with reclaimed water through Project APRICOT, a detail worth knowing before new pavers go in near the pool equipment pad."),
    "sections": [
        ("Lake Orienta anchored the city's earliest resort development",
         f"<p>A freshwater beach sits on Lake Orienta's southwest shore inside a city park today, but the lake's history goes back to 1883, when the Altamonte Land, Hotel and Navigation Company built the Altamonte Hotel on its shore as a winter resort ({ext(AS_WIKI_URL, 'Wikipedia, Altamonte Springs, Florida')}; {ext(AS_FLU_URL, 'City of Altamonte Springs, Future Land Use Element DIA')}). Many of the homes closest to that original lakefront core are old enough that their pool decks are candidates for an overlay rather than a first installation.</p>"),
        ("Project APRICOT changes what's running under the yard, not just the lawn",
         f"<p>Implemented in the 1980s, Project APRICOT now delivers reclaimed water to more than 99 percent of the city's residential, commercial and public properties for irrigation ({ext(AS_APRICOT_URL, 'City of Altamonte Springs, Project APRICOT')}). That reclaimed line is a separate system from the drinking-water service, so a pool deck paver project that disturbs ground near existing irrigation has a second utility line to locate and protect, on top of whatever runs to the pool equipment itself.</p>"),
    ],
    "scenario": ("An overlay near a pool pad already tied into reclaimed water",
                 f"<p>A home a few blocks from Lake Orienta has a 460 sq ft pool deck with a worn cool-deck finish, and reclaimed water already feeds the irrigation along one side of the equipment pad. Overlay pricing at {price('pool-deck-pavers')} per {per('pool-deck-pavers')} runs roughly $6,440 for a standard concrete paver and closer to $13,500 for travertine. "
                 "Before the overlay goes down, the crew locates that reclaimed line the way it would any other utility, since Project APRICOT's distribution network reaches the large majority of properties in this part of the city.</p>"),
    "faqs": [
        faq("Does Altamonte Springs' reclaimed water system affect a pool deck paver project?",
            "It can, mainly in locating the reclaimed irrigation line before digging near the pool equipment pad, since Project APRICOT reaches more than 99 percent of the city's properties."),
        faq("Are pool decks near Lake Orienta more likely to need an overlay?",
            "Often, since many of the homes closest to the original lakefront development date back further than homes in newer parts of the city, putting their pool decks further along in wear."),
        faq("What permit covers pool deck pavers in Altamonte Springs?",
            "The general Building Permit Application, the same one used for a concrete pool deck, with a drainage plan required once the project adds impervious area."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Altamonte Springs, FL",
    "meta": "Stamped concrete contractors in Altamonte Springs, FL: how a decorative finish is checked against the city's 45 percent lot coverage cap, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Altamonte Springs",
    "lede": capsule(f"Stamped concrete work in Altamonte Springs falls between {price('stamped-concrete')} per {per('stamped-concrete')} as of October 2026, swinging with the pattern and number of colors. "
                     "A decorative finish doesn't change which permit form applies or how much it counts against the city's lot coverage limit; a stamped slab is measured in square feet the same way a plain one would be."),
    "sections": [
        ("The driveway form checks construction type, not decorative finish",
         f"<p>Altamonte Springs' Driveway Construction Permit Application has the applicant check “3000 Concrete” as the construction type without a separate line for a stamped or stained surface ({ext(AS_DRIVEWAY_PERMIT_URL, 'City of Altamonte Springs, Driveway Construction Permit Application')}). A slate-pattern stamped driveway apron goes through the identical compaction-test-and-inspection sequence a plain gray pour would, and a stamped patio instead falls under the general building-permit checklist the same way an unadorned one does.</p>"),
        ("Square footage, not finish, drives the lot coverage math",
         f"<p>The R-1 district's 45 percent lot coverage cap under Land Development Code §3.7.8 counts a stamped patio or driveway exactly the way it counts a plain pour, by square footage rather than appearance ({ext(AS_ZONING_URL, 'Altamonte Springs LDC §3.7.8')}). A homeowner adding a decorative stamped walkway on a lot already close to that ceiling runs the same coverage calculation a plain-concrete version of the same footprint would need.</p>"),
    ],
    "scenario": ("Pricing a multi-color ashlar pattern against a plain pour",
                 f"<p>A homeowner is comparing a plain 300 sq ft driveway apron against an ashlar-pattern stamped version with two blended colors. At {price('stamped-concrete')} per {per('stamped-concrete')}, the stamped option runs roughly $3,600 to $4,800, against perhaps half that for a basic broom finish at concrete pricing. "
                 "Neither choice changes which box gets checked on the driveway application or how the square footage counts toward the lot's 45 percent coverage ceiling; the decision comes down to budget and appearance rather than paperwork.</p>"),
    "faqs": [
        faq("Does a stamped driveway need a different inspection sequence than plain concrete in Altamonte Springs?",
            "No. The city's driveway application checks construction type as concrete, asphalt or other, without a separate category for a decorative finish, so the same compaction test and inspections apply."),
        faq("Does a stamped patio count more heavily toward lot coverage than a plain one?",
            "No. The R-1 district's coverage cap is measured in square footage, so a stamped and a plain-finish patio of the same size count identically toward the 45 percent limit."),
        faq("Is a stamped pool deck resurfacing treated differently from a plain resurfacing job?",
            "Both route through the same Building Permit Application Checklist; the finish choice doesn't change which form applies, only the cost per square foot."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Altamonte Springs, FL",
    "meta": "Artificial turf installers in Altamonte Springs, FL: why Project APRICOT's reclaimed lines matter under the state's no-irrigation-under-turf rule, October 2026.",
    "h1": "Artificial Turf for Altamonte Springs Yards",
    "lede": capsule(f"Turf installed for an Altamonte Springs yard costs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "Because Project APRICOT already irrigates more than 99 percent of the city's properties with reclaimed water, a turf conversion here almost always means capping an existing reclaimed line rather than simply skipping a sprinkler install the way it might in a city without that system."),
    "sections": [
        ("Most Altamonte Springs lawns already run on reclaimed water, not the drinking-water line",
         f"<p>Project APRICOT, the city's reclaimed-water system built out in the 1980s, reaches more than 99 percent of residential, commercial and public properties for lawn and landscape irrigation ({ext(AS_APRICOT_URL, 'City of Altamonte Springs, Project APRICOT')}). Florida's statewide synthetic-turf rule, effective May 19, 2026, bars running an in-ground irrigation line underneath the finished turf ({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}), so converting a section of lawn here typically means capping or rerouting an existing reclaimed-water zone rather than removing a drinking-water sprinkler line, a different starting point than a yard that was never irrigated through a reclaimed system at all.</p>"),
        ("The same rule sets a shoreline buffer near the Little Wekiva and city lakes",
         f"<p>Rule 62-308.100 pulls turf back from open water generally: a panel has to stop 10 feet short of a pond, lake or river edge unless a seawall or something like it already stands between the lawn and the water, and the subgrade underneath has to be washed stone carrying natural infill rather than unwashed fill ({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). On a lot near the Little Wekiva River corridor or Lake Orienta, that buffer is worth measuring against the actual bank rather than estimated from a plat map, and Florida Statutes §125.572 caps how much tighter a local ordinance can set that distance beyond what the state already requires ({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Capping a reclaimed zone before laying turf",
                 f"<p>A front yard that's fought chinch bugs for years gets 380 sq ft of St. Augustine replaced with turf, in a section already fed by one zone of the home's reclaimed-water irrigation. At {price('artificial-turf')} per {per('artificial-turf')}, that project runs roughly $3,800 to $6,840. "
                 "Before the base goes in, that reclaimed zone gets capped and redirected to the remaining sod rather than left running under the new turf, satisfying the state rule's ban on in-ground irrigation beneath the finished lawn.</p>"),
    "faqs": [
        faq("Does Project APRICOT's reclaimed water change how artificial turf gets installed in Altamonte Springs?",
            "It changes what has to be capped first. Since reclaimed water already irrigates more than 99 percent of the city's properties, a turf conversion usually means rerouting an existing reclaimed zone rather than removing a drinking-water line."),
        faq("How close to the Little Wekiva River can turf be installed?",
            "The state's May 2026 rule sets a 10-foot buffer from open water, closing only if a seawall or comparable structure already sits between the panel and the river."),
        faq("Can irrigation keep running under a new turf lawn in Altamonte Springs?",
            "No. The state rule bars an in-ground irrigation line under finished turf regardless of whether that line carries reclaimed or potable water."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
