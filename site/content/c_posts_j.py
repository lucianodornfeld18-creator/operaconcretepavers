# -*- coding: utf-8 -*-
"""Blog posts, group j: the two general-planning posts (preparing a yard for installation day, choosing
the right season) and the four 'how to choose a contractor' posts (concrete and pavers, Orlando and
Sarasota). The contractor-choosing posts are criteria lists only: what to check on any concrete or paver
business before signing, never a claim about Opera's own license, insurance or track record."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext, price, per, contact, photo
from _photos import for_service


def p_prepare_your_yard_for_hardscape_installation():
    pids = for_service("concrete-slabs", 3)
    pid = pids[2] if len(pids) > 2 else (pids[0] if pids else None)
    body = "".join([
        sec("What Does \"Preparing the Yard\" Actually Mean Before a Crew Shows Up?",
            f"<p>Preparing for a {svc('concrete-driveways', 'concrete')} pour, a {svc('paver-patios', 'paver')} install or an "
            f"{svc('artificial-turf', 'artificial turf')} job comes down to four things: clearing the work area, marking what's buried "
            "in it, deciding where vehicles and equipment go for the day, and knowing what the crew needs from the household on the day "
            "itself. None of it is complicated, but skipping a step is the most common reason a scheduled start gets pushed to the "
            "afternoon, or to another day entirely.</p>"),
        sec("What Should You Do With Sprinklers and Irrigation Before Pavers or Turf Go In?",
            "<p>Irrigation heads sitting inside the footprint of a new driveway, patio or turf area get capped or relocated before "
            "excavation starts, not discovered mid-dig. Walking the planned footprint with the sprinkler system running, even briefly, "
            "shows every head and the general run of the lateral lines underneath, which is worth doing a week or two ahead rather than "
            "the morning of the job. Florida homeowners are also expected to call 811 before any digging on the property, a free service "
            "that notifies the utilities that have lines buried nearby so they can mark them, and it applies to a new paver base or turf "
            f"excavation the same as it does to a fence post ({ext('https://www.sunshine811.com/', 'Sunshine 811')}). Artificial turf "
            "carries one irrigation rule unique to the material: the state's 2026 turf standard bars watering a turf area with an "
            f"in-ground irrigation system, so heads inside the footprint get capped rather than just moved aside ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}).</p>"),
        sec("Where Does the Crew Need Truck and Equipment Access?",
            "<p>A concrete truck needs a clear path from the street to the pour, wide enough to turn and close enough that the chute "
            "reaches the forms without the driver backing across the lawn repeatedly. Overhanging branches, a parked trailer, or a gate "
            "narrower than the truck's width turn a half-hour pour into a longer, more awkward one, and on a tight lot the access route "
            "is worth walking with the measuring tape before the job is scheduled rather than after the truck is already in the "
            "driveway. Paver and turf deliveries are less picky about turning radius since the material usually comes on pallets moved "
            "by hand truck or small equipment, but the same basic rule holds: a clear, obstacle-free path from the street to the work "
            "area saves time that would otherwise go into moving things out of the way mid-job.</p>"),
        sec("What Happens to Pets, Kids and Cars During a Concrete Pour or Paver Install?",
            "<p>Pets and small children stay out of the work area entirely on pour day, both for their own safety around equipment and "
            "because a paw print or a footprint in fresh concrete sets permanently once the surface starts to skin over. A side room, a "
            "crate, or simply keeping the back door closed for the day handles most of it; a fenced yard isn't enough on its own if the "
            "work area and the rest of the yard share the same gate. Cars parked in the driveway or garage, meanwhile, need to move "
            "somewhere else, on the street or at a neighbor's, for the length of the job and through the cure; a concrete driveway "
            f"generally can't take vehicle traffic again until roughly a week after the pour ({src('nrmca-cip12', 'NRMCA CIP 12')}), "
            f"while {svc('paver-driveways', 'a paver driveway')} is usable again as soon as the base is compacted and the joint sand is "
            "swept in, with no cure to wait out.</p>"),
        sec("Should You Clear the Work Area and Mark Underground Lines First?",
            "<p>Anything sitting on or near the footprint, patio furniture, potted plants, a grill, a trampoline, a dog's water bowl, "
            "gets moved before the crew arrives rather than during setup, since every minute spent clearing the site on arrival is a "
            "minute not spent digging or forming. The same goes for anything staked or planted right at the edge of the new work: a "
            "shrub a foot from where a form board needs to go is easier to move ahead of time than to work around on the day. Beyond the "
            "811 utility marking covered above, a homeowner's own low-voltage wiring, landscape lighting and a dog fence often aren't on "
            "the utility locate at all, so flagging those separately before digging starts avoids a cut line discovered partway through "
            "excavation.</p>"
            + (photo(pid, "A worker in a high-visibility vest smooths freshly placed concrete, the kind of work day that follows weeks of site prep.") if pid else "")),
        sec("What Gate, Fence and HOA Steps Come Before Work Starts?",
            "<p>A side gate used for truck or wheelbarrow access gets measured against the equipment going through it, since a standard "
            "36 or 48 inch gate is tight for some compactors and wheelbarrows loaded with base material. Where the project also needs "
            "architectural review or a building permit, that approval has to clear before the crew shows up, not while they're standing "
            "in the driveway. A 2026 change to Florida law also keeps the association from demanding a building permit in hand just to "
            f"start reviewing a submission, so the two approvals can move on parallel tracks instead of one sitting idle until the other clears ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"{post('hoa-approval-for-pavers-and-concrete', 'Our guide to HOA approval for pavers and concrete')} walks through what a "
            "typical architectural review committee packet asks for, and the county permit guides cover the building or right-of-way "
            "side of the paperwork.</p>"),
        sec("What Should You Expect on Install Day Itself?",
            "<p>The crew's first hour on site is usually spent confirming layout, checking the access route and utility marks one more "
            "time, and setting up for demolition or excavation; the visible, fast-moving part of a concrete job, the actual pour, "
            "usually comes later in the sequence rather than first.</p>"
            + table("What to have ready, by project type", ["Project", "Before the crew arrives", "During the work"],
                    [["Concrete driveway or patio", "Cars moved, irrigation capped in the footprint, gate access measured", "Keep pets and kids out of the pour and cure area for several days"],
                     ["Paver driveway or patio", "Same clearing and irrigation steps; mark any buried low-voltage wiring", "Area usable again once compaction and joint sand are finished"],
                     ["Artificial turf", "Old sod or landscaping cleared; in-ground irrigation in the footprint capped", "Keep foot traffic light until infill and seams are finished"]],
                    "General planning guide, not a job-specific checklist; a site visit covers the particulars of a given yard.")
            + f"<p>{post('concrete-driveway-installation-process', 'Our day-by-day concrete driveway process guide')} and "
              f"{post('paver-installation-process-florida', 'our paver installation process guide')} go further into what the crew is "
              "doing at each stage once the site is ready, rather than what the homeowner needs to do beforehand.</p>"),
        sec("Say You're Preparing a Side-Yard Gate for a Paver Patio Crew in Oviedo",
            f"<p>A homeowner in {city('oviedo')} scheduling a paver patio measures the side-yard gate against the plate compactor and "
            "wheelbarrow width two weeks ahead, since the gate is the only route from the driveway to the backyard. The sprinkler zone "
            "that covers that corner of the yard gets run once to flag every head inside the planned footprint, and a low fence panel "
            "blocking the gate's swing gets unbolted and set aside before the delivery truck arrives rather than on the morning of. None "
            "of that changes the build itself; it just means the crew spends its first morning working instead of clearing a path.</p>"),
    ])
    faqs = [faq("How far ahead should I mark sprinkler heads before a paver or turf install?",
                "A week or two ahead is enough for most yards: run the irrigation zone that covers the planned footprint once to see every head and the general run of the lines, then flag them before excavation starts. Artificial turf also needs any in-ground irrigation inside its footprint capped, since Florida's 2026 turf standard bars watering turf with an irrigation system."),
            faq("Do I need to move my cars during a concrete driveway pour?",
                "Yes. Cars parked in the driveway or garage need another spot, on the street or at a neighbor's, for the pour and through the cure, since a concrete driveway generally can't take vehicle traffic again until roughly a week after the pour. A paver driveway is usable again once the base is compacted and the joint sand is swept in, with no multi-day cure to wait out."),
            faq("Can pets be in the yard during a concrete pour?",
                "No. Pets and kids stay out of the work area on pour day, both for safety around equipment and because a footprint or paw print sets permanently once the surface starts to skin over. A crate, a closed door or a separate fenced area handles it; the main work zone itself isn't a safe or practical place for them that day."),
            faq("What kind of truck access does a concrete pour need?",
                "A clear path from the street to the forms, wide enough for the truck to turn and close enough that the chute reaches without repeated backing across the lawn. Overhanging branches, a parked trailer or a narrow gate are worth checking with a tape measure before the job is scheduled, since they slow the pour down more than almost anything else on site."),
            faq("Does my HOA need to approve the project before the crew starts?",
                "Often, yes, for a driveway, paver patio or visible turf area in a master-planned community. A 2026 change to Florida law keeps the association from insisting on a building permit in hand before it will review the submission, so the architectural review and any building or right-of-way permit can proceed together rather than one waiting on the other.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/paver-patios/", "Paver patios & walkways"),
               ("/artificial-turf/", "Artificial turf"), ("/process/", "How a project runs with us"),
               ("/blog/best-time-of-year-for-hardscape-projects-florida/", "Best time of year for hardscape projects")]
    return page("/blog/prepare-your-yard-for-hardscape-installation/", "post",
                "How to Prepare for a Paver, Concrete or Turf Install",
                "How to prepare your yard for a concrete, paver or turf installation in Florida: irrigation, access, pets and HOA steps, as of October 2026.",
                "How to Prepare Your Home for a Concrete, Paver or Turf Installation",
                capsule("Preparing a Florida yard for a concrete, paver or turf installation means capping irrigation in the footprint, "
                        "clearing a truck or equipment path, moving cars and pets out of the work area, and getting any HOA or permit "
                        "approval done beforehand. As of October 2026, a concrete driveway needs about a week before it takes vehicle "
                        "traffic again, while a paver driveway is usable once the base is compacted."),
                body, faqs=faqs,
                sources=["rule62-308-100-text", "nrmca-cip12", "fs720-3035",
                         ("Sunshine 811, Florida's underground utility locate service", "https://www.sunshine811.com/")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image=pid, form=False)


def p_best_time_of_year_for_hardscape_projects_florida():
    body = "".join([
        sec("Is There a Best Time of Year to Pour Concrete or Lay Pavers in Florida?",
            f"<p>Florida's dry season, roughly mid-October through May, is the easier scheduling window for {svc('concrete-driveways', 'concrete')} "
            "and paver work, since it carries less risk of a pour getting rained on mid-job and fewer days hot enough to race against "
            "evaporation. That doesn't make the wet season off-limits. Crews plan around both seasons year-round across Central Florida "
            "and the Suncoast; the difference is how much weather-driven scheduling a given month adds to the job.</p>"),
        sec("Why Does Florida's Dry Season Suit Concrete and Paver Scheduling?",
            f"<p>NWS Melbourne's own climate record puts the median start of Central Florida's wet season at May 27 and the dry season's "
            f"start at October 15, based on records going back to 1950 ({src('nws-mlb-wetdry', 'NWS Melbourne')}); the Tampa Bay forecast "
            "office draws the line a little differently for the Suncoast, putting the regional rainy season at roughly May 15 to October "
            f"15 for Southwest Florida and May 25 to October 10 for the rest of West Central Florida ({src('nws-tbw-tstm-climo', 'NWS Tampa Bay')}). "
            "Inside that dry-season window, afternoon thunderstorms are far less frequent, which matters most on a concrete pour day, "
            "since a storm rolling in before the surface sets can mean patching the finish or, in a bad case, redoing part of the slab.</p>"),
        sec("What Changes About Scheduling During the Summer Rainy Season?",
            "<p>Pours still happen through the wet season, but the crew plans around the afternoon storm pattern rather than the "
            "calendar date, which usually means an early morning start so the concrete is placed, finished and past its most "
            f"storm-sensitive stage before clouds build later in the day. Heat adds a second factor on top of the rain: ACI guidance "
            "treats concrete placed above 95°F, or at an evaporation rate above roughly 0.2 lb per square foot per hour, as needing "
            f"extra steps, an evaporation retarder, earlier starts, prompt curing, to avoid plastic-shrinkage cracking while the surface "
            f"dries faster than the slab underneath it ({src('aci-faq-maxtemp', 'ACI')}; {src('nrmca-cip12', 'NRMCA CIP 12')}). "
            f"{post('pouring-concrete-in-florida-rainy-season', 'Our guide to pouring concrete in the rainy season')} and "
            f"{post('concrete-curing-in-florida-heat', 'our guide to curing in Florida heat')} go into both of those mechanics in more "
            "depth than fits here.</p>"),
        sec("Does Hurricane Season Affect When You Should Start a Project?",
            "<p>The Atlantic hurricane season runs June 1 through November 30 by the National Hurricane Center's own definition "
            f"({ext('https://www.nhc.noaa.gov/climo/', 'NOAA National Hurricane Center')}), which overlaps most of Florida's wet season "
            "and adds a storm-tracking variable on top of ordinary afternoon rain. That doesn't rule out a summer or early-fall project; "
            "it just means a pour or an install scheduled during an active storm watch is the kind of thing that gets moved a few days "
            f"rather than pushed through, the same way any outdoor trade handles a named storm approaching the coast. {post('pavers-and-concrete-in-hurricanes', 'Our guide to pavers, concrete and hurricanes')} "
            "covers how finished hardscape holds up once a storm does arrive.</p>"),
        sec("Is Artificial Turf Installation Less Weather-Sensitive Than Concrete or Pavers?",
            f"<p>Largely, yes. {svc('artificial-turf', 'Turf')} has no multi-day cure to protect from rain the way fresh concrete does, "
            "and the washed-rock base the state's 2026 turf standard requires is built to drain rather than hold water, so a rain delay "
            "mid-job is more about keeping the crew off a muddy excavation than about damage to the finished product. The practical "
            "limit is more mundane: seaming and nailing turf in a downpour is miserable and slower work, so crews still wait out an "
            "active storm rather than install through one, even though the material itself tolerates rain better than a curing slab "
            "does.</p>"),
        sec("Does a Florida Winter Ever Delay a Concrete Pour?",
            "<p>Rarely, and when it does the cause is nearly always an unusual overnight cold snap rather than the season in general. "
            "Both service areas sit well south of the climate where frozen ground or hard freezes routinely threaten a fresh pour, and a "
            "cool, dry December or January morning is, if anything, closer to ideal pour weather than a hot, humid August one, since "
            "slower evaporation gives the finishing crew more working time before the surface sets. The dry season's main advantage over "
            "winter elsewhere in the country isn't avoiding cold; it's avoiding the rain and heat that define a Florida summer.</p>"),
        sec("Say You're Planning a Pool Deck Replacement for Next Spring in Lakewood Ranch",
            f"<p>A homeowner in {city('lakewood-ranch')} planning a travertine pool deck for next spring gets the benefit of the dry "
            "season's lower rain risk on pour and compaction days, plus cooler mornings that give finishing crews more working time "
            "before a stamped or textured surface sets. Booking early in that window, rather than waiting for the first warm weekend, "
            "leaves more schedule room if the lakewood ranch ARC review or a county permit takes a few extra weeks, since the approval "
            f"timeline runs independently of the weather. {post('saltwater-pools-and-coastal-salt-air-hardscape', 'Our coastal salt-air guide')} "
            "covers the material side of planning a pool deck project in Sarasota and Manatee specifically.</p>"),
    ])
    faqs = [faq("What time of year is easiest for installing pavers in Florida?",
                "Roughly mid-October through May, Florida's dry season, carries the least weather-driven scheduling risk for pavers, concrete and most outdoor work, since afternoon thunderstorms are far less frequent than in summer. Projects still run through the wet season; they just plan around the storm pattern with earlier starts instead."),
            faq("Can you pour a concrete driveway during Florida's rainy season?",
                "Yes, with planning. Crews schedule an early morning start so the slab is placed, finished and past its most storm-sensitive stage before afternoon clouds typically build, and heat-mitigation steps like a curing compound or evaporation retarder address the added risk from high temperatures during the same months."),
            faq("Does hurricane season mean you shouldn't start a hardscape project?",
                "Not by itself. The Atlantic hurricane season runs June 1 through November 30 and overlaps most of Florida's wet season, but most weeks within it are ordinary work weeks. A pour or install scheduled during an active storm watch typically gets moved a few days rather than pushed through."),
            faq("Is artificial turf installation affected by Florida's rainy season?",
                "Less than concrete or a fresh paver base, since turf has no multi-day cure to protect and the required washed-rock base is built to drain. Crews still avoid seaming and nailing turf in an active downpour, but there's no equivalent to a pour getting rained on before it sets."),
            faq("Does cold weather ever delay concrete work in Florida?",
                "Rarely. Both the Orlando and Sarasota–Manatee areas sit well south of climates where frozen ground threatens a fresh pour, and a cool, dry winter morning is often closer to ideal pour weather than a hot, humid summer one, since slower evaporation gives the crew more time to finish the surface.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/paver-patios/", "Paver patios & walkways"),
               ("/artificial-turf/", "Artificial turf"),
               ("/blog/pouring-concrete-in-florida-rainy-season/", "Pouring concrete in Florida's rainy season"),
               ("/blog/concrete-curing-in-florida-heat/", "How concrete cures in Florida heat")]
    return page("/blog/best-time-of-year-for-hardscape-projects-florida/", "post",
                "Best Time to Install Pavers or Concrete in Florida",
                "When is the best time of year to install pavers, pour concrete or lay artificial turf in Florida? Dry season, hurricane season and heat, October 2026.",
                "When Is the Best Time of Year to Install Pavers, Concrete or Turf in Florida?",
                capsule("Florida's dry season, roughly mid-October through May, is the best time of year to install pavers or pour "
                        "concrete, since afternoon thunderstorms are far less frequent than in the May-to-October wet season. As of "
                        "October 2026, artificial turf is less weather-sensitive than either material, since it has no multi-day cure to "
                        "protect from rain across Greater Orlando or Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["nws-mlb-wetdry", "nws-tbw-tstm-climo", "aci-faq-maxtemp", "nrmca-cip12", "rule62-308-100-text",
                         ("NOAA National Hurricane Center, hurricane season dates", "https://www.nhc.noaa.gov/climo/")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image=None, form=False)


def p_how_to_choose_a_concrete_contractor_orlando():
    pids = for_service("concrete-driveways", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("How Do You Choose a Concrete Contractor in Orlando?",
            f"<p>Picking a {svc('concrete-driveways', 'concrete')} contractor in Orange, Osceola, Seminole or Lake County comes down to "
            "paperwork and method more than it does a photo gallery: whether the scope is in writing, who pulls the permit, how a "
            "deposit is structured, and whether the base, thickness and joint plan are spelled out before anyone signs. Ten checks cover "
            "most of what separates a clean job from a dispute later.</p>"),
        sec("What's the Best Way to Find and Vet the Best Concrete Contractor Near You?",
            "<p>Searching for the best concrete contractor near me usually turns up a long list sorted by ad spend or star rating, "
            "neither of which says much about how a specific driveway or patio will actually be built. A shorter, more useful filter "
            "runs through license status, permit handling, written scope and payment terms, in that order, before a single photo or "
            "review factors in.</p>"
            + table("Ten checks before hiring a concrete contractor in Orlando", ["Check", "Why it matters"],
                    [["License status on DBPR", "Shows discipline history and whether a state license applies to the scope"],
                     ["Which permit office handles the job", "Orange, Osceola, Seminole and Lake each run their own permit process"],
                     ["Notice of Commencement on jobs over $2,500", "Required under Florida's lien law; protects payment and title"],
                     ["License number in writing on the bid or contract", "State law requires it on every offer, bid or ad"],
                     ["Deposit amount and what it's tied to", "Over 10% triggers a permit-filing deadline under state law"],
                     ["Base depth and compaction method, in writing", "A price without a spec can't be compared to another bid"],
                     ["Slab thickness and reinforcement (fiber, mesh, rebar)", "Driveway vs. patio vs. slab loads call for different specs"],
                     ["Control joint spacing", "Joints control where a slab cracks; a missing plan means a guessing game later"],
                     ["Demolition and haul-off, spelled out", "A common line item left vague on low bids"],
                     ["Insurance certificate, not just a verbal claim", "Confirms coverage is current rather than assumed"]],
                    "General hiring checklist; not every item applies to every job size.")),
        sec("Does a Concrete Driveway Contractor Need a License in Florida?",
            f"<p>Not always, and that surprises a lot of homeowners. Florida law carves driveway installation out of state and local "
            f"licensing requirements by name, along with decorative stone, tile, marble and terrazzo installation ({src('fs489-117', 'F.S. 489.117')}). "
            "A permit can still be required even where a license can't be. Structural concrete work is handled separately: forming, "
            "placing and finishing slabs, footers, curbs and walls falls under the state's \"structural masonry specialty contractor\" "
            "certificate, a category created in 2024, so a concrete patio extension that ties into a footing or a slab that's part of a "
            f"larger structure can sit under a different rule than a stand-alone driveway ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). "
            f"Orange County's own current local licensing categories after the 2025 state preemption weren't something we could confirm "
            f"from a published page, so asking the county's contractor licensing office directly, and running any name through the "
            f"{src('dbpr-search', 'DBPR license search')}, is the reliable way to check a given business.</p>"
            + (photo(pid, "A two-car concrete driveway with a broom finish runs to the garage of a single-story Orlando-area home.") if pid else "")),
        sec("Who Pulls the Permit, and Does the Driveway Apron Need Its Own Approval?",
            "<p>Ask this before signing, not after the crew shows up. Cities inside Orange, Osceola, Seminole and Lake counties "
            "generally run their own permit process for driveway, patio and slab work, and the section of driveway between the sidewalk "
            "and the street often falls under a separate right-of-way permit since that strip technically sits in public property even "
            f"when the rest of the driveway is private. {post('orange-county-orlando-driveway-patio-permits', 'Our Orange County permit guide')}, "
            f"{post('osceola-county-kissimmee-st-cloud-permits', 'our Osceola County guide')}, "
            f"{post('seminole-county-driveway-patio-permits', 'our Seminole County guide')} and "
            f"{post('lake-and-polk-county-driveway-permits', 'our Lake and Polk County guide')} cover each department's specific process; "
            "a contractor who can't say clearly who applies for what is worth a follow-up question before it becomes a problem mid-job.</p>"),
        sec("What Should the Deposit and Payment Schedule Look Like?",
            f"<p>Florida law treats a deposit over 10 percent of the contract price as a trigger, not a formality: a contractor who takes "
            "more than that has 30 days to apply for the needed permits and has to start work within 90 days after the permit issues, "
            f"unless there's just cause or the homeowner agreed in writing to a longer wait ({src('fs489-126', 'F.S. 489.126')}). A "
            "payment schedule tied to completed stages, demolition, base, pour, finish, rather than one large sum up front, is easier to "
            "match against actual progress on site. It's also worth knowing that Florida's three-day buyer's-cancellation right applies "
            "only to a home-solicitation sale, meaning the seller approached the homeowner away from a fixed place of business; a job "
            "that started from the homeowner's own call or a web form generally falls outside that cooling-off window, so reading the "
            f"written contract before signing matters more than counting on a right to cancel after the fact ({src('fs501-025', 'F.S. 501.025')}).</p>"),
        sec("What Belongs in a Written Scope Before Work Starts?",
            "<p>A number on its own, without the line items behind it, can't be compared to another bid. A complete scope spells out the "
            "area and layout, demolition and haul-off of anything being replaced, base material and compacted depth, slab thickness and "
            "strength, reinforcement type, joint spacing, finish, and whether sealing is included. On jobs over $2,500, Florida's lien "
            "law also requires a Notice of Commencement, recorded before work actually gets underway and personally signed by the property owner, a "
            f"document that protects both sides if a payment or lien dispute comes up later ({src('fs713-13', 'F.S. 713.13')}). "
            f"{post('how-to-compare-concrete-and-paver-quotes', 'Our guide to comparing concrete and paver quotes line by line')} walks "
            "through how to read two bids side by side once both are in hand.</p>"),
        sec("Say You're Comparing Bids for a Driveway Replacement in Winter Garden",
            f"<p>A homeowner in {city('winter-garden')} collecting three bids for a driveway tear-out and repour lines up each one "
            "against the same checklist: base depth and compaction method, slab thickness, control joint spacing, and who's handling the "
            "city's engineering permit for the work. The lowest number on the page often turns out to specify a thinner base or skip the "
            "haul-off fee, which only becomes clear once the three scopes sit side by side rather than being judged on price alone. "
            f"{a('/concrete-driveway-cost/', 'Our concrete driveway cost guide')} covers where Florida market pricing typically lands for "
            "a job that size.</p>"),
    ])
    faqs = [faq("Does a concrete driveway contractor need a state license in Florida?",
                "Not always. Florida law carves driveway installation out of state and local licensing requirements by name, though a permit can still be required. Structural concrete work tied to a foundation, footer or wall falls under a different state certificate, so the answer can shift once a job's scope goes beyond a stand-alone driveway."),
            faq("How do I check a concrete contractor's license in Florida?",
                "Run the business name through the DBPR license search, which shows active status and any discipline history. Since local licensing rules changed in 2025, it's also worth asking the specific county directly which local certificates, if any, it still issues for concrete work."),
            faq("What deposit is reasonable for a concrete driveway or patio job?",
                "Florida law treats a deposit over 10 percent of the contract price as a trigger point: the contractor then has 30 days to apply for permits and 90 days to start work once the permit issues. A payment schedule tied to completed stages, rather than one large upfront sum, is easier to check against actual progress."),
            faq("What should be in writing before a concrete contractor starts work in Orlando?",
                "Area and layout, demolition and haul-off, base material and compacted depth, slab thickness and strength, reinforcement, joint spacing, finish, and who's responsible for the permit. Once the contract price passes $2,500, Florida's lien law also requires a Notice of Commencement, recorded before the work actually gets underway."),
            faq("Who pulls the permit for a driveway replacement in Orange County?",
                "It depends on the specific city or whether the lot is in unincorporated Orange County, and the driveway apron in the right-of-way sometimes needs a separate permit from the rest of the driveway. Asking a contractor to state clearly who applies for what, before signing, avoids finding out mid-job that no one has.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/concrete-patios/", "Concrete patios"),
               ("/concrete-slabs/", "Concrete slabs"),
               ("/blog/florida-contractor-license-check-concrete-pavers/", "Checking a Florida contractor's license"),
               ("/blog/how-to-compare-concrete-and-paver-quotes/", "Comparing concrete and paver quotes")]
    return page("/blog/how-to-choose-a-concrete-contractor-orlando/", "post",
                "How to Choose a Concrete Contractor in Orlando",
                "How to choose a concrete contractor in Orlando: license rules, permits, deposits and what belongs in a written scope, as of October 2026.",
                "How to Choose a Concrete Contractor in Orlando: 10 Criteria to Check",
                capsule("Choosing a concrete contractor in Orlando comes down to ten checks: license and DBPR status, who pulls the "
                        "permit, deposit terms under Florida law, and a written scope covering base depth, thickness and joints. As of "
                        "October 2026, driveway installation itself is exempt from Florida licensing requirements, though a permit can "
                        "still be required across Orange, Osceola, Seminole and Lake counties."),
                body, faqs=faqs,
                sources=["fs489-117", "fac61g4-15-100", "dbpr-search", "fs489-126", "fs501-025", "fs713-13"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image=pid, form=False)


def p_how_to_choose_a_concrete_contractor_sarasota():
    pids = for_service("concrete-patios", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("How Do You Choose a Concrete Contractor in Sarasota and Bradenton?",
            f"<p>Hiring a {svc('concrete-patios', 'concrete')} contractor on the Suncoast involves the same state-level checks that "
            "apply anywhere in Florida, license status, permits, deposits and a written scope, plus two checks that matter more here "
            "than inland: Manatee County's own local licensing categories and whether the project needs architectural review from a "
            "deed-restricted community before a county permit will even move.</p>"),
        sec("Searching for the Best Concrete Contractor Near Lakewood Ranch or Venice? Start With the Paperwork.",
            "<p>A business that looks good in search results or review sites isn't the same thing as one whose paperwork is in order, "
            "and the paperwork is what protects a homeowner if a job goes sideways. The checklist below runs in roughly the order it "
            "matters, license and permit status first, design preferences last.</p>"
            + table("What to check before hiring a concrete contractor in Sarasota or Manatee County", ["Check", "Why it matters"],
                    [["DBPR license status", "Shows discipline history and whether a state license applies"],
                     ["Manatee or Sarasota County local certificate, if any", "Local licensing rules shifted in 2025; confirm directly with the county"],
                     ["Who applies for the county or city permit", "Sarasota and Manatee run separate permitting processes"],
                     ["License number printed on the bid or ad", "Required by state law on every offer, bid or advertisement"],
                     ["Deposit amount and its 10 percent trigger", "Over 10 percent starts a 30-day permit-filing clock under state law"],
                     ["Notice of Commencement on jobs over $2,500", "Required under Florida's lien law before work starts"],
                     ["Base depth and compaction method, in writing", "Flatwoods soils and a shallow water table make base work matter more here"],
                     ["Slab thickness, strength and joint spacing", "A price without these numbers can't be compared to another bid"],
                     ["ARC or HOA approval process, if the lot is deed-restricted", "Lakewood Ranch and many Manatee/Sarasota communities review before a permit can proceed"],
                     ["Insurance certificate, not a verbal claim alone", "Confirms coverage is current rather than assumed"]],
                    "General hiring checklist for the Sarasota unit's service area.")),
        sec("Does Manatee County License Concrete Contractors Differently Than the State?",
            "<p>Manatee County says on its own pages that it issues and reciprocates local licenses covering categories including "
            "\"Mason, Masonry and Concrete\" and a separate \"Concrete\" certificate, and that state-certified contractors have the "
            f"option of registering with the county as well ({ext('https://www.mymanatee.org/departments/development-services-department/building-division/contractor-licensing-division', 'Manatee County Contractor Licensing')}). "
            "That's on top of the statewide rule that driveway installation itself can't be made to require a state or local license by "
            f"name ({src('fs489-117', 'F.S. 489.117')}), while structural concrete tied to a footing, foundation or wall falls under the "
            f"state's structural masonry specialty contractor certificate ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). "
            "Sarasota County's own current licensing categories weren't something we could confirm from a page we could fetch directly, "
            f"so calling the county's building division is the reliable way to ask what applies to a specific job. The {src('dbpr-search', 'DBPR license search')} "
            "covers the state side of that question regardless of which county the job is in.</p>"
            + (photo(pid, "Close-up of gray stamped concrete patterned to resemble irregular hexagonal flagstone, a common patio finish on the Suncoast.") if pid else "")),
        sec("Does a Lakewood Ranch or Other Deed-Restricted Lot Need Approval Before a Permit?",
            f"<p>Often, yes, and the order matters. Since 2026, Florida law bars a homeowners' association from requiring a building "
            f"permit before it reviews a project's application, which means the architectural review and the county or city permit can "
            f"run at the same time rather than one being forced to wait on the other ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"{post('lakewood-ranch-arc-approval-hardscape', 'Our Lakewood Ranch ARC approval guide')} covers that community's "
            f"district-based process specifically, and {post('hoa-approval-for-pavers-and-concrete', 'our general HOA approval guide')} "
            "covers the paperwork for other deed-restricted communities across both service areas.</p>"),
        sec("What Should the Deposit and Contract Terms Look Like?",
            "<p>The same 10 percent deposit threshold that applies statewide applies here: once a deposit passes that mark, the "
            "contractor has 30 days to apply for permits and 90 days to start work after the permit issues, barring just cause or a "
            f"written extension agreed to by the homeowner ({src('fs489-126', 'F.S. 489.126')}). Once the contract price tops $2,500, a "
            f"Notice of Commencement has to be recorded before the crew breaks ground, personally signed by the property owner; a "
            f"contractor who brings this up is following standard practice, not raising a red flag ({src('fs713-13', 'F.S. 713.13')}). A three-day right to cancel under "
            "Florida's home-solicitation law generally doesn't apply once the homeowner is the one who requested the quote, so reading "
            f"the contract carefully before signing matters more than counting on a cooling-off period afterward ({src('fs501-025', 'F.S. 501.025')}).</p>"),
        sec("Say You're Getting Bids for a Pool Patio Extension in Venice",
            f"<p>A homeowner in {city('venice')} collecting bids for a concrete patio extension around an existing pool deck checks "
            "each contractor's base and compaction plan carefully, since the sandy coastal soil common along that stretch of Sarasota "
            "County behaves differently under a slab than firmer inland ground does. Each bid also gets checked against whether the "
            "property sits in a deed-restricted community that requires architectural review first, and whether the deposit requested "
            f"lines up with the 10 percent threshold that triggers Florida's permit-filing clock. {a('/concrete-patio-cost/', 'Our concrete patio cost guide')} "
            "breaks down where Florida market pricing typically lands for an extension that size.</p>"),
    ])
    faqs = [faq("Does Manatee County issue its own concrete contractor license?",
                "Manatee County's own pages describe local licenses covering categories including Mason, Masonry and Concrete, with state-certified contractors able to register as well. That's separate from the statewide rule that driveway installation itself can't be made to require a state or local license by name."),
            faq("Do I need HOA approval before a county permit in Lakewood Ranch?",
                "Often yes for a visible driveway, patio or pool-deck project. A 2026 change to Florida law keeps the association from demanding a permit in hand before it will even review the submission, so the architectural review and the county permit process can run on parallel tracks instead of one waiting on the other."),
            faq("How do I check a concrete contractor's license in Sarasota County?",
                "Start with the DBPR license search for the state side of the question, then call Sarasota County's building division directly, since the county's current local licensing categories after a 2025 state law change weren't confirmed from a page available to check."),
            faq("What deposit is reasonable for a concrete patio job on the Suncoast?",
                "The same statewide rule applies here: once a deposit passes 10 percent of the contract price, the contractor has 30 days to apply for permits and 90 days to start work once the permit issues, barring just cause or a written extension."),
            faq("Does a concrete contractor need to handle the Notice of Commencement?",
                "Once a contract passes $2,500, Florida's lien law requires a Notice of Commencement recorded before the crew breaks ground, and the property owner signs it personally rather than the contractor. Raising this as a required step is standard practice, not extra paperwork someone invented.")]
    related = [("/concrete-patios/", "Concrete patios"), ("/concrete-driveways/", "Concrete driveways"),
               ("/concrete-slabs/", "Concrete slabs"),
               ("/blog/lakewood-ranch-arc-approval-hardscape/", "Lakewood Ranch ARC approval"),
               ("/blog/saltwater-pools-and-coastal-salt-air-hardscape/", "Saltwater pools and salt air")]
    return page("/blog/how-to-choose-a-concrete-contractor-sarasota/", "post",
                "How to Choose a Concrete Contractor in Sarasota, FL",
                "How to choose a concrete contractor in Sarasota and Bradenton: Manatee County licensing, ARC approval, deposits and permits, October 2026.",
                "How to Choose a Concrete Contractor in Sarasota and Bradenton",
                capsule("Choosing a concrete contractor in Sarasota or Manatee County means checking DBPR and local license status, "
                        "who handles the permit, deposit terms under Florida law, and, on many lots, architectural review before a "
                        "permit can proceed. As of October 2026, Manatee County issues its own local licenses covering masonry and "
                        "concrete work alongside the statewide driveway licensing exemption."),
                body, faqs=faqs,
                sources=["fs489-117", "fac61g4-15-100", "dbpr-search", "fs489-126", "fs501-025", "fs713-13", "fs720-3035",
                         ("Manatee County Contractor Licensing Division", "https://www.mymanatee.org/departments/development-services-department/building-division/contractor-licensing-division")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-patios",
                image=pid, form=False)


def p_how_to_choose_a_paver_contractor_orlando():
    pids = for_service("paver-driveways", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("How Do You Choose a Paver Contractor in Orlando?",
            f"<p>A {svc('paver-driveways', 'paver')} installation lives or dies on what's underneath it, so the most useful questions "
            "for an Orlando-area paver contractor are about base depth, compaction and edge restraint, not just paver color and "
            "pattern. License status, permits and deposit terms matter here the same way they do for concrete, with a few "
            "paver-specific items added on top.</p>"),
        sec("What Should You Ask Before Hiring the Best Paver Installer Near You?",
            "<p>Reviews and photos show finished results, not what's buried under them, and a sunken or spreading paver field almost "
            "always traces back to a base or edge-restraint shortcut rather than the pavers themselves. The checklist below separates "
            "the paver-specific build questions from the general contractor paperwork every hardscape job in Florida should cover.</p>"
            + table("What to check before hiring a paver contractor in Orlando", ["Check", "Why it matters"],
                    [["Base depth in writing (6 in. minimum for a driveway)", "Industry construction standard; thinner bases shift and sink"],
                     ["Compaction target (98% standard Proctor)", "A base that looks solid on top can still be loose underneath"],
                     ["Edge restraint spec, not plastic landscape edging", "The single most common reason a paver field spreads at the edges"],
                     ["Paver thickness for the use (60 mm vs. 80 mm)", "Driveways carrying vehicles need a thicker unit than a patio"],
                     ["DBPR license status", "Covers discipline history; driveway work itself is license-exempt by statute"],
                     ["Who pulls any required permit", "Pavers aren't named in the state licensing exemption the way driveways are"],
                     ["Deposit amount and the 10 percent trigger", "Over 10 percent starts a 30-day permit-filing clock under state law"],
                     ["Notice of Commencement on jobs over $2,500", "Required under Florida's lien law before work starts"],
                     ["Written warranty terms on settling or sinking", "Spells out what's covered if a section settles after installation"],
                     ["HOA or ARC approval process handled in writing", "Most master-planned Orlando communities review paver color and pattern"]],
                    f"{src('icpi-ts2', 'ICPI Tech Spec 2')} and {src('icpi-ts3', 'ICPI Tech Spec 3')} set the industry base and edge-restraint standards referenced here.")),
        sec("Is Paver Installation License-Exempt the Same Way a Driveway Is?",
            f"<p>Not necessarily, and this is a question worth asking directly rather than assuming. Florida law names \"driveway or "
            "tennis court installation\" and \"decorative stone, tile, marble, granite, or terrazzo installation\" as job scopes that "
            f"can't be made to require a state or local license ({src('fs489-117', 'F.S. 489.117')}). Pavers and patios aren't named in "
            "that list by themselves, and whether a given paver job \"substantially corresponds\" to the state's structural masonry "
            f"specialty category is a judgment call the statute doesn't fully settle ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). "
            f"Running any contractor's name through the {src('dbpr-search', 'DBPR license search')} and asking directly which license, "
            "if any, covers the specific scope avoids relying on an assumption either way.</p>"
            + (photo(pid, "A herringbone-pattern paver driveway and walkway lead up to a modern Central Florida home.") if pid else "")),
        sec("What Base and Edge-Restraint Spec Should Be in Writing?",
            f"<p>A driveway built to the construction industry's own standard carries at least 6 inches of aggregate under it, packed "
            "down tight on soil that drains well, with 2 to 4 extra inches worked in wherever the ground tends to stay damp; the "
            "compaction target itself sits at 98 percent of standard Proctor density, a number a crew checks on site rather than "
            f"assumes once the surface looks firm ({src('icpi-ts2', 'ICPI Tech Spec 2')}). Edge restraint "
            "has to run the full perimeter of the field, anchored into the compacted base rather than the soil beneath it; a quote that "
            f"substitutes plastic landscape edging meant for flower beds is cutting a corner that shows up within a year or two as "
            f"spreading joints ({src('icpi-ts3', 'ICPI Tech Spec 3')}). Asking for both numbers on the written estimate, not just a "
            "verbal assurance, is the single most useful question on this list.</p>"),
        sec("How Do Permits, Deposits and Warranty Terms Work for Paver Jobs?",
            f"<p>A deposit over 10 percent of the contract price obligates a contractor to apply for any needed permit within 30 days "
            f"and start work within 90 days of the permit issuing, under the same statewide rule that covers every residential "
            f"contract regardless of licensure ({src('fs489-126', 'F.S. 489.126')}). Jobs over $2,500 call for a recorded Notice of "
            f"Commencement before work starts ({src('fs713-13', 'F.S. 713.13')}). A written warranty on paver settling, separate from "
            f"any manufacturer warranty on the units themselves, is worth asking for in writing rather than assuming it's included; "
            f"{post('concrete-and-paver-warranty-what-it-should-cover', 'our guide to what a paver warranty should cover')} goes into "
            "what a reasonable warranty typically addresses.</p>"),
        sec("Say You're Comparing Paver Driveway Bids in Clermont",
            f"<p>A homeowner in {city('clermont')} comparing three paver driveway bids lines each one up against base depth, "
            "compaction target and edge restraint before looking at price or pattern options, since those three items drive most of "
            "the difference between a driveway that holds up and one that sinks at the tire paths within a couple of seasons. Clermont "
            "sits on the Lake Wales Ridge, where excessively drained sand behaves differently under a base than the flatwoods soil "
            "common closer to Orlando, which is one more reason to ask each bidder what soil condition they found on a site visit "
            f"rather than quoting from an address alone. {a('/paver-driveway-cost/', 'Our paver driveway cost guide')} covers where "
            "Florida market pricing lands for a driveway that size.</p>"),
    ])
    faqs = [faq("What base depth should a paver driveway contractor use in Orlando?",
                "A minimum of 6 inches of aggregate, packed down on soil that drains well and built up another 2 to 4 inches where the ground tends to stay wet, following the industry's own construction standard. Getting that figure written on the estimate, along with the compaction target, is more useful than judging a bid on pattern or color alone."),
            faq("Does a paver contractor need a license in Florida?",
                "It depends on the scope. State law exempts driveway installation by name from licensing requirements, but pavers and patios aren't named the same way, and whether a given job falls under the state's structural masonry category is a judgment call the statute doesn't fully settle. Checking DBPR directly and asking the contractor is the reliable approach."),
            faq("Why does edge restraint matter so much on a paver driveway?",
                "Restraint locks the field at its perimeter so vehicle loads don't push the pavers apart over time, and it has to anchor into the compacted base rather than the soil beneath it. Substituting plastic landscape edging meant for flower beds is one of the most common reasons a paver field spreads and opens gapping joints within a year or two."),
            faq("What deposit is normal for a paver driveway job?",
                "Florida law treats a deposit over 10 percent of the contract price as a trigger: the contractor then has 30 days to apply for any needed permit and 90 days to start work once it issues. That rule applies to paver jobs the same way it applies to concrete."),
            faq("Should a paver warranty be separate from the manufacturer's warranty?",
                "Worth asking for, since a manufacturer's warranty on the paver units themselves doesn't necessarily cover settling from a base or edge-restraint issue, which is a workmanship question rather than a product defect. Getting both terms in writing avoids confusion if a section needs re-leveling later.")]
    related = [("/paver-driveways/", "Paver driveways"), ("/paver-patios/", "Paver patios & walkways"),
               ("/pool-deck-pavers/", "Pool deck pavers"),
               ("/blog/paver-installation-process-florida/", "How pavers are installed in Florida"),
               ("/blog/concrete-and-paver-warranty-what-it-should-cover/", "What a paver warranty should cover")]
    return page("/blog/how-to-choose-a-paver-contractor-orlando/", "post",
                "Choosing a Paver Contractor in Orlando, FL",
                "How to choose a paver contractor in Orlando: base depth, edge restraint, licensing, permits and warranty terms to check, as of October 2026.",
                "How to Choose a Paver Contractor in Orlando",
                capsule("Choosing a paver contractor in Orlando means checking base depth (at least 6 in. compacted), compaction "
                        "target, and edge restraint in writing before judging pattern or price. As of October 2026, paver installation "
                        "isn't license-exempt the same clear way a driveway is under Florida law, so confirming license status through "
                        "DBPR is worth doing directly."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts3", "fs489-117", "fac61g4-15-100", "dbpr-search", "fs489-126", "fs713-13"],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-driveways",
                image=pid, form=False)


def p_how_to_choose_a_paver_contractor_sarasota():
    pids = for_service("pool-deck-pavers", 1)
    pid = pids[0] if pids else None
    body = "".join([
        sec("How Do You Choose a Paver Contractor in Sarasota and Lakewood Ranch?",
            f"<p>A {svc('pool-deck-pavers', 'paver')} contractor on the Suncoast gets judged on the same base-and-restraint "
            "fundamentals as anywhere else in Florida, plus two things that matter more on the coast: how a quote handles a "
            "saltwater pool deck or travertine, and whether a Lakewood Ranch or other deed-restricted lot needs architectural "
            "sign-off before the paperwork can move.</p>"),
        sec("What Should You Ask the Best Paver Company Near Sarasota or Bradenton?",
            "<p>A quote that only lists paver color and pattern is missing most of what actually determines whether the installation "
            "holds up. The checklist below adds the coastal- and travertine-specific items to the same base, permit and deposit "
            "fundamentals every Florida paver job should cover.</p>"
            + table("What to check before hiring a paver contractor in Sarasota or Manatee County", ["Check", "Why it matters"],
                    [["Base depth in writing (6 in. minimum for a driveway)", "Industry construction standard; coastal sand drains differently than inland soil"],
                     ["Compaction target (98% standard Proctor)", "A base that looks solid on top can still be loose underneath"],
                     ["Edge restraint spec, not plastic landscape edging", "Spreading joints are the most common early failure on a paver field"],
                     ["Sealing and rinsing plan for a saltwater pool deck", "Salt spray and splash-out accelerate wear on an unsealed surface"],
                     ["Travertine or shell stone handling, if chosen", "A different sealing and joint approach than concrete pavers"],
                     ["DBPR license status", "Covers discipline history across any Florida county"],
                     ["Manatee or Sarasota County local certificate, if any", "Confirm directly with the county given the 2025 licensing changes"],
                     ["ARC approval process for Lakewood Ranch or other districts", "Village-level architectural review runs ahead of some county permits"],
                     ["Deposit amount and the 10 percent trigger", "Over 10 percent starts a 30-day permit-filing clock under state law"],
                     ["Written warranty terms on settling or sinking", "Spells out what's covered if a section needs re-leveling"]],
                    f"{src('icpi-ts2', 'ICPI Tech Spec 2')} sets the base and compaction standard referenced here.")),
        sec("Does a Paver Driveway or Pool Deck Installer Need a License in Sarasota or Manatee?",
            f"<p>It depends on the scope, the same as anywhere in Florida. Driveway installation itself can't be made to require a "
            f"state or local license by name ({src('fs489-117', 'F.S. 489.117')}), but pavers and patios aren't named in that "
            "exemption the way driveways are, and whether a specific paver job falls under the state's structural masonry category is "
            f"a judgment call the statute leaves open ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). Manatee County's "
            "own pages describe local licenses covering masonry and concrete categories, with state-certified contractors able to "
            f"register as well ({ext('https://www.mymanatee.org/services-and-amenities/service-listing/service-details/contractor-licensing', 'Manatee County, Register Your Contractor License')}); "
            f"Sarasota County's current categories weren't confirmed from a page we could fetch directly, so a call to the county "
            f"building division settles it faster than guessing. The {src('dbpr-search', 'DBPR license search')} covers the state side "
            "either way.</p>"
            + (photo(pid, "A paver pool deck with wicker furniture and a linear fire pit sits beside palm trees near the water.") if pid else "")),
        sec("What Changes About a Paver Quote for a Saltwater Pool or Travertine Deck?",
            "<p>Salt spray and splash-out off a saltwater pool wear on an unsealed surface faster than fresh water does, so a quote for "
            "deck work in Siesta Key, Longboat Key or Anna Maria Island conditions should spell out a sealing and rinsing plan rather "
            f"than treat it as an afterthought. Travertine and other natural stone pavers take a different sealing approach than "
            "concrete pavers, since the stone's pitted surface and softer finish hold water and salt differently than a manufactured "
            f"unit. {post('saltwater-pools-and-coastal-salt-air-hardscape', 'Our saltwater pools and salt-air guide')} and "
            f"{post('travertine-pool-deck-care', 'our travertine pool deck care guide')} go deeper into both materials than fits in a "
            "hiring checklist.</p>"),
        sec("What About ARC Approval and Deposit Terms on a Deed-Restricted Lot?",
            f"<p>Lakewood Ranch and many other Sarasota- and Manatee-area communities review paver color, pattern and material before "
            f"a county permit can move forward. A 2026 change to state law keeps an HOA from insisting on a permit in hand before that "
            f"review happens, so the two processes can proceed together rather than one waiting on the other ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"{post('lakewood-ranch-arc-approval-hardscape', 'Our Lakewood Ranch ARC guide')} covers that district's specific process. "
            f"On the money side, a deposit over 10 percent of the contract price starts the same 30-day permit-filing clock that "
            f"applies to any Florida residential contract ({src('fs489-126', 'F.S. 489.126')}), and once the price passes $2,500 a "
            f"Notice of Commencement has to be recorded before the crew breaks ground ({src('fs713-13', 'F.S. 713.13')}).</p>"),
        sec("Say You're Hiring for a Travertine Pool Deck in Bradenton",
            f"<p>A homeowner in {city('bradenton')} getting quotes for a travertine pool deck around a saltwater pool checks each "
            "bid's sealing plan and joint-sand approach specifically, since those details matter more to a travertine deck's long-term "
            "look than the stone pattern chosen up front. The same base, permit and deposit checklist that applies to any Manatee "
            "County paver job still applies underneath the travertine; the coastal-specific questions sit on top of it rather than "
            f"replacing it. {a('/pool-deck-cost/', 'Our pool deck cost guide')} covers where Florida market pricing lands for a "
            "travertine deck of a given size, and asking two or three bidders for the same square footage and the same travertine "
            "grade keeps the comparison honest rather than pricing different stone against each other by accident.</p>"),
    ])
    faqs = [faq("Does Manatee County license paver installers differently than the state?",
                "Manatee County's own pages describe local licenses covering masonry and concrete categories, with state-certified contractors able to register as well. That's separate from the statewide question of whether a specific paver job falls under Florida's license-exempt driveway category or the structural masonry category."),
            faq("What should a paver quote for a saltwater pool deck include?",
                "A sealing and rinsing plan specific to the salt exposure, since salt spray and splash-out wear on an unsealed surface faster than fresh water does. Travertine and other natural stone also take a different sealing approach than concrete pavers, which a complete quote should address separately."),
            faq("Does Lakewood Ranch require ARC approval before a paver permit?",
                "Often yes. A 2026 change to Florida law keeps the association from demanding a building permit in hand before it will review the project, so the architectural review and the county permit can proceed together. Lakewood Ranch's district-based review process is worth confirming with the specific village's association."),
            faq("What base depth should a paver driveway have on the Suncoast?",
                "A minimum of 6 inches of aggregate packed over soil that drains well, with extra depth worked in where the ground tends to stay wet, following the same industry construction standard used statewide. Coastal sand can behave differently under a base than inland soil, which is one more reason to ask what a contractor found during a site visit rather than assuming."),
            faq("What deposit is normal for a paver job in Sarasota or Manatee County?",
                "The same statewide rule applies here: a deposit over 10 percent of the contract price obligates the contractor to apply for any needed permit within 30 days and start work within 90 days of it issuing.")]
    related = [("/pool-deck-pavers/", "Pool deck pavers"), ("/paver-patios/", "Paver patios & walkways"),
               ("/paver-driveways/", "Paver driveways"),
               ("/blog/saltwater-pools-and-coastal-salt-air-hardscape/", "Saltwater pools and salt air"),
               ("/blog/lakewood-ranch-arc-approval-hardscape/", "Lakewood Ranch ARC approval")]
    return page("/blog/how-to-choose-a-paver-contractor-sarasota/", "post",
                "Choosing a Paver Contractor in Sarasota, FL",
                "How to choose a paver contractor in Sarasota and Lakewood Ranch: base depth, saltwater pool decks, ARC approval and licensing, October 2026.",
                "How to Choose a Paver Contractor in Sarasota and Lakewood Ranch",
                capsule("Choosing a paver contractor in Sarasota or Manatee County starts with base depth, compaction and edge "
                        "restraint in writing, then adds coastal checks: a sealing plan for a saltwater pool deck and ARC approval for "
                        "a Lakewood Ranch lot. As of October 2026, Manatee County still issues its own local masonry and concrete "
                        "licenses alongside the statewide rules."),
                body, faqs=faqs,
                sources=["icpi-ts2", "fs489-117", "fac61g4-15-100", "dbpr-search", "fs489-126", "fs713-13", "fs720-3035",
                         ("Manatee County, Register Your Contractor License", "https://www.mymanatee.org/services-and-amenities/service-listing/service-details/contractor-licensing")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="pool-deck-pavers",
                image=pid, form=False)


def get_pages():
    return [p_prepare_your_yard_for_hardscape_installation(), p_best_time_of_year_for_hardscape_projects_florida(),
            p_how_to_choose_a_concrete_contractor_orlando(), p_how_to_choose_a_concrete_contractor_sarasota(),
            p_how_to_choose_a_paver_contractor_orlando(), p_how_to_choose_a_paver_contractor_sarasota()]
