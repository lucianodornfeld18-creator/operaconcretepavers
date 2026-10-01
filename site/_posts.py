# -*- coding: utf-8 -*-
"""Registry of every blog, compare, cost and FAQ URL so all modules link to the same slugs.
Generated from research/blog-plan.csv, compare-plan.csv and cost-pages.csv. slug -> (working H1, module, services, region)."""

POSTS = {
    'concrete-driveway-cracks-florida': ('Why Is My Concrete Driveway Cracking? Which Cracks Are Normal in Florida', 'c_posts_a', ['concrete-repair', 'concrete-driveways'], 'both'),
    'tree-roots-under-driveway-florida': ('Tree Roots Under Your Driveway or Sidewalk: What Florida Homeowners Can Do', 'c_posts_a', ['concrete-repair', 'concrete-walkways', 'paver-sealing'], 'both'),
    'why-pavers-sink-in-florida': ('Why Do Pavers Sink in Florida, and How Is It Fixed?', 'c_posts_a', ['paver-sealing', 'paver-driveways', 'pool-deck-pavers'], 'both'),
    'efflorescence-on-pavers-and-concrete': ('What Is the White Haze on New Pavers and Concrete (Efflorescence)?', 'c_posts_a', ['paver-sealing', 'concrete-patios'], 'both'),
    'mold-and-algae-on-pavers-florida': ('How to Stop Black Mold and Green Algae on Florida Pavers and Concrete', 'c_posts_a', ['paver-sealing', 'concrete-pool-decks'], 'both'),
    'ants-and-weeds-in-paver-joints': ('Ants and Weeds Between Pavers: Why It Happens in Florida and What Actually Works', 'c_posts_a', ['paver-sealing', 'paver-patios'], 'both'),
    'rust-and-irrigation-stains-on-concrete-pavers': ('Orange Rust Stains From Sprinklers: Removing and Preventing Well-Water Stains on Concrete and Pavers', 'c_posts_b', ['concrete-repair', 'paver-sealing'], 'both'),
    'oil-and-tire-stains-on-driveways': ('Oil Drips and Tire Marks on Driveways: Concrete vs Sealed Pavers', 'c_posts_b', ['paver-sealing', 'concrete-driveways'], 'both'),
    'pouring-concrete-in-florida-rainy-season': ('Can You Pour Concrete in the Rain? Florida Rainy-Season Scheduling Explained', 'c_posts_b', ['concrete-driveways', 'concrete-patios', 'concrete-slabs'], 'both'),
    'concrete-curing-in-florida-heat': ('How Concrete Cures in Florida Heat and Humidity', 'c_posts_b', ['concrete-driveways', 'concrete-patios', 'concrete-slabs'], 'both'),
    'pavers-and-concrete-in-hurricanes': ('How Pavers, Concrete and Pool Decks Hold Up to Florida Hurricanes and Flooding', 'c_posts_b', ['paver-driveways', 'paver-patios', 'pool-deck-pavers', 'concrete-driveways'], 'both'),
    'permeable-pavers-and-drainage-florida': ('Permeable Pavers and Yard Drainage in Florida: When They Make Sense', 'c_posts_b', ['paver-driveways', 'paver-patios'], 'both'),
    'how-hot-do-pool-decks-get-florida': ('How Hot Do Pool Decks Get in Florida? The Coolest Surfaces Compared by Feel', 'c_posts_c', ['pool-deck-pavers', 'concrete-pool-decks'], 'both'),
    'slippery-pool-deck-fixes': ('How to Make a Slippery Pool Deck Safer', 'c_posts_c', ['concrete-pool-decks', 'stamped-concrete', 'paver-sealing'], 'both'),
    'saltwater-pools-and-coastal-salt-air-hardscape': ('Saltwater Pools and Salt Air: Protecting Concrete, Pavers and Travertine on the Coast', 'c_posts_c', ['pool-deck-pavers', 'concrete-pool-decks', 'paver-sealing'], 'sarasota'),
    'sinkholes-and-settlement-central-florida': ('Sinkholes vs Normal Settlement: What a Sunken Slab in Central Florida Really Means', 'c_posts_c', ['concrete-repair', 'concrete-slabs'], 'orlando'),
    'artificial-turf-heat-in-florida': ('How Hot Does Artificial Turf Get in Florida, and How Do You Keep It Cooler?', 'c_posts_c', ['artificial-turf'], 'both'),
    'artificial-turf-for-dogs-florida': ('Artificial Turf for Dogs in Florida: Odor, Drainage and Infill', 'c_posts_c', ['artificial-turf'], 'both'),
    'artificial-turf-in-florida-rain-and-storms': ('Does Artificial Turf Hold Up to Florida Rain, Flooding and Hurricanes?', 'c_posts_d', ['artificial-turf'], 'both'),
    'orange-county-orlando-driveway-patio-permits': ('Do You Need a Permit for a Driveway, Patio or Pavers in Orlando and Orange County?', 'c_posts_d', ['concrete-driveways', 'paver-driveways', 'paver-patios', 'concrete-patios'], 'orlando'),
    'osceola-county-kissimmee-st-cloud-permits': ('Driveway and Patio Permits in Kissimmee, St. Cloud and Osceola County', 'c_posts_d', ['concrete-driveways', 'paver-driveways', 'paver-patios'], 'orlando'),
    'seminole-county-driveway-patio-permits': ('Driveway and Patio Permits in Seminole County (Sanford, Lake Mary, Oviedo, Winter Springs)', 'c_posts_d', ['concrete-driveways', 'paver-driveways'], 'orlando'),
    'lake-and-polk-county-driveway-permits': ('Driveway and Patio Permits in Clermont, Minneola, Groveland and Davenport (Lake and Polk Counties)', 'c_posts_d', ['concrete-driveways', 'paver-driveways', 'retaining-walls'], 'orlando'),
    'sarasota-county-driveway-patio-permits': ('Driveway and Patio Permits in Sarasota, Venice and North Port', 'c_posts_d', ['concrete-driveways', 'paver-driveways', 'paver-patios'], 'sarasota'),
    'manatee-county-driveway-permits': ('Driveway and Patio Permits in Bradenton, Lakewood Ranch, Parrish and Palmetto (Manatee County)', 'c_posts_e', ['concrete-driveways', 'paver-driveways'], 'sarasota'),
    'hoa-approval-for-pavers-and-concrete': ('How to Get HOA Approval for New Pavers, a Driveway or a Pool Deck in Florida', 'c_posts_e', ['paver-driveways', 'concrete-driveways', 'pool-deck-pavers'], 'both'),
    'lakewood-ranch-arc-approval-hardscape': ('Lakewood Ranch ARC Approval for Driveways, Pavers and Pool Decks', 'c_posts_e', ['paver-driveways', 'concrete-driveways', 'pool-deck-pavers'], 'sarasota'),
    'florida-hoa-artificial-turf-law': ('Can Your Florida HOA Ban Artificial Turf? What Statute 720.3045 and the 2025 Law Change Say', 'c_posts_e', ['artificial-turf'], 'both'),
    'driveway-apron-and-right-of-way-florida': ('Who Owns the Driveway Apron? Right-of-Way Rules for Florida Driveways', 'c_posts_e', ['concrete-driveways', 'paver-driveways', 'concrete-walkways'], 'both'),
    'driveway-widening-and-extensions-florida': ('Widening or Extending a Driveway in Florida: Rules, Options and Pitfalls', 'c_posts_e', ['concrete-driveways', 'paver-driveways'], 'both'),
    'how-to-clean-pavers-without-damage': ('How to Clean Pavers Without Ruining the Joints or Sealer', 'c_posts_f', ['paver-sealing'], 'both'),
    'stamped-concrete-maintenance-florida': ('Stamped Concrete Maintenance in Florida: Resealing, Fading and Flaking', 'c_posts_f', ['stamped-concrete'], 'both'),
    'travertine-pool-deck-care': ('Travertine Pool Deck Care in Florida: Cleaning, Sealing and Filling Holes', 'c_posts_f', ['pool-deck-pavers', 'paver-sealing'], 'both'),
    'how-to-clean-artificial-turf': ('How to Clean and Maintain Artificial Turf in Florida', 'c_posts_f', ['artificial-turf'], 'both'),
    'should-you-seal-a-concrete-driveway-florida': ('Should You Seal a Concrete Driveway in Florida?', 'c_posts_f', ['concrete-driveways', 'concrete-repair'], 'both'),
    'paver-driveway-ideas-florida': ('Paver Driveway Ideas for Florida Homes (Patterns, Borders and Colors)', 'c_posts_f', ['paver-driveways'], 'both'),
    'concrete-driveway-ideas-florida': ('Concrete Driveway Ideas Beyond Plain Gray', 'c_posts_g', ['concrete-driveways', 'stamped-concrete'], 'both'),
    'paver-patio-ideas-florida': ('Paver Patio Ideas for Florida Backyards and Lanais', 'c_posts_g', ['paver-patios'], 'both'),
    'concrete-patio-ideas-florida': ('Concrete Patio Ideas for Florida Homes', 'c_posts_g', ['concrete-patios', 'stamped-concrete'], 'both'),
    'pool-deck-ideas-florida': ('Pool Deck Ideas for Florida Homes', 'c_posts_g', ['pool-deck-pavers', 'concrete-pool-decks'], 'both'),
    'stamped-concrete-patterns-and-colors': ('Stamped Concrete Patterns and Colors That Work in Florida', 'c_posts_g', ['stamped-concrete'], 'both'),
    'front-walkway-ideas-curb-appeal': ('Front Walkway Ideas That Boost Curb Appeal', 'c_posts_g', ['concrete-walkways', 'paver-patios'], 'both'),
    'extend-patio-under-screen-enclosure': ('Extending a Patio Under (or Beyond) a Pool Screen Enclosure', 'c_posts_h', ['paver-patios', 'concrete-patios', 'pool-deck-pavers'], 'both'),
    'fire-pit-on-pavers-florida': ('Fire Pits on Pavers: Safe Setups for Florida Backyards', 'c_posts_h', ['paver-patios', 'retaining-walls'], 'both'),
    'backyard-putting-green-florida': ('Planning a Backyard Putting Green in Florida', 'c_posts_h', ['artificial-turf'], 'both'),
    'side-yard-ideas-florida': ('Side Yard Ideas for Florida Homes: Turf, Pavers or Gravel', 'c_posts_h', ['artificial-turf', 'paver-patios'], 'both'),
    'low-maintenance-backyard-florida': ('A Low-Maintenance Backyard Plan for Florida (Turf, Pavers and Concrete)', 'c_posts_h', ['artificial-turf', 'paver-patios', 'concrete-patios'], 'both'),
    'retaining-wall-ideas-florida-yards': ('Retaining Wall and Seat Wall Ideas for Florida Yards', 'c_posts_h', ['retaining-walls'], 'both'),
    'concrete-pad-for-rv-or-boat-parking': ('Adding an RV or Boat Parking Pad in Florida: Size, Thickness and Rules', 'c_posts_i', ['concrete-slabs', 'paver-driveways'], 'both'),
    'shed-slab-guide-florida': ('Shed Slabs in Florida: Thickness, Tie-Downs and Permits', 'c_posts_i', ['concrete-slabs'], 'both'),
    'concrete-driveway-installation-process': ('How a Concrete Driveway Is Installed, Step by Step', 'c_posts_i', ['concrete-driveways'], 'both'),
    'paver-installation-process-florida': ('How Pavers Are Installed in Florida: Base, Bedding Sand and Compaction', 'c_posts_i', ['paver-driveways', 'paver-patios', 'pool-deck-pavers'], 'both'),
    'artificial-turf-installation-process': ('How Artificial Turf Is Installed in Florida', 'c_posts_i', ['artificial-turf'], 'both'),
    'pavers-over-existing-concrete': ('Can You Put Pavers Over Existing Concrete? Driveways, Patios and Pool Decks', 'c_posts_i', ['pool-deck-pavers', 'paver-patios', 'paver-driveways'], 'both'),
    'prepare-your-yard-for-hardscape-installation': ('How to Prepare Your Home for a Concrete, Paver or Turf Installation', 'c_posts_j', ['concrete-driveways', 'paver-patios', 'artificial-turf'], 'both'),
    'best-time-of-year-for-hardscape-projects-florida': ('When Is the Best Time of Year to Install Pavers, Concrete or Turf in Florida?', 'c_posts_j', ['concrete-driveways', 'paver-patios', 'artificial-turf'], 'both'),
    'how-to-choose-a-concrete-contractor-orlando': ('How to Choose a Concrete Contractor in Orlando: 10 Criteria to Check', 'c_posts_j', ['concrete-driveways', 'concrete-patios', 'concrete-slabs'], 'orlando'),
    'how-to-choose-a-concrete-contractor-sarasota': ('How to Choose a Concrete Contractor in Sarasota and Bradenton', 'c_posts_j', ['concrete-driveways', 'concrete-patios', 'concrete-slabs'], 'sarasota'),
    'how-to-choose-a-paver-contractor-orlando': ('How to Choose a Paver Contractor in Orlando', 'c_posts_j', ['paver-driveways', 'paver-patios', 'pool-deck-pavers'], 'orlando'),
    'how-to-choose-a-paver-contractor-sarasota': ('How to Choose a Paver Contractor in Sarasota and Lakewood Ranch', 'c_posts_j', ['paver-driveways', 'paver-patios', 'pool-deck-pavers'], 'sarasota'),
    'how-to-choose-an-artificial-turf-installer': ('How to Choose an Artificial Turf Installer in Florida', 'c_posts_k', ['artificial-turf'], 'both'),
    'florida-contractor-license-check-concrete-pavers': ('Does a Concrete or Paver Contractor Need a License in Florida? How to Check', 'c_posts_k', ['concrete-driveways', 'paver-driveways'], 'both'),
    'concrete-and-paver-warranty-what-it-should-cover': ("What a Concrete or Paver Warranty Should (and Shouldn't) Cover", 'c_posts_k', ['concrete-driveways', 'paver-driveways', 'paver-patios'], 'both'),
    'how-to-compare-concrete-and-paver-quotes': ('How to Compare Concrete and Paver Quotes Line by Line', 'c_posts_k', ['concrete-driveways', 'paver-driveways', 'paver-patios'], 'both'),
    'does-a-new-driveway-add-home-value': ('Does a New Driveway, Patio or Pool Deck Add Home Value in Florida?', 'c_posts_k', ['paver-driveways', 'concrete-driveways', 'pool-deck-pavers'], 'both'),
    'how-to-budget-a-backyard-hardscape-project-in-phases': ('How to Budget a Backyard Hardscape Project in Phases', 'c_posts_k', ['paver-patios', 'artificial-turf', 'retaining-walls'], 'both'),
    'artificial-turf-water-savings-florida': ('How Much Water and Money Does Artificial Turf Save in Florida?', 'c_posts_l', ['artificial-turf'], 'both'),
    'best-pavers-for-florida': ('What Are the Best Pavers for Florida Homes? Concrete, Clay, Travertine, Porcelain and Shellstone', 'c_posts_l', ['paver-driveways', 'paver-patios', 'pool-deck-pavers'], 'both'),
}

COMPARES = {
    'pavers-vs-concrete-driveway': ('Pavers vs Concrete Driveway in Florida: Cost, Lifespan and Upkeep', 'c_compare_a'),
    'stamped-concrete-vs-pavers': ('Stamped Concrete vs Pavers for Patios and Outdoor Living', 'c_compare_a'),
    'pavers-vs-concrete-pool-deck': ('Pavers vs Concrete for a Florida Pool Deck', 'c_compare_a'),
    'cool-deck-vs-pavers-vs-travertine': ('Cool Deck vs Pavers vs Travertine: Resurface or Replace Your Pool Deck?', 'c_compare_a'),
    'travertine-vs-concrete-pavers': ('Travertine vs Concrete Pavers', 'c_compare_a'),
    'porcelain-vs-travertine-pavers': ('Porcelain vs Travertine Pavers in Florida', 'c_compare_a'),
    'clay-brick-vs-concrete-pavers': ('Clay Brick (Chicago Brick) vs Concrete Pavers', 'c_compare_b'),
    'concrete-driveway-finishes': ('Broom Finish vs Exposed Aggregate vs Stamped: Concrete Driveway Finishes Compared', 'c_compare_b'),
    'resurface-vs-replace-concrete': ('Resurface or Replace a Concrete Driveway?', 'c_compare_b'),
    'polymeric-sand-vs-joint-sand': ('Polymeric Sand vs Regular Joint Sand for Florida Pavers', 'c_compare_b'),
    'wet-look-vs-natural-paver-sealer': ('Wet-Look vs Natural-Finish Paver Sealer', 'c_compare_b'),
    'artificial-turf-vs-sod': ('Artificial Turf vs Sod in Florida', 'c_compare_b'),
}

COST_PAGES = {
    '/concrete-driveway-cost/': ('concrete driveway cost', 'c_cost_a', 'concrete-driveways'),
    '/concrete-patio-cost/': ('concrete patio cost', 'c_cost_a', 'concrete-patios'),
    '/stamped-concrete-cost/': ('stamped concrete cost', 'c_cost_a', 'stamped-concrete'),
    '/pool-deck-cost/': ('pool deck cost', 'c_cost_a', 'concrete-pool-decks'),
    '/concrete-slab-cost/': ('concrete slab cost', 'c_cost_b', 'concrete-slabs'),
    '/concrete-walkway-cost/': ('concrete sidewalk cost', 'c_cost_b', 'concrete-walkways'),
    '/concrete-repair-cost/': ('concrete driveway repair cost', 'c_cost_b', 'concrete-repair'),
    '/paver-driveway-cost/': ('paver driveway cost', 'c_cost_b', 'paver-driveways'),
    '/paver-patio-cost/': ('paver patio cost', 'c_cost_c', 'paver-patios'),
    '/paver-sealing-cost/': ('paver sealing cost', 'c_cost_c', 'paver-sealing'),
    '/retaining-wall-cost/': ('retaining wall cost', 'c_cost_c', 'retaining-walls'),
    '/artificial-turf-cost/': ('artificial turf cost', 'c_cost_c', 'artificial-turf'),
}

FAQ_PAGES = {"/faq/": "FAQ", "/faq/concrete/": "Concrete questions", "/faq/pavers/": "Paver questions", "/faq/artificial-turf/": "Artificial turf questions", "/faq/cost-and-permits/": "Cost, permit and HOA questions"}
CORE = ["/", "/concrete/", "/pavers/", "/cost/", "/service-areas/", "/central-florida/", "/sarasota-manatee/", "/blog/", "/compare/", "/permits/", "/about/", "/contact/", "/process/", "/privacy/", "/terms/", "/accessibility/"]


def posts_for(service, n=3):
    return [(f"/blog/{s}/", POSTS[s][0]) for s in POSTS if service in POSTS[s][2]][:n]


COST_ALIAS = {"pool-deck-pavers": "/pool-deck-cost/"}


def cost_for(service):
    if service in COST_ALIAS:
        return COST_ALIAS[service]
    for r, (kw, mod, s) in COST_PAGES.items():
        if s == service:
            return r
    return None
