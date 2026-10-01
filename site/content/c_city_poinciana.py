# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "poinciana"

APV_URL = "https://www.apvcommunity.com/villages-of-poinciana"
WIKI_URL = "https://en.wikipedia.org/wiki/Poinciana,_Florida"
CENSUS_URL = "http://censusreporter.org/profiles/16000US1257900-poinciana-fl/"
POLK_FAQ_URL = "https://www.polkfl.gov/services/building/faqs/"
PARKWAY_URL = "https://en.wikipedia.org/wiki/Florida_State_Road_538"
SFWMD_FAQ_URL = "https://www.sfwmd.gov/sites/default/files/documents/yr_faqs_new.pdf"

SRC = [
    ("Association of Poinciana Villages, Understanding Your HOA", APV_URL),
    ("Wikipedia, Poinciana, Florida", WIKI_URL),
    ("Census Reporter, Poinciana, FL", CENSUS_URL),
    ("Polk County Building Division, Building FAQ", POLK_FAQ_URL),
    ("Wikipedia, Florida State Road 538 (Poinciana Parkway)", PARKWAY_URL),
    ("SFWMD, Year-Round Landscape Irrigation FAQ", SFWMD_FAQ_URL),
    "osceola-parking-ord", "osceola-permit-info", "osceola-homeowners",
    "nrcs-myakka-osd", "nrcs-basinger-osd", "nrcs-felda-osd",
    "dep-rule", "fs125572",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("One community, two counties: the permit office changes at the Osceola-Polk line",
        f"<p>Poinciana is a single census-designated place split between two counties, its north side in Osceola and its south side in Polk "
        f"({ext(WIKI_URL, 'Wikipedia, Poinciana, Florida')}). On the Osceola side, a driveway permit and the county's 24-foot residential width cap run through the Community Development Building Office in Kissimmee "
        f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance §22-50.6')}); cross into the Polk County villages and the same driveway, a concrete slab against the house, or a section of sidewalk in the right-of-way instead goes through Polk's Building Division in Bartow, 863-534-6080 "
        f"({ext(POLK_FAQ_URL, 'Polk County Building Division, Building FAQ')}).</p>"),
    sec("Florida's largest HOA runs the community's own public works behind both counties",
        f"<p>The Association of Poinciana Villages, organized in 1972 by original developer Avatar out of ten separate village sub-associations, functions as what the community itself calls its only local government, supplementing county services with public works, parks and recreation while enforcing the original deed restrictions "
        f"({ext(APV_URL, 'Association of Poinciana Villages, Understanding Your HOA')}). Its Design Control Board reviews exterior changes, including {svc('paver-patios', 'paver')} and {svc('concrete-driveways', 'driveway')} work, against standards meant to keep the villages' original design consistent, a review that runs alongside whichever county's permit applies to a given address.</p>"),
    sec("Polk's own permit rules name pavers, slabs and retaining walls specifically",
        f"<p>Polk County's building guidance spells out, by category, that pavers set within required setbacks or next to a structure need a permit, that a concrete slab built to support a structure or that sits in the right-of-way or a setback needs one too, and that a retaining wall built for structural support, protection or erosion control needs a permit as well, with a plans examiner available by phone for a decorative wall "
        f"({ext(POLK_FAQ_URL, 'Polk County Building Division, Building FAQ')}). That's a more itemized list than many jurisdictions publish, and it applies to the southern half of Poinciana specifically.</p>"),
    sec("A toll road built to connect, not just cross, the two counties",
        f"<p>The Poinciana Parkway, State Road 538, opened in 2016 as a 7.2-mile toll connection running from US 17-92 and Kinny Harmon Road in Osceola County into Cypress Parkway on the Polk County side, crossing Reedy Creek Swamp on a 6,200-foot bridge built to keep the wildlife corridor beneath it open "
        f"({ext(PARKWAY_URL, 'Wikipedia, Florida State Road 538')}). That bridge is a reminder of how much wetland still threads through the area even as the villages around it have filled in with rooftops.</p>"),
    sec("From under 7,000 residents to more than 81,000 in three and a half decades",
        f"<p>Poinciana counted 6,753 residents in 1990, 13,647 by 2000, a jump to 53,193 by 2010 and 69,309 by 2020; Census Reporter's current estimate puts the CDP at 81,260 "
        f"({ext(WIKI_URL, 'Wikipedia, Poinciana, Florida')}; {ext(CENSUS_URL, 'Census Reporter, Poinciana, FL')}). That growth curve means most of the concrete and pavers going into the ground across the villages belong to homes built well after 2000, with the community's own real-estate data putting the typical construction year around 2005.</p>"),
    sec("Flatwoods soil and a water district most of Polk County doesn't share",
        f"<p>Myakka, Basinger and Felda are the soil series that turn up most often under Poinciana's villages, flatwoods ground where the water table can rise to within a couple of feet of grade for a good part of the year "
        f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}; {src('nrcs-basinger-osd', 'NRCS, Basinger series')}; {src('nrcs-felda-osd', 'NRCS, Felda series')}). Because Poinciana sits in the Kissimmee River basin rather than the Peace River side of Polk County, it falls under the South Florida Water Management District's two-day-a-week schedule rather than the tighter, once-a-week order most of Polk County is currently living under from a different district "
        f"({ext(SFWMD_FAQ_URL, 'SFWMD, Year-Round Landscape Irrigation FAQ')}).</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Is Poinciana in Osceola County or Polk County?",
        "Both. The community is a single census-designated place split by the county line, with the north side in Osceola County and the south side in Polk County, each reviewing its own building and driveway permits."),
    faq("Does Poinciana have its own city government?",
        "No. It's unincorporated in both counties. The Association of Poinciana Villages, the state's largest HOA, functions as the community's only local government, supplementing county services and enforcing the original deed restrictions."),
    faq("Does Polk County require a permit for a paver patio in Poinciana?",
        "Yes, where the pavers sit within a required setback or next to a structure. Polk County's own guidance lists that requirement specifically, alongside separate rules for slabs and retaining walls."),
    faq("Is Poinciana under the same watering restrictions as the rest of Polk County?",
        "No. Because Poinciana sits in the Kissimmee River basin, it falls under the South Florida Water Management District's twice-a-week schedule rather than the stricter once-a-week order in effect for most of Polk County under a different district."),
    faq("How do you choose a concrete contractor for a home in Poinciana?",
        f"Confirm which county the address falls under before pricing the permit, ask whether the bid accounts for the Association of Poinciana Villages' Design Control Board review, and check the contractor against the state's license lookup. {post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')} covers the remaining checks."),
]

HUB = page("/poinciana-fl/", "city", "Concrete, Pavers & Turf Contractor in Poinciana, FL",
           "Concrete, pavers and turf in Poinciana, FL: the Osceola-Polk county split, the Association of Poinciana Villages, and Polk's own permit list, Oct. 2026.",
           "Concrete, Pavers and Artificial Turf for Poinciana, Florida Homes",
           capsule(f"Split between Osceola and Polk counties and governed day to day by the Association of Poinciana Villages, Poinciana has grown to roughly 81,260 residents about 28 miles from Orlando. "
                   f"Opera's crews handle concrete, pavers and artificial turf on both sides of that county line; a new concrete driveway prices at {price('concrete-driveway')} per {per('concrete-driveway')}, current Florida figures for October 2026."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Poinciana",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/kissimmee-fl/", "Concrete, pavers and turf in Kissimmee"),
                    ("/davenport-fl/", "Concrete, pavers and turf in Davenport"),
                    ("/championsgate-fl/", "Concrete, pavers and turf in ChampionsGate"),
                    ("/retaining-wall-cost/", "Retaining wall cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Poinciana, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Poinciana, FL – Two Counties",
    "meta": "Concrete driveway contractors in Poinciana, FL: Osceola's 24-foot cap on one side of the line, Polk's slab permit rules on the other, Oct. 2026.",
    "h1": "Concrete Driveways for Poinciana Homes",
    "lede": capsule(f"A new concrete driveway in Poinciana currently prices between {price('concrete-driveway')} per {per('concrete-driveway')}, October 2026 Florida figures. "
                     "Which office reviews the job depends on the county: Osceola's side of the community caps driveway width at 24 feet in its own code, while Polk's side instead names a concrete slab directly in its permit list."),
    "sections": [
        ("Osceola's villages fall under the county-wide 24-foot driveway limit",
         f"<p>On the Osceola side of Poinciana, the county's parking ordinance sets a residential driveway's width at \"twenty-four (24) feet\" absent a conditional-use approval for something wider, with a separate driveway permit required for new construction or widening "
         f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance §22-50.6')}). The Community Development Building Office, 407-742-0200, is the county contact for that permit before a {cs('poinciana', 'concrete-driveways', 'driveway')} crew is scheduled.</p>"),
        ("Polk's villages name the slab itself, not just the right-of-way apron",
         f"<p>Cross into the Polk County side of the community, and the rule changes: Polk's own guidance requires a permit for a concrete slab that supports a structure, sits elevated, or falls within the right-of-way or a required setback, reviewed by the county's Building Division in Bartow, 863-534-6080 "
         f"({ext(POLK_FAQ_URL, 'Polk County Building Division, Building FAQ')}). A driveway replacement that stays entirely within an existing footprint, away from any setback, is the kind of detail worth confirming with that office before assuming the Osceola-side rule applies.</p>"),
    ],
    "scenario": ("A driveway widening split across the two-county line, worked out in square feet",
                 f"<p>A Poinciana homeowner on the Osceola side widening a 20 by 20 foot driveway by 5 feet to fit a boat trailer adds 100 square feet, landing at 500 total. At the {price('concrete-driveway')} per {per('concrete-driveway')} range, that pour runs roughly $3,000 to $7,500, still inside the county's 24-foot width cap for the finished driveway. "
                 "A few streets south in the Polk County villages, that same addition would instead be checked against Polk's setback and right-of-way rules for a concrete slab, a different review even though the finished product looks identical.</p>"),
    "faqs": [
        faq("Does Osceola County's 24-foot driveway cap apply across all of Poinciana?",
            "Only on the Osceola side of the community. South of the county line, Polk County reviews driveway and slab work under its own permit rules rather than the 24-foot width cap."),
        faq("Does a driveway replacement in the Polk County side of Poinciana need a permit?",
            "It depends on whether the slab supports a structure, sits elevated, or falls within a setback or the right-of-way; Polk County's guidance lists those specifically as requiring a permit."),
        faq("Who do I call to confirm which county my Poinciana address falls under?",
            "The Association of Poinciana Villages can usually confirm which village and county an address sits in, and each county's building office, Osceola at 407-742-0200 or Polk at 863-534-6080, can confirm the permit requirement from there."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Poinciana, FL – HOA Review",
    "meta": "Paver patio installers in Poinciana, FL: the Design Control Board's review and Polk County's setback-based permit rule for pavers, Oct. 2026.",
    "h1": "Paver Patios for Poinciana Backyards",
    "lede": capsule(f"{price('paver-patio')} per {per('paver-patio')} is the going Florida range for a paver patio in Poinciana this October 2026. "
                     "Every village in the community answers to the Association of Poinciana Villages' Design Control Board for exterior changes, and on the Polk County side, pavers set near a structure or inside a setback also trigger the county's own permit."),
    "sections": [
        ("The Design Control Board reviews exterior work across every village, regardless of county",
         f"<p>The Association of Poinciana Villages describes its Design Control Board's purpose as acquainting builders and homeowners with the standards used to keep the community's design consistent, staffed by resident volunteers who meet twice a month to review applications "
         f"({ext(APV_URL, 'Association of Poinciana Villages, Understanding Your HOA')}). That review applies the same way whether the lot sits in the Osceola or Polk half of the community, which makes it a constant across a {svc('paver-patios', 'paver patio')} project even when the county permit process itself changes.</p>"),
        ("Polk's setback rule is the detail that decides whether a county permit is even needed",
         f"<p>On the Polk County side, pavers installed within a required setback or next to an existing structure need a county permit, under guidance that also meets Building Code and Land Development Code drainage standards "
         f"({ext(POLK_FAQ_URL, 'Polk County Building Division, Building FAQ')}). A patio set well back from any setback line on a larger Polk-side lot can sometimes avoid that trigger, something worth confirming with the county's Building Division before the Design Control Board application goes in.</p>"),
    ],
    "scenario": ("A patio addition reviewed by the village association first, worked out in square feet",
                 f"<p>A Poinciana homeowner adding an 18 by 16 foot paver patio off the back of the house, 288 square feet, submits the plan to the Design Control Board before ordering material, regardless of which county the village sits in. At the {price('paver-patio')} per {per('paver-patio')} range, that patio prices out to roughly $2,880 to $4,896. "
                 "If the lot happens to fall on the Polk County side and the patio's edge lands inside a required setback, that same project also needs a county permit on top of the association's sign-off.</p>"),
    "faqs": [
        faq("Does every Poinciana village require Design Control Board approval for a patio?",
            "Yes. The Association of Poinciana Villages' review applies community-wide, regardless of which county a specific village sits in."),
        faq("Does a Poinciana paver patio always need a county permit too?",
            "On the Polk County side, only if the pavers fall within a required setback or next to a structure. The Osceola side's paver rules are reviewed separately through that county's own permitting process."),
        faq("How long does the Design Control Board take to review a patio application?",
            "The board meets twice a month to go through submitted applications, so timing a patio's design around that schedule can shorten the wait compared to filing right before a meeting."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Poinciana, FL – Wetland Buffers",
    "meta": "Artificial turf installers in Poinciana, FL: the state's 10-foot wetland buffer near Reedy Creek Swamp and SFWMD's two-day schedule, Oct. 2026.",
    "h1": "Artificial Turf for Poinciana Yards",
    "lede": capsule(f"Turf installation across Poinciana is priced at {price('artificial-turf')} per {per('artificial-turf')}, current Florida figures for this fall. "
                     "Reedy Creek Swamp and the wetlands connected to it run through enough of the area that a drainage canal borders more backyards here than in a community without that much open water nearby, which brings the state's turf buffer into play on more lots."),
    "sections": [
        ("Wetland-adjacent lots carry the same 10-foot rule as a lakefront yard",
         f"<p>Poinciana Parkway's own 6,200-foot bridge over Reedy Creek Swamp exists specifically to keep a wildlife corridor open beneath the road, a sign of how much wetland still runs through the area despite decades of village construction around it "
         f"({ext(PARKWAY_URL, 'Wikipedia, Florida State Road 538')}). Florida's statewide turf rule doesn't carve out an exception for a canal or drainage feature tied to that wetland system: installed turf still has to sit at least 10 feet back from the water's edge, on a washed base with no buried irrigation underneath "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}).</p>"),
        ("Where a lot sits decides the watering calendar sod has to survive on",
         f"<p>Poinciana's position in the Kissimmee River basin puts it under South Florida Water Management District rules instead of the water-shortage order covering most of the rest of Polk County, which works out to twice-weekly watering on a split calendar, Wednesday or Saturday for odd addresses and Thursday or Sunday for even ones, kept to the hours outside 10 a.m. to 4 p.m. "
         f"({ext(SFWMD_FAQ_URL, 'SFWMD, Year-Round Landscape Irrigation FAQ')}). A 2025 state law also limits how far either county can tighten residential turf rules beyond the statewide standard "
         f"({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Turf near a drainage canal, worked out in square feet",
                 f"<p>A Poinciana backyard bordering a neighborhood drainage canal, fenced at 560 square feet, loses about 70 square feet once the required 10-foot buffer is marked off, leaving roughly 490 square feet to install. Priced against the {price('artificial-turf')} per {per('artificial-turf')} figure, that works out to somewhere near $4,900 to $12,250, depending on the pile height and infill chosen. "
                 "Because the canal connects to the area's larger wetland system, the layout gets measured against the buffer before the base is cut rather than assumed from a fence line alone.</p>"),
    "faqs": [
        faq("Is a Poinciana drainage canal treated the same as a lake under the turf rule?",
            "Yes. Florida's synthetic-turf rule applies the same 10-foot buffer to a canal connected to the area's wetland system as it does to a lake, unless the edge is a seawall."),
        faq("How many watering days does Poinciana get each week?",
            "Two, under the South Florida Water Management District's schedule that covers this part of the Kissimmee basin, rather than the stricter once-a-week order in effect for most of the rest of Polk County."),
        faq("Does an HOA review apply to turf installation in Poinciana the same as a patio?",
            "The Association of Poinciana Villages' Design Control Board reviews exterior changes broadly, so confirming whether a specific turf plan needs that sign-off is worth doing before the base is cut."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
