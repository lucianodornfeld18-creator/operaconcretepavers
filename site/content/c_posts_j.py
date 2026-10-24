# -*- coding: utf-8 -*-
"""Blog posts, group j: the two general-planning posts (preparing a yard for installation day, choosing
the right season). The four hiring-guide posts that used to live here were removed on 2026-10-23 and 301 to
/blog/how-to-compare-concrete-and-paver-quotes/ (see build.write_headers)."""
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


def get_pages():
    return [p_prepare_your_yard_for_hardscape_installation(), p_best_time_of_year_for_hardscape_projects_florida()]
