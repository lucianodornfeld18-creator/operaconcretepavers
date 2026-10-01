# -*- coding: utf-8 -*-
"""Comparison pages, batch a: pavers vs concrete driveway, stamped vs pavers, pavers vs concrete pool deck,
cool deck vs pavers vs travertine, travertine vs concrete pavers, porcelain vs travertine pavers."""
from _helpers import page, capsule, sec, table, faq, ul, note, a, svc, city, cs, post, compare, src, ext, price, per, tel, contact
from _data import SERVICES, PRICE_DATE, PRICE_LABEL

NAR_OUTDOOR = ("NAR/NALP, 2023 Remodeling Impact Report: Outdoor Features",
               "https://www.nar.realtor/sites/default/files/documents/2023-03-remodeling-impact-outdoor-features-03-17-2023.pdf")
ANSI_PORCELAIN = ("ANSI, porcelain and ceramic tile standard A137.1", "https://blog.ansi.org/ansi/porcelain-ceramic-tile-ansi-a137-1-astm-definition/")
ARCHATRAK_2CM = ("Archatrak, 2 cm porcelain pavers for outdoor use", "https://archatrak.com/2cm-porcelain-pavers/")


def _price_note():
    return f"{PRICE_LABEL}, {PRICE_DATE}; a written quote follows a site visit."


def pavers_vs_concrete_driveway():
    verdict = sec("The Short Answer",
        f"<p>Concrete and pavers both hold up to Florida driveways when the base is built right; the difference is price, repair and who controls what the surface looks like. Concrete runs {price('concrete-driveway')} per {per('concrete-driveway')} installed and pavers run {price('paver-driveway')}, as of {PRICE_DATE} ({src('homeguide-concrete-driveway', 'HomeGuide')}; {src('homeguide-driveway-pavers', 'HomeGuide')}). The {svc('concrete-driveways', 'concrete driveway')} and {svc('paver-driveways', 'paver driveway')} pages cover how we build each one; this page is about choosing between them.</p>")

    cmp_table = sec("Pavers vs. Concrete Driveway at a Glance",
        table("Driveway comparison, Florida, " + PRICE_DATE,
              ["Factor", "Poured concrete", "Pavers"],
              [["Installed cost", f"{price('concrete-driveway')} / {per('concrete-driveway')}", f"{price('paver-driveway')} / {per('paver-driveway')}"],
               ["Lifespan", "No single verified Florida figure; a well-cured, correctly jointed slab goes a long time before it needs replacing", "No single verified Florida figure; base compaction and edge restraint matter more than the paver itself"],
               ["Upkeep", "Occasional rinse, optional sealer, crack filling as needed", "Joint sand tops off over time; cleaning and sealing on a schedule you pick, not a fixed one"],
               ["Feel underfoot in sun", "A light broom finish runs cooler than a dark one; color drives this more than the material", "Same rule by color; a light paver behaves like light concrete, a dark one holds more heat"],
               ["Heavy rain and standing water", "Sheet-flows off a correctly sloped slab; a flat or low spot holds water until it's cut and re-graded", "Can be specified as a permeable system that lets water infiltrate through the joints instead of sheeting off"],
               ["Repair after settling or a crack", "A patch usually reads as a patch; a full panel replacement blends in better but costs more", "The affected units lift out, the base gets corrected underneath, and the same pavers go back down"],
               ["HOA and community rules", "Plain concrete is common in older platted neighborhoods; some newer communities require a decorative finish", "Specified outright by some master-planned communities; changing material elsewhere usually needs written approval first"],
               ["Resale", "No driveway-specific figure is published", "No driveway-specific figure is published; a national patio project recovered most of its cost (see below)"]],
              f"{_price_note()} Lifespan and resale rows reflect the best available published data, not a site-specific estimate."))

    answered = sec("Which Is Better for a Driveway: Pavers or Concrete?",
        "<p>For most Florida homeowners the decision comes down to three things: how much you want to spend up front, whether a future crack or sunken corner bothers you enough to pay more now to avoid showing a patch later, and whether your HOA already decided for you. Concrete is the better pick when budget drives the project and you're comfortable with a joint eventually cracking the way it's designed to. Pavers are the better pick when the ability to lift, fix and relay a section without a visible seam matters, or when the community's design guidelines call for them.</p>"
        "<p>Neither material is the wrong answer on flatwoods soil. Concrete that's poured over a properly compacted base and jointed on schedule resists random cracking; pavers that are compacted to the right density and edge-restrained resist the shifting that causes gaps. The material matters less than whether the base underneath was built for the soil it's sitting on.</p>")

    choose = sec("When to Choose Each One",
        "<h3>Choose concrete if:</h3>"
        + ul(["Budget is the main driver and the driveway is large enough that a per-square-foot gap adds up fast.",
              "You want one continuous surface that's simple to pressure-wash and keep clean.",
              "A hairline crack along a control joint, which is the slab doing its job, doesn't bother you.",
              "You're matching an existing plain-concrete apron or sidewalk in an older subdivision."])
        + "<h3>Choose pavers if:</h3>"
        + ul([f"Your HOA's design guidelines specify pavers or a decorative surface; {post('hoa-approval-for-pavers-and-concrete', 'getting that approved')} is its own process.",
              "You'd rather pay more now for a surface where a stained or cracked section can be rebuilt in place.",
              "The lot has a history of soft spots or settling and you want to fix one corner without tearing out the whole driveway.",
              "You want a pattern, border or color mix without the extra step of stamping."]))

    florida = sec("What Florida Conditions Change About This Choice",
        "<h3>Flatwoods Soil and Uneven Settling</h3>"
        f"<p>Much of Greater Orlando sits on Myakka and Smyrna soils, and the Suncoast has EauGallie and Immokalee; all four hold a seasonal high water table within about 18 inches of the surface for part of the year ({src('nrcs-myakka-osd', 'NRCS Myakka series')}; {src('nrcs-smyrna-osd', 'NRCS Smyrna series')}; {src('nrcs-eaugallie-osd', 'NRCS EauGallie series')}; {src('nrcs-immokalee-osd', 'NRCS Immokalee series')}). That moisture swing is exactly why base compaction matters more here than the choice between concrete and pavers: a subgrade that's soft in August and firm in April moves either surface if it isn't compacted in lifts first.</p>"
        "<h3>Pour and Install Timing Through the Rainy Season</h3>"
        f"<p>Florida's rainy season runs roughly late May through mid-October on both coasts ({src('nws-mlb-wetdry', 'NWS Melbourne')}). A concrete pour needs a dry window to finish and start its cure before a storm hits; a paver base needs the same dry window to compact the aggregate and sweep joint sand without washing it out. Scheduling either job around an afternoon thunderstorm pattern is a planning problem, not a reason to favor one material over the other.</p>"
        "<h3>Salt Air on the Sarasota–Manatee Coast</h3>"
        f"<p>Within about 2,500 feet of water carrying meaningful chloride, FDOT treats exposed structural steel as sitting in a more corrosive environment, a bridge-engineering standard we use as context for any wire mesh in a concrete slab or metal edge restraint in a paver base near the coast ({src('fdot-sdg', 'FDOT Structures Design Guidelines')}). Inland Orlando-area driveways don't deal with this at all.</p>")

    example = sec("A Worked Example: A Two-Car Driveway",
        f"<p>Say you have an 800 sq ft driveway (20 × 40 ft) in a 1990s Kissimmee subdivision, replacing a cracked slab with plain concrete gutters and curb. Illustrative only: a plain concrete replacement at {price('concrete-driveway')} per sq ft runs roughly $4,800–$12,000, before demolition. The same footprint in pavers at {price('paver-driveway')} per sq ft runs roughly $8,000–$24,000. {post('does-a-new-driveway-add-home-value', 'Whether that difference pays back at resale')} is a separate question from what it costs to build; a national 2023 survey found a concrete-paver patio project recovered about 95 percent of its cost when the home sold, the closest published figure to a driveway, though it measures a patio, not a driveway ({ext(NAR_OUTDOOR[1], 'NAR/NALP 2023')}).</p>")

    links = sec("Related Reading",
        ul([compare('stamped-concrete-vs-pavers', 'Stamped concrete vs. pavers for a patio'),
            compare('resurface-vs-replace-concrete', 'Resurface or replace a concrete driveway'),
            compare('concrete-driveway-finishes', 'Broom finish vs. exposed aggregate vs. stamped'),
            post('concrete-driveway-cracks-florida', 'which driveway cracks are normal in Florida'),
            post('why-pavers-sink-in-florida', 'why pavers sink in Florida'),
            a('/concrete-driveway-cost/', 'concrete driveway cost guide'), a('/paver-driveway-cost/', 'paver driveway cost guide')]))

    body = "".join([verdict, cmp_table, answered, choose, florida, example, links])

    faqs = [
        faq("What's the real price difference between a paver and a concrete driveway in Florida?",
            f"On an 800 sq ft two-car driveway, concrete at {price('concrete-driveway')} per sq ft runs roughly $4,800–$12,000 and pavers at {price('paver-driveway')} run roughly $8,000–$24,000, before demolition or base repair. The gap widens on larger driveways and narrows if the old surface doesn't need to come out first."),
        faq("Can a cracked paver driveway be fixed without replacing the whole thing?",
            "Usually yes, which is the main repair advantage pavers have over a poured slab. The affected units get lifted, the base underneath gets corrected, and the same or matching pavers go back down over the fixed spot, rather than cutting out and repouring a full panel."),
        faq("Does my HOA get a say in whether I install pavers or concrete?",
            f"It can. Florida law lets an HOA control the appearance of improvements only to the extent its declaration or published guidelines say so, and it can't restrict your choice among options the documents already list ({src('fs720-3035', 'F.S. 720.3035')}). Some master-planned communities specify pavers or a decorative finish outright; changing material elsewhere usually needs a modification request approved first."),
        faq("Which costs less to maintain over time, pavers or a concrete driveway?",
            "Concrete asks for less routine attention: an occasional rinse and an optional sealer. Pavers need joint sand topped off periodically and sealing on whatever schedule you choose, since there's no fixed interval set by the industry. Neither one is expensive to maintain compared to the cost of installing it."),
        faq("Can pavers be installed over my existing concrete driveway instead of tearing it out?",
            f"Sometimes, if the slab is sound and the added height works against garage and entry thresholds. {post('pavers-over-existing-concrete', 'This overlay question')} has its own detailed answer, since it depends on the slab's condition more than on anything specific to driveways."),
        faq("Is a paver driveway slippery when it rains?",
            "A textured or tumbled paver finish grips about as well as a broom-finished concrete slab in the rain. A smooth, polished paver finish is less common on driveways specifically because it sheds traction faster than a textured one when wet."),
    ]

    return page("/compare/pavers-vs-concrete-driveway/", "compare",
                "Pavers vs. Concrete Driveway Cost in Florida",
                f"Concrete driveways run {price('concrete-driveway')} and pavers {price('paver-driveway')} per sq ft installed in Florida as of {PRICE_DATE}. Cost, repair, HOA rules and a worked example.",
                "Pavers vs Concrete Driveway in Florida: Cost, Lifespan and Upkeep",
                capsule(f"As of {PRICE_DATE}, a Florida concrete driveway runs {price('concrete-driveway')} per {per('concrete-driveway')} against {price('paver-driveway')} for pavers. Concrete wins on price and simplicity. Pavers cost more, but a sunken or stained section lifts out and resets without a visible patch, which matters more on flatwoods lots that settle unevenly or in HOAs that specify a paver or decorative surface."),
                body, faqs=faqs,
                sources=["homeguide-concrete-driveway", "homeguide-driveway-pavers", "nrcs-myakka-osd", "nrcs-smyrna-osd", "nrcs-eaugallie-osd", "nrcs-immokalee-osd",
                         "nws-mlb-wetdry", "fdot-sdg", "fs720-3035", NAR_OUTDOOR],
                related=[(SERVICES["concrete-driveways"]["route"], "concrete driveways"), (SERVICES["paver-driveways"]["route"], "paver driveways"),
                         ("/concrete-driveway-cost/", "concrete driveway cost guide"), ("/paver-driveway-cost/", "paver driveway cost guide"),
                         ("/compare/stamped-concrete-vs-pavers/", "stamped concrete vs. pavers"), ("/compare/resurface-vs-replace-concrete/", "resurface or replace concrete"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Comparisons", "/compare/")], form=False, published="2026-10-01")


def stamped_concrete_vs_pavers():
    verdict = sec("The Short Answer",
        f"<p>Stamped concrete and pavers both dress up a patio or outdoor living space, but they get the look two different ways: one surface stamped and colored while it's still wet, the other built from individual units with a joint between every one. Installed cost runs {price('stamped-concrete')} per {per('stamped-concrete')} for stamped concrete and {price('paver-patio')} for pavers as of {PRICE_DATE} ({src('homeguide-stamped', 'HomeGuide')}; {src('homeguide-paver-patio', 'HomeGuide')}). The {svc('stamped-concrete', 'stamped concrete')} and {svc('paver-patios', 'paver patio')} pages cover how each is built.</p>")

    cmp_table = sec("Stamped Concrete vs. Pavers for a Patio",
        table("Patio comparison, Florida, " + PRICE_DATE,
              ["Factor", "Stamped concrete", "Pavers"],
              [["Installed cost", f"{price('stamped-concrete')} / {per('stamped-concrete')}", f"{price('paver-patio')} / {per('paver-patio')}"],
               ["Lifespan", "No single verified Florida figure; depends on the base and how well the sealer coat is kept up", "No single verified Florida figure; depends on base compaction and joint sand maintenance"],
               ["Upkeep", "Resealing on a schedule you watch for, not a fixed interval; no joint sand to manage", "Joint sand top-ups and sealing on a schedule you choose; more surface to maintain, piece by piece"],
               ["Feel underfoot in sun", "Lighter integral colors run cooler than dark ones; the pattern itself doesn't change the heat", "Light-colored or light-finish pavers behave like light concrete; dark units hold more heat"],
               ["Pattern and color", "One continuous surface stamped and colored as a single pour", "A wider range of module sizes, textures and mixed-color layouts, since each unit is its own piece"],
               ["Repair after a crack or stain", "A patch in the pattern is hard to color-match perfectly; a full re-pour blends better", "The stained or cracked unit lifts out and gets replaced without touching the rest of the patio"],
               ["HOA acceptance", "Common and rarely restricted on its own; some communities limit color or pattern choices", "Common; some communities specify pavers for patios visible from a golf course or common area"],
               ["Resale", "No material-specific figure; curb appeal and condition weigh more than which one was used", "A national patio project matching this scope recovered about 95% of its cost (see below)"]],
              f"{_price_note()} The lifespan and resale cells above state what is and isn't published rather than a guaranteed number."))

    answered = sec("Is Stamped Concrete Better Than Pavers?",
        "<p>Neither one is better outright; they trade off differently. Stamped concrete gives you one continuous field poured as a single piece, so there's no joint pattern breaking up the design, and it typically costs less than pavers for the same square footage. Pavers give you more pattern and color combinations because each unit is its own piece, and a damaged section comes out and goes back in without redoing the whole patio.</p>"
        "<p>The decision usually comes down to how you weigh that trade: pay less and accept that a repair down the road will probably show, or pay more up front for a surface where it won't. A smaller, enclosed lanai patio where any stamped-concrete patch would be highly visible often tips toward pavers; a larger open patio where cost per square foot adds up fast often tips toward stamped concrete.</p>")

    choose = sec("When to Choose Each One",
        "<h3>Choose stamped concrete if:</h3>"
        + ul(["The patio is large enough that the per-square-foot price gap between the two materials adds up.",
              "You want one continuous surface with no joints to clean or re-sand.",
              "You're matching a stamped driveway or walkway already on the property.",
              "A repair down the road being visible is an acceptable trade-off for the lower starting price."])
        + "<h3>Choose pavers if:</h3>"
        + ul(["A damaged or stained section needs to come out cleanly without affecting the rest of the patio.",
              "You want a mixed-size or multi-color layout that a single stamped pattern can't replicate exactly.",
              "The patio sits under a screen enclosure where fixing a repair invisibly matters more because it's always on display.",
              "Your community's guidelines call for pavers on visible outdoor living spaces."]))

    florida = sec("What Florida Conditions Change About This Choice",
        "<h3>Hot-Weather Pours and Installs</h3>"
        f"<p>Stamping has to happen while the concrete is still plastic, which narrows the window on a hot Florida afternoon; ACI guidance treats concrete above 95°F at discharge, or an evaporation rate above 0.2 lb per sq ft per hour, as conditions that cause plastic shrinkage cracking before the stamping is even finished ({src('aci-faq-maxtemp', 'ACI FAQ')}; {src('aci-ci-evap-2007', 'ACI Concrete International, 2007')}). Paver installs don't race a cure window the same way, though joint sand compaction still needs a dry stretch.</p>"
        "<h3>Rainy-Season Scheduling</h3>"
        f"<p>Both coasts see their wet season run roughly late May into mid-October ({src('nws-mlb-wetdry', 'NWS Melbourne')}). A stamped pour caught by rain before the pattern sets loses its texture; a paver base caught by rain before compaction just needs to dry out and get re-tested before work continues. Either job gets scheduled around the afternoon storm pattern rather than around the calendar date alone.</p>"
        "<h3>Flatwoods Soil Under an Open Patio</h3>"
        f"<p>Patios built on Myakka, Smyrna, EauGallie or Immokalee soils sit over a water table that can rise within about 18 inches of the surface for part of the year ({src('nrcs-myakka-osd', 'NRCS Myakka series')}; {src('nrcs-eaugallie-osd', 'NRCS EauGallie series')}). That moisture swing is why we compact the subgrade in lifts under either material rather than assuming a patio-sized area needs less prep than a driveway.</p>")

    example = sec("A Worked Example: A Backyard Patio",
        f"<p>Say you have a 16 × 18 ft backyard patio (288 sq ft) off a 2000s-built Lakewood Ranch home, replacing a plain slab that's chipped at the edges. Illustrative only: stamped concrete at {price('stamped-concrete')} per sq ft runs roughly $2,300–$5,500. Pavers at {price('paver-patio')} per sq ft run roughly $2,900–$4,900. The gap is narrower here than on a driveway, which is part of why patios are the project where pavers most often win out over stamped concrete on a straight cost comparison.</p>")

    links = sec("Related Reading",
        ul([compare('pavers-vs-concrete-driveway', 'Pavers vs. concrete driveway'),
            compare('travertine-vs-concrete-pavers', 'Travertine vs. concrete pavers'),
            post('stamped-concrete-maintenance-florida', 'stamped concrete maintenance in Florida'),
            post('paver-patio-ideas-florida', 'paver patio ideas for Florida backyards'),
            a('/stamped-concrete-cost/', 'stamped concrete cost guide'), a('/paver-patio-cost/', 'paver patio cost guide')]))

    body = "".join([verdict, cmp_table, answered, choose, florida, example, links])

    faqs = [
        faq("Is stamped concrete more expensive than a paver patio in Florida?",
            f"Usually the other way around. Stamped concrete runs {price('stamped-concrete')} per sq ft and pavers run {price('paver-patio')}, so pavers typically cost more installed, not less, even though a plain poured slab would be the cheapest option of all three."),
        faq("Can pavers be laid in a pattern that looks like stamped concrete?",
            "To a point. Pavers come in enough shapes, sizes and colors to create a running-bond, herringbone or basketweave look that reads as intentional, but they won't replicate a stamped slate or wood-plank texture molded into a single continuous surface. The two achieve a decorative look through different means."),
        faq("Which is easier to repair around a lanai or pool cage, stamped concrete or pavers?",
            "Pavers, in most cases. A screen enclosure makes any repair more visible because it's enclosed and looked at daily, and lifting a stained or cracked paver unit and resetting it avoids the color-match problem that comes with patching a stamped pattern."),
        faq("Do pavers or stamped concrete look more natural for a Florida patio?",
            "That's a matter of taste more than a technical answer. Stamped concrete can mimic flagstone, slate or wood-plank patterns in a single continuous field; pavers give an actual joint line between units, which reads as more traditionally hardscaped rather than imitating another material."),
        faq("Can stamped concrete and pavers be combined in the same backyard?",
            "Yes, and it's a common way to control cost: a stamped concrete field for the main patio area with a paver border, fire-pit pad or walkway accent. The two meet at an expansion joint, the same detail used anywhere concrete meets a different material."),
    ]

    return page("/compare/stamped-concrete-vs-pavers/", "compare",
                "Stamped Concrete vs. Pavers: Florida Patios",
                f"Stamped concrete runs {price('stamped-concrete')} and pavers {price('paver-patio')} per sq ft installed in Florida as of {PRICE_DATE}. Cost, repair, patterns and a worked patio example.",
                "Stamped Concrete vs Pavers for Patios and Outdoor Living",
                capsule(f"Stamped concrete runs {price('stamped-concrete')} per {per('stamped-concrete')} and pavers run {price('paver-patio')} in Florida as of {PRICE_DATE}, which means pavers usually cost more, not less, than a stamped pattern poured in place. Stamped concrete gives one continuous field at a lower price; pavers give more pattern choice and a repair that doesn't show."),
                body, faqs=faqs,
                sources=["homeguide-stamped", "homeguide-paver-patio", "aci-faq-maxtemp", "aci-ci-evap-2007", "nws-mlb-wetdry", "nrcs-myakka-osd", "nrcs-eaugallie-osd"],
                related=[(SERVICES["stamped-concrete"]["route"], "stamped concrete"), (SERVICES["paver-patios"]["route"], "paver patios"),
                         ("/stamped-concrete-cost/", "stamped concrete cost guide"), ("/paver-patio-cost/", "paver patio cost guide"),
                         ("/compare/pavers-vs-concrete-driveway/", "pavers vs. concrete driveway"), ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Comparisons", "/compare/")], form=False, published="2026-10-01")


def pavers_vs_concrete_pool_deck():
    verdict = sec("The Short Answer",
        f"<p>Around a Florida pool, the choice is between a poured concrete deck (broom-finished, Kool Deck-style coated, or stamped) and pavers (travertine, shell stone or concrete). Concrete pool decks run {price('concrete-pool-deck')} per {per('concrete-pool-deck')} and pool deck pavers run {price('pool-deck-pavers')}, as of {PRICE_DATE} ({src('homeguide-pool-deck', 'HomeGuide')}). The {svc('concrete-pool-decks', 'concrete pool deck')} and {svc('pool-deck-pavers', 'pool deck pavers')} pages cover the build; this page is about which family of materials to pick.</p>")

    cmp_table = sec("Pavers vs. Concrete for a Pool Deck",
        table("Pool deck comparison, Florida, " + PRICE_DATE,
              ["Factor", "Poured concrete", "Pavers"],
              [["Installed cost", f"{price('concrete-pool-deck')} / {per('concrete-pool-deck')}", f"{price('pool-deck-pavers')} / {per('pool-deck-pavers')}"],
               ["Lifespan", "No single verified Florida figure; the isolation joint at the coping wears out well before the slab does", "No single verified Florida figure; joint sand and sealer wear out well before the units themselves"],
               ["Upkeep", "Rinse salt and chlorine residue off the coping area; recoat an acrylic finish when it chalks or goes smooth", "Rinse the splash zone more often than the rest of the field; reseal porous stone on a watched schedule"],
               ["Feel underfoot in sun", "A light broom or acrylic finish runs cooler than a dark stamped surface", "Travertine and shell stone stay noticeably cooler in direct sun than a dark concrete or stamped surface"],
               ["Repair after a crack", "A hairline crack away from the coping gets filled; one that tracks the coping usually means cutting out that section", "A sunk or stained unit lifts out, the base gets corrected, and the same or matching unit goes back"],
               ["HOA acceptance", "Common; some communities require a decorative finish on any deck visible from a common area", "Common, and often the default spec for decks in higher-end master-planned communities"],
               ["Salt and chlorine exposure", "Resists staining better when sealed; unsealed broom finish shows splash-zone residue over time", "Porous stone (travertine, shell stone) needs sealing to resist the same residue; concrete pavers resist it better unsealed"]],
              f"{_price_note()}"))

    answered = sec("Which Is Better Around a Pool: Pavers or Concrete?",
        "<p>Both hold up to Florida pool use when they're built and detailed correctly, so the decision usually turns on budget, feel underfoot and how a repair looks later. Concrete costs less installed and gives you a Kool Deck-style coating that can be recoated for a fraction of a full replacement. Pavers, especially travertine and shell stone, stay cooler underfoot in direct sun and let you fix one section without redoing the whole deck, at a higher starting price.</p>"
        f"<p>If the deck already exists and the question is whether to keep it or switch materials, {compare('cool-deck-vs-pavers-vs-travertine', 'the resurface-vs-upgrade decision')} has its own page. If you're choosing between stone types within the paver family, {compare('travertine-vs-concrete-pavers', 'travertine vs. concrete pavers')} goes deeper on that split.</p>")

    choose = sec("When to Choose Each One",
        "<h3>Choose concrete if:</h3>"
        + ul(["The deck is large and the per-square-foot gap to pavers adds up to a meaningful difference.",
              "You want the option to recoat an acrylic finish later for a fraction of a full rebuild.",
              "You're matching an existing concrete patio or lanai slab already on the property."])
        + "<h3>Choose pavers if:</h3>"
        + ul(["Staying cooler underfoot in full Florida sun matters more than the lower concrete price.",
              "You want travertine, shell stone or a mixed-pattern look that a poured slab can't replicate as finish texture.",
              "A future repair being invisible, lifting and resetting one unit instead of patching a slab, is worth paying more for now."]))

    florida = sec("What Florida Conditions Change About This Choice",
        "<h3>Open, Shadeless Pours and Hot-Weather Timing</h3>"
        f"<p>A pool deck usually goes in with no roof overhead until a screen cage is added later, so a concrete pour sits in full sun. ACI guidance flags concrete above 95°F at discharge, or an evaporation rate over 0.2 lb per sq ft per hour, as the threshold for plastic shrinkage cracking ({src('aci-faq-maxtemp', 'ACI FAQ')}). Paver base work doesn't carry that same cure-window pressure, but joint sand still needs a dry stretch to set up right.</p>"
        "<h3>Flatwoods Soil Near the Shell</h3>"
        f"<p>Both regions sit on flatwoods soils where the seasonal high water table can rise within about 18 inches of the surface for part of the year, Myakka and Smyrna around Orlando, EauGallie and Immokalee on the Suncoast ({src('nrcs-myakka-osd', 'NRCS Myakka series')}; {src('nrcs-immokalee-osd', 'NRCS Immokalee series')}). The backfill ring right around a pool shell is usually hand-placed excavation spoil rather than native soil, so it gets compacted and tested on its own regardless of which surface goes on top.</p>"
        "<h3>Salt Air and Splash-Out on the Coast</h3>"
        f"<p>A saltwater pool runs well below ocean salinity, but splash-out still leaves salt behind at the coping and the nearest few feet of deck as the water evaporates, on concrete and pavers alike. FDOT treats structures within about 2,500 feet of salt water as a more corrosive environment for exposed steel, a standard we use as context for any wire mesh or metal edge restraint near a coastal pool ({src('fdot-sdg', 'FDOT Structures Design Guidelines')}).</p>")

    example = sec("A Worked Example: A Pool Deck Resurface or Rebuild",
        f"<p>Say you have a 1,000 sq ft pool deck around a screen-enclosed pool in a 2005-built Bradenton home, with a faded, chalky Kool Deck-style finish. Illustrative only: recoating that acrylic finish runs roughly $3,000–$6,000, a new broom-finished slab at {price('concrete-pool-deck')} per sq ft runs roughly $5,000–$15,000, and travertine pavers over a demolished site run roughly $13,000–$30,000 ({src('homeguide-travertine', 'HomeGuide')}; {src('poolmechanic-pooldeck-cfl', 'Central Florida resurfacing data')}). The condition of the slab underneath, not the square footage alone, usually decides which of those three paths actually applies.</p>")

    links = sec("Related Reading",
        ul([compare('cool-deck-vs-pavers-vs-travertine', 'Cool deck vs. pavers vs. travertine'),
            compare('travertine-vs-concrete-pavers', 'Travertine vs. concrete pavers'),
            post('how-hot-do-pool-decks-get-florida', 'how hot pool decks get in Florida'),
            post('saltwater-pools-and-coastal-salt-air-hardscape', 'saltwater pools and salt air on the coast'),
            a('/pool-deck-cost/', 'pool deck cost guide')]))

    body = "".join([verdict, cmp_table, answered, choose, florida, example, links])

    faqs = [
        faq("Can you mix pavers and concrete on the same pool deck?",
            "Yes. A common approach is a poured concrete field with a paver or travertine border, or paver coping on an otherwise concrete deck. The two meet at an isolation joint with flexible sealant, the same detail used wherever a deck meets the coping."),
        faq("Which surface stays grippier by the water, broom-finished concrete or pavers?",
            "Both can be specified for traction. A broom finish leaves fine ridges that hold grip when wet, and a tumbled or brushed paver finish does the same through surface texture rather than a broom pattern. A smooth, polished finish on either material is the one to avoid right at the water's edge."),
        faq("Does a paver pool deck cost more to install than concrete?",
            f"Usually, yes. Pool deck pavers run {price('pool-deck-pavers')} per sq ft against {price('concrete-pool-deck')} for poured concrete, so the paver family, especially travertine and shell stone, typically costs more installed than a broom-finished or acrylic-coated slab."),
        faq("Which holds up better if the pool deck floods during a heavy storm?",
            "Both drain the same way, because the deciding factor is the slope built into the base, not the surface material. A poured deck with proper fall toward drains or a paver field set on a correctly sloped, compacted base both shed standing water; a flat spot in either one is a grading problem, not a material one."),
        faq("Can a damaged section of either surface be fixed without redoing the whole deck?",
            "A damaged paver section, yes, almost always, by lifting the affected units and resetting them. A damaged concrete section can sometimes be cut out and replaced as a panel, but matching the finish and color of the surrounding slab exactly is harder than resetting a paver that was already uniform to begin with."),
    ]

    return page("/compare/pavers-vs-concrete-pool-deck/", "compare",
                "Pavers vs. Concrete for a Pool Deck in Florida",
                f"Concrete pool decks run {price('concrete-pool-deck')} and pavers {price('pool-deck-pavers')} per sq ft installed in Florida as of {PRICE_DATE}. Cost, heat, repair and HOA notes.",
                "Pavers vs Concrete for a Florida Pool Deck",
                capsule(f"Concrete pool decks run {price('concrete-pool-deck')} per {per('concrete-pool-deck')} and pool deck pavers run {price('pool-deck-pavers')} in Florida as of {PRICE_DATE}. Concrete costs less and can be recoated cheaply later; travertine and concrete pavers stay cooler underfoot in full sun and let a damaged section be lifted and reset without a visible patch."),
                body, faqs=faqs,
                sources=["homeguide-pool-deck", "homeguide-travertine", "poolmechanic-pooldeck-cfl", "aci-faq-maxtemp", "nrcs-myakka-osd", "nrcs-immokalee-osd", "fdot-sdg"],
                related=[(SERVICES["concrete-pool-decks"]["route"], "concrete pool decks"), (SERVICES["pool-deck-pavers"]["route"], "pool deck pavers"),
                         ("/pool-deck-cost/", "pool deck cost guide"), ("/compare/cool-deck-vs-pavers-vs-travertine/", "cool deck vs. pavers vs. travertine"),
                         ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers"), ("/blog/pool-deck-ideas-florida/", "pool deck ideas"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Comparisons", "/compare/")], form=False, published="2026-10-01")


def cool_deck_vs_pavers_vs_travertine():
    verdict = sec("The Short Answer",
        f"<p>If your pool deck already has a worn Kool Deck-style acrylic coating, the choice isn't material from scratch, it's recoat, overlay or switch to pavers. Recoating an acrylic finish runs about $3–$6 per sq ft, a decorative overlay runs about $4–$8, and pavers over the demolished slab run {price('pool-deck-pavers')} as of {PRICE_DATE} ({src('poolmechanic-pooldeck-cfl', 'Central Florida resurfacing data')}). The {svc('concrete-pool-decks', 'concrete pool deck')} and {svc('pool-deck-pavers', 'pool deck pavers')} pages cover the build; this page is about which path fits a deck you already have.</p>")

    cmp_table = sec("Recoat, Overlay or Pavers: Comparing the Three Paths",
        table("Existing Kool Deck decision, Florida, " + PRICE_DATE,
              ["Factor", "Recoat the acrylic finish", "Decorative overlay", "Switch to pavers"],
              [["Typical cost", "$3–$6 / sq ft", "$4–$8 / sq ft", f"{price('pool-deck-pavers')} / sq ft"],
               ["What happens to the old slab", "Cleaned, patched and sprayed over", "Cleaned, patched and covered with a thicker decorative layer", "Demolished, or used as a sound base to set pavers on"],
               ["Fit", "Sound slab, cosmetic fading or chalking only", "Sound slab with minor surface flaws wanting a new look", "Cracked, sunken or undersized deck, or a wanted material change"],
               ["Feel underfoot in sun", "Depends on the coating color chosen", "Depends on the overlay color chosen", "Travertine and shell stone run noticeably cooler than a dark finish"],
               ["Repair later", "Recoat again when it chalks, loses texture or no longer beads water", "Patch or recoat the overlay; full removal is a bigger job than recoating acrylic", "Lift and reset the affected units individually"],
               ["Downtime around the pool", "Shortest; a spray-applied coating over an existing slab", "Short; thicker application but still over the existing slab", "Longest when it includes demolition and a new base"]],
              f"{_price_note()}"))

    answered = sec("Should You Resurface Your Kool Deck or Switch to Pavers?",
        "<p>Start with the slab underneath, not the surface finish. A sound slab that's just faded, chalky or showing only hairline cracking is a recoat or overlay candidate, both far cheaper than starting over. A slab that's cracked through, sunken at the coping, or hollow-sounding when tapped has a structural problem a new coating only hides for a while. Pavers become the better option once you're already removing the old surface, or once you've decided you want a different material regardless of the slab's condition.</p>"
        f"<p>Recoating buys the most time for the least money if the slab passes that check. {post('slippery-pool-deck-fixes', 'A slippery deck')} is usually a recoating or resurfacing problem on its own, separate from whether the slab needs replacing.</p>")

    choose = sec("When to Choose Each Path",
        "<h3>Recoat or overlay if:</h3>"
        + ul(["The slab is structurally sound and the only complaint is fading, chalking or a dated look.",
              "Budget is the main constraint and the deck doesn't need to change shape or size.",
              "You want the shortest possible downtime around the pool."])
        + "<h3>Switch to pavers if:</h3>"
        + ul(["The slab is already cracked, sunken or undersized and needs real work regardless of the finish.",
              "Staying cooler underfoot in direct Florida sun matters enough to justify the higher cost.",
              f"You want the option to {post('pavers-over-existing-concrete', 'set pavers over a sound old slab')} rather than demolish it, which can narrow the cost gap."]))

    florida = sec("What Florida Conditions Change About This Decision",
        "<h3>Chalking and Fading Happen Faster in Full Sun</h3>"
        f"<p>An acrylic deck coating with no shade overhead, which describes most Florida pool decks until a screen cage goes up, weathers under sustained UV and heat. The manufacturer of one common product markets it as staying cooler than plain concrete but publishes no degree figure for that difference, and no independently verified Florida temperature comparison exists for deck coatings ({src('mortex-kooldeck-brochure', 'Mortex Kool Deck brochure')}).</p>"
        "<h3>Rainy-Season Scheduling for Resurfacing Work</h3>"
        f"<p>Recoating, overlay work and paver joint sand all need a dry forecast to cure or compact correctly, which narrows the practical install window during the late-May-to-mid-October wet season on both coasts ({src('nws-mlb-wetdry', 'NWS Melbourne')}). A job planned for peak summer gets scheduled around the afternoon storm pattern rather than booked on a fixed date.</p>"
        "<h3>Settling at the Coping Isn't a Sinkhole</h3>"
        f"<p>A dish-shaped low spot away from the coping, on an old Kool Deck or any resurfaced deck, is almost always ordinary base settling. Statewide sinkhole claims concentrate heavily in Hernando, Pasco and Hillsborough counties; Orange County sits on the broader list of counties with similar geology, while Sarasota and Manatee do not ({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}).</p>")

    example = sec("A Worked Example: A Faded, 20-Year-Old Kool Deck",
        "<p>Say you have a 900 sq ft pool deck in a 2006-built Winter Garden home, with an acrylic Kool Deck-style coating that's chalky and has lost its texture, but the slab underneath taps solid with no cracking at the coping. Illustrative only: recoating runs roughly $2,700–$5,400, a decorative overlay runs roughly $3,600–$7,200, and switching to concrete pavers over the existing slab runs roughly $7,200–$13,500. If the slab passed the tap test, demolition and a full paver install from scratch isn't the first option worth pricing.</p>")

    links = sec("Related Reading",
        ul([compare('pavers-vs-concrete-pool-deck', 'Pavers vs. concrete for a pool deck'),
            compare('travertine-vs-concrete-pavers', 'Travertine vs. concrete pavers'),
            post('how-hot-do-pool-decks-get-florida', 'how hot pool decks get in Florida'),
            post('slippery-pool-deck-fixes', 'making a slippery pool deck safer'),
            a('/pool-deck-cost/', 'pool deck cost guide')]))

    body = "".join([verdict, cmp_table, answered, choose, florida, example, links])

    faqs = [
        faq("What's the real cost difference between recoating a Kool Deck and installing pavers?",
            f"Recoating an existing acrylic finish runs about $3–$6 per sq ft; pavers over a demolished site run {price('pool-deck-pavers')} per sq ft. On a 1,000 sq ft deck, that's roughly $3,000–$6,000 to recoat against $12,000–$30,000 for a full paver install, which is why a sound slab is worth confirming before pricing a switch."),
        faq("Can you tell from the surface alone whether the problem is the coating or the slab underneath?",
            "Not always, which is why a tap test matters. Chalking, fading and a smooth, slippery texture point to the coating. A hollow sound when tapped, a crack that tracks the coping line, or a visible dip points to the slab itself, and no amount of recoating fixes that."),
        faq("Is it worth sealing a worn Kool Deck instead of recoating it?",
            "Sealing alone helps water bead and slows further wear, but it doesn't restore lost texture or hide chalking the way a fresh coat does. Once the surface has gone smooth or stopped beading water, recoating addresses the underlying wear instead of masking it."),
        faq("Which option adds the least downtime around the pool?",
            "Recoating, since it's sprayed over the existing slab with no demolition. A decorative overlay takes a bit longer because the layer is thicker. Switching to pavers takes the longest when it includes removing the old deck and building a new compacted base underneath."),
        faq("Is travertine a good upgrade from a worn Kool Deck?",
            f"It's one option among several, and the right one if staying cooler underfoot in full sun and a pattern change both matter enough to justify the cost. {compare('travertine-vs-concrete-pavers', 'Travertine vs. concrete pavers')} compares it against the less expensive paver option within that same upgrade path."),
    ]

    return page("/compare/cool-deck-vs-pavers-vs-travertine/", "compare",
                "Cool Deck vs. Pavers vs. Travertine: Florida",
                "Recoating a worn Kool Deck runs about $3–$6/sq ft, pavers run $12–$30, in Florida as of October 2026. A resurface-or-replace decision guide with a worked example.",
                "Cool Deck vs Pavers vs Travertine: Resurface or Replace Your Pool Deck?",
                capsule(f"If your pool deck already has a worn acrylic Kool Deck-style finish, recoating runs about $3–$6 per sq ft, a decorative overlay about $4–$8, and switching to pavers runs {price('pool-deck-pavers')} as of {PRICE_DATE}. A sound slab with only cosmetic wear is a recoat or overlay candidate; a cracked, sunken or hollow-sounding slab needs more than a new finish."),
                body, faqs=faqs,
                sources=["poolmechanic-pooldeck-cfl", "mortex-kooldeck-brochure", "nws-mlb-wetdry", "fl-senate-2011-104"],
                related=[(SERVICES["concrete-pool-decks"]["route"], "concrete pool decks"), (SERVICES["pool-deck-pavers"]["route"], "pool deck pavers"),
                         ("/pool-deck-cost/", "pool deck cost guide"), ("/compare/pavers-vs-concrete-pool-deck/", "pavers vs. concrete for a pool deck"),
                         ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers"), ("/blog/slippery-pool-deck-fixes/", "fixing a slippery pool deck"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Comparisons", "/compare/")], form=False, published="2026-10-01")


def travertine_vs_concrete_pavers():
    verdict = sec("The Short Answer",
        f"<p>Travertine and concrete pavers are both common choices for a Florida pool deck or patio, and the split usually comes down to feel underfoot and price. Travertine installed runs {src('homeguide-travertine', '$13')}–$45 per sq ft depending on use, with pool deck installs toward {src('homeguide-travertine', '$13')}–$30; concrete pavers run {price('paver-patio')} for a patio and toward the lower half of {price('pool-deck-pavers')} for a pool deck, as of {PRICE_DATE}. The {svc('pool-deck-pavers', 'pool deck pavers')} and {svc('paver-patios', 'paver patio')} pages cover the build.</p>")

    cmp_table = sec("Travertine vs. Concrete Pavers at a Glance",
        table("Material comparison, Florida, " + PRICE_DATE,
              ["Factor", "Travertine", "Concrete pavers"],
              [["Installed cost", "$13–$30 / sq ft on a pool deck; $13–$45 overall", f"{price('pool-deck-pavers')} / sq ft on a pool deck; {price('paver-patio')} on a patio"],
               ["Lifespan", "No single verified Florida figure; a sealed, well-jointed install holds up to repeated use", "No single verified Florida figure; base compaction matters more than the unit material"],
               ["Upkeep", "Needs sealing, since it's porous; resealing has no fixed interval, watch for water that no longer beads", "Lower porosity; sealing is optional rather than needed, joint sand still tops off over time"],
               ["Feel underfoot in sun", "Stays noticeably cooler in direct sun than a dark concrete paver", "Warmer than natural stone in full sun; lighter colors run cooler than dark ones"],
               ["Repairability", "Individual units lift and reset; matching an exact vein pattern on a replacement can be harder", "Individual units lift and reset; easier to match since color runs consistent batch to batch"],
               ["HOA acceptance", "Often the default spec in higher-end master-planned communities for pool decks", "Common and broadly accepted; sometimes restricted to specific approved colors in some communities"],
               ["Salt and chlorine exposure", "Porous surface needs sealing to resist splash-zone residue and staining", "Lower porosity resists the same residue better without sealing, though sealing still helps"]],
              f"{_price_note()}"))

    answered = sec("Should I Use Travertine or Concrete Pavers Around My Pool?",
        "<p>Travertine is the better pick when staying cooler underfoot in full Florida sun is the priority worth paying for, since it reads noticeably cooler to bare feet than a dark concrete paver in direct light, and it gives a lighter, more natural stone look. Concrete pavers are the better pick when budget is the main driver, since they run less installed, resist splash-zone staining without sealing as urgently, and come in enough colors and shapes to avoid looking plain.</p>"
        "<p>Both need a properly compacted base to perform well; neither one makes up for skipped base work. The choice between them is a material and budget decision layered on top of a build quality decision that applies either way.</p>")

    choose = sec("When to Choose Each One",
        "<h3>Choose travertine if:</h3>"
        + ul(["Staying cooler underfoot around the pool in full sun matters enough to justify the higher price.",
              "You want a light, naturally textured stone look rather than a manufactured, uniform color.",
              "You're committed to sealing on a watched schedule rather than treating it as optional."])
        + "<h3>Choose concrete pavers if:</h3>"
        + ul(["Budget is the main constraint and the square footage is large.",
              "You want the widest range of colors and patterns at the lowest starting price.",
              "Lower-maintenance sealing, optional rather than needed, matters more than the coolest possible surface in sun."]))

    florida = sec("What Florida Conditions Change About This Choice",
        "<h3>Flatwoods Soil Under Either Material</h3>"
        f"<p>Both coasts sit on flatwoods soils that hold a seasonal high water table within about 18 inches of the surface for part of the year, Myakka and Smyrna around Orlando, EauGallie and Immokalee on the Suncoast ({src('nrcs-myakka-osd', 'NRCS Myakka series')}; {src('nrcs-eaugallie-osd', 'NRCS EauGallie series')}). ICPI's wet-soil guidance adds 2 to 4 inches of base thickness on soils like these, a rule that applies the same way under travertine or concrete pavers ({src('icpi-ts2', 'ICPI Tech Spec 2')}).</p>"
        "<h3>Rainy Season and Sealing</h3>"
        f"<p>Sealing either material needs a dry forecast to cure, which narrows the practical window during the late-May-to-mid-October wet season common to both coasts ({src('nws-mlb-wetdry', 'NWS Melbourne')}). Travertine's porosity makes that timing matter more, since an unsealed surface caught by a long wet stretch has more opportunity to stain.</p>"
        "<h3>Salt Air and Saltwater Pools</h3>"
        f"<p>A saltwater pool runs well below seawater concentration, but splash-out still leaves salt on the stone at the coping and nearest courses as the water evaporates, cycle after cycle. {post('saltwater-pools-and-coastal-salt-air-hardscape', 'Salt air and coastal hardscape')} covers how that plays out further along the Sarasota–Manatee coast specifically, where airborne salt adds to the splash-zone exposure.</p>")

    example = sec("A Worked Example: A Pool Deck Material Decision", (
        f"<p>Say you have a 1,200 sq ft pool deck around a new pool build in a 2026 Venice home. Illustrative only: travertine at $13–$30 per sq ft runs roughly $15,600–$36,000, and concrete pavers toward the lower half of {price('pool-deck-pavers')} per sq ft run roughly $9,600–$18,000. The gap narrows if you're comparing travertine against a mid-range concrete paver rather than the cheapest option, since paver pricing spans a wide range by color and shape on its own.</p>"))

    links = sec("Related Reading",
        ul([compare('pavers-vs-concrete-pool-deck', 'Pavers vs. concrete for a pool deck'),
            compare('porcelain-vs-travertine-pavers', 'Porcelain vs. travertine pavers'),
            compare('cool-deck-vs-pavers-vs-travertine', 'Cool deck vs. pavers vs. travertine'),
            post('travertine-pool-deck-care', 'travertine pool deck care'),
            post('best-pavers-for-florida', 'the best pavers for Florida homes'),
            a('/pool-deck-cost/', 'pool deck cost guide')]))

    body = "".join([verdict, cmp_table, answered, choose, florida, example, links])

    faqs = [
        faq("Is travertine more expensive than concrete pavers in Florida?",
            f"Yes, usually. Travertine runs $13–$30 per sq ft on a pool deck, while concrete pavers run toward the lower half of {price('pool-deck-pavers')} for the same use. The gap narrows against a higher-end concrete paver and widens against the most basic one."),
        faq("Which is more durable long-term, travertine or concrete pavers?",
            "No single published figure settles this for Florida conditions; both hold up for a long service life when the base is compacted correctly and joints or sealer are kept up. Travertine's main vulnerability is staining if it isn't sealed; concrete pavers hold their color and resist stains without sealing, but it still helps."),
        faq("Do concrete pavers fade faster than travertine in Florida sun?",
            "Concrete pavers can fade gradually with UV exposure over years, especially darker integral colors. Travertine is a natural stone and doesn't fade the same way, though an unsealed surface can pick up staining or etching from pool chemicals and sunscreen, which reads differently from fading but changes the look all the same."),
        faq("Can travertine and concrete pavers be mixed in the same patio or pool deck design?",
            "Yes. A common layout uses travertine or a travertine-look coping around the water's edge, where staying cool matters most, with concrete pavers filling the larger field farther from the pool at a lower cost per square foot."),
        faq("Which is easier to clean, travertine or concrete pavers?",
            "Concrete pavers, generally, since their lower porosity resists staining without sealing. Travertine needs sealing to resist the same stains and etching from pool chemicals, sunscreen and hard water, and an unsealed travertine surface shows spotting faster than an unsealed concrete paver does."),
    ]

    return page("/compare/travertine-vs-concrete-pavers/", "compare",
                "Travertine vs. Concrete Pavers: Florida Guide",
                f"Travertine runs $13–$30/sq ft on a Florida pool deck against {price('pool-deck-pavers')} for concrete pavers, as of {PRICE_DATE}. Cost, heat, upkeep and a worked example.",
                "Travertine vs Concrete Pavers",
                capsule(f"Travertine installed runs $13–$30 per sq ft on a Florida pool deck and concrete pavers run toward the lower half of {price('pool-deck-pavers')}, as of {PRICE_DATE}. Travertine stays noticeably cooler underfoot in direct sun and gives a lighter, natural look; concrete pavers cost less and resist splash-zone staining without sealing as urgently."),
                body, faqs=faqs,
                sources=["homeguide-travertine", "nrcs-myakka-osd", "nrcs-eaugallie-osd", "icpi-ts2", "nws-mlb-wetdry"],
                related=[(SERVICES["pool-deck-pavers"]["route"], "pool deck pavers"), (SERVICES["paver-patios"]["route"], "paver patios"),
                         ("/pool-deck-cost/", "pool deck cost guide"), ("/compare/porcelain-vs-travertine-pavers/", "porcelain vs. travertine pavers"),
                         ("/compare/pavers-vs-concrete-pool-deck/", "pavers vs. concrete for a pool deck"), ("/blog/travertine-pool-deck-care/", "travertine pool deck care"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Comparisons", "/compare/")], form=False, published="2026-10-01")


def porcelain_vs_travertine_pavers():
    verdict = sec("The Short Answer",
        f"<p>Porcelain and travertine are the two premium paver choices for a Florida patio or pool deck, and they differ mainly in porosity and price. Porcelain pavers for a driveway-grade install run $15–$32 per sq ft and travertine runs $13–$45 depending on use, with pool deck installs toward {src('homeguide-travertine', '$13')}–$30, as of {PRICE_DATE} ({src('homeguide-travertine', 'HomeGuide')}). See the {svc('pool-deck-pavers', 'pool deck pavers')} and {svc('paver-patios', 'paver patio')} service pages for how either one is actually built.</p>")

    cmp_table = sec("Porcelain vs. Travertine Pavers at a Glance",
        table("Material comparison, Florida, " + PRICE_DATE,
              ["Factor", "Porcelain", "Travertine"],
              [["Installed cost", "$15–$32 / sq ft (driveway-grade pricing; patio and pool deck pricing runs similar to higher)", "$13–$45 / sq ft; $13–$30 on a pool deck specifically"],
               ["Lifespan", "No single verified Florida figure; its low porosity resists staining and freeze damage better than most pavers", "No single verified Florida figure; a sealed, well-jointed install holds up to repeated pool use"],
               ["Upkeep", "Minimal sealing needed, since water absorption runs under 0.5% by the industry porcelain tile standard", f"Needs sealing, since it's porous; resealing has no fixed interval ({src('icpi-ts5', 'ICPI Tech Spec 5')})"],
               ["Feel underfoot in sun", "Lighter colors stay relatively cool; manufacturers favor light, reflective finishes for pool surrounds", "Stays noticeably cooler in direct sun than a dark concrete paver, a common reason it's chosen poolside"],
               ["Repairability", "Individual units lift and reset; thinner 2 cm units can chip at an edge under a sharp impact", "Individual units lift and reset; natural veining varies, which can make an exact match harder"],
               ["HOA acceptance", "Accepted broadly, though less common than travertine in older master-planned community guidelines written before it was widely used", "Often the default premium spec named in community design guidelines for pool decks"],
               ["Salt and chlorine exposure", "Very low porosity resists splash-zone residue and staining better than almost any paver option", "Porous surface needs sealing to resist the same splash-zone residue and staining"]],
              f"{_price_note()} Concrete pavers, for a lower-cost comparison, are covered on {compare('travertine-vs-concrete-pavers', 'the travertine vs. concrete pavers page')}."))

    answered = sec("Which Is Better for Florida: Porcelain or Travertine Pavers?",
        f"<p>Porcelain's main advantage is how little it absorbs: the industry standard for porcelain tile caps water absorption at 0.5 percent, against natural stone that can absorb several percent or more, which translates to less staining and less need for sealing over time ({ext(ANSI_PORCELAIN[1], 'ANSI, standard A137.1')}). Travertine's main advantage is feel and look: it reads as a natural stone with visible veining and texture, and it's the material most often specified by name in community design guidelines written for pool decks.</p>"
        "<p>Porcelain pavers for outdoor use are typically manufactured at 2 cm (about ¾ in) thick, thinner than most natural stone pavers, which keeps weight down but means an edge can chip under a hard, sharp impact in a way a thicker travertine unit resists better. Neither material makes up for a poorly compacted base; the choice between them is about upkeep and look, not structural performance.</p>")

    choose = sec("When to Choose Each One",
        "<h3>Choose porcelain if:</h3>"
        + ul(["Minimal sealing and the lowest practical staining risk from pool chemicals and sunscreen matter most.",
              "You want a uniform, manufactured look in a wide range of colors and large-format sizes.",
              "You're comfortable with a thinner unit that needs careful handling around sharp furniture legs or dropped tools."])
        + "<h3>Choose travertine if:</h3>"
        + ul(["A natural stone look with visible veining and texture matters more than the lowest upkeep.",
              "Your community's design guidelines name travertine specifically for pool decks.",
              "You're willing to seal on a watched schedule in exchange for that natural-stone appearance."]))

    florida = sec("What Florida Conditions Change About This Choice",
        "<h3>No Freeze-Thaw, but Plenty of Rain and Salt</h3>"
        f"<p>Porcelain's resistance to freeze-thaw damage is one of its selling points nationally, but that specific advantage matters less in Florida, which doesn't see the freeze cycles that crack porous pavers up north. What matters more here is splash-zone staining from pool chemicals and salt air, where porcelain's low absorption still helps, and sealing travertine against the same exposure, especially along the Sarasota–Manatee coast.</p>"
        "<h3>Rainy-Season Installation</h3>"
        f"<p>Both materials need a dry stretch to set bedding sand and joint material correctly, which narrows the install window during the late-May-to-mid-October wet season common to both coasts ({src('nws-mlb-wetdry', 'NWS Melbourne')}). Travertine's sealing step adds a second dry-weather requirement that porcelain, needing less sealing, doesn't carry the same way.</p>"
        "<h3>Flatwoods Base Requirements Apply to Both</h3>"
        f"<p>ICPI's base specs don't distinguish by paver material; a pedestrian or pool deck area still gets at least 4 inches of compacted base on well-drained soil, with 2 to 4 inches more on the flatwoods soils common to both coasts ({src('icpi-ts2', 'ICPI Tech Spec 2')}). A thin, lightweight porcelain unit depends on that base being flat and well compacted at least as much as a thicker travertine unit does.</p>")

    example = sec("A Worked Example: A Premium Pool Deck Upgrade",
        "<p>Say you have a 600 sq ft pool deck around a renovated pool in a 2026 Lakewood Ranch home, and the choice is between porcelain and travertine for a premium look. Illustrative only: porcelain at $15–$32 per sq ft runs roughly $9,000–$19,200, and travertine at $13–$30 per sq ft runs roughly $7,800–$18,000. At this scale the two often land in a similar range, which is why the decision tends to come down to look and upkeep rather than cost alone.</p>")

    links = sec("Related Reading",
        ul([compare('travertine-vs-concrete-pavers', 'Travertine vs. concrete pavers'),
            compare('pavers-vs-concrete-pool-deck', 'Pavers vs. concrete for a pool deck'),
            post('travertine-pool-deck-care', 'travertine pool deck care'),
            post('best-pavers-for-florida', 'the best pavers for Florida homes'),
            a('/pool-deck-cost/', 'pool deck cost guide'), a('/paver-patio-cost/', 'paver patio cost guide')]))

    body = "".join([verdict, cmp_table, answered, choose, florida, example, links])

    faqs = [
        faq("Is porcelain more expensive than travertine in Florida?",
            "Not necessarily. Porcelain for a driveway-grade install runs $15–$32 per sq ft, and travertine runs $13–$30 on a pool deck, so the two ranges overlap. Which one costs more on a given project depends on the specific product line and finish chosen more than on the material category alone."),
        faq("Does porcelain get as hot as concrete around a pool?",
            "Manufacturers favor light, reflective colors for porcelain pool pavers specifically because dark porcelain, like dark concrete, holds more heat in direct sun. No independently verified Florida temperature comparison exists between the two, so color is the more reliable guide than the material category."),
        faq("Can porcelain pavers crack or chip more easily than travertine?",
            f"Outdoor porcelain pavers are typically made at 2 cm (about ¾ in) thick, thinner than most travertine units, which can make an edge more vulnerable to chipping from a hard, sharp impact like a dropped tool ({ext(ARCHATRAK_2CM[1], 'Archatrak, 2 cm porcelain pavers')}). Travertine's greater thickness resists that specific kind of edge damage somewhat better, though both are durable under normal foot traffic and furniture."),
        faq("Does porcelain need to be sealed the way travertine does?",
            f"No, not to the same degree. Porcelain tile's water absorption is capped at 0.5 percent under the industry standard, which is far lower than a porous natural stone like travertine ({ext(ANSI_PORCELAIN[1], 'ANSI, standard A137.1')}). Sealing porcelain is more about joint protection than the paver itself; travertine needs it to resist staining and etching."),
        faq("Which is more slip-resistant when wet, porcelain or travertine?",
            "Both are available in textured, slip-resistant finishes rated for pool decks, and either one can be a poor choice if a smooth or polished finish is specified instead. The finish selected within each material line matters more for grip than which material it is."),
    ]

    return page("/compare/porcelain-vs-travertine-pavers/", "compare",
                "Porcelain Pavers vs. Travertine: Florida Guide",
                "Porcelain pavers run $15–$32 and travertine $13–$30 per sq ft on a Florida pool deck, as of October 2026. Cost, upkeep, heat and chip resistance compared.",
                "Porcelain vs Travertine Pavers in Florida",
                capsule(f"Porcelain pavers run $15–$32 per sq ft and travertine runs $13–$30 on a pool deck, as of {PRICE_DATE}, so the two overlap in price. Porcelain's low water absorption means less sealing and less staining risk; travertine gives a natural, veined stone look that's often named specifically in community design guidelines for pool decks."),
                body, faqs=faqs,
                sources=["homeguide-travertine", "icpi-ts2", "icpi-ts5", "nws-mlb-wetdry", ANSI_PORCELAIN, ARCHATRAK_2CM],
                related=[(SERVICES["pool-deck-pavers"]["route"], "pool deck pavers"), (SERVICES["paver-patios"]["route"], "paver patios"),
                         ("/pool-deck-cost/", "pool deck cost guide"), ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers"),
                         ("/compare/pavers-vs-concrete-pool-deck/", "pavers vs. concrete for a pool deck"), ("/blog/travertine-pool-deck-care/", "travertine pool deck care"),
                         ("/central-florida/", "Greater Orlando service area"), ("/sarasota-manatee/", "Sarasota–Manatee service area")],
                crumbs=[("Comparisons", "/compare/")], form=False, published="2026-10-01")


def get_pages():
    return [pavers_vs_concrete_driveway(), stamped_concrete_vs_pavers(), pavers_vs_concrete_pool_deck(),
            cool_deck_vs_pavers_vs_travertine(), travertine_vs_concrete_pavers(), porcelain_vs_travertine_pavers()]
