# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "hunters-creek"

HOA_URL = "https://cwsamsinc.com/rp/HOA/ArchitecturalGuidelinesAugust62024.pdf"
WIKI_URL = "https://en.wikipedia.org/wiki/Hunter%27s_Creek,_Florida"
SHINGLE_WIKI_URL = "https://en.wikipedia.org/wiki/Shingle_Creek_(Florida)"
CENSUS_URL = "http://censusreporter.org/profiles/16000US1231275-hunters-creek-fl/"

SRC = [
    ("Hunter's Creek Community Association, Architectural Guidelines (rev. Aug. 2024)", HOA_URL),
    ("Wikipedia, Hunter's Creek, Florida", WIKI_URL),
    ("Wikipedia, Shingle Creek (Florida)", SHINGLE_WIKI_URL),
    "orange-do-i-need-permit", "orange-residential-pavers", "orange-lot-grading", "orange-res-plan-guide", "orange-row-directory",
    "nrcs-myakka-osd", "nrcs-basinger-osd",
    "sjrwmd-watering", "dep-rule", "fs125572",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Orange County splits the review: concrete needs a building permit, pavers need a zoning permit",
        f"<p>Hunter's Creek has no city hall of its own; it's unincorporated Orange County, and the county draws a line most incorporated towns don't bother with: \"anytime you are pouring concrete or placing pavers, a permit is required,\" but \"Pavers require a Zoning permit only,\" while a poured slab goes through the full building-permit process "
        f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}). The paver path runs through the Zoning Division, 407-836-3111, with a dimensioned site plan, a $38 permit fee, a $38 Development Engineering review fee, and a 4-business-day turnaround "
        f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}).</p>"),
    sec("Residential open space has to stay at 40 percent of the lot",
        f"<p>The same county paver guidance cites Code §24-29(a): \"Residential private open space shall be forty (40) percent\" of the lot, a figure that sits alongside, not instead of, whatever setback and easement rules apply to a given address "
        f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). A homeowner adding a wider {cs('hunters-creek', 'concrete-driveways', 'driveway')} or a new {svc('paver-patios', 'patio')} on a Hunter's Creek lot is working against that same 40 percent figure, on top of whatever the community's own architectural review adds.</p>"),
    sec("The master community association reviews driveway and paver color before the county ever sees the permit",
        f"<p>Hunter's Creek is governed, address by address, by the Hunter's Creek Community Association, whose architectural guidelines limit driveway construction or extension to \"concrete or similar surfaces,\" and require the finished surface to be \"painted or stained with an approvable color so as to appear uniform in color\" "
        f"({ext(HOA_URL, "Hunter's Creek Community Association, Architectural Guidelines")}). That review sits ahead of, not instead of, the county's own zoning or building permit, so a driveway or {svc('paver-patios', 'paver')} project here typically clears the Architectural Review Committee before the county paperwork is filed.</p>"),
    sec("Shingle Creek starts inside Hunter's Creek and runs all the way to the Everglades",
        f"<p>Shingle Creek rises in southern Orange County and flows roughly 24 miles into Lake Tohopekaliga, marking it as the northernmost headwater of the entire Everglades system, and the Shingle Creek Management Area, a 1,585-acre urban nature preserve, sits inside the Hunter's Creek community itself "
        f"({ext(SHINGLE_WIKI_URL, 'Wikipedia, Shingle Creek (Florida)')}; {ext(WIKI_URL, "Wikipedia, Hunter's Creek, Florida")}). With that much wetland and open water threaded through the community, a site plan for {cs('hunters-creek', 'concrete-driveways', 'a driveway')} or patio near the preserve's edge gets checked against the flood-zone mapping for that specific parcel before grading starts.</p>"),
    sec("A Canadian developer's 1980s plan became a community of 24,000-plus and 109 lakes",
        f"<p>Genstar Development Company began planning the roughly 3,840-acre tract in 1984 and announced construction in 1986; the 2020 census counted 24,433 residents across 35 single-family neighborhoods, seven apartment communities, four condominium properties and one townhome neighborhood, with 109 lakes and ponds worked into the layout "
        f"({ext(WIKI_URL, "Wikipedia, Hunter's Creek, Florida")}). Most of that housing stock dates to the late 1980s through the 1990s, old enough now that {svc('concrete-repair', 'concrete repair and resurfacing')} and {svc('paver-sealing', 'paver resealing')} both come up regularly on streets that were new construction a generation ago.</p>"),
    sec("South Orange County's flatwoods soil holds water the way Lake County's ridge sand doesn't",
        f"<p>South Orange County sits on poorly drained flatwoods soils such as Myakka, Florida's official state soil, and Basinger, both with a water table that can sit within 18 inches of the surface for months at a time "
        f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}; {src('nrcs-basinger-osd', 'NRCS, Basinger series')}). On ground like that, a compacted aggregate base under a driveway or patio is managing standing water much more than it would on the excessively drained ridge sand common in Lake County's hill towns, which is part of why drainage planning carries more weight on a Hunter's Creek quote.</p>"),
    sec("Orange County hasn't been cut to one watering day, unlike Lake County",
        f"<p>Orange County follows SJRWMD's standard year-round schedule rather than the Phase III emergency order covering Lake County and several other counties: odd-numbered or no-number addresses water Wednesday and Saturday, even-numbered addresses Thursday and Sunday, nonresidential Tuesday and Friday, with nothing between 10 a.m. and 4 p.m. "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). That twice-a-week calendar gives new sod around Hunter's Creek more room to establish than towns under the emergency order get, though {svc('artificial-turf', 'artificial turf')} still comes up often for the shaded, root-filled yards common under this community's mature tree canopy.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does a new driveway in Hunter's Creek need a county permit?",
        "Yes. Orange County requires a building permit for poured concrete, while a paver driveway or patio only needs a zoning permit, filed through the Zoning Division with a site plan, a $38 permit fee and a $38 engineering review fee."),
    faq("Does the Hunter's Creek Community Association review driveway work separately from the county?",
        "Yes. The community's own architectural guidelines limit driveway material to concrete or similar surfaces, finished in an approvable, uniform color, and that review typically happens before the county permit is filed."),
    faq("What's the maximum impervious coverage on a Hunter's Creek lot?",
        "Orange County's residential private open space standard requires at least 40 percent of the lot to stay open, under Code §24-29(a), a figure that applies on top of ordinary setback rules."),
    faq("Is Hunter's Creek under the same one-day watering order as Lake County?",
        "No. Orange County follows SJRWMD's standard twice-a-week schedule rather than the Phase III emergency order in effect in Lake County and several other counties."),
    faq("How do you choose a concrete contractor for a Hunter's Creek home?",
        f"Check the contractor's standing with the state's license lookup, confirm the bid distinguishes between the county's building-permit path for concrete and the lighter zoning-permit path for pavers, and ask who's submitting the paperwork to the community association's Architectural Review Committee. {post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')} rounds out the list."),
]

HUB = page("/hunters-creek-fl/", "city", "Concrete, Pavers & Turf Contractor in Hunter's Creek, FL",
           "Concrete, pavers and turf in Hunter's Creek, FL: Orange County's permit split for concrete vs. pavers, the HOA's color rule, and Shingle Creek, Oct. 2026.",
           "Concrete, Pavers and Artificial Turf for Hunter's Creek, Florida Homes",
           capsule(f"Built around 109 lakes and ponds some 13 miles south of Orlando, Hunter's Creek is an unincorporated Orange County community of about 24,433 residents with no city hall of its own. "
                   f"Opera's crews pour concrete, lay pavers and install artificial turf here, with a new concrete driveway pricing at {price('concrete-driveway')} per {per('concrete-driveway')} under October 2026 Florida figures, reviewed by both the county and the community's architectural committee."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Hunter's Creek",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/dr-phillips-fl/", "Concrete, pavers and turf in Dr. Phillips"),
                    ("/lake-nona-fl/", "Concrete, pavers and turf in Lake Nona"),
                    ("/horizon-west-fl/", "Concrete, pavers and turf in Horizon West"),
                    ("/retaining-wall-cost/", "Retaining wall cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Hunter's Creek, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Hunter's Creek, FL",
    "meta": "Concrete driveway contractors in Hunter's Creek, FL: Orange County's building-permit rule, the lot grading policy's 6-inch spec, and the HOA color rule, Oct. 2026.",
    "h1": "Concrete Driveways for Hunter's Creek Homes",
    "lede": capsule(f"A new or replacement concrete driveway in Hunter's Creek is pricing at {price('concrete-driveway')} per {per('concrete-driveway')} under October 2026 Florida figures. "
                     "Orange County treats poured concrete as a building-permit job, and the county's own grading policy spells out a minimum thickness and strength for any driveway that touches the right-of-way, on top of the community association's own color rule."),
    "sections": [
        ("A poured driveway is a building permit here, not the lighter paver path",
         f"<p>Orange County's own guidance states it plainly: pouring concrete for a driveway, walkway or pad requires a building permit, a stricter review than the zoning-only permit the county allows for pavers "
         f"({src('orange-do-i-need-permit', 'Orange County, Do I Need a Permit')}). The county's Residential Lot Grading Policy adds a construction spec on top of that: a driveway has to be at least 6 inches thick at 3,000 psi, using non-steel-reinforced concrete through the right-of-way section, kept at least 3 feet from the property line "
         f"({src('orange-lot-grading', 'Orange County, Residential Lot Grading Policy')}).</p>"),
        ("The community's own color rule applies after the county's spec is met",
         f"<p>Once a {cs('hunters-creek', 'concrete-driveways', 'driveway')} meets the county's thickness and setback standard, the Hunter's Creek Community Association's architectural guidelines still require the finished surface to be concrete or a similar material, painted or stained to an approvable, uniform color rather than left as plain gray "
         f"({ext(HOA_URL, "Hunter's Creek Community Association, Architectural Guidelines")}). That review runs through the association's Architectural Review Committee, a separate step from the county's own permit file.</p>"),
    ],
    "scenario": ("A driveway replacement on a 1990s lot, worked out in square feet",
                 f"<p>A Hunter's Creek homeowner replacing an original, cracked 20 by 20 foot driveway from one of the community's 1990s-built neighborhoods is pouring 400 square feet of new concrete. At the {price('concrete-driveway')} per {per('concrete-driveway')} figure, the pour lands somewhere near $2,400 to $6,000, not counting demolition of the old slab. "
                 "Because the lot's drainage has to work with the area's poorly drained flatwoods soil rather than fast-draining sand, the base compaction gets as much attention as the pour itself, and the finished color still has to clear the association's review before it's considered done.</p>"),
    "faqs": [
        faq("Does a new driveway in Hunter's Creek require a building permit?",
            "Yes, poured concrete goes through Orange County's standard building-permit process, a stricter review than the zoning-only permit the county allows for a paver driveway."),
        faq("What thickness and strength does Orange County require for a driveway?",
            "At least 6 inches thick at 3,000 psi for the right-of-way section, using non-steel-reinforced concrete, with the driveway kept at least 3 feet from the property line under the county's lot grading policy."),
        faq("Does Hunter's Creek allow a plain gray concrete driveway?",
            "The community association's architectural guidelines call for the finished surface to be painted or stained to an approvable, uniform color, so plain unfinished gray concrete typically doesn't clear that review."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Hunter's Creek, FL – Zoning Permit",
    "meta": "Paver patio installers in Hunter's Creek, FL: the county's $38 zoning permit, the 40% open-space rule, and the community's own review, Oct. 2026.",
    "h1": "Paver Patios for Hunter's Creek Backyards",
    "lede": capsule(f"Paver patios around Hunter's Creek are running {price('paver-patio')} per {per('paver-patio')}, Florida pricing for October 2026. "
                     "Orange County reviews paver work as a zoning permit rather than a full building permit, a lighter process than poured concrete, but the lot's overall open-space ratio and the community association's own sign-off still apply."),
    "sections": [
        ("A $38 zoning permit, not a building-permit file",
         f"<p>Orange County's paver guidance sets the process apart from poured concrete: a dimensioned site plan showing the paver location against property lines and easements, a $38 permit fee, a $38 Development Engineering review fee, and roughly 4 business days for review "
         f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). Where the patio falls inside a recorded easement, an Easement Acknowledgement form goes in the same packet, and the Zoning Division, 407-836-3111, is the office that reviews it before a {svc('paver-patios', 'patio')} crew starts work.</p>"),
        ("The 40 percent open-space floor and a separate community review both still apply",
         f"<p>The same county guidance cites Code §24-29(a)'s 40 percent residential open-space requirement, a figure a new patio has to respect alongside the house, driveway and any pool deck already on the lot "
         f"({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). On top of that, the Hunter's Creek Community Association's own architectural review applies to exterior changes generally, so confirming what that process requires for a patio specifically, separate from the driveway color rule, is worth a call before pavers are ordered.</p>"),
    ],
    "scenario": ("A backyard patio addition, worked out in square feet",
                 f"<p>A Hunter's Creek homeowner adding a 15 by 20 foot paver patio off the back of the house is working with 300 square feet. At the {price('paver-patio')} per {per('paver-patio')} range, that prices out to roughly $3,000 to $5,100, before any fire-pit or seating-wall add-on. "
                 "Because the lot's existing driveway and pool deck already count against the 40 percent open-space figure, running the math on a current survey before the patio is designed is what keeps the whole package inside what the county allows.</p>"),
    "faqs": [
        faq("Is a paver patio a lighter permit than a concrete one in Hunter's Creek?",
            "Yes. Orange County reviews paver work as a zoning permit, with a $38 permit fee and a $38 engineering review fee, rather than the full building-permit process poured concrete requires."),
        faq("Does a Hunter's Creek patio count against the lot's open-space requirement?",
            "Yes. The county's 40 percent residential private open-space standard counts the patio alongside the house, driveway and any pool deck already on the lot."),
        faq("Does the Hunter's Creek Community Association review patios the same way it reviews driveways?",
            "The published color rule is written for driveways specifically; a patio still goes through the association's general architectural review, so confirming the exact requirement for a patio with the Architectural Review Committee is worth doing first."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Hunter's Creek, FL – Lakes & Shade",
    "meta": "Artificial turf installers in Hunter's Creek, FL: the state's lake setback near 109 ponds, mature tree shade, and the county's watering schedule, Oct. 2026.",
    "h1": "Artificial Turf for Hunter's Creek Yards",
    "lede": capsule(f"Homeowners around Hunter's Creek are budgeting {price('artificial-turf')} per {per('artificial-turf')} for turf this fall, current Florida pricing. "
                     "With 109 lakes and ponds worked into the community's layout, the state's shoreline buffer for turf comes up on more lots here than in a landlocked town, and decades of mature tree canopy leave plenty of shaded yard where sod alone struggles."),
    "sections": [
        ("A community built around water means the lake setback matters on more lots",
         f"<p>Florida's statewide turf rule builds the base out of washed stone and natural infill, leaves buried irrigation out of the design entirely, and pulls installed turf back 10 feet from open water on a pond, lake or canal, a gap that closes only when a seawall, not a natural bank, marks the property line "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). With 109 lakes and ponds designed into Hunter's Creek's original layout, a meaningfully higher share of backyards here border water than in a typical inland subdivision, and a 2025 state law caps how far local rules can tighten that buffer further "
         f"({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
        ("Mature shade changes where sod gives up first",
         f"<p>Housing in Hunter's Creek mostly dates to the late 1980s through the 1990s, old enough that the live oaks and other canopy trees planted with the original subdivisions have grown into real shade over a lot of backyards "
         f"({ext(WIKI_URL, "Wikipedia, Hunter's Creek, Florida")}). Orange County's standard twice-a-week watering schedule gives sod more of a chance here than the one-day order some counties are under, but shaded turf competing with mature tree roots for water and light still thins out in patches where {svc('artificial-turf', 'artificial turf')} holds up better.</p>"),
    ],
    "scenario": ("Turf near a shaded lakeside lot, worked out in square feet",
                 f"<p>A Hunter's Creek backyard backing onto one of the community's lakes, fenced at 480 square feet, loses some footage once the 10-foot shoreline buffer is subtracted, leaving around 440 square feet to actually install. Against the {price('artificial-turf')} per {per('artificial-turf')} range, that prices out to roughly $4,400 to $11,000 depending on the pile height and infill. "
                 "Because mature oaks shade part of the same yard, the layout is measured against both the water buffer and the tree canopy before the base is cut.</p>"),
    "faqs": [
        faq("How close to a Hunter's Creek lake can artificial turf be installed?",
            "Florida's turf rule holds the installed edge back 10 feet from a pond, lake or canal, a distance that only closes up where a seawall replaces the natural bank. The ground underneath still has to be a washed, non-irrigated base either way."),
        faq("Is Hunter's Creek under a one-day watering restriction like Lake County?",
            "No. Orange County follows SJRWMD's standard twice-a-week schedule, giving sod more watering opportunity here than towns under the Phase III emergency order."),
        faq("Does shade from mature trees affect where turf makes sense in Hunter's Creek?",
            "Often, yes. With much of the community's tree canopy decades old, sod competing with established roots for light and water tends to thin out first in those shaded sections, which is where turf gets asked about most."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
