# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "championsgate"

CDD_URL = "https://www.osceola.org/Government/Agencies-and-Departments-Directory/Community-Development-Districts"
MOVEMENTUM_URL = "https://movewithmomentum.com/neighborhoods/championsgate/"
SFWMD_FAQ_URL = "https://www.sfwmd.gov/sites/default/files/documents/yr_faqs_new.pdf"
SFWMD_KISS_URL = "https://www.sfwmd.gov/our-work/water-supply/upper-kissimmee"

SRC = [
    ("Osceola County, Community Development Districts directory", CDD_URL),
    ("MoveWithMomentum, ChampionsGate neighborhood guide", MOVEMENTUM_URL),
    ("SFWMD, Year-Round Landscape Irrigation FAQ", SFWMD_FAQ_URL),
    ("SFWMD, Upper Kissimmee Basin Water Supply Plan", SFWMD_KISS_URL),
    "osceola-parking-ord", "osceola-row-info", "osceola-homeowners", "osceola-permit-info",
    "nrcs-myakka-osd", "nrcs-basinger-osd", "nrcs-pomona-osd",
    "dep-rule", "fs125572",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("No city hall, no fixed driveway permit fee: Osceola County reviews every lot here",
        f"<p>ChampionsGate sits in unincorporated Osceola County, so a new driveway goes through the county's Community Development Building Office, 1 Courthouse Square, Suite 1400, Kissimmee, 407-742-0200, rather than a city building department "
        f"({src('osceola-permit-info', 'Osceola County, Permit Information')}). County code puts a hard number on driveway width that most jurisdictions leave vague: a residential driveway tops out at \"twenty-four (24) feet in width\" absent a conditional-use approval, and widening an existing driveway requires its own driveway permit "
        f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance §22-50.6')}).</p>"),
    sec("Two community development districts run the infrastructure behind the golf-resort brand",
        f"<p>Osceola County's own directory lists both the ChampionsGate Community Development District and the separate Stoneybrook South at ChampionsGate CDD among the special-purpose governments operating in the area "
        f"({ext(CDD_URL, 'Osceola County, Community Development Districts directory')}). Those CDDs fund and maintain the roads, drainage and landscaping behind the gates, which is separate from the county's own driveway and {svc('concrete-driveways', 'concrete')} permit review that still applies lot by lot.</p>"),
    sec("A county line runs through the middle of the community",
        f"<p>ChampionsGate sits at the I-4 and ChampionsGate Boulevard interchange, straddling the Polk and Osceola county line, with most addresses carrying a Davenport, 33896 mailing address even on the Osceola side "
        f"({ext(MOVEMENTUM_URL, 'MoveWithMomentum, ChampionsGate neighborhood guide')}). Because the jurisdiction a given lot falls under changes by street rather than by neighborhood name, confirming whether an address sits in unincorporated Osceola or unincorporated Polk is worth doing before a {cs('championsgate', 'concrete-driveways', 'driveway')} or {svc('paver-patios', 'patio')} permit is filed.</p>"),
    sec("Golf, a resort and whole-home rentals shape what gets built here",
        f"<p>Two Greg Norman-designed golf courses and the Omni Orlando Resort anchor the ChampionsGate brand, and part of the community operates as a short-term-rental resort district where whole-home nightly rentals are permitted "
        f"({ext(MOVEMENTUM_URL, 'MoveWithMomentum, ChampionsGate neighborhood guide')}). A pool deck, paver patio or turf installation on one of those rental homes gets built with heavier day-to-day use in mind than a typical owner-occupied lot nearby.</p>"),
    sec("Osceola's flatwoods soil holds water the ridge towns up in Lake County don't see",
        f"<p>Osceola County's share of the Kissimmee lowlands sits on poorly drained flatwoods soils including Myakka, Basinger and Pomona, each with a seasonal water table that can rise within a foot or two of the surface for months at a stretch "
        f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}; {src('nrcs-basinger-osd', 'NRCS, Basinger series')}; {src('nrcs-pomona-osd', 'NRCS, Pomona series')}). A base built for a ChampionsGate driveway or patio is managing that shallow water table far more than the excessively drained ridge sand common 25 miles north around Clermont and Groveland.</p>"),
    sec("The water district here runs a different clock than Lake County's",
        f"<p>ChampionsGate falls within the portion of Osceola County that the South Florida Water Management District, not SJRWMD, governs for irrigation, part of the tri-district Upper Kissimmee Basin area where SFWMD's boundary reaches north into Osceola and Polk "
        f"({ext(SFWMD_KISS_URL, 'SFWMD, Upper Kissimmee Basin Water Supply Plan')}). SFWMD's standing rule allows two watering days a week here, odd addresses Wednesday and Saturday and even addresses Thursday and Sunday, each before 10 a.m. or after 4 p.m., a materially looser calendar than the single-day order in force up in Lake County "
        f"({ext(SFWMD_FAQ_URL, 'SFWMD, Year-Round Landscape Irrigation FAQ')}).</p>"),
    sec("Retaining walls don't have a published height trigger in Osceola's own guidance",
        f"<p>Unlike the driveway-width number spelled out in county code, Osceola County's homeowner-facing permit pages don't list a specific height at which a retaining wall needs engineered, sealed plans "
        f"({src('osceola-homeowners', 'Osceola County, Homeowners')}). On the sloped sections of fairway-adjacent lots that back up to a golf-course pond, that makes a call to the Community Development Building Office, 407-742-0200, worth making before a {svc('retaining-walls', 'retaining wall')} design is finalized rather than assuming a threshold that isn't written down anywhere public.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("How wide can a driveway be in ChampionsGate?",
        "Twenty-four feet is the published ceiling under county code unless a conditional-use request clears that limit, and even widening an existing driveway has to go through its own driveway permit with Osceola County."),
    faq("Is ChampionsGate in Osceola County or Polk County?",
        "Both. The community straddles the county line near the I-4 interchange, and which county actually reviews a permit depends on the specific street and address rather than the ChampionsGate name itself."),
    faq("Does ChampionsGate have its own city government?",
        "No. It's unincorporated, governed day to day by community development districts that handle roads and amenities, with Osceola County (or Polk County, depending on the address) still reviewing building and driveway permits."),
    faq("How many watering days does ChampionsGate get under state rules?",
        "Two, under SFWMD's standard schedule for this part of Osceola County: odd addresses Wednesday and Saturday, even addresses Thursday and Sunday, each outside the 10 a.m. to 4 p.m. window."),
    faq("How do you pick a contractor for a ChampionsGate vacation-rental home?",
        f"Ask whether the crew has priced hardscape for rental-intensity use rather than a typical owner-occupied yard, confirm which county's permit office the address falls under, and check the contractor against the state's license lookup before signing. {post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')} has the rest of the checklist."),
]

HUB = page("/championsgate-fl/", "city", "Concrete, Pavers & Turf Contractor in ChampionsGate, FL",
           "Concrete, pavers and turf in ChampionsGate, FL: Osceola County's 24-foot driveway cap, the Polk/Osceola county line, and SFWMD's watering schedule, Oct. 2026.",
           "Concrete, Pavers and Artificial Turf for ChampionsGate, Florida Homes",
           capsule(f"ChampionsGate is an unincorporated golf-resort community straddling the Osceola-Polk county line, about 24 miles from Orlando, built around two Greg Norman courses and the Omni Orlando Resort. "
                   f"Opera's crews pour concrete driveways, build paver patios and install artificial turf for homes here, with a new driveway priced at {price('concrete-driveway')} per {per('concrete-driveway')} under Osceola County's 24-foot driveway-width cap, October 2026 figures."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="ChampionsGate",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/kissimmee-fl/", "Concrete, pavers and turf in Kissimmee"),
                    ("/celebration-fl/", "Concrete, pavers and turf in Celebration"),
                    ("/davenport-fl/", "Concrete, pavers and turf in Davenport"),
                    ("/retaining-wall-cost/", "Retaining wall cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in ChampionsGate, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in ChampionsGate, FL – 24-Ft Cap",
    "meta": "Concrete driveway contractors in ChampionsGate, FL: Osceola County's 24-foot width cap under §22-50.6 and the county driveway permit, Oct. 2026.",
    "h1": "Concrete Driveways for ChampionsGate Homes",
    "lede": capsule(f"Osceola County's current concrete driveway range for ChampionsGate runs {price('concrete-driveway')} per {per('concrete-driveway')}, October 2026 figures. "
                     "The county's own ordinance names 24 feet as the top width for a residential driveway here, with anything beyond that needing a conditional-use approval first, a specific published figure most Orlando-unit jurisdictions leave out of their code entirely."),
    "sections": [
        ("The 24-foot cap is written into county code, not left to a reviewer's judgment",
         f"<p>Osceola County's parking ordinance sets the number at \"twenty-four (24) feet in width,\" the cap for a residential driveway absent a conditional-use approval, and a separate clause requires that construction or widening \"be authorized by the issuance of a driveway permit by Osceola County\" "
         f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance §22-50.6')}). A {cs('championsgate', 'concrete-driveways', 'circular or side-load driveway')} common on larger ChampionsGate lots has to be designed against that 24-foot figure from the start rather than scaled back after a permit review.</p>"),
        ("Where the address sits decides which county's office reviews the job",
         f"<p>With ChampionsGate straddling the Osceola-Polk line, a driveway permit for one street runs through Osceola County's Community Development Building Office, 407-742-0200, while a lot a few blocks over on the Polk County side goes through that county's own building division instead "
         f"({src('osceola-permit-info', 'Osceola County, Permit Information')}). Confirming the county before a crew submits paperwork avoids a rejected application on an address that looks identical to its neighbors.</p>"),
    ],
    "scenario": ("A circular driveway at the 24-foot limit, worked out in square feet",
                 f"<p>A ChampionsGate home building a circular driveway at the maximum 24-foot width, with a 60-foot run on each side of the loop, comes to roughly 1,440 square feet once the center island is excluded. At the {price('concrete-driveway')} per {per('concrete-driveway')} range, that prices out to somewhere between $8,640 and $21,600 depending on finish. "
                 "Because the county's 24-foot cap applies to the driveway's width rather than its total footprint, a wider center island or a decorative apron section can still be designed in without pushing the loop itself past the limit.</p>"),
    "faqs": [
        faq("Can a ChampionsGate driveway be wider than 24 feet?",
            "Only with Osceola County's approval for a conditional use; the standard code limit for a residential driveway is 24 feet wide."),
        faq("Does widening an existing ChampionsGate driveway need a new permit?",
            "Yes. Osceola County code requires its own driveway permit for construction or widening, not just a modification to an existing building permit."),
        faq("Which office handles a ChampionsGate driveway permit?",
            "It depends on which side of the Osceola-Polk line the address falls on; Osceola County's Community Development Building Office handles the Osceola side, while Polk County's building division handles the other."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in ChampionsGate, FL – Resort Homes",
    "meta": "Paver patio installers in ChampionsGate, FL: building for rental-intensity pool decks near the Omni Resort and golf courses, Oct. 2026.",
    "h1": "Paver Patios for ChampionsGate Homes",
    "lede": capsule(f"Paver patio work in ChampionsGate is pricing at {price('paver-patio')} per {per('paver-patio')} this October 2026, current Florida figures. "
                     "With a meaningful share of ChampionsGate homes operating as whole-home vacation rentals near the Omni Orlando Resort, a paver patio or pool deck here is more often built for daily guest turnover than for a single owner-occupied family."),
    "sections": [
        ("Rental-intensity use changes what a patio has to hold up to",
         f"<p>ChampionsGate's resort district, built around the Omni Orlando Resort and two Greg Norman golf courses, allows whole-home nightly rentals on part of the community "
         f"({ext(MOVEMENTUM_URL, 'MoveWithMomentum, ChampionsGate neighborhood guide')}). A {svc('paver-patios', 'paver patio')} or pool deck on one of those homes sees a new set of guests cycling through most weeks of the year, which is a reason a denser edge restraint and a tighter joint-sand spec come up more often on a ChampionsGate quote than on a lot a family has lived in for a decade.</p>"),
        ("Flatwoods ground means drainage planning starts before the first paver is set",
         f"<p>Much of Osceola County's share of ChampionsGate sits on Myakka and Basinger flatwoods soil, both holding a seasonal water table close to the surface for months of the year "
         f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}; {src('nrcs-basinger-osd', 'NRCS, Basinger series')}). A patio base here is built with that shallow water table in mind from the compaction stage on, rather than assuming the fast drainage common on the sand-ridge lots up around Clermont and Groveland.</p>"),
    ],
    "scenario": ("A rental-home pool deck extension, worked out in square feet",
                 f"<p>A ChampionsGate vacation home extending its paver pool deck by 22 by 18 feet, 396 square feet, to add lounge seating for a larger guest group comes to roughly $3,960 to $6,732 at the {price('paver-patio')} per {per('paver-patio')} figure. "
                 "Given the shallow water table common on these lots, the crew checks the base compaction against the flatwoods soil rather than assuming the lighter prep a ridge-sand lot would need for the same square footage.</p>"),
    "faqs": [
        faq("Do ChampionsGate vacation-rental patios need a different build than an owner-occupied home?",
            "Often, yes, since guest turnover adds wear a typical owner-occupied yard doesn't see, which is why a tighter edge restraint and joint-sand spec come up more often on those quotes."),
        faq("Does a ChampionsGate paver patio need a county permit?",
            "Yes, reviewed by Osceola or Polk County's building office depending on the address; confirming which county applies before the project is designed avoids a misfiled application."),
        faq("Why does the soil matter more for a ChampionsGate patio than for one near Clermont?",
            "The ground here is poorly drained flatwoods soil with a seasonal water table close to the surface, unlike the fast-draining ridge sand common 25 miles north, so the patio base is built to manage standing water rather than loose, dry sand."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in ChampionsGate, FL – Golf-Pond Lots",
    "meta": "Artificial turf installers in ChampionsGate, FL: the state buffer near golf-course ponds and SFWMD's two-day watering schedule, Oct. 2026.",
    "h1": "Artificial Turf for ChampionsGate Yards",
    "lede": capsule(f"Turf installation around ChampionsGate is priced at {price('artificial-turf')} per {per('artificial-turf')}, October 2026 Florida figures. "
                     "A lot of ChampionsGate's lots back onto one of the community's golf-course ponds rather than a natural lake, and the state's turf buffer treats that water the same way it treats any other pond, lake or canal."),
    "sections": [
        ("A golf-course pond counts the same as a natural lake under the state rule",
         f"<p>Two Greg Norman-designed courses wind through ChampionsGate, and the irrigation ponds that shape those fairways border a sizable share of the community's backyards "
         f"({ext(MOVEMENTUM_URL, 'MoveWithMomentum, ChampionsGate neighborhood guide')}). Florida's synthetic-turf standard doesn't distinguish a constructed golf pond from a natural lake: either way, installed turf has to stop 10 feet short of the water's edge, on a washed base with natural infill and no buried irrigation line underneath "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}).</p>"),
        ("Two watering days a week, not one, under this community's water district",
         f"<p>ChampionsGate's portion of Osceola County sits inside the South Florida Water Management District's territory, where the standing rule allows watering twice a week, odd addresses on Wednesday and Saturday and even addresses on Thursday and Sunday, each outside the 10 a.m. to 4 p.m. window "
         f"({ext(SFWMD_FAQ_URL, 'SFWMD, Year-Round Landscape Irrigation FAQ')}). That's a looser calendar than Lake County's current single-day emergency order, which gives new sod on a ChampionsGate lot more of a chance to establish before {svc('artificial-turf', 'turf')} becomes the fallback for a stubborn patch.</p>"),
    ],
    "scenario": ("Turf along a golf-pond lot line, worked out in square feet",
                 f"<p>A ChampionsGate backyard backing onto a golf-course pond, fenced at 600 square feet, loses roughly 80 square feet to the required 10-foot buffer, leaving about 520 square feet available for turf. At the {price('artificial-turf')} per {per('artificial-turf')} range, that comes to around $5,200 to $13,000 depending on pile height and infill. "
                 "Because the pond's edge is a built landscape feature rather than a natural shoreline, the buffer still gets measured and marked the same way a lot backing onto a natural lake would require.</p>"),
    "faqs": [
        faq("Does the state turf buffer apply to golf-course ponds in ChampionsGate?",
            "Yes. Florida's synthetic-turf rule treats a constructed golf-course pond the same as a natural lake or canal, requiring installed turf to stay at least 10 feet from the water's edge."),
        faq("How many days a week can a ChampionsGate lawn be watered?",
            "Two, under SFWMD's standard schedule for this part of Osceola County: odd addresses Wednesday and Saturday, even addresses Thursday and Sunday, outside the 10 a.m. to 4 p.m. window."),
        faq("Is turf a common choice on ChampionsGate vacation-rental lots?",
            "It comes up often for smaller side yards and pet areas on rental homes, where low upkeep between guest turnovers matters more than it would on an owner-occupied lot."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
