# -*- coding: utf-8 -*-
from _helpers import page, capsule, sec, faq, svc, city, cs, post, src, ext, price, per
from _cityservice import cityservice_pages

SLUG = "lakewood-ranch"

SRC = [
    "acs-lakewoodranch", "lwr-cdp-counties", "census-gazetteer-fl", "lwr-about", "lwr-ceva-manual", "lwr-ceva-form", "lwr-gbva-srva-form",
    "manatee-ldc-1004.2-access-drainage-permit", "manatee-driveway-application", "manatee-driveway-culvert-service",
    "manatee-paver-driveway-inspections", "manatee-no-permit-list", "manatee-ldc-511.16-pool-decks",
    "sarasota-county-row-permit", "sarasota-county-98-3-culvert-row-fees", "sarasota-county-124-255-culverts",
    "sarasota-county-22-63-retaining-walls", "sarasota-county-building-page",
    "swfwmd-restrictions", "manatee-phase3", "nrcs-myakka-osd", "nrcs-eaugallie-osd", "nrcs-immokalee-osd",
    "dep-rule", "fs125572", "fs720-3045",
]

# ---------------------------------------------------------------------- hub

HUB_BODY = "".join([
    sec("Two county permit desks, split roughly 75/25 across one community",
        f"<p>Lakewood Ranch's census-designated place covers about 46 square miles, and roughly three-quarters of that area sits in Manatee County with the rest in Sarasota County "
        f"({src('lwr-cdp-counties', 'Census Reporter, Lakewood Ranch CDP geography')}; {src('census-gazetteer-fl', 'Census 2024 Gazetteer, Florida places')}). On the Manatee side, any driveway, apron or sidewalk reaching from the property line to the edge of the roadway pavement needs an access and drainage permit under LDC §1004.2, reviewed by the Public Works Infrastructure Engineering Division "
        f"({src('manatee-ldc-1004.2-access-drainage-permit', 'Manatee County LDC §1004.2')}). On the Sarasota side, the same work falls under the county's Right-of-Way Use Permit, required for all work inside the county right-of-way "
        f"({src('sarasota-county-row-permit', 'Sarasota County Code §124-48')}). {post('manatee-county-driveway-permits', 'Our Manatee County permit guide')} and {post('sarasota-county-driveway-patio-permits', 'our Sarasota County permit guide')} go further into each county's forms and fees.</p>"),
    sec("Community Association Services and the Modification Request Form",
        f"<p>Neither county permit above reaches the community's own design review. Lakewood Ranch's governance runs through an Inter-District Authority board, drawn one member from each of the community's five Community Development Districts, which assigns day-to-day review of exterior changes to Community Association Services, based at the community's Town Hall "
        f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}; {src('lwr-about', 'Lakewood Ranch / SMR, About Us')}). A driveway, patio or pool-deck project clears that second gate through a Modification Request Form, and the exact form depends on the village: Country Club and Edgewater share one, Greenbrook and Summerfield-Riverwalk another, with a generic community-wide version for everywhere else "
        f"({src('lwr-ceva-form', 'Lakewood Ranch CEVA Modification Request Form')}; {src('lwr-gbva-srva-form', 'Lakewood Ranch GBVA-SRVA Modification Request Form')}). {post('lakewood-ranch-arc-approval-hardscape', 'Our Lakewood Ranch ARC guide')} walks through that paperwork village by village.</p>"),
    sec("The newest housing stock in the Sarasota unit",
        f"<p>The Census Bureau's latest estimate puts the Lakewood Ranch CDP at 43,945 residents, with a median year structure built of 2014, the newest of the ten towns the Sarasota unit serves "
        f"({src('acs-lakewoodranch', 'Census Reporter, Lakewood Ranch CDP')}). That shows up on the ground: most driveways, pool decks and patios here are still close to their original builder-grade pour rather than due for a decades-old repour, and a lot of lots back onto one of the community's lakes or a golf-course fairway rather than a plain rear yard. {svc('paver-driveways', 'A paver driveway')} or {svc('stamped-concrete', 'a stamped finish')} upgrade on an otherwise young, plain-gray slab is a more common call here than a full tear-out.</p>"),
    sec("Myakka and EauGallie flatwoods soil under a community built around lakes",
        f"<p>Manatee and Sarasota counties share the same flatwoods ground found across the rest of the Sarasota unit. Myakka, named Florida's official state soil in 1989, covers much of it, alongside EauGallie and Immokalee, two more spodic series common on both sides of the county line; on all three, standing groundwater can climb to within a foot and a half of the yard for a stretch of most years "
        f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}; {src('nrcs-eaugallie-osd', 'NRCS, EauGallie series')}; {src('nrcs-immokalee-osd', 'NRCS, Immokalee series')}). Lakewood Ranch's own stormwater lakes are how a master-planned community on that ground manages runoff, which is also why a lot behind one of those lakes compacts and drains differently at the edge than a lot two streets back does. {svc('concrete-slabs', 'A slab')} or {svc('retaining-walls', 'a retaining wall')} on a lake lot gets a site check for that reason before it gets a price.</p>"),
    sec("A once-a-week watering order that runs through March 2027",
        f"<p>Manatee and Sarasota counties, Lakewood Ranch included, are currently under the Southwest Florida Water Management District's Modified Phase III shortage order, in effect since April 3, 2026 through the end of March 2027, which cuts irrigation to a single day a week keyed to the last digit of the street address "
        f"({src('swfwmd-restrictions', 'SWFWMD District Water Restrictions')}; {src('manatee-phase3', 'Manatee County, Modified Phase III water shortage restrictions')}). A newly poured driveway or patio slab needs its own hand-watering during curing, a routine that sits outside the lawn-irrigation order but is worth scheduling around it anyway. {svc('artificial-turf', 'Artificial turf')}, once it's watered in after installation, doesn't answer to that order at all.</p>"),
    sec("What the state's 2026 turf rule means on a lake or golf-course lot",
        f"<p>DEP's synthetic-turf standard, in force since May 19, 2026, keeps the installed turf a minimum of 10 feet back from any pond, lake or canal unless the edge is a seawall, rules out in-ground sprinklers running beneath it, and calls for a washed base under natural infill "
        f"({src('dep-rule', 'DEP Rule 62-308.100')}). On a lot that backs onto one of Lakewood Ranch's lakes or a golf-course pond, that 10-foot line is worth measuring before anyone draws a turf layout. A 2025 law caps how aggressively a city or county, though not a homeowners' association, can regulate residential turf beyond that state standard "
        f"({src('fs125572', 'F.S. 125.572')}), and separately, a community's design review can only say no to turf that a passerby or a neighbor can actually see "
        f"({src('fs720-3045', 'F.S. 720.3045')}). {post('florida-hoa-artificial-turf-law', 'Our Florida HOA artificial-turf law guide')} covers that protection in full.</p>"),
    "<!--AUTO:city-services-->",
])

HUB_FAQS = [
    faq("Do you work in all Lakewood Ranch villages and districts?",
        f"Yes, on both sides of the county line, Country Club, Edgewater, Greenbrook and Summerfield-Riverwalk included, along with the rest of the community's five Community Development Districts. The crew also reaches {city('bradenton')} and {city('sarasota')} directly, about 10 miles from the unit's Sarasota base."),
    faq("Which county issues my driveway permit in Lakewood Ranch?",
        "It depends on which side of the community line your lot sits on. Roughly three-quarters of the CDP is in Manatee County, where an access and drainage permit covers the driveway; the rest is in Sarasota County, where the same work falls under a Right-of-Way Use Permit."),
    faq("What is a Modification Request Form, and do I need one?",
        "It's the community's own design review, separate from the county permit, processed by Community Association Services out of the community's Town Hall. The specific form depends on your village, so confirming which association covers your address is the first step before submitting anything."),
    faq("Can I paint my concrete driveway in Lakewood Ranch?",
        f"In Country Club/Edgewater Village, the homeowners' manual states that painting residential driveways and sidewalks isn't permitted there. Integral color added during a {svc('stamped-concrete', 'stamped concrete')} pour is a different method from painting an existing surface, and it's worth asking your own village's committee how that distinction applies before ordering materials."),
    faq("How close to a pond can artificial turf be installed in Lakewood Ranch?",
        "No closer than 10 feet under the state's 2026 turf rule, unless the turf backs onto a seawall. That setback applies on top of whichever county permit and community Modification Request Form the lot otherwise needs."),
    faq("How do you pick the best concrete contractor in Lakewood Ranch?",
        f"Verify the contractor on the state's license-check tool, ask whether the quote accounts for both the county permit and the village's Modification Request Form, and compare how each bid handles a lot that backs onto one of the community's lakes. {post('how-to-choose-a-concrete-contractor-sarasota', 'Our guide to choosing a concrete contractor in Sarasota and Bradenton')} covers more ground."),
]

HUB = page("/lakewood-ranch-fl/", "city", "Concrete, Pavers & Turf Contractor in Lakewood Ranch, FL",
           "Concrete, pavers and turf in Lakewood Ranch, FL: the Manatee/Sarasota county split, the Modification Request Form, and the 2026 turf setback, Oct. 2026.",
           "Concrete, Pavers and Artificial Turf for Lakewood Ranch Homes",
           capsule("Opera builds concrete driveways, pavers, pool decks and artificial turf across Lakewood Ranch, a community of about 43,945 residents split roughly three-quarters into Manatee County and one-quarter into Sarasota County, with a median home built in 2014. "
                   f"A concrete driveway here currently prices out at {price('concrete-driveway')} per {per('concrete-driveway')}, current as of October 2026, and most exterior projects need both a county permit and the community's own Modification Request Form before a crew starts."),
           HUB_BODY, faqs=HUB_FAQS, sources=SRC, city=SLUG,
           crumbs=[("Service areas", "/service-areas/"), ("Sarasota, Lakewood Ranch & Bradenton", "/sarasota-manatee/")], crumb="Lakewood Ranch",
           related=[("/sarasota-manatee/", "The Sarasota unit: concrete, pavers and turf for the Suncoast"),
                    ("/blog/lakewood-ranch-arc-approval-hardscape/", "Lakewood Ranch ARC approval for hardscape"),
                    ("/blog/manatee-county-driveway-permits/", "Driveway and patio permits in Manatee County"),
                    ("/sarasota-fl/", "Concrete, pavers and turf in Sarasota"),
                    ("/bradenton-fl/", "Concrete, pavers and turf in Bradenton"),
                    ("/permits/", "Permits & HOA hub")],
           eyebrow="Concrete · Pavers · Turf in Lakewood Ranch, FL")

# ---------------------------------------------------------------------- services

LOCAL = {}

# 1. concrete-driveways ------------------------------------------------------
LOCAL["concrete-driveways"] = {
    "title": "Concrete Driveways in Lakewood Ranch, FL – Permits",
    "meta": "Concrete driveways in Lakewood Ranch, FL: Manatee's access and drainage permit, Sarasota County's ROW permit, and the Modification Request Form, Oct. 2026.",
    "h1": "Pouring or Widening a Concrete Driveway in Lakewood Ranch",
    "lede": capsule(f"A concrete driveway in Lakewood Ranch runs {price('concrete-driveway')} per {per('concrete-driveway')} as of October 2026. "
                     "Most homes here were built around 2014, so driveway work tends to mean widening or replacing a builder-spec pour rather than resurfacing decades of wear, and which county reviews the permit depends on which side of the community line the lot sits on."),
    "sections": [
        ("Why the permit office depends on which side of the line you're on",
         f"<p>On the Manatee County side, about three-quarters of the community by area "
         f"({src('lwr-cdp-counties', 'Census Reporter, Lakewood Ranch CDP geography')}), any driveway reaching from the property line to the edge of the roadway pavement needs an access and drainage permit under LDC §1004.2, filed through the Public Works Infrastructure Engineering Division "
         f"({src('manatee-ldc-1004.2-access-drainage-permit', 'Manatee County LDC §1004.2')}). On the Sarasota County side, the same scope of work falls under the county's Right-of-Way Use Permit, required for all work inside the county right-of-way "
         f"({src('sarasota-county-row-permit', 'Sarasota County Code §124-48')}). Neither permit is the community's own review; {post('lakewood-ranch-arc-approval-hardscape', 'the Modification Request Form')} that Community Association Services processes runs on a separate track afterward.</p>"),
        ("Manatee's own width and thickness spec, where it applies",
         f"<p>On the Manatee side, the county's Driveway and Culvert Application sets a 12-foot minimum and 24-foot maximum width for a residential driveway, widening to 30 feet for a street-facing three-car garage, with the slab itself 6 inches thick from the edge of the roadway pavement to the right-of-way line and an expansion joint set between the curb and the new concrete "
         f"({src('manatee-driveway-application', 'Manatee Driveway and Culvert Application')}). The application also rules out a shell driveway apron next to a paved road. Applications go in through the county's Accela portal under Building > Public Works > Driveway/Culvert "
         f"({src('manatee-driveway-culvert-service', 'Manatee County, Request a Driveway or Culvert Permit')}).</p>"),
    ],
    "scenario": ("A two-car driveway on the Manatee side, worked out in square feet",
                 f"<p>Say a two-car driveway on the Manatee County side of Lakewood Ranch measures 20 by 24 feet, 480 square feet, and the household wants it widened to fit a third vehicle alongside the county's access and drainage permit review. At {price('concrete-driveway')} per {per('concrete-driveway')}, a straight repour of that footprint lands between $2,880 and $7,200, narrowing to roughly $3,840 to $5,760 in the typical {price('concrete-driveway', typical=True)} band. Because the home dates to the community's 2014 median year, the existing slab is usually sound enough that the job is a widening rather than a full tear-out, and widening past the original footprint means a fresh look at the 12-to-24-foot width cap before the county signs off.</p>"),
    "faqs": [
        faq("Which office issues a driveway permit in Lakewood Ranch?",
            "It depends on the lot's location: Manatee County's Public Works Infrastructure Engineering Division on the Manatee side, under an access and drainage permit, or Sarasota County's Right-of-Way Use Permit on the Sarasota side. Confirming which side a given address falls on is the first step."),
        faq("How wide can a driveway be on the Manatee County side?",
            "12 feet minimum and 24 feet maximum for most residential driveways, with an exception up to 30 feet for a street-facing three-car garage, under the county's own Driveway and Culvert Application."),
        faq("Do I still need the community's approval if the county issues a permit?",
            f"Yes. The county permit and Community Association Services' Modification Request Form are two separate reviews. {post('lakewood-ranch-arc-approval-hardscape', 'Our Lakewood Ranch ARC guide')} covers which form applies to which village."),
    ],
    "sources": SRC,
}

# 2. paver-driveways ----------------------------------------------------------
LOCAL["paver-driveways"] = {
    "title": "Paver Driveways in Lakewood Ranch, FL – Upgrades",
    "meta": "Paver driveway upgrades in Lakewood Ranch, FL: the community's material-change review and Manatee's paver-driveway inspection spec, as of October 2026.",
    "h1": "Upgrading a Builder-Grade Driveway to Pavers in Lakewood Ranch",
    "lede": capsule(f"A paver driveway in Lakewood Ranch runs {price('paver-driveway')} per {per('paver-driveway')} as of October 2026. "
                     "Most driveways here left the builder as plain gray concrete, so a paver driveway is usually a material change on a home built since 2014 rather than new construction, and a material change is exactly what the community's Modification Request Form exists to review."),
    "sections": [
        ("Why swapping concrete for pavers needs its own sign-off",
         f"<p>The Country Club/Edgewater Village homeowners' manual lists changing the material of a residential driveway or walkway as one of the items that requires a Modification Request Form "
         f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}). Community Association Services processes that form regardless of which village the lot sits in, but the exact paperwork differs: Country Club and Edgewater share one form, Greenbrook and Summerfield-Riverwalk another "
         f"({src('lwr-ceva-form', 'Lakewood Ranch CEVA Modification Request Form')}; {src('lwr-gbva-srva-form', 'Lakewood Ranch GBVA-SRVA Modification Request Form')}). {post('lakewood-ranch-arc-approval-hardscape', 'Our Lakewood Ranch ARC guide')} walks through submitting the right one.</p>"),
        ("What a Manatee inspector checks on a paver driveway",
         f"<p>On the Manatee side, the subgrade is cut 6 inches deep so the compacted base plus the paver equal that same 6 inches, width stays within the 12-to-24-foot range, 30 feet for a street-facing three-car garage, and flares at the roadway add 3 feet to each side and run 8 feet long "
         f"({src('manatee-paver-driveway-inspections', 'Manatee County, Inspections Required for Paver Driveways')}). Neither the county inspection nor the village paperwork substitutes for the other; both have to clear before the base goes down.</p>"),
    ],
    "scenario": ("Converting a builder-grade driveway to pavers, worked out in square feet",
                 f"<p>Say a plain-concrete driveway original to a 2015-built home measures 500 square feet and the owner wants pavers instead. At {price('paver-driveway')} per {per('paver-driveway')}, that job runs between $5,000 and $15,000, narrowing to roughly $6,000 to $10,000 in the typical {price('paver-driveway', typical=True)} band depending on the paver and base thickness. Because the material is changing, the Modification Request Form has to clear Community Association Services before the old slab comes out; starting demolition ahead of that approval is the kind of sequencing mistake that turns a straightforward upgrade into a committee conversation after the fact.</p>"),
    "faqs": [
        faq("Can I replace a plain concrete driveway with pavers in Lakewood Ranch?",
            "Yes, but changing the driveway's material is one of the items Country Club/Edgewater Village's own guidelines flag for a Modification Request Form, processed by Community Association Services before the work starts."),
        faq("What does a Manatee County inspector check on a new paver driveway?",
            "A 6-inch grade cut so the compacted base plus the paver equal 6 inches, a width between 12 and 24 feet (30 feet for a street-facing three-car garage), and flares that add 3 feet to each side at the roadway."),
        faq("Which village's form do I use for a driveway material change?",
            "It depends on the address: Country Club and Edgewater share one form, Greenbrook and Summerfield-Riverwalk another, and the rest of the community uses a generic version. Confirming which association covers your lot comes before submitting anything."),
    ],
    "sources": SRC,
}

# 3. concrete-patios -----------------------------------------------------------
LOCAL["concrete-patios"] = {
    "title": "Concrete Patios in Lakewood Ranch, FL – Permits",
    "meta": "Concrete patios in Lakewood Ranch, FL: Manatee's non-structural patio exemption and lanai extensions on lake-facing lots, as of October 2026.",
    "h1": "Building a Concrete Patio in Lakewood Ranch",
    "lede": capsule(f"A concrete patio in Lakewood Ranch runs {price('concrete-patio')} per {per('concrete-patio')} as of October 2026. "
                     "On the Manatee side, a non-structural patio skips the county's building permit, though a slab poured with footers or one tied into a pool still needs one, and the community's own design review runs separately either way."),
    "sections": [
        ("Why a non-structural patio skips the county permit, but a pool tie-in doesn't",
         f"<p>Manatee County's current no-permit list puts a “non-structural concrete/paver patio” under work that doesn't need a building permit, while a “concrete slab with footers” or anything tied to a swimming pool still requires one "
         f"({src('manatee-no-permit-list', 'Manatee County, What Does Not Require a Permit')}). That exemption is about the county's building permit specifically, not about the community's own layer: a patio is still the kind of exterior change Community Association Services reviews on its own track, separate from whether the county needed paperwork first.</p>"),
        ("Extending a lanai patio behind a home built after 2014",
         f"<p>Because most Lakewood Ranch homes are recent, the screened pool cage and its original patio slab are usually part of the same build rather than a later addition. Extending that patio, toward a lake view or a fairway on the lots that back onto one, typically means tying a new edge into the existing slab rather than pouring under the screen frame itself, and matching the finish and slope of concrete that's rarely more than a decade old. {svc('concrete-pool-decks', 'A pool deck')} extension follows the same logic on a lot where the cage and the patio were poured together.</p>"),
    ],
    "scenario": ("A lanai patio extension, worked out in square feet",
                 f"<p>Say a 14 by 16 foot lanai extension, 224 square feet, adds a sitting area off the back of a screened pool cage on a lot that backs onto one of the community's lakes. At {price('concrete-patio')} per {per('concrete-patio')}, that runs $1,344 to $2,912, or roughly $1,568 to $2,240 in the typical {price('concrete-patio', typical=True)} band for a broom-finished slab tied into the existing cage footing. Because the addition is non-structural and stays on grade, it's the kind of scope that clears Manatee's no-permit list; the design still goes to Community Association Services separately.</p>"),
    "faqs": [
        faq("Does a concrete patio need a county permit in Lakewood Ranch?",
            "On the Manatee side, a non-structural concrete or paver patio is on the county's own no-permit list. A slab poured with footers, or one tied into a pool, still needs a permit either way."),
        faq("Does the community still review a patio that's exempt from the county permit?",
            "Yes. The county's exemption only covers the building permit; exterior changes like a new patio still go through Community Association Services on a separate track."),
        faq("Can I extend my patio toward the lake on my lot?",
            "Usually, as long as the extension stays on grade and ties into the existing slab. The lake frontage itself doesn't add a separate rule beyond the standard county and community review, but a CDD-maintained easement near the water's edge is worth checking before finalizing the layout."),
    ],
    "sources": SRC,
}

# 4. paver-patios ---------------------------------------------------------------
LOCAL["paver-patios"] = {
    "title": "Paver Patios in Lakewood Ranch, FL – Lake Lots",
    "meta": "Paver patios in Lakewood Ranch, FL: confirming the Sarasota-side permit question and building on a lake or golf-course lot, October 2026.",
    "h1": "Paver Patios for Lakewood Ranch Lake and Golf-Course Lots",
    "lede": capsule(f"A paver patio in Lakewood Ranch runs {price('paver-patio')} per {per('paver-patio')} as of October 2026. "
                     "On the Sarasota side of the community, the county's own building page doesn't name patios or pavers one way or the other, so confirming the permit question directly is part of the job on that side of the line."),
    "sections": [
        ("On the Sarasota side, call before you lay the base",
         f"<p>Sarasota County's Right-of-Way Use Permit covers work inside the county right-of-way, not a patio set back on private ground "
         f"({src('sarasota-county-row-permit', 'Sarasota County Code §124-48')}). A search summary of the county's own building page describes a residential patio without footings as possibly not needing a separate building permit, but the page couldn't be read in full to confirm it, so we treat that as a question for Planning & Development Services at 941-861-5000, not an answer "
         f"({src('sarasota-county-building-page', 'Sarasota County Building')}). On the Manatee side of the line, by contrast, a non-structural patio is confirmed on the county's own no-permit list.</p>"),
        ("Paver patios on a lake or golf-course lot",
         "<p>A lot of paver-patio work here goes in on a lot that backs onto one of the community's lakes or a golf-course fairway rather than a plain fence line, and that changes two things about the build: the edge restraint nearest the water or the course has to hold against irrigation overspray from the CDD's own common-area system, and the paver pattern often wraps around an existing drainage swale rather than running in a straight rectangle. Both are site-specific enough that a walk-through before pricing matters more here than on an interior lot.</p>"),
    ],
    "scenario": ("A paver patio on a golf-course lot, worked out in square feet",
                 f"<p>Say a 300 square foot paver patio extends a screened lanai toward a golf-course fairway on a Lakewood Ranch lot. At {price('paver-patio')} per {per('paver-patio')}, that runs $3,000 to $5,100, or roughly $3,600 to $4,800 in the typical {price('paver-patio', typical=True)} band depending on the paver size and pattern. Because the patio's outer edge sits close to the course's irrigation line, the edge restraint and joint sand get specified for regular overspray rather than the standard residential spec, and the layout is checked against any drainage swale the CDD maintains along that side of the lot before the base is cut.</p>"),
    "faqs": [
        faq("Does a paver patio need a permit on the Sarasota side of Lakewood Ranch?",
            "The county's published guidance doesn't say directly either way for a patio on private ground, so we confirm with Sarasota County Planning & Development Services at 941-861-5000 before pricing a job on that side of the community."),
        faq("Does backing onto a golf course change how a paver patio is built?",
            "It can. The edge restraint and joint sand closest to the course are worth specifying for regular irrigation overspray, and the layout gets checked against any drainage swale the CDD maintains along that property line."),
        faq("Do I need Community Association Services' approval for a paver patio?",
            f"A patio is the kind of exterior change the community's Modification Request Form covers, separate from either county's permit question. {post('lakewood-ranch-arc-approval-hardscape', 'Our Lakewood Ranch ARC guide')} covers the submission process.")
    ],
    "sources": SRC,
}

# 5. concrete-pool-decks -----------------------------------------------------
LOCAL["concrete-pool-decks"] = {
    "title": "Concrete Pool Decks in Lakewood Ranch, FL",
    "meta": "Concrete pool decks in Lakewood Ranch, FL: why most are first installs, and Manatee's 5-foot setback from a lot line or shoreline, Oct. 2026.",
    "h1": "Concrete Pool Decks for New-Build Lakewood Ranch Homes",
    "lede": capsule(f"A concrete pool deck in Lakewood Ranch runs {price('concrete-pool-deck')} per {per('concrete-pool-deck')} as of October 2026. "
                     "With a median home built in 2014, most pool decks here are a first install poured alongside the shell rather than a resurfacing job, and Manatee County sets a 5-foot setback from a lot line or shoreline for the deck itself."),
    "sections": [
        ("Why so many Lakewood Ranch pool decks are a first install",
         "<p>The community's newer housing stock means a pool deck here is more often part of a new build or a recent add-on pool than a replacement of something original to a decades-old home, a pattern that shows up less in the Sarasota unit's older towns. The deck's slope to the drains and its expansion joints at the coping still matter the same way on a new pour as on an older one; what changes is that the site visit is checking a shell contractor's layout rather than an existing deck's wear.</p>"),
        ("The county's 5-foot setback from a lot line or shoreline",
         f"<p>Manatee County's pool-code section sets single-family pool decks on grade at least 5 feet from any lot line or shoreline in the side or rear yard, and the same section states that a pool, cage, deck or patio isn't treated as a yard encroachment "
         f"({src('manatee-ldc-511.16-pool-decks', 'Manatee County LDC §511.16')}). On a lot that backs directly onto one of the community's lakes, that “shoreline” language is the number that decides how close the deck's edge can run to the water, not just the rear property line.</p>"),
    ],
    "scenario": ("A new pool deck on a lake lot, worked out in square feet",
                 f"<p>Say a new pool build on a lake-facing lot pours a 650 square foot deck around the shell. At {price('concrete-pool-deck')} per {per('concrete-pool-deck')}, that lands between $3,250 and $9,750, narrowing to roughly $4,550 to $7,800 in the typical {price('concrete-pool-deck', typical=True)} band depending on the finish. Because the lot backs onto the water, the deck's edge gets held back at least 5 feet from the shoreline under the county's pool-code setback, which on a narrower lake lot can be the dimension that sets how large the deck can actually be before the pool contractor even finalizes the shell's position.</p>"),
    "faqs": [
        faq("Why are most pool decks in Lakewood Ranch new rather than resurfaced?",
            "The community's median home was built in 2014, the newest in the Sarasota unit, so most pool decks are still close to their original pour rather than old enough to need resurfacing."),
        faq("How close to the water can a pool deck be built on a lake lot?",
            "Manatee County's pool-code section sets a 5-foot minimum from any lot line or shoreline in the side or rear yard for a pool deck on grade, which applies directly to lots backing onto one of the community's lakes."),
        faq("Does a pool deck count as a yard encroachment in Manatee County?",
            "No. The same county code section that sets the 5-foot setback also states that single-family pools, cages, decks and patios aren't considered a yard encroachment."),
    ],
    "sources": SRC,
}

# 6. pool-deck-pavers ---------------------------------------------------------
LOCAL["pool-deck-pavers"] = {
    "title": "Pool Deck Pavers in Lakewood Ranch, FL",
    "meta": "Pool deck pavers in Lakewood Ranch, FL go in on new pool builds more than as an overlay, with Manatee's setback rule, as of October 2026.",
    "h1": "Travertine and Paver Pool Decks in Lakewood Ranch",
    "lede": capsule(f"Pool deck pavers or travertine in Lakewood Ranch run {price('pool-deck-pavers')} per {per('pool-deck-pavers')} as of October 2026. "
                     "With most homes dating to 2014 or later, pavers and travertine here go in on a new pool build more often than as an overlay on a worn original deck, the pattern that dominates in the unit's older towns."),
    "sections": [
        ("A new build's pool deck is a specification decision, not a repair",
         f"<p>A deck poured and finished when the home is first built typically clears Community Association Services as part of the builder's original site plan for the lot, so choosing pavers or travertine at that stage is a design decision made once "
         f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}). Changing an existing deck's material or color later, on a resale or a renovation, is the kind of exterior change that goes back through a Modification Request Form, since it's no longer the plan the community already reviewed.</p>"),
        ("The same county setback applies whether the deck is poured or paved",
         "<p>Manatee County's 5-foot setback from a lot line or shoreline for a pool deck on grade doesn't change based on the surface material; a travertine or paver deck gets measured the same way a plain concrete one does. On a lake-facing lot, that means the paver layout, not just the pool shell, gets checked against the shoreline distance before the first course goes down.</p>"),
    ],
    "scenario": ("A new pool deck in travertine, worked out in square feet",
                 f"<p>Say a new pool build on a Lakewood Ranch lot specifies a 600 square foot travertine deck around the shell rather than plain concrete. At {price('pool-deck-pavers')} per {per('pool-deck-pavers')}, that runs $7,200 to $18,000, narrowing to roughly $8,400 to $13,200 in the typical {price('pool-deck-pavers', typical=True)} band depending on the stone and pattern. Because the material is specified at the same time as the pool permit, it typically moves through Community Association Services as part of the original site plan rather than as a separate Modification Request Form, which is not the case for a homeowner swapping an existing deck's surface years later.</p>"),
    "faqs": [
        faq("Is a paver pool deck more common as new construction or an overlay in Lakewood Ranch?",
            "New construction, more often than in the unit's older towns, since most homes here date to 2014 or later and their original pool decks haven't reached the point where an overlay makes more sense than keeping the existing surface."),
        faq("Does changing an existing pool deck to pavers need community approval?",
            "Yes, since it changes the material from what the builder's original site plan showed, which puts it back through a Modification Request Form with Community Association Services."),
        faq("Does the 5-foot setback apply to a travertine pool deck the same as concrete?",
            "Yes. Manatee County's pool-code setback from a lot line or shoreline applies to a pool deck on grade regardless of whether the surface is poured concrete, pavers or travertine."),
    ],
    "sources": SRC,
}

# 7. stamped-concrete ---------------------------------------------------------
LOCAL["stamped-concrete"] = {
    "title": "Stamped Concrete in Lakewood Ranch, FL – Color Rules",
    "meta": "Stamped concrete in Lakewood Ranch, FL: why integral color isn't the painting the community's manual prohibits, as of October 2026.",
    "h1": "Stamped Concrete Driveways and Walks in Lakewood Ranch",
    "lede": capsule(f"Stamped concrete in Lakewood Ranch runs {price('stamped-concrete')} per {per('stamped-concrete')} as of October 2026. "
                     "Country Club/Edgewater Village's own guidelines say painting a residential driveway or sidewalk isn't permitted, which makes it worth understanding why an integral color added during a stamped pour is a different method, not the same thing."),
    "sections": [
        ("Why stamped concrete's color isn't the “painting” the manual bans",
         f"<p>The Country Club/Edgewater Village homeowners' manual states plainly that painting residential driveways and sidewalks is not permitted "
         f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}). Stamped concrete gets its color a different way: an integral pigment mixed into the concrete itself, plus a release agent used during the stamping, rather than a coating applied to an existing surface afterward. Because the rule as published targets painting specifically, a stamped or colored pour is worth confirming with your own village's committee before ordering materials, since the manual's wording addresses CEVA directly and other villages may read it differently.</p>"),
        ("A young driveway is a candidate for a design upgrade, not a repair",
         f"<p>Because most Lakewood Ranch driveways and entry walks are still close to a builder's original plain-gray pour, stamped concrete work here tends to be a style upgrade on sound concrete rather than a resurfacing job covering up cracking. Changing the material from plain to stamped is the kind of driveway change the community flags for a Modification Request Form the same way a plain-to-paver conversion is "
         f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}). {svc('concrete-repair', 'Concrete repair and resurfacing')} covers the separate case of an older slab that actually needs patching first.</p>"),
    ],
    "scenario": ("A stamped entry walk and driveway accent, worked out in square feet",
                 f"<p>Say a homeowner adds a slate-pattern stamped finish and an integral color to a 320 square foot entry walk and driveway apron on a home built in the mid-2010s. At {price('stamped-concrete')} per {per('stamped-concrete')}, that runs $2,560 to $6,080, or roughly $3,840 to $5,120 in the typical {price('stamped-concrete', typical=True)} band depending on the number of colors and the release agent. Before the pour, the pattern and color go to Community Association Services as a material change, and the owner confirms with the village's committee that the integral color reads as a stamped finish rather than the kind of painting the manual addresses separately.</p>"),
    "faqs": [
        faq("Can I paint a stamped concrete driveway in Lakewood Ranch?",
            "Country Club/Edgewater Village's guidelines say painting a residential driveway isn't permitted there, so a stamped finish's color has to come from integral pigment and a release agent added during the pour, not a coating applied afterward."),
        faq("Does a plain-to-stamped conversion need community approval?",
            "Yes, changing the material or finish of an existing driveway is the kind of exterior change the community reviews through a Modification Request Form, the same way a plain-to-paver conversion is."),
        faq("Does this painting rule apply across all of Lakewood Ranch?",
            "The published wording is specific to Country Club/Edgewater Village's own manual. Other villages may handle the same question differently, so confirming with your address's own committee is worth doing before assuming the rule applies community-wide."),
    ],
    "sources": SRC,
}

# 8. concrete-walkways --------------------------------------------------------
LOCAL["concrete-walkways"] = {
    "title": "Concrete Walkways in Lakewood Ranch, FL",
    "meta": "Concrete walkways in Lakewood Ranch, FL: why homeowners can't repair the public sidewalk themselves, and the driveway-crossing spec, Oct. 2026.",
    "h1": "Concrete Sidewalks and Walkways in Lakewood Ranch",
    "lede": capsule(f"A concrete walkway in Lakewood Ranch runs {price('concrete-walkway')} per {per('concrete-walkway')} as of October 2026. "
                     "The community's manual makes a point of saying public sidewalk repairs aren't something a homeowner does on their own, and the sidewalk section that crosses a Manatee-side driveway has to meet its own thickness and width spec."),
    "sections": [
        ("The public sidewalk isn't a homeowner repair, even when it cracks in front of your house",
         f"<p>Lakewood Ranch's homeowners' manual states that public sidewalk repairs are not permitted by the homeowner "
         f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}), which is a narrower rule than it sounds: it covers the public sidewalk strip itself, not a private front walkway running from the driveway to the door, which is the kind of walkway work we price and build. A cracked public sidewalk segment is worth reporting to the CDD or the county rather than patched by a contractor hired independently.</p>"),
        ("What a sidewalk crossing a Manatee-side driveway has to meet",
         f"<p>Where a concrete sidewalk crosses a driveway on the Manatee County side, it has to be 4 inches thick and 5 feet wide, framed from side lot line to side lot line, finished with a broom texture, and saw-cut every 10 feet "
         f"({src('manatee-paver-driveway-inspections', 'Manatee County, Inspections Required for Paver Driveways')}). That's a different, thinner spec than the driveway slab on either side of it, which is why the crossing section gets poured and jointed as its own piece rather than as a continuation of the driveway.</p>"),
    ],
    "scenario": ("A front walkway replacement, worked out in square feet",
                 f"<p>Say a 4 by 50 foot front walkway, 200 square feet, connects the driveway to the entry on a home built in the mid-2010s. At {price('concrete-walkway')} per {per('concrete-walkway')}, that runs $1,400 to $3,400, or roughly $1,600 to $2,400 in the typical {price('concrete-walkway', typical=True)} band for a broom-finished walk. Where that walk crosses the driveway near the street on the Manatee side, the crossing section gets built to the county's 4-inch, 5-foot sidewalk spec with saw cuts every 10 feet rather than matched to the driveway's own thickness.</p>"),
    "faqs": [
        faq("Can I repair a cracked public sidewalk myself in Lakewood Ranch?",
            "No. The community's manual states that public sidewalk repairs aren't permitted by the homeowner; that section is reported through the CDD or the county rather than fixed independently."),
        faq("What thickness does a sidewalk crossing a driveway need on the Manatee side?",
            "4 inches thick and 5 feet wide, framed from side lot line to side lot line, broom finished, with saw cuts every 10 feet, under Manatee County's paver-driveway inspection spec, which applies to the concrete crossing as well."),
        faq("Does a private front walkway need the same permit as the public sidewalk?",
            "No, a walkway that stays on private ground between the driveway and the entry isn't the public sidewalk segment the manual addresses, though it still goes through whichever county permit and community review the project otherwise needs."),
    ],
    "sources": SRC,
}

# 9. concrete-slabs ------------------------------------------------------------
LOCAL["concrete-slabs"] = {
    "title": "Concrete Slabs in Lakewood Ranch, FL – Sheds & Pads",
    "meta": "Concrete slabs in Lakewood Ranch, FL: what Manatee's no-permit list exempts for a shed or AC pad, as of October 2026.",
    "h1": "Concrete Slabs for Sheds, AC Pads and Parking in Lakewood Ranch",
    "lede": capsule(f"Pricing a slab for a shed, an AC pad or a parking pad in Lakewood Ranch starts at {price('concrete-slab')} per {per('concrete-slab')}, current as of October 2026. "
                     "Manatee County's no-permit list draws a specific line between a small detached deck and a slab poured with footers, which is the first thing worth checking before pricing a pad."),
    "sections": [
        ("What Manatee's no-permit list actually exempts",
         f"<p>A detached deck under 30 inches high and under 120 square feet is exempt from a building permit on the county's current no-permit list, while every attached deck needs one, and a concrete slab poured with footers requires a permit regardless of size "
         f"({src('manatee-no-permit-list', 'Manatee County, What Does Not Require a Permit')}). A plain slab-on-grade for a shed or an AC pad, without footers, is the kind of scope that falls closer to the exempt side of that line, though confirming the specific footprint against the current list is worth a call before concrete is ordered.</p>"),
        ("New-build lots still need a slab sized to current equipment",
         "<p>Because most Lakewood Ranch homes date to the 2010s, the original builder AC pad was sized for equipment that's often smaller than a current replacement heat pump, so a slab swap is as much a resizing job as a repour. A shed slab on a lake or golf-course lot also gets checked against where the CDD maintains drainage along that property line before the pad's location is finalized.</p>"),
    ],
    "scenario": ("A shed slab, worked out in square feet",
                 f"<p>Say a homeowner pours an 8 by 10 foot shed slab, 80 square feet, on the side yard of a home built around 2016. At {price('concrete-slab')} per {per('concrete-slab')}, that runs $320 to $800, or roughly $480 to $640 at the typical {price('concrete-slab', typical=True)} rate, a 4-inch pour over a base compacted in advance. Because the slab is a plain pad without footers and under the county's detached-structure size threshold, it's a candidate for the no-permit exemption, though the final check against the current list and against any CDD drainage easement along that side of the lot still happens before the forms go up.</p>"),
    "faqs": [
        faq("Does a small shed slab need a permit in Lakewood Ranch?",
            "On the Manatee side, a detached deck or structure under 30 inches high and under 120 square feet is exempt from the county's no-permit list, while a concrete slab poured with footers needs a permit regardless of size. Confirm the specific footprint against the current list first."),
        faq("Can I pour a bigger AC pad than the original builder slab?",
            "Yes, and it's common on homes from the mid-2010s, since current equipment often needs a larger footprint than the original unit. The new pad's size is checked against the no-permit threshold the same as any other slab."),
        faq("Does a shed slab on a lake lot need extra checks?",
            "Often, since the CDD maintains drainage along some lake-facing property lines. We confirm the shed's placement against any drainage easement before pricing the slab on a lot like that."),
    ],
    "sources": SRC,
}

# 10. concrete-repair ----------------------------------------------------------
LOCAL["concrete-repair"] = {
    "title": "Concrete Repair in Lakewood Ranch, FL – New Homes",
    "meta": "Concrete repair in Lakewood Ranch, FL: why cracking here traces to new-construction settlement more than age, plus the overlay review, Oct. 2026.",
    "h1": "Concrete Repair and Resurfacing in Lakewood Ranch",
    "lede": capsule(f"Patching or resurfacing a cracked slab in Lakewood Ranch costs {price('concrete-repair')} per {per('concrete-repair')}, current as of October 2026. "
                     "With a median home built in 2014, cracking here traces more often to new-construction fill settlement or a utility trench than to decades of ordinary wear, and a resurfacing overlay still goes through the community's own review."),
    "sections": [
        ("Why concrete repair looks different in a community built mostly after 2010",
         "<p>A driveway cracking in a town where the median home was built in 1976 or 1992 usually points to joint fatigue or a root working under the slab after decades of exposure. In Lakewood Ranch, with a 2014 median build year, the more common cause is a settling fill section near a retention pond's edge, or a utility or irrigation trench cut across the driveway after the original pour, both of which can crack a young slab well before age alone would.</p>"),
        ("A concrete overlay still needs the community's sign-off",
         f"<p>Country Club/Edgewater Village's manual treats a concrete overlay resurfacing technique as its own category, requiring a Modification Request Form and stating that it has to be applied by a professional "
         f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}). That review applies whether the overlay is covering ordinary wear or a crack traced to a trench, so the same paperwork step comes before the resurfacing crew starts either way.</p>"),
    ],
    "scenario": ("Resurfacing a cracked section near a utility trench, worked out in square feet",
                 f"<p>Say a 350 square foot section of driveway shows diagonal cracking along the line where an irrigation trench was cut after the original pour. At {price('concrete-repair')} per {per('concrete-repair')} for resurfacing, that runs $1,050 to $3,500, or roughly $1,400 to $2,450 at the typical {price('concrete-repair', typical=True)} rate, the lower end for a plain overlay and the higher end once a decorative finish is folded into the same visit. Because the overlay technique is its own category under the village's manual, the Modification Request Form clears before the resurfacing crew starts, the same step a stamped or paver conversion would need.</p>"),
    "faqs": [
        faq("Why would a driveway crack in a community built mostly after 2010?",
            "Settling fill near a retention pond's edge or a utility trench cut across the slab after the original pour are more common causes here than age-related joint fatigue, which is the typical cause in the unit's older towns."),
        faq("Does resurfacing a driveway need community approval in Lakewood Ranch?",
            "Yes, Country Club/Edgewater Village's manual treats a concrete overlay as its own category requiring a Modification Request Form, applied by a professional, separate from whether the county's building permit is involved."),
        faq("Is a crack from a utility trench repaired differently than ordinary wear?",
            "The resurfacing technique is usually the same either way, an overlay or a patch sized to the affected section, but tracing the crack back to the trench first helps decide whether the trench itself needs re-compacting before the surface repair goes on."),
    ],
    "sources": SRC,
}

# 11. paver-sealing -------------------------------------------------------------
LOCAL["paver-sealing"] = {
    "title": "Paver Sealing in Lakewood Ranch, FL – Approved Colors",
    "meta": "Paver and driveway sealing in Lakewood Ranch, FL: the community's approved sealer colors and its Modification Request Form, as of October 2026.",
    "h1": "Paver and Driveway Sealing in Lakewood Ranch",
    "lede": capsule(f"Sealing a driveway or paver surface in Lakewood Ranch runs {price('paver-sealing')} per {per('paver-sealing')} as of October 2026. "
                     "Country Club/Edgewater Village's manual requires a Modification Request Form for sealing a residential driveway or walkway and lists specific approved colors, a step worth planning before the cleaning crew even shows up."),
    "sections": [
        ("Sealing needs its own form, with a published list of approved colors",
         f"<p>The Country Club/Edgewater Village homeowners' manual states that sealing a concrete residential driveway or walkway requires a Modification Request Form submitted to and approved by the village, and it lists specific approved sealer colors, Sherwin-Williams Silverplate SW7649, Gray Clouds SW7658 and Amazing Gray SW7044 among them "
         f"({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual 2022')}). Picking from that published list before the job is scheduled avoids a resubmission after the fact.</p>"),
        ("Sealing day doesn't depend on the region's watering calendar",
         f"<p>The Southwest Florida Water Management District's current Modified Phase III order limits irrigation to one day a week, through March 2027, by the last digit of the street address "
         f"({src('swfwmd-restrictions', 'SWFWMD District Water Restrictions')}; {src('manatee-phase3', 'Manatee County, Modified Phase III water shortage restrictions')}). Those restrictions govern lawn irrigation, not a hose-fed pressure washer cleaning a driveway before sealing, so the cleaning and re-sanding steps get scheduled around the weather and the approved-color paperwork, not an address's watering day.</p>"),
    ],
    "scenario": ("Sealing a driveway in an approved color, worked out in square feet",
                 f"<p>Say a 440 square foot concrete driveway gets a full clean, crack check and seal in one of the village's approved colors. At {price('paver-sealing')} per {per('paver-sealing')}, that lands between $660 and $1,430, or roughly $788 to $1,238 in the typical {price('paver-sealing', typical=True)} band depending on prep work. Because sealing is its own line item in the village's manual, the Modification Request Form naming the specific approved color goes in before the job is scheduled, which is a step a lot of first-time sealing jobs on these young, still-original driveways haven't gone through before.</p>"),
    "faqs": [
        faq("Do I need approval to reseal my driveway in Lakewood Ranch?",
            "In Country Club/Edgewater Village, yes, the manual requires a Modification Request Form for sealing a concrete residential driveway or walkway, submitted before the work starts."),
        faq("What sealer colors are approved in Lakewood Ranch?",
            "Country Club/Edgewater Village's manual lists specific approved colors, including Sherwin-Williams Silverplate SW7649, Gray Clouds SW7658 and Amazing Gray SW7044. Picking from that list before the job avoids a resubmission."),
        faq("Does the watering restriction affect pressure washing before sealing?",
            "No. SWFWMD's current restrictions govern lawn irrigation, not a hose-fed pressure washer used to clean a driveway or paver surface before sealing."),
    ],
    "sources": SRC,
}

# 12. retaining-walls -----------------------------------------------------------
LOCAL["retaining-walls"] = {
    "title": "Retaining Walls in Lakewood Ranch, FL",
    "meta": "Retaining walls in Lakewood Ranch, FL: Sarasota County's 4-foot engineering line and Manatee's any-height masonry permit, as of October 2026.",
    "h1": "Retaining Walls for Lakewood Ranch Lake and Golf-Course Lots",
    "lede": capsule(f"A retaining wall in Lakewood Ranch runs {price('retaining-wall')} per {per('retaining-wall')}, current as of October 2026. "
                     "On the Sarasota side of the community, a wall over 4 feet needs engineered drawings; on the Manatee side, any masonry wall needs a permit regardless of height, a difference worth knowing before a lot that steps down to a lake or a fairway gets designed."),
    "sections": [
        ("A four-foot line that matters only on the Sarasota side",
         f"<p>In unincorporated Sarasota County, a 1994-era pool-code provision still sets the engineering trigger for a retaining wall: past 4 feet tall at any point, the design needs a sealed drawing before the county permit clears "
         f"({src('sarasota-county-22-63-retaining-walls', 'Sarasota County Code §22-63')}). Below that mark, a segmental block wall can typically move forward on the standard permit, no engineer required. That threshold applies on the Sarasota side of Lakewood Ranch specifically, not the Manatee side, where the rule works differently.</p>"),
        ("On the Manatee side, any masonry wall needs a permit",
         f"<p>Manatee County's current no-permit list names masonry fences, walls and columns as work that does need a permit, with no separate height threshold published for a retaining wall specifically "
         f"({src('manatee-no-permit-list', 'Manatee County, What Does Not Require a Permit')}). On a lot that steps down to one of the community's lakes or a golf-course fairway, a seat wall or a low retaining wall is as often a landscape feature holding a slope as it is a structural necessity, but either way it needs that county permit before work starts.</p>"),
    ],
    "scenario": ("A seat wall on a sloped lake lot, worked out in square feet",
                 f"<p>Say a sloped lot backing onto one of the community's lakes needs a 40 linear foot segmental block wall, 3 feet tall, 120 square feet of wall face. At {price('retaining-wall')} per {per('retaining-wall')}, that lands between $1,800 and $4,800, narrowing to roughly $2,400 to $4,200 at the typical {price('retaining-wall', typical=True)} rate, before drainage behind the wall is figured in. Because the wall stays under Sarasota County's 4-foot engineering threshold, it's less likely to need a sealed drawing there than a taller wall would, though on the Manatee side of the line the same wall still needs its own masonry permit regardless of that height.</p>"),
    "faqs": [
        faq("At what height does a retaining wall need an engineer in Lakewood Ranch?",
            "On the Sarasota County side, 4 feet is the published threshold for engineered drawings. On the Manatee County side, no separate height threshold was published; any masonry wall needs a permit regardless of height."),
        faq("Do I need a permit for a low seat wall on a lake lot?",
            "On the Manatee side, yes, masonry fences, walls and columns are on the county's permit-required list with no height exemption. On the Sarasota side, the wall still needs sign-off, with engineered drawings required only above 4 feet."),
        faq("Does Community Association Services review retaining walls too?",
            f"A wall built to manage a sloped lake or golf-course lot is the kind of landscape change the community's design review covers. {post('lakewood-ranch-arc-approval-hardscape', 'Our Lakewood Ranch ARC guide')} covers the submission process for exterior changes generally."),
    ],
    "sources": SRC,
}

# 13. artificial-turf ------------------------------------------------------------
LOCAL["artificial-turf"] = {
    "title": "Artificial Turf in Lakewood Ranch, FL – Lake Setbacks",
    "meta": "Artificial turf in Lakewood Ranch, FL: the state's 10-foot water-body setback for lake and golf-course lots, as of October 2026.",
    "h1": "Artificial Turf for Lakewood Ranch Lake and Golf-Course Lots",
    "lede": capsule(f"Artificial turf in Lakewood Ranch runs {price('artificial-turf')} per {per('artificial-turf')} as of October 2026. "
                     "On a lot that backs onto one of the community's lakes or a golf-course pond, the state's 2026 turf rule keeps synthetic turf at least 10 feet from the water unless it backs onto a seawall, a setback worth measuring before a layout is drawn."),
    "sections": [
        ("The state's 10-foot rule for a lake or pond lot",
         f"<p>Florida's turf standard, effective May 19, 2026, requires synthetic turf to stay at least 10 feet from a water body unless the lot backs onto a seawall, bars in-ground irrigation under the turf itself, and calls for natural infill and a washed base "
         f"({src('dep-rule', 'DEP Rule 62-308.100')}). On a lot where the rear yard runs right up to one of Lakewood Ranch's stormwater lakes, that 10-foot line, not the property line itself, is usually what decides how far back the turf can start.</p>"),
        ("What the community's committee can and can't say about turf",
         f"<p>As of 2026, an HOA can restrict turf only where it's visible from the lot's frontage or an adjoining parcel, under a state law change that protects turf tucked into a screened or fenced backyard regardless of what a community's declaration says "
         f"({src('fs720-3045', 'F.S. 720.3045')}). A 2025 state law otherwise limits how far a local government, not an HOA, can go in regulating residential turf "
         f"({src('fs125572', 'F.S. 125.572')}). Turf is still the kind of exterior change Community Association Services reviews on its own track, separate from either statute.</p>"),
    ],
    "scenario": ("Backyard turf on a lake lot, worked out in square feet",
                 f"<p>Say a 600 square foot backyard replaces a struggling lawn with artificial turf on a lot where the rear yard slopes down to one of the community's lakes. At {price('artificial-turf')} per {per('artificial-turf')}, that lands between $6,000 and $15,000, narrowing to roughly $7,200 to $10,800 in the typical {price('artificial-turf', typical=True)} band depending on the pile height and backing. Because the lot backs onto open water rather than a seawall, the turf's edge has to stay at least 10 feet from the water under the state's 2026 rule, which on a lot with a narrow setback can mean the usable turf area is smaller than the full 600 square feet originally measured.</p>"),
    "faqs": [
        faq("How close to a lake can artificial turf be installed in Lakewood Ranch?",
            "At least 10 feet, under the state's 2026 turf rule, unless the lot backs onto a seawall rather than open water. That setback is measured before the turf layout is finalized."),
        faq("Can my village's committee ban artificial turf entirely?",
            "As of 2026, an HOA can only restrict turf that's visible from the lot's frontage or an adjoining parcel, under F.S. 720.3045, which protects turf in a screened or fenced backyard regardless of the declaration's wording."),
        faq("Does artificial turf still need Community Association Services' approval?",
            f"Yes, it's the kind of exterior and landscape change the community reviews separately from the state's turf statute. {post('florida-hoa-artificial-turf-law', 'Our Florida HOA artificial-turf law guide')} covers what the HOA can and can't require."),
    ],
    "sources": SRC,
}


def get_pages():
    return [HUB] + cityservice_pages(SLUG, LOCAL)
