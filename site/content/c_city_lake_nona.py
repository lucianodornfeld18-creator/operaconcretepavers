# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "lake-nona"

NORTHLAKE_ARC_URL = "https://www.lelandmanagement.com/community-portal/content/menu-item/14212"
NORTHLAKE_ABOUT_URL = "https://lakenona.com/neighborhoods/northlake-park/"
WATERATLAS_URL = "https://orange.wateratlas.usf.edu/waterbodies/lakes/140353/lake-nona"
DOWDEN_URL = "https://www.clickorlando.com/news/local/2026/03/17/orlando-approves-380-acre-development-district-in-lake-nona/"
WIKI_LN_URL = "https://en.wikipedia.org/wiki/Lake_Nona,_Orlando,_Florida"

SRC = [
    "orlando-engineering-permit", "orlando-esm", "orlando-res-requirements", "orlando-hb803-guide",
    "orlando-row-permit", "lakenona-about", "laureatepark-faq", "dep-rule", "fs125572", "fs720-3045",
    "sjrwmd-watering",
    ("NorthLake Park at Lake Nona, Community Portal (ARC approval)", NORTHLAKE_ARC_URL),
    ("Lake Nona, NorthLake Park neighborhood page", NORTHLAKE_ABOUT_URL),
    ("Orange County Water Atlas, Lake Nona", WATERATLAS_URL),
    ("ClickOrlando, Dowden Central CDD approval", DOWDEN_URL),
    ("Wikipedia, Lake Nona, Orlando, Florida", WIKI_LN_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Lake Nona has no city hall of its own",
        f"<p>Lake Nona isn't a separate municipality; it sits inside the Orlando city limits, so the same Permitting Services Division that reviews a driveway downtown reviews one here, through the engineering permit rather than a building permit "
        f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}). A handful of clauses in the city's construction manual matter more on a community built mostly from scratch: no single-family driveway may sit inside an intersection's radius return, a curb opening can't run more than 3 feet wider than the driveway on either side, and anywhere a driveway crosses a sidewalk or bike path the slope tops out at 2 percent "
        f"({src('orlando-esm', 'City of Orlando, Engineering Standards Manual §8.11')}). {post('orange-county-orlando-driveway-patio-permits', 'How that permit works, county by county')} covers the surrounding jurisdictions.</p>"),
    sec("Four areas carry the Lake Nona name, not one",
        f"<p>Lake Nona is marketed as a single 17-square-mile community, developed by Tavistock Development Company "
        f"({src('lakenona-about', 'Lake Nona, About')}), but it's built out in distinct sections: Lake Nona Central around VillageWalk and the USTA National Campus, Lake Nona Estates around the Golf & Country Club, Lake Nona South around Medical City and Laureate Park, and NorthLake Park around Morningside and Waters Edge "
        f"({ext(WIKI_LN_URL, 'Wikipedia, Lake Nona, Orlando, Florida')}). A {svc('concrete-driveways', 'driveway')} or {svc('concrete-pool-decks', 'pool deck')} quote in one of those sections often runs into a different homeowners' association review than the one next door, so which village a lot sits in matters before the city's own permit is even filed.</p>"),
    sec("NorthLake Park: one of the community's first neighborhoods, and its own sign-off",
        f"<p>NorthLake Park sits on 500 acres at the community's northernmost point and is described by its own developer as “one of Lake Nona's first neighborhoods” "
        f"({ext(NORTHLAKE_ABOUT_URL, 'Lake Nona, NorthLake Park neighborhood page')}). Homeowners there “MUST obtain ARC approval prior to any work being started,” and the community's management portal warns that a modification made outside the guidelines can mean extra cost later to bring the property back into compliance "
        f"({ext(NORTHLAKE_ARC_URL, 'NorthLake Park at Lake Nona, Community Portal')}). Other villages run a comparable review under their own association; in Laureate Park it's the Master Association's architectural board, reached by email before a permit is filed "
        f"({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}).</p>"),
    sec("The lake the community is named for sets the water-body math",
        f"<p>Lake Nona is a real, 587-acre lake inside Orange County's Lake Hart Watershed, tracked under waterbody ID 3171D with water-quality samples going back to 1972 "
        f"({ext(WATERATLAS_URL, 'Orange County Water Atlas, Lake Nona')}). Add in the stormwater ponds built throughout the community's newer phases and a lot here is more likely than most Orlando addresses to sit within reach of a water body, which matters directly for {svc('artificial-turf', 'artificial turf')}: the city won't permit it within 50 feet of one, tighter than the state's 10-foot baseline "
        f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}; {src('dep-rule', 'DEP Rule 62-308.100')}).</p>"),
    sec("Still under construction: a new district approved for roads and drainage",
        f"<p>In March 2026, Orlando's city commission approved the Dowden Central Community Development District, covering nearly 380 acres in the southeast part of the city within the broader Lake Nona area, built specifically to put in roads, drainage systems, utilities and parks ahead of new homes "
        f"({ext(DOWDEN_URL, 'ClickOrlando, Dowden Central CDD approval')}). That infrastructure gets paid for through assessments on the district's own property, not a citywide tax, and it's a reminder that parts of Lake Nona are still being graded and platted rather than sitting on decades-old lots; {svc('concrete-slabs', 'a new slab')} or driveway going in on one of those freshly built streets is poured on recently engineered fill, not undisturbed native ground.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is Lake Nona its own city with its own permit office?",
        f"No. Lake Nona is a community inside the City of Orlando, so a driveway, patio or pool deck there goes through the same Permitting Services Division and engineering permit that covers the rest of the city, not a separate town hall "
        f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')})."),
    faq("Does every Lake Nona neighborhood have the same HOA rules?",
        "No. Lake Nona is made up of distinct villages, NorthLake Park, Laureate Park, Lake Nona Estates and others, each generally run by its own homeowners' association or architectural review board, so the approval process for a driveway or pool deck can differ from one street to the next."),
    faq("How far is Lake Nona from downtown Orlando?",
        f"About 14 miles from the center of Orlando, which the Orlando-unit crew reaches directly alongside {city('orlando', 'Orlando')} itself, {city('st-cloud', 'St. Cloud')} and the rest of Osceola and Orange County."),
    faq("Why does a lake matter for an artificial turf project in Lake Nona?",
        "Because the community sits around a real 587-acre lake plus a network of stormwater ponds, more lots here are within reach of a water body than in a typical Orlando neighborhood. The city keeps turf at least 50 feet from any water body, tighter than the state's 10-foot standard."),
    faq("Is Lake Nona still being built out?",
        "Parts of it, yes. Orlando approved a new community development district covering almost 380 acres in the area in March 2026, specifically to build roads, drainage and utilities ahead of new construction, which is why some Lake Nona streets sit on recently placed fill rather than long-settled ground."),
]

HUB = page("/lake-nona-fl/", "city", "Concrete, Pavers & Turf Contractor in Lake Nona, FL",
           "Concrete, pavers and turf in Lake Nona, Orlando, FL: City of Orlando permits, four HOA-reviewed villages, and the 587-acre lake's turf setback, October 2026.",
           "Concrete, Pavers and Artificial Turf for Lake Nona Homes",
           capsule(f"Opera pours concrete and lays pavers and artificial turf for Lake Nona, a roughly 17-square-mile community inside the City of Orlando, about 14 miles from downtown. "
                   f"A new driveway falls in the {price('concrete-driveway')} {per('concrete-driveway')} market range this October, reviewed under Orlando's own engineering permit, with most Lake Nona villages adding a homeowners' association review of their own."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Lake Nona",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
                    ("/st-cloud-fl/", "Concrete, pavers and turf in St. Cloud"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Orlando and Orange County permits"),
                    ("/blog/hoa-approval-for-pavers-and-concrete/", "Getting HOA approval for pavers and concrete"),
                    ("/pool-deck-cost/", "Pool deck cost guide")],
           eyebrow="Concrete · Pavers · Turf in Lake Nona, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Lake Nona, FL – Permits",
    "meta": "Concrete driveway installers in Lake Nona, FL: Orlando's engineering permit, curb-opening and intersection clauses, and new-build fill, October 2026.",
    "h1": "Pouring a Concrete Driveway in Lake Nona",
    "lede": capsule(f"A concrete driveway in Lake Nona runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026, the same Orlando-wide market range. "
                     "Because Lake Nona sits inside Orlando, the driveway goes through the city's engineering permit, and because much of the community is recently built, the subgrade under a new pour is often engineered fill rather than native flatwoods soil."),
    "sections": [
        ("An engineering permit, with a couple of clauses that matter here specifically",
         f"<p>Orlando's Permitting Services Division reviews a Lake Nona driveway exactly the way it reviews one anywhere else in the city, as an engineering permit rather than a building permit "
         f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}). Two clauses in the city's construction manual come up more often on a newer grid of streets like this one: no single-family driveway can sit inside an intersection's radius return, and a curb opening can't exceed the driveway's own width by more than 3 feet on either side "
         f"({src('orlando-esm', 'City of Orlando, Engineering Standards Manual §8.11')}). The 2026 state exemption for work under $7,500 doesn't reach this engineering review "
         f"({src('orlando-hb803-guide', 'the HB 803 exemption guide')}).</p>"),
        ("New-construction lots mean a different subgrade conversation",
         f"<p>A Lake Nona address built within the past few years often sits on ground that was graded, filled and compacted as part of a CDD-funded subdivision build-out rather than left as undisturbed native soil "
         f"({ext(DOWDEN_URL, 'ClickOrlando, Dowden Central CDD approval')}). That changes the pre-pour conversation: on an older Orlando lot the question is usually how deep the original fill goes, while on a freshly platted Lake Nona street it's whether the engineered base under the road extends far enough into the driveway apron to be relied on, or whether the driveway's own subgrade needs its own compaction pass.</p>"),
    ],
    "scenario": ("A new-construction driveway in a Lake Nona village, worked out in square feet",
                 f"<p>Say a newly built single-family home in one of Lake Nona's newer phases pours a 20 by 20 foot driveway, 400 square feet, as part of the original build rather than a later replacement. At {price('concrete-driveway')} per {per('concrete-driveway')}, that lands between roughly $2,400 and $6,000 before any builder-grade upgrade such as a broom border or a wider apron at the street. "
                 "On a corner lot near one of the community's newer intersections, the driveway's placement also has to clear the radius-return rule before the layout is finalized.</p>"),
    "faqs": [
        faq("Does Lake Nona have its own driveway permit process separate from Orlando?",
            "No. Lake Nona sits inside the Orlando city limits, so the same engineering permit and Permitting Services Division that reviews a driveway anywhere else in the city reviews one here."),
        faq("Why would a new Lake Nona driveway need extra subgrade work if the lot was just built?",
            "Recently platted streets sit on fill and compaction work tied to the subdivision's own build-out, which doesn't always extend fully into the driveway apron itself, so a site check confirms the base under the slab is compacted on its own before pouring."),
        faq("Can a driveway be placed anywhere on a Lake Nona corner lot?",
            "Not quite. Orlando's construction manual bars a single-family driveway from sitting inside an intersection's radius return, a rule that comes up more often on Lake Nona's newer corner lots than on older, established blocks."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Lake Nona, FL – HOA Review",
    "meta": "Paver driveway installers in Lake Nona, FL: NorthLake Park's ARC rule, Orlando's engineering permit, and village-by-village review, October 2026.",
    "h1": "Paver Driveways in Lake Nona",
    "lede": capsule(f"A paver driveway in Lake Nona runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026. "
                     "The city's engineering permit covers the material the same way it covers plain concrete, but in villages such as NorthLake Park, a color or paver change needs the neighborhood association's sign-off before the city application even goes in."),
    "sections": [
        ("NorthLake Park's rule: approval first, work second",
         f"<p>In NorthLake Park, one of the community's first neighborhoods, homeowners “MUST obtain ARC approval prior to any work being started,” and skipping that step risks a modification violation that can cost more to fix after the fact than it would have to clear beforehand "
         f"({ext(NORTHLAKE_ARC_URL, 'NorthLake Park at Lake Nona, Community Portal')}). A paver driveway replacement, a color swap or widening an existing apron all count as the kind of exterior change that rule is written to catch, separate from whatever the city's own engineering permit requires.</p>"),
        ("The city doesn't treat pavers more lightly than poured concrete",
         f"<p>Orlando reviews a paver driveway under the identical engineering permit it uses for concrete, which is a heavier process than unincorporated Orange County applies to the same material "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). On a Lake Nona lot, that city review runs alongside, not instead of, whichever village's architectural board also has to sign off, so a homeowner is generally clearing two separate approvals rather than one.</p>"),
    ],
    "scenario": ("Replacing a paver driveway in an established Lake Nona village, worked out in square feet",
                 f"<p>Picture a home in one of Lake Nona's earlier-built sections relaying 480 square feet of driveway, a single-car-plus-guest-parking layout, in a different paver color than the original. Pricing that out at {price('paver-driveway')} {per('paver-driveway')} puts the job somewhere between $5,760 and $14,400, with the paver choice and base depth moving the number within that band, and the neighborhood's own architectural review typically scheduled before the crew's start date is confirmed.</p>"),
    "faqs": [
        faq("Does a paver driveway in Lake Nona need HOA approval even if the city already permits it?",
            "In villages such as NorthLake Park, yes. The city's engineering permit and the neighborhood's own architectural review are two separate approvals, and starting work before the HOA signs off can mean a modification violation."),
        faq("Does switching from concrete to pavers change the city permit process in Lake Nona?",
            "No. Orlando reviews pavers under the same engineering permit category it uses for poured concrete, rather than a lighter process the way unincorporated Orange County does."),
        faq("Do all Lake Nona neighborhoods run the same architectural review?",
            "No. NorthLake Park, Laureate Park and other villages each run their own association, so the specific approval steps and timelines for a paver driveway can differ from one Lake Nona street to the next."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Lake Nona, FL – Builder Lots",
    "meta": "Concrete patio contractors in Lake Nona, FL: adding onto a builder-grade lanai, Orlando's engineering permit, and village drainage, October 2026.",
    "h1": "Building a Concrete Patio in Lake Nona",
    "lede": capsule(f"A concrete patio in Lake Nona runs {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "A lot of homes here were sold with a small builder-grade lanai slab, so the most common patio job isn't new construction from bare ground; it's extending that original pour into a full-size patio."),
    "sections": [
        ("Extending a builder slab is still new permit work",
         f"<p>A patio addition, even one that ties into an existing builder-poured lanai, goes through the same engineering permit the city applies to a driveway or a fresh slab "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). Because many Lake Nona homes are recent construction, the original builder's slab and the new extension don't always share a control-joint layout, which is why we plan the joint pattern across both sections rather than treating the addition as a stand-alone pour.</p>"),
        ("Drainage has to work with a community built around stormwater ponds",
         f"<p>Lake Nona's newer sections are laid out around a network of engineered stormwater ponds feeding the 587-acre lake the community is named for "
         f"({ext(WATERATLAS_URL, 'Orange County Water Atlas, Lake Nona')}). A patio extension's slope has to keep pushing runoff toward the yard's existing drainage path rather than redirecting it, since those ponds are sized for a planned flow pattern across the whole subdivision, not just one lot's convenience.</p>"),
    ],
    "scenario": ("Extending a builder-grade lanai into a full patio, worked out in square feet",
                 f"<p>Say a Lake Nona home's original 10 by 10 foot builder lanai, 100 square feet, gets extended by another 150 square feet to make room for an outdoor dining set. At {price('concrete-patio')} per {per('concrete-patio')}, the 150 square foot addition lands between roughly $900 and $1,950, with the existing slab's control joints checked first so the new pour ties in cleanly rather than cracking along the seam.</p>"),
    "faqs": [
        faq("Does extending a builder-grade lanai in Lake Nona need its own permit?",
            "Yes, the addition is reviewed under the same engineering permit as any new patio or slab, even though it connects to concrete the builder already poured."),
        faq("Why do Lake Nona patios often start as a small builder slab?",
            "Many homes here were sold with a basic lanai pad rather than a full patio, since the community is newer construction overall, so adding on later is a common first hardscape project rather than an unusual one."),
        faq("Does a patio's drainage matter more in a community built around ponds?",
            "It's worth checking more carefully. Lake Nona's stormwater system is engineered around the whole subdivision's runoff pattern, so a patio's slope should continue feeding that same drainage path rather than pooling water against the house or a neighboring yard."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Lake Nona, FL",
    "meta": "Paver patio installers in Lake Nona, FL: Laureate Park's review board, Orlando's engineering permit, and Medical City-area lots, October 2026.",
    "h1": "Paver Patios and Walkways Around a Lake Nona Home",
    "lede": capsule(f"A paver patio in Lake Nona runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "In Laureate Park, the Lake Nona South village built around Medical City, the Master Association reviews a new patio by email before the city's engineering permit moves forward."),
    "sections": [
        ("Laureate Park's board reviews the layout before the city does",
         f"<p>Laureate Park's Master Association requires its Architectural Review Board to sign off on property improvements, submitted by email, ahead of construction "
         f"({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}). That review sits on top of Orlando's own engineering permit, which covers paver patios under the same category as concrete and asphalt citywide "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). A homeowner there typically has both approvals in motion before ordering material rather than starting the city process alone.</p>"),
        ("Medical City's newer lots change what a walkway connects to",
         f"<p>Lake Nona South, where Laureate Park sits, is built around the Medical City district "
         f"({ext(WIKI_LN_URL, 'Wikipedia, Lake Nona, Orlando, Florida')}), and homes there tend to back onto a narrower band of yard than an older Orlando subdivision, with alley-loaded garages common across the village. A front paver walkway often has to route around a narrower side-yard setback than it would on a larger, older lot elsewhere in the city, which is a detail worth confirming on the survey before the layout is drawn.</p>"),
    ],
    "scenario": ("A Laureate Park patio and walkway combination, worked out in square feet",
                 f"<p>Say a Laureate Park home adds a 200 square foot paver patio off the back of the house plus a 60 square foot front walkway section, 260 square feet combined. At {price('paver-patio')} per {per('paver-patio')}, that lands between roughly $3,120 and $4,160, with the Master Association's email approval typically running in parallel with the city's engineering permit rather than adding a separate waiting period beforehand.</p>"),
    "faqs": [
        faq("Does Laureate Park require approval for a new paver patio?",
            "Yes. The Master Association's Architectural Review Board reviews property improvements, submitted by email, separate from and in addition to Orlando's engineering permit."),
        faq("Are Lake Nona lots in Medical City's area smaller than elsewhere in Orlando?",
            "Often, yes, particularly in alley-loaded sections of Laureate Park, where a narrower side yard can shape how a front walkway or patio extension is laid out compared with an older, larger Orlando lot."),
        faq("Can the HOA review and the city permit for a Lake Nona patio happen at the same time?",
            "Generally yes. Submitting the Master Association's request by email and filing the city's engineering permit are separate processes that can move in parallel rather than one waiting on the other to finish first."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Lake Nona, FL",
    "meta": "Concrete pool deck builders in Lake Nona, FL: Lake Nona Estates' golf-course lots, Orlando's permit, and the 50-ft water setback, October 2026.",
    "h1": "Concrete Pool Decks for Lake Nona Homes",
    "lede": capsule(f"A concrete pool deck in Lake Nona runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} as of October 2026. "
                     "In Lake Nona Estates, the village built around the Golf & Country Club, a new pool deck often backs directly onto a fairway, which adds a sightline and drainage conversation that a landlocked lot elsewhere in the community doesn't need."),
    "sections": [
        ("A golf-course lot changes the grading plan",
         f"<p>Lake Nona Estates is laid out around the community's Golf & Country Club "
         f"({ext(WIKI_LN_URL, 'Wikipedia, Lake Nona, Orlando, Florida')}), and a pool deck on one of its course-fronting lots has to grade away from both the house and the course itself, since fairway irrigation and turf maintenance equipment both cross that boundary regularly. The deck still goes through the same engineering permit the city applies to any slab "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}), with the survey noting the course boundary alongside the usual property lines.</p>"),
        ("New pools, not aging ones, make up most of the work here",
         f"<p>Lake Nona's population grew from roughly 1,500 residents in 2000 to more than 50,000 by 2015 "
         f"({ext(WIKI_LN_URL, 'Wikipedia, Lake Nona, Orlando, Florida')}), growth that shows up today as a steady stream of first-time pool decks rather than resurfacing jobs on worn-out originals. A newly poured deck here is more often being matched to a brand-new pool shell and a fresh landscape plan than being patched into decades of prior settling.</p>"),
    ],
    "scenario": ("A new pool deck on a Lake Nona Estates course lot, worked out in square feet",
                 f"<p>Say a home backing onto the Golf & Country Club course pours an 800 square foot deck around a new pool, with extra grading built in to keep irrigation runoff off the fairway side. At {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, that lands between roughly $4,000 and $12,000 depending on the finish, from a basic broom texture to a decorative cool-touch surface.</p>"),
    "faqs": [
        faq("Does a pool deck on a golf-course lot in Lake Nona need special grading?",
            "Generally yes. A deck backing onto the Golf & Country Club's fairway has to grade away from both the house and the course boundary, since irrigation and maintenance equipment cross that line regularly."),
        faq("Are most Lake Nona pool decks new construction or repairs?",
            "Mostly new construction. The community's rapid population growth since 2000 means a larger share of its pools and decks are first installs rather than resurfacing work on an aging original."),
        faq("What permit covers a new pool deck in Lake Nona?",
            "The same engineering permit Orlando uses for a driveway or patio slab anywhere else in the city, filed through the Permitting Services Division."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Lake Nona, FL",
    "meta": "Pool deck pavers in Lake Nona, FL: matching a paver choice to a village's architectural review, and the community's own lake, October 2026.",
    "h1": "Pool Deck Pavers for Lake Nona Backyards",
    "lede": capsule(f"Pool deck pavers in Lake Nona fall in the {price('pool-deck-pavers')} {per('pool-deck-pavers')} range as of October 2026. "
                     "Because almost every village here runs its own architectural review, the paver color and material get checked against a neighborhood's design standard before the city's engineering permit is the limiting factor."),
    "sections": [
        ("Color and material clear the HOA before the city permit matters",
         f"<p>Across Lake Nona's villages, an exterior change, a pool deck among them, typically needs the resident's own association to review the plan first: NorthLake Park requires approval “prior to any work being started” "
         f"({ext(NORTHLAKE_ARC_URL, 'NorthLake Park at Lake Nona, Community Portal')}), and Laureate Park's Master Association reviews the same category of change by email "
         f"({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}). The city's own engineering permit for the deck itself is a second, separate step "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}).</p>"),
        ("A lake-adjacent lot keeps the turf rule in mind even for a paver project",
         f"<p>Where a pool deck sits near the 587-acre lake the community takes its name from, or one of the stormwater ponds feeding it "
         f"({ext(WATERATLAS_URL, 'Orange County Water Atlas, Lake Nona')}), the paver deck itself isn't restricted by the city's water-body setback the way {svc('artificial-turf', 'artificial turf')} is, but any turf planned alongside the deck has to stay the required 50 feet back, a detail worth confirming on the same site visit that plans the paver layout.</p>"),
    ],
    "scenario": ("A paver pool deck near Lake Nona itself, worked out in square feet",
                 f"<p>Say a home within sight of the lake pours a 700 square foot paver pool deck, with a strip of turf planned along one side of the yard. At {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, the deck lands between roughly $8,400 and $21,000 depending on the paver, and the turf strip gets measured separately to confirm it clears the 50-foot water-body setback before it's added to the same project.</p>"),
    "faqs": [
        faq("Do pool deck pavers in Lake Nona need HOA approval?",
            "In most villages, yes, the paver color and material typically go to the neighborhood's own architectural board before or alongside the city's engineering permit."),
        faq("Does being near Lake Nona's own lake restrict a paver pool deck?",
            "Not the paver deck itself; the city's 50-foot water-body setback applies specifically to artificial turf, not to pavers or concrete, though it's worth checking if turf is planned as part of the same project."),
        faq("How long does HOA review usually take for a Lake Nona pool deck?",
            "It varies by village and isn't published as a fixed number of days, which is why we confirm each association's own review timeline before setting a construction schedule."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Lake Nona, FL – HOA Review",
    "meta": "Stamped concrete contractors in Lake Nona, FL: why pattern and color changes go to the village's architectural board, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Lake Nona",
    "lede": capsule(f"Stamped concrete in Lake Nona falls in the {price('stamped-concrete')} {per('stamped-concrete')} range as of October 2026, set by the pattern and the number of colors used. "
                     "With no historic district here the way parts of older Orlando have, the review that actually governs a stamped pattern or integral color is each village's own architectural board, not a city preservation rule."),
    "sections": [
        ("No historic district, but a design review all the same",
         f"<p>Lake Nona isn't inside one of Orlando's designated historic preservation districts, so a stamped pattern or color change here doesn't need a Certificate of Appropriateness the way one in an older downtown neighborhood would "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}). What takes its place is the village's own review: in NorthLake Park, any exterior work, a new pattern or color on a driveway included, needs approval before the crew starts "
         f"({ext(NORTHLAKE_ARC_URL, 'NorthLake Park at Lake Nona, Community Portal')}).</p>"),
        ("The same engineering permit applies regardless of finish",
         f"<p>Whether the concrete is plain gray or a multi-color stamped pattern, Orlando's engineering permit covers the slab the same way "
         f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}). On a newer Lake Nona street, that permit is filed alongside, not instead of, the village's design approval, so a stamped driveway upgrade on an existing home typically clears two reviews rather than the one a brand-new build goes through as part of its original construction.</p>"),
    ],
    "scenario": ("Upgrading a builder-grade driveway to stamped concrete, worked out in square feet",
                 f"<p>Picture a home in one of Lake Nona's established villages resurfacing a plain 320 square foot driveway in a stamped slate pattern. Working from the {price('stamped-concrete')} {per('stamped-concrete')} range puts the total somewhere between $3,840 and $7,680, with the number of integral colors chosen moving the bid within that spread, and the village's architectural board reviewing the color before the city's engineering permit is filed for the resurfacing.</p>"),
    "faqs": [
        faq("Does Lake Nona have a historic district that restricts stamped concrete colors?",
            "No. Lake Nona isn't inside one of Orlando's designated historic preservation districts, so a stamped pattern or color change doesn't trigger the Certificate of Appropriateness those districts require."),
        faq("Who reviews a stamped concrete color change in Lake Nona if not a historic board?",
            "Each village's own homeowners' association or architectural review board typically reviews exterior changes like a new driveway pattern or color, separate from the city's engineering permit for the concrete work itself."),
        faq("Does a stamped finish cost more to permit than plain concrete in Lake Nona?",
            "No, the city's engineering permit treats the slab the same regardless of finish. Any added review comes from the village's own architectural board, not from the city charging differently for a decorative pattern."),
    ],
    "sources": SRC,
}

# 8. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Lake Nona, FL – Water Setback",
    "meta": "Artificial turf installers in Lake Nona, FL: the 50-foot water-body setback near the community's lake and ponds, October 2026.",
    "h1": "Artificial Turf for Lake Nona Yards",
    "lede": capsule(f"Artificial turf in Lake Nona runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "Because the community is built around a 587-acre lake and a network of stormwater ponds, the city's 50-foot water-body setback for turf comes up on more Lake Nona lots than it would in a typical Orlando neighborhood."),
    "sections": [
        ("Water is closer than it looks on a typical Lake Nona lot",
         f"<p>Lake Nona itself covers 587 acres and sits inside Orange County's Lake Hart Watershed, with the community's newer villages laced with smaller stormwater ponds that feed into it "
         f"({ext(WATERATLAS_URL, 'Orange County Water Atlas, Lake Nona')}). Orlando's own rule keeps artificial turf at least 50 feet from any water body, tighter than the state Department of Environmental Protection's 10-foot baseline that applies where a city hasn't set something stricter "
         f"({src('orlando-res-requirements', 'City of Orlando, Residential Permitting Requirements')}; {src('dep-rule', 'DEP Rule 62-308.100')}). A lot backing onto one of the community's ponds needs that distance measured before a turf layout is finalized, not assumed.</p>"),
        ("HOA visibility rules stack on top of the city's setback",
         f"<p>Most Lake Nona villages also require their own sign-off on an exterior change like a turf lawn, on top of the city's distance rule, and under state law as of 2026 an HOA can only restrict turf that's actually visible from the street frontage or an adjoining lot "
         f"({src('fs720-3045', 'F.S. 720.3045')}). A 2025 state law otherwise limits how far a local government can go in regulating residential turf beyond the standard DEP already sets "
         f"({src('fs125572', 'F.S. 125.572')}).</p>"),
    ],
    "scenario": ("Backyard turf near a Lake Nona stormwater pond, worked out in square feet",
                 f"<p>Say a home backing onto one of Lake Nona's retention ponds replaces 450 square feet of struggling sod with artificial turf, keeping the new lawn's edge measured back from the water. At {price('artificial-turf')} per {per('artificial-turf')}, that lands between roughly $4,500 and $11,250 depending on the pile height and backing, with the 50-foot setback checked against the pond's edge before the layout is finalized rather than the property line alone.</p>"),
    "faqs": [
        faq("How close to Lake Nona's lake or ponds can artificial turf be installed?",
            "No closer than 50 feet under Orlando's own rule, which applies to the community's namesake lake as well as the smaller stormwater ponds built throughout its newer villages."),
        faq("Is the water-body setback for turf different in Lake Nona than elsewhere in Orlando?",
            "The rule itself is the same citywide 50-foot standard, but it comes up more often in Lake Nona because the community has more water features, the lake plus its stormwater ponds, within reach of a typical lot."),
        faq("Does a Lake Nona HOA need to approve turf even where the city allows it?",
            "Usually yes. Most villages review exterior changes including a new turf lawn, and as of 2026 state law limits an HOA to restricting turf that's visible from the street or an adjoining property."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
