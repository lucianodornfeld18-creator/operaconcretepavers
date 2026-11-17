# -*- coding: utf-8 -*-
"""Hand-written paver-restoration pages for the two service units: Kissimmee, Orlando, Sarasota, Lakewood Ranch."""
from _helpers import page, capsule, sec, table, faq, svc, city, cs, post, a, src, ext, price, per, tel, offer
from _data import city_service_route

PR = "paver-restoration"
SS487 = "https://ask.ifas.ufl.edu/publication/SS487"
BRADENTON_NORMALS = "https://climatecenter.fsu.edu/products-services/data/1991-2020-normals/bradenton"
P = price(PR)
U = per(PR)


def _related(slug, name, sibling, sibling_name, unit_route, unit_label, posts):
    r = [("/paver-restoration/", "Paver restoration: how the work is done"),
         (city_service_route(slug, "paver-sealing"), f"Paver sealing in {name}"),
         (f"/{slug}-fl/", f"Concrete, pavers and turf in {name}"),
         (city_service_route(sibling, PR), f"Paver restoration in {sibling_name}"),
         (unit_route, unit_label), ("/paver-sealing-cost/", "Paver sealing and repair cost guide")]
    return r + [(f"/blog/{s}/", t) for s, t in posts]


# ----------------------------------------------------------------------------- Kissimmee
def kissimmee():
    sec1 = sec("Why do pavers settle in Kissimmee's flatwoods ground?",
        f"<p>Because the water sits close to the surface for weeks at a time. Smyrna soil, the series first described in Osceola County, has a water table under 18 inches for one to four months in most years, and Myakka drains slowly enough that the NRCS description calls its runoff slow to ponded "
        f"({src('nrcs-smyrna-osd', 'NRCS, Smyrna series')}; {src('nrcs-myakka-osd', 'NRCS, Myakka series')}). Orlando International, the nearest NOAA station, averages 51.45 inches a year, with June alone at 8.05 and November the low point at 1.79 "
        f"({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}).</p>"
        f"<p>Put those together and a driveway sits on a saturated base every summer. Wet sand under the pavers flows toward the low spot, and the joints above it drop. ICPI asks for 2 to 4 more inches of base on wet or weak soils "
        f"({src('icpi-ts2', 'ICPI Tech Spec 2')}), so when we lift a sunken wheel track in Kissimmee we dig down to see whether that extra depth was ever there. If it wasn't, topping up bedding sand alone buys a season, not a fix. "
        f"That is the dividing line between a quick re-sand and real {svc(PR, 'paver restoration')}.</p>")
    sec2 = sec("Which problem is it? A short field guide for Kissimmee driveways and lanais",
        "<p>Most calls start with one visible symptom. The table is how we read them on site, before anything gets lifted.</p>" +
        table("Common paver symptoms around Kissimmee and what they usually mean",
              ["What you see", "Likely cause", "What restoration does"],
              [["Two shallow ruts where the tires roll", "Base compressed under repeated loads on wet soil", "Lift the pavers, rebuild and recompact the base, reset"],
               ["Dips near the garage apron after storms", "Bedding sand washed toward a low point", "Pull the area, replace sand to a 1 in. screed, re-lay"],
               ["Border row spreading outward", "Edge restraint failed or was never spiked into the base", "Reset the edge, re-lay the loose field"],
               ["Dark, slick patches on a shaded lanai", "Mold and algae growing in damp joints", "Deep clean, re-sand the joints, seal if wanted"],
               ["White haze after a sealer coat", "Moisture trapped under the film", "Strip the film, clean, re-sand, reseal"]],
              "The cost per square foot applies only to the part that is releveled or repaired, not the whole surface."))
    sec3 = sec("Homes from the early 1990s are now past thirty",
        f"<p>The median Kissimmee home was built in 1992 ({src('acs-kissimmee', 'Census Reporter, ACS 2020–2024')}). Any paver patio or pool deck added at that time is old enough that the original bedding sand has migrated and the border has had decades of mower and car-tire abuse. "
        f"Pavers themselves are rarely the issue; the concrete units outlast the base. On a house that age the failed part is often a fraction of the surface, which is why "
        f"{post('restore-or-replace-old-pavers', 'restore-or-replace')} often comes out in favor of restoring. Pool decks get the same treatment as drives; a deck at that age may also be in line for {svc('pool-deck-pavers', 'a paver overlay')} if the owner wants a new look.</p>"
        f"<p>On lakefront and canal lots, the soil at the yard's low edge stays wetter than the middle of the street. Lake Tohopekaliga is the city's own anchor, with its marina on the Big Toho shoreline ({src('kissimmee-parks', 'City of Kissimmee, Parks')}), and homes within a few blocks of the water commonly show the biggest dips at the rear patio edge. "
        f"Read why in {post('why-pavers-sink-in-florida', 'why pavers sink in Florida')}.</p>")
    sec4 = sec("What does an association near Kissimmee need to see before pavers come up?",
        f"<p>It depends on the association, and the honest answer is to ask first. In Celebration, the community's review committee sits once a month, on a Monday, with a posted cutoff for applications "
        f"({src('celebration-arc', 'Celebration, Architectural Review Committee')}). The published guidelines for driveways and pavers sit behind the owner login, so we haven't verified what they say about a like-for-like re-lay. "
        f"Putting a different paver color or pattern in is a change of material in most communities, and we'd rather you send a one-page description than start digging on a hunch.</p>"
        f"<p>Public side: a driveway apron or sidewalk in the right-of-way is reviewed by the city's Engineering Division, 407-518-2278, for addresses inside Kissimmee, and by the county for addresses outside it "
        f"({src('kissimmee-driveway-sidewalk', 'City of Kissimmee, Driveway/Sidewalk Construction')}). The county rules are in {post('osceola-county-kissimmee-st-cloud-permits', 'our Osceola County permit guide')}. Work that stays inside your own lot line is a different conversation, and we'll tell you where we think the line falls before quoting.</p>")
    sec5 = sec("A worked example: one sunken wheel track on a two-car drive",
        f"<p>Say a 22 × 20 ft driveway, 440 sq ft, has a pair of ruts about 3 ft wide and 8 ft long where the family's SUV parks every night, roughly 48 sq ft. At the market range of {P} {U}, "
        f"that part of the job lands between about $144 and $576. If the base is sound and only the sand dropped, you're near the bottom. If the base has to be dug out and rebuilt, expect the upper half. "
        f"A wash-and-reseal of the whole drive is a separate line, priced in {cs('kissimmee', 'paver-sealing', 'the sealing page for Kissimmee')} and in the {a('/paver-sealing-cost/', 'cost guide')}, "
        f"and it only makes sense after the dip is fixed.</p>")
    sec6 = sec("How do I reach the crew that works the Kissimmee side?",
        f"<p>Call {tel('orlando')} and describe where the pavers sit, how big the problem area is and whether an association is involved. A phone photo of the dip with a broom handle laid across it tells us a lot. "
        f"The same unit covers {city('orlando', 'Orlando')}, and you can read how that page differs in {cs('orlando', PR, 'Orlando paver restoration')}. More on the unit is on the {a('/central-florida/', 'Kissimmee and Greater Orlando page')}.</p>")
    faqs = [
        faq("Why do my pavers dip after every summer storm in Kissimmee?",
            "Heavy June to September rain saturates flatwoods soil that already holds the water table within a foot and a half of the surface, and the bedding sand migrates toward whatever is lowest. A dip that returns each wet season usually points to a weak or thin base, not just lost sand."),
        faq("Is a sunken area at my garage apron a drainage problem or a base problem?",
            "Often both. If water stands on the spot an hour after rain stops, grade or a nearby downspout is feeding it. If it drains but the pavers still rock, the base underneath has softened. We probe with a rod and a level before deciding."),
        faq("Should I restore or replace pavers on a Kissimmee home built around 1992?",
            "Restore when the units are sound and the problem is sand, edges or one soft zone. Replace when many pavers are cracked or spalled, or a slab under the field is moving. Lifting a test patch usually settles it in an hour."),
        faq("How do you handle moss and algae in joints on a shaded Kissimmee lot?",
            "Deep cleaning at an angle, so the wand doesn't empty the joints, then fresh joint sand. Shade is the real cause, so trimming a canopy or redirecting an irrigation head matters as much as the wash."),
        faq("How do I get a restoration estimate for pavers in the Kissimmee area?",
            f"Call {tel('orlando')} with the address, the rough square footage of the damaged area and a photo. We confirm the scope on site, because the price depends on what's under the sand."),
    ]
    return page(
        "/kissimmee-fl/paver-restoration/", "cityservice",
        "Paver Restoration in Kissimmee, FL: Sunken Pavers",
        "Paver restoration in Kissimmee, FL, where Smyrna soil holds water within 18 in. of the surface and the median home dates to 1992. Market range $3–$12 per sq ft.",
        "Fixing Sunken, Stained and Loose Pavers in Kissimmee",
        capsule(f"As of October 2026, paver restoration in Kissimmee runs a Florida market range of {P} {U}, covering deep cleaning, releveling, replacing broken units and re-sanding. "
                "Kissimmee's flatwoods soil holds the water table within 18 inches of the surface for part of most years, which is why driveways and lanais here sink in the rainy season."),
        "\n".join([sec1, sec2, sec3, sec4, sec5, sec6]),
        faqs=faqs,
        sources=["nrcs-smyrna-osd", "nrcs-myakka-osd", "ncei-annual-prcp", "icpi-ts2", "acs-kissimmee", "kissimmee-parks", "celebration-arc", "kissimmee-driveway-sidewalk"],
        related=_related("kissimmee", "Kissimmee", "orlando", "Orlando", "/central-florida/", "Kissimmee and Greater Orlando unit",
                         [("mold-and-algae-on-pavers-florida", "Mold and algae on Florida pavers"), ("paver-sealer-turned-white-or-cloudy", "Why paver sealer turns cloudy")]),
        related_title="More for Kissimmee homeowners",
        crumbs=[("Kissimmee", "/kissimmee-fl/")], crumb="Paver Restoration", service=PR, city="kissimmee",
        hero_photo="interlocking-pavers", offer=offer(PR), eyebrow="Paver Restoration · Kissimmee, FL")


# ----------------------------------------------------------------------------- Orlando
def orlando():
    sec1 = sec("Lifted pavers beside an oak: can the root simply be cut?",
        f"<p>Not automatically. The city treats any tree 6 inches or larger at breast height as protected, and it is unlawful to encroach into the minimum undisturbed area around one without a Tree Encroachment Permit "
        f"({src('orlando-tree-ord', 'City of Orlando Ordinance 2020-13')}). A root hump under a walkway can sit inside that zone, so we stop, photograph the root and talk to you about options before a saw touches it.</p>"
        f"<p>The usual fixes keep the root: re-lay the affected pavers over a thinner, flexible bedding with a reset border, or reroute a short section of path around the flare. "
        f"Next door in Winter Park, a live oak or bald cypress of 30 inches or more is a landmark tree under Ordinance 3320-24 ({src('winterpark-tree-ord', 'City of Winter Park Ordinance 3320-24')}). "
        f"Details on why roots win against rigid surfaces are in {post('tree-roots-under-driveway-florida', 'the tree-root guide')}.</p>")
    sec2 = sec("What does Orange County's water table do to a base?",
        f"<p>The USGS survey of Orange County describes a water table that follows the land surface, highest after the wet season, and at one monitored site at or very near land surface "
        f"({src('usgs-orange-gw', 'USGS WRI 03-4257')}). Myakka and Smyrna flatwoods soils under much of the city stay saturated within about 18 inches for one to four months a year "
        f"({src('nrcs-smyrna-osd', 'NRCS, Smyrna series')}). ICPI warns that its 98 percent compaction target may not be reachable in extremely saturated soil ({src('icpi-ts2', 'ICPI Tech Spec 2')}).</p>"
        f"<p>That's why we schedule base rebuilds for the dry stretch. The NWS Melbourne median puts the dry season's start at October 15 ({ext('https://www.weather.gov/mlb/wetdry', 'NWS Melbourne, wet and dry season onset')}), and November averages 1.79 inches ({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}). "
        "Digging out a soft zone in August means compacting wet sand that never reaches density, and the spot comes back. We'd rather wait three weeks and do it once.</p>")
    sec3 = sec("Which Orlando pavers can stay and which have to go?",
        table("Triage of common Orlando paver failures",
              ["Situation", "Keep and reset", "Replace"],
              [["Edge pavers tilted by a root", "Units uncracked, root flare still moves little", "Units cracked where the root pressed"],
               ["Joint sand gone, field still flat", "All of it: clean and re-sand", "Nothing"],
               ["Hump 1 to 2 in. high near a tree", "Lift, shave bedding, re-lay with a flexible border", "Only broken units"],
               ["Pavers laid over an old slab that moved", "Rarely; the slab is the problem", "Usually the whole section"],
               ["Spalled, crumbling surface", "No", "Units that flake"]],
              "Triage is done on site with a level and a probing rod; photos help us estimate before the visit.") +
        f"<p>A driveway that looks failed from the street is sometimes only an edge and joint problem. If your list looks more like the bottom rows, the "
        f"{post('restore-or-replace-old-pavers', 'restore-or-replace article')} walks through the numbers.</p>")
    sec4 = sec("Do you need a city permit to re-lay pavers in Orlando?",
        f"<p>Inside the city limits, the Permitting Services Division treats paver work as an engineering permit and answers at 407-246-2271 "
        f"({src('orlando-engineering-permit', 'City of Orlando, Apply for an Engineering Permit')}). Whether a like-for-like repair of existing pavers falls under it is a question for that office, and we'd ask before the crew arrives. "
        f"The strip between sidewalk and street is public right-of-way, and the Engineering Standards Manual governs what is built there ({src('orlando-esm', 'City of Orlando Engineering Standards Manual')}).</p>"
        f"<p>Many Orlando mailing addresses are in unincorporated Orange County, where the county's own page for residential pavers applies ({src('orange-residential-pavers', 'Orange County, Residential Pavers')}). "
        f"{post('orange-county-orlando-driveway-patio-permits', 'The Orange County permit guide')} lays out both routes side by side.</p>")
    sec5 = sec("A worked example: a hump and a dip on a back patio",
        f"<p>Say a 600 sq ft patio has a 36 sq ft hump where an oak root runs under the field, and a 120 sq ft dip near the screen door where the downspout discharges. "
        f"That is 156 sq ft of work. At the market range of {P} {U}, you're looking at about $468 to $1,872. The hump is the unpredictable part, because the root decides how much we can lower. "
        f"Re-sanding and sealing the other 444 sq ft is optional and priced separately in the {a('/paver-sealing-cost/', 'cost guide')}.</p>")
    sec6 = sec("Reaching the Orlando crew",
        f"<p>{tel('orlando')} is the line for the Kissimmee and Greater Orlando unit. Tell us the neighborhood, whether a tree is involved and whether an association needs to approve it. "
        f"Neighbors in Osceola County can read the {cs('kissimmee', PR, 'Kissimmee version of this page')}, and the {city('orlando', 'Orlando hub')} lists the rest of what we do here. "
        f"The wash, re-sand and seal side of the work lives on the {cs('orlando', 'paver-sealing', 'sealing page for Orlando')}.</p>")
    faqs = [
        faq("Will you cut a live oak root to relevel my pavers in Orlando?",
            "Not as a first move. A protected tree has an undisturbed area, and encroaching on it needs a city permit. We look for a way to keep the root, such as a flexible border and thinner bedding, and bring in a certified arborist if cutting is on the table."),
        faq("Is September a poor month to restore pavers in Orlando?",
            "Rebuilding a base is. Rain in the wet season keeps sand saturated, so compaction falls short. Joint cleaning and replacing a few broken units can happen anytime the surface is dry; base rebuilds wait for the drier stretch that begins in mid-October."),
        faq("Who handles the paver strip between my driveway and the street?",
            "That area is public right-of-way, and the city's Engineering Standards Manual governs it. Call Permitting Services at 407-246-2271 before anyone lifts those pavers, and we'll scope only what sits on your side of the line."),
        faq("How can I tell if the base or just the sand has failed under my pavers?",
            "Press a level across the dip. If the pavers are flat but gapped, sand left the joints. If the units rock and the dip is soft underfoot, the base is the problem. A probing rod pushed through a joint tells us how deep the soft layer goes."),
        faq("What do you need from me for an Orlando restoration estimate?",
            f"Call {tel('orlando')} with the address, the area that looks wrong, and a photo with a straightedge across it. Mention any large trees nearby, because that changes the plan more than anything else."),
    ]
    return page(
        "/orlando-fl/paver-restoration/", "cityservice",
        "Paver Restoration in Orlando, FL: Roots and Re-Lays",
        "Paver restoration in Orlando, FL, where trees 6 in. or larger are protected and the water table sits near the surface. Market range $3–$12 per sq ft, October 2026.",
        "Orlando Paver Restoration for Lifted, Cracked and Tilted Pavers",
        capsule(f"As of October 2026, paver restoration in Orlando runs a Florida market range of {P} {U}. Orlando adds two local wrinkles: trees of 6 inches or more are protected by city ordinance, "
                "so root-lifted pavers can't simply be cut free, and a water table near the surface means base rebuilds wait for the dry season."),
        "\n".join([sec1, sec2, sec3, sec4, sec5, sec6]),
        faqs=faqs,
        sources=["orlando-tree-ord", "winterpark-tree-ord", "usgs-orange-gw", "nrcs-smyrna-osd", "icpi-ts2", "ncei-annual-prcp", "orlando-engineering-permit", "orlando-esm", "orange-residential-pavers", ("NWS Melbourne, wet and dry season onset", "https://www.weather.gov/mlb/wetdry")],
        related=_related("orlando", "Orlando", "kissimmee", "Kissimmee", "/central-florida/", "Kissimmee and Greater Orlando unit",
                         [("orange-county-orlando-driveway-patio-permits", "Orange County permit guide"), ("tree-roots-under-driveway-florida", "Tree roots under driveways in Florida")]),
        related_title="More for Orlando homeowners",
        crumbs=[("Orlando", "/orlando-fl/")], crumb="Paver Restoration", service=PR, city="orlando",
        hero_photo="paver-driveway-herringbone", offer=offer(PR), eyebrow="Paver Restoration · Orlando, FL")


# ----------------------------------------------------------------------------- Sarasota
def sarasota():
    sec1 = sec("Is repairing pavers in Sarasota maintenance or a permit job?",
        f"<p>The city's building guidance says repairs of $1,000 or less with no structural or code work need no permit, and tells owners to call the Building Division at (941) 263-6494 when in doubt "
        f"({src('city-sarasota-bp-guidelines', 'City of Sarasota, When a Building Permit Is Needed')}). A restoration can cross that dollar line quickly on a large deck, so we confirm before quoting. "
        f"The apron between the sidewalk and the street is another matter: cutting a curb or building a driveway in the right-of-way needs a permit from the city engineer under Sec. 29.5-7 "
        f"({src('city-sarasota-code-29.5-7-curb-cut-driveway', 'Sec. 29.5-7')}).</p>"
        f"<p>Outside the city limits, Sarasota County keeps its own rules, summarized in {post('sarasota-county-driveway-patio-permits', 'the county permit guide')}.</p>")
    sec2 = sec("Does salt air wreck pavers, or is something else going on?",
        f"<p>Salt is real but overrated as a paver killer. Concrete pavers don't rust; what salt does is dry as white residue, speed up wear on an unsealed surface and attack metal edging and fasteners. "
        f"FDOT classifies structures within 2,500 feet of water above 2,000 ppm chloride as marine, a bridge rule we cite only for scale ({src('fdot-sdg', 'FDOT Structures Design Guidelines §1.3.2')}). "
        f"On a bayfront lot, the practical consequence is that metal edge restraint and screws get inspected during restoration.</p>"
        f"<p>Saltwater pools throw chloride water onto the deck beside the coping, and that band is where we see the most joint loss. "
        f"The posts on {post('saltwater-pools-and-coastal-salt-air-hardscape', 'salt pools and coastal air')} and on {post('paver-sealer-turned-white-or-cloudy', 'cloudy sealer')} help sort salt residue from a failed coat.</p>")
    sec3 = sec("A 1976 median home means different pavers and different problems",
        f"<p>Sarasota has the oldest housing in the unit, with a median build year of 1976 ({src('acs-sarasota', 'Census Reporter, ACS 2020–2024')}). Many pavers in town were laid years after the house, often as a retrofit on a narrow lot or over an old slab. "
        f"If your pavers sit over a 1970s concrete pad, a rocking unit signals a different diagnosis than one over sand, because the pad may have cracked or tilted. We find out by lifting a test section.</p>"
        f"<p>On older lots the canopy is mature, and the city protects it. A permit is required before removing a tree larger than 4.5 inches at breast height, and a live oak 24 inches or more across is a Grand Tree "
        f"({src('sarasota-tree', 'City of Sarasota, Tree Protection')}). When a Grand Tree's roots lift a pool deck, the repair has to respect the tree, and we write the plan with that limit in view.</p>")
    sec4 = sec("What do 49 inches of rain and a shallow water table do under Sarasota pavers?",
        f"<p>The Sarasota-Bradenton airport averages 49.05 inches a year, with August the wettest month at 9.11 "
        f"({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}; {src('ncei-srq-monthly', 'NOAA monthly normals, SRQ')}). EauGallie and Immokalee soils across the area hold the water table within 6 to 18 inches for one to four months a year "
        f"({src('nrcs-eaugallie-osd', 'NRCS, EauGallie series')}; {src('nrcs-immokalee-osd', 'NRCS, Immokalee series')}).</p>"
        f"<p>Add the once-a-week watering order, in force through March 31, 2027 ({src('sarasota-city-phase3', 'City of Sarasota, Modified Phase III')}), and the picture is dry lawns beside soaked bases at the paver edge during storms. "
        f"Lawn edges stay thirsty while the paving next to them holds runoff, which is what pulls edge sand out of a border. The explanation is in {post('why-pavers-sink-in-florida', 'why pavers sink')}.</p>")
    sec5 = sec("A worked example: a lanai-to-pool deck with a lifted band",
        f"<p>Say a 400 sq ft pool deck has a 5 ft wide band of lifted units along the coping, about 60 sq ft, plus joints gone to green growth across the rest. "
        f"At the market range of {P} {U}, the lifted band comes to about $180 to $720. Washing, re-sanding and optionally sealing the whole deck is a separate per-square-foot line, "
        f"covered in {cs('sarasota', 'paver-sealing', 'Sarasota paver sealing')} and the {a('/paver-sealing-cost/', 'cost guide')}. "
        f"Mold in shaded joints is handled in {post('mold-and-algae-on-pavers-florida', 'the mold and algae guide')}.</p>")
    sec6 = sec("Calling the Sarasota crew",
        f"<p>{tel('sarasota')} reaches the Sarasota unit. Tell us whether the property is bayfront, near a pool, or shaded by a big oak, since those three facts steer the visit. "
        f"The wider unit is on the {a('/sarasota-manatee/', 'Sarasota and Manatee page')}, the {city('sarasota', 'Sarasota hub')} covers our other services, "
        f"and {cs('lakewood-ranch', PR, 'the Lakewood Ranch restoration page')} covers the community east of I-75.</p>")
    faqs = [
        faq("Do bayfront pavers in Sarasota need a different restoration than inland ones?",
            "The steps are the same, but we add a freshwater rinse, inspect metal edging and screws, and watch for white salt residue that can be mistaken for failed sealer. The base work depends more on the water table than on distance from the bay."),
        faq("A Grand Tree's roots are lifting my pool deck. Who decides what I can do?",
            "The city's tree rules decide. A live oak of 24 inches or more is a Grand Tree, and work near its roots has to go through the city's process. We scope a repair that leaves roots alone and document it for the arborist."),
        faq("Why do my pavers turn green every July on a shaded Sarasota lanai?",
            "Summer rain and shade keep joints damp, and mold and algae live in the sand. Cleaning removes it, but the lasting fix is drier joints: trimming, redirecting spray and a fresh joint sand."),
        faq("Is it worth restoring pavers laid over a 1970s slab in Sarasota?",
            "Often yes if the slab is stable, because the pavers can be lifted, bedded and reset. If the slab has moved, the pavers are only as good as what's under them, and we'll say so before you spend money."),
        faq("Which number reaches the Sarasota paver crew?",
            f"Call {tel('sarasota')}. The same unit works Sarasota, Lakewood Ranch and Bradenton, and a photo of the damaged area speeds up the first conversation."),
    ]
    return page(
        "/sarasota-fl/paver-restoration/", "cityservice",
        "Paver Restoration in Sarasota, FL: Salt, Roots, Repairs",
        "Paver restoration in Sarasota, FL, where homes date to a 1976 median and Grand Trees are protected by city rules. Market range $3–$12 per sq ft, October 2026.",
        "Sarasota Paver Restoration: Bayfront Salt, Older Lots, Grand Oaks",
        capsule(f"As of October 2026, paver restoration in Sarasota runs a Florida market range of {P} {U}. The city has the oldest housing in the Sarasota unit, with a median build year of 1976, "
                "plus bayfront salt exposure and protected Grand Trees, so the work here starts with finding out what is under the pavers and what is beside them."),
        "\n".join([sec1, sec2, sec3, sec4, sec5, sec6]),
        faqs=faqs,
        sources=["city-sarasota-bp-guidelines", "city-sarasota-code-29.5-7-curb-cut-driveway", "fdot-sdg", "acs-sarasota", "sarasota-tree", "ncei-annual-prcp", "ncei-srq-monthly",
                 "nrcs-eaugallie-osd", "nrcs-immokalee-osd", "sarasota-city-phase3"],
        related=_related("sarasota", "Sarasota", "lakewood-ranch", "Lakewood Ranch", "/sarasota-manatee/", "Sarasota and Manatee unit",
                         [("saltwater-pools-and-coastal-salt-air-hardscape", "Salt pools and coastal air"), ("sarasota-county-driveway-patio-permits", "Sarasota County permit guide")]),
        related_title="More for Sarasota homeowners",
        crumbs=[("Sarasota", "/sarasota-fl/")], crumb="Paver Restoration", service=PR, city="sarasota",
        hero_photo="pressure-washing-pavers", offer=offer(PR), eyebrow="Paver Restoration · Sarasota, FL")


# ----------------------------------------------------------------------------- Lakewood Ranch
def lakewood_ranch():
    sec1 = sec("Pavers in a ten-year-old Lakewood Ranch home shouldn't be sinking, so why are they?",
        f"<p>The Census Bureau puts the median year built in Lakewood Ranch at 2014, the newest in the Sarasota unit ({src('acs-lakewoodranch', 'Census Reporter, Lakewood Ranch CDP')}). "
        f"Pavers that age are not worn out, so a dip points to the build: a base compacted too quickly, thin sand, or lots filled and graded around a stormwater lake. "
        f"Standing groundwater on EauGallie, Immokalee and Myakka ground can rise within about 18 inches of the surface ({src('nrcs-eaugallie-osd', 'NRCS, EauGallie series')}; {src('nrcs-myakka-osd', 'NRCS, Myakka series')}).</p>"
        f"<p>The nearby Bradenton station averages 56.28 inches a year, wetter than the airport figure ({ext(BRADENTON_NORMALS, 'FSU Climate Center, Bradenton normals')}). "
        f"That rain falls on lots where water has to go somewhere, so lake-edge driveways often show the first settling. We confirm the cause before touching anything, and the answer sometimes involves the original builder's work instead of anything you did.</p>")
    sec2 = sec("What the community's approval process means for a re-lay",
        f"<p>Lakewood Ranch pavers sit under village rules. In Country Club and Edgewater, changing the material of a driveway or walkway, sealing concrete and applying an overlay each need a Modification Request Form "
        f"({src('lwr-ceva-manual', 'CEVA Homeowners’ Manual 2022')}). The form's deadline is noon on the Thursday before the committee meets, and work done before approval is subject to a violation "
        f"({src('lwr-ceva-form', 'CEVA Modification Request Form')}).</p>"
        f"<p>A like-for-like re-lay isn't listed by name in what we read, so call Community Association Services at 941-907-0202 and ask. Start that conversation before scheduling the crew, "
        f"and see {post('lakewood-ranch-arc-approval-hardscape', 'the Lakewood Ranch approval guide')} for the village-by-village forms.</p>")
    sec3 = sec("What happens if the work isn't finished inside the approval window?",
        f"<p>On the CEVA form, a resubmittal is required if work isn't completed within six months ({src('lwr-ceva-form', 'CEVA Modification Request Form')}). "
        f"Restoration rarely takes that long, but a schedule slip behind a rainy week or a delivery can push a job near the edge, so we plan around the approval date instead of the other way around. "
        f"The CEVA manual also says public sidewalk repairs are not permitted by the homeowner ({src('lwr-ceva-manual', 'CEVA Homeowners’ Manual 2022')}), so a lifted paver on a public path is a call to the association, not to us.</p>")
    sec4 = sec("Rust-colored spots near the lawn: irrigation or a sealer problem?",
        f"<p>Irrigation, more often than not. UF/IFAS notes that watering with iron-rich water can stain surfaces, and measured iron in southwest Florida groundwater ranges from 0.1 to 7.0 ppm "
        f"({ext(SS487, 'UF/IFAS EDIS SS487')}). Pavers near sprinkler heads pick up orange freckles that a sealer coat won't hide and a pressure wash won't always lift.</p>"
        f"<p>We start by finding the offending head, since cleaning stains without redirecting the spray guarantees a repeat. "
        f"Treatment choices are in {post('rust-and-irrigation-stains-on-concrete-pavers', 'the rust stain guide')}, and watering cuts under the once-a-week order, in force through March 2027 "
        f"({src('swfwmd-restrictions', 'SWFWMD District Water Restrictions')}), make that heavy staining less frequent but not rare.</p>")
    sec5 = sec("Two counties, one community: who regulates what?",
        f"<p>About three-quarters of Lakewood Ranch lies in Manatee County and about a quarter in Sarasota County ({src('lwr-cdp-counties', 'Census Reporter geography')}). "
        f"Manatee's code requires a permit for driveway work between the property line and the road but states that a permit is not required for regular driveway maintenance "
        f"({src('manatee-ldc-1004.2-access-drainage-permit', 'Manatee County LDC §1004.2')}). The Sarasota side has its own right-of-way rules. "
        f"The Manatee details are in {post('manatee-county-driveway-permits', 'the Manatee driveway guide')}.</p>")
    sec6 = sec("A worked example: a three-car apron and a lake-edge patio",
        f"<p>Say the apron of a three-car garage has a 90 sq ft rutted strip, and a lake-edge patio has a 30 sq ft dip. That is 120 sq ft of restoration, which at {P} {U} comes to about $360 to $1,440. "
        f"If the committee asks for a sample or a written scope, we'll supply it and the schedule slides to the next meeting. Compare with {cs('lakewood-ranch', 'paver-sealing', 'the Lakewood Ranch sealing page')}, "
        f"which covers approved sealer colors, and the {a('/paver-sealing-cost/', 'cost guide')}.</p>"
        f"<p>To reach the crew, call {tel('sarasota')}. The unit page is {a('/sarasota-manatee/', 'Sarasota and Manatee')}, there is a {city('lakewood-ranch', 'Lakewood Ranch hub')}, "
        f"and {cs('sarasota', PR, 'Sarasota restoration')} covers the city side.</p>")
    faqs = [
        faq("Why do pavers in a Lakewood Ranch home built about ten years ago already sink at the garage?",
            "Usually the base, not the pavers. A base compacted in a hurry, thin bedding sand or fill around a stormwater lake lets the surface drop under tire loads. We lift a test patch to see which of the three it is."),
        faq("What if my Lakewood Ranch approval expires before the pavers are done?",
            "On the Country Club and Edgewater form, work not completed within six months needs a new submittal. We schedule backward from your approval date and tell you early if weather could push the job past it."),
        faq("Do pavers beside a Lakewood Ranch stormwater lake behave differently?",
            "They tend to, because the ground at the lake edge stays wetter and the grade steers runoff toward the paving. Dips and spreading borders show up there first, and we pay more attention to edge restraint and base depth."),
        faq("Are the orange spots on my pavers from irrigation or from the sealer?",
            "Orange spots near sprinkler heads are usually iron in the irrigation water. Sealer problems look white, cloudy or peeling. We locate the head first, because cleaning without redirecting the spray brings the spots back."),
        faq("Can I lift a paver on the public sidewalk in front of my house myself?",
            "The CEVA manual says homeowners may not repair public sidewalks. Report a lifted paver to Community Association Services, and keep our work to the driveway, patio and deck on your lot."),
    ]
    return page(
        "/lakewood-ranch-fl/paver-restoration/", "cityservice",
        "Paver Restoration in Lakewood Ranch, FL: Approvals First",
        "Paver restoration in Lakewood Ranch, FL, where the median home dates to 2014 and village forms govern exterior changes. Market range $3–$12 per sq ft, October 2026.",
        "Lakewood Ranch Paver Restoration for Younger Pavers and Village Rules",
        capsule(f"As of October 2026, paver restoration in Lakewood Ranch runs a Florida market range of {P} {U}. With a median build year of 2014, most pavers here are about a decade old, "
                "so sunken sections point to base or lake-edge drainage, and village modification forms shape the schedule before a crew arrives."),
        "\n".join([sec1, sec2, sec3, sec4, sec5, sec6]),
        faqs=faqs,
        sources=["acs-lakewoodranch", "nrcs-eaugallie-osd", "nrcs-myakka-osd", ("FSU Climate Center, Bradenton 1991–2020 normals", BRADENTON_NORMALS),
                 "lwr-ceva-manual", "lwr-ceva-form", ("UF/IFAS EDIS SS487, Dealing with Iron and Other Micro-Irrigation Plugging Problems", SS487),
                 "swfwmd-restrictions", "lwr-cdp-counties", "manatee-ldc-1004.2-access-drainage-permit"],
        related=_related("lakewood-ranch", "Lakewood Ranch", "sarasota", "Sarasota", "/sarasota-manatee/", "Sarasota and Manatee unit",
                         [("lakewood-ranch-arc-approval-hardscape", "Lakewood Ranch ARC approval guide"), ("rust-and-irrigation-stains-on-concrete-pavers", "Rust and irrigation stains on pavers")]),
        related_title="More for Lakewood Ranch homeowners",
        crumbs=[("Lakewood Ranch", "/lakewood-ranch-fl/")], crumb="Paver Restoration", service=PR, city="lakewood-ranch",
        hero_photo="interlocking-pavers", offer=offer(PR), eyebrow="Paver Restoration · Lakewood Ranch, FL")


def get_pages():
    return [kissimmee(), orlando(), sarasota(), lakewood_ranch()]
