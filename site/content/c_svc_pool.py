# -*- coding: utf-8 -*-
"""Service pages: concrete pool decks and pool deck pavers."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, cs, post, compare, src, ext, price, per, price_note, tel, contact, photo, offer
from _photos import for_service
from _data import SERVICES, PRICE_DATE


def concrete_pool_decks():
    K = "concrete-pool-decks"
    pids = for_service(K, 3)
    hero = pids[0] if pids else None

    intro = sec("What a Concrete Pool Deck Covers",
        f"<p>A concrete pool deck is the slab that rings the water between the coping and the screen enclosure or the open yard beyond it, built to carry foot traffic, lounge furniture and the occasional grill rather than a vehicle. In Florida that one phrase covers three different jobs: pouring a new deck where there isn't one or the old slab is beyond saving, resurfacing an existing deck with a spray-applied acrylic coating such as Kool Deck, and stamping a pattern into either a new pour or an overlay. Installed cost runs {price('concrete-pool-deck')} per square foot as of {PRICE_DATE}, with resurfacing running well under that and a full new pour at the upper end ({src('homeguide-pool-deck', 'HomeGuide')}; {src('poolmechanic-pooldeck-cfl', 'Central Florida resurfacing data')}).</p>"
        + (photo(hero, "A broom-finished concrete deck with a tile accent band bordering a pool and spa.") if hero else ""))

    choosing = sec("New Pour, Resurfacing or Pavers: How to Pick",
        f"<p>The deciding question is whether the concrete underneath is still structurally sound. If the slab is solid but faded, chalky or showing only hairline cracking, a coating or stamped overlay buys back the look for a fraction of what a new pour costs. If the slab is cracked through, sunken, or hollow-sounding when you tap it, resurfacing just hides a problem that keeps moving underneath. Pavers are the third path, laid over a demolished site or directly on top of a sound old slab; that option, including travertine and shell stone, is its own page: {svc('pool-deck-pavers')}.</p>"
        + table("Pool deck options, installed cost per sq ft",
                ["Option", "What happens to the old surface", "Typical cost", "Best fit"],
                [["Acrylic or Kool Deck-style coating", "Sprayed over the existing cured slab", "$3–$6", "Sound slab, cosmetic refresh"],
                 ["Spray deck or micro-topping overlay", "Thicker decorative layer over the slab", "$4–$8", "Sound slab with minor surface flaws"],
                 ["New poured concrete deck", "Old deck removed, new slab poured", price('concrete-pool-deck'), "Cracked, sunken or undersized deck"],
                 ["Stamped concrete deck or overlay", "New pour or overlay with a pattern", "$7–$20", "New pours or sound slabs wanting a pattern"]],
                f"Central Florida contractor pricing for an 800–1,200 sq ft deck; see {src('poolmechanic-pooldeck-cfl', 'Pool Mechanic, Central Florida, July 2026')} and {price_note()}"))

    spec = sec("What We Build To",
        f"<p>Florida's residential code sets 3½ inches as the minimum thickness for a slab on the ground (FBC Residential R506.1); we typically build a pool deck to 4 inches, the same standard most residential flatwork uses, since a pool deck never carries the point loads a driveway does ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}).</p>"
        + table("Concrete pool deck spec",
                ["Element", "What we build", "Why"],
                [["Thickness", "4 in (code minimum 3½ in)", "Pedestrian and furniture loads only"],
                 ["Base", "Compacted fill under the slab, graded away from the pool", "Uniform support; prevents low spots"],
                 ["Control joints", "24–36× slab thickness, about 8–12 ft apart, never past 15 ft", f"{src('nrmca-cip6', 'NRMCA CIP 6')} on crack control"],
                 ["Isolation joint", "Compressible filler and flexible sealant at the coping, full perimeter", "The deck and the pool's bond beam move at different rates"],
                 ["Slope", "Positive fall from the house side to deck drains, not toward the water", "Keeps runoff and debris out of the pool"],
                 ["Finish", "Broom, acrylic spray coating or stamped pattern", "Texture for grip; see below for heat and slip"]],
                "The slab itself is a structural detail; the isolation joint and slope are the two most common places a pool deck fails early."))

    build_steps = sec("How a Concrete Pool Deck Is Built, Step by Step",
        "<p>A new pour and a full resurfacing job share most of the same sequence, minus demolition and forming on a resurfacing job.</p>"
        + steps([
            ("Protect the pool and the equipment pad.", "The water gets covered and the filter, pump and heater are shielded from dust, debris and foot traffic before anything is cut or demolished."),
            ("Demolish or saw-cut the old surface.", "On a replacement, the old slab is broken out working away from the coping; on an overlay, only loose or failed sections come out."),
            ("Set the isolation strip against the bond beam.", "A compressible material goes against the pool shell before the base is compacted, so the new work never bears directly on the pool structure."),
            ("Grade and compact the base.", "The subgrade is shaped with a two-direction slope, toward deck drains and away from the house, then compacted in lifts."),
            ("Form, reinforce and pour.", "Forms set the finished elevation against the coping and any door threshold; wire mesh goes in to hold cracks together, not to stop them from forming."),
            ("Finish and texture the surface.", "A broom finish, a stamped pattern or a base ready for a later acrylic coating gets worked in while the concrete is still plastic."),
            ("Cure for at least 3 days.", "The slab is kept moist and off-limits to foot traffic through the minimum curing window before any coating or sealer goes on."),
            ("Caulk the isolation joint and walk every drain.", "The flexible sealant goes in last, and the finished deck gets tested with a hose to confirm water actually reaches the drains.")]))

    florida = sec("Florida Conditions This Build Plans For",
        "<h3>Heat, Humidity and an Open, Shadeless Pour</h3>"
        f"<p>A pool deck usually pours in full sun with no roof overhead until a screen cage goes up later, during a rainy season that runs roughly late May through mid-October on both coasts ({src('nws-mlb-wetdry', 'NWS Melbourne')}). ACI 305.1 and ACI 301 limit concrete temperature to 95°F at discharge, and the industry threshold for plastic shrinkage cracking is an evaporation rate above 0.2 lb per square foot per hour ({src('aci-faq-maxtemp', 'ACI FAQ')}; {src('aci-ci-evap-2007', 'ACI Concrete International, 2007')}). We schedule hot pours early, dampen the subgrade, and keep a curing compound ready rather than letting the surface dry before the slab underneath has gained strength.</p>"
        "<h3>Flatwoods Water Table and the Backfill Around the Shell</h3>"
        f"<p>Much of Greater Orlando sits on flatwoods soils such as Myakka and Smyrna, where the seasonal high water table can sit within 18 inches of the surface for part of the year ({src('nrcs-myakka-osd', 'NRCS Myakka series')}; {src('nrcs-smyrna-osd', 'NRCS Smyrna series')}). The Suncoast has its own version in series like EauGallie, which behaves the same way ({src('nrcs-eaugallie-osd', 'NRCS EauGallie series')}). The ring of backfill immediately around a pool shell is usually excavation spoil placed back by hand, not native soil, so we test and compact that ring on its own rather than assuming it matches the rest of the yard.</p>"
        "<h3>Screen Cage Footers Landing on the Deck</h3>"
        "<p>Almost every pool deck in this market eventually gets a screen enclosure, and its aluminum posts sit on isolated concrete footers poured separately from the deck slab, with their own small isolation gap. Skipping that detail lets ordinary settling of either one crack the deck outward from each post location, a pattern that shows up as cracks radiating from a line of fixed points rather than at random.</p>"
        "<h3>Settling Near the Coping Is Not a Sinkhole</h3>"
        f"<p>A dish-shaped low spot away from the coping is almost always ordinary base settling, not a sign of trouble underneath the pool itself. Statewide sinkhole claims concentrate heavily in Hernando, Pasco and Hillsborough counties; Orange County sits on the broader list of counties with similar geology, while Sarasota and Manatee do not ({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}).</p>"
        "<h3>Saltwater Pools and Exposed Steel</h3>"
        f"<p>A saltwater pool runs far below ocean salinity, but splash-out still leaves salt behind on the coping and the nearest few feet of deck as the water evaporates, and airborne salt does the same along the Sarasota–Manatee coast. FDOT treats structures within 2,500 feet of water carrying meaningful chloride as a more corrosive environment for exposed steel, a bridge-engineering standard we use as context, not a code requirement, for keeping any exposed wire mesh or rebar covered with enough concrete at the coping ({src('fdot-sdg', 'FDOT Structures Design Guidelines')}).</p>")

    cost = sec("What a Concrete Pool Deck Costs",
        f"<p>Installed concrete pool decks run {price('concrete-pool-deck')} per square foot in Florida as of {PRICE_DATE}, with resurfacing and coatings at the low end and a full new pour or stamped finish at the top ({src('homeguide-pool-deck-resurfacing', 'HomeGuide')}). Removing an old deck before a replacement typically adds a few dollars a square foot on top of that. The {a('/pool-deck-cost/', 'pool deck cost guide')} works through an 800 and a 1,200 square foot deck for every option on this page.</p>")

    permits = sec("Permits and HOA Rules for Pool Deck Work",
        f"<p>In the City of Orlando, a pool-deck slab goes through the same engineering permit as a driveway or pavers; artificial turf near a pool also needs one because it counts as impervious surface ({src('orlando-res-requirements', 'City of Orlando Residential Permitting Requirements')}). In unincorporated Manatee County, a pool deck on grade can sit as close as 5 feet to a side or rear lot line, a setback written specifically for pools, screen cages and the decks around them ({src('manatee-ldc-511.16-pool-decks', 'Manatee County LDC §511.16')}). Rules vary by city and county; the {a('/permits/', 'permits and HOA hub')} and the {post('orange-county-orlando-driveway-patio-permits', 'Orlando and Orange County guide')}, {post('manatee-county-driveway-permits', 'Bradenton and Lakewood Ranch guide')} and {post('sarasota-county-driveway-patio-permits', 'Sarasota and Venice guide')} cover each jurisdiction.</p>"
        f"<p>Master-planned communities add a layer most cities don't. At Lakewood Ranch's Country Club/Edgewater community, resurfacing an existing driveway with a concrete overlay technique requires a Modification Request Form submitted and approved first, and the manual specifies it has to be applied by a professional ({src('lwr-ceva-manual', 'Lakewood Ranch CEVA Homeowners Manual')}); pool-deck resurfacing commonly goes through that same architectural review. In Lake Nona's Laureate Park, the HOA's own language is broader still: any improvement to the property, including the pool, needs Architectural Review Board sign-off before work starts ({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}). A 2026 change to Florida law means an HOA can no longer demand a building permit before it will even review the request ({src('fs720-3035', 'F.S. 720.3035')}). More in {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for a pool deck or driveway')}.</p>")

    care = sec("Caring for a Concrete Pool Deck",
        "<p>Rinse the coping and the few feet of deck closest to the water a few times a month; chlorine and salt residue builds into a dull film if it never gets hosed off between pool-service visits. Walk the isolation joint once or twice a year and look for the sealant cracking, pulling away, or gapping anywhere along the coping; it's the part of the deck that wears out first, well before the surrounding concrete does, and a simple recaulk fixes it early. "
        f"There's no fixed number of years published for recoating an acrylic or Kool Deck-style finish; watch for chalking, a texture gone smooth, or water that no longer beads instead of counting calendar years ({src('mortex-kooldeck-brochure', 'Mortex Kool Deck brochure')}). Keep deck drains clear ahead of the rainy season, and treat a crack that follows the coping line, rather than running across an open panel, as worth a professional look. More on surface care in {post('slippery-pool-deck-fixes', 'making a slippery pool deck safer')} and {post('mold-and-algae-on-pavers-florida', 'stopping mold and algae on concrete and pavers')}.</p>")

    choose = sec("How Do You Pick the Best Pool Deck Contractor in Florida?",
        f"<p>Start with how they describe the isolation joint at the coping; a contractor who can't explain it without being asked probably isn't planning to build one. Ask who pulls the engineering or zoning permit the job needs, since that answer tells you whether it's priced into the bid. For anything over $2,500, a recorded Notice of Commencement protects you under Florida's lien law, and a legitimate contractor expects to handle it ({src('fs713-13', 'F.S. 713.13')}). Florida's pool-contractor license category covers the shell and its equipment; the statute's text doesn't single out the surrounding deck, so a concrete or masonry background matters more here than a pool license by itself ({src('fs489-105', 'F.S. 489.105')}). Before you commit to a quote, check {src('dbpr-search', 'the DBPR license search')} for anyone claiming a state certification, and ask for proof of the liability insurance Florida requires contractors to carry ({src('fs489-115', 'F.S. 489.115')}). {post('how-to-choose-a-concrete-contractor-orlando', 'More criteria for Orlando')} and {post('how-to-choose-a-concrete-contractor-sarasota', 'for Sarasota and Bradenton')}.</p>")

    links = sec("Related Reading",
        ul([compare('cool-deck-vs-pavers-vs-travertine', 'Cool deck vs. pavers vs. travertine: resurface or replace?'),
            compare('pavers-vs-concrete-pool-deck', 'Pavers vs. concrete for a Florida pool deck'),
            post('how-hot-do-pool-decks-get-florida', 'How hot do pool decks get in Florida?'),
            post('saltwater-pools-and-coastal-salt-air-hardscape', 'Saltwater pools and salt air on the coast'),
            post('pool-deck-ideas-florida', 'Pool deck ideas for Florida homes')]))

    areas = sec("Concrete Pool Deck Service Areas",
        "<p>We build and resurface concrete pool decks across Greater Orlando and the Sarasota–Manatee area, including:</p>"
        + ul([cs("orlando", K), cs("sarasota", K), cs("lakewood-ranch", K), cs("winter-garden", K)]))

    body = "".join([intro, choosing, spec, build_steps, florida, cost, permits, care, choose, areas, links,
                     "<!--AUTO:service-cities-->"])

    faqs = [
        faq("What is Kool Deck, and can it be resurfaced?",
            f"Kool Deck is a brand name for a spray-applied acrylic cement coating troweled over an existing concrete pool deck for texture and color; 'cool deck' and 'spray deck' describe the same category from other makers ({src('mortex-kooldeck-brochure', 'Mortex')}). Yes, it can be resurfaced again once it's worn, chalky or chipped, usually by cleaning, patching low spots and spraying a new coat over the cured base slab."),
        faq("How long does pool deck resurfacing last in Florida?",
            "No single published figure covers Florida specifically. Cost guides describe acrylic and Kool Deck-style coatings as meant to be recoated on a cycle measured in a handful of years, while a new poured slab or a full stamped overlay goes much longer before it needs that kind of surface work again. Watch for chalking, hairline cracking in the coating, or a slick texture rather than counting years."),
        faq("Can a cracked pool deck be resurfaced, or does it need replacing?",
            f"A hairline crack away from the coping is usually fine to fill and coat. A crack that tracks the coping line, keeps widening, or sits over a hollow-sounding spot points to a base or isolation-joint problem that resurfacing won't solve, which calls for cutting out and rebuilding that section. {compare('resurface-vs-replace-concrete', 'Resurface vs. replace')} covers the same decision on a driveway."),
        faq("Do I need to drain the pool for pool deck work?",
            "Usually no. Resurfacing or replacing the deck around a pool that's staying full is done from the deck side, with the water covered and the equipment pad protected, and the pool can often keep circulating through most of the job. Draining only becomes necessary if the work reaches the coping or bond beam itself."),
        faq("How soon can we use the pool deck after resurfacing?",
            f"Plan on at least the 3-day minimum curing window hot-weather guidance calls for before regular foot traffic, longer after a wet or cool stretch ({src('nrmca-cip12', 'NRMCA CIP 12')}). A stamped or decorative overlay needs a similar cure before sealing, and sealing itself needs a dry forecast to set up right."),
        faq("Can you replace the pool coping at the same time?",
            f"Yes. Coping work is a common add-on to a deck resurfacing or replacement job, since the isolation joint between the two gets rebuilt either way. {svc('pool-deck-pavers')} details paver and travertine coping; a poured concrete deck usually gets a cantilevered or precast bullnose concrete edge instead."),
    ]

    return page("/concrete-pool-decks/", "service",
                "Concrete Pool Decks in Florida: Resurfacing & Kool Deck",
                "Concrete pool decks and Kool Deck-style resurfacing in Florida run $5–$15 per sq ft installed as of October 2026, with specs, process and FAQs.",
                "Pouring and Resurfacing a Concrete Pool Deck in Florida",
                capsule(f"A concrete pool deck in Greater Orlando or Sarasota–Manatee runs about {price('concrete-pool-deck')} per square foot installed as of {PRICE_DATE}, covering a new broom-finished slab, a Kool Deck-style acrylic coating sprayed over an existing deck, or a stamped overlay. Which one fits depends on whether the slab underneath is still structurally sound."),
                body, faqs=faqs,
                sources=["homeguide-pool-deck", "homeguide-pool-deck-resurfacing", "poolmechanic-pooldeck-cfl", "fbcr-2020-ch5", "nrmca-cip6", "nrmca-cip12",
                         "aci-faq-maxtemp", "aci-ci-evap-2007", "mortex-kooldeck-brochure", "nws-mlb-wetdry", "nrcs-myakka-osd", "nrcs-smyrna-osd", "nrcs-eaugallie-osd",
                         "fl-senate-2011-104", "fdot-sdg", "orlando-res-requirements", "manatee-ldc-511.16-pool-decks", "lwr-ceva-manual", "laureatepark-faq",
                         "fs720-3035", "fs489-105", "fs489-115", "fs713-13", "dbpr-search"],
                related=[("/pool-deck-cost/", "pool deck cost guide"), ("/compare/cool-deck-vs-pavers-vs-travertine/", "cool deck vs. pavers vs. travertine"),
                         ("/blog/pool-deck-ideas-florida/", "pool deck ideas"), (SERVICES["stamped-concrete"]["route"], "stamped concrete"),
                         (SERVICES["concrete-patios"]["route"], "concrete patios"), (SERVICES["pool-deck-pavers"]["route"], "pool deck pavers"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Concrete", "/concrete/")], crumb="Concrete pool decks", service=K,
                hero_photo=hero, offer=offer(SERVICES[K]["price"]), eyebrow="Concrete · Greater Orlando & Sarasota–Manatee",
                howto=("How a Concrete Pool Deck Is Built", [
                    ("Protect the pool and the equipment pad.", "Cover the water and shield the filter, pump and heater from dust and debris before any demolition starts."),
                    ("Demolish or saw-cut the old surface.", "Break out the old slab working away from the coping, or remove only failed sections on an overlay."),
                    ("Set the isolation strip against the bond beam.", "Place a compressible material against the pool shell before the base is compacted."),
                    ("Grade and compact the base.", "Shape a two-direction slope toward deck drains and away from the house, then compact in lifts."),
                    ("Form, reinforce and pour.", "Set forms to the finished elevation and place wire mesh before the concrete goes in."),
                    ("Finish and texture the surface.", "Work in a broom finish, a stamped pattern, or a base ready for a later acrylic coating."),
                    ("Cure for at least 3 days.", "Keep the slab moist and off-limits to foot traffic through the minimum curing window."),
                    ("Caulk the isolation joint and test every drain.", "Finish the flexible sealant and run water across the deck to confirm drainage."),
                ]))


def pool_deck_pavers():
    K = "pool-deck-pavers"
    pids = for_service(K, 3)
    hero = pids[0] if pids else None
    second = pids[1] if len(pids) > 1 else None

    intro = sec("What Pool Deck Pavers Cover",
        f"<p>Pool deck pavers are individual units, travertine, shell stone or concrete, set in a sand bed over a compacted aggregate base around the water, instead of one continuous poured slab. Installed cost runs {price('pool-deck-pavers')} per square foot as of {PRICE_DATE}, depending on material, with travertine and shell stone at the top of that range and concrete pavers at the bottom ({src('homeguide-travertine', 'HomeGuide')}; {src('poolmechanic-pooldeck-cfl', 'Central Florida resurfacing data')}). The same materials work both on a new build and set over an old concrete deck that's still structurally sound.</p>"
        + (photo(hero, "Pavers surround a pool deck furnished with wicker seating and a linear fire pit.") if hero else ""))

    material = sec("Choosing a Material: Travertine, Shell Stone or Concrete",
        "<p>Travertine stays noticeably cooler underfoot in direct sun than a dark concrete paver, which is a large part of why it's the material most often chosen right around a Florida pool; we won't attach a specific temperature figure to that difference, since no verified measurement for Florida conditions exists. Shell stone, quarried coquina with visible shell fragments running through it, offers a similarly light, naturally textured surface in a different look. Both are porous enough that sealing matters more than it does on concrete. Concrete pavers cost the least, come in the widest range of colors, and are the cheapest to pull and replace individually if one cracks.</p>"
        + table("Pool deck paver materials compared",
                ["Material", "Feel underfoot in sun", "Sealing", "Installed cost"],
                [["Travertine", "Noticeably cooler than dark concrete", "Needed; porous stone", f"{src('homeguide-travertine', '$13')}–$30 per sq ft for pool deck installs"],
                 ["Shell stone (coquina)", "Light, naturally textured surface", "Needed; porous stone", f"$16–$35 per sq ft, natural stone ({src('homeguide-pool-deck', 'HomeGuide')})"],
                 ["Concrete pavers", "Warmer than natural stone in full sun", "Optional; lower porosity", f"$8–$15 per sq ft ({src('poolmechanic-pooldeck-cfl', 'Central Florida data')})"]],
                "A 1,000 sq ft travertine pool deck runs roughly $22,000–$28,000 installed in published Florida contractor pricing."))

    base = sec("Base and Spec for a Paver Pool Deck",
        f"<p>A paver pool deck carries a light pedestrian load, the same as a patio, so it follows the lighter ICPI spec rather than the heavier one written for driveways. Units for a pedestrian or lightly used area run 2⅜ inches thick; the base underneath goes at least 4 inches on well-drained soil, with 2 to 4 inches more on wet or poorly drained ground, compacted to 98% of standard Proctor density ({src('icpi-ts2', 'ICPI Tech Spec 2')}). Bedding sand screeds to an uncompacted 1 inch, and a continuous edge restraint runs the full perimeter, including the inside edge where the field meets the coping ({src('icpi-ts3', 'ICPI Tech Spec 3')}).</p>"
        + table("Pool deck paver spec",
                ["Element", "Spec", "Why"],
                [["Paver thickness", "2⅜ in (60 mm), pedestrian grade", "No vehicle loads around a pool"],
                 ["Base depth", "4 in minimum on well-drained soil, +2–4 in wet soil", "Flatwoods soils near a pool often run wet"],
                 ["Compaction", "98% standard Proctor, 4–6 in lifts", "Prevents settling under furniture and traffic"],
                 ["Bedding sand", "1 in uncompacted, screeded level", "Sets the paver bearing surface"],
                 ["Edge restraint", "Continuous perimeter, including against the coping", "Stops the field from creeping toward the water"],
                 ["Coping joint", "Flexible sealant over backer rod, not sand", "Coping and field move independently"]],
                f"{src('icpi-ts2', 'ICPI Tech Spec 2')} and {src('icpi-ts3', 'ICPI Tech Spec 3')}, 2020."))

    coping = sec("Coping: What Finishes the Pool's Edge",
        "<p>Field pavers are sand-set on a flexible base; coping along the water's edge is almost always mortar-set onto the pool's bond beam, a different structural system entirely. We set the coping course first, working the field pattern back from that fixed line, and detail the joint between the two with a flexible sealant rather than sand, since sand-set pavers and mortar-set coping move at different rates. Precast bullnose coping, with a rounded, overhanging front edge, is the standard profile because a square-edged unit left proud of the bond beam is uncomfortable against bare skin.</p>")

    overlay = sec("Pavers Over an Existing Concrete Deck",
        f"<p>Setting pavers over a sound old concrete deck skips excavation but not prep: the slab gets sounded for hollow or soft spots, patched where needed, and cleaned before a thin bedding system, sand-set on a membrane or mortar-set, carries the new pavers. That added height has to be checked against every door threshold, the pool equipment housing and the coping before work starts, since the paver plus bedding layer adds real thickness the original slab didn't have. General overlay feasibility is covered in {post('pavers-over-existing-concrete', 'can you put pavers over existing concrete')}; pool decks have the added wrinkle of the coping line.</p>")

    build_steps = sec("How Pool Deck Pavers Are Installed, Step by Step",
        "<p>A ground-up install and an overlay over an existing slab share most of this sequence, minus excavation on an overlay.</p>"
        + steps([
            ("Protect the pool and sound the old slab, if there is one.", "The water gets covered, and on an overlay job, the existing deck is checked for hollow or failed sections before anything is set."),
            ("Excavate or clean and prep the surface.", "A new install is excavated to the base depth and graded; an overlay gets pressure-washed and patched instead."),
            ("Set and cure the coping.", "Mortar-set coping along the bond beam goes in early and cures on its own schedule before field work starts against it."),
            ("Compact the base in lifts.", "Aggregate base is placed and compacted to 98% Proctor, with the two-direction slope toward deck drains built in."),
            ("Screed the bedding sand.", "A 1-inch layer of bedding sand is screeded level across the compacted base, or over the bedding system on an overlay."),
            ("Lay the field pattern from the coping outward.", "Full pavers go in first against the fixed coping line, with cut pieces pushed to the outer perimeter."),
            ("Set edge restraint and compact.", "Restraint goes in at every open edge, including against the coping, before the whole field is compacted."),
            ("Sweep joint sand, seal, and test every drain.", "Joint sand is swept and compacted, the deck is sealed where specified, and water is run across the surface to confirm it reaches the drains."),
        ]))

    florida = sec("Florida Conditions a Paver Pool Deck Has to Handle",
        "<h3>Wet Flatwoods Soil Right Where the Deck Sits</h3>"
        f"<p>Flatwoods soils common on the Suncoast, series like EauGallie and Immokalee, hold a seasonal high water table within about 18 inches of the surface for part of the year, and splash-out and equipment-pad runoff add to that moisture right where a pool deck's base sits ({src('nrcs-eaugallie-osd', 'NRCS EauGallie series')}; {src('nrcs-immokalee-osd', 'NRCS Immokalee series')}). Greater Orlando has its own flatwoods soils in Myakka and Smyrna with the same behavior ({src('nrcs-myakka-osd', 'NRCS Myakka series')}). We default to the thicker, wet-soil base near the coping on both sides of the territory rather than waiting to find a soft spot.</p>"
        "<h3>Saltwater Pools and Salt Residue on Stone</h3>"
        "<p>A saltwater pool runs well below seawater concentration, but splash-out still leaves that salt on the coping and the nearest paver courses as the water evaporates, cycle after cycle, and it reads as a dull white residue that recurs on a schedule tied to pool use rather than fading out like ordinary efflorescence does. Sealed travertine and shell stone resist that staining far better than the same stone left bare.</p>"
        "<h3>Scheduling Around the Rainy Season</h3>"
        f"<p>Joint sand compaction and sealing both need a dry window, which matters on a job scheduled during the rainy season that typically runs from late May into October across both coasts ({src('nws-mlb-wetdry', 'NWS Melbourne')}). We push base compaction to the morning and save joint sand and sealing for the driest stretch in the forecast, since a downpour on fresh, uncompacted joint sand washes it toward the pool before it locks in.</p>"
        "<h3>Settling at the Coping Versus a Structural Problem</h3>"
        f"<p>A low spot or an opening joint right along the coping is almost always ordinary base settling, not movement in the pool shell itself. Orange County sits on the state's broader list of counties with higher documented sinkhole claims; Sarasota and Manatee do not ({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). Coastal salt exposure near the water, by FDOT's bridge-engineering standard for structures within 2,500 feet of salt water, is a separate, more common reason to check for corrosion at any exposed metal edge restraint, not a structural pool issue ({src('fdot-sdg', 'FDOT Structures Design Guidelines')}).</p>")

    cost = sec("What Pool Deck Pavers Cost",
        f"<p>Installed pool deck pavers run {price('pool-deck-pavers')} per square foot in Florida as of {PRICE_DATE}, with concrete pavers at the bottom of that range and travertine and shell stone toward the top. The {a('/pool-deck-cost/', 'pool deck cost guide')} breaks that down by size and material, including how an overlay over an existing slab compares to a ground-up install.</p>"
        + (photo(second, "A close-up of interlocking concrete pavers set in a tight zigzag pattern.") if second else ""))

    permits = sec("Permits and HOA Rules",
        f"<p>In unincorporated Manatee County, a pool deck on grade can sit as close as 5 feet to a side or rear lot line, a setback written specifically for pools and the decks around them ({src('manatee-ldc-511.16-pool-decks', 'Manatee County LDC §511.16')}). In Orlando, pavers around a pool go through the same engineering permit as concrete or asphalt ({src('orlando-res-requirements', 'City of Orlando Residential Permitting Requirements')}). The {a('/permits/', 'permits and HOA hub')}, {post('manatee-county-driveway-permits', 'Bradenton and Lakewood Ranch guide')} and {post('sarasota-county-driveway-patio-permits', 'Sarasota and Venice guide')} cover the rest.</p>"
        f"<p>Lakewood Ranch's Country Club/Edgewater community manual requires a Modification Request Form before the material of a residential driveway or walkway changes, approved before work starts ({src('lwr-ceva-manual', 'Lakewood Ranch CEVA Homeowners Manual')}); pool-area hardscape typically goes through that same architectural review. In Lake Nona's Laureate Park, any improvement to the property, including the pool, needs sign-off from the Architectural Review Board ({src('laureatepark-faq', 'Laureate Park Master Association FAQ')}). A 2026 change to Florida law bars an HOA from requiring a building permit before it will review the request ({src('fs720-3035', 'F.S. 720.3035')}). {post('lakewood-ranch-arc-approval-hardscape', 'Lakewood Ranch ARC approval for pavers and pool decks')} goes deeper.</p>")

    care = sec("Caring for Pool Deck Pavers",
        "<p>Rinse the coping and the paver courses closest to the water more often than the rest of the deck; salt, chlorine residue and sunscreen oils concentrate there and build into staining faster than ordinary rain and dust ever would elsewhere on the field. Joint sand in that same zone wears out faster too, from splash-out and hose-downs on top of normal weathering, so it's worth topping off on a shorter cycle than the rest of the deck. "
        f"Travertine and shell stone don't have a published resealing interval; watch for water that no longer beads, or a color gone flat in the splash zone specifically, rather than counting years ({src('icpi-ts5', 'ICPI Tech Spec 5')}). {post('travertine-pool-deck-care', 'Travertine pool deck care')} and {post('how-to-clean-pavers-without-damage', 'cleaning pavers without damaging the joints')} cover the routine.</p>")

    choose = sec("How Do You Pick the Best Pool Deck Paver Contractor?",
        f"<p>Ask to see how they detail the coping joint before you sign anything; a flexible sealant over a backer rod, not sand run straight up to mortar-set coping, is the detail that keeps that first course of pavers from rocking loose within a year or two. Ask who's applying for whatever permit the job needs and whether that fee is in the quote. For work over $2,500, a recorded Notice of Commencement protects you under Florida's lien law ({src('fs713-13', 'F.S. 713.13')}). Check {src('dbpr-search', 'the DBPR license search')} for anyone claiming a state certification, and ask for proof of the liability insurance coverage Florida requires ({src('fs489-115', 'F.S. 489.115')}). {post('how-to-choose-a-paver-contractor-orlando', 'More criteria for Orlando')} and {post('how-to-choose-a-paver-contractor-sarasota', 'for Sarasota and Lakewood Ranch')}.</p>")

    links = sec("Related Reading",
        ul([compare('travertine-vs-concrete-pavers', 'Travertine vs. concrete pavers'),
            compare('porcelain-vs-travertine-pavers', 'Porcelain vs. travertine pavers'),
            post('extend-patio-under-screen-enclosure', 'Extending a patio under a pool screen enclosure'),
            post('does-a-new-driveway-add-home-value', 'Does a pool deck add home value?'),
            post('best-pavers-for-florida', 'The best pavers for Florida homes')]))

    areas = sec("Pool Deck Paver Service Areas",
        "<p>We install travertine, shell stone and concrete pool deck pavers across Greater Orlando and the Sarasota–Manatee area, including:</p>"
        + ul([cs("orlando", K), cs("sarasota", K), cs("lakewood-ranch", K), cs("bradenton", K)]))

    body = "".join([intro, material, base, coping, overlay, build_steps, florida, cost, permits, care, choose, areas, links,
                     "<!--AUTO:service-cities-->"])

    faqs = [
        faq("Will pavers over my existing pool deck end up higher than the coping?",
            f"Often, since the paver plus its bedding layer adds height the original slab didn't have. We check that buildup against the coping, the equipment housing and every nearby door threshold before starting, and set a thinner bedding system or shave the old slab where it's needed so the finished surface meets the coping cleanly. {post('pavers-over-existing-concrete', 'General overlay feasibility')} covers driveways and patios too."),
        faq("Is travertine a good choice for a saltwater pool?",
            f"Yes, with routine sealing and rinsing. A saltwater pool runs far below seawater concentration, but splash-out still leaves salt on the stone, and travertine's porosity means that residue and moisture need a sealed surface to keep from working in over time. {post('saltwater-pools-and-coastal-salt-air-hardscape', 'More on salt air and coastal hardscape')}."),
        faq("Is travertine slippery when wet?",
            "A honed or polished finish can get slick around a pool. A tumbled or brushed travertine finish, the finish most often specified for pool decks, carries enough surface texture to hold traction when wet, which is why it's chosen far more than a polished finish in this use."),
        faq("Can you install new paver or travertine coping?",
            "Yes. Precast bullnose units, in paver or travertine, set along the pool's bond beam with a rounded edge that overhangs the water slightly, giving bare feet a comfortable, non-slip lip to grip. Bullnose coping prices separately from the field pavers, typically by the linear foot rather than the square foot."),
        faq("What size travertine pavers are best for a pool deck?",
            "There's no single right size. A French pattern, a mix of four module sizes laid in a repeating layout, hides cut pieces well around a curved coping, while a single large format such as 16x16 or 12x24 inches gives a cleaner, more modern look with fewer joints. The coping's curve and the deck's overall shape usually settle which one fits."),
        faq("Can pavers be installed inside a screen enclosure without removing it?",
            "Usually, yes. A screen cage's aluminum frame sits on isolated footers around the deck's perimeter, not on the deck surface itself, so a crew can work the base and lay pavers inside the enclosure without taking the screen down, as long as base material and equipment can get through an existing door or panel."),
        faq("Does a travertine pool deck have to be sealed?",
            f"Not structurally required, but close to it in practice. Travertine is porous enough that sunscreen, chlorine splash and standing water will stain or etch an unsealed surface faster than most homeowners expect. {post('travertine-pool-deck-care', 'Routine travertine pool deck care')} covers how often and what that upkeep looks like."),
    ]

    return page("/pool-deck-pavers/", "service",
                "Pool Deck Pavers in Florida: Travertine & Shell Stone",
                "Pool deck pavers in travertine, shell stone and concrete run $12–$30 per sq ft installed in Florida as of October 2026, including overlays and coping.",
                "Travertine, Shell Stone and Concrete Pavers for a Pool Deck",
                capsule(f"Pool deck pavers in Greater Orlando or Sarasota–Manatee run about {price('pool-deck-pavers')} per square foot installed as of {PRICE_DATE}, in travertine, shell stone or concrete, set either on a new compacted base or as an overlay on a sound old concrete deck. Travertine and shell stone stay cooler underfoot than concrete pavers in direct sun."),
                body, faqs=faqs,
                sources=["homeguide-travertine", "homeguide-pool-deck", "poolmechanic-pooldeck-cfl", "craftpavers-fl-pricing", "icpi-ts2", "icpi-ts3", "icpi-ts5",
                         "nrcs-eaugallie-osd", "nrcs-immokalee-osd", "nrcs-myakka-osd", "fl-senate-2011-104", "fdot-sdg", "orlando-res-requirements",
                         "manatee-ldc-511.16-pool-decks", "lwr-ceva-manual", "laureatepark-faq", "fs720-3035", "fs489-115", "fs713-13", "dbpr-search", "nws-mlb-wetdry"],
                related=[("/pool-deck-cost/", "pool deck cost guide"), ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers"),
                         ("/blog/best-pavers-for-florida/", "best pavers for Florida"), (SERVICES["concrete-pool-decks"]["route"], "concrete pool decks"),
                         (SERVICES["paver-patios"]["route"], "paver patios"), (SERVICES["paver-sealing"]["route"], "paver sealing"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Pavers", "/pavers/")], crumb="Pool deck pavers", service=K,
                hero_photo=hero, offer=offer(SERVICES[K]["price"]), eyebrow="Pavers · Greater Orlando & Sarasota–Manatee",
                howto=("How Pool Deck Pavers Are Installed", [
                    ("Protect the pool and sound the old slab, if there is one.", "Cover the water and check any existing deck for hollow or failed sections before setting anything."),
                    ("Excavate or clean and prep the surface.", "Excavate to base depth and grade, or pressure-wash and patch an existing slab for an overlay."),
                    ("Set and cure the coping.", "Install mortar-set coping along the bond beam early and let it cure before field work starts."),
                    ("Compact the base in lifts.", "Place and compact aggregate base to 98% Proctor with a two-direction slope toward deck drains."),
                    ("Screed the bedding sand.", "Screed a 1-inch layer of bedding sand level across the compacted base or bedding system."),
                    ("Lay the field pattern from the coping outward.", "Set full pavers against the fixed coping line first, pushing cut pieces to the outer edge."),
                    ("Set edge restraint and compact.", "Install restraint at every open edge, including against the coping, then compact the field."),
                    ("Sweep joint sand, seal, and test every drain.", "Sweep and compact joint sand, seal where specified, and run water to confirm drainage."),
                ]))


def get_pages():
    return [concrete_pool_decks(), pool_deck_pavers()]
