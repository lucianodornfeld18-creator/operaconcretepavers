# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, table, faq, svc, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "oviedo"

WATER_ATLAS_URL = "https://seminole.wateratlas.usf.edu/library/learn-more/learnmore.aspx?toolsection=lm_soils"
ECON_WIKI_URL = "https://en.wikipedia.org/wiki/Econlockhatchee_River"
OVIEDO_WIKI_URL = "https://en.wikipedia.org/wiki/Oviedo,_Florida"

SRC = [
    "census-pep-v2025", "acs-oviedo",
    "oviedo-building-services", "oviedo-row-type1", "oviedo-slab-paver", "oviedo-permit-guidelines",
    "seminole-driveway-app", "seminole-hb803",
    "sjrwmd-watering", "fl-dos-state-soil", "fl-senate-2011-104", "dep-rule", "fs125572", "oviedo-otp",
    (f"Seminole County Water Atlas, Learn More: Soils", WATER_ATLAS_URL),
    ("Wikipedia, Econlockhatchee River", ECON_WIKI_URL),
    ("Wikipedia, Oviedo, Florida", OVIEDO_WIKI_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Does Oviedo's 2026 permit exemption cover a new driveway or paver patio?",
        "<p>House Bill 803 took effect July 1, 2026 and frees a homeowner, or the contractor working for one, from a building permit on residential work valued under $7,500. Oviedo's Building Services department confirms that exemption applies here, then publishes its own list of “Non-Structural residential work that would still require a planning and zoning permit through the Planning Department,” and two lines on that list matter most to anyone pouring or paving: "
        f"“Pavers/driveways/sidewalks on private property” and “Non-structural 4\" concrete slabs on grade” "
        f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). In plain terms, the 2026 exemption doesn't reach {cs('oviedo', 'paver-driveways', 'a paver driveway')} or {cs('oviedo', 'concrete-patios', 'a patio slab')} inside the city limits; a planning and zoning permit still applies. Call Building Services at 407-971-5755 or buildingpermits@cityofoviedo.net before ordering material, since the city's own guidance is specific about what it exempts and what it doesn't.</p>"),
    sec("What does a right-of-way permit for the apron cost in Oviedo?",
        f"<p>Any part of a driveway, walk or paver apron that crosses the right-of-way, the strip between a homeowner's property line and the street, needs its own Right-of-Way Type I application through the Development Review Division at 400 Alexandria Blvd., 407-971-5796. The current form, revised October 2023, carries an application fee of $79.00 plus a $25.00 technology fee, $104.00 total, and the city asks for a sealed boundary survey, a maintenance-of-traffic plan and a certificate of insurance alongside it "
        f"({src('oviedo-row-type1', 'City of Oviedo, Right-of-Way Type I Application')}). That review runs separately from, and on top of, whatever permit covers the rest of {svc('concrete-driveways', 'the driveway')} on private ground.</p>"),
    sec("Outside the city, Seminole County caps a driveway at 18 feet plus flares",
        f"<p>A fair amount of ground with an Oviedo mailing address actually sits in unincorporated Seminole County, where a different office, the Development Review Division, reviews the Residential Driveway Construction Application (Plandesk@seminolecountyfl.gov, 407-665-7371, with inspections called in 24 to 48 hours ahead at 407-665-7409). The form's own numbers are specific "
        f"({src('seminole-driveway-app', 'Seminole County, Residential Driveway Construction Application')}):</p>"
        + table("Seminole County residential driveway specifications (unincorporated area)",
                ["Item", "County requirement"],
                [["Driveway width", "18 ft maximum, with 3 ft flares (24 ft total at the roadway)"],
                 ["Driveway material in the ROW", "6 in of non-steel or fiber-reinforced concrete, 3,000 psi minimum"],
                 ["Culvert diameter", "18 in minimum, or per an engineer's specification"],
                 ["Setback from property line", "5 ft minimum"],
                 ["Clearance from a neighbor's flare", "6 ft minimum"]],
                "Source: Seminole County Residential Driveway Construction Application, checked October 2026. Pavers are allowed in the right-of-way but not across a crosswalk or sidewalk section, and the county won't replace paver sections it has to cut into later.")
        + f"<p>The county's own 2026 rundown of HB 803's new exemptions lists fences, pergolas, floating docks, non-bearing interior walls, cabinets and sheds of 200 sq ft or less, and it doesn't mention driveways, pavers, slabs or retaining walls at all "
        f"({src('seminole-hb803', 'Seminole County, New State Legislation Affecting Permits')}), so a {cs('oviedo', 'retaining-walls', 'retaining wall')} or a parking pad on an unincorporated lot still goes through standard review; call the Building Division at 407-665-7050 to confirm scope before pricing the job.</p>"),
    sec("How do the Econlockhatchee River and Lake Jesup change where water goes on a lot?",
        f"<p>Oviedo grew up on the shore of Lake Jesup, where homesteaders settled in 1875, and the city is still bordered by that lake to the north and by the Econlockhatchee River, a 54.5-mile blackwater tributary of the St. Johns River, running through its eastern side, with the Little Econlockhatchee River crossing the south "
        f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}; {ext(ECON_WIKI_URL, 'Wikipedia, Econlockhatchee River')}). Neither the city's permit guidance nor Seminole County's driveway application publishes a stand-alone setback from either waterway for a {svc('concrete-pool-decks', 'pool deck')} or a {svc('retaining-walls', 'retaining wall')}; the grading question on a lot that slopes toward the river corridor or the lake is about where the fill goes and how the pad or wall sheds water, which a site visit settles before forms go up, not a published number to look up.</p>"),
    sec("What does a median 1997 build year mean for an Oviedo project?",
        f"<p>Seminole County counted Oviedo's population at 41,317 residents on July 1, 2025 "
        f"({src('census-pep-v2025', 'Census Bureau, Vintage 2025 population estimates')}), and the city's typical home dates to 1997 "
        f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), newer than a lot of Central Florida's older suburbs but old enough that an original driveway or patio slab is approaching three decades of Florida summers. Much of that growth traces back to the University of Central Florida, chartered in 1963 a short drive west, and the Central Florida Research Park that followed in 1978, which pulled rooftops out past the old Lake Jesup settlement and its historic downtown, where free-roaming chickens were once a local fixture "
        f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). More recently, the city's own Oviedo on the Park development has added newer construction around Center Lake Park, “the crown jewel of the city's new Oviedo on the Park development area” "
        f"({src('oviedo-otp', 'City of Oviedo, Oviedo on the Park')}), so a two-year-old {svc('concrete-pool-decks', 'pool deck')} there and a 1997-era original a few miles away aren't rare to find on the same street map.</p>"),
    sec("Does Oviedo's soil hold water the way the rest of Seminole County's flatwoods does?",
        f"<p>Seminole County's own water-quality education program names Myakka fine sand as “typical” of the flatwoods ground found across the county, and the state legislature designated Myakka fine sand Florida's official state soil in 1989, found on more than 1.5 million acres statewide "
        f"({ext(WATER_ATLAS_URL, 'Seminole County Water Atlas, Learn More: Soils')}; {src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}). Flatwoods ground like that holds a water table close to the surface for part of a typical year, which is the reason a crew checks a yard with a shovel before pricing {svc('concrete-slabs', 'a slab')} or a {svc('paver-patios', 'paver patio')}, rather than assuming every Seminole County lot drains the way a ridge-sand lot farther west does.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Does the City of Oviedo or Seminole County review my driveway permit?",
        "It depends on whether the lot sits inside the city limits or in the surrounding unincorporated county, which can share the same mailing address. Oviedo's Building Services reviews work inside the limits and its Right-of-Way Type I application covers anything touching the street; the county's Development Review Division reviews everything outside the line."),
    faq("What are Oviedo's current watering days for new sod or landscaping?",
        f"St. Johns River Water Management District runs a year-round, twice-a-week schedule here: during Daylight Saving Time, odd-numbered and no-number addresses water Wednesday and Saturday, even-numbered addresses water Thursday and Sunday, with nothing allowed between 10 a.m. and 4 p.m. "
        f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). New landscaping can water daily for 30 days, then every other day for 30 more before dropping to that standard schedule."),
    faq("Does the 2026 permit exemption mean I can pour a patio slab in Oviedo without a permit?",
        "No. Oviedo's own carve-out list keeps a planning and zoning permit on non-structural 4-inch slabs on grade and on pavers, driveways and sidewalks on private property, even though the same work might clear the state's new $7,500 exemption threshold for a building permit elsewhere."),
    faq("Is there a published setback from the Econlockhatchee River or Lake Jesup for a pool deck or wall?",
        "Not one we found in either the city's or the county's permit guidance. A lot that slopes toward the river corridor or the lake gets its grading and fill checked on site, since the general rule is to keep water moving away from the house and off a neighbor's yard, not a specific foot count published for either waterway."),
    faq("How do I pick the best concrete contractor for a job in Oviedo?",
        f"Check the contractor on the state's license-verification tool, confirm whether the city's Building Services or Seminole County's Development Review Division actually reviews your lot before a quote assumes one or the other, and ask how the bid handles a flatwoods water table. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Our guide to choosing a concrete contractor')} covers the rest."),
    faq("Does a retaining wall in Oviedo need an engineer's drawings?",
        f"Yes, the city's wall permit guideline requires “signed and sealed engineered drawings” with wind design data for a freestanding or retaining wall, and it doesn't state a height below which that requirement drops away "
        f"({src('oviedo-permit-guidelines', 'City of Oviedo, Permit Guidelines')})."),
]

HUB = page("/oviedo-fl/", "city", "Concrete, Pavers & Turf Contractor in Oviedo, FL",
           "Opera builds concrete driveways, pavers and turf in Oviedo, FL, where a planning permit still covers pavers under the city's 2026 exemption list, as of October 2026.",
           "Concrete, Pavers and Artificial Turf for Oviedo Homes",
           capsule(f"Opera pours concrete, sets pavers and installs artificial turf for homes in Oviedo, a Seminole County city of about 41,317 residents roughly {str(__import__('_data').CITIES['oviedo']['miles'])} miles from the Orlando unit's base. "
                   f"A new concrete driveway here runs {price('concrete-driveway')} per {per('concrete-driveway')}, a Florida market range as of October 2026, and a paver driveway or patio slab still needs the city's planning and zoning permit even though House Bill 803 exempted other remodeling work from a building permit in 2026."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Oviedo",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/seminole-county-driveway-patio-permits/", "Driveway and patio permits in Seminole County"),
                    ("/winter-springs-fl/", "Concrete, pavers and turf in Winter Springs"),
                    ("/lake-mary-fl/", "Concrete, pavers and turf in Lake Mary"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Oviedo, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Oviedo, FL – Permits",
    "meta": "Concrete driveway contractors in Oviedo, FL: the city's $104 right-of-way fee versus Seminole County's 18-foot width cap, as of October 2026.",
    "h1": "Pouring or Replacing a Concrete Driveway in Oviedo",
    "lede": capsule(f"A new or replacement concrete driveway in Oviedo runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "Inside the city, the private portion is reviewed separately from the apron crossing into the right-of-way, which carries its own $104 application fee; in unincorporated Seminole County, the whole driveway instead goes through a single county application capped at 18 feet wide."),
    "sections": [
        ("Inside Oviedo, the apron gets its own $104 right-of-way review",
         f"<p>Where a driveway meets the street, that section falls under the city's Right-of-Way Type I application, filed with the Development Review Division at 400 Alexandria Blvd., 407-971-5796. The current form, revised October 2023, totals $104.00, a $79.00 application fee plus a $25.00 technology fee, and the city also wants a sealed boundary survey, a maintenance-of-traffic plan and proof of insurance before it signs off "
         f"({src('oviedo-row-type1', 'City of Oviedo, Right-of-Way Type I Application')}). The rest of the slab on private ground is a separate planning and zoning permit, since Oviedo's own 2026 exemption list keeps driveways on private property out of the building-permit exemption HB 803 otherwise created "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}).</p>"),
        ("Outside the city, one county application sets the width at 18 feet",
         f"<p>A lot carrying an Oviedo address can still sit in unincorporated Seminole County, where the Residential Driveway Construction Application caps a driveway at 18 feet wide, 24 feet counting the 3-foot flares on each side, and requires 6 inches of non-steel or fiber-reinforced concrete at 3,000 psi inside the right-of-way "
         f"({src('seminole-driveway-app', 'Seminole County, Residential Driveway Construction Application')}). That review runs through the county's Development Review Division (Plandesk@seminolecountyfl.gov, 407-665-7371) rather than the city desk, and a driveway planned wider than 18 feet on an unincorporated lot is worth confirming against that cap before {cs('oviedo', 'paver-driveways', 'a paver driveway')} or a wide concrete apron gets designed.</p>"),
    ],
    "scenario": ("A two-car driveway crossing the right-of-way, worked out in square feet",
                 f"<p>Picture a 24 by 22 ft two-car driveway, 528 sq ft, replacing an original slab on a lot inside the Oviedo city limits. At {price('concrete-driveway')} per {per('concrete-driveway')}, the private portion lands between roughly $3,168 and $7,920 before demolition is added. "
                 "A 9 by 5 ft section of that same driveway, 45 sq ft, sits in the right-of-way where it meets the street, and that piece adds the separate $104 Right-of-Way Type I fee on top of the per-square-foot driveway cost, along with the survey and traffic-control plan the city asks for before approving it. On an otherwise identical lot in unincorporated Seminole County, that same width clears the county's 18-foot cap without a conditional review.</p>"),
    "faqs": [
        faq("Does Oviedo charge a separate fee for the part of my driveway that meets the street?",
            "Yes. The Right-of-Way Type I application covers that section, $79.00 plus a $25.00 technology fee, $104.00 total, filed with the Development Review Division along with a sealed survey, a traffic-control plan and proof of insurance."),
        faq("How wide can a driveway be in unincorporated Seminole County?",
            "The county's Residential Driveway Construction Application caps an ordinary driveway at 18 feet wide, 24 feet including the 3-foot flares on each side, reviewed by the Development Review Division rather than the city."),
        faq("Does Oviedo's 2026 permit exemption cover a new driveway?",
            "No. The city's own list of work that still needs a planning and zoning permit names “pavers/driveways/sidewalks on private property” directly, so HB 803's $7,500 building-permit exemption doesn't reach a driveway inside the city limits."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Oviedo, FL – 2026 Exemption",
    "meta": "Paver driveway installers in Oviedo, FL: why HB 803's 2026 exemption still leaves pavers on the city's planning-permit list, October 2026.",
    "h1": "Paver Driveways in Oviedo: What the 2026 Exemption Doesn't Cover",
    "lede": capsule(f"A paver driveway in Oviedo runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026, roughly double the plain-concrete range on material and base labor. "
                     "Florida's 2026 building-permit exemption for small residential jobs doesn't reach it: the city's own guidance names pavers on private property directly as work that still needs a planning and zoning permit."),
    "sections": [
        ("Pavers sit at the top of the city's non-exempt list, by name",
         f"<p>Oviedo's Building Services department publishes a list titled “Non-Structural residential work that would still require a planning and zoning permit through the Planning Department” to go alongside HB 803's new $7,500 exemption, and the very first line reads “Pavers/driveways/sidewalks on private property,” with a note that Engineering Department right-of-way permits are required separately for anything in the right of way "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). Call Building Services at 407-971-5755 before ordering pallets, since the exemption homeowners may have heard about from the new law simply doesn't apply to {svc('paver-driveways', 'a paver driveway')} inside the city.</p>"),
        ("The slab-and-paver package wants two site plans, not a stack of paperwork",
         f"<p>Once the permit applies, Oviedo's own paver permit guidelines, last revised January 2021, ask for a notarized building permit application, the contractor's license, general liability and workers' compensation insurance naming the city, and two site plans showing the distance from the paved area to the property line "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}). That packet covers a driveway the same way it covers a {svc('paver-patios', 'patio')} or a {svc('pool-deck-pavers', 'pool deck')}, so gathering the insurance documents and site plan ahead of ordering material keeps the application from stalling at the counter.</p>"),
    ],
    "scenario": ("A paver driveway sized to Seminole County's maximum width, worked out in square feet",
                 f"<p>Consider an 18 by 32 ft paver driveway, 576 sq ft, on an unincorporated Seminole County lot sized to the county's own 18-foot maximum width. At {price('paver-driveway')} per {per('paver-driveway')}, that job lands between roughly $5,760 and $17,280 depending on the paver and base depth. "
                 "Inside the Oviedo city limits, the same square footage still needs the planning and zoning permit the 2026 exemption list leaves in place, plus the slab-and-paver package's two site plans measuring distance to the property line, before the pallets show up on site.</p>"),
    "faqs": [
        faq("Does Florida's 2026 small-project exemption cover a paver driveway in Oviedo?",
            "No. The city's non-exempt list names pavers and driveways on private property directly, so the new $7,500 building-permit exemption that took effect July 1, 2026 doesn't reach that work inside the city limits."),
        faq("What documents does Oviedo's paver permit package require?",
            "A notarized building permit application, the contractor's license, general liability and workers' compensation insurance naming the city, and two site plans showing the distance from the paved area to the property line."),
        faq("Does a paver driveway need a different review than a concrete one in Oviedo?",
            "The underlying slab-and-paver permit package is the same either way. Where the two differ is on the exemption list itself, which calls out pavers, driveways and sidewalks together as work still requiring a planning and zoning permit."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Oviedo, FL – 4-In Slabs",
    "meta": "Concrete patio contractors in Oviedo, FL: why a non-structural 4-inch patio slab still needs a city permit, and flatwoods drainage, October 2026.",
    "h1": "Building a Concrete Patio in Oviedo",
    "lede": capsule(f"A concrete patio in Oviedo costs {price('concrete-patio')} per {per('concrete-patio')}, a Florida market range as of October 2026. "
                     "The city's own guidance names a standard 4-inch patio slab on grade as work that still needs a planning and zoning permit, and the flatwoods ground under a lot of Seminole County yards holds water close enough to the surface to shape how the slab is pitched."),
    "sections": [
        ("A non-structural 4-inch slab is still on Oviedo's permit list by name",
         f"<p>Oviedo's carve-out list for HB 803's 2026 exemption spells out “Non-structural 4\" concrete slabs on grade” as work that still needs a planning and zoning permit, sitting alongside pavers and driveways on the same list "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). A typical patio pour is exactly that: a 4-inch slab on grade, not a footed foundation, so the exemption homeowners may expect from the new law doesn't apply. Permit packages for a patio run through the same application the city uses for {svc('concrete-slabs', 'a slab')}, reviewed with the project's distance to the property line "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Flatwoods ground sets the slope before the forms go up",
         f"<p>Seminole County's own water-quality program names Myakka fine sand, Florida's official state soil since 1989, as typical of the flatwoods ground found across the county "
         f"({ext(WATER_ATLAS_URL, 'Seminole County Water Atlas, Learn More: Soils')}; {src('fl-dos-state-soil', 'Florida Dept. of State, State Soil')}). Ground like that can hold a water table close to the surface for part of a typical year, so a patio's pitch has to carry rainwater away from the house rather than let it pond against the slab, a detail worth checking on site rather than assuming a flat, dry backyard.</p>"),
    ],
    "scenario": ("A backyard patio addition on flatwoods ground, worked out in square feet",
                 f"<p>Say a home adds a 16 by 18 ft patio off the back of the house, 288 sq ft, replacing a bare patch of St. Augustine between the lanai and the yard. Pricing that at {price('concrete-patio')} per {per('concrete-patio')} works out to roughly $1,728 to $3,744 before a broom or stamped finish changes the number. "
                 "Because the slab counts as non-structural 4-inch flatwork, it still needs Oviedo's planning and zoning permit even under the 2026 exemption, and because the lot sits on the kind of flatwoods soil common across the county, the crew checks where the yard already sheds water before the forms go in, rather than after.</p>"),
    "faqs": [
        faq("Is a concrete patio exempt from a permit in Oviedo under the 2026 law?",
            "No. The city's own list names “Non-structural 4\" concrete slabs on grade” as work that still needs a planning and zoning permit, which covers a typical backyard patio pour."),
        faq("Does Oviedo's soil affect how a patio drains?",
            "It can. Flatwoods ground common across Seminole County, including Myakka fine sand, Florida's official state soil, can hold a water table close to the surface for part of the year, which shapes a patio's slope more than it changes the mix design."),
        faq("What permit application covers a patio slab in Oviedo?",
            "The same slab-and-paver permit package the city uses for a driveway or pool deck: a notarized application, the contractor's license, insurance naming the city, and two site plans showing distance to the property line."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Oviedo, FL – Econlockhatchee Lots",
    "meta": "Paver patio installers in Oviedo, FL on lots near the Econlockhatchee River and Lake Jesup, about 14 miles from Orlando, October 2026.",
    "h1": "Paver Patios and Walkways Around an Oviedo Home",
    "lede": capsule(f"A paver patio in Oviedo runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     f"The city sits about {str(__import__('_data').CITIES['oviedo']['miles'])} miles from the Orlando unit's base, bordered by Lake Jesup and the Econlockhatchee River, and a backyard that slopes toward either waterway needs its grading worked out before a paver base goes down."),
    "sections": [
        ("A lot near the Econlockhatchee or Lake Jesup drains differently than an inland yard",
         f"<p>The Econlockhatchee River, a 54.5-mile blackwater tributary of the St. Johns River, runs along Oviedo's eastern side, with the Little Econlockhatchee crossing the south, and the city itself grew up on the shore of Lake Jesup to the north "
         f"({ext(ECON_WIKI_URL, 'Wikipedia, Econlockhatchee River')}; {ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). Neither the city's paver guidelines nor Seminole County's driveway application publishes a setback from either waterway for a patio, but a yard that slopes toward the river corridor or the lake has less room to shed rainwater than a flat inland lot, which is the kind of thing a crew checks with a level before cutting into the base.</p>"),
        ("A patio or walkway still goes through the same two-site-plan package",
         f"<p>Oviedo's slab-and-paver permit guidelines ask for a notarized application, the contractor's license, liability and workers' comp insurance naming the city, and two site plans showing the paved area's distance to the property line "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}), the same packet whether the patio sits on a dry inland lot or one backing up to the Econ corridor. {cs('oviedo', 'concrete-patios', 'A poured concrete patio')} on the same lot goes through that identical review.</p>"),
    ],
    "scenario": ("A paver patio on a lot backing toward the Econlockhatchee corridor, worked out in square feet",
                 f"<p>Take a home on the east side of Oviedo, a 20 by 15 ft paver patio, 300 sq ft, added off the back of the house on a lot that slopes gently toward the Econlockhatchee floodplain. Figuring {price('paver-patio')} per {per('paver-patio')} puts that job around $3,000 to $5,100 depending on the paver and pattern chosen. "
                 "Before the base goes in, the crew checks where the existing yard already carries water toward the river corridor, since a patio poured flat against a lot that's already working with less fall than an inland yard can push water back toward the house instead of away from it.</p>"),
    "faqs": [
        faq("Is there a setback from the Econlockhatchee River for a paver patio in Oviedo?",
            "Not one published in the city's own paver guidelines or the county's driveway application. The practical question is grading: a yard sloping toward the river corridor has less natural fall to shed water than an inland lot, which gets checked on site before the base is cut."),
        faq("How far is Oviedo from the Orlando unit's base?",
            f"About {str(__import__('_data').CITIES['oviedo']['miles'])} miles. Oviedo sits in Seminole County, bordered by Lake Jesup to the north and the Econlockhatchee River along its eastern side."),
        faq("Does a paver patio need the same permit package as a driveway in Oviedo?",
            "Yes. The city's slab-and-paver guidelines use the same notarized application, insurance requirements and two-site-plan package for a patio, a driveway or a pool deck."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Oviedo, FL – 1997 Homes",
    "meta": "Concrete pool deck builders in Oviedo, FL: original 1997-era decks versus newer Oviedo on the Park construction, October 2026.",
    "h1": "Concrete Pool Decks for Oviedo Homes",
    "lede": capsule(f"Pricing a concrete pool deck in Oviedo runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, a Florida market range as of October 2026. "
                     "With the city's typical home dating to 1997, a lot of original pool decks are now approaching three decades old, while newer construction around Oviedo on the Park is pouring first decks rather than resurfacing anything."),
    "sections": [
        ("A deck from the city's median build year is old enough to need a closer look",
         f"<p>Oviedo's median year of home construction is 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), old enough that a share of the city's original pool decks are showing the hairline cracking and worn cool-deck coating that call for a resurfacing decision rather than another spot patch. The same slab-and-paver permit package, requiring two site plans showing distance to the property line, covers a deck replacement or overlay the way it covers new construction "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Newer pools cluster around Oviedo on the Park",
         f"<p>The city's Oviedo on the Park development has added newer housing around Center Lake Park, described on the city's own site as “the crown jewel of the city's new Oviedo on the Park development area” "
         f"({src('oviedo-otp', 'City of Oviedo, Oviedo on the Park')}). A pool going in on a lot built in the last few years there is a first installation rather than a resurfacing job, and the deck's finished elevation gets set against current grading rather than whatever settling an older, 1997-era yard has already gone through.</p>"),
    ],
    "scenario": ("A new pool deck on recently developed ground, worked out in square feet",
                 f"<p>Picture a newer home near Oviedo on the Park pouring a 650 sq ft deck around a freshly set pool shell. Figuring {price('concrete-pool-deck')} per {per('concrete-pool-deck')} puts that job between roughly $3,250 for a plain broom finish and $9,750 for a cool-touch decorative surface. "
                 "A deck going in around an original 1997-era pool instead typically starts with a resurfacing conversation first, since the existing slab's cracking pattern decides whether an overlay holds up or a tear-out and repour makes more sense before the new finish goes on.</p>"),
    "faqs": [
        faq("Should I expect to resurface rather than replace an original Oviedo pool deck?",
            "Often, yes. With the city's median home dating to 1997, a lot of original decks are old enough for hairline cracking and a worn coating without being structurally compromised, which usually points toward resurfacing rather than a full tear-out."),
        faq("Is a pool deck permit different for a newer Oviedo on the Park home?",
            "No, the slab-and-paver permit package is the same whether the deck is a first installation or a resurfacing job, built around two site plans showing distance to the property line."),
        faq("What finish holds up best on an older Oviedo pool deck?",
            "A slip-resistant, cool-touch broom or textured finish wears better than a smooth trowel finish once the original coating is past its useful life, which is one reason resurfacing jobs on older decks often switch finishes rather than matching the original."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Oviedo, FL – Overlays",
    "meta": "Pool deck paver overlays in Oviedo, FL: resurfacing 1990s decks and the city's two-site-plan permit package, October 2026.",
    "h1": "Pool Deck Pavers in Oviedo: New Decks and Overlays",
    "lede": capsule(f"Pool deck pavers in Oviedo cost {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, a Florida market range as of October 2026, whether the pavers go down fresh or get set over an existing slab. "
                     "With the city's typical home dating to 1997, a share of the original cool-deck surfaces around Oviedo's older neighborhoods are old enough for a paver overlay instead of another patch."),
    "sections": [
        ("An original cool-deck surface from the late 1990s is a common overlay candidate",
         f"<p>Oviedo's median year of home construction is 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), which puts a meaningful share of the city's original pool decks in the range where a worn coating and hairline cracking make a paver overlay worth pricing against a full tear-out. The city's own slab-and-paver guidelines, last revised January 2021, apply the same documentation, a notarized application, insurance naming the city, and two site plans, whether the job is an overlay or a first installation "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Lots near Lake Jesup add a grading check before the pavers go down",
         f"<p>Oviedo grew up along Lake Jesup, and some of its older lakefront streets sit close enough to the water that the yard's slope matters more than it would a few blocks inland "
         f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). On a lot like that, the overlay's finished height has to account for whatever grading the original deck already set, since pavers laid directly over an existing slab inherit that slab's drainage pattern rather than starting from a clean grade.</p>"),
    ],
    "scenario": ("A paver overlay on a 1990s-era pool deck, worked out in square feet",
                 f"<p>Say a home built around the city's 1997 median resurfaces a 500 sq ft original cool-deck patio with pavers set directly over the existing slab. Figuring {price('pool-deck-pavers')} per {per('pool-deck-pavers')} puts that overlay somewhere around $6,000 on the plain end and up near $15,000 for travertine. "
                 "A full tear-out instead of an overlay adds demolition cost to the job but avoids building the new surface on top of whatever cracking or settling the original late-1990s slab has already developed.</p>"),
    "faqs": [
        faq("Can pavers go over an existing Oviedo pool deck without a full tear-out?",
            "Usually, as an overlay, reviewed under the same slab-and-paver permit package the city uses for new construction. How much the existing slab has already cracked or settled decides whether an overlay is the right call."),
        faq("Does a lakefront lot near Lake Jesup need special grading for pool deck pavers?",
            "No separate permit, but the slope matters more. An overlay set over an existing slab inherits that slab's drainage pattern, so the finished height gets checked against the yard's existing grade before pavers go down."),
        faq("Are older Oviedo pool decks more likely to need an overlay than new ones?",
            "Generally, yes. With the city's median home dating to 1997, a meaningful share of original pool decks are old enough that a worn coating and hairline cracking make an overlay worth pricing against a tear-out."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Oviedo, FL – Downtown Charm",
    "meta": "Stamped concrete contractors in Oviedo, FL: why a decorative slab still needs the city's planning permit, near the historic downtown, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Oviedo",
    "lede": capsule(f"A stamped-concrete project in Oviedo costs {price('stamped-concrete')} per {per('stamped-concrete')}, a Florida market range as of October 2026 that moves with the pattern and the number of colors chosen. "
                     "The finish doesn't change which permit applies: Oviedo's 2026 exemption list still keeps a decorative driveway or patio slab on its planning-permit roster the same as a plain gray pour."),
    "sections": [
        ("A decorative finish doesn't move a slab off the city's permit list",
         f"<p>Oviedo's carve-out list for HB 803's 2026 exemption names “Pavers/driveways/sidewalks on private property” and “Non-structural 4\" concrete slabs on grade” without carving out an exception for color or pattern "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). A slate-pattern stamped driveway or an integral-color front walk still goes through the city's planning and zoning review, and through the same slab-and-paver documentation, a notarized application, insurance naming the city and two site plans, that a plain broom-finish pour would need "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("Oviedo's historic downtown sets a different visual bar than its newer subdivisions",
         f"<p>Oviedo's historic downtown, once known for the chickens that roamed its streets, still carries older houses and storefronts along the Florida Trail and Cross Seminole Trail crossing "
         f"({ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}), a different visual context than the newer construction spreading out from Oviedo on the Park. A {svc('stamped-concrete', 'stamped walkway')} or driveway near the older core is more often matched to a historic-looking brick or slate pattern, while newer subdivisions further out see more uniform, contemporary colors.</p>"),
    ],
    "scenario": ("A stamped entry walk and driveway apron, worked out in square feet",
                 f"<p>Imagine a home near Oviedo's older core replacing a 240 sq ft driveway apron and front walk with a slate-pattern stamped finish and an integral color. Pricing it at {price('stamped-concrete')} per {per('stamped-concrete')} puts the job between roughly $1,920 and $4,560, with the number of colors and the release agent used swinging it toward either end. "
                 "Because the work still touches private-property flatwork, the city's planning and zoning permit applies the same way it would to a plain gray pour, and any part of the apron reaching the street still needs the separate right-of-way review.</p>"),
    "faqs": [
        faq("Does stamped concrete need a different permit than plain concrete in Oviedo?",
            "No. The city's 2026 exemption carve-out list covers driveway and patio slabs generally, without an exception for a decorative finish, so a stamped pattern goes through the same planning and zoning review a plain pour would."),
        faq("Do homes near Oviedo's historic downtown favor a particular stamped pattern?",
            "There's no published rule requiring it, but a brick or slate-style pattern tends to read better against the older houses and storefronts downtown than it would in a newer subdivision, where more uniform colors are common."),
        faq("Does a stamped driveway apron still need the city's right-of-way permit?",
            "Yes, if any part of it crosses into the right-of-way. That review runs separately from the planning and zoning permit covering the private portion of the slab."),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Sidewalks & Walkways in Oviedo, FL",
    "meta": "Concrete walkway contractors in Oviedo, FL: the city's permit list for sidewalks on private property versus the right-of-way review, October 2026.",
    "h1": "Concrete Sidewalks and Walkways in Oviedo",
    "lede": capsule(f"A concrete walkway in Oviedo runs {price('concrete-walkway')} per {per('concrete-walkway')} as of October 2026. "
                     "The city groups sidewalks on private property with driveways and pavers on its 2026 exemption carve-out list, while a walkway section crossing into the right-of-way needs its own separate review."),
    "sections": [
        ("Private-property walkways share a line item with driveways and pavers",
         f"<p>Oviedo's non-exempt list reads “Pavers/driveways/sidewalks on private property” as a single line, so a front walk connecting the driveway to the entry doesn't clear HB 803's 2026 exemption any more than a driveway does "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). The same note on that list flags that Engineering Department right-of-way permits apply separately to “driveway/sidewalk work in the right of way,” a distinction worth checking before assuming a front-walk project is a single application.</p>"),
        ("The right-of-way section has its own $104 fee and paperwork",
         f"<p>Wherever a walkway crosses from the property line into the public right-of-way, Oviedo's Right-of-Way Type I application applies: $79.00 plus a $25.00 technology fee, with a sealed boundary survey, a maintenance-of-traffic plan and a certificate of insurance required alongside it "
         f"({src('oviedo-row-type1', 'City of Oviedo, Right-of-Way Type I Application')}). A path that stays entirely on private ground, connecting a side door to a patio rather than to the street, skips that particular review even though it still needs the planning permit covering private flatwork.</p>"),
    ],
    "scenario": ("A front walkway crossing the right-of-way, worked out in square feet",
                 f"<p>Consider a 4 by 35 ft front walkway, 140 sq ft, replacing a cracked original path from the driveway to the front door. At {price('concrete-walkway')} per {per('concrete-walkway')}, that lands between roughly $980 and $2,380. "
                 "Where that walk crosses the sidewalk strip near the street, the $104 Right-of-Way Type I fee and its paperwork apply on top of the planning permit covering the rest of the path; a side-yard walkway that never leaves private ground only needs the latter.</p>"),
    "faqs": [
        faq("Does a front walkway in Oviedo need a permit separate from the driveway?",
            "The city lists sidewalks, driveways and pavers on private property together on its 2026 exemption carve-out, so the planning review is similar either way. Where the walk crosses into the right-of-way, it adds a separate Right-of-Way Type I application."),
        faq("What does Oviedo's right-of-way permit cost for a sidewalk section?",
            "$104.00 total, a $79.00 application fee plus a $25.00 technology fee, along with a sealed boundary survey, a maintenance-of-traffic plan and proof of insurance."),
        faq("Does a side-yard walkway that stays on private property need the right-of-way permit?",
            "No, only the planning and zoning permit that covers private-property flatwork generally. The right-of-way review applies specifically to the section that crosses from the property line into the public strip."),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Oviedo, FL – Shed Pads",
    "meta": "Concrete slab contractors in Oviedo, FL: the city's 4-inch slab permit line and Seminole County's shed-size exemption, October 2026.",
    "h1": "Concrete Slabs for Sheds, Pads and Parking in Oviedo",
    "lede": capsule(f"A concrete slab in Oviedo runs {price('concrete-slab')} per {per('concrete-slab')} as of October 2026. "
                     "Inside the city, a shed, AC or parking pad falls under the “non-structural 4-inch slab” line on the 2026 exemption carve-out; in unincorporated Seminole County, a shed of 200 sq ft or less is separately exempt, though the slab under it isn't automatically covered."),
    "sections": [
        ("A 4-inch pad is on the city's permit list by name, regardless of use",
         f"<p>Oviedo's carve-out for HB 803's 2026 exemption names “Non-structural 4\" concrete slabs on grade” directly, a category that covers a shed pad, an AC pad or a small parking slab the same way it covers a patio "
         f"({src('oviedo-building-services', 'City of Oviedo, Building Services')}). The slab-and-paver permit package behind that review wants a notarized application, the contractor's license, insurance naming the city, and two site plans showing distance to the property line "
         f"({src('oviedo-slab-paver', 'City of Oviedo, Slab/Paver Permit Guidelines')}).</p>"),
        ("The county's shed exemption and the slab under it are two different questions",
         f"<p>In unincorporated Seminole County, the 2026 list of HB 803 exemptions names sheds of 200 sq ft or less among the non-structural work that no longer needs a building permit, alongside fences, pergolas and floating docks, but the same list doesn't mention driveways, pavers, slabs or retaining walls "
         f"({src('seminole-hb803', 'Seminole County, New State Legislation Affecting Permits')}). That gap means a small shed itself may be exempt while the concrete pad underneath it is worth a call to the county's Building Division at 407-665-7050 before assuming the same exemption covers both.</p>"),
    ],
    "scenario": ("A shed pad on each side of the city line, worked out in square feet",
                 f"<p>Say a 10 by 12 ft shed pad, 120 sq ft, goes in near the edge of the Oviedo city limits. At {price('concrete-slab')} per {per('concrete-slab')}, that lands between roughly $480 and $1,200 depending on the mix and reinforcement. "
                 "Inside the city, that pad is filed as a non-structural 4-inch slab through the planning and zoning permit. On an otherwise identical lot in unincorporated Seminole County, a shed under 200 sq ft may clear the state's exemption for the structure itself, though confirming whether the slab underneath needs its own review is worth a call to the Building Division first.</p>"),
    "faqs": [
        faq("Does a shed slab need a permit in Oviedo under the 2026 exemption?",
            "Yes. The city's carve-out list keeps “Non-structural 4\" concrete slabs on grade” on its planning-permit roster, which covers a shed pad the same way it covers a patio or AC pad."),
        faq("Is a small shed exempt from a permit in unincorporated Seminole County?",
            "Sheds of 200 sq ft or less are on the county's 2026 list of exempt non-structural work. The concrete pad underneath isn't named on that same list, so confirming with the Building Division before pouring is worth the call."),
        faq("What documents does an Oviedo slab permit require?",
            "A notarized building permit application, the contractor's license, general liability and workers' compensation insurance naming the city, and two site plans showing the slab's distance to the property line."),
    ],
    "sources": SRC,
}

# 10. concrete-repair ----------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair & Resurfacing in Oviedo, FL",
    "meta": "Concrete repair and resurfacing in Oviedo, FL: cracking in 1997-era driveways and why Seminole isn't on the state's top sinkhole-claims list, October 2026.",
    "h1": "Concrete Repair and Resurfacing in Oviedo",
    "lede": capsule(f"A concrete repair or resurfacing job in Oviedo costs {price('concrete-repair')} per {per('concrete-repair')}, a Florida market range as of October 2026. "
                     "Oviedo's population grew from 40,023 at the 2020 census to 41,317 by mid-2025, and a lot of the city's original driveways, dating to the 1997 median build year, are now old enough that cracking and worn joints are routine."),
    "sections": [
        ("A driveway from Oviedo's median build year has had nearly three decades of Florida weather",
         f"<p>Oviedo's typical home dates to 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), which puts a meaningful share of the city's original driveways and walkways at the point where hairline cracking, a widened control joint or a chalky surface is ordinary wear rather than a warning sign. Whether a resurfacing job needs the full planning permit depends on whether it stays inside the existing footprint; call Building Services at 407-971-5755 to confirm before assuming a smaller job is exempt.</p>"),
        ("Seminole isn't on the state's list of counties with the heaviest sinkhole claims",
         f"<p>A 2010 Florida Senate interim report names eleven counties that together accounted for more than 88 percent of sinkhole insurance claims filed statewide between 2006 and 2009: Hernando, Pasco, Hillsborough, Pinellas, Marion, Polk, Orange, Alachua, Citrus, Miami-Dade and Broward "
         f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). Seminole isn't one of them, though the same geological report notes the county shares a similar shallow-limestone setting with parts of Orange and other nearby counties. A dip or crack in an Oviedo driveway is far more likely to trace back to a wet flatwoods subgrade or loose fill under the original pour than to the abrupt collapse Florida's catastrophic ground-cover-collapse coverage is written around.</p>"),
    ],
    "scenario": ("Resurfacing an original Oviedo driveway, worked out in square feet",
                 f"<p>Take a 420 sq ft two-car driveway, original to a home built around the city's 1997 median, showing a network of hairline cracks along its control joints. Resurfacing it at {price('concrete-repair')} per {per('concrete-repair')} works out to somewhere between $1,260 and $4,200, cheaper toward the broom-finish end and pricier with a decorative overlay added at the same time. "
                 "A full tear-out and repour instead would shift the job into driveway pricing territory and bring back both the planning permit and, if the apron is involved, the city's separate right-of-way review.</p>"),
    "faqs": [
        faq("Should I worry about cracking in an original 1997 Oviedo driveway?",
            "Not automatically. With the city's median home dating to 1997, hairline cracking and worn joints on a driveway that age are typically routine wear. A sudden, deep depression rather than a gradual crack is the kind of thing worth a closer look."),
        faq("Is Seminole County at high risk for sinkholes the way some nearby counties are?",
            "No, it isn't on the Florida Senate's 2010 list of eleven counties with the heaviest sinkhole insurance claims from 2006 to 2009, unlike neighboring Orange County. The report does place Seminole in a similar underlying geological setting, though claims activity there runs far lower."),
        faq("Is a permit needed to resurface an existing driveway in Oviedo?",
            "Work that stays inside the existing footprint is typically a lighter submission than a full replacement, but confirming the scope with Building Services before assuming a resurfacing job is exempt is worth the call."),
    ],
    "sources": SRC,
}

# 11. paver-sealing -------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing & Restoration in Oviedo, FL",
    "meta": "Paver sealing and restoration in Oviedo, FL: why SJRWMD's watering schedule doesn't govern a pre-seal pressure wash, October 2026.",
    "h1": "Paver Sealing and Restoration in Oviedo",
    "lede": capsule(f"Cleaning, re-sanding and sealing pavers in Oviedo costs {price('paver-sealing')} per {per('paver-sealing')}, a Florida market range as of October 2026. "
                     "St. Johns River Water Management District's twice-a-week schedule governs lawn irrigation, not a hose-fed pressure washer, so cleaning pavers ahead of a seal doesn't have to wait for a particular address day."),
    "sections": [
        ("SJRWMD's watering calendar doesn't reach a pre-seal pressure wash",
         f"<p>During Daylight Saving Time, St. Johns River Water Management District limits irrigation here to odd-numbered and no-number addresses on Wednesday and Saturday, even-numbered addresses on Thursday and Sunday, with nothing allowed between 10 a.m. and 4 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}). That calendar covers sprinkler zones watering grass, not a hose running through a pressure washer to strip algae and dirt off a paver surface, so the clean-and-re-sand step ahead of sealing books around the crew's schedule and the forecast rather than a numbered address day.</p>"),
        ("A deck from the city's median build year is a common first-seal candidate",
         f"<p>With Oviedo's typical home dating to 1997 "
         f"({src('acs-oviedo', 'Census Reporter, Oviedo FL')}), a lot of the original paver walkways and patios around the city are old enough that the first sealing application, or the first in years, is overdue rather than routine maintenance. Re-sanding with polymeric sand before sealing holds joints in place better on a surface that's gone that long without attention than a quick rinse and reseal would.</p>"),
    ],
    "scenario": ("Resealing an Oviedo paver driveway, worked out in square feet",
                 f"<p>Picture a 480 sq ft paver driveway getting a full clean, a polymeric re-sand and a seal for the first time since it went in. Pricing that at {price('paver-sealing')} per {per('paver-sealing')} puts the job around $720 to $1,560, with releveling any sunken pavers pushing it toward the higher figure. "
                 "The pressure wash ahead of sealing can run on any day the crew and the weather line up, since it isn't subject to the district's irrigation schedule the way a sprinkler zone watering the surrounding lawn would be.</p>"),
    "faqs": [
        faq("Can pavers be pressure-washed on a day SJRWMD doesn't allow irrigation in Oviedo?",
            "Yes. The watering schedule governs sprinklers irrigating grass, not a hose feeding a pressure washer, so the pre-seal rinse can happen on any day a crew and the weather line up."),
        faq("Does a permit cover cleaning and sealing pavers that are already down in Oviedo?",
            "No. The city's slab-and-paver permit guidelines are built around new construction or replacing a paved area, not maintenance on a surface that's already in place."),
        faq("Why do so many Oviedo paver surfaces need their first sealing now?",
            "With the city's typical home dating to 1997, a share of the original paver walkways and patios are old enough that a first or long-overdue sealing, rather than routine upkeep, is what the surface actually needs."),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Oviedo, FL – Engineering",
    "meta": "Retaining wall contractors in Oviedo, FL: the city's signed-and-sealed engineering requirement near the Econlockhatchee floodplain, October 2026.",
    "h1": "Retaining Walls for Oviedo Yards",
    "lede": capsule(f"Building a retaining wall in Oviedo costs {price('retaining-wall')} per {per('retaining-wall')}, a Florida market range as of October 2026. "
                     "The city's own wall permit guideline requires signed and sealed engineered drawings for any freestanding or retaining wall, with no height written in below which that requirement drops away."),
    "sections": [
        ("Oviedo requires sealed engineering on a wall regardless of height",
         f"<p>Oviedo's permit guidelines for freestanding and retaining walls call for “signed and sealed engineered drawings” including wind design data, and the document doesn't name a height below which a homeowner could skip that step "
         f"({src('oviedo-permit-guidelines', 'City of Oviedo, Permit Guidelines')}). That's a stricter default than some nearby jurisdictions that simply don't publish a threshold at all; in Oviedo, the engineering requirement is the starting point, confirmed with Building Services at 407-971-5755 before a wall's design is finalized.</p>"),
        ("A yard sloping toward the Econlockhatchee or Lake Jesup usually has more fill to hold",
         f"<p>Oviedo sits along the Econlockhatchee River, a 54.5-mile blackwater tributary of the St. Johns River, with Lake Jesup bordering the city to the north "
         f"({ext(ECON_WIKI_URL, 'Wikipedia, Econlockhatchee River')}; {ext(OVIEDO_WIKI_URL, 'Wikipedia, Oviedo, Florida')}). A yard that drops toward either waterway typically needs more retained fill than a flat inland lot, since the grade falls further over the same horizontal run, which is part of what the sealed engineering on the wall's drawings has to account for.</p>"),
    ],
    "scenario": ("A sloped yard near the river corridor, worked out in square feet",
                 f"<p>Say a yard on Oviedo's east side needs a 30 linear ft segmental block wall, 3 ft tall, 90 sq ft of wall face, to hold a grade that drops toward the Econlockhatchee floodplain. Pricing it at {price('retaining-wall')} per {per('retaining-wall')} puts that job between roughly $1,350 and $3,600 before drainage behind the wall is added in. "
                 "Because the city requires signed and sealed engineered drawings on any retaining wall regardless of height, that design step comes before construction starts rather than after, with wind design data included in the same submission.</p>"),
    "faqs": [
        faq("Does every retaining wall in Oviedo need an engineer's drawings?",
            "Yes. The city's permit guideline requires signed and sealed engineered drawings with wind design data for a freestanding or retaining wall, and it doesn't set a height below which that requirement is waived."),
        faq("Does a wall near the Econlockhatchee River need extra drainage?",
            "Often, yes. A wall holding back a slope toward the river corridor or Lake Jesup typically carries more retained fill and water pressure than one on a flat inland lot, which the sealed engineering has to account for."),
        faq("Who reviews a retaining wall permit in Oviedo?",
            "Building Services, reachable at 407-971-5755, using the city's own permit guidelines for freestanding and retaining walls rather than the slab-and-paver package used for driveways and patios."),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Oviedo, FL – Water Rules",
    "meta": "Artificial turf installers in Oviedo, FL: the statewide water-body setback near Lake Jesup and SJRWMD's watering schedule, October 2026.",
    "h1": "Artificial Turf for Oviedo Yards",
    "lede": capsule(f"Installing artificial turf in Oviedo costs {price('artificial-turf')} per {per('artificial-turf')}, a Florida market range as of October 2026. "
                     "On lots near Lake Jesup or the Econlockhatchee River, the state's turf rule keeps synthetic grass at least 10 feet from the water unless it backs onto a seawall, and because turf isn't irrigated, it sits outside St. Johns River Water Management District's watering schedule entirely."),
    "sections": [
        ("A 10-foot water-body setback applies near the lake and the river",
         f"<p>Under the state's turf rule, effective May 19, 2026, synthetic grass has to stay 10 feet clear of a natural or man-made water body unless the lot backs onto a seawall or similar barrier, with a washed base, natural infill and no buried irrigation line underneath rounding out the installation standard "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A separate 2025 law caps how far a city or county can go in writing its own turf restrictions on top of that state standard "
         f"({src('fs125572', 'Florida Statutes §125.572')}). On a lot backing onto Lake Jesup or the Econlockhatchee River, that 10-foot line is the first measurement worth checking before laying out where the turf starts.</p>"),
        ("Turf sidesteps SJRWMD's twice-a-week schedule entirely",
         f"<p>During Daylight Saving Time, the district limits lawn irrigation here to odd-numbered addresses on Wednesday and Saturday and even-numbered addresses on Thursday and Sunday, nothing between 10 a.m. and 4 p.m. "
         f"({src('sjrwmd-watering', 'SJRWMD, Watering Restrictions')}), a schedule that governs sprinkler zones watering grass, not a turf system that doesn't need watering once the base is compacted. That matters on a lot where St. Augustine has struggled against the flatwoods water table or a shaded tree canopy, since turf swaps out the watering question rather than working around it.</p>"),
    ],
    "scenario": ("Backyard turf near the Econlockhatchee floodplain, worked out in square feet",
                 f"<p>Imagine a lot on Oviedo's east side swapping out 500 sq ft of thinning St. Augustine for artificial turf, with the layout kept 10 feet clear of the floodplain edge. Figuring {price('artificial-turf')} per {per('artificial-turf')} puts that job between roughly $5,000 for a basic pile and $12,500 for a thicker, more realistic build. "
                 "Staying outside that 10-foot line means the project doesn't need to lean on the seawall exception at all, though a layout planned any closer to the water would have to confirm that condition first.</p>"),
    "faqs": [
        faq("How close to Lake Jesup can artificial turf be installed in Oviedo?",
            "No closer than 10 feet under the state's turf rule, unless the lot backs onto a seawall or similar barrier. The rule also bars in-ground irrigation from running under the turf and requires natural infill and a washed base."),
        faq("Does artificial turf follow SJRWMD's watering schedule in Oviedo?",
            "No. That schedule governs irrigated grass, not turf, since an installed turf system doesn't need watering once the base is compacted, which makes it easier to manage than sod on the district's twice-a-week calendar."),
        faq("Can an Oviedo HOA ban artificial turf entirely?",
            "State law caps how far a local government can go in restricting residential turf, and the DEP rule sets the baseline installation standard. A specific HOA's own design guidelines may still layer on additional rules, which is worth checking before installation regardless of what the city otherwise allows."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
