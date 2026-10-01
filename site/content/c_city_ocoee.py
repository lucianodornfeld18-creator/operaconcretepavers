# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "ocoee"

BLDGFAQ_URL = "https://www.ocoee.org/FAQ.aspx?QID=181"
BLDGDIV_URL = "https://www.ocoee.org/163/Building-Division"
ROW_URL = "https://www.ocoee.org/230/Right-of-Way-Permitting"
DOWNTOWN_URL = "https://www.ocoee.org/1099/Downtown"
FACTS_URL = "https://www.ocoee.org/951/Facts-Figures"
ACS_URL = "https://censusreporter.org/profiles/16000US1251075-ocoee-fl/"
HISTDIST_URL = "https://en.wikipedia.org/wiki/Ocoee_Street_Historic_District"
WITHERS_URL = "https://en.wikipedia.org/wiki/Withers-Maguire_House"

SRC = [
    "census-pep-v2025", "sjrwmd-watering", "fl-senate-2011-104", "dep-rule", "fs125572", "orange-res-plan-guide",
    "nrcs-candler-osd", "nrcs-tavares-osd", "nrcs-astatula-osd", "nrcs-myakka-osd", "nrcs-smyrna-osd",
    ("City of Ocoee, Building FAQ: concrete slab, patio, driveway and paver permits", BLDGFAQ_URL),
    ("City of Ocoee, Building Division", BLDGDIV_URL),
    ("City of Ocoee, Right-of-Way Permitting", ROW_URL),
    ("City of Ocoee, Downtown", DOWNTOWN_URL),
    ("City of Ocoee, Facts & Figures", FACTS_URL),
    ("Census Reporter, Ocoee FL (ACS 2020-2024 5-yr, B25035/B01003)", ACS_URL),
    ("Wikipedia, Ocoee Street Historic District", HISTDIST_URL),
    ("Wikipedia, Withers-Maguire House", WITHERS_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Does Ocoee require a permit for a concrete slab, patio, driveway or pavers?",
        f"<p>Yes, every time. The city's own building FAQ answers the question directly: \"Yes, a site plan will be required with a description of what is being done,\" adding that \"depending on the scope of work, additional structural detail may also be required\" "
        f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')}). The Building Division reviews that application from 1 North Bluford Avenue, 407-905-3104, bldgdept@ocoee.org, Monday through Thursday 7:30 a.m. to 5:30 p.m. and Friday 8 a.m. to 5 p.m., with applications filed through permits.ocoee.org "
        f"({ext(BLDGDIV_URL, 'City of Ocoee, Building Division')}). A new concrete driveway here runs {price('concrete-driveway')} per {per('concrete-driveway')}, the Florida market figure tracked this October 2026.</p>"),
    sec("What counts as right-of-way work, and who handles it?",
        f"<p>Ocoee draws a wide circle around what needs a right-of-way permit: the city requires one for \"excavation, construction, installation, or maintenance of any public or private utility, roadway, street or any other facility, structure, driveway, culvert, drainage system, pavement, easement or object\" in a city street, right-of-way or easement "
        f"({ext(ROW_URL, 'City of Ocoee, Right-of-Way Permitting')}). Driveways and pavement are named outright in that list, so a driveway apron or a widened curb cut routes through this review in addition to the Building Division's own site-plan approval. Public Works, 407-905-3170, fields questions on the right-of-way process, and applications go through the same permits.ocoee.org portal the Building Division uses "
        f"({ext(ROW_URL, 'City of Ocoee, Right-of-Way Permitting')}).</p>"),
    sec("How fast has Ocoee grown, and how old is the typical house?",
        f"<p>The Census Bureau's latest population estimate puts Ocoee at 51,932 residents on July 1, 2025, up from a 2020 base of 47,348, close to 10 percent growth in five years "
        f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}). The Census Reporter profile for the city puts the median year a home here was built at 2000 "
        f"({ext(ACS_URL, 'Census Reporter, Ocoee FL')}), and the city's own Facts & Figures page traces that growth back further still, from 26,546 residents at the 2000 Census to 35,579 by 2010 "
        f"({ext(FACTS_URL, 'City of Ocoee, Facts & Figures')}). A driveway or patio original to a 2000-era home is now old enough that a repair or resurfacing call isn't unusual, while newer construction along the SR 50 corridor is still pouring first slabs.</p>"),
    sec("What's happening around Starke Lake and the historic downtown right now?",
        f"<p>Ocoee's own downtown page states that the city recently completed \"more than $44 million of capital projects to enhance public spaces and key infrastructure in Downtown Ocoee,\" work that \"created or expanded public spaces along the western shore of beautiful Starke Lake\" and included \"a stormwater facility which serves several blocks\" "
        f"({ext(DOWNTOWN_URL, 'City of Ocoee, Downtown')}). Bill Breeze Park and the grounds of the historic Withers-Maguire House, an 1888 house on the National Register of Historic Places since April 2, 1987, both sit inside that improved area "
        f"({ext(DOWNTOWN_URL, 'City of Ocoee, Downtown')}; {ext(WITHERS_URL, 'Wikipedia, Withers-Maguire House')}). A few blocks away, the Ocoee Street Historic District, listed on the National Register December 13, 1995, carries 40 contributing homes built mostly before 1900 on 16 acres "
        f"({ext(HISTDIST_URL, 'Wikipedia, Ocoee Street Historic District')}).</p>"),
    sec("What does the SR 50 corridor's growth mean for a newer Ocoee home?",
        f"<p>The city's own figures describe West Oaks Mall, 1.1 million square feet, and Orlando Health Central Hospital as the anchors of what it calls the \"Fifty West Business Corridor\" along State Road 50 "
        f"({ext(FACTS_URL, 'City of Ocoee, Facts & Figures')}). Subdivisions that grew up around that corridor over the past two decades sit on newer construction than the homes near the original downtown core, which changes the kind of project a crew typically sees in each part of the city, first installs of {svc('paver-driveways', 'driveways')} and {svc('concrete-pool-decks', 'pool decks')} near the corridor, repair and resurfacing work closer to Starke Lake's older blocks.</p>"),
    sec("What's under the ground on a typical Ocoee lot?",
        f"<p>West Orange County's soil splits between two very different conditions, often within the same subdivision: Candler and Tavares, both sandy and excessively to moderately well drained with the water table well below the surface, and Myakka and Smyrna, poorly drained flatwoods soils that hold water within 18 inches of grade for months of the year "
        f"({src('nrcs-candler-osd', 'NRCS Official Series Description, Candler')}; {src('nrcs-myakka-osd', 'NRCS Official Series Description, Myakka')}). That mix is part of why the city's own downtown capital program included a new stormwater facility rather than relying on the ground to carry rainfall on its own "
        f"({ext(DOWNTOWN_URL, 'City of Ocoee, Downtown')}), and it's a reason a {svc('concrete-slabs', 'slab')} or {svc('paver-patios', 'patio')} base gets checked against the actual soil on a given lot rather than a citywide assumption.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Ocoee require a site plan for a driveway or patio permit?",
        f"Yes. The city's building FAQ states that a site plan is required along with a description of the work, and that additional structural detail may be requested depending on the scope "
        f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')})."),
    faq("Is a driveway apron in Ocoee covered by the same permit as the rest of the slab?",
        f"Not necessarily. Driveways, culverts and pavement are named directly in the city's right-of-way permit scope, so the section crossing into the street or easement often needs that separate review in addition to the Building Division's site-plan approval "
        f"({ext(ROW_URL, 'City of Ocoee, Right-of-Way Permitting')})."),
    faq("What's the $44 million downtown project in Ocoee?",
        f"A set of capital improvements the city completed along Starke Lake's western shore, including expanded public space, a new stormwater facility serving several downtown blocks, and upgrades to Bill Breeze Park and the Withers-Maguire House grounds "
        f"({ext(DOWNTOWN_URL, 'City of Ocoee, Downtown')})."),
    faq("How old is a typical Ocoee home?",
        f"Census Reporter's estimate puts the median year of construction at 2000, though homes near the historic downtown core predate that by a century or more, while subdivisions along the SR 50 corridor skew newer "
        f"({ext(ACS_URL, 'Census Reporter, Ocoee FL')})."),
    faq("How do you pick the best concrete contractor near Ocoee?",
        f"Verify the contractor on the state's license-check tool, confirm the quote already accounts for the city's site-plan requirement and, if the work touches the street, a separate right-of-way application, and ask how demolition of an existing slab is priced. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} covers the rest."),
]

HUB = page("/ocoee-fl/", "city", "Concrete, Pavers & Turf Contractor in Ocoee, FL",
           "Opera builds concrete driveways, pavers and turf in Ocoee, FL, where a site plan is required for every slab, patio, driveway or paver job, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Ocoee, Florida Homes",
           capsule(f"Opera's crews pour concrete and set pavers and artificial turf for homes across Ocoee, an Orange County city of 51,932 residents as of mid-2025, about "
                   f"{str(__import__('_data').CITIES['ocoee']['miles'])} miles from Orlando. A new concrete driveway here runs {price('concrete-driveway')} per {per('concrete-driveway')} on the current October 2026 Florida market range, and the city's own building FAQ requires a site plan and work description on every slab, patio, driveway or paver application that comes through its door."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Ocoee",
           related=[("/central-florida/", "The Orlando-unit coverage area"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Driveway and patio permits in Orlando and Orange County"),
                    ("/winter-garden-fl/", "Concrete, pavers and turf in Winter Garden"),
                    ("/windermere-fl/", "Concrete, pavers and turf in Windermere"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Ocoee, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Ocoee, FL – Site Plan",
    "meta": "Concrete driveway installers in Ocoee, FL: the city's site-plan requirement and when a separate right-of-way permit applies, Oct. 2026.",
    "h1": "Pouring a Concrete Driveway in Ocoee",
    "lede": capsule(f"A new or replacement concrete driveway in Ocoee this October runs {price('concrete-driveway')} per {per('concrete-driveway')}, the current Florida market figure. "
                     "The city's building office asks for a site plan and a written description of the work on every driveway application, and the apron section meeting the street carries its own separate review."),
    "sections": [
        ("A site plan comes before the forms go up, every time",
         f"<p>Ocoee's building FAQ doesn't leave room for a shortcut: \"Yes, a site plan will be required with a description of what is being done,\" and the city notes that \"additional structural detail may also be required\" depending on the scope "
         f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')}). The Building Division, at 1 North Bluford Avenue, 407-905-3104, reviews that submittal for {svc('concrete-driveways', 'a driveway')} the same way it reviews a patio or slab application.</p>"),
        ("The apron at the street is a second, separate review",
         f"<p>Ocoee's right-of-way permit scope names \"driveway, culvert, drainage system, pavement\" directly among the work that needs that permit when it touches a city street, right-of-way or easement "
         f"({ext(ROW_URL, 'City of Ocoee, Right-of-Way Permitting')}). A driveway rebuilt inside its existing footprint on private ground typically needs only the Building Division's site-plan review; one that widens the curb cut or extends into the swale picks up the right-of-way application too, filed through Public Works at 407-905-3170.</p>"),
    ],
    "scenario": ("Replacing a two-car driveway near the right-of-way line, worked out in square feet",
                 f"<p>A 22 by 24 ft two-car driveway comes to 528 sq ft. At {price('concrete-driveway')} per {per('concrete-driveway')}, that pour runs roughly $3,168 to $7,920 before demolition of the old slab is added. "
                 "If 40 of those 528 sq ft sit in the apron crossing toward the street, that section needs the right-of-way permit on top of the Building Division's standard site-plan review, a second application worth building into the project timeline from the start rather than discovering partway through.</p>"),
    "faqs": [
        faq("Does a concrete driveway need a permit in Ocoee?",
            "Yes. The city's building FAQ confirms a permit, with a site plan and work description, applies to every driveway, patio, slab or paver job, and additional structural detail can be requested depending on scope."),
        faq("Does an Ocoee driveway apron need a separate permit from the rest of the slab?",
            "Often, yes. The right-of-way permit scope names driveways and pavement directly, so the section crossing the street or easement typically needs that review in addition to the Building Division's site-plan approval."),
        faq("Where is Ocoee's Building Division located?",
            "1 North Bluford Avenue, Ocoee, FL 34761, reachable at 407-905-3104 or bldgdept@ocoee.org, with applications filed online through permits.ocoee.org."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Ocoee, FL – SR 50 Growth",
    "meta": "Paver driveway installers in Ocoee, FL: the city's site-plan rule and new construction along the Fifty West corridor, Oct. 2026.",
    "h1": "Paver Driveways for Ocoee Homes",
    "lede": capsule(f"Figure {price('paver-driveway')} per {per('paver-driveway')} for a paver driveway in Ocoee heading into the final quarter of 2026. "
                     "With the city's typical home dating to 2000, paver work splits fairly evenly between first installs on newer construction near the SR 50 corridor and replacements on older driveways closer to downtown."),
    "sections": [
        ("Material doesn't change the paperwork",
         f"<p>Ocoee's building review doesn't treat pavers differently from poured concrete; the same site-plan-and-description requirement applies to \"concrete slab, patio, driveway, or pavers\" as one category "
         f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')}). A {svc('paver-driveways', 'paver driveway')} that widens toward the street still routes the apron section through the separate right-of-way application, the same as a poured one would "
         f"({ext(ROW_URL, 'City of Ocoee, Right-of-Way Permitting')}).</p>"),
        ("New rooftops near the SR 50 corridor mean more first installs",
         f"<p>The city's own figures point to West Oaks Mall and Orlando Health Central Hospital anchoring the \"Fifty West Business Corridor,\" the commercial spine that newer residential growth has followed over the past two decades "
         f"({ext(FACTS_URL, 'City of Ocoee, Facts & Figures')}). Subdivisions built up around that corridor skew newer than the city's 2000 median, which is why a paver crew working that side of Ocoee sees more fresh-fill lots than it does closer to the older blocks ringing Starke Lake.</p>"),
    ],
    "scenario": ("A paver driveway on newer fill near the business corridor, worked out in square feet",
                 f"<p>A 24 by 22 ft paver driveway on a recently built lot comes to 528 sq ft, and at {price('paver-driveway')} per {per('paver-driveway')}, that job runs roughly $5,280 to $15,840 depending on the paver style and base depth. "
                 "On ground graded within the last few years, a base crew typically spends extra time confirming compaction before setting bedding sand, since fill that hasn't been through a full rainy season yet can still settle unevenly under a vehicle load.</p>"),
    "faqs": [
        faq("Does a paver driveway in Ocoee need a different permit than a concrete one?",
            "No. The city's building FAQ groups slabs, patios, driveways and pavers together under the same site-plan-and-description requirement, so a paver driveway goes through the identical review."),
        faq("Is most new paver driveway work in Ocoee near the SR 50 corridor?",
            "A meaningful share is, since residential growth has followed the commercial development along State Road 50 over the past two decades, putting more new-construction lots in that part of the city than near the older downtown core."),
        faq("Does fresh fill on a new Ocoee lot change how a paver base is built?",
            "It can. A crew typically checks compaction more carefully on recently graded ground than on an older, already-settled lot, since fill that hasn't gone through a full wet season can still shift."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Ocoee, FL – Drainage",
    "meta": "Concrete patio contractors in Ocoee, FL: why downtown's new stormwater facility reflects the soil split across the city, Oct. 2026.",
    "h1": "Building a Concrete Patio in Ocoee",
    "lede": capsule(f"Budget {price('concrete-patio')} per {per('concrete-patio')} for a concrete patio in Ocoee, the Florida range current this October. "
                     "The soil under a given lot here can swing from fast-draining sand to a shallow water table within a short distance, which is part of why the city just built a stormwater facility to serve several downtown blocks."),
    "sections": [
        ("A patio slab still needs the city's standard site plan",
         f"<p>Ocoee's own FAQ doesn't carve out a lighter process for a backyard addition; a {svc('concrete-patios', 'patio')} falls under the same \"site plan will be required with a description of what is being done\" rule as a driveway or slab "
         f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')}). The Building Division's review checks that submittal the same way regardless of whether the patio is a first addition or a replacement of an older slab.</p>"),
        ("Two very different soils can sit within the same subdivision",
         f"<p>Candler and Tavares, the sandy ridge soils common across west Orange County, drain excessively with the water table well below the surface, while Myakka and Smyrna, both poorly drained flatwoods soils, can hold water within 18 inches of grade for months at a stretch "
         f"({src('nrcs-candler-osd', 'NRCS Official Series Description, Candler')}; {src('nrcs-myakka-osd', 'NRCS Official Series Description, Myakka')}). That split is part of why the city's own downtown capital program added a stormwater facility to serve several blocks rather than counting on the ground alone to carry runoff "
         f"({ext(DOWNTOWN_URL, 'City of Ocoee, Downtown')}), and it's a reason a patio's slope gets checked against the actual lot rather than a general rule for the neighborhood.</p>"),
    ],
    "scenario": ("A patio addition on a lot with mixed drainage, worked out in square feet",
                 f"<p>A 16 by 18 ft patio off the back of the house comes to 288 sq ft, and at {price('concrete-patio')} per {per('concrete-patio')}, that pour runs roughly $1,728 to $3,744 before a decorative finish changes the number. "
                 "On a lot where the back corner tests out wetter than the rest of the yard, the pitch of that 288 sq ft slab gets set to carry water toward whatever drainage path already exists on the property, rather than assuming the whole lot drains the same way front to back.</p>"),
    "faqs": [
        faq("Does a concrete patio need a site plan in Ocoee?",
            "Yes. The city's building FAQ applies the same site-plan-and-description requirement to a patio that it applies to a driveway, slab or paver installation."),
        faq("Why would the city build a stormwater facility downtown if the soil already drains?",
            "Because the soil doesn't drain uniformly. Fast-draining ridge sand and poorly drained flatwoods soil both occur across the area, and the downtown facility was built to serve several blocks that needed that extra capacity."),
        faq("Does a patio's slope need to account for soil variation in Ocoee?",
            "On a lot where part of the yard holds water longer than the rest, yes, the pitch gets set to the actual drainage path on that property rather than a general assumption carried over from the neighborhood."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Ocoee, FL – Starke Lake",
    "meta": "Paver patio installers in Ocoee, FL near the historic downtown and Starke Lake, where the city just finished $44 million in upgrades, Oct. 2026.",
    "h1": "Paver Patios and Walkways Near Historic Ocoee",
    "lede": capsule(f"A paver patio in Ocoee runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "Homes closest to Starke Lake and the historic downtown core sit on some of the city's oldest lots, a different starting point for a patio project than the newer subdivisions spreading out toward the edges of town."),
    "sections": [
        ("Downtown's recent upgrades reach right up to the water's edge",
         f"<p>Ocoee's own downtown page describes more than $44 million in recently finished capital projects that \"created or expanded public spaces along the western shore of beautiful Starke Lake,\" including new landscaping and event space around Bill Breeze Park and the Withers-Maguire House grounds "
         f"({ext(DOWNTOWN_URL, 'City of Ocoee, Downtown')}). A backyard {svc('paver-patios', 'paver patio')} a few blocks from that shoreline sits in a part of the city that's seen more public investment over the past decade than almost anywhere else in Ocoee.</p>"),
        ("The historic district nearby carries some of the city's oldest houses",
         f"<p>The Ocoee Street Historic District, listed on the National Register of Historic Places on December 13, 1995, covers 40 contributing homes and two contributing structures on 16 acres, most built before 1900 in Colonial Revival, Tudor Revival and Queen Anne styles "
         f"({ext(HISTDIST_URL, 'Wikipedia, Ocoee Street Historic District')}). A paver patio or walkway near that district often has to work around mature trees and an older house footprint that a newer subdivision lot simply doesn't have to account for.</p>"),
    ],
    "scenario": ("A paver walkway near the historic core, worked out in square feet",
                 f"<p>A 4 by 40 ft front walkway near the historic district, 160 sq ft, replacing a narrow original path, runs roughly $1,600 to $2,720 once the {price('paver-patio')} per {per('paver-patio')} range is applied. "
                 "On a lot that old, the crew often has to route the new base around established root systems and an existing foundation line, a planning step that barely comes up on a paver job a few miles out near the city's newer growth.</p>"),
    "faqs": [
        faq("Has Starke Lake's shoreline changed recently in Ocoee?",
            "Yes. The city completed more than $44 million in capital projects along the lake's western shore, expanding public space and adding infrastructure including a new stormwater facility serving nearby blocks."),
        faq("What is the Ocoee Street Historic District?",
            "A National Register district, listed December 13, 1995, covering 40 contributing homes and two structures on 16 acres, most built before 1900 in Colonial Revival, Tudor Revival and Queen Anne styles."),
        faq("Does a paver patio near Ocoee's historic downtown need extra planning?",
            "Often, since mature trees and older house footprints near that core take more care to work around than a newer subdivision lot does, even though the permit process itself is the same citywide."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Ocoee, FL – New Builds",
    "meta": "Concrete pool deck builders in Ocoee, FL: growth along the Fifty West corridor and the city's site-plan permit rule, Oct. 2026.",
    "h1": "Concrete Pool Decks for Ocoee Homes",
    "lede": capsule(f"A concrete pool deck in Ocoee falls between {price('concrete-pool-deck')} per {per('concrete-pool-deck')} under current October 2026 Florida pricing. "
                     "A meaningful share of new pool decks are going in around the newer subdivisions that have grown up along the SR 50 business corridor over the past two decades, rather than being poured as replacements near the older downtown core."),
    "sections": [
        ("New rooftops along the corridor bring new pools with them",
         f"<p>Ocoee's own description of the Fifty West Business Corridor names West Oaks Mall and Orlando Health Central Hospital as its anchors along State Road 50 "
         f"({ext(FACTS_URL, 'City of Ocoee, Facts & Figures')}), and the residential growth that followed that commercial spine put a lot of newer housing stock, pools included, along that stretch of the city. A {svc('concrete-pool-decks', 'pool deck')} poured there today is more often going in with a brand-new shell than resurfacing one that's been through two decades of Florida summers.</p>"),
        ("The city's site-plan rule applies the same way to a new deck or a redo",
         f"<p>Ocoee's building FAQ doesn't separate new construction from a later addition; a pool deck, like any other slab, needs \"a site plan... with a description of what is being done,\" with more structural detail possibly required depending on scope "
         f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')}). That review applies the same way whether the deck is going in with a freshly set pool shell or being poured around a pool that's been in the ground for years.</p>"),
    ],
    "scenario": ("A new pool deck on a corridor-area lot, worked out in square feet",
                 f"<p>A newly built home near the SR 50 corridor pouring a 520 sq ft deck around a just-set pool shell prices out between roughly $2,600 and $7,800 once the {price('concrete-pool-deck')} per {per('concrete-pool-deck')} range is applied, trending higher for a cool-touch decorative finish. "
                 "Because the deck and the pool shell are going in together, the pour schedule typically coordinates with the pool contractor's own timeline rather than fitting into a yard that's already landscaped.</p>"),
    "faqs": [
        faq("Are most new Ocoee pool decks near the SR 50 corridor or downtown?",
            "More often near the corridor, where residential growth has followed the Fifty West business development over the past two decades, putting a larger share of new pool construction in that part of the city."),
        faq("Does Ocoee's permit process differ for a new pool deck versus a replacement?",
            "No. Both go through the same site-plan-and-description requirement the city applies to any slab, with additional structural detail requested depending on the scope of the specific job."),
        faq("What's the price range for a concrete pool deck in Ocoee?",
            f"Figure {price('concrete-pool-deck')} per {per('concrete-pool-deck')} heading into the end of 2026, with a plain broom finish toward the lower end and a cool-touch decorative texture pushing it higher."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Ocoee, FL – Lakefront Lots",
    "meta": "Pool deck paver installers in Ocoee, FL: grading near Starke Lake and the city's site-plan requirement for travertine or paver decks, Oct. 2026.",
    "h1": "Travertine and Paver Pool Decks in Ocoee",
    "lede": capsule(f"Contractors quoting a travertine or paver pool deck for an Ocoee backyard this fall land somewhere in the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} Florida range. "
                     "A deck going in near Starke Lake answers to the same permit review as one on a corridor-area new build, but the lakefront lot usually asks a few more questions about grading before the base goes down."),
    "sections": [
        ("The same site-plan review covers a lakefront deck and an inland one",
         f"<p>Ocoee's building review doesn't set a different standard for a lot near the water; every {svc('pool-deck-pavers', 'pool deck')} application needs the site plan and work description the city's FAQ spells out, regardless of where the lot sits "
         f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')}). Where that review can differ in practice is the level of grading detail a reviewer wants to see on a lot that slopes toward Starke Lake versus one on flat, inland ground.</p>"),
        ("Downtown's recent public-space work raised the bar for grading nearby",
         f"<p>The city's $44 million downtown capital program included a stormwater facility built specifically to serve several blocks near the lake, alongside new landscaping around Bill Breeze Park "
         f"({ext(DOWNTOWN_URL, 'City of Ocoee, Downtown')}). A private paver or travertine deck going in nearby doesn't tie into that public infrastructure directly, but the same underlying soil and slope conditions that justified the public project are often present on the residential lots around it.</p>"),
    ],
    "scenario": ("A travertine deck on a lot sloping toward Starke Lake, worked out in square feet",
                 f"<p>A 460 sq ft travertine pool deck on a lot that drops gently toward the lake prices out between roughly $5,980 and $13,800 once the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} range is applied. "
                 "Before the base goes in, the crew checks where that slope naturally carries rainwater, since a deck pitched the wrong way on a lakefront lot pushes runoff toward the house instead of away from it, a mistake that costs far more to fix after the pavers are set than before.</p>"),
    "faqs": [
        faq("Does a pool deck near Starke Lake need a different permit than one inland?",
            "No, the same site-plan review applies citywide, though a reviewer may ask more grading detail of a lakefront lot given how the slope there carries water compared with flat, inland ground."),
        faq("Is travertine or a concrete paver more common on Ocoee pool decks near the lake?",
            "Both appear on lakefront lots. Travertine runs noticeably cooler underfoot in full sun, which pulls some homeowners toward it despite the higher price, while budget tends to be the deciding factor for everyone else."),
        faq("Why does grading matter more for a pool deck near Starke Lake?",
            "A lot that slopes toward the water needs its deck pitched to carry rain away from the house and toward the yard's own low point, rather than letting it run straight toward the shoreline."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Ocoee, FL – Historic Patterns",
    "meta": "Stamped concrete contractors in Ocoee, FL: patterns that echo the historic district's Colonial Revival homes, and the city's permit rule, Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Ocoee",
    "lede": capsule(f"Stamped concrete in Ocoee currently prices between {price('stamped-concrete')} per {per('stamped-concrete')}, moving with the pattern and the number of colors chosen. "
                     "A brick-look or slate pattern near the historic Ocoee Street district picks up a visual cue the newer subdivisions along SR 50 simply don't have, though the same site-plan permit applies either way."),
    "sections": [
        ("The district's Colonial Revival homes give a stamped pattern a real reference point",
         f"<p>More than 70 percent of the homes in the Ocoee Street Historic District are Colonial Revival, alongside Tudor Revival and Queen Anne styles, on a 16-acre district listed on the National Register since December 1995 "
         f"({ext(HISTDIST_URL, 'Wikipedia, Ocoee Street Historic District')}). A running-bond brick stamp or a cobble pattern on a driveway near that core echoes those older architectural lines without the long-term upkeep of real clay brick, a starting point worth considering before picking a pattern off a generic sample board.</p>"),
        ("The permit process treats a decorative finish the same as a plain pour",
         f"<p>Ocoee's building FAQ applies its site-plan-and-description rule to every slab regardless of finish, so a multi-color stamped driveway goes through the identical review a plain gray pour would "
         f"({ext(BLDGFAQ_URL, 'City of Ocoee, Building FAQ')}). Where the apron reaches the street, the separate right-of-way permit applies the same way too, since that review is tied to location rather than appearance "
         f"({ext(ROW_URL, 'City of Ocoee, Right-of-Way Permitting')}).</p>"),
    ],
    "scenario": ("Pricing a stamped front walk near the historic core",
                 f"<p>A brick-pattern stamped front walkway near the historic district, 150 sq ft with a single integral color, runs roughly $1,200 to $2,400 once the {price('stamped-concrete')} per {per('stamped-concrete')} range is applied. "
                 "Adding a second color and a deeper tooled joint pattern to better match the surrounding Colonial Revival trim work pushes the same footprint closer to $3,000, with the city's site-plan review applying the same way regardless of which option gets chosen.</p>"),
    "faqs": [
        faq("Does a stamped pattern need to match Ocoee's historic district architecture?",
            "There's no rule requiring it, but a brick or slate-style stamp tends to read better next to the Colonial Revival and Queen Anne homes near the historic core than it would in a newer subdivision further out."),
        faq("Does stamped concrete cost more to permit in Ocoee than plain concrete?",
            "The review itself is identical either way, since the city's site-plan requirement applies to any slab regardless of finish; only the contract price, not the permit process, changes with a decorative choice."),
        faq("Does a stamped driveway apron still need Ocoee's right-of-way permit?",
            "Yes, if it crosses into the street or easement. That review is tied to location, not to whether the concrete is plain or decorative."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Ocoee, FL – Statewide Rules",
    "meta": "Artificial turf installers in Ocoee, FL: the state's 2026 turf rule, Orange County's sinkhole-claims history, and SJRWMD's schedule, Oct. 2026.",
    "h1": "Artificial Turf for Ocoee Yards",
    "lede": capsule(f"Turf installers are pricing Ocoee jobs at {price('artificial-turf')} per {per('artificial-turf')} this fall. "
                     "The statewide 2026 turf rule sets the same base, infill and water-edge buffer here as anywhere else in Florida, and Orange County's inclusion on the state's own sinkhole-claims list is one more reason that base gets built to spec rather than skipped."),
    "sections": [
        ("The 2026 turf rule applies the same way across Ocoee as anywhere else in the state",
         f"<p>Florida's synthetic turf rule, in effect since May 19, 2026, calls for a washed, permeable subgrade, bars any buried irrigation line under the turf, and requires the panel to stay at least 10 feet from the edge of a pond, lake or canal unless a seawall already separates the two "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A 2025 law limits how much further a city or county can tighten that standard "
         f"({src('fs125572', 'Florida Statutes §125.572')}). On a lot backing up to one of Ocoee's retention ponds or drainage canals, that buffer gets measured from the water's real edge, not from a fence line set back from it, before a {svc('artificial-turf', 'turf')} layout is finalized.</p>"),
        ("A sound base matters on ground that sits inside the state's sinkhole-claims counties",
         f"<p>A 2010 Florida Senate interim report, drawing on state insurance-regulator data, places Orange among the counties responsible for the bulk of Florida's sinkhole insurance claims filed between 2006 and 2009 "
         f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). That history doesn't mean a soft patch of yard is a sinkhole, but it is a reason the compacted, washed-stone base the state turf rule already requires gets built carefully rather than rushed, since a weak base under turf can pond the same water it was supposed to shed.</p>"),
    ],
    "scenario": ("Laying out turf against a drainage canal setback",
                 f"<p>Consider a 380 sq ft stretch of side yard that backs up to a drainage canal on an Ocoee lot: pulling the layout back the required 10 feet from the canal's edge trims off roughly 45 sq ft, leaving about 335 sq ft to actually turf. At {price('artificial-turf')} per {per('artificial-turf')}, that comes to somewhere between $3,350 and $8,375 depending on pile height and backing. "
                 "Measuring from the canal's actual waterline, rather than guessing from where the grass currently stops, is what sets the real number before material gets ordered.</p>"),
    "faqs": [
        faq("How close to a drainage canal can artificial turf go in Ocoee?",
            "No closer than 10 feet from the water's actual edge under the statewide turf rule, unless a seawall or similar barrier already separates the lawn from the water."),
        faq("Does Orange County's sinkhole-claims history affect turf installation in Ocoee?",
            "Not as a direct rule, but it's a reason the washed, compacted base the state turf standard already requires gets built properly, since poorly draining ground is more likely to show problems on geology like this."),
        faq("Can an HOA in Ocoee still restrict artificial turf beyond the state rule?",
            "An HOA's own architectural guidelines sit outside the state law limiting city and county turf restrictions, so checking a specific community's rules is still worth doing before ordering material."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
