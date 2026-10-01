# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "avalon-park"

COUNTY_URL = "https://www.orangecountyfl.net/PlanningDevelopment/AvalonPark.aspx"
ABOUT_URL = "https://avalonparkorlando.com/about/"
NRCS_SMYRNA_URL = "https://soilseries.sc.egov.usda.gov/OSD_Docs/S/SMYRNA.html"

SRC = [
    ("Orange County Government, Avalon Park", COUNTY_URL),
    ("Avalon Park Orlando, About", ABOUT_URL),
    "orange-do-i-need-permit", "orange-residential-pavers", "orange-lot-grading", "orange-res-plan-guide",
    "sjrwmd-watering", "dep-rule", "fs125572", "fs720-3045", "nrcs-smyrna-osd", "nrcs-myakka-osd",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("No city hall here: Orange County runs every permit",
        f"<p>Avalon Park was never incorporated as its own town; it's an unincorporated Orange County community, so every driveway, slab or paver job inside it is reviewed by the county's own Division of Building Safety rather than a city office "
        f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}). The county's own language is blunt about it: \"anytime you are pouring concrete or placing pavers, a permit is required,\" with pavers specifically routed through a zoning permit rather than the fuller building-permit review a poured slab gets "
        f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}).</p>"),
    sec("A 1998 planned development built as its own village cluster",
        f"<p>Orange County approved Avalon Park as a 1,860-acre Planned Development in 1998, a Traditional Neighborhood Development laid out in New Urbanism fashion around a central Town Center, with roughly 3,400 single-family homes and 1,431 multifamily units built out around it "
        f"({ext(COUNTY_URL, 'Orange County Government, Avalon Park')}; {ext(ABOUT_URL, 'Avalon Park Orlando, About')}). That PD status means a homeowner here answers to both the county's standard permit review and the project's own county-approved design standards, a second layer most unincorporated Orange County lots don't carry.</p>"),
    sec("Two hundred fifty acres of lakes built into the site plan",
        f"<p>Avalon Park's own description of itself counts 240 acres of preserved wetlands, 400 acres of upland preserve and 250 acres of man-made lakes woven through its villages "
        f"({ext(ABOUT_URL, 'Avalon Park Orlando, About')}), acreage that exists because the ground under much of east Orange County drains poorly to begin with. Myakka and Smyrna, the two flatwoods soil series most common across this stretch of the county, are both built on a shallow, slow-moving water table that the USDA pegs within a foot and a half of grade for part of a typical year "
        f"({src('nrcs-smyrna-osd', 'NRCS soil survey, Smyrna series')}), a drainage profile the development's own lake network was clearly sized around rather than fought.</p>"),
    sec("The county's own driveway spec, inches and feet",
        f"<p>Orange County's residential lot-grading policy spells out the driveway apron itself: a minimum 6-inch-thick, 3,000-psi slab, set back at least 3 feet from the property line, with one driveway allowed per lot where the frontage runs under 100 feet "
        f"({src('orange-lot-grading', 'Orange County, Residential Lot Grading Policy')}). A {svc('retaining-walls', 'retaining wall')} holding back more than 4 feet of fill, or one over 2 feet that also resists a lateral load, needs its own signed and sealed engineering under the county's residential plan guide "
        f"({src('orange-res-plan-guide', 'Orange County, A Guide for Residential Plan Approval')}).</p>"),
    sec("Newer construction than most of the Orange County towns nearby",
        f"<p>Avalon Park's villages have been filling in since the PD's 1998 approval, which puts the bulk of its {svc('concrete-driveways', 'driveways')}, patios and pool decks at under three decades old, younger than the median home in Winter Park, Belle Isle or Maitland. Younger concrete here means {svc('concrete-repair', 'resurfacing')} is the exception rather than the rule, and most calls into the community are for new work rather than replacing an original 1980s pour.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Avalon Park have its own building department?",
        f"No. Avalon Park is unincorporated Orange County, so the county's Division of Building Safety reviews every driveway, slab and paver permit rather than a city office "
        f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')})."),
    faq("Is a paver patio reviewed differently than a poured concrete one in Avalon Park?",
        "Yes, under county rules. Pouring concrete needs a building permit, while placing pavers on a driveway or walkway goes through a zoning permit instead, a lighter review with its own fee and site-plan requirement."),
    faq("Why does Avalon Park have so many ponds and lakes built into it?",
        "The 1998 planned development set aside 250 acres for man-made lakes alongside 240 acres of wetlands and 400 acres of upland preserve, acreage that also answers to the poorly drained flatwoods soil underneath much of the surrounding area."),
    faq("Does Avalon Park's HOA add anything on top of the county permit?",
        "The community sits inside a county-approved Planned Development with its own design standards, on top of the standard permit review, so an exterior project here typically clears both the county's sign-off and the development's own architectural process."),
    faq("Is Avalon Park's concrete newer than other Orange County communities?",
        "Generally yes. The development has been building out since 1998, so most of its driveways, patios and pool decks are still under three decades old, younger than the typical home in several incorporated Orange County cities nearby."),
    faq("What should a homeowner in Avalon Park confirm before hiring a contractor?",
        f"Nail down whether the job needs the county's full building permit or the lighter zoning permit that covers pavers, ask how the quote accounts for the development's own design review on top of that, and run the company through the state's license search before signing. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'See our concrete-contractor guide')} for the rest of what a solid bid should include."),
]

HUB = page("/avalon-park-fl/", "city", "Concrete, Pavers & Turf Contractor in Avalon Park, FL",
           "Concrete, pavers and turf in Avalon Park, FL: Orange County's own permit rules, 250 acres of built-in lakes, and a 1998 planned-development layout, October 2026.",
           "Concrete, Pavers and Artificial Turf for Avalon Park Homes",
           capsule(f"Opera pours concrete and lays pavers and artificial turf for Avalon Park, a 1,860-acre unincorporated Orange County community east of Orlando built around a Town Center and roughly 250 acres of man-made lakes. "
                   f"A concrete driveway here falls in the {price('concrete-driveway')} per {per('concrete-driveway')} market range this October, reviewed through Orange County's own permit process rather than a city hall."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Avalon Park",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/orlando-fl/", "Concrete, pavers and turf in Orlando"),
                    ("/lake-nona-fl/", "Concrete, pavers and turf in Lake Nona"),
                    ("/blog/orange-county-orlando-driveway-patio-permits/", "Orlando and Orange County permits"),
                    ("/compare/concrete-vs-pavers/", "Concrete vs. pavers")],
           eyebrow="Concrete · Pavers · Turf in Avalon Park, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways -------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Avalon Park, FL",
    "meta": "Concrete driveway contractors in Avalon Park, FL: Orange County's 6-inch, 3,000-psi apron spec, and the one-driveway-per-lot rule, October 2026.",
    "h1": "Pouring a Concrete Driveway in Avalon Park",
    "lede": capsule(f"A concrete driveway in Avalon Park falls in the {price('concrete-driveway')} per {per('concrete-driveway')} market range this October. "
                     "Because the community sits in unincorporated Orange County, every driveway permit runs through the county's own Division of Building Safety rather than a town building department."),
    "sections": [
        ("A county permit and a specific apron spec",
         f"<p>The county requires a permit for any new or widened driveway, and its residential lot-grading policy spells out the apron itself: minimum 6-inch-thick, 3,000-psi concrete, with non-steel reinforcement anywhere the apron crosses the right-of-way "
         f"({src('orange-lot-grading', 'Orange County, Residential Lot Grading Policy')}). A lot with under 100 feet of frontage is limited to one driveway, a rule that can matter on Avalon Park's narrower village lots more than on wider suburban ones elsewhere in the county.</p>"),
        ("Three feet from the line, and a second layer from the community itself",
         f"<p>Orange County sets a minimum 3-foot setback from the property line for a residential driveway "
         f"({src('orange-lot-grading', 'Orange County, Residential Lot Grading Policy')}). On top of that county review, Avalon Park's own status as a county-approved Planned Development means the project's design standards weigh in on a driveway's visible details, color and material included, a second check most unincorporated lots outside a PD don't have "
         f"({ext(COUNTY_URL, 'Orange County Government, Avalon Park')}).</p>"),
    ],
    "scenario": ("A driveway upgrade on a newer Avalon Park lot, worked out in square feet",
                 f"<p>Say a home built within the last two decades of Avalon Park's build-out widens its 10 by 20 foot driveway, 200 square feet, to a 20 by 22 foot layout, 440 square feet, for a second vehicle. At {price('concrete-driveway')} per {per('concrete-driveway')}, that comes to roughly $2,640 to $6,600 before the county's permit fee, and because the lot carries under 100 feet of frontage, the county's one-driveway limit is worth confirming before the wider apron gets designed.</p>"),
    "faqs": [
        faq("Who issues a driveway permit in Avalon Park?",
            "Orange County's Division of Building Safety, since Avalon Park is an unincorporated community with no city building department of its own."),
        faq("What thickness and strength does an Avalon Park driveway apron need?",
            "The county's lot-grading policy calls for a minimum 6-inch-thick, 3,000-psi slab, with non-steel reinforced concrete specifically wherever the apron sits inside the right-of-way."),
        faq("Can a narrow Avalon Park lot have two driveways?",
            "Not under the county's standard rule. A lot with less than 100 feet of frontage is limited to one driveway unless a conditional use is separately approved."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios & Walkways in Avalon Park, FL",
    "meta": "Paver patio installers in Avalon Park, FL: the county's zoning-permit path for pavers, and the 40% open-space rule, October 2026.",
    "h1": "Paver Patios and Walkways for an Avalon Park Home",
    "lede": capsule(f"A paver patio or walkway in Avalon Park runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "Orange County reviews pavers through a zoning permit rather than the fuller building-permit path a poured slab gets, though the same open-space math applies to either one."),
    "sections": [
        ("A lighter review, with its own paperwork",
         f"<p>Orange County's rule is specific: \"pavers require a zoning permit only,\" filed with a dimensioned site plan showing property lines, easements and the paver's location, plus a flat $38 permit fee and a $38 development-engineering review fee "
         f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). A paver patio that sits inside a recorded easement needs an easement acknowledgement form added to that same submission.</p>"),
        ("Forty percent open space, county-wide",
         f"<p>Orange County's code sets residential private open space at a minimum of 40 percent of the lot "
         f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}), the flip side of the same coverage math other jurisdictions express as a maximum impervious percentage. A {svc('paver-patios', 'paver patio')} added to a lot that already carries a full driveway and house footprint is weighed against that 40 percent floor before the layout is finalized.</p>"),
    ],
    "scenario": ("A paver patio reviewed under the county's zoning permit, worked out in square feet",
                 f"<p>Picture an Avalon Park home adding a 15 by 16 foot paver patio, 240 square feet, off the back of the house. At {price('paver-patio')} per {per('paver-patio')} for that footprint, the job runs roughly $2,400 to $3,840, plus the county's combined $76 in zoning and engineering review fees, filed with a site plan rather than the fuller building-permit package a poured-concrete version of the same patio would need.</p>"),
    "faqs": [
        faq("Does a paver patio in Avalon Park need a full building permit?",
            "No. Orange County reviews pavers through a zoning permit specifically, a lighter process than the building-permit review a poured concrete patio or slab goes through."),
        faq("What does Avalon Park's paver permit cost through the county?",
            "Orange County's residential paver permit runs a $38 zoning fee plus a $38 development-engineering review fee, with review typically taking about 4 business days."),
        faq("Does a patio inside an easement need extra paperwork in Avalon Park?",
            "Yes. Orange County requires an easement acknowledgement form added to the permit application whenever the paver work falls inside a recorded easement."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Avalon Park, FL – Rules",
    "meta": "Artificial turf installers in Avalon Park, FL: the state's lake setback, relevant near the community's 250 acres of built-in ponds, October 2026.",
    "h1": "Artificial Turf for Avalon Park Yards",
    "lede": capsule(f"Artificial turf in Avalon Park runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "With roughly 250 acres of man-made lakes designed into the community's villages, a fair number of backyards here border open water closely enough for the state's turf setback to come into play."),
    "sections": [
        ("A rule that lines up with how the community itself was laid out",
         f"<p>Rule 62-308.100 keeps new turf at least 10 feet from a pond or lake unless a seawall sits between the turf and the water, and it also requires a washed base, natural infill and no irrigation line buried beneath the turf "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). Because the 1998 planned development threaded 250 acres of lakes through its villages specifically for stormwater and amenity value "
         f"({ext(ABOUT_URL, 'Avalon Park Orlando, About')}), that 10-foot line comes up often on lots backing one of those ponds rather than being an unusual circumstance.</p>"),
        ("Where county rules and state turf law overlap",
         f"<p>Unincorporated Orange County doesn't layer its own turf-specific ordinance on top of the state rule, so the county's general concrete-and-paver permit process is the one that applies to the hardscape around a turf install, not a separate turf permit "
         f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}). F.S. 125.572 caps how far a local government could go even if it tried, and a turf lawn drops off the twice-weekly SJRWMD watering calendar that governs sod across the rest of the county "
         f"({src('fs125572', 'F.S. 125.572')}; {src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}).</p>"),
    ],
    "scenario": ("Turf along one of Avalon Park's built-in ponds, worked out in square feet",
                 f"<p>Consider an Avalon Park yard that backs onto one of the community's stormwater ponds, where 350 square feet of lawn along the bank won't hold a stand of grass through the wet season. At {price('artificial-turf')} per {per('artificial-turf')}, turf for that strip runs roughly $3,500 to $6,300, with the installer measuring the 10-foot setback from the pond's edge before the washed base goes down, unless the bank is already lined with a retaining wall or seawall that waives the buffer.</p>"),
    "faqs": [
        faq("Does Avalon Park have its own turf ordinance beyond the state rule?",
            "No separate community or county turf ordinance was found; the state's Rule 62-308.100 is the construction standard that applies, the same as anywhere else in unincorporated Orange County."),
        faq("Why does the lake setback come up so often in Avalon Park?",
            "The development built roughly 250 acres of man-made lakes into its village layout, so a larger-than-typical share of backyards sit close enough to open water for the state's 10-foot turf setback to apply."),
        faq("Does turf near an Avalon Park pond still need SJRWMD watering days?",
            "No. Once a lawn is turf, there's no irrigation zone left for the district's schedule to govern, regardless of how close the yard sits to the pond."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
