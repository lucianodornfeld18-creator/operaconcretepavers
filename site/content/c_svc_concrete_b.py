# -*- coding: utf-8 -*-
"""Service pages: concrete patios, stamped concrete (patio/driveway/pool deck/walkway all in one)."""
from _helpers import page, capsule, sec, table, faq, ul, steps, a, svc, cs, post, compare, src, ext, price, per, price_note, contact, photo, offer
from _data import SERVICES
from _photos import for_service


def concrete_patios():
    K = "concrete-patios"
    pids = for_service(K, 3)
    patio_steps = [
        ("Lay out and mark.", "We set stakes and string lines for the patio footprint, check it against the setback and impervious-surface limits for the lot, and flag any footings a lanai or outdoor kitchen island will need."),
        ("Excavate and grade.", "Sod and loose topsoil come out to reach soil that can actually be compacted. The subgrade is shaped to fall away from the house rather than toward it before any fill goes in."),
        ("Compact the base.", "Fill goes down in lifts and gets compacted for uniform support, per Florida's residential code, with at least 4 inches of clean graded sand, gravel or crushed stone under the slab (FBC Residential R506.2)."),
        ("Form and reinforce.", "Wood forms set the elevation and edges. Fiber-reinforced mix is standard on an open patio; wire mesh or rebar goes in where a job calls for it, pulled up into the slab's middle as the pour proceeds."),
        ("Pour and finish.", "Concrete is screeded level, bull floated, then finished with a broom, a trowel or an exposed-aggregate wash, with edging and control joints cut while the surface is still workable."),
        ("Cure.", "The surface stays moist, by curing compound or wet curing, for at least 3 days before anyone treats it as finished work, longer in hot, dry, windy weather (NRMCA CIP 12)."),
        ("Clean up and walk the slope.", "Forms come out, the site is graded back around the new edge, and we check that water actually runs away from the foundation before calling the job done."),
    ]
    body = "".join([
        sec("What a concrete patio covers, and where stamped or paver patios fit",
            f"<p>A concrete patio is a poured slab behind or beside a Florida house: a plain back patio, a lanai extension tied to an existing slab, or a pad built for an outdoor kitchen or fire feature. "
            f"Most of what we pour here is a broom or trowel finish, because that is the budget option and the one that matches an older lanai without redoing the whole thing. "
            f"If you want a pattern pressed into the surface, slate, ashlar or a wood-plank look, that is {svc('stamped-concrete', 'stamped concrete')}, which owns every stamped surface on this site, patios included, so its page covers patterns, color and sealer in depth. "
            f"If you are set on individual pavers instead of a poured slab, {svc('paver-patios', 'paver patios and walkways')} is the page for base depth, bedding sand and edge restraint. "
            f"As of October 2026, plain concrete patios in Florida run {price('concrete-patio')} per square foot installed, with {price('concrete-patio', True)} the typical middle for a broom or trowel finish ({price_note()}).</p>"),
        sec("Thickness, strength and the base underneath",
            "<p>A concrete patio in our area is 4 inches thick at 3,000 to 4,000 psi, poured over at least 4 inches of compacted base. That is thicker than the state's bare floor for any slab "
            f"on the ground, 3½ inches under FBC Residential R506.1, because a patio that stops right at code leaves little room for a loaded planter, a grill island or a few years of settling before it starts to show. "
            f"Florida's residential code sets strength by weathering exposure rather than one number for every slab: Table R402.2 calls for 2,500 psi at the lightest exposure class, climbing to 3,000 and 3,500 psi as exposure gets more severe, and whether an open patio or a covered lanai falls into a given class is something the local building official classifies, not something a crew assumes on site.</p>"
            + table("Concrete patio spec, typical build", ["Element", "Typical spec", "Why"],
                    [["Thickness", "4 in.", "Code floor is 3½ in. (FBC R506.1); the extra margin covers furniture, planters and normal settling"],
                     ["Strength", "3,000–4,000 psi", "Above the 2,500–3,500 psi weathering-class range in FBC Table R402.2"],
                     ["Base", "4 in.+ compacted fill", "Clean graded sand, gravel or crushed stone, compacted for uniform support (FBC R506.2)"],
                     ["Control joints", "~10 ft apart, ¼-depth groove", "24–36× slab thickness; panels kept close to square (NRMCA CIP 6)"],
                     ["Vapor retarder", "6-mil poly under most slabs", "FBC R506.2.3, with exceptions for unconditioned structures"]],
                    f"{src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}; {src('fbcr-2020-ch4', 'FBC Residential Ch. 4')}; {src('nrmca-cip6', 'NRMCA CIP 6')}.")),
        (photo(pids[1], "A covered patio furnished with a dining table and a sectional, open lawn behind it.") if len(pids) > 1 else ""),
        sec("Grading a patio so water moves away from the house",
            f"<p>Florida's residential code requires a lot to be graded so surface water drains away from the foundation, falling at least 6 inches over the first 10 feet, and it sets a minimum 2 percent slope, roughly a quarter inch of fall per foot, for any impervious surface within 10 feet of the building ({src('fbcr-2020-ch4', 'FBC Residential R401.3')}). "
            f"A patio poured tight against the house has to meet that number at the threshold, not just somewhere out past the edge of the slab. Orlando's airport averages 51.45 inches of rain a year and Sarasota-Bradenton's airport averages 49.05, most of it in a wet season that runs roughly late May into October, so a flat or backward-sloped patio does not wait long to prove the grading was wrong "
            f"({src('fcc-orlando-normals', 'NOAA normals, Orlando')}; {src('fcc-bradenton-normals', 'NOAA normals, Sarasota-Bradenton')}). The flatwoods soils under much of Greater Orlando and the Suncoast, Myakka, the state soil, among them, already hold a water table within 18 inches of the surface for part of most years, so a patio with the wrong fall does not just puddle once; it keeps that water sitting near the house through an entire rainy season instead of a single storm ({src('nrcs-myakka-osd', 'NRCS Myakka series')}; {src('fl-dos-state-soil', 'Florida state soil')}).</p>"),
        sec("Finish options: broom, trowel, salt finish and stain",
            "<p>A broom finish is the default on a Florida patio: dragging a broom across the surface while it is still workable leaves a texture that sheds water and gives bare feet some grip around a pool or outdoor kitchen. "
            "A smooth trowel finish reads more formal under a covered lanai where the surface rarely gets wet underfoot. A salt finish, pressing rock salt into the surface before it sets and washing out the pits once it cures, gives a pitted, non-slip texture that some coastal homeowners like for a porch or walkway. "
            f"Integral color or an acid stain changes the slab's appearance without changing the mix design, and either can go under a broom or trowel finish. None of these choices involve a pattern pressed into the concrete; the moment a homeowner wants slate, brick or wood-plank texture, that is {svc('stamped-concrete', 'stamped concrete')}, built to its own spec and sealed for the pattern to hold its color.</p>"),
        sec("Footings for a hot tub, pergola or outdoor kitchen",
            f"<p>A patio built to carry furniture and foot traffic is not automatically built to carry a hot tub full of water, a pergola's posts or a masonry outdoor-kitchen island, and the fix is a thickened edge or a dedicated footing sized to that specific load rather than pouring the whole slab heavier than it needs to be. "
            f"Several of the jurisdictions we work in draw a formal line at the same point: Clermont's own permit types separate a plain \"Concrete/Driveway/Patio\" slab on grade with no footers from one that has them ({src('clermont-permit-types', 'City of Clermont permit types')}), and Manatee County exempts a non-structural concrete or paver patio from a permit while a \"concrete slab with footers\" needs one ({src('manatee-no-permit-list', 'Manatee County permit list')}). "
            f"That decision has to happen at the design stage, since footings cannot be added later without cutting into finished concrete.</p>"),
        sec("Tying a new slab into an existing patio or lanai",
            "<p>Extending a patio means pouring new concrete against ground and an edge that have already settled for years under the old slab, and the two sections age differently once both carry weight again. "
            "We isolate the new pour from the old slab with a joint rather than bonding fresh concrete directly to it, because the new concrete will still shrink as it cures while the existing slab finished shrinking long ago; forcing them to move together is what cracks a tie-in seam within the first year or two. "
            f"Matching the new subgrade's compaction and elevation to the old slab's edge matters as much as the joint itself. A lanai or screen enclosure added onto the extension needs its own footings, poured and often inspected before the surrounding flatwork, which is the detail {post('extend-patio-under-screen-enclosure', 'our guide to extending a patio under a screen enclosure')} walks through.</p>"),
        sec("How we build a concrete patio, step by step", steps(patio_steps)),
        sec("Soil and weather this build plans around",
            f"<p>Much of Greater Orlando and the Suncoast sits on flatwoods soils, Myakka, Smyrna and EauGallie are common series, that hold a seasonal water table within 18 inches of the surface for part of most years, while ridge sands like Candler and Astatula out toward Clermont and Winter Garden drain so well the water table can sit 80 inches down ({src('nrcs-smyrna-osd', 'NRCS soil survey')}). "
            f"Both extremes change how the base compacts: wet ground often needs 2 to 4 inches more compacted fill than the code minimum, and loose dry sand needs wetting and shallow lifts so a compactor locks it together instead of pushing it sideways. "
            f"Heat works against a fresh patio in its own way: once the evaporation rate off the surface climbs past about 0.2 pounds per square foot per hour, cracking starts before the concrete finishes setting ({src('aci-ci-evap-2007', 'ACI evaporation research')}), and ACI guidance caps concrete temperature at 95°F at discharge for that reason ({src('aci-faq-maxtemp', 'ACI hot-weather FAQ')}). "
            f"We schedule hot pours early, dampen the subgrade without ponding water, and keep the surface moist for at least 3 days rather than the 7-day figure some older guidance cites ({src('nrmca-cip12', 'NRMCA CIP 12')}; {src('nrmca-cip5', 'NRMCA CIP 5')}).</p>"),
        sec("What a concrete patio costs in Florida",
            f"<p>Installed concrete patios run {price('concrete-patio')} per square foot in current Florida and national cost-guide data, with {price('concrete-patio', True)} typical for a broom or trowel finish on a straightforward job ({price_note()}). "
            f"Angi's Orlando data puts a plain patio closer to $4–$7 per square foot and prices a 450-square-foot patio at about $2,700 before site conditions change the number ({src('angi-slab-orlando', 'Angi Orlando')}). Demolition of an old slab, a soft or wet subgrade, footings for a lanai, and the finish you pick all move the price from there. "
            f"The {a('/concrete-patio-cost/', 'concrete patio cost guide')} works through those line items with full-size examples, and {compare('stamped-concrete-vs-pavers', 'stamped concrete vs. pavers')} is the place to compare against the other two patio materials on cost and upkeep.</p>"),
        sec("Permits and HOA review for a patio",
            f"<p>Whether a patio needs a permit depends on the jurisdiction and on whether it has footings. Orlando runs patio and pool-deck slabs through the same engineering permit it uses for driveways and pavers ({src('orlando-res-requirements', 'City of Orlando permitting requirements')}). "
            f"Manatee County exempts a non-structural concrete or paver patio but still requires a permit once footers are involved ({src('manatee-no-permit-list', 'Manatee County')}). The City of Sarasota has no published flatwork exemption at all and tells homeowners to call the Building Division when in doubt ({src('city-sarasota-bp-guidelines', 'City of Sarasota permit guidelines')}). "
            f"Winter Park requires a building or miscellaneous permit for any hard-surface deck or patio ({src('winterpark-do-i-need-permit', 'City of Winter Park')}). On a project over $2,500, Florida's lien law also calls for a Notice of Commencement recorded before work starts ({src('fs713-13', 'F.S. 713.13')}). "
            f"State law carves driveway-only work out of local licensing requirements, but it does not name patios the same way, so whether a given patio job needs a state-certified contractor can come down to how closely its scope matches the structural masonry category that covers slabs, footers and walls ({src('fs489-117', 'F.S. 489.117')}). "
            f"See the {a('/permits/', 'permits and HOA hub')} for the full jurisdiction list, or go straight to the county guide: {post('orange-county-orlando-driveway-patio-permits', 'Orlando and Orange County')}, {post('sarasota-county-driveway-patio-permits', 'Sarasota, Venice and North Port')} or {post('manatee-county-driveway-permits', 'Bradenton and Lakewood Ranch')}. HOA review runs on its own track; a 2026 change to state law stops an association from requiring a building permit before it reviews your application, but the appearance review itself still applies ({src('fs720-3035', 'F.S. 720.3035')}), which {post('hoa-approval-for-pavers-and-concrete', 'our HOA approval guide')} covers in more detail.</p>"),
        (photo(pids[2], "A covered patio and outdoor seating area beside a mowed lawn.") if len(pids) > 2 else ""),
        sec("Caring for a new patio",
            f"<p>A broom finish holds surface moisture in its texture longer than a sealed or trowel-finished surface, so a shaded section, under a lanai roof or mature trees, tends to pick up algae or mildew staining before a sun-exposed section of the same patio does; rinsing the shaded side on a tighter schedule heads that off. "
            f"Sweep control joints clear before rainy season so they shed water instead of trapping leaves and sand. New landscaping planted right after the pour usually qualifies for a temporary watering exemption rather than the standard restricted schedule, under either the Orlando-area rules or the Sarasota side's current once-a-week order ({src('sjrwmd-watering', 'SJRWMD watering restrictions')}; {src('swfwmd-restrictions', 'SWFWMD water shortage order')}). "
            f"A hairline crack sitting quietly along a control joint is ordinary shrinkage; a sudden dip paired with cracking that reaches toward the house is worth a call.</p>"),
        sec("Choosing a concrete patio contractor",
            f"How do you find the best concrete patio contractor near you in Orlando or Sarasota? Start with the same checklist for any flatwork bid, in writing rather than as a verbal promise ({src('dbpr', 'DBPR license search')}). " + ul([
                "A written scope with thickness, psi, base depth and finish spelled out, not just a square-foot number.",
                "A plan for drainage at the house, not just at the yard's low point.",
                "Who pulls which permit, and whether the fee is already in the estimate.",
                "A joint layout that accounts for any footings, columns or tie-ins before the pour, not after.",
            ]) + f"<p>More detail in {post('how-to-choose-a-concrete-contractor-orlando', 'how to choose a concrete contractor in Orlando')} and {post('how-to-choose-a-concrete-contractor-sarasota', 'how to choose a concrete contractor in Sarasota')}, or {contact('send us your patio dimensions')} for a written estimate.</p>"),
        sec("Where we build concrete patios",
            f"<p>Our {a('/central-florida/', 'Greater Orlando crew')} and {a('/sarasota-manatee/', 'Sarasota-Manatee crew')} each pour patios across their county list, with local notes on permits, HOAs and soil for "
            f"{cs('orlando', K, 'Orlando')}, {cs('winter-garden', K, 'Winter Garden')}, {cs('sarasota', K, 'Sarasota')} and {cs('lakewood-ranch', K, 'Lakewood Ranch')}, among other towns.</p>"),
        "<!--AUTO:service-cities-->",
    ])
    faqs = [
        faq("Can you extend my existing concrete patio or lanai slab?",
            "Usually, yes. We tie new concrete into the old slab with an isolation joint rather than bonding directly to it, since the new pour still has to shrink as it cures while the existing slab already finished shrinking. Matching the new subgrade's compaction and elevation to the old edge matters as much as the joint itself, especially if a screen enclosure's footings are part of the extension."),
        faq("How thick should a concrete patio be?",
            "4 inches is standard, at 3,000 to 4,000 psi, over at least 4 inches of compacted base. Florida's code floor for any slab on the ground is 3½ inches, so the extra half inch is margin, not a requirement. A section carrying a grill island, a hot tub or a lanai's footings needs more than the standard thickness right there, decided before the pour."),
        faq("Can a concrete patio hold a hot tub, pergola or outdoor kitchen?",
            "Yes, with a thickened edge or a dedicated footing sized to that load rather than building the whole slab heavier than it needs to be. Several local permit offices treat a footed patio differently from a plain one, so the footings have to be planned, and sometimes permitted separately, before the surrounding flatwork goes in."),
        faq("What finishes can I choose for a concrete patio?",
            "Broom finish is standard and the most slip-resistant around a pool or kitchen. Smooth trowel suits a covered, rarely-wet lanai. A salt finish gives a pitted, non-slip texture some coastal homeowners like. Integral color or acid stain changes the look without changing the mix. A pressed pattern is stamped concrete, a separate build and finish."),
        faq("How do you make sure water drains away from the house?",
            "Florida's code requires a minimum 2 percent slope, about a quarter inch per foot, for any impervious surface within 10 feet of the building, and the lot overall has to fall at least 6 inches over the first 10 feet away from the foundation. We set that grade in the subgrade before forms go up, not after the pour."),
    ]
    return page("/concrete-patios/", "service", "Concrete Patios in Florida | Orlando & Sarasota",
                "Concrete patio installation and lanai extensions in Greater Orlando and Sarasota-Manatee: thickness, drainage, finishes and Florida prices as of October 2026.",
                "Concrete patios built for Florida rain and heat",
                capsule(f"As of October 2026, a plain concrete patio in Florida runs {price('concrete-patio')} per square foot installed, typically {price('concrete-patio', True)}. We pour 4-inch slabs at 3,000–4,000 psi over a compacted base, graded at least 2 percent away from the house per Florida's building code, for homes across Greater Orlando and Sarasota-Manatee."),
                body, faqs=faqs,
                sources=["homeguide-concrete-patio", "angi-slab-orlando", "fbcr-2020-ch5", "fbcr-2020-ch4", "nrmca-cip6", "nrmca-cip12", "nrmca-cip5", "aci-faq-maxtemp", "aci-ci-evap-2007",
                         "nrcs-myakka-osd", "nrcs-smyrna-osd", "fl-dos-state-soil", "fcc-orlando-normals", "fcc-bradenton-normals", "sjrwmd-watering", "swfwmd-restrictions",
                         "clermont-permit-types", "manatee-no-permit-list", "city-sarasota-bp-guidelines", "winterpark-do-i-need-permit", "orlando-res-requirements", "fs713-13", "fs489-117", "fs720-3035", "dbpr"],
                related=[("/concrete-patio-cost/", "Concrete patio cost guide"), ("/compare/stamped-concrete-vs-pavers/", "Stamped concrete vs. pavers"),
                         ("/blog/concrete-patio-ideas-florida/", "Concrete patio ideas for Florida homes"), ("/stamped-concrete/", "Stamped concrete"),
                         ("/paver-patios/", "Paver patios & walkways"), ("/permits/", "Permits & HOA hub")],
                crumbs=[("Concrete", "/concrete/")], crumb="Concrete patios", service=K,
                hero_photo=pids[0] if pids else None, offer=offer(SERVICES[K]["price"]), eyebrow="Concrete · Greater Orlando & Sarasota",
                howto=("How a Concrete Patio Is Built", patio_steps))


def stamped_concrete():
    K = "stamped-concrete"
    pids = for_service(K, 3)
    stamp_steps = [
        ("Lay out the pattern.", "Before any concrete is ordered, the pattern, border and joint layout are planned on paper against the slab's actual shape, so a control joint lands on a grout line instead of cutting across the middle of a pattern."),
        ("Form, base and reinforce.", "The base follows the same code minimum as any slab on the ground, at least 4 inches of compacted fill, regardless of what finish goes on top. Fiber reinforcement is common under a stamped slab since mats pressed into wet concrete can push wire mesh out of position."),
        ("Pour and float.", "Concrete is screeded and bull floated to a level surface, with color hardener broadcast and floated into the top layer where the design calls for it."),
        ("Release and stamp.", "A powder or liquid release agent keeps the texture mats from sticking and leaves a secondary color in the pattern's low points. Mats are pressed in panel by panel, with hand tools working any borders and tight corners."),
        ("Cut joints and wash the release.", "Joints are sawn or routed to fall along a pattern line, and the chalky release residue is pressure washed off once the slab can be walked on."),
        ("Cure, then seal.", "The slab cures at least 3 days before sealing. The sealer, chosen with a slip-resistant additive on a pool deck, is what saturates the color and protects the pattern from UV and foot traffic."),
    ]
    body = "".join([
        sec("What stamped concrete is, and where it works",
            f"<p>Stamped concrete is a poured slab that gets a pattern pressed into it before it sets, slate, ashlar, wood-plank or cobble among the common choices, along with integral color, a release agent and a sealer to finish it off. "
            f"This page covers every stamped surface we build: driveways, patios, pool decks and walkways. Pressing a pattern into a slab is a finishing choice, not a different service for each location, so stamped concrete gets one page rather than one per surface. "
            f"If you want plain broom or trowel concrete instead, those live on {svc('concrete-driveways', 'concrete driveways')}, {svc('concrete-patios', 'concrete patios')} and {svc('concrete-pool-decks', 'concrete pool decks')}; those pages cover the base spec and process for an unstamped slab. "
            f"As of October 2026, stamped concrete in Florida runs {price('stamped-concrete')} per square foot installed, with {price('stamped-concrete', True)} typical for a one- or two-color pattern ({price_note()}).</p>"),
        sec("Patterns and color: integral, hardener or stain",
            "<p>Integral color is mixed into the concrete at the plant, tinting the full thickness of the slab, so a chip or a worn spot shows the same color underneath rather than bare gray. Color hardener is broadcast onto the surface after the pour and floated in by hand, producing a harder, more saturated top layer but one that reveals plain gray if it ever wears all the way through. "
            "A release agent, dusted or sprayed on right before the mats go down, keeps the texture from sticking and leaves a secondary antiquing color in the pattern's recessed lines once it is pressed in and washed off. "
            f"Flagstone's wide, irregular joint lines read more casual than a tight ashlar slate or running-bond brick pattern, and the pattern choice affects more than looks: wide flagstone joints can double as control joints with little extra planning, while a tighter pattern still needs true joints cut at the proper spacing, just routed along an existing line. "
            f"{post('stamped-concrete-patterns-and-colors', 'Stamped concrete patterns and colors that work in Florida')} walks through the options in more detail.</p>"),
        (photo(pids[1], "Close-up of gray stamped concrete patterned to resemble irregular hexagonal flagstone pavers.") if len(pids) > 1 else ""),
        sec("Build spec: thickness, joints and base by surface",
            "<p>Stamping is a surface finish, not a different base or thickness. A stamped driveway follows the same 4-inch, 3,000–4,000 psi standard as a plain one because it carries the same daily traffic; a stamped patio or walkway can follow the lighter patio spec since it only ever sees foot traffic and furniture; a stamped pool deck needs an isolation joint where the slab meets the coping so the deck and the shell can move independently. "
            f"Control joints still follow the same spacing rule as plain concrete, about 24 to 36 times the slab's thickness, roughly 10 feet apart on a 4-inch slab ({src('nrmca-cip6', 'NRMCA CIP 6')}), but on a stamped surface that joint is planned to land on a grout line in the pattern rather than cut as a visible groove across it.</p>"
            + table("Stamped concrete by surface", ["Surface", "Thickness / psi", "Base", "Note"],
                    [["Driveway", "4 in., 3,000–4,000 psi", "4 in.+ compacted fill", "Same vehicle-load spec as plain concrete"],
                     ["Patio / walkway", "4 in., 3,000–4,000 psi", "4 in.+ compacted fill", "Pattern and border double as part of the joint layout"],
                     ["Pool deck", "4 in., 3,000–4,000 psi", "4 in.+ compacted fill", "Isolation joint required at the coping"]],
                    f"{src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}; {src('nrmca-cip6', 'NRMCA CIP 6')}.")),
        sec("Slip resistance around a pool or wet deck",
            "<p>Stamped concrete can be slippery when wet if it is sealed with a plain, high-gloss film and nothing else, because the sealer builds up over the texture and smooths out the grip the pattern is supposed to provide. "
            "The fix is a slip-resistant additive, a fine polymer grit, mixed into the sealer on any surface that sees standing water regularly, a pool deck especially, rather than relying on the pattern's texture alone once a film sealer is on top of it. "
            f"A driveway or front walkway can often get by with a standard sealer since it dries between rains; a pool deck cannot. If an existing deck already feels slick, {post('slippery-pool-deck-fixes', 'our guide to fixing a slippery pool deck')} covers the resurfacing and resealing options without a full tear-out.</p>"),
        sec("Cracking, control joints and what's normal",
            "<p>Stamped concrete cracks for the same reasons plain concrete does: shrinkage as the slab cures, movement at an unsupported edge, or a control joint spaced too far apart. The pattern does not add extra crack resistance and it does not add extra risk by itself, but it does change where a crack is easiest to hide, "
            "since a hairline crack that follows an existing grout line reads as part of the pattern rather than as damage. Fiber mixed into the batch, more common than wire mesh under a stamped slab since mesh can get pushed out of position by the stamp mats, keeps a crack from opening wider once it forms; neither fiber nor mesh stops a crack from forming in the first place. "
            "A sudden depression paired with cracking that reaches toward the house is a different matter from ordinary shrinkage cracking along a joint line.</p>"),
        sec("How long stamped concrete lasts, and when to reseal",
            f"<p>A properly built and sealed stamped slab commonly lasts 25 to 30 years in Florida's climate, the same general range as plain concrete, as long as it is resealed on schedule ({ext('https://www.decorativeconcretetampa.com/stamped-concrete-expect-lifespan/', 'Decorative Concrete Tampa, Feb. 2024')}). "
            f"There is no fixed code interval for resealing; it depends on sun exposure, traffic and, around a pool, chlorinated splash. Florida contractor guidance generally points to resealing every 2 to 3 years, sooner on a surface in full sun or near salt air, because intense UV and heat wear an acrylic sealer down faster here than in a milder climate "
            f"({ext('https://www.concretesolutionsfl.com/blog/concrete-sealing-florida-guide/', 'Concrete Solutions FL')}). Watch for the sealer going dull or chalky, or water that stops beading on the surface, rather than counting years on a calendar; {post('stamped-concrete-maintenance-florida', 'our stamped concrete maintenance guide')} covers fading, flaking and the cleaning routine in between resealing.</p>"),
        sec("Stamped overlay vs a new pour",
            f"<p>An existing driveway, patio or pool deck in sound structural condition, no major cracking, no settlement, can sometimes take a stamped overlay instead of a full tear-out: a thin layer of polymer-modified concrete bonded to the old slab, textured and colored the same way a new pour would be. "
            f"Overlay work runs {ext('https://homeguide.com/costs/stamped-concrete-patio-cost', '$7–$15 per square foot')} nationally, generally less than a full stamped replacement because there is no demolition. An overlay is only as good as what is underneath it, though; a slab with active cracking or a settling corner will usually telegraph that movement right back through the new surface, which is when a full replacement is the better call. "
            f"{compare('resurface-vs-replace-concrete', 'Resurface or replace a concrete driveway?')} walks through that decision for plain concrete, and the same logic applies to a stamped overlay.</p>"),
        sec("Color choices and heat around a pool",
            f"<p>Lighter colors absorb less solar radiation than dark charcoal or brown tones, which is standard heat-island physics rather than anything specific to stamped concrete: the EPA notes that conventional dark paving can reach surface temperatures up to 152°F at midday, while lighter, more reflective pavements ran 10 to 16°F cooler in one Arizona pilot program "
            f"({src('epa-cool-pavements', 'EPA, cool pavements')}). Manufacturer claims for acrylic coatings like Kool Deck say the product lowers surface temperature and that its darker color options run warmer, but the manufacturer itself gives no degree figure, so we do not print one ({src('mortex-kooldeck-page', 'Mortex Kool Deck')}). "
            f"The practical takeaway for a stamped pool deck is to lean toward a lighter integral color or release color if bare feet around the pool matter to you, and to expect a dark charcoal pattern to run hotter underfoot on a sunny afternoon than a tan or gray one. {post('how-hot-do-pool-decks-get-florida', 'How hot do pool decks get in Florida?')} compares deck materials by feel in more depth.</p>"),
        sec("How we install stamped concrete, step by step", steps(stamp_steps)),
        sec("Weather and soil this build plans around",
            f"<p>Stamping adds a narrower weather window than a plain pour. Once the evaporation rate off the surface climbs past about 0.2 pounds per square foot per hour, hot, dry, breezy afternoons that Florida produces often enough, concrete stiffens faster than usual, and a crew pressing mats into a surface that has already started to set gets a blurred imprint instead of a crisp one ({src('aci-ci-evap-2007', 'ACI evaporation research')}). "
            f"Summer storms in this part of the state tend to build through the morning and break by early afternoon within a wet season running roughly late May into mid-October, so a stamped pour scheduled during that stretch starts early enough to finish stamping before a typical afternoon cell arrives. "
            f"The ground underneath matters too: flatwoods soils across much of Greater Orlando and the Suncoast, Myakka and Smyrna among the common series, hold a seasonal water table within 18 inches of the surface, which calls for a thicker compacted base than the code minimum on the wettest lots ({src('nrcs-myakka-osd', 'NRCS soil survey')}). Curing still runs at least 3 days before sealing, longer in a hot stretch ({src('nrmca-cip12', 'NRMCA CIP 12')}).</p>"),
        sec("What stamped concrete costs in Florida",
            f"<p>Stamped concrete runs {price('stamped-concrete')} per square foot installed in current Florida and national data, with {price('stamped-concrete', True)} typical for a one- or two-color pattern; multi-color, multi-layer work runs higher ({price_note()}). "
            f"A 20×20 ft stamped patio works out to roughly $3,200 to $7,600 before site conditions, and a 24×24 ft stamped driveway to roughly $6,900 to $10,400, both well above the plain-concrete figures for the same footprint. "
            f"The {a('/stamped-concrete-cost/', 'stamped concrete cost guide')} breaks that down by pattern tier, and {compare('stamped-concrete-vs-pavers', 'stamped concrete vs. pavers')} and {compare('concrete-driveway-finishes', 'broom vs. exposed aggregate vs. stamped finishes')} cover the decision against the alternatives.</p>"),
        sec("Permits and HOA review for a stamped surface",
            f"<p>A stamped driveway, patio or pool deck needs whatever permit the same surface would need unstamped; the pattern and color do not change the permit category. Orlando and Orange County require an engineering or zoning permit for the apron and for pavers alike, and a stamped driveway's apron follows the same rule ({src('orange-do-i-need-permit', 'Orange County permitting')}). "
            f"What a stamped finish does add is a second layer of review in many HOAs: an association's authority to approve the \"location, size, type, or appearance\" of a project covers color and pattern choices specifically, so clearing a building permit does not automatically clear a stamped driveway's color scheme with the architectural committee ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"Check both before ordering materials, not just the permit. See the {a('/permits/', 'permits and HOA hub')}, or the county guides for {post('orange-county-orlando-driveway-patio-permits', 'Orlando and Orange County')} and {post('manatee-county-driveway-permits', 'Bradenton, Lakewood Ranch and Palmetto')}.</p>"),
        sec("Choosing a stamped concrete contractor",
            f"Finding the best stamped concrete contractor near you in Orlando or Sarasota comes down to checking the same things any decorative work needs confirmed before a deposit changes hands. " + ul([
                "A sample panel or a recent job to see the actual color and texture in person, not just a brochure photo.",
                "Which sealer is specified, and whether it includes a slip-resistant additive for a pool deck.",
                "Whether the quote states thickness, psi and base depth, the same as it would for a plain slab.",
                "How a multi-truckload pour will be sequenced so a color seam does not land somewhere visible.",
                f"A license lookup on the state's own database before signing anything ({src('dbpr', 'DBPR license search')}).",
            ]) + f"<p>{post('how-to-choose-a-paver-contractor-orlando', 'Our guide to vetting a hardscape contractor in Orlando')} and {post('how-to-choose-a-concrete-contractor-sarasota', 'the Sarasota version')} both apply to stamped work. For a written estimate, {contact('send us the surface, size and pattern you have in mind')}.</p>"),
        sec("Where we pour stamped concrete",
            f"<p>Our {a('/central-florida/', 'Greater Orlando crew')} and {a('/sarasota-manatee/', 'Sarasota-Manatee crew')} both stamp driveways, patios and pool decks, with local permit and HOA notes for "
            f"{cs('orlando', K, 'Orlando')}, {cs('windermere', K, 'Windermere')}, {cs('sarasota', K, 'Sarasota')} and {cs('lakewood-ranch', K, 'Lakewood Ranch')}, among other towns.</p>"),
        "<!--AUTO:service-cities-->",
    ])
    faqs = [
        faq("Is stamped concrete slippery when wet?",
            "It can be, if it is sealed with a plain, high-gloss film and no slip-resistant additive. The pattern itself provides grip, but a smooth sealer coat can mask it. We mix a fine polymer grit into the sealer on any surface that sees standing water regularly, a pool deck especially, and an existing slick deck can usually be fixed without a full tear-out."),
        faq("Does stamped concrete crack?",
            "It can, for the same reasons any concrete cracks: shrinkage, an unsupported edge, or joints spaced too far apart. Control joints are planned to fall along a grout line in the pattern rather than cut as a visible groove, so ordinary shrinkage cracking tends to follow a line that is already part of the design."),
        faq("How often does stamped concrete need resealing in Florida?",
            "Every 2 to 3 years is the general range Florida contractors point to, sooner on a deck in full sun or near salt air, since UV and heat wear an acrylic sealer faster here than in a milder climate. Watch for a dull or chalky sheen, or water that stops beading, rather than counting on a fixed calendar."),
        faq("Can stamped concrete be installed over my existing slab?",
            "Often, yes, if the old surface has no major cracking or settlement. A polymer-modified overlay, textured and colored like a new pour, bonds to the existing slab for less than a full replacement. A slab that is already cracking or settling will usually telegraph that movement through the new overlay, which is when a tear-out and new pour makes more sense."),
        faq("How long does stamped concrete last?",
            "A properly built and sealed stamped slab commonly lasts 25 to 30 years in Florida, close to the range for plain concrete, provided the sealer gets reapplied on a normal schedule. Neglecting resealing shortens that: UV and traffic wear through an unprotected sealer well before the concrete itself is at risk."),
        faq("Which stamped concrete colors stay coolest around a pool?",
            "Lighter tones, tan, buff and light gray, absorb less heat than dark charcoal or brown, the same physics behind any light-colored pavement running cooler than a dark one. No manufacturer publishes a verified degree-by-degree comparison for stamped color options specifically, so treat it as a real but unmeasured difference and plan accordingly if bare feet around the pool are a priority."),
    ]
    return page("/stamped-concrete/", "service", "Stamped Concrete in Florida | Patios, Driveways & Pool Decks",
                "Stamped concrete patios, driveways and pool decks in Greater Orlando and Sarasota-Manatee: patterns, spec, slip resistance and Florida prices, Oct. 2026.",
                "Stamped concrete for driveways, patios and pool decks",
                capsule(f"As of October 2026, stamped concrete in Florida runs {price('stamped-concrete')} per square foot installed, typically {price('stamped-concrete', True)}, across driveways, patios, walkways and pool decks. We build to the same thickness and joint spec as plain concrete, cure at least 3 days, and seal with a slip-resistant additive on wet surfaces for homes across Greater Orlando and Sarasota-Manatee."),
                body, faqs=faqs,
                sources=["homeguide-stamped", "homeguide-concrete-driveway", "fbcr-2020-ch5", "nrmca-cip6", "nrmca-cip12", "aci-ci-evap-2007", "nrcs-myakka-osd", "epa-cool-pavements", "mortex-kooldeck-page",
                         "orange-do-i-need-permit", "fs720-3035", "dbpr"],
                related=[("/stamped-concrete-cost/", "Stamped concrete cost guide"), ("/compare/stamped-concrete-vs-pavers/", "Stamped concrete vs. pavers"),
                         ("/compare/concrete-driveway-finishes/", "Broom vs. exposed aggregate vs. stamped"), ("/blog/stamped-concrete-patterns-and-colors/", "Stamped concrete patterns and colors"),
                         ("/concrete-patios/", "Concrete patios"), ("/permits/", "Permits & HOA hub")],
                crumbs=[("Concrete", "/concrete/")], crumb="Stamped concrete", service=K,
                hero_photo=pids[0] if pids else None, offer=offer(SERVICES[K]["price"]), eyebrow="Concrete · Greater Orlando & Sarasota",
                howto=("How Stamped Concrete Is Installed", stamp_steps))


def get_pages():
    return [concrete_patios(), stamped_concrete()]
