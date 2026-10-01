# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "osprey"

CENSUS_OSPREY_URL = "http://censusreporter.org/profiles/16000US1253425-osprey-fl/"
WIKI_OSPREY_URL = "https://en.wikipedia.org/wiki/Osprey,_Florida"
WIKI_HSP_URL = "https://en.wikipedia.org/wiki/Historic_Spanish_Point"
SELBY_HSP_URL = "https://selby.org/hsp/visit-historic-spanish-point/"
WIKI_OSCAR_URL = "https://en.wikipedia.org/wiki/Oscar_Scherer_State_Park"

SRC = [
    "sarasota-county-row-permit", "sarasota-county-98-3-culvert-row-fees", "sarasota-county-124-255-culverts",
    "sarasota-county-124-76-rsf-standards", "sarasota-county-124-283-nonconforming-isr", "sarasota-county-22-63-retaining-walls",
    "sarasota-county-online-permitting", "sarasota-county-building-page",
    "fema-coastal-firm", "fdep-cccl-program", "swfwmd-restrictions", "fdot-sdg", "fl-senate-2011-104",
    "nrcs-eaugallie-osd", "nrcs-immokalee-osd", "nrcs-pomello-osd", "dep-rule", "fs125572", "fs720-3045", "palmerranch",
    ("Census Reporter, Osprey CDP, FL (ACS 2020-2024 5-yr, B01003/B25035)", CENSUS_OSPREY_URL),
    ("Wikipedia, Osprey, Florida", WIKI_OSPREY_URL),
    ("Wikipedia, Historic Spanish Point", WIKI_HSP_URL),
    ("Selby Gardens, Visit Historic Spanish Point", SELBY_HSP_URL),
    ("Wikipedia, Oscar Scherer State Park", WIKI_OSCAR_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Since Osprey isn't its own city, who actually signs off on a driveway or patio?",
        "<p>There's no Osprey town hall to file with. The community sits entirely in unincorporated Sarasota County, so every " + cs("osprey", "concrete-driveways", "driveway pour") + ", " +
        cs("osprey", "paver-patios", "patio") + " or pool-deck job here goes through the County's Building Division rather than a municipal office. Any work touching the public right-of-way "
        "needs its own Right-of-Way Use Permit under the county's land development code, worded broadly enough to cover the apron, the culvert and the swale together " +
        src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ". Filing happens through the county's own online system " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") +
        ", and a search-cached look at the county's building page suggests a straight driveway repair that leaves the culvert alone might not need that review at all, a point worth a phone call "
        "to confirm rather than assume " + src("sarasota-county-building-page", "Sarasota County Building") + ".</p>"
    ),
    sec(
        "What has to happen before a culvert pipe goes in along a county right-of-way?",
        "<p>Osprey's lots, like most of unincorporated Sarasota County, drain to a roadside swale rather than a storm sewer, so the pipe crossing under a driveway gets its own permit category, "
        "separate from the slab or pavers above it " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ".</p>"
        + table(
            "What Sarasota County's §124-255 sets for a residential culvert",
            ["Item the County Engineer checks", "What the code requires"],
            [
                ["How long the pipe runs", "20 ft at the short end, 24 ft at the long end, stretching further only on a deeper-than-standard ditch"],
                ["What the pipe is made of", "Reinforced or asphalt-coated corrugated metal, or an alternate the County Engineer accepts in writing"],
                ["Who sets the line and grade", "The County Engineer, before the driveway's own forms go up"],
                ["Where paving may not go", "Inside a drainage easement, for a driveway, walkway or any other paved surface"],
            ],
            "Checked against Sarasota County Code §124-255 in October 2026 " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + "."
        )
    ),
    sec(
        "How does Osprey's lot-coverage math change between an older platted street and a newer one?",
        "<p>Most of Osprey's RSF-zoned ground caps the house itself at 35 percent building coverage, a number that leaves the driveway, patio or pool deck entirely out of the count "
        + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". A parcel still carrying its original RMF plat from on or before November 11, 1975 answers to a different, "
        "stricter rule instead: 50 percent impervious coverage, counting the roof, pool, pool deck and any concrete, asphalt or paver surface, while leaving grass and shell out of the total "
        + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ". " + svc("concrete-patios", "A concrete patio") + " addition on one of those older parcels is worth "
        "checking against that 1975 cutoff before a number gets quoted.</p>"
    ),
    sec(
        "What do Historic Spanish Point and Oscar Scherer State Park say about how old this ground is?",
        "<p>Pioneer John Greene Webb settled his family on Little Sarasota Bay in 1867, and the 30-acre site that grew around that homestead, Historic Spanish Point, became the first property in "
        "Sarasota County listed on the National Register of Historic Places, added on April 16, 1975 " + ext(WIKI_HSP_URL, "Wikipedia, Historic Spanish Point") + ", and now operates as a companion "
        "campus of Marie Selby Botanical Gardens " + ext(SELBY_HSP_URL, "Selby Gardens, Visit Historic Spanish Point") + ". Just south, Oscar Scherer State Park covers 1,400 acres between Sarasota and "
        "Venice, including the 3-acre Lake Osprey, and a 1992 expansion added 922 of those acres straight from the adjoining Palmer Ranch specifically to protect habitat for the Florida scrub jay "
        + ext(WIKI_OSCAR_URL, "Wikipedia, Oscar Scherer State Park") + ". That neighboring Palmer Ranch describes itself as more than 90 subdivisions and assisted-living communities spread across "
        "roughly 60 square miles " + src("palmerranch", "Palmer Ranch Master Association") + ", and the Blackburn Point Bridge, a one-lane span over the Intracoastal Waterway, carries its own "
        "National Register listing where it crosses from Osprey toward Casey Key " + ext(WIKI_OSPREY_URL, "Wikipedia, Osprey, Florida") + ".</p>"
    ),
    sec(
        "How does Osprey's housing age and population compare with the rest of the Sarasota unit?",
        "<p>Census Reporter's current five-year estimate counts 5,943 residents in the Osprey CDP, with the median home here dated to 1998 " + ext(CENSUS_OSPREY_URL, "Census Reporter, Osprey CDP") +
        ", a full two decades newer than the typical home in neighboring " + city("nokomis", "Nokomis") + ". That later build-out means fewer original driveways are nearing failure here than in an "
        "older Sarasota County community, though a late-1990s " + svc("concrete-driveways", "driveway") + " or " + svc("concrete-pool-decks", "pool deck") + " is now old enough that resurfacing "
        "calls are becoming routine rather than rare.</p>"
    ),
    sec(
        "What do the area's flatwoods soils and the retaining-wall rule mean for a build here?",
        "<p>Three sandy flatwoods series dominate Osprey's subgrade: EauGallie and Immokalee, both prone to standing close to grade for a stretch of the year, and Pomello, somewhat better drained "
        "at 18 to 48 inches down " + src("nrcs-eaugallie-osd", "NRCS OSD EauGallie") + " " + src("nrcs-immokalee-osd", "NRCS OSD Immokalee") + " " + src("nrcs-pomello-osd", "NRCS OSD Pomello") + ". Knowing "
        "which one sits under a given lot is why a crew builds the compacted base to the wetter end of spec rather than defaulting to a ridge-sand minimum that wouldn't hold up here. A wall standing "
        "taller than 4 feet anywhere along its run, "
        "measured from the lower grade, needs engineered drawings under the county's own pool-code amendment before construction starts " + src("sarasota-county-22-63-retaining-walls", "Sarasota County Code §22-63") +
        ", a rule that comes up often on a Little Sarasota Bay lot holding back fill near the water. A 2010 legislative review of statewide sinkhole insurance claims left Sarasota County off "
        "its roster of the hardest-hit counties entirely " + src("fl-senate-2011-104", "Florida Senate Interim Report 2011-104") + ", which points toward that shallow water table, not karst "
        "below the surface, as the usual explanation for a dip near an Osprey driveway's edge.</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Does Osprey have its own permitting office?",
        "No town office exists for Osprey specifically; it's unincorporated ground, so every application, from a driveway to a retaining wall, lands on Sarasota County's desk, filed through the county's own online system rather than a counter in Osprey itself."
    ),
    faq(
        "Does a culvert permit apply to most Osprey driveways?",
        "Most lots drain to a roadside swale rather than a storm sewer, so yes, a culvert crossing that swale typically needs its own permit under the county's code, reviewed apart from the driveway's surface material."
    ),
    faq(
        "Is Osprey's housing newer than other Sarasota County communities?",
        "On average, yes. The area's median home dates to 1998, noticeably newer than several neighboring unincorporated communities, though pockets platted decades earlier still exist and answer to the county's older nonconforming-lot rules."
    ),
    faq(
        "How do you find the best concrete contractor for an Osprey address?",
        "Run the contractor through the state's license lookup, and beyond that, ask two pointed questions a generic bid often skips: has this crew pulled a Sarasota County culvert permit before, and does the proposal name a specific soil series rather than a generic base depth. " +
        post("how-to-choose-a-concrete-contractor-sarasota", "Our contractor guide") + " covers the rest."
    ),
    faq(
        "Does the current watering order change sod or turf decisions in Osprey?",
        "Yes. Sarasota County falls entirely under SWFWMD's Modified Phase III shortage order, in effect through March 31, 2027, limiting irrigation to one assigned day a week. New sod gets a short daily-watering start; artificial turf needs no watering schedule at all once installed."
    ),
]

HUB = page(
    "/osprey-fl/", "city",
    "Concrete, Paver & Turf Contractor in Osprey, FL",
    "Concrete, pavers and turf for unincorporated Osprey, FL: Sarasota County's culvert and coverage rules, Oscar Scherer State Park and flatwoods soil, October 2026.",
    "Building Driveways, Patios and Turf in Osprey",
    capsule(
        "Osprey is an unincorporated Sarasota County community of about 5,943 residents on Little Sarasota Bay, between Historic Spanish Point and Oscar Scherer State Park. As of October 2026, "
        "the county's Building Division reviews every driveway, patio and pool-deck permit here, and a culvert crossing the roadside swale needs its own right-of-way sign-off before the slab is poured."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Osprey",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/nokomis-fl/", "Concrete, pavers and turf in Nokomis"),
        ("/sarasota-fl/", "Concrete, pavers and turf in Sarasota"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Osprey, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Osprey, FL – Culvert Permit",
    "meta": "Concrete driveway installers in Osprey, FL: Sarasota County's §124-255 culvert spec and swale rules; market range " + price("concrete-driveway") + " per " + per("concrete-driveway") + ".",
    "h1": "Pouring a Concrete Driveway in Unincorporated Osprey",
    "lede": capsule(
        "A concrete driveway in Osprey costs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. Osprey answers to Sarasota County rather than a town "
        "building department, and wherever the drive crosses the roadside swale, a culvert permit has to clear before the slab goes in."
    ),
    "sections": [
        (
            "The swale crossing is its own review, not an add-on",
            "<p>County code treats the pipe beneath an Osprey driveway as a distinct permit category from the surface above it. The material has to be reinforced or asphalt-coated corrugated "
            "metal, or an alternative the County Engineer signs off on, and the pipe itself has to fall between 20 and 24 feet long, stretching further only where the ditch is cut deeper than "
            "standard " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ". A drainage easement, separately, is off-limits to any paved surface at all, driveway or "
            "walkway alike " + src("sarasota-county-124-255-culverts") + ".</p>"
        ),
        (
            "Filing goes to the county, not a local office",
            "<p>There's no Osprey building counter to visit; the county's own online portal is the only filing route, the same one that handles the broader Right-of-Way Use Permit for work placed "
            "in the county's right-of-way " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + " " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") +
            ". A driveway repair that doesn't disturb the culvert pipe itself may clear faster under the county's own guidance, a point we still confirm by phone rather than assume on every job "
            + src("sarasota-county-building-page", "Sarasota County Building") + ".</p>"
        ),
    ],
    "scenario": (
        "Replacing a late-1990s driveway near Little Sarasota Bay, worked out in square feet",
        "<p>An 18 by 36 foot driveway, 648 square feet, sits on an Osprey lot built around the area's 1998 median, with the original culvert pipe showing enough corrosion to need replacing at the "
        "same time. Pricing the slab at " + price("concrete-driveway") + " per " + per("concrete-driveway") + " runs $3,888 to $9,720, narrowing to roughly $5,184 to $7,776 inside the typical " +
        price("concrete-driveway", typical=True) + " band. Because the old pipe is being swapped out, the job carries both a culvert permit and the driveway permit together, with the County "
        "Engineer setting the replacement pipe's grade before either gets poured.</p>"
    ),
    "faqs": [
        faq(
            "What pipe length does Sarasota County require for an Osprey driveway culvert?",
            "The standard range runs 20 to 24 feet, and that upper figure only climbs when the swale itself has been cut deeper than the county's typical section calls for."
        ),
        faq(
            "Can an Osprey driveway cross a drainage easement?",
            "No. The county's rule is categorical on this point: a driveway, walkway or any other paved surface simply can't occupy a drainage easement, full stop, no matter how the rest of the lot is configured."
        ),
        faq(
            "Does a simple driveway patch in Osprey need a culvert permit?",
            "Not always. Leaving the pipe itself untouched can simplify the review, but calling the Building Division ahead of time is the only way to know for certain on a given address."
        ),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Osprey, FL – Coverage & ROW",
    "meta": "Paver driveway installers in Osprey, FL: the county's nonconforming-lot coverage math on older parcels; market range " + price("paver-driveway") + " per " + per("paver-driveway") + ".",
    "h1": "Paver Driveway Installation Near Osprey",
    "lede": capsule(
        "A paver driveway near Osprey runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. On most RSF-zoned lots the paving itself doesn't count against "
        "any coverage limit, but an older, pre-1975 parcel answers to a tighter rule where every square foot of paver adds to the total."
    ),
    "sections": [
        (
            "Why the plat date decides the paving math",
            "<p>Sarasota County's RSF standard caps building coverage, the house footprint alone, at 35 percent, leaving a paver driveway's own square footage out of that particular count "
            + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ". A parcel still carrying its original plat from on or before November 11, 1975 instead faces a 50 "
            "percent impervious ceiling that names pavers directly, alongside concrete and asphalt, while exempting grass and shell " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") +
            ". Checking which rule a given Osprey lot falls under comes before quoting a driveway expansion, not after.</p>"
        ),
        (
            "The right-of-way review doesn't change with the surface",
            "<p>Whether the finish is poured concrete or pavers, Sarasota County's Right-of-Way Use Permit requirement covers 'all work' in its rights-of-way without a separate track for either "
            "material " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ", and where the drive crosses the swale, the culvert permit under §124-255 applies the identical way "
            "it would to a concrete pour " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ".</p>"
        ),
    ],
    "scenario": (
        "Widening a paver driveway on an older Osprey parcel, worked out in square feet",
        "<p>A homeowner on a lot platted in the early 1970s near Little Sarasota Bay wants to widen a single-car paver driveway to two cars, adding 340 square feet to an existing 280, for "
        "620 total. At " + price("paver-driveway") + " per " + per("paver-driveway") + ", the full job prices between $6,200 and $18,600, tightening to about $7,440 to $12,400 inside the typical "
        + price("paver-driveway", typical=True) + " band. Because the lot predates the 1975 cutoff, the added square footage gets weighed against the county's 50 percent impervious ceiling "
        "before the final layout is approved, something a newer RSF-zoned lot down the street wouldn't have to do.</p>"
    ),
    "faqs": [
        faq(
            "Does a paver driveway count toward my Osprey lot's coverage limit?",
            "On a standard RSF lot, no, since that rule measures building footprint only. On a parcel platted on or before November 11, 1975, yes, since the county's nonconforming rule names pavers directly in its 50 percent impervious-coverage count."
        ),
        faq(
            "Is the right-of-way permit different for pavers versus concrete in Osprey?",
            "No. The county's Right-of-Way Use Permit requirement applies to all work in its rights-of-way regardless of surface material, so a paver driveway and a poured one face the same review."
        ),
        faq(
            "How do I find out if my Osprey lot is pre-1975?",
            "The county's property records show the original plat date, which decides whether the lot answers to the 35 percent building-only cap or the stricter 50 percent impervious-coverage rule for older parcels."
        ),
    ],
    "sources": SRC,
}

# 3. concrete-patios -------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Osprey, FL – Flatwoods Base",
    "meta": "Concrete patio contractors in Osprey, FL: building the subgrade over EauGallie and Pomello flatwoods soil; market range " + price("concrete-patio") + " per " + per("concrete-patio") + ".",
    "h1": "Building a Concrete Patio in Osprey",
    "lede": capsule(
        "A concrete patio near Osprey costs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. The sandy flatwoods soil under most of the area keeps a seasonal "
        "high water table close enough to grade that drainage, not just the finish, decides how the slab performs over time."
    ),
    "sections": [
        (
            "What EauGallie and Pomello soils mean for a patio's base",
            "<p>The two sandy series that turn up most often under an Osprey patio behave differently underground: EauGallie's wetness peaks closer to the surface, while Pomello generally "
            "doesn't saturate until well below typical slab depth " + src("nrcs-eaugallie-osd", "NRCS OSD EauGallie") + " " + src("nrcs-pomello-osd", "NRCS OSD Pomello") + ". Whichever one a "
            "soil boring turns up, a patio on the wetter ground calls for extra compacted fill graded to push water toward the yard rather than the house, a step that a dry ridge-sand lot "
            "never has to budget for.</p>"
        ),
        (
            "Whether a small patio needs its own permit here",
            "<p>A cached summary of the county's building guidance suggests an on-grade patio without footings may fall outside the standard permit requirement, though the source page itself "
            "returned an access error when checked directly, so we confirm that with the Building Division on each project instead of assuming it holds " + src("sarasota-county-building-page", "Sarasota County Building") +
            ". " + svc("concrete-pool-decks", "A pool deck") + " addition on the same lot gets that identical confirm-first treatment.</p>"
        ),
    ],
    "scenario": (
        "A patio addition off a 1990s Osprey lanai, worked out in square feet",
        "<p>A 300 square foot patio extension goes in off the back of a home built close to the area's 1998 median, on ground that tests out as EauGallie fine sand with water sitting close "
        "enough to the surface to call for a deeper compacted base. At " + price("concrete-patio") + " per " + per("concrete-patio") + ", the job runs $1,800 to $3,900, settling near $2,100 to "
        "$3,000 inside the typical " + price("concrete-patio", typical=True) + " range for a broom finish. The extra base depth adds modestly to the labor but not to the concrete volume itself, "
        "since the added material is compacted aggregate rather than additional slab thickness.</p>"
    ),
    "faqs": [
        faq(
            "Does an Osprey patio need a deeper base than usual?",
            "Often, on ground that tests out as EauGallie, since that particular series is prone to wetness close to grade for a stretch of the year, which calls for extra compacted fill under the slab."
        ),
        faq(
            "Is Pomello soil drier than EauGallie around Osprey?",
            "Yes. Pomello's seasonal high water table sits 18 to 48 inches down, noticeably deeper than EauGallie's, so a patio on Pomello ground typically needs less extra base preparation."
        ),
        faq(
            "Does a small on-grade Osprey patio need a permit?",
            "A secondary summary of county guidance suggests one without footings may be exempt, but since the county's own page couldn't be verified directly, we confirm current practice with the Building Division before pricing a job as permit-free."
        ),
    ],
    "sources": SRC,
}

# 4. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Osprey, FL – Bay-Area Lots",
    "meta": "Paver patio installers in Osprey, FL: easement rules near Little Sarasota Bay and the county's coverage math; market range " + price("paver-patio") + " per " + per("paver-patio") + ".",
    "h1": "Paver Patios and Walkways Near Osprey",
    "lede": capsule(
        "A paver patio near Osprey runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. On a lot reaching toward Little Sarasota Bay, a path's route matters as "
        "much as its square footage, since a paved surface can't cross a drainage easement on its way to the water."
    ),
    "sections": [
        (
            "Routing a walkway around the easement, not through it",
            "<p>Sarasota County's culvert code bars any walkway, driveway or other paved surface from occupying a drainage easement outright " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") +
            ", a rule that comes up on an Osprey lot where the shortest line from the patio to the dock crosses exactly that kind of easement. A path that stays on private ground skips the "
            "county's Right-of-Way Use Permit review, but one reaching toward the street doesn't " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ".</p>"
        ),
        (
            "Where the new paving lands on the coverage ledger",
            "<p>A paver patio on a standard RSF lot doesn't touch the county's 35 percent building-coverage cap, since that figure counts the house alone " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") +
            ". On a pre-1975 platted parcel, the same square footage counts directly toward the stricter 50 percent impervious limit instead " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") +
            ". " + svc("concrete-walkways", "A concrete walkway") + " on that older lot runs into the identical ceiling.</p>"
        ),
    ],
    "scenario": (
        "A paver patio and path near Little Sarasota Bay, worked out in square feet",
        "<p>A 310 square foot paver patio and connecting path goes in behind an Osprey home a few lots from Little Sarasota Bay, routed to avoid a drainage easement that runs along the rear "
        "property line. At " + price("paver-patio") + " per " + per("paver-patio") + ", that prices between $3,100 and $5,270, narrowing to roughly $3,720 to $4,960 inside the typical " +
        price("paver-patio", typical=True) + " band. Keeping the layout clear of the easement adds a bend to the path's route rather than a straight shot, a tradeoff the county's own rule "
        "makes non-negotiable on this particular lot.</p>"
    ),
    "faqs": [
        faq(
            "Can a paver path cross a drainage easement on an Osprey lot?",
            "No. County code specifically bars any paved surface, a walkway included, from sitting inside a drainage easement, which sometimes means routing the path around it rather than straight through."
        ),
        faq(
            "Does a paver patio need a right-of-way permit in Osprey?",
            "Only the portion that reaches into the county's right-of-way does. A patio or walkway kept entirely on private ground doesn't trigger that particular review."
        ),
        faq(
            "Does a paver patio count against an older Osprey lot's coverage limit?",
            "It can, specifically on ground still carrying its pre-1975 plat, where the county's impervious-surface math catches every paved square foot. A current RSF lot's cap only reaches the house footprint, leaving the patio's own area untouched by that calculation."
        ),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Osprey, FL – Bay Flood Zones",
    "meta": "Concrete pool deck builders in Osprey, FL: FEMA flood categories near Little Sarasota Bay and the coverage rule; range " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + ".",
    "h1": "Concrete Pool Deck Installation in Osprey",
    "lede": capsule(
        "A concrete pool deck in Osprey runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. Grading the slab to drain toward the yard rather than "
        "toward Little Sarasota Bay or a neighboring lot takes as much planning here as the finish does, especially on ground that sits over a wet flatwoods soil series."
    ),
    "sections": [
        (
            "Slope and soil matter before the flood map even gets checked",
            "<p>A fair share of Osprey sits on EauGallie or Immokalee flatwoods, both prone to a water table that creeps toward the surface for part of most years " +
            src("nrcs-eaugallie-osd", "NRCS OSD EauGallie") + " " + src("nrcs-immokalee-osd", "NRCS OSD Immokalee") + ". A pool deck poured on either series needs a pitch steep enough to carry "
            "runoff away from the house and off toward an approved drainage point rather than letting it sheet across a flat yard, a detail that matters whether or not the parcel ever shows up "
            "inside a FEMA flood boundary.</p>"
        ),
        (
            "Where Little Sarasota Bay adds a second layer of review",
            "<p>A deck going in on a lot fronting Little Sarasota Bay carries whatever FEMA designation that stretch of shoreline has been assigned, Zone AE's roughly one-percent flood chance "
            "or the tougher Coastal High Hazard Zone VE " + src("fema-coastal-firm", "FEMA's coastal flood-map guidance") + ", on top of the drainage and coverage questions every Osprey lot "
            "faces regardless of its distance from open water. " + svc("pool-deck-pavers", "A paver overlay") + " on that same bay-front parcel answers to the identical flood check.</p>"
        ),
    ],
    "scenario": (
        "Grading a deck on EauGallie soil away from a neighbor's yard",
        "<p>A 480 square foot pool deck is going in around a cage on an Osprey lot that tests out as EauGallie fine sand, with the rear property line sitting a few feet lower than the "
        "house pad. Pricing the pour at " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " works out to $2,400 and $7,200, landing near $3,360 to $5,760 inside the "
        "typical " + price("concrete-pool-deck", typical=True) + " band for a textured, slope-to-drain finish. The low rear line means the slope gets engineered to route water toward an "
        "approved swale on the side yard instead of straight across the property line, a fix that costs more in planning time than in concrete.</p>"
    ),
    "faqs": [
        faq(
            "Why does soil matter so much for an Osprey pool deck?",
            "A good share of the area sits on EauGallie or Immokalee flatwoods, both of which hold water close to the surface for part of most years, which affects how steeply a deck has to be pitched to actually shed water rather than pond on it."
        ),
        faq(
            "How do I know if my Osprey pool deck lot is in a flood zone?",
            "Pulling up the address on FEMA's map viewer settles it. Lots along Little Sarasota Bay often fall into Zone AE or the higher-risk Zone VE, while many inland Osprey addresses carry no coastal flood designation at all."
        ),
        faq(
            "Does an Osprey pool deck need a state coastal permit?",
            "Only where the lot reaches toward the Gulf side of the barrier islands and crosses Florida's Coastal Construction Control Line. Most Little Sarasota Bay and inland Osprey lots don't cross that particular line."
        ),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ----------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Osprey, FL – Bay Salt Air",
    "meta": "Pool deck pavers and travertine in Osprey, FL: FDOT's marine-chloride threshold near Little Sarasota Bay; market range " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + ".",
    "h1": "Travertine and Paver Pool Decks in Osprey",
    "lede": capsule(
        "Pool deck pavers or travertine in Osprey run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. Being a short walk from Little Sarasota Bay "
        "matters more to how a sealed surface ages here than how far the lot sits from the Gulf itself."
    ),
    "sections": [
        (
            "A bay-front material classification, not just a beachfront one",
            "<p>The yardstick FDOT's bridge engineers use for a corrosive marine setting is a chemistry reading, not a view of the Gulf: water testing above 2,000 parts per million chloride "
            "within 2,500 feet of the structure " + src("fdot-sdg") + ", a number that reaches well past the barrier islands into bay-front Osprey streets along Little Sarasota Bay. That "
            "classification leaves the paver base and bedding sand spec exactly as they'd be inland, but it's a fair signal that joint sand and a sealer coat won't last as long here as the "
            "identical job set a mile back from the water.</p>"
        ),
        (
            "Where a bigger overlay lands on an older lot's coverage total",
            "<p>Expanding a pool deck in pavers or travertine on a parcel platted on or before November 11, 1975 adds that new square footage straight to the county's 50 percent impervious "
            "ceiling, the same rule that names pool decks and paved surfaces directly " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ". A newer RSF lot "
            "skips that particular math entirely, since its 35 percent cap only reaches the house footprint " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ".</p>"
        ),
    ],
    "scenario": (
        "A travertine overlay on a bay-adjacent Osprey deck, worked out in square feet",
        "<p>A 480 square foot concrete pool deck two streets from Little Sarasota Bay is getting a travertine overlay on a lot that's also still carrying its original 1970s plat. Pricing the "
        "overlay at " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " comes to $5,760 and $14,400, tightening to about $6,720 to $10,560 inside the typical " +
        price("pool-deck-pavers", typical=True) + " range once the stone grade is chosen. Because the lot predates 1975, the new overlay's footprint gets checked against the nonconforming "
        "coverage ceiling before the number gets quoted, a step a newer lot across town wouldn't need.</p>"
    ),
    "faqs": [
        faq(
            "Does bay-front Osprey count as a marine environment for pavers?",
            "Under FDOT's own engineering standard, yes, within about 2,500 feet of water carrying more than 2,000 parts per million chloride, a boundary that reaches well past the barrier islands into bay-front neighborhoods."
        ),
        faq(
            "Does a pool deck paver overlay need a county permit in Osprey?",
            "Yes, the same building-permit review that applies to the original deck applies to a paver or travertine overlay over it, regardless of whether the stone sits on new concrete or an older slab."
        ),
        faq(
            "Does an overlay on an older Osprey lot affect its coverage limit?",
            "On a parcel platted on or before November 11, 1975, yes, since the overlay's square footage adds to the county's 50 percent impervious-coverage total that names pool decks directly."
        ),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -------------------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Osprey, FL – Newer Subdivisions",
    "meta": "Stamped concrete contractors in Osprey, FL: pattern choices for the area's late-1990s subdivisions; market range " + price("stamped-concrete") + " per " + per("stamped-concrete") + ", Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Osprey",
    "lede": capsule(
        "Expect " + price("stamped-concrete") + " per " + per("stamped-concrete") + " for stamped concrete in Osprey this October. Because so much of the area's housing wasn't built until the "
        "late 1990s, a stamped driveway or walk here is more often a fresh design choice than a rescue job over failing original concrete."
    ),
    "sections": [
        (
            "A later build-out shifts the typical stamped-concrete call",
            "<p>Osprey's median year of construction lands at 1998, Census Reporter's current estimate shows, a full two decades past where " + city("nokomis", "Nokomis") + " sits on the same "
            "measure " + ext(CENSUS_OSPREY_URL, "Census Reporter, Osprey CDP") + ". A homeowner here is more likely to be picking a stamp pattern for a driveway going in on bare ground than "
            "choosing an overlay to hide forty years of hairline cracking, the kind of call that's far more common a few miles away in an older platted community.</p>"
        ),
        (
            "The finish on top doesn't excuse the review underneath",
            "<p>Choosing a stamp pattern over a plain broom finish changes nothing about what the county checks: the §124-48 right-of-way permit still applies wherever the driveway meets the "
            "street " + src("sarasota-county-row-permit", "Sarasota County UDC §124-48") + ", and on ground still carrying its pre-1975 plat, the new surface's square footage counts toward "
            "the 50 percent impervious ceiling exactly as a plain pour would " + src("sarasota-county-124-283-nonconforming-isr", "Sarasota County Code §124-283") + ". " +
            svc("concrete-driveways", "A plain concrete driveway") + " on the same lot clears that identical pair of checks.</p>"
        ),
    ],
    "scenario": (
        "A stamped driveway on a newer Osprey subdivision lot, worked out in square feet",
        "<p>A 24 by 22 foot stamped driveway, 528 square feet, is going in fresh on a lot built close to the area's 1998 median, replacing nothing and starting from bare ground. At " +
        price("stamped-concrete") + " per " + per("stamped-concrete") + ", the project prices between $4,224 and $10,032, settling closer to $6,336 to $8,448 inside the typical " +
        price("stamped-concrete", typical=True) + " band once color count and pattern are picked. Since the lot is well inside the county's post-1975 RSF rule, the new stamped surface doesn't "
        "add to any coverage calculation, leaving the pattern choice free of any permitting consequence beyond the usual right-of-way review at the street.</p>"
    ),
    "faqs": [
        faq(
            "Is stamped concrete usually a new feature or a repair in Osprey?",
            "Lean toward new. The area's housing stock runs younger than most of its Sarasota County neighbors, so a fresh design on bare ground comes up more often than rescuing a cracked original driveway with an overlay."
        ),
        faq(
            "Does a stamped driveway face a different permit process in Osprey?",
            "No. The same Right-of-Way Use Permit and, where applicable, culvert review apply regardless of whether the finish is plain concrete, stamped concrete or pavers."
        ),
        faq(
            "Does stamped concrete count differently toward coverage on a newer Osprey lot?",
            "No differently than plain concrete would. A standard RSF lot's 35 percent cap only measures the house footprint, so neither finish choice affects that particular limit."
        ),
    ],
    "sources": SRC,
}

# 8. artificial-turf --------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Osprey, FL – Scrub Habitat Nearby",
    "meta": "Artificial turf installers in Osprey, FL: the state's 10-foot water-buffer rule near Little Sarasota Bay; market range " + price("artificial-turf") + " per " + per("artificial-turf") + ".",
    "h1": "Artificial Turf for Osprey Yards",
    "lede": capsule(
        "Artificial turf in Osprey costs " + price("artificial-turf") + " per " + per("artificial-turf") + " as of October 2026. Yards backing to Little Sarasota Bay or a residential canal "
        "have to clear the state's water-buffer condition first, a step a yard bordering Oscar Scherer State Park's uplands doesn't face at all."
    ),
    "sections": [
        (
            "The rulebook a bay-front lot has to design around",
            "<p>A synthetic lawn in Florida has had to answer to Rule 62-308.100 since May 19, 2026, and the checklist runs four items deep: infill that's natural rather than synthetic, a "
            "base of washed rock, nothing irrigating from underneath, and a 10-foot gap held back from any open waterbody unless the edge in question is a seawall " + src("dep-rule", "DEP Rule 62-308.100") +
            ". On Osprey ground touching Little Sarasota Bay, that last item is the one worth measuring off a survey rather than a fence line, since the gap decides where the layout's "
            "edge can actually sit. F.S. 125.572 keeps every local government, Sarasota County included, from adding a stricter version of that same floor " + src("fs125572", "F.S. 125.572") + ".</p>"
        ),
        (
            "A lawn that's already struggling has fewer paths back under Phase III",
            "<p>The county's current shortage declaration, SWFWMD's Modified Phase III, lasts through March 31, 2027 and leaves homeowners exactly one sprinkler day a week, timed to an "
            "overnight or late-night stretch rather than daylight hours " + src("swfwmd-restrictions", "SWFWMD district restrictions") + ". Sod that's already patchy rarely bounces back on "
            "that thin a schedule, which is why a failing lawn, not just a new-build yard, is often where the turf conversation starts. A yard that stays out of view from the street frontage "
            "also keeps whatever protection F.S. 720.3045 extends against an HOA objection as of 2026 " + src("fs720-3045", "F.S. 720.3045") + ".</p>"
        ),
    ],
    "scenario": (
        "A turf lawn near Little Sarasota Bay, worked out in square feet",
        "<p>An Osprey backyard runs down to a seawall on Little Sarasota Bay, and the owner wants 500 square feet of turf laid right up to within a few feet of that wall rather than the "
        "open-water buffer a non-seawalled lot would need. At " + price("artificial-turf") + " per sq ft, the full range runs $5,000 to $12,500, with most comparable jobs settling into the "
        "typical " + price("artificial-turf", typical=True) + " band, near $6,000 to $9,000. Because a seawall, not open shoreline, forms that property line, the state's 10-foot buffer condition "
        "doesn't apply here the way it would on a lot with a natural bank instead.</p>"
    ),
    "faqs": [
        faq(
            "Does every Osprey yard have to clear the turf water-buffer rule?",
            "Only a yard backing to open water like Little Sarasota Bay or a residential canal. A yard bordering dry uplands, including ground near Oscar Scherer State Park's boundary, doesn't trigger that particular condition."
        ),
        faq(
            "Does a seawall change the turf setback distance in Osprey?",
            "Yes. Where a seawall itself forms the property line, the state's 10-foot buffer from open water doesn't apply, unlike a lot where the shoreline is a natural bank instead."
        ),
        faq(
            "Does turf skip Sarasota County's current watering restriction?",
            "It does. The single sprinkler day a week that SWFWMD's shortage order sets through early 2027 is an irrigation rule, and a turf lawn, needing no irrigation at all once it's down, simply falls outside what that order regulates."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
