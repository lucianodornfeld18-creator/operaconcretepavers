# -*- coding: utf-8 -*-
"""Blog posts, group h: backyard feature and planning posts (screen-enclosure patio extensions, fire pits,
backyard putting greens, side yards, whole-yard low-maintenance plans, retaining wall and seat wall ideas).
These are design and planning posts; they link out to the service pages for base specs, to the permit and
HOA posts for jurisdiction detail, and to the cost guides for pricing, rather than repeating any of that."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext, price, per, contact, photo
from _photos import for_service


def p_extend_patio_under_screen_enclosure():
    pids = for_service("paver-patios", 1)
    pid = pids[0] if pids else None
    body = "".join([
        sec("What Does It Mean to Extend a Patio Under a Screen Enclosure?",
            f"<p>Extending a patio under a screen enclosure means pouring or laying new {svc('concrete-patios', 'concrete')} or "
            f"{svc('paver-patios', 'paver')} flooring inside an existing pool cage, or pushing a {svc('pool-deck-pavers', 'pool deck')} field "
            "out past the cage's current footprint so a new section of screen can be added over it. The two parts of the job, the flooring and "
            "the aluminum structure overhead, are built by different trades on different schedules, and most of what goes wrong on this kind of "
            "project traces back to one side moving ahead of the other rather than to the paving itself.</p>"
            + (photo(pid, "A circular paver patio bordered by granite edging stones among garden shrubs and tall grass.") if pid else "")),
        sec("Who Pours the Footers: the Paving Crew or the Aluminum Contractor?",
            "<p>Florida treats aluminum screen and patio enclosures as their own specialty trade, and that trade's own rule draws the line: an "
            "aluminum specialty contractor may build \"foundations, slabs and block kneewalls incidental to\" its enclosure work, but it may not "
            "perform any work that alters a structure's load-bearing elements or foundations "
            f"({src('fac61g4-15-015', 'Fla. Admin. Code R. 61G4-15.015')}). In practice that means the enclosure's own post footers are usually "
            "set by the aluminum crew as part of its own scope, sized for wind uplift on the aluminum frame rather than for foot traffic, while "
            "the surrounding patio slab or paver field is a separate pour built to the flatwork spec on the paver patio or concrete patio page. "
            "A new footer poured after the flooring is already down means cutting into finished concrete or pulling pavers back up, so the two "
            "trades plan the layout together before either one starts.</p>"),
        sec("Can Pavers or Concrete Go Over an Existing Lanai Slab Inside the Cage?",
            "<p>Often, yes, if the old slab is sound and roughly level, which saves the cost and mess of a full tear-out. A paver overlay goes "
            "down on a thin leveling bed over the existing concrete rather than on an excavated aggregate base, so it changes finished height by "
            "only an inch or two; concrete poured over an old slab needs a bonding agent or an isolation layer and still has to clear the screen "
            "track and any door threshold by the same margin pavers do. A slab with active cracking, a settled corner or standing water after rain "
            f"is usually worth replacing rather than covering, since an overlay reads every flaw in what's underneath it. {svc('concrete-repair', 'Our concrete repair page')} "
            "covers how we judge that call on an existing slab.</p>"),
        sec("What Permits Does a Patio Extension Under a Screen Enclosure Need?",
            "<p>Usually two separate approvals rather than one, because the flooring and the aluminum structure are different scopes of work "
            f"in most building departments. Orlando runs pavers, asphalt and concrete flatwork through an engineering permit "
            f"({src('orlando-res-requirements', 'City of Orlando permitting requirements')}), while a new or extended screen enclosure is a "
            "structural permit for the aluminum framing itself, reviewed separately for wind load. Since July 1, 2026, Florida law exempts "
            "owners of single-family homes from a building permit for work valued under $7,500, but the exemption explicitly excludes structural "
            "work and does not reach land development, engineering or zoning permits, so a screen enclosure's framing and a right-of-way-adjacent "
            f"flatwork permit generally still apply regardless of the dollar figure ({src('orlando-hb803-guide', 'City of Orlando, HB 803 exemption guide')}). "
            f"Manatee County exempts a non-structural concrete or paver patio from a permit but still requires one once footers are involved "
            f"({src('manatee-no-permit-list', 'Manatee County')}), which is exactly the condition a screen enclosure's posts create. A project "
            f"over $2,500 also triggers Florida's Notice of Commencement requirement under the state's lien law, recorded before either trade "
            f"breaks ground ({src('fs713-13', 'F.S. 713.13')}). "
            f"{post('orange-county-orlando-driveway-patio-permits', 'Our Orange County and Orlando permit guide')} and "
            f"{post('sarasota-county-driveway-patio-permits', 'our Sarasota County permit guide')} go further on what each department asks for.</p>"),
        sec("How Does Drainage Change Once a Screen Enclosure Covers the New Patio?",
            "<p>A screened patio still gets wet in a wind-driven Florida storm, since a screen slows rain more than it stops it, so the slope "
            "that carries water away from the house matters just as much under a cage as it does on an open patio. What does change is where "
            "that water comes from: an enclosure's roof panels and gutters, where it has them, concentrate runoff at specific downspout points "
            "rather than spreading it evenly, and those points need to land on graded ground or a drain, not directly against the new paving's "
            "edge restraint. A patio extension planned without the enclosure's gutter layout in hand is the most common reason a corner of an "
            "otherwise well-built lanai floor holds water after a storm.</p>"),
        sec("What Height and Slope Does the New Flooring Need Where It Meets the Screen Track?",
            "<p>The aluminum track that holds the screen typically sits at a fixed height set when the cage itself was engineered, so the new "
            "paver or concrete surface has to be built to meet that elevation rather than the other way around. Where the paving runs slightly "
            "proud of the track or a door threshold, water backs up against the frame instead of draining past it; where it sits too low, the "
            "screen's bottom rail is left exposed to standing water and grit after every rain. We isolate the new flooring from the enclosure's "
            "footers with a flexible joint rather than pouring or setting pavers tight against them, since the two structures settle and expand "
            "at different rates and a rigid connection is what cracks first.</p>"
            + table("Who typically handles what", ["Element", "Usually handled by", "Note"],
                    [["Enclosure posts and footers", "Aluminum / screen contractor", "Sized for wind uplift on the frame, not foot traffic"],
                     ["Patio slab or paver field", "Concrete or paver crew", "Built to the flatwork spec on the paver patio or concrete patio page"],
                     ["Isolation joint at the footer", "Paving crew, coordinated with the enclosure layout", "Lets the two structures move independently"],
                     ["Grading and downspout tie-ins", "Paving crew, using the enclosure's gutter plan", "Set before the final paver course or pour"]],
                    "A project that sequences these out of order is the most common source of rework on a cage-and-patio job.")),
        sec("Where This Overlaps With HOA Review",
            f"<p>An architectural review committee generally wants to see the enclosure's height, roofline and screen color as its own line "
            f"item, separate from whatever finish the patio flooring underneath it uses, so a single submission package that treats both as "
            f"one project tends to move faster than two filed apart. {post('lakewood-ranch-arc-approval-hardscape', 'the Lakewood Ranch ARC process')} "
            f"is one example of a community that reviews enclosures on its own form, and {post('hoa-approval-for-pavers-and-concrete', 'our broader HOA approval guide')} "
            f"covers the submission basics that apply more generally. {a('/paver-patio-cost/', 'Our paver patio cost guide')} and "
            f"{a('/concrete-patio-cost/', 'our concrete patio cost guide')} break down pricing for the flooring side of a project like this once "
            f"the layout with the enclosure contractor is settled.</p>"),
    ])
    faqs = [faq("Can a patio be extended inside an existing screen enclosure without removing the cage?",
                "Usually yes, if there is room to work around the existing posts and the footers are not in the way of the new paving's layout. A full re-screen is a different job and may be worth timing together with a flooring extension so the posts are only disturbed once."),
            faq("Does the paving crew or the screen contractor pour the enclosure's footers?",
                "Florida's aluminum specialty contractor rule lets that trade build foundations and slabs incidental to its own enclosure work, so the enclosure posts and their footers are usually set by the screen contractor, sized for wind load on the frame rather than for foot traffic. The surrounding patio slab or paver field is a separate pour."),
            faq("Can pavers go directly over an old concrete lanai floor?",
                "Often, as a thin overlay on a leveling bed rather than an excavated base, which keeps the finished height within an inch or two of the original slab. A slab with active cracking or a settled corner is usually worth replacing first, since those flaws tend to show through an overlay."),
            faq("Does a screened patio still need to drain properly?",
                "Yes. Wind-driven rain gets past a screen more than most homeowners expect, and an enclosure's gutters and downspouts concentrate runoff at specific points rather than spreading it evenly, so the slope and drain layout underneath still matter."),
            faq("Do I need a separate permit for the patio and for the screen enclosure?",
                "Usually, since they are different scopes reviewed by different parts of a building department: an engineering or flatwork permit for the paving and a structural permit for the aluminum framing. Florida's 2026 exemption for work under $7,500 does not cover structural work, so the enclosure's permit still generally applies."),
            ]
    related = [("/paver-patios/", "Paver patios & walkways"), ("/paver-patio-cost/", "Paver patio cost guide"),
               ("/concrete-patios/", "Concrete patios"), ("/pool-deck-pavers/", "Pool deck pavers"),
               ("/blog/fire-pit-on-pavers-florida/", "Fire pits on pavers"),
               ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete")]
    return page("/blog/extend-patio-under-screen-enclosure/", "post",
                "How to Extend a Patio Under a Pool Screen Enclosure",
                "Extending a patio under a pool screen enclosure in Florida: who pours the footers, overlay vs. tear-out, permits and drainage, as of October 2026.",
                "Extending a Patio Under (or Beyond) a Pool Screen Enclosure",
                capsule("Extending a patio under a Florida pool screen enclosure means coordinating two separate trades: the aluminum "
                        "contractor's own footers for the cage posts, and a new concrete or paver surface built to meet the screen track's "
                        "fixed height. As of October 2026, the two are usually permitted and built separately, with an isolation joint at "
                        "each footer so the structures can move independently."),
                body, faqs=faqs,
                sources=["fac61g4-15-015", "orlando-res-requirements", "orlando-hb803-guide", "manatee-no-permit-list", "fs713-13"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-patios",
                image=pid, form=False)


def p_fire_pit_on_pavers_florida():
    pids = for_service("paver-patios", 3)
    pid = pids[2] if len(pids) > 2 else (pids[0] if pids else None)
    body = "".join([
        sec("What Does a Safe Fire Pit Setup on Pavers Look Like?",
            f"<p>A fire pit built on a {svc('paver-patios', 'paver patio')} needs a non-combustible ring or insert set on its own denser base "
            "section, kept the setback distance local rules require from the house and any overhanging branches, and a clear, furniture-free "
            "radius around it for anyone standing up or stepping back from the heat. Orange County's open-burning rule, which governs Orlando "
            "and the rest of the county, caps an open fire at 3 feet across and 2 feet tall unless it burns inside a contained outdoor fireplace, "
            "grill or barbecue pit, which almost any manufactured or built-in fire pit insert qualifies as "
            f"({ext('https://www.orangecountyfl.net/Portals/0/Library/Environment/docs/Open%20Burning%20Frequently%20Asked%20Questions-CERT.pdf', 'Orange County, Open Burning FAQ')}). "
            "Sarasota County's rule reaches the same conclusion through a different route, defining a fire bowl, chiminea or built-in outdoor "
            "fireplace as a \"warming type container\" with its own shorter setback from a structure "
            f"({ext('https://library.municode.com/fl/sarasota_county/codes/code_of_ordinances?nodeId=PTIICOOR_CH54ENNARE_ARTVAISOPO', 'Sarasota County Code §54-116, Open Burning')}).</p>"
            + (photo(pid, "A stone fire pit ringed by wicker chairs and an umbrella table on a paver patio.") if pid else "")),
        sec("How Far Does a Fire Pit Need to Sit From the House?",
            "<p>The distance depends on whether the fire counts as \"contained\" under the local rule, and the two counties in our service "
            "areas answer that question differently enough to be worth checking before a fire pit's location is final, not after the pavers "
            "are down.</p>"
            + table("Fire pit setback rules, selected counties (checked October 2026)", ["Jurisdiction", "Open or uncontained fire", "Contained fire pit, fire bowl or outdoor fireplace"],
                    [["Orange County", "25 ft from any building or combustible structure", "Same 25 ft rule, but the 3 ft × 2 ft size cap does not apply once the fire is contained in an outdoor fireplace, grill or barbecue pit"],
                     ["Sarasota County", "25 ft from any structure or combustible material", "A \"warming type container,\" chiminea, fire bowl or built-in outdoor fireplace among them, needs only about 10 ft"]],
                    f"{ext('https://www.orangecountyfl.net/Portals/0/Library/Environment/docs/Open%20Burning%20Frequently%20Asked%20Questions-CERT.pdf', 'Orange County, Open Burning FAQ')}; "
                    f"{ext('https://library.municode.com/fl/sarasota_county/codes/code_of_ordinances?nodeId=PTIICOOR_CH54ENNARE_ARTVAISOPO', 'Sarasota County Code §54-116')}. "
                    "Manatee, Osceola, Lake, Seminole and Polk counties were not confirmed to the same level of detail; call the local fire marshal's office before finalizing a location close to the house.")
            + "<p>Both counties also require the fire to be constantly attended by someone with a garden hose or another fire extinguishing "
              "tool within reach until it is fully out, and both give the local fire official authority to order any fire extinguished when "
              "drought conditions make it hazardous, which is the same trigger behind the burn bans issued most years during Florida's dry "
              "spring months.</p>"),
        sec("What Base Does a Paver-Set Fire Pit Need?",
            "<p>The ring itself sits on a denser, more compacted section of base than the open paver field around it, since a masonry or steel "
            "insert concentrates weight in a tighter footprint and a wood or gas fire cycles that section through repeated heating and cooling "
            "that an open field never experiences. The edge restraint around the fire pit's own footprint is set separately from the restraint "
            "along the patio's outer perimeter, the same principle that applies anywhere a paver field changes material or purpose "
            f"({src('icpi-ts3', 'ICPI Tech Spec 3')}). A built-in fire pit poured as a short masonry or block ring, rather than set as a "
            f"freestanding metal bowl, is close kin to a low {svc('retaining-walls', 'seat wall')} in how its base and footing are built, and "
            f"the two are often designed together; {post('retaining-wall-ideas-florida-yards', 'our retaining wall and seat wall ideas guide')} "
            "covers seat wall height and layout.</p>"),
        sec("Wood-Burning or Gas: What Changes About the Setup?",
            "<p>A wood-burning fire pit falls under the open-burning rules above regardless of what it is built from, since those rules track "
            "the fuel and the flame, not the material of the ring. A gas fire pit with a fixed line run from the house's natural gas or a buried "
            "propane tank is plumbing and gas work, not flatwork, and needs a licensed gas or plumbing contractor to make that connection and "
            "pull the gas permit, separate from whoever builds the pit's masonry or paver base. A portable propane fire table that runs off a "
            "swappable tank under the unit skips that gas-line permit step entirely, which is part of why portable units are the simpler choice "
            "on a patio where the exact final location is not locked in yet.</p>"),
        sec("Does the Fire Pit Need to Sit on Its Own Pad, or Can It Share the Main Patio Field?",
            "<p>Both approaches work, and the choice is mostly about how much the fire pit area functions as its own destination versus an "
            "extension of the main seating field. A fire pit set into the main paver or concrete field, with seating pulled up around it, reads "
            "as one continuous space and suits a smaller yard where a second, separate pad would crowd the lot. A fire pit built on its own "
            "pad, often with a different paver pattern, a gravel surround or a low seat wall ringing it, reads as a distinct zone and works "
            "better where the main patio already has a dining or lounge layout that a fire feature would otherwise compete with for space.</p>"),
        sec("What Does an HOA Typically Ask About a Fire Pit?",
            f"<p>A fixed, built-in fire feature changes the yard's landscape plan and stays visible from neighboring lots year-round, which "
            f"puts it on most architectural committees' submission list well before the first fire is lit. A portable propane fire table is "
            f"less likely to need the same paperwork in most communities, since it reads as furniture rather than a permanent structure, "
            f"though that line is set by the specific declaration, not a rule that holds everywhere. {post('hoa-approval-for-pavers-and-concrete', 'Our HOA approval guide')} "
            "walks through what a submission package for a permanent yard feature typically includes.</p>"),
    ])
    faqs = [faq("How close to the house can a fire pit be built?",
                "It depends on whether the local rule treats it as a contained fire. Orange County sets a 25-foot setback from any structure for an open fire, though the 3-by-2-foot size cap does not apply once the fire burns inside an outdoor fireplace, grill or barbecue pit. Sarasota County allows a contained fire pit, fire bowl or chiminea, termed a warming type container, to sit as close as about 10 feet. Other counties in our service areas were not confirmed to the same detail, so a call to the local fire marshal is worth it before the location is final."),
            faq("Does a fire pit need a denser base than the rest of the patio?",
                "Yes. A masonry or steel insert concentrates weight in a tighter footprint than an open paver field, and repeated heat cycling adds stress a plain seating area never sees, so that section gets its own compacted base and its own edge restraint, separate from the restraint around the patio's outer perimeter."),
            faq("Does a gas fire pit need a permit?",
                "A fixed line run from a natural gas supply or a buried propane tank is plumbing and gas work and needs a licensed gas or plumbing contractor to make the connection and pull the permit, separate from the masonry or paver work around it. A portable propane fire table that runs off a swappable tank under the unit skips that step."),
            faq("Can a fire pit go on an existing paver patio, or does it need its own pad?",
                "Either works. Setting it into the main field keeps the yard reading as one continuous space, which suits a smaller lot, while a separate pad with its own pattern or a seat wall around it reads as a distinct zone and works better where the main patio already has a full seating or dining layout."),
            faq("Does an HOA need to approve a fire pit before it is built?",
                "A permanent, built-in fire feature is the kind of improvement most architectural review committees want to see in advance, since it changes the landscape plan and is often visible from neighboring lots. A portable propane fire table is less likely to trigger the same review in most communities, but that depends on the specific declaration."),
            ]
    related = [("/paver-patios/", "Paver patios & walkways"), ("/retaining-walls/", "Retaining walls"),
               ("/blog/retaining-wall-ideas-florida-yards/", "Retaining wall and seat wall ideas"),
               ("/blog/paver-patio-ideas-florida/", "Paver patio ideas"),
               ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete")]
    return page("/blog/fire-pit-on-pavers-florida/", "post",
                "Fire Pit on Pavers: Safe Setups for Florida Yards",
                "A fire pit on pavers in Florida: setback rules in Orange and Sarasota County, base and edge-restraint detail, and gas vs. wood-burning setups, October 2026.",
                "Fire Pits on Pavers: Safe Setups for Florida Backyards",
                capsule("A fire pit on a Florida paver patio needs a denser, separately restrained base section and a setback from the house "
                        "that depends on local rules: Orange County requires 25 feet unless the fire is contained in an outdoor fireplace, "
                        "grill or barbecue pit, and Sarasota County allows a contained fire pit as close as about 10 feet, as of October 2026. "
                        "A gas line needs a licensed plumbing or gas contractor; a portable propane unit does not."),
                body, faqs=faqs,
                sources=["icpi-ts3",
                         ("Orange County, Open Burning FAQ", "https://www.orangecountyfl.net/Portals/0/Library/Environment/docs/Open%20Burning%20Frequently%20Asked%20Questions-CERT.pdf"),
                         ("Sarasota County Code §54-116, Open Burning", "https://library.municode.com/fl/sarasota_county/codes/code_of_ordinances?nodeId=PTIICOOR_CH54ENNARE_ARTVAISOPO")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-patios",
                image=pid, form=False)


def p_backyard_putting_green_florida():
    pids = for_service("artificial-turf", 2)
    pid = pids[0] if pids else None
    body = "".join([
        sec("How Big Should a Backyard Putting Green Be?",
            f"<p>A backyard {svc('artificial-turf', 'putting green')} commonly runs anywhere from under 400 square feet, enough for a couple "
            "of cups and short chip shots, to over 2,000 square feet on a lot with room for a longer, multi-tier layout, and size is the single "
            "biggest driver of price per square foot, not the other way around. Small greens under about 400 square feet run higher per square "
            "foot, roughly $25 to $40, since labor and shaping cost about the same regardless of footprint; medium greens from 400 to 2,000 "
            "square feet run closer to $20 to $30; and larger greens over 2,000 square feet drop to roughly $15 to $25 per square foot "
            f"({src('angi-putting-green', 'Angi, backyard putting greens')}). A single hole with its flagstick adds about $150 on top of the "
            f"base turf cost ({src('angi-putting-green', 'Angi, backyard putting greens')}). {a('/artificial-turf-cost/', 'Our artificial turf cost guide')} "
            "breaks the full pricing picture down by size and use; this guide focuses on planning the layout itself.</p>"
            + (photo(pid, "Bright green artificial turf bordered by large gray pavers in a backyard setting.") if pid else "")),
        sec("What Makes Putting Green Turf Different From a Lawn Product?",
            "<p>A putting surface needs a short, dense, consistent pile so a ball rolls true rather than deflecting off individual blades the "
            "way it would on a taller lawn-replacement product, and it carries little or no infill on the putting surface itself so the roll "
            "stays predictable from edge to edge. The fringe and collar areas ringing the green, where chips and short approach shots land, "
            "usually step up to a slightly taller pile closer to a standard lawn turf, which both looks more natural against the surrounding "
            "yard and gives a short chip somewhere to settle rather than skidding across a surface built for putting, not landing a ball from "
            "the air.</p>"),
        sec("What Does the Base Look Like, and Does Florida's Turf Rule Apply?",
            "<p>Yes, the same way it applies to any other synthetic lawn: Florida's 2026 turf standard requires a permeable subgrade of washed "
            "crushed rock or crushed concrete under any synthetic turf on a residential lot of an acre or less, with no in-ground irrigation "
            f"allowed to water it ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}). What changes for a putting green specifically is how "
            "precisely that base gets screeded: a lawn panel tolerates small dips and crowns that a homeowner never notices underfoot, while a "
            "putting surface reads every low spot as a place a ball drifts toward rather than rolling across in a straight line, so the "
            "screeding pass is finished to a tighter tolerance before turf goes down. The rule also sets no new state permit for the turf itself, "
            "it establishes a material floor a local permit still has to meet, not an extra approval step on top of one.</p>"),
        sec("How Many Holes and Cups Should a Backyard Green Have?",
            "<p>Most residential greens carry one to three cups rather than a full nine, since each additional hole adds shaping, grading and "
            "break complexity without adding much practice value past the third or fourth pin position on a footprint under a few thousand "
            "square feet. Placing cups at varied distances and on different sections of slope, rather than clustering them on the flattest part "
            "of the green, is what actually builds a useful short-game practice tool rather than a flat patch of green turf with a hole cut in "
            "it; a single gentle swale or ridge running through the green gives each cup a different read even on a small footprint.</p>"),
        sec("Where Can a Putting Green Go Relative to a Pond, a Pool or a Property Line?",
            "<p>A backyard pond, a retention area or a canal edge brings the same water-setback rule into play that applies to any synthetic "
            "turf: the state standard requires turf to stay at least 10 feet back from a natural or constructed waterbody's water line unless "
            f"a seawall or similar barrier already separates the two ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}). A green drawn close "
            "to a mature oak or live oak runs into the same rule's tree-root protection, which keeps synthetic turf out from under a tree's "
            "canopy edge except where a certified arborist signs off that the installation will not damage what is growing underneath. "
            "Property-line setbacks for a putting "
            "green itself are a zoning question, not a turf-rule one, and vary by jurisdiction the way any other yard improvement's setback "
            f"does; {post('hoa-approval-for-pavers-and-concrete', 'our HOA approval guide')} is worth a read if the lot sits in a community "
            "with its own architectural review.</p>"),
        sec("Putting Green Size Tiers Compared",
            table("Backyard putting green size tiers", ["Size", "Typical price per sq ft", "What it fits"],
                  [["Small, under 400 sq ft", "$25–$40", "One or two cups, short chip-and-putt practice"],
                   ["Medium, 400–2,000 sq ft", "$20–$30", "Two or three cups, varied break and distance"],
                   ["Large, over 2,000 sq ft", "$15–$25", "Multiple holes, longer approach and chipping area"]],
                  f"{src('angi-putting-green', 'Angi, backyard putting greens')}. Each additional hole and flagstick adds about $150.")),
        sec("How Much Upkeep Does a Backyard Putting Green Need?",
            f"<p>A synthetic green needs less upkeep than a mowed and rolled natural green, but it is not maintenance-free: a putting surface "
            f"collects pollen, leaf litter and loose infill that has to be brushed and groomed on a routine basis to keep the roll consistent, "
            f"running roughly $250 to $550 a year for that upkeep nationally ({src('homeguide-putting-green', 'HomeGuide, backyard putting greens')}). "
            f"{post('how-to-clean-artificial-turf', 'Our turf cleaning and maintenance guide')} covers the brushing and debris routine that "
            "keeps a putting surface rolling true from one season to the next.</p>"),
    ])
    faqs = [faq("Does a backyard putting green need a permit in Florida?",
                "Florida's 2026 turf standard does not create a new state permit for synthetic turf; it sets a material and base floor that any local permit a jurisdiction already requires has to meet. Whether your specific lot needs a local permit for the turf work itself depends on the city or county, which is worth confirming before work starts."),
            faq("How many cups should a backyard putting green have?",
                "Most residential greens carry one to three cups rather than a full nine. Placing them at different distances and on different parts of a slope, rather than clustering them on the flattest section, builds more useful practice variety than adding a fourth or fifth hole to a small footprint."),
            faq("Can a putting green go near a pool or pond?",
                "A pond, retention area or canal brings Florida's 10-foot water-line setback into play, the same rule that applies to any synthetic turf, unless a seawall or similar barrier already separates the green from the water. A pool itself is a constructed waterbody under the same standard, so the same buffer logic applies there too."),
            faq("Is putting green turf different from regular artificial lawn turf?",
                "Yes. The putting surface itself uses a shorter, denser pile with little or no infill so a ball rolls true, while the fringe and collar areas around it step up to a taller pile closer to standard lawn turf, giving short chips somewhere to settle rather than skidding off a surface built for putting."),
            faq("How much does a backyard putting green cost compared to a regular lawn?",
                "More per square foot, since shaping breaks, grading cups and finishing the surface to a tighter tolerance all add labor that a flat lawn panel does not need. Small greens under 400 square feet run the highest per-square-foot cost, since labor costs about the same regardless of footprint size."),
            ]
    related = [("/artificial-turf/", "Artificial turf"), ("/artificial-turf-cost/", "Artificial turf cost guide"),
               ("/compare/artificial-turf-vs-sod/", "Artificial turf vs. sod"),
               ("/blog/how-to-clean-artificial-turf/", "Cleaning and maintaining artificial turf"),
               ("/blog/low-maintenance-backyard-florida/", "A low-maintenance backyard plan for Florida")]
    return page("/blog/backyard-putting-green-florida/", "post",
                "Backyard Putting Green Ideas for Florida Yards",
                "Planning a backyard putting green in Florida: size and price tiers, cup placement, Florida's 2026 turf rule and water setbacks, October 2026.",
                "Planning a Backyard Putting Green in Florida",
                capsule("A backyard putting green in Florida ranges from a small, under-400-square-foot green at $25 to $40 per square foot to "
                        "a large multi-hole green under $25, as of October 2026, built on the same permeable, washed-rock base Florida's 2026 "
                        "turf rule requires for any synthetic lawn. Cup placement and a varied slope matter more to how useful the green plays "
                        "than its total size does."),
                body, faqs=faqs,
                sources=["angi-putting-green", "homeguide-putting-green", "rule62-308-100-text"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf",
                image=pid, form=False)


def p_side_yard_ideas_florida():
    pids = for_service("paver-patios", 4)
    pid = pids[3] if len(pids) > 3 else (pids[0] if pids else None)
    body = "".join([
        sec("What Makes a Florida Side Yard Different to Plan For?",
            f"<p>A Florida side yard is often the narrowest usable strip on the lot, frequently carrying a drainage swale, a utility meter run "
            f"or a buried easement that a front or back yard rarely has to deal with, so a side-yard plan starts with what is already running "
            f"through that strip rather than with a finish material. {svc('artificial-turf', 'Turf')}, {svc('paver-patios', 'pavers')} and "
            "gravel all work in a narrow side yard, but each one interacts with a swale or easement differently, which is the real decision "
            "behind a side-yard redesign more than the look of any single material.</p>"
            + (photo(pid, "A paver stepping-stone path crossing a lawn toward a house, bordered by landscaping.") if pid else "")),
        sec("Can Artificial Turf Go in a Side Yard That Doubles as a Drainage Swale?",
            "<p>Not where the side yard is an engineered drainage swale carrying stormwater between lots: Florida's 2026 turf standard "
            "specifically bars synthetic turf inside a swale, ditch, stormwater pond or a pond's littoral zone, regardless of how shallow or "
            f"overgrown that swale currently looks ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}). A side yard that simply slopes a "
            "few inches toward a rear or side property line, without carrying a named, engineered swale, is a different situation, and turf "
            "there still has to meet the rule's permeability and grading requirements so water keeps moving through rather than pooling against "
            "the house. Checking whether a specific strip is a mapped drainage easement or just a graded low point is worth doing before "
            "ordering material, not after a crew shows up to install it.</p>"),
        sec("Are Pavers Allowed in a Side-Yard Easement?",
            "<p>Often not, or only with the easement holder's sign-off, since a paved surface can block the access a utility or the county "
            "needs to maintain what runs underneath it. Sarasota County's drainage easement rule is explicit on this point for residential "
            f"lots: no walkway, driveway or other paved surface may be located in the easement at all ({src('sarasota-county-124-255-culverts', 'Sarasota County Code')}). "
            "A removable or permeable surface, large-format stepping stones set with open joints rather than a continuously bonded paver field, "
            "is sometimes acceptable where a solid surface is not, because it still allows the ground underneath to be reached if a line ever "
            "needs repair; confirming that with the specific easement holder, not assuming it, is the safer order of operations. Gravel and "
            "compacted stone also count as impervious surface for lot-coverage purposes in at least one jurisdiction we checked, so a side "
            "yard's material choice can affect a lot's overall impervious surface ratio even when nothing is poured or set in mortar "
            f"({src('sanford-schedule-f', 'City of Sanford, Schedule F')}).</p>"),
        sec("How Wide Does a Side-Yard Path Actually Need to Be?",
            f"<p>Wide enough for one person to walk comfortably with something in hand, a trash can, a hose reel or a ladder, which in "
            "practice means most side-yard paths land narrower than a front walkway or a connecting path elsewhere on the lot. A path built "
            "exactly to the clear width between the house and a fence or property line leaves no margin for a planting bed or a utility box "
            "along the way, so measuring the full available width before committing to a path's finished width avoids a redesign once a meter "
            f"or a hose bib turns up mid-strip. {svc('paver-patios', 'Our paver patio and walkway page')} covers the base spec a path this "
            "narrow still needs.</p>"),
        sec("What Works Better in a Narrow, Shaded Side Yard: Turf, Pavers or Gravel?",
            "<p>A side yard that runs along the shaded north or west face of a neighboring house dries out more slowly after rain than an open "
            f"yard does, which matters more for material choice than square footage does. {svc('paver-sealing', 'Sealed pavers')} resist the "
            f"mold and algae a shaded, damp strip tends to grow faster than {post('mold-and-algae-on-pavers-florida', 'a sun-exposed patio does')}, "
            "while turf's open, permeable backing drains the strip without holding surface water the way bare dirt or mulch can in a narrow, "
            "low-airflow gap between two houses. Loose gravel moves and scatters in a strip this narrow more than it does spread across an open "
            "yard, since foot traffic in a tight side yard tends to follow one worn line rather than spreading the load, which is often the "
            "reason a gravel side yard needs regular raking that a paver or turf strip does not.</p>"),
        sec("What Should a Side-Yard Gate and Access Path Plan Around?",
            "<p>An AC condenser, a gas or electric meter, a hose bib and the gate itself are the fixed points most side yards are built around, "
            "and planning the path's layout after those are marked, rather than running a straight line and working around them later, avoids "
            "an awkward jog partway down the strip. A gate wide enough for a trash can or a wheelbarrow, rather than just a person, is worth "
            "the extra foot of clearance if the side yard is the route trash and recycling bins travel on collection day, which it usually is "
            "on a lot with no direct side access from the driveway.</p>"
            + table("Side yard material options", ["Material", "Works well where", "Watch for"],
                    [["Artificial turf", "A graded, non-swale strip; shaded ground that stays damp as bare soil", "Barred inside a mapped drainage swale or easement"],
                     ["Paver stepping stones, open joints", "A utility or drainage easement that needs access preserved", "Confirm with the easement holder before installing"],
                     ["Full paver or concrete path", "A clear strip outside any easement, used as regular walking access", "Counts toward a lot's impervious surface total"],
                     ["Gravel", "A low-traffic strip with no fixed walking line", "Scatters along a single worn path with regular foot traffic"]],
                  "Confirm which, if any, of these conditions apply to a specific strip before ordering material.")),
        sec("How Does a Side Yard Fit Into a Whole-Backyard Plan?",
            f"<p>A side yard is usually the connector between the front of the house and the main backyard space, so its material and width "
            f"choices work best when they are set after the backyard's own plan, not before it. {post('low-maintenance-backyard-florida', 'Our low-maintenance backyard guide')} "
            "covers the whole-yard version of this planning question, zoning turf, pavers and planting beds across a full lot rather than one "
            "narrow strip.</p>"),
    ])
    faqs = [faq("Can artificial turf go in a Florida side yard?",
                "Only if that strip is not a mapped, engineered drainage swale, ditch or stormwater feature, which Florida's 2026 turf rule bars turf from regardless of how it currently looks. A side yard that is simply graded to slope away from the house, without carrying a named swale, is a different case and can usually carry turf if it meets the rule's drainage and permeability standard."),
            faq("Can pavers be installed in a drainage or utility easement along the side of the house?",
                "Often not. Sarasota County's rule bars any walkway, driveway or paved surface in a drainage easement outright, and other jurisdictions review easement work case by case. A removable, open-jointed stepping-stone layout is sometimes acceptable where a solid paver field is not, since it still allows access to what runs underneath."),
            faq("How wide should a side-yard path be?",
                "Wide enough to walk comfortably while carrying a trash can, hose reel or ladder, which in practice lands narrower than most front walkways. Measuring the full clear width between the house and the fence or property line before fixing a finished width avoids a redesign if a meter or hose bib turns up mid-strip."),
            faq("Is gravel a good option for a narrow side yard?",
                "It works where there is no fixed walking line, but foot traffic in a narrow strip tends to follow one worn path rather than spreading out, which scatters loose gravel faster than it would across an open yard. Gravel can also count toward a lot's impervious surface total in some jurisdictions, worth checking before assuming it is the lower-impact choice."),
            faq("Does a shaded side yard need a different material than a sunny one?",
                "It is worth favoring a material that handles standing moisture well. A shaded, low-airflow side yard dries more slowly after rain, which favors sealed pavers or turf's permeable backing over bare dirt, mulch or an unsealed surface that tends to grow mold or algae faster in that kind of spot."),
            ]
    related = [("/paver-patios/", "Paver patios & walkways"), ("/artificial-turf/", "Artificial turf"),
               ("/blog/low-maintenance-backyard-florida/", "A low-maintenance backyard plan for Florida"),
               ("/blog/permeable-pavers-and-drainage-florida/", "Permeable pavers and yard drainage"),
               ("/blog/mold-and-algae-on-pavers-florida/", "Stopping mold and algae on pavers")]
    return page("/blog/side-yard-ideas-florida/", "post",
                "Side Yard Ideas for Florida Homes: Turf or Pavers",
                "Side yard ideas for Florida homes: turf vs. pavers vs. gravel in a narrow strip, drainage swale and easement rules, as of October 2026.",
                "Side Yard Ideas for Florida Homes: Turf, Pavers or Gravel",
                capsule("Side yard ideas for Florida homes start with what already runs through that narrow strip: a drainage swale, a "
                        "utility easement or a meter run. Florida's 2026 turf rule bars synthetic turf inside a mapped swale or stormwater "
                        "feature, and some counties bar paved surfaces from a drainage easement outright, as of October 2026, which narrows "
                        "the material choice more than the side yard's width does."),
                body, faqs=faqs,
                sources=["rule62-308-100-text", "sarasota-county-124-255-culverts", "sanford-schedule-f"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf",
                image=pid, form=False)


def p_low_maintenance_backyard_florida():
    pids = for_service("artificial-turf", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("What Does a Low-Maintenance Backyard Plan Actually Cut Out?",
            f"<p>A low-maintenance Florida backyard plan replaces the parts of a yard that demand the most routine time, mowing, edging and "
            f"watering turf grass, with {svc('artificial-turf', 'synthetic turf')}, {svc('paver-patios', 'paver')} or "
            f"{svc('concrete-patios', 'concrete')} hardscape and a smaller bed of plants matched to the site, rather than trying to reduce "
            "upkeep on the same amount of lawn. It does not mean no planting at all; a yard with zero live plants reads flat and loses the "
            "shade and screening a few well-placed trees and shrubs still provide. The goal is fewer square feet that need a mower, an edger "
            "and a sprinkler zone, not fewer square feet that need any attention whatsoever.</p>"
            + (photo(pid, "A manicured green lawn beside a covered patio with outdoor seating.") if pid else "")),
        sec("How Do You Zone a Yard Into Turf, Hardscape and Planting?",
            "<p>The most workable low-maintenance layouts split a backyard into three zones rather than blending turf and planting beds "
            "across the whole lot: a hardscape zone for the patio, path and any fire pit or seating area; a turf zone sized to where bare feet "
            "and pets actually use open lawn; and a planting zone kept to borders, foundation beds and a few specimen trees rather than spread "
            "thin across the yard. Planting pulled to the edges also keeps irrigation zones simple, since beds along a fence line or the house "
            "can run on one drip zone while the open turf area needs none at all, rather than scattering individual beds that each need their "
            "own watering schedule across an otherwise synthetic lawn.</p>"),
        sec("How Does Florida-Friendly Landscaping Fit a Low-Maintenance Plan?",
            f"<p>The University of Florida's Florida-Friendly Landscaping program sets out nine principles for the state's climate and soils, "
            "starting with \"right plant, right place,\" choosing species suited to a site's sun, shade and water availability rather than "
            f"fighting the site to keep an unsuited plant alive, through watering efficiently and reducing stormwater runoff "
            f"({ext('https://ffl.ifas.ufl.edu/about-ffl/9-principles/', 'UF/IFAS, Florida-Friendly Landscaping, Nine Principles')}). A yard "
            "built around those principles for its remaining planted beds, paired with turf and hardscape for the rest, tends to need less "
            "routine input across the board than a lawn-only yard with a handful of mismatched ornamentals scattered through it.</p>"),
        sec("Does Cutting Lawn Area Actually Reduce Watering Under Current Restrictions?",
            "<p>Yes, directly, since both water management districts covering our service areas currently limit how often and how long a lawn "
            "can be watered rather than how much total area exists to water. The St. Johns district's year-round schedule for the Orlando area "
            "caps each irrigation zone at about three-quarters of an inch per run, and several Orlando-area counties currently sit under a "
            f"stricter once-a-week emergency order on top of that baseline ({src('sjrwmd-watering', 'SJRWMD watering restrictions')}). The "
            "Southwest Florida district's current order for Sarasota and Manatee runs through March 2027 and limits watering to one day a "
            f"week within narrow overnight windows ({src('swfwmd-restrictions', 'SWFWMD district water restrictions')}). A smaller turf-grass "
            "footprint means fewer zones competing for those limited watering windows, and the synthetic turf or hardscape replacing the rest "
            "of the lawn draws no water at all.</p>"),
        sec("What Role Does Hardscape Play in a No-Mow Yard?",
            f"<p>A paver or concrete patio, path and a {svc('retaining-walls', 'seat wall')} or planter edge do more than give the yard a "
            "place to sit; they set the hard boundary a turf or planting zone butts against, which keeps the layout crisp instead of a lawn "
            "or turf edge that drifts and blurs into beds over a season or two without a physical edge holding the line. A generously sized "
            "patio, planned as the anchor the rest of the yard is zoned around rather than an afterthought carved out of leftover space, "
            f"usually does more to cut routine upkeep than any single planting or turf decision does on its own. {post('paver-patio-ideas-florida', 'Our paver patio ideas guide')} "
            "and " + post('concrete-patio-ideas-florida', 'our concrete patio ideas guide') + " cover layout options for that anchor space.</p>"),
        sec("How Much of the Yard Can Reasonably Go Hardscape or Turf?",
            "<p>Most residential zoning caps how much of a lot can go impervious regardless of what a homeowner would prefer, so a low-maintenance "
            "plan has to work within that ceiling rather than around it; one Sarasota-area jurisdiction we checked caps combined driveway, "
            f"parking and turnaround impervious area at 40 percent of the required front or street-side yard alone, separate from the rest of "
            f"the lot ({src('orlando-ord-2022-45', 'City of Orlando, Ordinance 2022-45')}). Artificial turf counts as pervious under Florida's "
            "2026 turf rule when it is built to the rule's permeable base standard, which is part of why it often fits inside a stricter "
            "impervious-surface limit in a way a poured patio of the same footprint would not.</p>"),
        sec("Low-Maintenance Backyard Zones Compared",
            table("Low-maintenance backyard zones", ["Zone", "Typical material", "What it replaces"],
                  [["Hardscape anchor", "Pavers or concrete patio, path, seat wall", "A mowed lawn area used for seating, dining or a fire pit"],
                   ["Turf zone", "Artificial turf, sized to actual foot traffic", "The portion of lawn that mainly needs mowing, not walking on"],
                   ["Planting zone", "Borders, foundation beds, a few specimen trees", "Scattered beds that each need their own watering and weeding"]],
                  "A yard that keeps these three zones distinct generally needs fewer separate maintenance routines than one that blends them.")),
    ])
    faqs = [faq("Does a low-maintenance backyard mean no plants at all?",
                "No. A yard with zero live plants loses shade and screening that only trees and shrubs provide, and most low-maintenance plans keep a planting zone, usually at the borders and foundation beds, while cutting back the lawn area that needs routine mowing and watering."),
            faq("Does less lawn area really save water under current restrictions?",
                "Yes, directly. Both water management districts covering Greater Orlando and Sarasota-Manatee currently limit watering frequency and duration rather than total area, so a smaller turf-grass footprint competes for fewer of those limited watering windows, and synthetic turf or hardscape draws no water at all."),
            faq("How much of a backyard can be turned into patio or turf?",
                "It depends on local zoning, which typically caps how much of a lot can go impervious regardless of preference. Artificial turf built to Florida's 2026 turf rule generally counts as pervious, which is part of why it often fits inside a stricter impervious-surface limit better than a poured patio of the same footprint."),
            faq("What is Florida-Friendly Landscaping, and does it apply to a low-maintenance plan?",
                "It is a University of Florida program built around nine principles for the state's climate and soils, starting with matching plants to a site's actual sun, shade and water conditions. A low-maintenance yard that applies those principles to its remaining planted beds, alongside turf and hardscape for the rest, tends to need less routine care than a lawn-only yard with mismatched plantings."),
            faq("Should the patio or the planting plan come first in a yard redesign?",
                "The patio or other hardscape anchor is usually worth planning first, since it sets a physical edge the turf and planting zones butt against. Planning planting beds first and fitting hardscape into whatever space is left tends to produce a more fragmented layout."),
            ]
    related = [("/artificial-turf/", "Artificial turf"), ("/paver-patios/", "Paver patios & walkways"),
               ("/concrete-patios/", "Concrete patios"), ("/compare/artificial-turf-vs-sod/", "Artificial turf vs. sod"),
               ("/blog/side-yard-ideas-florida/", "Side yard ideas for Florida homes")]
    return page("/blog/low-maintenance-backyard-florida/", "post",
                "Low-Maintenance Backyard Ideas for Florida Yards",
                "A low-maintenance backyard plan for Florida: zoning turf, pavers and planting beds, watering restrictions and impervious limits, October 2026.",
                "A Low-Maintenance Backyard Plan for Florida (Turf, Pavers and Concrete)",
                capsule("A low-maintenance Florida backyard plan zones a lot into a hardscape anchor, a sized turf area and a smaller planting "
                        "zone, replacing the lawn area that demands the most mowing and watering. As of October 2026, both regional water "
                        "management districts limit lawn watering by schedule, not by area, so cutting turf-grass square footage cuts watering "
                        "demand directly while synthetic turf and hardscape draw no water at all."),
                body, faqs=faqs,
                sources=["sjrwmd-watering", "swfwmd-restrictions", "orlando-ord-2022-45", "rule62-308-100-text",
                         ("UF/IFAS, Florida-Friendly Landscaping, Nine Principles", "https://ffl.ifas.ufl.edu/about-ffl/9-principles/")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf",
                image=pid, form=False)


def p_retaining_wall_ideas_florida_yards():
    pids = for_service("retaining-walls", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("What Retaining Wall and Seat Wall Ideas Work in a Florida Yard?",
            f"<p>Most {svc('retaining-walls', 'retaining wall')} work homeowners actually ask for in Florida turns out to be a seat wall, a "
            "raised garden bed or a short terraced wall rather than a tall structural wall holding back a serious grade change, since most "
            "Florida lots are flat enough that the yards needing a true engineered wall are the exception. The design choices below, height, "
            "terracing, block color and what the wall doubles as, all sit on top of the base and drainage spec covered on the retaining wall "
            f"service page and the height thresholds covered in {a('/retaining-wall-cost/', 'the retaining wall cost guide')}; this guide "
            "focuses on what a wall looks like and does, not what it costs or when it needs an engineer.</p>"
            + (photo(pid, "A modular concrete retaining wall built into a grassy slope, backfilled with gravel.") if pid else "")),
        sec("What Is a Seat Wall, and What Design Choices Go Into One?",
            "<p>A seat wall is built for sitting rather than holding back soil, usually free-standing or backed by only a shallow grade "
            "change, which is why most seat walls skip the drainage column a true retaining wall needs behind its face. The standard comfort "
            "range for a seat wall's height runs from about 18 to 24 inches, close to a dining chair's seat height, with a cap at least 12 "
            "inches wide so two people can share it without crowding, and a wall built closer to 24 inches than 18 generally needs a backrest "
            f"or a taller planting bed behind it to feel finished rather than exposed "
            f"({ext('https://www.landscapingnetwork.com/walls/seat-walls.html', 'Landscaping Network, seat walls')}). "
            f"A seat wall built around a {post('fire-pit-on-pavers-florida', 'fire pit')} is one of the most common pairings in both service "
            "areas, since it gives a fire feature fixed seating without adding furniture that has to be pulled back from the heat every time "
            "the pit is lit.</p>"),
        sec("How Do You Build a Retaining Wall for a Raised Garden Bed?",
            "<p>A raised bed is closer to a small retaining wall than a planter box is, since the soil and mulch packed inside it hold "
            "moisture against the back of the block much the way backfill does behind a full-height wall, just at a smaller scale and over a "
            "shorter run. Free-draining aggregate behind the face, rather than garden soil packed straight against the block, keeps that "
            "moisture from working the joints apart over a few rainy seasons, and a bed built without that drainage layer is the most common "
            "reason a raised garden wall starts leaning or separating well before a comparable retaining wall would. A bed built two or three "
            "courses tall, roughly 12 to 18 inches, is usually enough to raise soil above a flatwoods yard's shallow water table without "
            "needing the engineering review a taller freestanding wall can trigger.</p>"),
        sec("Can a Tall Grade Change Be Handled Without One Tall Wall?",
            "<p>Often, yes, by terracing a slope into two or three shorter walls separated by a planted or turfed step rather than building "
            "one wall tall enough to take the whole grade change at once. Terracing spreads the lateral load across multiple shorter, simpler "
            "walls instead of concentrating it on a single face, and since several jurisdictions in our service areas set their engineering "
            "trigger at a specific wall height rather than at the total grade change across a yard, a terraced design can sometimes keep each "
            "individual wall under that threshold even where one tall wall would cross it. The planted step between tiers also does double "
            "duty as a planting bed, which a single tall wall's face never offers.</p>"),
        sec("What Wall Styles and Colors Work in Florida Yards?",
            "<p>Segmental block, the interlocking, dry-stacked system most residential walls in both service areas use, comes in a range of "
            "tan, gray and charcoal tones, chosen most often to either match the paver field it borders or sit as a deliberate contrast "
            "against it rather than disappear into the same palette. A boulder or natural-stone-faced wall reads less formal and suits a "
            "wooded or naturally sloped lot better than a crisp block system does, though it generally costs more per linear foot for the "
            "same height. A wall's cap course, the top row the eye actually lands on from a distance, is worth choosing deliberately even on "
            "a budget wall, since a contrasting cap color does more to dress up a plain wall face than upgrading every course underneath it.</p>"),
        sec("Why Does Clermont See More Retaining Wall and Terracing Work Than Flatter Towns Nearby?",
            f"<p>{city('clermont')} and the rest of the Lake County ridge sit on genuinely hilly ground for Central Florida, part of the "
            "Lake Wales Ridge, where excessively drained sandy soils and real grade change between a house pad and the street are common in "
            "a way they are not on the flatter land closer to Orlando or the coast. That terrain is why terracing, seat walls built into a "
            "slope rather than a flat yard, and raised beds that double as erosion control show up more often in {} than elsewhere in the "
            f"Orlando unit's service area. {post('lake-and-polk-county-driveway-permits', 'Our Lake and Polk County permit guide')} covers the "
            "driveway and patio side of building on sloped ground in that part of the county.</p>".format(city("clermont"))),
        sec("What Pairs Well With a Retaining Wall in a Backyard Design?",
            f"<p>A seat wall or a short terraced wall is often planned alongside a {svc('paver-patios', 'paver patio')} rather than as a "
            f"standalone feature, since the wall gives the patio a defined edge the way a planting bed alone does not, and a {svc('artificial-turf', 'turf')} "
            "step between tiers on a terraced slope keeps the grade change from reading as bare dirt between two hard surfaces. "
            f"{post('low-maintenance-backyard-florida', 'Our low-maintenance backyard guide')} covers zoning a whole lot around a hardscape "
            "anchor, which a retaining or seat wall is often part of on a yard with any real grade change to work around.</p>"),
    ])
    faqs = [faq("What is the difference between a seat wall and a retaining wall design-wise?",
                "A seat wall is built for sitting and usually holds back little or no soil, so its main design requirement is a comfortable height, generally 18 to 24 inches, and a cap wide enough to sit on. A retaining wall holds real lateral pressure from a slope behind it and needs a drainage column and, past certain heights set by the local jurisdiction, engineered drawings."),
            faq("Can a tall slope be handled without one tall retaining wall?",
                "Often yes, by terracing the grade change into two or three shorter walls separated by a planted step rather than one wall built to the full height. Terracing spreads the load across multiple simpler walls and can sometimes keep each individual wall under a jurisdiction's engineering-review threshold."),
            faq("What height works best for a seat wall?",
                "About 18 to 24 inches, close to a dining chair's seat height, with a cap at least 12 inches wide so it is comfortable for two people to share. A wall built toward the taller end of that range usually benefits from a backrest or a planting bed behind it."),
            faq("Does a raised garden bed need the same drainage as a full retaining wall?",
                "It needs the same principle at a smaller scale: free-draining aggregate behind the block rather than garden soil packed straight against it, since the moisture held inside a planted bed works the joints apart the same way backfill does behind a taller wall, just over a shorter run."),
            faq("Why do Clermont and the Lake County ridge see more retaining wall work?",
                "That part of Lake County sits on the Lake Wales Ridge, genuinely hilly ground with excessively drained sandy soils and real grade change between a house pad and the street, conditions that are less common on the flatter land closer to Orlando or the coast."),
            ]
    related = [("/retaining-walls/", "Retaining walls"), ("/retaining-wall-cost/", "Retaining wall cost guide"),
               ("/blog/fire-pit-on-pavers-florida/", "Fire pits on pavers"),
               ("/blog/low-maintenance-backyard-florida/", "A low-maintenance backyard plan for Florida"),
               ("/blog/lake-and-polk-county-driveway-permits/", "Lake and Polk County permits")]
    return page("/blog/retaining-wall-ideas-florida-yards/", "post",
                "Retaining Wall Ideas for Florida Backyards",
                "Retaining wall and seat wall ideas for Florida yards: seat wall height, raised garden beds, terracing a slope and Clermont's ridge terrain, October 2026.",
                "Retaining Wall and Seat Wall Ideas for Florida Yards",
                capsule("Retaining wall ideas for Florida yards run from a seat wall built 18 to 24 inches tall around a patio or fire pit to "
                        "a raised garden bed two or three courses high to terracing a steep slope into shorter stepped walls instead of one "
                        "tall wall, as of October 2026. Lake County's Clermont ridge sees more of this work than flatter towns nearby because "
                        "of its genuinely hilly terrain."),
                body, faqs=faqs,
                sources=[("Landscaping Network, seat walls", "https://www.landscapingnetwork.com/walls/seat-walls.html")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="retaining-walls",
                image=pid, form=False)


def get_pages():
    return [p_extend_patio_under_screen_enclosure(), p_fire_pit_on_pavers_florida(), p_backyard_putting_green_florida(),
            p_side_yard_ideas_florida(), p_low_maintenance_backyard_florida(), p_retaining_wall_ideas_florida_yards()]
