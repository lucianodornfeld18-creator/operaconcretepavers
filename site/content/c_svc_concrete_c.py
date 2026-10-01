# -*- coding: utf-8 -*-
"""Service pages: concrete slabs (accessory pads) and concrete repair & resurfacing."""
from _helpers import (page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext,
                       price, per, tel, contact, photo, offer)
from _photos import for_service

CRUMBS = [("Concrete", "/concrete/")]


def slabs():
    K = "concrete-slabs"
    pids = for_service(K, 3)
    body = "".join([
        sec("What this page covers, and what it doesn't",
            "<p>A concrete slab, in the sense this page means it, is a flat pour that supports something sitting on the ground rather than a room "
            "people live in: a shed floor, a carport or detached-garage floor, a pad for an HVAC condenser, pool pump or portable generator, or a "
            "parking pad for an RV or boat trailer. We also pour the slab for a garage or small addition, working from plans an engineer or "
            "designer has already drawn. What this doesn't cover is the structural foundation for a new, habitable room; that falls under the "
            f"state-certified structural masonry specialty contractor category rather than ordinary accessory flatwork ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). "
            f"For a driveway specifically, see {svc('concrete-driveways', 'our concrete driveway page')}; for a back patio, {svc('concrete-patios', 'concrete patios')}.</p>"
            + (photo(pids[0], "A broad concrete driveway runs up to a house with two garage doors.") if pids else "")),
        sec("Thickness, strength and reinforcement: it depends on what sits on the slab",
            "<p>Florida's residential code sets 3½ inches as the minimum thickness for a slab on the ground, but that floor is written for an "
            "ordinary interior room, not for what actually sits on an accessory pad. A shed floor or a generator pad carrying a light, evenly "
            "spread load can stay close to the common 4-inch, 3,000 to 4,000 psi pour used for most flatwork. A pad built for an RV, a boat "
            "trailer or a work truck needs the jump a driveway makes under those loads, 5 to 6 inches, because the weight concentrates on a "
            f"narrow wheel path instead of spreading evenly ({src('fbcr-2020-ch5', '2020 FBC Residential Ch. 5')}). Garage floors, carports and "
            "porches answer to a separate strength table tied to weathering exposure rather than one flat number.</p>"
            + table("Concrete slab specs by use", ["Pad type", "Typical thickness", "Strength", "Note"],
                    [["Shed or storage floor", "4 in", "2,500–3,000 psi", "Code minimum is 3½ in; 4 in is the common practical floor"],
                     ["Generator, HVAC or pool-equipment pad", "4 in", "2,500–3,000 psi", "Set slightly proud of grade so runoff drains away from the unit"],
                     ["Detached garage or carport floor", "4–5 in", "2,500 (negligible), 3,000 (moderate) or 3,500 psi (severe weathering)", "Strength set by the weathering-exposure table, not a flat number"],
                     ["RV or boat parking pad", "5–6 in", "3,500–4,000 psi", "Thickened along the wheel path or reinforced for the point load"],
                     ["Garage addition or room slab (engineered)", "Per engineer's plan", "Per engineer's plan", "Structural scope; outside ordinary accessory flatwork"]],
                    f"2020 FBC Residential Ch. 4–5 strength and thickness tables ({src('fbcr-2020-ch4', '2020 FBC Residential Ch. 4')}, {src('fbcr-2020-ch5')}); "
                    "national thickness-to-price breakdown for context "
                    f"({src('homeguide-concrete-slab', 'HomeGuide')}).")
            + "<p>A slab that will carry a stud wall along one edge, a garage addition tying into the house is the usual case, gets a thickened "
              "perimeter rather than the same 4 inches all the way to the form, so the wall's load spreads over more concrete instead of "
              "concentrating on an edge built for foot traffic. Wire mesh or dispersed fiber goes into every pour as baseline reinforcement; "
              "neither one stops a crack from forming, but both hold a crack together once it does, which is also why they don't substitute "
              f"for the right thickness in the first place ({src('nrmca-cip6', 'NRMCA CIP 6')}). A 6-mil polyethylene vapor retarder goes under "
              "most slabs on the ground, with an exception the code carves out for garages and unheated accessory structures; a shed that will "
              f"stay unconditioned storage can usually skip it, a space meant to become a finished room later should not ({src('fbcr-2020-ch5')}).</p>"),
        sec("Control joints: sized to the slab, not applied by habit",
            "<p>Joint spacing runs roughly 24 to 36 times the slab's thickness, about 8 to 12 feet apart on a standard 4-inch pour, with 15 feet "
            "as the ceiling before a panel is too large to control where it cracks. A 10-by-10 or 10-by-12 shed pad can sometimes get by on "
            "perimeter joints alone, since the whole slab already sits inside that spacing, while a 24-by-24 garage floor or a longer RV pad "
            f"needs an interior layout of roughly square panels ({src('nrmca-cip6')}). Groove depth runs at least a quarter of the slab's "
            "thickness, and early-entry saw cuts go in within a few hours of finishing so the joint, not a random crack, opens first.</p>"),
        sec("Sizing a slab: how much bigger than the structure it should be",
            "<p>A pad is sized to the footprint of what sits on it plus a small working margin, not to a round number picked in advance. A shed "
            "pad usually runs the shed's footprint plus 6 to 12 inches on each side so the walls don't overhang bare ground, with a little extra "
            "apron out front for the door. An RV or boat pad is sized to the trailer's length and width with room for the tongue jack and, often, "
            f"a side strip for stepping out of the vehicle; the full breakdown by vehicle type is in {post('concrete-pad-for-rv-or-boat-parking', 'adding an RV or boat parking pad in Florida')}, "
            f"and shed-specific sizing and tie-down detail is in {post('shed-slab-guide-florida', 'our shed slab guide')}.</p>"
            + (photo(pids[1], "A worker finishes the surface of a freshly poured concrete slab.") if len(pids) > 1 else "")),
        sec("How a slab goes in, step by step",
            "<p>The sequence is the same whether the pour is a 10-by-10 shed pad or a 400 sq ft garage floor; only the scale of each step changes.</p>"
            + steps([("Lay out and survey the footprint.", "Stake the pad against the structure it will carry or, for an addition, against the existing house corners, and check the setback to the property line."),
                     ("Excavate and compact the subgrade.", "Remove soft or organic topsoil and compact the exposed ground in shallow lifts before any base material goes down."),
                     ("Set forms and place the base.", "Forms define the pad's exact dimensions; a granular base goes down and is compacted to support the slab evenly."),
                     ("Place the vapor retarder and reinforcement, where required.", "A 6-mil poly sheet goes down on conditioned or future-conditioned space, with wire mesh or fiber mixed through the mix for every pour."),
                     ("Pour, screed and float.", "Concrete is placed, struck level with the forms, and floated to bring the finish together before it sets."),
                     ("Cut control joints and finish the surface.", "Joints are cut within a few hours of finishing, and the surface gets a broom, trowel or other finish depending on use."),
                     ("Cure for at least three days before loading.", "Curing compound or wet curing keeps the surface moist while the concrete gains the strength it needs to carry weight.")])
            + "<p>A single shed or generator pad is often a one-day pour with a separate forming day ahead of it; a garage floor or a larger RV pad "
              f"usually runs two to three days from forms to final finish. {post('concrete-curing-in-florida-heat', 'How concrete cures in Florida heat and humidity')} "
              f"covers why the first three days matter more here than in a milder climate, and {post('pouring-concrete-in-florida-rainy-season', 'pouring concrete in rainy-season Florida')} "
              "explains how a pour gets scheduled around an afternoon storm.</p>"),
        sec("What Florida ground does to a small pad, and how we build around it",
            "<p>A shed or garage pad sits on the same ground a driveway would, and flatwoods soils common across both service areas, Myakka, "
            "Smyrna and EauGallie among them, hold a seasonal water table within about 18 inches of the surface for part of most years. "
            "Treating a small pad as too minor to need real subgrade work, skipping the removal of saturated native soil and the compacted fill "
            f"that replaces it, is how a light structure ends up with a door that no longer closes square a season or two later ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). "
            "On the drier sand-ridge soils west of Orlando, Candler and Astatula among them, the opposite problem shows up: loose, excessively "
            "drained sand that won't lock together under a compactor without being wetted first, so the same shallow-lift compaction a driveway "
            f"gets applies to a garage floor on that kind of ground too ({src('nrcs-candler-osd', 'NRCS, Candler series')}).</p>"
            "<p>Grading matters even on a small pour. A pad poured flat, or slightly bowl-shaped, holds rainwater against its own edge instead of "
            "shedding it, and standing water against a compacted base does the same slow damage to a shed pad that it would to a driveway, just "
            "with less room for error on a smaller pour. Checking a new pad's planned elevation against the house's finished floor before forming "
            "starts also catches a common mistake: a detached pad lower than the surrounding grade becomes the yard's low point during a storm, "
            "no matter how level and well compacted the slab itself is. Hot, humid afternoons change the finishing window too; concrete placed "
            "above 95°F, or where the evaporation rate crosses 0.2 lb/ft² per hour, can crust on top before the slab underneath has set, which is "
            f"why an early start and a curing compound applied right after finishing matter on a shed pad the same as on a driveway ({src('nrmca-cip12', 'NRMCA CIP 12')}, "
            f"{src('nrmca-cip5', 'NRMCA CIP 5')}).</p>"),
        sec("Cost: what a slab runs in Florida",
            f"<p>Installed concrete slabs run {price('concrete-slab')} per {per('concrete-slab')} in current Florida market data, typically "
            f"{price('concrete-slab', True)} depending on thickness, mix and site access; a plain 4-inch shed floor sits near the low end, a "
            f"6-inch RV pad with heavier reinforcement near the high end ({src('homeguide-concrete-slab', 'HomeGuide')}, {src('angi-slab-orlando', 'Angi Orlando')}). "
            "These are market ranges pulled from published Florida and national pricing as of October 2026, not a quote for a specific yard; what "
            "a small pad actually costs depends more on mobilization, demolition of whatever was there before and how far the truck has to reach "
            f"than on the square footage alone. The {a('/concrete-slab-cost/', 'concrete slab cost guide')} works through sizes from a small generator "
            "pad to a full garage floor.</p>"),
        sec("Permits: when a pad needs one, and when HB 803 covers it",
            "<p>Since July 1, 2026, Florida law exempts single-family homeowners and their contractors from a local building permit for work "
            "valued under $7,500, as long as the scope isn't structural and the property isn't in a flood-hazard area, which covers a fair "
            f"number of shed, generator and small parking pads, though it still requires filing a written exemption request ({src('orlando-hb803-guide', 'City of Orlando HB 803 guide')}). "
            "A garage addition slab tied into the house's structure is a different case, far more likely to need the full permit and inspection "
            "process since it falls inside the structural masonry scope rather than the accessory-pad exemption.</p>"
            + table("Slab permits, selected jurisdictions (checked October 2026)", ["Jurisdiction", "What applies", "Notes"],
                    [["City of Kissimmee", "Building permit, type \"Slab With/Without Footer\"", "Separate from the driveway/sidewalk permit track"],
                     ["City of Orlando", "Engineering permit for pavers, asphalt or concrete, including pads", "Same permit track used for driveways and patios"],
                     ["Manatee County (unincorporated)", "No permit for a non-structural concrete slab", "A slab with footers, or one carrying a structure, still needs one"],
                     ["Statewide (HB 803)", "No building permit under $7,500 for non-structural work outside flood zones", "Written exemption request still required; doesn't cover structural additions"]],
                    f"{src('kissimmee-permit-types', 'City of Kissimmee')}; {src('orlando-res-requirements', 'City of Orlando')}; "
                    f"{src('manatee-no-permit-list', 'Manatee County')}; {src('orlando-hb803-guide', 'City of Orlando')}.")
            + "<p>On a contract over $2,500, Florida's lien law requires a recorded Notice of Commencement before work starts regardless of which "
              f"permit track applies ({src('fs713-13', 'F.S. 713.13')}), and since 2026 an HOA can't require a government permit as a condition of "
              f"reviewing your application first ({src('fs720-3035', 'F.S. 720.3035')}). A county-by-county breakdown is in "
              f"{post('orange-county-orlando-driveway-patio-permits', 'our Orange County and Orlando permit guide')} and "
              f"{post('manatee-county-driveway-permits', 'Manatee County permits')}; if your pad is already failing rather than new, "
              f"{compare('resurface-vs-replace-concrete', 'resurface or replace')} walks through that decision instead.</p>"),
        sec("Caring for a slab after it's poured",
            "<p>An accessory pad needs less upkeep than a driveway, but the same basics apply. Keep stored boxes and landscaping clear of the "
            "control joints along a shed or garage pad's perimeter so leaves and mulch don't pack into them and hold water against the edge. "
            "A pad's original grading can stop shedding water the way it was built to once a few years of landscaping or settling soil change "
            "how the yard drains around it, so walking the perimeter after yard work and confirming it still slopes away is worth five minutes. "
            "A crack lined up with a boat trailer's wheel path or a tongue jack's bearing point deserves more attention than ordinary shrinkage "
            f"cracking along a joint elsewhere, since the first points to a load the slab wasn't sized for; {svc('concrete-repair', 'our concrete repair service')} "
            "covers what to do once a pad is actually settling rather than just aging.</p>"
            + (photo(pids[2], "Clean, broom-finished concrete with cut control joints running toward a garage.") if len(pids) > 2 else "")),
        sec("How do you pick the right contractor for a slab pour?",
            "<p>Searching for a concrete slab contractor near me mostly turns up driveway specialists; a smaller pad still deserves the same questions.</p>"
            + ul(["Ask for the thickness and strength in writing, tied to what will actually sit on the pad, not a generic number.",
                  "Confirm whether the pad needs a permit, and if it falls under the HB 803 exemption, who files the written request.",
                  "For a garage addition tied into the house, confirm the scope is treated as structural work with the sign-off that requires.",
                  f"Check a contractor doing structural masonry work against the {src('dbpr-search', 'DBPR license search')}; driveway and pad flatwork alone sits outside that requirement.",
                  "Ask how the crew handles a pad with no direct truck access, since that usually means a pump or wheelbarrow relay and a longer day."])
            + f"<p>{post('how-to-choose-a-concrete-contractor-orlando', 'Our Orlando concrete contractor checklist')} and "
              f"{post('sinkholes-and-settlement-central-florida', 'sinkholes vs. normal settlement in Central Florida')} go further into questions worth asking before a pour.</p>"),
        sec("Where we pour slabs",
            f"<p>We pour slabs across Greater Orlando and Sarasota–Manatee, each quoted by the crew that knows that county's permit desk. "
            f"Related towns: {cs('orlando', K)}, {cs('kissimmee', K)}, {cs('sarasota', K)} and {cs('bradenton', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("What size slab do I need for my shed?",
                "Size the pad to the shed's footprint plus about 6 to 12 inches of margin on each side so the walls don't sit on bare ground, with a little extra apron in front of the door for foot traffic. A 10×12 shed usually gets an 11×13 or 12×14 pad. Thickness and reinforcement depend on what's stored inside, not the footprint; our shed slab guide walks through both together."),
            faq("Can you pour a slab for a detached garage or carport?",
                "Yes. A detached garage or carport floor typically runs 4 to 5 inches thick at a strength set by Florida's weathering-exposure table, and we thicken the perimeter where a stud wall will bear on the slab. If the structure is being tied into the house as an addition rather than standing alone, that shifts into engineered, structural scope with its own permit path."),
            faq("Do you pour pads for generators, AC units and pool equipment?",
                "Yes, and it's common work after hurricane season in both service areas. These pads are usually 4 inches thick, set slightly above the surrounding grade so water drains away from the equipment rather than pooling under it, and sized a few inches larger than the unit's footprint on each side for service access."),
            faq("How do you keep a slab from settling in sandy Florida soil?",
                "By treating the subgrade as its own step, not an afterthought: removing soft or saturated native soil, bringing in compacted fill in shallow lifts, and grading the finished pad to shed water away from its own edges. Flatwoods soils with a shallow seasonal water table and loose ridge sands both need that same compaction discipline, just for different reasons."),
            faq("Do you pour house foundations or room additions?",
                "We pour the slab portion of a garage or small addition from an engineer's or designer's plans, but a full habitable-room foundation falls under Florida's state-certified structural masonry specialty contractor scope rather than ordinary accessory flatwork. We'll tell you plainly when a project needs that engineered path instead of a standard pad."),
            faq("What is the smallest slab or job you will take?",
                "A single generator pad or a small shed floor is a normal job for us, though the cost per square foot runs higher on a small pour than a large one, since forming, mobilization and a minimum crew day cost about the same whether the slab is 60 sq ft or 600. Ask for a quote and we'll tell you honestly if a job is too small to be worth scheduling a crew for.")]
    return page("/concrete-slabs/", "service", "Concrete Slab Installation | Orlando & Sarasota, FL",
                "Concrete pads for sheds, carports, AC and generator units, RV and boat parking, and garage slabs. Florida market range as of October 2026.",
                "Concrete Slabs Sized and Based for What Sits on Them",
                capsule("A concrete slab for a shed, carport, generator, RV pad or garage floor is sized, thickened and reinforced for what it will "
                        "actually carry, not poured to one default spec. As of October 2026, installed slabs run $4–$10 per sq ft in Florida market "
                        "data, with thickness and base work doing more to decide cost than square footage alone. We pour accessory pads and slabs "
                        "across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["fac61g4-15-100", "fbcr-2020-ch4", "fbcr-2020-ch5", "nrmca-cip6", "nrmca-cip12", "nrmca-cip5", "nrcs-myakka-osd", "nrcs-candler-osd",
                         "homeguide-concrete-slab", "angi-slab-orlando", "orlando-hb803-guide", "kissimmee-permit-types", "orlando-res-requirements",
                         "manatee-no-permit-list", "fs713-13", "fs720-3035", "dbpr-search"],
                related=[("/concrete-slab-cost/", "concrete slab cost guide"), ("/compare/resurface-vs-replace-concrete/", "resurface or replace concrete"),
                         ("/compare/concrete-driveway-finishes/", "concrete driveway finishes compared"),
                         ("/blog/shed-slab-guide-florida/", "shed slabs in Florida"), ("/blog/concrete-pad-for-rv-or-boat-parking/", "RV and boat parking pads"),
                         ("/blog/sinkholes-and-settlement-central-florida/", "sinkholes vs. normal settlement"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=CRUMBS, crumb="Concrete slabs", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("concrete-slab"), eyebrow="Concrete · Greater Orlando & Sarasota",
                howto=("How a concrete slab is poured", [("Lay out and survey the footprint", "Stake the pad against the structure or house it ties into, and check the property-line setback."),
                                                          ("Excavate and compact the subgrade", "Remove soft topsoil and compact the exposed ground in shallow lifts."),
                                                          ("Set forms and place the base", "Forms define the pad's dimensions; granular base is compacted to support the slab evenly."),
                                                          ("Place vapor retarder and reinforcement", "A 6-mil poly sheet where required, plus wire mesh or fiber mixed through the pour."),
                                                          ("Pour, screed and float", "Concrete is placed, struck level and floated before it sets."),
                                                          ("Cut joints and finish", "Control joints are cut within hours of finishing, and the surface gets its final texture."),
                                                          ("Cure at least three days before loading", "Curing compound or wet curing keeps the surface moist while strength develops.")]))


def repair():
    K = "concrete-repair"
    pids = for_service(K, 3)
    body = "".join([
        sec("What's actually wrong with a cracked, sunken or pitted slab",
            "<p>Concrete repair covers four different problems, and the fix depends on telling them apart before anything else. A crack that "
            "isn't widening and isn't tied to a sunken panel is usually a cosmetic or shrinkage crack, treated by filling it. A slab that's "
            "settled into a dip is almost always missing material under it, a void that formed when water carried sand and fines out through a "
            "joint or crack over several rainy seasons, and that's a leveling job, mudjacking or polyurethane foam injection, rather than a "
            "surface fix. A slab that's scaled, pitted or faded but structurally sound is a resurfacing candidate, a new bonded layer over the "
            "old one. And a panel that's cracked into several independent pieces, or badly broken at an edge, usually needs to come out and be "
            f"replaced rather than patched. {svc('concrete-driveways', 'Our concrete driveway page')} and {svc('concrete-slabs', 'concrete slabs page')} "
            "cover new construction; this page is specifically about fixing what's already there.</p>"
            + (photo(pids[0], "Broom-finished concrete with cut control joints leading to a garage.") if pids else "")),
        sec("Crack filling and sealant: for a crack that isn't moving",
            "<p>A hairline or moderate crack that hasn't widened recently and isn't sitting over a void gets treated as a linear repair rather "
            "than a surface one: a flexible filler or sealant worked directly into the crack, priced by the linear foot rather than the square "
            f"foot. Orlando-area pricing for this runs roughly $0.50 to $5 per linear foot depending on the crack's width and depth ({src('angi-driveway-repair-orlando', 'Angi Orlando')}). "
            "It's a maintenance step for a crack that's stable, not a fix for one that's actively opening, since filler alone does nothing about "
            f"whatever is still moving underneath. {post('concrete-driveway-cracks-florida', 'Why concrete cracks, and which cracks are normal')} "
            "covers how to tell ordinary shrinkage cracking from a crack that needs more than a bead of sealant.</p>"),
        sec("Leveling a sunken slab: mudjacking versus polyurethane foam",
            "<p>Both methods raise a settled panel back toward grade by filling the void underneath it, working through small holes drilled "
            "across the sunken area, without demolishing the slab. They part ways on what goes into the hole and how much it weighs once it's "
            "there.</p>"
            + table("Slab leveling methods compared", ["Method", "Cost (national)", "Hole size", "Best fit"],
                    [["Mudjacking (mud-jacking)", "$4–$9/sq ft; $300–$700 minimum", "About 1–2 in", "Firm, well-drained soil that can carry the grout's added weight"],
                     ["Polyjacking (foam)", "$8–$25/sq ft; $300–$700+ minimum", "About ⅝ in", "Soft, saturated or flatwoods ground where added weight is a risk"]],
                    f"{src('homeguide-mudjacking', 'HomeGuide, mudjacking')}; {src('homeguide-polyjacking', 'HomeGuide, polyjacking')}. "
                    f"Orlando mudjacking runs $3–$8/sq ft, averaging about $1,667 per job ({src('angi-mudjacking-orlando', 'Angi Orlando')}).")
            + "<p>Mudjacking pumps a soil-cement-water slurry under the slab that carries real weight once it sets, which matters on ground "
              "that's already struggling to hold the concrete above it. Polyurethane foam expands into the same kind of void but weighs a "
              "fraction as much, which is usually the better call on soft or saturated soil, the flatwoods ground common across both service "
              "areas, where adding more weight under an already-settling panel can bring the same problem back within a year or two. Either "
              "way, leveling only works if the slab itself is sound enough to rise as one piece; a panel cracked into several independent "
              "sections doesn't lift evenly and calls for cut-out-and-replace instead.</p>"),
        sec("Resurfacing and overlays: a new surface, not a new base",
            "<p>A bonded resurfacing overlay is a thin cementitious layer applied over a bonding agent so it grips the existing slab instead of "
            "sitting on top of it loosely. It changes nothing about what's a few inches below the surface, which is exactly why it only works "
            "on a slab whose problem is cosmetic, pitting, scaling or hairline surface cracking, and not on a panel that's actively settling "
            "into a void. A basic decorative overlay runs roughly $6 to $10 per square foot nationally, and a stamped or textured overlay runs "
            f"$7 to $20, higher for a multi-color design ({src('homeguide-concrete-resurfacing', 'HomeGuide')}). Driveway resurfacing specifically runs "
            f"$3 to $5 per square foot, and a 2-car driveway typically totals $1,200 to $2,900 ({src('homeguide-concrete-resurfacing')}). Pool-deck "
            f"resurfacing has its own pricing and finish options, covered on {svc('concrete-pool-decks', 'our concrete pool deck page')} rather than here.</p>"),
        sec("Cut-out-and-replace: when repair won't hold",
            f"<p>Installed concrete repair work, section replacement and resurfacing together, runs {price('concrete-repair')} per {per('concrete-repair')} "
            f"in current Florida market data, typically {price('concrete-repair', True)}; a full tear-out and replacement of damaged sections in "
            f"Orlando runs higher, $10 to $15 per square foot, since it includes demolition, base rebuild and a full new pour rather than a "
            f"surface treatment ({src('angi-driveway-repair-orlando', 'Angi Orlando')}). A replaced panel is built to the same thickness and strength "
            "as the surrounding slab, 3,000 to 4,000 psi for typical residential flatwork, with a clean saw-cut edge and steel dowels tied into "
            "the adjoining panels so the new section moves with the old rather than settling on its own. These are Florida and national market "
            "figures current as of October 2026, not a quote; what a given repair costs turns on how many panels are affected and how the crew "
            f"reaches them. The {a('/concrete-repair-cost/', 'concrete repair cost guide')} breaks this down by job size, and "
              f"{compare('resurface-vs-replace-concrete', 'our resurface-or-replace comparison')} walks through the decision in more detail than fits here.</p>"),
        sec("The repair sequence, start to finish",
            "<p>The order changes by method, but every repair starts the same way: figuring out why the slab cracked or sank before picking a "
            "fix off a list.</p>"
            + steps([("Diagnose before quoting a method.", "Check whether there's a void under the slab, whether a crack is still moving, and whether the surrounding panels are sound enough for an overlay or a lift."),
                     ("Fill or seal a stable crack.", "A flexible sealant is worked into a crack that isn't tied to settlement, priced by the linear foot."),
                     ("Lift a settled panel by injection.", "Mudjacking grout or polyurethane foam is pumped through small drilled holes until the panel reaches grade, then each hole is patched."),
                     ("Prep and apply a resurfacing overlay.", "The slab is pressure washed, spalls and wide cracks are patched, then the bonded overlay goes down and is sealed once cured."),
                     ("Cut out and replace a failed panel.", "The damaged section is saw-cut, demolished and hauled off, the base is rebuilt and compacted, dowels are set, and the new panel is formed and poured to match."),
                     ("Cure before returning the area to use.", "At least three days of curing before regular traffic, longer for a replaced panel in summer heat.")])
            + f"<p>A mudjacking or polyjacking day usually wraps in hours once the void is confirmed; a resurfacing overlay adds a day for prep "
              f"and another for the overlay and sealer; a cut-out-and-replace job runs closest to new construction, including the three-day cure. "
              f"{post('concrete-curing-in-florida-heat', 'How concrete cures in Florida heat and humidity')} covers why that cure window matters "
              "more here than in a milder climate.</p>"
            + (photo(pids[1], "Finishing a slab's surface with a trowel before the concrete sets.") if len(pids) > 1 else "")),
        sec("What causes the damage in the first place, and why it keeps coming back if the cause isn't fixed",
            "<p>Nearly every repair traces back to water finding a path into or under the slab: through an open joint, a crack left unsealed, "
            "or a base that was never compacted to standard in the first place. On flatwoods soils with a water table that sits within about 18 "
            "inches of the surface for part of most years, Myakka, Smyrna and EauGallie among the common series, that erosion process runs faster "
            f"than it does on drier ground ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). A driveway can look stable for a long stretch and "
            "then develop a noticeable dip in a single wet season once the void underneath finally collapses under traffic, which is why a repair "
            "that only addresses the surface, resurfacing over an active void, rarely holds past the next rainy season.</p>"
            "<p>Tree roots are a separate, mechanical cause: a root running under a slab's edge lifts rather than sinks the concrete, which "
            f"needs a different fix than a settled panel does, covered in {post('tree-roots-under-driveway-florida', 'tree roots under your driveway or sidewalk')}. "
            "A sunken slab is also not the same thing as a sinkhole. Florida's insurance statute requires coverage only for a catastrophic "
            "ground-cover collapse, an abrupt event with a visible depression and structural damage severe enough that the building is condemned; "
            "ordinary settlement from a washed-out base is a far more common and far less dramatic cause, and a state Senate report found more "
            "than 88 percent of Florida's sinkhole insurance claims concentrated in eleven counties, with Orange among them and Sarasota and "
            f"Manatee absent from that list ({src('fs-627-706', 'F.S. 627.706')}, {src('fl-senate-2011-104', 'FL Senate Interim Report 2011-104')}). "
            f"{post('sinkholes-and-settlement-central-florida', 'Sinkholes vs. normal settlement in Central Florida')} goes through how to tell the "
            "difference before calling a geologist instead of a repair crew.</p>"),
        sec("Permits and HOA notice for a repair job",
            "<p>A repair that doesn't change a slab's footprint, filling a crack, leveling by injection, or resurfacing within the existing "
            "edges, typically doesn't trigger the same permit review a new driveway or patio does, though a full cut-out-and-replace of a "
            "right-of-way apron or a structural section can fall back under the ordinary flatwork permit for that jurisdiction. Manatee County's "
            "published list of work that doesn't require a permit covers routine non-structural repair; Orange County and the City of Orlando "
            f"route larger section replacements through the same engineering permit used for new concrete and pavers ({src('manatee-no-permit-list', 'Manatee County')}, "
            f"{src('orange-do-i-need-permit', 'Orange County')}). On a contract over $2,500, the lien-law Notice of Commencement still applies "
            f"regardless of whether the job needs a building permit ({src('fs713-13', 'F.S. 713.13')}). An HOA with architectural control over "
            "a driveway or patio's appearance can generally require notice of a repair that changes color or finish, color-matched resurfacing "
            "is the most common trigger, even where the repair itself needs no government permit; "
            f"{post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for a driveway, pavers or a pool deck')} covers that process.</p>"),
        sec("Setting expectations: a repair rarely matches the old concrete exactly",
            "<p>New concrete and old concrete age differently. A freshly poured patch or a replaced panel starts out a slightly different "
            "shade than the slab around it, and even with a close color match at mix time, each section cures and weathers at its own rate, "
            "so a visible line between old and new is a normal, cosmetic outcome rather than a sign the work was done wrong. A resurfacing "
            "overlay covers the whole visible surface in one pass, which is why it reads as more uniform than a cut-out repair, where only "
            "the replaced section is new. We set this expectation before the job starts rather than after, since a structurally sound repair "
            "that's visibly newer than its surroundings is still a successful repair.</p>"
            + (photo(pids[2], "A broad concrete driveway runs up to a house with two garage doors.") if len(pids) > 2 else "")),
        sec("How do you choose the right repair, and the right contractor, for a damaged slab?",
            "<p>Searching for concrete repair near me usually returns a mix of driveway installers and dedicated leveling companies; a few "
            "questions sort out which one actually fits the problem.</p>"
            + ul(["Ask for a diagnosis before a method. A quote for resurfacing or mudjacking written before anyone checks for a void or confirms a crack has stopped moving is a guess with a price attached.",
                  "For a sunken panel, ask whether mudjacking or polyjacking is recommended and why; the soil underneath, not personal preference, should drive that choice.",
                  "Get the cut-out panel's thickness, strength and dowel detail in writing if replacement is recommended, not just a square-footage price.",
                  f"Check a repair contractor's standing on the {src('dbpr-search', 'DBPR license search')} if the scope includes structural work beyond ordinary flatwork repair.",
                  "Ask directly whether the same spot has failed before on this driveway or patio, since a repeat failure usually points to an uncorrected drainage cause, not a weak original repair."])
            + f"<p>{post('should-you-seal-a-concrete-driveway-florida', 'Should you seal a concrete driveway in Florida?')} and "
              f"{post('rust-and-irrigation-stains-on-concrete-pavers', 'removing rust and sprinkler stains')} cover the surface-care side of keeping "
              "a repaired slab from needing the same fix again.</p>"),
        sec("Where we repair concrete",
            f"<p>We handle concrete repair across Greater Orlando and Sarasota–Manatee. Related towns: {cs('orlando', K)}, {cs('winter-garden', K)}, "
            f"{cs('sarasota', K)} and {cs('venice', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("Can you repair just the cracked part of my driveway?",
                "Often, yes. A single damaged panel can usually be cut out and replaced without touching the rest of the driveway, tied into the adjoining sections with steel dowels so it moves with them rather than as an independent piece. Whether that's the right call instead of resurfacing or replacing the whole driveway depends on how many panels are affected; our resurface-or-replace comparison walks through that decision."),
            faq("Does crack filler work on concrete driveway cracks?",
                "For a hairline or moderate crack that's stable, not actively widening and not sitting over a settled area, a flexible sealant worked into the crack is an effective, inexpensive fix priced by the linear foot. It doesn't address a crack caused by a void underneath or ongoing movement; filling that kind of crack without fixing the cause usually means doing it again within a season or two."),
            faq("How long does concrete resurfacing last on a driveway?",
                "There's no fixed number in the industry's own guidance, since it depends heavily on the condition of the base and slab underneath the overlay and how the surface is used and sealed afterward. Resurfacing applied over a sound, stable slab with cosmetic wear holds up well; applied over a slab that's still settling, it tends to crack again in roughly the same place within a wet season or two."),
            faq("Can you fix a trip hazard where a slab has lifted?",
                "Yes, and the fix depends on the cause. A lift from a tree root usually needs grinding the raised edge down or cutting and resetting that section, since the root is still pushing from below. A lift from one panel settling lower than its neighbor is more often a leveling job on the low side rather than grinding the high one."),
            faq("Can you level a sunken concrete slab?",
                "Yes, by mudjacking or polyurethane foam injection, both of which fill the void under the slab through small drilled holes and raise the panel back toward grade without demolishing it. Which method we recommend depends on the soil condition under your slab; foam is usually the better fit on soft or saturated ground, since it adds far less weight than mudjacking's slurry does."),
            faq("Will the repaired section match my old concrete?",
                "Not exactly, and we say so before starting rather than after. New concrete starts out a different shade than weathered concrete and ages at its own rate, so a visible line between old and new sections is normal and cosmetic, not a sign of a flawed repair. A full resurfacing overlay gives a more uniform look across the whole surface than a cut-out section replacement does.")]
    return page("/concrete-repair/", "service", "Concrete Repair & Resurfacing | Orlando & Sarasota, FL",
                "Crack repair, resurfacing overlays, mudjacking and foam leveling, and cut-out-and-replace for driveways, patios and slabs. Florida range as of October 2026.",
                "Concrete Repair Matched to What's Actually Wrong",
                capsule("Concrete repair covers four different problems with four different fixes: crack filling for a stable crack, mudjacking or "
                        "polyurethane foam for a sunken panel, a bonded overlay for cosmetic wear, and cut-out-and-replace for a panel too damaged "
                        "to save. As of October 2026, repair and resurfacing work runs $3–$10 per sq ft in Florida market data. We diagnose before "
                        "quoting a method, across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["angi-driveway-repair-orlando", "homeguide-mudjacking", "homeguide-polyjacking", "angi-mudjacking-orlando",
                         "homeguide-concrete-resurfacing", "nrcs-myakka-osd", "fs-627-706", "fl-senate-2011-104", "manatee-no-permit-list",
                         "orange-do-i-need-permit", "fs713-13", "dbpr-search"],
                related=[("/concrete-repair-cost/", "concrete repair cost guide"), ("/compare/resurface-vs-replace-concrete/", "resurface or replace concrete"),
                         ("/blog/concrete-driveway-cracks-florida/", "why concrete cracks in Florida"),
                         ("/blog/tree-roots-under-driveway-florida/", "tree roots under a driveway"),
                         ("/blog/sinkholes-and-settlement-central-florida/", "sinkholes vs. normal settlement"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=CRUMBS, crumb="Concrete repair", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("concrete-repair"), eyebrow="Concrete · Greater Orlando & Sarasota",
                howto=("How a concrete repair job is done", [("Diagnose before quoting a method", "Check for a void underneath, whether a crack is still moving, and whether nearby panels are sound."),
                                                              ("Fill or seal a stable crack", "A flexible sealant is worked into a crack that isn't tied to settlement."),
                                                              ("Lift a settled panel by injection", "Mudjacking grout or polyurethane foam is pumped through small holes until the panel reaches grade."),
                                                              ("Prep and apply a resurfacing overlay", "The slab is washed, patched and recoated with a bonded overlay, then sealed."),
                                                              ("Cut out and replace a failed panel", "The damaged section is removed, the base rebuilt, dowels set, and a new panel poured to match."),
                                                              ("Cure before returning the area to use", "At least three days of curing before regular traffic.")]))


def get_pages():
    return [slabs(), repair()]
