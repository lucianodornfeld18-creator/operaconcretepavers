# -*- coding: utf-8 -*-
"""FAQ hub (/faq/) and four topic FAQ pages: concrete, pavers, artificial turf, cost and permits.
Each page's Q&A matches the owner_page assignments in research/questions.csv; the body carries only
topic intros and link lists so the Q&A itself lives once, in faqs=[...], and renders as FAQPage schema."""
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, post, compare, src, ext, tel, contact


def faq_hub():
    body = "".join([
        sec("What this FAQ covers",
            "<p>This page answers the questions we hear most about working with Opera Concrete &amp; Pavers directly: estimates, service area, licensing, permits, HOA paperwork, scheduling and payment. "
            "Questions specific to concrete work, paver work, artificial turf, or project cost and permitting each have their own page, linked below, so the answers here stay focused on how a project with us actually runs rather than repeating what those four pages already cover.</p>"
            + ul([a("/faq/concrete/", "Concrete questions: strength, curing, joints and reinforcement"),
                  a("/faq/pavers/", "Paver questions: lifespan, patterns, edge restraint and care"),
                  a("/faq/artificial-turf/", "Artificial turf questions: humidity, shade, heat and the environment"),
                  a("/faq/cost-and-permits/", "Cost, permit and HOA questions by jurisdiction")])),
        sec("Getting an estimate and finding the right contractor",
            "<p>A free, on-site estimate is the starting point for any project, concrete, pavers or turf, in either service area. Before that visit, it helps to know what separates a careful bid from a cheap one: the base depth and compaction standard, the slab thickness and strength, whether demolition and permit fees are itemized, and whether the contractor's experience with your city's engineering or HOA process is specific rather than general. "
            "The three questions below set out criteria for finding and comparing concrete, paver and turf contractors near you, in Orlando, Sarasota and the towns in between, without us making the case for ourselves.</p>"),
        sec("Where Opera Concrete & Pavers works",
            f"<p>Opera Concrete &amp; Pavers runs two crews. The Orlando unit covers Orange, Osceola, Seminole, Lake and Polk counties, including {city('orlando')}, {city('kissimmee')}, {city('clermont')}, {city('oviedo')} and {city('winter-garden')}; the full list is on the {a('/central-florida/', 'Central Florida service-area page')}. "
            f"The Sarasota unit covers Sarasota and Manatee counties, including {city('sarasota')}, {city('lakewood-ranch')}, {city('bradenton')} and {city('venice')}, listed on the {a('/sarasota-manatee/', 'Sarasota-Manatee service-area page')}. A project outside either list is still worth a call; county lines don't always match where a crew can reasonably work in a day.</p>"),
        sec("Licensing, permits and HOA paperwork",
            f"<p>Florida treats concrete, paver and turf work differently depending on what's being built. Driveway installation and decorative stone work sit on the state's list of scopes a city or county may not require a license for, F.S. 489.117(4)(a)1, while structural slabs, footers and walls fall under the state's structural masonry specialty contractor category instead. "
            f"None of that changes whether a permit is required locally; it only changes whether a license can be demanded to get one. {post('florida-contractor-license-check-concrete-pavers', 'How to check a Florida contractor license')} and {a('/permits/', 'our permit guide')} go deeper than the three questions below.</p>"),
        sec("Scheduling and payment",
            f"<p>Florida law sets a few hard rules around how a residential contract gets paid and started, regardless of which company does the work. A deposit over 10 percent of the contract price starts a 30-day permit-application clock under F.S. 489.126(2), and any direct contract over $2,500 needs the lien-law notice required by F.S. 713.015 and, in most cases, a recorded Notice of Commencement under {src('fs713-13', 'F.S. 713.13')}. "
            "The two questions below cover how we schedule and structure payment inside those rules.</p>"),
    ])
    faqs = [
        faq("Do you offer free estimates?",
            f"Yes. We visit the site, measure the area, and note access and drainage, then provide a written estimate at no cost for concrete, paver and artificial turf projects across Greater Orlando and Sarasota-Manatee. {contact('Request a free estimate')} to set a time, or use {tel('orlando', 'the Orlando line')} or {tel('sarasota', 'the Sarasota line')} if you already know which unit covers your address."),
        faq("How do I find the best concrete contractor near me in Orlando?",
            f"Start with the base and the paperwork, not the photos. Ask what thickness and psi the quote specifies, whether the price includes demolition and a right-of-way or engineering permit where one applies, and whether the written scope names a control-joint layout rather than just a square-foot number. {post('how-to-choose-a-concrete-contractor-orlando', '10 criteria for choosing an Orlando concrete contractor')} walks through the rest."),
        faq("What should I look for in the best paver installer near me in Sarasota or Bradenton?",
            f"Ask for the base depth and compaction method in writing; the industry construction standard calls for at least 6 inches of compacted aggregate under a residential driveway, more on wet or poorly drained soil ({src('icpi-ts2', 'ICPI Tech Spec 2')}). Confirm whether edge restraint is its own line item, and ask how the subgrade under your specific lot factors in. {post('how-to-choose-a-paver-contractor-sarasota', 'How to choose a paver contractor in Sarasota and Lakewood Ranch')} covers more."),
        faq("How do I compare quotes from concrete and paver contractors near me?",
            f"Line up thickness, strength or paver class, base depth, demolition, who pulls the permit, and cure or settling time side by side; a lower total that's missing one of those usually explains the gap rather than reflecting a genuinely better price. {post('how-to-compare-concrete-and-paver-quotes', 'How to compare concrete and paver quotes line by line')} has a worked example."),
        faq("What areas do you serve?",
            f"Two service areas. {a('/central-florida/', 'Greater Orlando')} covers Orange, Osceola, Seminole, Lake and Polk counties, and {a('/sarasota-manatee/', 'Sarasota-Manatee')} covers Sarasota and Manatee counties. Each unit runs its own crew and schedule, so {contact('tell us your address')} when requesting an estimate and we route it to the right one."),
        faq("Are you licensed and insured?",
            f"Ask that question of any contractor, including us, before signing anything. Driveway installation sits on Florida's list of scopes a city or county can't require a license for (F.S. 489.117(4)(a)1), while structural slabs, footers and walls fall under the state's structural masonry specialty contractor category instead, so the honest answer depends on the exact scope of work. We'd rather point you to {src('dbpr-search', 'the DBPR license search')} to verify any contractor's status yourself than print a claim here you can't check."),
        faq("Do you pull the permits for my project?",
            f"For work that needs one, yes: we prepare the application, submit the site plan and schedule inspections as part of the job. Which permit applies, engineering, right-of-way, zoning or building, and what it costs, varies by city and county. {a('/permits/', 'Our permit guide')} and the county posts linked from it cover Orlando, Osceola, Seminole, Lake, Sarasota and Manatee individually."),
        faq("Do you handle the HOA application?",
            f"We provide what most associations ask for: a dimensioned site plan, material and color specs, and product information, so you or we can submit it to the architectural review committee. Florida law limits how an HOA applies its own rules (F.S. 720.3035) and bars requiring a building permit before that review happens, but it doesn't remove the review itself. {post('hoa-approval-for-pavers-and-concrete', 'How to get HOA approval for pavers or concrete')} walks through the process."),
        faq("How soon can you start my project?",
            f"It depends on the season and the permit more than on crew availability. Rainy-season scheduling, roughly late May through mid-October, and permit review time, which varies by city, both affect the start date. {post('best-time-of-year-for-hardscape-projects-florida', 'The best time of year for hardscape projects')} explains the seasonal pattern; ask for a realistic date at your estimate rather than a generic promise."),
        faq("What is your payment schedule and deposit?",
            f"We structure payment around what the job needs: a deposit at signing, then a balance due at completion for most driveway, patio and turf jobs, or progress payments tied to finished phases on larger projects. Florida law limits deposits in one specific way: taking more than 10 percent of the contract price starts a 30-day clock to apply for permits under F.S. 489.126(2), and any contract over $2,500 needs the lien-law notice required by F.S. 713.015."),
    ]
    return page("/faq/", "faq", "Concrete, Paver & Turf FAQ | Orlando & Sarasota",
                "Estimates, service areas, licensing, permits, HOA approval, scheduling and payment, answered for concrete, paver and turf projects in Florida as of October 2026.",
                "Frequently Asked Questions",
                capsule("Answers about getting an estimate, service areas, licensing, permits, HOA approval, scheduling and payment with Opera Concrete &amp; Pavers across Greater Orlando and Sarasota-Manatee, as of October 2026. "
                        "Questions specific to concrete, pavers, artificial turf or cost and permits each have their own page, linked below, for answers that go deeper than this hub does."),
                body, faqs=faqs, faq_schema_off=False, faq_title="General questions about working with us",
                sources=["dbpr-search", "fs489-117", "fs489-126", "fs713-13", "fs720-3035", "icpi-ts2"],
                related=[("/process/", "how a project runs start to finish"), ("/permits/", "permit guide by county"), ("/contact/", "request an estimate")],
                crumbs=[], crumb="FAQ", form=False, eyebrow="FAQ")


def faq_concrete():
    body = "".join([
        sec("Strength and reinforcement",
            f"<p>Florida's residential code sets a floor, not a target. FBC Residential R506.1 requires any slab on the ground to be at least 3½ inches thick, and Table R402.2 ties required strength to a weathering-exposure class rather than one number for every pour ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}; {src('fbcr-2020-ch4', 'FBC Residential Ch. 4')}). "
            f"Most driveways and patios in Greater Orlando and Sarasota-Manatee are built heavier than either floor: {svc('concrete-driveways', 'our driveway page')} and {svc('concrete-patios', 'our patio page')} cover the specific thickness and mix for each project type. Reinforcement, fiber, wire mesh or rebar, is a separate decision from strength, and the question below covers what each one actually does.</p>"
            + table("Strength and reinforcement, by the term", ["Term", "What it means", "Typical Florida driveway or patio"],
                    [["Weathering-exposure class", "Sets the strength floor under FBC Table R402.2, not one number statewide", "Most residential flatwork is poured well above the floor, at 3,000-4,000 psi"],
                     ["Fiber mesh", "Synthetic fibers mixed through the whole batch, not laid in sheets", "Common standard reinforcement for a driveway or patio"],
                     ["Wire mesh", "A welded steel grid, pulled up into the slab as the pour proceeds", "Specified where a heavier load is expected"],
                     ["Rebar", "Steel bar, used where a slab needs more support than mesh alone gives", "Thickened edges, footings and heavier pads"]],
                    f"{src('fbcr-2020-ch4', 'FBC Residential Ch. 4')}.")),
        sec("Curing, joints and cracking",
            f"<p>A poured slab goes through two different processes that get confused for one another, and it loses strength or finish quality when either one gets rushed. NRMCA's own guidance is to keep the surface moist for at least 3 days after finishing, not the 7-day figure some older references repeat ({src('nrmca-cip12', 'NRMCA CIP 12')}; {src('nrmca-cip5', 'NRMCA CIP 5')}). "
            f"Control joints are cut while that moist-curing clock is already running, within hours of finishing, not after the slab has dried out. {post('concrete-curing-in-florida-heat', 'How concrete cures in Florida heat and humidity')} and {post('concrete-driveway-cracks-florida', 'which cracks are normal in a new driveway')} go further than the two questions below.</p>"),
        sec("Overlays and color",
            f"<p>Existing concrete factors into two common questions: whether new concrete can go over it, and why a fresh pour doesn't always look uniform right away. Both come down to bond and curing conditions rather than a flaw in the mix itself. {svc('concrete-repair', 'Our repair and resurfacing page')} covers overlay thickness and when a full tear-out is the better call instead of a bonded layer on top.</p>"),
        sec("Concrete terms homeowners ask about",
            f"<p>A handful of words get used loosely around a job site, and one mix-up comes up often enough to answer directly below. {a('/concrete/', 'The concrete services hub')} lists every concrete project we build, from driveways to slabs, in plain terms rather than industry shorthand.</p>"),
    ])
    faqs = [
        faq("What strength (PSI) concrete is used for driveways and patios?",
            f"3,000 to 4,000 psi is standard for residential driveways and patios in both service areas, above Florida's code floor of 2,500 to 3,500 psi set by weathering-exposure class ({src('fbcr-2020-ch4', 'FBC Residential Table R402.2')}). Some right-of-way specs set their own minimum regardless of the rest of the slab: Orlando's engineering standards manual requires the apron section specifically to be at least 3,000 psi and 6 inches thick ({src('orlando-esm', 'City of Orlando Engineering Standards Manual')})."),
        faq("What is the difference between concrete curing and drying?",
            "Drying is water leaving the slab; curing is the chemical reaction, hydration, that gives concrete its strength, and that reaction needs moisture to keep going rather than losing it fast. A slab that dries out too quickly, which a hot, dry, windy Florida afternoon does easily, cures unevenly and can craze or crack at the surface even though it looks dry and finished on top."),
        faq("Why do contractors cut lines (joints) into concrete?",
            f"Concrete shrinks as it gains strength and will crack somewhere regardless, so a control joint gives it a planned, straight line to crack along instead of a random one across the middle of the slab. Industry spacing guidance multiplies slab thickness by 24 to 36; on a typical 4-inch driveway or patio that lands joints about every 8 to 12 feet, cut to roughly a quarter of the slab's depth within hours of finishing ({src('nrmca-cip6', 'NRMCA CIP 6')})."),
        faq("Is fiber mesh as good as rebar or wire mesh?",
            "They solve different problems, so it isn't really a fair swap. NRMCA's own guidance, and the same logic applies to rebar and fiber, is that wire mesh doesn't keep a crack from forming in the first place; it only keeps a crack from opening wider once one does. What actually decides where a slab cracks is correct, well-spaced control joints, not which reinforcement sits inside the concrete."),
        faq("Can new concrete be poured over old concrete?",
            f"Sometimes, as a thin bonded overlay, but it depends on the old slab's condition more than on preference. The existing surface has to be structurally sound, profiled or roughened for bond, and free of oil, sealer or coatings; a cracked or settling slab underneath will usually telegraph the same crack through a new overlay within a season or two. {svc('concrete-repair', 'Our repair and resurfacing page')} covers when an overlay works and when it doesn't."),
        faq("Why does new concrete look blotchy or uneven in color?",
            "Almost always from uneven curing, not a bad batch. Spots that dry or cure faster, near an edge, under direct sun, or where curing compound went on thin, lighten or darken differently than the rest of the slab while it's fresh, and most of that variation fades as the concrete finishes curing over the following weeks. A color that's still sharply blotchy past a month is worth a call."),
        faq("Is concrete the same as cement?",
            "No, though the two words get used interchangeably around a job site, including by us sometimes. Cement is the fine gray powder, a binder, mixed with water, sand and crushed stone to make concrete; concrete is the finished, poured material. A driveway, patio or slab is concrete, not cement, even though plenty of homeowners ask for a cement driveway and mean the same thing."),
    ]
    return page("/faq/concrete/", "faq", "Concrete FAQ: Strength, Curing & Joints | Florida",
                "Concrete strength, curing versus drying, control joints, reinforcement, overlays and color, answered for Florida driveways and patios as of October 2026.",
                "Concrete Questions, Answered",
                capsule("Direct answers on concrete strength, curing versus drying, control joints, reinforcement, overlays and color, for driveways and patios in Greater Orlando and Sarasota-Manatee, as of October 2026. "
                        "For a specific driveway, patio or pool deck project, the service pages linked throughout go further than this FAQ does."),
                body, faqs=faqs, faq_schema_off=False, faq_title="Concrete questions homeowners ask most",
                sources=["fbcr-2020-ch5", "fbcr-2020-ch4", "orlando-esm", "nrmca-cip12", "nrmca-cip5", "nrmca-cip6"],
                related=[("/faq/", "the full FAQ hub"), ("/concrete-driveway-cost/", "concrete driveway cost guide"), ("/compare/resurface-vs-replace-concrete/", "resurface vs. replace")],
                crumbs=[("FAQ", "/faq/")], crumb="Concrete questions", form=False, eyebrow="FAQ · Concrete")


def faq_pavers():
    body = "".join([
        sec("Lifespan and patterns",
            f"<p>Pavers are a manufactured masonry unit, concrete, clay or natural stone, set in sand rather than poured as one continuous slab, and that construction method is behind most of what makes them different from poured concrete. {svc('paver-driveways', 'Our paver driveway page')} and {svc('paver-patios', 'our paver patio page')} cover installation and base depth in full; "
            "the two questions below cover how long the units themselves hold up and which layout pattern locks together best under a vehicle.</p>"
            + table("Common paver layout patterns", ["Pattern", "How it interlocks", "Where it's typically used"],
                    [["Herringbone (45° or 90°)", "No two units share a straight joint running the same direction", "Driveways and other vehicle-loaded areas"],
                     ["Running bond", "Offset rows with long straight joints parallel to traffic", "Walkways, patios and low-traffic borders"],
                     ["Basketweave", "Pairs of units set at right angles to each other", "Patios, courtyards and decorative fields with light foot traffic"],
                     ["Random or European fan", "Mixed unit sizes locked together with no repeating joint line", "Driveway aprons and transition zones where a formal grid would look stiff"]],
                    "Pattern choice is a design and load decision, not a strength rating on the paver unit itself.")),
        sec("Joints and edge restraint",
            f"<p>Two details separate a paver field that stays tight for years from one that spreads or weeds out: the joint itself, and what holds the outer edge in place. Both are deliberate parts of the design, not gaps left by a rushed install. "
            "Flatwoods soils common across both service areas, Myakka and EauGallie among them, hold more moisture near the surface than ridge sand does, which is part of why edge restraint and a correctly compacted base matter more here than they would on a drier, sandier lot. "
            f"{post('why-pavers-sink-in-florida', 'Why pavers sink in Florida')} and {post('ants-and-weeds-in-paver-joints', 'ants and weeds between pavers')} go deeper on what happens when either one fails.</p>"),
        sec("Heat, reuse and cleaning",
            f"<p>Upkeep questions come up almost as often as installation ones: whether pavers get too hot to walk on barefoot, whether old units are worth saving during a remodel, and how to clean them without damaging the joints. None of the three has a one-size answer, since color, material and how a surface gets used all change the result. "
            f"{svc('paver-sealing', 'Our paver sealing and restoration page')} and {post('how-to-clean-pavers-without-damage', 'how to clean pavers without ruining the joints or sealer')} cover routine care beyond the three questions below.</p>"),
    ])
    faqs = [
        faq("How long do pavers last?",
            "Individual pavers, concrete, clay or natural stone, are a manufactured unit, not a poured slab, so there's no single published lifespan figure the way there might be for a roofing shingle. What actually wears out first is the joint sand and any sealer coat, not the units themselves; a field that's properly based and edge-restrained can be lifted, releveled and relaid with the same pavers for a renovation years later. The base, not the paver, is usually the real limiting factor."),
        faq("Which paver pattern is strongest for a driveway?",
            "Herringbone, laid at 45 or 90 degrees to the direction of travel, is the pattern most contractors choose under a driveway because no two adjoining units share a straight joint line in the direction tires turn, which spreads vehicle load across the interlocking field instead of working one seam loose. A running-bond or basketweave pattern looks cleaner but has longer straight joint runs that can creep apart under repeated turning near a garage."),
        faq("Why are there gaps between pavers?",
            f"The joint is doing two things on purpose: letting the field flex slightly under load instead of cracking the way one rigid slab would, and giving rainwater somewhere to go instead of sheeting off the surface. The industry construction spec keeps that gap narrow, an eighth of an inch or less, filled with dry or polymeric sand rather than left open ({src('icpi-ts2', 'ICPI Tech Spec 2')}). A joint visibly wider than that usually means sand has washed or been swept out."),
        faq("What is a paver edge restraint?",
            f"A fixed border, plastic, aluminum, steel or a concrete curb, anchored into the compacted base along the entire perimeter of a paver field and anywhere the material changes. Without it, repeated vehicle or foot traffic pushes the outer rows sideways over time, opening the joints nearest the edge first. Restraint spikes have to reach the base layer itself; edging sold for flower beds anchors only into soil and isn't a substitute ({src('icpi-ts3', 'ICPI Tech Spec 3')})."),
        faq("Do pavers get hot in the summer?",
            f"Yes, dark concrete pavers in direct Florida sun get hot enough underfoot to notice, though we don't have a verified degree-by-degree figure to put on every color and material. Lighter colors, and travertine or shell stone, generally run cooler than dark concrete pavers in full sun. {post('how-hot-do-pool-decks-get-florida', 'How hot do pool decks get in Florida')} compares surfaces around a pool specifically."),
        faq("Can old pavers be reused when remodeling?",
            "Often, yes. If the units aren't cracked or badly worn, they can be lifted, cleaned and relaid on a rebuilt base for an addition, a pattern change or a repair; the base and bedding sand underneath, not the pavers on top, are usually what needed replacing in the first place. Matching an older, possibly discontinued color to new units added alongside the reused ones is the main limit, not the pavers' condition. It's worth asking before a full tear-out is assumed."),
        faq("Can pavers be pressure washed?",
            f"Yes, with the right pressure and a wide fan tip; pressure washing is standard practice before resealing. What damages pavers isn't the washing itself, it's a narrow turbo nozzle held too close for too long, which can etch the surface or blast joint sand out faster than a normal rinse would. {post('how-to-clean-pavers-without-damage', 'How to clean pavers without ruining the joints or sealer')} covers technique."),
    ]
    return page("/faq/pavers/", "faq", "Paver FAQ: Lifespan, Patterns & Care | Florida",
                "Paver lifespan, driveway patterns, joint sand, edge restraint, summer heat, reuse and cleaning, answered for Florida pavers as of October 2026.",
                "Paver Questions, Answered",
                capsule("Direct answers on paver lifespan, driveway patterns, joint sand, edge restraint, summer heat, reuse and pressure washing, for concrete, clay and travertine pavers in Greater Orlando and Sarasota-Manatee, as of October 2026. "
                        "Installation and base-depth specifics live on the paver service pages linked throughout."),
                body, faqs=faqs, faq_schema_off=False, faq_title="Paver questions homeowners ask most",
                sources=["icpi-ts2", "icpi-ts3", "nrcs-myakka-osd"],
                related=[("/faq/", "the full FAQ hub"), ("/paver-driveway-cost/", "paver driveway cost guide"), ("/compare/pavers-vs-concrete-driveway/", "pavers vs. concrete driveway")],
                crumbs=[("FAQ", "/faq/")], crumb="Paver questions", form=False, eyebrow="FAQ · Pavers")


def faq_turf():
    body = "".join([
        sec("Humidity, pests and shade",
            f"<p>Florida's climate raises three practical questions before anyone decides on synthetic turf: what humidity does to it, whether it keeps weeds and pests out, and whether it works in the shade under an oak canopy where grass already struggles. A rainy season that runs roughly late May through mid-October and delivers most of a 49- to 51-inch annual total across both service areas ({src('noaa-normals', 'NOAA 1991-2020 climate normals')}) makes the humidity and drainage question a reasonable one to ask before, not after, installation. "
            f"{svc('artificial-turf', 'Our artificial turf page')} covers the washed-rock base and the DEP Rule 62-308.100 material standard that answer most of this by design: permeable backing, natural infill, no in-ground irrigation. "
            "The three questions below cover what that construction does and doesn't solve, including the tree-protection rules several cities in both service areas apply to any work, turf included, that reaches under a large oak's canopy.</p>"),
        sec("Heat and reflections",
            f"<p>Heat is the trade-off turf can't fully engineer around, and it shows up two different ways: direct sun across a wide-open lawn, and a concentrated reflection off a nearby window. Both call for different fixes, shade, rinsing and infill choice for the first, window film or landscaping for the second, which is why the two questions below treat them separately rather than as one heat problem. "
            "Neither is a reason to rule turf out on its own, but both are worth asking about before a lawn goes in rather than after a hot afternoon makes the answer obvious. "
            f"{post('artificial-turf-heat-in-florida', 'How hot does artificial turf get in Florida')} and {post('how-to-clean-artificial-turf', 'how to clean and maintain artificial turf')} go deeper than the two questions below on both fronts.</p>"),
        sec("Weighing the environmental trade-offs",
            f"<p>Synthetic turf is marketed as the water-saving, maintenance-free alternative to a Florida lawn, and part of that holds up under research, part of it doesn't. The honest answer below draws on an independent university comparison, measured against the Nine Principles of Florida-Friendly Landscaping, rather than either a turf manufacturer's claims or a reflexive objection to synthetic surfaces. "
            f"{post('artificial-turf-for-dogs-florida', 'Turf for dogs: odor, drainage and infill')} and {post('backyard-putting-green-florida', 'planning a backyard putting green')} cover two common uses in more depth; "
            f"the {compare('artificial-turf-vs-sod', 'artificial turf vs. sod comparison')} weighs the full trade-off against a living lawn, and the question below focuses specifically on runoff, heat and the state's current rule.</p>"),
    ])
    faqs = [
        faq("Does artificial turf get moldy or smell in Florida humidity?",
            "Not from the turf material itself, since the fibers and backing required under Florida's 2026 turf rule are synthetic and don't absorb moisture the way organic thatch does. Odor and mildew-smell complaints almost always trace back to what collects underneath or in the infill, pet waste, trapped moisture from a base that doesn't drain, or organic debris left to decompose, rather than to humidity exposure on its own. Rinsing and a draining base prevent most of it."),
        faq("Can artificial turf be installed in shade?",
            f"Yes, and it answers a problem Florida lawns have under mature oaks: live turfgrass thins or dies where canopy blocks enough sun, while synthetic turf doesn't need light to stay green. The base still has to clear the tree's drip line or get an arborist's sign-off under Florida's current turf rule ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}). Orlando and Sarasota, among other cities, also protect larger trees by ordinance, so a shaded install near a mature oak can call for a separate tree permit."),
        faq("Do bugs or fire ants live in artificial turf?",
            "Less than in natural grass, but not never. The washed-rock base and weed barrier required under Florida's current turf rule remove the organic matter and loose soil that ants and other pests nest in, which cuts the problem significantly without eliminating it outright. Ants can still move in from an adjoining planting bed, or under an edge that isn't sealed tight to a hardscape border. A lawn that borders mulch or loose soil on every side is more exposed than one framed by a paver or concrete edge."),
        faq("Can window reflections melt artificial turf?",
            f"Yes, this is a real and documented issue with double-pane low-E windows, not a turf defect. A slight bow in the glass combined with a reflective coating can focus sunlight into a concentrated hot spot well past the temperature where synthetic turf fibers start to soften, the same phenomenon that scorches nearby plants or warps vinyl siding ({ext('https://reflectdefensewindowfilm.com/blogs/news/how-low-e-windows-affect-artificial-turf-and-siding', 'window-film industry explainer')}). A lawn section that browns in one consistent spot, regardless of weather, is worth checking against nearby windows first."),
        faq("Does artificial turf need to be watered or rinsed?",
            f"Not for the lawn's health, since there's no plant to keep alive, but an occasional rinse keeps it looking and smelling right: hosing off dust, pollen and pet waste, and cooling the surface before use on a hot afternoon. Florida's current turf rule bars running an in-ground irrigation zone to turf areas, so any watering has to come from a hose rather than the sprinkler system ({src('rule62-308-100-text', 'DEP Rule 62-308.100')})."),
        faq("Is artificial turf bad for the environment in Florida?",
            f"It's a real trade-off, not a clear win either way. UF/IFAS's own comparison of synthetic and natural turfgrass found that installing it involves compacting the soil underneath, linked to more stormwater runoff than a living lawn, and surface temperatures as much as 100°F hotter than natural turfgrass ({ext('https://ask.ifas.ufl.edu/publication/EP612', 'UF/IFAS EDIS ENH1348, Synthetic Turf and the Nine Principles of Florida-Friendly Landscaping')}). "
            "Florida's 2026 rule answers part of that: natural infill only, a permeable base, and a ban on added runoff onto neighbors, while the water savings from skipping irrigation are real."),
    ]
    return page("/faq/artificial-turf/", "faq", "Artificial Turf FAQ: Heat, Humidity & More | FL",
                "Humidity, shade, pests, window-reflection heat, watering and the environmental trade-offs of artificial turf in Florida, answered as of October 2026.",
                "Artificial Turf Questions, Answered",
                capsule("Direct answers on humidity, shade, pests, window-reflection heat, watering and the real environmental trade-offs of synthetic turf in Greater Orlando and Sarasota-Manatee, as of October 2026, including what Florida's 2026 turf rule now requires. "
                        "Installation and base specifics live on the artificial turf service page."),
                body, faqs=faqs, faq_schema_off=False, faq_title="Artificial turf questions homeowners ask most",
                sources=["rule62-308-100-text", "flrules62-308-100", "noaa-normals",
                         ("UF/IFAS EDIS ENH1348, Synthetic Turf and the Nine Principles of Florida-Friendly Landscaping", "https://ask.ifas.ufl.edu/publication/EP612"),
                         ("Reflect Defense, how low-E windows affect artificial turf and siding", "https://reflectdefensewindowfilm.com/blogs/news/how-low-e-windows-affect-artificial-turf-and-siding")],
                related=[("/faq/", "the full FAQ hub"), ("/artificial-turf-cost/", "artificial turf cost guide"), ("/faq/cost-and-permits/", "permit and HOA questions")],
                crumbs=[("FAQ", "/faq/")], crumb="Artificial turf questions", form=False, eyebrow="FAQ · Artificial Turf")


def faq_cost_permits():
    body = "".join([
        sec("Permits for driveways, patios and pavers",
            f"<p>Permit rules for a driveway, patio or paver project are set city by city and county by county in both service areas; there's no single statewide answer. Florida's HB 803 lets single-family owners skip a <em>building</em> permit for some non-structural work under $7,500 starting July 1, 2026, but it doesn't touch right-of-way, engineering or zoning permits, and it requires a written exemption request before work starts ({src('orlando-hb803-guide', 'the City of Orlando HB 803 guide')}). "
            f"{a('/permits/', 'Our permit guide')} and six county-specific posts, {post('orange-county-orlando-driveway-patio-permits', 'Orange County and Orlando')}, {post('osceola-county-kissimmee-st-cloud-permits', 'Osceola County')}, {post('seminole-county-driveway-patio-permits', 'Seminole County')}, {post('lake-and-polk-county-driveway-permits', 'Lake and Polk counties')}, {post('sarasota-county-driveway-patio-permits', 'Sarasota County')} and {post('manatee-county-driveway-permits', 'Manatee County')}, "
            "cover the two questions below in jurisdiction-specific detail.</p>"),
        sec("Walls, sidewalks and what insurance covers",
            "<p>Three more questions come up once permitting is settled: who's responsible for the sidewalk out front, when a retaining wall needs engineering, and what a homeowner's policy actually covers if a slab or deck cracks or settles. None of these three have a single Florida-wide answer either, which is exactly why each one below names the jurisdictions that differ rather than giving one number for the whole state. "
            "A retaining wall in particular is worth checking early, since the height that triggers engineered drawings changes the design, the cost and sometimes the timeline well before a crew ever breaks ground.</p>"),
        sec("Taxes and comparing estimates",
            f"<p>The last two questions are less about rules and more about numbers: whether a new driveway or patio moves a tax bill, and why three contractors can quote the same job so differently even when they're all bidding the same square footage. Neither question has a single right number attached to it, which is exactly the point; both come down to understanding what's actually being compared. "
            f"{post('how-to-compare-concrete-and-paver-quotes', 'How to compare concrete and paver quotes line by line')} and {post('does-a-new-driveway-add-home-value', 'does a new driveway add home value')} go further than the two questions below.</p>"),
    ])
    faqs = [
        faq("Do I need a permit for a paver patio in Florida?",
            f"In most of the jurisdictions we build in, yes, though several current building pages, including Sarasota's and St. Cloud's, exempt an on-grade patio or paver surface from a <em>building</em> permit specifically while still requiring a zoning or right-of-way approval for anything touching the street side. The answer depends on your city or county and whether the patio sits in a setback, easement or the right-of-way; {a('/permits/', 'the permit guide')} links to the specific rule for each jurisdiction we serve."),
        faq("Do I need a permit to replace my driveway in Florida?",
            "Almost always yes for the portion in the public right-of-way, the apron, even in cities that waive a permit for private-property flatwork; Orlando, Orange County, Sarasota, Manatee and every other jurisdiction we build in requires some form of driveway or right-of-way permit. Replacing a driveway entirely on private property, with no apron work involved, is exempt in a few cities but not most. Check the county-specific post linked above before scheduling demolition."),
        faq("Who is responsible for repairing the public sidewalk in front of my house?",
            "It varies by city, which is part of why it's worth confirming before assuming either way: the sidewalk itself usually sits in the public right-of-way, but a number of Florida municipalities place the repair obligation, or at least the cost, on the abutting property owner by local ordinance, even though the city owns the land underneath. Call your city or county public works department and ask directly rather than going by a neighbor's experience."),
        faq("Does a retaining wall need a permit in Florida?",
            f"Yes in every jurisdiction we checked, though the height that triggers engineered, signed-and-sealed drawings instead of a simple permit varies widely: Sarasota County requires engineering above 4 feet ({src('sarasota-county-22-63-retaining-walls', 'Sarasota County Code §22-63')}), Longboat Key caps a retaining wall at 8 feet outright ({src('lbk-code-158.118-retaining-wall', 'Longboat Key Code §158.118')}), and Orange County applies the state building code's general unbalanced-fill threshold instead of its own number ({src('orange-res-plan-guide', 'Orange County residential plan guide')}). Palmetto requires a permit at any height ({src('palmetto-code-10-46-retaining-wall-permit', 'Palmetto Code §10-46')}). Your city's building department confirms the exact figure for your address."),
        faq("Does homeowners insurance cover a cracked driveway or pool deck?",
            f"Usually not for ordinary settling or shrinkage cracking, since most policies treat gradual wear and earth movement as excluded causes rather than a covered sudden loss. The one guaranteed exception is catastrophic ground cover collapse: every Florida property insurer must cover that specific, narrowly defined event under {src('fs-627-706', 'F.S. 627.706')}, while broader optional sinkhole-loss coverage is a separate add-on most policies don't include automatically. {post('sinkholes-and-settlement-central-florida', 'Sinkholes vs. normal settlement')} explains what a sunken slab usually signals instead."),
        faq("Will a new driveway or patio raise my property taxes?",
            "Sometimes, but rarely by much on its own. Florida county property appraisers reassess value as of January 1 each year based largely on permitted improvements reported to their office; a resurfaced or replaced driveway or patio is the kind of improvement that's often excluded from the square-footage calculations that drive a bigger reassessment, unlike a home addition. Ask your county property appraiser's office directly, since the treatment of borderline cases differs by county."),
        faq("Why do estimates for the same driveway vary so much?",
            f"Because the number hides different scopes underneath, not because contractors are padding or lowballing at random. One bid might include demolition, a thicker right-of-way apron section and a permit fee, while another assumes all three are extra; one might specify 3,000 psi and the other 4,000. {post('how-to-compare-concrete-and-paver-quotes', 'How to compare concrete and paver quotes line by line')} has a line-by-line worked example of exactly where two quotes on the same driveway diverge."),
    ]
    return page("/faq/cost-and-permits/", "faq", "Cost, Permit & HOA FAQ | Florida",
                "Permits, sidewalk repair, retaining wall rules, insurance, property taxes and comparing quotes, answered for Florida concrete and paver projects, October 2026.",
                "Cost, Permit and HOA Questions",
                capsule("Direct answers on permits, sidewalk repair responsibility, retaining wall engineering thresholds, insurance coverage, property taxes and why quotes vary, for concrete and paver projects across Greater Orlando and Sarasota-Manatee, as of October 2026. "
                        "County-specific permit rules are linked throughout rather than generalized here."),
                body, faqs=faqs, faq_schema_off=False, faq_title="Cost, permit and HOA questions homeowners ask most",
                sources=["orlando-hb803-guide", "fs-627-706", "sarasota-county-22-63-retaining-walls", "lbk-code-158.118-retaining-wall",
                         "orange-res-plan-guide", "palmetto-code-10-46-retaining-wall-permit"],
                related=[("/faq/", "the full FAQ hub"), ("/permits/", "permit guide by county"), ("/compare/pavers-vs-concrete-driveway/", "pavers vs. concrete driveway")],
                crumbs=[("FAQ", "/faq/")], crumb="Cost, permit and HOA questions", form=False, eyebrow="FAQ · Cost & Permits")


def get_pages():
    return [faq_hub(), faq_concrete(), faq_pavers(), faq_turf(), faq_cost_permits()]
