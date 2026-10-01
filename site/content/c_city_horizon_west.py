# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "horizon-west"

ARCH_GUIDE_URL = "http://ocfl.net/Portals/0/resource%20library/planning%20-%20development/Horizon%20West%20Architectural%20Guide-CERT.pdf"
WIKI_HW_URL = "https://en.wikipedia.org/wiki/Horizon_West,_Florida"
CENSUSREPORTER_HW_URL = "http://censusreporter.org/profiles/16000US1232610-horizon-west-fl/"
NEWSCHOOL_URL = "https://www.orangeobserver.com/news/2026/jan/07/forecast-2026-horizon-wests-newest-elementary-school/"
NEWSCHOOL_LABEL = "Orange Observer, forecast on Horizon West's newest elementary school"
OVERCROWD_URL = "https://www.horizonwestinfo.com/school-year-ends-with-horizon-west-schools-still-overcrowded/"

SRC = [
    "orange-bldg", "orange-do-i-need-permit", "orange-residential-pavers", "orange-row-directory",
    "orange-code-ch21-art6", "orange-lot-grading", "orange-res-plan-guide", "ocfl-tree-permit",
    "ocfl-horizonwest", "sjrwmd-watering", "dep-rule", "fs125572", "fs720-3045",
    ("Orange County Planning Division, Horizon West Architectural Design Standards Guidebook (Dec. 2015)", ARCH_GUIDE_URL),
    ("Wikipedia, Horizon West, Florida", WIKI_HW_URL),
    ("Census Reporter, Horizon West, FL", CENSUSREPORTER_HW_URL),
    ("Orange Observer, forecast on Horizon West's newest elementary school", NEWSCHOOL_URL),
    ("Horizon West Happenings, school year overcrowding report", OVERCROWD_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("No town hall here, so a permit means a trip to the county",
        f"<p>Horizon West has never incorporated; the county's own page calls it a special planning area sitting in southwest unincorporated Orange County, which means the Division of Building Safety, not a mayor's office, signs off on residential construction "
        f"({src('ocfl-horizonwest', 'Orange County, Horizon West')}; {src('orange-bldg', 'Orange County Division of Building Safety')}). That office is blunt about what triggers a permit: set a paver or pour a slab anywhere on a residential lot and paperwork is required, with pavers landing in a faster zoning review and poured concrete going through the fuller building process "
        f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}). {post('orange-county-orlando-driveway-patio-permits', 'Our Orange County permit guide')} covers how that compares to the incorporated cities nearby.</p>"),
    sec("One planning area, five villages, and a code with its own history",
        f"<p>Tally the villages, the Town Center and the greenbelt buffers the county wraps around them, and the special planning area comes to about 20,704 gross acres, with roughly 11,850 of those acres cleared for actual development "
        f"({src('ocfl-horizonwest', 'Orange County, Horizon West')}). The underlying zoning, the Horizon West Village Planned Development Code, dates to 1997 and has been updated twice since, in 2009 and 2014, and it governs five named Specific Area Plan villages, Lakeside Village, the Village of Bridgewater, and Villages H, F and I, along with the Town Center at the development's civic core "
        f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}).</p>"),
    sec("That same code decides whether a house even gets a front driveway",
        f"<p>Lot width, not homeowner preference, decides the layout: a lot 50 feet wide or narrower must use an alley-loaded garage under the county's design code, which routes the driveway to the rear lane instead of the street frontage, while a lot wider than 50 feet is allowed a conventional front-loaded garage "
        f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}). A {svc('concrete-driveways', 'concrete driveway')} or {svc('paver-driveways', 'paver driveway')} quote here starts with that lot-width number, since it decides whether the job is a short alley apron or a full front approach, well before anyone talks finish or thickness.</p>"),
    sec("The area's growth shows up first in its schools",
        f"<p>Horizon West counted about 14,000 residents at the 2010 Census, its first appearance as a Census-recognized place, and 58,101 by the 2020 Census, a jump of more than 300 percent in a decade "
        f"({ext(WIKI_HW_URL, 'Wikipedia, Horizon West, Florida')}). That pace hasn't let up: local school enrollment of 18,529 students outran the combined capacity of area campuses by the close of the 2024-25 school year, with Water Spring Elementary alone serving 1,071 students in a building designed for 725 "
        f"({ext(OVERCROWD_URL, 'Horizon West Happenings, school-year overcrowding report')}), which is why a new 834-seat elementary school on 15 acres off Hartzog Road is set to open in August 2026 specifically to take pressure off Water Spring and Panther Lake elementary "
        f"({ext(NEWSCHOOL_URL, NEWSCHOOL_LABEL)}). Families moving into a brand-new section here are, more often than in an older Orlando suburb, pouring a {svc('concrete-patios', 'patio')} or {svc('artificial-turf', 'turf lawn')} on ground that was still raw a year or two earlier.</p>"),
    sec("The design code reaches past the garage into porches and street-facing walls",
        f"<p>The same residential standards that set garage placement also require a front porch, at least 8 feet wide and 7 feet deep with three steps up from the sidewalk grade, on at least half the lots under 75 feet wide in a given village "
        f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}), and it limits how many homes on one block face can share the same front elevation. Those rules shape the house before a homeowner ever calls about a driveway or a backyard pour, but they're worth knowing going in, since a {svc('stamped-concrete', 'stamped walkway')} or entry apron is being laid against a streetscape the county already designed for variety.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is Horizon West a city, and who issues building permits there?",
        f"No. Horizon West is an unincorporated special planning area in southwest Orange County, so the county's own Division of Building Safety, not a city hall, reviews a driveway, patio or pool deck permit "
        f"({src('ocfl-horizonwest', 'Orange County, Horizon West')})."),
    faq("Why might a Horizon West house not have a front driveway at all?",
        "Lots 50 feet wide or narrower are required under the county's design code to use an alley-loaded garage, which puts the driveway at the rear of the lot off a service lane instead of the front street."),
    faq("How big is the Horizon West planning area?",
        "About 20,704 gross acres, with roughly 11,850 of those acres approved for development, spread across five villages and a Town Center southwest of Winter Garden and Windermere."),
    faq("Why are Horizon West's schools so crowded?",
        "The area's population grew more than 300 percent between the 2010 and 2020 Census counts, faster than new school construction could keep pace, which is why a new elementary school is opening in August 2026 specifically to relieve two of the most overcrowded campuses."),
    faq("How far is Horizon West from downtown Orlando?",
        f"About 16 miles, inside the territory the Orlando-unit crew covers alongside {city('windermere', 'Windermere')}, {city('winter-garden', 'Winter Garden')} and the rest of west Orange County."),
]

HUB = page("/horizon-west-fl/", "city", "Concrete, Pavers & Turf Contractor in Horizon West, FL",
           "Concrete, pavers and turf in Horizon West, FL: Orange County's lot-width garage code, the area's 300%-plus growth, and county permitting, October 2026.",
           "Concrete, Pavers and Artificial Turf for Horizon West Homes",
           capsule(f"Opera pours concrete and lays pavers and artificial turf across Horizon West, the roughly 20,704-acre unincorporated planning area about 16 miles southwest of downtown Orlando. "
                   f"A new driveway runs {price('concrete-driveway')} per {per('concrete-driveway')} this October 2026, and whether that driveway faces the street or a rear alley is set by a lot-width rule in the county's own design code, not by the builder's preference."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Horizon West",
           related=[("/central-florida/", "The Orlando-unit coverage area"),
                    ("/windermere-fl/", "Concrete, pavers and turf in Windermere"),
                    ("/winter-garden-fl/", "Concrete, pavers and turf in Winter Garden"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Orlando and Orange County permits"),
                    ("/blog/driveway-widening-and-extensions-florida/", "Widening or extending a driveway in Florida"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide")],
           eyebrow="Concrete · Pavers · Turf in Horizon West, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Horizon West, FL – Permits",
    "meta": "Concrete driveway installers in Horizon West, FL: the county's alley-loaded garage rule, lot-width thresholds, and the ROW apron spec, October 2026.",
    "h1": "Pouring a Concrete Driveway in Horizon West",
    "lede": capsule(f"A concrete driveway in Horizon West runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "Before square footage or finish come up, the county's own design code already decided whether the driveway faces the front street or a rear service lane, based on nothing more than how wide the lot is."),
    "sections": [
        ("A 50-foot line in the code decides the whole layout",
         f"<p>Orange County's residential design standards for Horizon West require an alley-loaded garage, and therefore a rear driveway off a service lane, on any lot 50 feet wide or narrower; a lot wider than that may use a conventional front-loaded garage instead, and anything under 65 feet in width is barred from a double-wide garage door regardless of which layout it uses "
         f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}). Narrower, alley-loaded lots end up with a shorter driveway run but a longer concrete section in back, which changes the arithmetic from what the same square-foot price would produce on a conventional front-facing lot.</p>"),
        ("Where the driveway still meets the right-of-way, the usual county spec applies",
         f"<p>On a front-loaded lot, the apron crossing into the right-of-way still has to meet Orange County's lot-grading standard, a minimum of 6 inches of 3,000 psi concrete, kept at least 3 feet off the property line "
         f"({src('orange-lot-grading', 'Orange County, Residential Lot Grading Policy 2023')}). Garage setbacks run at least 20 feet from the front property line under the village design code "
         f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}), which sets the maximum practical length of a front driveway on a lot wide enough to have one.</p>"),
    ],
    "scenario": ("An alley-loaded driveway on a narrow Horizon West lot, worked out in square feet",
                 f"<p>Picture a 45-foot-wide lot in one of Horizon West's newer villages, required under the lot-width rule to run its garage off the rear alley. A 14 by 22 foot driveway section connecting the garage to the lane, 308 square feet, prices out between roughly $1,850 and $4,620 at {price('concrete-driveway')} per {per('concrete-driveway')}, shorter than a comparable front-facing driveway would run but poured against the alley's own paving grade rather than the street's.</p>"),
    "faqs": [
        faq("Why would a Horizon West home have its driveway off an alley instead of the street?",
            "The county's residential design code requires an alley-loaded garage on any lot 50 feet wide or narrower, which puts the driveway at the back of the lot rather than the front."),
        faq("Does a wider Horizon West lot get to choose a front driveway?",
            "Yes. Lots wider than 50 feet may use a front-loaded garage, though lots under 65 feet wide are still barred from a double-wide garage door under the same code."),
        faq("What concrete spec applies where a Horizon West driveway meets the street?",
            "The same Orange County standard used countywide: at least 6 inches of 3,000 psi concrete across the right-of-way, kept a minimum of 3 feet off the property line."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Horizon West, FL – Design Code",
    "meta": "Paver driveway installers in Horizon West, FL: the county's driveway-placement rule for front-loaded garages, and the zoning permit, October 2026.",
    "h1": "Paver Driveways in Horizon West",
    "lede": capsule(f"A paver driveway in Horizon West runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026. "
                     "On the wider, front-loaded lots where a paver driveway is even an option, the county's own design code asks builders to stagger where that driveway sits relative to the house next door, so two identical paver layouts rarely sit side by side."),
    "sections": [
        ("A randomization rule most homeowners never hear about until they ask",
         f"<p>Orange County's design standards for Horizon West direct that front-loaded garages “should randomly alternate the location of driveways in relation to front façade,” a streetscape rule meant to keep a block from reading as a repeating row of identical driveway cuts "
         f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}). A {svc('paver-driveways', 'paver driveway')} replacement on an existing lot doesn't have to meet that standard again since the layout is already built, but it explains why neighboring driveways in the same village rarely line up the way they would in an older, more uniform subdivision.</p>"),
        ("The permit itself is the same lighter review used countywide",
         f"<p>Pavers go through Orange County's residential paver permit rather than the fuller review a poured driveway needs, with a $38 permit fee, a matching $38 Development Engineering review fee, and about 4 business days to turn around once a dimensioned site plan is submitted "
         f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). That same zoning code holds residential lots to a 40 percent minimum of private open space, a figure a wide paver driveway on a freshly built Horizon West lot has to leave room for.</p>"),
    ],
    "scenario": ("A front-loaded paver driveway sized against the open-space minimum, worked out in square feet",
                 f"<p>Say a 70-foot-wide lot in Lakeside Village, wide enough for a front-loaded garage, lays a 520 square foot paver driveway. At {price('paver-driveway')} per {per('paver-driveway')}, that runs roughly $6,240 to $15,600, and because the county's zoning code holds the lot to a 40 percent open-space floor, that 520 square feet gets checked against the porch, walkway and any rear patio before the final width is confirmed.</p>"),
    "faqs": [
        faq("Does Horizon West's design code control where a paver driveway sits on the lot?",
            "For new construction on front-loaded lots, yes; the county's design standards ask builders to vary driveway placement relative to the house next door rather than repeating the same layout down the block. A driveway replacement on an already-built lot isn't required to meet that rule again."),
        faq("What does Orange County charge for a paver driveway permit in Horizon West?",
            "The same countywide residential paver permit: a $38 permit fee plus a $38 Development Engineering review fee, typically reviewed within about 4 business days."),
        faq("Does a wide paver driveway in Horizon West have to leave room elsewhere on the lot?",
            "Generally yes. The county's zoning code sets residential private open space at a 40 percent minimum, so a wide driveway is weighed against the porch, walkway and any patio already using up that allowance."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Horizon West, FL – New Builds",
    "meta": "Concrete patio contractors in Horizon West, FL: extending off a required front porch, and pouring on freshly graded village lots, October 2026.",
    "h1": "Building a Concrete Patio in Horizon West",
    "lede": capsule(f"A concrete patio in Horizon West runs {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "Most homes here were required to be built with a real front porch under the county's own design code, so the backyard patio homeowners add later is often the first outdoor living space on a lot that came with porch square footage but no rear slab."),
    "sections": [
        ("The porch out front is required; the patio out back is not",
         f"<p>On at least half the lots under 75 feet wide in a given Horizon West village, the county's residential design standards require a front porch at least 8 feet wide and 7 feet deep, elevated at least three steps above the sidewalk "
         f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}). That porch covers the entry; it's not backyard living space, which is why a {svc('concrete-patios', 'rear patio')} is frequently the first slab a Horizon West homeowner adds after closing, rather than a feature the builder poured already.</p>"),
        ("A patio here is more often going over compacted fill from last year, not decades-old ground",
         f"<p>Horizon West's population grew from about 14,000 at the 2010 Census to 58,101 by 2020 "
         f"({ext(WIKI_HW_URL, 'Wikipedia, Horizon West, Florida')}), growth that keeps producing freshly platted streets where the subgrade under a new lot was engineered and compacted as part of the subdivision's own build-out within the past few years. On ground that recent, the pre-pour question is less about decades of settling and more about whether the compaction done for the house itself extends far enough into the patio footprint to be relied on without its own pass.</p>"),
    ],
    "scenario": ("A first patio added behind a required front porch, worked out in square feet",
                 f"<p>Picture a new Horizon West home with its required 8 by 7 foot front porch already in place, where the owners add a 240 square foot concrete patio off the back of the house for a grill and seating area. At {price('concrete-patio')} per {per('concrete-patio')}, that patio runs roughly $1,440 to $3,120, poured on a lot where the subdivision's own compacted fill is checked first rather than assumed to extend under the new slab.</p>"),
    "faqs": [
        faq("Do Horizon West homes come with a backyard patio already built?",
            "Not usually. The county's design code requires a front porch on most narrower lots, but that's entry space, not a backyard patio, so a rear slab is typically a homeowner addition after move-in."),
        faq("Why would a brand-new Horizon West lot need extra compaction work for a patio?",
            "Recently platted lots sit on fill and grading done as part of the subdivision's own build-out, which doesn't always extend fully into a backyard patio's footprint, so confirming the base under that specific area is worth doing before the pour."),
        faq("Is a permit required for a first patio addition in Horizon West?",
            "Yes. Orange County's standard rule applies to any new concrete poured on the lot, patio addition or not, and review runs through the county's Division of Building Safety."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Horizon West, FL",
    "meta": "Paver patio installers in Horizon West, FL: building across five villages and a Town Center still under construction, October 2026.",
    "h1": "Paver Patios and Walkways Across Horizon West's Villages",
    "lede": capsule(f"A paver patio in Horizon West runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "The planning area isn't one neighborhood but five separate villages plus a Town Center, and a backyard paver project can mean a different stage of build-out depending on which of those the lot sits in."),
    "sections": [
        ("Five villages, a civic core, and not all of it finished at once",
         f"<p>Horizon West's governing code organizes the area into five Specific Area Plan villages, Lakeside Village, the Village of Bridgewater, and Villages H, F and I, built around a Town Center meant as the development's commercial and civic hub "
         f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}). Lakeside Village, among the earliest built out, has streets where a {svc('paver-patios', 'paver patio')} job is more likely tying into an established yard, while a lot in one of the newer villages is more often starting from bare, recently graded ground.</p>"),
        ("Greenbelt buffers shape where a paver layout can run",
         f"<p>The county's own description of the planning area notes that its villages and Town Center sit surrounded by greenbelts "
         f"({src('ocfl-horizonwest', 'Orange County, Horizon West')}), conservation buffers built into the community's layout from the start rather than added piecemeal. A paver patio or walkway on a lot backing onto one of those greenbelts gets checked against the buffer line the same way a lot backing onto a pond would, before the layout is finalized.</p>"),
    ],
    "scenario": ("A paver patio and walkway combination on a newer village lot, worked out in square feet",
                 f"<p>Say a home in one of Horizon West's newer villages adds a 220 square foot paver patio plus a 50 square foot front walkway section tying into the required porch, 270 square feet combined. At {price('paver-patio')} per {per('paver-patio')}, that runs roughly $3,240 to $4,320, with the rear property line checked against any adjoining greenbelt buffer before the patio's final footprint is set.</p>"),
    "faqs": [
        faq("Are all of Horizon West's villages built out the same amount?",
            "No. Lakeside Village is among the area's earliest-built sections, while Villages F, H and I have newer construction still underway in parts, so a paver project can mean working with an established yard or a freshly graded one depending on the address."),
        faq("Does a greenbelt buffer limit a paver patio's layout in Horizon West?",
            "Where a lot backs onto one of the conservation greenbelts built into the villages, yes, the buffer line is checked the same way a pond or wetland edge would be before the patio's footprint is finalized."),
        faq("Is the Town Center area open for residential paver work yet?",
            "Much of the Town Center is still being built out as the planning area's commercial and civic core, so most residential paver patio work happens in the surrounding villages rather than in the Town Center itself."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Horizon West, FL",
    "meta": "Concrete pool deck builders in Horizon West, FL: keeping pace with one of Central Florida's fastest-growing areas, October 2026.",
    "h1": "Concrete Pool Decks for Horizon West's New Construction",
    "lede": capsule(f"A concrete pool deck in Horizon West runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} as of October 2026. "
                     "Population here more than quadrupled between the 2010 and 2020 Census counts, and that growth hasn't slowed enough to make an older, resurfaced deck the norm; most Horizon West pool decks are still going in alongside a pool that's just as new."),
    "sections": [
        ("Growth figures that explain why so much of the work here is first-time construction",
         f"<p>Horizon West had roughly 14,000 residents at the 2010 Census, its first count as a recognized place, and 58,101 by 2020, a gain of more than 300 percent in ten years "
         f"({ext(WIKI_HW_URL, 'Wikipedia, Horizon West, Florida')}), with the area's own population tracker now running closer to 69,000 "
         f"({ext(CENSUSREPORTER_HW_URL, 'Census Reporter, Horizon West, FL')}). A {svc('concrete-pool-decks', 'pool deck')} poured in that environment is far more often matched to a brand-new pool shell on a recently built lot than it is a replacement for a deck that's spent decades in the Florida sun.</p>"),
        ("Permitting runs through the same county desk regardless of how new the street is",
         f"<p>Even on a lot finished within the past year, the pool deck still goes through Orange County's Division of Building Safety under the standard unincorporated-county permit, not a separate new-construction fast track "
         f"({src('orange-bldg', 'Orange County Division of Building Safety')}). What differs is the subgrade conversation: a deck on a freshly graded Horizon West lot is usually checking whether the subdivision's own compaction extends into the pool area, rather than evaluating years of settling the way an older Orlando-area deck would.</p>"),
    ],
    "scenario": ("A new pool deck on a recently built Horizon West lot, worked out in square feet",
                 f"<p>Picture a newly closed home in one of Horizon West's active villages pouring a 650 square foot deck around a pool installed the same season as the house. At {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, that deck runs roughly $3,250 to $9,750 depending on the finish, from a plain broom texture to a decorative cool-touch surface, with the subdivision's own compacted fill checked under the deck footprint before the forms go up.</p>"),
    "faqs": [
        faq("Are most Horizon West pool decks new installs or replacements?",
            "Mostly new installs. With population more than quadrupling between the 2010 and 2020 Census counts, a larger share of the area's pool decks are going in alongside a newly built pool than are being resurfaced on an aging original."),
        faq("Does a new Horizon West subdivision get a faster permit process for a pool deck?",
            "No. The deck still goes through the same Orange County Division of Building Safety review as anywhere else in unincorporated Orange County, regardless of how recently the street was built."),
        faq("What changes about pool deck prep on a freshly built Horizon West lot?",
            "The main question becomes whether the subdivision's own grading and compaction work extends fully into the pool deck's footprint, rather than assessing years of soil settling the way an older deck replacement would."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Horizon West, FL",
    "meta": "Pool deck pavers in Horizon West, FL: keeping pace with the area's overcrowded schools and steady new-home pipeline, October 2026.",
    "h1": "Pool Deck Pavers for Horizon West Backyards",
    "lede": capsule(f"Pool deck pavers in Horizon West fall in the {price('pool-deck-pavers')} {per('pool-deck-pavers')} range as of October 2026. "
                     "The same growth that's kept local elementary schools running over capacity is filling Horizon West's villages with young families finishing a backyard for the first time, often with a paver deck rather than plain broom concrete."),
    "sections": [
        ("Overcrowded schools are a rough proxy for how many backyards are still unfinished",
         f"<p>By the close of the 2024-25 school year, Horizon West's local public schools were serving 18,529 students against a combined design capacity of 17,857, a 104 percent utilization rate, with Water Spring Elementary alone running at 148 percent of its intended enrollment "
         f"({ext(OVERCROWD_URL, 'Horizon West Happenings, school-year overcrowding report')}). That volume of young families moving in tracks closely with how much {svc('pool-deck-pavers', 'pool deck')} work in the area is a first install rather than a resurfacing job on an older deck.</p>"),
        ("A new school opening in 2026 is itself a sign of how fast new construction keeps arriving",
         f"<p>A new 834-seat elementary school on 15 acres off Hartzog Road is set to open in August 2026, built specifically to relieve Water Spring and Panther Lake elementary schools "
         f"({ext(NEWSCHOOL_URL, NEWSCHOOL_LABEL)}). A new public school of that size going up is the kind of infrastructure that only gets built where enough new rooftops, and the pools and paver decks that come with them, are already filling in behind it.</p>"),
    ],
    "scenario": ("A new paver pool deck sized for a first-time backyard build-out, worked out in square feet",
                 f"<p>Say a family in one of Horizon West's growing villages finishes a 500 square foot travertine pool deck around a newly installed pool, the first hardscape project on the lot since closing. At {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, that deck runs roughly $6,000 to $15,000 depending on the paver material chosen, priced the same whether the lot sits in an established village or one still filling in.</p>"),
    "faqs": [
        faq("Why mention school overcrowding on a pool deck page?",
            "It's a useful stand-in for how many Horizon West families are newly moved in and still finishing a backyard. The same growth straining local elementary schools is behind a steady volume of first-time pool deck installs rather than resurfacing work."),
        faq("Is a new school opening nearby a sign that more homes are being built?",
            "Generally, yes. A public school built for 834 new students, like the one opening in Horizon West in August 2026, typically follows the rooftops rather than leading them."),
        faq("Does pool deck paver pricing differ between Horizon West's older and newer villages?",
            "No. The market price range is the same across the area; what differs is whether the job is tying into an established yard or starting on a lot finished within the past year or two."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Horizon West, FL – Street Rules",
    "meta": "Stamped concrete contractors in Horizon West, FL: the county's block-face variety rule and the walkway every narrow lot must have, October 2026.",
    "h1": "Stamped Concrete Driveways and Walkways in Horizon West",
    "lede": capsule(f"Stamped concrete in Horizon West falls in the {price('stamped-concrete')} {per('stamped-concrete')} range as of October 2026, set by the pattern and the number of colors chosen. "
                     "Unlike a typical Orlando-area subdivision, the county's own design code already limits how many identical-looking homes can sit on one block, which makes a stamped pattern a real way to set an entry walk or driveway apart rather than just a cosmetic upgrade."),
    "sections": [
        ("A rule against repetition, written into the zoning code itself",
         f"<p>Orange County's residential design standards for Horizon West cap any given block face at five homes sharing the same front elevation, and require homes with matching façades to be separated by at least two lots with a different look "
         f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}). A {svc('stamped-concrete', 'stamped')} driveway apron or front walk in a distinct pattern or color plays into that same variety the county is already requiring at the architectural level, even though the code itself only regulates the house, not the hardscape.</p>"),
        ("Narrower lots are required to lead visitors to the door on foot",
         f"<p>On any lot 60 feet wide or less, the design code requires a visible primary entrance connected to the public sidewalk by its own pedestrian walkway "
         f"({ext(ARCH_GUIDE_URL, 'Orange County Planning Division, Horizon West Architectural Design Standards Guidebook')}), a walkway that's a natural candidate for a stamped finish since it's a required, highly visible part of the house's street presence rather than a backyard feature nobody but the homeowner sees.</p>"),
    ],
    "scenario": ("A stamped entry walk on a narrow village lot, worked out in square feet",
                 f"<p>Picture a 55-foot-wide Horizon West lot where the required pedestrian walkway to the sidewalk, 4 feet wide and 25 feet long, 100 square feet, gets finished in a stamped slate pattern with a single integral color to match the porch columns. At the {price('stamped-concrete')} per {per('stamped-concrete')} range, that walkway runs roughly $1,200 to $1,900, a small share of the lot's overall hardscape but one that's required to exist under the county's own entrance rule.</p>"),
    "faqs": [
        faq("Does Horizon West's design code limit matching driveways and entries on the same block?",
            "It regulates the house's front elevation directly, capping any block face at five homes with the same façade and requiring at least two different-looking homes between repeats, which indirectly encourages varied driveway and entry treatments as well."),
        faq("Is a front walkway required on every Horizon West lot?",
            "On lots 60 feet wide or less, yes. The design code requires a visible primary entrance connected to the public sidewalk by its own pedestrian walkway."),
        faq("Does a stamped pattern change the county's review of a Horizon West driveway or walkway?",
            "No. The permit and the underlying slab spec stay the same regardless of finish; the county's architectural variety rules apply to the house itself, not to the stamped pattern chosen for the concrete."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Horizon West, FL – Water Setback",
    "meta": "Artificial turf installers in Horizon West, FL: the state's 10-foot setback across a village layout built around stormwater ponds, October 2026.",
    "h1": "Artificial Turf for Horizon West Yards",
    "lede": capsule(f"Artificial turf in Horizon West runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "Every village here was planned with greenbelts and stormwater ponds built in from the start rather than added later, so the state's water-body setback for turf comes up on a larger share of lots than it would in an older, less engineered subdivision."),
    "sections": [
        ("A layout built around water from day one",
         f"<p>Orange County describes Horizon West's villages and Town Center as surrounded by greenbelts "
         f"({src('ocfl-horizonwest', 'Orange County, Horizon West')}), and that conservation-and-stormwater framework means retention ponds and buffer strips run through the community at a density an older, piecemeal-built suburb doesn't usually have. Florida's rule for synthetic turf still applies the same way regardless: at least 10 feet back from a pond, lake or canal, unless a seawall forms that edge, with no buried irrigation underneath and a washed-stone base instead "
         f"({src('dep-rule', 'the DEP turf rule')}).</p>"),
        ("A newer lot means measuring the pond edge fresh, not relying on an old survey",
         f"<p>On a lot finished within the past year or two, the pond or swale edge nearby was shaped as part of the subdivision's own stormwater design, so the 10-foot line is worth measuring directly off the current grading rather than assumed from a plat drawing that predates the final landscaping. As of 2026, state law also limits a homeowners association to restricting {svc('artificial-turf', 'turf')} only where it's visible from the street or an adjoining lot "
         f"({src('fs720-3045', 'F.S. 720.3045')}).</p>"),
    ],
    "scenario": ("Backyard turf set back from a village retention pond, worked out in square feet",
                 f"<p>Say a home in one of Horizon West's newer villages backs onto a stormwater pond and wants to replace 420 square feet of new sod that's struggled to take hold with turf instead. Pulling the layout back the required 10 feet from the pond's edge trims the usable area to roughly 370 square feet, which at {price('artificial-turf')} per {per('artificial-turf')} runs between about $3,700 and $9,250 depending on pile height and backing.</p>"),
    "faqs": [
        faq("Are more Horizon West lots near water than in an older Orlando subdivision?",
            "Proportionally, yes. The area's villages were planned with greenbelts and stormwater ponds built into the layout from the start, so a larger share of lots sit within reach of a water body than in an older suburb built without that kind of integrated stormwater design."),
        faq("Does a newly graded pond edge in Horizon West need to be re-measured for turf setback?",
            "It's worth it. A pond or swale shaped as part of a subdivision's recent build-out can differ slightly from an older plat drawing, so measuring the 10-foot setback off the current grading avoids relying on an outdated line."),
        faq("Can a Horizon West HOA still restrict artificial turf under state law?",
            "Only turf that's actually visible from the street frontage or an adjoining lot, as of 2026. That's on top of, not instead of, the state's own 10-foot water-body setback and installation standard."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
