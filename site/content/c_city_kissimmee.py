# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, a, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "kissimmee"

TOHO_URL = "https://www.tohowater.com/residents-business/watering-days-and-times"
STRPD_URL = "https://www.osceola.org/My-Property/Zoning-and-Land-Use/Zoning-Designation/STRPD"

SRC = [
    "census-pep-v2025", "acs-kissimmee", "kissimmee-parks",
    "kissimmee-driveway-sidewalk", "kissimmee-row-permit", "kissimmee-permit-types",
    "osceola-row-info", "osceola-parking-ord", "osceola-permit-info", "osceola-homeowners",
    "nrcs-smyrna-osd", "nrcs-myakka-osd", "celebration-arc", "dep-rule", "fs125572",
    ("Toho Water Authority, Watering Days and Times", TOHO_URL),
    ("Osceola County, STRPD District", STRPD_URL),
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Kissimmee's Engineering Division reviews driveway and sidewalk work in EnerGov",
        "<p>Inside the city limits, a new driveway, a widened apron or a sidewalk repair goes through the Engineering Division at 101 Church St., 3rd Floor, filed in the city's EnerGov portal under “Driveway / Sidewalk Construction.” "
        f"Staff tell applicants which documents a given lot needs, and routing takes at least two business days; call 407-518-2278 or email engineering@kissimmee.gov before ordering concrete "
        f"({src('kissimmee-driveway-sidewalk', 'City of Kissimmee, Apply for Driveway/Sidewalk Construction')}). The city notes that some of the right-of-way along a given street actually belongs to FDOT or Osceola County rather than the city itself, which changes who signs off. "
        f"Any separate work “in a street, under a sidewalk, or in the grassy area next to a street” needs its own right-of-way permit, routed through Aaron Mendez at 407-518-2536 or engineeringpermitting@kissimmee.gov, with fees starting at a $25 minimum "
        f"({src('kissimmee-row-permit', 'City of Kissimmee, Apply for Right-of-Way Permits')}). {cs('kissimmee', 'concrete-driveways', 'A driveway replacement')} and {svc('concrete-walkways', 'a walkway repair')} both start at this office.</p>"),
    sec("Step outside the city line and Osceola County caps a driveway at 24 feet",
        f"<p>A lot of ground that carries a Kissimmee mailing address actually sits in unincorporated Osceola County, and out there, Code §22-50.6 pegs the maximum width of an ordinary residential driveway at 24 feet, wider than that takes a conditional use approval from the county first "
        f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance Ch. 22 Art. II')}). The county's Building Office handles that review from 1 Courthouse Square, Suite 1400, a few blocks from the city's own Engineering counter; call 407-742-0200 "
        f"({src('osceola-row-info', 'Osceola County, Right-of-Way Permit Information')}). The city has not published a comparable stand-alone width cap for driveways inside its own limits, so {cs('kissimmee', 'paver-driveways', 'a paver driveway')} wider than the county's 24-foot figure is worth confirming with whichever office actually reviews the lot.</p>"),
    sec("Lake Tohopekaliga shapes what goes in near the water",
        f"<p>The city's own description of Big Toho Marina calls Lake Tohopekaliga “one of the nation's best bass fishing lakes,” and Kissimmee's lakefront, canals and golf-course edges put a fair number of backyards within sight of open water "
        f"({src('kissimmee-parks', 'City of Kissimmee, Parks')}). Statewide, artificial turf laid within 10 feet of a water body has to back onto a seawall or stay out of that buffer altogether, along with a washed base and no in-ground irrigation run underneath it "
        f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). {svc('retaining-walls', 'A retaining or seat wall')} is also a common way to manage a yard that slopes down toward a shoreline or a drainage canal rather than a flat inland lot.</p>"),
    sec("A share of Kissimmee's yards work as short-term rentals",
        f"<p>Osceola County only allows a short-term rental in a lot zoned for it, either a Short Term Rental Planned Development or an area shown on the county's short-term rental overlay map, and a property “in a Subdivision or a Planned Development” can carry additional architectural rules on top of that zoning "
        f"({ext(STRPD_URL, 'Osceola County, STRPD District')}). That zoning check runs separately from the state vacation-rental license and the county business tax receipt a rental operator also needs. Along the US-192 corridor and the resort-style subdivisions near the attractions, that overlay, not the driveway or pool-deck spec itself, is usually the first thing worth confirming before exterior work gets scoped.</p>"),
    sec("Toho Water Authority, not the regional district, sets Kissimmee's watering days",
        f"<p>Kissimmee's own utility, Toho Water Authority, runs a year-round twice-a-week schedule: odd-numbered and no-number addresses water Wednesday and Saturday, even-numbered addresses water Thursday and Sunday, and nothing runs between 10 a.m. and 4 p.m. on any address "
        f"({ext(TOHO_URL, 'Toho Water Authority, Watering Days and Times')}). New sod gets a graduated exception, daily for the first ten days, tapering down to the standard two-day schedule by day 21. {svc('artificial-turf', 'Artificial turf')} doesn't run on that schedule at all, since nothing underneath it needs watering once the base is set.</p>"),
    sec("Flatwoods soil that got its official name inside Osceola County",
        f"<p>The Smyrna series, one of the flatwoods soils that cover a lot of ground under Central Florida driveways and patios, carries this line in its federal soil survey record: “SERIES ESTABLISHED: Osceola County, Florida; 1976” "
        f"({src('nrcs-smyrna-osd', 'NRCS, Official Series Description, Smyrna')}). Smyrna sits alongside Myakka, Florida's official state soil, across much of the flatwoods ground in the county, and both can hold a water table within 18 inches of the surface for part of a typical year "
        f"({src('nrcs-myakka-osd', 'NRCS, Official Series Description, Myakka')}). That's the kind of ground a crew checks with a shovel and a compaction test before pricing {svc('concrete-slabs', 'a slab')} or {svc('concrete-pool-decks', 'a pool deck')}, not after the forms are up.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Do you build driveways and pool decks for vacation rental homes in Kissimmee and ChampionsGate?",
        f"Yes. A lot of the driveway, patio and pool-deck work priced around Kissimmee sits on lots zoned for short-term rental use, inside a Short Term Rental Planned Development or the county's overlay map "
        f"({ext(STRPD_URL, 'Osceola County, STRPD District')}). The concrete or paver spec itself doesn't change for a rental, though property managers often ask for a lower-maintenance finish that holds up to weekly turnover traffic rather than occasional weekend use."),
    faq("Does the City of Kissimmee or Osceola County issue my driveway permit?",
        "It depends on whether the lot sits inside the city limits or in unincorporated Osceola County, which share the same ZIP codes and the same “Kissimmee” address in a lot of neighborhoods. The city's Engineering Division reviews work inside the limits through EnerGov; the county's Building Office, a few blocks away at 1 Courthouse Square, reviews everything outside them."),
    faq("What are Kissimmee's watering days for new sod or a landscape reset?",
        "Toho Water Authority runs a twice-a-week schedule by address, Wednesday and Saturday for odd and no-number addresses, Thursday and Sunday for even ones, with nothing between 10 a.m. and 4 p.m. New sod gets extra watering for the first 30 days on a tapering schedule before it drops to the standard days."),
    faq("Is a retaining wall near Lake Tohopekaliga regulated differently than one inland?",
        "Neither the city's permit-types page nor the county's homeowner guidance publishes a stand-alone height that triggers engineering review for a wall, so a call to whichever office covers the lot is worth making before finalizing a design. Grading toward the lake or a canal is the bigger variable on a waterfront lot, since the wall usually has more fill to hold back than one on a flat inland yard."),
    faq("How do I find the best concrete contractor in Kissimmee?",
        f"Check the contractor on the state's license-verification tool, confirm whether the city's Engineering Division or Osceola County's Building Office actually reviews your lot before a quote assumes one or the other, and ask how the bid handles compaction on flatwoods soil. "
        f"{post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor')} covers the rest."),
    faq("Does Celebration require approval before I reseal or repave a driveway?",
        f"Celebration, the planned community just outside Kissimmee in unincorporated Osceola County, runs its exterior changes through an Architectural Review Committee that meets on the third Monday of each month, with applications due ahead of a published monthly deadline "
        f"({src('celebration-arc', 'Celebration, Architectural Review Committee')}). That review sits alongside, not instead of, whatever county permit the same job needs."),
]

HUB = page("/kissimmee-fl/", "city", "Concrete, Pavers & Turf Contractor in Kissimmee, FL",
           "Concrete, pavers and turf in Kissimmee, FL: city vs. Osceola County permits, Lake Tohopekaliga, short-term rental zoning and Toho watering days, October 2026.",
           "Concrete, pavers and artificial turf in Kissimmee, Florida",
           capsule("Opera pours concrete and lays pavers and artificial turf for homes in Kissimmee, a city of about 85,591 residents in Osceola County where the typical house dates to 1992. "
                   f"A new concrete driveway here costs {price('concrete-driveway')} per {per('concrete-driveway')}, a Florida market range as of October 2026, and whether the permit comes from the city's Engineering Division or Osceola County's Building Office depends on which side of the city line the lot actually sits."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Orlando & Central Florida", "/central-florida/")], crumb="Kissimmee",
           related=[("/central-florida/", "The Orlando-unit coverage page"),
                    ("/blog/osceola-county-kissimmee-st-cloud-permits/", "Kissimmee and Osceola County permits"),
                    ("/celebration-fl/", "Concrete, pavers and turf in Celebration"),
                    ("/st-cloud-fl/", "Concrete, pavers and turf in St. Cloud"),
                    ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
                    ("/permits/", "Permits and HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Kissimmee, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Kissimmee, FL – Permits",
    "meta": "Concrete driveway installers in Kissimmee, FL: the city's EnerGov process versus Osceola County's 24-foot width cap, as of October 2026.",
    "h1": "Pouring or Replacing a Concrete Driveway in Kissimmee",
    "lede": capsule(f"A new or replacement concrete driveway in Kissimmee runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "Which office reviews the job, the city's Engineering Division or Osceola County's Building Office, depends on whether the lot sits inside the Kissimmee city limits or in the surrounding unincorporated county, and the two offices don't apply the same width rule."),
    "sections": [
        ("Inside the city, EnerGov routes the job in at least two business days",
         f"<p>The Engineering Division, at 101 Church St., 3rd Floor, takes driveway and sidewalk applications through the city's EnerGov portal under “Driveway / Sidewalk Construction,” and staff there confirm which documents a specific lot needs before the job moves forward "
         f"({src('kissimmee-driveway-sidewalk', 'City of Kissimmee, Apply for Driveway/Sidewalk Construction')}). Call 407-518-2278 or email engineering@kissimmee.gov to start the file. The city flags that some right-of-way along a given street belongs to FDOT or the county rather than the city, so a driveway on a state road or a county-maintained street can route through a second reviewer before the city's own sign-off is final.</p>"),
        ("Outside the limits, a driveway can't legally exceed 24 feet without a conditional use",
         f"<p>Osceola County's own driveway ordinance, Code §22-50.6, sets a hard ceiling of 24 feet for an ordinary residential driveway out in the unincorporated county, and getting past that number takes a conditional use approval before construction or widening can start "
         f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance Ch. 22 Art. II')}). That review runs through the county's Building Office at 1 Courthouse Square, Suite 1400, 407-742-0200 "
         f"({src('osceola-row-info', 'Osceola County, Right-of-Way Permit Information')}). The city hasn't published an equivalent limit for driveways inside its own limits, so a three-car layout that would trip the county's conditional-use review may clear the city's counter without it; confirming which jurisdiction actually governs the lot is the first call to make, before {cs('kissimmee', 'paver-driveways', 'a paver driveway')} or a wide concrete apron gets designed around the wrong rule.</p>"),
    ],
    "scenario": ("A two-car driveway on each side of the city line, worked out in square feet",
                 f"<p>Say a two-car driveway measures 20 by 24 feet, 480 square feet, replacing a cracked original pour. At {price('concrete-driveway')} per {per('concrete-driveway')}, that job lands between roughly $2,880 and $7,200 before demolition of the old slab is added. "
                 "Inside the city limits, that width clears Engineering's review without a special finding. On an otherwise identical lot in unincorporated Osceola County, a 24-foot-wide driveway sits right at the code's cap, so a homeowner planning anything wider, a third bay or a boat-trailer apron, needs a conditional use approval from the county before the extra footage gets poured.</p>"),
    "faqs": [
        faq("Does Kissimmee require a permit for a concrete driveway?",
            "Inside the city limits, yes: the Engineering Division reviews it through EnerGov, with routing taking at least two business days once the application and required documents are in. Outside the city, the same lot goes through Osceola County's Building Office instead."),
        faq("How wide can a driveway be in unincorporated Osceola County?",
            "County Code §22-50.6 caps a residential driveway at 24 feet wide unless the county approves a conditional use for something wider. That figure applies outside the Kissimmee city limits; the city itself hasn't published a comparable stand-alone width cap."),
        faq("Who do I call if I'm not sure whether my lot is inside Kissimmee city limits?",
            "Either office can usually tell you from the address: the city's Engineering Division at 407-518-2278, or Osceola County's Building Office at 407-742-0200. Confirming jurisdiction before a design is finalized avoids submitting a driveway plan to the office that doesn't actually review that parcel."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Kissimmee, FL – Permits",
    "meta": "Paver driveway installers in Kissimmee, FL: the city's right-of-way permit fees and why pavers have no listed permit type, as of October 2026.",
    "h1": "Paver Driveways in Kissimmee: Permits and Fees",
    "lede": capsule(f"A paver driveway in Kissimmee runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026, roughly double the plain-concrete range because of material and base labor. "
                     "The city's own permit-types list has no separate line item for pavers, and any part of the job that reaches into the right-of-way needs its own permit with fees that start at a $25 minimum."),
    "sections": [
        ("No separate paver line item means confirming the scope before ordering material",
         f"<p>The city's permit-types page spells out “Slab With/Without Footer,” a stand-alone pool and spa category, and “Fences & Walls” for masonry, but pavers have no entry of their own "
         f"({src('kissimmee-permit-types', 'City of Kissimmee, Types of Permits')}). That's not the same as being exempt; it means the permitting desk, at 407-518-2379 or permitting@kissimmee.gov, is the one to call to confirm which category a given paver driveway actually falls under before the pallets show up on site.</p>"),
        ("The right-of-way permit for the apron has its own fee schedule",
         f"<p>Where a paver driveway's apron crosses into the right-of-way, it needs a separate right-of-way permit, covering any work “in a street, under a sidewalk, or in the grassy area next to a street,” routed through Aaron Mendez at 407-518-2536 or engineeringpermitting@kissimmee.gov "
         f"({src('kissimmee-row-permit', 'City of Kissimmee, Apply for Right-of-Way Permits')}). Fees start at a $25 minimum; an open cut on a paved street runs $150, an open cut on an unpaved surface runs $25, and a bore-and-jack crossing runs $50. Outside the right-of-way, the rest of {svc('paver-driveways', 'the driveway')} on private property doesn't carry that particular fee.</p>"),
    ],
    "scenario": ("A paver driveway apron tying into the right-of-way, worked out in square feet",
                 f"<p>Say a 480 square foot two-car paver driveway ties into the street with an 8-foot-wide, 6-foot-deep apron section, 48 square feet, that technically sits in the right-of-way. At {price('paver-driveway')} per {per('paver-driveway')}, the full driveway lands between roughly $4,800 and $14,400 before the apron's open-cut fee, $150 if the street is paved, is added on top. "
                 "The rest of the driveway, the 432 square feet back from the street, doesn't carry that particular line item, though it still needs the city's or county's standard driveway review depending on the lot's jurisdiction.</p>"),
    "faqs": [
        faq("Does a paver driveway need a different permit than concrete in Kissimmee?",
            "The city's permit-types list doesn't name pavers separately the way it names slabs or pool decks, so confirming the correct category with the permitting desk before ordering material is worth the call. The scope of review isn't necessarily lighter just because pavers aren't listed by name."),
        faq("What does a right-of-way permit cost for a Kissimmee driveway apron?",
            "Fees start at a $25 minimum, with an open cut on a paved street running $150, an open cut on an unpaved surface running $25, and a bore-and-jack crossing running $50. That's separate from whatever the driveway permit itself costs for the rest of the lot."),
        faq("Who approves paver work that crosses into the Kissimmee right-of-way?",
            "Right-of-way permits route through Aaron Mendez in the Engineering Division, reachable at 407-518-2536 or engineeringpermitting@kissimmee.gov, covering any paver work that extends into the street, under a sidewalk, or in the grassy strip next to the road."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Kissimmee, FL – Permits",
    "meta": "Concrete patio contractors in Kissimmee, FL: the city's slab permit type and grading a backyard patio toward Lake Tohopekaliga, October 2026.",
    "h1": "Building a Concrete Patio in Kissimmee",
    "lede": capsule(f"A concrete patio in Kissimmee costs {price('concrete-patio')} per {per('concrete-patio')}, a Florida market range as of October 2026. "
                     "Kissimmee files a patio slab under its “Slab With/Without Footer” permit type, the same category covering a shed pad or an AC pad, and on the lots that back up to Lake Tohopekaliga or one of its canals, the slope away from the water matters as much as the mix design."),
    "sections": [
        ("A patio goes through the same slab permit type as a shed or AC pad",
         f"<p>Kissimmee's permitting office lists “Slab With/Without Footer” as one of its building permit types, a category that covers a patio the same way it covers a utility pad, separate from the pool-and-spa category or the “Fences & Walls” category for masonry "
         f"({src('kissimmee-permit-types', 'City of Kissimmee, Types of Permits')}). Call Permitting at 407-518-2379 or permitting@kissimmee.gov to confirm scope before pouring. A patio that stays inside the existing footprint of an older slab is typically a smaller submission than one that extends the paved area outward.</p>"),
        ("Grading toward Lake Tohopekaliga or a canal comes before the pour",
         f"<p>The city's own parks page describes Big Toho Marina on Lake Tohopekaliga as home to “one of the nation's best bass fishing lakes,” and a meaningful share of Kissimmee's backyards sit along that lake, a connected canal, or a community pond "
         f"({src('kissimmee-parks', 'City of Kissimmee, Parks')}). On a lot like that, a patio's slope has to carry rainwater away from the house without dumping it straight toward the shoreline, since the yard is already working with less fall than an inland lot has to spare. {svc('paver-patios', 'A paver patio')} on the same lot faces the identical grading question before the base goes down.</p>"),
    ],
    "scenario": ("A lakefront patio addition, worked out in square feet",
                 f"<p>Say a home backing onto Lake Tohopekaliga adds a 14 by 16 foot patio off the back of the house, 224 square feet, between the existing lanai and the yard that slopes toward the water. Pricing that at {price('concrete-patio')} per {per('concrete-patio')} puts the job somewhere around $1,344 to $2,912 before a broom or stamped finish changes the number. "
                 "Before the forms go in, the crew checks where the existing yard already sheds water, since a patio poured flat against a lot that already drains slowly toward the lake can pond against the house rather than carry water away from it.</p>"),
    "faqs": [
        faq("What permit covers a concrete patio in Kissimmee?",
            "The “Slab With/Without Footer” permit type, the same category the city uses for a shed pad or an AC pad, reviewed by Permitting at 407-518-2379. A patio that stays within an existing footprint is usually a smaller submission than one that extends the paved area."),
        faq("Does a lakefront lot need special grading for a new patio?",
            "Not a separate permit, but the slope matters more. A yard near Lake Tohopekaliga or a connected canal already has less natural fall to carry rainwater away from the house, so the patio's pitch gets checked against the existing drainage pattern before forming begins rather than left to chance."),
        faq("Can I add a patio without extending the existing slab's footprint?",
            "Often, yes, and staying within the existing paved footprint keeps the permit submission smaller. Extending outward into new ground, closer to the lake or into a side yard, brings in the same slab review but with a larger survey and drainage check attached."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Kissimmee, FL – HOA Rules",
    "meta": "Paver patio installers in Kissimmee, FL: Celebration's monthly architectural review and why a 1992-era yard often needs a flatter base, October 2026.",
    "h1": "Paver Patios and Walkways Around a Kissimmee Home",
    "lede": capsule(f"A paver patio in Kissimmee runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "In Celebration, the planned community just outside the city, a patio or walkway change goes to a monthly Architectural Review Committee meeting before it goes to the county, and on the area's older, 1990s-era lots, the base usually needs more regrading than a newer subdivision's yard."),
    "sections": [
        ("Celebration's Architectural Review Committee meets once a month",
         f"<p>Celebration, in unincorporated Osceola County a short drive from downtown Kissimmee, runs its exterior approvals through an Architectural Review Committee that “meets on the 3rd Monday of each month, unless posted otherwise,” at Town Hall, 851 Celebration Ave "
         f"({src('celebration-arc', 'Celebration, Architectural Review Committee')}). Applications carry a monthly deadline; the committee's own example cites an April application due by the first week of May. Planning a {cs('kissimmee', 'paver-patios', 'paver patio')} in Celebration around that monthly cycle avoids a design sitting idle for weeks waiting on the next meeting date.</p>"),
        ("A lot built around 1992 usually needs more base correction than a new one",
         f"<p>Kissimmee's typical home dates to 1992, old enough that the original backyard grading on a lot that age has usually settled, shifted with tree growth, or been reworked at least once by a prior owner "
         f"({src('acs-kissimmee', 'Census Reporter, Kissimmee')}). A newer paver patio on ground like that starts with more subgrade correction than a patio going into a yard graded within the last decade, since the compacted aggregate base has to make up for whatever settling already happened rather than simply following an undisturbed grade.</p>"),
    ],
    "scenario": ("A Celebration paver patio, worked out in square feet",
                 f"<p>Say a Celebration home relays 260 square feet of paver patio off the back porch, timed to clear the third-Monday ARC meeting before work starts. At {price('paver-patio')} per {per('paver-patio')}, that job lands between roughly $2,600 and $4,160 depending on the paver and base depth. "
                 "If the application misses one month's deadline, the next review doesn't happen for another four weeks, which is worth building into a start date before materials are ordered.</p>"),
    "faqs": [
        faq("How often does Celebration's architectural committee meet?",
            "On the third Monday of each month, unless the community posts a different date. Applications have their own monthly deadline ahead of that meeting, so a patio or walkway plan submitted after the cutoff waits for the following month's review."),
        faq("Does a paver patio need county approval in addition to Celebration's review?",
            "Celebration sits in unincorporated Osceola County, so its Architectural Review Committee reviews the design on top of, not instead of, whatever county permit the slab-and-base work itself requires."),
        faq("Why does an older Kissimmee yard need more base work for pavers?",
            "With the typical home dating to 1992, a lot of backyards have already settled, been regraded once, or grown mature tree roots since the original construction. A paver base built on ground like that corrects for that history rather than following an undisturbed natural grade."),
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Kissimmee, FL",
    "meta": "Concrete pool deck builders in Kissimmee, FL: flatwoods soil and the water table, plus short-term rental zoning for new pool homes, October 2026.",
    "h1": "Concrete Pool Decks for Kissimmee Homes",
    "lede": capsule(f"Pricing a concrete pool deck in Kissimmee runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, a Florida market range as of October 2026. "
                     "A fair share of the newer pools going in around the city sit on lots zoned for short-term rental use, and across the area generally, the flatwoods soil under the slab holds water close to the surface for part of the year, which shapes how the deck is graded."),
    "sections": [
        ("Flatwoods soil holds a water table within 18 inches for part of the year",
         f"<p>The Smyrna soil series, officially established in Osceola County in 1976, is one of the flatwoods soils that cover a lot of ground under Kissimmee-area yards, alongside Myakka, Florida's own state soil "
         f"({src('nrcs-smyrna-osd', 'NRCS, Official Series Description, Smyrna')}; {src('nrcs-myakka-osd', 'NRCS, Official Series Description, Myakka')}). Both can sit wet within about a foot and a half of grade for one to four months of a typical year, so a crew lays out a pool deck's pitch and its finished height over the yard before forming, instead of trusting a site plan drawn for a lot with faster-draining sand.</p>"),
        ("New pools near the attractions often sit on rental-zoned lots",
         f"<p>A lot of the newer construction around Kissimmee's resort corridor is on parcels zoned for short-term rental use, either inside a Short Term Rental Planned Development or an area on the county's rental overlay map "
         f"({ext(STRPD_URL, 'Osceola County, STRPD District')}). A pool deck on one of those lots goes through the same slab review as any other, but a property manager overseeing a rental often specifies a slip-resistant, cool-touch finish built for guests in wet feet rather than the household's own routine use.</p>"),
    ],
    "scenario": ("A new pool deck on flatwoods ground, worked out in square feet",
                 f"<p>Say a new-construction home pours a 720 square foot pool deck around a freshly set pool shell on ground mapped as Smyrna fine sand. Figuring {price('concrete-pool-deck')} per {per('concrete-pool-deck')} puts the job somewhere between $3,600 for a plain broom texture and $10,800 for a cool-touch decorative surface, with most finishes falling between those two numbers. "
                 "Because the water table on that soil can sit within 18 inches of the surface during the wettest months, the crew confirms the pool's finished elevation against the yard's drainage pattern before the deck forms go up, not after.</p>"),
    "faqs": [
        faq("Does Kissimmee's soil affect how a pool deck is built?",
            "The Smyrna and Myakka series common under Kissimmee-area lots can sit wet within about a foot and a half of grade for part of the year. That shapes the deck's slope and finished elevation more than it changes the concrete mix itself."),
        faq("Do rental-zoned pool homes near Kissimmee need a different deck permit?",
            "No, the slab permit process is the same regardless of how the home is used. Zoning for short-term rental use is a separate check against the county's overlay map or a Short Term Rental Planned Development designation, not a different building permit category."),
        faq("What finish works best on a pool deck that sees heavy guest traffic?",
            "A slip-resistant, cool-touch broom or textured finish holds up to wet feet and frequent turnover better than a smooth trowel finish, which is one reason property managers on rental-zoned lots often specify it even though the underlying slab spec doesn't change."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Kissimmee, FL – Overlays",
    "meta": "Pool deck paver overlays in Kissimmee, FL: resurfacing 1990s-era decks near Lake Tohopekaliga and the city's slab permit type, October 2026.",
    "h1": "Pool Deck Pavers in Kissimmee: New Decks and Overlays",
    "lede": capsule(f"Pool deck pavers in Kissimmee cost {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, a Florida market range as of October 2026, and that number holds whether the pavers go down fresh or get relaid over a deck that's already there. "
                     "With the typical Kissimmee home dating to 1992, a share of the original cool-deck and broom-finish pool surfaces around the older neighborhoods are now well past 30 years old and candidates for a paver overlay rather than a full tear-out."),
    "sections": [
        ("Original 1990s decks are old enough for an overlay, not just a patch",
         f"<p>Kissimmee's median year of home construction is 1992 "
         f"({src('acs-kissimmee', 'Census Reporter, Kissimmee')}), old enough that a meaningful share of the city's original pool decks have reached the stage where a worn cool-deck coating and hairline cracking call for a resurfacing decision rather than another spot patch. The city's slab permit type, filed with Permitting at 407-518-2379, covers that overlay the same way it covers a brand-new pour "
         f"({src('kissimmee-permit-types', 'City of Kissimmee, Types of Permits')}).</p>"),
        ("Older decks sit closer to downtown and the lake, newer ones toward the resort corridor",
         f"<p>Homes near the older, lake-adjacent parts of Kissimmee, closer to Lake Tohopekaliga and the historic core, tend to carry original pool decks from that same early-1990s era, while construction nearer the US-192 resort corridor skews newer, often on lots zoned for short-term rental use "
         f"({ext(STRPD_URL, 'Osceola County, STRPD District')}). That split shows up in the work itself: older, lake-area homes lean toward a paver overlay on an aging slab, while newer rental-zoned builds more often choose pavers for a first pool install.</p>"),
    ],
    "scenario": ("A paver overlay on a 1990s-era Kissimmee pool deck, worked out in square feet",
                 f"<p>Say a home built in 1992, the city's median construction year, resurfaces a 540 square foot original cool-deck patio with pavers set directly over the existing slab. Figuring {price('pool-deck-pavers')} per {per('pool-deck-pavers')} puts that overlay somewhere around $6,480 on the plain end and up near $16,200 if the owner picks travertine over a standard concrete paver. "
                 "A full tear-out instead of an overlay adds demolition cost but avoids building the new surface on top of whatever settling the original 1990s slab has already done.</p>"),
    "faqs": [
        faq("Can pavers go over a cracked pool deck in Kissimmee without tearing it out?",
            "Usually, as an overlay, reviewed under the same slab permit type the city uses for a brand-new pour. How much the existing slab has already settled or cracked is what decides whether an overlay holds up or a tear-out is the better call."),
        faq("Are older Kissimmee pool decks more likely to need an overlay than newer ones?",
            "Generally, yes. Homes closer to the older, lake-area parts of the city tend to carry pool decks dating to around the city's 1992 median construction year, while newer construction nearer the resort corridor more often involves a first paver install rather than a resurfacing job."),
        faq("Does a pool deck overlay need the same permit as a new pool deck?",
            "Yes, the city's slab permit type covers an overlay on an existing deck the same way it covers new construction, filed through Permitting at 407-518-2379."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Kissimmee, FL – Celebration",
    "meta": "Stamped concrete contractors in Kissimmee, FL: Celebration's monthly design review and Osceola County's 24-foot driveway cap, October 2026.",
    "h1": "Stamped Concrete Driveways and Patios in Kissimmee",
    "lede": capsule(f"A stamped-concrete project in Kissimmee costs {price('stamped-concrete')} per {per('stamped-concrete')}, a Florida market range as of October 2026 that moves with the pattern and the number of colors chosen. "
                     "In Celebration, the planned community outside the city known for its coordinated streetscapes, a new pattern or color on a visible driveway or walk goes to the monthly Architectural Review Committee, and any driveway there still has to fit inside the county's 24-foot width cap regardless of the finish chosen."),
    "sections": [
        ("Celebration's monthly review covers color and pattern changes too",
         f"<p>Celebration's Architectural Review Committee meets on the third Monday of each month at Town Hall, 851 Celebration Ave, with applications due ahead of a published monthly cutoff "
         f"({src('celebration-arc', 'Celebration, Architectural Review Committee')}). On a community built around a coordinated streetscape, a new stamped pattern or an integral color on a front driveway or walk is the kind of visible change that review exists to catch, so timing a stamped-concrete project around that monthly meeting avoids weeks of delay waiting for the next date.</p>"),
        ("The county's 24-foot driveway cap doesn't bend for a decorative finish",
         f"<p>Celebration sits in unincorporated Osceola County, where Code §22-50.6 caps a residential driveway at 24 feet wide unless the county approves a conditional use for something wider "
         f"({src('osceola-parking-ord', 'Osceola County, Parking Ordinance Ch. 22 Art. II')}). A stamped slate or ashlar pattern, or a decorative border added around the edge, doesn't change that width calculation; a driveway planned at 24 feet of stamped concrete still needs the same conditional-use review a plain gray pour at the same width would.</p>"),
    ],
    "scenario": ("A Celebration stamped driveway replacement, worked out in square feet",
                 f"<p>Say a Celebration home replaces a plain 260 square foot driveway-and-walk combination with a slate-pattern stamped finish and an integral color, staying within the county's 24-foot width cap. Pricing it at {price('stamped-concrete')} per {per('stamped-concrete')} puts the job somewhere between $2,080 and $4,940, with the number of colors and the release agent used swinging it toward either end. "
                 "Before the pour, the color and pattern go to the ARC for the next third-Monday meeting, a step that runs alongside, not instead of, the county's own driveway permit.</p>"),
    "faqs": [
        faq("Does Celebration review stamped concrete colors before installation?",
            "Yes, its Architectural Review Committee meets monthly to review exterior changes, and a new stamped pattern or integral color on a visible driveway or walk is the kind of change that review covers, separate from the county's driveway permit."),
        faq("Does a stamped-concrete driveway still have to meet the 24-foot width cap?",
            "In unincorporated Osceola County, yes. County Code §22-50.6 applies to driveway width regardless of finish, so a stamped pattern or decorative border doesn't exempt a driveway from the same 24-foot cap a plain pour would have to meet."),
        faq("How far in advance should I plan a Celebration stamped-concrete project?",
            "Build in time for the Architectural Review Committee's monthly cycle. Its meeting falls on the third Monday of most months, with applications due by a published deadline ahead of that date, so missing one cutoff means waiting roughly four weeks for the next review."),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Sidewalks & Walkways in Kissimmee, FL",
    "meta": "Concrete walkway and sidewalk contractors in Kissimmee, FL: the city's right-of-way permit versus the county's 48-hour regrade rule, October 2026.",
    "h1": "Concrete Sidewalks and Walkways in Kissimmee",
    "lede": capsule(f"A concrete walkway in Kissimmee runs {price('concrete-walkway')} per {per('concrete-walkway')} as of October 2026. "
                     "A walkway that touches the right-of-way goes through the city's right-of-way permit inside the city limits, with fees starting at a $25 minimum, or Osceola County's process outside them, which doesn't publish a fee but requires any disturbed ground to be regraded within 48 hours."),
    "sections": [
        ("Inside the city, right-of-way walkway work has a published fee schedule",
         f"<p>Any walkway work “in a street, under a sidewalk, or in the grassy area next to a street” needs a city right-of-way permit, routed through Aaron Mendez at 407-518-2536, with fees starting at a $25 minimum and an open cut on a paved surface running $150 "
         f"({src('kissimmee-row-permit', 'City of Kissimmee, Apply for Right-of-Way Permits')}). A walkway section that crosses a driveway apron is reviewed as part of that same driveway application rather than filed separately, under “Driveway / Sidewalk Construction” in EnerGov "
         f"({src('kissimmee-driveway-sidewalk', 'City of Kissimmee, Apply for Driveway/Sidewalk Construction')}).</p>"),
        ("In unincorporated Osceola County, disturbed ground has 48 hours to be regraded",
         f"<p>The county's own right-of-way page is written mostly with utility work in mind, but the same rule applies to a walkway or sidewalk repair that disturbs the grassy strip next to the road: the area has to be regraded within 48 hours, and lane closures are only allowed Monday, Tuesday, Thursday and Friday from 9 a.m. to 3 p.m., or Wednesday from 9 a.m. to 1 p.m. "
         f"({src('osceola-row-info', 'Osceola County, Right-of-Way Permit Information')}). No fee amount is published for that permit, unlike the city's itemized schedule, so confirming the cost ahead of time means a call to the Building Office at 407-742-0200.</p>"),
    ],
    "scenario": ("A front walkway replacement crossing the right-of-way, worked out in square feet",
                 f"<p>Say a 4-foot-wide, 30-foot-long front walkway, 120 square feet, needs replacing where it crosses the grassy strip next to the street. At {price('concrete-walkway')} per {per('concrete-walkway')}, that lands between roughly $840 and $2,040 before any right-of-way permit fee. "
                 "Inside the city limits, that permit runs a published $25 to $150 depending on whether the cut lands on a paved or unpaved surface; in unincorporated Osceola County, the same scope of work still needs regrading finished within 48 hours, with the fee itself confirmed directly with the Building Office.</p>"),
    "faqs": [
        faq("Does replacing a Kissimmee sidewalk always need a right-of-way permit?",
            "Only the part of the work that touches the street, the sidewalk itself, or the grassy strip next to the road. Inside the city, that's a right-of-way permit with a published fee schedule; in unincorporated Osceola County, the process is similar but without a published fee."),
        faq("How quickly does disturbed ground have to be regraded in unincorporated Osceola County?",
            "Within 48 hours of the work disturbing it, per the county's right-of-way guidance, along with limited lane-closure hours: weekdays other than Wednesday from 9 a.m. to 3 p.m., and Wednesday from 9 a.m. to 1 p.m."),
        faq("Is a walkway permit separate from a driveway permit in Kissimmee?",
            "Not when the walkway ties into the driveway apron; the city reviews both under the same “Driveway / Sidewalk Construction” application in EnerGov. A standalone walkway replacement elsewhere on the lot may still need its own right-of-way permit if it touches the street-side strip."),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Kissimmee, FL – Shed Pads",
    "meta": "Concrete slab contractors in Kissimmee, FL: the city's slab permit type and Osceola County's exemption disclosure form for small jobs, October 2026.",
    "h1": "Concrete Slabs for Sheds, Pads and Parking in Kissimmee",
    "lede": capsule(f"A concrete slab in Kissimmee runs {price('concrete-slab')} per {per('concrete-slab')} as of October 2026. "
                     "Inside the city, a shed, AC or parking pad goes through the “Slab With/Without Footer” permit type; in unincorporated Osceola County, a small enough job may instead qualify for the state's 2026 exemption, applied through the county's own disclosure form."),
    "sections": [
        ("The city's slab permit type covers sheds, AC pads and parking pads alike",
         f"<p>Kissimmee's permit-types page lists “Slab With/Without Footer” as its own building permit category, separate from the pool-and-spa line item and the “Fences & Walls” category "
         f"({src('kissimmee-permit-types', 'City of Kissimmee, Types of Permits')}). A 10 by 10 foot shed pad and a full RV parking slab both fall under that same category inside the city limits; size changes the fee and the review, not which permit type applies. Call Permitting at 407-518-2379 or permitting@kissimmee.gov to confirm the specific submission a given pad needs.</p>"),
        ("The county applies the state's exemption through its own disclosure form",
         f"<p>In unincorporated Osceola County, a small slab under the state's 2026 permit-exemption threshold is handled through an “Owner Disclosure of Exempt Work” form sent to buildingmailbox@osceola.org, rather than a full building-permit submission "
         f"({src('osceola-permit-info', 'Osceola County, Permit Information')}). The county's Homeowners page doesn't spell out a separate process for slabs, pavers or retaining walls beyond that disclosure route, so a call to the Building Office at 407-742-0200 is the way to confirm whether a specific pad qualifies "
         f"({src('osceola-homeowners', 'Osceola County, Homeowners')}).</p>"),
    ],
    "scenario": ("A shed pad on each side of the city line, worked out in square feet",
                 f"<p>Say a 10 by 12 foot shed pad, 120 square feet, goes in on a lot near the Kissimmee city line. At {price('concrete-slab')} per {per('concrete-slab')}, that lands between roughly $480 and $1,200 depending on the mix and reinforcement. "
                 "Inside the city, that pad is filed as a slab permit through Permitting. On an otherwise identical lot in unincorporated Osceola County, the same pad may qualify for the state's exemption instead, filed through the county's disclosure form rather than a full permit review, though confirming that with the Building Office is worth doing before the forms go up.</p>"),
    "faqs": [
        faq("What permit covers a shed slab in Kissimmee?",
            "Inside the city, the “Slab With/Without Footer” building permit type, the same category used for AC pads and parking pads. Outside the city, in unincorporated Osceola County, a small enough slab may instead qualify for the state's exemption process."),
        faq("Does Osceola County still require paperwork for an exempt slab?",
            "Yes. The county applies the state's 2026 exemption through an Owner Disclosure of Exempt Work form sent to its building mailbox, rather than skipping documentation entirely. A call to the Building Office confirms whether a specific slab qualifies."),
        faq("Is an AC pad permitted differently from a shed pad in Kissimmee?",
            "Inside the city, no, both fall under the same slab permit category, reviewed with a location survey showing where the pad sits on the lot relative to the property line."),
    ],
    "sources": SRC,
}

# 10. concrete-repair ----------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair & Resurfacing in Kissimmee, FL",
    "meta": "Concrete repair and resurfacing in Kissimmee, FL: why 1992-era driveways are cracking, and why Osceola isn't on the state's sinkhole-claims list, October 2026.",
    "h1": "Concrete Repair and Resurfacing in Kissimmee",
    "lede": capsule(f"A concrete repair or resurfacing job in Kissimmee costs {price('concrete-repair')} per {per('concrete-repair')}, a Florida market range as of October 2026. "
                     "The city's population climbed from 79,229 in the 2020 census to about 85,591 by mid-2025, so brand-new driveways now sit next to originals from the early 1990s, and the two age very differently once cracking shows up."),
    "sections": [
        ("A driveway from Kissimmee's median construction year has had three decades to move",
         f"<p>Kissimmee's median year of home construction is 1992 "
         f"({src('acs-kissimmee', 'Census Reporter, Kissimmee')}), which puts a sizable share of the city's original flatwork past the point where hairline cracking, a widened joint or a dulled finish is ordinary wear rather than a warning sign. Whether a given job needs a full permit depends on whether it stays inside the existing footprint or expands it; call Permitting at 407-518-2379 to confirm before assuming a resurfacing job is exempt.</p>"),
        ("Osceola isn't on the state's sinkhole-claims list the way some nearby counties are",
         f"<p>A 2010 Florida Senate interim report names eleven counties that together accounted for more than 88 percent of sinkhole insurance claims filed statewide between 2006 and 2009: Hernando, Pasco, Hillsborough, Pinellas, Marion, Polk, Orange, Alachua, Citrus, Miami-Dade and Broward "
         f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). Osceola isn't one of them. A dip or crack in a Kissimmee driveway is far more likely to trace back to loose fill under the original pour, a cracked irrigation line, or ground that simply holds water close to the surface for part of the year than to the abrupt collapse the state's catastrophic ground-cover-collapse coverage is written around.</p>"),
    ],
    "scenario": ("Resurfacing an original Kissimmee driveway, worked out in square feet",
                 f"<p>Say a 390 square foot two-car driveway, original to a house built around the city's 1992 median, is showing a network of hairline cracks and a chalky, worn surface. Resurfacing it at {price('concrete-repair')} per {per('concrete-repair')} works out to somewhere between $1,170 and $3,900, cheaper toward the broom-finish end and pricier if a decorative overlay gets added at the same time. "
                 "A full tear-out and repour instead would shift the job into driveway pricing territory and whatever permit process, city or county, actually covers that address.</p>"),
    "faqs": [
        faq("Should I worry about cracking in an original 1990s Kissimmee driveway?",
            "Not automatically. With the city's median home dating to 1992, hairline cracking and worn joints on a driveway that age are typically routine wear, not a structural issue. A sudden, deep depression rather than a gradual crack is the kind of thing worth a closer look."),
        faq("Does Osceola County see the sinkhole activity that Orange County does?",
            "No, it isn't on the Florida Senate's 2010 list of eleven counties with the heaviest sinkhole insurance claims from 2006 to 2009, unlike neighboring Orange County. Settlement from loose fill or a wet subgrade remains the more common explanation locally."),
        faq("Is a permit needed to resurface an existing driveway in Kissimmee?",
            "A full replacement goes through the same review as a new driveway, but work that stays inside the existing footprint is usually a lighter submission. Confirm the scope with Permitting before assuming a resurfacing job is exempt."),
    ],
    "sources": SRC,
}

# 11. paver-sealing -------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing & Restoration in Kissimmee, FL",
    "meta": "Paver sealing and restoration in Kissimmee, FL: why Toho Water Authority's watering days don't apply to a pressure wash, October 2026.",
    "h1": "Paver Sealing and Restoration in Kissimmee",
    "lede": capsule(f"Cleaning, re-sanding and sealing pavers in Kissimmee costs {price('paver-sealing')} per {per('paver-sealing')}, a Florida market range as of October 2026. "
                     "Toho Water Authority's twice-a-week schedule governs irrigation, not a hose-fed pressure washer, so cleaning pavers ahead of a seal doesn't have to wait for a particular day of the week."),
    "sections": [
        ("A pre-seal pressure wash doesn't follow Toho's watering calendar",
         f"<p>Toho Water Authority, the city's own utility, runs a year-round schedule: odd and no-number addresses water Wednesday and Saturday, even addresses water Thursday and Sunday, with nothing allowed between 10 a.m. and 4 p.m. "
         f"({ext(TOHO_URL, 'Toho Water Authority, Watering Days and Times')}). That calendar covers sprinklers and irrigation heads watering grass, and a hose running through a pressure washer to blast algae and dirt off a paver surface simply isn't the same category of water use, so the clean-and-re-sand step before sealing books around the crew's schedule and the forecast rather than a numbered address day.</p>"),
        ("Rental-zoned patios and driveways see joint sand wear out faster",
         f"<p>On lots zoned for short-term rental use, where a driveway or paver patio sees a new set of feet and vehicles every few days, joint sand washes out and pavers settle unevenly faster than on a lot with one household's ordinary traffic "
         f"({ext(STRPD_URL, 'Osceola County, STRPD District')}). Re-sanding with polymeric sand before sealing holds up better under that turnover pace than standard sand does, which is one reason property managers on those lots often schedule sealing more often than a homeowner on an inland, owner-occupied street.</p>"),
    ],
    "scenario": ("Resealing a Kissimmee paver driveway, worked out in square feet",
                 f"<p>Say a 480 square foot paver driveway gets a full clean, a polymeric re-sand and a seal. Pricing that at {price('paver-sealing')} per {per('paver-sealing')} puts the job around $720 to $1,560, with releveling any sunken pavers pushing it toward the higher figure. "
                 "On a rental-zoned property with weekly guest turnover, that same job often gets scheduled on a shorter cycle than an owner-occupied driveway would need, since the joint sand and surface wear faster under steady vehicle and foot traffic.</p>"),
    "faqs": [
        faq("Is a city or county permit required to reseal a Kissimmee paver driveway?",
            "Neither office treats maintenance on pavers that are already down as something to review. The slab and driveway permits both offices use are built around new construction or expanding a paved area, not around washing, re-sanding or sealing a surface that's already in place."),
        faq("Can pavers be pressure-washed on a day Toho Water Authority doesn't allow irrigation?",
            "Yes, since the irrigation schedule has nothing to do with a pressure washer. A sprinkler head watering grass and a hose feeding a pressure washer aren't regulated the same way, so the pre-seal rinse can happen any day a crew and the weather line up."),
        faq("How often should pavers on a rental property be resealed?",
            "More often than an owner-occupied driveway typically needs, since steady guest turnover wears joint sand and surface sealer down faster. There's no fixed interval set by any code; it depends on how much traffic the surface actually sees between sealing jobs."),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Kissimmee, FL – Permits",
    "meta": "Retaining wall contractors in Kissimmee, FL: why neither the city nor Osceola County publishes a wall-height trigger, October 2026.",
    "h1": "Retaining Walls for Kissimmee Yards",
    "lede": capsule(f"Building a retaining wall in Kissimmee costs {price('retaining-wall')} per {per('retaining-wall')}, a Florida market range as of October 2026. "
                     "Neither the city's permit-types page nor Osceola County's homeowner guidance publishes a stand-alone wall height that triggers engineering review, so confirming the threshold directly with whichever office covers the lot is part of planning the job."),
    "sections": [
        ("Both the city and the county leave the wall-height trigger unpublished",
         f"<p>Kissimmee's permit-types page lists “Fences & Walls” as covering masonry walls, but doesn't spell out a specific retaining-wall height that requires sealed engineering "
         f"({src('kissimmee-permit-types', 'City of Kissimmee, Types of Permits')}). Osceola County's own Homeowners page is silent on slabs, pavers and retaining walls alike, directing residents instead to call the Building Office at 407-742-0200 for specifics "
         f"({src('osceola-homeowners', 'Osceola County, Homeowners')}). That makes a direct call to whichever office reviews a given lot worth making before a wall design is finalized, rather than assuming a figure used elsewhere in Central Florida applies locally.</p>"),
        ("Lakefront and canal lots usually have more fill to hold back",
         f"<p>A yard that slopes down toward Lake Tohopekaliga or a connected canal typically needs more retained fill than a flat inland lot, since the grade drops further over the same horizontal distance "
         f"({src('kissimmee-parks', 'City of Kissimmee, Parks')}). A low seat wall is sometimes enough on a gently sloped inland lot; a taller segmental block wall closer to the water usually needs more attention to drainage behind the wall, since water that can't weep through the wall face adds pressure the wall wasn't sized for.</p>"),
    ],
    "scenario": ("A sloped lakefront-adjacent wall, worked out in square feet",
                 f"<p>Say a yard near a canal off Lake Tohopekaliga needs a 25 linear foot segmental block wall, 3 feet tall, 75 square feet of wall face, to hold the grade at the edge of a patio. Pricing it at {price('retaining-wall')} per {per('retaining-wall')} puts that job somewhere between $1,125 and $3,000 before drainage behind the wall is added in. "
                 "Before finalizing the height, a call to whichever office, city or county, reviews that address confirms whether this particular wall crosses into sealed-engineering territory, since neither one publishes the trigger outright.</p>"),
    "faqs": [
        faq("What height retaining wall needs a permit in Kissimmee?",
            "Neither the city's permit-types page nor Osceola County's homeowner guidance states a specific height, unlike some neighboring jurisdictions. Call Permitting at 407-518-2379 inside the city, or the Building Office at 407-742-0200 outside it, to confirm before finalizing a design."),
        faq("Does a retaining wall near Lake Tohopekaliga need extra drainage?",
            "Often, yes. A wall holding back a steeper slope toward the lake or a canal typically carries more water pressure behind it than a wall on a flat inland lot, so weep holes or a drainage system behind the wall matter more on waterfront ground."),
        faq("Is a retaining wall covered under Kissimmee's 'Fences & Walls' permit type?",
            "The city's permit-types list uses that category for masonry walls, though it doesn't spell out whether every retaining wall falls under it or when sealed engineering kicks in. Confirming the specific category with Permitting avoids submitting under the wrong type."),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Kissimmee, FL – Rules",
    "meta": "Artificial turf installers in Kissimmee, FL: the statewide water-body setback near Lake Tohopekaliga and Toho's watering schedule, October 2026.",
    "h1": "Artificial Turf for Kissimmee Yards",
    "lede": capsule(f"Installing artificial turf in Kissimmee costs {price('artificial-turf')} per {per('artificial-turf')}, a Florida market range as of October 2026. "
                     "On lots near Lake Tohopekaliga or a connected canal, the state's turf rule keeps synthetic grass at least 10 feet from the water unless it backs onto a seawall, and because turf isn't irrigated, it sits outside Toho Water Authority's twice-a-week watering schedule entirely."),
    "sections": [
        ("A 10-foot water-body setback applies near the lake and its canals",
         f"<p>Under the state's turf rule, which took effect in May 2026, synthetic grass has to stay 10 feet clear of a water body unless the lot backs onto a seawall, and a washed base, natural infill and no buried irrigation line underneath round out the installation standard "
         f"({src('dep-rule', 'Florida Administrative Code, Rule 62-308.100')}). A separate 2025 law caps how aggressively a city or county can write its own turf restrictions on top of that state standard "
         f"({src('fs125572', 'Florida Statutes §125.572')}). On a lot backing onto Lake Tohopekaliga or one of its canals, that 10-foot line is the first measurement worth checking before laying out where the turf starts.</p>"),
        ("Turf skips Toho's watering schedule, useful for off-site rental owners",
         f"<p>Toho Water Authority's twice-a-week schedule, Wednesday and Saturday for odd addresses, Thursday and Sunday for even ones, governs irrigated sod, not turf, since nothing under an installed turf system needs watering once the base is compacted "
         f"({ext(TOHO_URL, 'Toho Water Authority, Watering Days and Times')}). That matters in particular for an owner managing a short-term rental lot from out of town, who can't always track which watering day applies to a given address the way someone living in the house year-round can.</p>"),
    ],
    "scenario": ("Backyard turf near a Lake Tohopekaliga canal, worked out in square feet",
                 f"<p>Say a canal-front lot swaps out 600 square feet of struggling St. Augustine for artificial turf, with the layout kept 10 feet clear of the water's edge. Figuring {price('artificial-turf')} per {per('artificial-turf')} puts that job somewhere between $6,000 for a basic pile and $15,000 for a thicker, more realistic build. "
                 "Staying outside that 10-foot line means the project doesn't need to lean on the seawall exception at all, though a layout planned any closer to the water would have to confirm that condition first.</p>"),
    "faqs": [
        faq("How close to Lake Tohopekaliga can artificial turf be installed?",
            "No closer than 10 feet under the state's turf rule, unless the lot backs onto a seawall, in which case that buffer doesn't apply the same way. The rule also bars in-ground irrigation from running under the turf and requires natural infill and a washed base."),
        faq("Does artificial turf need to follow Toho Water Authority's watering schedule?",
            "No, that schedule governs irrigated sod and landscaping, not turf, since an installed turf system doesn't need watering once the base is in. That makes turf easier to manage for an owner who isn't checking the local watering calendar regularly."),
        faq("Can an HOA in the Kissimmee area ban artificial turf entirely?",
            "State law caps how far a local government can go in restricting residential turf, and the DEP's rule sets the baseline installation standard. A specific HOA's design guidelines may still layer on additional rules, which is worth checking before installation regardless of what the city or county otherwise allows."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
