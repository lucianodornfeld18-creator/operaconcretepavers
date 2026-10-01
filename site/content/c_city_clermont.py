# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "clermont"

SKYRIDGE_URL = "https://citizenportal.ai/articles/7286789/Florida/Lake-County/City-of-Clermont/Council-denies-variance-for-expanded-pavers-at-Sky-Ridge-Road-but-gives-homeowners-90-days-to-comply"
KINGSRIDGE_URL = "https://www.kings-ridge.net/community-portal/content/menu-item/12538"

SRC = [
    "clermont-faq", "clermont-permit-checklists", "clermont-forms", "clermont-permit-types", "clermont-r1-isr", "clermont-econ",
    "census-pep-v2025", "acs-clermont", "wiki-sugarloaf",
    "lake-exempt", "lake-driveway-apron", "lake-ldr-appendix-a", "lake-row-permit", "lake-building-services",
    "nrcs-candler-osd", "nrcs-tavares-osd", "nrcs-astatula-osd",
    "sjrwmd-watering", "dep-rule", "fs125572", "fl-senate-2011-104",
    ("Citizen Portal, Clermont City Council meeting summary — Sky Ridge Road paver variance", SKYRIDGE_URL),
    ("Kings Ridge Community, Frequently Asked Questions", KINGSRIDGE_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Clermont calls it a zoning approval, not a building permit",
        "<p>Pour a driveway or a sidewalk on private property inside the Clermont city limits and Building Services doesn't open a building-permit file at all: the city's own checklist says plainly that "
        f"“a building permit is not required; however, a zoning approval is required,” a notarized application plus a survey that shows the lot's impervious surface, side setbacks included, for a flat $45 fee with no inspection "
        f"({src('clermont-permit-checklists', 'City of Clermont, Permit Checklists')}). The math changes the moment the work reaches the apron in the city right-of-way: that still needs a zoning application and a survey showing the apron's width, built “per City Standards,” but the $45 now buys a city driveway inspection too "
        f"({src('clermont-forms', 'City of Clermont, Applications & Forms')}). {cs('clermont', 'concrete-driveways', 'A new driveway')} and {svc('concrete-walkways', 'a sidewalk repair')} both start at Building Services, 685 W. Montrose St., 352-241-7315 "
        f"({src('clermont-faq', 'City of Clermont, Building Services FAQ')}).</p>"),
    sec("Step outside the city line and the paperwork becomes an exemption, not a fee",
        f"<p>A lot that reads as Clermont on a mailing label can still sit in unincorporated Lake County, where the county's own exemption list, built on Florida Building Code 105.2 #2, lets a driveway or sidewalk skip the building permit entirely once it's “not more than 30 inches above adjacent grade” and isn't part of an accessible route, zoning and flood rules still apply "
        f"({src('lake-exempt', 'Lake County, Residential Work Exempt from Permits')}). The apron itself is a separate matter: Lake County's own transportation standards set a single-family driveway at 10 feet minimum width, an 8-foot radius or 8-by-4-foot flares at the road, at least 10 feet clear of the property corner, and paved back at least 10 feet from the edge of pavement, with valley gutters required where the road is curbed "
        f"({src('lake-ldr-appendix-a', 'Lake County, LDR Appendix A Transportation Standards')}). Public Works, 352-253-6019, reviews that apron permit separately from any other county right-of-way work "
        f"({src('lake-row-permit', 'Lake County, Right-of-Way Permit')}).</p>"),
    sec("A Sky Ridge Road paver job shows what the 45-percent line actually costs",
        f"<p>Clermont's R-1 zoning caps total impervious coverage at 55 percent of a lot, and inside that number, the house itself plus the driveway and walkways together can't pass 45 percent "
        f"({src('clermont-r1-isr', 'City of Clermont, Municode Ch. 125 Div. 5, R-1')}). That isn't an abstract line: in 2026 the City Council turned down a homeowner's request to expand a paver driveway at a Sky Ridge Road home because the plan pushed past the 55 percent impervious cap and crowded a side setback down to zero, and gave the owner 90 days to narrow the pavers back from the lot line, trade part of the surface for a two-strip “Hollywood” driveway or gravel, and get the area back under the cap "
        f"({ext(SKYRIDGE_URL, 'Citizen Portal, Sky Ridge Road paver variance')}). {svc('paver-driveways', 'A paver driveway')} expansion on a lot that's already close to that 45 percent figure is worth checking against a survey before the pavers are ordered, not after.</p>"),
    sec("Sugarloaf Mountain and the Lake Wales Ridge explain the retaining walls",
        f"<p>Clermont brands itself the “Choice of Champions,” pointing to its “award-winning parks, trails, hills and fresh water bodies” "
        f"({src('clermont-econ', 'City of Clermont, Economic Information')}), and the hills are real: Sugarloaf Mountain, just outside town, rises 312 feet above sea level, the highest point on the Florida peninsula, part of the Lake Wales Ridge, “a series of sand hills running south to Highlands County” "
        f"({src('wiki-sugarloaf', 'Wikipedia, Sugarloaf Mountain (Florida)')}). The sand under that ridge, Candler and Astatula, drains excessively, with the water table more than 60 to 80 inches down, a world away from the flatwoods soils that sit wet for months elsewhere in the Orlando unit "
        f"({src('nrcs-candler-osd', 'NRCS, Official Series Description, Candler')}; {src('nrcs-astatula-osd', 'NRCS, Official Series Description, Astatula')}). A lot that drops several feet from the street to the back fence is why {svc('retaining-walls', 'a retaining wall')} shows up on so many Clermont quotes that would never need one on a flat inland lot.</p>"),
    sec("The state's one-day-a-week order reaches Lake County too",
        f"<p>SJRWMD's normal year-round schedule runs twice a week, but under Phase III Extreme Water Shortage Order 2026-017, Lake County is one of the counties limited to a single watering day: odd-numbered addresses on Saturday, even-numbered on Sunday, nonresidential irrigation on Tuesday, and nothing between 8 a.m. and 6 p.m. any day "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). New sod planted under that order has less room to recover between waterings than it did under the old twice-weekly calendar, which is part of why {svc('artificial-turf', 'artificial turf')} keeps coming up as an alternative for a slope that's hard to keep green on one watering day.</p>"),
    sec("The newest housing stock in the Orlando unit, and growing fast",
        f"<p>Clermont's population reached an estimated 52,812 by July 2025, up from a 2020 base of 42,992, a jump of close to a quarter in five years "
        f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}). The typical Clermont home was built in 2006, the newest median construction year of the nine incorporated cities the Orlando unit tracks "
        f"({src('acs-clermont', 'Census Reporter, Clermont')}). That combination means a lot of the driveways and patios going in right now are first installs on a freshly graded lot rather than a replacement for something original to the house, though the earliest of that 2006-era concrete is old enough that {svc('concrete-repair', 'concrete repair and resurfacing')} is starting to come up on the oldest of those subdivisions.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Why are retaining walls so common in Clermont and Minneola?",
        f"Clermont sits near Sugarloaf Mountain, 312 feet above sea level and the highest point on the Florida peninsula, part of the Lake Wales Ridge, a chain of sand hills that runs south through this part of Lake County "
        f"({ext('https://en.wikipedia.org/wiki/Sugarloaf_Mountain_(Florida)', 'Wikipedia, Sugarloaf Mountain')}). A lot that drops several feet from the street to the rear property line needs something to hold the grade at the edge of a driveway, patio or pool deck, which is why a wall shows up on so many quotes here and in neighboring Lake County communities that sit among the same hills."),
    faq("Does Clermont require a permit for a new driveway?",
        "Not a building permit, inside the city limits: driveway and sidewalk work on private property goes through a zoning approval instead, a notarized application and survey for a flat $45 fee with no inspection. Work on the apron in the city right-of-way carries the same $45 fee but adds a required city inspection."),
    faq("What's the difference between Clermont's rules and Lake County's for a driveway?",
        "Inside the city, the process is a zoning approval, not a building permit, reviewed by Building Services. Just outside the limits, in unincorporated Lake County, a driveway or sidewalk under 30 inches above grade is exempt from a building permit altogether, though the apron in the county right-of-way still needs its own permit with a published width and flare spec."),
    faq("What are Clermont's watering days under the state's 2026 order?",
        "Under SJRWMD's Phase III Extreme Water Shortage Order, Lake County is down to one watering day a week: Saturday for odd-numbered addresses, Sunday for even-numbered ones, Tuesday for nonresidential irrigation, with nothing allowed between 8 a.m. and 6 p.m."),
    faq("How do you pick the best concrete contractor in Clermont?",
        f"Verify the contractor on the state's license-check tool, ask whether the bid's driveway or patio size was checked against the city's 45 percent impervious sub-cap before pricing, and confirm whether the quote assumes a zoning approval inside the city or a county permit outside it. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')} covers the rest."),
]

HUB = page("/clermont-fl/", "city", "Concrete, Pavers & Turf Contractor in Clermont, FL",
           "Concrete, pavers and turf in Clermont, FL: the city's zoning approval, Lake County's exemption and the 45% impervious cap, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Clermont, Florida Homes",
           capsule("Opera pours concrete and lays pavers and artificial turf for homes in Clermont, a Lake County city of about 52,812 residents, up from 42,992 in 2020, about 24 miles from Orlando. "
                   f"Expect {price('concrete-driveway')} per {per('concrete-driveway')} for a new concrete driveway, current Florida pricing for October 2026, and most driveway work on private property needs only a $45 zoning approval rather than a building permit."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Clermont",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/lake-and-polk-county-driveway-permits/", "Driveway and patio permits in Lake and Polk counties"),
                    ("/minneola-fl/", "Concrete, pavers and turf in Minneola"),
                    ("/montverde-fl/", "Concrete, pavers and turf in Montverde"),
                    ("/retaining-wall-cost/", "Retaining wall cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Clermont, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Clermont, FL – Zoning Rules",
    "meta": "Concrete driveway installers in Clermont, FL: the city's $45 zoning approval and the 45% impervious sub-cap that can limit a wider pour, Oct. 2026.",
    "h1": "Pouring or Replacing a Concrete Driveway in Clermont",
    "lede": capsule(f"Expect {price('concrete-driveway')} per {per('concrete-driveway')} for a new or replacement concrete driveway in Clermont, current Florida pricing heading into late 2026. "
                     "Inside the city limits, that job goes through a zoning approval rather than a building permit, and in the R-1 zoning that covers most of Clermont's neighborhoods, the driveway shares a 45-percent impervious ceiling with the house itself and the walkways."),
    "sections": [
        ("A zoning approval, a survey and a $45 fee replace the building permit",
         f"<p>Clermont's own permit checklist states that driveway or sidewalk work on private property doesn't need a building permit, only a zoning approval: a notarized application plus a survey showing the lot's dimensions and impervious surface, filed for a flat $45 fee with no inspection required "
         f"({src('clermont-permit-checklists', 'City of Clermont, Permit Checklists')}). Call Building Services at 352-241-7315 to confirm which documents a specific lot needs before a crew is scheduled. Work that crosses into the apron at the street is a separate submission: the same $45 fee, but this time with a required city driveway inspection, built to the city's own apron standard rather than left to the installer's judgment "
         f"({src('clermont-forms', 'City of Clermont, Applications & Forms')}).</p>"),
        ("The 45-percent sub-cap is the number that decides how wide a driveway can go",
         f"<p>In Clermont's R-1 district, total impervious coverage on a lot tops out at 55 percent, and within that figure, the principal building plus the driveway and walkways together can't exceed 45 percent "
         f"({src('clermont-r1-isr', 'City of Clermont, Municode Ch. 125 Div. 5, R-1')}). That cap isn't theoretical: in 2026 the City Council denied a homeowner's request to widen a paver driveway on Sky Ridge Road once the plan pushed past the 55 percent impervious limit and crowded a side setback, and set a 90-day window to pull the surface back under the cap "
         f"({ext(SKYRIDGE_URL, 'Citizen Portal, Sky Ridge Road paver variance')}). A survey showing how much of that 45 percent a lot has already used, before a widened driveway or {cs('clermont', 'paver-driveways', 'a paver conversion')} gets designed, saves a redesign later.</p>"),
    ],
    "scenario": ("A driveway replacement and widening, worked out in square feet",
                 f"<p>A Clermont homeowner widening a cracked 20 by 20 foot driveway into a 20 by 25 foot pour picks up 500 total square feet to fit a second vehicle alongside the garage. Multiplying that by the {price('concrete-driveway')} per {per('concrete-driveway')} range puts the pour somewhere between $3,000 and $7,500, not counting demolition of the old slab. "
                 "On a lot where the house already sits close to the R-1 district's 45 percent sub-cap, the extra 100 or so square feet from the widening is exactly the kind of addition worth checking against a current survey first, the same math that tripped up the Sky Ridge Road expansion before it ever reached pavers.</p>"),
    "faqs": [
        faq("Does Clermont require a building permit for a concrete driveway?",
            "Not a building permit, on private property: it's a zoning approval instead, a notarized application and survey for a flat $45 fee with no inspection. A driveway apron that reaches into the city right-of-way carries the same fee but adds a required city inspection."),
        faq("What is Clermont's impervious surface ratio limit for a driveway?",
            "In the R-1 district, total lot coverage tops out at 55 percent, and the house plus the driveway and walkways together can't pass 45 percent of that. A survey showing how much of that figure a lot has already used comes before a wider driveway is designed."),
        faq("What happens if a driveway exceeds Clermont's impervious cap?",
            "The city can deny the design, as it did with a 2026 paver driveway expansion on Sky Ridge Road that crossed the 55 percent limit. The homeowner in that case was given 90 days to narrow the surface, swap part of it for a gravel or two-strip section, and resubmit under the cap."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Clermont, FL – County Specs",
    "meta": "Paver driveway installers near Clermont, FL: Lake County's 10-foot width minimum and flare spec outside the city, plus the ridge sand below, Oct. 2026.",
    "h1": "Paver Driveways in and Around Clermont",
    "lede": capsule(f"Paver driveway work near Clermont currently prices out at {price('paver-driveway')} per {per('paver-driveway')}, per October 2026 Florida contractor pricing. "
                     "Outside the city limits, in unincorporated Lake County, a residential driveway has its own published dimensions, a 10-foot minimum width and a required flare or radius at the road, and the excessively drained ridge sand under much of the area behaves differently from the flatwoods soil common elsewhere in the Orlando unit."),
    "sections": [
        ("Lake County's transportation standards set the driveway's width and flares",
         f"<p>For a lot outside Clermont's city limits, Lake County's own development standards set a single-family driveway at a 10-foot minimum width, with either an 8-foot radius or 8-by-4-foot flares where it meets the road, kept at least 10 feet clear of the property corner and paved back at least 10 feet from the edge of pavement "
         f"({src('lake-ldr-appendix-a', 'Lake County, LDR Appendix A Transportation Standards')}). On a curbed road, a valley gutter is required through the driveway itself. A culvert, where one is needed, either matches the neighborhood's existing culverts or runs at least 15 inches in diameter and 30 feet long "
         f"({src('lake-driveway-apron', 'Lake County, Residential Driveway Apron Permit')}). Public Works, 352-253-6019, reviews that apron permit.</p>"),
        ("Ridge sand drains fast, which changes what the base is checking for",
         f"<p>Candler soil, common on the sand hills around Clermont, is excessively drained with a water table deeper than 80 inches, and Astatula, nearby, drains just as fast with saturation more than 60 inches down "
         f"({src('nrcs-candler-osd', 'NRCS, Official Series Description, Candler')}; {src('nrcs-astatula-osd', 'NRCS, Official Series Description, Astatula')}). That's close to the opposite of the flatwoods ground that sits wet for months elsewhere in the Orlando unit, so a compacted aggregate base under {svc('paver-driveways', 'a paver driveway')} here is less often fighting a shallow water table and more often fighting loose, excessively permeable sand that needs real compaction effort to hold a stable grade under vehicle loads.</p>"),
    ],
    "scenario": ("A driveway outside the city limits, worked out in square feet",
                 f"<p>A driveway on an unincorporated Lake County lot measuring 12 by 40 feet runs 480 square feet on its own, and two 8-by-4-foot flares where it meets the road add another 64, for 544 square feet total. Multiplied against the {price('paver-driveway')} per {per('paver-driveway')} range, that comes to somewhere between $5,440 and $16,320, not counting a culvert priced separately if the lot needs one. "
                 "Because the ground here is Candler or Astatula sand rather than flatwoods clay-adjacent soil, the crew spends more of the prep time on compaction passes than on drainage planning, since the water table on ridge sand like this sits well below where the base itself ever reaches.</p>"),
    "faqs": [
        faq("How wide does a driveway have to be in unincorporated Lake County?",
            "At least 10 feet, with either an 8-foot radius or 8-by-4-foot flares where the driveway meets the road, and the paved surface has to run at least 10 feet back from the edge of pavement. Those figures apply outside the Clermont city limits."),
        faq("Does a paver driveway near Clermont need a culvert?",
            "Only where Lake County's apron permit calls for one, typically to match the culverts already in place along that stretch of road, or at least 15 inches in diameter and 30 feet long if there's no existing pattern to match."),
        faq("Does Clermont's ridge sand change how a paver base is built?",
            "It changes what the base is built to resist. Candler and Astatula sand drain excessively, so the compaction effort focuses on building a stable, well-packed base in loose sand rather than managing a shallow water table the way a flatwoods lot would."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Clermont, FL – Impervious Limits",
    "meta": "Concrete patio contractors in Clermont, FL: how a patio counts toward the city's 55% impervious cap, and grading on a sloped Lake Wales Ridge lot, Oct. 2026.",
    "h1": "Building a Concrete Patio in Clermont",
    "lede": capsule(f"Clermont homeowners pricing a concrete patio should plan on {price('concrete-patio')} per {per('concrete-patio')}, the Florida range tracked this October 2026. "
                     "A patio doesn't fall under the city's narrower 45-percent sub-cap for the house, driveway and walkways, but it still counts toward the overall 55-percent impervious ceiling on an R-1 lot, and on a lot that slopes toward Sugarloaf Mountain's hills, grading the patio away from the house matters as much as that math."),
    "sections": [
        ("A patio counts toward the 55-percent total, even though it skips the 45-percent sub-cap",
         f"<p>Clermont's R-1 zoning caps total impervious surface at 55 percent of the lot, and while the city specifically names the building, driveway and walkways under its tighter 45-percent sub-cap, a patio still adds to that broader 55-percent figure once it's poured "
         f"({src('clermont-r1-isr', 'City of Clermont, Municode Ch. 125 Div. 5, R-1')}). Call Building Services at 352-241-7315 to confirm where a new patio's square footage lands against a lot's current survey before the forms go in, particularly on a lot that already carries a pool cage or a wide driveway.</p>"),
        ("A sloped lot changes which way a patio has to shed water",
         f"<p>Clermont sits near Sugarloaf Mountain, 312 feet above sea level and the highest point on the Florida peninsula, part of a ridge of sand hills that runs through this part of Lake County "
         f"({src('wiki-sugarloaf', 'Wikipedia, Sugarloaf Mountain (Florida)')}). A backyard that drops several feet from the house to the rear property line sheds water differently than a flat lot does, so a patio's pitch gets checked against the yard's actual slope rather than assumed flat, especially where {svc('retaining-walls', 'a retaining wall')} or a terraced step already breaks up the grade nearby.</p>"),
    ],
    "scenario": ("A patio addition on a sloped lot, worked out in square feet",
                 f"<p>A 15 by 15 foot patio off the back of a Clermont house works out to 225 square feet, on a lot that drops about 3 feet from the rear door to the back fence line. That square footage against the {price('concrete-patio')} per {per('concrete-patio')} range prices the pour between roughly $1,350 and $2,925, before a stamped or decorative finish changes the number. "
                 "Before the forms go up, the crew checks the patio's square footage against the lot's current impervious total and grades the slab to carry water sideways along the slope rather than straight down toward the foundation.</p>"),
    "faqs": [
        faq("Does a concrete patio count toward Clermont's impervious limit?",
            "Yes, it adds to the overall 55 percent impervious ceiling on an R-1 lot, even though the city's tighter 45-percent sub-cap only names the house, driveway and walkways by name. Checking the current survey before pouring avoids a surprise at the zoning review."),
        faq("Why does a sloped Clermont lot need extra grading for a patio?",
            "Because the yard itself isn't flat. On a lot that drops toward the rear property line, a patio's pitch has to work with that existing slope to carry rainwater sideways rather than toward the house, which takes more site-specific planning than a patio on level ground."),
        faq("Does a patio in Clermont need a permit or just a zoning approval?",
            "Patio work on private property follows the same path as a driveway: a zoning approval and survey rather than a full building permit, filed with Building Services before the forms go in."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Clermont, FL – HOA Review",
    "meta": "Paver patio installers in Clermont, FL: Kings Ridge's two-step committee review and why most patios here are still close to a 2006-era pour, Oct. 2026.",
    "h1": "Paver Patios and Walkways for Clermont Homes",
    "lede": capsule(f"{price('paver-patio')} per {per('paver-patio')} is the going Florida range this October 2026 for a paver patio in Clermont. "
                     "In Kings Ridge, a 55-and-over community in Clermont, no exterior change clears without sign-off from two separate committees, and with the city's median home dating to 2006, a lot of paver-patio work here is an extension of a still-fairly-new builder slab rather than a full tear-out."),
    "sections": [
        ("Kings Ridge requires two committees to sign off before work starts",
         f"<p>Kings Ridge's own community FAQ spells out a two-step review: a Neighborhood Architectural Review Committee looks at the application first and helps a resident match the guidelines, then the community-wide Architectural Control Committee gives the final approval or denial, and the page states plainly, “please do not make any change without having first received the approval of both the NARC and ACC” "
         f"({ext(KINGSRIDGE_URL, 'Kings Ridge Community, Frequently Asked Questions')}). Some individual neighborhoods inside the community can layer on stricter rules of their own, so confirming which guideline applies to a specific address comes before a {cs('clermont', 'paver-patios', 'paver patio')} design is finalized.</p>"),
        ("A 2006 median build year means a lot of extensions, not tear-outs",
         f"<p>Clermont's population climbed from 42,992 in 2020 to about 52,812 by mid-2025, and the typical home here was built in 2006, the newest median construction year among the Orlando unit's incorporated cities "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {src('acs-clermont', 'Census Reporter, Clermont')}). A patio that age is usually sound enough that paver work means extending an existing slab's footprint toward a lake view or a shaded corner of the yard, tying a new edge into the original pour rather than starting from a cracked, decades-old base.</p>"),
    ],
    "scenario": ("A Kings Ridge patio extension, worked out in square feet",
                 f"<p>A Kings Ridge lanai patio extended with 260 square feet of pavers has to clear both the Neighborhood Architectural Review Committee and the community-wide Architectural Control Committee before the first paver is set. Applying the {price('paver-patio')} per {per('paver-patio')} range to that footprint prices the job between about $2,600 and $4,420, depending on the paver and base depth. "
                 "Submitting to only one of the two committees doesn't clear the project; the community's own guidance is explicit that both have to sign off before pavers go down.</p>"),
    "faqs": [
        faq("How many committees review a paver patio in Kings Ridge?",
            "Two: the Neighborhood Architectural Review Committee reviews it first, then the community-wide Architectural Control Committee gives final approval or denial. The community's own FAQ states that no change should be made without both approvals in hand."),
        faq("How old are most existing patios in Clermont?",
            "With a median home construction year of 2006, a lot of Clermont's original patio slabs are still well short of the age where resurfacing becomes the obvious call, which is part of why paver work here often means extending an existing slab rather than tearing it out."),
        faq("Do individual Clermont neighborhoods add their own paver rules on top of an HOA's?",
            "In communities like Kings Ridge, yes, some neighborhoods inside the larger community can set additional guidelines beyond the community-wide standard. Confirming which one applies to a specific address is worth doing before a design is finalized."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Clermont, FL – Sloped Lots",
    "meta": "Concrete pool deck builders in Clermont, FL: grading a deck on the Lake Wales Ridge's hills and the state's one-day watering order, Oct. 2026.",
    "h1": "Concrete Pool Decks for Clermont Homes",
    "lede": capsule(f"A concrete pool deck in Clermont falls between {price('concrete-pool-deck')} per {per('concrete-pool-deck')} under current, October 2026 Florida pricing. "
                     "On a lot that sits among the hills near Sugarloaf Mountain, the deck's finished elevation against a sloped yard matters more than it would on flat ground, and the state's current once-a-week watering order shapes the landscaping around the deck rather than the pour itself."),
    "sections": [
        ("A sloped lot changes the deck's finished elevation, not the mix design",
         f"<p>Clermont sits among the Lake Wales Ridge's sand hills, a formation that includes Sugarloaf Mountain, 312 feet above sea level and the highest point on the Florida peninsula "
         f"({src('wiki-sugarloaf', 'Wikipedia, Sugarloaf Mountain (Florida)')}). On a lot that drops toward the rear fence rather than sitting flat, the pool shell's own elevation and the deck's slope away from the house both get checked against the yard's actual grade before forms go up, since a deck poured level to a site plan drawn for a flat lot can end up shedding water the wrong direction.</p>"),
        ("The state's watering order touches the lawn around the deck, not the concrete itself",
         f"<p>Under SJRWMD's Phase III Extreme Water Shortage Order, Lake County is limited to one watering day a week, odd addresses Saturday and even addresses Sunday, with nothing between 8 a.m. and 6 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). That order governs irrigation, not the hand-watering a freshly poured deck needs during its first few days of curing, so scheduling the pour doesn't depend on which day of the week the address is assigned to water.</p>"),
    ],
    "scenario": ("A new pool deck on a graded lot, worked out in square feet",
                 f"<p>A new-construction home on a gently sloped lot pouring a 540 square foot deck around a freshly set pool shell is looking at a range of about $2,700 on the plain end up to roughly $8,100 for a cool-touch decorative surface, running that footage against the {price('concrete-pool-deck')} per {per('concrete-pool-deck')} figure. "
                 "Because the lot drops a couple of feet from the street side to the rear, the crew confirms the pool's finished elevation against that slope before the deck forms go up, rather than relying on a flat-lot site plan that doesn't match the ground.</p>"),
    "faqs": [
        faq("Do Clermont's hills change how a pool deck is built?",
            "They change what gets checked before the pour: the deck's finished elevation against the actual slope of the lot, since a site plan drawn for flat ground doesn't automatically match a yard that drops toward the rear fence near the Lake Wales Ridge hills."),
        faq("Does the state's watering order affect curing a new Clermont pool deck?",
            "No. SJRWMD's one-day-a-week order governs lawn irrigation, not the hand-watering a freshly poured deck needs during its first few days of curing, so the watering schedule assigned to an address doesn't dictate when a deck can be poured."),
        faq("What soil is typically under a Clermont pool deck?",
            "Much of the area sits on Candler or Astatula sand, both excessively drained with the water table well over 60 inches down, different from the flatwoods ground that holds water closer to the surface elsewhere in the Orlando unit."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Clermont, FL – New Builds",
    "meta": "Pool deck paver installers in Clermont, FL: why most decks here are first installs on 2006-era or newer homes, not resurfacing jobs, Oct. 2026.",
    "h1": "Travertine and Paver Pool Decks in Clermont",
    "lede": capsule(f"Clermont pool decks finished in travertine or pavers are pricing between {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, tracking current Florida contractor rates. "
                     "With Clermont's median home built in 2006, the newest of the Orlando unit's nine incorporated cities, a paver pool deck here is more often a first install alongside new construction than an overlay on a worn original deck."),
    "sections": [
        ("A newer city means more first installs than overlays",
         f"<p>Clermont's population grew from 42,992 residents in 2020 to roughly 52,812 by mid-2025, and the typical home dates to 2006 "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {src('acs-clermont', 'Census Reporter, Clermont')}). That pace of new construction means a meaningful share of the pool decks going in around Clermont are specified in travertine or pavers at the same time the pool itself is built, a design decision made once, rather than a resurfacing call on a deck that's already cracked or faded.</p>"),
        ("On a sloped lot, the deck's layout gets checked against the shell before the first course goes down",
         f"<p>A lot that sits among the Lake Wales Ridge's hills rarely has a perfectly flat building pad, so on a new pool build, the paver or travertine deck's layout gets checked against the pool contractor's shell elevation before the base is cut, the same grading question {svc('concrete-pool-decks', 'a poured concrete deck')} faces on the identical lot. Getting that elevation wrong on a sloped lot means pavers that don't sit level with the coping, a harder fix after the base is already compacted than before.</p>"),
    ],
    "scenario": ("A new paver pool deck, worked out in square feet",
                 f"<p>A newly built pool on a Clermont lot calling for 580 square feet of travertine instead of plain concrete lands in the {price('pool-deck-pavers')} per {per('pool-deck-pavers')} bracket, which works out to roughly $6,960 on the low end and $17,400 toward the high end depending on the stone and pattern chosen. "
                 "Because the deck and the pool shell are both new, the paver layout is set against the contractor's own elevation survey from the start, rather than measured against an existing deck the way an older-city resurfacing job would be.</p>"),
    "faqs": [
        faq("Are pool deck pavers in Clermont usually new construction or an overlay?",
            "More often new construction, since the city's median home was built in 2006, the newest of the Orlando unit's incorporated cities, and a lot of pools and their decks are going in together on recently graded lots rather than replacing a worn original surface."),
        faq("Does a sloped Clermont lot change how a paver pool deck is installed?",
            "It changes what gets checked first: the paver layout is set against the pool shell's actual elevation on a lot that isn't perfectly flat, rather than assumed level the way it might be on flat ground."),
        faq("What's the price range for travertine or pavers on a Clermont pool deck?",
            f"{price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026, a range that moves with the stone, pattern and whether the deck is new construction or an overlay on an existing slab."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Clermont, FL – Zoning & Grip",
    "meta": "Stamped concrete contractors in Clermont, FL: the same $45 zoning approval as plain concrete, and texture choices for a sloped driveway, Oct. 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Clermont",
    "lede": capsule(f"Budget {price('stamped-concrete')} per {per('stamped-concrete')} for a stamped-concrete project in Clermont; where the final number lands within that current Florida range depends on the pattern and how many colors go into the pour. "
                     "The city doesn't review a stamped driveway any differently than a plain gray one, a zoning approval rather than a building permit either way, though on a sloped lot, the texture itself is worth picking with grip in mind, not just color."),
    "sections": [
        ("The zoning approval doesn't change because the finish is decorative",
         f"<p>Clermont's checklist for driveway and sidewalk work on private property calls for a zoning approval, a notarized application and a survey, for a flat $45 fee with no inspection "
         f"({src('clermont-permit-checklists', 'City of Clermont, Permit Checklists')}). A stamped slate or ashlar pattern, an integral color, or a decorative border doesn't move that review into a different category or change the fee; the survey still has to show the same impervious-surface math a plain pour would, under the R-1 district's 45-percent sub-cap "
         f"({src('clermont-r1-isr', 'City of Clermont, Municode Ch. 125 Div. 5, R-1')}).</p>"),
        ("On a sloped driveway, the stamp pattern is a traction decision as much as a style one",
         "<p>On a lot that drops toward the garage rather than sitting flat, a deeply grooved slate or cobble pattern holds a tire or a shoe better in a sudden Florida downpour than a smooth, lightly textured stamp does, which is a reason to pick the pattern with the slope in mind rather than purely on how it looks dry. A release agent that's too glossy can make that same slope slicker when wet, something worth weighing against the color before a sample board gets approved.</p>"),
    ],
    "scenario": ("A stamped driveway on a graded lot, worked out in square feet",
                 f"<p>A slate-pattern stamped finish with an integral color over a 280 square foot driveway apron section, on a lot that slopes down toward the garage, falls somewhere between $2,240 and $5,320 once the {price('stamped-concrete')} per {per('stamped-concrete')} range is applied, with the number of colors and the release agent swinging it toward either end. "
                 "Before the pour, the pattern depth gets weighed against the slope itself, since a flatter texture that looks fine on a level walkway can turn slick on a graded driveway after a heavy afternoon storm.</p>"),
    "faqs": [
        faq("Does a stamped driveway need a different approval than plain concrete in Clermont?",
            "No, both go through the same zoning approval rather than a building permit, with the same $45 fee and survey requirement. The decorative finish doesn't change which office reviews the job."),
        faq("Does Clermont's impervious cap change for a stamped or decorative finish?",
            "No, the 45-percent sub-cap for the building, driveway and walkways in the R-1 district is based on square footage, not finish, so a stamped pour counts the same as a plain one against that figure."),
        faq("What stamped pattern works best on a sloped Clermont driveway?",
            "A deeper, more textured pattern like slate or cobble tends to hold traction better on a graded driveway in the rain than a smoother, finer stamp does, and a less glossy release agent helps avoid adding slickness on top of the slope."),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Sidewalks & Walkways in Clermont, FL – Permits",
    "meta": "Concrete walkway contractors near Clermont, FL: Lake County's 30-inch exemption outside the city, and the zoning approval inside it, Oct. 2026.",
    "h1": "Concrete Sidewalks and Walkways In and Near Clermont",
    "lede": capsule(f"A concrete walkway near Clermont runs {price('concrete-walkway')} per {per('concrete-walkway')} as of October 2026. "
                     "Just outside the city limits, in unincorporated Lake County, a walkway under 30 inches above grade is exempt from a building permit entirely; inside Clermont, that same walkway instead goes through the city's $45 zoning approval, the same process a driveway uses."),
    "sections": [
        ("Outside the city, a low walkway can skip the building permit altogether",
         f"<p>Lake County's exemption list, built on Florida Building Code 105.2 #2, covers “sidewalks and driveways not more than 30 inches (762 mm) above adjacent grade,” as long as the walkway doesn't sit over a basement or lower story and isn't part of a required accessible route, zoning and flood requirements still apply on top of that exemption "
         f"({src('lake-exempt', 'Lake County, Residential Work Exempt from Permits')}). That exemption covers most ordinary front walkways, since a walk from the driveway to the door rarely climbs anywhere near 30 inches off the yard.</p>"),
        ("Inside the city, the walkway follows the same zoning path as a driveway",
         f"<p>Once a lot sits inside Clermont's city limits, that same low walkway no longer qualifies for the county's height-based exemption; it instead goes through the city's zoning approval, a notarized application and survey for a flat $45 fee with no inspection, the identical process the city applies to {cs('clermont', 'concrete-driveways', 'driveway work')} "
         f"({src('clermont-permit-checklists', 'City of Clermont, Permit Checklists')}). Confirming which side of the city line a lot actually sits on is worth a call to Building Services, 352-241-7315, before assuming the county's exemption applies.</p>"),
    ],
    "scenario": ("A front walkway replacement, worked out in square feet",
                 f"<p>Say a 4-foot-wide, 40-foot-long front walkway, 160 square feet, needs replacing between the driveway and the entry. At {price('concrete-walkway')} per {per('concrete-walkway')}, that lands between roughly $1,120 and $2,720. "
                 "On a lot in unincorporated Lake County, a walkway that low off the grade typically clears the county's building-permit exemption outright; on an otherwise identical lot inside the Clermont city limits, the same walkway instead goes through the city's $45 zoning approval before the old concrete comes out.</p>"),
    "faqs": [
        faq("Is a walkway exempt from a permit in unincorporated Lake County?",
            "Often, yes, if it stays under 30 inches above the adjacent grade and isn't part of a required accessible route. Zoning and flood requirements still apply even where the building-permit exemption covers the walkway itself."),
        faq("Does a walkway need a different review than a driveway inside Clermont?",
            "No, the city applies the same zoning-approval process to both, a notarized application and survey for a flat $45 fee with no inspection, rather than treating a walkway as a separate permit category."),
        faq("How do I know if my Clermont-area lot is inside or outside the city limits?",
            "Building Services, 352-241-7315, can confirm from the address. That distinction decides whether a low walkway qualifies for Lake County's height-based exemption or instead needs the city's own zoning approval."),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Clermont, FL – Sheds & Pads",
    "meta": "Concrete slab contractors near Clermont, FL: Lake County's unpublished slab threshold and building on excessively drained ridge sand, Oct. 2026.",
    "h1": "Concrete Slabs for Sheds, Pads and Parking Near Clermont",
    "lede": capsule(f"A concrete slab near Clermont is pricing between {price('concrete-slab')} per {per('concrete-slab')} this October 2026, per published Florida contractor figures. "
                     "Lake County's homeowner exemption spells out a height limit for driveways and sidewalks but stays silent on a shed, AC or parking slab specifically, so confirming that one directly with the Building Services office is part of planning the job, and the ridge sand under much of the area changes what the base is actually compacting against."),
    "sections": [
        ("A gap worth a phone call before the forms go up",
         f"<p>Lake County's exemption guidance names sidewalks and driveways under 30 inches above grade and masonry or concrete fences 4 feet or shorter as building-permit exempt, but it doesn't spell out a comparable threshold for a stand-alone shed, AC or parking pad "
         f"({src('lake-exempt', 'Lake County, Residential Work Exempt from Permits')}). Building Services, 352-343-9634, is the office to call before assuming a given slab qualifies for an exemption or needs a full permit "
         f"({src('lake-building-services', 'Lake County, Building Services')}).</p>"),
        ("Excessively drained ridge sand changes what the compaction test is checking for",
         f"<p>Much of the ground around Clermont is Candler or Astatula soil, both excessively drained with the water table more than 60 inches down "
         f"({src('nrcs-candler-osd', 'NRCS, Official Series Description, Candler')}; {src('nrcs-astatula-osd', 'NRCS, Official Series Description, Astatula')}). Under a shed pad or {svc('concrete-slabs', 'a parking slab')}, that means the subgrade rarely holds standing water the way flatwoods soil does elsewhere in the Orlando unit, but loose, fast-draining sand still needs real compaction passes to hold a stable grade under the slab, rather than simply being assumed firm because it drains well.</p>"),
    ],
    "scenario": ("A shed pad on ridge sand, worked out in square feet",
                 f"<p>An 8 by 13 foot shed pad, 104 square feet, going in on a side yard mapped as Candler fine sand prices out between about $416 and $1,040 once the {price('concrete-slab')} per {per('concrete-slab')} figure is applied, depending on the mix and reinforcement. "
                 "Before the forms go up, a quick call to Lake County Building Services confirms whether a pad that size needs a full permit or qualifies for an exemption, since the county's published list doesn't name sheds or pads the way it names driveways and sidewalks.</p>"),
    "faqs": [
        faq("Does a shed slab need a permit near Clermont?",
            "Lake County's exemption list doesn't spell out a threshold for a shed or utility pad the way it does for driveways and sidewalks, so a call to Building Services at 352-343-9634 is worth making before assuming a given size is exempt."),
        faq("Does Clermont's ridge sand change how a slab is built?",
            "It changes what the compaction is managing. Candler and Astatula sand drain fast and rarely hold a shallow water table, but the loose sand still needs thorough compaction to hold a stable grade under the slab rather than settling later."),
        faq("Is an AC pad treated the same as a shed pad near Clermont?",
            "Likely, though neither has a published size threshold the way driveways do, so confirming with Lake County Building Services before pricing either one avoids assuming an exemption that may not apply."),
    ],
    "sources": SRC,
}

# 10. concrete-repair ----------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair & Resurfacing in Clermont, FL",
    "meta": "Concrete repair in Clermont, FL: why cracking here often traces to fill settlement on a graded lot, not sinkhole activity, as of October 2026.",
    "h1": "Concrete Repair and Resurfacing in Clermont",
    "lede": capsule(f"Concrete repair and resurfacing work in Clermont is pricing between {price('concrete-repair')} per {per('concrete-repair')}, Florida contractor figures current for late 2026. "
                     "With the city's median home dating to 2006, the newest in the Orlando unit, cracking here more often traces back to fill settlement on a newly graded, sloped lot than to decades of ordinary wear, and Lake County isn't one of the counties the state ties to heavy sinkhole claims."),
    "sections": [
        ("A young, fast-growing city means settlement cracking more than age cracking",
         f"<p>Clermont's population jumped from 42,992 in 2020 to about 52,812 by mid-2025, and the median home here was built in 2006 "
         f"({src('census-pep-v2025', 'Census Bureau PEP, Vintage 2025')}; {src('acs-clermont', 'Census Reporter, Clermont')}). On ground that's been graded and filled to build a driveway or patio pad on a sloped Lake Wales Ridge lot, a crack is more often explained by that fill settling under the slab than by decades of joint fatigue the way it would be in an older, flatter town.</p>"),
        ("Lake County isn't on the state's list of the heaviest sinkhole-claims counties",
         f"<p>A 2010 Florida Senate interim report traces upwards of 88 percent of the sinkhole insurance claims Florida insurers paid out in the 2006-to-2009 window to just eleven counties: Pinellas, Hillsborough, Pasco, Citrus, Marion, Hernando, Miami-Dade, Broward, Alachua, Orange and Polk "
         f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). Lake County doesn't make that roster, even though Orange and Polk, both neighbors, do, so a dip or crack showing up in a Clermont driveway more plausibly comes from fill settling under a graded hillside lot, or a cracked irrigation line, than from the sudden ground collapse behind that claims data.</p>"),
    ],
    "scenario": ("Patching a settlement crack on a graded lot, worked out in square feet",
                 f"<p>A 350 square foot section of driveway on a lot built around 2010, showing a diagonal crack along the low side of a graded slope, can run anywhere from $1,050 up near $3,500 to resurface, applying the {price('concrete-repair')} per {per('concrete-repair')} figure; a plain broom finish sits toward the bottom of that span, and folding in a decorative overlay pushes it higher. "
                 "Tracing the crack back to the fill that was placed when the lot was graded, rather than assuming it, helps decide whether the subgrade under that section needs re-compacting before the surface repair goes on.</p>"),
    "faqs": [
        faq("Why would a newer Clermont driveway already be cracking?",
            "More often fill settlement than age. On a lot that was graded and filled to build a pad on a sloped site, the ground under the slab can settle in the first years after the pour, which shows up as a crack well before decades of ordinary wear would explain it."),
        faq("Does Clermont see the sinkhole activity that Polk or Orange counties do?",
            "Not by the state's own count. A 2010 Florida Senate report lists Polk and Orange among the eleven counties with the heaviest sinkhole claims statewide between 2006 and 2009; Lake County doesn't appear on that roster. Settling fill explains most local cracking far more often."),
        faq("Is a permit needed to resurface a driveway in Clermont?",
            "Resurfacing that stays within the existing footprint typically follows the same zoning-approval path as a new driveway, though confirming the scope with Building Services before assuming a lighter review avoids a surprise."),
    ],
    "sources": SRC,
}

# 11. paver-sealing -------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing & Restoration in Clermont, FL",
    "meta": "Paver sealing in Clermont, FL: why the state's once-a-week watering order doesn't cover a pressure washer, and ridge sand's drying effect, Oct. 2026.",
    "h1": "Paver Sealing and Restoration in Clermont",
    "lede": capsule(f"Cleaning, re-sanding and sealing pavers in Clermont falls between {price('paver-sealing')} per {per('paver-sealing')}, Florida pricing current for this October. "
                     "Lake County's current once-a-week watering order governs lawn irrigation, not a hose-fed pressure washer, and the excessively drained ridge sand under most Clermont yards dries a cleaned paver surface faster than flatwoods ground would elsewhere."),
    "sections": [
        ("A pre-seal pressure wash doesn't follow the state's watering calendar",
         f"<p>Under SJRWMD's Phase III Extreme Water Shortage Order, Lake County addresses are limited to a single watering day a week, Saturday for odd addresses and Sunday for even ones, with nothing allowed between 8 a.m. and 6 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). That order covers sprinklers watering grass, not a hose running through a pressure washer to clean algae and grime off a paver surface ahead of sealing, so the clean-and-re-sand step before a seal can be scheduled around the crew's calendar and the weather rather than a specific address's watering day.</p>"),
        ("Ridge sand means pavers dry out faster between rain events",
         f"<p>Candler and Astatula soil, common under Clermont-area yards, are both excessively drained, with the water table more than 60 inches below the surface "
         f"({src('nrcs-candler-osd', 'NRCS, Official Series Description, Candler')}; {src('nrcs-astatula-osd', 'NRCS, Official Series Description, Astatula')}). A paver surface set on a base over that kind of sand sheds water and dries faster after a storm than one set over the flatwoods soil common elsewhere in the Orlando unit, which can mean less of the standing moisture that feeds algae and mold between {svc('paver-sealing', 'sealing cycles')}.</p>"),
    ],
    "scenario": ("Resealing a Clermont paver patio, worked out in square feet",
                 f"<p>A 380 square foot paver patio due for a wash, a polymeric sand refresh and a fresh seal coat falls in the $570 to $1,235 range once the {price('paver-sealing')} per {per('paver-sealing')} figure is applied to that footprint, with any sunken pavers that need releveling pushing the total toward the upper end. "
                 "Because the patio sits on fast-draining ridge sand rather than flatwoods ground, the clean-and-dry window before the sealer goes on tends to run shorter after a summer storm than it would on a lot with slower-draining soil.</p>"),
    "faqs": [
        faq("Can pavers be pressure-washed on a day Clermont's watering order doesn't allow?",
            "Yes. The state's once-a-week order governs sprinkler irrigation, not a hose-fed pressure washer, so the pre-seal cleaning can happen on whichever day the crew and the weather line up, regardless of the address's assigned watering day."),
        faq("Does Clermont's soil affect how often pavers need resealing?",
            "It can affect how fast the surface dries after rain rather than the sealing interval itself. The excessively drained ridge sand common here sheds water faster than flatwoods soil, which can mean less standing moisture feeding algae between cleanings."),
        faq("Is a permit required to reseal an existing paver driveway in Clermont?",
            "No. Maintenance on pavers that are already down, cleaning, re-sanding or sealing, isn't the kind of new construction the city's zoning-approval process is built to review."),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Clermont, FL – 3-Foot Rule",
    "meta": "Retaining wall contractors in Clermont, FL: the city's 3-foot engineering trigger and the Lake Wales Ridge terrain behind the demand, as of October 2026.",
    "h1": "Retaining Walls for Clermont's Hillside Yards",
    "lede": capsule(f"Retaining wall construction in Clermont runs between {price('retaining-wall')} per {per('retaining-wall')}, based on current Florida contractor data for this fall. "
                     "The city's own permit guidance draws a clear line at 3 feet: shorter walls still need a permit but skip engineered plans, while anything taller needs a sealed design, a distinction that comes up often on the sloped lots near Sugarloaf Mountain and the Lake Wales Ridge."),
    "sections": [
        ("Clermont's 3-foot line decides whether an engineer signs the plans",
         f"<p>The city's permit type descriptions state it directly: “Retaining Walls less than 3 ft in heights still require a permit, however do not require engineered plans unless they are over 3 ft in height” "
         f"({src('clermont-permit-types', 'City of Clermont, Permit Type Descriptions')}). That means even a low seat wall holding back a couple of feet of fill at the edge of a patio needs a permit filed with Building Services, 352-241-7315, even though it skips the added cost and time of a sealed engineering drawing.</p>"),
        ("The hills that make retaining walls common have a name and an elevation",
         f"<p>Sugarloaf Mountain, just outside Clermont, rises 312 feet above sea level, the highest point on the Florida peninsula, part of the Lake Wales Ridge, “a series of sand hills running south to Highlands County” "
         f"({src('wiki-sugarloaf', 'Wikipedia, Sugarloaf Mountain (Florida)')}). The Candler and Astatula sand that makes up much of that ridge is excessively drained, so a wall cut into a slope here is usually managing loose, dry sand that wants to slump downhill rather than wet clay pushing against the wall face the way it might on flatwoods ground "
         f"({src('nrcs-candler-osd', 'NRCS, Official Series Description, Candler')}).</p>"),
    ],
    "scenario": ("A low seat wall on a sloped lot, worked out in square feet",
                 f"<p>Holding a terraced planting bed at the edge of a Clermont patio might take a block wall running 28 feet along the bed and standing 3 feet tall, 84 square feet of face once multiplied out. Applying the {price('retaining-wall')} per {per('retaining-wall')} figure to that area puts the job in the neighborhood of $1,260 to $3,360, before drainage behind the wall is figured in. "
                 "Staying right at 3 feet keeps the wall on the simpler side of the city's rule, filed with a permit but without a sealed engineering drawing; going even a few inches taller moves the same wall into the engineered category.</p>"),
    "faqs": [
        faq("Does a 3-foot retaining wall need an engineer in Clermont?",
            "No. The city's own guidance says a wall under 3 feet still needs a permit but doesn't require engineered plans. Once a wall passes 3 feet, a sealed engineering drawing becomes part of the submission."),
        faq("Why are retaining walls common on Clermont's sloped lots?",
            "Clermont sits among the Lake Wales Ridge's hills, the same formation that includes Sugarloaf Mountain, the highest point on the Florida peninsula. A lot that drops several feet across the yard needs something to hold the grade at a driveway, patio or pool deck edge."),
        faq("Does Lake County require anything different for a retaining wall outside Clermont?",
            "Lake County's own guidance doesn't publish a specific height threshold for a retaining wall, unlike the city's clear 3-foot line. Calling Building Services at 352-343-9634 before finalizing a design on an unincorporated lot is worth the time."),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Clermont, FL – Watering Order",
    "meta": "Artificial turf installers in Clermont, FL: the state's once-a-week order for sod versus turf, and the 10-foot lake setback, as of October 2026.",
    "h1": "Artificial Turf for Clermont Yards",
    "lede": capsule(f"Artificial turf installation in Clermont is priced between {price('artificial-turf')} per {per('artificial-turf')}, current Florida figures for this fall. "
                     "Under the state's current Phase III order, Lake County addresses water lawns just one day a week, a tighter calendar than the normal twice-weekly schedule, while turf itself sidesteps that calendar entirely once the base is set, and near any of Clermont's lakes, a 10-foot setback from the water still applies."),
    "sections": [
        ("One day a week makes a sloped sod lawn harder to keep alive",
         f"<p>SJRWMD's Phase III Extreme Water Shortage Order limits Lake County to a single watering day, odd addresses on Saturday and even addresses on Sunday, with nothing between 8 a.m. and 6 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). On a lot that slopes toward Sugarloaf Mountain's hills, water runs off a graded yard faster than it does on flat ground to begin with, so new sod trying to establish on one watering day a week struggles more on a slope than it would on level turf, which is part of why {svc('artificial-turf', 'artificial turf')} comes up as an option for the steepest section of a yard.</p>"),
        ("A 10-foot setback applies near any of Clermont's lakes",
         f"<p>The city describes itself around its “fresh water bodies” among its defining features "
         f"({src('clermont-econ', 'City of Clermont, Economic Information')}), and the state's synthetic-turf standard sets a 10-foot minimum buffer between installed turf and a pond, lake or canal, waived only where a seawall forms the edge; underneath the turf itself, the rule rules out buried irrigation and calls instead for a washed base topped with natural infill "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A 2025 law layered on top of that limits how far a city or county can push its own turf restrictions further, though it leaves an HOA's own rules untouched "
         f"({src('fs125572', 'Florida Statutes §125.572')}).</p>"),
    ],
    "scenario": ("Turf on a sloped lot near the water, worked out in square feet",
                 f"<p>A backyard sloping toward a neighborhood lake, fenced in at 560 square feet, loses some of that to the required buffer once the turf layout is pulled back from the shoreline, leaving around 520 square feet to actually install. Running that against the {price('artificial-turf')} per {per('artificial-turf')} figure prices the job between roughly $5,200 and $13,000, depending on the pile height and backing chosen. "
                 "Because the lot slopes and sits near the water, the layout is measured against both the buffer and the grade before the base is cut, rather than against the full fenced area originally measured.</p>"),
    "faqs": [
        faq("Does Clermont's watering order affect new sod differently than turf?",
            "Yes. Sod planted under the one-day-a-week order has less room to recover between waterings, especially on a sloped lot where runoff is faster, while installed turf doesn't need watering at all once the base is set."),
        faq("How close to a Clermont lake can artificial turf be installed?",
            "The state standard requires a 10-foot buffer between the turf and the water, waived only where the edge is a seawall rather than open shoreline. Underneath the turf itself, buried irrigation is off the table, and the base has to be washed stone topped with natural infill."),
        faq("Can an HOA in the Clermont area ban artificial turf entirely?",
            "State law limits how far a city or county can restrict residential turf, though an HOA's own design guidelines can still add rules beyond that, which is worth checking with the specific community before installation."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
