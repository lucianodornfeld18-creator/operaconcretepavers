# -*- coding: utf-8 -*-
"""Service pages: paver sealing and retaining walls."""
from _helpers import (page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext,
                       price, per, price_note, tel, contact, photo, offer)
from _photos import for_service

CRUMBS = [("Pavers", "/pavers/")]


def sealing():
    K = "paver-sealing"
    pids = for_service(K, 4)
    body = "".join([
        sec("What does paver sealing do, and what doesn't it do?",
            "<p>A sealer is a liquid coating or penetrating treatment that goes onto a clean, dry paver surface. The paver industry's technical bulletin says it "
            f"reduces the intrusion of water, stains, oils and dirt, and that most sealers darken the paver and intensify its color ({src('icpi-ts5', 'ICPI Tech Spec 5')}). "
            "It also soaks into the top of the joint sand, so it gives the joints a little stabilization as a side effect.</p>"
            "<p>What it doesn't do is fix anything underneath. A sealer adds no load-bearing strength, it won't raise a sunken corner, and it can't bind joints that "
            "have already emptied out. Sealing is also optional: the same industry spec calls sealers and joint sand stabilizers refinements, not a requirement for a paver "
            f"field to perform ({src('icpi-ts2', 'ICPI Tech Spec 2')}). People choose it for color, easier cleaning and fewer stained joints, and that's a fair reason. "
            "Whatever is wrong with the surface itself belongs on the "
            f"{svc('paver-restoration', 'paver restoration')} page, because coating over a problem only hides it for a season."
            "</p>"
            + (photo(pids[0], "A worker in a hat and gloves pressure-washing a paver patio in front of a stucco house.") if pids else "")),
        sec("Which paver sealer type fits: water-based, solvent-based, acrylic or urethane?",
            "<p>There are two separate questions folded into that one. First is the carrier: a sealer is either water-based or solvent-based. Second is the resin: acrylic, urethane, "
            "silane, siloxane or a water-based epoxy blend. Tech Spec 5 gives the working differences, and it says the supplier should confirm any product for the environment it's going into.</p>"
            + table("Sealer types for concrete pavers (from ICPI Tech Spec 5)", ["Type", "Look when cured", "Good to know"],
                    [["Acrylic (solvent or water-based)", "Gloss, strong color enhancement", "Good stain resistance; a few years between coats; can be cleaned and recoated; made-for-paver acrylics don't yellow"],
                     ["Urethane (solvent or water-based)", "High gloss", "More chemical-resistant than acrylic; aromatic types need a UV inhibitor; can't be refreshed by recoating, and removal is difficult"],
                     ["Silane or siloxane", "Flat, no gloss, slight color deepening at first", "Penetrates rather than coating; breathable; can deter efflorescence; doesn't resist oil unless it has an additive for that"],
                     ["Water-based epoxy blend", "Slight sheen", "Open surface that breathes; generally doesn't change skid resistance; meant for heavy-use areas"]],
                    "Alkyd, ester and polyvinyl acetate sealers are not recommended for pavers, and epoxies and silicones are generally not used on them, per the same bulletin.")
            + "<p>The solvent-versus-water split matters for how it behaves on the day. Solvent carries its solids as deep as the solvent will go and flashes off fast. Water-based "
              "sealers are emulsions: the particles can't go as deep, and they dry more slowly, with cure time that swings with temperature, wind and humidity. Solvent products are also the ones "
              "that tend to run into VOC rules and need good ventilation, with no flame or sparks nearby; most water-based sealers meet those limits, per the same source.</p>"
              "<p>So which one fits? There's no single answer. A residential driveway that sees tires and oil leans acrylic. A pool deck facing chlorine leans penetrating silane or siloxane. "
              "A urethane is the one to think hardest about, because the day you want a different finish it can't just be recoated. We name the product and its type in the written scope so you "
              "can read its manufacturer data sheet before anything is opened.</p>"),
        sec("Wet-look or natural finish: how will it look?",
            "<p>Almost every sealer changes the surface, so the real choice is how much. Gloss acrylics and urethanes give the dark, glossy wet-look. Siloxane and silane products leave a flat "
            "finish, and some acrylics and water-based blends sit in between at a low sheen. The bulletin notes that over-applying a sealer can leave the surface slippery once cured, so a heavy gloss "
            "coat isn't automatically better, particularly around a pool. Ask for a test patch in a corner, let it cure, and look at it in morning and late-afternoon light before the whole field gets "
            f"coated. The side-by-side is in {compare('wet-look-vs-natural-paver-sealer', 'wet-look vs. natural-finish paver sealer')}.</p>"
            + (photo(pids[1], "Herringbone-pattern paver driveway and walkway leading to a modern house garage.") if len(pids) > 1 else "")),
        sec("Joint-stabilizing and sand-binding sealers",
            "<p>The industry bulletin treats joint sand stabilizers and sealers as two products with overlapping jobs. A liquid stabilizer is often built from the same resins as a sealer, with a "
            "higher solids content (typically 18% to 28%), and it's meant to soak at least three-quarters of an inch into the joint sand. Dry stabilizers get mixed into the sand and activated "
            f"with water. Either way, the goal is to keep sand from washing, blowing or getting scuffed out, and to discourage seeds and insects from moving in ({src('icpi-ts5', 'Tech Spec 5')}).</p>"
            "<p>The spec says stabilizing joints is generally optional, since silt and fines settle into the sand and firm it up over time. It does recommend it on slopes over 7% or "
            "under 1.5%, and it names two spots where it earns its keep at a house: downspouts and under the eaves, where concentrated water keeps stripping sand. Which you'd choose between "
            f"plain sand and a binder is covered in {compare('polymeric-sand-vs-joint-sand', 'polymeric sand vs. regular joint sand')}.</p>"),
        sec("When should you seal new pavers?",
            "<p>Wait for the first bloom to show and fade. Efflorescence is a whitish calcium carbonate film that can appear immediately or within months and can peak in as short as 60 days; it "
            "doesn't affect the strength or durability of the pavers, and some of it wears off. If the job was installed in the dry season, the first stretch of wet weather may be what brings it up "
            f"({src('icpi-ts5', 'ICPI Tech Spec 5')}).</p>"
            "<p>The reason to wait is trapping. The same bulletin lists conditions that make a sealer turn white: a surface or joints that aren't dry, pavers that haven't had enough exposure to moisture, "
            "a source of efflorescence in the sand, base or soil, and a sealer that can't breathe. Florida adds a twist, because a paver patio installed in the dry winter months hasn't been through a "
            f"summer storm cycle. See {post('efflorescence-on-pavers-and-concrete', 'the white haze on new pavers')} for what that looks like, and "
            f"{post('paver-sealer-turned-white-or-cloudy', 'why sealer turns cloudy')} for what happens when it gets sealed too early.</p>"),
        sec("Sealing pool decks and travertine",
            "<p>A pool deck gets a harder life than a driveway: chlorine, splash-out, bare feet and constant wet-dry cycles. For concrete pavers, the bulletin says silanes and siloxanes are "
            "useful around pool decks to limit chlorine damage and are suited to salt exposure. An acrylic still earns its place when color depth matters more than breathability. Because over-applied "
            "sealer can go slick, we keep the coat thin on a deck and ask the manufacturer for slip performance wet and dry.</p>"
            "<p>Travertine is natural stone, not concrete, and the paver industry bulletin covers concrete pavers only. The sealer you'd pick for one isn't automatically right for the other, "
            "so read the data sheet for a rating on natural stone, and test a loose corner first. Travertine's open pores and filled holes bring their own care questions, which are laid out in "
            f"{post('travertine-pool-deck-care', 'travertine pool deck care in Florida')}, and the {post('saltwater-pools-and-coastal-salt-air-hardscape', 'saltwater pool and salt air guide')} "
            "goes into what a salt system does to a deck.</p>"),
        sec("Salt air on the coast, sandy ridge soil inland",
            "<p>The two service areas ask different things of a sealer. Near the Gulf in Sarasota and Manatee counties, salt air and a high water table are the main factors; the "
            "bulletin points to silane and siloxane for chloride and salt-air exposure, and says a poorly draining base can leave a sealer cloudy. Inland around Kissimmee and Orlando, the "
            f"ridge sands such as Candler and Astatula drain fast ({src('nrcs-candler-osd', 'NRCS, Candler series')}), while flatwoods ground such as Myakka holds water close to the surface for "
            f"part of the year ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). Wet sand under a paver field is exactly the situation where trapped moisture clouds a coat, so drainage under the "
            "pavers is part of how we judge whether a surface is ready.</p>"),
        sec("Weather window: when can pavers be sealed in Florida?",
            "<p>The surface and joints must be dry through, and the bulletin asks for at least 24 hours without moisture or surface dampness before application, with calm wind so the product "
            "doesn't drift or lay on unevenly. Turn off the sprinklers during cleaning, sealing and drying too. Rain totals are close in the two areas, 51.45 inches a year at Orlando's airport against 49.05 at Sarasota-Bradenton's, "
            f"and the wet months run roughly late May into mid-October ({src('ncei-annual-prcp', 'NOAA 1991-2020 normals')}). That doesn't make summer impossible, but it makes the "
            "late-October-to-May stretch easier, and it explains why we reschedule rather than seal a field that's damp underneath.</p>"
            "<p>Once the coat is down, keep all traffic off until the sealer is completely dry, typically 24 hours per the same bulletin. Plan for cars to wait longer, and check the label.</p>"),
        sec("How we apply sealer",
            "<p>This is the method, in the order it happens. Stains come out first, then the efflorescence and dirt. The joints are checked, and if they're low, they get topped up before coating.</p>"
            + steps([("Protect what's nearby.", "Plants, stucco and door thresholds get covered, and sprinklers get switched off."),
                     ("Confirm the surface is dry.", "We allow a full dry period after washing instead of trusting how the top looks."),
                     ("Test a small area.", "A corner patch shows the finish and the absorption rate of that particular paver."),
                     ("Spread and squeegee.", "A roller or low-pressure sprayer lays the product down, then a rubber squeegee moves surplus off the surface so it doesn't build up and so joint sand isn't pulled out."),
                     ("Let the chamfers and joints soak.", "The goal is penetration into the joint sand, not a thick film on top; generally one coat is enough."),
                     ("Keep traffic off.", "Feet and wheels wait for the cure time on the label.")])),
        sec("How often does a paver sealer need redoing?",
            "<p>No fixed number. Tech Spec 5 says sealers normally need reapplication after a period of wear and weather, depending on use, climate and the quality of the sealer, and that acrylics "
            "generally last for a few years before recoating. Watch the surface: water that used to bead now soaks in, or color goes flat. A full-sun driveway wears through a coat sooner than a shaded walk. "
            f"The {post('how-to-clean-pavers-without-damage', 'how to clean pavers without damaging them')} guide helps you keep it going between visits.</p>"),
        sec("Cleaning, releveling, stripping and replacing pavers: the short version",
            "<p>Sealing goes last. If the surface has black algae, rust stains, a failed hazy coat, rocking pavers or broken units, those get dealt with first, and that's a separate scope with its own "
            f"steps. Everything about it is on the {svc('paver-restoration', 'paver restoration')} page, so it isn't repeated here.</p>"),
        sec("What does paver sealing cost in Florida?",
            f"<p>Combined cleaning, re-sanding and sealing runs {price('paver-sealing')} per {per('paver-sealing')} in current market data, typically {price('paver-sealing', True)} "
            f"({src('homeguide-seal-pavers', 'HomeGuide')}; {src('castle-paver-sealing-cfl', 'Castle Clean & Seal, Central Florida')}). Those are market ranges as of October 2026, not a quote. "
            "A written number follows a look at the surface, since size, joint condition and stains change it more than a ZIP code does. Line by line, see the "
            f"{a('/paver-sealing-cost/', 'paver sealing cost guide')}.</p>"),
        sec("Permits and paperwork for sealing",
            "<p>Sealing an existing surface isn't new construction and doesn't touch the right-of-way, so it isn't treated as permitted work. On a contract over $2,500, Florida's lien law still "
            f"calls for a recorded Notice of Commencement before work begins ({src('fs713-13', 'F.S. 713.13')}). In an HOA community, a color or sheen change can be an architectural "
            "review item, so check the covenants before you pick a gloss. Since 2026 an HOA can't make a government permit a condition of reviewing a project "
            f"({src('fs720-3035', 'F.S. 720.3035')}).</p>"),
        sec("How do you choose the best paver sealing company near you?",
            "<p>Searching for paver sealing near me turns up a long list in both areas. A few criteria separate a crew that coats a surface from one that just sprays it.</p>"
            + ul(["The product named in writing, with its type (acrylic, urethane, silane or siloxane) and a link to its data sheet.",
                  "A dry period after washing stated in the scope, not a same-hour pressure wash and seal.",
                  "A test patch before the whole surface is committed.",
                  "A certificate of insurance sent directly by the agent, and the company looked up on Sunbiz so the name on the contract is active.",
                  "A coat rate or coverage figure, so you can tell a thin coat from a flooded one.",
                  "Who handles HOA paperwork if a finish change needs approval."])),
        sec("Where we seal pavers",
            f"<p>We seal pavers across Kissimmee and Greater Orlando, with the {a('/central-florida/', 'Kissimmee & Greater Orlando crew')} reached at {tel('orlando')}, and across Sarasota, "
            f"Lakewood Ranch and Bradenton, with the {a('/sarasota-manatee/', 'Sarasota crew')} at {tel('sarasota')}. Town pages: {cs('orlando', K)}, {cs('kissimmee', K)}, {cs('sarasota', K)} "
            f"and {cs('bradenton', K)}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("How often should pavers be sealed in Florida?",
                "There's no fixed number of years in the sealer specification. It says sealers need reapplication after wear and weather, and that acrylics typically last a few years. A sunny driveway with daily traffic wears a coat sooner than a shaded walkway, and a pool deck or coastal surface takes more water, chlorine or salt. Watch for water soaking in rather than beading, or color going flat, instead of marking a date."),
            faq("How long should I wait to seal new pavers?",
                "Efflorescence can peak in as short as 60 days and may only show after the first wet weather if pavers went in during the dry season. Sealing over an active bloom can trap it. Waiting for the first wet season to pass, then cleaning, usually gives a clearer result than sealing on a fixed schedule."),
            faq("How long after sealing can I walk or drive on my pavers?",
                "The industry bulletin says to keep traffic off until the sealer is completely dry, typically 24 hours. Many people allow foot traffic sooner and hold vehicles longer. Cure time moves with the product, humidity and temperature, so the label for the specific sealer is the final word before furniture or a car goes back."),
            faq("Does sealing pavers stop weeds and ants?",
                "It helps indirectly. Sealers and joint stabilizers soak into the sand and hold it in place, which reduces the loose gap seeds and insects use. It isn't a herbicide or an ant treatment, and joints that have already lost their sand need refilling before a coat does much. More in the post on ants and weeds in paver joints."),
            faq("Why did my pavers turn white or cloudy after sealing?",
                "Usually moisture or efflorescence got trapped: damp joints, a thick coat, a base that drains poorly, or a sealer that can't breathe. It is different from the white film on new pavers that appears before sealing. The fix typically means removing or re-dissolving the coat under drier conditions. The full explanation is in the post on why paver sealer turns white or cloudy."),
            faq("Is a wet-look sealer slippery?",
                "It can be if too much goes on. The industry bulletin warns against over-applying sealer because the surface can turn slick once cured, and it points to the manufacturer for wet and dry slip performance. On a pool deck, a thin coat or a flat-finish penetrating sealer is the cautious route."),
            faq("Can I seal travertine with the same product as concrete pavers?",
                "Not automatically. The paver industry's sealer guidance covers concrete pavers; travertine is natural stone with open pores. Check the data sheet for a natural-stone rating and test a hidden corner first. A sealer that looks fine on concrete can leave natural stone blotchy or darker than you wanted.")]
    return page("/paver-sealing/", "service", "Paver Sealing in Kissimmee, Orlando & Sarasota, FL",
                "Paver sealing types, wet-look vs natural, timing for new pavers and Florida weather. Market range $1.50-$3.25/sq ft as of October 2026.",
                "Paver Sealing: Sealer Types, Finish, Timing and Cost in Florida",
                capsule("Paver sealing is a protective coat over clean, dry, re-sanded pavers. As of October 2026, Florida installers price cleaning, re-sanding and sealing "
                        "at $1.50–$3.25 per square foot. We apply sealer in Kissimmee, Orlando, Sarasota, Lakewood Ranch and Bradenton, "
                        "choosing acrylic, urethane or penetrating types around the surface and the weather."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts5", "homeguide-seal-pavers", "castle-paver-sealing-cfl", "nrcs-myakka-osd", "nrcs-candler-osd", "ncei-annual-prcp", "fs713-13", "fs720-3035"],
                related=[("/faq/pavers/", "more paver questions"), ("/paver-restoration/", "paver restoration: cleaning, releveling and repair"), ("/paver-sealing-cost/", "paver sealing cost guide"),
                         ("/compare/wet-look-vs-natural-paver-sealer/", "wet-look vs. natural-finish sealer"), ("/compare/polymeric-sand-vs-joint-sand/", "polymeric sand vs. joint sand"),
                         ("/blog/paver-sealer-turned-white-or-cloudy/", "why paver sealer turns cloudy"),
                         ("/blog/efflorescence-on-pavers-and-concrete/", "the white haze on new pavers"),
                         ("/central-florida/", "the Kissimmee & Greater Orlando crew"), ("/sarasota-manatee/", "the Sarasota crew")],
                crumbs=CRUMBS, crumb="Paver sealing", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("paver-sealing"), eyebrow="Pavers · Kissimmee, Orlando & Sarasota",
                howto=("How paver sealer is applied", [("Protect plants and trim", "Cover nearby plants and surfaces and switch off the sprinklers."),
                                                      ("Confirm the surface is dry", "Allow a full dry period after washing, at least 24 hours without moisture."),
                                                      ("Test a small area", "Check finish and absorption on a corner patch."),
                                                      ("Spread and squeegee", "Lay the product with a roller or low-pressure sprayer and move surplus off with a rubber squeegee."),
                                                      ("Let joints soak", "Allow the product to penetrate the joint sand; one coat is usually enough."),
                                                      ("Keep traffic off", "Hold feet and wheels until the label's cure time passes.")]))


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
              "material itself. These are Florida market ranges compiled from published installer pricing and cost guides, current as of October "
              "2026; a firm number follows a site visit, since slope, soil and access change the labor more than the wall type does.</p>"),
        sec("Does a retaining wall need drainage behind it?",
            "<p>Yes. Water pressure builds behind a wall from the bottom of the backfill up, so a drainage plan addresses the base of the "
            "excavation first, not just the top. The standard detail is a column of free-draining aggregate directly behind the block, wrapped to "
            "keep soil fines from clogging it, with a perforated pipe running along the base of that stone to carry water to an outlet that "
            "daylights at grade instead of trapping it behind the wall. Native soil dug out of the trench isn't a substitute for that aggregate; "
            "it compacts differently and holds water against the wall rather than letting it pass through, and on a flatwoods lot the fines in that "
            "soil can migrate into a drain system within a season or two and clog it from the inside.</p>"
            "<p>This matters more here than in a drier climate. Myakka and the other flatwoods soils found in both service areas let the "
            f"seasonal water table come up to about 18 inches below the ground in most years ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}), and "
            f"annual rainfall at the Orlando and Sarasota–Bradenton airports is close to 50 inches, the bulk of it falling between late May and "
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
        sec("Permits, engineering and the Notice of Commencement",
            "<p>Retaining walls sit in a different spot than a driveway. A wall holds back soil, so the permit office treats it as a structure, "
            "and past the local height threshold it needs engineered drawings before the permit is issued. That's a reason to ask, before signing, "
            "who's pulling the permit, who's drawing the plans if a drawing is required, and whose name goes on the application.</p>"
            f"<p>A wall contract priced over $2,500 brings in the lien-law Notice of Commencement, recorded ahead of the first day of work ({src('fs713-13', 'F.S. 713.13')}). "
            "Starting in 2026 an HOA is barred from demanding a government permit before it will look at a project, yet it keeps its own "
            f"architectural-control review over where a wall sits, how tall it is and what it's made of ({src('fs720-3035', 'F.S. 720.3035')}). "
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
            "or dock structures, which are marine construction with their own engineering and permitting. "
            f"Waterfront homeowners in {city('venice')}, on {city('longboat-key')} or along {city('siesta-key')} looking for seawall or bulkhead "
            "work need a marine construction company, not a hardscape crew.</p>"),
        sec("How do you choose the best retaining wall company near you?",
            "<p>Retaining wall companies near me returns a mix of landscapers and structural builders in both service areas; a few questions "
            "separate the ones who understand drainage from the ones who just stack block.</p>"
            + ul(["Ask what's going behind the wall besides the blocks: aggregate type, pipe size and where the outlet daylights.",
                  "Get the base depth and leveling-pad spec in writing, not just a linear-foot price.",
                  f"If the wall is near the local height threshold, ask directly whether engineered drawings are required, and confirm who's drawing them.",
                  "Get the certificate of insurance from the company's insurance agent, and tie each payment to a finished stage of the wall rather than paying ahead of it.",
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
                "No. This service covers segmental block retaining walls, raised planters and seat walls on land. Seawalls, bulkheads and dock structures are marine construction, with their own engineering and permitting, so waterfront homeowners need a marine construction company for that work."),
            faq("How long does a block retaining wall last?",
                "A segmental block wall built on a proper leveling pad with working drainage behind it is designed to hold for decades; the blocks themselves are durable concrete units, and the limiting factor is almost always the drainage system behind the face, not the block. A wall that loses its drainage to clogged outlets or fines migrating in from native-soil backfill can start showing bulging or leaning well before the block itself would otherwise wear out.")]
    return page("/retaining-walls/", "service", "Retaining Wall Company | Orlando & Sarasota, FL",
                "Segmental block retaining walls, raised planters and seat walls with drainage behind the wall. Florida market range $15-$40/sq ft of wall face, October 2026.",
                "Retaining Walls Built With Drainage Behind Them, Not Just a Face of Block",
                capsule("A retaining wall holds back a slope with interlocking segmental block, a compacted leveling pad and free-draining aggregate "
                        "behind the face, so water pressure has somewhere to go besides the wall itself. As of October 2026, Florida market pricing "
                        "runs $15–$40 per square foot of wall face. We also build raised planters and seat walls across Greater Orlando and "
                        "Sarasota–Manatee."),
                body, faqs=faqs,
                sources=["homeguide-retaining-wall", "nrcs-myakka-osd", "ncei-annual-prcp", "orange-res-plan-guide", "clermont-permit-types",
                         "sarasota-county-22-63-retaining-walls", "palmetto-code-10-46-retaining-wall-permit", "lbk-code-158.118-retaining-wall",
                         "fs713-13", "fs720-3035"],
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
