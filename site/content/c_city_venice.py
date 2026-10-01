# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "venice"

VENETIAN_ACC_URL = "https://img1.wsimg.com/blobby/go/9771004e-4c48-48de-b5b3-d2a698ae623a/downloads/2dbcf307-d484-4c91-8173-7cf2ca76a901/ACC%20Application%2004.16.26.pdf?ver=1790705617734"
WATERATLAS_IC_URL = "https://sarasota.wateratlas.usf.edu/waterbodies/bays/14572/intracoastal-waterway-venice"
WATERATLAS_RB_URL = "https://sarasota.wateratlas.usf.edu/waterbodies/bays/14295/roberts-bay-venice"

SRC = [
    "venice-ldr-9.1-row-definition", "venice-ldr-3.1-general-standards", "venice-ldr-3.8-walls",
    "venice-engineering-permits", "venice-building-faq", "venice-bp-guidelines-3rdparty",
    "census-pep-v2025", "acs-venice", "wiki-nolen-venice",
    "swfwmd-restrictions", "fdot-sdg", "fema-coastal-firm", "fdep-cccl-program", "fdep-cccl-apply",
    "fl-senate-2011-104", "sarasota-county-124-255-culverts", "sarasota-county-124-76-rsf-standards",
    "sarasota-county-22-63-retaining-walls", "sarasota-county-online-permitting", "dep-rule", "fs125572",
    ("Venetian Golf & River Club POA, ACC Application", VENETIAN_ACC_URL),
    ("Sarasota County / USF Water Atlas, Intracoastal Waterway (Venice)", WATERATLAS_IC_URL),
    ("Sarasota County / USF Water Atlas, Roberts Bay (Venice)", WATERATLAS_RB_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec(
        "Which city office permits a new driveway or right-of-way opening in Venice?",
        "<p>The city's Engineering Department reviews any work placed in the public right-of-way under a Right-of-Way Use Permit, defined in the Land Development Regulations as the authorization "
        "'required under this Code prior to commencement of any placement or maintenance of facilities in the public rights-of-way' " + src("venice-ldr-9.1-row-definition", "Venice LDR §9.1") + ". "
        "That sign-off has to come from Engineering before construction starts in the right-of-way, and on a lot where pavers are going down over an existing concrete apron rather than a fresh pour, "
        "the city treats it as a License Agreement hardship case, built to its own Paver Installation Guidelines " + src("venice-engineering-permits", "City of Venice Engineering, Permits, Forms and Applications") + ". "
        "How many openings a lot gets is set by frontage: §3.1 caps a residential lot under 80 feet of street frontage at one driveway opening, allows two between 80 and 200 feet, "
        "and adds one more for every extra 100 feet beyond that " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ". " +
        cs("venice", "concrete-driveways", "A concrete driveway") + " and " + cs("venice", "paver-driveways", "a paver driveway") + " both start with that frontage math before the apron gets designed.</p>"
    ),
    sec(
        "Do pavers, a patio or a pool deck count against a Venice lot's coverage limit?",
        "<p>Not the way some nearby zoning codes count them. Venice's own Land Development Regulations define lot coverage as building footprint only, and the text is specific that coverage "
        "'does not include paved areas such as parking lots, pools, driveways or pedestrian walkways' " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ", with no separate residential "
        "impervious-surface cap found anywhere in LDR Chapter 87. That is a real difference from a per-zone paving percentage some neighboring cities apply to every square foot of driveway, deck and roof combined. "
        "It doesn't mean a Venice patio, " + svc("pool-deck-pavers", "pool deck paver") + " job or " + svc("artificial-turf", "turf") + " install skips review: the city's own Building Permit Guidelines sheet, "
        "written for the 2014 edition of the Florida Building Code, lists an on-grade patio or deck without footings as not needing a permit, a point worth confirming is still current with the Building Department before pouring " +
        src("venice-bp-guidelines-3rdparty", "Venice Building Permit Guidelines") + ". Online permitting is the only route either way; the department does not take paper applications " + src("venice-building-faq", "Venice Building Division FAQ") + ".</p>"
    ),
    sec(
        "What does Venice's fast growth and 1986 median build year mean for a project here?",
        "<p>Venice added residents faster than any of the other nine towns the Sarasota unit serves between 2020 and 2025, growing from a base of 25,473 to an estimated 30,477, a jump of roughly 19.6 percent " +
        src("census-pep-v2025", "Census Bureau PEP, Vintage 2025") + ". That growth sits next to a median year-structure-built of 1986 " + src("acs-venice", "Census Reporter, Venice FL") + ", so a new-construction " +
        svc("concrete-slabs", "slab") + " on a freshly platted lot is as common a call here as a " + svc("concrete-repair", "repair") + " on a driveway now pushing forty years old. The city also skews "
        "older than its growth numbers suggest, with a median age close to 69 against a statewide figure far below it " + src("acs-venice") + ", part of why low-maintenance finishes come up often in quotes. "
        "Downtown, the John Nolen Plan Historic District carries a different housing stock again: platted in 1926 for the Brotherhood of Locomotive Engineers and listed on the National Register of Historic Places "
        "in September 2009, it runs narrower early-20th-century lots bounded by Laguna Drive, Home Park Road, the Corso and the Esplanade " + src("wiki-nolen-venice") + ".</p>"
    ),
    sec(
        "What do Venice Island, the Intracoastal Waterway and Gulf flood zones change for a build?",
        "<p>" + ext(WATERATLAS_IC_URL, "USF Water Atlas") + " describes the Intracoastal Waterway's canal, dug through in the 1960s, as the cut that turned the Gulf-front strip of the city into Venice "
        "Island, crossed today by three bridges, while " + ext(WATERATLAS_RB_URL, "the same source") + " traces Roberts Bay at the island's north end back to Hatchett Creek, Curry Creek and Blackburn Canal "
        "feeding into it. A home close to that water answers to FEMA's coastal flood categories, Zone AE for roughly a one-percent annual chance of flooding with lighter wave action, stepping up to the "
        "Coastal High Hazard Zone VE where storm surf can tear into a low wall or an unprotected deck edge " + src("fema-coastal-firm", "FEMA's coastal flood-map guidance") + ". A project reaching past "
        "Florida's own Coastal Construction Control Line toward the beach needs DEP's sign-off first, through the agency's Bureau of Beaches and Coastal Systems " + src("fdep-cccl-program", "FDEP's CCCL program") +
        ", a separate application from whatever the city's own permit desk requires " + src("fdep-cccl-apply", "FDEP's CCCL application page") + ". " + svc("retaining-walls", "A retaining wall") + " holding "
        "fill on a canal lot and " + svc("artificial-turf", "turf") + " near the water both start with that same flood-zone and control-line question before the design gets drawn.</p>"
    ),
    sec(
        "Do South Venice and Nokomis answer to the city or to Sarasota County?",
        "<p>Plenty of ground with a Venice mailing address actually sits in unincorporated Sarasota County rather than inside the city line, " + city("south-venice", "South Venice") + " and " +
        city("nokomis", "Nokomis") + " among the nearby communities where that applies. Out there, the county, not the city, reviews a driveway's culvert and swale under its own code, which sets the pipe length, "
        "grade and drainage-easement rules for any paved surface tying into the road " + src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ", filed through the county's own online "
        "permitting system rather than Venice's portal " + src("sarasota-county-online-permitting", "Sarasota County Online Permitting") + ". The county's building-coverage limit in its RSF zoning districts caps "
        "the house itself at 35 percent of the lot, a building limit that does not touch a driveway or patio's own square footage " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") +
        ". A retaining wall over 4 feet tall on one of these lots needs engineered drawings under the county's pool-code amendment, a threshold Venice's own code does not spell out the same way inside the city line " +
        src("sarasota-county-22-63-retaining-walls", "Sarasota County Code §22-63") + ".</p>"
    ),
    sec(
        "How does the current watering order change sod, turf and new concrete here?",
        "<p>Sarasota County, Venice included, falls entirely inside the area the Southwest Florida Water Management District placed under a Modified Phase III shortage order that runs from April 3, 2026 "
        "through March 31, 2027 " + src("swfwmd-restrictions", "SWFWMD's shortage-order page") + ". Addresses get exactly one watering day a week, assigned by the last digit of the street number, in an "
        "overnight or late-night window rather than daytime hours. New sod still gets a short runway, daily water for 30 days, then three days a week for the next 30, before it drops onto that same "
        "one-day calendar. " + svc("artificial-turf", "Artificial turf") + " is free of that calendar entirely once it's installed and rinsed in, which is part of why it comes up so often on the shaded, "
        "older-canopy lots near Venice's downtown grid, and " + svc("paver-sealing", "paver cleaning and sealing") + " never answered to it in the first place, since a pressure washer isn't the kind of "
        "irrigation the order targets.</p>"
    ),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq(
        "Do you work in Venice, South Venice and Nokomis?",
        "Yes. The Sarasota unit covers the city of Venice along with the unincorporated South Venice and Nokomis areas nearby, though the permit desk differs: Venice's own Engineering and Building Departments review work inside the city line, while Sarasota County's Building Division reviews the same scope in South Venice and Nokomis. Barrier-island and canal-front lots in any of the three add the salt-air and flood-zone questions a mainland lot further from the water doesn't face."
    ),
    faq(
        "Does Venice require a permit for a new driveway opening?",
        "Yes, inside the city, under a Right-of-Way Use Permit from the Engineering Department, and how many openings a lot is allowed depends on its street frontage: one opening under 80 feet, two between 80 and 200 feet, and one more for every additional 100 feet past that."
    ),
    faq(
        "Do pavers or a pool deck count against my Venice lot's coverage limit?",
        "No. Venice's Land Development Regulations define lot coverage as building footprint only and specifically exclude paved areas, pools, driveways and pedestrian walkways from that count, a different approach than a percentage-based paving cap some neighboring cities use."
    ),
    faq(
        "Is my Venice Island home in a FEMA flood zone?",
        "Possibly, especially close to the Intracoastal Waterway or the Gulf. FEMA's coastal maps split that risk into Zone AE, with modest wave action, and the higher-hazard Zone VE, and anything seaward of Florida's Coastal Construction Control Line needs its own DEP permit before a local one is relevant."
    ),
    faq(
        "How do I find the best concrete contractor in Venice?",
        "Check the contractor on the state's license-verification tool, confirm whether the city's Engineering Department or Sarasota County's Building Division actually reviews your address, and ask how the bid handles a flatwoods subgrade near the water table. " +
        post("how-to-choose-a-concrete-contractor-sarasota", "Ten criteria for choosing a concrete contractor") + " covers the rest."
    ),
    faq(
        "Does the current watering order affect new sod or turf in Venice?",
        "Yes. Sarasota County, Venice included, is under SWFWMD's Modified Phase III shortage order through March 2027, limiting irrigation to one day a week by address. New sod gets a short grace period; artificial turf sits outside the schedule entirely once it's installed."
    ),
]

HUB = page(
    "/venice-fl/", "city",
    "Concrete, Pavers & Turf Contractor in Venice, FL",
    "Concrete, pavers and turf in Venice, FL: driveway-opening permits by frontage, Gulf flood zones and the Nolen Historic District, October 2026.",
    "Concrete, Pavers and Artificial Turf for Venice Homes",
    capsule(
        "Venice sits about 17 miles south of Sarasota on the Gulf coast, a city the Census Bureau counted at 30,477 residents in July 2025. As of October 2026, its Engineering Department permits "
        "driveway openings by street frontage rather than a flat number, lot coverage is measured by building footprint only, not total paving, and SWFWMD's Modified Phase III order still limits "
        "irrigation countywide to one day a week."
    ),
    HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
    crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Venice",
    related=[
        ("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
        ("/blog/sarasota-county-driveway-patio-permits/", "Driveway and patio permits in Sarasota, Venice and North Port"),
        ("/sarasota-fl/", "Concrete, pavers and turf in Sarasota"),
        ("/bradenton-fl/", "Concrete, pavers and turf in Bradenton"),
        ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
        ("/paver-driveway-cost/", "Paver driveway cost guide"),
    ],
    eyebrow="Concrete · Pavers · Turf in Venice, FL",
)

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Venice, FL – Opening Permits",
    "meta": "Concrete driveway installers in Venice, FL: LDR Sec. 3.1's frontage rule on opening count and the Right-of-Way Use Permit, as of October 2026.",
    "h1": "Pouring or Replacing a Concrete Driveway in Venice",
    "lede": capsule(
        "A new or replacement concrete driveway in Venice runs " + price("concrete-driveway") + " per " + per("concrete-driveway") + " as of October 2026. Before the apron gets poured, the city's "
        "Engineering Department checks it against the Right-of-Way Use Permit the project needs and the number of openings a lot's street frontage allows under LDR §3.1."
    ),
    "sections": [
        (
            "Why the opening count depends on your lot's street frontage",
            "<p>Venice's Land Development Regulations cap how many driveway openings a residential lot gets, tied directly to frontage: under 80 feet of frontage allows one opening per street, 80 to 200 feet allows "
            "two, and each additional 100 feet past 200 adds one more " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ". A corner lot or a wide Gulf-side parcel can clear that 80-foot line without "
            "much extra width, which matters on a property planning a second apron for a boat trailer or a side motor court rather than widening the one cut it already has. Before pricing " +
            cs("venice", "paver-driveways", "a paver driveway") + " alternative or a second concrete opening, we measure the actual frontage against that table rather than assume a figure that applies elsewhere in the unit.</p>"
        ),
        (
            "The Right-of-Way Use Permit is separate from the private slab",
            "<p>Anything built or placed in the public right-of-way, the curb cut and apron included, needs its own Right-of-Way Use Permit from the Engineering Department before construction starts, defined in "
            "code as authorization required ahead of 'any placement or maintenance of facilities in the public rights-of-way' " + src("venice-ldr-9.1-row-definition", "Venice LDR §9.1") + ". The Engineering "
            "Department's permits page describes that review running ahead of the private portion of the job, and the city keeps its own Paver Installation Guidelines for an apron built in pavers rather than "
            "poured concrete " + src("venice-engineering-permits", "City of Venice Engineering, Permits, Forms and Applications") + ". The Building Department, at 941-882-7547, takes applications online only; "
            "paper submissions aren't accepted " + src("venice-building-faq", "Venice Building Division FAQ") + ".</p>"
        ),
    ],
    "scenario": (
        "A two-opening driveway on a wide Venice lot, worked out in square feet",
        "<p>Say a lot carries 140 feet of street frontage, over the 80-foot line but under 200, qualifying it for two driveway openings under LDR §3.1 rather than one. The main apron to the garage measures "
        "18 by 40 feet, 720 square feet, and a second, narrower opening for a side parking pad adds 10 by 20 feet, 200 square feet, for 920 square feet combined. At " + price("concrete-driveway") + " per " +
        per("concrete-driveway") + ", that full scope runs $5,520 to $13,800, narrowing to roughly $7,360 to $11,040 in the typical " + price("concrete-driveway", typical=True) + " band. Both openings still "
        "need their own Right-of-Way Use Permit sign-off from Engineering where they cross into the public strip, reviewed together rather than as two separate applications.</p>"
    ),
    "faqs": [
        faq(
            "How many driveway openings can a Venice lot have?",
            "It depends on street frontage under LDR §3.1: one opening for a lot under 80 feet, two for 80 to 200 feet, and one additional opening for every extra 100 feet beyond that, per street the lot fronts."
        ),
        faq(
            "Does a straight driveway replacement in Venice need a permit?",
            "The portion in the public right-of-way does, under a Right-of-Way Use Permit from the Engineering Department. The city's own online portal is the only way to apply; paper applications aren't accepted."
        ),
        faq(
            "Can I add a second driveway opening in Venice?",
            "Only if the lot's street frontage supports it under LDR §3.1's table. A lot with at least 80 feet of frontage on a given street qualifies for two openings; narrower lots are limited to one."
        ),
    ],
    "sources": SRC,
}

# 2. paver-driveways -----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Venice, FL – ROW Guidelines",
    "meta": "Paver driveway installers in Venice, FL: the Engineering Department's License Agreement for pavers over concrete, as of October 2026.",
    "h1": "Paver Driveway Installation in Venice",
    "lede": capsule(
        "A paver driveway in Venice runs " + price("paver-driveway") + " per " + per("paver-driveway") + " as of October 2026. Where the apron sits in the public right-of-way, the city treats pavers "
        "differently from a fresh concrete pour, with its own Paver Installation Guidelines and a License Agreement hardship exception for pavers laid over an existing slab."
    ),
    "sections": [
        (
            "Pavers over an existing apron go through a License Agreement, not a standard permit",
            "<p>The Engineering Department's own guidance singles out paver work as an exception case: a License Agreement is granted for hardship or special circumstances, and the department's own example is "
            "'pavers installed over concrete per city details,' built to the city's separate Paver Installation Guidelines " + src("venice-engineering-permits", "City of Venice Engineering, Permits, Forms and Applications") +
            ". That matters on a driveway that already has a sound concrete base and just needs a paver finish over it, since the review path differs from a brand-new opening cut into the right-of-way. The "
            "underlying Right-of-Way Use Permit requirement still applies to any work in that strip " + src("venice-ldr-9.1-row-definition", "Venice LDR §9.1") + "; the License Agreement is the mechanism for "
            "the paver-over-concrete case specifically.</p>"
        ),
        (
            "Pavers don't push a lot toward Venice's coverage limit",
            "<p>A paver driveway counts the same as any other paving for Venice's lot-coverage review, but the city's own definition limits that coverage to building footprint and expressly excludes 'paved "
            "areas such as parking lots, pools, driveways or pedestrian walkways' " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ", with no separate residential impervious-surface percentage "
            "found in LDR Chapter 87. A homeowner widening a two-car paver driveway to three cars, or adding a side motor court, isn't working against the per-zone paving ceiling some neighboring cities apply, "
            "though the frontage-based opening count under §3.1 and the right-of-way review still govern how the apron itself gets built.</p>"
        ),
    ],
    "scenario": (
        "Relaying a concrete apron in pavers, worked out in square feet",
        "<p>Say a 540 square foot two-car driveway has a sound concrete base but a worn, stained surface, and the plan is to relay it in pavers rather than tear it out. At " + price("paver-driveway") + " per " +
        per("paver-driveway") + ", that runs $5,400 to $16,200, narrowing to roughly $6,480 to $10,800 in the typical " + price("paver-driveway", typical=True) + " band depending on the paver and whether the "
        "old slab needs grinding or patching first. Where the driveway crosses into the right-of-way, the paver-over-concrete scope goes through Engineering's License Agreement process rather than a standard "
        "new-opening review, built to the city's Paver Installation Guidelines.</p>"
    ),
    "faqs": [
        faq(
            "Can I put pavers over my existing Venice driveway without tearing it out?",
            "Often, yes, through the Engineering Department's License Agreement process for hardship or special cases, which names pavers installed over concrete as its own example, built to the city's Paver Installation Guidelines."
        ),
        faq(
            "Does a paver driveway count differently than concrete for Venice's lot coverage?",
            "No. The city's lot-coverage definition excludes paved areas, driveways and pedestrian walkways from the count either way, since coverage is measured by building footprint only, not by total paving."
        ),
        faq(
            "Do I still need the frontage-based opening count for a paver driveway in Venice?",
            "Yes. LDR §3.1's table on driveway openings per street frontage applies regardless of whether the surface is concrete or pavers."
        ),
    ],
    "sources": SRC,
}

# 3. concrete-patios -------------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Venice, FL – Permit Guidance",
    "meta": "Concrete patio contractors in Venice, FL: why an older city guidance sheet's on-grade exemption needs confirming first, October 2026.",
    "h1": "Building a Concrete Patio in Venice",
    "lede": capsule(
        "A concrete patio in Venice runs " + price("concrete-patio") + " per " + per("concrete-patio") + " as of October 2026. An older city guidance sheet lists an on-grade patio without footings as not "
        "needing a permit, though we confirm that's still current with the Building Department before pouring rather than assume it still applies."
    ),
    "sections": [
        (
            "What an older city guidance sheet says about patios on grade",
            "<p>A Building Permit Guidelines sheet written for the 2014 edition of the Florida Building Code lists 'decks and patios directly on grade and without footings' as work that does not require a "
            "permit, alongside a parallel entry for a non-buildable-slab patio or deck on grade " + src("venice-bp-guidelines-3rdparty", "Venice Building Permit Guidelines") + ". Florida's building code has "
            "moved through several editions since that sheet was written, and the copy available is hosted on a third-party site rather than the city's own, so we treat it as a starting point and confirm "
            "current practice with the Building Department, at 941-882-7547, before pricing a patio as permit-exempt " + src("venice-building-faq", "Venice Building Division FAQ") + ".</p>"
        ),
        (
            "A patio doesn't count toward Venice's lot-coverage limit the way an addition does",
            "<p>Venice's own lot-coverage rule measures building footprint, and the code text specifically excludes paved areas, a backyard patio among them, from that count " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") +
            ". That's useful on a lot that already carries a full house footprint and a pool cage, since a " + svc("paver-patios", "paver") + " or concrete patio addition doesn't push the parcel toward a "
            "coverage ceiling the way it might under a percentage-based impervious cap. " + svc("concrete-pool-decks", "A concrete pool deck") + " on the same lot works the same way under this definition, "
            "though online permitting through the city's portal is still the only application path either way.</p>"
        ),
    ],
    "scenario": (
        "A lanai extension off a screened pool cage, worked out in square feet",
        "<p>Say a 1980s Venice home adds an 18 by 14 foot patio extension, 252 square feet, off the back of an existing screened lanai, flush with the current grade and without footings. At " +
        price("concrete-patio") + " per " + per("concrete-patio") + ", that runs $1,512 to $3,276, or roughly $1,764 to $2,520 in the typical " + price("concrete-patio", typical=True) + " band for a broom "
        "finish with a control-joint layout matched to the slab. Because the addition stays on grade without footings, it's the kind of scope the city's older guidance sheet treats as exempt, but we still "
        "confirm with the Building Department before scheduling the pour rather than rely on a document written for an earlier code edition.</p>"
    ),
    "faqs": [
        faq(
            "Does a small concrete patio in Venice need a building permit?",
            "An older city guidance sheet lists an on-grade patio without footings as exempt, but since it was written for an earlier Florida Building Code edition, we confirm current practice with the Building Department at 941-882-7547 before pricing a job as permit-free."
        ),
        faq(
            "Does a patio count against my Venice lot's coverage limit?",
            "No, under the city's own definition. Lot coverage measures building footprint only and excludes paved areas, including a patio, from that count."
        ),
        faq(
            "Can I apply for a Venice patio permit on paper instead of online?",
            "No. The Building Division's FAQ page is explicit that online permitting is the only route and paper applications aren't accepted."
        ),
    ],
    "sources": SRC,
}

# 4. paver-patios ------------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Venice, FL – HOA & ACC Rules",
    "meta": "Paver patio installers in Venice, FL: Venetian Golf & River Club's monthly ACC review and the city's right-of-way rule, October 2026.",
    "h1": "Paver Patios and Walkways in Venice",
    "lede": capsule(
        "A paver patio in Venice runs " + price("paver-patio") + " per " + per("paver-patio") + " as of October 2026. In the Venetian Golf & River Club community in North Venice, a patio or walkway change "
        "needs the Architectural Control Committee's sign-off before work starts, reviewed on a monthly cycle separate from any city permit."
    ),
    "sections": [
        (
            "Venetian Golf & River Club's ACC reviews exterior changes monthly",
            "<p>The community's Master Declaration requires that 'no material alteration, modification or addition to a Home, or material change in external appearance of a Home, shall be undertaken without "
            "the prior written approval of the ACC' " + ext(VENETIAN_ACC_URL, "Venetian Golf & River Club POA, ACC Application") + ". The committee meets the first Monday of each month at 2 p.m., with "
            "applications due by noon on the last Monday of the prior month, and decisions go out by email within 72 hours; approval holds for six months once granted. A home inside a sub-HOA or condo "
            "association needs that association's president or manager to sign the application too, on top of the ACC's own review.</p>"
        ),
        (
            "A walkway crossing the property line adds the city's right-of-way review",
            "<p>A paver walkway running from the driveway to the front door usually stays entirely on private ground, but one that crosses the sidewalk strip toward the street falls under the same "
            "Right-of-Way Use Permit the city requires for any work placed in the public right-of-way " + src("venice-ldr-9.1-row-definition", "Venice LDR §9.1") + ". " + svc("concrete-walkways", "A concrete walkway") +
            " crossing that same strip faces an identical review regardless of surface material. Inside a community like Venetian Golf & River Club, that city-level review runs alongside, not instead of, "
            "the ACC's own sign-off on the finished look.</p>"
        ),
    ],
    "scenario": (
        "A Venetian Golf & River Club paver patio, worked out in square feet",
        "<p>Say a North Venice household in Venetian Golf & River Club relays 275 square feet of paver patio off the lanai, timed to clear the ACC's first-Monday meeting before materials get ordered. "
        "Pricing it at " + price("paver-patio") + " per " + per("paver-patio") + " puts the job between $2,750 and $4,675, settling near $3,300 to $4,400 inside the typical " + price("paver-patio", typical=True) +
        " range once the paver size and pattern are picked. Since the application deadline falls at noon on the last Monday before the meeting, missing that cutoff bumps the whole project, review and "
        "start date alike, back by roughly four weeks.</p>"
    ),
    "faqs": [
        faq(
            "Does Venetian Golf & River Club require approval before a new patio?",
            "Yes. Its Master Declaration bars any material change to a home's external appearance without the ACC's prior written approval, reviewed at a monthly meeting with applications due by the last Monday of the prior month."
        ),
        faq(
            "How long is an ACC approval good for at Venetian Golf & River Club?",
            "Six months from the date granted. A patio project that stalls past that window needs a fresh application before work can start."
        ),
        faq(
            "Does a paver walkway to the street need a separate city permit in Venice?",
            "The portion crossing the public sidewalk strip does, under the same Right-of-Way Use Permit a driveway apron needs. A path that stays fully on private ground doesn't trigger that particular review."
        ),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Venice, FL – Flood Zones",
    "meta": "Concrete pool deck builders in Venice, FL: FEMA Zone AE/VE near the Intracoastal and Gulf, and lot-coverage rules, October 2026.",
    "h1": "Concrete Pool Deck Installation in Venice",
    "lede": capsule(
        "A concrete pool deck in Venice runs " + price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " as of October 2026. Lots near the Intracoastal Waterway or the Gulf side of Venice "
        "Island often sit in a FEMA flood zone, and the deck itself doesn't count toward the city's lot-coverage limit the way the house footprint does."
    ),
    "sections": [
        (
            "Checking a lot's flood category before the forms go up",
            "<p>Lots along Venice Island's Gulf frontage or facing the Intracoastal fall into one of two FEMA categories: Zone AE, carrying roughly a one-percent annual flood chance with lighter wave "
            "action, or the Coastal High Hazard Zone VE, the same odds paired with surf capable of punching through a low deck edge in a major storm " + src("fema-coastal-firm", "FEMA's coastal flood-map guidance") +
            ". " + ext(WATERATLAS_RB_URL, "Roberts Bay") + " marks where the Intracoastal meets the island's north end, and parcels along that stretch are the ones most worth checking on FEMA's map "
            "viewer before a deck's finished height is set. A pour that reaches toward the beach side of the control line adds Florida's own DEP review on top of whatever the city otherwise requires " +
            src("fdep-cccl-program", "FDEP's CCCL program") + ".</p>"
        ),
        (
            "Why the deck doesn't change Venice's lot-coverage math",
            "<p>A pool deck, like a roof, is not exempt from review, but Venice's own rule only ties coverage to the structure's footprint, listing pools specifically among the paved features it leaves out "
            "of the count " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ". That matters on an older 1986-era lot where the original pool cage and deck are smaller than a current family "
            "wants: expanding the deck's footprint doesn't push the parcel toward a separate coverage ceiling, though the slope and drainage at the slab's edge still have to carry water away from the house "
            "rather than toward a neighbor's yard or the canal behind it.</p>"
        ),
    ],
    "scenario": (
        "A pool deck pour near the Intracoastal, worked out in square feet",
        "<p>Say a canal-front home on Venice Island pours a 600 square foot deck around a screened cage, close enough to Roberts Bay to land inside FEMA's Zone AE on the current flood map. Pricing that at " +
        price("concrete-pool-deck") + " per " + per("concrete-pool-deck") + " puts the job between $3,000 and $9,000, or about $4,200 to $7,200 in the typical " + price("concrete-pool-deck", typical=True) +
        " range, for a textured, slip-resistant surface pitched toward the yard drain rather than a plain trowel finish. Sitting inside a mapped flood zone means the deck's edge height and the fill "
        "beneath it get set against that base-flood number instead of an inland assumption, and the deck's own footprint still leaves the lot's coverage total untouched, unlike an addition to the house itself.</p>"
    ),
    "faqs": [
        faq(
            "Is my Venice pool deck lot in a flood zone?",
            "Possibly, especially near the Intracoastal Waterway or the Gulf side of Venice Island. FEMA's map viewer shows Zone AE or the higher-hazard Zone VE by address, and the line can split a single street."
        ),
        faq(
            "Does a Venice pool deck need a state permit as well as a city one?",
            "If it's seaward of Florida's Coastal Construction Control Line, a DEP permit is required first. Most mainland and canal-front lots away from the beach itself don't cross that line."
        ),
        faq(
            "Does a bigger pool deck push my Venice lot over a coverage limit?",
            "No. The city's lot-coverage definition excludes pools and paved areas from the count, measuring coverage by building footprint only, unlike a percentage-based cap some other cities use."
        ),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ----------------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Venice, FL – CCCL & Salt",
    "meta": "Pool deck paver overlays in Venice, FL: when the Coastal Construction Control Line adds a DEP permit, plus salt air, October 2026.",
    "h1": "Travertine and Paver Pool Decks in Venice",
    "lede": capsule(
        "Pool deck pavers or travertine in Venice run " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " as of October 2026. Stretching a deck toward the Gulf-facing side of Venice "
        "Island can put part of it past Florida's own construction control line, which brings in a state review before the city's permitting office even looks at the job."
    ),
    "sections": [
        (
            "Reaching toward the beach brings in a state review first",
            "<p>Where a deck extends past Florida's Coastal Construction Control Line, the Department of Environmental Protection's Bureau of Beaches and Coastal Systems has to sign off first, since the "
            "program exists to limit beach erosion and dune damage rather than to judge the deck design itself " + src("fdep-cccl-program", "FDEP's CCCL program") + ", with its own separate application "
            "process " + src("fdep-cccl-apply", "FDEP's CCCL application page") + ". A travertine or paver overlay stretching toward the Gulf-facing edge of a Venice Island lot is exactly the kind of "
            "addition where that state line, not any setback the city might otherwise apply, decides how far the deck gets to reach.</p>"
        ),
        (
            "Salt air off the Gulf and the Intracoastal shortens the sealing clock",
            "<p>Bridge engineers at FDOT use a specific cutoff for what counts as a corrosive marine environment, water running above 2,000 parts per million chloride within 2,500 feet of the structure, "
            "and that same standard is a reasonable stand-in for how salt-laden the air gets off the Gulf beach and the Intracoastal stretch wrapping Venice Island " + src("fdot-sdg") + ". The paver "
            "base and bedding sand go in the same way regardless, but that salt load speeds up how soon joint sand washes out and an unsealed surface starts staining around the pool coping, which is "
            "why " + svc("paver-sealing", "resealing") + " a Gulf-side deck tends to land on a shorter cycle than the identical job a few miles inland.</p>"
        ),
    ],
    "scenario": (
        "A travertine overlay on an older Venice Island pool deck, worked out in square feet",
        "<p>Say a home on Venice Island is ready to overlay an aging 750 square foot concrete pool deck in travertine, and part of the existing slab sits close enough to the Gulf that the control line "
        "cuts right across the yard. Pricing the overlay at " + price("pool-deck-pavers") + " per " + per("pool-deck-pavers") + " comes out between $9,000 and $22,500, tightening toward $10,500 to "
        "$16,500 inside the typical " + price("pool-deck-pavers", typical=True) + " range once the stone and pattern are picked. Figuring out exactly where that line falls on the parcel happens before "
        "a number gets quoted, and the salt exposure on a lot this close to open water steers which sealer and edge-restraint hardware get specified rather than defaulting to an inland spec.</p>"
    ),
    "faqs": [
        faq(
            "Does a pool deck overlay on Venice Island need a state permit?",
            "Only the portion that falls past Florida's Coastal Construction Control Line. Where that applies, DEP's own sign-off comes first, before the city's permitting office gets involved, so pinning down the line's exact position on a given parcel is step one."
        ),
        faq(
            "Why does salt air matter more for a Venice pool deck than an inland one?",
            "FDOT's bridge-design cutoff for a corrosive marine environment, water above 2,000 parts per million chloride within 2,500 feet, happens to describe nearly the whole of Venice Island and its Gulf-facing lots, which is why sealer and hardware choices differ on a deck built that close to the water."
        ),
        faq(
            "Is travertine cooler than a concrete paver pool deck in Venice's heat?",
            "Manufacturer and third-party claims point that direction, but no verified degree figure exists for either material, so we don't quote a specific temperature difference when pricing the job."
        ),
    ],
    "sources": SRC,
}

# 7. stamped-concrete -------------------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Venice, FL – Nolen District",
    "meta": "Stamped concrete contractors in Venice, FL: pattern choices in the John Nolen Plan Historic District, as of October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Venice",
    "lede": capsule(
        "Stamped concrete in Venice runs " + price("stamped-concrete") + " per " + per("stamped-concrete") + " as of October 2026. Downtown, the John Nolen Plan Historic District's 1920s grid tends toward "
        "a muted, period-appropriate pattern, while the city's newer, fast-growing subdivisions give homeowners more room to choose a bolder stamp and color."
    ),
    "sections": [
        (
            "A 1926 planned district downtown shapes the pattern choice, not the permit",
            "<p>The John Nolen Plan Historic District, listed on the National Register of Historic Places in September 2009, was laid out in 1926 by planner John Nolen for the Brotherhood of Locomotive "
            "Engineers and is bounded by Laguna Drive to the north, Home Park Road to the east, the Corso to the south and the Esplanade to the west " + src("wiki-nolen-venice") + ". Nothing in that "
            "designation dictates a stamp pattern, but homeowners inside the district tend to gravitate toward a quieter slate or ashlar look over a busier, brightly colored cobble job, since the "
            "latter can read out of place against a 1920s facade in a way it wouldn't on a 1990s subdivision street.</p>"
        ),
        (
            "Stamped work still answers to the same opening and right-of-way rules",
            "<p>A stamped driveway or walkway crossing into the public right-of-way needs the same Right-of-Way Use Permit as a plain pour " + src("venice-ldr-9.1-row-definition", "Venice LDR §9.1") + ", "
            "and a stamped finish doesn't change how many openings a lot's frontage supports under LDR §3.1 " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ". On the narrower lots common "
            "in the historic grid, that frontage math matters more than it does on a wide subdivision lot, since a downtown property is more likely to sit close to the single-opening threshold. " +
            svc("concrete-driveways", "A plain concrete driveway") + " on the same lot faces an identical frontage and right-of-way review.</p>"
        ),
    ],
    "scenario": (
        "A stamped entry walk in the Nolen district, worked out in square feet",
        "<p>Say a 350 square foot stamped-concrete front walk and entry patio replaces a cracked original path on a lot inside the John Nolen Plan Historic District, near the Corso. At " +
        price("stamped-concrete") + " per " + per("stamped-concrete") + ", that project prices between $2,800 and $6,650, settling closer to $4,200 to $5,600 inside the typical " +
        price("stamped-concrete", typical=True) + " range once the pattern and color count are set. Given the address, a single-color slate or ashlar layout is usually where the conversation with "
        "the homeowner lands, since a louder, multi-tone cobble finish tends to clash with the proportions of a house built to the Nolen plan's original scale.</p>"
    ),
    "faqs": [
        faq(
            "Does stamped concrete in the Nolen Historic District need special approval?",
            "No separate review was found tied to the stamp pattern itself; the standard Right-of-Way Use Permit and the frontage-based opening count under LDR §3.1 apply the same as anywhere else in the city."
        ),
        faq(
            "What pattern suits a 1920s Venice home best?",
            "A muted slate or ashlar pattern in a single integral color tends to read more period-appropriate on a John Nolen Plan Historic District lot than a bright multi-color cobble pattern built for a newer subdivision."
        ),
        faq(
            "Does stamped concrete cost more than plain concrete in Venice?",
            "Yes, the labor for the release agent, integral color and stamping pushes the price above a plain pour, though the subgrade work, frontage math and right-of-way review underneath it don't change based on the finish chosen."
        ),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Concrete Walkways in Venice, FL – Coverage Rules",
    "meta": "Concrete walkway and sidewalk contractors in Venice, FL: walkways named in the lot-coverage exclusion and the right-of-way permit; range " + price("concrete-walkway") + " per " + per("concrete-walkway") + ".",
    "h1": "Concrete Sidewalks and Walkways in Venice",
    "lede": capsule(
        "A concrete walkway or sidewalk section in Venice runs " + price("concrete-walkway") + " per " + per("concrete-walkway") + " as of October 2026. The city's own code names pedestrian walkways "
        "directly among the paved areas excluded from its lot-coverage count, and any section crossing the right-of-way still needs Engineering's sign-off."
    ),
    "sections": [
        (
            "Walkways are named directly in Venice's lot-coverage exclusion",
            "<p>Venice's Land Development Regulations define lot coverage as building footprint only, and the exclusion list names 'paved areas such as parking lots, pools, driveways or pedestrian "
            "walkways' outright " + src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ", so a front walkway, a side-yard path or a connector between the driveway and the pool cage doesn't add "
            "to that total the way an addition to the house would. No separate residential impervious-surface percentage was found elsewhere in LDR Chapter 87 either, so a walkway's own footprint isn't "
            "working against a second ceiling on top of the coverage rule.</p>"
        ),
        (
            "The part that crosses the sidewalk strip still needs Engineering's sign-off",
            "<p>A walkway running from the driveway to the front door is usually private work, but once it crosses the sidewalk strip toward the street, it falls under the same Right-of-Way Use Permit "
            "that governs a driveway apron " + src("venice-ldr-9.1-row-definition", "Venice LDR §9.1") + ", reviewed by the Engineering Department before construction starts " +
            src("venice-engineering-permits", "City of Venice Engineering, Permits, Forms and Applications") + ". In the city's older downtown grid, narrower lots mean that strip often sits closer to "
            "the house than it does on a newer subdivision lot, so confirming the property line before forms go up avoids a walkway built partly outside it.</p>"
        ),
    ],
    "scenario": (
        "A front walkway replacement, worked out in square feet",
        "<p>Say a 4 by 35 foot front walkway, 140 square feet, connects the driveway to the entry on an older downtown lot, replacing a cracked original path that crosses the sidewalk strip near the "
        "street. At " + price("concrete-walkway") + " per " + per("concrete-walkway") + ", that runs $980 to $2,380, or roughly $1,120 to $1,680 in the typical " + price("concrete-walkway", typical=True) +
        " band for a broom-finished walk. Because it's named directly in the city's lot-coverage exclusion, the new walkway doesn't add to the property's coverage total, but the section crossing the "
        "sidewalk strip still goes through the same Right-of-Way Use Permit a driveway apron would need.</p>"
    ),
    "faqs": [
        faq(
            "Does a new walkway count toward my Venice lot's coverage limit?",
            "No. The city's Land Development Regulations name pedestrian walkways directly among the paved areas excluded from lot coverage, which is measured by building footprint only."
        ),
        faq(
            "Does a front walkway need the same permit as a driveway in Venice?",
            "The portion that crosses the public sidewalk strip does, under the Right-of-Way Use Permit the Engineering Department reviews. A path that stays entirely on private ground doesn't trigger that particular review."
        ),
        faq(
            "Are downtown Venice lots narrower for walkway planning?",
            "Often, yes, in the older in-town grid near the John Nolen Plan Historic District, where the sidewalk strip sits closer to the house than it does on a newer subdivision lot."
        ),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Venice, FL – City & County",
    "meta": "Concrete slab contractors in Venice, FL: why slabs skip the city's coverage count, and county rules near South Venice, October 2026.",
    "h1": "Concrete Slabs for Sheds, AC Pads and Parking in Venice",
    "lede": capsule(
        "Pricing a utility slab in Venice, a shed pad, an AC pad or an RV parking strip, comes to " + price("concrete-slab") + " per " + per("concrete-slab") + " as of October 2026. Inside the city "
        "line that footprint leaves the lot's coverage total alone; a lot over the line in unincorporated South Venice or Nokomis answers to Sarasota County's permit process instead."
    ),
    "sections": [
        (
            "Inside Venice, a slab doesn't add to the lot-coverage total",
            "<p>The city's own lot-coverage definition measures building footprint only and excludes paved areas, which covers a shed, AC or parking slab the same way it covers a driveway or patio " +
            src("venice-ldr-3.1-general-standards", "Venice LDR §3.1") + ". That's useful on a lot that already carries a full house footprint and a pool cage, since adding or enlarging a utility pad "
            "doesn't push the parcel toward a separate coverage ceiling. The slab still needs its own building-permit review through the city's online-only portal, since lot coverage and permit review are "
            "two different questions " + src("venice-building-faq", "Venice Building Division FAQ") + ".</p>"
        ),
        (
            "South Venice and Nokomis lots answer to the county instead",
            "<p>A shed or AC pad on a lot in unincorporated " + city("south-venice", "South Venice") + " or " + city("nokomis", "Nokomis") + " goes through Sarasota County's own process rather than "
            "Venice's. Where the pad ties into a drainage easement or a driveway culvert, the county's code bars any paved surface from sitting inside that easement outright " +
            src("sarasota-county-124-255-culverts", "Sarasota County Code §124-255") + ", and building coverage in the county's RSF districts is capped at 35 percent of the lot for the house itself, a "
            "limit that doesn't extend to a detached slab " + src("sarasota-county-124-76-rsf-standards", "Sarasota County Code §124-76") + ".</p>"
        ),
    ],
    "scenario": (
        "A shed pad on each side of the Venice city line, worked out in square feet",
        "<p>Say a 10 by 14 foot shed pad, 140 square feet, goes in on a lot sitting right near the Venice city line. Pricing it at " + price("concrete-slab") + " per " + per("concrete-slab") + " puts the "
        "job between $560 and $1,400, tightening to roughly $840 to $1,120 inside the typical " + price("concrete-slab", typical=True) + " range for a reinforced 4-inch pour. Inside the city, that pad "
        "goes through Venice's own online-only permitting and leaves the lot's coverage total untouched. On an otherwise identical lot just across the line in unincorporated South Venice, the same pad "
        "instead goes through Sarasota County's process, and its footprint gets checked against any drainage easement on the property before the forms go up.</p>"
    ),
    "faqs": [
        faq(
            "Does a shed slab count toward my Venice lot's coverage limit?",
            "No, inside the city. Venice's lot-coverage definition measures building footprint only and excludes paved areas, including a utility or shed slab, from that count."
        ),
        faq(
            "Is a slab permitted differently in South Venice than inside the Venice city line?",
            "Yes. South Venice and Nokomis sit in unincorporated Sarasota County, so the county's own permit process and drainage-easement rules apply there instead of the city's."
        ),
        faq(
            "Can a slab sit inside a drainage easement near South Venice?",
            "No. The county's code bars any paved surface, a driveway or shed slab among them, from being located inside a drainage easement."
        ),
    ],
    "sources": SRC,
}

# 10. concrete-repair -----------------------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair in Venice, FL – 1986-Era Slabs",
    "meta": "Concrete repair and resurfacing in Venice, FL: why 1986-median driveways are cracking, and why the county isn't on the state's sinkhole-claims list, October 2026.",
    "h1": "Concrete Driveway and Slab Repair in Venice",
    "lede": capsule(
        "Concrete repair and resurfacing in Venice runs " + price("concrete-repair") + " per " + per("concrete-repair") + " as of October 2026. The city's median home was built in 1986, and Venice has "
        "grown faster than any other town the Sarasota unit serves since 2020, so brand-new slabs now sit next to driveways approaching forty years old."
    ),
    "sections": [
        (
            "A driveway from Venice's median build year is nearing forty years old",
            "<p>Venice's median year structure built is 1986 " + src("acs-venice", "Census Reporter, Venice FL") + ", and the city's population climbed from 25,473 in 2020 to an estimated 30,477 by "
            "mid-2025, a roughly 19.6 percent gain that outpaces every other town the Sarasota unit covers " + src("census-pep-v2025", "Census Bureau PEP, Vintage 2025") + ". Put those two figures "
            "together and a crew can be pouring a brand-new " + svc("concrete-driveways", "driveway") + " on one block while patching joints on a slab from the Reagan era two streets over. A "
            "driveway at that 1986 mark has absorbed roughly forty summers of expansion and contraction and as many rainy seasons, long enough that a crack patched twice over usually means the panel "
            "is better off resurfaced than repaired again.</p>"
        ),
        (
            "Why the cause of the crack matters more than its age",
            "<p>The Florida Senate's 2010 review of statewide sinkhole insurance claims names eleven counties, concentrated in the west-central part of the state, Hernando, Pasco and Hillsborough "
            "among the heaviest, and Sarasota County isn't one of them " + src("fl-senate-2011-104", "Florida Senate Interim Report 2011-104") + ". A dip near a Venice driveway's edge usually tells "
            "a more ordinary story instead: fill that was never quite compacted enough under the original pour, a canal lot's water table sitting close to the surface, or plain joint fatigue, not "
            "the sudden ground-cover collapse state law treats as its own mandatory insurance category. Telling the two apart calls for a look at the actual crack pattern, not a guess from a photo.</p>"
        ),
    ],
    "scenario": (
        "Resurfacing a 1980s-era Venice driveway, worked out in square feet",
        "<p>Say a 500 square foot two-car driveway, original to a home from around the city's 1986 median, has gone chalky on the surface and developed a web of hairline cracking across both panels. "
        "A resurfacing overlay at " + price("concrete-repair") + " per " + per("concrete-repair") + " lands between $1,500 and $5,000, or about $2,000 to $3,500 inside the typical " +
        price("concrete-repair", typical=True) + " range, well under what a full tear-out and new pour would run at the higher " + price("concrete-driveway") + " per sq ft driveway figure. Choosing "
        "between the two comes down to whether the base beneath the slab has held up; a full replacement also brings back the Right-of-Way Use Permit question wherever the apron reaches the public "
        "strip, a step resurfacing inside the same footprint usually skips.</p>"
    ),
    "faqs": [
        faq(
            "Should I worry about cracking in a 1986-era Venice driveway?",
            "Not automatically. With the city's median home built that year, a web of hairline cracking and worn joints is typically what forty years of heat and rain cycling looks like, not a sign the slab is failing structurally."
        ),
        faq(
            "Is sinkhole activity common under Venice driveways?",
            "No. Sarasota County isn't among the counties the Florida Senate flagged for the heaviest sinkhole insurance claims in its 2010 review, unlike several counties in the west-central part of the state. Settlement from loose fill is the far more common local explanation."
        ),
        faq(
            "Is resurfacing cheaper than full replacement for an old Venice driveway?",
            "It usually runs less per square foot, but a resurfacing overlay only holds up when the slab underneath hasn't lost structural integrity. A look at the base and the actual crack pattern is what decides which path makes sense for a given driveway."
        ),
    ],
    "sources": SRC,
}

# 11. paver-sealing --------------------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing in Venice, FL – Island Salt Air",
    "meta": "Paver sealing and restoration in Venice, FL: why Venice Island salt air shortens the resealing clock, October 2026.",
    "h1": "Paver Sealing and Restoration in Venice",
    "lede": capsule(
        "Cleaning, re-sanding and sealing pavers in Venice runs " + price("paver-sealing") + " per " + per("paver-sealing") + " as of October 2026. Proximity to the Gulf or the Intracoastal Waterway "
        "is the biggest variable in how soon that work comes due, since FDOT classifies the air around Venice Island as a marine environment."
    ),
    "sections": [
        (
            "Salt on Venice Island ages a sealed surface faster than inland lots",
            "<p>FDOT draws its marine-environment boundary at 2,500 feet from water carrying more than 2,000 ppm chloride for bridge-design purposes, and that boundary swallows essentially all of "
            "Venice Island, which the Intracoastal Waterway's canal cuts off from the mainland " + src("fdot-sdg") + " " + ext(WATERATLAS_IC_URL, "USF Water Atlas") + ". Salt in that air works on "
            "joint sand and sealer coatings much the way it works on hardware near any dock or seawall, pulling moisture and minerals through faster than a dry inland breeze would. Pricing a reseal "
            "without asking how close the lot sits to open water is the kind of shortcut that shows up again in a year or two instead of three or four.</p>"
        ),
        (
            "Where cleaning ends and a permit question starts",
            "<p>A reseal, re-sand or cleaning job on pavers already in place doesn't touch the Right-of-Way Use Permit the Engineering Department requires for new work placed in the public right-of-way " +
            src("venice-ldr-9.1-row-definition", "Venice LDR §9.1") + ", since nothing structural is being added or altered there. That changes the moment loose or sunken pavers inside the apron "
            "need pulling up and resetting rather than just rinsing and recoating; at that point the scope has crossed into construction and the permit question comes back. On the irrigation side, "
            "SWFWMD's current shortage order governs sprinklers, not a hose running a pressure washer, so prepping a surface for sealer isn't tied to any particular day of the week " +
            src("swfwmd-restrictions") + ".</p>"
        ),
    ],
    "scenario": (
        "Cleaning and resealing a driveway near the Intracoastal, worked out in square feet",
        "<p>Say a 450 square foot driveway-and-walkway combination near the Intracoastal on Venice Island hasn't been sealed in six years. A full clean, polymeric re-sand and reseal at " +
        price("paver-sealing") + " per " + per("paver-sealing") + " prices out between $675 and $1,462.50, tightening toward $787.50 to $1,237.50 inside the typical " + price("paver-sealing", typical=True) +
        " range depending on how much sand washed out and whether a salt-rated sealer formula gets specified over a standard acrylic. Pavers near the street edge that have settled enough to rock "
        "underfoot get quoted as a separate releveling line item rather than bundled into the base cleaning price.</p>"
    ),
    "faqs": [
        faq(
            "Do pavers on Venice Island need sealing more often than inland pavers?",
            "Usually. FDOT's own marine-environment threshold, 2,500 feet from salty water, covers nearly the whole island, and that salt exposure pulls joint sand and sealer coatings down faster than a dry inland lot ever sees."
        ),
        faq(
            "Is a city permit required to clean and reseal an existing paver driveway in Venice?",
            "No, as long as the work stays limited to cleaning, re-sanding and sealing pavers already in place. Pulling up and resetting sunken pavers inside the right-of-way apron is a different scope that can bring the permit question back."
        ),
        faq(
            "Does Venice's watering order limit when pavers can be pressure-washed before sealing?",
            "No. SWFWMD's current order restricts lawn sprinklers, not a pressure washer on a hose bib, so prepping a paver surface for sealant isn't tied to a particular day."
        ),
    ],
    "sources": SRC,
}

# 12. retaining-walls -------------------------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Venice, FL – Canal Lots",
    "meta": "Retaining wall contractors in Venice, FL: LDR Sec. 3.8's rules versus the county's 4-foot engineering trigger, October 2026.",
    "h1": "Retaining Walls for Venice Yards",
    "lede": capsule(
        "Building a retaining wall in Venice costs " + price("retaining-wall") + " per " + per("retaining-wall") + " as of October 2026. City code sets rules on where a wall can sit and how its height "
        "stacks with a fence on top, but no numeric height threshold for engineering, unlike the 4-foot trigger on nearby unincorporated county lots."
    ),
    "sections": [
        (
            "What Venice's own wall code covers, and what it doesn't",
            "<p>LDR §3.8 requires a zoning permit for a fence, wall, berm or retaining wall 'unless otherwise permitted through building permits,' bars any of them from sitting inside a visibility "
            "triangle, and in residential districts counts a retaining wall's height toward any fence built on top of it " + src("venice-ldr-3.8-walls", "Venice LDR §3.8") + ". Slopes inside a required "
            "setback can't exceed a 1-foot rise over 4 feet of run. No numeric height figure that automatically triggers engineering review turned up in that section, which makes a call to the "
            "Building Department worth making before a wall design over a couple of feet gets finalized.</p>"
        ),
        (
            "A canal-front wall in South Venice or Nokomis plays by a different rule",
            "<p>Step outside the city line into unincorporated " + city("south-venice", "South Venice") + " or " + city("nokomis", "Nokomis") + ", and Sarasota County's own pool-code amendment sets a "
            "clear number: any retaining wall over 4 feet tall, measured from grade at any point along it, needs engineered drawings " + src("sarasota-county-22-63-retaining-walls", "Sarasota County Code §22-63") +
            ". A yard sloping down toward Roberts Bay, Hatchett Creek or one of the canals feeding the Intracoastal Waterway typically holds back more fill than a flat inland lot does " +
            ext(WATERATLAS_RB_URL, "USF Water Atlas, Roberts Bay (Venice)") + ". " + svc("retaining-walls", "A retaining wall") + " built to hold grade is a different scope from a true seawall, which "
            "the dedicated retaining-walls page addresses on its own.</p>"
        ),
    ],
    "scenario": (
        "A canal-lot wall sized against the county's 4-foot trigger",
        "<p>Say a yard backing onto a canal off Roberts Bay calls for 40 linear feet of segmental block, standing 3.5 feet tall for 140 square feet of face, to level a patio pad against the slope "
        "down to the water. Pricing that at " + price("retaining-wall") + " per " + per("retaining-wall") + " comes to $2,100 to $5,600, or about $2,800 to $4,900 inside the typical " +
        price("retaining-wall", typical=True) + " range, before drainage behind the block gets added in. At 3.5 feet, the wall stays under the 4-foot mark that would force engineered drawings a few "
        "lots away in unincorporated Nokomis; inside Venice's own city line, where no comparable number exists in the code, we still walk the design past the Building Department before footings get poured.</p>"
    ),
    "faqs": [
        faq(
            "Does Venice set a specific height that triggers engineering on a retaining wall?",
            "Not in the sections of LDR §3.8 reviewed. A zoning permit applies above a certain scope, but no numeric threshold for engineering review turned up, so checking with the Building Department before finalizing a wall over a couple of feet is the safer move."
        ),
        faq(
            "Does a Venice retaining wall need an engineer above 4 feet?",
            "Inside the city, no fixed number was found; a short drive into unincorporated South Venice or Nokomis, Sarasota County's own code requires engineered drawings for any wall over 4 feet measured from grade."
        ),
        faq(
            "Can a Venice retaining wall double as a fence?",
            "Not quite the same thing structurally, but the code treats them together for height: in residential districts, a fence built on top of a retaining wall counts its height as additive to the wall's own, per LDR §3.8."
        ),
    ],
    "sources": SRC,
}

# 13. artificial-turf --------------------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Venice, FL – Canal Setbacks",
    "meta": "Artificial turf installers in Venice, FL: the state's 10-ft water-body setback near canals and the Intracoastal, plus SWFWMD watering rules, October 2026.",
    "h1": "Artificial Turf for Venice Yards",
    "lede": capsule(
        "A synthetic lawn in Venice runs " + price("artificial-turf") + " per " + per("artificial-turf") + " installed, as of October 2026. Canal-front and Intracoastal-adjacent lots have to hold the "
        "turf's edge back from the water under a statewide buffer rule, unless a seawall already sits there, and once the installation is rinsed in, the yard is done with the county's watering calendar for good."
    ),
    "sections": [
        (
            "A statewide rule sets the buffer before any city or HOA layer gets added",
            "<p>Florida's turf rule, Administrative Code Rule 62-308.100, took effect May 19, 2026 and sets a single bar for synthetic lawns statewide: natural infill material, a washed aggregate "
            "base, and a 10-foot buffer from any water body unless a seawall backs the lot, with buried irrigation barred from running underneath it " + src("dep-rule", "Florida Administrative Code, Rule 62-308.100") +
            ". A companion 2025 statute caps how much stricter a city or county is allowed to get on top of that baseline " + src("fs125572", "Florida Statutes §125.572") + ". For a lot backing onto "
            "Roberts Bay or any of the canals threading into the Intracoastal " + ext(WATERATLAS_RB_URL, "USF Water Atlas") + ", that 10-foot figure is the number to measure against before a single "
            "roll of turf gets ordered.</p>"
        ),
        (
            "Turf sidesteps the county's watering order, and suits Venice's older homeowners",
            "<p>Sarasota County, Venice included, sits under SWFWMD's Modified Phase III shortage order, limiting lawn irrigation to one day a week by address through March 2027 " +
            src("swfwmd-restrictions") + ". Turf, once installed and rinsed in, needs none of that watering at all. Venice's median age runs close to 69 " + src("acs-venice", "Census Reporter, Venice FL") +
            ", well above the statewide figure, and a low-maintenance yard that doesn't depend on a sprinkler schedule or regular mowing is a common ask from homeowners here who would rather spend a "
            "weekend on the water than on the lawn.</p>"
        ),
    ],
    "scenario": (
        "Replacing a dying strip of sod along a canal",
        "<p>Say a homeowner near Roberts Bay is ready to give up on 500 square feet of patchy St. Augustine along the back fence and switch to synthetic turf, keeping the new edge a full 10 feet "
        "back from the water rather than relying on a seawall exception. Pricing it at " + price("artificial-turf") + " per " + per("artificial-turf") + " puts the project between $5,000 and "
        "$12,500, tightening to roughly $6,000 to $9,000 inside the typical " + price("artificial-turf", typical=True) + " range for a washed-rock base with pet-friendly infill. Holding that "
        "10-foot line means nobody has to document whether a seawall is actually present, though a layout drawn any closer to the canal would need that question settled first. Once the "
        "installation is rinsed in, the yard drops off SWFWMD's watering calendar entirely.</p>"
    ),
    "faqs": [
        faq(
            "How far back from a Venice canal does artificial turf have to stay?",
            "At least 10 feet under the state's installation rule, unless the lot already has a seawall at the water's edge, in which case that particular buffer doesn't apply. The rule also keeps buried irrigation lines from running under the turf itself."
        ),
        faq(
            "Does installing turf get a yard out of Venice's current watering restrictions?",
            "Once it's down and rinsed in, yes. SWFWMD's Modified Phase III order still holds any remaining sod to one watering day a week through March 2027, but the turfed section no longer has to follow that calendar at all."
        ),
        faq(
            "Can a homeowners association in Venice refuse to allow artificial turf?",
            "Partly. State law limits how restrictive a local government's own turf rules can be, and DEP's rule sets the installation floor everyone has to meet, but an individual community's design guidelines, the kind Venetian Golf & River Club enforces through its ACC, can still add conditions on top of that."
        ),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
