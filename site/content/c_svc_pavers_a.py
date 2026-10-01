# -*- coding: utf-8 -*-
"""Service pages: paver driveways and paver patios/walkways."""
from _helpers import (page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext,
                       price, per, price_note, tel, contact, photo, offer)
from _photos import for_service

CRUMBS = [("Pavers", "/pavers/")]


def driveways():
    K = "paver-driveways"
    pids = for_service(K, 3)
    body = "".join([
        sec("What a paver driveway is, and when it beats concrete",
            "<p>A paver driveway is built from individual concrete, brick, permeable or natural-stone units set in sand over a compacted "
            "aggregate base, rather than poured as one continuous slab. The interlock between units, not glue or mortar, is what carries "
            "the load, which is why a sunken corner or a stained section can be lifted, fixed and reset without leaving a patch. Homeowners "
            "choose pavers over concrete for three reasons more than any other: a repair blends in instead of standing out, an HOA's "
            "architectural guidelines specify a paved look rather than plain gray, or the driveway needs a pattern and border that stamped "
            f"concrete can't match as cleanly. The full trade-off, including lifespan and resale, is in our {compare('pavers-vs-concrete-driveway', 'pavers vs. concrete driveway comparison')}; "
            f"this page covers how we build a paver driveway and what Florida ground does to one.</p>"
            + (photo(pids[0], "A row of paver driveways along a palm-lined Florida street.") if pids else "")),
        sec("The base spec: what's under the pavers matters more than what's on top",
            "<p>ICPI's Tech Spec 2, the industry construction standard for interlocking concrete pavements, sets a residential driveway base "
            "at a minimum of 6 inches of compacted aggregate over well-drained soil, 2 to 4 inches deeper where the soil is wet or drains "
            "poorly. That's a full 2 inches more than the roughly 4-inch minimum the same spec allows under a patio or walkway, because a "
            "car puts far more point load on the ground than foot traffic ever does. The base is compacted in lifts of about 4 to 6 inches, "
            f"not dumped and rolled once, and checked against 98 percent of standard Proctor density before bedding sand ever goes down ({src('icpi-ts2', 'ICPI Tech Spec 2')}).</p>"
            + table("Paver driveway build spec", ["Layer", "Standard", "Note"],
                    [["Compacted aggregate base", "6 in minimum, well-drained soil", "2–4 in more on wet or poorly drained ground"],
                     ["Subgrade compaction", "98% standard Proctor (ASTM D698)", "Modified Proctor for heavier vehicle loads"],
                     ["Paver thickness", "60 mm (2⅜ in)", "80 mm (3⅛ in) for trucks, RVs and boat trailers"],
                     ["Bedding sand", "1 in, screeded, not compacted first", "Pavers set and compacted after laying"],
                     ["Joint width", "⅛ in or less", "Filled with dry or polymeric joint sand"],
                     ["Edge restraint", "Full perimeter, spiked into the base", "Plastic, aluminum or steel; never landscape edging"]],
                    f"ICPI Tech Spec 2 and Tech Spec 3, construction standards for interlocking concrete pavements and edge restraints ({src('icpi-ts2')}, {src('icpi-ts3', 'ICPI Tech Spec 3')})."),
            ),
        sec("Material options and what they cost installed",
            "<p>The unit itself moves the price more than the base work does. Concrete pavers sit at the lower end of the Florida range; "
            "brick, permeable systems, porcelain and natural stone climb from there on material cost rather than labor.</p>"
            + table("Paver driveway materials, installed cost per sq ft", ["Material", "Range", "Notes"],
                    [["Concrete pavers", "$10–$18", "Widest color and pattern selection; easiest to spot-repair"],
                     ["Brick", "$12–$22", "Fixed color; clay brick does not fade the way pigmented concrete can"],
                     ["Permeable pavers", "$15–$25", "Open-graded base lets water pass through instead of running off"],
                     ["Porcelain", "$15–$30", "Dense, low-absorption surface; needs a flat, well-compacted base"],
                     ["Natural stone", "$20–$35", "Highest material cost; each unit is a different thickness to set"]],
                    f"Angi national material breakdown for paver driveways ({src('angi-paver-driveway', 'Angi')}); labor runs $5–$15 per sq ft on top of material.")
            + f"<p>Across all materials, installed paver driveways run {price('paver-driveway')} per {per('paver-driveway')} in current Florida market data, "
              f"typically {price('paver-driveway', True)}. A one-car driveway (about 200 sq ft) lands near $2,900 to $8,600 before demolition; a two-car "
              f"24 × 24 ft driveway (576 sq ft) runs roughly $5,700 to $17,200 ({src('homeguide-driveway-pavers', 'HomeGuide')}). "
              f"{price_note()} The {a('/paver-driveway-cost/', 'paver driveway cost guide')} works through more sizes and the line items that move a bid.</p>"),
        sec("How a paver driveway goes in, step by step",
            "<p>The order rarely changes from one driveway to the next, though the time each step takes depends on size and how much cutting "
            "the layout needs.</p>"
            + steps([("Excavate and check the subgrade.", "Dig to the depth the base, bedding sand and pavers need together, and compact or stabilize the exposed soil."),
                     ("Place and compact the base in lifts.", "Aggregate goes down 4 to 6 inches at a time, each lift run over with a plate compactor before the next one is added."),
                     ("Screed the bedding sand.", "A 1-inch layer, leveled with pipe rails, goes down uncompacted so pavers can settle into it evenly."),
                     ("Lay the pavers.", "Full units are set course by course from a fixed edge; border and apron pieces are measured and cut last."),
                     ("Install edge restraint.", "Restraint goes in along the entire perimeter, anchored into the compacted base rather than the surrounding soil."),
                     ("Sweep and compact the joint sand.", "Dry sand is worked into the joints, then the whole surface gets a final compactor pass to lock the field together.")])
            + (photo(pids[1], "A herringbone-pattern paver driveway and walkway leading to a garage.") if len(pids) > 1 else "")
            + f"<p>A standard driveway is usually a 2 to 4 day job once the site is ready. Pavers are load-ready as soon as the joint sand is compacted, "
              f"unlike concrete, which needs days to gain enough strength to carry a car; see {post('concrete-driveway-installation-process', 'how a concrete driveway compares step by step')}. "
              f"The full base-building detail is in {post('paver-installation-process-florida', 'how pavers are installed in Florida')}.</p>"),
        sec("What Florida ground does to a driveway base, and how we build around it",
            "<p>Central Florida and the Suncoast sit on two very different subgrades. Ridge sands such as Candler and Astatula drain almost "
            f"immediately, with a water table that can sit 80 inches or deeper ({src('nrcs-candler-osd', 'NRCS, Candler series')}). Flatwoods soils such "
            f"as Myakka, Florida's official state soil, hold a seasonal water table within about 18 inches of the surface for part of most years "
            f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). The same 6-inch base number performs very differently on those two lots, which is why we "
            "check the soil before quoting a depth rather than using one number everywhere.</p>"
            f"<p>Timing is the other variable. Orlando averages 51.45 inches of rain a year and Sarasota–Bradenton about 49.05, most of it in a rainy "
            f"season that runs roughly late May into mid-October ({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}). Compacting an aggregate base on "
            "soil that's already saturated doesn't reach 98 percent of Proctor density no matter how many passes the compactor makes; it just looks "
            "finished on top. Scheduling the base and bedding-sand stages for a dry window, and covering exposed sand if a storm is close, keeps that "
            "step from having to be redone.</p>"
            f"<p>A mature live oak's roots can run well past the canopy and lift a section of base years after installation; {city('orlando')}, "
            f"{city('winter-park')} and {city('sarasota')} all protect larger oaks by ordinance, which can limit root cutting near a driveway even where "
            f"a root is the problem ({src('orlando-tree-ord', 'Orlando tree ordinance')}, {src('sarasota-tree', 'City of Sarasota tree protection')}). "
            "Routing the base around a known root zone is usually more realistic than fighting the tree for the space.</p>"),
        sec("Permits for a paver driveway in Orlando, Orange County and Manatee County",
            "<p>Florida law exempts driveway installation from needing a state or local contractor license, but it never exempts the permit "
            f"itself ({src('fs489-117', 'F.S. 489.117')}). What's required, and from whom, changes block by block.</p>"
            + table("Paver driveway permits, selected jurisdictions (checked October 2026)", ["Jurisdiction", "What's required", "Notes"],
                    [["Orange County (unincorporated)", "Zoning permit only for pavers", "$38 permit fee plus $38 engineering review; about 4 business days"],
                     ["City of Orlando", "Engineering permit", "Apron: 6 in, 3,000 psi minimum; pavers in the right-of-way need a Paver's MOU"],
                     ["Manatee County (unincorporated)", "Access and Drainage (driveway/culvert) permit", "12–24 ft wide (up to 30 ft for a street-facing 3-car garage); 6 in grade cut"],
                     ["Sarasota County (unincorporated)", "Right-of-Way Use Permit; culvert permit for driveway culverts", "Culvert pipe 20–24 ft; no paving allowed inside a drainage easement"]],
                    f"{src('orange-residential-pavers', 'Orange County')}; {src('orlando-esm', 'City of Orlando Engineering Standards Manual')}; "
                    f"{src('manatee-paver-driveway-inspections', 'Manatee County')}; {src('sarasota-county-row-permit', 'Sarasota County')}.")
            + f"<p>The strip between the sidewalk and the street, the apron, almost always sits in a right-of-way the city or county controls, so it can "
              f"carry a different spec than the rest of the driveway even on the same permit. Manatee's paver driveway inspection sheet, for example, "
              f"calls for a concrete sidewalk crossing the drive to run 4 inches thick and 5 feet wide, broom-finished, with saw cuts every 10 feet, even "
              f"though the driveway on either side is pavers ({src('manatee-paver-driveway-inspections', 'Manatee County, paver driveway inspections')}). "
              f"On a contract over $2,500, Florida's lien law also requires a recorded Notice of Commencement before work starts ({src('fs713-13', 'F.S. 713.13')}), "
              f"and since 2026 an HOA can no longer require a government permit as a condition of reviewing your application ({src('fs720-3035', 'F.S. 720.3035')}). "
              f"County-by-county detail: {post('orange-county-orlando-driveway-patio-permits', 'Orange County and Orlando')}, {post('manatee-county-driveway-permits', 'Manatee County')} "
              f"and {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for a new driveway')}.</p>"),
        sec("Caring for a paver driveway",
            "<p>A new concrete paver can show a whitish, powdery bloom called efflorescence within about 60 days; ICPI's own spec is clear that it's a "
            f"calcium-carbonate deposit that doesn't affect the paver's strength, and it fades with normal weather and traffic ({src('icpi-ts2', 'ICPI Tech Spec 2')}). "
            f"Sealing is optional, not required by the spec, and there's no fixed resealing interval, only a note that an acrylic sealer typically holds "
            f"up a few years before it's worth recoating ({src('icpi-ts5', 'ICPI Tech Spec 5')}). Joint sand works loose over time from rain, traffic and "
            "the odd ant colony; topping it off and compacting it back in before the joints visibly open keeps the field interlocked. "
            f"{svc('paver-sealing', 'Our paver sealing service')} covers cleaning, re-sanding, sealing and releveling a driveway that's drifted off this schedule.</p>"
            + (photo(pids[2], "Close-up of interlocking concrete pavers set tight against each other.") if len(pids) > 2 else "")),
        sec("How do you choose the best paver driveway contractor near you?",
            "<p>Searching for paver driveway contractors near me turns up a long list; narrowing it comes down to paperwork and method, not photos.</p>"
            + ul([f"Ask who applies for the permit and confirm it covers both the driveway and any work in the right-of-way apron.",
                  "Get the base depth and compaction standard in writing, not just a square-footage price; a bid that skips this skipped the step that fails first.",
                  "Confirm paver thickness for the load: 60 mm for a standard car driveway, 80 mm if an RV, boat trailer or work truck will use it regularly.",
                  f"Check the business on the {src('dbpr-search', 'DBPR license search')} if the scope includes anything beyond flatwork, since structural concrete work falls under a different category than driveway installation.",
                  "Ask whether the estimate includes edge restraint as a line item; it's invisible once the job is done and easy to leave off a cheap bid."])
            + f"<p>{post('how-to-choose-a-paver-contractor-orlando', 'Our Orlando paver contractor checklist')} and {post('how-to-compare-concrete-and-paver-quotes', 'how to compare quotes line by line')} go further.</p>"),
        sec("Where we build paver driveways",
            f"<p>We lay paver driveways across Greater Orlando and Sarasota–Manatee, each quoted by the crew that knows that county's permit desk. "
            f"Related towns: {cs('orlando', K)}, {cs('kissimmee', K)}, {cs('sarasota', K)} and {cs('lakewood-ranch', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("Are pavers strong enough for a driveway, or will they crack under a truck?",
                "Pavers don't crack under normal vehicle weight the way a thin or under-based concrete slab can; the load spreads through the interlocking field instead of one point. For an RV, boat trailer or work truck, we specify 80 mm pavers and compact the base to the stricter vehicular standard instead of the usual 60 mm driveway spec."),
            faq("How thick are driveway pavers compared with patio pavers?",
                "Driveway pavers are typically 60 mm (2⅜ in), the standard thickness for both residential driveways and pedestrian areas under ICPI's spec. Heavier loads, like RVs or boat trailers, call for 80 mm (3⅛ in) units instead. Patio pavers are usually the same 60 mm unit; the difference between a patio and a driveway is mostly the base depth underneath, not the paver itself."),
            faq("Do paver driveways need edge restraints?",
                "Yes, along the entire perimeter and anywhere the material changes. Without it, the field has nothing stopping it from spreading sideways under tire loads, and the joints near the edge open up within a season or two. Plastic landscape edging sold for flower beds isn't a substitute; the spikes have to anchor into the compacted base."),
            faq("Can you add pavers just to the apron or as a border on my concrete driveway?",
                "Yes. A paver apron or a paver border framing a concrete field is a common hybrid in both service areas, and it still needs its own compacted base and edge restraint where it meets the concrete. The two materials settle differently, so we set a rigid restraint at the seam rather than letting pavers butt straight against the slab."),
            faq("How long does a paver driveway installation take?",
                "A typical one- or two-car driveway runs 2 to 4 days from excavation to swept joints, depending on how much border cutting the layout needs. Unlike concrete, pavers are ready for vehicle traffic as soon as the base is compacted and the joint sand is swept and compacted, with no cure time to wait out."),
            faq("Will new pavers change the height at my garage door?",
                "It can. A paver driveway adds the thickness of the base, bedding sand and paver on top of whatever grade is there now, which sometimes raises the surface an inch or more at the garage threshold. We check that transition during the site visit and adjust the base depth or add a taper so water still runs away from the garage rather than into it.")]
    return page("/paver-driveways/", "service", "Paver Driveway Installation | Orlando & Sarasota, FL",
                "Paver driveways in 60 mm or 80 mm pavers over a compacted aggregate base with edge restraint. Florida market range as of October 2026, Orlando and Sarasota.",
                "Paver Driveways Built on a Base That Won't Settle",
                capsule("A paver driveway sets 60 mm or 80 mm units on a compacted aggregate base at least 6 inches deep, with edge restraint along every "
                        "border so the field can't spread. As of October 2026, installed paver driveways run $10–$30 per sq ft in Florida market data, "
                        "more than concrete but repairable one unit at a time. We build to that spec across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts3", "icpi-ts5", "homeguide-driveway-pavers", "angi-paver-driveway", "nrcs-candler-osd", "nrcs-myakka-osd",
                         "ncei-annual-prcp", "orlando-tree-ord", "sarasota-tree", "fs489-117", "fs713-13", "fs720-3035", "orange-residential-pavers",
                         "orlando-esm", "manatee-paver-driveway-inspections", "sarasota-county-row-permit", "dbpr-search"],
                related=[("/paver-driveway-cost/", "paver driveway cost guide"), ("/compare/pavers-vs-concrete-driveway/", "pavers vs. concrete driveway"),
                         ("/compare/clay-brick-vs-concrete-pavers/", "clay brick vs. concrete pavers"),
                         ("/blog/paver-driveway-ideas-florida/", "paver driveway ideas"), ("/blog/why-pavers-sink-in-florida/", "why pavers sink, and the fix"),
                         ("/blog/driveway-widening-and-extensions-florida/", "widening or extending a driveway"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=CRUMBS, crumb="Paver driveways", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("paver-driveway"), eyebrow="Pavers · Greater Orlando & Sarasota",
                howto=("How a paver driveway is built", [("Excavate and check the subgrade", "Dig to the combined depth of base, bedding sand and pavers, and stabilize the exposed soil."),
                                                          ("Place and compact the base in lifts", "Compacted aggregate goes down 4 to 6 inches at a time, checked against 98% Proctor density."),
                                                          ("Screed the bedding sand", "A 1-inch layer, leveled with pipe rails, left uncompacted before the pavers go down."),
                                                          ("Lay the pavers", "Full units set course by course; border and apron pieces cut to fit last."),
                                                          ("Install edge restraint", "Anchored into the compacted base along the full perimeter."),
                                                          ("Sweep and compact the joint sand", "Dry sand worked into the joints, then a final compactor pass locks the field together.")]))


def patios():
    K = "paver-patios"
    pids = for_service(K, 4)
    body = "".join([
        sec("Patios, walkways, fire-pit areas and lanai extensions, one base system",
            "<p>This page covers every paver surface that isn't a driveway or a pool deck: back patios, front and side walkways, fire-pit areas, and "
            "extensions that tie a new paver field into an existing lanai or screen enclosure. Travertine is a material option here too, not a separate "
            "service, chosen most often for the way it stays cooler underfoot in direct sun than a dark concrete paver, though we won't put an unverified "
            "number on how much cooler. All of it shares the same base principles as a driveway, built lighter because furniture and foot traffic load "
            f"the ground far less than a parked car. For the stamped-concrete alternative, see {compare('stamped-concrete-vs-pavers', 'stamped concrete vs. pavers for patios')}.</p>"
            + (photo(pids[0], "A circular paver patio with a granite edge restraint in a landscaped yard.") if pids else "")),
        sec("The base spec for a patio or walkway",
            "<p>ICPI Tech Spec 2 sets a minimum of about 4 inches of compacted aggregate base under a patio or walkway on well-drained soil, 2 to 4 "
            f"inches more where the ground is wet or drains poorly, the same wet-soil allowance the spec gives a driveway ({src('icpi-ts2', 'ICPI Tech Spec 2')}). "
            "That's roughly two-thirds the depth a driveway needs, not because the work is less careful but because the load is lighter. The base is "
            "still compacted in lifts and checked against 98 percent of standard Proctor density before bedding sand goes down, and a narrow 3- or "
            "4-foot walkway gets the same base program as an open patio, since a path with no base shifts and dishes faster than a wide one.</p>"
            + table("Paver patio and walkway build spec", ["Layer", "Standard", "Note"],
                    [["Compacted aggregate base", "4 in minimum, well-drained soil", "2–4 in more on wet or poorly drained ground"],
                     ["Paver thickness", "60 mm (2⅜ in)", "Standard for all pedestrian surfaces; no need to upsize for a patio"],
                     ["Bedding sand", "1 in, screeded, uncompacted before laying", "Compacted only after the pavers and joint sand are in"],
                     ["Joint width", "⅛ in or less", "Dry or polymeric joint sand"],
                     ["Edge restraint", "Full perimeter, spiked into the base", "Required anywhere the paving material changes, including at a fire pit"],
                     ["Finished slope", "About 1 in per 8–10 ft, away from the house", "Keeps water off the foundation and the lanai threshold"]],
                    f"ICPI Tech Spec 2 and Tech Spec 3 ({src('icpi-ts2')}, {src('icpi-ts3', 'ICPI Tech Spec 3')}).")),
        sec("Material options: concrete pavers or travertine",
            "<p>Concrete pavers and travertine solve the same problem with very different materials and very different prices.</p>"
            + table("Paver patio materials, installed cost per sq ft", ["Material", "Range", "A 300 sq ft patio"],
                    [["Concrete pavers", f"{price('paver-patio')}", "About $3,000–$5,100"],
                     ["Travertine", "$13–$45", "About $3,900–$13,500"]],
                    f"HomeGuide, paver patio and travertine cost guides ({src('homeguide-paver-patio', 'HomeGuide, paver patios')}, {src('homeguide-travertine', 'HomeGuide, travertine')}).")
            + f"<p>Concrete pavers run more pattern and color options and cost less to replace if a unit cracks. Travertine is a porous natural stone that "
              f"needs sealing to resist stains, and it's the material most homeowners choose around a pool for exactly the reason it suits a patio: it "
              f"doesn't hold heat underfoot the way a dark surface does. These are market ranges, not a quote for your yard; we price a patio after seeing the site. "
              f"The {a('/paver-patio-cost/', 'paver patio cost guide')} breaks "
              f"down sizes from a small seating area to a full backyard patio.</p>"),
        sec("Walkways, fire-pit areas and lanai extensions",
            "<p>A connecting walkway from the driveway to a side gate or the backyard usually runs 3 to 4 feet wide and shares the same base and bedding "
            f"sand as the open patio it connects to; the design options are in {post('front-walkway-ideas-curb-appeal', 'front walkway ideas')}. A paver-set "
            "fire pit needs a separate, denser base detail under the fire pit ring itself, plus clearance from the house, any screen enclosure and "
            f"overhanging branches, covered in {post('fire-pit-on-pavers-florida', 'safe fire pit setups on pavers')}. Extending a patio under or beyond "
            "an existing pool cage means matching the paver field's elevation to the enclosure's track and setting a flexible joint where the two meet "
            "so they can move independently without cracking the enclosure's footer; the full walkthrough is in "
            f"{post('extend-patio-under-screen-enclosure', 'extending a patio under a screen enclosure')}.</p>"
            + (photo(pids[1], "A paver patio with a stone fire pit and outdoor seating.") if len(pids) > 1 else "")),
        sec("Installation, step by step",
            "<p>A straightforward patio or walkway follows the same order as a driveway, scaled to a lighter base.</p>"
            + steps([("Layout and excavation.", "Stake the footprint against the house and excavate past the planned grade to leave room for base, sand and pavers together."),
                     ("Compact the base in lifts.", "Aggregate goes down 4 to 6 inches at a time, each lift compacted before the next, graded to slope water away from the house."),
                     ("Screed the bedding sand.", "A uniform 1-inch layer goes down last, guided by pipe rails, and stays uncompacted until the pavers are set."),
                     ("Lay the field and cut the borders.", "Full pavers are set course by course from a fixed edge; pieces at a curve, a fire pit or an enclosure track are cut to fit."),
                     ("Set edge restraint.", "Installed along the full perimeter and anywhere the material changes, including around a fire pit."),
                     ("Sweep and compact the joints.", "Dry joint sand is worked in and the whole surface gets a final compactor pass to lock the field together.")])
            + f"<p>An average patio runs 1 to 2 days once the site is prepared; a straightforward walkway can finish in a single day. "
              f"{post('paver-installation-process-florida', 'How pavers are installed in Florida')} goes deeper on the base and compaction steps.</p>"),
        sec("What rain, sun and shade do to a paver patio",
            "<p>A patio graded flat, or tipped back toward the house, holds water against the slider or the lanai door instead of carrying it into the "
            f"yard, which is exactly what the roughly 1-in-10-ft slope in the spec table above is built to prevent. Orlando and Sarasota–Bradenton both see "
            f"around 50 inches of rain a year, most of it in a rainy season running late May into mid-October, often as a sharp afternoon storm "
            f"({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}). Where standing water in the yard is a bigger issue than drainage off the patio, a "
            f"permeable paver system can help; {post('permeable-pavers-and-drainage-florida', 'permeable pavers and yard drainage')} covers when that "
            "trade-off is worth it.</p>"
            "<p>Pigments in concrete pavers fade gradually under UV exposure, lighter colors less noticeably than dark ones; a sealer slows the fade but "
            "doesn't stop it. A patio tucked under tree canopy or on the north side of the house stays damp longer after each rain, which is the "
            "condition that lets mold and algae take hold in the joints; good drainage through the base helps it dry faster, but a shaded patio still "
            "needs more frequent cleaning than one in full sun.</p>"),
        sec("Permits for a patio or paver walkway",
            "<p>Whether a patio needs a permit varies more than driveway rules do, since a patio rarely touches the public right-of-way.</p>"
            + table("Patio and walkway permits, selected jurisdictions (checked October 2026)", ["Jurisdiction", "What's required", "Notes"],
                    [["Orange County (unincorporated)", "Zoning permit for pavers", "Same $38 + $38 fee structure as a paver driveway"],
                     ["City of Orlando", "Engineering permit", "Covers pavers, asphalt or concrete patios and pool-deck slabs alike"],
                     ["Manatee County (unincorporated)", "No permit for a non-structural concrete or paver patio", "A concrete slab with footers, or a pool, still needs one"],
                     ["City of Sarasota", "No flatwork-specific rule published", "Call the Building Division to confirm before a larger patio"]],
                    f"{src('orange-residential-pavers', 'Orange County')}; {src('orlando-res-requirements', 'City of Orlando')}; "
                    f"{src('manatee-no-permit-list', 'Manatee County')}; {src('city-sarasota-bp-guidelines', 'City of Sarasota')}.")
            + f"<p>Several cities also cap how much of a lot can be covered by driveways, patios and roofs combined; the City of Sarasota's zoning table "
              f"runs 60 to 75 percent of the lot depending on the zone, with coastal-island parcels capped at 70 percent "
              f"({src('city-sarasota-zoning-vi-203-impervious', 'City of Sarasota zoning code')}). A screen enclosure built over the new patio has its own "
              "separate permit, tied to its footers rather than the paver field. On a contract over $2,500, Florida's lien law still requires a recorded "
              f"Notice of Commencement ({src('fs713-13', 'F.S. 713.13')}). More in {post('orange-county-orlando-driveway-patio-permits', 'Orange County and Orlando permits')} "
              f"and {post('hoa-approval-for-pavers-and-concrete', 'HOA approval for pavers and a pool deck')}.</p>"),
        sec("Caring for a paver patio",
            "<p>New concrete pavers can show a whitish efflorescence bloom within about 60 days; it's cosmetic and fades with normal weather, not "
            f"something a sealer is required to fix ({src('icpi-ts2', 'ICPI Tech Spec 2')}). Joint sand that's thinned from rain and foot traffic gives "
            "ants and weed seed an opening, so topping it off and compacting it back in is routine upkeep rather than a repair. Sealing has no fixed "
            f"interval in the industry's own guidance, only a rough few years for an acrylic coat before it's worth recoating ({src('icpi-ts5', 'ICPI Tech Spec 5')}); "
            f"travertine, being more porous, benefits from staying on that schedule more than concrete pavers do. {svc('paver-sealing', 'Our paver sealing service')} "
            "handles cleaning, re-sanding, sealing and resetting pavers that have sunk or shifted.</p>"
            + (photo(pids[2], "A covered paver patio furnished with a dining table and a sectional sofa.") if len(pids) > 2 else "")),
        sec("How do you choose the best paver patio contractor near you?",
            "<p>Paver patio contractors near me is a long list in both service areas; a few questions narrow it to the ones worth a quote.</p>"
            + ul(["Ask for the base depth in writing, not just a square-footage price. A patio quoted with no stated base depth is a patio quoted on hope.",
                  "If a fire pit or a screen-enclosure tie-in is part of the scope, ask specifically how that section's base and edge restraint differ from the open field.",
                  f"Confirm who pulls any required permit, and ask directly whether your jurisdiction needs one; Manatee County's non-structural exemption doesn't apply everywhere.",
                  "Get the paver brand, color and thickness specified, not just 'pavers,' so a second bid can be compared on the same material.",
                  "Ask how the crew handles a downpour mid-install, since an open base or screeded sand left exposed to a storm often has to be redone."])
            + f"<p>{post('how-to-choose-a-paver-contractor-orlando', 'Our paver contractor checklist')} and {post('concrete-and-paver-warranty-what-it-should-cover', 'what a paver warranty should cover')} go further.</p>"),
        sec("Where we build paver patios and walkways",
            f"<p>We lay paver patios, walkways and fire-pit areas across Greater Orlando and Sarasota–Manatee. Related towns: {cs('orlando', K)}, "
            f"{cs('winter-garden', K)}, {cs('sarasota', K)} and {cs('bradenton', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("How long does it take to install a paver patio?",
                "Most patios take 1 to 2 days once the site is prepared, and a straightforward connecting walkway can finish in a single day. Size, how much border cutting the layout needs, and whether the job ties into an existing slab or screen enclosure all change that range; a 400 sq ft patio with a curved edge runs longer than a square one the same size."),
            faq("Can you match new pavers to my existing driveway or pool deck pavers?",
                "Sometimes. If the original paver line is still in production, a close match is usually possible; many lines are discontinued or re-blended over a few years, which is the more common outcome. We bring a sample to the site visit so you can see the match before committing, and blending a slightly different shade into a new section, rather than hiding it, is often the better-looking result."),
            faq("How deep is the base under a paver patio in Florida?",
                "About 4 inches of compacted aggregate on well-drained soil, 2 to 4 inches more where the ground is wet or drains poorly, per the industry construction standard. That's thinner than the 6-inch minimum under a driveway because foot traffic and furniture load the ground far less than a car. The full build-up, lift by lift, is in our paver installation process guide."),
            faq("Will a paver patio drain during heavy rain?",
                "Yes, if it's graded to shed water away from the house and the joints stay filled; we slope the finished surface roughly 1 inch per 8 to 10 feet toward the yard rather than toward the foundation. Standing water in the surrounding lawn, not the patio itself, is usually a base-and-grading issue; a permeable paver system is worth considering where yard drainage, not the patio surface, is the real problem."),
            faq("Do pavers fade in the Florida sun?",
                "Pigmented concrete pavers fade gradually under UV exposure, lighter colors less than dark ones, which is a cosmetic change rather than a structural one. A sealer slows the fade and deepens the color for a while after it's applied, but no sealer stops UV fading permanently. Travertine and other natural stone don't carry a pigment to fade the same way."),
            faq("Can you install a paver walkway around the side of the house?",
                "Yes, side-yard walkways connecting a driveway, gate or trash-can area to the backyard are common work in both service areas and fall under this service. They run the same base and bedding-sand program as a patio, scaled to a narrower 3- to 4-foot width, and can tie into an existing patio or stand on their own.")]
    return page("/paver-patios/", "service", "Paver Patio Installation | Orlando & Sarasota, FL",
                "Paver patios, walkways, fire-pit areas and lanai extensions in concrete pavers or travertine, on a compacted base. Florida price range as of October 2026.",
                "Paver Patios, Walkways and Fire-Pit Areas for Florida Backyards",
                capsule("A paver patio, walkway or fire-pit area sets concrete pavers or travertine on a compacted aggregate base at least 4 inches deep, "
                        "thinner than a driveway because furniture and foot traffic load the ground far less than a car. As of October 2026, installed "
                        "paver patios run $10–$17 per sq ft in Florida market data, and travertine runs higher. We build patios, walkways, lanai "
                        "extensions and fire-pit pads to that spec across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts3", "icpi-ts5", "homeguide-paver-patio", "homeguide-travertine", "ncei-annual-prcp",
                         "orange-residential-pavers", "orlando-res-requirements", "manatee-no-permit-list", "city-sarasota-bp-guidelines",
                         "city-sarasota-zoning-vi-203-impervious", "fs713-13"],
                related=[("/paver-patio-cost/", "paver patio cost guide"), ("/compare/stamped-concrete-vs-pavers/", "stamped concrete vs. pavers"),
                         ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers"),
                         ("/blog/paver-patio-ideas-florida/", "paver patio ideas"), ("/blog/fire-pit-on-pavers-florida/", "fire pits on pavers"),
                         ("/blog/extend-patio-under-screen-enclosure/", "extending a patio under a screen enclosure"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=CRUMBS, crumb="Paver patios", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("paver-patio"), eyebrow="Pavers · Greater Orlando & Sarasota",
                howto=("How a paver patio or walkway is built", [("Layout and excavation", "Stake the footprint and excavate past the planned grade for base, sand and pavers together."),
                                                                  ("Compact the base in lifts", "Aggregate goes down 4 to 6 inches at a time, graded to slope water away from the house."),
                                                                  ("Screed the bedding sand", "A uniform 1-inch layer, guided by pipe rails, left uncompacted until the pavers are set."),
                                                                  ("Lay the field and cut the borders", "Full pavers set course by course; curved or fitted pieces cut last."),
                                                                  ("Set edge restraint", "Installed along the full perimeter and anywhere the material changes."),
                                                                  ("Sweep and compact the joints", "Dry joint sand worked in, then a final compactor pass locks the field together.")]))


def get_pages():
    return [driveways(), patios()]
