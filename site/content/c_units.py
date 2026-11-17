# -*- coding: utf-8 -*-
"""The two service-unit pages: /central-florida/ (Kissimmee & Greater Orlando crew) and /sarasota-manatee/ (Sarasota crew).
Each page is the entity page its Google Business Profile links to: brand + place + phone + counties + services."""
from _data import SERVICES
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, cs, post, src, tel, price, per
from _photos import for_service

ORLANDO_PID = (for_service("concrete-driveways", 1) or [None])[0]
SARASOTA_PID = (for_service("pool-deck-pavers", 1) or [None])[0]

ORLANDO_TOWNS = ["orlando", "kissimmee", "clermont", "oviedo", "winter-garden", "windermere"]
SARASOTA_TOWNS = ["sarasota", "lakewood-ranch", "bradenton", "venice"]
TABLE_SERVICES = ["paver-patios", "pool-deck-pavers", "paver-sealing", "concrete-driveways"]


def _service_table(caption, towns, note):
    headers = ["Town"] + [SERVICES[s]["name"] for s in TABLE_SERVICES]
    rows = [[city(slug)] + [cs(slug, s) for s in TABLE_SERVICES] for slug in towns]
    return table(caption, headers, rows, note)


def central_florida():
    contact_block = ul([
        "<strong>Business name:</strong> Opera Concrete &amp; Pavers",
        "<strong>Unit:</strong> Kissimmee &amp; Greater Orlando",
        "<strong>Based in:</strong> Kissimmee, FL (a service-area business: no storefront and no street address, the crew comes to your property)",
        f"<strong>Phone:</strong> {tel('orlando')}",
        "<strong>Counties served:</strong> Orange, Osceola, Seminole, Lake and Polk",
        f"<strong>Main towns:</strong> {city('kissimmee')}, {city('orlando')}, {city('clermont')}, {city('oviedo')}, {city('winter-garden')} and {city('windermere')}",
        "<strong>What we do:</strong> pavers first (driveways, patios, pool decks), paver sealing and paver restoration, then concrete and artificial turf",
        "<strong>Estimates:</strong> free, on site",
    ])
    body = "".join([
        sec("Contact this crew",
            contact_block + "<p>Calls go straight to the Kissimmee &amp; Greater Orlando crew. If the project is on the Gulf side, the "
            f"{a('/sarasota-manatee/', 'Sarasota crew')} has its own line.</p>", sid="contact-crew"),
        sec("What this crew builds and repairs",
            f"<p>Pavers are the center of the work here. That means {svc('paver-driveways', 'paver driveways')}, {svc('paver-patios', 'paver patios and walkways')} and {svc('pool-deck-pavers', 'pool deck pavers')}, "
            f"including travertine. Next to new installs, the crew does the upkeep that keeps a paver surface looking right: {svc('paver-sealing', 'paver cleaning and sealing')} and {svc('paver-restoration', 'paver restoration')}, "
            "which covers deep cleaning, stripping a failed sealer, releveling sunken spots, swapping cracked units and re-filling the joints.</p>"
            f"<p>Poured work comes after that: {svc('concrete-driveways', 'concrete driveways')}, {svc('concrete-patios', 'patios')}, {svc('stamped-concrete', 'stamped concrete')}, {svc('concrete-slabs', 'slabs')} and {svc('concrete-repair', 'repair and resurfacing')}. "
            f"The crew also lays {svc('artificial-turf', 'artificial turf')} and builds {svc('retaining-walls', 'segmental retaining walls')}. "
            f"Around Kissimmee the most common paver questions are about {cs('kissimmee', 'paver-sealing', 'sealing in Kissimmee')} and {cs('kissimmee', 'paver-restoration', 'restoring tired pavers in Kissimmee')}; "
            f"in town and in the northern suburbs they come up as {cs('orlando', 'paver-restoration', 'paver restoration in Orlando')}.</p>"
            + table("Central Florida market ranges, pavers first (not a quote)", ["Service", "Market range", "Unit"],
                    [[svc("paver-sealing", "Paver cleaning, re-sanding and sealing"), price("paver-sealing"), per("paver-sealing")],
                     [svc("paver-restoration", "Paver restoration (releveling, repairs)"), price("paver-restoration"), per("paver-restoration")],
                     [svc("pool-deck-pavers", "Pool deck pavers, installed"), price("pool-deck-pavers"), per("pool-deck-pavers")]],
                    "Ranges as of October 2026, drawn from installer price lists and national cost guides. Price tracks demolition, drainage and approvals rather than the ZIP code.")),
        sec("Paver sealing and restoration: when a surface needs which",
            "<p>Sealing is for pavers that are sound but dull, stained or losing sand from the joints. The surface gets washed, the joints get re-filled and a sealer goes on. Restoration is for pavers that have moved: a dip where the base settled, "
            "a corner that rocks, a puddle that never drains. Sealer can't fix any of that, because the problem sits under the surface.</p>"
            f"<p>On timing, the industry guide doesn't give a number of years. ICPI's Tech Spec 5 says sealers need re-coating after a period of wear and weather, and acrylics generally last a few years ({src('icpi-ts5', 'ICPI Tech Spec 5')}). "
            "So we look at the surface rather than a calendar: water that no longer beads, joint sand washed out after a summer of storms, or color that has faded unevenly. "
            "That same guide notes that a whitish bloom called efflorescence can appear within about 60 days of an install and doesn't hurt the pavement's structure, so a fresh patio with a white haze isn't automatically a defect.</p>"),
        sec("What changes when you build in Central Florida",
            "<p>The ground under a Clermont driveway and the ground under a Kissimmee driveway are not the same. Lake County's ridge towns sit on Candler and Astatula sand, drained so well that the water table lies below 80 inches "
            f"({src('nrcs-candler-osd', 'NRCS, Candler series')}). Through Orlando, Kissimmee and St. Cloud the common series are Myakka, Smyrna and Pomona, where water can stand within a foot and a half of the surface part of the year "
            f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). ICPI's driveway spec starts at 6 inches of compacted aggregate on well-drained ground and adds 2 to 4 inches where the soil stays wet "
            f"({src('icpi-ts2', 'ICPI Tech Spec 2')}), so two paver bases a few miles apart can legitimately differ by a third.</p>"
            f"<p>Rain and heat set the calendar. Orlando International averages 51.45 inches a year, most of it from late May to mid-October ({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}), which is why "
            f"{post('pouring-concrete-in-florida-rainy-season', 'rainy-season concrete work')} starts at sunrise. "
            f"Orange County also appears on the Florida Senate's list of eleven counties holding most sinkhole claims ({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}); a sunken paver field is far more often a washed-out base than a geological event, and "
            f"{post('sinkholes-and-settlement-central-florida', 'this guide to settlement')} explains how to tell the difference.</p>"),
        sec("Permits: who handles what in Osceola, Orange and the rest",
            "<p>The apron where a driveway meets the street is public right-of-way, and nearly every office here wants a permit for it. Beyond the apron the answers split. "
            "The City of Kissimmee runs driveway permits through the engineering division's online system, while Osceola County caps a residential driveway at 24 feet wide unless a conditional use is approved. "
            "Unincorporated Orange County treats residential pavers as a zoning permit rather than a building permit.</p>"
            + table("Where to call before the work starts (checked October 2026)", ["Jurisdiction", "What it asks for", "Desk"],
                    [["City of Kissimmee", "Driveway or sidewalk permit, filed online", "407-518-2278"],
                     ["Osceola County", "Driveway permit; 24 ft width limit without conditional use", "407-742-0200"],
                     ["City of Orlando", "Engineering permit, pavers included", "407-246-2271"],
                     ["Orange County (unincorporated)", "Zoning permit for pavers", "407-836-5550"],
                     ["City of Clermont", "Zoning approval for a driveway", "352-394-4081"]],
                    "Phone numbers belong to each government office, not to us. HB 803 (effective July 1, 2026) removes the single-family building permit below $7,500 but leaves zoning, engineering and right-of-way reviews in place.")
            + f"<p>Per-county detail lives in the posts on {post('osceola-county-kissimmee-st-cloud-permits', 'Osceola County and Kissimmee')}, {post('orange-county-orlando-driveway-patio-permits', 'Orange County and Orlando')} and "
            f"{post('lake-and-polk-county-driveway-permits', 'Lake and Polk counties')}, and the {a('/permits/', 'permits and HOA hub')} covers the full list.</p>"),
        sec("HOA and architectural review in this region",
            "<p>Many neighborhoods here answer to an architectural board before the city ever sees the plan. Baldwin Park's review committee meets twice a month and takes at most 25 applications per meeting; "
            f"its guidelines hold a front driveway to the width of the garage door ({src('bp-network', 'Baldwin Park Network, ROA/ARC')}; {src('bp-guidelines', 'Baldwin Park Residential Guidelines, 2024')}). "
            f"Lake Nona's Laureate Park wants its board's sign-off on any improvement, sent by email ahead of time ({src('laureatepark-faq', 'Laureate Park HOA FAQ')}), and "
            f"Celebration's committee works from a monthly posted deadline ({src('celebration-arc', 'Celebration, Architectural Review Committee')}). "
            f"Florida law now stops an association from demanding a building permit before it reviews your request ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"The step-by-step version is in {post('hoa-approval-for-pavers-and-concrete', 'this HOA approval guide')}.</p>"),
        sec("How an estimate works",
            f"<p>You call {tel('orlando')} or send the form with your address and a few photos. We schedule a visit, measure, check the slope, the soil and where the water goes, and note the HOA or permit questions. "
            f"The written scope that follows lists base depth, paver type and pattern, joints, sealer, permits and cleanup, so two bids can be compared line by line. The full sequence is on the {a('/process/', 'process page')}; "
            f"{post('how-to-compare-concrete-and-paver-quotes', 'comparing quotes')} shows what to check in anyone's bid. Visits and estimates are free.</p>"),
        sec("Services in the main Kissimmee and Orlando-area towns",
            "<p>Each of the six towns below has its own page for pavers, sealing and concrete. The list underneath it covers every other town the crew reaches, by county.</p>"
            + _service_table("Pavers, sealing and concrete by town", ORLANDO_TOWNS,
                             "Smaller towns nearby use the county-level permit and soil notes above.")
            + "<!--AUTO:unit-cities-->"),
    ])
    faqs = [
        faq("Where is the Kissimmee & Greater Orlando crew based?",
            "In Kissimmee, Florida. It's a service-area business with no storefront or street address, so the crew drives to your property. The Google Business Profile for this unit is set in Kissimmee, and the same crew covers Orange, Osceola, Seminole, Lake and Polk counties."),
        faq("Do you work in Celebration, Poinciana, Lake Nona or Windermere?",
            f"Yes. {city('celebration')} and {city('poinciana')} are in Osceola County, {city('lake-nona')} and {city('windermere')} in Orange. Each has a page here with its own permit and HOA notes. If your community isn't listed, call {tel('orlando')} and ask."),
        faq("Who pulls the permit in Osceola County versus Orange County?",
            "We pull a permit when the work requires one. The offices differ: Osceola County issues a driveway permit with a 24-foot width limit for unincorporated lots, while unincorporated Orange County treats residential pavers as a zoning permit. A city address follows its own desk."),
        faq("My HOA wants plans first. Can you help with that?",
            "Yes. Associations like Baldwin Park, Laureate Park and Celebration each have their own review steps and deadlines. We can supply the dimensions, material and color the application asks for, and the approval comes from the association's board."),
        faq("Is my paver driveway too far gone to just seal?",
            "If the surface is level and only faded or stained, cleaning and sealing is the right call. If sections have sunk, rock underfoot or hold standing water, the base has moved, and restoration (lifting, re-compacting, relaying) comes before any sealer."),
        faq("Does the Kissimmee crew also work on the Gulf coast?",
            f"No, that's the other crew. Sarasota and Manatee counties are handled by the {a('/sarasota-manatee/', 'Sarasota crew')}, which has its own phone line and knows that coast's salt air and water table."),
    ]
    return page("/central-florida/", "unit", "Opera Concrete & Pavers – Kissimmee & Orlando, FL",
                "Opera Concrete & Pavers, based in Kissimmee, FL. Pavers, sealing, restoration, concrete and turf in Orange, Osceola, Seminole, Lake and Polk. (689) 354-0025.",
                "Kissimmee & Greater Orlando: pavers, paver sealing and concrete",
                capsule("Opera Concrete & Pavers' Kissimmee & Greater Orlando crew is based in Kissimmee, FL and answers at (689) 354-0025. "
                        "As of November 2026 it installs pavers, seals and restores them, and pours concrete and lays artificial turf across Orange, Osceola, Seminole, Lake and Polk counties, with free on-site estimates."),
                body, faqs=faqs, crumbs=[("Service areas", "/service-areas/")], unit="orlando",
                related=[("/sarasota-manatee/", "The Sarasota crew"), ("/kissimmee-fl/", "Kissimmee, FL"), ("/pavers/", "Pavers and turf overview"), ("/permits/", "Permits and HOA hub")],
                hero_photo=ORLANDO_PID, eyebrow="Kissimmee & Greater Orlando",
                sources=["icpi-ts2", "icpi-ts5", "nrcs-candler-osd", "nrcs-myakka-osd", "nrcs-smyrna-osd", "nrcs-pomona-osd", "nrcs-astatula-osd", "ncei-annual-prcp", "fl-senate-2011-104",
                         "kissimmee-driveway-sidewalk", "osceola-parking-ord", "orange-residential-pavers", "orlando-engineering-permit", "clermont-permit-types",
                         "bp-network", "bp-guidelines", "laureatepark-faq", "celebration-arc", "fs720-3035"])


def sarasota_manatee():
    contact_block = ul([
        "<strong>Business name:</strong> Opera Concrete &amp; Pavers",
        "<strong>Unit:</strong> Sarasota, Lakewood Ranch &amp; Bradenton",
        "<strong>Based in:</strong> Sarasota, FL (a service-area business: no storefront and no street address, the crew comes to your property)",
        f"<strong>Phone:</strong> {tel('sarasota')}",
        "<strong>Counties served:</strong> Sarasota and Manatee",
        f"<strong>Main towns:</strong> {city('sarasota')}, {city('lakewood-ranch')}, {city('bradenton')} and {city('venice')}",
        "<strong>What we do:</strong> pavers first (driveways, patios, pool decks), paver sealing and paver restoration, then concrete and artificial turf",
        "<strong>Estimates:</strong> free, on site",
    ])
    body = "".join([
        sec("Contact this crew",
            contact_block + "<p>Calls go straight to the Sarasota crew. A project in Orlando, Kissimmee or elsewhere inland goes to the "
            f"{a('/central-florida/', 'Kissimmee &amp; Greater Orlando crew')} instead.</p>", sid="contact-crew"),
        sec("What this crew builds and repairs",
            f"<p>On the Suncoast the work starts with pavers: {svc('paver-driveways', 'paver driveways')}, {svc('paver-patios', 'paver patios and walkways')} and {svc('pool-deck-pavers', 'pool deck pavers')}, "
            f"with travertine and other stone for decks. The same crew handles {svc('paver-sealing', 'paver cleaning and sealing')} and {svc('paver-restoration', 'paver restoration')}, "
            "meaning stripping a worn sealer, lifting and relaying settled areas, replacing broken units and re-sanding the joints.</p>"
            f"<p>After pavers come {svc('concrete-driveways', 'concrete driveways')}, {svc('concrete-pool-decks', 'concrete pool decks')}, {svc('concrete-walkways', 'walkways')}, {svc('stamped-concrete', 'stamped concrete')} and {svc('concrete-repair', 'concrete repair')}, "
            f"plus {svc('artificial-turf', 'artificial turf')} and {svc('retaining-walls', 'retaining walls')}. "
            f"Homeowners in Sarasota proper usually ask about {cs('sarasota', 'paver-sealing', 'sealing pavers in Sarasota')} and {cs('sarasota', 'paver-restoration', 'restoring pavers in Sarasota')}; "
            f"east in the master-planned communities the same requests show up as {cs('lakewood-ranch', 'paver-restoration', 'paver restoration in Lakewood Ranch')}.</p>"
            + table("Suncoast market ranges, pavers first (not a quote)", ["Service", "Market range", "Unit"],
                    [[svc("paver-sealing", "Paver cleaning, re-sanding and sealing"), price("paver-sealing"), per("paver-sealing")],
                     [svc("paver-restoration", "Paver restoration (releveling, repairs)"), price("paver-restoration"), per("paver-restoration")],
                     [svc("pool-deck-pavers", "Pool deck pavers, installed"), price("pool-deck-pavers"), per("pool-deck-pavers")]],
                    "Ranges as of October 2026, drawn from installer price lists and national cost guides. Access, drainage and approvals move a final number more than the town does, so the written quote comes after the visit.")),
        sec("Sealing near salt water, and when pavers need restoring instead",
            "<p>Gulf air and pool chemistry are hard on a paver surface, and a coastal patio tends to show it sooner than an inland one. A sealer slows staining and keeps joint sand in place; it won't level a field that has dropped. "
            "When the surface is flat and only dull, wash, re-sand and seal. When it dips, rocks or pools water, the base needs attention first, and restoration is the job.</p>"
            f"<p>The paver industry's own guide gives no fixed interval for re-coating; it says sealers need renewing after a period of wear and weather ({src('icpi-ts5', 'ICPI Tech Spec 5')}). "
            f"Near the water we inspect more often and judge by what the surface is doing. {post('saltwater-pools-and-coastal-salt-air-hardscape', 'This post on salt air and saltwater pools')} covers the coastal upkeep in more detail.</p>"),
        sec("What changes when you build around Sarasota and Manatee",
            "<p>Nearly every lot in both counties is flatwoods sand with groundwater close to the surface. EauGallie and Immokalee, the two most common series, hold a seasonal high water table within about 6 to 18 inches "
            f"({src('nrcs-eaugallie-osd', 'NRCS, EauGallie series')}; {src('nrcs-immokalee-osd', 'NRCS, Immokalee series')}), and Felda holds water within a foot for part of the year ({src('nrcs-felda-osd', 'NRCS, Felda series')}). "
            f"For pavers that points to the thicker end of ICPI's range: 6 inches of compacted aggregate as the starting point, with 2 to 4 inches added where the soil stays wet ({src('icpi-ts2', 'ICPI Tech Spec 2')}).</p>"
            "<p>The coast adds layers. FEMA's Zone AE marks at least a 1-percent annual flood chance, and Zone VE adds wave action strong enough to damage structures "
            f"({src('fema-coastal-firm', 'FEMA, Coastal FIRM features')}). Building seaward of the state's Coastal Construction Control Line needs a DEP permit on top of local approvals, and Sarasota County keeps its own Gulf Beach Setback Line "
            f"({src('fdep-cccl-program', 'FDEP CCCL Program')}; {src('sarasota-county-54-723-gbsl', 'Sarasota County Code §54-723')}). Siesta Key, Longboat Key and Anna Maria Island are where those lines come up most.</p>"
            "<p>Rain is similar on both sides of the state. The Sarasota–Bradenton airport normal is 49.05 inches a year "
            f"({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}), concentrated between late May and mid-October. Watering rules are tighter than usual right now: the Southwest Florida Water Management District has both counties under a once-a-week order through March 31, 2027 "
            f"({src('swfwmd-restrictions', 'SWFWMD District Water Restrictions')}), one reason {post('artificial-turf-water-savings-florida', 'turf versus sod')} is a live question.</p>"),
        sec("Permits: Sarasota County, Manatee County and the cities",
            "<p>As on the other coast, the driveway apron needs a right-of-way permit almost everywhere. Patios and pavers on private ground range from exempt to a zoning review, depending on which office has the address.</p>"
            + table("Where to call before the work starts (checked October 2026)", ["Jurisdiction", "What it asks for", "Desk"],
                    [["City of Sarasota", "City engineer permit to cut a curb or build a driveway", "(941) 263-6494"],
                     ["Sarasota County", "Right-of-Way Use Permit for the apron", "941-861-5000"],
                     ["City of Venice", "Right-of-way use permit before any work in the right-of-way", "941-882-7547"],
                     ["Manatee County", "Access and Drainage permit; non-structural paver patios are on its no-permit list", "311"],
                     ["City of Bradenton", "Public Works approval and a zoning permit for paved areas", "(941) 932-9414"]],
                    "These numbers belong to each government office. HB 803 waives only the single-family building permit for work under $7,500 and doesn't touch right-of-way, zoning or engineering reviews.")
            + f"<p>Detail and statute citations: {post('sarasota-county-driveway-patio-permits', 'Sarasota, Venice and North Port permits')}, {post('manatee-county-driveway-permits', 'Manatee County, Bradenton and Parrish permits')} and the {a('/permits/', 'permits and HOA hub')}.</p>"),
        sec("HOAs and architectural approvals in Lakewood Ranch and beyond",
            "<p>Lakewood Ranch generates the most paperwork questions. In the Country Club and Edgewater villages, a Modification Request Form has to be approved before a homeowner reseals, repaints or changes the material of a driveway or walkway, "
            f"and the manual lists approved sealer colors ({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual')}). "
            f"In North Venice, the Venetian Golf &amp; River Club's committee takes applications until noon on the last Monday of the month ({src('venetian-acc-app', 'Venetian Golf & River Club POA, ACC Application')}), and "
            f"Palmer Ranch leaves architectural review to its individual neighborhoods ({src('palmerranch', 'Palmer Ranch Master Association')}). "
            f"State law bars an HOA from requiring a building permit before it reviews your request ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"{post('lakewood-ranch-arc-approval-hardscape', 'This Lakewood Ranch ARC guide')} walks through the steps.</p>"),
        sec("How an estimate works",
            f"<p>Call {tel('sarasota')} or use the form with the address and a few photos. The crew visits, measures, checks slope, soil and drainage, and flags permit and HOA questions on the spot. "
            f"The written scope lists base depth, paver type, joint material, sealer, approvals and cleanup, and is built so it can sit next to another bid. See the {a('/process/', 'six-step process')} for the whole sequence. "
            "Estimates are free.</p>"),
        sec("Services in the main Sarasota-area towns",
            "<p>The four towns below each have their own page for pavers, sealing and concrete. Below them, every other town the crew reaches is listed by county.</p>"
            + _service_table("Pavers, sealing and concrete by town", SARASOTA_TOWNS,
                             "Nearby towns in the same county use the county-level permit and soil notes above.")
            + "<!--AUTO:unit-cities-->"),
    ])
    faqs = [
        faq("Where is the Sarasota crew based?",
            "In Sarasota, Florida. It's a service-area business with no storefront or street address, so the crew comes to you. The unit's Google Business Profile is set in Sarasota, and the crew covers Sarasota and Manatee counties."),
        faq("Do you work in Lakewood Ranch, Venice, North Port and the islands?",
            f"Yes. {city('lakewood-ranch')} straddles the Sarasota–Manatee line, {city('venice')} and {city('north-port')} are in Sarasota County, and {city('siesta-key')}, {city('longboat-key')} and {city('anna-maria-island')} are covered too. For a town that isn't listed, call {tel('sarasota')} and ask."),
        faq("Does sealing matter more near the Gulf?",
            "Salt air, pool chemicals and a high water table are tough on a paver surface, so coastal owners often check theirs more often. There's no fixed re-seal date in the industry guide, so we judge by the surface: water no longer beading, joint sand gone, color fading unevenly."),
        faq("Do I need approval before changing a Lakewood Ranch driveway?",
            "In the Country Club and Edgewater villages, yes. A Modification Request Form comes first for sealing, repainting or overlaying a driveway or walkway. We can supply dimensions and materials for it; the association decides."),
        faq("Do pavers near the beach need a state permit?",
            "Seaward of the Coastal Construction Control Line, a DEP permit applies in addition to local approvals, and Sarasota County has its own Gulf Beach Setback Line on county beaches. We'll tell you at the visit if your lot falls near either line."),
        faq("Does the Sarasota crew also work in Orlando?",
            f"No. Central Florida jobs go to the {a('/central-florida/', 'Kissimmee &amp; Greater Orlando crew')}, which is based in Kissimmee and has a separate phone line."),
    ]
    return page("/sarasota-manatee/", "unit", "Opera Concrete & Pavers – Sarasota & Manatee, FL",
                "Opera Concrete & Pavers, based in Sarasota, FL. Pavers, paver sealing and restoration, concrete and turf across Sarasota and Manatee counties. (941) 207-7585.",
                "Sarasota, Lakewood Ranch & Bradenton: pavers, sealing and concrete",
                capsule("Opera Concrete & Pavers' Sarasota crew is based in Sarasota, FL and answers at (941) 207-7585. "
                        "As of November 2026 it installs pavers, seals and restores them, and pours concrete and lays artificial turf across Sarasota and Manatee counties, including Lakewood Ranch and Bradenton, with free on-site estimates."),
                body, faqs=faqs, crumbs=[("Service areas", "/service-areas/")], unit="sarasota",
                related=[("/central-florida/", "The Kissimmee & Greater Orlando crew"), ("/sarasota-fl/", "Sarasota, FL"), ("/pavers/", "Pavers and turf overview"), ("/permits/", "Permits and HOA hub")],
                hero_photo=SARASOTA_PID, eyebrow="Sarasota, Lakewood Ranch & Bradenton",
                sources=["icpi-ts2", "icpi-ts5", "nrcs-eaugallie-osd", "nrcs-immokalee-osd", "nrcs-felda-osd", "fema-coastal-firm", "fdep-cccl-program", "sarasota-county-54-723-gbsl",
                         "ncei-annual-prcp", "swfwmd-restrictions", "city-sarasota-engineering-row", "sarasota-county-row-permit", "venice-ldr-9.1-row-definition", "manatee-no-permit-list",
                         "manatee-ldc-1004.2-access-drainage-permit", "bradenton-lur-2.2-zoning-permit", "lwr-ceva-manual", "venetian-acc-app", "palmerranch", "fs720-3035"])


def get_pages():
    return [central_florida(), sarasota_manatee()]
