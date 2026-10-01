# -*- coding: utf-8 -*-
"""Blog posts, group e: permits in Manatee County, HOA/ARC approval for hardscape (general and Lakewood Ranch),
the Florida HOA artificial-turf law, driveway apron/right-of-way ownership, and driveway widening/extensions."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, cs, post, compare, src, ext, price, per, contact, photo


def p_manatee_county_driveway_permits():
    body = "".join([
        sec("Do you need a permit for a driveway in unincorporated Manatee County?",
            "<p>Yes. Manatee County's land development code treats any part of a driveway that reaches from your property line out to the "
            f"roadway as work in the right-of-way, and that requires an access and drainage permit before a crew touches it. The county's code "
            "defines \"driveway\" broadly for this purpose, covering the sidewalk crossing, culvert, drainage structure, swale and apron, not just "
            f"the paved surface itself ({src('manatee-driveway-application', 'Manatee County LDC §1004.2')}). A {svc('concrete-driveways', 'new concrete driveway')} "
            f"or a {svc('paver-driveways', 'paver driveway')} both fall under this permit the moment any part of the job sits between the property "
            "line and the pavement edge; only \"regular driveway maintenance\" is exempt, and the county doesn't spell out exactly where cleaning "
            "or resealing ends and reconstruction begins, so it's worth a quick call before assuming a resurfacing job is maintenance.</p>"),
        sec("How do you apply, and what does the county expect to see?",
            "<p>The Driveway/Culvert permit runs through Public Works' Infrastructure Engineering Division, applied for in the county's Accela "
            "portal under Building, then Public Works, then Driveway/Culvert. Residential building and development questions route through "
            "Development Services at 1112 Manatee Ave W, 941-749-3047, or the county's general line, 311 (311@mymanatee.org, Monday through "
            f"Friday 7:30 to 3:30) ({src('manatee-driveway-application', 'Manatee, Request a Driveway or Culvert Permit')}). The application itself "
            "sets the construction spec, not just the paperwork:</p>"
            + table("Manatee County residential driveway specs (unincorporated)", ["Element", "Requirement"],
                    [["Width", "12 ft minimum, 24 ft maximum; up to 30 ft for a street-facing three-car garage"],
                     ["Thickness to the right-of-way line", "6 in, from the edge of pavement to the right-of-way"],
                     ["Joint at the curb", "Expansion joint between the curb and the concrete drive"],
                     ["Clearances", "At least 3 ft from catch basins and 3 ft from the mitered ends of a culvert"],
                     ["Curb removal", "Type \"F\" curb removed within the width of the drive"],
                     ["Shell aprons", "Not allowed next to a paved roadway"]],
                    f"From the county's Driveway and Culvert Application ({src('manatee-driveway-application', 'full form, PDF')})."
                    )),
        sec("What's different for a paver driveway in Manatee County?",
            "<p>A paver driveway gets its own inspection sequence rather than a simple sign-off, because the county checks the base before the "
            "surface goes down. The subgrade is cut 6 inches deep so the compacted sub-base plus the pavers come out flush with that 6-inch depth, "
            "the same width rule applies (12 ft minimum, 24 ft maximum, 30 ft for a street-facing three-car garage), and flares at the roadway add "
            "3 ft on each side over an 8-ft run. Where a concrete sidewalk crosses the driveway, that section has to be 4 inches thick and 5 feet "
            "wide, framed from one side lot line to the other, broom-finished, with saw cuts every 10 feet "
            f"({src('manatee-driveway-application', 'Manatee, Inspections Required for Paver Driveways')}).</p>"),
        sec("Does a patio, pool deck or slab need a permit on a Manatee County lot?",
            "<p>Often not, if the work stays non-structural. The county's current \"What Does Not Require a Permit\" list, updated June 16, 2026, "
            f"puts a non-structural concrete or paver patio in the no-permit column ({src('manatee-no-permit-list', 'Manatee, What Does Not Require a Permit, 6-16-26')}). "
            "A concrete slab poured with footers and any swimming pool still need one, and a detached deck is only exempt below 30 inches high and "
            "120 square feet; every attached deck needs a permit regardless of size. The county's pool code also sets a minimum setback for a deck "
            "built on grade next to a single-family pool or screen enclosure: a 5-foot clearance from the side or rear property line, or from the "
            f"shoreline, without that distance counting against the lot's required yard space ({src('manatee-no-permit-list', 'Manatee County LDC §511.16')}). "
            f"{svc('pool-deck-pavers', 'Pool deck pavers')} "
            "built on grade generally fall under that same deck language, though the county's no-permit page doesn't name pavers specifically, so "
            "it's worth confirming a travertine or paver deck's exact footing before you assume the exemption applies.</p>"),
        sec("Bradenton runs a separate process from the county",
            "<p>Once you cross into the City of Bradenton, the county rules above don't apply; the city has its own land use regulations for "
            "the same work. A curb cut needs the public works director's review, and if the street is a county or state road, that agency signs "
            "off too. Homes with up to six units get one driveway per street frontage, a single access point tops out at 24 feet wide, and a "
            f"circular drive is capped at 12 feet per curb cut with at least 25 feet between the two cuts ({src('bradenton-lur-4.1-access-sidewalks', 'Bradenton LUR §4.1')}). "
            "Building, altering or paving any \"street, driveway, access road, or parking area\" also needs a zoning permit with a scaled site plan "
            f"before work starts ({src('bradenton-lur-2.2-zoning-permit', 'Bradenton LUR §2.2')}), and driveway or sidewalk work in the public "
            "right-of-way needs a signed Driveway/Sidewalk Affidavit filed with Public Works & Utilities, 1411 9th St W, where you agree to maintain "
            f"the work and move it at your own cost if the city asks ({src('bradenton-driveway-affidavit', 'Bradenton Driveway Affidavit, 2024')}).</p>"
            + table("Bradenton impervious surface limit by zoning district", ["District", "Maximum impervious coverage"],
                    [["R-1", "50%"], ["R-2", "60%"], ["R-3, UV, R-4", "70%"]],
                    f"Counts building footprint, paved drives and terraces, pool decks and other hard surfaces; a worksheet is available from the city ({src('bradenton-lur-3.2-isr', 'Bradenton LUR §3.2')}).")),
        sec("Palmetto requires a permit for the driveway and for any retaining wall, at any height",
            "<p>Palmetto's code is blunt about the right-of-way: it's unlawful for a contractor to place or build culverts, driveways, curbs or "
            f"sidewalks within any public street or right-of-way until Public Works issues a written permit ({ext('https://library.municode.com/fl/palmetto/codes/code_of_ordinances?nodeId=CD_ORD_CH25STSIOTPUPL_ARTIINGE_S25-2PEREUSSTRI-W', 'Palmetto Code §25-2')}). "
            "The Right-of-Way Use Application wants 48 hours' notice before you start, work beginning within 60 days of issue and finishing within "
            f"30 ({ext('https://www.palmettofl.org/DocumentCenter/View/117/Right-of-Way-Permit-PDF', 'Palmetto ROW Use Permit application')}). Retaining walls get their own, separate rule: "
            "it's unlawful to \"construct, alter, repair, remove or demolish any seawall, retaining wall or bulkhead\" without a permit, regardless "
            f"of the wall's height, and the fee runs $10 plus $0.10 per linear foot ({ext('https://library.municode.com/fl/palmetto/codes/code_of_ordinances?nodeId=CD_ORD_CH10COARWA_ARTIISE_DIV2PE_S10-46RE', 'Palmetto Code §10-46')}). "
            "For a patio, pool deck or pavers on your own lot, Palmetto's Building Department page doesn't give a specific exemption; staff told us "
            "to call ahead when it's unclear, so a 941-721-2166 call before you design around \"no permit needed\" saves a redo "
            f"({ext('https://www.palmettofl.org/79/Building-Department', 'Palmetto Building Department')}).</p>"),
        sec("Parrish and the Manatee side of Lakewood Ranch",
            f"<p>Both {city('parrish')} and the Manatee County portion of {city('lakewood-ranch')} sit in unincorporated Manatee County, so the "
            "driveway, patio and paver rules above apply the same way they do anywhere else outside a city line: an access and drainage permit for "
            "anything touching the right-of-way, and a non-structural patio generally exempt. Lakewood Ranch adds a second layer on top of the "
            f"county permit, a community Modifications Committee review that most of the right-of-way rules above don't replace; "
            f"{post('lakewood-ranch-arc-approval-hardscape', 'our Lakewood Ranch ARC guide')} walks through that process and what it requires before "
            "a driveway is sealed, resurfaced or changed to a different material.</p>"),
        sec("What this looks like for a real project",
            "<p>Say a homeowner in a 1980s Bradenton subdivision wants to replace a cracked 10 by 20 ft concrete driveway with pavers and add a "
            "small patio off the back door. The driveway falls under the City of Bradenton's zoning permit and the driveway/sidewalk affidavit, "
            "plus the public works director's sign-off on the curb cut, since it touches the right-of-way at the street. The patio, if it's on "
            "grade without footers, likely needs only the zoning review tied to the city's impervious-surface limit, not a separate building permit. "
            "If the same project sat a few miles east in unincorporated Parrish instead, the driveway would go through the county's Driveway/Culvert "
            "permit and the patio would likely be exempt outright under the county's non-structural patio rule. Two different departments, two "
            "different forms, for jobs that look identical from the curb.</p>"
            + table("Who to call, Manatee County jurisdictions", ["Jurisdiction", "Driveway / apron", "Patio or pavers on your lot", "Contact"],
                    [["Unincorporated county (Parrish, Myakka City, Manatee side of Lakewood Ranch)", "Access and drainage permit, LDC §1004.2", "Non-structural patio exempt; slab with footers or a pool needs a permit", "311 / 311@mymanatee.org"],
                     ["City of Bradenton", "Public works director review and driveway/sidewalk affidavit", "Zoning permit for any paved area", "941-932-9414"],
                     ["City of Palmetto", "Public Works right-of-way permit", "Not specifically addressed; call ahead", "941-721-2166"]],
                    "Summaries of each department's published rules, checked October 2026; confirm specifics with the office before work starts.")
            + (photo("concrete-driveway-two-car", "Two-car concrete driveway in front of a house with two garage doors") or "")),
    ])
    faqs = [faq("Does a non-structural patio need a permit in Manatee County?",
                 "Not in unincorporated Manatee County, where the current no-permit list exempts a non-structural concrete or paver patio. A concrete slab poured with footers, a swimming pool, or an attached deck of any size still needs one, and Bradenton and Palmetto don't publish the same exemption, so confirm with the city if your lot isn't in the unincorporated county."),
            faq("How wide can a residential driveway be in Manatee County?",
                 "The county's Driveway and Culvert Application sets 12 feet as the minimum and 24 feet as the maximum, except for a street-facing three-car garage, which can go up to 30 feet. Bradenton caps a single access point at 24 feet and limits circular drives to 12 feet per curb cut."),
            faq("Do I need a permit to build a retaining wall in Palmetto?",
                 "Yes, at any height. Palmetto's code requires a permit to construct, alter, repair or demolish a retaining wall regardless of how tall it is, which is stricter than Sarasota County's rule of engineered drawings only above 4 feet. The fee is $10 plus $0.10 per linear foot."),
            faq("Is Lakewood Ranch handled differently from the rest of Manatee County?",
                 "The county permit layer is the same, split between Manatee County or Sarasota County depending on which side of the community line a home sits. Lakewood Ranch adds a community Modifications Committee review on top of that, covering things like driveway sealing and material changes that the county permit doesn't touch.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/paver-driveways/", "Paver driveways"),
               ("/permits/", "Permits & HOA hub"), ("/blog/lakewood-ranch-arc-approval-hardscape/", "Lakewood Ranch ARC approval"),
               ("/blog/driveway-apron-and-right-of-way-florida/", "Who owns the driveway apron")]
    return page("/blog/manatee-county-driveway-permits/", "post", "Manatee County Driveway Permit Guide (2026)",
                "Driveway, patio and paver permit rules for unincorporated Manatee County, Bradenton and Palmetto, with widths, thickness and contacts, as of October 2026.",
                "Driveway and Patio Permits in Bradenton, Lakewood Ranch, Parrish and Palmetto (Manatee County)",
                capsule("In unincorporated Manatee County, a driveway touching the right-of-way needs an access and drainage permit and must run "
                        "12 to 24 feet wide and 6 inches thick at the right-of-way line, while a non-structural concrete or paver patio does not "
                        "need one. As of October 2026, Bradenton and Palmetto each run their own separate permit process for the same kind of work."),
                body, faqs=faqs,
                sources=["manatee-driveway-application", "manatee-no-permit-list", "bradenton-lur-4.1-access-sidewalks", "bradenton-lur-2.2-zoning-permit",
                         "bradenton-lur-3.2-isr", "bradenton-driveway-affidavit",
                         ("Palmetto Code §25-2, right-of-way permit required", "https://library.municode.com/fl/palmetto/codes/code_of_ordinances?nodeId=CD_ORD_CH25STSIOTPUPL_ARTIINGE_S25-2PEREUSSTRI-W"),
                         ("Palmetto Code §10-46, retaining wall permit", "https://library.municode.com/fl/palmetto/codes/code_of_ordinances?nodeId=CD_ORD_CH10COARWA_ARTIISE_DIV2PE_S10-46RE"),
                         ("Palmetto Right-of-Way Use Permit application", "https://www.palmettofl.org/DocumentCenter/View/117/Right-of-Way-Permit-PDF"),
                         ("Palmetto Building Department", "https://www.palmettofl.org/79/Building-Department")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image="concrete-driveway-two-car", form=False)


def p_hoa_approval_for_pavers_and_concrete():
    body = "".join([
        sec("How do I get HOA approval for a paver driveway?",
            "<p>Submit an architectural or modification review application before any work starts, not after, including a site plan, the exact "
            "material and color you're installing, and any dimensions the committee needs to check against the community's rules. Florida law "
            "limits what an HOA can require: its power to approve the \"location, size, type, or appearance\" of an improvement exists only to the "
            "extent the declaration or published guidelines specifically state or reasonably imply, and the board has to apply that authority "
            f"reasonably and equitably rather than case by case on a whim ({src('fs720-3035', 'F.S. 720.3035')}). The same statute doesn't mention "
            f"pavers, driveways or pool decks by name, which means the real rulebook for a {svc('paver-driveways', 'paver driveway')}, a "
            f"{svc('concrete-driveways', 'concrete driveway')} or a {svc('pool-deck-pavers', 'paver pool deck')} is whatever your community's own "
            "declaration and design guidelines say, not a state-mandated checklist.</p>"),
        sec("What can an HOA actually control, and what can't it?",
            "<p>An HOA's reach is tied directly to its own documents, so the honest answer to \"can they say no\" starts with reading the "
            "declaration rather than guessing at state law. If the governing documents list specific material or design options, for example "
            "a set of approved paver colors, the association can't restrict your choice to one option off that list once it's published "
            f"({src('fs720-3035', 'F.S. 720.3035')}). A change that took effect in the 2026 statutes also closed off one common delay tactic: an "
            "HOA can no longer make a government building permit a condition of reviewing your application in the first place, so a board that "
            "tells you to \"get your permit first, then we'll look at it\" is asking for something the law no longer lets it require. That doesn't "
            "flip the order the other way either; you still need the city or county permit covered in our "
            f"{a('/permits/', 'permits and HOA hub')} before work actually begins, the association just can't use it as a gate to reviewing the "
            "design itself.</p>"),
        sec("What happens if the HOA denies a driveway extension or a new paver patio?",
            "<p>A denial has to be in writing and has to cite the specific rule you didn't meet and the part of your plan that doesn't conform; "
            f"a verbal \"no\" or a vague form letter doesn't satisfy that requirement ({src('fs720-3035', 'F.S. 720.3035')}). Once you have the "
            "written reason, check it against two things: whether your material was among the options the guidelines already list, since the board "
            "can't restrict a listed choice, and whether the denial actually traces back to a stated rule rather than a committee member's personal "
            "preference. Communities that run on a monthly meeting cycle often accept a revised submission at the next session rather than require "
            "a full new application, so a denial for something fixable, a color swap, a narrower driveway, an edge moved off a setback line, is "
            "usually a delay rather than a dead end.</p>"),
        sec("How this plays out in practice: three different committees",
            "<p>Every community runs its own calendar and its own paperwork, and the differences matter for how long you should expect to wait. "
            f"In {city('celebration')}, the Architectural Review Committee meets on the third Monday of each month and works off a monthly "
            "application deadline; a request submitted in early April, for example, had to be in by the start of May for that month's meeting "
            "(Celebration, Architectural Review Committee). The Venetian Golf & River Club, a deed-restricted community in North Venice, runs on a "
            "similar monthly cycle: its Architectural Control Committee meets the first Monday of the month at 2 p.m., emails its decision within "
            "72 hours, and an approval stays valid for six months before you'd need to resubmit (Venetian Golf & River Club POA, ACC Application). "
            f"{city('lakewood-ranch')} runs a more granular process tied to a Modification Request Form rather than a general ARC, with its own "
            f"deadline and documentation rules; {post('lakewood-ranch-arc-approval-hardscape', 'our Lakewood Ranch guide')} covers that community "
            "in full, since it doesn't match the generic process described here closely enough to cover in a sentence or two.</p>"
            + table("Three community review processes compared", ["Community", "Meeting cadence", "Submission deadline", "Decision window"],
                    [["Celebration (Osceola County)", "3rd Monday of the month", "Set monthly cutoff ahead of the meeting", "Not published"],
                     ["Venetian Golf & River Club (North Venice)", "1st Monday of the month, 2 p.m.", "Before the meeting date", "Emailed within 72 hours; approval valid 6 months"],
                     ["Lakewood Ranch (CEVA)", "Set committee meeting schedule", "Noon the Thursday before the next meeting", "See our Lakewood Ranch ARC guide"]],
                    "From each community's own published forms and manuals, checked October 2026; every community sets its own process, so confirm the current schedule with your management company.")),
        sec("Steps that keep a submission from bouncing back",
            "<p>Most of what separates a first-try approval from a round of resubmissions is paperwork, not design.</p>"
            + steps([("Read the declaration and any published design guidelines first.", "The approved material list, color palette and any setback rules usually live there, and they set the real boundaries of what the board can say no to."),
                     ("Get the current application form from the management company.", "Forms change, and an old version can get rejected on a technicality before anyone looks at the design."),
                     ("Include a dimensioned site plan and the exact material or color.", "A sample chip, a product name and SKU, or a manufacturer's spec sheet heads off a request for more information that costs you a meeting cycle."),
                     ("Submit before any work starts.", "Work done ahead of approval risks a violation notice regardless of whether the finished result would have passed review."),
                     ("Keep the government permit on a separate track.", f"The city or county permit covered in the {a('/permits/', 'permits and HOA hub')} runs through its own office and its own timeline; the 2026 rule change means the HOA can no longer require that permit before it reviews your design, but you still need both before the crew starts.")])),
        sec("Does this cover artificial turf too?",
            f"<p>Only partly. The general rules above, that an HOA's authority has to be stated in its documents and a denial has to cite a specific "
            f"rule, apply to turf the same way they apply to pavers or concrete. But turf also has its own statute, F.S. 720.3045, which protects "
            f"turf that isn't visible from your lot's frontage or a neighboring parcel regardless of what the declaration says. "
            f"{post('florida-hoa-artificial-turf-law', 'Our guide to the Florida HOA artificial-turf law')} covers that separate protection and "
            "the 2026 state turf standard in detail.</p>"),
    ])
    faqs = [faq("How long does HOA approval take for a driveway or paver project?",
                 "It depends entirely on the community's own meeting schedule, since Florida law sets no statewide timeline. Communities that meet monthly, which is common, typically turn a complete application around within that month's cycle; an incomplete submission or a denial that needs a resubmission adds another full cycle."),
            faq("Can an HOA require a specific paver brand or color?",
                 "An HOA can require you to choose from a published list of approved materials or colors. What it can't do is deny you a choice that's already on that published list, or apply a rule that isn't written down anywhere in the declaration or guidelines; a denial has to cite the specific rule your plan conflicts with."),
            faq("What if I already poured concrete or laid pavers before getting approval?",
                 "Each community's governing documents set its own consequence for unapproved work, and that can range from a formal violation notice to a requirement that you remove or redo the work at your own cost. Check your declaration or Modification Request Form for the specific process before assuming a project finished quickly enough to avoid review."),
            faq("Does getting HOA approval replace the city or county permit?",
                 "No. They're two separate approvals on two separate tracks, and a 2026 change to Florida law means the HOA can no longer require the government permit as a condition of reviewing your design, which also means the reverse holds: HOA sign-off doesn't excuse you from the permit your city or county requires.")]
    related = [("/paver-driveways/", "Paver driveways"), ("/concrete-driveways/", "Concrete driveways"),
               ("/pool-deck-pavers/", "Pool deck pavers"), ("/permits/", "Permits & HOA hub"),
               ("/blog/lakewood-ranch-arc-approval-hardscape/", "Lakewood Ranch ARC approval"),
               ("/blog/florida-hoa-artificial-turf-law/", "Florida HOA artificial-turf law")]
    return page("/blog/hoa-approval-for-pavers-and-concrete/", "post", "HOA Approval for Pavers, Driveways & Pool Decks",
                "How Florida HOA and ARC approval works for a new paver driveway, concrete driveway or pool deck, what boards can and can't require, October 2026.",
                "How to Get HOA Approval for New Pavers, a Driveway or a Pool Deck in Florida",
                capsule("A Florida HOA can require architectural review before you pour concrete or lay pavers, but F.S. 720.3035 limits that power "
                        "to what the declaration or its published guidelines actually state, applied reasonably and equitably. As of October 2026, "
                        "a denial must be in writing and must cite the specific rule, and the board can no longer require a building permit before "
                        "it will even review your application."),
                body, faqs=faqs, sources=["fs720-3035", "fs720-3045",
                         ("Celebration, Architectural Review Committee", "https://celebration.fl.us/events/architectural-review-committee-43/"),
                         ("Venetian Golf & River Club POA, ACC Application", "https://img1.wsimg.com/blobby/go/9771004e-4c48-48de-b5b3-d2a698ae623a/downloads/2dbcf307-d484-4c91-8173-7cf2ca76a901/ACC%20Application%2004.16.26.pdf?ver=1790705617734")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-driveways",
                image="paver-driveway-herringbone", form=False)


def p_lakewood_ranch_arc_approval_hardscape():
    body = "".join([
        sec("Two approvals, not one, for hardscape work in Lakewood Ranch",
            "<p>A driveway or paver job in Lakewood Ranch needs a government permit first, and then a separate community review on top of it; "
            "treating the two as the same step is the most common way a project stalls. Lakewood Ranch spans two counties, roughly three-quarters "
            "of its land area in Manatee County and the rest in Sarasota County, so which office issues the government permit depends on which "
            "side of that line a home sits on (Census Reporter, Lakewood Ranch CDP geography). "
            f"{post('manatee-county-driveway-permits', 'Our Manatee County permit guide')} and "
            f"{post('sarasota-county-driveway-patio-permits', 'our Sarasota County permit guide')} cover each county's driveway and patio rules; "
            "this page covers the layer the county permit doesn't touch, the community's own Modifications Committee review.</p>"),
        sec("Who runs that second review, and what's it called?",
            "<p>Lakewood Ranch's governance runs through an Inter-District Authority board made up of one member from each of the community's five "
            "Community Development Districts, which handles management and property services for the CDDs and the homeowner associations under "
            "them. Changes to a home's exterior, including a driveway, go through a Modification Request Form submitted to Community Association "
            "Services, the office that processes these requests out of Town Hall at 8175 Lakewood Ranch Blvd, 941-907-0202 (Lakewood Ranch Town "
            "Hall, CEVA Homeowners' Manual 2022). Different villages use slightly different forms, a form specific to Country Club/Edgewater "
            "Village, another for Greenbrook and Summerfield-Riverwalk, and a generic community-wide version, so the first step is confirming "
            "which association covers your address before you submit anything.</p>"),
        sec("What actually requires a Modification Request Form?",
            "<p>The Country Club/Edgewater Village homeowners' manual spells out driveway and walkway work in specific terms, and it's stricter "
            "than most homeowners expect:</p>"
            + table("Lakewood Ranch (CEVA) driveway and walkway rules requiring approval", ["Work", "Rule"],
                    [["Sealing a concrete driveway or walkway", "Requires a Modification Request Form; approved sealer colors include Sherwin-Williams Silverplate SW7649, Gray Clouds SW7658 and Amazing Gray SW7044"],
                     ["Painting a driveway or sidewalk", "Not permitted at all, with or without approval"],
                     ["Concrete overlay (resurfacing technique)", "Requires a Modification Request Form and must be applied by a professional"],
                     ["Changing the material of a driveway or walkway", "Requires a Modification Request Form"],
                     ["Repairing the public sidewalk in front of your home", "Not permitted by the homeowner at all"]],
                    "From the Lakewood Ranch Town Hall CEVA Homeowners' Manual, 2022; other Lakewood Ranch villages may set their own rules, so confirm with your association's current manual.")
            + f"<p>That list means a routine job like resealing a faded driveway, something that needs no government permit at all in most "
              "jurisdictions, still needs sign-off from the committee before you schedule it in Lakewood Ranch specifically. The same goes for "
              f"switching a worn concrete driveway over to {svc('paver-driveways', 'pavers')}, or applying a resurfacing overlay instead of a "
              f"{svc('concrete-driveways', 'full tear-out and repour')}; both count as a material change under the manual's wording.</p>"),
        sec("How and when to submit",
            "<p>The Country Club/Edgewater Village Modification Request Form has a firm cutoff: completed requests are due by noon the Thursday "
            "before the next scheduled committee meeting, and the manual is explicit that work finished before the committee actually approves it "
            "is treated as a violation, not a formality you can backfill. An approval isn't open-ended either; if the work isn't completed within "
            "six months of approval, the homeowner has to resubmit the request from scratch (Lakewood Ranch, CEVA Modification Request Form). That "
            "timeline matters most for a project tied to a contractor's schedule, since a missed Thursday cutoff pushes the whole job to the "
            "following meeting cycle, not just a few days.</p>"
            + steps([("Confirm your village association.", "Country Club/Edgewater Village, Greenbrook/Summerfield-Riverwalk and other Lakewood Ranch neighborhoods each use their own Modification Request Form."),
                     ("Get the current form from Community Association Services.", "941-907-0202, or the forms section of the Town Hall site."),
                     ("Submit by the posted deadline, not the meeting date.", "Country Club/Edgewater Village requires completed requests by noon the Thursday before the meeting."),
                     ("Wait for written approval before any work starts.", "Work completed ahead of approval is treated as a modification violation under the CEVA manual."),
                     ("Finish within six months of approval, or resubmit.", "An approved request that sits unused past six months has to go through the committee again.")])),
        sec("A driveway-width rule worth confirming before you design",
            "<p>A search summary of an older Lakewood Ranch guidance document suggests driveway pavers can't extend wider than the home's garage, "
            "but we weren't able to read the full current text of that document to confirm the exact wording, so treat it as something to check "
            "rather than a settled rule. Confirm any width limit directly with Community Association Services before finalizing a driveway "
            "extension design, since a rule like that would sit on top of, not instead of, the government width limits your county permit already "
            f"enforces (see {post('driveway-widening-and-extensions-florida', 'our driveway widening and extension guide')} for those).</p>"),
        sec("What the community committee doesn't cover",
            "<p>The Modifications Committee reviews appearance and material, not engineering or government compliance, so a few things stay "
            f"entirely outside its process. Right-of-way work, the apron and any culvert at the street, still goes through Manatee or Sarasota "
            f"County directly, covered in {post('manatee-county-driveway-permits', 'the Manatee County permit guide')}. A "
            f"{svc('retaining-walls', 'retaining wall')} needs engineered drawings once it crosses the height threshold either county sets, which "
            "the community review doesn't substitute for. And artificial turf carries its own statewide statute protecting turf that isn't visible "
            f"from the street or a neighboring lot regardless of what the community's modification rules say; "
            f"{post('florida-hoa-artificial-turf-law', 'our Florida HOA artificial-turf guide')} covers that protection on its own.</p>"),
        sec("Say you own a home in Country Club at Lakewood Ranch",
            "<p>Your driveway has faded and you want it resealed before the winter season. Under the CEVA manual, that's a Modification Request "
            "Form, not a phone call to a sealing contractor on a Monday: pick a color from the approved list, submit the form by noon the Thursday "
            "before the next meeting, and wait for written approval before the crew shows up. If the county side of the project needs anything, a "
            "resealing job on an already-permitted driveway usually doesn't, that's a separate step entirely, handled by whichever county your "
            "address falls in rather than by Town Hall.</p>"
            + (photo("concrete-driveway-modern", "Broom-finish concrete driveway leading to a house with a dark garage door") or "")),
    ])
    faqs = [faq("Do I need both a county permit and Lakewood Ranch community approval?",
                 "For most hardscape work, yes. The government permit covers engineering and right-of-way questions through Manatee or Sarasota County depending on which side of Lakewood Ranch you're on, and the Modifications Committee separately reviews appearance, material and color for your village association. Sealing an existing driveway typically needs only the committee approval, not a new county permit."),
            faq("What happens if I reseal my Lakewood Ranch driveway without approval?",
                 "The Country Club/Edgewater Village manual treats work completed before the Modifications Committee approves it as a violation, not a technicality to clean up afterward. Submit the Modification Request Form and wait for written approval before scheduling the work, even for something as routine as sealing."),
            faq("Can I paint my driveway in Lakewood Ranch?",
                 "No. The CEVA Homeowners' Manual states that painting a residential driveway or sidewalk is not permitted at all, regardless of approval. Sealing with an approved color is treated differently and does go through the Modification Request Form process."),
            faq("Who do I contact to start a Lakewood Ranch modification request?",
                 "Community Association Services at Town Hall, 8175 Lakewood Ranch Blvd, 941-907-0202, handles Modification Request Forms for Lakewood Ranch's villages. Confirm which association covers your address first, since Country Club/Edgewater Village, Greenbrook/Summerfield-Riverwalk and other neighborhoods use slightly different forms.")]
    related = [("/paver-driveways/", "Paver driveways"), ("/concrete-driveways/", "Concrete driveways"),
               ("/pool-deck-pavers/", "Pool deck pavers"), ("/blog/manatee-county-driveway-permits/", "Manatee County driveway permits"),
               ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete"),
               ("/blog/florida-hoa-artificial-turf-law/", "Florida HOA artificial-turf law")]
    return page("/blog/lakewood-ranch-arc-approval-hardscape/", "post", "Lakewood Ranch ARC Approval for Driveways & Pavers",
                "How Lakewood Ranch's Modification Request Form process works for driveway sealing, pavers and pool decks, and how it fits with county permits, October 2026.",
                "Lakewood Ranch ARC Approval for Driveways, Pavers and Pool Decks",
                capsule("Lakewood Ranch spans Manatee and Sarasota counties, so a driveway or paver job needs a county permit first and then a "
                        "separate community approval through a Modification Request Form filed with Community Association Services. As of October "
                        "2026, sealing, resurfacing or changing a driveway's material or color in Country Club/Edgewater Village all require that "
                        "form before work starts, and painting a driveway is never permitted."),
                body, faqs=faqs,
                sources=[("Lakewood Ranch Town Hall, CEVA Homeowners' Manual 2022", "https://content.civicplus.com/api/assets/07e300e3-1105-41c9-b71a-8f514fb7521e"),
                         ("Lakewood Ranch, CEVA Modification Request Form", "https://content.civicplus.com/api/assets/12d6c811-993f-4b28-8037-19a92d533e1f"),
                         ("Lakewood Ranch, GBVA/SRVA Modification Request Form", "https://content.civicplus.com/api/assets/da597a78-9dca-4610-b61a-6a1700827dc4"),
                         ("Census Reporter, Lakewood Ranch CDP geography (county split)", "https://api.censusreporter.org/1.0/geo/tiger2024/16000US1239067/parents"),
                         "fs720-3045"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-driveways",
                image="concrete-driveway-modern", form=False)


def p_florida_hoa_artificial_turf_law():
    body = "".join([
        sec("Can my HOA stop me from installing artificial turf in Florida?",
            "<p>Often not, but only for turf your neighbors and the street can't see. F.S. 720.3045 keeps a Florida HOA from blocking items a "
            "parcel owner installs, displays or stores once those items sit where the lot's own frontage, a neighboring parcel, a nearby common "
            f"area and any community golf course all fail to see them, and the statute calls out artificial turf by name as a protected item "
            f"({src('fs720-3045', 'F.S. 720.3045')}). "
            f"That protection has a real limit built into it: a {svc('artificial-turf', 'front-yard lawn')} that's visible from the street is "
            "outside the statute's scope entirely, which means the HOA's general architectural-review authority still applies to it the same way "
            "it applies to a driveway or a fence.</p>"),
        sec("What does \"not visible from the frontage\" actually mean in practice?",
            "<p>The statute protects turf in spots your own lot's frontage, a neighboring parcel, an adjacent common area or a community golf "
            "course can't see, which in most subdivisions means a side yard behind a fence or a backyard a privacy wall screens from the house "
            "next door. A front lawn, by contrast, sits squarely in what the frontage can see by definition, so the HOA keeps its ordinary say over "
            "it under the architectural-control statute, F.S. 720.3035: that authority has to come from what the declaration or published "
            "guidelines actually state, applied reasonably, with a written denial that cites the specific rule you didn't meet "
            f"({src('fs720-3035', 'F.S. 720.3035')}). {post('hoa-approval-for-pavers-and-concrete', 'Our general HOA approval guide')} covers how "
            "that review process works for anything an association can legitimately control, turf included.</p>"),
        sec("Does the 2025 law, HB 683, change what my HOA can do?",
            "<p>No, it regulates cities and counties, not homeowner associations. HB 683 created F.S. 125.572, which tells the Florida Department "
            "of Environmental Protection to adopt minimum standards for synthetic turf on single-family lots of an acre or less, and once those "
            "standards exist, a local government can't prohibit compliant turf or regulate it in a way that's stricter than DEP's rule "
            f"({src('fs125-572', 'F.S. 125.572')}). The bill's own analysis draws the HOA line explicitly: it notes that the law already kept "
            "associations from restricting turf hidden from a lot's frontage before the bill ever passed, while nothing on the books at the time "
            f"put any limit on a city or county regulating turf however it liked, which is the exact gap HB 683 closed "
            f"({src('hb683-analysis', 'HB 683 Final Bill Analysis')}). A 2026 statute amendment also carved out one exception: the "
            "local-government preemption doesn't stop a community development district from enforcing its own deed restrictions on turf.</p>"),
        sec("What does Florida's new DEP turf rule actually require?",
            f"<p>Regardless of what your HOA says, a rule that took effect May 19, 2026 sets statewide minimum standards for residential turf on "
            f"lots of an acre or less ({src('flrules62-308-100', 'FDEP Rule 62-308.100')}). It doesn't create a new DEP permit of its own, but it "
            "does set hard requirements local governments can't regulate below:</p>"
            + table("DEP Rule 62-308.100, synthetic turf minimum standards", ["Requirement", "What it says"],
                    [["Infill", "Clean silica sand, rock, shell or other natural material; rubber or synthetic infill only inside a playground footprint"],
                     ["Base", "Natural materials such as crushed rock or crushed concrete, washed before installation to keep fines from binding"],
                     ["Irrigation", "In-ground irrigation systems can't be used to water synthetic turf areas"],
                     ["Water setback", "A 10-ft buffer back from any natural or built waterbody, except where a seawall or similar barrier already stands"],
                     ["Tree drip lines", "Kept clear of a tree's drip line, unless a certified arborist signs off on installing there"],
                     ["Color", "Green synthetic turf is explicitly allowed"]],
                    f"From the adopted rule text ({src('rule62-308-100-text', '62-308.100, full text')}); local governments may not regulate turf in a way that's inconsistent with these minimums.")),
        sec("What if my city or county has its own turf ordinance already?",
            "<p>After May 19, 2026, any local ordinance has to line up with DEP's minimum standards; a city or county can still regulate synthetic "
            "turf, it just can't set a rule stricter than what the state adopted. That's a separate question from what your HOA can require, since "
            "125.572 reaches only \"local government\" action, not a private community's declaration, so a city easing its turf rules to match the "
            "state standard doesn't loosen whatever your HOA's own design guidelines still say about visible turf.</p>"),
        sec("Two examples that land on opposite sides of the statute",
            "<p>Say a homeowner's backyard sits behind a 6-foot privacy fence that blocks the view from the street and from both side neighbors. "
            f"F.S. 720.3045 protects {svc('artificial-turf', 'turf installed there')} from an HOA ban even if the declaration never mentions turf "
            "at all, because the statute's visibility test, not the HOA's silence or approval, is what controls. Now say the same homeowner wants "
            "turf across the front lawn instead, fully visible from the sidewalk. The 720.3045 protection doesn't reach that spot, so the HOA's "
            "ordinary architectural review applies, the same review a new driveway or a pool deck would go through, and a written denial citing a "
            "specific design guideline would be enforceable the way it would be for any other visible improvement.</p>"),
        sec("Does a community development district change any of this?",
            "<p>In some communities, yes. A 2026 amendment to F.S. 125.572 added a specific carve-out: the preemption that keeps local "
            f"governments from regulating turf more strictly than the DEP rule \"does not apply to... a community development district to enforce "
            f"deed restrictions\" ({src('fs125-572', 'F.S. 125.572')}). A CDD is a special taxing district, not the same legal structure as an HOA, "
            "and some master-planned communities, including large ones across Central Florida and the Suncoast, run both a CDD and one or more "
            "homeowner associations layered on top of each other. If your deed restrictions come through a CDD rather than, or in addition to, a "
            "standard HOA declaration, that CDD keeps its own enforcement power over turf even after the state turf standard took effect, separate "
            "from the F.S. 720.3045 visibility protection and separate from the DEP rule's statewide minimums. Reading which entity actually holds "
            "your community's deed restrictions, an HOA, a CDD, or both, is worth doing before assuming any single statute settles the question "
            "for your address.</p>"),
    ])
    faqs = [faq("Can my HOA stop me from installing artificial turf in Florida?",
                 "It depends on visibility. F.S. 720.3045 protects turf that can't be seen from your lot's frontage, an adjacent parcel or a community golf course, regardless of what the declaration says. Front-yard turf visible from the street isn't covered by that statute, so the HOA's ordinary architectural-review authority still applies to it."),
            faq("Is green artificial turf allowed under Florida's new DEP rule?",
                 "Yes. Rule 62-308.100, effective May 19, 2026, explicitly states that green synthetic turf is allowed, alongside requirements covering infill, base material, irrigation and setbacks from water and trees."),
            faq("Can I run my sprinklers under artificial turf?",
                 "No. The DEP rule prohibits using in-ground irrigation systems to water synthetic turf areas, and a local government can require existing sprinkler heads to be removed and the pipe capped."),
            faq("Does the new turf rule require a DEP permit before installation?",
                 "No. The rule sets minimum standards that local governments must follow when they regulate turf, but it doesn't establish or require a new DEP-issued permit of its own."),
            faq("Can my HOA still deny turf that's visible from the street?",
                 "Generally yes, subject to the same limits that apply to any other architectural-review decision: the authority has to come from the declaration or published guidelines, applied reasonably, with a written denial citing the specific rule. Our general HOA approval guide covers that process.")]
    related = [("/artificial-turf/", "Artificial turf"), ("/artificial-turf-cost/", "Artificial turf cost guide"),
               ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete"),
               ("/blog/artificial-turf-water-savings-florida/", "Artificial turf water savings in Florida"),
               ("/permits/", "Permits & HOA hub")]
    return page("/blog/florida-hoa-artificial-turf-law/", "post", "Is Artificial Turf Allowed by HOA in Florida?",
                "Can a Florida HOA ban artificial turf? What F.S. 720.3045 protects, how HB 683 changed local law, and the DEP turf rule effective May 2026.",
                "Can Your Florida HOA Ban Artificial Turf? What Statute 720.3045 and the 2025 Law Change Say",
                capsule("Yes, in most front yards: F.S. 720.3045 only bars a Florida HOA from restricting turf that isn't visible from your lot's "
                        "frontage, an adjacent lot or a community golf course, so turf the street can see isn't automatically protected. As of "
                        "October 2026, HB 683 and its new DEP rule limit cities and counties instead, and never mention HOAs at all."),
                body, faqs=faqs, sources=["fs720-3045", "fs720-3035", "fs125-572", "hb683-analysis", "flrules62-308-100", "rule62-308-100-text"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf",
                image="green-lawn-patio", form=False)


def p_driveway_apron_and_right_of_way_florida():
    body = "".join([
        sec("Who owns the driveway apron between the sidewalk and the street?",
            "<p>The apron sits inside the public right-of-way, the strip of land the city or county controls for the street, sidewalk and "
            "drainage, not on the part of the lot you own outright, even though you paid for it and it's the first thing in your path leaving the "
            "garage. Bradenton's driveway affidavit makes that split explicit in writing: the homeowner builds and maintains the work, but has to "
            f"remove or relocate it at their own cost if the city later asks ({src('bradenton-driveway-affidavit', 'Bradenton Driveway Affidavit, 2024')}). "
            f"Nearly every jurisdiction we checked treats the apron the same way, public land, private maintenance duty, which is why a "
            f"{svc('concrete-driveways', 'driveway replacement')} that never crosses the property line can skip a permit in places where the apron "
            "section can't.</p>"),
        sec("Do you need a permit to replace your apron?",
            "<p>Yes, almost everywhere. The right-of-way is public infrastructure, so building, replacing or widening the apron section nearly "
            "always triggers a separate permit from whatever you'd need for the rest of the driveway, even on a straight like-for-like "
            "replacement. The City of Orlando requires an engineering permit specifically because \"installing/removing pavers, asphalt, concrete "
            f"or expanding your driveway\" touches that public strip ({src('orlando-esm', 'City of Orlando, Engineering Standards Manual')}). Orange "
            "County's own Residential Lot Grading Policy uses language that catches repair work too, not just new construction, since its standard "
            f"covers anyone who wants to \"construct, reconstruct, install or repair a driveway, sidewalk, pavement\" in the right-of-way "
            f"({src('orange-lot-grading', 'Orange County Residential Lot Grading Policy, 2023')}). Seminole County, Manatee County and the City of "
            "Sarasota each run their own version of the same rule under different names, a Residential Driveway Construction Application, an "
            f"access and drainage permit, or an engineering permit tied to curb cuts ({src('seminole-driveway-app', 'Seminole County')}, "
            f"{src('manatee-driveway-application', 'Manatee County')}, {src('city-sarasota-code-29.5-7-curb-cut-driveway', 'City of Sarasota §29.5-7')}).</p>"),
        sec("Why does the apron get stricter specs than the rest of the driveway?",
            "<p>Because it's public infrastructure that has to carry whatever traffic the street does, the apron almost always calls for thicker, "
            "stronger concrete than a private driveway slab needs on its own. The pattern repeats across jurisdictions with only the exact numbers "
            "changing:</p>"
            + table("Apron construction specs by jurisdiction (public right-of-way section)", ["Jurisdiction", "Minimum thickness", "Minimum strength", "Notes"],
                    [["City of Orlando", "6 in", "3,000 psi", "Break joint required at the property line"],
                     ["Orange County", "6 in", "3,000 psi", "Non-steel reinforced concrete across the right-of-way, including the sidewalk section"],
                     ["Seminole County", "6 in", "3,000 psi", "Fiber-reinforced concrete allowed"],
                     ["Manatee County", "6 in", "Not specified", "Measured from the edge of pavement to the right-of-way line"],
                     ["City of Sanford", "Not specified (apron); sidewalks 6 in at vehicular crossings", "3,000 psi (apron)", "Standard sidewalk is 4 in; crossings go to 6 in"],
                     ["Town of Windermere", "6 in", "3,000 psi, fiber mesh", "Saw-cut road edge; 5 ft minimum flares each side"]],
                    f"From each jurisdiction's published driveway or engineering standards, checked October 2026 ({src('orlando-esm', 'Orlando ESM')}, "
                    f"{src('orange-lot-grading', 'Orange County')}, {src('seminole-driveway-app', 'Seminole County')}, {src('manatee-driveway-application', 'Manatee County')}, "
                    f"{src('sanford-schedule-n', 'Sanford')}, {src('windermere-row-app', 'Windermere')}).")),
        sec("What about the sidewalk section where it crosses your driveway?",
            "<p>Where a sidewalk crosses the apron, several jurisdictions require that short section to be thicker than an ordinary sidewalk, "
            f"since it carries vehicle weight the rest of the walk never sees. Orlando's manual requires the sidewalk section through the driveway "
            f"to run at least 3,000 psi concrete and at least 6 inches thick, matching the apron itself, with pavers allowed only if they meet the "
            f"city's own paver spec ({src('orlando-esm', 'City of Orlando Engineering Standards Manual')}). Seminole County ties new driveway "
            f"construction to the same rule: a new driveway means the sidewalk section through it gets replaced at 6 inches thick, not left at the "
            f"standard 4 ({src('seminole-driveway-app', 'Seminole County')}). Manatee County's own paver driveway inspection checklist calls for a "
            "4-inch crossing slab, 5 feet across, framed lot line to lot line, with a broom texture and a saw cut every 10 feet along its length "
            f"({src('manatee-driveway-application', 'Manatee, Inspections Required for Paver Driveways')}).</p>"),
        sec("Are pavers allowed in the apron?",
            f"<p>In most places, yes, but with conditions attached that don't apply to a {svc('paver-driveways', 'paver driveway')} built entirely "
            "on private property. Orlando allows brick pavers in the apron if they meet its own paver spec, but still requires the sidewalk "
            f"crossing through it to be 3,000 psi concrete at 6 inches, and a paver driveway in the right-of-way needs its own Paver's Memorandum "
            f"of Understanding with the city ({src('orlando-esm', 'City of Orlando Engineering Standards Manual')}). Orange County and Seminole "
            "County both allow pavers in the right-of-way but draw a line at the crosswalk and sidewalk itself, where pavers aren't permitted "
            f"({src('orange-lot-grading', 'Orange County')}, {src('seminole-driveway-app', 'Seminole County')}). Windermere sets a materials "
            "standard rather than a flat ban: paver aprons there have to meet ASTM C902 inside a ribbon curb, or follow FDOT's paving spec where "
            f"there's no sidewalk at all ({src('windermere-row-app', 'Town of Windermere/PDCS')}).</p>"),
        sec("Does a cracked or sunken apron need the same permit as a full replacement?",
            "<p>Usually, yes, because most jurisdictions' permit language covers repair the same way it covers new construction. Orange County's "
            "lot grading policy, for example, uses \"construct, reconstruct, install or repair\" in the same sentence, which leaves no gap for a "
            f"patch job to skip the permit a full rebuild would need. That matters most for a slab that's settled rather than cracked outright; "
            f"a {svc('concrete-repair', 'mudjacking or releveling job')} on the apron itself can still trip the same right-of-way permit a "
            f"replacement would, even though the repair work is smaller. {compare('resurface-vs-replace-concrete', 'Our resurface-or-replace guide')} "
            f"and {a('/concrete-repair-cost/', 'our concrete repair cost guide')} cover how to weigh that decision once the apron's condition is "
            "clear, but the permit question comes first either way.</p>"),
        sec("Exceptions worth knowing about",
            "<p>Not every right-of-way touch requires a full permit everywhere. The City of St. Cloud's no-permit list specifically excludes "
            "resealing existing on-site asphalt from the permit requirement, while still requiring Public Works and Engineering approval for any "
            f"work that actually sits within the right-of-way ({src('stcloud-permit-info', 'City of St. Cloud, Permit Information')}). That's the "
            "kind of distinction worth confirming by phone rather than assuming; a reseal and a rebuild can sit on opposite sides of a permit line "
            "even in the same city.</p>"
            + (photo("concrete-driveway-joints", "Concrete driveway with cut control joints running toward a garage") or "")),
    ])
    faqs = [faq("Who owns the driveway apron?",
                 "The city or county owns the right-of-way the apron sits in, even though the homeowner typically pays to build it, maintains it, and has to move it at their own cost if the local government ever needs the space for utility or road work."),
            faq("Do I need a permit just to reseal or clean my apron?",
                 "Often not; several jurisdictions, including the City of St. Cloud, exclude resealing from their permit requirement while still regulating any work that actually alters the apron itself. Check your city or county's current rules before assuming a maintenance job is exempt, since the line between resealing and reconstruction isn't drawn the same way everywhere."),
            faq("Can I use pavers for my apron instead of concrete?",
                 "In most jurisdictions we checked, yes, but with extra requirements: a separate paver agreement with the city in some places, a materials spec the pavers have to meet, and a ban on pavers crossing the sidewalk or crosswalk section itself, which usually still has to be concrete."),
            faq("Does widening my apron need the same permit as widening the rest of my driveway?",
                 "They're usually two different permits from two different review processes, since the apron sits in the right-of-way and the rest of the driveway sits on private property. Our guide to widening or extending a driveway in Florida covers both sides of that project.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/paver-driveways/", "Paver driveways"),
               ("/concrete-walkways/", "Sidewalks & walkways"), ("/permits/", "Permits & HOA hub"),
               ("/blog/driveway-widening-and-extensions-florida/", "Widening or extending a driveway in Florida"),
               ("/compare/resurface-vs-replace-concrete/", "Resurface or replace concrete")]
    return page("/blog/driveway-apron-and-right-of-way-florida/", "post", "Driveway Apron Replacement: FL Right-of-Way Rules",
                "Who owns a Florida driveway apron, when a right-of-way permit is required to replace it, and the thickness and strength rules, as of October 2026.",
                "Who Owns the Driveway Apron? Right-of-Way Rules for Florida Driveways",
                capsule("The driveway apron sits inside the public right-of-way, the strip the city or county controls between your property "
                        "line and the street, even though you build and maintain it yourself. As of October 2026, nearly every Florida "
                        "jurisdiction we checked requires a right-of-way or engineering permit to replace it, built to a stricter spec than the "
                        "rest of the driveway, typically 6 inches thick and 3,000 psi."),
                body, faqs=faqs,
                sources=["orlando-esm", "orange-lot-grading", "seminole-driveway-app", "manatee-driveway-application",
                         "city-sarasota-code-29.5-7-curb-cut-driveway", "bradenton-driveway-affidavit", "windermere-row-app",
                         "sanford-schedule-n", "stcloud-permit-info"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image="concrete-driveway-joints", form=False)


def p_driveway_widening_and_extensions_florida():
    body = "".join([
        sec("Can I widen my driveway in Florida?",
            "<p>Usually, but nearly every city and county caps how wide a residential driveway can be at the right-of-way line, commonly 18 to "
            "24 feet, with a few places allowing up to 30 feet for a street-facing three-car garage. The exact number, and whether it's measured "
            "at the property line, the curb or the roadway edge, changes by jurisdiction, so the first call before designing an extension is "
            f"confirming the local limit, not assuming a neighboring city's rule applies. A {svc('concrete-driveways', 'concrete driveway')} or a "
            f"{svc('paver-driveways', 'paver driveway')} extension both run into the same width ceiling; the material you choose doesn't change "
            "how wide the local code lets you go.</p>"),
        sec("How wide can a driveway actually be, by jurisdiction?",
            "<p>The spread across jurisdictions is wide enough that a rule you've heard about one city shouldn't be assumed to apply in the next "
            "one over.</p>"
            + table("Maximum driveway width by jurisdiction (at or near the right-of-way line)", ["Jurisdiction", "Maximum width", "Notes"],
                    [["City of Orlando", "18 ft at the property line", "Up to 20 ft through the front setback; apron must match the driveway width"],
                     ["Osceola County (unincorporated)", "24 ft", "Wider requires a conditional use approval"],
                     ["Lake County (unincorporated)", "24 ft at the property line", "10 ft minimum; 8 ft radius or 8 by 4 ft flares"],
                     ["Seminole County (unincorporated)", "24 ft at the roadway", "18 ft driveway plus 3 ft flares on each side"],
                     ["Manatee County (unincorporated)", "24 ft", "Up to 30 ft for a street-facing three-car garage"],
                     ["Town of Longboat Key", "24 ft for a two-way drive", "12 ft maximum for a one-way drive"]],
                    "From each jurisdiction's published driveway or zoning standards, checked October 2026; confirm the current limit with the permitting office before finalizing a design.")),
        sec("What stops an extension even where the width itself is allowed?",
            "<p>Width limits are only half the equation; a lot's impervious surface ratio, the share of the property covered by roofs, driveways, "
            "patios and pool decks, often runs out of room before the driveway's own width limit does. Winter Park caps most single-family zones "
            "at 50% total impervious coverage and separately requires half the front yard to stay pervious, counting hard-surface driveway "
            f"material against that limit either way ({src('winterpark-driveway-permit', 'City of Winter Park, Driveway Permit Requirements')}). "
            "Sanford sets the same 50% ceiling across several zoning districts and counts artificial turf as impervious along with concrete and "
            f"pavers ({src('sanford-schedule-f', 'City of Sanford, LDR Schedule F')}). Bradenton's limit moves with the zoning district, from 50% "
            f"in R-1 up to 70% in its denser zones ({src('bradenton-lur-3.2-isr', 'Bradenton LUR §3.2')}), and the City of Sarasota runs a similar "
            f"range, 60% to 75% depending on the zone, with coastal islands like Lido and St. Armands capped lower at 70% "
            f"({src('city-sarasota-zoning-vi-203-impervious', 'City of Sarasota Zoning Code §VI-203')}). Clermont splits the limit two ways: 55% "
            "total impervious coverage in its R-1 district, but the principal building plus driveway and walkways specifically can't exceed 45% "
            f"({src('clermont-r1-isr', 'City of Clermont, Municode Ch. 125')}). Before sketching an 8-foot-wide addition next to an existing "
            "driveway, it's worth pulling your lot's current impervious percentage, since an extension that's perfectly legal on width can still "
            "get turned down on coverage.</p>"),
        sec("Matching new concrete to an existing driveway",
            "<p>An extension poured next to an old slab is a different job from a full replacement, because the two sections have to move "
            "together instead of cracking apart at the seam. Crews typically drill into the existing slab's edge and epoxy dowel bars across the "
            "new joint so both panels settle and expand as one unit rather than as two independent slabs working against each other; left as a "
            "plain butt joint with no dowels, that seam is usually the first place a new extension cracks. Control joints in the new section "
            "should match the spacing already cut into the old slab, roughly 8 to 12 feet for a 4-inch driveway, cut a quarter of the slab's own "
            f"depth, so the extension reads as one continuous pattern instead of two mismatched grids running into each other ({src('nrmca-cip6', 'NRMCA CIP 6')}). "
            f"Color and finish are the other half of the match; a broom-finish slab poured years apart rarely comes out an identical shade, and "
            f"{svc('stamped-concrete', 'a stamped or stained finish')} narrows that gap more than a plain gray pour does.</p>"),
        sec("Extending with pavers next to existing concrete",
            f"<p>Tying a {svc('paver-driveways', 'paver extension')} into an existing concrete driveway runs into a different set of problems than "
            "concrete-to-concrete work does, mainly at the edge where the two materials meet. The paver section needs its own edge restraint "
            "along that seam, since nothing holds a paver field in place the way a continuous concrete pour holds itself, and the base depth under "
            "the new pavers has to match or exceed the compacted base under the original driveway or the two surfaces will settle at different "
            "rates and leave a visible step at the joint. A transition strip or a change in material pattern at the seam, rather than trying to "
            "disguise where old concrete ends and new pavers begin, usually reads better and holds up longer than forcing an exact color match that "
            f"two materials poured years apart were never going to achieve on their own. {compare('pavers-vs-concrete-driveway', 'Our pavers vs. concrete comparison')} "
            "covers the broader trade-offs between the two materials.</p>"),
        sec("Does an older, never-permitted driveway still need a permit to widen?",
            "<p>Generally yes, because most permit rules apply to the new work itself, not to the driveway's history. Orange County's own rule is "
            "blunt about this: \"anytime you are pouring concrete or placing pavers, a permit is required,\" with no carve-out for driveways that "
            f"predate the current code ({src('orange-lot-grading', 'Orange County, Do I Need a Permit')}). That means a 1980s home with a driveway "
            "built before any current permit system existed still needs a new permit for the extension itself, even if nobody can find paperwork "
            "for the original pour. It's worth confirming this directly with the local permitting office for an older home, since some "
            "jurisdictions treat a widening next to a pre-existing driveway differently from a brand-new installation, and that distinction isn't "
            "published consistently across the cities and counties we checked.</p>"),
        sec("A parking pad instead of a full-width extension",
            "<p>Some lots can't legally support a wider driveway at all, usually because of a one-driveway-per-frontage rule rather than a width "
            "cap. Orange County's lot grading policy limits a property to one driveway if its frontage is under 100 feet, which pushes a second "
            "parking space toward tying into the existing driveway opening instead of cutting a new curb access for a separate pad "
            f"({src('orange-lot-grading', 'Orange County, Residential Lot Grading Policy, 2023')}). A {svc('concrete-slabs', 'standalone parking pad')} "
            f"set beside the driveway, rather than widening the drive itself, sometimes sidesteps that one-driveway rule since it doesn't need its "
            f"own curb cut; {post('concrete-pad-for-rv-or-boat-parking', 'our guide to RV and boat parking pads')} covers sizing and thickness for "
            "that approach.</p>"),
        sec("Say you have a 1990s Kissimmee home with a single 16-foot driveway",
            "<p>You want to add an 8-foot strip alongside it for a second car. First, check Osceola County's 24-foot maximum residential driveway "
            "width; a 16-foot drive plus an 8-foot strip lands at 24 feet, right at the ceiling, so the layout and any flare at the curb need to "
            "fit inside that number rather than beside it. Next, pull the lot's impervious surface calculation, since adding 8 feet of concrete "
            "over the driveway's length can push an older subdivision lot with a modest front yard closer to whatever limit applies. Then check "
            "whether an HOA covers the subdivision; if it does, the extension needs its own design review separate from the county permit, "
            f"covered in {post('hoa-approval-for-pavers-and-concrete', 'our HOA approval guide')}. Only after those three checks does the actual "
            "construction question, matching the new concrete's joints and finish to the old slab, become the thing that decides how the job "
            "goes.</p>"),
    ])
    faqs = [faq("How wide can a driveway be in Florida?",
                 "It varies by jurisdiction, roughly 18 to 24 feet at the right-of-way line in most of the cities and counties we checked, with some going up to 30 feet for a street-facing three-car garage and others as low as 12 feet for a one-way drive. Confirm the current number with your specific city or county before designing an extension."),
            faq("Can I widen my driveway without a permit?",
                 "No, in every jurisdiction we checked. Pouring concrete or placing pavers for a driveway extension triggers a permit requirement regardless of whether the original driveway predates the current code, so budget time for the permit process before scheduling the work."),
            faq("Will new concrete crack differently from my old driveway?",
                 "It can, if the two sections aren't tied together. Drilling dowel bars across the new joint and matching the control-joint spacing from the existing slab keeps both panels moving as one unit instead of cracking independently at the seam where they meet."),
            faq("Does widening my driveway affect HOA review separately from the county permit?",
                 "Yes, if your community has an HOA with architectural control. The county permit and the HOA's design review are two separate approvals on two separate timelines, and getting one doesn't substitute for the other.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/paver-driveways/", "Paver driveways"),
               ("/blog/driveway-apron-and-right-of-way-florida/", "Who owns the driveway apron"),
               ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete"),
               ("/blog/concrete-pad-for-rv-or-boat-parking/", "RV or boat parking pads"),
               ("/compare/pavers-vs-concrete-driveway/", "Pavers vs. concrete driveway")]
    return page("/blog/driveway-widening-and-extensions-florida/", "post", "Driveway Extension Concrete: Florida Rules & Options",
                "Can you widen a driveway in Florida? Width limits by jurisdiction, impervious-surface caps and how to tie new concrete or pavers into an old driveway, October 2026.",
                "Widening or Extending a Driveway in Florida: Rules, Options and Pitfalls",
                capsule("Yes, you can widen a driveway in Florida, but nearly every city and county caps the width at the right-of-way line, "
                        "commonly 18 to 24 feet and up to 30 feet for a three-car garage in some places. As of October 2026, matching the new "
                        "concrete's control joints to the old slab, and checking your lot's impervious-surface limit, matter as much as the "
                        "jurisdiction's width rule."),
                body, faqs=faqs,
                sources=["winterpark-driveway-permit", "sanford-schedule-f", "bradenton-lur-3.2-isr", "city-sarasota-zoning-vi-203-impervious",
                         "clermont-r1-isr", "nrmca-cip6", "orange-lot-grading",
                         ("Osceola County, Parking Ordinance §22-50.6", "https://www.osceola.org/files/assets/county/v/1/services/transportation-and-transit-dept-services/documents/osceola-county-parking-ordinance.pdf"),
                         ("Lake County, LDR Appendix A Transportation Standards", "https://cdn.lakecountyfl.gov/media/svzhjaw5/lc_ldr_appendix_a_transdesignconstr_standards.pdf"),
                         ("Seminole County, Residential Driveway Construction Application", "https://www.seminolecountyfl.gov/docs/default-source/pdf/row-driveway-application-ada9374f1d4-2d72-44db-8736-e2360bade3af.pdf?sfvrsn=bd3e5de0_3"),
                         "manatee-driveway-application",
                         ("Longboat Key Code §158.100, off-road parking access", "https://library.municode.com/fl/longboat_key/codes/code_of_ordinances?nodeId=TIT15LADECO_CH158ZOCO_ARTVSUDEST_DIV4OREPALO_158.100OREPA")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image="interlocking-pavers", form=False)


def get_pages():
    return [p_manatee_county_driveway_permits(), p_hoa_approval_for_pavers_and_concrete(), p_lakewood_ranch_arc_approval_hardscape(),
            p_florida_hoa_artificial_turf_law(), p_driveway_apron_and_right_of_way_florida(), p_driveway_widening_and_extensions_florida()]
