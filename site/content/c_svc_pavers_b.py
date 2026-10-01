# -*- coding: utf-8 -*-
"""Service pages: paver sealing & restoration, and retaining walls."""
from _helpers import (page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext,
                       price, per, price_note, tel, contact, photo, offer)
from _photos import for_service

CRUMBS = [("Pavers", "/pavers/")]


def sealing():
    K = "paver-sealing"
    pids = for_service(K, 4)
    body = "".join([
        sec("What paver sealing and restoration covers",
            "<p>This service bundles four separate jobs that usually get quoted and done together: pressure washing to strip algae and grime, "
            "re-sanding the joints with dry or polymeric sand, a sealer coat, and, where a section has sunk or gone wavy, releveling the base "
            "underneath the affected pavers. None of those steps is optional filler to pad a quote; a sealer applied over loose joint sand or a "
            "low spot in the base just locks the problem under a glossy finish instead of fixing it, so the order in which they happen matters "
            "as much as whether they happen at all. For the original install spec on a driveway, patio or pool deck, see "
            f"{svc('paver-driveways', 'paver driveways')}, {svc('paver-patios', 'paver patios')} or {svc('pool-deck-pavers', 'pool deck pavers')}; "
            f"this page covers what it takes to bring an existing paver surface back to that condition.</p>"
            + (photo(pids[0], "A worker in a hat and gloves pressure-washing a paver patio in front of a stucco house.") if pids else "")),
        sec("Cleaning: what a pressure wash actually accomplishes",
            "<p>Pressure washing alone runs about $0.35 to $0.80 per square foot and does more than make a dull surface look new; it strips the "
            f"algae, grime and old sand haze that would otherwise get trapped under a fresh sealer coat ({src('homeguide-pressure-wash', 'HomeGuide')}). "
            "It also doubles as an inspection pass. A wand held close and straight down into a joint pulls out whatever sand is still sitting there, "
            "which defeats the point of a step meant to prep the surface rather than strip it bare, so the spray goes in at an angle across the "
            "field, with direct pressure saved only for a stain that actually needs it. Walking the whole surface during this stage, not just the "
            "obviously dirty sections, is how a soft spot or a rocking unit gets caught before any sand or sealer goes down over it.</p>"),
        sec("Re-sanding: dry joint sand or polymeric sand",
            "<p>Once the surface is clean and dry, the joints get swept full again. Dry sand and polymeric sand do the same basic job differently, "
            "and the choice changes how often the next visit is needed.</p>"
            + table("Dry joint sand vs. polymeric sand", ["", "Dry sand", "Polymeric sand"],
                    [["How it's placed", "Swept in dry, compacted", "Swept in dry, then misted to activate a binder"],
                     ["Resistance to washout", "Lower; can migrate with heavy rain or traffic", "Higher once cured, resists washout better"],
                     ["Joint width it suits", "Any joint meeting the spec", "Any joint meeting the spec; wider joints need more sand per pass"],
                     ["Required by spec", "No fixed material is mandated", "No fixed material is mandated"]],
                    f"Joint sand and sealer are both optional refinements under the industry's own construction standard, not a requirement for a "
                    f"paver field to perform ({src('icpi-ts2', 'ICPI Tech Spec 2')}).")
            + "<p>Plain sand costs less upfront and is easier to top off by hand between full services. Polymeric sand costs more at the time of "
              "installation and holds up better against washout, which matters more on a sloped patio, a driveway apron that sees runoff, or a "
              f"pool deck that gets splashed daily. The full trade-off is in {compare('polymeric-sand-vs-joint-sand', 'polymeric sand vs. regular joint sand')}.</p>"),
        sec("Sealing: wet-look, natural finish and why there's no fixed resealing interval",
            "<p>A sealer coat deepens paver color, adds sheen if it's a wet-look product, and slows UV fading and staining, but the paver industry's own "
            f"technical guidance gives no fixed number of years before a coat needs redoing, only that it \"requires reapplication after a period of "
            f"wear and weather\" and that acrylic coatings typically hold up a few years before a recoat is worth it ({src('icpi-ts5', 'ICPI Tech Spec 5')}). "
            "A driveway in full sun with daily car traffic wears through a coat faster than a shaded walkway on the same property ever will, so the real "
            "clock is the surface itself: water that used to bead and roll off now soaks in, or a color that looked rich has gone flat. A wet-look "
            "sealer darkens and adds noticeable shine compared with a natural matte finish, and there's no single standard dictating which one a given "
            f"product produces, which is why we test a small, less visible section before committing a whole surface to it. {compare('wet-look-vs-natural-paver-sealer', 'Wet-look vs. natural-finish sealer')} "
            "covers the look each one leaves behind.</p>"
            + (photo(pids[1], "A close-up top-down view of gray interlocking concrete pavers fitted tightly together.") if len(pids) > 1 else "")),
        sec("Releveling a sunken or rocking paver",
            "<p>A paver that's sunk or started to rock almost always points to a problem underneath it, a soft spot or a void in the compacted "
            "aggregate base, not something a surface coat can reach. The fix mirrors the original installation on a smaller scale rather than "
            "patching over it.</p>"
            + steps([("Pull the affected paver or pavers.", "The unit comes out intact in most cases so it can go back in the same spot."),
                     ("Rebuild the bedding sand.", "The sand layer under the removed paver is restored to its original, uncompacted depth, not just topped off."),
                     ("Reset the paver flush.", "The unit goes back in level with its neighbors and checked with a straightedge across the joint."),
                     ("Sweep and compact fresh joint sand.", "New sand fills the joint around the reset paver and gets compacted into place."),
                     ("Match the surrounding sealer and sand.", "A previously sealed area gets the reset section brought back into line with the rest of the field.")])
            + f"<p>Paver repair work, priced by scope rather than a flat per-square-foot sealing rate, runs roughly $7 to $30 per sq ft nationally "
              f"({src('angi-patio-repair', 'Angi')}), and a Southwest Florida contractor quotes paver repair in Cape Coral at a narrower $4 to $8 per sq ft "
              f"({src('outdoorlifepros-paver-repair-capecoral', 'Outdoor Life Pros')}). A small corrected area costs far less than letting several pavers in the "
              "same spot sink before calling it in.</p>"),
        sec("Why Florida ground makes joints and bases move",
            "<p>Flatwoods soils common to both service areas, Myakka among them, hold a seasonal water table within about 18 inches of the surface for "
            f"part of most years ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). When that water table rises into the base under a paver field, fine "
            "material can migrate upward through the joints from below, not just wash out from above during a storm, which is one reason a patio or "
            "driveway on this kind of ground often needs its joints checked more than once a season even without a change in traffic. Ridge sands "
            "farther from the coast drain fast enough that the same joints tend to go longer between visits. Orlando averages 51.45 inches of rain a "
            f"year and Sarasota–Bradenton about 49.05, most of it in a rainy season running roughly late May into mid-October ({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}); "
            "scheduling cleaning and sealing for a dry stretch, rather than racing a forecast, keeps a sealer from going down on a surface that's still "
            "damp underneath.</p>"),
        sec("Cost of paver cleaning, re-sanding and sealing",
            f"<p>Combined cleaning, re-sanding and sealing runs {price('paver-sealing')} per {per('paver-sealing')} in current Florida market data, "
            f"typically {price('paver-sealing', True)} ({src('homeguide-seal-pavers', 'HomeGuide')}; {src('castle-paver-sealing-cfl', 'Castle Clean & Seal, Central Florida')}). "
            "These are market ranges compiled from published contractor pricing and cost guides, current as of October 2026; a written number for a "
            f"given surface follows a site visit, not a guess from the square footage alone. The {a('/paver-sealing-cost/', 'paver sealing cost guide')} "
            "breaks the range down by surface size and condition.</p>"),
        sec("Permits for cleaning, sealing and releveling",
            "<p>Cleaning, re-sanding and sealing an existing paver surface isn't new construction and doesn't touch the right-of-way, so none of the "
            "jurisdictions in either service area treat it as permitted work. Releveling a small, localized section follows the same logic. A large "
            "releveling job that amounts to pulling and rebuilding most of a driveway or patio's base, by contrast, is close enough to a new "
            f"installation that it can trigger the same permit review a new paver surface would; {post('driveway-widening-and-extensions-florida', 'widening or rebuilding a driveway')} "
            f"covers that line. On any contract over $2,500, Florida's lien law still requires a recorded Notice of Commencement before work starts "
            f"({src('fs713-13', 'F.S. 713.13')}), and since 2026 an HOA can't require a government permit as a condition of reviewing a project "
            f"({src('fs720-3035', 'F.S. 720.3035')}), which can matter if a different sealer finish changes how a paver surface reads from the street.</p>"),
        sec("Caring for pavers between professional visits",
            "<p>A light sweep and an occasional rinse between full sealing visits keeps windblown sand and grit from scratching a sealed surface "
            "underfoot, since that slow abrasion does more cumulative damage than any single storm. A handful of joints losing sand faster than the "
            "rest, often near a downspout or a shaded corner that stays damp, can usually be topped off by hand rather than left until the whole "
            "surface needs attention again. Acidic or ammonia-heavy household cleaners can dull or strip a sealer coat faster than ordinary sun and "
            "rain ever would, so checking a product's label against paver compatibility before using it on a stain is worth the extra minute. "
            f"{post('how-to-clean-pavers-without-damage', 'How to clean pavers without ruining the joints or sealer')} goes further.</p>"
            + (photo(pids[2], "A herringbone-pattern paver driveway and walkway leading to a garage.") if len(pids) > 2 else "")),
        sec("How do you choose the best paver sealing contractor near you?",
            "<p>Paver sealing contractors near me turns up plenty of results in both service areas; a few questions sort the ones who inspect the "
            "base from the ones who just spray and go.</p>"
            + ul(["Ask whether the crew checks for sunken or rocking pavers before cleaning, not after the sealer's already down.",
                  "Get the sand type specified, dry or polymeric, rather than a generic line item that just says \"re-sand.\"",
                  "Ask to see a sample of the sealer finish, wet-look or natural, on a small test area before committing the whole surface.",
                  f"Check the business on the {src('dbpr-search', 'DBPR license search')} if the scope includes any base rebuilding beyond spot releveling.",
                  "Confirm the order of operations in writing: any releveling first, then cleaning, then sand, then sealer, not sealer first."])
            + f"<p>{post('why-pavers-sink-in-florida', 'Why pavers sink in Florida, and how it gets fixed')} and {post('efflorescence-on-pavers-and-concrete', 'the white haze on new pavers')} go into the causes behind two of the most common calls.</p>"),
        sec("Where we clean, re-sand and seal pavers",
            f"<p>We clean, re-sand, seal and relevel paver surfaces across Greater Orlando and Sarasota–Manatee. Related towns: {cs('orlando', K)}, "
            f"{cs('windermere', K)}, {cs('sarasota', K)} and {cs('bradenton', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("How often should pavers be sealed in Florida?",
                "There's no fixed number of years written into the sealer's own specification, only that acrylic coatings typically hold up a few years before a recoat is worth doing. A driveway in full sun with daily traffic wears through a coat sooner than a shaded walkway, and a pool deck or coastal surface facing more water, chlorine or salt spray tends to need attention sooner too. Watching the surface, rather than a date on a calendar, is the more reliable signal."),
            faq("How long should I wait to seal new pavers?",
                "New concrete pavers can show a whitish efflorescence bloom within about 60 days of installation; it's cosmetic and typically fades on its own with normal weathering. Sealing over an active bloom before it's had a chance to clear can trap it under the coat instead, so waiting roughly a season before the first sealing visit usually gives a better result than sealing on a fixed schedule regardless of the paver's age."),
            faq("How long after sealing can I walk or drive on my pavers?",
                "Most sealers are dry to the touch, and safe for foot traffic, within a few hours; manufacturers generally recommend waiting a day or two before parking a vehicle on the surface so the coat has time to cure fully. Cure time varies by product, humidity and temperature, so checking the specific sealer's label is worth doing before moving furniture or a car back onto a freshly sealed area."),
            faq("Can sunken pavers be re-leveled without new pavers?",
                "Yes, in most cases the same pavers come back out, get reset on rebuilt bedding sand, and go back in flush with their neighbors; replacement units are only needed if a paver has cracked or chipped during removal. Releveling addresses the base problem that caused the sinking in the first place, which is why it has to happen before any cleaning or sealing on that section."),
            faq("Can you replace a few cracked or stained pavers?",
                "Yes, individual units can be pulled and swapped without disturbing the rest of the field, which is one of the practical advantages pavers have over a poured slab. The caveat is color match: if the original paver line is still in production, a close match is usually possible, but many lines get discontinued or re-blended within a few years, so an exact match isn't guaranteed on an older surface."),
            faq("Does sealing pavers stop weeds and ants?",
                "Sealing helps indirectly by locking compacted joint sand in place, which removes the loose, hospitable gap that weed seed and ants are drawn to in the first place. It isn't a pesticide or an herbicide, and a joint that's already lost its sand needs re-sanding before a sealer coat does much good against either problem."),
            faq("Why did my pavers turn white or cloudy after sealing?",
                "A cloudy or whitish film right after a sealer goes down is usually blushing, moisture trapped underneath the coat before it fully cured, often from sealing a surface that wasn't completely dry or from applying it during high humidity. It's a different issue from efflorescence, which is a mineral deposit that shows up before sealing, not after; a blushed coat typically needs to be stripped and reapplied under drier conditions rather than left to clear on its own.")]
    return page("/paver-sealing/", "service", "Paver Sealing & Restoration | Orlando & Sarasota, FL",
                "Paver cleaning, re-sanding with dry or polymeric sand, sealing and releveling sunken pavers. Florida market range $1.50-$3.25/sq ft as of October 2026.",
                "Clean, Re-Sand, Seal and Relevel: Paver Restoration in the Right Order",
                capsule("Paver sealing and restoration combines pressure washing, re-sanding with dry or polymeric joint sand, a sealer coat and, where "
                        "pavers have sunk or shifted, releveling the base underneath them. As of October 2026, Florida contractors price the combined "
                        "service at $1.50–$3.25 per square foot. We handle all four steps, in that order, across Greater Orlando and Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts5", "homeguide-seal-pavers", "homeguide-pressure-wash", "castle-paver-sealing-cfl", "angi-patio-repair",
                         "outdoorlifepros-paver-repair-capecoral", "nrcs-myakka-osd", "ncei-annual-prcp", "fs713-13", "fs720-3035", "dbpr-search"],
                related=[("/paver-sealing-cost/", "paver sealing cost guide"), ("/compare/polymeric-sand-vs-joint-sand/", "polymeric sand vs. joint sand"),
                         ("/compare/wet-look-vs-natural-paver-sealer/", "wet-look vs. natural-finish sealer"),
                         ("/blog/why-pavers-sink-in-florida/", "why pavers sink, and the fix"), ("/blog/mold-and-algae-on-pavers-florida/", "black mold and algae on pavers"),
                         ("/blog/ants-and-weeds-in-paver-joints/", "ants and weeds in paver joints"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=CRUMBS, crumb="Paver sealing", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("paver-sealing"), eyebrow="Pavers · Greater Orlando & Sarasota",
                howto=("How paver sealing and restoration is done", [("Inspect the surface", "Walk the whole field to flag sunken, rocking or stained pavers before anything else starts."),
                                                                      ("Relevel sunken pavers first", "Pull affected units, rebuild the bedding sand, and reset them flush before cleaning begins."),
                                                                      ("Pressure wash the field", "Strip algae, grime and old sand haze at an angle, keeping the wand off the joints."),
                                                                      ("Re-sand the joints", "Sweep in dry or polymeric sand and compact it into place."),
                                                                      ("Let the surface dry fully", "Pause until the field is dry through, not just dry on top, before sealing."),
                                                                      ("Apply the sealer", "Coat the dry, clean, re-sanded surface, working in cooler parts of the day to avoid flash-off.")]))


def retaining_walls():
    K = "retaining-walls"
    pids = for_service(K, 2)
    body = "".join([
        sec("Retaining walls, raised planters and seat walls",
            "<p>A retaining wall holds soil at two different grades apart, carrying real lateral pressure from the ground behind it. A raised "
            "planter borrows the same block system at a smaller scale to contain soil and mulch above the surrounding grade. A seat wall does "
            "neither job: it's built for sitting, usually without a slope pressing against its back, which is why most of the retaining-wall "
            "work homeowners actually ask for in both service areas turns out to be a seat wall or a planter rather than a true structural wall. "
            f"We build all three on the same segmental block system, scaled to what each one has to resist. {svc('paver-patios', 'Paver patios')} "
            f"and {svc('pool-deck-pavers', 'pool deck pavers')} often pair with a seat wall or planter as part of the same project.</p>"
            + (photo(pids[0], "A modular concrete crib-style retaining wall built into a grassy slope and filled with gravel.") if pids else "")),
        sec("The build: a leveling pad, a battered face and interlocking block",
            "<p>A segmental wall starts below grade, with a trench cut for a leveling pad of compacted crushed stone, built flat before the first "
            "course of block goes down. Every course above follows the line that first row sets, which is why getting the pad level matters more "
            "than it looks like it should; a small error there compounds into a visible lean by the top course. The blocks themselves aren't "
            "mortared together. They interlock, and the wall steps back slightly into the slope as it rises, a batter that lets the wall's own "
            "weight and the backfill behind it share the load the soil is pushing forward, rather than resisting that pressure on a perfectly "
            "vertical face alone.</p>"
            + table("Retaining wall cost by type and material, installed", ["Type or material", "Range per sq ft of wall face", "Note"],
                    [["Segmental block (interlocking, dry-stacked)", "$15–$35", "Most common system for a residential wall in both service areas"],
                     ["Gravity wall", "$20–$50", "Relies on mass alone; no mechanical interlock between units"],
                     ["Cantilevered", "$40–$80", "Reinforced concrete footing and stem; reserved for taller or engineered walls"],
                     ["Concrete block (material only, any system)", "$15–$40", ""],
                     ["Poured concrete", "$20–$45", ""],
                     ["Brick", "$30–$60", "Highest material cost of the common options"]],
                    f"HomeGuide, retaining wall cost guide. Project minimums run $1,500–$3,000; engineering review for a taller wall often adds "
                    f"$500–$2,000 or more on top of the build itself ({src('homeguide-retaining-wall', 'HomeGuide')}).")
            + "<p>Length changes the number more than most homeowners expect going in. A 10-linear-foot section at 2 feet tall runs roughly "
              f"$700 to $1,300 installed; the same 10 feet at 4 feet tall roughly doubles to $1,400–$2,600 ({src('homeguide-retaining-wall', 'HomeGuide')}), "
              "since a taller wall needs a deeper buried base course, more backfill volume and, past certain heights, engineering on top of the "
              "material itself. These are Florida market ranges compiled from published contractor pricing and cost guides, current as of October "
              "2026; a firm number follows a site visit, since slope, soil and access change the labor more than the wall type does.</p>"),
        sec("Does a retaining wall need drainage behind it?",
            "<p>Yes. Water pressure builds behind a wall from the bottom of the backfill up, so a drainage plan addresses the base of the "
            "excavation first, not just the top. The standard detail is a column of free-draining aggregate directly behind the block, wrapped to "
            "keep soil fines from clogging it, with a perforated pipe running along the base of that stone to carry water to an outlet that "
            "daylights at grade instead of trapping it behind the wall. Native soil dug out of the trench isn't a substitute for that aggregate; "
            "it compacts differently and holds water against the wall rather than letting it pass through, and on a flatwoods lot the fines in that "
            "soil can migrate into a drain system within a season or two and clog it from the inside.</p>"
            "<p>This matters more here than in a drier climate. Flatwoods soils common to both service areas, including Myakka, hold a seasonal "
            f"water table within about 18 inches of the surface for part of most years ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}), and "
            f"Orlando and Sarasota–Bradenton both see roughly 50 inches of rain a year, most of it in a rainy season running late May into "
            f"mid-October ({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}). A wall with nowhere for that water to go is carrying the full "
            "weight of every storm's runoff against its back with no release, which is a leading cause of bulging, cracking or an outright toppled "
            "wall over time.</p>"),
        sec("How tall can a wall be before it needs engineered drawings?",
            "<p>The height that triggers engineered plans isn't one statewide number; it's set jurisdiction by jurisdiction, and several in both "
            "service areas publish a specific figure.</p>"
            + table("Retaining wall height that triggers engineered drawings (checked October 2026)", ["Jurisdiction", "Threshold", "Note"],
                    [["Orange County (unincorporated)", "24 in if resisting a lateral load beyond soil, or 48 in of unsupported fill", "Florida Residential Code R404.4; signed and sealed engineering required above it"],
                     ["City of Clermont", "3 ft (36 in)", "A permit is required under 3 ft too, just without engineered plans"],
                     ["Sarasota County (unincorporated, incl. Siesta Key)", "4 ft (48 in)", "County wall-construction amendment; engineered drawings required above it"],
                     ["City of Palmetto", "Any height", "Permit required regardless of height; fee is $10 plus $0.10 per linear ft"],
                     ["Town of Longboat Key", "n/a", "8 ft is the maximum height the town allows for a retaining wall, not an engineering trigger"]],
                    f"{src('orange-res-plan-guide', 'Orange County')}; {src('clermont-permit-types', 'City of Clermont')}; "
                    f"{src('sarasota-county-22-63-retaining-walls', 'Sarasota County')}; {src('palmetto-code-10-46-retaining-wall-permit', 'City of Palmetto')}; "
                    f"{src('lbk-code-158.118-retaining-wall', 'Town of Longboat Key')}.")
            + f"<p>Orlando, Kissimmee, Osceola County, Lake County, Oviedo, Seminole County, Winter Garden, Windermere, St. Cloud, Winter Park, "
              f"Sanford, the City of Sarasota, Venice, North Port, Manatee County and Bradenton all require a permit for a retaining wall but don't "
              "publish a specific height that triggers engineering; the honest answer there is to confirm the trigger with the local building "
              f"department before finalizing a design, not to guess. {city('clermont')}, {city('minneola')} and {city('montverde')}, the hillier "
              "corner of the Orlando unit on the Lake Wales Ridge, see more retaining-wall work for exactly this reason: grade change between the "
              "house pad and the yard is a bigger factor there than it is on flatter ground closer to the coast.</p>"),
        sec("Permits, licensing and the Notice of Commencement",
            "<p>Retaining walls sit in a different legal spot than a driveway. Florida's license exemption for job scopes a local government can't "
            f"require a license for names driveway installation and decorative stone work specifically, but not walls ({src('fs489-117', 'F.S. 489.117')}). "
            "The state's \"structural masonry specialty contractor\" certificate, by contrast, explicitly covers \"all types of foundations, slabs, "
            f"footers, curbs, walls, columns, beams and other structures,\" which reads on retaining-wall work more directly than it does on a plain "
            f"driveway or patio ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). That's a reason to ask who's pulling the permit and "
            f"under what category, and to run any contractor through the {src('dbpr-search', 'DBPR license search')} before signing.</p>"
            f"<p>On a contract over $2,500, Florida's lien law requires a recorded Notice of Commencement before work starts ({src('fs713-13', 'F.S. 713.13')}), "
            "and since 2026 an HOA can't require a government permit as a precondition of reviewing a project, though it can still apply its own "
            f"architectural-control review to a wall's location, height and materials ({src('fs720-3035', 'F.S. 720.3035')}). "
            f"{post('lake-and-polk-county-driveway-permits', 'Driveway and patio permits in Lake and Polk County')} and "
            f"{post('hoa-approval-for-pavers-and-concrete', 'getting HOA approval for hardscape')} go further on the paperwork side.</p>"),
        sec("Seat walls and raised planters: lighter structures, the same base rules",
            "<p>A seat wall skips the engineered backfill and drainage column a true retaining wall needs, since it isn't holding back a slope, but "
            "it still needs a compacted base under its footing so the cap course sits level enough for someone to actually sit on. A raised "
            "planter is closer to a miniature retaining wall than a seat wall is: soil and mulch inside it hold moisture against the back of the "
            "block the same way backfill does behind a full wall, just at a smaller scale, so it still needs free-draining aggregate behind the "
            "face rather than garden soil packed straight against it. Treating a short wall as exempt from that base work because it doesn't look "
            "structural is how a planter or seat wall ends up leaning or separating at the joints within a season or two, even on ground that "
            "never had a drainage problem to begin with.</p>"),
        sec("What we build, and what we don't",
            "<p>This service covers segmental block retaining walls, raised planters and seat walls on land. It doesn't cover seawalls, bulkheads "
            "or dock structures. Florida's contractor-licensing rules treat marine work as its own set of specialty certificate categories, "
            f"separate from the structural masonry category that covers an on-land retaining wall ({src('fac61g4-15-100', 'Fla. Admin. Code R. 61G4-15.100')}). "
            f"Waterfront homeowners in {city('venice')}, on {city('longboat-key')} or along {city('siesta-key')} looking for seawall or bulkhead "
            "work need a marine contractor with that specific scope, not a hardscape contractor.</p>"),
        sec("How do you choose the best retaining wall contractor near you?",
            "<p>Retaining wall contractors near me returns a mix of landscapers and structural contractors in both service areas; a few questions "
            "separate the ones who understand drainage from the ones who just stack block.</p>"
            + ul(["Ask what's going behind the wall besides the blocks: aggregate type, pipe size and where the outlet daylights.",
                  "Get the base depth and leveling-pad spec in writing, not just a linear-foot price.",
                  f"If the wall is near the local height threshold, ask directly whether engineered drawings are required, and confirm who's drawing them.",
                  f"Check the contractor on the {src('dbpr-search', 'DBPR license search')} and ask which category the permit falls under.",
                  "Ask how backfill goes in: in stages as the wall rises, or dumped in all at once after the face is finished. The second answer is a problem."])
            + f"<p>{post('retaining-wall-ideas-florida-yards', 'Retaining wall and seat wall ideas for Florida yards')} and "
              f"{post('how-to-budget-a-backyard-hardscape-project-in-phases', 'budgeting a backyard project in phases')} go further.</p>"),
        sec("Where we build retaining walls, planters and seat walls",
            f"<p>We build retaining walls, raised planters and seat walls across Greater Orlando and Sarasota–Manatee. Related towns: {cs('orlando', K)}, "
            f"{cs('clermont', K)}, {cs('sarasota', K)} and {cs('lakewood-ranch', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("Does a retaining wall need drainage behind it?",
                "Yes. Water pressure builds behind a wall from the base up, so a drainage plan addresses the bottom of the excavation first: a column of free-draining aggregate behind the block face, wrapped to keep soil fines out, with a perforated pipe carrying water to an outlet that daylights at grade. On flatwoods ground with a shallow seasonal water table, skipping this step is a leading cause of a bulging or cracking wall within a few rainy seasons."),
            faq("How tall can a retaining wall be before it needs an engineer?",
                "It depends on where the wall is. Unincorporated Orange County applies Florida's residential code figures of 24 inches (if the wall resists lateral load beyond soil) or 48 inches (unsupported fill); Clermont's threshold is 3 feet; Sarasota County requires engineered drawings above 4 feet. Most other jurisdictions in both service areas require a permit for any retaining wall but don't publish a specific height that triggers engineering, so confirming with the local building department is the reliable step, not a general rule of thumb."),
            faq("Can you build a seat wall around a patio or fire pit?",
                "Yes, and it's one of the most common wall requests in both service areas. A seat wall needs a compacted base under its footing so the cap sits level for sitting, but it skips the engineered backfill and drainage column a true retaining wall needs, since it isn't holding back a slope."),
            faq("What is the difference between a retaining wall and a seat wall?",
                "A retaining wall is structural: it holds soil at two different grades apart and carries real lateral pressure, which is why it needs engineered drainage behind it and, above certain heights, engineered drawings. A seat wall is decorative and functional in a different sense, built for sitting, usually without a slope pressing against its back, so its main design requirement is a level, properly sized cap rather than a drainage system."),
            faq("Do you build seawalls?",
                "No. This service covers segmental block retaining walls, raised planters and seat walls on land. Seawalls, bulkheads and dock structures fall under separate marine specialty-contractor categories in Florida, distinct from the structural masonry category that covers an on-land retaining wall, so waterfront homeowners need a marine contractor with that specific scope."),
            faq("How long does a block retaining wall last?",
                "A segmental block wall built on a proper leveling pad with working drainage behind it is designed to hold for decades; the blocks themselves are durable concrete units, and the limiting factor is almost always the drainage system behind the face, not the block. A wall that loses its drainage to clogged outlets or fines migrating in from native-soil backfill can start showing bulging or leaning well before the block itself would otherwise wear out.")]
    return page("/retaining-walls/", "service", "Retaining Wall Contractor | Orlando & Sarasota, FL",
                "Segmental block retaining walls, raised planters and seat walls with drainage behind the wall. Florida market range $15-$40/sq ft of wall face, October 2026.",
                "Retaining Walls Built With Drainage Behind Them, Not Just a Face of Block",
                capsule("A retaining wall holds back a slope with interlocking segmental block, a compacted leveling pad and free-draining aggregate "
                        "behind the face, so water pressure has somewhere to go besides the wall itself. As of October 2026, Florida market pricing "
                        "runs $15–$40 per square foot of wall face. We also build raised planters and seat walls across Greater Orlando and "
                        "Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["homeguide-retaining-wall", "nrcs-myakka-osd", "ncei-annual-prcp", "orange-res-plan-guide", "clermont-permit-types",
                         "sarasota-county-22-63-retaining-walls", "palmetto-code-10-46-retaining-wall-permit", "lbk-code-158.118-retaining-wall",
                         "fs489-117", "fac61g4-15-100", "dbpr-search", "fs713-13", "fs720-3035"],
                related=[("/retaining-wall-cost/", "retaining wall cost guide"),
                         ("/blog/retaining-wall-ideas-florida-yards/", "retaining wall and seat wall ideas"),
                         ("/blog/fire-pit-on-pavers-florida/", "fire pits on pavers"),
                         ("/blog/how-to-budget-a-backyard-hardscape-project-in-phases/", "budgeting a backyard project in phases"),
                         ("/blog/lake-and-polk-county-driveway-permits/", "Lake and Polk County permits"),
                         ("/central-florida/", "the Orlando unit"), ("/sarasota-manatee/", "the Sarasota unit")],
                crumbs=CRUMBS, crumb="Retaining walls", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("retaining-wall"), eyebrow="Pavers · Greater Orlando & Sarasota",
                howto=("How a segmental retaining wall is built", [("Stake the line and excavate the trench", "Cut below grade deep enough for the leveling pad and the first buried course of block."),
                                                                    ("Compact the leveling pad", "A flat, level pad of compacted crushed stone sets the line every course above follows."),
                                                                    ("Lay the first course and begin backfill", "Block goes in, then free-draining aggregate and the perforated drain pipe start going in behind it."),
                                                                    ("Build the wall and backfill together", "Each course goes up and gets backfilled in stages, checking line and batter every few courses."),
                                                                    ("Route the drain to daylight", "The perforated pipe runs to an outlet that exits at grade, not trapped behind the finished wall."),
                                                                    ("Set the cap course and finish grading", "A level cap finishes the top course, and the ground behind the wall is graded to shed water away from it.")]))


def get_pages():
    return [sealing(), retaining_walls()]
