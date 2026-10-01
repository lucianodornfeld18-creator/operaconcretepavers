# -*- coding: utf-8 -*-
"""Blog posts, module c_posts_c: pool deck heat, slip fixes, saltwater/salt air, sinkholes vs settlement,
artificial turf heat, artificial turf for dogs. See research/blog-plan.csv for the plan and research/questions.csv
for the owned questions."""
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, cs, post, compare, src, ext, price, per, contact, photo
from _data import PRICE_DATE


def how_hot_do_pool_decks_get():
    body = "".join([
        sec("What Is the Coolest Pool Deck Surface for Bare Feet?",
            "<p>Among the surfaces we install, light-colored natural stone, travertine and shell stone, tests as the coolest underfoot in direct Florida sun, with a light acrylic coating such as Kool Deck close behind. Dark stamped concrete and dark concrete pavers run hottest. No single lab has measured every one of these materials side by side under Florida sun, so treat this as a ranking by color and material rather than a chart of exact degrees.</p>"
            f"<p>Two properties do almost all the work. A light surface reflects more sunlight than it absorbs, so it simply takes in less solar energy to begin with; a dark surface absorbs more and turns it into heat at the surface. Material comes second: a dense, light-colored stone like travertine holds less of that heat than a dense, dark-colored unit like a charcoal concrete paver. {svc('pool-deck-pavers')} and {svc('concrete-pool-decks')} both come in light finishes for exactly this reason, and it's worth asking about color before anything else when picking a pool deck surface.</p>"
            + (photo("pool-deck-pavers", "Light-toned pavers surround a resort-style pool deck shaded by palm trees, with wicker furniture and a linear fire pit along the edge.") or "")),
        sec("Why Does Color Matter More Than Material?",
            f"<p>Color sets how much solar energy a surface absorbs before material properties ever come into play. Federal heat-island research puts dark asphalt paving's midday surface reading as high as 152°F, with a lighter-colored, more reflective pavement option measured 10 to 16°F cooler on the same day in an Arizona field test ({src('epa-cool-pavements', 'EPA')}). That work covers pavements broadly, not a Florida pool deck test by itself, but the underlying principle holds for any outdoor surface baking in direct sun: light reflects, dark absorbs. It's why a pale concrete sealer reads cooler underfoot than a charcoal one, and why a light travertine deck outperforms a dark paver even though both are equally hard, mineral surfaces.</p>"),
        sec("Travertine and Shell Stone: Why They Run Cooler",
            f"<p>Travertine and shell stone, quarried coquina with visible shell fragments running through it, share two traits that keep them toward the cool end of the range: a pale, naturally variable color straight from the quarry, with no dark pigment added, and a matte, textured face rather than a polished one. {svc('pool-deck-pavers')} covers both materials alongside concrete pavers for the same deck. No Florida-specific lab reading separates travertine from concrete by a measured number, so we won't publish one, but the color and finish line up with the reflectance principle above.</p>"),
        sec("What About Stamped and Colored Concrete?",
            f"<p>A stamped pattern changes a slab's texture, not its color, and texture alone doesn't lower surface temperature the way color does. A stamped deck finished in a pale sand or buff tone performs close to plain broom concrete in the same shade; the same pattern finished in a dark charcoal or terra-cotta release color runs hotter, the same way a dark stamped driveway runs hotter than a light one in full sun. {svc('stamped-concrete')} covers color and release options in more depth. For a pool deck specifically, we steer homeowners away from the darkest end of any stamped color chart, especially around the stairs and shallow end where people stand the longest.</p>"),
        sec("Does Kool Deck or an Acrylic Coating Help?",
            f"<p>Manufacturers describe Kool Deck-style acrylic coatings as staying cooler than plain concrete or other decking surfaces, and say the line's darker 'Designer' colors run warmer than its standard colors, though the manufacturer publishes no specific degree figure for either claim ({src('mortex-kooldeck-brochure', 'Mortex')}). That matches the color principle above: a pale acrylic coating reflects more sunlight than a dark one. Resurfacing with an acrylic coating is one of the lower-cost ways to lighten an existing dark deck without a full tear-out. {svc('concrete-pool-decks')} and the {a('/pool-deck-cost/', 'pool deck cost guide')} cover what that resurfacing runs as of {PRICE_DATE}.</p>"
            + table("Pool deck surfaces by heat tendency",
                    ["Surface", "Typical color range", "What drives its heat", "Installed cost"],
                    [["Travertine or shell stone, light tones", "Pale, naturally variable", "Light color, matte texture", f"{price('pool-deck-pavers')} per {per('pool-deck-pavers')}"],
                     ["Acrylic coating, light colors", "Wide range; lightest standard colors run coolest", "Thin, reflective coating", f"{price('concrete-pool-deck')} per {per('concrete-pool-deck')}"],
                     ["Broom-finish concrete, light sealer", "Gray to tan", "Color is the main variable", f"{price('concrete-pool-deck')} per {per('concrete-pool-deck')}"],
                     ["Concrete pavers, light tones", "Wide color range", "Dense material; heat follows color", f"{price('pool-deck-pavers')} per {per('pool-deck-pavers')}"],
                     ["Stamped concrete or dark pavers", "Often darker: charcoal, terra-cotta", "Dark color absorbs the most heat", f"{price('stamped-concrete')} per {per('stamped-concrete')}"]],
                    f"Florida market ranges as of {PRICE_DATE}, compiled from published cost-guide and contractor data; see sources below.")),
        sec("Practical Ways to Keep a Pool Deck Cooler",
            "<p>Short of replacing the whole deck, a few changes move the needle more than the rest.</p>"
            + ul(["Pick a light sealer or coating color on the next resurfacing or reseal, rather than matching the darker color that's already there.",
                  "Put real shade, a pergola, a large umbrella or the screen enclosure's own roofline, over the stretch of deck used most, since the sun angle changes through the day and a cage's screen alone doesn't block every square foot.",
                  "Hose the deck down before bare feet or small kids use it at midday; it's a short-term fix, not a permanent one, but it works in the moment.",
                  "Keep the darkest material or color off the areas people stand longest: the stairs, the shallow end, and any spot right next to a hot tub or sun shelf."])),
        sec("A Quick Example",
            f"<p>Say you have a west-facing pool deck in a 2010s Lakewood Ranch subdivision with no overhead shade until early evening. A dark stamped finish in that orientation sits in direct sun through the hottest hours of the afternoon. Switching the plan to a light stamped color, or to pale travertine around the coping where bare feet land most, changes more than any coating or sealer applied later. {post('how-to-choose-a-paver-contractor-sarasota', 'A Sarasota paver contractor')} can walk a specific yard's sun exposure before you commit to a finish.</p>"),
        sec("Related Reading",
            ul([post("slippery-pool-deck-fixes", "making a slippery pool deck safer"),
                post("saltwater-pools-and-coastal-salt-air-hardscape", "protecting a coastal pool deck from salt air"),
                post("artificial-turf-heat-in-florida", "how hot artificial turf runs by comparison"),
                compare("travertine-vs-concrete-pavers", "travertine vs. concrete pavers")])),
    ])
    faqs = [
        faq("Is travertine really cooler than concrete around a pool?",
            f"Generally yes, for two reasons: it's almost always a lighter color than standard gray or dark concrete, and a light color reflects more sunlight than a dark one absorbs. No independent Florida lab test compares the two surfaces side by side, so treat this as a color-and-material ranking rather than a measured temperature gap. {svc('pool-deck-pavers')} covers travertine alongside shell stone and concrete pavers."),
        faq("Does resurfacing with Kool Deck actually lower surface temperature?",
            f"The manufacturer describes its coating as staying cooler than plain concrete, without a specific degree figure, and says its darker 'Designer' colors run warmer than the standard line ({src('mortex-kooldeck-brochure', 'Mortex')}). Choosing one of the lighter standard colors is the more reliable lever than the coating itself."),
        faq("Why does a dark stamped deck feel hotter than plain gray concrete?",
            "Texture from a stamped pattern doesn't change how much sunlight a surface absorbs; color does. A stamped deck finished in a dark charcoal or terra-cotta release color absorbs more solar energy than the same pattern in a pale sand or buff tone, the same reason a dark car seat gets hotter than a light one left in the sun."),
        faq("Can I make an existing pool deck cooler without replacing it?",
            f"Often, yes. Resealing plain concrete in a lighter color, or resurfacing with a light acrylic coating, changes the color without a tear-out. {compare('cool-deck-vs-pavers-vs-travertine', 'Resurfacing versus replacing with pavers or travertine')} compares the full set of options and what each one costs."),
        faq("Does shade from a screen enclosure help with deck heat?",
            "Wherever its panels or roofline actually block direct sun on the deck below, yes; a screen cage alone doesn't shade every square foot, since the sun angle changes through the day. Pairing real shade with a lighter surface color does more than either change on its own."),
    ]
    return page("/blog/how-hot-do-pool-decks-get-florida/", "post",
                "The Coolest Pool Deck Surface for a Florida Backyard",
                "Color predicts the coolest Florida pool deck surface: light travertine, shell stone and light acrylic coatings beat dark stamped concrete, as of Oct. 2026.",
                "How Hot Do Pool Decks Get in Florida? The Coolest Surfaces Compared by Feel",
                capsule("No single Florida study has measured every pool deck material side by side, but material and color predict heat better than anything else: light-toned travertine, shell stone and acrylic coatings like Kool Deck stay noticeably cooler underfoot in direct sun than dark stamped or broom concrete. As of October 2026, color is the first thing worth checking before choosing a deck surface in Greater Orlando or Sarasota-Manatee."),
                body, faqs=faqs,
                sources=["epa-cool-pavements", "mortex-kooldeck-brochure", "homeguide-pool-deck", "homeguide-travertine", "poolmechanic-pooldeck-cfl"],
                related=[("/pool-deck-pavers/", "pool deck pavers"), ("/concrete-pool-decks/", "concrete pool decks"),
                         ("/pool-deck-cost/", "pool deck cost guide"), ("/compare/cool-deck-vs-pavers-vs-travertine/", "cool deck vs. pavers vs. travertine"),
                         ("/blog/artificial-turf-heat-in-florida/", "how hot artificial turf gets")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="pool-deck-pavers", image="pool-deck-pavers", form=False)


def slippery_pool_deck_fixes():
    body = "".join([
        sec("How Do You Make a Pool Deck Less Slippery?",
            "<p>Most slick decks get fixed one of three ways: cleaning off the film that's causing the slip (algae, mineral scale or built-up sealer), adding texture back to a surface that's worn smooth, or switching to a sealer or coating with an anti-slip additive mixed in. Which one applies depends on whether the deck is actually slicker than it used to be, or whether it was finished too smooth from the start.</p>"
            f"<p>A deck that's gotten slicker over time usually has something sitting on top of the surface rather than a problem with the material itself. {post('mold-and-algae-on-pavers-florida', 'Algae and mold')} in shaded, damp spots is the most common culprit in both service areas; a cloudy mineral film from hard water and splash-out is the second. A deck that was never textured enough, often a trowel-smooth finish or a honed stone, needs a mechanical or chemical fix rather than just a cleaning.</p>"
            + (photo("concrete-pool-deck", "A broom-finished concrete pool deck with a tile accent band circles a modern pool and spa beside a contemporary house.") or "")),
        sec("Why Pool Decks Get Slick in Florida",
            f"<p>Shade, standing moisture and a warm, humid climate are a reliable recipe for algae and mold, and a pool deck has all three in spots the sun doesn't reach for most of the day. Sealer buildup is the second common cause: each new coat applied over an old one without stripping first adds a thin, smoother film, and after several cycles a once-textured surface can read almost glassy. A worn broom finish is the third: years of foot traffic, pressure washing and sun exposure gradually round off the fine texture a broom leaves in fresh concrete, which is a maintenance issue rather than a sign the slab needs replacing. {svc('paver-sealing')} and {svc('concrete-pool-decks')} both touch on cleaning and resealing; this page focuses specifically on the slip problem.</p>"),
        sec("What 'Slip Resistant' Actually Means",
            f"<p>Florida's rule for public pools, F.A.C. Chapter 64E-9, binds shared-use pools (HOA, condo, apartment and hotel pools) rather than a single-family backyard, but it's the closest published Florida standard for deck surfaces and contractors still use it as a target on residential work ({ext('https://www.flrules.org/gateway/ChapterHome.asp?Chapter=64E-9', 'F.A.C. 64E-9')}). For a private in-ground pool, the Florida Residential Code instead points to a national construction standard, ANSI/APSP/ICC-5, for design and workmanship rather than spelling out its own slip-resistance numbers (FBC Residential R4501.6.1, {ext('https://up.codes/viewer/florida/fl-residential-code-2023/chapter/45/private-swimming-pools', 'up.codes copy of Ch. 45')}). On the tile-industry side, a 2021 update to ANSI A326.3 set a minimum wet dynamic coefficient of friction of 0.50 to 0.55 for pool deck surfaces specifically, tighter than the 0.42 minimum used for ordinary wet walkways ({ext('https://tcnatile.com/critical-product-testing-for-new-uniform-swimming-pool-spa-and-hot-tub-slip-resistance-code/', 'Tile Council of North America')}). None of these numbers get measured on a typical residential job, but they explain why a textured, matte finish is the standard answer and a glossy, polished one isn't.</p>"),
        sec("Fixes for an Existing Slippery Deck",
            "<p>The right fix depends on what's actually causing the slip.</p>"
            + table("Slippery deck problems and fixes",
                    ["What you have", "Likely cause", "Fix"],
                    [["Honed or polished travertine", "Smooth factory finish", "Switch to a tumbled or brushed finish on replacement units, or add an anti-slip sealer additive"],
                     ["Worn, smooth broom-finish concrete", "Years of foot traffic and pressure washing have rounded off the texture", "Light surface grinding or acid etching, then reseal with a textured or matte product"],
                     ["Stamped concrete, glossy after several seal coats", "Sealer buildup, or the wrong sheen for a wet area", "Strip and reseal with a matte, slip-rated sealer and an anti-slip additive mixed in"],
                     ["Green or black film in shaded spots", "Algae or mold growth", "Clean and treat, then reseal; see the mold and algae post below"],
                     ["Cloudy white haze that feels slick when wet", "Mineral or efflorescence buildup", "Clean with the right method for the surface, not a generic acid wash; see the efflorescence post below"]],
                    f"{src('icpi-ts5', 'ICPI Tech Spec 5')} on paver cleaning and sealing.")),
        sec("Can You Add Slip Resistance Without Replacing the Deck?",
            "<p>In most cases, yes. A broadcast anti-slip additive, fine polymer or grit beads worked into a fresh sealer coat before it cures, is the most common fix on both concrete and sealed pavers and doesn't change the surface's color. Light mechanical grinding, sometimes called scarifying, cuts fresh texture into concrete that's been worn glass-smooth, and an acid etch does the same job chemically on a dense trowel-finished slab. Concrete pavers can usually be cleaned, re-sanded and resealed with a textured product rather than pulled up. The harder case is honed or polished natural stone: roughening it back up usually means replacing those units with a tumbled or brushed finish rather than treating the existing surface, since grinding stone down repeatedly removes real thickness.</p>"),
        sec("When Does the Deck Need Replacing Instead of Treating?",
            f"<p>If the slick spot sits over a crack, a hollow-sounding section or a part of the deck that's sunk or heaved, resurfacing or adding an anti-slip coat only hides a base problem that keeps moving underneath it. {compare('resurface-vs-replace-concrete', 'Resurface or replace a concrete driveway')} works through that same decision for a driveway, and the logic carries over to a pool deck. If a full new surface turns out to be the better call, the {a('/pool-deck-cost/', 'pool deck cost guide')} breaks down what a new pour, an overlay or new pavers run in Florida.</p>"),
        sec("A Quick Example",
            "<p>Say a pool deck in a 1990s Orlando subdivision has had three sealer coats applied over fifteen years without ever being stripped first. The surface now looks glossy and feels slick the moment it's wet, even though the broom texture under those coats is probably still intact. Stripping back to bare concrete and resealing with a matte, slip-rated product, rather than adding a fourth coat, is usually the fix that actually works.</p>"),
        sec("Related Reading",
            ul([svc("concrete-pool-decks"), svc("paver-sealing"),
                post("mold-and-algae-on-pavers-florida", "stopping mold and algae on concrete and pavers"),
                post("efflorescence-on-pavers-and-concrete", "what the white haze on new concrete and pavers is")])),
    ])
    faqs = [
        faq("What's the fastest fix for a slippery pool deck before a pool party?",
            "A thorough cleaning, removing algae film, sunscreen residue and any loose sand or dirt, fixes a surprising share of 'suddenly slick' complaints on its own, since a layer of grime on top of a textured surface is often the real problem. It won't fix a deck that was finished too smooth to begin with; that needs the sealer or texture work above, which isn't a same-day job."),
        faq("Do anti-slip additives change how a sealed deck looks?",
            "A little. Most additives add a faint, fine texture you can feel underfoot and sometimes see as a subtle matte sheen rather than a glossy one, but they don't change the surface's color or pattern. Ask to see a sample panel before a full deck gets coated, since products vary in how coarse that texture feels."),
        faq("Is acid etching safe on travertine or only concrete?",
            "Acid etching is a concrete and some paver technique; it isn't the right method for natural stone like travertine, which reacts differently to acid and can etch unevenly or dull its finish. Travertine that's too smooth usually needs mechanical re-texturing or replacement with a tumbled or brushed finish instead."),
        faq("How often does a slip-resistant sealer need to be redone?",
            "There's no fixed published interval; it depends on foot traffic, sun exposure and how often the deck gets pressure washed. Watch for the surface starting to feel glossy again or the texture smoothing out underfoot, rather than counting years, and plan on stripping old coats periodically instead of layering a new one over every old one."),
        faq("Does a rougher texture mean a dirtier-looking deck?",
            "A more textured surface does tend to hold a bit more dirt and sunscreen residue between cleanings than a smooth one, which is part of the trade-off. Regular rinsing keeps that from building into a stain, and the traction a textured finish adds around a pool matters more than a small difference in how often it needs a hose-down."),
    ]
    return page("/blog/slippery-pool-deck-fixes/", "post",
                "Fixing a Slippery Pool Deck in Florida",
                "Fixes for a slippery pool deck in Florida: cleaning, re-texturing, anti-slip sealer additives and when the slab needs replacing instead of treating.",
                "How to Make a Slippery Pool Deck Safer",
                capsule("A slippery pool deck usually traces back to one of three things: algae or mineral film sitting on top of the surface, sealer buildup from recoating without stripping, or a finish that was too smooth to start with. Cleaning, re-texturing and an anti-slip sealer additive fix most existing decks in Greater Orlando and Sarasota-Manatee without a full replacement, as of October 2026."),
                body, faqs=faqs,
                sources=["icpi-ts5", "homeguide-pool-deck-resurfacing", "mortex-kooldeck-brochure",
                         ("Florida Residential Code, Private Swimming Pools, Ch. 45 (up.codes copy)", "https://up.codes/viewer/florida/fl-residential-code-2023/chapter/45/private-swimming-pools"),
                         ("F.A.C. Chapter 64E-9, Public Swimming Pools and Bathing Places", "https://www.flrules.org/gateway/ChapterHome.asp?Chapter=64E-9"),
                         ("Tile Council of North America, ANSI A326.3 pool and spa slip-resistance testing", "https://tcnatile.com/critical-product-testing-for-new-uniform-swimming-pool-spa-and-hot-tub-slip-resistance-code/")],
                related=[("/concrete-pool-decks/", "concrete pool decks"), ("/paver-sealing/", "paver sealing and restoration"),
                         ("/blog/mold-and-algae-on-pavers-florida/", "stopping mold and algae"), ("/compare/resurface-vs-replace-concrete/", "resurface or replace"),
                         ("/blog/how-hot-do-pool-decks-get-florida/", "the coolest pool deck surface")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-pool-decks", image="concrete-pool-deck", form=False)


def saltwater_pools_and_coastal_salt_air():
    body = "".join([
        sec("Does a Saltwater Pool Damage Travertine or Concrete?",
            f"<p>Not much on its own. A saltwater chlorine generator runs at roughly 2,700 to 3,600 parts per million of salt, less than a tenth of ocean water's roughly 35,000 ppm, so the pool itself is mild compared to the Gulf ({ext('https://www.troublefreepool.com/wiki/index.php?title=Salt', 'TroubleFreePool')}). What does the damage along the coast is the combination of splash-out concentrating that salt on the coping over and over, plus airborne salt from the Gulf settling on every outdoor surface nearby, pool or no pool. Porous stone stains and weathers faster under that combination than dense concrete does, and exposed metal corrodes faster than either.</p>"
            + (photo("interlocking-pavers", "A close-up, top-down view of gray interlocking concrete pavers fitted tightly together.") or "")),
        sec("Why Coastal Salt Air Is the Bigger Factor",
            f"<p>FDOT's engineering standard draws the line at 2,000 parts per million of chloride within 2,500 feet of the water, the point where it starts calling a structure a marine environment, and raises that to an extremely aggressive classification above 6,000 ppm for both what's above and below grade ({src('fdot-sdg', 'FDOT Structures Design Guidelines')}). That's a bridge and structures standard, not a code requirement for a residential driveway or patio, but it's a useful yardstick: homes on {city('longboat-key')}, {city('siesta-key')} or {city('anna-maria-island')} sit well inside that distance from salt water on every side, where a home a mile or two inland in {city('sarasota')} or {city('bradenton')} does not. Salt air reaches a pool deck, a driveway or a patio the same way it reaches a dock, slowly and constantly, rather than only where water splashes directly.</p>"),
        sec("Protecting Travertine and Shell Stone From Salt",
            f"<p>Both stones are porous enough that salt residue and moisture work into the surface over repeated cycles rather than washing off completely between rinses, which shows up as a dull, grayish film that keeps coming back faster than ordinary weathering would explain. Sealing slows that absorption; ICPI's own guidance on paver and stone care sets no fixed resealing interval, since traffic, sun and in this case salt exposure all shift the timeline ({src('icpi-ts5', 'ICPI Tech Spec 5')}). On a coastal deck we lean toward resealing on the shorter end of whatever range a product's maker recommends, and we rinse the coping and the first few paver courses with fresh water on a tighter schedule than the rest of the deck, since that's the zone carrying the most concentrated residue. {post('travertine-pool-deck-care', 'Our travertine pool deck care guide')} covers the full routine.</p>"),
        sec("Protecting Concrete Near a Saltwater Pool",
            "<p>Plain concrete holds up to salt better than porous stone does, but two details still matter on the coast. First, any crack that opens up near the coping or an edge is worth watching for a reddish-brown stain bleeding out of it; that's a sign of rust working on embedded wire mesh or rebar, different from the white haze of ordinary efflorescence, and it means moisture and salt have reached the steel inside. Second, the flexible sealant in a pool deck's isolation joint and in any control joint near the water breaks down faster under constant salt and UV exposure than it does further inland, so we check and recaulk those joints on a shorter cycle on coastal jobs.</p>"),
        sec("What About Pool Equipment and Metal Fixtures?",
            "<p>Ladders, handrails, light fixtures and the chlorine generator's own hardware are a pool-equipment question rather than a hardscape one, and salt air accelerates corrosion on all of them faster than it damages the concrete or pavers around them. If a pool builder or service company hasn't already specified corrosion-resistant hardware for a coastal install, that's worth raising with them directly; it's outside what a concrete and paver contractor specifies or installs.</p>"),
        sec("How Often Should Coastal Pavers and Concrete Be Rinsed and Sealed?",
            f"<p>We recommend hosing down the coping and the first several feet of deck weekly on a home within a mile or two of the Gulf, rather than the monthly rinse that works fine further inland, because salt residue left to dry and reconcentrate day after day bonds to a porous surface harder each cycle than a single heavy exposure would. Sealing on the shorter end of a product's recommended range follows the same logic. {svc('paver-sealing')} covers cleaning, re-sanding and sealing for pavers specifically; {svc('concrete-pool-decks')} and {svc('pool-deck-pavers')} cover the decks themselves.</p>"),
        sec("A Quick Example",
            f"<p>Say you have a travertine pool deck two blocks from the Gulf on {city('siesta-key')}. Splash-out concentrates salt on the coping daily, onshore breeze adds more to the whole deck even on days nobody swims, and both effects stack on top of ordinary Florida sun and rain. A weekly fresh-water rinse of the coping, paired with sealing on a shorter interval than the same deck would need in {city('lakewood-ranch')}, is the practical response; nothing about the build itself needs to change.</p>"),
        sec("Related Reading",
            ul([post("travertine-pool-deck-care", "travertine pool deck care: cleaning, sealing and filling holes"),
                post("efflorescence-on-pavers-and-concrete", "the white haze on new pavers and concrete"),
                compare("travertine-vs-concrete-pavers", "travertine vs. concrete pavers"),
                svc("paver-sealing")])),
    ])
    faqs = [
        faq("Does a saltwater chlorine generator corrode rebar inside a concrete pool deck?",
            "It's a secondary contributor at most. A saltwater pool runs far below seawater concentration, and splash-out affects only the coping and the nearest paving; ordinary airborne salt from the Gulf reaches every exposed surface in a coastal yard regardless of whether the pool itself uses salt or traditional chlorine. A reddish stain bleeding from a crack is the sign worth watching for either way."),
        faq("How close to the coast does salt air actually become a factor?",
            f"There's no single Florida homeowner threshold, but FDOT treats structures within 2,500 feet of salt water as a more corrosive environment for engineering purposes ({src('fdot-sdg', 'FDOT Structures Design Guidelines')}). Homes on barrier islands like {city('longboat-key')} or {city('anna-maria-island')} sit well inside that range on every side; the effect fades gradually moving inland rather than stopping at a hard line."),
        faq("Will a saltwater pool stain my pavers?",
            "Splash-out and evaporation can leave a dull, recurring white or gray residue on the coping and nearest paver courses, more a repeating cycle tied to pool use than the one-time bloom of ordinary efflorescence. Sealed stone resists that staining far better than the same material left bare."),
        faq("Should coastal pavers and pool decks be sealed more often than inland ones?",
            "Generally yes, toward the shorter end of whatever interval a product's manufacturer recommends, since constant salt exposure adds to ordinary sun and traffic wear. There's no single published number for how much shorter that interval should be; watch for the surface losing its water-beading finish rather than counting a fixed number of years."),
        faq("Does salt air affect a concrete driveway the same way it affects a pool deck?",
            "Yes, if the driveway sits within roughly a mile or two of salt water; the exposure comes from the air, not from the pool, so a driveway on the same coastal lot weathers under the same conditions as the deck out back. Rinsing and sealing on a similar schedule applies to both."),
    ]
    return page("/blog/saltwater-pools-and-coastal-salt-air-hardscape/", "post",
                "Saltwater Pools and Salt Air on the Sarasota Coast",
                "Saltwater pools run mild compared to the Gulf, but coastal salt air still stains travertine and corrodes exposed steel. Sarasota-Manatee guidance as of October 2026.",
                "Saltwater Pools and Salt Air: Protecting Concrete, Pavers and Travertine on the Coast",
                capsule("A saltwater pool itself is mild, roughly a tenth of ocean salinity, so the bigger threat to concrete, pavers and travertine on the Suncoast is airborne salt from the Gulf, not the pool's own chlorine generator. Splash-out concentrates that salt on the coping, porous stone stains faster than dense concrete, and exposed metal corrodes fastest of all. Rinsing and sealing on a shorter cycle than an inland home needs is the practical fix, as of October 2026."),
                body, faqs=faqs,
                sources=["fdot-sdg", "icpi-ts5", "homeguide-travertine",
                         ("TroubleFreePool, saltwater pool salt levels vs. ocean salinity", "https://www.troublefreepool.com/wiki/index.php?title=Salt")],
                related=[("/pool-deck-pavers/", "pool deck pavers"), ("/concrete-pool-decks/", "concrete pool decks"),
                         ("/paver-sealing/", "paver sealing and restoration"), ("/blog/travertine-pool-deck-care/", "travertine pool deck care"),
                         ("/compare/travertine-vs-concrete-pavers/", "travertine vs. concrete pavers")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="pool-deck-pavers", image=None, form=False)


def sinkholes_and_settlement():
    body = "".join([
        sec("Is a Sunken Slab a Sign of a Sinkhole?",
            f"<p>Almost always no. The far more common explanation for a sunken driveway, patio or slab is ordinary settlement, soil underneath compressing under the weight of the slab or shifting from moisture changes, not Florida's limestone geology giving way. Florida Geological Survey draws a clear line between the two: a cover-collapse sinkhole forms suddenly when soil ravels down into a cavity already dissolved in the limestone below, while a cover-subsidence sinkhole develops gradually as the same thing happens more slowly ({src('fgs-sinkhole-faq', 'FDEP/FGS Sinkhole FAQ')}). Ordinary settlement is a different mechanism entirely: no void in the limestone, just soil doing what soil does under load or moisture change.</p>"
            + (photo("finishing-concrete", "A worker finishes a freshly poured concrete slab, kneeling with a trowel.") or "")),
        sec("Where Sinkhole Risk Actually Concentrates in Florida",
            f"<p>Risk isn't evenly spread across the state, and it isn't evenly spread across our own service area either. A 2010 Florida Senate interim report, citing the Office of Insurance Regulation, found that Hernando, Pasco and Hillsborough accounted for more than 66 percent of sinkhole insurance claims from 2006 to 2009, and that eleven counties together, including Orange, accounted for more than 88 percent of claims statewide ({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). The total across the 2006-2010 data call ran to 24,671 claims statewide ({src('floir-2010-sinkhole', 'FL OIR 2010 Sinkhole Data Call')}).</p>"
            + table("Sinkhole claims concentration, Greater Orlando counties",
                    ["County", "On the 11-county high-claims list?", "Note"],
                    [["Orange", "Yes", "Named directly in the Senate report's 88-percent list"],
                     ["Lake", "No", "FGS staff describe similar shallow-limestone geology, not a claims-count match"],
                     ["Seminole", "No", "Same FGS geology note as Lake; not on the claims list"],
                     ["Osceola", "Not found", "No sinkhole-frequency source for Osceola was found in this research; don't assume either way"],
                     ["Polk", "Yes", "Named directly in the Senate report's 88-percent list"]],
                    f"{src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}. Hernando, Pasco and Hillsborough, outside our service area, carry the largest share by far.")),
        sec("How to Tell Settlement From a Sinkhole at a Glance",
            "<p>Neither of us can diagnose the ground underneath a slab by looking at a crack, but a few patterns point one way more than the other. Settlement tends to show as a gradual dip confined to one slab or one section of it, often where a base wasn't compacted evenly or where water has been draining under an edge for years. It stays roughly the same shape over time once the cause is addressed. Sinkhole activity more often shows as a circular or oval depression that keeps deepening, sometimes appears away from any structure entirely, and can come with doors or windows binding, new cracks that radiate from a point, or cloudy well water if the property uses one. A single sunken slab with no other symptoms anywhere else on the property leans heavily toward settlement.</p>"),
        sec("What Causes Ordinary Settlement Under a Driveway or Slab",
            f"<p>Most of what we see traces back to the base, not the concrete mix. A subgrade that wasn't compacted evenly before the pour settles unevenly afterward, especially on Central Florida's flatwoods soils where a seasonal high water table complicates compaction. Decomposing organic material left under fill, an old tree stump, roots or construction debris, does the same thing as it breaks down and leaves a void behind; Florida Geological Survey lists exactly that, along with collapsed drain pipes and improperly compacted soil after excavation, as common non-karst causes of a depression that gets reported and investigated but turns out not to be a true sinkhole ({src('fgs-sinkhole-faq', 'FDEP/FGS Sinkhole FAQ')}). A downspout or irrigation line draining against a slab edge for years can wash fines out from under it the same way.</p>"),
        sec("What to Do If You Suspect a Sinkhole",
            "<p>If a depression looks like more than ordinary settlement, especially a circular hole that keeps growing, a structured response matters more than guessing.</p>"
            + steps([("Mark and secure the area.", "Keep people, pets and vehicles away from the depression until it's been looked at."),
                     ("Call your homeowners insurance adjuster.", "Report it right away, since Florida law sets specific coverage rules for a confirmed ground-cover collapse."),
                     ("Call the FGS Sinkhole Helpline at 850-245-2118.", "Florida Geological Survey tracks reported incidents in its subsidence database and can advise on next steps."),
                     ("Get a geotechnical evaluation before any concrete or paver work goes back in.", "A structural or geotechnical engineer, not a hardscape contractor, determines whether the cause is karst activity or ordinary settlement.")])
            + f"<p>{src('fgs-sinkhole-faq', 'FDEP/FGS Sinkhole FAQ')} covers the reporting process in more detail.</p>"),
        sec("Insurance: What Florida Law Actually Requires",
            f"<p>F.S. 627.706 requires every Florida property insurer to cover catastrophic ground cover collapse, but only when all four conditions are met at once: an abrupt collapse, a visible depression, structural damage that reaches the foundation, and a structure condemned and ordered vacated ({src('fs-627-706', 'F.S. 627.706')}). A broader 'sinkhole loss' policy, covering damage that doesn't meet that four-part test, is optional and sold for an added premium. Whether a specific claim, including a cracked driveway or pool deck on its own, is covered depends on the policy and the cause; the {a('/faq/cost-and-permits/', 'cost and permits FAQ')} covers that insurance question in more general terms.</p>"),
        sec("Repairing a Settled Slab vs. Repairing Sinkhole Damage",
            f"<p>Ordinary settlement is squarely a hardscape repair: releveling an existing slab, patching and resurfacing, or cutting out and replacing a section that's too far gone are all standard work. {svc('concrete-repair')} covers that range, and {compare('resurface-vs-replace-concrete', 'resurface or replace a concrete driveway')} walks through how to decide between them. Confirmed sinkhole activity is a different project entirely: it needs a geotechnical investigation and engineered remediation, grouting or underpinning, before any new concrete or pavers go back in, and that's outside what a concrete and paver contractor scopes or performs. We'll tell a homeowner plainly when a crack or a depression looks like it needs that kind of engineering sign-off before we touch the surface.</p>"),
        sec("Related Reading",
            ul([svc("concrete-repair"), svc("concrete-slabs"),
                post("concrete-driveway-cracks-florida", "which driveway cracks are normal in Florida"),
                post("tree-roots-under-driveway-florida", "tree roots under a driveway or sidewalk")])),
    ])
    faqs = [
        faq("What's the difference between a cover-collapse and a cover-subsidence sinkhole?",
            f"Both start with soil raveling into a cavity already dissolved in the limestone below. A cover-collapse sinkhole does that suddenly, often overnight; a cover-subsidence sinkhole does it gradually, over months or years, and can look a lot like ordinary settlement until it's investigated ({src('fgs-sinkhole-faq', 'FDEP/FGS Sinkhole FAQ')})."),
        faq("Does Orange County have a high sinkhole risk?",
            f"Orange County appears on the 11-county list that accounted for more than 88 percent of Florida's sinkhole insurance claims in a 2006-2009 data review, but it's well behind Hernando, Pasco and Hillsborough, the counties that made up the bulk of that total ({src('fl-senate-2011-104', 'Florida Senate Interim Report 2011-104')}). A high county-level ranking doesn't mean any specific property is at risk; most sunken slabs in Orange County, like anywhere else, turn out to be settlement."),
        faq("Can a sunken spot near a pool deck be a sinkhole?",
            "It's almost always ordinary base settling near the coping rather than anything happening under the pool itself, the same pattern we see on concrete and paver pool decks generally. The signs worth escalating are the same as anywhere else: a growing circular depression, or symptoms showing up in more than one spot on the property."),
        faq("Who do I call if I think I have a sinkhole in Central Florida?",
            "Start with your homeowners insurance adjuster, since a claim often needs to be opened before any investigation, then the Florida Geological Survey's Sinkhole Helpline at 850-245-2118 to have the incident logged and get guidance on next steps. A geotechnical engineer, not a concrete or paver contractor, makes the final call on cause."),
        faq("Will mudjacking or polyjacking fix a slab over a real sinkhole?",
            "No. Mudjacking and polyjacking relevel a slab by filling the void underneath it, which works well for ordinary settlement but doesn't address an active cavity in the limestone below. Releveling a slab over unconfirmed sinkhole activity without a geotechnical evaluation first risks masking the problem rather than fixing it."),
    ]
    return page("/blog/sinkholes-and-settlement-central-florida/", "post",
                "Sinkhole or Settlement? Reading a Sunken Slab",
                "Most sunken slabs in Central Florida are ordinary settlement, not sinkholes. How to tell the difference and what Florida law requires, Oct. 2026.",
                "Sinkholes vs Normal Settlement: What a Sunken Slab in Central Florida Really Means",
                capsule("A sunken driveway, patio or slab in Central Florida is almost always ordinary settlement, soil compressing or shifting under the load, rather than a sinkhole. Orange and Polk counties sit on Florida's broader list of higher sinkhole-claims counties, well behind Hernando, Pasco and Hillsborough, which account for most claims statewide. A circular, growing depression away from any structure is the pattern worth a geotechnical look, as of October 2026."),
                body, faqs=faqs,
                sources=["fgs-sinkhole-faq", "fl-senate-2011-104", "floir-2010-sinkhole", "fs-627-706"],
                related=[("/concrete-repair/", "concrete repair and resurfacing"), ("/concrete-slabs/", "concrete slabs"),
                         ("/compare/resurface-vs-replace-concrete/", "resurface or replace a concrete driveway"),
                         ("/blog/concrete-driveway-cracks-florida/", "which driveway cracks are normal in Florida"),
                         ("/concrete-repair-cost/", "concrete repair cost guide")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="concrete-repair", image="finishing-concrete", form=False)


def artificial_turf_heat():
    body = "".join([
        sec("How Hot Does Artificial Turf Get in Florida?",
            f"<p>Hotter than almost anything else in a Florida yard. UF/IFAS Extension in Orange County reports that on peak summer days, synthetic turf surface temperatures can run up to 100°F hotter than natural grass nearby, reaching as high as 160°F, while living grass stays far more moderate thanks to shade and the cooling effect of transpiration ({ext('https://blogs.ifas.ufl.edu/orangeco/2025/04/15/synthetic-turf-and-the-environment/', 'UF/IFAS Extension, Orange County')}). A separate account of the same UF research, citing Fort Lauderdale Research and Education Center faculty, put peak turf readings at roughly 174°F on the hottest days ({ext('https://www.theinvadingsea.com/2025/08/14/artificial-turf-lawns-heat-xeriscapes-florida-friendly-landscaping-hb-683-water-california/', 'The Invading Sea')}). The two figures differ because they're measured on different days and sites, but both point the same direction: turf in full Florida sun gets too hot for bare feet or paws for stretches of a summer afternoon.</p>"
            + (photo("turf-pavers-pool", "A bright green artificial turf lawn bordered by large concrete pavers next to a pool and a modern house.") or "")),
        sec("Why Turf Runs Hotter Than Grass",
            "<p>Living grass cools itself through transpiration, the same process that keeps a tree canopy noticeably cooler than open pavement, releasing moisture that carries heat away as it evaporates. Synthetic fiber and infill have no such mechanism; they absorb solar radiation and hold it at the surface instead of shedding it. Darker fiber and darker infill both absorb more than lighter versions of the same product, which is why color matters on a turf lawn the same way it matters on a pool deck or a driveway.</p>"),
        sec("Does Rinsing Turf With Water Actually Cool It Down?",
            f"<p>Yes, but only for a short window. A university study out of Greece measured artificial turf surface temperatures dropping by as much as 30°C (about 54°F) right after irrigation, with that cooler reading holding for roughly 90 to 120 minutes before the surface climbed back toward its pre-irrigation temperature ({ext('https://wseas.com/journals/articles.php?id=9293', 'WSEAS Transactions on Environment and Development, 2024')}). That study wasn't run in Florida, but the mechanism, water evaporating off the surface and carrying heat with it, works the same way here. A quick hose-down before kids or pets use a turf area buys a real window of relief; it isn't a permanent fix, and Florida's own turf rule doesn't allow an in-ground sprinkler zone to do that job automatically.</p>"),
        sec("Ways to Make an Artificial Turf Area Cooler",
            f"<p>A few choices at installation, and a few habits afterward, make a real difference without changing the product entirely.</p>"
            + ul(["Site turf where afternoon shade reaches it, a tree canopy, a pergola or the house's own shadow, rather than in the most exposed, full-sun stretch of the yard. Any tree used for shade still has to sit outside the canopy's drip line under Florida's turf rule, unless a certified arborist signs off.",
                  "Choose a lighter fiber or infill color where the product line offers one; darker 'true green' shades read better in photos but run hotter underfoot.",
                  "Keep a hose handy for a quick rinse before midday use, knowing the cooling effect fades within one to two hours rather than lasting all afternoon.",
                  "Avoid running turf directly against a west-facing wall, fence or dark hardscape that radiates its own heat back onto the lawn in the late afternoon."])),
        sec("Is Artificial Turf Too Hot for Bare Feet or Pets?",
            f"<p>During the hottest stretch of a Florida afternoon, often yes, by UF/IFAS's own measurements above. Scheduling outdoor time for mornings or evenings, when surface temperatures drop well below their midday peak, matters more for comfort than any product choice. Pets add their own wrinkle since paw pads sit much closer to the surface than bare human feet do; {post('artificial-turf-for-dogs-florida', 'our guide to artificial turf for dogs')} covers paw safety, odor and drainage together.</p>"),
        sec("Does Turf Heat Change the Way We Design a Lawn?",
            f"<p>It changes where we put furniture, seating and play equipment more than it changes whether turf gets specified at all. A turf lawn that doubles as a side-yard dog run, a play area, or the surface right outside a lanai door gets planned with afternoon shade or a planting buffer in mind from the start, rather than treated as an afterthought once the panels are already down. A decorative accent strip between pavers, or a small putting green used mostly in the morning or evening, carries far less of a heat penalty than an open, full-sun lawn meant for midday use. {svc('artificial-turf')} covers how lawns, pet areas, putting greens and paver accents each get built; heat is one more variable that shapes the layout on top of drainage and the state's material rule.</p>"
            + table("Where turf heat matters most",
                    ["Use", "Typical sun exposure", "Heat planning that helps"],
                    [["Open front or back lawn", "Often full sun most of the day", "Shade structure, lighter color, or limit peak-hour use"],
                     ["Side-yard pet area", "Varies by lot; often narrower and partly shaded by fencing or the house", "Site along the shadier side of the yard where the layout allows it"],
                     ["Putting green", "Usually open for a clean sightline", "Plan for morning or evening play rather than midday"],
                     ["Paver accent strip", "Matches the surrounding paver field's exposure", "Smaller footprint limits how much hot surface is underfoot at once"]],
                    "General layout guidance, not a measured comparison between uses.")),
        sec("A Quick Example",
            f"<p>Say you're planning a turf side yard in a Kissimmee subdivision with full southern exposure and no mature trees yet. Without added shade, that lawn behaves like the UF measurements above through the hottest part of the day. Planning a pergola or fast-growing shade tree into the same project, and picking a lighter-toned product, does more for comfort than anything done after installation. {svc('artificial-turf')} and the {a('/artificial-turf-cost/', 'artificial turf cost guide')} cover what that planning looks like in practice.</p>"),
        sec("Related Reading",
            ul([svc("artificial-turf"), post("artificial-turf-for-dogs-florida", "artificial turf for dogs: odor, drainage and infill"),
                post("how-hot-do-pool-decks-get-florida", "the coolest pool deck surface, for comparison"),
                compare("artificial-turf-vs-sod", "artificial turf vs. sod in Florida")])),
    ])
    faqs = [
        faq("Can artificial turf burn bare feet in Florida?",
            f"At its peak, turf can reach temperatures hot enough to be uncomfortable or painful underfoot; UF/IFAS Extension in Orange County reports readings up to 160°F on the hottest summer days ({ext('https://blogs.ifas.ufl.edu/orangeco/2025/04/15/synthetic-turf-and-the-environment/', 'UF/IFAS Extension')}). Shade, timing outdoor use for mornings or evenings, and a quick rinse before bare feet touch it all help manage that risk."),
        faq("Does shade really lower turf temperature?",
            "Yes, consistently. Turf in full sun absorbs solar radiation directly; turf under a tree canopy, a pergola or even a building's own shadow for part of the day never reaches the same peak. It's one of the most reliable ways to cut turf heat, alongside choosing a lighter color."),
        faq("Is there a type of infill that stays cooler?",
            "Lighter-colored infill generally runs cooler than darker infill, the same reflectance principle that applies to any outdoor surface in direct sun. We don't have a verified, product-by-product comparison to point to beyond that general rule, so ask a specific manufacturer for its own testing data if heat is a priority."),
        faq("Does hosing turf down help for more than a few minutes?",
            f"Research on artificial turf cooling found the effect fades within about one to two hours after watering, not all afternoon ({ext('https://wseas.com/journals/articles.php?id=9293', 'WSEAS Transactions on Environment and Development, 2024')}). It's a useful tool right before use, not a substitute for shade or a lighter color."),
        faq("Is turf hotter in Orlando or on the coast in Sarasota?",
            "No verified comparison between the two metro areas exists. How hot a specific lawn gets depends far more on sun exposure, shade and color than on which Florida city it's in; a shaded turf area in either place runs cooler than an exposed one in the other."),
    ]
    return page("/blog/artificial-turf-heat-in-florida/", "post",
                "How Hot Does Artificial Turf Get in Florida?",
                "UF/IFAS Extension measured artificial turf up to 100°F hotter than grass in Florida, reaching 160°F on peak days. How to keep a turf lawn cooler, as of October 2026.",
                "How Hot Does Artificial Turf Get in Florida, and How Do You Keep It Cooler?",
                capsule("UF/IFAS Extension in Orange County measured synthetic turf running up to 100°F hotter than natural grass on peak summer days, with surface readings reaching as high as 160°F. Shade, a lighter color and timing outdoor use for mornings or evenings cut that heat more than anything applied after installation. A quick hose rinse helps for about an hour, as of October 2026."),
                body, faqs=faqs,
                sources=[("UF/IFAS Extension, Orange County: synthetic turf and the environment", "https://blogs.ifas.ufl.edu/orangeco/2025/04/15/synthetic-turf-and-the-environment/"),
                         ("The Invading Sea: UF/IFAS turf heat research", "https://www.theinvadingsea.com/2025/08/14/artificial-turf-lawns-heat-xeriscapes-florida-friendly-landscaping-hb-683-water-california/"),
                         ("WSEAS Transactions on Environment and Development, 2024: turf surface temperature and irrigation", "https://wseas.com/journals/articles.php?id=9293"),
                         "rule62-308-100-text"],
                related=[("/artificial-turf/", "artificial turf installation"), ("/blog/artificial-turf-for-dogs-florida/", "artificial turf for dogs"),
                         ("/artificial-turf-cost/", "artificial turf cost guide"), ("/compare/artificial-turf-vs-sod/", "artificial turf vs. sod"),
                         ("/blog/how-hot-do-pool-decks-get-florida/", "the coolest pool deck surface")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf", image="turf-pavers-pool", form=False)


def artificial_turf_for_dogs():
    body = "".join([
        sec("Does Artificial Turf Smell When Dogs Pee on It?",
            "<p>It can, but a properly built pet area is designed specifically to stop that from happening. The two things that cause lingering odor are a backing that doesn't let liquid pass through and a base underneath that holds moisture instead of draining it away. Get both right and routine rinsing keeps odor from building up; get either wrong and no amount of cleaning fully fixes it afterward.</p>"
            f"<p>{svc('artificial-turf')} covers lawns, putting greens and paver accents alongside pet areas, but a dog run or pet zone is built differently from the rest: a more open-backed turf, a steeper drainage slope, and infill chosen for how it handles liquid rather than just how it looks.</p>"),
        sec("What Makes Pet Turf Different From Lawn Turf",
            f"<p>A standard lawn panel is backed to hold its shape and drain rainwater; a pet-area product is backed to let far more liquid through, far faster, since urine volume concentrates in a small footprint rather than spreading across an open yard. Florida's 2026 turf standard, DEP Rule 62-308.100, limits infill statewide to clean silica sand, rock, shell or coated silica sand, with rubber infill allowed only inside a playground's equipment footprint ({src('rule62-308-100-text', 'Rule 62-308.100')}). That rule applies the same way to a dog run as it does to a front lawn; there's no separate pet-turf exception in the state standard.</p>"),
        sec("Backing and Base: Where Odor Problems Actually Start",
            f"<p>A turf backing with few or no drainage perforations holds liquid against the base instead of letting it through, and that trapped moisture is what turns into ammonia odor over time, not the turf fibers themselves. The base matters just as much: Florida's rule requires washed crushed rock or crushed concrete under any new turf, specifically because fines-heavy fill compacts and seals the way a sidewalk base is meant to, which is the opposite of what a pet area needs underneath it ({src('rule62-308-100-text', 'Rule 62-308.100')}). The same rule bars using an in-ground irrigation zone to water turf, so a pet area's odor control depends on drainage and rinsing by hose, not an automatic sprinkler doing the work.</p>"),
        sec("Routine Care That Actually Controls Odor",
            "<p>Build quality sets the ceiling; routine care determines whether a pet area actually stays under it.</p>"
            + ul(["Rinse the high-use spots with a hose on a regular schedule rather than waiting for a smell to show up; a few minutes a few times a week does more than one deep clean a month.",
                  "Pick up solid waste promptly, since it sits on the surface and breaks down slower than liquid drains away.",
                  f"Avoid a pressure washer on the turf itself; it can drive debris into the backing instead of out, and {post('how-to-clean-artificial-turf', 'our turf cleaning guide')} covers gentler methods that work better.",
                  "Plan a seasonal deeper clean with an enzyme-based turf cleaner where odor has built up in a heavily used spot, on top of routine rinsing rather than instead of it."])),
        sec("Picking the Right Infill for a Dog Run or Pet Area",
            "<p>Every option below meets Florida's current material rule; they differ mainly in how actively they manage odor.</p>"
            + table("Pet-area infill options under Florida's turf rule",
                    ["Infill type", "What it does", "Note"],
                    [["Clean silica sand", "Weighs the backing down and supports the fibers", "Baseline option; no active odor control"],
                     ["Coated or antimicrobial silica sand", "Same base function, with a coating marketed to resist bacterial odor buildup", "Costs more than plain sand; ask for the manufacturer's own testing data"],
                     ["Natural rock or crushed shell", "Alternative mineral infill allowed under the state rule", "Heavier and coarser than sand; less common for pet areas specifically"],
                     ["Zeolite-type mineral infill", "A porous mineral marketed to adsorb ammonia odor from urine", "A coated-sand category under the rule; performance claims vary by brand"]],
                    f"{src('rule62-308-100-text', 'Rule 62-308.100')} sets the allowed material categories; it doesn't rank them by odor performance.")),
        sec("How Big Should a Dog Run Be, and Does It Need Its Own Drainage?",
            "<p>A dedicated run for one or two dogs typically needs less square footage than homeowners expect, often a fenced strip along a side yard rather than the whole backyard, which also keeps the rest of the lawn in regular turf or sod. We build pet areas with a steeper base slope than an open lawn panel gets, moving liquid toward a drain point rather than letting it sit anywhere in the footprint. On a larger run serving more than two dogs, tying that slope into a subsurface drain line, rather than relying on sheet drainage across the base alone, keeps the system from being overwhelmed during the rainy season.</p>"),
        sec("A Quick Example",
            "<p>Say you have two medium dogs and want to fence a 10-by-20-foot side yard in a Winter Garden subdivision for them. A pet-grade backing, a washed-rock base sloped toward one corner, and a coated sand infill, combined with rinsing that corner a few times a week, keeps the space usable without the smell building up the way an open-backed lawn panel used as a makeshift dog run often does.</p>"),
        sec("Related Reading",
            ul([svc("artificial-turf"), post("artificial-turf-heat-in-florida", "how hot artificial turf gets, and keeping it cooler"),
                post("how-to-clean-artificial-turf", "cleaning and maintaining artificial turf"),
                compare("artificial-turf-vs-sod", "artificial turf vs. sod in Florida")])),
    ])
    faqs = [
        faq("Can I use rubber infill for a dog run?",
            f"Not under Florida's current rule, outside a playground-equipment footprint. Rule 62-308.100 limits infill statewide to clean silica sand, rock, shell or coated silica sand ({src('rule62-308-100-text', 'Rule 62-308.100')}), which applies to a pet area the same way it applies to the rest of the yard."),
        faq("How often should I rinse artificial turf with pets?",
            "A few times a week for the spots dogs actually use, rather than the whole lawn on a fixed calendar, is the routine that keeps odor from building up. High-traffic corners near a gate or a favorite spot need it more than the rest of the area."),
        faq("Does a dog run need its own drainage system?",
            "For one or two dogs, a properly sloped washed-rock base usually handles it without anything extra. A run serving more dogs, or a smaller footprint with heavy use, benefits from a subsurface drain tied into the rest of the yard's drainage rather than relying on the base alone."),
        faq("Will artificial turf hurt a dog's paws in summer?",
            f"It can; turf surface temperatures run well above natural grass on hot days, and a dog's paw pads sit closer to the surface than a person's bare feet do. {post('artificial-turf-heat-in-florida', 'Our turf heat guide')} covers how hot it gets and what actually cools it down."),
        faq("Can turf be installed right up to a privacy fence for a dog run?",
            "Usually yes, as long as the layout still meets Florida's turf rule, including staying clear of any waterbody setback and any tree's drip line unless a certified arborist signs off. A fence line itself doesn't trigger a separate restriction under the state standard."),
    ]
    return page("/blog/artificial-turf-for-dogs-florida/", "post",
                "Artificial Turf for Dogs in Florida: Odor and Drainage",
                "A pet-grade backing, washed-rock base and the right infill control odor on artificial turf for dogs in Florida. What to ask for, as of October 2026.",
                "Artificial Turf for Dogs in Florida: Odor, Drainage and Infill",
                capsule("Artificial turf controls pet odor when the backing drains liquid through instead of trapping it and the base underneath is open, washed rock rather than fines that seal up. Florida's 2026 turf rule limits infill statewide to sand, rock, shell or coated silica sand, the same list for a dog run as for a front lawn. Routine rinsing, not an automatic sprinkler, does the rest, as of October 2026."),
                body, faqs=faqs,
                sources=["rule62-308-100-text", "fs125-572",
                         ("Turf Network, fully permeable turf backing", "https://turfnetwork.org/artificial-grass/features/drainage/fully-permeable/"),
                         ("IDA, zeolite uses in turf infill", "https://ida-ore.com/uses-for-zeolite/turf-infill/")],
                related=[("/artificial-turf/", "artificial turf installation"), ("/blog/artificial-turf-heat-in-florida/", "how hot artificial turf gets"),
                         ("/blog/how-to-clean-artificial-turf/", "cleaning and maintaining artificial turf"), ("/artificial-turf-cost/", "artificial turf cost guide"),
                         ("/compare/artificial-turf-vs-sod/", "artificial turf vs. sod")],
                crumbs=[("Blog", "/blog/")], published="2026-10-01", service="artificial-turf", image=None, form=False)


def get_pages():
    return [how_hot_do_pool_decks_get(), slippery_pool_deck_fixes(), saltwater_pools_and_coastal_salt_air(),
            sinkholes_and_settlement(), artificial_turf_heat(), artificial_turf_for_dogs()]
