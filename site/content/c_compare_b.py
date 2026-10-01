# -*- coding: utf-8 -*-
"""Comparison pages (module c_compare_b of COMPARES): clay brick vs concrete pavers, concrete driveway finishes,
resurface vs replace, polymeric vs regular joint sand, wet-look vs natural paver sealer, artificial turf vs sod."""
from _data import SERVICES, PRICE_DATE
from _helpers import page, capsule, sec, table, faq, ul, a, svc, city, post, compare, src, ext, price, per


def clay_brick_vs_concrete():
    body = "".join([
        sec("Clay brick vs. concrete pavers: cost, color and strength side by side",
            f"<p>Florida contractor pricing puts clay brick pavers at $12 to $22 per square foot installed, with reclaimed or specialty brick running $25 to $50 or more, against $10 to $20 per square foot for concrete pavers of a comparable size and pattern "
            f"({src('angi-paver-driveway', 'Angi, Apr 2026')}; {src('craftpavers-fl-pricing', 'Craft Pavers, Jul 2026')}; {src('homeguide-driveway-pavers', 'HomeGuide, Jan 2026')}). "
            "The gap in price traces back to how each unit is made. Clay brick is shaped and fired in a kiln at nearly 2,000°F, which bakes the color through the entire body of the unit rather than onto the surface. "
            f"Concrete pavers are cast and cured with pigment mixed into or applied over the mix, which is faster and cheaper to produce at scale but means the color sits closer to the surface ({ext('https://www.gobrick.com/learn-about-brick/clay-pavers', 'Brick Industry Association, clay paver guide')}).</p>"
            + table("Clay brick vs. concrete pavers", ["Factor", "Clay brick", "Concrete pavers"],
                    [["Installed cost (FL market)", "$12–$22/sq ft, $25–$50+ for reclaimed or specialty units", "$10–$20/sq ft"],
                     ["Color", "Fired through the body; does not fade from UV exposure", "Pigment on or in the mix; can fade over years of direct sun"],
                     ["Strength rating", "Most clay units exceed 10,000 psi compressive strength", "Manufacturer-rated by product line, no single Florida figure"],
                     ["Sealing", "Not required to hold color or finish", "Optional, no fixed resealing interval set by the paver industry"],
                     ["Storms and standing water", "Sand-set units drain at the joints and can be lifted and reset", "Same sand-set, lift-and-reset behavior as brick"],
                     ["Repair", "Individual units replaced; reclaimed brick supply is limited", "Individual units replaced; new stock stays in production"],
                     ["HOA review", "Governed by the same architectural-control rules as any paver choice", "Governed by the same architectural-control rules as any paver choice"]],
                    f"Compressive strength from {ext('https://www.gobrick.com/learn-about-brick/clay-pavers', 'the Brick Industry Association')}, a clay-brick trade group; sealing from {src('icpi-ts5', 'ICPI Tech Spec 5')}, which covers concrete unit pavers, not clay brick.")),
        sec("Can clay brick handle a driveway, or is it patios and walkways only?",
            "<p>Both, depending on the unit. The paving-brick industry rates pedestrian and light-vehicular brick under one ASTM standard and heavier vehicular brick under a separate, thicker standard, so a driveway needs a vehicular-rated unit rather than a thin patio brick. "
            f"Concrete pavers follow the same logic from the paver side: {src('icpi-ts2', 'ICPI Tech Spec 2')} specifies 2⅜ in. units for pedestrian areas and driveways and thicker 3⅛ in. units for streets and industrial pavement. "
            "What a driveway actually needs, in either material, is the base underneath built to the vehicular spec, not a thin patio section stretched to cover a parking pad.</p>"),
        sec("When to choose clay brick",
            ul(["A historic or traditional look matters more than minimizing upfront cost, especially near a brick-street neighborhood.",
                "Color permanence without resealing is worth paying for; a faded concrete paver eventually needs attention, a faded clay brick does not.",
                "A border or accent band is the goal rather than the whole field, which keeps the brick premium to a manageable square footage.",
                "Salvaged or reclaimed brick is available locally and matches the character of an older street or subdivision."])),
        sec("When to choose concrete pavers",
            ul(["Budget per square foot is the deciding factor on a larger driveway or pool deck.",
                "A specific color, shape or surface texture is wanted that a local brick supplier does not stock.",
                "The project needs units in volume on a tighter schedule; concrete paver manufacturing runs are generally easier to match quickly than specialty brick orders.",
                "A future color refresh or sealer upgrade is part of the long-term maintenance plan anyway."])),
        sec("Clay brick's place in Central Florida's historic streets",
            f"<p>Brick is not just a patio material here; it is the surface under entire neighborhoods. {city('winter-park', 'Winter Park')} still has roughly 19 miles of brick streets out of more than 100 miles of city roadway, and the city's own street-brick policy estimates a properly installed brick street lasts 40 to 50 years against 10 to 15 years for an asphalt overlay "
            f"({ext('https://cityofwinterpark.org/docs/departments/public-works-transportation/streets/BrickingPolicy.pdf', 'City of Winter Park Street Brick Policy')}). That is a municipal road built on an engineered base, not a residential driveway, so the figure describes the material's durability potential rather than a warranty for a home project. "
            f"Downtown {city('sarasota', 'Sarasota')}'s streetscape used roughly 222,905 clay pavers cut into mosaic patterns at Main Street and Pineapple Avenue, which is one reason clay brick reads as the default historic surface on the Suncoast side as well as in Orange County "
            f"({ext('https://pinehallbrick.com/streetscape-celebrates-sarasotas-pride-of-place/', 'Pine Hall Brick, Sarasota streetscape')}). Reclaimed historic brick exists in limited supply through salvage yards and municipal reclamation programs, and availability varies year to year rather than on demand.</p>"
            f"<p>Under Florida's architectural-control statute, an HOA's governing documents can list approved paver materials, and where they do the association cannot block a homeowner's choice among the listed options ({src('fs720-3035', 'F.S. 720.3035')}). Neither brick nor concrete pavers are named in the statute itself, so what actually governs the choice is each community's own declaration and design guidelines, which is worth checking before ordering material.</p>"),
        sec("Pricing a 600 sq ft driveway in brick vs. concrete pavers",
            "<p>Say you have a 600 square foot driveway section on a 1960s lot near a Winter Park brick corridor, and the plan is either a full clay-brick surface or a full concrete-paver surface in a similar herringbone pattern. "
            "At the published Florida ranges, the brick version runs roughly $7,200 to $13,200, and the concrete-paver version runs roughly $6,000 to $12,000, before base prep, edge restraint or any demolition of an existing surface.</p>"
            "<p>Say instead the budget only stretches to concrete pavers for the full field, but the character of a brick street still matters to the homeowner. A common middle path is a brick border or soldier course framing a concrete-paver field, which keeps the brick premium to a narrow linear footage instead of the whole driveway.</p>"),
        sec("Related reading",
            f"<p>{svc('paver-driveways', 'Our paver driveways page')} and {svc('paver-patios', 'paver patios page')} cover installation and base depth for both materials. For a full cost breakdown by size, see the {a('/paver-driveway-cost/', 'paver driveway cost guide')} and {a('/paver-patio-cost/', 'paver patio cost guide')}. "
            f"If the decision is pavers versus poured concrete rather than brick versus concrete pavers, {compare('pavers-vs-concrete-driveway', 'pavers vs. concrete driveway')} covers that question directly, and {compare('travertine-vs-concrete-pavers', 'travertine vs. concrete pavers')} compares a different premium material against the same concrete-paver baseline. "
            f"{post('best-pavers-for-florida', 'What are the best pavers for Florida homes')} rounds up the material options in one place, and {svc('paver-sealing', 'paver sealing')} covers the upkeep concrete pavers may need down the road.</p>"),
    ])
    faqs = [
        faq("Does clay brick fade in Florida's sun?",
            "No, not in the way a concrete paver can. Clay brick is fired at nearly 2,000°F, which bakes the color through the entire unit, so there is no pigment layer at the surface to bleach out under UV exposure the way a concrete paver's applied color can over years in full Florida sun."),
        faq("Are clay brick pavers more expensive than concrete pavers?",
            "Usually, yes. Florida contractor pricing runs $12 to $22 per square foot for clay brick against $10 to $20 for concrete pavers of a similar size, and specialty or reclaimed brick can run $25 to $50 or more. The gap narrows when brick is used as a border or accent rather than the full field."),
        faq("Can clay brick be used for a driveway, or only patios and walkways?",
            "It can be used for a driveway if the brick is rated for vehicular loads rather than pedestrian use; paving-brick manufacturers make both. The base underneath matters as much as the unit rating, since a driveway-grade base is what actually carries the weight of a car or truck."),
        faq("Do clay brick pavers need to be sealed like concrete pavers?",
            "No. Clay brick's color is fired through the body of the unit, so there is no surface pigment or coating that needs a sealer to protect it. Concrete pavers can be sealed to deepen color or add stain resistance, but it is optional rather than required."),
        faq("Can clay brick and concrete pavers be combined in the same driveway or patio?",
            "Yes, and it is a common way to get the look of brick without pricing the whole project at brick rates. A brick border, soldier course or accent band around a concrete-paver field keeps the character while limiting brick to a smaller linear footage.")]
    return page("/compare/clay-brick-vs-concrete-pavers/", "compare", "Clay Brick vs. Concrete Pavers: Florida Cost & Care",
                "Clay brick vs. concrete pavers in Florida as of October 2026: cost per sq ft, why brick resists fading, strength, upkeep and when each fits a driveway.",
                "Clay Brick (Chicago Brick) vs Concrete Pavers",
                capsule("As of October 2026, clay brick pavers run $12 to $22 per square foot installed in Florida against $10 to $20 for concrete pavers, with brick's higher cost buying color that is fired through the unit rather than applied to the surface. "
                        "Concrete pavers offer a wider size and color selection at a lower price; brick holds its color without sealing and suits historic-district streets like Winter Park's."),
                body, faqs=faqs,
                sources=["angi-paver-driveway", "craftpavers-fl-pricing", "homeguide-driveway-pavers", "icpi-ts2", "icpi-ts5", "fs720-3035",
                         ("Brick Industry Association, clay paver guide", "https://www.gobrick.com/learn-about-brick/clay-pavers"),
                         ("City of Winter Park Street Brick Policy", "https://cityofwinterpark.org/docs/departments/public-works-transportation/streets/BrickingPolicy.pdf"),
                         ("Pine Hall Brick, Sarasota streetscape", "https://pinehallbrick.com/streetscape-celebrates-sarasotas-pride-of-place/")],
                crumbs=[("Comparisons", "/compare/")], crumb="Clay brick vs. concrete pavers", form=False, published="2026-10-01")


def driveway_finishes():
    body = "".join([
        sec("Broom, exposed aggregate or stamped: how much does each concrete driveway finish cost?",
            f"<p>A plain broom finish is the floor of the price range at $6 to $10 per square foot installed in Florida, exposed aggregate runs roughly $2 to $3 more per square foot than plain concrete at $10 to $15, and stamped work spans $15 to $25 or more depending on how many colors and layers are involved "
            f"({src('homeguide-concrete-driveway', 'HomeGuide, Jun 2025')}; {src('homeguide-exposed-aggregate', 'HomeGuide, 2023')}). All three start from the same slab: the same thickness, the same base and the same control-joint spacing. What changes is what happens to the surface in the last few minutes before the concrete sets.</p>"
            + table("Concrete driveway finish comparison", ["Finish", "Cost (FL, per sq ft)", "Texture underfoot", "Resealing"],
                    [["Broom", "$6–$10", "Even, consistent texture across the whole slab", "Optional; nothing to fade"],
                     ["Exposed aggregate", "$10–$15", "Stone shows through the surface for natural, gritty texture", "Occasional reseal keeps the stone's sheen"],
                     ["Stamped (mid to high-end)", "$15–$25+", "Depends on the mold; texture can be shallow if the pattern is pressed lightly", "Needs periodic resealing to hold color and sheen"]],
                    f"Florida market ranges, {PRICE_DATE}; HomeGuide's concrete driveway and exposed-aggregate cost guides.")),
        sec("Which finish grips best and shows the least wear in Florida rain?",
            "<p>Broom finish is the most consistent choice for grip because the texture is uniform across the whole slab rather than concentrated in a pattern or around exposed stone. Exposed aggregate comes close behind it, since the stone itself breaks up the surface and adds natural traction even when wet. "
            "Stamped concrete depends more on the mold and the sealer: a deep, well-maintained texture grips fine, but a shallow stamp finished with a high-gloss sealer can get slick once water sits on it.</p>"
            f"<p>Florida's rainy season puts real volume through a driveway most years. Orlando averages 51.45 inches of rain a year and Sarasota–Bradenton averages 49.05 inches, most of it concentrated from late May through mid-October ({src('ncei-annual-prcp', 'NOAA NCEI 1991–2020 normals')}). "
            "A finish with reliable traction when wet matters more here than in a drier climate, which is one reason broom and exposed aggregate stay the default choice for the main driving surface even when a stamped accent band is added at the entry.</p>"),
        sec("Which finish holds its color longest in Florida sun?",
            "<p>Broom finish has the least color to lose in the first place, since it is usually plain gray or a single integral tint with no release agent or antiquing layer sitting on top. Exposed aggregate's color lives mostly in the stone itself, which does not fade the way a surface stain can. "
            "Stamped concrete carries the most color risk because the look depends on a sealer coat staying intact, and a sealer that wears thin lets the underlying color look flat long before the slab itself is in trouble.</p>"
            "<p>Timing the pour also matters more for stamped work than for the other two finishes. A crew has to press the mold into the slab before the surface firms up, and Florida's heat shortens that window on a hot, dry afternoon, which is why stamped pours are often scheduled for an early start rather than mid-day.</p>"),
        sec("When a plain or exposed-aggregate finish makes sense",
            ul(["The driveway is a daily-use surface where traction and a predictable budget matter more than a decorative pattern.",
                "The plan includes a future reseal or color refresh down the line, and starting with less color investment keeps that cheaper.",
                "The lot backs onto a right-of-way apron that already has to meet a city's own concrete spec regardless of the decorative finish chosen.",
                "A natural, stone-flecked texture fits the house better than a uniform smooth gray slab."])),
        sec("When stamped is worth the extra cost",
            ul(["The driveway doubles as a visible design feature, such as a circular entry court or a border along a front walk.",
                "A specific pattern (slate, cobble, wood-plank) is part of the overall landscape design and worth the added labor time.",
                "Budget allows for the ongoing resealing a stamped finish needs to keep its color and sheen over time.",
                "A matching stamped patio or pool deck is already planned, so the pattern and color carry through the whole property."])),
        sec("Does the finish change what a Florida city requires at the street?",
            f"<p>No. Several cities set a minimum concrete spec for the portion of a driveway that crosses the public right-of-way, and that applies no matter what finish covers the rest of the slab. The City of Orlando's Engineering Standards Manual requires the apron, the section within the right-of-way, to be at least 3,000 psi concrete and at least 6 inches thick with a break joint at the property line, whether the driveway beyond it is plain broom or stamped "
            f"({ext('https://www.orlando.gov/files/sharedassets/public/documents/engineering/platting/engineeringstandardsmanual.pdf', 'City of Orlando Engineering Standards Manual')}). "
            f"Some HOA-governed communities add a separate layer of review on top of that. In Lakewood Ranch's Country Club/Edgewater Village, changing a driveway's finish, sealing it or applying a decorative overlay all require a Modification Request Form submitted to the community association before the work starts, with approved sealer colors specified by name ({src('lwr-ceva-manual', "Lakewood Ranch CEVA Homeowners' Manual")}). "
            "Checking both the city's right-of-way spec and any HOA architectural rule before ordering a specific finish avoids a redo after the fact.</p>"),
        sec("Three finishes, one 400 sq ft driveway",
            "<p>Say you have a bare 20 × 20 ft (400 sq ft) driveway pad planned for a Clermont lot. In plain broom finish, that lands around $2,400 to $4,000. Switching to exposed aggregate pushes the same pad to roughly $4,000 to $6,000, mostly because of the extra labor to expose and clean the stone before it cures fully. "
            "A mid-range stamped pattern on the same footprint runs $6,000 to $10,000, and a high-end multi-color stamp can clear $10,000 before any additional sealer work.</p>"
            "<p>A common compromise on a budget-limited project is a plain broom field with a narrow stamped or exposed-aggregate border along the entry and garage apron, which concentrates the decorative cost into a few dozen square feet instead of the whole pad.</p>"),
        sec("Related reading",
            f"<p>{svc('concrete-driveways', 'Our concrete driveways page')} covers thickness and base prep for any finish, and {svc('stamped-concrete', 'our stamped concrete page')} goes deeper into pattern and color options. The {a('/concrete-driveway-cost/', 'concrete driveway cost guide')} and {a('/stamped-concrete-cost/', 'stamped concrete cost guide')} break totals down by size. "
            f"If pavers are also on the table, {compare('pavers-vs-concrete-driveway', 'pavers vs. concrete driveway')} compares the two material families, and {compare('resurface-vs-replace-concrete', 'resurface or replace a concrete driveway')} is worth a look if the question is reviving an old slab rather than choosing a finish for a new one. "
            f"{post('concrete-driveway-ideas-florida', 'Concrete driveway ideas beyond plain gray')} and {post('stamped-concrete-maintenance-florida', 'stamped concrete maintenance in Florida')} go further into design and upkeep.</p>"),
    ])
    faqs = [
        faq("Is a broom-finish driveway slippery when wet?",
            "No, broom finish is one of the more slip-resistant options specifically because the broom drags a consistent texture across the entire slab while the concrete is still plastic. That texture stays in place for the life of the slab, unlike a sealer coat on a stamped finish, which can wear smoother over time."),
        faq("Does exposed aggregate cost much more than plain broom concrete?",
            "A bit more, not dramatically. Exposed aggregate runs roughly $2 to $3 more per square foot than plain broom concrete, which on a 400-square-foot driveway works out to an extra $800 to $1,200, mostly for the labor to wash and expose the stone before the surface sets too hard."),
        faq("Can a driveway have two finishes, like a stamped border on a broom field?",
            "Yes, and it is a common way to add a decorative touch without stamping the entire driveway. A stamped or exposed-aggregate border along the entry or garage apron, poured against a plain broom field, keeps most of the slab at the lower cost tier."),
        faq("Does a stamped finish need to be resealed more often than broom or exposed aggregate?",
            "Yes. A stamped finish's color and sheen depend on an intact sealer coat, so it needs periodic resealing to look the way it did on day one. Broom concrete has little to no applied color to protect, and exposed aggregate's color lives mostly in the stone rather than a coating."),
        faq("Which finish is easiest to patch if a section cracks or stains?",
            "Plain broom finish is the easiest to color-match for a partial repair, since there is no pattern alignment or multi-color blend to replicate. A stamped repair has to match both the mold pattern and the color layering, which is harder to do seamlessly on an older slab that has already weathered some.")]
    return page("/compare/concrete-driveway-finishes/", "compare", "Broom vs. Exposed Aggregate vs. Stamped Concrete",
                "Broom finish vs. exposed aggregate vs. stamped concrete driveways in Florida as of October 2026: cost per sq ft, grip in the rain and which finish fades.",
                "Broom Finish vs Exposed Aggregate vs Stamped: Concrete Driveway Finishes Compared",
                capsule("As of October 2026, a plain broom concrete driveway in Florida runs $6 to $10 per square foot, exposed aggregate runs $10 to $15, and stamped work runs $15 to $25 or more. "
                        "Broom grips best in Florida's rainy season and holds color with no sealer to maintain; stamped carries the highest upfront cost and the most ongoing resealing to keep its pattern and color looking right."),
                body, faqs=faqs,
                sources=["homeguide-concrete-driveway", "homeguide-exposed-aggregate", "ncei-annual-prcp", "lwr-ceva-manual",
                         ("City of Orlando Engineering Standards Manual", "https://www.orlando.gov/files/sharedassets/public/documents/engineering/platting/engineeringstandardsmanual.pdf")],
                crumbs=[("Comparisons", "/compare/")], crumb="Concrete driveway finishes", form=False, published="2026-10-01")


def resurface_vs_replace():
    body = "".join([
        sec("How much cheaper is resurfacing than a full driveway replacement?",
            f"<p>Resurfacing a sound but worn driveway runs $3 to $7 per square foot nationally, and Orlando's published figures run a bit higher at $5 to $10 per square foot ({src('homeguide-concrete-resurfacing', 'HomeGuide, Feb 2026')}; {src('angi-driveway-repair-orlando', 'Angi Orlando, Jun 2026')}). "
            f"A full replacement, by comparison, runs $6 to $15 per square foot for a new pour depending on thickness, and Orlando's figures for replacing damaged slabs or a complete tear-out and repour land at $10 to $15 per square foot ({src('homeguide-concrete-driveway', 'HomeGuide')}; {src('angi-driveway-repair-orlando', 'Angi Orlando')}). "
            "The price gap is real, but it only holds if the driveway is actually a resurfacing candidate. A thin overlay bonded to a failing base does not save money if it has to be torn out again in a year or two.</p>"
            + table("Resurfacing vs. full replacement", ["Factor", "Resurfacing (overlay)", "Full replacement"],
                    [["Cost (FL, per sq ft)", "$3–$10", "$6–$15, plus demolition if an old slab comes out"],
                     ["What it fixes", "Cosmetic cracking, surface wear, faded color", "Structural cracks, settlement, undersized thickness"],
                     ["Base condition required", "Needs a sound, stable base underneath", "Rebuilds the base from scratch"],
                     ["Storm or root damage", "Does not correct a base that has shifted or washed out", "Resets the base and drainage entirely"],
                     ["Repair if it fails again", "Can delaminate at the edges if the slab beneath keeps moving", "Starts from a fresh, inspected base"],
                     ["HOA review (where it applies)", "Some communities require a modification form specifically for overlay work", "Treated the same as any new driveway installation"]],
                    f"Florida and national ranges, {PRICE_DATE}, from the sources on this page.")),
        sec("What kind of cracking can actually be resurfaced?",
            "<p>A resurfacing overlay works when the damage is cosmetic and the slab underneath is stable: hairline map-cracking, surface scaling, color fade, or a worn texture on an otherwise flat, level driveway. "
            "It does not fix the cause of a crack, only the surface over it, so a crack that keeps opening because the base is still moving will usually telegraph straight through a new overlay within a season or two.</p>"
            "<p>Cracks with a vertical offset, where one side of the crack sits noticeably higher than the other, are the clearest sign that resurfacing is the wrong call. That offset means the slab has settled or heaved unevenly, which an overlay bonded to the surface cannot correct. "
            f"The same goes for a driveway where a live oak or other large root has lifted a section; see {post('tree-roots-under-driveway-florida', 'tree roots under your driveway')} for how that specific cause plays out.</p>"),
        sec("Does resurfacing fix a sunken or uneven driveway?",
            f"<p>No. A resurfacing overlay is a thin cosmetic layer, not a structural fix, so it cannot lift a sunken section back to grade. Leveling a sunken driveway is a separate repair category, mudjacking or polyjacking, that pumps material underneath the existing slab to raise it rather than adding a new surface on top "
            f"({src('homeguide-mudjacking', 'HomeGuide, Nov 2025')}). Orlando's published mudjacking figures run $3 to $8 per square foot, with a typical minimum job fee around $500 ({src('angi-mudjacking-orlando', 'Angi Orlando, May 2026')}). "
            "If a driveway is both cracked and sunken, leveling the slab usually has to happen before a resurfacing overlay goes down, or the overlay telegraphs the same unevenness right back to the surface.</p>"),
        sec("When resurfacing makes sense",
            ul(["The cracking is cosmetic: hairline, map-pattern or surface-only, with no vertical offset at any joint.",
                "The base underneath has not shifted; a flashlight check along the edges shows no voids or soft spots.",
                "Budget is the deciding factor and the driveway's current thickness and layout are already adequate.",
                "The goal is mainly a color or texture refresh on a slab that is still structurally sound."])),
        sec("When full replacement makes sense",
            ul(["A crack shows a vertical offset, meaning the two sides of the slab have settled or heaved unevenly.",
                "A tree root, a drainage problem or a known soft spot in the soil is actively moving the slab.",
                "The existing driveway is undersized for its use, such as a 4-inch section now carrying a boat trailer or RV that needs 5 to 6 inches.",
                "More than one patch job has already failed on the same section, which usually means the base, not the surface, is the real problem."])),
        sec("Florida's sinkhole counties change the calculus",
            f"<p>Most settlement in Florida is ordinary soil consolidation, not a sinkhole, and resurfacing is still the right call for that kind of gradual, even settling. Sinkhole claims concentrate in a specific band of west-central counties where the limestone sits close to the surface under a layer of sand and clay, including Hernando, Pasco and Hillsborough, with Orange County also appearing on the state's list of higher-claims counties; Sarasota and Manatee counties are not on that list "
            f"({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). "
            f"A driveway crack alone is not enough to diagnose a sinkhole either way; see {post('sinkholes-and-settlement-central-florida', 'sinkholes vs. normal settlement in Central Florida')} for the signs worth watching for on a property in or near that band, and for why a crack pattern on its own is not a reliable test.</p>"),
        sec("Two driveways, two different answers",
            "<p>Say you have a 400-square-foot driveway off a 1990s Oviedo home with a network of hairline cracks across the surface but no vertical offset anywhere and a flat, stable feel underfoot. That is a textbook resurfacing candidate, running roughly $1,200 to $4,000 for a basic to decorative overlay rather than a full tear-out.</p>"
            "<p>Say instead you have a 400-square-foot driveway near a mature oak in Winter Garden where one joint has lifted almost an inch and a crack runs the full width of the slab with a visible step on one side. That combination, root pressure plus a vertical offset, points to replacement: roughly $2,400 to $6,000 for the new pour, plus demolition of the old slab at $1,200 to $3,200 more.</p>"),
        sec("Related reading",
            f"<p>{svc('concrete-repair', 'Our concrete repair and resurfacing page')} covers crack repair, overlays and leveling in more depth, and the {a('/concrete-repair-cost/', 'concrete repair cost guide')} breaks down pricing by repair type. {svc('concrete-driveways', 'Our concrete driveways page')} and the {a('/concrete-driveway-cost/', 'concrete driveway cost guide')} cover a full replacement from the ground up. "
            f"{post('concrete-driveway-cracks-florida', 'Which cracks are normal in a Florida driveway')} and {post('should-you-seal-a-concrete-driveway-florida', 'should you seal a concrete driveway in Florida')} go deeper into the day-to-day side of keeping a slab in good shape, and {compare('concrete-driveway-finishes', 'broom vs. exposed aggregate vs. stamped finishes')} is worth a look if a replacement is on the table and the finish is still an open question.</p>"),
    ])
    faqs = [
        faq("How do I know if my driveway needs resurfacing or full replacement?",
            "Look at whether any crack has a vertical offset, where one side sits higher than the other. Hairline, flat cracking with a stable base underneath usually resurfaces well; a crack with a step, a sunken section, or more than one failed patch in the same spot points to replacement instead."),
        faq("Is a resurfaced driveway as strong as a newly poured one?",
            "No, and it is not meant to be. A resurfacing overlay is a thin cosmetic and protective layer bonded to the existing slab, which still does the structural work underneath. If the existing slab is undersized or compromised, resurfacing does not add strength back to it."),
        faq("Does resurfacing add noticeable thickness to a driveway?",
            "Usually not much. Most resurfacing overlays are a thin coating or topping, a fraction of an inch in most cases, rather than a new structural layer, so the driveway's grade and how it meets the garage floor or walkway stay close to where they started."),
        faq("Can a driveway be resurfaced more than once?",
            "Sometimes, if the base and original slab are still sound and the first overlay simply wore out or faded. Each additional layer adds a small amount of thickness and another bond line that can eventually delaminate, so a driveway on its second or third resurfacing is worth a closer look before adding another coat."),
        faq("Does Florida's sinkhole risk change whether resurfacing is safe?",
            "It can, in the specific counties where sinkhole claims concentrate. A driveway settling unevenly in Hernando, Pasco or Hillsborough County deserves a closer look at the cause before resurfacing over it, while the same crack pattern in Sarasota or Manatee County, which are not on the state's higher-claims list, is far more likely to be ordinary settlement.")]
    return page("/compare/resurface-vs-replace-concrete/", "compare", "Resurface vs. Replace a Concrete Driveway",
                "Resurface or replace a concrete driveway in Florida as of October 2026: cost comparison, which cracks resurface well, and when a full tear-out is the right call.",
                "Resurface or Replace a Concrete Driveway?",
                capsule("As of October 2026, resurfacing a Florida driveway runs $3 to $10 per square foot against $6 to $15 for a full replacement. Resurfacing works on cosmetic, flat cracking over a stable base; a crack with a vertical offset, active settlement or root damage is a sign the base itself needs rebuilding, not just a new surface."),
                body, faqs=faqs,
                sources=["homeguide-concrete-resurfacing", "angi-driveway-repair-orlando", "homeguide-concrete-driveway", "homeguide-mudjacking",
                         "angi-mudjacking-orlando", "fl-senate-2011-104"],
                crumbs=[("Comparisons", "/compare/")], crumb="Resurface vs. replace concrete", form=False, published="2026-10-01")


def polymeric_vs_regular_sand():
    body = "".join([
        sec("What's the difference between polymeric sand and regular joint sand?",
            f"<p>Polymeric sand is graded sand blended with a polymer binder that activates when it is misted with water after installation, which locks the sand in place between pavers. Regular joint sand, usually plain or silica sand, has no binder and stays loose once it is swept into the joints and compacted "
            f"({ext('https://unilock.com/material-choices/polymeric-sand/', 'Unilock, polymeric sand guide')}). Both sit inside the same paver-sealing service here, typically {price('paver-sealing')} per square foot for cleaning, re-sanding and sealing together ({src('icpi-ts5', 'ICPI Tech Spec 5')}).</p>"
            + table("Polymeric sand vs. regular joint sand", ["Factor", "Polymeric sand", "Regular joint sand"],
                    [["Binder", "Yes, activates with water after sweeping in", "None; stays loose"],
                     ["Washout in heavy rain", "Resists washout once properly cured", "Washes out and needs regular top-ups"],
                     ["Weed and ant resistance", "Forms a tighter seal that discourages both", "Loose joints are easier for weeds and ants to work into"],
                     ["Install timing", "Needs dry weather for installation and a dry window after activation", "Can be swept in and compacted in most weather"],
                     ["Repairing a single paver", "Bonded joints make lifting one unit harder", "Loose sand lifts out easily for a spot repair"],
                     ["Cost", "Upper end of a re-sanding job", "Lower end of a re-sanding job"]],
                    f"{ext('https://unilock.com/material-choices/polymeric-sand/', 'Unilock')}; {src('icpi-ts5', 'ICPI Tech Spec 5')}, which covers joint sand stabilizers generally without naming a specific brand or product.")),
        sec("Which one holds up better to a Florida rainy season?",
            f"<p>Polymeric sand is built for exactly this problem. Orlando averages 51.45 inches of rain a year and Sarasota–Bradenton averages 49.05 inches, with most of it concentrated from late May through mid-October ({src('ncei-annual-prcp', 'NOAA NCEI 1991–2020 normals')}), and a joint packed with regular sand can lose material to a single heavy downpour, let alone a full season of them. "
            "Once activated and cured, polymeric sand resists that washout and keeps the joints filled through the wet months without the repeated top-ups regular sand needs.</p>"
            "<p>The trade-off is installation timing. Polymeric sand has to go in on dry pavers and then cure through a dry window after it is misted with water, which is harder to schedule reliably during Florida's wettest stretch than it is in a drier season. A crew working around an afternoon thunderstorm pattern often schedules polymeric sand installs for the drier months rather than mid-summer.</p>"),
        sec("When to choose polymeric sand",
            ul(["The joints have had recurring weed or ant problems with regular sand in the past.",
                "The paver area sees heavy runoff or a steep grade where regular sand tends to wash toward a low point.",
                "Fewer maintenance visits matter more than the slightly higher material cost.",
                "The installation can be scheduled for a dry stretch with time for the sand to cure properly."])),
        sec("When regular joint sand still makes sense",
            ul(["Budget is tight and the paver area is low-traffic with minimal slope.",
                "The joints are unusually tight or narrow, which can make it harder to get polymeric sand's activation water down into the joint evenly.",
                "A homeowner wants to do their own periodic top-ups rather than schedule a professional re-sanding visit.",
                "The paver field is being re-sanded on a short timeline where a dry curing window cannot be guaranteed."])),
        sec("Sand choice inside a Florida sealing job",
            f"<p>Re-sanding is usually bundled into a paver cleaning-and-sealing visit rather than sold on its own, which is why the market range for that work, {price('paver-sealing')} per square foot, covers both the sand and the sealer coat ({src('icpi-ts5', 'ICPI Tech Spec 5')}). "
            "Polymeric sand tends to sit at the upper end of that range because of the material cost and the extra care needed during installation; plain sand sits closer to the lower end. "
            f"Either way, {svc('paver-sealing', 'a paver sealing visit')} is also the point where loose, weedy or ant-infested joints from years of regular sand usually get swept out and replaced, which is a natural time to switch to polymeric if washout has been a recurring problem.</p>"),
        sec("Related reading",
            f"<p>{svc('paver-sealing', 'Our paver sealing and restoration page')} covers the cleaning, re-sanding and sealing process together, and the {a('/paver-sealing-cost/', 'paver sealing cost guide')} breaks the pricing down further. "
            f"{svc('paver-driveways', 'Paver driveways')} and {svc('paver-patios', 'paver patios')} cover the base and bedding sand that goes in underneath, separate from the joint sand on top. "
            f"{compare('wet-look-vs-natural-paver-sealer', 'Wet-look vs. natural-finish paver sealer')} is the companion decision for the sealer itself, and {post('ants-and-weeds-in-paver-joints', 'ants and weeds between pavers')} and {post('why-pavers-sink-in-florida', 'why pavers sink in Florida')} go deeper into the problems joint sand choice is trying to prevent.</p>"),
    ])
    faqs = [
        faq("Should I use polymeric sand on my pavers?",
            "For most Florida driveways and patios, yes, especially on a sloped area, a pool deck, or any spot that has had weed or ant problems before. Polymeric sand costs more up front and needs a dry window to cure properly, but it holds up to heavy rain and foot traffic better than plain sand over the life of the joints."),
        faq("How long does polymeric sand last before it needs replacing?",
            "It depends on climate, traffic and how well it was activated during installation, but properly installed polymeric sand needs far fewer touch-ups than plain sand over several years. A joint that starts washing out or crumbling again is usually a sign the original activation did not fully cure."),
        faq("Can polymeric sand be installed on a rainy Florida afternoon?",
            "It should not be. Polymeric sand needs dry pavers going in and a dry period afterward for the binder to cure once it is activated with water; installing it right before or during rain can wash the binder out before it sets, which defeats the purpose of using it."),
        faq("Does polymeric sand stop ants and weeds completely?",
            "It significantly reduces both by forming a tighter seal in the joints than loose regular sand does, but it is not an absolute guarantee. A joint that was not fully filled or properly activated during installation can still leave small gaps where weeds or ants find a way in."),
        faq("Is polymeric sand harder to install than regular sand?",
            "Yes, it takes more care. Regular sand just gets swept in and compacted, while polymeric sand has to be swept in, the excess brushed off the paver surface before it gets wet, and then activated with a careful misting rather than a heavy soak, all before any rain arrives.")]
    return page("/compare/polymeric-sand-vs-joint-sand/", "compare", "Polymeric Sand vs. Regular Paver Joint Sand",
                "Polymeric sand vs. regular joint sand for Florida pavers as of October 2026: how each holds up to the rainy season, cost, and which one stops weeds and ants.",
                "Polymeric Sand vs Regular Joint Sand for Florida Pavers",
                capsule("As of October 2026, polymeric sand costs more than regular joint sand but resists washout through Florida's rainy season, which averages 51.45 inches a year in Orlando and 49.05 inches in Sarasota. "
                        "Regular sand is cheaper and easier to install in any weather, but it washes out faster and needs more frequent top-ups on sloped or heavily used paver areas."),
                body, faqs=faqs,
                sources=["icpi-ts5", "ncei-annual-prcp", ("Unilock, polymeric sand guide", "https://unilock.com/material-choices/polymeric-sand/")],
                crumbs=[("Comparisons", "/compare/")], crumb="Polymeric vs. regular joint sand", form=False, published="2026-10-01")


def wet_look_vs_natural_sealer():
    body = "".join([
        sec("What's the difference between a wet-look and a natural-finish paver sealer?",
            f"<p>A wet-look sealer is a higher-gloss topical coating that darkens the paver color and leaves a visible sheen, while a natural-finish sealer is a lower-gloss or matte product that protects the surface without changing its look much at all "
            f"({ext('https://www.blanerspressurecleaning.com/pressure-washing-articles/paver-sealing-wet-look-vs-natural-finish-what-daytona-beach-homeowners-should-choose', "Blaner's Pressure Cleaning, Daytona Beach")}). Both fall inside the same Florida market range for paver sealing, {price('paver-sealing')} per square foot for cleaning, re-sanding and sealing together "
            f"({src('icpi-ts5', 'ICPI Tech Spec 5')}), and neither has a fixed reapplication interval; acrylic sealers in general need recoating after a period of wear and weather rather than on a set schedule.</p>"
            + table("Wet-look vs. natural-finish paver sealer", ["Factor", "Wet-look sealer", "Natural-finish sealer"],
                    [["Appearance", "Glossy, darkens the color noticeably", "Matte to low-sheen, close to the unsealed look"],
                     ["Slip resistance when wet", "Lower; smoother surfaces get slicker in the rain", "Higher; closer to the paver's original texture"],
                     ["Heat and glare in full sun", "Darker surface can run warmer; more glare off the sheen", "Reflects more light; less color shift in direct sun"],
                     ["Coastal durability", "Needs a breathable, water-based formula near salt air", "Same requirement; gloss level does not change this"],
                     ["Cost", "Same market range as natural finish", "Same market range as wet-look"],
                     ["Best setting", "Driveways and entries where color pop matters most", "Pool decks and lanais where traction matters most"]],
                    f"{ext('https://www.blanerspressurecleaning.com/pressure-washing-articles/paver-sealing-wet-look-vs-natural-finish-what-daytona-beach-homeowners-should-choose', "Blaner's Pressure Cleaning")}; {src('icpi-ts5', 'ICPI Tech Spec 5')}.")),
        sec("Which sealer is safer around a pool deck?",
            "<p>Natural or low-gloss finishes are the safer default around a pool. A high-gloss wet-look coating reduces traction on a surface that is wet most of the day anyway, and that trade-off matters more on a pool deck than almost anywhere else on the property. "
            "A traction additive can be blended into either finish to improve grip, which is worth asking about specifically if a wet-look sealer is still the preferred appearance for a deck.</p>"
            f"<p>{svc('pool-deck-pavers', 'Our pool deck pavers page')} and {svc('concrete-pool-decks', 'concrete pool decks page')} both cover slope and drainage, which affect how much standing water a deck sealer has to deal with in the first place regardless of gloss level.</p>"),
        sec("Which sealer handles Florida heat and glare better?",
            "<p>A wet-look sealer darkens the paver surface, and a darker surface in full Florida sun runs warmer underfoot than a lighter one, along with more glare bouncing off the glossy coating itself. A natural or matte finish keeps the color closer to the unsealed paver and reflects more light, which cuts down on both the added warmth and the glare on a south-facing driveway or open patio. "
            "Neither effect has been measured in degrees for paver sealers specifically, so the comparison here is about which direction each finish pushes, not a guaranteed temperature difference.</p>"),
        sec("When to choose a wet-look sealer",
            ul(["A driveway or entry is meant to be a visual focal point and the deeper, glossier color is worth the trade-off.",
                "The surface sees light foot traffic rather than bare feet around a pool.",
                "A specific paver color needs to be enhanced or evened out after years of sun exposure.",
                "Glare and surface heat are not a major concern for that particular area of the property."])),
        sec("When to choose a natural-finish sealer",
            ul(["A pool deck or lanai is the surface being sealed, where bare feet and wet conditions make traction the priority.",
                "The goal is protecting the pavers without changing how they look.",
                "The area gets heavy direct sun for most of the day and added surface heat or glare is a real concern.",
                "A quieter, stone-like appearance fits the rest of the landscaping better than a glossy coating."])),
        sec("Coastal salt air changes the sealer, not just the finish",
            f"<p>Along the Sarasota and Manatee coastline, salt air and humidity put more stress on a sealer than gloss level alone. A breathable, water-based formula that lets trapped moisture escape is the better choice in that environment regardless of whether the finish is wet-look or natural, since a sealer that traps moisture underneath can whiten or haze over time "
            f"({ext('https://www.blanerspressurecleaning.com/pressure-washing-articles/paver-sealing-wet-look-vs-natural-finish-what-daytona-beach-homeowners-should-choose', "Blaner's Pressure Cleaning")}). "
            f"{post('saltwater-pools-and-coastal-salt-air-hardscape', 'Saltwater pools and salt air')} covers how that same salt exposure affects concrete, pavers and travertine more broadly, beyond the sealer question alone.</p>"),
        sec("Sealing a pool deck vs. a driveway entry",
            "<p>Say you have a 500 square foot travertine pool deck near Lakewood Ranch and a 500 square foot concrete-paver driveway entry at the same property. The pool deck is a clear case for a natural or low-gloss sealer with a traction additive, both for bare feet and because a matte finish keeps the deck from reading noticeably hotter in full sun. "
            "The driveway entry, seeing shoes rather than bare feet and acting as the first visual impression of the house, is a reasonable place for a wet-look sealer if the deeper color is worth the slightly higher glare. Both jobs fall in the same per-square-foot sealing range; the difference is the product chosen, not the labor involved.</p>"),
        sec("Related reading",
            f"<p>{svc('paver-sealing', 'Our paver sealing and restoration page')} covers the cleaning and re-sanding steps that come before any sealer goes down, and the {a('/paver-sealing-cost/', 'paver sealing cost guide')} has the full pricing breakdown. "
            f"{compare('polymeric-sand-vs-joint-sand', 'Polymeric sand vs. regular joint sand')} is the companion decision for what happens inside the joints before sealing. "
            f"{svc('pool-deck-pavers', 'Pool deck pavers')} and {post('travertine-pool-deck-care', 'travertine pool deck care in Florida')} go deeper into deck-specific upkeep, and {post('how-to-clean-pavers-without-damage', 'how to clean pavers without ruining the joints or sealer')} covers the maintenance side once a sealer is down.</p>"),
    ])
    faqs = [
        faq("Does a wet-look sealer make pavers hotter in the sun?",
            "It can push a surface slightly warmer, since the glossy coating darkens the paver color and darker surfaces generally absorb more heat in direct sun than lighter ones. No specific temperature difference has been measured for paver sealers, so treat this as a direction rather than a guaranteed number."),
        faq("Is a wet-look finish too slippery for a pool deck?",
            "It can be less safe than a matte finish, since the higher gloss reduces traction on a surface that stays wet much of the day. A natural or low-gloss sealer, with a traction additive if extra grip is needed, is the more common choice for pool decks for this reason."),
        faq("Can I switch from a wet-look sealer to a natural finish later, or the other way around?",
            "Generally yes, though it usually means stripping or letting the existing sealer wear down before the new coating is applied, since layering a different sealer type over an existing one can trap moisture or cause uneven adhesion. A professional assessment before switching avoids a patchy result."),
        faq("Do wet-look and natural sealers need the same prep work before application?",
            "Yes. Both need the pavers cleaned, old sealer residue removed if present, and joints re-sanded before the new coat goes down. The prep work is the same regardless of which finish is chosen; the difference is entirely in the product applied at the end."),
        faq("Does a wet-look sealer darken pavers permanently?",
            "The darkening lasts as long as the sealer coat does, not permanently. Once the sealer wears down or is stripped, the paver returns closer to its original color, which is why resealing on a schedule is what keeps a wet-look finish looking consistent over the years.")]
    return page("/compare/wet-look-vs-natural-paver-sealer/", "compare", "Wet-Look vs. Natural Paver Sealer Finish",
                "Wet-look vs. natural-finish paver sealer in Florida as of October 2026: gloss, slip resistance, heat and glare, and which fits a pool deck versus a driveway.",
                "Wet-Look vs Natural-Finish Paver Sealer",
                capsule("As of October 2026, wet-look and natural-finish paver sealers cost the same per square foot in Florida; the difference is gloss, not price. "
                        "Wet-look deepens color for a driveway or entry but reduces traction and adds glare; natural or matte finishes keep better footing and less surface heat, which is why pool decks and lanais usually call for the lower-gloss option."),
                body, faqs=faqs,
                sources=["icpi-ts5", ("Blaner's Pressure Cleaning, Daytona Beach", "https://www.blanerspressurecleaning.com/pressure-washing-articles/paver-sealing-wet-look-vs-natural-finish-what-daytona-beach-homeowners-should-choose")],
                crumbs=[("Comparisons", "/compare/")], crumb="Wet-look vs. natural paver sealer", form=False, published="2026-10-01")


def turf_vs_sod():
    body = "".join([
        sec("Sod or artificial turf: what changes about keeping a Florida yard green?",
            f"<p>St. Augustinegrass, the default sod across both service areas, needs at least an inch of irrigation a week once established, applied in a half to three-quarter inch dose, and shows stress by folding, wilting or turning blue-gray before it browns "
            f"({ext('https://ask.ifas.ufl.edu/publication/LH010', 'UF/IFAS, St. Augustinegrass for Florida Lawns')}). Its main pest, the southern chinch bug, feeds on the grass and shows up as yellowish patches, especially in the sunniest, most water-stressed parts of a lawn. "
            "Artificial turf has no watering schedule, no mowing and no chinch bugs to manage, but Florida's 2026 turf rule now sets specific installation standards that sod was never subject to in the first place.</p>"
            + table("Artificial turf vs. St. Augustine sod", ["Factor", "Artificial turf", "St. Augustine sod"],
                    [["Installed cost (FL market)", f"{price('artificial-turf')} per sq ft", "$0.70–$1.75 per sq ft, Central Florida contractor pricing"],
                     ["Weekly water", "None; in-ground irrigation on turf areas is barred by state rule", "At least 1 in./week once established, more during establishment"],
                     ["Upkeep", "Occasional grooming and rinsing", "Mowing at 3.5–4 in., fertilizing, pest watch"],
                     ["Stormwater", "Must not increase runoff to neighbors under the 2026 rule", "Living soil infiltrates rainfall; no permeability standard applies"],
                     ["Repair", "Seams and worn sections patched by a professional", "Dead patches re-sodded in place, inexpensively"],
                     ["HOA visibility rule", "Turf not visible from the frontage is protected by state law", "Not specifically addressed; most HOAs require a maintained lawn"]],
                    f"Turf cost from {src('homeguide-artificial-grass', 'HomeGuide')}; sod cost from a Central Florida contractor ({ext('https://provlawncare.com/blog/sod-installation-cost-central-florida-2026', 'Prov Lawn Care, Jul 2026')}); watering from UF/IFAS; stormwater and water setback from Florida's synthetic turf rule.")),
        sec("What does Florida's 2026 turf rule require that sod never did?",
            f"<p>Rule 62-308.100, effective May 19, 2026, sets minimum standards for synthetic turf on single-family lots of an acre or less statewide, and a local government may not regulate turf more strictly than the rule once it applies ({src('flrules62-308-100', 'FLRules 62-308.100')}; {src('fs125572', 'F.S. 125.572')}). "
            "None of this applies to a living lawn, since sod is not a manufactured product subject to a materials or installation standard.</p>"
            + ul([f"Infill must be clean silica sand, rock, shell or other natural material; rubber or synthetic infill is allowed only under playground equipment ({src('rule62-308-100-text', 'Rule 62-308.100 text')}).",
                  "The subgrade has to be washed natural material such as crushed rock or crushed concrete, laid to keep the whole system permeable.",
                  "In-ground irrigation cannot be used to water a turf area, and a local government may require existing sprinkler heads to be capped.",
                  "Turf has to sit at least 10 feet from a natural or man-made waterbody unless a seawall or bulkhead already forms a barrier.",
                  "Turf cannot be installed inside a tree's drip line unless a certified arborist signs off, and it cannot go in a swale, pond or a pond's littoral zone.",
                  "The rule does not mention homeowners' associations at all; it binds local governments, and a 2026 change carved community development districts' deed-restriction enforcement out of the preemption entirely."])),
        sec("Can I still water turf the way I water sod?",
            f"<p>No, and this is one of the clearest differences between the two. The 2026 rule bars in-ground irrigation systems from watering synthetic turf areas, full stop, which means the sprinkler zone that used to keep a St. Augustine lawn alive either gets capped off or redirected to the landscaping around the turf instead ({src('rule62-308-100-text', 'Rule 62-308.100 text')}). "
            f"Sod, by contrast, is squarely inside both {ext('https://www.sjrwmd.com/wateringrestrictions/', "SJRWMD's")} and {ext('https://www.swfwmd.state.fl.us/business/epermitting/district-water-restrictions', "SWFWMD's")} watering-day schedules, and both districts carve out a temporary allowance specifically for new sod: SJRWMD permits watering at any time for the first 30 days after installation, then every other day for the next 30; SWFWMD's current Modified Phase III order allows daily watering on new plant material for the first 30 days before stepping down to three days a week. "
            f"As of October 2026, Sarasota, Manatee and Polk counties are under that Modified Phase III order through March 31, 2027, with established lawns limited to one watering day a week by address digit ({src('swfwmd-restrictions', 'SWFWMD District Water Restrictions')}; {src('manatee-phase3', 'Manatee County, Jan 2026')}).</p>"),
        sec("When sod is the better fit",
            ul(["A traditional lawn is the look and feel wanted, with no interest in adding a materials standard or permeability requirement to the project.",
                "An existing irrigation system is already in place and the household is comfortable following the current watering-day schedule.",
                "Budget favors the lower upfront cost of resodding over a full turf conversion.",
                "The yard already grows St. Augustine or another cultivar successfully with full sun exposure."])),
        sec("When artificial turf is the better fit",
            ul(["A lawn area has repeatedly struggled to establish under the current once-a-week watering restriction.",
                "The household wants to stop budgeting mowing, fertilizing and pest treatment into the yard's upkeep.",
                "A section of yard will sit inside a tree's drip line or close to water, which narrows what a turf installer can do there under the 2026 rule, so that specific area gets planned around the setback and drip-line requirements from the start.",
                "A dedicated low-traffic accent area, rather than the whole yard, is the actual goal."])),
        sec("Resod or convert: a 1,500 sq ft backyard in Lakewood Ranch",
            f"<p>Say you have a 1,500 square foot backyard in {city('lakewood-ranch', 'Lakewood Ranch')} that has thinned out under SWFWMD's once-a-week schedule, and the choice is resodding in St. Augustine or converting the area to artificial turf. "
            "Resodding at Central Florida contractor pricing runs roughly $1,050 to $2,625, plus the ongoing cost of mowing, fertilizing and the weekly watering allowance the district currently permits. "
            f"Converting the same area to turf runs roughly ${1500*10:,} to ${1500*25:,} at Florida market rates for artificial turf, a far larger upfront number, with no further watering cost afterward since in-ground irrigation on the turf area is off the table under the 2026 rule. Which number makes more sense depends on how many more seasons the household expects to fight the same watering restriction with sod.</p>"),
        sec("Related reading",
            f"<p>{svc('artificial-turf', 'Our artificial turf page')} covers installation, infill and base in full, and the {a('/artificial-turf-cost/', 'artificial turf cost guide')} has size-by-size pricing. "
            f"{post('artificial-turf-heat-in-florida', 'How hot does artificial turf get in Florida')}, {post('artificial-turf-water-savings-florida', 'how much water artificial turf saves')} and {post('florida-hoa-artificial-turf-law', "can your Florida HOA ban artificial turf")} each go deeper into a question this page only touches on. "
            f"{a('/faq/artificial-turf/', 'Our artificial turf FAQ hub')} covers shade, pests and humidity questions in more detail, and {post('backyard-putting-green-florida', 'planning a backyard putting green')} is worth a look if turf is being considered for a specific feature rather than the whole yard.</p>"),
    ])
    faqs = [
        faq("Is artificial turf better than sod in Florida?",
            "Neither is better across the board; the choice depends on what's failing about the current yard. Turf costs far more upfront and skips the weekly watering schedule, mowing and pest treatment sod needs, while sod costs less to install and gives a traditional lawn, as long as the household keeps up with watering-day rules and seasonal lawn care."),
        faq("Does Florida's 2026 turf rule apply to sod?",
            "No. Rule 62-308.100 sets minimum standards specifically for synthetic turf, covering infill, subgrade, setbacks from water and tree drip lines. A living lawn is not a manufactured product and is not subject to any part of that rule."),
        faq("Can I run my sprinklers over artificial turf the way I water sod?",
            "No. The 2026 turf rule prohibits using in-ground irrigation to water a synthetic turf area, and a local government may require existing sprinkler heads in that zone to be capped off. Sod remains on the normal watering-district schedule for its area."),
        faq("Is St. Augustine sod drought-tolerant once it's established?",
            "Not especially. Established St. Augustinegrass still needs at least an inch of water a week and shows visible stress, folding leaf blades, wilting, a blue-gray color, when it goes without. It tolerates occasional dry stretches better than a brand-new lawn does, but it is not a low-water grass."),
        faq("Does artificial turf count against a stormwater or impervious limit the way concrete does, when sod doesn't?",
            "The 2026 turf rule treats turf differently from a hard surface: it requires a permeable backing and pervious subgrade and bars turf from increasing runoff to neighboring property, which is a stricter standard than sod faces but still distinct from how a driveway or patio is measured for stormwater purposes."),
        faq("Does a community development district (CDD) follow the same turf rules as a city?",
            "Mostly, but with one carve-out. The state preemption in F.S. 125.572 binds local governments generally, and a 2026 change to the law specifically exempted a CDD's enforcement of its own deed restrictions from that preemption, which means a CDD can still enforce turf-related deed restrictions separately from what the state rule requires of cities and counties.")]
    return page("/compare/artificial-turf-vs-sod/", "compare", "Artificial Turf vs. Sod: Florida Guide",
                "Artificial turf vs. sod in Florida as of October 2026: cost, watering under the 2026 district restrictions, and what the new DEP turf rule requires that sod doesn't.",
                "Artificial Turf vs Sod in Florida",
                capsule("As of October 2026, artificial turf runs far more per square foot than St. Augustine sod but needs no weekly watering, while sod stays on SJRWMD's and SWFWMD's current watering-day schedules. "
                        "Florida's turf rule, effective May 19, 2026, sets infill, subgrade and water-setback standards sod never faced; no rebate for switching to turf is currently confirmed."),
                body, faqs=faqs,
                sources=["homeguide-artificial-grass", "flrules62-308-100", "fs125572", "rule62-308-100-text", "sjrwmd-watering", "swfwmd-restrictions",
                         "manatee-phase3", ("UF/IFAS, St. Augustinegrass for Florida Lawns", "https://ask.ifas.ufl.edu/publication/LH010"),
                         ("Prov Lawn Care, Central Florida sod cost 2026", "https://provlawncare.com/blog/sod-installation-cost-central-florida-2026")],
                crumbs=[("Comparisons", "/compare/")], crumb="Artificial turf vs. sod", form=False, published="2026-10-01")


def get_pages():
    return [clay_brick_vs_concrete(), driveway_finishes(), resurface_vs_replace(), polymeric_vs_regular_sand(),
            wet_look_vs_natural_sealer(), turf_vs_sod()]
