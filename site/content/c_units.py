# -*- coding: utf-8 -*-
"""The two service-unit pages: /central-florida/ (Orlando crew) and /sarasota-manatee/ (Sarasota crew)."""
from _data import SERVICES
from _helpers import page, capsule, sec, table, faq, a, svc, city, cs, post, src
from _photos import for_service

ORLANDO_PID = (for_service("concrete-driveways", 1) or [None])[0]
SARASOTA_PID = (for_service("pool-deck-pavers", 1) or [None])[0]

ORLANDO_TOWNS = ["orlando", "kissimmee", "clermont", "oviedo", "winter-garden", "windermere"]
SARASOTA_TOWNS = ["sarasota", "lakewood-ranch", "bradenton", "venice"]
TABLE_SERVICES = ["concrete-driveways", "paver-patios", "pool-deck-pavers", "artificial-turf"]


def _service_table(caption, towns):
    headers = ["Town"] + [SERVICES[s]["name"] for s in TABLE_SERVICES]
    rows = [[city(slug)] + [cs(slug, s) for s in TABLE_SERVICES] for slug in towns]
    return table(caption, headers, rows, "Every tier-1 town in the unit has a dedicated page for each service; smaller towns nearby share the county's service and permit pages.")


def central_florida():
    body = "".join([
        sec("Counties and towns the Orlando crew covers",
            "<p>The Orlando unit is the crew behind every job between Winter Garden and St. Cloud. It covers five counties: Orange, Osceola, Seminole, Lake and the northeast corner of Polk, built around "
            f"{city('orlando')}, {city('kissimmee')}, {city('clermont')}, {city('oviedo')} and {city('winter-garden')}, the town of {city('windermere')}, and smaller communities such as {city('apopka')} and {city('davenport')}, with that address's permit office, soil and HOA rules already factored into the estimate.</p>"
            "<!--AUTO:unit-cities-->"),
        sec("Sand ridges and flatwoods: the ground changes by the mile",
            "<p>Lake County's ridge towns sit on different ground, literally, than the flatwoods covering most of Orange, Osceola and Seminole. Around Clermont and Minneola, near Sugarloaf Mountain, the peninsula's highest point at 312 feet "
            f"({src('wiki-sugarloaf', 'Wikipedia, citing USGS GNIS')}), the dominant soils are Candler and Astatula: excessively drained sand with a water table deeper than 80 inches ({src('nrcs-candler-osd', 'NRCS, Candler series')}). Drop into Orlando, Kissimmee or St. Cloud "
            f"and the soils switch to Myakka, Florida's official state soil, with Smyrna, Pomona and Basinger, where the seasonal high water table can sit within 18 inches of the surface part of the year "
            f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}; {src('fl-dos-state-soil', 'Florida Dept. of State, state soil')}). ICPI's paver spec calls for 2 to 4 inches more compacted base on soil that stays wet than the 6 inches it calls for on well-drained ground, "
            "so a Clermont ridge base and a Kissimmee flatwoods base rarely match, which is why the site visit checks soil first.</p>"),
        sec("A wet season on a schedule, heat that fights the cure, and Orange County's sinkhole history",
            f"<p>Orlando International Airport averages 51.45 inches of rain a year, most of it between late May and mid-October ({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}; {src('nws-mlb-wetdry', 'NWS Melbourne')}), which is why "
            f"{post('pouring-concrete-in-florida-rainy-season', 'pouring concrete in the rainy season')} starts early in the day. Heat works against the same pour: ACI hot-weather guidance flags concrete above 95°F and an evaporation rate past 0.2 "
            f"pounds per square foot an hour as the point where plastic shrinkage cracking gets likely, a bar a July afternoon clears easily, and {post('concrete-curing-in-florida-heat', 'how concrete cures in Florida heat')} covers the countermeasures.</p>"
            "<p>Orange County also carries a reputation worth naming. A 2010 Florida Senate interim report found that more than 88 percent of sinkhole claims filed between 2006 and 2009 landed in eleven counties, Orange among them, alongside the better-known \"sinkhole alley\" counties of Hernando, Pasco and Hillsborough "
            f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). Most settling slabs trace back to ordinary causes (loose fill, a leaking pipe, a rotted root); {post('sinkholes-and-settlement-central-florida', 'what a sunken slab usually means')} separates that from the rarer geological event, which Florida's insurance law (F.S. 627.706) treats on its own terms, and {svc('concrete-repair', 'concrete repair and resurfacing')} covers the fix either way.</p>"),
        sec("Permit desks across the Orlando unit",
            "<p>Every jurisdiction here treats the driveway apron as right-of-way work requiring a permit. What happens on the rest of the lot varies more, from a flat no-permit answer to a full engineering review; the table below is a snapshot, so call the desk listed before you design anything.</p>"
            + table("Permit desk by jurisdiction (checked October 2026)", ["Jurisdiction", "Driveway or apron", "Patio, slab or pavers on your lot", "Permit desk"],
                    [["City of Orlando", "Engineering permit; apron at least 6 in., 3,000 psi", "Same engineering permit covers patios, pool decks and pavers; artificial turf needs one too", "407-246-2271"],
                     ["Orange County (unincorporated)", "Right-of-way permit for the apron", "Permit required for poured concrete; pavers need a zoning permit only", "407-836-5550"],
                     ["City of Kissimmee", "Driveway/Sidewalk Construction permit through EnerGov", "“Slab With/Without Footer” permit type exists; pavers aren’t listed on their own", "407-518-2278"],
                     ["City of Clermont", "Zoning approval and a $45 fee, no building permit", "“Concrete/Driveway/Patio” permit type for slabs on grade", "352-394-4081"],
                     ["Lake County (unincorporated)", "County driveway permit; apron 10 to 24 ft at the property line", "Driveways and sidewalks under 30 in. above grade skip the building permit", "352-253-6019"],
                     ["City of Oviedo", "Right-of-Way Type I application, about $104 in combined fees", "Notarized slab/paver permit package with two site plans and insurance on file", "407-971-5755"],
                     ["City of Winter Garden", "Right-of-way utilization under Orange County's adopted regulations", "Impervious-area worksheet required; the city's own form states “pavers are impervious”", "407-656-4111"],
                     ["Town of Windermere", "Right-of-Way Use Application, $75 plus a $50 inspection fee", "No town rule published for patios or pavers on private lots", "407-277-9795"]],
                    "Summarized from each office's own pages. HB 803 (effective July 1, 2026) waives the single-family building permit for work under $7,500; it reaches none of the zoning, engineering or right-of-way reviews in this table.")
            + f"<p>County-by-county detail, including the statute citations, lives in {post('orange-county-orlando-driveway-patio-permits', 'Orlando and Orange County permits')}, {post('osceola-county-kissimmee-st-cloud-permits', 'Kissimmee, St. Cloud and Osceola County')}, "
            f"{post('seminole-county-driveway-patio-permits', 'Seminole County')} and {post('lake-and-polk-county-driveway-permits', 'Lake and Polk counties')}, and the {a('/permits/', 'permits and HOA hub')} rounds up every jurisdiction we serve.</p>"),
        sec("HOAs and master-planned communities",
            "<p>A city permit is often the easier approval. Several of the unit's larger communities run their own architectural review on top of it, with a deadline that usually falls weeks before the city's. "
            f"Baldwin Park's Residential Owners Association reviews every driveway change through an Architectural Review Committee that meets twice monthly and caps applications at 25 per meeting; its guidelines cap a front driveway's width at the garage door opening "
            f"and require the first 7 feet of an alley driveway to stay solid concrete, no pavers ({src('bp-network', 'Baldwin Park Network, ROA/ARC')}; {src('bp-guidelines', 'Baldwin Park Residential Guidelines, 2024')}). "
            f"In Lake Nona, the Laureate Park Master Association requires its Architectural Review Board to sign off on any property improvement, submitted by email before work starts ({src('laureatepark-faq', 'Laureate Park HOA FAQ')}; {src('lakenona-about', 'Lake Nona, About')}), and "
            f"Celebration's Architectural Review Committee meets monthly with a posted deadline ({src('celebration-arc', 'Celebration, Architectural Review Committee')}). Horizon West, bordering Windermere and Winter Garden, is unincorporated Orange County rather than one HOA, so its villages set their own rules "
            f"({src('ocfl-horizonwest', 'Orange County, Horizon West')}). As of 2026, none of these boards can require a building permit before reviewing your application "
            f"({src('fs720-3035', 'F.S. 720.3035')}), and for artificial turf, state law only protects the turf a neighbor or the street can't see ({src('fs720-3045', 'F.S. 720.3045')}). "
            f"{post('hoa-approval-for-pavers-and-concrete', 'Getting HOA approval for a driveway or pavers')} and {post('florida-hoa-artificial-turf-law', 'what Florida law says about HOAs and turf')} go further.</p>"),
        sec("Water restrictions in 2026: what SJRWMD allows",
            "<p>Most of the Orlando unit falls under the St. Johns River Water Management District, which runs a year-round twice-a-week watering schedule by address, with no watering between 10 a.m. and 4 p.m. and a one-hour, three-quarter-inch limit per zone "
            f"({src('sjrwmd-watering', 'SJRWMD Watering Restrictions')}). Lake County sits under something tighter: SJRWMD's Phase III Extreme Water Shortage order cuts watering to one day a week by address, 8 a.m. to 6 p.m. off-limits; Orange, Osceola and Seminole follow the standard schedule. "
            f"{svc('artificial-turf', 'Artificial turf')} sidesteps that schedule entirely, and {post('artificial-turf-water-savings-florida', 'how much water turf actually saves')} runs the numbers.</p>"),
        sec("Services in our main Orlando-area towns",
            "<p>Every tier-1 town below has its own page for each core service, with that town's soil and permit office covered in detail; smaller towns lean on the county-level permit guide above.</p>"
            + _service_table("Concrete, paver and turf services by town", ORLANDO_TOWNS)
            + f"<p>The full catalog, including {svc('stamped-concrete')}, {svc('concrete-slabs', 'concrete slabs and pads')}, {svc('retaining-walls')} and {svc('paver-sealing', 'paver cleaning and sealing')}, is on the "
            f"{a('/concrete/', 'concrete services overview')} and the {a('/pavers/', 'pavers and turf overview')}.</p>"),
    ])
    faqs = [
        faq("Which counties does the Orlando crew serve?",
            "Orange, Osceola, Seminole and Lake counties in full, plus the northeast corner of Polk County around Davenport. That covers Orlando, Kissimmee, Clermont, Oviedo, Winter Garden, Windermere, Sanford, Apopka, Winter Park, St. Cloud and the smaller towns between them."),
        faq("How do I know if my lot is on ridge sand or flatwoods soil?",
            "Elevation and the neighborhood's age are rough clues: the Clermont and Minneola ridge drains fast and rarely floods a yard, while older flatwoods subdivisions through Orlando and Kissimmee can hold water near the surface for months. The USDA Web Soil Survey gives an exact series for any address, and we check it on the site visit."),
        faq("Does Orange County's sinkhole history mean my driveway could be at risk?",
            "Not in the way most people picture it. Orange made an 11-county list for sinkhole insurance claims, but most sunken concrete near Orlando comes from ordinary settlement (soft fill, a leaking pipe, a decayed root), not a geological collapse. A contractor who has seen both can usually tell which one a sunken slab is."),
        faq("Is my town under a water restriction in 2026?",
            "Most of the unit follows SJRWMD's standard twice-weekly schedule, but Lake County is under the district's Phase III Extreme order, which limits lawn watering to one day a week. Orange, Osceola and Seminole follow the standard district schedule."),
        faq("Can my HOA stop me from resealing or changing my driveway?",
            "It can require its own approval first, but as of 2026 it can't make a building permit a precondition for reviewing your request, under F.S. 720.3035. Communities like Baldwin Park, Lake Nona and Celebration run their own architectural review on top of whatever the city requires, often on a monthly meeting schedule."),
        faq("Do I need a permit to add pavers in unincorporated Orange County?",
            "Yes, but it's a lighter one than poured concrete. Orange County requires a zoning permit for residential pavers rather than a full building permit, with a dimensioned site plan and, if the pavers sit in an easement, an Easement Acknowledgement form."),
    ]
    return page("/central-florida/", "unit", "Concrete, Pavers & Turf in Greater Orlando, FL", "Opera's Orlando crew covers Orange, Osceola, Seminole, Lake and northeast Polk counties: soils, permits, HOAs and 2026 water rules, by town.",
                "The Orlando crew: concrete, pavers and turf across Central Florida",
                capsule("Opera's Orlando unit pours concrete and lays pavers and artificial turf across Orange, Osceola, Seminole, Lake and the northeast corner of Polk County, from Winter Garden to St. Cloud. "
                        "As of October 2026, the area spans excessively drained ridge sand near Clermont, flatwoods soil through Orlando and Kissimmee with a water table that can sit within 18 inches of the surface, and eight separate permit desks."),
                body, faqs=faqs, crumbs=[("Service areas", "/service-areas/")], unit="orlando",
                related=[("/sarasota-manatee/", "The Sarasota–Manatee unit"), ("/concrete/", "Concrete services overview"), ("/pavers/", "Pavers and turf overview"), ("/permits/", "Permits and HOA hub")],
                hero_photo=ORLANDO_PID, eyebrow="Service area",
                sources=["nrcs-candler-osd", "nrcs-myakka-osd", "nrcs-tavares-osd", "nrcs-astatula-osd", "nrcs-pomona-osd", "nrcs-basinger-osd", "nrcs-smyrna-osd", "fl-dos-state-soil", "wiki-sugarloaf",
                         "ncei-annual-prcp", "nws-mlb-wetdry", "fl-senate-2011-104", "fs-627-706", "sjrwmd-watering", "orlando-engineering-permit", "orlando-esm", "orange-do-i-need-permit", "orange-residential-pavers",
                         "kissimmee-driveway-sidewalk", "clermont-permit-types", "lake-exempt", "lake-driveway-apron", "oviedo-row-type1", "oviedo-slab-paver",
                         "wintergarden-isr-worksheet", "wintergarden-row-app", "windermere-row-app", "bp-network", "bp-guidelines", "lakenona-about", "laureatepark-faq", "celebration-arc",
                         "ocfl-horizonwest", "fs720-3035", "fs720-3045"])


def sarasota_manatee():
    body = "".join([
        sec("Counties and towns the Sarasota crew covers",
            f"<p>The Sarasota unit is the crew behind every job on the Suncoast side of the business, covering Sarasota and Manatee counties from {city('palmetto')} and {city('parrish')} in the north to {city('venice')} and {city('north-port')} in the south. "
            f"The main towns are {city('sarasota')}, {city('lakewood-ranch')} (a master-planned community that straddles the Sarasota–Manatee line) and {city('bradenton')}, with the barrier islands ({city('siesta-key')}, {city('longboat-key')} and {city('anna-maria-island')}) "
            "and inland communities like Myakka City and Englewood covered by the same crew.</p>"
            "<!--AUTO:unit-cities-->"),
        sec("Flatwoods soil and a water table close to the surface",
            "<p>Sarasota and Manatee sit almost entirely on flatwoods soil, which means most lots hold water closer to the surface than the ridge towns on the Orlando side of the business. EauGallie and Immokalee, the two most common series here, both carry a seasonal high water table "
            f"within 6 to 18 inches of the surface for part of the year, and Myakka, Florida's official state soil, covers both counties as well ({src('nrcs-eaugallie-osd', 'NRCS, EauGallie series')}; {src('nrcs-immokalee-osd', 'NRCS, Immokalee series')}; {src('nrcs-myakka-osd', 'NRCS, Myakka series')}). "
            f"Pomello, a somewhat better-drained sand found on some of the higher ground, and Felda, a very poorly drained series with water within a foot of the surface for part of the year, round out the list ({src('nrcs-pomello-osd', 'NRCS, Pomello series')}; {src('nrcs-felda-osd', 'NRCS, Felda series')}). "
            "ICPI's paver spec treats wet, poorly drained ground as its own case: 2 to 4 inches more compacted base than the 6 inches it calls for on well-drained lots, which in this unit is closer to the rule than the exception.</p>"),
        sec("Salt air, flood zones and the Coastal Construction Control Line",
            "<p>Proximity to the Gulf and the bay changes how a project is built on the barrier islands and much of the mainland shoreline. FDOT treats any structure within 2,500 feet of water carrying more than 2,000 parts per million of chloride as a marine environment, a bridge standard rather than a residential code, "
            f"but a useful marker for how much salt is in the air near Siesta Key or along the bay ({src('fdot-sdg', 'FDOT Structures Design Guidelines')}). FEMA's flood maps add their own layer: Zone AE carries at least a 1-percent annual flood chance with wave heights under 3 feet, and the Coastal High Hazard "
            f"Zone VE adds wave action strong enough to cause structural damage in a base flood event, both common on the barrier islands and low-lying stretches of Venice and North Port ({src('fema-coastal-firm', 'FEMA, Coastal FIRM features')}). Building seaward of the state's Coastal Construction Control Line "
            f"needs its own DEP permit on top of any city or county approval, and Sarasota County layers an additional Gulf Beach Setback Line on its own beaches ({src('fdep-cccl-program', 'FDEP CCCL Program')}; {src('sarasota-county-54-723-gbsl', 'Sarasota County Code §54-723')}). "
            f"Salt and humidity are also why coastal pool decks get more sealer attention than inland ones; {post('saltwater-pools-and-coastal-salt-air-hardscape', 'saltwater pools and salt air on hardscape')} and {svc('paver-sealing', 'paver sealing and restoration')} cover the upkeep.</p>"),
        sec("Permit desks across the Sarasota unit",
            "<p>As on the Orlando side, a permit for the driveway apron in the right-of-way is nearly universal; what a patio or a set of pavers on private ground needs varies from an outright exemption to a full zoning review. The table below summarizes each office; confirm specifics before you design.</p>"
            + table("Permit desk by jurisdiction (checked October 2026)", ["Jurisdiction", "Driveway or apron", "Patio, slab or pavers on your lot", "Permit desk"],
                    [["City of Sarasota", "City engineer permit to cut a curb or build a driveway (Sec. 29.5-7)", "No flatwork exemption published; impervious coverage runs 60–75% by zone, 70% on coastal islands", "(941) 263-6494"],
                     ["Sarasota County (unincorporated)", "Right-of-Way Use Permit, plus a culvert permit where drainage is open", "Not published for patios; retaining walls over 4 ft need engineered drawings", "941-861-5000"],
                     ["City of Venice", "Right-of-Way Use Permit before any work in city right-of-way", "Older guidance exempts on-grade patios without footers; confirm it's still current", "941-882-7547"],
                     ["Manatee County (unincorporated)", "Access and Drainage permit; 12 to 24 ft wide, 6 in. thick to the right-of-way line", "Non-structural concrete or paver patios are permit-exempt; slabs with footers are not", "311 / 311@mymanatee.org"],
                     ["City of Bradenton", "Public Works approval plus a signed driveway/sidewalk affidavit", "Zoning permit required for paved areas; impervious coverage 50–70% by zone", "(941) 932-9414"],
                     ["Town of Longboat Key", "Rights-of-way use permit for any work in, on or above the right-of-way", "Driveways and patios on grade skip the building permit with zoning sign-off", "941-316-1966"]],
                    "Summarized from each office's own pages. HB 803 waives only the single-family building permit for work under $7,500 and never reaches a right-of-way, zoning or engineering permit.")
            + f"<p>Full detail and statute citations are in {post('sarasota-county-driveway-patio-permits', 'Sarasota, Venice and North Port permits')} and {post('manatee-county-driveway-permits', 'Bradenton, Lakewood Ranch, Parrish and Palmetto permits')}, "
            f"and the {a('/permits/', 'permits and HOA hub')} covers every jurisdiction we serve on both coasts.</p>"),
        sec("HOAs and master-planned communities",
            "<p>Lakewood Ranch drives the most HOA questions on this coast. Its Country Club/Edgewater Village Association requires a Modification Request Form before a homeowner seals, repaints, overlays or changes the material of a residential driveway or walkway, and the "
            f"homeowners' manual names the approved sealer colors, including Sherwin-Williams Silverplate and Gray Clouds; painting a driveway outright isn't permitted at all ({src('lwr-ceva-manual', 'Lakewood Ranch Town Hall, CEVA Homeowners’ Manual')}). The same modification process runs across most of the roughly 35,000-acre master plan, "
            f"since the IDA's board draws one member from each of its five community development districts ({src('lwr-about', 'Lakewood Ranch / SMR, About Us')}). Palmer Ranch, the roughly 60-square-mile community off I-75 in unincorporated Sarasota County, runs a Master Association that maintains common "
            f"grounds across more than 90 subdivisions, with architectural review handled neighborhood by neighborhood ({src('palmerranch', 'Palmer Ranch Master Association')}). In North Venice, the Venetian Golf & River Club's Architectural Control Committee requires written approval before any "
            f"exterior change, with applications due by noon on the last Monday of the month and approvals valid for six months ({src('venetian-acc-app', 'Venetian Golf & River Club POA, ACC Application')}). As of 2026, F.S. 720.3035 keeps any of these boards from requiring a building permit as a "
            f"condition of review, and F.S. 720.3045 protects artificial turf only where it can't be seen from the street or an adjoining lot. {post('lakewood-ranch-arc-approval-hardscape', 'Lakewood Ranch ARC approval for driveways and pavers')} and {post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for pavers or a driveway')} go further.</p>"),
        sec("Water restrictions in 2026: SWFWMD's Modified Phase III order",
            "<p>Sarasota and Manatee counties both fall under the Southwest Florida Water Management District, which has placed them under a Modified Phase III “Extreme” Water Shortage order running April 3, 2026 through March 31, 2027. Watering drops to one day a week, assigned by the last digit of the street address, "
            f"in one of two windows: 12:01 to 4 a.m. or 8 p.m. to 11:59 p.m. ({src('swfwmd-restrictions', 'SWFWMD District Water Restrictions')}). Manatee County has posted fines of $100, $250 and $500 for a first, second and third violation ({src('manatee-phase3', 'Manatee County Utilities')}), and the City of "
            f"Sarasota confirmed the same schedule through March 2027 ({src('sarasota-city-phase3', 'City of Sarasota')}). {svc('artificial-turf', 'Artificial turf')} sidesteps that schedule entirely, and {post('artificial-turf-water-savings-florida', 'how much water and money it saves')} runs the comparison against sod.</p>"),
        sec("Services in our main Sarasota-area towns",
            "<p>Each tier-1 town below has its own page for every core service, covering that town's soil, flood zone and permit office. Nearby towns in the same county use the county-level permit guide above instead.</p>"
            + _service_table("Concrete, paver and turf services by town", SARASOTA_TOWNS)
            + f"<p>The rest of the catalog, including {svc('stamped-concrete')}, {svc('concrete-walkways', 'sidewalks and walkways')}, {svc('retaining-walls')} and {svc('concrete-repair', 'concrete repair and resurfacing')}, is on the "
            f"{a('/concrete/', 'concrete services overview')} and the {a('/pavers/', 'pavers and turf overview')}.</p>"),
    ])
    faqs = [
        faq("Which towns does the Sarasota crew serve?",
            "Sarasota and Manatee counties in full: Sarasota, Lakewood Ranch, Bradenton, Venice, North Port, Palmetto, Parrish and the barrier islands (Siesta Key, Longboat Key and Anna Maria Island), along with inland communities like Myakka City and Englewood."),
        faq("Does Lakewood Ranch require approval before I reseal my driveway?",
            "Yes, for homes inside Country Club/Edgewater Village. A Modification Request Form has to be approved before sealing, repainting, overlaying or changing the material of a concrete driveway or walkway, and the homeowners' manual lists the sealer colors the association has already approved."),
        faq("Can I add a pool deck seaward of the Coastal Construction Control Line?",
            "Only with a DEP permit on top of whatever the city or county requires, and on Sarasota County beaches the county's own Gulf Beach Setback Line applies as well. Longboat Key, Siesta Key and Anna Maria are the barrier islands in this unit where that extra layer comes up most often."),
        faq("Is Sarasota or Manatee County under a water restriction in 2026?",
            "Both counties are under SWFWMD's Modified Phase III Extreme Water Shortage order, in effect through March 31, 2027. Lawn watering is limited to one day a week, assigned by the last digit of the street address, in an overnight or late-evening window."),
        faq("Do I need a permit for a patio in unincorporated Manatee County?",
            "A non-structural concrete or paver patio is on the county's own no-permit list, but a concrete slab with footers and any work tying into the right-of-way, such as the driveway connection, still need a permit through Manatee's Access and Drainage process."),
        faq("Does building near the Gulf change how concrete or pavers are built?",
            "The construction method stays the same, but upkeep changes: salt-laden air and a high water table push more homeowners on the barrier islands and the bay shoreline toward sealed pavers and more frequent joint and sealer checks than an inland Bradenton or Parrish lot typically needs."),
    ]
    return page("/sarasota-manatee/", "unit", "Concrete, Pavers & Turf in Sarasota & Manatee, FL", "Opera's Sarasota crew covers Sarasota and Manatee counties: soils, salt air, flood zones, permits and the 2026 SWFWMD watering order, by town.",
                "The Sarasota crew: concrete, pavers and turf for the Suncoast",
                capsule("Opera's Sarasota unit builds concrete, pavers and artificial turf across Sarasota and Manatee counties, from Palmetto and Lakewood Ranch to Venice and the barrier islands. "
                        "As of October 2026, the area combines flatwoods soil with a water table within 18 inches of the surface, salt air and flood zones near the Gulf, and a once-a-week SWFWMD watering order that runs through March 31, 2027."),
                body, faqs=faqs, crumbs=[("Service areas", "/service-areas/")], unit="sarasota",
                related=[("/central-florida/", "The Greater Orlando unit"), ("/concrete/", "Concrete services overview"), ("/pavers/", "Pavers and turf overview"), ("/permits/", "Permits and HOA hub")],
                hero_photo=SARASOTA_PID, eyebrow="Service area",
                sources=["nrcs-eaugallie-osd", "nrcs-immokalee-osd", "nrcs-pomello-osd", "nrcs-felda-osd", "nrcs-myakka-osd", "fdot-sdg", "fema-coastal-firm", "fdep-cccl-program", "fdep-cccl-apply",
                         "sarasota-county-54-723-gbsl", "city-sarasota-engineering-row", "sarasota-county-row-permit", "sarasota-county-124-255-culverts", "sarasota-county-22-63-retaining-walls",
                         "venice-ldr-9.1-row-definition", "venice-bp-guidelines-3rdparty", "manatee-ldc-1004.2-access-drainage-permit", "manatee-driveway-application",
                         "manatee-no-permit-list", "bradenton-lur-4.1-access-sidewalks", "bradenton-lur-2.2-zoning-permit", "lbk-code-57.03-row-permit",
                         "lwr-ceva-manual", "lwr-about", "palmerranch", "venetian-acc-app", "swfwmd-restrictions", "manatee-phase3", "sarasota-city-phase3", "fs720-3035", "fs720-3045"])


def get_pages():
    return [central_florida(), sarasota_manatee()]
