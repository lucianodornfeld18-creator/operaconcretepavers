# -*- coding: utf-8 -*-
"""Service pages: concrete driveways, and sidewalks & walkways (including right-of-way sidewalk sections)."""
from _data import SERVICES
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, cs, post, compare, src, ext, price, per, price_note, contact, photo, offer
from _photos import for_service


def driveways():
    K = "concrete-driveways"
    pids = for_service(K, 3)
    body = "".join([
        sec("What a Concrete Driveway Job Covers",
            "<p>Most of what we quote under this service is a new driveway on a lot that never had one, a full tear-out-and-replace on a cracked or sunken slab, or a widening that adds a parking pad or a second strip next to an existing drive. "
            "The job runs from the edge of the garage or the house out to the street, which in practice means it crosses two different kinds of ground: the private part of the lot, where you set the layout, and the apron in the public right-of-way, where the city or county sets the rules. "
            f"A short extension to park a boat or a trailer is the same trade but a different scope than a full rebuild, and {a('/concrete-driveway-cost/', 'pricing runs differently for each')}. "
            f"If the goal is interlocking pavers instead of a poured slab, that's a separate build with its own base spec; see {svc('paver-driveways', 'paver driveways')}.</p>"),
        sec("Concrete or Pavers: When a Slab Still Makes Sense",
            f"<p>Concrete stays the lower-cost option for a straight driveway rebuild, running roughly {price('concrete-driveway')} per square foot installed against {price('paver-driveway')} for pavers, and it pours as one continuous surface with no joint sand to top off later. "
            "It makes the most sense on a budget-driven replacement, a rental or investment property, a long straight run with no curves to work around, or a subdivision where the HOA has no finish requirement beyond color. "
            "Pavers earn their higher price where a sunken section needs to disappear without a visible patch, where a master-planned community specifies a paver or decorative finish, or where the driveway wraps a curve that a slab would have to joint heavily to handle. "
            f"The full trade-offs, including how each one takes a Florida storm, are in {compare('pavers-vs-concrete-driveway', 'our pavers vs. concrete driveway comparison')}.</p>"),
        sec("The Concrete Spec We Build To",
            "<p>Florida's residential code sets a bare floor for slab thickness that isn't meant for a surface carrying a car every day, so our driveway spec starts above it rather than at it.</p>"
            + table("Driveway concrete spec, standard car traffic vs. heavy vehicles", ["Element", "Daily cars and light trucks", "RVs, boats and heavy trailers"],
                    [["Thickness", "4 in.", "5–6 in."],
                     ["Strength", "3,000–4,000 psi", "3,000–4,000 psi"],
                     ["Reinforcement", "Fiber mesh standard", "Wire mesh or rebar, by request"],
                     ["Control joints", f"Every 8–12 ft, cut a quarter of the slab's depth ({src('nrmca-cip6', 'NRMCA CIP 6')})", "Same spacing rule, laid out around the heavier panels"],
                     ["Vapor retarder", f"6-mil poly under the slab, 6-in. laps, where code calls for it ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')})", "Same"],
                     ["Finish", "Broom standard; exposed aggregate or stamped optional", "Broom, for traction under a loaded trailer"]],
                    "Our build standard, above the code floor of 3½ in. for an ordinary slab on ground.")
            + "<h3>Why a Standard Slab Isn't the Right Call for a Boat Trailer</h3>"
            f"<p>A 4-inch driveway is sized for the distributed weight of a car or a pickup, not for the narrow, concentrated load a loaded boat trailer or an RV's jacks put on one spot. Going to 5 or 6 inches spreads that point load over more concrete, which does more for a heavy, narrow load than adding strength to the mix alone. Florida's code table ties required strength to weathering exposure for porches, carports and garage floors ({src('fbcr-2020-ch4', 'FBC Residential Table R402.2')}); interior slabs need 2,500 psi at minimum, and we build driveways well above that floor regardless.</p>"
            + (photo(pids[1], "Smooth concrete driveway in front of a house with two garage doors") if len(pids) > 1 else "")),
        sec("How the Job Runs, Start to Finish",
            "<p>A driveway replacement and a brand-new pour follow the same order; a replacement just adds a demolition day up front.</p>"
            + steps([("Site visit and layout.", "We check the subgrade, the slope toward the street and the house, any tree roots in the path, and what the city or HOA will require before a shovel moves."),
                     ("Permits and the Notice of Commencement.", f"Where the apron falls in the right-of-way, that's a separate permit from any work on the rest of the lot. On jobs over $2,500, Florida's lien law also calls for a recorded Notice of Commencement before work starts ({src('fs713-13', 'F.S. 713.13')})."),
                     ("Demolition, if replacing an existing slab.", "The old concrete comes out and gets hauled off, which is usually priced and listed as its own line."),
                     ("Grading and base.", "Any soft, wet or organic material comes out, and compacted fill goes in, in lifts, graded to carry water away from the garage rather than toward it."),
                     ("Forming, pour and finish.", "Forms set the layout, the truck pours, and the crew screeds, floats and finishes the surface before cutting control joints while the concrete is still workable."),
                     ("Curing and walkthrough.", "The surface stays moist, by curing compound or wet cure, for at least 3 days before we hand the job back and go over when it's ready for foot and vehicle traffic.")])),
        sec("What Florida Ground and Weather Do to a Driveway",
            "<p>Three regional conditions shape how we build, more than the concrete mix itself does.</p>"
            f"<p><strong>The subgrade holds water on a schedule.</strong> A lot of both service areas sits on flatwoods soil, Myakka, Smyrna, Immokalee and similar series, where the water table can sit within 18 inches of the surface for part of the year ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}). Soil in that condition in August behaves differently than the same lot in April, so we test and compact rather than assume one pass of the plate compactor settled it.</p>"
            f"<p><strong>Heat and wind dry the surface faster than the slab gains strength.</strong> Hot-weather guidance flags concrete at 95°F or an evaporation rate above 0.2 pounds per square foot per hour as the point where plastic shrinkage cracking becomes likely ({src('aci-faq-maxtemp', 'ACI')}; {src('aci-ci-evap-2007', 'Concrete International, 2007')}). A still, hot Central Florida afternoon crosses that line easily, which is why we schedule pours early and keep sprinkling water on a stiffening surface off the table entirely ({src('nrmca-cip12', 'NRMCA CIP 12')}).</p>"
            "<p><strong>The rainy season has a start date, roughly.</strong> Orlando averages 51.45 inches of rain a year and Sarasota–Bradenton about 49, most of it between late May and mid-October, with NWS Melbourne putting Central Florida's median wet-season onset at May 27 "
            f"({src('ncei-annual-prcp', 'NOAA 1991–2020 normals')}; {src('nws-mlb-wetdry', 'NWS Melbourne')}). A base left uncovered ahead of a 3 p.m. storm, or a slab rained on before it sets, is a scheduling problem we plan around rather than something to fix afterward.</p>"
            "<p>A fourth factor matters more for repairs than new pours: a driveway that develops a slow, uneven dip almost always traces back to a soft spot in the base or a drainage path that changed, not to the geological event Florida law defines as a catastrophic ground cover collapse, which requires a sudden, visible depression and structural damage "
            f"({src('fs-627-706', 'F.S. 627.706')}). Orange County sits on the state's broader list of counties with concentrated sinkhole claims; Sarasota and Manatee do not ({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). Either way, settlement is the far more common explanation, and it's fixable.</p>"
            + (photo(pids[2], "Broom-finish concrete driveway with cut control joints leading to a garage") if len(pids) > 2 else "")),
        sec("What a New Driveway Costs",
            f"<p>As of October 2026, Florida market data puts a new concrete driveway at {price('concrete-driveway')} per square foot installed, with a typical job landing nearer {price('concrete-driveway', True)}. Angi's Orlando figures put the average project around $6,490, inside that band ({src('angi-driveway-orlando', 'Angi, Orlando, May 2026')}). "
            "A plain 400-square-foot two-car driveway at the published range works out to roughly $2,400 to $6,000 before demolition; tearing out an old one typically adds $3 to $8 per square foot on top. "
            f"Thickness, reinforcement, finish and demolition each move the number, which is exactly what {a('/concrete-driveway-cost/', 'the concrete driveway cost guide')} breaks down by size and scope, with worked examples for a one-, two- and three-car job.</p>"),
        sec("Permits and HOA Approval for a Driveway",
            "<p>The section between the sidewalk and the street is almost never just yours to build however you like. Every jurisdiction we checked across Greater Orlando and Sarasota–Manatee requires a permit for work on the apron, even in cities that waive a building permit for small private-lot jobs under Florida's 2026 exemption law. "
            f"Orlando's standard calls for a 6-inch, 3,000-psi apron with a break joint at the property line ({src('orlando-esm', 'City of Orlando Engineering Standards Manual')}); Orange County's lot-grading policy requires the same 6-inch, non-steel-reinforced section through the right-of-way, including the sidewalk crossing ({src('orange-lot-grading', 'Orange County Residential Lot Grading Policy')}); and Manatee County specifies 6 inches from the edge of pavement to the right-of-way line on every residential driveway permit ({src('manatee-driveway-application', 'Manatee County Driveway & Culvert Application')}). "
            f"Florida law does bar a city or county from requiring a state or local license specifically for driveway installation ({src('fs489-117', 'F.S. 489.117')}); that's a licensing rule, not a permit exemption, and the permit still applies. Homeowners can check any contractor's license status directly through {src('dbpr-search', 'DBPR’s license search')}.</p>"
            f"<p>HOAs add a second layer in master-planned communities, and since 2026 a Florida HOA can't require a building permit to already be issued before it will review your application ({src('fs720-3035', 'F.S. 720.3035')}). The {a('/permits/', 'permits and HOA hub')} has the jurisdiction-by-jurisdiction table, and the county guides for {post('orange-county-orlando-driveway-patio-permits', 'Orlando and Orange County')} and {post('sarasota-county-driveway-patio-permits', 'Sarasota, Venice and North Port')} go through the local paperwork in detail.</p>"),
        sec("Caring for a New Driveway",
            "<p>Once the slab is handed over, upkeep is mostly about keeping the joints and the drainage doing what they were built to do. Sweep soil and mulch out of the control joints before the rainy season builds, since a packed joint can't shed water the way an open one does. "
            "Check sprinkler heads against the new edge; a head that cleared an old garden bed can land squarely on fresh concrete, and repeated overspray both works against a compacted base and leaves mineral staining on the surface over time. "
            "Sealing is optional on plain concrete and runs $1 to $3 per square foot in national cost data when it's added; it's worth doing before the first wet season if the finish is stamped or exposed aggregate rather than plain broom. "
            f"A hairline crack along a joint is the slab doing what it was designed to do; a crack that wanders diagonally across a panel, or a corner that's noticeably lower than the rest, is worth a call. More in {post('should-you-seal-a-concrete-driveway-florida', 'whether a Florida driveway needs sealing')} and {post('concrete-driveway-cracks-florida', 'which driveway cracks are normal')}.</p>"),
        sec("How Do You Pick the Best Concrete Driveway Contractor Near You?",
            "<p>Searching for the best concrete driveway contractor near you turns up a long list of businesses that all say roughly the same thing, so the shortlist comes down to what each one puts in writing rather than what's on the homepage. A handful of questions separate a comparable bid from a cheaper one that's missing a step:</p>"
            + ul(["Ask for thickness, strength, joint spacing and reinforcement in writing, not just a square-foot price. A number without a spec can't be compared to another bid.",
                  "Ask who applies for the apron or right-of-way permit and whether the fee is included. If nobody mentions it, that's a gap, not a savings.",
                  f"Ask about the base: what gets removed, what gets compacted, and how thick it ends up. This is where a low bid most often cuts a corner that doesn't show until the first wet season ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')}).",
                  f"Check the business on {src('dbpr-search', 'DBPR’s license search')} and ask which category, if any, the quoted scope falls under.",
                  "Ask how the crew handles a hot or rainy pour day. A contractor who hasn't thought about it hasn't poured many Florida driveways."])
            + f"<p>{post('how-to-choose-a-concrete-contractor-orlando', 'Ten criteria for choosing a concrete contractor in Orlando')} goes through this in more depth, and {post('driveway-apron-and-right-of-way-florida', 'who owns the driveway apron')} is worth reading before the first estimate if the lot backs onto a public street.</p>"),
        sec("Concrete Driveways by City",
            f"<p>Permit rules, soil and HOA review change from one town to the next even when the concrete spec doesn't, so we keep a page for each: {cs('orlando', K, 'concrete driveways in Orlando')}, {cs('kissimmee', K, 'Kissimmee')}, "
            f"{cs('sarasota', K, 'Sarasota')} and {cs('lakewood-ranch', K, 'Lakewood Ranch')}. If your town isn't one of those four, {contact('tell us the address')} and we'll confirm which crew and which local rules apply.</p>"),
    ])
    faqs = [
        faq("How long before I can drive on a new concrete driveway?",
            "Concrete is rated by the strength it reaches at 28 days, which is also roughly when a slab reaches its full design strength, though it carries foot and car traffic well before that. Curing itself has to continue at least 3 days once finishing is done, keeping the surface moist rather than letting it dry out in the Florida sun. We give each homeowner a specific date for driving on it based on that day's mix, pour time and weather instead of one fixed number for every job."),
        faq("How thick should a concrete driveway be in Florida?",
            "4 inches is standard for cars and light trucks; 5 to 6 inches is the move for RVs, boat trailers or anything else that concentrates weight on a narrow footprint. Several of the counties we build in also require a thicker, 6-inch section specifically where the driveway crosses the right-of-way, regardless of what the private portion is poured to, so the apron and the rest of the slab aren't always the same thickness."),
        faq("How long does a concrete driveway last in Florida?",
            "There's no single number that applies everywhere, because what shortens a driveway's service life is almost always something under it, not the concrete itself. A base that was compacted in lifts and tested, joints that were cut to the right depth and spacing, and grading that keeps water moving away from the slab are what keep a driveway from needing attention for a long time. A soft subgrade that was never corrected, or a root from a tree that wasn't there at pour time, is what shows up first."),
        faq("Do you use rebar, wire mesh or fiber in driveways?",
            "Fiber mesh is our standard reinforcement for a typical 4-inch driveway. Wire mesh or rebar is available on request, usually for heavier-use slabs, but it's worth knowing what reinforcement actually does: NRMCA's guidance is direct that wire mesh does not prevent cracking, it just holds a crack together once it forms. Control joints, not the reinforcement, are what decide where the slab cracks."),
        faq("How long does it take to replace a concrete driveway?",
            "Demolition and haul-off usually take a day, forming and base work another, and the pour and finish a third, with the schedule stretching for a larger driveway or one with a lot of landscaping to protect. The slab then needs to cure before it's back in daily use. The full walk-through of the process, step by step, is in our post on how a concrete driveway is installed."),
        faq("Do you remove and haul away the old driveway?",
            "Yes, on a replacement job. Demolition and disposal are priced and listed as their own line on the estimate rather than folded into the per-square-foot rate, since the cost depends on the old slab's thickness and whether it has reinforcement in it. National cost data puts removal at roughly $3 to $8 per square foot, and Angi's Orlando figures run close to the top of that range."),
    ]
    related = [("/concrete-driveway-cost/", "Concrete driveway cost guide"),
               ("/compare/pavers-vs-concrete-driveway/", "Pavers vs. concrete driveway"),
               ("/compare/concrete-driveway-finishes/", "Broom vs. exposed aggregate vs. stamped"),
               ("/blog/concrete-driveway-installation-process/", "How a concrete driveway is installed, step by step"),
               ("/blog/driveway-apron-and-right-of-way-florida/", "Who owns the driveway apron"),
               ("/central-florida/", "Greater Orlando service area"),
               ("/sarasota-manatee/", "Sarasota–Manatee service area")]
    return page("/concrete-driveways/", "service", "Concrete Driveways in Orlando & Sarasota, FL", "New, replacement and widened concrete driveways in Greater Orlando and Sarasota–Manatee: 4–6 in. slabs, control joints every 8–12 ft, and 2026 Florida pricing.",
                "Concrete driveways poured for Florida soil, heat and rain",
                capsule(f"A new concrete driveway in Greater Orlando or Sarasota–Manatee runs {price('concrete-driveway')} per square foot installed, as of October 2026, poured 4 inches thick for daily traffic or 5 to 6 inches for RVs, boats and heavy trailers. We size the base, joint spacing and cure schedule to the county's permit rules and to sandy soil that holds water for months at a time."),
                body, faqs=faqs, sources=["homeguide-concrete-driveway", "angi-driveway-orlando", "nrmca-cip6", "fbcr-2020-ch5", "fbcr-2020-ch4", "aci-faq-maxtemp", "aci-ci-evap-2007", "nrmca-cip12",
                                          "nrcs-myakka-osd", "ncei-annual-prcp", "nws-mlb-wetdry", "fs-627-706", "fl-senate-2011-104", "orlando-esm", "orange-lot-grading", "manatee-driveway-application",
                                          "fs489-117", "dbpr-search", "fs713-13", "fs720-3035"],
                related=related, crumbs=[("Concrete", "/concrete/")], crumb="Concrete driveways", service=K,
                hero_photo=pids[0] if pids else None, offer=offer(SERVICES[K]["price"]), eyebrow="Concrete · Greater Orlando & Sarasota",
                howto=("How a Concrete Driveway Is Built", [("Site visit and layout.", "Check subgrade, slope and tree roots; confirm what the city and HOA require."),
                                                             ("Permits and Notice of Commencement.", "Apply for the right-of-way or engineering permit and record the Notice of Commencement on jobs over $2,500."),
                                                             ("Demolition, if replacing a driveway.", "Remove and haul off the old slab."),
                                                             ("Grading and base.", "Strip soft or organic material and compact clean fill in lifts, graded away from the house."),
                                                             ("Forming, pour and finish.", "Set forms, place and finish the concrete, and cut control joints while it is still workable."),
                                                             ("Curing and walkthrough.", "Keep the surface moist for at least 3 days and review care and driving timelines with the homeowner.")]))


def walkways():
    K = "concrete-walkways"
    pids = for_service(K, 3)
    body = "".join([
        sec("What a Walkway or Sidewalk Job Covers",
            "<p>This service covers the narrower concrete work around a house: a front walk from the driveway to the door, a side-yard path to a gate or a trash can pad, and sidewalk work, both the section on private property and the stretch that sits in the public right-of-way. "
            "It also covers section repairs, where one slab of an existing walk has cracked, heaved or sunk and the rest is still sound. "
            f"A full driveway rebuild is a related but separate job with its own thickness and joint spec; see {svc('concrete-driveways', 'concrete driveways')}. "
            f"If the plan is a path of individual stepping pavers through a lawn rather than a continuous poured slab, that's covered under {svc('paver-patios', 'paver patios & walkways')}.</p>"),
        sec("Private Walk or Right-of-Way Sidewalk? The Difference Changes the Spec",
            "<p>A walkway on your own lot and a sidewalk section in the public right-of-way are not the same build, even when they're poured the same week and look identical once they're finished. The private section is yours to design within setback and impervious-surface rules; the right-of-way section follows the city or county's standard, and in several of the jurisdictions we build in, that standard is thicker than an ordinary walk.</p>"
            f"<p>Orange County's lot-grading policy calls for 6 inches of non-steel-reinforced concrete anywhere a driveway crosses the right-of-way, “including the sidewalk section,” and Seminole County's driveway application uses nearly identical language for the sidewalk crossing a new driveway ({src('orange-lot-grading', 'Orange County Residential Lot Grading Policy')}; {src('seminole-driveway-app', 'Seminole County Residential Driveway Application')}). "
            f"Orlando's engineering manual says the sidewalk section through a driveway “must be at least 3000 psi concrete at least 6 inches in thickness,” even where the sidewalk on either side of that crossing is thinner ({src('orlando-esm', 'City of Orlando Engineering Standards Manual')}). "
            f"Manatee County's paver-driveway inspection sheet specifies a concrete sidewalk crossing at 4 inches thick and 5 feet wide, broom-finished, with saw cuts every 10 feet, framed from one side lot line to the other ({src('manatee-paver-driveway-inspections', 'Manatee County paver driveway inspection guidance')}). "
            f"Bradenton sets a general residential sidewalk minimum of 4 inches thick and 5 feet wide citywide ({src('bradenton-lur-4.1-access-sidewalks', 'Bradenton Land Use Regulations §4.1')}). "
            "None of that is optional once it applies: a walk built to a uniform 4 inches everywhere, with no thicker section where it meets the driveway, is the kind of detail that fails inspection on a permitted job.</p>"),
        sec("The Spec We Build To",
            "<p>Because a private front walk and a right-of-way sidewalk crossing answer to different standards, we spec them separately rather than pouring one thickness for the whole run.</p>"
            + table("Walkway and sidewalk spec by location", ["Element", "Private walk or path", "Right-of-way sidewalk or driveway crossing"],
                    [["Thickness", "4 in.", "4–6 in.; 6 in. where several counties require it at a driveway crossing"],
                     ["Width", "3–4 ft for a single-file path; 4–5 ft where two people need to pass", "5 ft is the standard in Bradenton and in Manatee's sidewalk-crossing spec"],
                     ["Strength", "2,500–3,000 psi", "3,000 psi where county right-of-way rules apply"],
                     ["Joints", f"Spaced about equal to the walk's width so panels stay close to square ({src('nrmca-cip6', 'NRMCA CIP 6')})", "Saw cuts about every 10 ft on Manatee's sidewalk-crossing spec"],
                     ["Base", f"Compacted subgrade, clean fill per FBC where soil allows ({src('fbcr-2020-ch5', 'FBC Residential Ch. 5')})", "Same, with county inspection before the pour where a permit applies"],
                     ["Finish", "Broom standard; stamped or colored to match a patio on request", "Broom finish, per the jurisdictions that specify it"]],
                    "Our build standard; confirm the exact right-of-way thickness and width with the local permit desk before a bid is final.")
            + (photo(pids[1], "Concrete paver stepping-stone path crossing a lawn toward a house entrance") if len(pids) > 1 else "")),
        sec("How a Walkway or Sidewalk Gets Built, Start to Finish",
            "<p>The sequence is shorter than a driveway's but follows the same logic: check the ground, confirm what's required, build the base, then pour.</p>"
            + steps([("Site visit and layout.", "We walk the path, note any root crossings, grade changes or a gate the walk has to clear, and flag whether any part of the run sits in the right-of-way."),
                     ("Permit check.", "A private front walk is often exempt from a building permit in our area and only needs a zoning sign-off; a right-of-way sidewalk section almost always needs a separate permit from the city or county."),
                     ("Demolition, for a repair or replacement.", "Damaged sections get cut out and removed rather than poured over."),
                     ("Forming and base.", "Forms follow the walk's final width and any curve, and the subgrade is compacted before concrete goes down."),
                     ("Pour and finish.", "The slab is poured, broomed or stamped to match an adjoining patio if requested, and joints are cut at roughly the walk's own width."),
                     ("Curing and walkthrough.", "The surface cures before regular foot traffic resumes, and we point out where joints and any color match sit relative to the house.")])),
        sec("What Florida Ground Does to a Narrow Slab",
            "<p>A walkway behaves differently from a driveway under the same ground conditions, mostly because it's narrow enough that one problem spot can affect the whole width at once.</p>"
            "<p><strong>A single root can lift an entire panel.</strong> On a wide driveway, a root under one edge can tent part of a panel while the rest stays flat. A 3- or 4-foot walk doesn't have that margin: the same root runs under the whole width, so the lift shows up edge to edge rather than as a partial tilt. Orlando, Winter Park and Sarasota each protect trees above a set trunk diameter by ordinance, and cutting into a protected root system to fix a lifted walk can need a permit of its own, not just a shovel.</p>"
            f"<p><strong>Standing water on a path people use barefoot is a bigger nuisance than the same puddle on a driveway.</strong> Flatwoods soils common across both service areas hold a water table within roughly 18 inches of the surface for part of the year ({src('nrcs-myakka-osd', 'NRCS, Myakka series')}), and a walk graded flat, instead of with a slight crown or cross-slope, is where that shows up first as standing water after an afternoon storm.</p>"
            "<p><strong>A narrow pour dries out just as fast as a wide one.</strong> The same hot-weather threshold that applies to a driveway applies to a front walk: once the evaporation rate crosses roughly 0.2 pounds per square foot per hour, the surface can dry faster than the slab underneath gains strength, and a walk poured in the open sun with no windbreak hits that line as easily as a larger pour does.</p>"),
        sec("What a Concrete Walkway Costs",
            f"<p>As of October 2026, a concrete walkway or sidewalk runs {price('concrete-walkway')} per square foot installed, with a typical job nearer {price('concrete-walkway', True)}; national data also prices a standard 4-foot-wide section at $28 to $68 per linear foot ({src('homeguide-sidewalk', 'HomeGuide, concrete sidewalk')}). "
            "A short front walk, 4 feet wide by 20 feet long, works out to about $560 to $1,360 at that per-square-foot range before any demolition of an old section. Width, thickness at a right-of-way crossing, and whether an old walk has to come out first are what move a quote from one end of the range to the other. "
            f"{a('/concrete-walkway-cost/', 'The full cost guide')} runs through more sizes and scopes.</p>"),
        sec("Permits for Walks, Sidewalks and Right-of-Way Sections",
            "<p>Whether a permit applies depends on which side of the property line the work falls on, and the answer changes by city. Clermont, for example, doesn't require a building permit for a driveway or walk on private property, only a zoning approval, while the apron and sidewalk crossing in the city right-of-way need their own application and a city inspection "
            f"({src('clermont-permit-checklists', 'City of Clermont permit checklists')}). The City of Sarasota has no published exemption for private flatwork and tells homeowners to call the Building Division when in doubt "
            f"({src('city-sarasota-bp-guidelines', 'City of Sarasota Building Permit Requirement Guidelines')}). Sarasota County requires a Right-of-Way Use Permit for any work in the county right-of-way, and its code is explicit that no walkway may be placed inside a drainage easement "
            f"({src('sarasota-county-row-permit', 'Sarasota County Right-of-Way Use Permit')}; {src('sarasota-county-124-255-culverts', 'Sarasota County Code §124-255')}). "
            f"On jobs over $2,500, Florida's lien law also requires a recorded Notice of Commencement before work starts ({src('fs713-13', 'F.S. 713.13')}); a small section repair under that threshold is exempt from most of the same lien-law paperwork, though not from any permit the city still requires "
            f"({src('fs713-02', 'F.S. 713.02')}). The {a('/permits/', 'permits and HOA hub')} has the full jurisdiction table, and {post('orange-county-orlando-driveway-patio-permits', 'Orlando and Orange County')} and {post('sarasota-county-driveway-patio-permits', 'Sarasota, Venice and North Port')} cover their counties in more depth.</p>"),
        sec("Caring for a Walkway",
            "<p>A walkway sees more foot traffic and less vehicle weight than a driveway, so upkeep leans toward keeping it level and clean rather than watching for the kind of load-related cracking a driveway deals with. Keep the joints swept clear of dirt and mulch, especially where a path runs under a tree canopy, since organic debris packed into a joint traps moisture against the edges of each panel. "
            "Walk the path after a storm or two each rainy season and look for water sitting in one spot rather than sheeting off; that's usually a sign the original grading needs a touch-up, not that the concrete has failed. "
            "A single cracked or sunken section can often be cut out and replaced on its own rather than repouring the whole run, though a color or texture match on an older walk isn't guaranteed; weathering and sun exposure change concrete's color over the years in ways a fresh batch can't always match exactly.</p>"),
        sec("Choosing a Walkway or Sidewalk Contractor",
            "<p>A walkway is a smaller job than a driveway, but the same gaps in a bid show up at this scale too, just with smaller dollar amounts attached.</p>"
            + ul(["Ask whether any part of the path falls in the right-of-way, and if so, who pulls that permit. A bid that only covers the private portion can leave a homeowner to sort out the sidewalk crossing separately.",
                  "Get the thickness and width in writing, especially at a driveway crossing, since that's the one spot several local codes set a higher standard than the rest of the walk.",
                  "If matching an existing patio's color or stamp pattern matters, ask to see a sample poured and cured rather than judging from a wet sample at the truck.",
                  "For a section repair, ask whether the existing slab will be cut on a clean joint line or just patched at the crack, since a patch at a crack tends to fail again at the same spot."]),
        ),
        sec("Walkways and Sidewalks by City",
            f"<p>The sidewalk and right-of-way rules in this service differ enough by jurisdiction that we keep a page for each town: {cs('orlando', K, 'walkways in Orlando')}, {cs('winter-garden', K, 'Winter Garden')}, "
            f"{cs('sarasota', K, 'Sarasota')} and {cs('bradenton', K, 'Bradenton')}. {contact('Send us the address')} if your town isn't on that list and we'll confirm the local rules before we quote.</p>"),
    ])
    faqs = [
        faq("How wide should a front walkway be?",
            "We usually lay out a front walk 3 to 4 feet wide, enough for one person to move comfortably with a delivery or a trash can. Where two people need to pass, or the walk serves as a main entry path, 4 to 5 feet is a better fit. A right-of-way sidewalk crossing a driveway is a separate question: several cities in our area set that section at 5 feet regardless of how wide the private walk leading to it is."),
        faq("Can you build a walkway from the driveway to the backyard or side gate?",
            "Yes, and it's one of the more common requests we get, usually for trash and recycling cans, a side-yard gate, or access to a detached garage or shed. A side path like this sits entirely on private property in most cases, which generally keeps it out of right-of-way permitting, though it may still count toward a city's impervious-surface or lot-coverage limit."),
        faq("How far apart should joints be in a concrete walkway?",
            "Roughly equal to the walk's own width, so a 4-foot-wide path gets a joint about every 4 feet, keeping each panel close to square rather than long and narrow. That's a tighter spacing than a driveway uses, because a narrow slab left in long panels is more likely to crack randomly between the cuts than a properly jointed one."),
        faq("Can you replace just one cracked section of my walkway?",
            "Usually, yes. We cut the damaged panel out at its joint lines and pour a new one in its place rather than repouring the whole run. The one caveat is color: concrete lightens and weathers over the years, so a new section poured next to a decade-old walk won't match it exactly on day one, even with the same mix design."),
        faq("Can a concrete walkway be colored or stamped to match my patio?",
            "Yes, within reason. A walkway can be integrally colored or stamped to carry a pattern through from an adjoining patio or driveway, which is a common request on a backyard project built in phases. It works best when it's planned before the first pour, since matching a stamp pattern or color on a walk poured separately, months or years later, is harder than getting it right the first time; see our stamped concrete page for the pattern and color options.")
    ]
    related = [("/concrete-walkway-cost/", "Concrete walkway cost guide"),
               ("/compare/resurface-vs-replace-concrete/", "Resurface or replace a concrete section"),
               ("/compare/concrete-driveway-finishes/", "Broom vs. exposed aggregate vs. stamped"),
               ("/blog/front-walkway-ideas-curb-appeal/", "Front walkway ideas that boost curb appeal"),
               ("/blog/tree-roots-under-driveway-florida/", "Tree roots under a driveway or sidewalk"),
               ("/central-florida/", "Greater Orlando service area"),
               ("/sarasota-manatee/", "Sarasota–Manatee service area")]
    return page("/concrete-walkways/", "service", "Concrete Walkways & Sidewalks | Orlando & Sarasota", "Front walks, side paths and right-of-way sidewalk sections in Greater Orlando and Sarasota–Manatee, built to each city's thickness rules, priced as of October 2026.",
                "Concrete walkways built for Florida yards and rights-of-way",
                capsule(f"A concrete walkway or sidewalk in Greater Orlando or Sarasota–Manatee runs {price('concrete-walkway')} per square foot installed, as of October 2026, typically 4 inches thick on private ground. Several cities in our area require a thicker, 6-inch section specifically where the sidewalk crosses a driveway, which we build to on every job that touches the right-of-way."),
                body, faqs=faqs, sources=["homeguide-sidewalk", "nrmca-cip6", "fbcr-2020-ch5", "orange-lot-grading", "seminole-driveway-app", "orlando-esm", "manatee-paver-driveway-inspections",
                                          "bradenton-lur-4.1-access-sidewalks", "nrcs-myakka-osd", "clermont-permit-checklists", "city-sarasota-bp-guidelines", "sarasota-county-row-permit",
                                          "sarasota-county-124-255-culverts", "fs713-13", "fs713-02"],
                related=related, crumbs=[("Concrete", "/concrete/")], crumb="Sidewalks & walkways", service=K,
                hero_photo=pids[0] if pids else None, offer=offer(SERVICES[K]["price"]), eyebrow="Concrete · Greater Orlando & Sarasota",
                howto=("How a Concrete Walkway or Sidewalk Is Built", [("Site visit and layout.", "Walk the path, note roots and grade changes, and flag any right-of-way section."),
                                                                       ("Permit check.", "Confirm whether the private walk and any right-of-way sidewalk crossing each need a permit."),
                                                                       ("Demolition, for a repair.", "Cut out and remove any damaged section."),
                                                                       ("Forming and base.", "Form the walk's width and compact the subgrade before the pour."),
                                                                       ("Pour and finish.", "Place and finish the concrete, matching color or stamp pattern where requested, and cut joints near the walk's own width."),
                                                                       ("Curing and walkthrough.", "Cure before regular foot traffic and review joint and color details with the homeowner.")]))


def get_pages():
    return [driveways(), walkways()]
