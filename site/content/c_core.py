# -*- coding: utf-8 -*-
"""About, contact, process, legal, thank-you, 404 and the index pages (blog, compare, service areas)."""
from _data import PUBLIC_NAME, UNITS, UNIT_ORDER, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, EMAIL, REVIEWED
from _helpers import page, capsule, sec, table, faq, ul, steps, note, a, svc, city, post, compare, src, ext, price, per, contact, tel
from _posts import COMPARES, POSTS

ABOUT = page(
    "/about/", "about", "About Opera Concrete & Pavers | Orlando & Sarasota",
    "Who we are, how we build concrete, pavers and turf in Florida, and the two service units that cover Greater Orlando and Sarasota–Manatee.",
    "About Opera Concrete & Pavers",
    capsule("Opera Concrete & Pavers is a Florida hardscape contractor with two service units: one for Greater Orlando and one for Sarasota, Lakewood Ranch and Bradenton. We pour concrete driveways, patios and pool decks, lay pavers and travertine, build segmental retaining walls and install artificial turf, and every price we give follows a site visit."),
    "".join([
        sec("What the name stands for", "<p>The logo carries three words under the name: driveways, patios, lifestyles. The first two are the work. The third is the reason people call: a driveway that doesn't crack across the middle, a back patio wide enough for the table, a pool deck you can cross barefoot in July, a yard the dog can use after a storm.</p>"
            f"<p>We keep the scope deliberately narrow. Flatwork and hardscape only: {svc('concrete-driveways', 'concrete driveways')}, {svc('paver-patios', 'paver patios and walkways')}, {svc('concrete-pool-decks', 'pool decks')}, {svc('retaining-walls', 'retaining walls')} and {svc('artificial-turf', 'turf')}. No roofing, no remodeling, no pools. Doing one trade family well is the whole plan.</p>"),
        sec("Two units, one standard", "<p>Florida isn't one market. A driveway in Clermont sits on deep ridge sand that drains in minutes; one in Bradenton may sit on flatwoods soil with the water table a foot down for half the year, a few miles from salt water. Permit desks differ too, from Orlando's engineering permit for any driveway or paver work to Manatee County's right-of-way rules.</p>"
            f"<p>So the business runs as two units, each quoting and building in its own counties: the {a('/central-florida/', 'Orlando and Central Florida unit')} and the {a('/sarasota-manatee/', 'Sarasota, Lakewood Ranch and Bradenton unit')}. The methods are the same in both: compacted base in lifts, joints planned before the pour, curing that accounts for Florida heat, and a written scope you can compare line by line.</p>"),
        sec("How we write about prices and rules", f"<p>The prices on this site are market ranges from published cost data, labeled with the month they were checked, never a promise of what your project costs. Rules come from the statute, the county code or the city's own permit page, linked where we cite them. When a city doesn't publish a rule, we say so rather than guess. You can read the method behind each estimate on the {a('/process/', 'project process page')}.</p>"),
        sec("Get in touch", f"<p>The fastest way to reach the right crew is the estimate form: choose your area and describe the project. You can also start from the {a('/contact/', 'contact page')} or browse the {a('/service-areas/', 'service areas')} to see which towns each unit covers.</p>"),
    ]), wide=False, crumb="About", form=False)

CONTACT = page(
    "/contact/", "contact", "Contact Opera Concrete & Pavers | Free Estimates",
    "Request a free on-site estimate for concrete, pavers, pool decks or artificial turf in Greater Orlando or Sarasota–Manatee. Choose your area and we'll call.",
    "Request a free estimate",
    capsule("Send the form with your area, the service and a few details about the project, and the crew that covers your county will call to set up a free site visit. We work in Greater Orlando (Orange, Osceola, Seminole, Lake and northeast Polk) and in Sarasota and Manatee counties."),
    "".join([
        sec("What to include", ul(["The address or ZIP code, so the right unit gets it",
                                   "What's there now (grass, old concrete, pavers, nothing) and roughly how big the area is",
                                   "Whether an HOA or architectural review committee has to approve the work",
                                   "Any timing you're working around: a closing, a pool build, guests"])
            + "<p>Photos help but aren't required; the site visit is where we measure.</p>"),
        sec("Which crew covers you", f"<p>The {a('/central-florida/', 'Orlando unit')} covers Orlando, {city('kissimmee')}, {city('clermont')}, {city('oviedo')}, {city('winter-garden')}, {city('windermere')} and the rest of Central Florida. The {a('/sarasota-manatee/', 'Sarasota unit')} covers {city('sarasota')}, {city('lakewood-ranch')}, {city('bradenton')}, {city('venice')} and the Suncoast. Not sure? Pick the closest area and include your ZIP code.</p>"),
    ]), unit=None, form=True, form2=False, crumb="Contact", kind_override=None)
CONTACT["kind"] = "contact"

PROCESS = page(
    "/process/", "page", "How a Concrete or Paver Project Works | Opera",
    "From site visit to walkthrough: how we measure, scope, permit, demolish, build the base, pour or lay, cure and hand over a Florida hardscape project.",
    "How a project runs, from site visit to walkthrough",
    capsule("A concrete, paver or turf project with Opera runs in six steps: site visit, written scope, approvals, demolition and base, the pour or the lay, and a walkthrough. Most of the quality is decided in step four, the base, which is why we put its depth and compaction in writing."),
    "".join([
        sec("1. Site visit and measure", "<p>We measure the area, note the existing surface and what's under it where we can see it, check the slope and where storm water runs, mark trees whose roots matter, and look at access for equipment and a concrete truck. In master-planned communities we ask for the architectural guidelines, because they often decide the material and color before you do.</p>"),
        sec("2. Written scope and price", "<p>The estimate lists area, demolition, base material and depth, concrete thickness and strength or paver type and pattern, joints, finish, sealer, permits and cleanup. If two bids don't list the same items, they aren't the same job. "
            f"The post on {post('how-to-compare-concrete-and-paver-quotes', 'comparing quotes line by line')} shows what to look for.</p>"),
        sec("3. Approvals", f"<p>HOA or ARC approval and any city or county permit come before demolition. Driveway aprons in the public right-of-way nearly always need a right-of-way or engineering permit. Since July 1, 2026, small single-family jobs under $7,500 are exempt from building permits in Florida, but zoning, engineering and right-of-way permits still apply where the local government requires them. County details: {post('orange-county-orlando-driveway-patio-permits', 'Orange and Orlando')}, {post('sarasota-county-driveway-patio-permits', 'Sarasota County')}, {post('manatee-county-driveway-permits', 'Manatee County')}.</p>"),
        sec("4. Demolition and base", f"<p>Old concrete is cut and broken out, roots and organic soil are dug out, and the subgrade is compacted. Under pavers, the aggregate base goes in lifts and is compacted to the density the industry standard calls for ({src('icpi-ts2', 'ICPI Tech Spec 2')}). Under turf, the base is washed crushed rock or crushed concrete, as Florida's 2026 turf rule requires.</p>"),
        sec("5. Pour, lay or install", f"<p>Concrete is placed early in the day when it's hot, finished, jointed at the planned spacing and cured with a compound or wet cure. Pavers are laid on screeded bedding sand, cut, compacted and swept with joint sand. Turf is rolled out, seamed, nailed or edged and infilled. See {post('concrete-driveway-installation-process', 'how a concrete driveway is installed')} and {post('paver-installation-process-florida', 'how pavers are installed in Florida')}.</p>"),
        sec("6. Walkthrough and care", f"<p>We walk the finished work with you, confirm when you can drive or walk on it, and leave care instructions. For sealed surfaces we note when the sealer should be renewed based on wear, not a calendar; the paver industry's own guide sets no fixed interval ({src('icpi-ts5', 'ICPI Tech Spec 5')}).</p>"),
    ]), crumb="Our process", sources=["icpi-ts2", "icpi-ts5"],
    howto=("How a concrete or paver project is built", [("Site visit", "Measure, check slope, drainage, trees and access."), ("Written scope", "List base, thickness, joints, finish, permits."), ("Approvals", "HOA/ARC and city or county permits."), ("Demolition and base", "Remove old surface, compact subgrade and base in lifts."), ("Pour or lay", "Place and cure concrete, or lay and compact pavers, or install turf."), ("Walkthrough", "Confirm cure time and care.")]))


def _legal(route, title, h1, meta, paras):
    return page(route, "page", title, meta, h1, f"<p>Last updated {REVIEWED}.</p>", "".join(sec(h, p) for h, p in paras), crumb=h1, form=False)


PRIVACY = _legal("/privacy/", "Privacy Policy | Opera Concrete & Pavers", "Privacy policy",
                 "How Opera Concrete & Pavers collects, uses and protects the information you send through this website's estimate forms.",
                 [("What we collect", "<p>When you send an estimate request we receive what you type (name, phone, email, city or ZIP, service, project details), the page you sent it from and, if present, campaign parameters in the link you followed. We don't sell this information.</p>"),
                  ("How we use it", "<p>To contact you about your project, schedule a site visit, prepare an estimate and keep a record of the job. It is shared only with crew members and subcontractors who need it to do the work, and with service providers that host our forms and records.</p>"),
                  ("Calls and texts", "<p>By sending the form you agree that we may call, text or email you about your request. You can ask us to stop at any time and we will.</p>"),
                  ("Cookies and analytics", "<p>The site uses no advertising cookies. Basic, privacy-preserving traffic statistics may be collected by our hosting provider.</p>"),
                  ("Your choices", "<p>Ask us through the contact form to see, correct or delete the information we hold about you.</p>")])
TERMS = _legal("/terms/", "Terms of Use | Opera Concrete & Pavers", "Terms of use",
               "Terms for using the Opera Concrete & Pavers website: prices are market ranges, information is general, and estimates follow a site visit.",
               [("Information on this site", "<p>Articles, guides and price ranges are general information for Florida homeowners, checked on the date shown. They are not engineering, legal or financial advice and do not replace a site visit, a permit review or a written estimate.</p>"),
                ("Prices", "<p>Prices shown are market ranges compiled from published cost data. They are not offers. Your price is the one in a written estimate after we see the site.</p>"),
                ("Links", "<p>We link to government and industry sources for reference. We don't control those sites.</p>"),
                ("Contact", "<p>Questions about these terms can be sent through the contact form.</p>")])
ACCESS = _legal("/accessibility/", "Accessibility | Opera Concrete & Pavers", "Accessibility",
                "Our commitment to an accessible website: keyboard navigation, readable contrast, text alternatives, and how to tell us about a barrier.",
                [("Our approach", "<p>The site is built to WCAG 2.2 AA practices: keyboard navigation with a visible focus ring, a skip link, labeled form fields, text alternatives for images, readable contrast and layouts that work at 320 pixels wide and at 200% zoom.</p>"),
                 ("Tell us about a problem", "<p>If something on the site is hard to use, describe it in the contact form and we'll fix it or get you the information another way.</p>")])

THANKS = page("/thank-you/", "plain", "Thank You | Opera Concrete & Pavers", "Your estimate request reached Opera Concrete & Pavers. The crew for your area will call to set up a free site visit.",
              "Thank you, your request is in",
              "<p>The crew that covers your area will call to set up the site visit. If you'd like to add photos or details, reply to our message when it arrives.</p>",
              f"<p>While you wait: {a('/cost/', 'cost guides')} · {a('/blog/', 'homeowner guides')} · {a('/faq/', 'frequently asked questions')}</p>", noindex=True, form=False)
NOTFOUND = page("/404/", "plain", "Page Not Found | Opera Concrete & Pavers", "This page doesn't exist. Find concrete, paver and turf services, cost guides and service areas from the links below.",
                "That page isn't here",
                "<p>The address may have changed. These links cover most of the site:</p>",
                ul([a("/concrete/", "Concrete services"), a("/pavers/", "Paver services"), a("/artificial-turf/", "Artificial turf"), a("/cost/", "Cost guides"), a("/service-areas/", "Service areas"), a("/contact/", "Request an estimate")]), noindex=True, form=False)

BLOG = page("/blog/", "index", "Concrete, Paver & Turf Guides for Florida Homes | Opera",
            "Plain-language guides on Florida driveways, pavers, pool decks and artificial turf: cracks, sinking pavers, permits, HOAs, heat, rain and costs.",
            "Guides for Florida homeowners",
            "<p>Straight answers about concrete, pavers, pool decks and turf in Florida: why things crack or sink, what the permit desk wants, how heat and rain change the work, and how to compare bids.</p>",
            "<!--AUTO:blog-index-->", crumb="Blog", form=False, wide=True)
COMPARE = page("/compare/", "index", "Concrete vs. Pavers and Other Comparisons | Opera",
               "Side-by-side comparisons for Florida homes: pavers vs. concrete, stamped vs. pavers, travertine vs. pavers, Cool Deck, sealers, joint sand and turf vs. sod.",
               "Side-by-side comparisons",
               "<p>When two materials could both do the job, these pages put cost, lifespan, upkeep, heat and storm behavior side by side for Florida conditions.</p>",
               '<ul class="grid">' + "".join(f'<li class="card"><h3><a href="/compare/{s}/">{h}</a></h3></li>' for s, (h, m) in COMPARES.items()) + "</ul>",
               crumb="Comparisons", form=False, wide=True)
AREAS = page("/service-areas/", "index", "Service Areas: Greater Orlando & Sarasota–Manatee | Opera",
             "Every town Opera Concrete & Pavers serves, by county: Orange, Osceola, Seminole, Lake, Polk, Sarasota and Manatee, with local permit and HOA notes.",
             "Where we work",
             "<p>Two crews cover two regions. Each town below has a page with its permit office, soil, HOA notes and the services we offer there.</p>",
             f'<div class="units"><div class="unit"><h3><a href="/central-florida/">{UNITS["orlando"]["name"]}</a></h3><p>Orange, Osceola, Seminole, Lake and northeast Polk counties.</p></div><div class="unit"><h3><a href="/sarasota-manatee/">{UNITS["sarasota"]["name"]}</a></h3><p>Sarasota and Manatee counties.</p></div></div><!--AUTO:all-areas-->',
             crumb="Service areas", form=False, wide=True)


def get_pages():
    return [ABOUT, CONTACT, PROCESS, PRIVACY, TERMS, ACCESS, THANKS, NOTFOUND, BLOG, COMPARE, AREAS]
