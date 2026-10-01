# -*- coding: utf-8 -*-
"""Blog posts, group i: utility slabs (RV/boat pad, shed slab) and installation-process narratives
(concrete driveway, pavers, artificial turf, pavers-over-existing-concrete). These posts explain how a
job actually gets built, step by step, rather than selling it; the service pages are the offer and the
spec tables, so these link back to them instead of repeating the base-depth and strength numbers."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext, price, per, contact, photo
from _photos import for_service


def p_concrete_pad_for_rv_or_boat_parking():
    body = "".join([
        sec("How Big Should an RV or Boat Parking Pad Be?",
            f"<p>Most residential RV pads run about 12 ft wide and anywhere from 26 ft long for a van-class rig to roughly 50 ft for a "
            "full Class A motorhome towing a car behind it, with 2 to 3 ft of clearance on each side so doors can open and a person can "
            "walk the length of the pad. A boat pad is sized to the trailer rather than the hull, usually 10 to 12 ft wide and as long as "
            f"the boat and trailer tongue together, plus turning room if the driveway doesn't run straight to the street.</p>"
            + table("RV pad size by vehicle, rough guide", ["Vehicle", "Typical pad size"],
                    [["Class B van (about 20 ft)", "12 ft × 26 ft"],
                     ["Class C motorhome (about 28 ft)", "12 ft × 34 ft"],
                     ["Class A plus a towed car (about 45 ft combined)", "14 ft × 51 ft"]],
                    f"{ext('https://drivewayzusa.co/guides/rv-parking-pad-design-and-requirements/', 'DrivewayzUSA, RV parking pad design')}; measure your own unit's length and width before ordering concrete, since models vary within each class.")
            + f"<p>{svc('concrete-slabs', 'Our concrete slabs page')} covers how we size and quote a utility pad once the vehicle's exact dimensions "
              "and the lot's access route are known; this guide focuses on the planning questions specific to parking an RV or a boat.</p>"),
        sec("How Thick Does a Concrete RV or Boat Pad Need to Be?",
            f"<p>Florida's residential code sets 3½ in as the bare floor for any ground-supported slab, but a pad carrying an RV or a "
            f"loaded boat trailer is built well above that minimum ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}). A 5 in slab handles "
            "most RVs up to about 16,000 lb, and dual-axle trailers or a heavier Class A rig call for 6 in with reinforcement, the same "
            f"step up driveways take once trucks and boat trailers are the regular load rather than daily cars ({ext('https://drivewayzusa.co/guides/rv-parking-pad-design-and-requirements/', 'DrivewayzUSA')}). "
            f"Florida market data for concrete slabs runs {price('concrete-slab')} per {per('concrete-slab')}, with thickness and base "
            f"compaction, not square footage, doing most of the work to move that price up or down ({src('homeguide-concrete-slab', 'HomeGuide')}; "
            f"{src('angi-slab-orlando', 'Angi Orlando')}).</p>"),
        sec("Gravel, Pavers or Poured Concrete: Which Surface Holds Up Under an RV?",
            "<p>All three carry a parked RV or boat trailer, and the choice usually comes down to drainage, upkeep and whether the pad "
            "also needs to look finished from the street rather than purely functional.</p>"
            + table("RV and boat pad surfaces compared", ["Surface", "What it takes to hold the load", "Trade-off"],
                    [["Poured concrete", "5 to 6 in, reinforced, on a compacted base", "Highest upfront cost; least upkeep once it's down"],
                     ["Pavers", "80 mm (about 3⅛ in) units over a 6 in compacted aggregate base, the same step up driveways take for trucks and trailers", "A sunken corner can be lifted and reset rather than patched"],
                     ["Compacted gravel", "A crowned, well-drained base, deeper where soil is poor", "Ruts and scatters under repeated turning; needs periodic regrading"]],
                    f"ICPI Tech Spec 2, the construction standard for interlocking concrete pavements ({src('icpi-ts2', 'ICPI Tech Spec 2')}).")
            + f"<p>Gravel is the cheapest way to get a vehicle off the lawn, but a tire turning sharply on loose stone tends to push it into "
              f"ruts within a season or two, which is the main reason owners who keep an RV long-term move to a paved surface. "
              f"{svc('paver-driveways', 'Our paver driveway page')} covers the base build in more depth for a pad that doubles as extra "
              "driveway parking rather than a standalone slab.</p>"),
        sec("Does a Florida HOA Have to Allow an RV or Boat Pad?",
            "<p>Not automatically, and most master-planned communities in both service areas restrict where a recreational vehicle or boat "
            "can sit in plain view, even on an improved pad. Florida law protects what an owner stores only where it can't be seen: an "
            "association may not restrict items, including a boat or an RV, that aren't visible from the parcel's frontage, an adjacent "
            f"parcel or an adjacent common area, which is why most approved RV pads sit behind a fence, a hedge or the side of the house "
            f"rather than in the open front driveway ({src('fs720-3045', 'F.S. 720.3045')}).</p>"
            f"<p>Manatee County's own zoning rule follows the same logic on the government side: a restricted vehicle, its definition covers "
            "boats and RVs, can sit in a side or rear yard without extending more than 5 ft past the front of the house, or in a front "
            "yard only on a corner lot's secondary frontage, set back 10 ft and screened behind a fence or hedge at least 6 ft tall "
            f"({ext('https://library.municode.com/fl/manatee_county/codes/land_development_code', 'Manatee County Land Development Code')}). "
            "Sarasota County's rule caps the count rather than the visibility: an operational, currently tagged RV or boat owned by the "
            "resident can be stored outside, up to two per lot, without the same screening requirement "
            f"({ext('http://sarasotacounty.elaws.us/code/coor_apxa_art7_sec7.1', 'Sarasota County Zoning Code, Appendix A §7.1')}). "
            f"{post('hoa-approval-for-pavers-and-concrete', 'Our HOA approval guide')} covers the paperwork side of getting a pad approved "
            "before it's poured.</p>"),
        sec("Does an RV or Boat Pad Need a County Permit?",
            "<p>Often yes, and the permit frequently covers the vehicle itself as well as the pad underneath it, not just the concrete "
            "work. Orange County requires a Boat, Recreational Vehicle or Temporary Portable Storage Container permit under its zoning "
            "code, separate from any building permit for the slab, with a $47 fee, a site plan showing the setback from each property "
            "line, and a photo and registration for the vehicle being stored; installing pavers or another improved surface for the pad "
            f"needs its own sign-off as part of that application ({ext('https://www.orangecountyfl.net/PermitsLicenses/Permits/Boat,RecreationVehicleandorTemporaryPortable.aspx', 'Orange County, Boat/RV storage permit')}). "
            f"A plain slab pour over $2,500 also triggers Florida's lien-law Notice of Commencement, recorded before work starts "
            f"regardless of whether the local zoning permit is separate ({src('fs713-13', 'F.S. 713.13')}). Requirements vary enough "
            f"between cities and counties that a call to the local zoning office before ordering concrete is worth it; "
            f"{post('orange-county-orlando-driveway-patio-permits', 'our Orange County permit guide')} and "
            f"{post('sarasota-county-driveway-patio-permits', 'our Sarasota County permit guide')} cover the flatwork side of that process.</p>"),
        sec("How Do You Keep Water From Pooling Around an RV or Boat Pad?",
            "<p>A pad built flat, or worse, sloped toward the house, holds rainwater against tires and the base long enough to soften the "
            "ground underneath over a few wet seasons. We grade an RV or boat pad with a slight crown or a consistent slope away from the "
            "house and any structure nearby, carrying water to the same swale or yard drain the rest of the lot already uses rather than "
            "creating a new low spot. On flatwoods soils with a seasonal water table that can sit within about 18 in of the surface for "
            f"part of most years, Myakka among them, that slope matters more than it would on excessively drained ridge sand "
            f"({src('nrcs-myakka-osd', 'NRCS, Myakka series')}).</p>"),
        sec("Say You're Adding a Pad for a 32-Foot Travel Trailer in a Kissimmee Subdivision",
            f"<p>A homeowner in a 1990s {city('kissimmee')} subdivision with a 32-foot trailer first checks the HOA declaration for a "
            "screening requirement, since the pad is going in the side yard behind a six-foot fence to stay clear of the frontage "
            "visibility rule. The pad itself comes in around 14 by 40 ft, poured at 5 in with wire mesh, graded to shed water toward the "
            "existing side-yard swale rather than back toward the house. Osceola County's driveway permit process covers the pad since "
            f"it's new impervious construction, and the HOA's own architectural form goes in alongside it so both approvals move at the "
            f"same time instead of one waiting on the other. {post('osceola-county-kissimmee-st-cloud-permits', 'Our Osceola County permit guide')} "
            "walks through what that application packet typically includes.</p>"),
    ])
    faqs = [faq("Do I need a permit for an RV or boat parking pad in Florida?",
                "Often, and the permit can cover the vehicle as well as the pad. Orange County, for example, requires its own Boat, RV and Temporary Portable Storage Container permit in addition to any permit the concrete or paver work needs, with a site plan showing the setback from each property line. Rules differ enough by city and county that confirming with the local zoning office before pouring is worth the call."),
            faq("Can an HOA stop a resident from parking an RV or boat in the driveway?",
                "Usually, if it's visible from the street or a neighboring lot. Florida law only protects items that aren't visible from the parcel's frontage or an adjacent parcel, which is why most approved pads sit behind a fence or on the side of the house rather than in an open front driveway."),
            faq("How thick should a concrete RV pad be?",
                "Five inches handles most RVs up to about 16,000 lb; dual-axle trailers or a heavier Class A motorhome call for 6 inches with reinforcement. That's the same step up a driveway takes once it carries trucks or boat trailers instead of daily cars."),
            faq("Is gravel an acceptable surface for an RV or boat pad?",
                "It can be for a short-term or budget setup, but loose gravel tends to rut where a vehicle turns sharply, which usually means regrading every season or two. Concrete or pavers over a compacted base hold up longer under repeated turning and braking."),
            faq("How big should an RV parking pad be?",
                "Most residential pads run about 12 to 14 ft wide and 26 to 51 ft long depending on the RV class, with 2 to 3 ft of clearance on each side. Measuring the specific unit's length and width, rather than going by its class alone, avoids ordering a pad that's a few feet short.")]
    related = [("/concrete-slabs/", "Concrete slabs"), ("/concrete-slab-cost/", "Concrete slab cost guide"),
               ("/paver-driveways/", "Paver driveways"),
               ("/blog/driveway-widening-and-extensions-florida/", "Widening or extending a driveway"),
               ("/blog/hoa-approval-for-pavers-and-concrete/", "HOA approval for pavers and concrete")]
    return page("/blog/concrete-pad-for-rv-or-boat-parking/", "post",
                "RV Pad Concrete: Size, Thickness and Florida Rules",
                "Sizing and pouring an RV or boat parking pad in Florida: pad dimensions, slab thickness, HOA visibility rules and county permits, as of October 2026.",
                "Adding an RV or Boat Parking Pad in Florida: Size, Thickness and Rules",
                capsule("An RV or boat parking pad in Florida typically runs 12 to 14 ft wide and 26 to 51 ft long, poured 5 to 6 in thick "
                        "depending on the vehicle's weight. As of October 2026, Florida market data puts a concrete slab at $4 to $10 per "
                        "sq ft installed, and most jurisdictions in Greater Orlando and Sarasota-Manatee require a separate zoning or "
                        "storage permit on top of the flatwork permit."),
                body, faqs=faqs,
                sources=["fs720-3045", "fs713-13", "homeguide-concrete-slab", "angi-slab-orlando", "fbcr-2020-ch5", "icpi-ts2", "nrcs-myakka-osd",
                         ("Orange County, Boat/RV/TPSC storage permit", "https://www.orangecountyfl.net/PermitsLicenses/Permits/Boat,RecreationVehicleandorTemporaryPortable.aspx"),
                         ("Sarasota County Zoning Code, Appendix A §7.1", "http://sarasotacounty.elaws.us/code/coor_apxa_art7_sec7.1"),
                         ("Manatee County Land Development Code, restricted-vehicle parking standards", "https://library.municode.com/fl/manatee_county/codes/land_development_code"),
                         ("DrivewayzUSA, RV parking pad design and requirements", "https://drivewayzusa.co/guides/rv-parking-pad-design-and-requirements/")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-slabs",
                image=None, form=False)


def p_shed_slab_guide_florida():
    pids = for_service("concrete-slabs", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("How Thick Should a Shed Slab Be in Florida?",
            f"<p>Four inches is the common built thickness for a shed slab in Florida, a full half-inch above the state's 3½ in code floor "
            f"for any ground-supported slab, with 3,000 psi concrete and wire mesh or fiber mixed through the pour to hold hairline "
            f"cracks together rather than prevent them outright ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}). A heavier metal "
            "building or a shed stocked with a riding mower, a generator and shelving loaded with tools can justify stepping up to "
            f"5 or 6 in, the same jump a driveway takes once it carries real weight rather than foot traffic. "
            f"{svc('concrete-slabs', 'Our concrete slabs page')} covers the full thickness and reinforcement range across every kind of utility pad.</p>"
            + (photo(pid, "A worker smooths a freshly placed utility pad before it sets, well below the footprint of a full driveway pour.") if pid else "")),
        sec("What Size Pad Does a Shed Need?",
            "<p>A pad is normally cut 6 to 12 in larger than the shed's footprint on every side, enough to keep the structure's sill plate "
            "and door threshold off bare soil and to give a mower or a dolly a solid edge to roll onto rather than stepping down into "
            f"grass or mulch. {svc('concrete-slabs', 'The concrete slabs page')} walks through sizing a pad against a specific shed's "
            "dimensions once the model and footprint are picked out; this guide focuses on thickness, anchoring and permitting rather "
            "than repeating that sizing detail.</p>"),
        sec("Does a Shed Slab Need a Vapor Retarder or Wire Mesh?",
            "<p>Florida's residential code calls for a 6-mil polyethylene sheet under most slabs, with laps of at least 6 in, though it "
            "carves out an exception for unheated accessory structures, which covers the overwhelming majority of backyard sheds; wire "
            f"mesh is standard practice regardless, since it keeps a shrinkage crack from opening into a trip hazard even though it "
            f"doesn't stop the crack from forming in the first place ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}). A small slab "
            "under about 120 sq ft rarely needs a control joint cut into it the way a driveway panel does, since there's little room for "
            "the slab to move before it reaches an edge.</p>"),
        sec("How Do You Anchor a Shed Against Florida Hurricane Wind?",
            "<p>A shed anchored to a concrete slab holds together far better in high wind than one sitting loose on blocks or gravel, "
            "since the slab lets the structure act as one connected box instead of a frame that can rack and separate at the corners. "
            "The state's own hurricane retrofit guidance puts the problem in concrete terms: an 8 by 8 ft shed in a 130 mph wind faces "
            "roughly 2,100 lb of horizontal force, and the guidance recommends anchoring the frame directly to the slab, with screw "
            "anchors and crisscrossed straps as the fallback where no slab exists, plus a rope tied around the structure at mid-height "
            f"as extra restraint ({ext('https://apps.floridadisaster.org/hrg/content/equipment/equipment_index.asp', 'Florida Division of Emergency Management, Hurricane Retrofit Guide')}). "
            "Anchor bolts or straps cast into the slab at the time of the pour, rather than drilled in afterward, give the shed's floor "
            "plate a connection that doesn't rely on the concrete's surface alone holding the fastener.</p>"),
        sec("Does a Shed Slab Need a Permit?",
            "<p>It depends heavily on the shed's size and the specific city or county, more than almost any other flatwork question in "
            "this guide. Seminole County's non-structural exemption list names sheds of 200 sq ft or less specifically, while its list "
            f"says nothing about driveways, pavers or other slabs, which shows how size-specific these thresholds get "
            f"({src('seminole-hb803', 'Seminole County, state legislation affecting permits')}). Since July 1, 2026, Florida law also "
            "exempts single-family owners from a building permit for work valued under $7,500, though the exemption excludes structural "
            "work and never reaches a separate zoning or land-development permit a city might still require for a new accessory "
            f"structure ({src('orlando-hb803-guide', 'City of Orlando, HB 803 exemption guide')}). Because exemption thresholds vary this "
            "much by jurisdiction, and several counties in our service areas publish no shed-specific rule at all, calling the local "
            "building department before pouring is the only reliable way to know whether a given shed slab needs its own permit.</p>"),
        sec("Gravel Pad or Poured Slab Under a Shed: Does It Matter?",
            "<p>A gravel pad costs less and drains well, but it gives a shed's floor nothing to anchor into beyond what's driven straight "
            "into the ground, and it settles unevenly enough over a few wet seasons that doors can bind against their frames. A poured "
            "slab costs more upfront and takes longer to cure before the shed can go up, but it gives the structure a continuous, level "
            "connection point for anchoring and keeps the floor from settling at a different rate than the walls around it. Most owners "
            "planning to keep a shed in place for years, rather than a seasonal or portable unit, find the slab pays for itself in fewer "
            "sticking doors and a sturdier anchor point alone.</p>"),
        sec("Say You're Pouring a Pad for a 10×12 Shed in a Central Florida Subdivision",
            f"<p>A 10×12 ft shed gets an 11×13 ft pad, 4 in thick with wire mesh, which keeps the slab under most counties' smallest "
            "non-structural exemption thresholds where one exists, though that's confirmed with the local building department before "
            "the pour rather than assumed. Anchor bolts are set into the wet concrete at the shed manufacturer's bolt pattern, and the "
            "pad is graded with a slight slope away from the house so runoff from the shed's roof doesn't pool against the structure's "
            f"own foundation. {post('concrete-pad-for-rv-or-boat-parking', 'Our RV and boat pad guide')} covers the same base and "
            "permitting questions for a larger utility pad on the same lot.</p>"),
    ])
    faqs = [faq("How thick should a shed slab be?",
                "Four inches is the common built thickness, a half-inch above Florida's 3½-inch code floor for any ground-supported slab, with wire mesh or fiber mixed through the pour. A heavier building or a shed loaded with equipment can justify stepping up to 5 or 6 inches."),
            faq("Does a shed need to be anchored to its slab in Florida?",
                "Anchoring a shed directly to a concrete slab is one of the most effective ways to keep it from racking apart or lifting in high wind, since the slab lets the structure act as one connected unit rather than a loose frame. State hurricane guidance recommends anchor bolts or straps cast into the slab at the time of the pour."),
            faq("Do I need a permit for a shed slab in Florida?",
                "It depends on the shed's size and the specific city or county; thresholds vary widely. Seminole County, for example, exempts sheds of 200 square feet or less from its non-structural permit list, while other jurisdictions publish no size-specific rule at all. Confirming with the local building department before pouring is the only reliable approach."),
            faq("Can a shed sit on a gravel pad instead of a poured slab?",
                "It can, and it costs less upfront, but gravel gives a shed's floor nothing solid to anchor into and tends to settle unevenly over time, which can bind doors against their frames. A poured slab holds its level better and gives anchor bolts a continuous connection point."),
            faq("Does a shed slab need a vapor barrier?",
                "Florida's residential code generally requires a 6-mil poly sheet under slabs, but it carves out an exception for unheated accessory structures, which covers most backyard sheds. Wire mesh is still standard practice regardless, since it keeps a shrinkage crack from opening into a trip hazard.")]
    related = [("/concrete-slabs/", "Concrete slabs"), ("/concrete-slab-cost/", "Concrete slab cost guide"),
               ("/blog/concrete-pad-for-rv-or-boat-parking/", "Adding an RV or boat parking pad"),
               ("/blog/pavers-and-concrete-in-hurricanes/", "How pavers and concrete hold up to hurricanes"),
               ("/permits/", "Permits and HOA hub")]
    return page("/blog/shed-slab-guide-florida/", "post",
                "How Thick Should a Shed Slab Be in Florida?",
                "Shed slabs in Florida: built thickness, hurricane anchoring with real wind-load figures, and why shed permit rules vary so much by county, October 2026.",
                "Shed Slabs in Florida: Thickness, Tie-Downs and Permits",
                capsule("A shed slab in Florida is commonly poured 4 in thick, a half-inch above the state's 3½-inch code minimum, with "
                        "anchor bolts cast in at pour time so the structure can act as one connected unit in high wind. As of October "
                        "2026, an 8×8 ft shed faces roughly 2,100 lb of horizontal force in a 130 mph wind, and whether the slab itself "
                        "needs a permit varies sharply by Florida city and county."),
                body, faqs=faqs,
                sources=["fbcr-2020-ch5", "seminole-hb803", "orlando-hb803-guide", "homeguide-concrete-slab", "angi-slab-orlando",
                         ("Florida Division of Emergency Management, Hurricane Retrofit Guide", "https://apps.floridadisaster.org/hrg/content/equipment/equipment_index.asp")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-slabs",
                image=pid, form=False)


def p_concrete_driveway_installation_process():
    pids = for_service("concrete-driveways", 3)
    pid = pids[2] if len(pids) > 2 else (pids[0] if pids else None)
    body = "".join([
        sec("What's the Realistic Timeline From Tear-Out to a Drivable Driveway?",
            f"<p>A standard residential {svc('concrete-driveways', 'concrete driveway')} runs about a week from the first day of "
            "demolition to the point it can carry a car, though a straightforward new pour on bare ground with no old slab to remove can "
            "move faster, and a large or oddly shaped driveway runs longer. Most of that week isn't the pour itself, which usually takes "
            "a few hours once the truck arrives; it's excavation, base compaction and the curing days afterward that set the actual "
            "schedule.</p>"
            + table("A typical concrete driveway installation, day by day", ["Day", "What happens"],
                    [["1", "Old driveway demolished and hauled off, if one exists; new site excavated to depth"],
                     ["2", "Subgrade compacted, forms set, base material placed and compacted"],
                     ["3", "Concrete delivered and poured, screeded, floated and finished; control joints cut the same day"],
                     ["4–6", "Curing under plastic sheeting, a curing compound or wet curing; no traffic on the slab"],
                     ["7", "Light vehicle traffic typically allowed; full design strength isn't reached until 28 days"]],
                    f"Sequence and timing from NRMCA's own guidance on joints, hot-weather placing and curing ({src('nrmca-cip6', 'NRMCA CIP 6')}, {src('nrmca-cip12', 'NRMCA CIP 12')}).")),
        sec("What Happens on Demolition and Excavation Day?",
            "<p>Where an old driveway is coming out, it's broken up and hauled off before anything new goes in, and the exposed ground is "
            "then excavated to the combined depth the base and the new slab need together. On a typical Florida lot, that means digging "
            "past the topsoil's organic layer to firmer sand, since anything with roots, mulch or loose fill left under a slab compacts "
            "unevenly later and shows up as a settled spot within a season or two. Old concrete that's reinforced with rebar or wire mesh "
            "takes longer to break out than plain slabs, since the steel has to be cut free rather than just cracked and lifted.</p>"
            + (photo(pid, "A broad concrete driveway runs up to a house with two garage doors, the finished result of a week-long build sequence.") if pid else "")),
        sec("What Happens on Base and Forming Day?",
            f"<p>The exposed subgrade is compacted first, then wood or metal forms are staked along the driveway's finished edges to hold "
            "the concrete's shape and set its slope while it's still liquid. Base material, where the soil needs the extra support, goes "
            "down and gets compacted in lifts rather than dumped and rolled once, since a base that's compacted all at once often leaves "
            f"soft pockets underneath that a single pass can't reach. {svc('concrete-driveways', 'Our concrete driveway page')} covers the "
            "thickness and strength spec this base work is built to meet; this guide is about the sequence, not the numbers behind it.</p>"),
        sec("What Happens on Pour Day in Florida Heat?",
            "<p>Ready-mix concrete arrives by truck and is placed, screeded level and floated before the mix begins to set, a window that "
            "closes faster on a hot Florida afternoon than it does on a cool morning. Hot-weather guidance calls for starting early, "
            "before the sun and the slab temperature climb, keeping the subgrade damp without ponding water on it, and avoiding adding "
            "water to the mix once it's more than about an hour and a half old, since diluting curing concrete weakens the surface it "
            f"was meant to strengthen ({src('nrmca-cip12', 'NRMCA CIP 12')}). Control joints are saw-cut within hours of finishing, timed "
            "to the concrete's set rather than to a fixed clock, so the cuts relieve shrinkage stress before an uncontrolled crack beats "
            f"them to it ({src('nrmca-cip6', 'NRMCA CIP 6')}).</p>"),
        sec("Why Does the Pour Get Scheduled Around the Weather, Not Just the Calendar?",
            "<p>A pour placed above about 95°F, or at an evaporation rate past roughly 0.2 lb per sq ft per hour, loses surface moisture "
            "faster than the slab underneath can keep up with, which shows up later as fine, closely spaced plastic-shrinkage cracking "
            f"rather than a structural problem ({src('aci-faq-maxtemp', 'ACI')}; {ext('https://www.concrete.org/publications/internationalconcreteabstractsportal/m/details/id/20064', 'ACI Concrete International, evaporation rate')}). "
            "An afternoon thunderstorm rolling in mid-pour is the other scheduling risk through Florida's wet season, roughly late May "
            f"into mid-October, which is why crews here plan pours for early morning starts more often than not. {post('pouring-concrete-in-florida-rainy-season', 'Our rainy-season pour-scheduling guide')} "
            f"and {post('concrete-curing-in-florida-heat', 'our guide to curing in Florida heat')} go deeper on both of those weather "
            "questions than fits in a step-by-step walkthrough.</p>"),
        sec("How Long Does Curing Actually Take Before the Driveway Is Ready?",
            "<p>Curing and strength gain aren't the same clock. Industry guidance calls for at least 3 days of moist curing, by curing "
            "compound or wet curing, before the surface is considered set enough for light use, while the concrete itself keeps gaining "
            f"strength for about 28 days before it reaches the mix design's full rated psi ({src('nrmca-cip12', 'NRMCA CIP 12')}). In "
            "practice that means a new driveway can usually take a car within about a week, but it's worth holding off on parking a "
            "loaded RV, a dumpster or heavy equipment on it until closer to that 28-day mark, since those loads ask more of the slab than "
            "ordinary daily traffic does.</p>"),
        sec("Say You're Replacing a 24×24 ft Two-Car Driveway in Winter Garden",
            f"<p>A 576 sq ft driveway in a {city('winter-garden')} subdivision follows the same sequence at a slightly larger scale: a "
            "day to demo and haul off the old slab, a day to compact the base and set forms for the two-car width, a pour day that "
            "typically wraps the placing and finishing in under half a day given the size, then the curing window before the owner's "
            "cars go back in the garage. A two-car driveway built in Florida market data at this size runs toward the lower end of the "
            f"{price('concrete-driveway')} per {per('concrete-driveway')} range once the base work is straightforward and there's no old "
            f"reinforced slab to cut through. {a('/concrete-driveway-cost/', 'Our concrete driveway cost guide')} breaks that pricing down "
            "further by size and finish.</p>"),
    ])
    faqs = [faq("How many days does a concrete driveway installation take?",
                "About a week from demolition through the point the slab can take light traffic, though a straightforward new pour with no old driveway to remove can move faster. Most of that week is excavation, base compaction and curing rather than the pour itself, which usually takes a few hours once the truck arrives."),
            faq("What happens to the old driveway during a tear-out?",
                "It's broken up and hauled off before any new work starts, and reinforced slabs with rebar or wire mesh take longer to demolish than plain concrete since the steel has to be cut free rather than just cracked loose. The exposed ground underneath is then excavated to the depth the new base and slab need together."),
            faq("Why are control joints cut the same day as the pour?",
                "The cuts are timed to the concrete's own set, not to a fixed schedule, so they relieve shrinkage stress in a controlled line before an uncontrolled crack forms somewhere else on the slab. Early-entry saws typically cut within a few hours of finishing; conventional saws follow a bit later the same day."),
            faq("Does rain delay a concrete driveway pour in Florida?",
                "An afternoon thunderstorm rolling in mid-pour is one of the main scheduling risks during the state's wet season, roughly late May into mid-October, which is why crews here plan early morning starts more than later ones. A pour that gets rained on before the surface sets can need patching or, in bad cases, part of the slab redone."),
            faq("When does a new driveway reach full strength?",
                "The surface is generally ready for light vehicle traffic after about a week once the minimum 3-day moist cure is complete, but the concrete keeps gaining strength for roughly 28 days before it reaches the mix design's full rated strength. Heavy loads like a loaded trailer or equipment are worth holding off until closer to that mark.")]
    related = [("/concrete-driveways/", "Concrete driveways"), ("/concrete-driveway-cost/", "Concrete driveway cost guide"),
               ("/blog/pouring-concrete-in-florida-rainy-season/", "Pouring concrete in Florida's rainy season"),
               ("/blog/concrete-curing-in-florida-heat/", "How concrete cures in Florida heat"),
               ("/compare/pavers-vs-concrete-driveway/", "Pavers vs. concrete driveway")]
    return page("/blog/concrete-driveway-installation-process/", "post",
                "Concrete Driveway Installation Process in Florida",
                "How a concrete driveway is installed in Florida, day by day: tear-out, base, pour, control joints and curing, as of October 2026.",
                "How a Concrete Driveway Is Installed, Step by Step",
                capsule("A concrete driveway installation in Florida runs about a week from tear-out to the point it can take light "
                        "traffic: a day for demolition and excavation, a day for base and forms, a pour day timed around the heat, and a "
                        "minimum 3-day cure. As of October 2026, full design strength isn't reached until about 28 days after the pour."),
                body, faqs=faqs,
                sources=["nrmca-cip6", "nrmca-cip12", "aci-faq-maxtemp", "fbcr-2020-ch5", "homeguide-concrete-driveway", "angi-driveway-orlando",
                         ("ACI Concrete International, estimating evaporation rate", "https://www.concrete.org/publications/internationalconcreteabstractsportal/m/details/id/20064")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-driveways",
                image=pid, form=False)


def p_paver_installation_process_florida():
    pids = for_service("paver-driveways", 3)
    pid = pids[2] if len(pids) > 2 else (pids[0] if pids else None)
    body = "".join([
        sec("How Are Pavers Installed in Florida, Start to Finish?",
            f"<p>A {svc('paver-driveways', 'paver')} installation builds from the ground up in a fixed order: excavate, compact a "
            "crushed-aggregate base, screed a thin layer of bedding sand, set the pavers, lock the field with edge restraint, then sweep "
            "and compact joint sand to finish. Unlike concrete, a paver surface is load-ready as soon as the joint sand is compacted and "
            "the base compactor's last pass is done; there's no multi-day cure to wait out before the driveway or patio can be used.</p>"
            + (photo(pid, "Closely fitted interlocking concrete pavers, the kind of tight, compacted joint a finished installation leaves behind.") if pid else "")),
        sec("How Deep Does the Base Need to Be?",
            "<p>The industry's own construction standard sets a residential driveway base at a minimum of 6 in of compacted aggregate "
            "over soil that drains well, 2 to 4 in deeper where the ground stays wet, while a patio or walkway needs roughly 4 in on the "
            f"same well-drained ground, since foot traffic never loads a base the way a parked car does ({src('icpi-ts2', 'ICPI Tech Spec 2')}). "
            f"{svc('paver-driveways', 'Our paver driveway page')} and {svc('paver-patios', 'our paver patio page')} carry the full base "
            "spec table by use; this guide is about how that base actually gets built, lift by lift, rather than the finished numbers.</p>"),
        sec("Can Crushed Concrete Be Used as Paver Base in Florida?",
            f"<p>Yes. Florida's own transportation department allows crushed concrete from demolished pavement to be recycled into new "
            "base and aggregate material, and it's a common, locally available base option in both service areas rather than a "
            f"compromise material ({ext('https://www.fdot.gov/materials/administration/resources/library/issues-trends/recycling-faqs.shtm', 'FDOT, recycled materials FAQ')}). "
            "What matters more than whether the base is virgin limerock or recycled concrete is that it's a well-graded aggregate that "
            "compacts to the same density standard either way; a load of loose, uncrushed rubble swapped in to save money doesn't meet "
            "that standard and compacts unevenly under the plate compactor.</p>"),
        sec("How Is the Base Compacted, and to What Standard?",
            "<p>Aggregate goes down in lifts of about 4 to 6 in, not dumped to full depth and rolled once, with each lift run over by a "
            "plate compactor, typically rated around 7,000 lbf for this kind of work, before the next lift is added on top. The target is "
            "at least 98 percent of standard Proctor density for pedestrian areas and driveways, checked rather than assumed, since a "
            "base that looks solid on the surface can still be loose a few inches down if a lift was skipped or the compactor only made "
            f"one pass ({src('icpi-ts2', 'ICPI Tech Spec 2')}). On flatwoods soils with a shallow seasonal water table, Myakka and Smyrna "
            "among them, that compaction standard can be harder to reach without extra base depth or a drainage pipe worked into the "
            f"subgrade first ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}).</p>"),
        sec("What Is Bedding Sand, and How Does It Go Down?",
            "<p>Bedding sand is a thin, uncompacted layer, screeded to about 1 in using pipe rails as a depth guide, that sits between "
            "the compacted base and the pavers themselves; it's never compacted before the units are set, since compacting it first "
            "would leave no give for the pavers to settle evenly into as they're laid and tamped. A rake or a flat board, pulled across "
            "the pipe rails, levels the sand to a consistent depth across the whole field in one pass, and any low spot left in the sand "
            "telegraphs straight up through the finished surface once pavers sit on top of it.</p>"),
        sec("How Are the Pavers Laid, Cut and Compacted Into Place?",
            "<p>Full units are set first, working course by course from a fixed, straight edge, usually the house or garage line, with "
            "border and apron pieces measured and cut last once the main field's pattern is established. A plate compactor runs over "
            "the laid field before joint sand goes in, which seats each paver into the bedding sand and tightens the gaps between units "
            "to the standard eighth-of-an-inch joint width or less that the construction spec calls for.</p>"),
        sec("How Is Edge Restraint Installed, and Why Does It Matter This Much?",
            "<p>Restraint runs the entire perimeter of the finished field and anywhere the paving material changes, spiked down into the "
            "compacted aggregate base rather than into the soil beneath it, since soil alone doesn't hold a spike against the sideways "
            f"push a loaded field exerts over time ({src('icpi-ts3', 'ICPI Tech Spec 3')}). Skipping restraint, or substituting plastic "
            "landscape edging meant for flower beds, is the single most common reason a paver field spreads at the edges and opens "
            "gapping joints within a year or two, long before the pavers themselves show any wear.</p>"),
        sec("How Do You Finish a Paver Installation: Joint Sand and the Final Pass",
            f"<p>Dry joint sand, or polymeric sand where the project calls for it, is swept across the finished field and worked down "
            "into the joints, then the whole surface gets one more compactor pass to lock the sand in and settle the field as one "
            "connected unit. Sealing is a separate, optional step that can happen weeks or months later once the pavers have weathered "
            f"in; it's not part of the base installation sequence itself, and the industry's own guidance sets no fixed interval for how "
            f"often a sealed surface needs recoating ({src('icpi-ts5', 'ICPI Tech Spec 5')}).</p>"),
        sec("Say You're Installing a Paver Driveway on a Candler Sand Lot Near Clermont",
            f"<p>{city('clermont')} sits on the Lake Wales Ridge, where excessively drained Candler sand lets a 6-inch base compact "
            "cleanly without the extra lifts a flatwoods lot nearby might need, since the water table there can sit 80 in or deeper "
            f"rather than within 18 in of the surface ({src('nrcs-candler-osd', 'NRCS, Candler series')}). The build sequence doesn't "
            "change, excavate, base, sand, lay, restrain, finish, but the number of compaction passes and whether a drainage pipe gets "
            f"worked into the base often does, which is why we test the soil on site rather than quoting one base depth for every lot in "
            f"the same town. {post('tree-roots-under-driveway-florida', 'Our guide to tree roots under a driveway')} covers a different "
            "soil-related installation question worth checking on a lot with mature trees nearby.</p>"),
    ])
    faqs = [faq("What's the difference between the paver base and the bedding sand?",
                "The base is 4 to 6 inches of compacted aggregate that carries the actual load and is checked against a density standard before anything else goes down. Bedding sand is a thin, 1-inch, uncompacted layer on top of that base that lets each paver settle in evenly as it's laid; the two layers do different jobs and neither substitutes for the other."),
            faq("Can crushed concrete be used under pavers in Florida?",
                "Yes. Florida's transportation department allows crushed concrete recycled from old pavement to be used as base and aggregate material, and it's a common, locally available option rather than a lesser substitute, as long as it's a well-graded material that compacts to the required density."),
            faq("How many inches of compacted base do pavers need?",
                "A residential driveway needs at least 6 inches of compacted aggregate over well-drained soil, 2 to 4 inches more where the ground stays wet; a patio or walkway needs roughly 4 inches on the same well-drained soil, since it never carries the load a parked car does."),
            faq("What tool compacts the base and the finished paver field?",
                "A plate compactor, typically rated around 7,000 lbf for this kind of work, runs over each 4-to-6-inch lift of base material before the next lift goes down, then makes a final pass over the laid pavers once joint sand has been swept in."),
            faq("Is a paver driveway usable right after installation, unlike concrete?",
                "Yes. A paver field is load-ready as soon as the joint sand is compacted and the final compactor pass is done, since the interlock between units carries the load rather than a cured bond. Concrete, by comparison, needs a multi-day cure before it can take regular traffic.")]
    related = [("/paver-driveways/", "Paver driveways"), ("/paver-patios/", "Paver patios & walkways"),
               ("/pool-deck-pavers/", "Pool deck pavers"), ("/paver-driveway-cost/", "Paver driveway cost guide"),
               ("/blog/why-pavers-sink-in-florida/", "Why pavers sink, and the fix")]
    return page("/blog/paver-installation-process-florida/", "post",
                "How Are Pavers Installed? Florida Base to Finish",
                "How pavers are installed in Florida, step by step: base depth, crushed concrete, compaction standards, bedding sand and edge restraint, October 2026.",
                "How Pavers Are Installed in Florida: Base, Bedding Sand and Compaction",
                capsule("Pavers are installed in a fixed sequence: excavate, compact a 4-to-6-inch aggregate base to 98 percent standard "
                        "Proctor, screed 1 inch of bedding sand, lay and cut the units, lock the field with edge restraint, then sweep "
                        "and compact joint sand. As of October 2026, a paver field is ready for use as soon as that last compactor pass "
                        "is done, with no curing wait the way a poured driveway needs across Greater Orlando and Sarasota-Manatee."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts3", "icpi-ts5", "nrcs-myakka-osd", "nrcs-candler-osd",
                         ("FDOT, recycled materials and crushed concrete FAQ", "https://www.fdot.gov/materials/administration/resources/library/issues-trends/recycling-faqs.shtm")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="paver-driveways",
                image=pid, form=False)


def p_artificial_turf_installation_process():
    pids = for_service("artificial-turf", 2)
    pid = pids[1] if len(pids) > 1 else (pids[0] if pids else None)
    body = "".join([
        sec("How Is Artificial Turf Installed in Florida, Step by Step?",
            f"<p>A {svc('artificial-turf', 'synthetic turf')} installation runs through the same six stages whether it's covering a "
            "full front lawn, a pet run or a narrow accent strip between pavers: remove the old lawn, grade and compact a washed-rock "
            "base, cap any irrigation in the footprint, roll out and seam the turf, apply infill, then anchor every edge and seam. "
            "Florida's 2026 turf standard sets rules for several of those steps that don't apply to a lawn installed the same way in "
            f"most other states.</p>"
            + (photo(pid, "A manicured artificial lawn runs beside a covered patio, the finished result once infill is brushed in and the perimeter is anchored.") if pid else "")),
        sec("What Base Material Does Florida's Turf Rule Require?",
            f"<p>The subgrade has to be washed crushed rock or crushed concrete, with the fines removed before installation so they "
            "can't bind together and seal the ground the way a sidewalk base is built to do, since that would defeat the permeability "
            f"turf is required to keep ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}). That requirement is state law, not a build "
            "preference a crew can skip to save a trip: a base laid with ordinary compacted fill or road base with fines mixed in won't "
            "drain the way the rule requires, no matter how well the turf on top of it is installed.</p>"),
        sec("Does Artificial Turf Need a Weed Barrier Underneath?",
            "<p>Often, though it's the one step in the sequence that's a build preference rather than a rule. A fabric weed barrier goes "
            "down between the base and the subgrade below it, with seams overlapped 6 to 12 in and secured with landscape staples, and "
            f"it's commonly skipped specifically on pet-area turf, since a solid fabric layer can trap moisture and odor underneath the "
            f"turf rather than letting it drain through ({ext('https://www.rcpblock.com/installation-artificial-turf.html', 'RCP Block & Brick, artificial turf installation')}). "
            "A lawn panel in a yard with a known weed problem benefits from the barrier most; a pet run generally does better without "
            "it.</p>"),
        sec("How Are Turf Seams Joined?",
            "<p>Two methods do the job: nailing the seam directly, with fasteners spaced 1 to 2 in apart along the joint, or taping it "
            "from underneath, where the turf is folded back, seaming tape is laid flat on the base with a few inches left to stick to "
            "each piece, and the two edges are pressed together over the adhesive. Whichever method is used, installers line up the "
            "pile's grain direction across every seam first, since turf laid with the nap running opposite directions reads as a visible "
            f"stripe even once the seam itself is tight ({ext('https://www.rcpblock.com/installation-artificial-turf.html', 'RCP Block & Brick')}).</p>"),
        sec("How Is Turf Nailed Down at the Perimeter?",
            "<p>Perimeter nails typically go in every 3 to 4 in around the full edge of the turf area, driven just deep enough to hold "
            "the backing flat without punching through it, since a nail set too deep leaves a small dip that shows as a low spot once "
            f"foot traffic finds it ({ext('https://www.rcpblock.com/installation-artificial-turf.html', 'RCP Block & Brick')}). Florida's "
            "turf rule adds its own requirement on top of that manufacturer spec: edges and seams have to be anchored against wind and "
            f"flooding specifically, which in practice means a tighter nail spacing at the perimeter than the open field needs "
            f"({src('rule62-308-100-text', 'DEP Rule 62-308.100')}).</p>"),
        sec("How Is Infill Applied, and What Infill Does Florida Allow?",
            "<p>Infill is spread with a drop spreader once the turf is seamed and nailed, then worked upright and down into the pile "
            "with a power broom so the blades stand rather than mat flat. Florida's material rule limits what can go into that spreader "
            "to natural options, clean silica sand, rock, shell or coated silica sand, and bars rubber infill everywhere except inside "
            f"the footprint of playground equipment, a narrower list than many turf products ship with by default ({src('rule62-308-100-text', 'DEP Rule 62-308.100')}).</p>"),
        sec("How Long Does a Turf Installation Take?",
            "<p>Most of the schedule goes into removal, grading and the compacted base, not into rolling out and seaming the turf "
            "itself, which is usually the fastest single stage once the site is ready for it. A standard quarter- to half-acre lawn "
            "typically finishes in a few days once the old sod is out, while a narrow side yard or a layout with a lot of cutting around "
            f"beds and a pool deck can take longer than its square footage suggests. {svc('artificial-turf', 'Our artificial turf page')} "
            "covers how the sequence shifts between a lawn, a pet area and a putting green.</p>"),
        sec("Say You're Installing Turf Between Pavers on a Pool Deck in Sarasota",
            f"<p>A narrow turf accent strip inside a {city('sarasota')} pool deck's paver field follows the same base and anchoring "
            "rule as a full lawn, washed-rock subgrade, perimeter nailing, state-compliant infill, but ties into the paver field's "
            "existing edge restraint instead of needing its own perimeter restraint cut into open ground. That's a narrower, more "
            "detail-heavy job than an open lawn of the same square footage, since every cut edge against a paver course has to land "
            f"tight and stay anchored despite pool splash-out and foot traffic concentrated along that one strip. {post('artificial-turf-for-dogs-florida', 'Our guide to turf for dogs')} "
            "covers how the base and infill shift again for a pet-focused installation.</p>"),
    ])
    faqs = [faq("Does artificial turf need a weed barrier in Florida?",
                "Often, though it's a build choice rather than a state requirement. A fabric barrier with overlapped seams goes between the base and the subgrade and helps on a lawn panel in a yard with a known weed problem, but it's commonly skipped on pet-area turf since a solid fabric layer can trap moisture and odor rather than letting it drain through."),
            faq("How far apart are the nails that hold turf down?",
                "Perimeter nails typically go in every 3 to 4 inches around the full edge of the turf area, driven just deep enough to hold the backing flat without punching through it. Florida's turf rule also requires every edge and seam to be anchored against wind and flooding, on top of the manufacturer's own spacing spec."),
            faq("Do turf seams need glue, nails or tape?",
                "Either nails spaced 1 to 2 inches apart along the joint or seaming tape applied underneath the turf and pressed together over adhesive. Both methods work; what matters more is lining up the pile's grain direction across the seam first, since mismatched nap direction shows as a visible stripe even with a tight seam."),
            faq("What infill can be used under artificial turf in Florida?",
                "Clean silica sand, rock, shell or coated silica sand only. Rubber infill is barred everywhere on a residential lot except inside the footprint of playground equipment, which is narrower than what many turf products ship with by default."),
            faq("How long does it take to install an artificial turf lawn?",
                "Most of the schedule goes into removal, grading and the compacted base rather than laying the turf itself, which is usually the fastest stage. A standard quarter- to half-acre Florida lawn typically finishes in a few days once the old sod is out and the site is ready.")]
    related = [("/artificial-turf/", "Artificial turf"), ("/artificial-turf-cost/", "Artificial turf cost guide"),
               ("/compare/artificial-turf-vs-sod/", "Artificial turf vs. sod"),
               ("/blog/artificial-turf-for-dogs-florida/", "Artificial turf for dogs in Florida"),
               ("/blog/how-to-clean-artificial-turf/", "Cleaning and maintaining artificial turf")]
    return page("/blog/artificial-turf-installation-process/", "post",
                "Artificial Turf Installation Steps for Florida Yards",
                "How artificial turf is installed in Florida, step by step: base material, weed barrier, seaming, nail spacing and allowed infill, October 2026.",
                "How Artificial Turf Is Installed in Florida",
                capsule("Artificial turf installation in Florida runs through six stages: removal, a washed-rock base, irrigation "
                        "capping, seaming, infill and perimeter anchoring. As of October 2026, state Rule 62-308.100 requires a "
                        "permeable crushed-rock or crushed-concrete subgrade and limits infill to natural sand, rock or shell, rules "
                        "that apply the same way across Greater Orlando and Sarasota-Manatee."),
                body, faqs=faqs,
                sources=["rule62-308-100-text", "flrules62-308-100",
                         ("RCP Block & Brick, artificial turf installation", "https://www.rcpblock.com/installation-artificial-turf.html")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf",
                image=pid, form=False)


def p_pavers_over_existing_concrete():
    pids = for_service("pool-deck-pavers", 1)
    pid = pids[0] if pids else None
    body = "".join([
        sec("Can You Put Pavers Over Existing Concrete?",
            f"<p>Yes, on a driveway, patio or pool deck, as long as the slab underneath is sound: not actively cracking, not settled "
            "into a void and not heaving from a root or frost issue. Two different methods do it, an overlay on a thin bedding-sand "
            "system for a surface that still has to carry vehicle loads, or a mortar-set installation for a pedestrian-only area, and "
            "picking the wrong one for the load the surface actually sees is the most common reason an overlay fails early.</p>"
            + (photo(pid, "Light-toned pavers surround a resort-style pool deck, the kind of surface often set as an overlay on a sound existing slab.") if pid else "")),
        sec("What Condition Does the Existing Slab Need to Be In First?",
            f"<p>A candidate slab is flat, structurally sound and free of active movement, hairline shrinkage cracks that aren't tied "
            "to settlement are fine, but a panel that's sunk into a void, heaved by a root, or cracked into several independently "
            "moving pieces isn't, since an overlay reads every one of those flaws straight through to the new surface rather than "
            f"hiding them. {svc('concrete-repair', 'Our concrete repair page')} covers how we judge whether a slab is a repair "
            "candidate or needs to come out before anything goes over it.</p>"),
        sec("Overlay vs. Mortar-Set: What's the Difference, and Which One Carries a Car?",
            "<p>The two methods aren't interchangeable, and the difference comes down to what's allowed to sit on top of the finished "
            "surface.</p>"
            + table("Paver-over-concrete methods compared", ["Method", "How it's built", "Load it's rated for"],
                    [["Overlay (bedding sand)", "A new or rehabilitative layer of pavers and bedding sand over the existing concrete or asphalt base", "Pedestrian and vehicular areas, including driveways"],
                     ["Mortar-set (thick bed or thin-set)", "Pavers set directly on a latex-fortified mortar bed or thin-set over the cured slab", "Pedestrian traffic only, not rated for vehicles"]],
                    f"Guide specifications from the Concrete Masonry & Hardscapes Association, the industry body for paver construction standards ({ext('https://www.cmha.org/resource/pav-gsp-006/', 'CMHA PAV-GSP-006, interlocking pavement overlay')}; "
                    f"{ext('https://www.cmha.org/resource/pav-gsp-010/', 'CMHA PAV-GSP-010, pavers on a mortar setting bed')}).")
            + "<p>A mortar-set installation set on a driveway anyway, carrying daily car loads it was never rated for, is a common "
              "reason bond failure and cracked units show up within a year or two on a job that otherwise looked fine the day it was "
              "finished.</p>"),
        sec("How Much Height Does a Paver Overlay Add, and Why Does That Matter at a Door?",
            "<p>An overlay's bedding layer plus the paver thickness itself typically adds somewhere between an inch and two to the "
            "existing surface, nowhere near a full excavated base's buildup, but still enough to matter at a garage door, a threshold "
            "or a pool's coping line. We check that added height against every nearby door, the garage door's swing clearance and the "
            "coping or equipment pad before committing to an overlay, and where the buildup would leave a door dragging or a deck "
            "sitting proud of the coping, a thinner bedding system or shaving the old slab down slightly solves it without abandoning "
            "the overlay approach altogether.</p>"),
        sec("Can Pavers Go Over an Existing Driveway?",
            f"<p>Yes, using the overlay method rated for vehicle loads rather than the pedestrian-only mortar-set system, since a "
            "driveway carries the heaviest, most repetitive load any paved residential surface sees. The existing driveway slab still "
            f"has to meet the same soundness bar as any other overlay candidate, and {svc('paver-driveways', 'our paver driveway page')} "
            "covers the base-building detail for a ground-up installation where tearing out the old concrete turns out to be the "
            "better call instead.</p>"),
        sec("Can Pavers Go Over an Existing Pool Deck?",
            f"<p>Often, and it's one of the more common overlay jobs in both service areas, since a pool deck's concrete frequently "
            "stays structurally sound long after its surface has worn, pitted or started holding water. The height buildup question "
            "matters more here than almost anywhere else on a property, since the finished paver surface has to meet the pool's coping "
            f"cleanly rather than sitting above or below it. {svc('pool-deck-pavers', 'Our pool deck pavers page')} covers that coping-"
            "height detail specifically; this guide is about whether an overlay is feasible at all, across driveways, patios and pool "
            "decks alike.</p>"),
        sec("Does a Paver Overlay Over Existing Concrete Still Need a Permit?",
            "<p>Often yes, since most jurisdictions in our service areas treat new paver installation as its own permitted scope "
            "regardless of what's underneath it, the same engineering or zoning review a ground-up paver driveway or patio needs. "
            f"{post('orange-county-orlando-driveway-patio-permits', 'Our Orange County permit guide')} and "
            f"{post('sarasota-county-driveway-patio-permits', 'our Sarasota County permit guide')} cover what each department asks for "
            "on new paver work; checking before scheduling an overlay avoids finding out about a required permit after the crew has "
            "already started.</p>"),
        sec("Say You're Overlaying a 1990s Driveway in Clermont",
            f"<p>A plain concrete driveway poured in a 1990s {city('clermont')} subdivision, cracked only along its original control "
            "joints and showing no settlement, is a reasonable overlay candidate rather than a tear-out. The existing slab is pressure "
            "washed and checked for hollow or loose sections, the overlay's bedding system is set to meet the garage door's clearance "
            "and the existing driveway apron, and the vehicle-rated overlay method goes down rather than a mortar-set system, since the "
            f"driveway still carries daily car traffic. {a('/paver-driveway-cost/', 'Our paver driveway cost guide')} breaks down how an "
            "overlay's pricing compares with tearing out the old slab and starting from bare ground.</p>"),
    ])
    faqs = [faq("Can pavers be installed over a cracked concrete driveway?",
                "Only if the cracking is cosmetic, hairline shrinkage cracks that aren't tied to a settled void, rather than active movement. A slab that's sunk, heaved by a root or cracked into independently moving pieces reads straight through an overlay and is usually worth repairing or replacing first."),
            faq("Is installing pavers over concrete cheaper than tearing it out first?",
                "Often, since an overlay skips demolition and disposal costs entirely and adds only the bedding system and paver material on top of what's already there. The savings depend on the existing slab being sound enough to build on; a slab that needs repair before an overlay can go down narrows that cost gap."),
            faq("How much height does a paver overlay add to a surface?",
                "Typically an inch or two once the bedding layer and the paver thickness are both counted, far less than a full excavated base adds. That buildup still has to be checked against nearby doors, a garage door's clearance and a pool's coping line before the overlay is finalized."),
            faq("Can you drive a car on pavers installed over an existing driveway?",
                "Yes, but only with the overlay method built for vehicle loads, not the mortar-set system used on pedestrian-only surfaces. Setting a mortar-set installation under daily car traffic is a common reason for early bond failure and cracked units."),
            faq("Does a paver overlay over existing concrete need a permit?",
                "Often, since most jurisdictions in Greater Orlando and Sarasota-Manatee review new paver installation under the same permit a ground-up paver driveway or patio needs, regardless of what sits underneath it. Confirming with the local building or engineering department before scheduling the work avoids a mid-job surprise.")]
    related = [("/pool-deck-pavers/", "Pool deck pavers"), ("/paver-patios/", "Paver patios & walkways"),
               ("/paver-driveways/", "Paver driveways"), ("/concrete-repair/", "Concrete repair & resurfacing"),
               ("/compare/resurface-vs-replace-concrete/", "Resurface or replace concrete")]
    return page("/blog/pavers-over-existing-concrete/", "post",
                "Pavers Over Existing Concrete: When It Works",
                "Can you put pavers over existing concrete? Overlay vs. mortar-set methods, added height at doors and coping, and permits, as of October 2026.",
                "Can You Put Pavers Over Existing Concrete? Driveways, Patios and Pool Decks",
                capsule("Pavers can go over existing concrete on a driveway, patio or pool deck as long as the slab is sound, using a "
                        "vehicle-rated overlay system for driveways or a mortar-set system for pedestrian-only areas. As of October "
                        "2026, the added height typically runs an inch or two, which matters most where the surface meets a door "
                        "threshold or a pool's coping line."),
                body, faqs=faqs,
                sources=["icpi-ts2",
                         ("CMHA PAV-GSP-006, interlocking concrete pavement overlay", "https://www.cmha.org/resource/pav-gsp-006/"),
                         ("CMHA PAV-GSP-010, concrete pavers on a mortar setting bed", "https://www.cmha.org/resource/pav-gsp-010/")],
                related=related, crumbs=[("Blog", "/blog/")], published="2026-10-01", service="pool-deck-pavers",
                image=pid, form=False)


def get_pages():
    return [p_concrete_pad_for_rv_or_boat_parking(), p_shed_slab_guide_florida(), p_concrete_driveway_installation_process(),
            p_paver_installation_process_florida(), p_artificial_turf_installation_process(), p_pavers_over_existing_concrete()]
