# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "orlando"

HP_URL = "https://www.orlando.gov/Our-Government/News-and-Information/History/Historic-Preservation-Districts"
LA_URL = "https://en.wikipedia.org/wiki/Lake_Adair%E2%80%93Lake_Concord_Historic_District"

SRC = [
    "census-pep-v2025", "acs-orlando", "orlando-engineering-permit", "orlando-esm", "orlando-ord-2022-45",
    "orlando-res-requirements", "orlando-row-permit", "orlando-hb803-guide", "orlando-bp-history", "bp-network",
    "bp-guidelines", "lakenona-about", "laureatepark-faq", "orlando-tree-ord", "usgs-orange-gw",
    "fl-senate-2011-104", "nrcs-myakka-osd", "nrcs-smyrna-osd", "sjrwmd-watering", "orange-do-i-need-permit",
    "orange-residential-pavers", "orange-res-plan-guide", "fs720-3045", "fs125572", "dep-rule",
    ("City of Orlando — Historic Preservation Districts", HP_URL),
    ("Wikipedia, Lake Adair–Lake Concord Historic District", LA_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Orlando's engineering permit covers the driveway, the patio and the pavers",
        "<p>The city treats a new or widened driveway, a patio or pool-deck slab, and a paver installation as the same category of work: an engineering permit, not a building permit. "
        "The Permitting Services Division, at 400 S. Orange Avenue, reviews the application; call 407-246-2271 or email digitalpermits@orlando.gov before ordering materials "
        f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}). {src('orlando-esm', 'The Engineering Standards Manual')} sets the apron in the right-of-way at a minimum 6 inches of 3,000 psi concrete with a break joint at the property line, "
        "and a single-family driveway runs 7 to 18 feet wide at the throat. The checklist for that permit asks for a dimensioned survey, a front-yard impervious-surface worksheet, and a recorded Notice of Commencement on any contract over $5,000 "
        f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}); the state's 2026 exemption for single-family work under $7,500 waives only the building permit, not this engineering review "
        f"({src('orlando-hb803-guide', 'the HB 803 exemption guide')}). {post('orange-county-orlando-driveway-patio-permits', 'County-by-county permit detail')} and {a('/permits/', 'the permits hub')} go further.</p>"),
    sec("Baldwin Park: a driveway width cap, an alley rule and a twice-monthly review",
        "<p>Baldwin Park sits on the former Naval Training Center Orlando Main Base, identified for closure in the 1993 round of federal base realignments and later redeveloped into one of the city's larger neighborhoods "
        f"({src('orlando-bp-history', 'City of Orlando, Baldwin Park history')}). Its Residential Owners Association reviews every exterior change through an Architectural Review Committee that meets twice a month and caps applications at 25 per session "
        f"({src('bp-network', 'Baldwin Park ROA, ARC page')}). The 2024 update to the neighborhood's residential guidelines limits a front driveway's width to the garage door opening, rules out circular drives in the front yard, and keeps the first 7 feet of any "
        f"alley-loaded driveway built in brick or pavers in solid concrete ({src('bp-guidelines', 'Baldwin Park Residential Guidelines, 2024')}). {cs('orlando', 'concrete-driveways', 'Concrete driveways')} and {cs('orlando', 'artificial-turf', 'artificial turf')} both run into this guideline before the city permit is even filed.</p>"),
    sec("Lake Nona and Laureate Park: newer construction, a second approval step",
        f"<p>Lake Nona is a 17-square-mile mixed-use community inside the Orlando city limits, planned and developed by Tavistock Development Company, with housing stock generally newer than the rest of the city "
        f"({src('lakenona-about', 'Lake Nona, About')}). In Laureate Park, one of its neighborhoods, the Master Association's Architectural Review Board signs off on any property improvement, a pool deck, a fence, a landscape change, before the city permit moves forward, "
        f"with requests submitted by email ({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}). Homeowners near {city('lake-nona', 'Lake Nona')} budget for that review alongside the engineering permit described above; "
        f"{svc('concrete-pool-decks', 'pool decks')} and {svc('paver-patios', 'paver patios')} are the services that come up most often there.</p>"),
    sec("A water table that sits close to the surface",
        f"<p>Orange County's own hydrogeology survey describes a water table that generally mimics land surface, running higher under hilltops than in the low ground between them, and standing “at or very near land surface” at monitored sites after the wet season "
        f"({src('usgs-orange-gw', 'USGS WRI 03-4257')}). Myakka, Florida's own official state soil, and Smyrna cover much of the flatwoods ground under Orlando and Kissimmee, and on both series the seasonal high mark can climb to within a foot and a half of the ground for stretches of a typical year "
        f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}; {src('nrcs-smyrna-osd', 'NRCS, Smyrna series')}). That combination is why a site visit checks drainage and fill depth before a crew prices {svc('concrete-slabs', 'a slab')} or {svc('retaining-walls', 'a retaining wall')}.</p>"),
    sec("Six historic districts, and when a Certificate of Appropriateness applies",
        f"<p>Orlando has designated six historic preservation districts: Downtown (1980), Lake Cherokee (1981), Lake Copeland (1984), Lake Eola Heights (1989), Lake Lawsona (1994) and Colonialtown South (2000) "
        f"({ext(HP_URL, 'City of Orlando, Historic Preservation Districts')}). College Park, just north of those districts, holds its own federally recognized Lake Adair–Lake Concord Historic District, added to the National Register of Historic Places in December 2011, where most homes went up in the first half of the 20th century "
        f"({ext(LA_URL, 'Wikipedia, Lake Adair–Lake Concord Historic District')}). A driveway, patio or color change inside a designated district needs a Certificate of Appropriateness filed alongside the engineering permit "
        f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}); {svc('stamped-concrete', 'stamped concrete')} and {svc('concrete-walkways', 'walkway')} work in those neighborhoods both go through that extra step.</p>"),
    sec("Protected trees and Orange County's place on the sinkhole-claims list",
        f"<p>Ordinance 2020-13 defines a protected tree as any existing tree 6 inches or more in diameter at breast height; removing one takes a Tree Removal Permit, and building inside the required undisturbed area around it without a Tree Encroachment Permit is a code violation "
        f"({src('orlando-tree-ord', 'City of Orlando Ordinance 2020-13')}). That matters on the older, oak-shaded lots common across the city, where the typical home was built in 1992 "
        f"({src('acs-orlando', 'Census Reporter, Orlando')}). A 2010 Florida Senate report placed Orange among eleven counties where, from 2006 through 2009, the state's sinkhole insurance claims piled up past the 88 percent mark statewide, a history worth knowing even though most sunken concrete locally still comes from ordinary settlement rather than a geological event "
        f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). {svc('concrete-repair', 'Concrete repair and resurfacing')} covers either cause.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Which Orlando-area cities and neighborhoods do you serve?",
        f"From Orlando itself, including Baldwin Park, College Park, Lake Nona and Horizon West, the crew reaches {city('winter-garden')}, {city('oviedo')}, {city('kissimmee')}, {city('clermont')} and {city('windermere')} directly, plus smaller communities such as {city('apopka')} and {city('davenport')}. "
        f"{a('/central-florida/', 'The Orlando-unit coverage page')} lists every county and town the crew serves, with a dedicated page for each tier-one city."),
    faq("Do I need a permit for a new or widened driveway in Orlando?",
        f"Yes. The city treats it as an engineering permit rather than a building permit, covering the apron in the right-of-way as well as the driveway on your lot. The 2026 state exemption for single-family work under $7,500 waives only building permits, so it doesn't reach this review "
        f"({src('orlando-hb803-guide', 'HB 803 exemption guide')})."),
    faq("What does Baldwin Park require before I replace a driveway?",
        "Its Residential Owners Association reviews the change through an Architectural Review Committee that meets twice a month, and the 2024 guidelines cap front-driveway width at the garage door opening while keeping the first 7 feet of an alley driveway in solid concrete. "
        "That review runs alongside, not instead of, the city's engineering permit."),
    faq("Does Lake Nona have its own approval process for a pool deck or patio?",
        "In Laureate Park, yes. The Master Association's Architectural Review Board signs off on property improvements, submitted by email, before work starts, separate from the city's engineering permit. Other Lake Nona neighborhoods may run a similar process, so check with the specific HOA before ordering materials."),
    faq("Is Orlando at higher risk of sinkholes than other parts of Central Florida?",
        "Orange County sits on an 11-county list for sinkhole insurance claims filed between 2006 and 2009, alongside the better-known sinkhole-alley counties to the west. Most sunken concrete in the area still comes from ordinary settlement, a leaking pipe or a decayed root, rather than a geological collapse, and the two are diagnosed differently."),
    faq("How do you find the best concrete contractor in Orlando?",
        f"Check the contractor on the state's license-verification tool, ask whether the quote already includes the engineering permit and any HOA review your neighborhood requires, and compare how each bid handles subgrade compaction on flatwoods soil. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor in Orlando')} covers the rest."),
]

HUB = page("/orlando-fl/", "city", "Concrete, Pavers & Turf Contractor in Orlando, FL",
           "Concrete, pavers and turf in Orlando, FL: the city's engineering permit, Baldwin Park and Lake Nona rules, and six historic districts, October 2026.",
           "Concrete, pavers and artificial turf in Orlando, Florida",
           capsule("Opera pours concrete and lays pavers and artificial turf across Orlando, a city of about 333,888 residents in Orange County where most homes date to the early 1990s. "
                   f"As of October 2026, a concrete driveway here runs {price('concrete-driveway')} per {per('concrete-driveway')}, and almost every project on the property, from a widened apron to a new pool deck, needs the city's engineering permit rather than a building permit."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Orlando",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Orlando and Orange County permits"),
                    ("/winter-garden-fl/", "Concrete, pavers and turf in Winter Garden"),
                    ("/oviedo-fl/", "Concrete, pavers and turf in Oviedo"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Orlando, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Orlando, FL – Permit Guide",
    "meta": "Concrete driveway installers in Orlando, FL: the city's engineering permit, 3,000 psi apron spec, and Baldwin Park's alley-driveway rule, as of October 2026.",
    "h1": "Pouring or Replacing a Concrete Driveway in Orlando",
    "lede": capsule(f"A new or replacement concrete driveway in Orlando runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "Every job, from a straight repour to a widened apron, needs the city's engineering permit rather than a building permit, and the apron itself has to be at least 6 inches of 3,000 psi concrete with a break joint at the property line."),
    "sections": [
        ("Why this is an engineering permit, not a building permit",
         f"<p>The Permitting Services Division reviews driveway work under an engineering permit, the same category covering any work that touches the right-of-way, with Permitting Services reachable at 407-246-2271 "
         f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}). The Engineering Standards Manual sets single-family driveway width at 7 to 18 feet measured at the throat, with ribbon driveways built 23 to 36 inches per ribbon and a 28-inch gap between them, and no driveway closer than 3 feet to the property line or within 3 feet of a drainage inlet "
         f"({src('orlando-esm', 'City of Orlando, Engineering Standards Manual §8.11')}). Submitting a permit means a dimensioned survey, MOT notes for any apron work, and a recorded Notice of Commencement if the contract runs past $5,000 "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). That's a heavier review than a straight resurfacing of the existing footprint, which is why we confirm scope with the permit desk before quoting a number.</p>"),
        ("Baldwin Park's alley-loaded lots keep the first 7 feet in concrete",
         f"<p>A lot of Baldwin Park homes load their garage off a rear alley rather than the street, so the driveway rule there works in reverse from a typical apron. The neighborhood's 2024 residential guidelines limit a front driveway to the width of the garage door opening, discourage oversized or circular drives, and, where the alley-side drive is built in brick or concrete pavers, require the first 7 feet measured from the edge of the alley pavement to stay solid concrete "
         f"({src('bp-guidelines', 'Baldwin Park Residential Guidelines, 2024')}). The association's Architectural Review Committee signs off on the change at one of its twice-monthly meetings before work starts "
         f"({src('bp-network', 'Baldwin Park ROA, ARC page')}). Outside Baldwin Park, {svc('paver-driveways', 'a paver driveway')} skips that particular rule, but the city's own apron spec still applies at the street.</p>"),
    ],
    "scenario": ("A Baldwin Park alley driveway, worked out in square feet",
                 f"<p>Say a Baldwin Park alley-loaded driveway measures 10 by 20 feet, 200 square feet, replacing a cracked original pour. Under the neighborhood's 2024 guideline, the first 7 feet back from the alley pavement, about 70 square feet, "
                 f"has to be poured in solid concrete even if the rest of the driveway later gets pavers. At {price('concrete-driveway')} per {per('concrete-driveway')} for a straight repour, that 200 square foot job lands between $1,200 and $3,000 before an old-slab removal or the apron tie-in is added. "
                 "A driveway sized for a two-car household, 24 by 24 feet, runs the same per-square-foot range across 576 square feet, roughly $3,456 to $8,640, before the alley-concrete requirement changes the mix of materials on the job.</p>"),
    "faqs": [
        faq("Does the City of Orlando require a permit for a concrete driveway?",
            "Yes, an engineering permit covers both the apron in the right-of-way and the driveway on your lot, reviewed by the Permitting Services Division. A straight repour within the existing footprint is a smaller submission than a widened or relocated driveway, so confirm the scope with the permit desk before ordering concrete."),
        faq("How wide can a single-family driveway be in Orlando?",
            "The Engineering Standards Manual sets 7 to 18 feet at the throat, and a 2022 parking-code update, read from its adoption draft, caps the front or street-side yard's impervious coverage at 40 percent for any driveway, parking pad or turnaround. Confirm the current codified figure with Permitting Services before finalizing a design."),
        faq("Can I use pavers instead of concrete in a Baldwin Park alley driveway?",
            "Mostly. The 2024 neighborhood guidelines allow brick or concrete pavers for the rest of the driveway, but the first 7 feet back from the alley pavement still has to be solid concrete, and the Architectural Review Committee reviews the plan before the city permit moves forward."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Orlando, FL – Permits & MOU",
    "meta": "Paver driveway installers in Orlando, FL: the city's engineering permit, the right-of-way paver MOU, and the 40% front-yard coverage draft rule, October 2026.",
    "h1": "Paver Driveways in Orlando: Permits, Easements and Coverage Limits",
    "lede": capsule(f"A paver driveway in Orlando runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026, roughly double the plain concrete range because of material and labor. "
                     "Unlike unincorporated Orange County, which only asks for a zoning permit on residential pavers, the city reviews a paver driveway under the same engineering permit as poured concrete, and any paver work that extends into the right-of-way needs its own memorandum of understanding with the city."),
    "sections": [
        ("A paver driveway in the right-of-way needs its own MOU",
         f"<p>Brick or concrete pavers are allowed in the apron if they meet the manual's paver section, but the sidewalk portion crossing the driveway still has to be at least 3,000 psi concrete, 6 inches thick, and any paver driveway reaching into the right-of-way needs a City Paver's Memorandum of Understanding on file "
         f"({src('orlando-esm', 'City of Orlando, Engineering Standards Manual §8.11')}). New driveways have to be paved at least 15 feet into the property from that apron line "
         f"({src('orlando-esm', 'Engineering Standards Manual')}). That's a heavier review than unincorporated Orange County runs for the same material: there, a residential paver installation needs a zoning permit and a $38 fee rather than a full engineering submission "
         f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}).</p>"),
        ("The front-yard coverage cap, read from the 2022 draft ordinance",
         f"<p>Orlando's 2022 parking-code amendments, as drafted, set the impervious-surface ratio of the required front or street-side yard at no more than 40 percent for any driveway, parking area or turnaround, with the driveway itself 7 to 18 feet wide at the property line and no wider than 20 feet through the front setback "
         f"({src('orlando-ord-2022-45', 'City of Orlando, Ordinance 2022-45')}). The outside edge has to sit at least 4 feet from the side line where it meets the right-of-way and at least 2 feet elsewhere, and hammerhead turnarounds aren't allowed on Local Streets. "
         "That cap applies to a paver driveway the same way it applies to plain concrete, which is one reason a wider three-car layout sometimes needs a design revision before the permit clears. Confirm the current codified figure with Permitting Services before finalizing a layout.</p>"),
    ],
    "scenario": ("A two-car paver driveway near Lake Nona, worked out in square feet",
                 f"<p>Say a two-car paver driveway near {city('lake-nona', 'Lake Nona')} measures 24 by 24 feet, 576 square feet. At {price('paver-driveway')} per {per('paver-driveway')}, that job falls between roughly $5,760 and $17,280 depending on the paver material and base thickness, before any City Paver's MOU paperwork for the right-of-way portion is factored in. "
                 "If the home sits inside Laureate Park, the Master Association's Architectural Review Board still has to clear the paver color and layout by email before the city permit is submitted, a step that doesn't apply outside that community.</p>"),
    "faqs": [
        faq("Is a paver driveway permitted differently from concrete in Orlando?",
            "Not really: the city reviews pavers under the same engineering permit it uses for poured concrete, unlike unincorporated Orange County, which only requires a lighter zoning permit for residential pavers. The paver driveway also needs a separate memorandum of understanding if it extends into the right-of-way apron."),
        faq("What is the City Paver's Memorandum of Understanding?",
            "It's a document the city requires on file before a paver driveway crosses into the right-of-way apron, on top of the engineering permit itself. The sidewalk section running through the driveway still has to be poured concrete at the manual's minimum thickness and strength, even when pavers cover the rest."),
        faq("Does the 40 percent front-yard coverage limit apply to pavers?",
            "Yes, the 2022 parking-code draft treats any driveway, parking pad or turnaround the same regardless of material, counting it toward the front or street-side yard's impervious-surface ratio. A wider paver layout sometimes needs narrowing or a landscaped island to stay under that cap."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Orlando, FL – Permits & Trees",
    "meta": "Concrete patio contractors in Orlando, FL: the city's engineering permit, why backyard patios usually skip the coverage cap, and protected trees, October 2026.",
    "h1": "Building a Concrete Patio in Orlando",
    "lede": capsule(f"A concrete patio in Orlando runs {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "The city reviews a patio slab under the same engineering permit it uses for a driveway or pavers, though a backyard patio usually sits outside the 40 percent coverage cap that governs the front or street-side yard, and a protected oak near the back of the house can still shape where the slab goes."),
    "sections": [
        ("Your patio uses the same engineering permit as the driveway",
         f"<p>A patio or pool-deck slab goes through the identical engineering permit the city uses for driveways and pavers "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). The 40 percent impervious-coverage limit in the 2022 parking-code draft is written to govern the required front or street-side yard specifically, so a patio tucked behind the house generally sits outside that calculation, while a side patio visible from the street can still count toward it "
         f"({src('orlando-ord-2022-45', 'City of Orlando, Ordinance 2022-45')}). A recorded Notice of Commencement is required once the contract passes $5,000, the same lien-law threshold that applies to every other flatwork project on the lot "
         f"({src('orlando-res-requirements', 'Residential Permitting Requirements')}).</p>"),
        ("Flatwoods drainage: why the patio's slope gets checked first",
         f"<p>Orange County's groundwater survey describes a water table that climbs close to the surface after the wet season, sitting “at or very near land surface” at some monitored locations "
         f"({src('usgs-orange-gw', 'USGS WRI 03-4257')}). On a patio, that shows up as standing water against the house if the slope away from the foundation isn't set correctly, or as a slab that heaves where fill was never properly compacted. "
         "We check which way an existing yard already drains before pricing a patio extension, not after the forms go up, since regrading after the fact costs more than getting the pitch right on the first pour.</p>"),
    ],
    "scenario": ("A College Park bungalow patio, worked out in square feet",
                 f"<p>Say a 1920s-era bungalow in College Park adds a 12 by 12 foot back patio off the kitchen, 144 square feet. At {price('concrete-patio')} per {per('concrete-patio')}, that lands between roughly $864 and $1,872 before a finish upgrade such as a broom texture or a border. "
                 "On an older lot like this, a live oak with a trunk over 6 inches in diameter counts as a protected tree under the city's tree ordinance, so the patio footprint and the contractor's equipment path both have to stay clear of its required undisturbed area unless a Tree Encroachment Permit is approved first.</p>"),
    "faqs": [
        faq("Does a concrete patio need the same permit as a driveway in Orlando?",
            "Yes, the city reviews patio and pool-deck slabs under the same engineering permit it uses for driveways and pavers. The application still needs a dimensioned survey and, on larger contracts, a recorded Notice of Commencement."),
        faq("Does the 40 percent coverage limit apply to a backyard patio?",
            "Usually not. The 2022 parking-code draft writes that cap around the required front or street-side yard, so a patio set behind the house typically isn't counted, while a side-yard patio visible from the street may still be. Confirm with Permitting Services if your lot's layout is close to the line."),
        faq("What if a protected oak is in the way of a new patio?",
            "Orlando's tree ordinance protects any existing tree 6 inches or larger in diameter at breast height, and building inside its required undisturbed area without a Tree Encroachment Permit is a code violation. We lay out the patio around the root zone first, then apply for the encroachment permit if the design still needs it."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Orlando, FL",
    "meta": "Paver patio installers in Orlando, FL: the city's engineering permit, Laureate Park's architectural review, and Baldwin Park's flush-porch-paver rule, October 2026.",
    "h1": "Paver Patios and Walkways Around an Orlando Home",
    "lede": capsule(f"A paver patio in Orlando runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "The city reviews pavers on a patio under the same engineering permit it uses for concrete, and in Lake Nona's Laureate Park neighborhood a homeowners' architectural review board signs off on the layout before that permit is even filed."),
    "sections": [
        ("Pavers on a patio still need the engineering permit, but skip the MOU",
         f"<p>Patio and walkway pavers fall under the same engineering permit review the city applies to a patio slab or a driveway, since the submission covers “pavers, asphalt, concrete” as one category "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). The separate City Paver's Memorandum of Understanding only applies where pavers cross into the public right-of-way, so a backyard patio or a front walkway that stays on private property skips that extra document "
         f"({src('orlando-esm', 'Engineering Standards Manual §8.11')}). Inside one of the city's six historic districts, a Certificate of Appropriateness still applies to a visible front paver walkway "
         f"({src('orlando-res-requirements', 'Residential Permitting Requirements')}).</p>"),
        ("Laureate Park's Architectural Review Board reviews patios too",
         f"<p>In Laureate Park, the Lake Nona neighborhood built around its namesake park, the Master Association requires its Architectural Review Board to approve “all improvements to your property (home, landscape, pool, fence, etc.)” before work starts, with the request submitted by email "
         f"({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}). That review sits on top of, not instead of, the city's own engineering permit. Outside Lake Nona, {cs('orlando', 'paver-driveways', 'a paver driveway')} or patio in most Orlando neighborhoods only has the city process to clear, though Baldwin Park and a handful of other communities run their own design committees as well.</p>"),
    ],
    "scenario": ("A Baldwin Park porch and patio paver job, worked out in square feet",
                 f"<p>Say a Baldwin Park home relays 240 square feet of paver patio off the back porch. At {price('paver-patio')} per {per('paver-patio')}, that lands between roughly $2,400 and $4,080 depending on the paver and the base depth. "
                 "A 2024 amendment to the neighborhood's residential guidelines added a flush-paver requirement for the front porch and walkway, so where that same crew also resets porch pavers, the finished surface has to sit flush with the surrounding grade rather than stepped or proud of it.</p>"),
    "faqs": [
        faq("Do paver patios need a separate permit from a paver driveway in Orlando?",
            "They go through the same engineering permit category, covering pavers, asphalt and concrete together, but a patio that stays on private property skips the City Paver's Memorandum of Understanding that applies only where pavers extend into the right-of-way."),
        faq("Does Laureate Park require approval for a new patio?",
            "Yes. The Master Association's Architectural Review Board reviews property improvements, including patios, landscaping and pool areas, with requests submitted by email before work starts. That review runs alongside the city's engineering permit, not in place of it."),
        faq("What is Baldwin Park's rule about flush porch pavers?",
            "A 2024 update to the neighborhood's design guidelines requires pavers on the front porch and walkway to sit flush with the surrounding surface rather than raised or recessed, a detail worth planning for when releveling or replacing porch pavers there."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Orlando, FL – New Builds",
    "meta": "Concrete pool deck builders in Orlando, FL: Lake Nona's newer housing stock, the city's engineering permit, and grading on a high water table, October 2026.",
    "h1": "Concrete Pool Decks for Orlando Homes",
    "lede": capsule(f"A concrete pool deck in Orlando runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} as of October 2026. "
                     "Many of the city's newest pools are going in around Lake Nona, where a pool deck permit runs through the same engineering review as a driveway, plus a second sign-off from the neighborhood's own architectural board in communities like Laureate Park."),
    "sections": [
        ("New construction in Lake Nona means more first-time pool decks",
         f"<p>Lake Nona is described by its own developer as a 17-square-mile community inside the Orlando city limits, planned by Tavistock Development Company, and its housing is newer on average than the rest of a city where the typical home dates to 1992 "
         f"({src('lakenona-about', 'Lake Nona, About')}; {src('acs-orlando', 'Census Reporter, Orlando')}). A pool deck slab there goes through the same engineering permit review the city uses for a driveway or a patio "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}), and in Laureate Park the Master Association's Architectural Review Board separately signs off on the pool and deck layout by email before the city process starts "
         f"({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}).</p>"),
        ("Grading a deck where the water table rises after the wet season",
         f"<p>Orange County's hydrogeology survey notes that the water table “generally is highest after the wet season” and sits close to the surface at low points across the county "
         f"({src('usgs-orange-gw', 'USGS WRI 03-4257')}). On a pool deck, that means the slope away from the coping and the height of the deck above surrounding grade both matter more than on a lot with deep, excessively drained sand. "
         "We confirm the finished pool elevation against the yard's existing drainage pattern before forming the deck, since a deck poured flat against a high water table can pond at the equipment pad even when the rest of the yard drains fine.</p>"),
    ],
    "scenario": ("A new Lake Nona pool deck, worked out in square feet",
                 f"<p>Say a new build near Lake Nona pours a 900 square foot pool deck around a fresh pool shell. At {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, that lands between roughly $4,500 and $13,500 depending on the finish, from a basic broom texture at the low end to a cool-touch decorative finish at the high end. "
                 "If the lot sits inside Laureate Park, that budget also needs to account for the Architectural Review Board's email approval step before pouring day is scheduled.</p>"),
    "faqs": [
        faq("Does a new pool deck near Lake Nona need two approvals?",
            "In Laureate Park, yes: the Master Association's Architectural Review Board reviews the pool and deck design by email, separate from the city's engineering permit that covers the slab itself. Other Lake Nona neighborhoods may run a similar process, so check with the specific HOA."),
        faq("What permit covers a concrete pool deck in Orlando?",
            "The same engineering permit the city uses for a driveway or a patio slab, filed through the Permitting Services Division rather than a building permit. A recorded Notice of Commencement applies once the contract passes $5,000."),
        faq("Does the high water table around Orlando affect pool deck construction?",
            "It affects grading more than the slab itself. Orange County's groundwater data shows the table rising close to the surface after the wet season in low-lying spots, so the deck's slope and elevation relative to the yard's drainage get checked before forming begins."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Orlando, FL – Overlays",
    "meta": "Pool deck paver overlays in Orlando, FL: resurfacing 1990s-era decks, the city's engineering permit for pavers, and newer Lake Nona construction, October 2026.",
    "h1": "Pool Deck Pavers in Orlando: New Decks and Overlays",
    "lede": capsule(f"Pool deck pavers in Orlando run {price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026, whether laid over a new slab or set as an overlay on an older deck. "
                     "With the typical Orlando home dating to 1992, a lot of the original broom-finish and cool-deck pool surfaces around the city are now old enough that a paver overlay is a common alternative to full resurfacing."),
    "sections": [
        ("Resurfacing a 1990s-era pool deck with pavers still needs a permit",
         f"<p>Orlando's median year of home construction is 1992 "
         f"({src('acs-orlando', 'Census Reporter, Orlando')}), old enough that many original concrete pool decks around the city are candidates for a paver overlay rather than a full tear-out. The city's engineering permit covers pavers “whether installing/removing pavers, asphalt, concrete or expanding” an existing paved area, which reaches an overlay laid over an existing slab, not just new construction "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). Inside a historic district, a Certificate of Appropriateness applies if the new deck color or coping is visible from a public street "
         f"({ext(HP_URL, 'City of Orlando, Historic Preservation Districts')}).</p>"),
        ("Older pools inland, newer pools near Lake Nona",
         f"<p>Because Lake Nona's 17 square miles were planned and built out largely after the rest of the city "
         f"({src('lakenona-about', 'Lake Nona, About')}), most of its pools and decks are recent enough that homeowners there are choosing pavers for a first install rather than resurfacing an aging slab. Closer to the city's older, established neighborhoods, where the typical home is now more than three decades old, the opposite pattern shows up more often: an original deck reaching the point where an overlay, rather than a patch, makes more sense. "
         f"{svc('concrete-pool-decks', 'A new concrete pool deck')} is the other option at either stage.</p>"),
    ],
    "scenario": ("A paver overlay on a 1990s-era Orlando pool deck, worked out in square feet",
                 f"<p>Say a 1990s-built home resurfaces a 600 square foot original cool-deck pool patio with pavers over the existing slab. At {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, that overlay lands between roughly $7,200 and $18,000 depending on the paver material, from standard concrete pavers at the lower end to travertine at the upper end. "
                 "A tear-out and full replacement instead of an overlay adds demolition cost but avoids building on whatever settling the original slab has already done.</p>"),
    "faqs": [
        faq("Can pavers go over an existing cracked pool deck in Orlando?",
            "Often yes, as an overlay, and the city's engineering permit covers that scope the same way it covers a new installation. Whether an overlay or a tear-out makes more sense depends on how much the existing slab has settled or cracked, which is worth checking before committing to either approach."),
        faq("Is a permit needed for a pool deck paver overlay, or just new construction?",
            "Both. Orlando's engineering permit language covers installing, removing or expanding pavers, asphalt or concrete, which reaches an overlay on an existing deck as well as a brand-new pour."),
        faq("Are older or newer Orlando homes more likely to need pool deck paver work?",
            "Both, for different reasons. Newer construction around Lake Nona tends toward a first paver install on a new pool, while the city's older, established neighborhoods, where the typical home is now more than 30 years old, see more overlay and resurfacing work on original concrete decks."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Orlando, FL – Historic Rules",
    "meta": "Stamped concrete contractors in Orlando, FL: the Certificate of Appropriateness required in six historic districts, and the 40% coverage cap, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Orlando",
    "lede": capsule(f"Stamped concrete in Orlando runs {price('stamped-concrete')} per {per('stamped-concrete')} as of October 2026, depending on the pattern and the number of colors used. "
                     "Inside any of the city's six historic preservation districts, a pattern or color change on a visible driveway or walk needs a Certificate of Appropriateness filed alongside the engineering permit, a step a plain gray pour outside those districts skips."),
    "sections": [
        ("Six historic districts, and why pattern and color need sign-off there",
         f"<p>Orlando has designated six historic preservation districts: Downtown (1980), Lake Cherokee (1981), Lake Copeland (1984), Lake Eola Heights (1989), Lake Lawsona (1994) and Colonialtown South (2000) "
         f"({ext(HP_URL, 'City of Orlando, Historic Preservation Districts')}). A visible change to a driveway or front walk inside one of those districts, including a new stamped pattern or an integral color that wasn't there before, needs a Certificate of Appropriateness submitted with the engineering permit application "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). College Park, just outside those six, carries its own federally recognized Lake Adair–Lake Concord Historic District, where the same review practice is worth checking with the city before a color is picked "
         f"({ext(LA_URL, 'Wikipedia, Lake Adair–Lake Concord Historic District')}).</p>"),
        ("The front-yard coverage cap treats stamped concrete the same as plain",
         f"<p>Orlando's 2022 parking-code draft caps the front or street-side yard's impervious coverage at 40 percent for “any driveway, parking, or turn around configuration,” regardless of the finish poured "
         f"({src('orlando-ord-2022-45', 'City of Orlando, Ordinance 2022-45')}). A stamped border or an accent band doesn't change that calculation; the driveway still has to run 7 to 18 feet wide at the property line and no wider than 20 feet through the front setback. "
         "We account for that cap at the design stage, before a stamped pattern or a decorative border adds square footage the permit can't cover.</p>"),
    ],
    "scenario": ("A historic-district stamped concrete replacement, worked out in square feet",
                 f"<p>Say a home in Colonialtown South replaces a plain apron-and-walk combination, 300 square feet, with a slate-pattern stamped finish and an integral color. At {price('stamped-concrete')} per {per('stamped-concrete')}, that lands between roughly $2,400 and $5,700 depending on the number of colors and the release agent used. "
                 "Before the pour, the color and pattern go to the city's Historic Preservation Board for a Certificate of Appropriateness, a step that doesn't apply to the same job on a lot outside one of the six districts.</p>"),
    "faqs": [
        faq("Do I need special approval for a stamped concrete color in a historic district?",
            "Yes, inside any of Orlando's six historic preservation districts, a Certificate of Appropriateness has to be filed with the engineering permit before a new pattern or integral color goes down on a visible driveway or walk."),
        faq("Does the 40 percent coverage limit apply to stamped concrete differently than plain concrete?",
            "No, the 2022 parking-code draft treats any driveway, parking pad or turnaround the same regardless of finish, so a stamped pattern or decorative border still counts toward the front or street-side yard's coverage cap."),
        faq("Which Orlando neighborhoods are designated historic districts?",
            "Downtown, Lake Cherokee, Lake Copeland, Lake Eola Heights, Lake Lawsona and Colonialtown South are the city's six designated districts, with College Park's Lake Adair–Lake Concord Historic District recognized separately on the National Register of Historic Places."),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Sidewalks & Walkways in Orlando, FL – Permits",
    "meta": "Concrete walkway and sidewalk contractors in Orlando, FL: the right-of-way permit, College Park's oak canopy, and the 6-inch protected-tree rule, October 2026.",
    "h1": "Concrete Sidewalks and Walkways in Orlando",
    "lede": capsule(f"A concrete walkway in Orlando runs {price('concrete-walkway')} per {per('concrete-walkway')} as of October 2026. "
                     "Any walkway or sidewalk repair that touches the right-of-way goes through the same right-of-way permit as a driveway apron, and in older, oak-lined neighborhoods like College Park, root heave from a protected tree is as common a reason to replace a walk as plain cracking."),
    "sections": [
        ("Sidewalk work falls under the same right-of-way permit as the apron",
         f"<p>Any work “in the street, under the sidewalk or in the grassy area next to the street” needs a right-of-way permit, which may already be covered if a larger engineering permit is on file for the same address "
         f"({src('orlando-row-permit', 'City of Orlando, Apply for a Right-of-Way Permit')}). Plans are reviewed within 10 business days. A sidewalk section that crosses a driveway has to meet the same 3,000 psi, 6-inch minimum the manual sets for the apron itself, even where the rest of the walkway is thinner "
         f"({src('orlando-esm', 'Engineering Standards Manual §8.11')}).</p>"),
        ("College Park's oak canopy and a 6-inch protected-tree threshold",
         f"<p>College Park's Lake Adair–Lake Concord Historic District, added to the National Register of Historic Places in December 2011, is a neighborhood where most homes went up in the first half of the 20th century, long enough ago for street trees to have grown into the sidewalks "
         f"({ext(LA_URL, 'Wikipedia, Lake Adair–Lake Concord Historic District')}). Citywide, Ordinance 2020-13 protects any existing tree 6 inches or larger in diameter at breast height, and removing one, or encroaching into the required undisturbed area around it, needs a separate permit "
         f"({src('orlando-tree-ord', 'City of Orlando Ordinance 2020-13')}). On a lot like that, root pruning, a flexible joint around the trunk, or rerouting the walk entirely are all on the table before concrete goes down again.</p>"),
    ],
    "scenario": ("A College Park walkway replacement, worked out in square feet",
                 f"<p>Say a bungalow in College Park replaces a 4-foot-wide, 40-foot-long front walkway lifted by a live oak's roots, 160 square feet. At {price('concrete-walkway')} per {per('concrete-walkway')}, that lands between roughly $1,120 and $2,720, before any root-pruning or encroachment-permit cost if the oak's trunk measures 6 inches or more across. "
                 "Because the walkway sits in the city's right-of-way for part of its length, the same application doubles as the right-of-way permit for that section.</p>"),
    "faqs": [
        faq("Does replacing a cracked sidewalk in Orlando need a permit?",
            "Yes, any sidewalk or walkway work touching the right-of-way needs a right-of-way permit, reviewed within about 10 business days, and it may already be covered if a broader engineering permit is on file for the address."),
        faq("What counts as a protected tree under Orlando's tree ordinance?",
            "Any existing tree measuring 6 inches or more in diameter at breast height. Removing one needs a Tree Removal Permit, and building or paving inside its required undisturbed area without a Tree Encroachment Permit is a violation of Ordinance 2020-13."),
        faq("Is College Park a designated historic district in Orlando?",
            "College Park holds its own federally recognized historic district, the Lake Adair–Lake Concord Historic District, added to the National Register in 2011, separate from the city's six locally designated preservation districts elsewhere in Orlando."),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Orlando, FL – Shed & Pad Permits",
    "meta": "Concrete slab contractors in Orlando, FL: shed, AC and parking pad permits, and what Baldwin Park's redeveloped base ground means for subgrade, October 2026.",
    "h1": "Concrete Slabs for Sheds, Pads and Parking in Orlando",
    "lede": capsule(f"A concrete slab in Orlando runs {price('concrete-slab')} per {per('concrete-slab')} as of October 2026. "
                     "A shed, AC or parking pad goes through the same engineering permit review as a patio, and on a redeveloped lot like Baldwin Park's former military base ground, a site visit checks what kind of fill sits under the slab before pricing the job."),
    "sections": [
        ("A shed, AC or parking pad goes through the same permit review",
         f"<p>The city's permitting checklist covers any slab, not just a driveway or a patio, under the same engineering review, with a dimensioned survey showing the pad's location relative to the property line "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). A recorded Notice of Commencement applies once the contract passes $5,000, and the 2026 building-permit exemption for work under $7,500 still doesn't reach this engineering review "
         f"({src('orlando-hb803-guide', 'HB 803 exemption guide')}). A small shed pad and a full RV or boat parking slab both fall under the same category; size is what changes the fee and the review time, not the type of permit.</p>"),
        ("Baldwin Park's redevelopment means a site visit checks the fill first",
         f"<p>Baldwin Park was built on the former Naval Training Center Orlando Main Base, identified for closure in 1993 and redeveloped afterward into residential streets and lots "
         f"({src('orlando-bp-history', 'City of Orlando, Baldwin Park history')}). A slab poured on ground that was graded and filled as part of that redevelopment doesn't behave the same as one poured on undisturbed native soil, so we check what's actually under a Baldwin Park lot, compacted engineered fill versus the native flatwoods sand found elsewhere in the city, before pricing a shed or parking pad there.</p>"),
    ],
    "scenario": ("A Baldwin Park shed slab, worked out in square feet",
                 f"<p>Say a Baldwin Park homeowner pours a 10 by 10 foot shed pad, 100 square feet. At {price('concrete-slab')} per {per('concrete-slab')}, that lands between roughly $400 and $1,000 depending on the mix and reinforcement. "
                 "A larger 20 by 20 foot parking pad, 400 square feet, scales the same per-square-foot range to roughly $1,600 to $4,000, with the fill check adding a step a slab on undisturbed ground elsewhere in the city wouldn't need.</p>"),
    "faqs": [
        faq("Does a shed slab need a permit in Orlando?",
            "Yes, a shed, AC or parking pad goes through the same engineering permit review the city uses for a patio or driveway slab, with a site survey showing where the pad sits on the lot."),
        faq("Is an AC pad permitted separately from a shed slab?",
            "They're the same permit category, an engineering review for a slab on grade, though each pad is still submitted with its own location on the survey."),
        faq("Why does Baldwin Park's history matter for a new slab there?",
            "The neighborhood sits on the former Naval Training Center Orlando Main Base, closed in 1993 and redeveloped into residential lots, so a site visit checks whether a given lot has compacted engineered fill from that redevelopment rather than undisturbed native soil before a slab is priced."),
    ],
    "sources": SRC,
}

# 10. concrete-repair ----------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair & Resurfacing in Orlando, FL",
    "meta": "Concrete repair and resurfacing in Orlando, FL: why 1990s-era driveways are cracking, Orange County's sinkhole-claims history, and ordinary settlement, October 2026.",
    "h1": "Concrete Repair and Resurfacing in Orlando",
    "lede": capsule(f"Concrete repair and resurfacing in Orlando runs {price('concrete-repair')} per {per('concrete-repair')} as of October 2026. "
                     "With the typical Orlando home dating to 1992, a large share of the city's original driveways are now more than three decades old, past the point where cracking and surface wear are routine rather than a sign of a bigger problem."),
    "sections": [
        ("Many Orlando driveways are now more than 30 years old",
         f"<p>Orlando's median year of home construction is 1992 "
         f"({src('acs-orlando', 'Census Reporter, Orlando')}), which puts a large share of the city's original concrete driveways and walks well past three decades old, the stretch where control joints open up, surface spalling shows, and a straight resurfacing starts making more sense than another patch. "
         f"A full driveway replacement still goes through the city's engineering permit, but a repair or resurfacing within the existing footprint is a smaller submission; confirm the exact scope with Permitting Services at 407-246-2271 before assuming a given job is permit-exempt "
         f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}).</p>"),
        ("Orange County's sinkhole-claims history, and what it usually doesn't mean",
         f"<p>A 2010 Florida Senate interim report found Orange County among 11 counties that together accounted for more than 88 percent of the sinkhole insurance claims filed statewide between 2006 and 2009, grouped there with counties sharing a similar shallow-limestone geology "
         f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). That history is worth knowing, but most sunken or settled concrete locally still traces back to ordinary causes, loose fill under the original pour, a leaking irrigation or sewer line, or a decayed tree root, rather than the sudden ground collapse the insurance claims describe. Telling the two apart usually comes down to how the slab moved: a gradual, localized dip points toward settlement, while a sudden, deep depression warrants a closer look.</p>"),
    ],
    "scenario": ("Resurfacing a 1990s-era Orlando driveway, worked out in square feet",
                 f"<p>Say a driveway poured in 1992, the city's median construction year, shows surface cracking and spalling across a 400 square foot two-car pad. At {price('concrete-repair')} per {per('concrete-repair')} for resurfacing, that lands between roughly $1,200 and $4,000 depending on whether it's a basic overlay or a decorative finish added at the same time. "
                 "A full tear-out and repour instead of a resurfacing moves the job into the driveway price range and the full engineering permit process described above.</p>"),
    "faqs": [
        faq("Is it normal for a 30-year-old Orlando driveway to crack?",
            "Yes, with a typical home built around 1992, a lot of original driveways are well past 30 years old, where control-joint cracking and surface wear are routine maintenance items rather than a structural problem."),
        faq("Does a concrete repair or resurfacing job need a permit in Orlando?",
            "A full replacement goes through the same engineering permit as a new driveway, but a repair or resurfacing within the existing footprint is typically a smaller submission. Check the specific scope with Permitting Services before assuming a job is exempt."),
        faq("How can I tell if a sunken driveway is settlement or a sinkhole?",
            "A gradual, localized dip usually points to ordinary settlement, loose fill, a leaking line or a decayed root, while a sudden, deep depression is the kind of event the state's catastrophic ground-cover-collapse insurance coverage describes. Orange County's history with sinkhole claims makes the question worth asking, even though settlement is the more common cause."),
    ],
    "sources": SRC,
}

# 11. paver-sealing -------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing & Restoration in Orlando, FL",
    "meta": "Paver sealing and restoration in Orlando, FL: why sealing day doesn't follow the SJRWMD watering schedule, and Baldwin Park's flush-porch-paver rule, October 2026.",
    "h1": "Paver Sealing and Restoration in Orlando",
    "lede": capsule(f"Paver sealing in Orlando runs {price('paver-sealing')} per {per('paver-sealing')} as of October 2026, including the pressure-wash, re-sand and seal steps. "
                     "Orange County follows the St. Johns River Water Management District's year-round lawn-watering schedule, but a hose-fed pressure washer used to rinse pavers before sealing isn't irrigation, so the job doesn't have to wait for a particular watering day."),
    "sections": [
        ("Sealing day doesn't depend on Orlando's watering calendar",
         f"<p>Orange County follows the St. Johns River Water Management District's restrictions in full, which set a year-round schedule, odd or no-address homes on Wednesday and Saturday, even addresses on Thursday and Sunday under Daylight Saving Time, with no sprinkler irrigation between 10 a.m. and 4 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}). Those limits apply to irrigation systems and lawn watering, not to a pressure washer rinsing a driveway or patio, so the pre-seal cleaning step and the re-sanding that follows it get scheduled around the weather and the crew, not an address's watering day.</p>"),
        ("Baldwin Park's 2024 guideline keeps porch pavers flush when they're relaid",
         f"<p>A 2024 amendment to Baldwin Park's residential design guidelines added a flush-paver requirement for the front porch and walkway "
         f"({src('bp-guidelines', 'Baldwin Park Residential Guidelines, 2024')}). That matters on a sealing and releveling job specifically: where joint sand has washed out or a paver has settled unevenly, resetting it flush with its neighbors is part of the standard, not just a nice-to-have, before the sealer goes on. Elsewhere in the city, the same flush-and-level standard is good practice even without a written guideline requiring it.</p>"),
    ],
    "scenario": ("Resealing an Orlando paver driveway, worked out in square feet",
                 f"<p>Say a 500 square foot paver driveway gets a full clean, re-sand with polymeric sand, and seal. At {price('paver-sealing')} per {per('paver-sealing')}, that lands between roughly $750 and $1,625 depending on how much releveling the joints need before sealing. "
                 "A smaller 240 square foot porch-and-walkway job in Baldwin Park scales down proportionally, with the added step of confirming every relaid paver sits flush with the surrounding surface under the neighborhood's 2024 guideline.</p>"),
    "faqs": [
        faq("Does paver sealing need a permit in Orlando?",
            "No, cleaning, re-sanding and sealing existing pavers isn't the kind of work the city's engineering permit covers; that permit applies to new or expanded paved areas, not maintenance on pavers already installed."),
        faq("Can I have my pavers washed on a day SJRWMD doesn't allow watering?",
            "Yes. The district's restrictions govern lawn irrigation and sprinkler systems, not a hose-fed pressure washer, so rinsing pavers before sealing isn't tied to the twice-a-week schedule Orange County follows."),
        faq("Does Baldwin Park require anything specific when resealing porch pavers?",
            "A 2024 update to the neighborhood's residential guidelines requires porch and front-walkway pavers to sit flush with the surrounding surface, which is worth checking during any releveling that happens as part of a sealing job there."),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Orlando, FL – Engineering Rules",
    "meta": "Retaining wall contractors in Orlando, FL: the city's unpublished height trigger, the statewide 48-inch engineering threshold, October 2026.",
    "h1": "Retaining Walls for Orlando Yards",
    "lede": capsule(f"A retaining wall in Orlando runs {price('retaining-wall')} per {per('retaining-wall')} of wall face as of October 2026. "
                     "The city's own permitting pages don't publish a stand-alone height that triggers engineering review for a wall, so we confirm the threshold with Permitting Services directly, working from the statewide code figure used elsewhere in the region as the likely baseline."),
    "sections": [
        ("Orlando publishes no stand-alone height trigger for a retaining wall",
         f"<p>Unlike the driveway, patio and paver rules, the city's engineering permit pages don't state a specific wall height that requires signed and sealed engineering, which makes a direct call to Permitting Services at 407-246-2271 worth making before finalizing a design "
         f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}). Florida's residential code sets that trigger statewide at 48 inches of unbalanced retained fill where the top isn't otherwise supported, or 24 inches where the wall also resists lateral loads beyond the soil itself, the same threshold Orange County's own permitting guide cites for its unincorporated area "
         f"({src('orange-res-plan-guide', 'Orange County, A Guide for Residential Plan Approval')}).</p>"),
        ("Lake Nona and Laureate Park: a wall counts as a landscape change too",
         f"<p>In Laureate Park, the Master Association's Architectural Review Board reviews “all improvements to your property (home, landscape, pool, fence, etc.)” before work starts "
         f"({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}), language broad enough to cover a retaining or seat wall built to manage a sloped yard. On the gently rolling lots common around Lake Nona, a low seat wall is as often a landscape feature as a structural necessity, but either way the neighborhood's review happens before, not after, the city's own permit process.</p>"),
    ],
    "scenario": ("A sloped-yard retaining wall near Lake Nona, worked out in square feet",
                 f"<p>Say a sloped lot near Laureate Park needs a 30 linear foot segmental block wall, 3 feet tall, 90 square feet of wall face. At {price('retaining-wall')} per {per('retaining-wall')} of wall face, that lands between roughly $1,350 and $3,600 before drainage behind the wall or an engineering review is added in. "
                 "Because the wall stays under the 48-inch statewide threshold for unbalanced fill, it's less likely to need a sealed engineering drawing than a taller wall would, though confirming that with the city is still worth the phone call.</p>"),
    "faqs": [
        faq("Does Orlando publish a retaining wall height that requires a permit?",
            "Not on its public permitting pages. Call Permitting Services at 407-246-2271 to confirm the threshold for a specific design; the statewide residential code figure of 48 inches of unbalanced fill, used by Orange County's own guide, is a reasonable baseline to plan around."),
        faq("Does Laureate Park's architectural board review retaining walls?",
            "Its review covers landscape changes broadly, which includes a retaining or seat wall, separate from whatever the city's own permit process requires. Submit the plan to the Master Association by email before the city application is filed."),
        faq("What height retaining wall needs engineering in Florida?",
            "The statewide residential code sets the trigger at 48 inches of unbalanced retained fill where the top isn't otherwise supported, or 24 inches where the wall also resists lateral loads beyond the soil, a figure Orange County's permitting guide cites directly."),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Orlando, FL – Permits & Rules",
    "meta": "Artificial turf installers in Orlando, FL: the city's engineering permit, the 50-foot water-body setback, and Baldwin Park's turf-screening rule, October 2026.",
    "h1": "Artificial Turf for Orlando Yards",
    "lede": capsule(f"Artificial turf in Orlando runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "The city counts turf as impervious surface and requires its own engineering permit, with a rule keeping it at least 50 feet from any water body, a stricter local setback than the statewide standard, plus a screening requirement in Baldwin Park for anywhere it's visible from the street."),
    "sections": [
        ("Orlando treats turf as impervious and keeps it 50 feet from water",
         f"<p>The city's residential permitting page states plainly that artificial turf “also needs an engineering permit because it counts as impervious,” and that it “isn't allowed within 50 ft of a water body” "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). That local rule is tighter than the statewide standard set by the Department of Environmental Protection's turf rule, which keeps synthetic turf 10 feet from a water body unless it backs onto a seawall, bars in-ground irrigation under it, and requires natural infill and a washed base "
         f"({src('dep-rule', 'DEP Rule 62-308.100')}). A 2025 state law otherwise limits how far local governments can go in regulating residential turf "
         f"({src('fs125572', 'F.S. 125.572')}).</p>"),
        ("Baldwin Park screens turf from the street and the neighbors",
         f"<p>A 2021 amendment to Baldwin Park's residential guidelines permits artificial turf only in private zones, and requires it to be “screened from view from public right of way or adjacent properties with fencing or a landscape hedge” "
         f"({src('bp-guidelines', 'Baldwin Park Residential Guidelines, 2024')}). That lines up with state law more broadly: as of 2026, an HOA can only restrict turf that's visible from the frontage or an adjoining lot, not turf tucked into a screened backyard "
         f"({src('fs720-3045', 'F.S. 720.3045')}). Outside Baldwin Park, a different community's HOA may still apply its own version of that same visibility test.</p>"),
    ],
    "scenario": ("Backyard turf behind a Baldwin Park hedge, worked out in square feet",
                 f"<p>Say a Baldwin Park backyard replaces 500 square feet of struggling St. Augustine with artificial turf, screened from the alley by an existing hedge. At {price('artificial-turf')} per {per('artificial-turf')}, that lands between roughly $5,000 and $12,500 depending on the pile height and backing. "
                 "Because the area sits behind the hedge rather than facing the street, it meets both the neighborhood's 2021 screening rule and the statewide HOA-visibility test, on top of the city's own engineering permit and the 50-foot water-body setback if a pond or canal is anywhere near the yard.</p>"),
    "faqs": [
        faq("Does artificial turf count as impervious surface in Orlando?",
            "Yes, the city's own permitting page states that turf counts as impervious and requires an engineering permit, the same category covering driveways and pavers, rather than being treated as a landscaping change that skips review."),
        faq("How close to a pond or lake can artificial turf be installed in Orlando?",
            "No closer than 50 feet under the city's own rule, tighter than the state Department of Environmental Protection's 10-foot standard that applies where local rules don't set something stricter."),
        faq("Does my HOA need to approve artificial turf even if the city allows it?",
            "Often yes. Baldwin Park's guidelines, for example, require turf to be screened from the street or neighboring lots with fencing or a hedge, and as of 2026 state law only lets an HOA restrict turf that's actually visible from the frontage or an adjoining property."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
