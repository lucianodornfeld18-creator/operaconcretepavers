# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "groveland"

ZONING_PACKET_URL = "https://groveland-fl.gov/DocumentCenter/View/5175/Paver-or-Slab-Only-Zoning-Packet-PDF"
VERNACULAR_URL = "https://library.municode.com/fl/groveland/codes/community_development_code?nodeId=ART6FLVERE"
HISTORY_URL = "https://groveland-fl.gov/655/Our-History"
WIKI_URL = "https://en.wikipedia.org/wiki/Groveland,_Florida"
TRAIL_URL = "https://en.wikipedia.org/wiki/South_Lake_Trail"
CENSUS_URL = "http://censusreporter.org/profiles/16000US1227800-groveland-fl/"

SRC = [
    ("City of Groveland, Building Division — Pavers or Concrete Slab Checklist", ZONING_PACKET_URL),
    ("City of Groveland, Community Development Code — Article 6, Florida Vernacular Requirements", VERNACULAR_URL),
    ("City of Groveland — Our History", HISTORY_URL),
    ("Wikipedia — Groveland, Florida", WIKI_URL),
    ("Wikipedia — South Lake Trail", TRAIL_URL),
    ("Census Reporter — Groveland, FL", CENSUS_URL),
    "nrcs-candler-osd", "nrcs-astatula-osd",
    "sjrwmd-watering", "dep-rule", "fs125572",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Groveland calls a new driveway or paver patio a zoning permit, not a flat-fee building permit",
        f"<p>The city's own checklist for pavers or a concrete slab skips the building-permit counter entirely: homeowners file a zoning application, a property record card and a dimensioned site plan showing the new surface, work out the lot's impervious-surface math on the city's own worksheet, and, where a subdivision has one, attach an HOA approval letter, plus an easement waiver if the work lands in a drainage or utility easement "
        f"({ext(ZONING_PACKET_URL, 'City of Groveland, Pavers or Concrete Slab Checklist')}). No flat fee is printed on the form itself, so the Building Division, 352-429-2141 option 2 or permitting@groveland-fl.gov, is the office that quotes one for a specific lot before {cs('groveland', 'concrete-driveways', 'a driveway pour')} or {svc('paver-patios', 'a patio')} gets scheduled.</p>"),
    sec("The Florida Vernacular code picks the materials, right down to banning phosphogypsum",
        f"<p>Groveland's Community Development Code does not leave driveway material up to the installer: Article 6 names brick pavers, compacted clay, gravel, crushed oyster shell or concrete as approved surfaces, with anything else needing staff sign-off first, and it explicitly rules out recycled concrete and phosphogypsum, the radioactive fertilizer byproduct some states have weighed as a paving aggregate "
        f"({ext(VERNACULAR_URL, 'City of Groveland, Article 6 (Florida Vernacular Requirements)')}). A patio is held to a different standard inside that same article: it has to be laid in permeable pavers and cleared by the Community Development Director or a designee, a step {svc('paver-patios', 'paver-patio')} work doesn't skip just because a driveway nearby already has its permit.</p>"),
    sec("There's no single citywide impervious ratio, so the worksheet sends you to Planning instead",
        f"<p>Where some nearby cities publish one fixed lot-coverage percentage, Groveland's own impervious-surface calculator leaves the \"Maximum Impervious Coverage allowed per Subdivision/Zoning\" line blank and tells the applicant to contact the Planning Division for the number that applies to that specific zoning district or subdivision "
        f"({ext(ZONING_PACKET_URL, 'City of Groveland, Impervious Surface Calculations worksheet')}). The same worksheet counts the house, garage, porches, deck, driveway, walkways, pool and pool deck together against whatever ratio Planning confirms, so a widened {cs('groveland', 'concrete-driveways', 'driveway')} and a new patio on the same lot share one running total rather than two separate caps.</p>"),
    sec("A city that quadrupled since 2010 means mostly recent concrete, not decades-old slabs",
        f"<p>Groveland counted 1,747 residents in 1960 and still only 8,729 by the 2010 census; by 2020 that had more than doubled again to 18,505, and Census Reporter's current estimate puts the city at 22,012 "
        f"({ext(WIKI_URL, 'Wikipedia, Groveland population history')}; {ext(CENSUS_URL, 'Census Reporter, Groveland, FL')}). With so much of that growth stacked into the past decade and a half, most of the concrete and pavers going into the ground around town belong to brand-new lots rather than aging subdivisions, which is also why the zoning packet's HOA-approval line applies to so many Groveland addresses at once.</p>"),
    sec("Lake David, Cherry Lake and a trail that climbs: Groveland's ground isn't flat",
        f"<p>Lake David, a 44-acre lake at Lake David Park, sits at the center of the city the Taylor brothers first called Taylorville before a 1922 council meeting renamed it Groveland, and Cherry Lake Park, the newest addition to the park system, opened its first phase in 2020 along the same chain of interconnected lakes "
        f"({ext(HISTORY_URL, 'City of Groveland, Our History')}). Groveland sits at the western end of the South Lake Trail, a 12.5-mile paved path unusual among Florida trails for crossing genuinely hilly ground on its way toward Clermont "
        f"({ext(TRAIL_URL, 'Wikipedia, South Lake Trail')}), terrain built on the same excessively drained Candler and Astatula sand common across this stretch of Lake County's ridge country "
        f"({src('nrcs-candler-osd', 'NRCS, Candler series')}; {src('nrcs-astatula-osd', 'NRCS, Astatula series')}). A backyard that drops toward one of those lakes is a reason {svc('retaining-walls', 'a retaining wall')} or extra grading comes up on a Groveland patio quote more than it would on a flat inland lot.</p>"),
    sec("Lake County's one-day order reaches Groveland the same as the rest of the county",
        f"<p>SJRWMD's Phase III Extreme Water Shortage order has cut Lake County down to a single watering day, odd-numbered addresses on Saturday and even-numbered ones on Sunday, nonresidential irrigation on Tuesday, with nothing allowed between 8 a.m. and 6 p.m. "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). New sod on a Groveland lot gets a single weekly soak to take root under that schedule, a reason homeowners bring up {svc('artificial-turf', 'artificial turf')} for whichever stretch of the yard refuses to fill in.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does Groveland require a building permit for a new driveway?",
        "Not the building-permit counter: driveway and paver work on private property goes through a zoning permit instead, with a site plan, an impervious-surface calculation, an HOA approval letter if the subdivision has one, and an easement waiver if the work sits in a drainage or utility easement. The city's checklist doesn't print a flat fee, so Building Division at 352-429-2141 option 2 confirms the current one."),
    faq("What driveway materials does Groveland allow?",
        "Brick pavers, compacted clay, gravel, crushed oyster shell or concrete are approved outright under the city's Florida Vernacular code; any other surface needs Community Development staff approval first. Recycled concrete and phosphogypsum are both explicitly prohibited."),
    faq("Is there one impervious-surface limit for every Groveland lot?",
        "No. The city's own worksheet leaves that figure blank and tells applicants to call the Planning Division, because the allowed ratio depends on the specific zoning district and subdivision rather than one citywide number."),
    faq("Does a Groveland patio have different rules than a driveway?",
        "Yes. The vernacular code requires patios to be built in permeable pavers and reviewed by the Community Development Director or a designee, a step that's separate from the driveway material list even on the same lot."),
    faq("How do you pick a concrete contractor for a Groveland driveway?",
        f"Start by checking the contractor's standing with the state's license lookup, then make sure the bid treats the job as a zoning permit with an impervious-surface worksheet rather than a standard building-permit quote, and confirm who's gathering the HOA approval letter before material gets ordered. For the rest of what to check, see {post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')}."),
]

HUB = page("/groveland-fl/", "city", "Concrete, Pavers & Turf Contractor in Groveland, FL",
           "Concrete driveways, paver patios and turf in Groveland, FL: the city's zoning permit, its banned-materials list and the Lake County watering order, Oct. 2026.",
           "Concrete, Pavers and Artificial Turf for Groveland, Florida Homes",
           capsule(f"Groveland is a fast-growing Lake County city of roughly 22,012 people, about 29 miles southwest of Orlando, where Opera installs concrete driveways, paver patios and artificial turf. "
                   f"A new concrete driveway here currently runs {price('concrete-driveway')} per {per('concrete-driveway')}, October 2026 Florida pricing, and the city reviews the work through a zoning permit rather than a building-permit counter."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Groveland",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/lake-and-polk-county-driveway-permits/", "Driveway and patio permits in Lake and Polk counties"),
                    ("/montverde-fl/", "Concrete, pavers and turf in Montverde"),
                    ("/clermont-fl/", "Concrete, pavers and turf in Clermont"),
                    ("/retaining-wall-cost/", "Retaining wall cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Groveland, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Groveland, FL – Permit Rules",
    "meta": "Concrete driveway contractors in Groveland, FL: the city's zoning-permit checklist and its approved-materials list under Article 6, Oct. 2026.",
    "h1": "Pouring a Concrete Driveway in Groveland",
    "lede": capsule(f"A new or replacement concrete driveway in Groveland is pricing at {price('concrete-driveway')} per {per('concrete-driveway')} heading into late 2026, by current Florida contractor figures. "
                     "City Hall treats the job as a zoning permit rather than a building permit, built around an impervious-surface worksheet, and concrete is only one of several surfaces the Florida Vernacular code names as approved."),
    "sections": [
        ("A zoning application and an impervious-surface worksheet replace a flat permit fee",
         f"<p>Groveland's checklist for a new driveway asks for a zoning application, a property record card and a dimensioned site plan, plus the lot's impervious-surface math worked out on the city's own form; where the lot sits inside a subdivision with an HOA, an approval letter from that association goes in the same packet "
         f"({ext(ZONING_PACKET_URL, 'City of Groveland, Pavers or Concrete Slab Checklist')}). No set fee is printed on the form, so a call to the Building Division, 352-429-2141 option 2, or an email to permitting@groveland-fl.gov, pins down the current one for a specific address before a crew is scheduled.</p>"),
        ("Concrete is one approved surface among several, not the only option on the list",
         f"<p>Article 6 of the city's Community Development Code names brick pavers, compacted clay, gravel, crushed oyster shell and concrete as approved driveway materials, with staff approval required for anything outside that list, and it rules out recycled concrete and phosphogypsum outright "
         f"({ext(VERNACULAR_URL, 'City of Groveland, Article 6 (Florida Vernacular Requirements)')}). A straight concrete pour clears that list without extra review, which is part of why it stays the most common choice for a {cs('groveland', 'concrete-driveways', 'new Groveland driveway')} even though the code leaves room for gravel or clay instead.</p>"),
    ],
    "scenario": ("A driveway widening on a recently platted lot, worked out in square feet",
                 f"<p>A Groveland homeowner adding a 10-foot-wide, 22-foot-long extension alongside an existing one-car driveway picks up 220 square feet to park a second vehicle off the street. Figured against the {price('concrete-driveway')} per {per('concrete-driveway')} range, that addition lands somewhere around $1,320 to $3,300, not counting any saw-cut tie-in to the existing slab. "
                 "Because the city's impervious-surface worksheet totals the driveway against the house, porch and any patio already on the lot, running that math on a current survey before the extension is designed is what keeps the project inside whatever ratio Planning confirms for that subdivision.</p>"),
    "faqs": [
        faq("Does a new driveway in Groveland need a building permit?",
            "It's reviewed as a zoning permit instead, with a site plan, an impervious-surface calculation and an HOA approval letter where the subdivision has one. The city's own form doesn't list a flat fee, so Building Division confirms the current one by phone or email."),
        faq("Can a Groveland driveway be built in gravel instead of concrete?",
            "Yes. The city's Florida Vernacular code approves gravel, compacted clay, crushed oyster shell and brick pavers alongside concrete; anything outside that list needs Community Development staff approval before it's installed."),
        faq("Is recycled concrete allowed for a Groveland driveway base or surface?",
            "No. Article 6 of the city's Community Development Code specifically prohibits recycled concrete as a driveway material, along with phosphogypsum."),
    ],
    "sources": SRC,
}

# 2. paver-patios --------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Groveland, FL – Permeable Rule",
    "meta": "Paver patio installers in Groveland, FL: why the city requires permeable pavers and Community Development sign-off, plus the lake-chain backyard grading, Oct. 2026.",
    "h1": "Paver Patios for Groveland Backyards",
    "lede": capsule(f"Paver patio work in Groveland is tracking at {price('paver-patio')} per {per('paver-patio')} under October 2026 Florida pricing. "
                     "Unlike a driveway, the city's vernacular code calls for patio pavers to be permeable and signed off by the Community Development Director, and on a lot backing up to Groveland's Chain of Lakes, where that patio sheds water is part of what staff checks."),
    "sections": [
        ("Permeable pavers and a director-level sign-off, not the driveway material list",
         f"<p>Groveland's Article 6 splits patios out from driveways: where a driveway can be concrete, gravel, clay, crushed shell or brick pavers, a patio has to be built in permeable pavers specifically, and the Community Development Director or a designee reviews it before work starts "
         f"({ext(VERNACULAR_URL, 'City of Groveland, Article 6 (Florida Vernacular Requirements)')}). That review sits alongside the same zoning application, site plan and impervious-surface worksheet the city uses for {cs('groveland', 'concrete-driveways', 'driveway work')}, so a {svc('paver-patios', 'patio')} project on a lot that already has a driveway permit on file still needs its own packet.</p>"),
        ("A backyard on the Chain of Lakes changes where the water goes",
         f"<p>Lake David and Cherry Lake anchor two of Groveland's city parks along an interconnected chain of lakes that the South Lake Trail corridor runs alongside on its way toward Clermont "
         f"({ext(HISTORY_URL, 'City of Groveland, Our History')}; {ext(TRAIL_URL, 'Wikipedia, South Lake Trail')}). On a lot that backs onto one of those lakes or a connecting canal, a patio's slope toward the water gets checked against the easement waiver question on the zoning packet, since pavers set inside a platted drainage easement need that waiver signed before the base goes in.</p>"),
    ],
    "scenario": ("A lakeside patio addition, worked out in square feet",
                 f"<p>A 16 by 18 foot permeable-paver patio behind a Groveland home backing onto one of the city's chain lakes works out to 288 square feet. Set against the {price('paver-patio')} per {per('paver-patio')} range, that patio comes in somewhere near $2,880 to $4,896, before a fire-pit section or a different paver grade changes the total. "
                 "Because the rear of the lot sits close to the water, the crew checks whether any part of that footprint falls inside a recorded drainage easement before ordering material, since that triggers the same easement waiver the zoning packet asks for.</p>"),
    "faqs": [
        faq("Do Groveland patios have to use permeable pavers?",
            "Yes. The city's Florida Vernacular code requires patio surfaces to be permeable pavers specifically, reviewed by the Community Development Director or a designee, a stricter standard than the broader materials list that applies to driveways."),
        faq("Does a patio need its own zoning packet if the driveway already has one?",
            "Yes. Each addition, patio included, goes through its own zoning application, site plan and impervious-surface worksheet, even on a lot where a driveway permit is already on file."),
        faq("What happens if a Groveland patio falls inside a drainage easement?",
            "The homeowner signs an easement waiver acknowledging the city can require the pavers removed later if the easement needs to function, which is a separate step from the standard zoning review."),
    ],
    "sources": SRC,
}

# 3. artificial-turf -------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Groveland, FL – Watering Order",
    "meta": "Artificial turf installers in Groveland, FL: Lake County's one-day watering order, the state turf rule, and why so much of the city is new construction, Oct. 2026.",
    "h1": "Artificial Turf for Groveland Yards",
    "lede": capsule(f"Turf installation around Groveland costs {price('artificial-turf')} per {per('artificial-turf')} by this fall's Florida figures. "
                     "Every address in the city is down to one watering day a week under the county's current order, a calendar that turf doesn't have to follow once the base is in, while a separate state rule governs what sits underneath it."),
    "sections": [
        ("A single weekly soak is a hard way to grow in new sod",
         f"<p>Lake County addresses, Groveland included, have been held to one watering day under SJRWMD's Phase III Extreme Water Shortage order: Saturday for odd-numbered addresses, Sunday for even-numbered, Tuesday for businesses, with the clock closed between 8 a.m. and 6 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). Because so much of Groveland has been platted within the last decade and a half, a good share of the lawns needing cover today sit on freshly graded ground trying to root under that single weekly session instead of the twice-weekly schedule builders once planned around, pushing more homeowners toward {svc('artificial-turf', 'artificial turf')} for the patches that won't take.</p>"),
        ("State rule, not city code, decides what goes under the turf",
         f"<p>Florida's statewide synthetic-turf rule calls for a washed base with natural infill, bars buried irrigation underneath it, and keeps installed turf at least 10 feet from a pond, lake or canal unless the edge is a seawall "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A Groveland yard near Lake David, Cherry Lake or one of the smaller lakes threaded through town gets that buffer measured off the actual shoreline before the layout is cut, and a 2025 statute caps how much further a city or county is allowed to restrict residential turf beyond that standard "
         f"({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Turf on a new-construction lot, worked out in square feet",
                 f"<p>A freshly graded Groveland backyard measuring 30 by 24 feet, 720 square feet, is losing its sod to bare patches after a summer of one-day-a-week watering. Against the {price('artificial-turf')} per {per('artificial-turf')} range, swapping it for turf comes to somewhere around $7,200 to $18,000, depending on the pile height and infill chosen. "
                 "Because the lot is new construction rather than an older yard, the base underneath gets built to the state's washed-rock standard from the start rather than retrofitted around an existing irrigation system.</p>"),
    "faqs": [
        faq("How many days a week can a Groveland lawn be watered right now?",
            "One. Lake County is under SJRWMD's Phase III order, limiting odd-numbered addresses to Saturday and even-numbered addresses to Sunday, with no watering allowed between 8 a.m. and 6 p.m."),
        faq("How close to a Groveland lake can artificial turf be installed?",
            "Florida's turf rule keeps installed turf back at least 10 feet from a pond, lake or canal edge, unless that edge is a seawall rather than open shoreline. Either way, irrigation can't be buried underneath the turf itself."),
        faq("Does Groveland's zoning permit apply to artificial turf the same way it applies to a driveway?",
            "Turf counts as an added impervious or semi-impervious surface on the same worksheet the city uses for driveways and patios, so it's worth confirming with the Building Division whether a specific lot's turf plan needs the same zoning packet."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
