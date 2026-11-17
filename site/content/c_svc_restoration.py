# -*- coding: utf-8 -*-
"""Service page: paver restoration (cleaning, stripping, releveling, replacing, re-sanding)."""
from _helpers import (page, capsule, sec, table, faq, ul, steps, note, cta, a, svc, city, cs, post, compare, src, ext,
                       price, per, price_note, tel, contact, photo, offer)
from _photos import for_service

CRUMBS = [("Pavers", "/pavers/")]


def restoration():
    K = "paver-restoration"
    pids = for_service(K, 4)
    body = "".join([
        sec("What is paver restoration?",
            "<p>Restoration means bringing an existing paver surface back to how it was meant to perform and look, without tearing it out. In practice it's a short list of "
            "jobs chosen after a walk-through: deep cleaning, removing a failed sealer, pulling and resetting sunken or rocking units, swapping out broken ones, refilling the joints, and "
            f"(only if you want it) a fresh coat of sealer at the end. A new coat on its own is covered on the {svc('paver-sealing', 'paver sealing')} page. This page is for what has to be "
            "dealt with before any coating goes down.</p>"
            "<p>The sequence matters more than any single step. Anything that involves lifting pavers happens first, because it disturbs the sand and dirties the surface. "
            "Washing follows, then the joints, and any sealer comes last. Done in a different order, you'd be washing twice or sealing over loose joints.</p>"
            + (photo(pids[0], "A paver driveway in a herringbone pattern, the kind of surface restoration is meant to keep in service.") if pids else "")),
        sec("How do you diagnose what's wrong with a paver surface?",
            "<p>Start with the base, because that's where most movement comes from. We walk the full surface, press on low spots, tap for rocking, and look along the edges for pavers that have "
            "crept out of line. Edge restraint is one of the first things to check: the industry's edge-restraint bulletin calls for restraint along the whole perimeter and wherever the material changes, "
            f"fastened into the aggregate base and not the soil, and it says garden-bed edging isn't an acceptable restraint ({src('icpi-ts3', 'ICPI Tech Spec 3')}).</p>"
            "<p>What we're sorting is cosmetic from structural. Stains, algae and faded color are cosmetic. A surface that dips more than the construction tolerance of 3/8 inch over 10 feet, "
            f"or pavers that rock when you step on them, point to the base or bedding ({src('icpi-ts2', 'ICPI Tech Spec 2')}). Roots are a third cause, and the causes behind sinking are in "
            f"{post('why-pavers-sink-in-florida', 'why pavers sink in Florida')}.</p>"),
        sec("Symptom, likely cause and restoration step",
            table("Common paver problems and what restoration does about them", ["What you see", "Likely cause", "Restoration step"],
                  [["Dip or low spot in the field", "Bedding or base settled, often after water moved fines out", "Pull the units, fix the base and bedding, reset and compact"],
                   ["Paver rocks underfoot", "Void under the unit, or bedding sand washed away", "Lift, refill and screed the bedding, reset flush"],
                   ["Raised or heaved section near a tree", "Root pushing the base up", "Lift, cut the root only if an arborist agrees, rebuild the base, reset"],
                   ["Edge pavers drifting or gapped", "Edge restraint missing, loose or never anchored", "Reset the edge units and install restraint spiked into the base"],
                   ["Joints empty or sand lower than the chamfer", "Washout from downspouts, wind, pressure washing", "Refill and compact sand, or use a binder"],
                   ["Black or green film", "Algae and mold in damp, shaded spots", "Wash with a wide spray, treat, then consider a sealer"],
                   ["Orange or brown streaks", "Sprinkler water with iron", "Rust-specific remover, then fix the sprinkler spray"],
                   ["White cloud on a sealed surface", "Moisture trapped under the coat", "Strip or re-dissolve the coat under dry conditions"],
                   ["Cracked, chipped or stained units", "Impact, loads, stains that won't lift", "Replace individual units"]],
                  "Causes are the usual ones; a visit confirms which applies. The structural rows need the base looked at, not just the surface."),
            "decision"),
        sec("Deep cleaning: surface cleaner, wand angle and stains",
            "<p>Professionals typically use a pressure washer, and the paver industry bulletin puts the range at 1,000 to 4,000 psi and 2 to 6 gallons per minute, with a wide nozzle at a low angle "
            f"to avoid pulling sand out of the joints ({src('icpi-ts5', 'ICPI Tech Spec 5')}). That's why a rotary surface cleaner on a big driveway and an angled fan wand near the edges and joints usually "
            "make sense. The same bulletin adds that a lot of rinse water matters more than high pressure.</p>"
            "<p>Stains come out first, and each kind has its own treatment: oil needs an absorbent and, often, repeated applications; tire marks respond to scrubbing with detergent; leaf and wood-rot "
            "stains respond to household bleach and a stiff brush. Acidic cleaners lighten or change paver color and can hurt grass, so a test patch comes first. Steel-bristle brushes are out because "
            "stray bristles rust and leave their own marks. For the Florida-specific ones, see "
            f"{post('mold-and-algae-on-pavers-florida', 'black mold and algae on pavers')}, {post('rust-and-irrigation-stains-on-concrete-pavers', 'rust and irrigation stains')} and "
            f"{post('oil-and-tire-stains-on-driveways', 'oil and tire stains on driveways')}. A DIY approach is in {post('how-to-clean-pavers-without-damage', 'cleaning pavers without damage')}.</p>"
            + (photo(pids[2], "Pressure washing a paver patio is the first visible step after any lifting and resetting.") if len(pids) > 2 else "")),
        sec("Stripping old sealer that has hazed or peeled",
            "<p>Whether a failed coat has to come off depends on what it is. Acrylic sealers can be cleaned and resealed when soiled or worn, without extremely hazardous materials. Urethane is "
            "different: it can't be refreshed by recoating, and if it has to be removed, the bulletin says methylene chloride or sandblasting is often needed. Methylene chloride is hazardous and must not "
            "go down a storm drain or soak into the soil, which is why removal is a job for professionals.</p>"
            "<p>A coat that went cloudy is a related case. The bulletin says that when sealer turns cloudy because of damp joints, poor drainage or heavy application, it has to be removed or "
            f"re-dissolved, and the supplier should advise on how. Sorting out the cause is in {post('paver-sealer-turned-white-or-cloudy', 'why paver sealer turns white or cloudy')}. "
            "We don't strip until we know the product underneath, because the wrong remover can etch the paver.</p>"),
        sec("Releveling sunken, rocking or heaved pavers",
            "<p>Releveling treats the cause, not the symptom. The affected pavers come out and are stacked in order, the bad bedding comes out, and the base gets checked. A soft base is dug out and "
            "rebuilt in compacted lifts. Then the bedding sand, which the industry spec sets at about 1 inch uncompacted, is screeded, the units go back flush, and joint sand is compacted in.</p>"
            + steps([("Mark and lift.", "Mark the affected area, lift the units and stack them in order so the pattern lines up on the way back."),
                     ("Find the reason.", "Probe for a void, a wet spot, a root or a washout path before anything else goes back."),
                     ("Rebuild the base where needed.", "Soft or contaminated aggregate is removed and replaced and compacted in lifts."),
                     ("Screed new bedding.", "About 1 inch of sand, screeded flat and left uncompacted under the pavers."),
                     ("Reset and compact.", "Units go back in pattern, are plate-compacted, and checked against a straightedge."),
                     ("Fix the edge.", "Restraint is added or re-anchored where it's missing, so the area doesn't walk out again.")])
            + f"<p>A fix that ignores the reason is temporary. Orlando's inland flatwoods and Sarasota's high water tables both move water under pavers, which is why drainage gets the same attention as sand. "
              f"Soil background: {src('nrcs-myakka-osd', 'NRCS Myakka series')}.</p>"),
        sec("Replacing broken or discolored pavers, and the color-match caveat",
            "<p>Individual units can be lifted and swapped without disturbing neighbors, which is a real advantage over a poured slab. The paver industry bulletin recommends replacing cracked or "
            "broken units, and notes that badly stained ones can be replaced but cleaning is usually easier and cheaper. The catch is color. A new unit can differ from weathered neighbors; the bulletin says "
            f"that difference should eventually disappear, and that proprietary color-improving cleaners can minimize it ({src('icpi-ts5', 'Tech Spec 5')}). We'd rather tell you before the work "
            "than after: a match to an older paver line may not exist, so salvage units from a hidden corner can go to the visible spot while new ones go to the hidden one.</p>"),
        sec("Re-sanding the joints",
            "<p>Once the units are level and the surface is clean and dry, the joints get swept full again and compacted. Industry spec limits joints to 1/8 inch, and plain dry sand is the baseline. "
            "A binder gives you more resistance to washout where water is concentrated, such as under a downspout or at the eave line. Neither is a structural material; the bulletin is clear that stabilizers "
            f"add no load capacity. The trade-offs are laid out in {compare('polymeric-sand-vs-joint-sand', 'polymeric sand vs. regular joint sand')}. Pests are a related subject, and "
            f"{post('ants-and-weeds-in-paver-joints', 'ants and weeds in paver joints')} explains why they move in when the sand drops.</p>"),
        sec("Sealing at the end, if you want it",
            f"<p>Sealing is the optional last step, and it's best on a surface that's level, clean, dry and full of sand. Types, finish and timing are on the {svc('paver-sealing', 'paver sealing')} page.</p>"),
        sec("What does paver restoration cost?",
            f"<p>Paver repair and releveling is priced by scope, not by the whole patio. Market data puts it at {price('paver-restoration')} {per('paver-restoration')}, with {price('paver-restoration', True)} "
            f"as the typical band ({src('homeguide-driveway-repair', 'HomeGuide')}; {src('outdoorlifepros-paver-repair-capecoral', 'Outdoor Life Pros, Cape Coral')}). For comparison, the cleaning, "
            f"re-sanding and sealing package runs {price('paver-sealing')} per {per('paver-sealing')} across the whole surface, because it doesn't involve lifting anything. A small repair "
            "can cost less than that on a total-dollar basis, while a big rebuild costs more.</p>"
            + table("Where the money goes", ["Line item", "What drives it"],
                    [["Releveling", "Area lifted, how deep the base problem goes, access for a compactor"],
                     ["Replacement units", "Matching availability, how many units, hauling away debris"],
                     ["Deep cleaning and stain treatment", "Surface size, stain type, repeat applications"],
                     ["Sealer stripping", "Product underneath, area, hazardous material handling"],
                     ["Re-sanding", "Joint width and sand type"]],
                    f"Market ranges as of October 2026, not a quote. See the {a('/paver-sealing-cost/', 'paver sealing cost guide')} for the line-by-line detail.")),
        sec("When restoration isn't enough",
            "<p>Sometimes the surface has failed across most of its area: a base that was never built to spec, widespread settlement, or pavers so worn there's nothing to save. At that point resetting "
            f"a patch after patch costs more than starting over. {post('restore-or-replace-old-pavers', 'Restore or replace old pavers')} walks through how to tell, and "
            f"{svc('paver-driveways', 'a new paver driveway')} or {svc('paver-patios', 'patio')} is the other path.</p>"),
        sec("Permits for cleaning, releveling and rebuilds",
            "<p>Washing, sanding and resetting a few units isn't treated as permitted work in the jurisdictions we serve, since nothing new is being built and the right-of-way isn't touched. "
            "Pulling up and rebuilding most of a driveway's base is closer to new construction, and the city or county can ask for the same review. If you're changing the footprint, "
            f"{post('driveway-widening-and-extensions-florida', 'widening or rebuilding a driveway')} explains the line. Over $2,500, a Notice of Commencement is required under "
            f"{src('fs713-13', 'F.S. 713.13')}.</p>"),
        sec("How do you pick a paver restoration company?",
            "<p>Restoration is judgment-heavy, so the questions are about process rather than price. Ask about these.</p>"
            + ul(["A walk-through that includes pressing on low spots and checking the edge, not just a look at the surface.",
                  "A written scope listing each step in order: lift and reset, then wash, then sand, then optional sealer.",
                  "What they'll do about the cause of a sunken area, not just reset the units.",
                  "What the existing sealer is, and how it will be removed.",
                  "A certificate of insurance sent straight from the agent, plus a Sunbiz lookup for the company name on the contract.",
                  "Whether replacement units will be matched or sourced from salvage, and what happens if they don't match.",
                  "A payment schedule tied to finished steps."])),
        sec("Where we restore pavers",
            f"<p>The {a('/central-florida/', 'Kissimmee & Greater Orlando crew')} works at {tel('orlando')} and the {a('/sarasota-manatee/', 'Sarasota crew')} at {tel('sarasota')}. "
            f"Local pages: {cs('kissimmee', K, 'paver restoration in Kissimmee')}, {cs('orlando', K, 'paver restoration in Orlando')}, "
            f"{cs('sarasota', K, 'paver restoration in Sarasota')} and {cs('lakewood-ranch', K, 'paver restoration in Lakewood Ranch')}.</p><!--AUTO:service-cities-->"),
    ])
    faqs = [faq("Can sunken pavers be releveled without buying new ones?",
                "Usually yes. The same units are lifted, the bedding or base is corrected, and they go back flush. New units are only needed for any that crack or chip on the way out. The important part is finding why the area sank, since resetting pavers over the same wet spot or void puts you back where you started."),
            faq("Can you replace just a few cracked or stained pavers?",
                "Yes, units come out individually. The question is color: new pavers can look different next to weathered neighbors, and the paver industry says the difference should fade, though color-improving cleaners can help it along. If the original line has been discontinued, no exact match may exist."),
            faq("Do I have to strip old sealer before resealing?",
                "Not always. Industry guidance says acrylic can be cleaned and resealed when worn. A cloudy coat or a urethane needs a different approach, since urethane can't be refreshed by recoating and its removal often involves hazardous chemicals or sandblasting. Knowing the product on the surface is step one."),
            faq("Can I pressure wash my own pavers?",
                "On a small patio or walk, yes, with a wide fan nozzle at a low angle so the sand stays in the joints, and no steel brushes. On a large driveway or when stains need cleaners, equipment and chemistry matter more, and refilling washed-out joints becomes part of the job."),
            faq("Why do black spots keep coming back on my pavers?",
                "Algae and mold return wherever shade, irrigation overspray or poor drainage keep the surface damp. Removing them is the easy part; changing the damp conditions is what slows them down. See the post on mold and algae on Florida pavers for treatment options."),
            faq("What are the orange stains on my pavers from?",
                "Usually iron in well or irrigation water that gets sprayed on the surface. A rust-specific remover treats the mark, and redirecting the sprinkler heads keeps it from returning. Regular acid cleaners may change the paver color, so a test patch comes first."),
            faq("Is it worth restoring pavers that are decades old?",
                "If the units are sound and the problem is the base, joints or surface, usually yes, since lifting and resetting costs less than replacement. If settlement or damage covers most of the area, a new installation can make more sense. The restore-or-replace post goes through the checks.")]
    return page("/paver-restoration/", "service", "Paver Restoration in Kissimmee, Orlando & Sarasota, FL",
                "Paver restoration: releveling sunken pavers, deep cleaning, sealer stripping and re-sanding. Repair market range $3-$12/sq ft as of October 2026.",
                "Paver Restoration: Diagnose, Relevel, Clean and Re-Sand in Florida",
                capsule("Paver restoration repairs an existing surface instead of replacing it: releveling sunken pavers, replacing broken ones, deep cleaning, removing failed sealer and "
                        "re-sanding joints. As of October 2026, repair and releveling run $3–$12 per square foot of area worked. We restore pavers in "
                        "Kissimmee, Orlando, Sarasota and Lakewood Ranch."),
                body, faqs=faqs,
                sources=["icpi-ts2", "icpi-ts3", "icpi-ts5", "homeguide-driveway-repair", "outdoorlifepros-paver-repair-capecoral", "homeguide-seal-pavers", "nrcs-myakka-osd", "fs713-13"],
                related=[("/faq/pavers/", "paver questions, answered"), ("/paver-sealing/", "paver sealing: sealer types and timing"), ("/paver-sealing-cost/", "paver sealing and restoration cost guide"),
                         ("/blog/why-pavers-sink-in-florida/", "why pavers sink in Florida"), ("/blog/restore-or-replace-old-pavers/", "restore or replace old pavers"),
                         ("/blog/mold-and-algae-on-pavers-florida/", "black mold and algae on pavers"),
                         ("/blog/rust-and-irrigation-stains-on-concrete-pavers/", "rust and irrigation stains"),
                         ("/blog/oil-and-tire-stains-on-driveways/", "oil and tire stains"),
                         ("/central-florida/", "the Kissimmee & Greater Orlando crew"), ("/sarasota-manatee/", "the Sarasota crew")],
                crumbs=CRUMBS, crumb="Paver restoration", service=K,
                hero_photo=pids[0] if pids else None, offer=offer("paver-restoration"), eyebrow="Pavers · Kissimmee, Orlando & Sarasota",
                howto=("How a paver surface is restored", [("Inspect the surface and edges", "Walk the field, press on low spots, tap for rocking and check the edge restraint."),
                                                          ("Lift and reset failed areas", "Pull sunken units, correct the base and bedding sand, and reset them flush."),
                                                          ("Replace broken units", "Swap cracked or badly stained pavers and plan for color difference."),
                                                          ("Deep clean the surface", "Treat stains first, then wash with a wide spray at a low angle."),
                                                          ("Remove failed sealer if needed", "Identify the product and strip or re-dissolve only what has failed."),
                                                          ("Re-sand the joints", "Sweep, compact and top off the joint sand."),
                                                          ("Seal if you want it", "Coat the dry, clean, full-jointed surface.")]))


def get_pages():
    return [restoration()]
