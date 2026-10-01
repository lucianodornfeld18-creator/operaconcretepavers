# -*- coding: utf-8 -*-
"""Artificial turf service page (its own pillar) and the concrete / pavers pillar pages."""
from _data import SERVICES, SERVICE_ORDER
from _helpers import page, capsule, sec, table, faq, ul, steps, a, svc, cs, post, compare, src, price, per, photo, offer, thumb
from _photos import for_service
from _posts import cost_for


def _cards(pillar):
    out = []
    for k in SERVICE_ORDER:
        S = SERVICES[k]
        if S["pillar"] == pillar:
            pid = (for_service(k, 1) or [None])[0]
            img = thumb(pid) if pid else ""
            cost = cost_for(k)
            cl = f' &middot; <a href="{cost}">cost guide</a>' if cost else ""
            out.append(f'<li class="card">{img}<h3><a href="{S["route"]}">{S["name"]}</a></h3><p><small>Market range {price(S["price"])} per {per(S["price"])}{cl}</small></p></li>')
    return '<ul class="grid">' + "".join(out) + "</ul>"


def turf():
    K = "artificial-turf"
    pids = for_service(K, 2)
    body = "".join([
        sec("What an artificial turf project covers",
            "<p>This service covers four kinds of work, and most jobs mix at least two of them. A full front or back lawn replaces sod with a synthetic lawn panel, graded and based the same way across the yard. A pet area is usually a fenced run or a side strip built with a more open-backed turf and a steeper drainage slope, since it carries far more liquid than a lawn ever does. A backyard putting green is a different product, a short, dense nylon or polyethylene face with little or no infill, set on a flatter, more precisely screeded base than a lawn panel needs. Turf between pavers, a narrow accent strip inside a driveway, along a walkway edge or framing a fire pit, follows the same subgrade rule as the rest of the yard but ties into the paver field's existing edge restraint instead of standing on its own perimeter. Lawn, pet area, putting green or paver accent, all four now answer to the same state material and base standard.</p>"
            + (photo(pids[0], "Bright green artificial turf lawn bordered by large concrete pavers next to a swimming pool.") if pids else "")),
        sec("The 2026 Florida turf standard: what DEP Rule 62-308.100 requires",
            "<p>Florida didn't regulate synthetic turf at the state level until recently. HB 683, passed in 2025, created F.S. 125.572 and directed the Department of Environmental Protection to write minimum standards for turf on single-family lots of one acre or less "
            f"({src('hb683', 'HB 683, 2025')}; {src('fs125-572', 'F.S. 125.572')}). DEP adopted Rule 62-308.100 to do that, and it took effect May 19, 2026 ({src('flrules62-308-100', 'FLRules 62-308.100')}). The rule doesn't create a new state permit; it sets the floor a compliant lawn has to clear, whichever city or county issues the local permit.</p>"
            + table("Florida's turf standard, Rule 62-308.100 (effective May 19, 2026)", ["Requirement", "What it means"],
                    [["Materials", "No heavy metals or intentionally added PFAS in turf, backing or infill; everything disposable at a landfill"],
                     ["Infill", "Clean silica sand, rock, shell or coated silica sand only; rubber infill limited to inside playground-equipment footprints"],
                     ["Subgrade / base", "Washed crushed rock or crushed concrete; no limerock or road base with fines"],
                     ["Permeability", "Turf and backing must be permeable over a pervious subgrade; a local government may set a 10 in/hour maximum"],
                     ["Irrigation", "In-ground irrigation can't water turf; a local government may require existing heads capped below grade"],
                     ["Water setback", "At least 10 ft from a natural or man-made waterbody, unless a seawall or bulkhead already separates the yard from it"],
                     ["Tree drip lines", "No turf inside a tree's drip line unless a certified arborist signs off that installing it won't harm the roots"],
                     ["Anchoring", "Edges and seams anchored against wind and flooding, on top of the manufacturer's own installation spec"]],
                    f"{src('rule62-308-100-text', 'Rule 62-308.100, adopted text')}.")
            + "<p>Two more requirements sit outside that table: turf can't go inside a swale, ditch, stormwater pond or a pond's littoral zone, and it can't block a septic tank's access lid, since pump-out crews still need to reach it with the lawn installed.</p>"),
        sec("Who the law actually binds: local governments, not HOAs",
            f"<p>The preemption in F.S. 125.572 reaches local governments only. Once DEP's rule took effect, a city or county can no longer ban compliant turf or write a stricter local standard ({src('fs125-572', 'F.S. 125.572')}). Community development districts keep the right to enforce their own deed restrictions, a carve-out added in 2026, and the statute never mentions homeowners' associations at all. That distinction holds because an HOA is a private contract, not a unit of local government, and a different statute governs what it can and can't restrict.</p>"
            f"<p>F.S. 720.3045 is the statute homeowners usually mean when they ask whether an HOA can ban turf, and it protects less than most people assume. It bars an association from restricting items that aren't visible from the parcel's frontage, an adjacent parcel, an adjacent common area or a community golf course, naming artificial turf specifically among those items ({src('fs720-3045', 'F.S. 720.3045')}). A backyard lawn hidden by a fence usually qualifies; a front lawn facing the street usually doesn't, since it's the one place turf is most visible. Florida law also stopped HOAs, as of 2026, from requiring a government permit to already be issued before the board will review an application, so the two approvals can move together instead of one waiting on the other "
            f"({src('fs720-3035', 'F.S. 720.3035')}). {post('florida-hoa-artificial-turf-law', 'Our full read on Florida HOAs and the turf law')} and {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for pavers or turf')} go further.</p>"),
        sec("How a turf lawn is installed, step by step",
            "<p>The order rarely changes between a lawn, a pet area and a paver accent strip; what changes is the detail inside each step.</p>"
            + steps([("Remove the old lawn or bed.", "Sod, mulch and any irrigation heads inside the turf footprint come out down to bare soil."),
                     ("Grade and compact the base.", "Washed crushed rock or crushed concrete goes down in thin lifts, graded for positive drainage and kept open enough to meet the rule's permeability standard."),
                     ("Cap or redirect irrigation.", "Heads inside the turf zone are capped below grade or moved to serve beds and sod that still need them, since the rule bars watering turf with an in-ground system."),
                     ("Roll out and seam the turf.", "Panels are trimmed to the footprint and joined at seams rather than overlapped, with extra care on any run that crosses a slope."),
                     ("Add infill and brush the pile.", "Clean sand, rock or shell infill, never rubber outside a playground footprint, is worked into the pile with a power broom."),
                     ("Anchor the perimeter.", "Edges and seams are nailed or spiked at tighter spacing than the open field, the anchoring the rule requires against wind and flooding.")])
            + (photo(pids[1], "A manicured artificial turf lawn beside a covered patio with outdoor seating.") if len(pids) > 1 else "")
            + f"<p>{post('artificial-turf-installation-process', 'The full walkthrough of how turf goes in')} covers the base work in more detail, including what changes on a sandy ridge lot versus a flatwoods yard.</p>"),
        sec("Lawns, pet areas, putting greens and turf between pavers: how the build changes",
            "<p>All four uses start from the same rule, but the backing, infill and base thickness shift with how the surface gets used.</p>"
            + table("Turf by use: what changes", ["Use", "Backing and base", "Infill", "Note"],
                    [["Lawn panel", "Standard washed-rock base", "Clean sand or rock", "Widest range of pile heights and colors"],
                     ["Pet area", "More open, perforated backing for faster drainage", "Light, natural infill, rinsed on a routine", "Hose rinsing keeps odor down since the lawn can't be watered by an in-ground zone"],
                     ["Putting green", "Flatter, more precisely screeded base", "Little to none on the putting surface itself", "Fringe around the cups is built closer to lawn spec"],
                     ["Paver accent strip", "Same washed-rock base, tied into the paver's edge restraint", "Matches the surrounding turf", "Edge restraint, not nails alone, holds the seam where turf meets pavers"]])
            + f"<p>{post('backyard-putting-green-florida', 'Planning a backyard putting green')} and {post('artificial-turf-for-dogs-florida', 'turf for dogs: odor, drainage and infill')} go deeper on those two uses specifically.</p>"),
        sec("What artificial turf costs in Florida",
            f"<p>As of October 2026, installed turf runs {price('artificial-turf')} per {per('artificial-turf')} in Florida and national market data, typically {price('artificial-turf', True)}. Angi's Orlando-specific figures put the average project at $4,758, with a typical range of $2,811 to $6,950 for excavation, base and turf material together "
            f"({src('angi-turf-orlando', 'Angi, Orlando')}). Tampa's figures run higher, averaging $7,246 ({src('angi-turf-tampa', 'Angi, Tampa')}), a reminder that these ranges move with yard size, slope and how much of the old lawn has to come out, not with which Florida city the work is in. A backyard putting green costs more per square foot than a lawn panel, commonly $15 to $40 depending on size, since a small green carries more labor per square foot than an open lawn does "
            f"({src('homeguide-putting-green', 'HomeGuide, putting greens')}; {src('angi-putting-green', 'Angi, putting greens')}). These are market ranges compiled from published Florida and national cost-guide data, not a quote for your yard; a written price follows a site visit. The {a('/artificial-turf-cost/', 'artificial turf cost guide')} breaks the numbers down further by size and use.</p>"),
        sec("Water restrictions make turf worth a second look in 2026",
            f"<p>Both water management districts covering our service areas are under tighter-than-normal rules as of October 2026, part of why turf keeps coming up as an option. In the Orlando unit's counties, the St. Johns River Water Management District's year-round schedule already limits lawn irrigation to set days, caps each zone at roughly an inch of water, and bars watering between 10 a.m. and 4 p.m.; parts of Lake County and several neighboring counties currently sit under a Phase III Extreme Water Shortage order that cuts watering to one day a week "
            f"({src('sjrwmd-watering', 'SJRWMD watering restrictions')}). On the Sarasota side, the Southwest Florida Water Management District's Modified Phase III Extreme Water Shortage order, in effect April 3, 2026 through March 31, 2027 across Sarasota, Manatee, Polk and several neighboring counties, limits watering to one day a week by the last digit of the street address, inside two narrow overnight or late-evening windows "
            f"({src('swfwmd-restrictions', 'SWFWMD district water restrictions')}). Manatee County confirms it's following that order through March 2027 ({src('manatee-phase3', 'Manatee County, Modified Phase III')}), and the City of Sarasota reports the same extension ({src('sarasota-city-phase3', 'City of Sarasota, Modified Phase III')}). Turf built to Rule 62-308.100 never draws on an in-ground irrigation zone in the first place, which sidesteps that restriction schedule rather than working around it. "
            f"{post('artificial-turf-water-savings-florida', 'How much water and money turf saves')} and {compare('artificial-turf-vs-sod', 'turf vs. sod in Florida')} cover the trade-off in more depth.</p>"),
        sec("Turf and Florida heat",
            "<p>Turf gets hotter underfoot in direct Florida sun than the grass it replaces, and darker fiber and infill both absorb more heat than light-colored stone or concrete nearby. We don't have a verified, Florida-specific measurement to publish for how much hotter a given product runs, since the figures in circulation vary by manufacturer and test method and we won't print a number we can't stand behind. What does help in practice: siting turf where afternoon shade reaches it, picking a lighter infill color where the product line offers one, and a quick hose rinse before bare feet or pets use it, which is allowed since a hose isn't the in-ground system the state rule restricts. "
            f"{post('artificial-turf-heat-in-florida', 'Our full look at turf heat in Florida')} compares turf against pavers and concrete nearby.</p>"),
        sec("Caring for artificial turf",
            "<p>A new lawn needs less upkeep than sod, but not none. Leaves, oak pollen and storm debris sit on top of the pile instead of breaking down into soil, so a regular pass with a blower or a stiff broom keeps the surface from matting. Infill migrates toward low spots and high-traffic paths over a few seasons and needs the occasional top-up with the same natural material the rule requires at installation, never a rubber substitute swept in to save a trip. A pet area benefits from a routine hose rinse rather than an occasional deep clean, since odor comes from liquid sitting on the infill, not from the turf fibers themselves. "
            f"{post('how-to-clean-artificial-turf', 'Our turf cleaning and maintenance guide')} covers the full routine, season by season.</p>"),
        sec("How do you find the best artificial turf installer near you?",
            "<p>Searching for artificial turf installers near you turns up landscaping companies, pool contractors and general handymen alongside dedicated turf crews, and the state's new rule gives an easy first filter: ask whether the quote names the base material specifically.</p>"
            + ul(["'Compacted base' isn't enough on its own; Rule 62-308.100 requires washed crushed rock or crushed concrete with the fines removed, and a crew that doesn't know the difference is likely to cut that corner.",
                  "Confirm the infill is on the state's approved list, natural sand, rock, shell or coated silica sand, rather than a generic 'infill' line item with no material named.",
                  "Ask directly whether the project sits within 10 ft of a pond, canal or other waterbody, or inside a tree's drip line, since both trigger specific requirements the quote should already address.",
                  "Get the irrigation plan in writing: which heads get capped, and where the lines get rerouted.",
                  "If the work happens near a fenced pool, ask how the crew protects the water and the equipment pad during base work."])
            + f"<p>{post('how-to-choose-an-artificial-turf-installer', 'Our full turf installer checklist')} goes further.</p>"),
        sec("Where we install artificial turf",
            f"<p>We install artificial turf lawns, pet areas, putting greens and paver accent strips across Greater Orlando and Sarasota–Manatee. Related towns: {cs('orlando', K)}, {cs('kissimmee', K)}, {cs('sarasota', K)} and {cs('lakewood-ranch', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("How long does artificial turf last in the Florida sun?",
                "Published lifespan claims vary widely by product line and manufacturer, and we don't have a verified, Florida-specific figure to put a number on. What drives how long a lawn holds up is UV exposure, foot and pet traffic, and whether infill gets topped off before it thins out. Ask any product you're considering for its manufacturer warranty terms, which is a more reliable lifespan figure than a sales page."),
            faq("Does artificial turf drain during heavy rain?",
                f"It should, if it's built to Florida's current standard. Rule 62-308.100 requires turf to be permeable and affixed to a permeable backing over a pervious subgrade, graded for positive drainage ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}). A lawn that holds standing water after a storm almost always traces back to a base built with fines-heavy fill instead of washed rock, not to the turf material itself."),
            faq("What goes under artificial turf in Florida?",
                "A subgrade of washed crushed rock or crushed concrete, never limerock or road base with fines, compacted in thin lifts and graded so water keeps moving through it. That's a state requirement, not just a build preference: fines bind together once compacted and wet, sealing the soil the way a sidewalk base is meant to seal it, which is the opposite of what turf needs underneath it."),
            faq("Is artificial turf safe for kids?",
                "The materials are regulated for that question specifically: Rule 62-308.100 bars heavy metals and intentionally added PFAS in the turf, backing and infill, and limits infill to natural sand, rock, shell or coated silica sand, with rubber crumb allowed only inside playground-equipment footprints. The one caveat worth knowing is heat; turf gets hotter underfoot in direct sun than grass does, so shade or a quick rinse matters more for comfort than for safety."),
            faq("Does artificial turf need infill?",
                "Most lawn and pet-area turf does. Infill weighs the backing down, holds the blades upright instead of matting flat, and helps the surface drain the way it's meant to. A putting green is the exception, built with little or no infill so the ball rolls true. Whatever product goes in has to meet Florida's material rule: clean silica sand, rock, shell or coated silica sand, with rubber limited to playground-equipment areas."),
            faq("How long does an artificial turf installation take?",
                "Most of the time on a standard yard goes into removal, grading and the compacted base, not into laying the turf itself. A typical quarter- to half-acre Florida lawn usually finishes in a few days once the site is ready, longer if the soil needs more prep or the layout has a lot of cutting around beds, trees or a pool deck. A narrow side yard with limited equipment access can take longer than its square footage suggests."),
            faq("Can artificial turf be installed over concrete or pavers?",
                "Yes, with a drainage layer or pad between the hard surface and the turf rather than laying it straight on top. That suits a balcony, an old concrete patio that isn't worth tearing out, or dressing up a section of pavers. The base rule for a full ground-level lawn, washed crushed rock over soil, doesn't apply the same way on top of an existing slab; drainage and attachment to that surface do the work instead.")]
    return page("/artificial-turf/", "service", "Artificial Turf Installation | Orlando & Sarasota, FL",
                "Artificial turf lawns, pet areas, putting greens and turf between pavers, built to Florida's Rule 62-308.100 (effective May 2026). Market range as of October 2026.",
                "Artificial Turf Lawns, Pet Areas and Putting Greens Built to Florida's New Turf Rule",
                capsule("Artificial turf in Florida covers more than a front lawn: we install pet areas, backyard putting greens and turf set between pavers, all built to DEP Rule 62-308.100, the state turf standard that took effect May 19, 2026. As of October 2026, installed turf runs $10 to $25 per sq ft in Florida market data, with a typical Orlando project averaging about $4,758. We build to that standard across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["hb683", "fs125-572", "flrules62-308-100", "rule62-308-100-text", "fs720-3045", "fs720-3035", "hb683-analysis",
                         "sjrwmd-watering", "swfwmd-restrictions", "manatee-phase3", "sarasota-city-phase3",
                         "homeguide-artificial-grass", "angi-turf-orlando", "angi-turf-tampa", "angi-turf-national", "homeguide-putting-green", "angi-putting-green"],
                related=[("/artificial-turf-cost/", "artificial turf cost guide"), ("/compare/artificial-turf-vs-sod/", "artificial turf vs. sod"),
                         ("/blog/florida-hoa-artificial-turf-law/", "can your HOA ban turf"), ("/blog/artificial-turf-heat-in-florida/", "how hot turf gets in Florida"),
                         ("/blog/how-to-clean-artificial-turf/", "cleaning and maintaining turf"), ("/blog/how-to-choose-an-artificial-turf-installer/", "choosing a turf installer"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=[], crumb="Artificial turf", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("artificial-turf"), eyebrow="Artificial Turf · Greater Orlando & Sarasota",
                howto=("How artificial turf is installed in Florida", [("Remove the old lawn or bed", "Sod, mulch and any irrigation heads inside the footprint come out down to bare soil."),
                                                                        ("Grade and compact the base", "Washed crushed rock or crushed concrete goes down in thin lifts, graded for positive drainage."),
                                                                        ("Cap or redirect irrigation", "Heads inside the turf zone are capped below grade or redirected to beds and sod that still need them."),
                                                                        ("Roll out and seam the turf", "Panels are trimmed to the footprint and joined at seams rather than overlapped."),
                                                                        ("Add infill and brush the pile", "Clean sand, rock or shell infill is worked into the pile with a power broom."),
                                                                        ("Anchor the perimeter", "Edges and seams are nailed or spiked at tighter spacing than the open field.")]))


def concrete_pillar():
    pids = for_service("concrete-driveways", 1)
    body = "".join([
        sec("Seven jobs, one trade",
            f"<p>Concrete work on this site splits into seven services, and most of what separates them is load and finish rather than the trade itself. {svc('concrete-driveways', 'Concrete driveways')} carry daily vehicle weight and are built to a thicker standard than anything else on this list. "
            f"{svc('concrete-patios', 'Concrete patios')} and {svc('concrete-walkways', 'walkways')} carry foot traffic and furniture, so they're poured lighter. {svc('concrete-pool-decks', 'Pool decks')} add a slope toward drains and an isolation joint at the coping that neither driveways nor patios need. "
            f"{svc('stamped-concrete', 'Stamped concrete')} isn't a separate build at all, it's a decorative finish that can go on a driveway, patio or pool deck without changing the thickness underneath. {svc('concrete-slabs', 'Concrete slabs')} cover the utility pours, pads for a shed, an AC unit, an RV or a garage addition, sized by what sits on them. "
            f"And {svc('concrete-repair', 'concrete repair')} is the odd one out: it starts from an existing slab rather than bare ground, fixing cracks, resurfacing worn surfaces or cutting out and replacing a section that's past saving.</p>"),
        sec("How do you choose among them?",
            "<p>Most homeowners already know roughly what they need; the table below maps the common starting points to the right service.</p>"
            + table("Picking the right concrete service", ["If you need...", "Start here", "Why"],
                    [["A new or replacement driveway", svc("concrete-driveways", "concrete driveways"), "Built for daily vehicle load; 4 in. standard, 5 to 6 in. for RVs and trailers"],
                     ["A back patio, lanai pad or outdoor-kitchen base", svc("concrete-patios", "concrete patios"), "Lighter foot-traffic spec; broom, trowel or stamped finish"],
                     ["The slab that rings a pool", svc("concrete-pool-decks", "concrete pool decks"), "Isolation joint at the coping, slope toward drains, cool-touch finish options"],
                     ["A decorative pattern on any of the above", svc("stamped-concrete", "stamped concrete"), "A finish option, not a separate base or thickness"],
                     ["A front walk, side path or sidewalk repair", svc("concrete-walkways", "sidewalks and walkways"), "A narrower, lighter-load spec, including right-of-way sections"],
                     ["A pad for a shed, AC unit, RV or garage floor", svc("concrete-slabs", "concrete slabs"), "Thickness and strength set by what sits on it"],
                     ["A cracked, sunken or failing existing slab", svc("concrete-repair", "concrete repair and resurfacing"), "Crack repair, an overlay or a cut-out-and-replace, not a new pour"]])),
        sec("The engineering every concrete surface in Florida shares",
            f"<p>Underneath the differences, every one of these seven services answers to the same handful of numbers. Florida's residential code sets 3½ in. as the bare floor for any slab on the ground, though almost nothing we build stays at that minimum ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}). "
            f"Strength requirements scale with weathering exposure rather than one fixed number; FBC Table R402.2 calls for 2,500 psi at the lightest class, climbing to 3,500 psi at the most severe, and most residential flatwork in our area lands at 3,000 to 4,000 psi regardless ({src('fbcr-2020-ch4', 'FBC Residential Table R402.2')}). Control joints follow NRMCA's rule of thumb across every service: roughly 24 to 36 times the slab's thickness, which on a standard 4-inch pour puts the saw cuts about 8 to 12 ft apart, each one scored to roughly a quarter of the slab's depth "
            f"({src('nrmca-cip6', 'NRMCA CIP 6')}). And every pour in a Central Florida or Suncoast summer runs into the same heat problem: concrete placed above 95°F, or at an evaporation rate past 0.2 lb per sq ft per hour, is prone to cracking before it ever carries a load, which is why an early start and a minimum three-day moist cure, by compound or wet curing, are standard on every service rather than an upcharge "
            f"({src('aci-faq-maxtemp', 'ACI')}; {src('nrmca-cip12', 'NRMCA CIP 12')}).</p>"
            + table("Shared concrete build facts", ["Element", "Standard"],
                    [["Code-floor thickness", "3½ in. for any ground-supported slab"],
                     ["Typical built thickness", "4 in. for driveways and patios; 5 to 6 in. under RVs, boats and heavy trailers"],
                     ["Strength", "2,500 psi minimum by weathering class; 3,000 to 4,000 psi typical residential flatwork"],
                     ["Control joints", "24 to 36 times slab thickness, roughly 8 to 12 ft on a 4-in. slab, cut a quarter of the depth"],
                     ["Curing in Florida heat", "At least 3 days moist cure; earlier starts and a curing compound once concrete nears 95°F"]],
                    "Build standards above the code floor; see FBC Residential Ch. 4 and 5, and NRMCA CIP 6 and 12 for the underlying rules.")
            + "<p>Two regional facts explain why those numbers matter here more than in a drier, cooler state. Much of both service areas sits on flatwoods soil, with a seasonal high water table that can sit within 18 in. of the surface for part of most years, which is reason enough to test and compact the subgrade on each job rather than quote one base depth for every lot. And the wet season, running roughly from late May into mid-October, puts an afternoon downpour on the forecast often enough that scheduling a pour or a base lift around it is routine, not an exception.</p>"),
        sec("Concrete services",
            "<p>Every service below shares the engineering above, scaled to its own load and finish.</p>" + _cards("concrete")),
        sec("What concrete work costs in Florida",
            f"<p>As of October 2026, Florida and national market data puts a plain concrete driveway at {price('concrete-driveway')} per sq ft installed, a concrete patio at {price('concrete-patio')}, and stamped concrete, which adds color, pattern and sealer labor on top of the same base pour, at {price('stamped-concrete')}. A pool deck resurfacing job runs lower than a new pour, since it reuses the existing base. These are market ranges compiled from published Florida and national cost-guide data, not a quote for your project; a written price follows a site visit. "
            f"Each service's own cost guide breaks the range down by size and scope: {a('/concrete-driveway-cost/', 'driveways')}, {a('/concrete-patio-cost/', 'patios')}, {a('/stamped-concrete-cost/', 'stamped concrete')}, {a('/pool-deck-cost/', 'pool decks')}, {a('/concrete-slab-cost/', 'slabs')}, {a('/concrete-walkway-cost/', 'walkways')} and {a('/concrete-repair-cost/', 'repair')}.</p>"),
        sec("Permits, HOAs and repair vs. replace",
            f"<p>Almost every concrete job that touches the right-of-way, the strip between the sidewalk and the street, needs a permit even where the rest of the driveway doesn't. HOAs add a second approval in master-planned communities, and since 2026 a Florida association can't require a government permit to already be issued before it will review an application "
            f"({src('fs720-3035', 'F.S. 720.3035')}). Florida's lien law adds its own paperwork above $2,500: a Notice of Commencement, signed by the owner and recorded with the county, has to be in place before the job gets underway ({src('fs713-13', 'F.S. 713.13')}). The {a('/permits/', 'permits and HOA hub')} has the full jurisdiction table, and {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for a new driveway or pool deck')} walks through the paperwork.</p>"
            f"<p>Not every cracked or sunken slab needs to come out, either. A hairline crack along a control joint is the joint doing its job; a section that's sunk or heaved usually points to the base, not the concrete mix. {compare('resurface-vs-replace-concrete', 'Resurface or replace a concrete driveway')} and {post('concrete-driveway-cracks-florida', 'which driveway cracks are normal in Florida')} cover how to tell the difference before calling anyone out.</p>"),
    ])
    faqs = [faq("What's the difference between a concrete patio and a concrete slab?",
                "A patio is finished and often decorative work meant to be lived on, broom, stamped or trowel-finished flatwork usually tied to the house by a door or a lanai. A slab is a utility pour in our pricing, a pad for a shed, an AC unit, a generator or a parking spot, sized by what sits on it rather than by foot traffic. The base and thickness principles are the same; the finish and the layout usually aren't."),
            faq("Is exposed aggregate its own service, or a finish option?",
                "It's a finish, not a separate service. Exposed aggregate is a plain or decorative pour with the top layer of paste washed or etched away to expose the stone underneath, available on a driveway, patio or walkway at the same thickness and joint spacing the base concrete work would use. It's priced as a finish upgrade on whichever service page covers the surface you're building."),
            faq("Can stamped concrete be added to a plain slab after it's already poured?",
                "Sometimes, as a stamped overlay rather than new stamped concrete. A bonded overlay goes over an existing slab that's still in good structural condition and can be stamped and colored, though the pattern reads shallower than one stamped into a fresh pour. A slab with wide cracks, settlement or a failing base isn't a good overlay candidate; our concrete repair and resurfacing page covers when cutting it out and starting over makes more sense."),
            faq("Does a concrete pool deck need a different build than a patio?",
                "The slab itself follows the same thickness and strength standard as a patio, but a pool deck adds two details a patio doesn't need: a slope graded toward drains and away from the house or the pool, and an isolation joint at the coping so the deck and the pool's shell can move independently. Skipping either one is the most common reason a pool deck cracks or holds water sooner than it should."),
            faq("Do all seven concrete services use the same control-joint spacing?",
                "The spacing rule is the same across all of them, roughly 24 to 36 times the slab's thickness, which works out to about 8 to 12 ft on a standard 4-inch pour. What changes is the layout: a driveway's joints usually run straight across a rectangle, a patio's are planned around furniture areas and door thresholds, and a stamped surface's joints are routed along a pattern line instead of cut as a visible groove.")]
    return page("/concrete/", "pillar", "Concrete Services | Orlando & Sarasota, FL",
                "Concrete driveways, patios, pool decks, stamped concrete, walkways, slabs and repair across Greater Orlando and Sarasota-Manatee, built to one Florida spec.",
                "Concrete Driveways, Patios, Pool Decks and More, Built to One Florida Spec",
                capsule("Opera pours seven kinds of concrete work: driveways, patios, pool decks, stamped concrete, walkways, slabs and repair. As of October 2026, Florida market data puts a plain concrete driveway at $6 to $15 per sq ft installed, with a stamped patio running higher. Every service shares the same 4-inch, 3,000 to 4,000 psi build standard, scaled by load, across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["fbcr-2020-ch5", "fbcr-2020-ch4", "nrmca-cip6", "nrmca-cip12", "aci-faq-maxtemp", "fs713-13", "fs720-3035"],
                related=[("/concrete-driveway-cost/", "concrete driveway cost guide"), ("/concrete-repair-cost/", "concrete repair cost guide"),
                         ("/compare/pavers-vs-concrete-driveway/", "pavers vs. concrete driveway"), ("/compare/resurface-vs-replace-concrete/", "resurface or replace"),
                         ("/blog/concrete-driveway-cracks-florida/", "which driveway cracks are normal"), ("/blog/concrete-curing-in-florida-heat/", "how concrete cures in Florida heat"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=[], crumb="Concrete",
                hero_photo=pids[0] if pids else None, eyebrow="Concrete · Greater Orlando & Sarasota")


def pavers_pillar():
    pids = for_service("paver-driveways", 1)
    body = "".join([
        sec("Five paver services, one base system",
            f"<p>Every paver job on this site is built the same way, from the ground up: a compacted aggregate base, a screeded layer of bedding sand, individual units set and compacted together, and edge restraint locking the field at every border. What changes between services is the load the base has to carry and the material on top. "
            f"{svc('paver-driveways', 'Paver driveways')} get the deepest base, since a car is the heaviest thing most residential paving ever carries. {svc('paver-patios', 'Paver patios and walkways')} carry foot traffic and furniture on a thinner base. {svc('pool-deck-pavers', 'Pool deck pavers')} add the coping detail and lean toward travertine or lighter-colored units. "
            f"{svc('paver-sealing', 'Paver sealing and restoration')} isn't a new install at all, it's cleaning, re-sanding, sealing and releveling units that have already been down for a while. And {svc('retaining-walls', 'retaining walls')} share the idea of a compacted base but carry soil pressure instead of foot or vehicle traffic, which changes the detail behind the wall more than the detail under it. "
            f"{svc('artificial-turf', 'Artificial turf')} fits into this family too, wherever it runs as an accent strip inside a paver field rather than across an open lawn.</p>"),
        sec("How do you choose among them?",
            "<p>The table below maps the common starting points to the service that covers them.</p>"
            + table("Picking the right paver service", ["If you need...", "Start here", "Why"],
                    [["A new or replacement driveway", svc("paver-driveways", "paver driveways"), "60 mm pavers standard, 80 mm for RVs, boats or work trucks, over a 6-in. base"],
                     ["A back patio, walkway or fire-pit area", svc("paver-patios", "paver patios and walkways"), "60 mm pavers over a 4-in. base; lighter foot-traffic load"],
                     ["The surface around a pool", svc("pool-deck-pavers", "pool deck pavers"), "Travertine or concrete pavers set to the coping; cooler underfoot than dark concrete"],
                     ["A sunken, stained or shifted paver surface", svc("paver-sealing", "paver sealing and restoration"), "Cleaning, re-sanding, sealing and releveling, not a new install"],
                     ["A retaining wall, raised planter or seat wall", svc("retaining-walls", "retaining walls"), "Segmental block with drainage behind the wall, not just under it"],
                     ["A turf accent inside a paver field", svc("artificial-turf", "artificial turf"), "Same washed-rock base as a full lawn, tied into the paver's edge restraint"]])),
        sec("Materials: concrete, travertine, clay brick and porcelain",
            "<p>The unit itself moves the price more than the base work underneath it does. Concrete pavers sit at the lower end of the Florida range; brick, porcelain and natural stone climb from there mostly on material cost.</p>"
            + table("Paver materials compared, installed cost per sq ft", ["Material", "Range", "Note"],
                    [["Concrete pavers", "$10 to $18", "Widest color and pattern selection; easiest to spot-repair one unit at a time"],
                     ["Clay brick", "$12 to $22", "A fixed, fired-in color that doesn't fade the way a pigmented concrete unit can"],
                     ["Porcelain", "$15 to $30", "A dense, low-absorption surface that needs a flat, well-compacted base"],
                     ["Travertine", "$13 to $45", "Natural stone; the material most homeowners pick for a pool deck for how it feels underfoot"]],
                    f"{src('angi-paver-driveway', 'Angi, paver driveways')}; {src('homeguide-travertine', 'HomeGuide, travertine')}.")
            + "<p>Travertine and porcelain need sealing more routinely than concrete pavers do, since they're more porous or show staining more easily; concrete pavers can go years without a sealer and still hold up structurally.</p>"),
        sec("The base system every paver surface shares",
            f"<p>ICPI's Tech Spec 2, the industry construction standard for interlocking concrete pavements, sets the base depth by use: residential driveways need at least 6 in. of compacted aggregate on soil that drains well, with 2 to 4 in. more where it doesn't; patios and walkways need roughly 4 in. on the same well-drained soil "
            f"({src('icpi-ts2', 'ICPI Tech Spec 2')}). Bedding sand screeds to an uncompacted 1 in. everywhere, laid last and never compacted before the pavers go down. Joint width stays at an eighth of an inch or less, filled with dry or polymeric sand once the field is set. "
            f"Edge restraint runs the full perimeter of every paver surface, and anywhere the material changes, since nothing else stops the field from creeping sideways under load; landscape edging sold for flower beds doesn't count ({src('icpi-ts3', 'ICPI Tech Spec 3')}).</p>"
            + table("Paver base spec by use", ["Layer", "Driveways", "Patios and walkways"],
                    [["Compacted aggregate base", "6 in. minimum, well-drained soil", "4 in. minimum, well-drained soil"],
                     ["Subgrade compaction", "98% standard Proctor", "98% standard Proctor"],
                     ["Paver thickness", "60 mm (80 mm for RVs, boats, trucks)", "60 mm"],
                     ["Bedding sand", "1 in. screeded, uncompacted before laying", "1 in. screeded, uncompacted before laying"]])),
        sec("Sealing: optional, and on no fixed schedule",
            f"<p>{src('icpi-ts5', 'ICPI Tech Spec 5')}, the industry's own guidance on paver care, doesn't set a required resealing interval; an acrylic coat typically holds up a few years before it's worth recoating, which varies by traffic, climate and product. "
            f"What isn't optional is topping off joint sand as it thins from rain and foot traffic, since a loose joint is what lets a field spread or shift. New pavers can also show a whitish efflorescence bloom within about 60 days; it's cosmetic and fades on its own, not something a sealer has to fix. "
            f"{svc('paver-sealing', 'Our paver sealing service')} covers cleaning, re-sanding, sealing and releveling, and {post('efflorescence-on-pavers-and-concrete', 'the post on efflorescence')} explains the white haze in more detail.</p>"),
        sec("Paver services",
            "<p>Every service below shares the base system above, built to the depth and load the surface needs.</p>" + _cards("pavers")),
        sec("What paver work costs in Florida",
            f"<p>As of October 2026, Florida market data puts an installed paver driveway at {price('paver-driveway')} per sq ft and a paver patio at {price('paver-patio')}, both well above plain concrete, since the per-unit material and the labor to set and compact each piece cost more than one continuous pour. These are market ranges compiled from published Florida and national cost-guide data, not a quote for a specific yard; a written price follows a site visit. "
            f"Full breakdowns by size and material: {a('/paver-driveway-cost/', 'driveways')}, {a('/paver-patio-cost/', 'patios')}, {a('/pool-deck-cost/', 'pool decks')}, {a('/paver-sealing-cost/', 'sealing')} and {a('/retaining-wall-cost/', 'retaining walls')}.</p>"),
    ])
    faqs = [faq("What's the difference between a paver patio and pool deck pavers?",
                "The units and base principles are the same; what changes is the edge. Pool deck pavers meet the coping with a continuous edge restraint and a layout planned around drains, skimmers and the pool's isolation joint, while a patio's restraint only has to hold the field together at the perimeter. Material choice leans toward travertine or a lighter concrete paver around a pool more often than on a patio, mainly for how it feels underfoot in full sun."),
            faq("Which paver material costs the least installed?",
                "Concrete pavers, typically $10 to $18 per sq ft installed in current Florida market data, run below clay brick, porcelain and travertine. The gap is almost entirely in material cost, not labor; the base, bedding sand and edge restraint are priced about the same no matter which unit goes on top. Concrete pavers also carry the widest color and pattern selection, part of why they're the most common driveway material in both service areas."),
            faq("Can artificial turf be set as a strip or border between pavers?",
                "Yes. A turf accent inside a driveway, along a walkway edge or framing a fire pit uses the same washed-rock subgrade Florida's turf rule requires everywhere else, but it ties into the paver field's existing edge restraint instead of standing on its own perimeter. That's a different detail than laying turf over the top of an existing paver surface, which uses a drainage layer rather than an excavated base."),
            faq("Does a retaining wall need the same base as a paver patio?",
                "No. A retaining wall carries soil pressure behind it, so its base is a compacted leveling pad of crushed stone under the first course, plus drainage, gravel backfill and a perforated pipe behind the wall to relieve water pressure. A paver patio's base carries foot traffic on top, not soil pressure from behind, so the two share the idea of a compacted aggregate base but not the same depth or drainage detail."),
            faq("Is a paver pool deck more work to maintain than a paver patio?",
                "Not structurally, but it sees more exposure. Pool chemicals, sunscreen residue and more frequent water contact mean a pool deck's joints and sealer, where sealed, wear faster near the coping than a patio's do across the rest of the yard. The base, bedding sand and edge restraint underneath don't need anything different; it's the surface care, rinsing and resealing on whatever schedule the product needs, that runs on a shorter clock near the water.")]
    return page("/pavers/", "pillar", "Paver Services | Orlando & Sarasota, FL",
                "Paver driveways, patios, pool decks, sealing and retaining walls in concrete, travertine, clay brick or porcelain, on a compacted base. Florida ranges, Oct. 2026.",
                "Paver Driveways, Patios, Pool Decks and Walls Built on One Compacted Base",
                capsule("Opera lays paver driveways, patios and walkways, pool deck pavers, retaining walls and paver sealing, plus artificial turf set between paver fields. As of October 2026, Florida market data puts installed pavers at $10 to $30 per sq ft depending on material; every paver surface starts with a compacted aggregate base, never bare sand, across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts3", "icpi-ts5", "angi-paver-driveway", "homeguide-travertine", "homeguide-driveway-pavers", "homeguide-paver-patio"],
                related=[("/paver-driveway-cost/", "paver driveway cost guide"), ("/paver-sealing-cost/", "paver sealing cost guide"),
                         ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers"), ("/compare/clay-brick-vs-concrete-pavers/", "clay brick vs. concrete pavers"),
                         ("/blog/why-pavers-sink-in-florida/", "why pavers sink, and the fix"), ("/blog/paver-installation-process-florida/", "how pavers are installed in Florida"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=[], crumb="Pavers",
                hero_photo=pids[0] if pids else None, eyebrow="Pavers · Greater Orlando & Sarasota")


def get_pages():
    return [turf(), concrete_pillar(), pavers_pillar()]
