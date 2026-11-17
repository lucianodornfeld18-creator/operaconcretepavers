# Google Business Profile kit — Opera Concrete & Pavers (2 profiles)

Internal. Everything here matches the site, the portal and the business cards (2026-11-17). Copy it field by field.

## Rules for both profiles

- **Business name:** `Opera Concrete & Pavers`, exactly. No city, no "Paver Sealing", no extra words (Google suspends keyword-stuffed names).
- **Service-area business:** hide the address. The address used for verification must be real and must not be the address of any other Google profile you manage (Kissimmee Concrete, Sarasota Concrete, Lakewood Ranch Concrete, Ocoee, Windermere, Groveland). Same address = one of the profiles gets filtered or suspended.
- **Phone:** each profile has its own Twilio number below. Don't add the other unit's number or the forwarding cell.
- **Photos:** upload only real photos of your crews, equipment and jobs. Don't upload the website's stock photos.
- **Description:** no "licensed", no "contractor", no prices, no links, no phone numbers.
- **Categories:** Google's own labels; type them in the category field and pick what appears. Use a pavers-first primary so the profile does not compete with the owner's concrete-branded profiles in the same area. Suggested (confirm in the picker): primary `Paving contractor`; secondary `Concrete contractor`, `Pressure washing service`, `Landscaper`. These are Google's category names, not claims on the site; the site itself keeps zero "contractor"/"licen" wording.
- **Hours:** set the real hours you answer the phone. The site does not publish hours, so nothing to match.
- After verification, send the profile links so they go into `UNITS[...]["same_as"]` in `site/_data.py`.

## Profile 1 — Kissimmee

| Field | Value |
|---|---|
| Name | Opera Concrete & Pavers |
| Phone | (689) 354-0025 |
| Website | https://operaconcretepavers.com/central-florida/?utm_source=gbp&utm_medium=organic&utm_campaign=kissimmee |
| Appointment link | https://operaconcretepavers.com/contact/?utm_source=gbp&utm_medium=organic&utm_campaign=kissimmee |
| Base | Kissimmee, FL (address hidden) |
| Business card | brand/business-cards/card-kissimmee.pdf |

**Description (704 characters):**

> Opera Concrete & Pavers is a paver and concrete company based in Kissimmee, serving homeowners across Osceola, Orange, Seminole, Lake and northeast Polk counties. We install paver driveways, patios, walkways and pool decks in concrete pavers and travertine, and we bring older pavers back with cleaning, releveling, re-sanding and sealing. We also pour concrete driveways, patios and pool decks, build retaining walls and install artificial turf. Every estimate is free and done on site: we measure, check the base, drainage and any HOA requirements, then send a written scope and price. We work in Kissimmee, Orlando, St. Cloud, Celebration, Clermont, Windermere, Winter Garden, Oviedo and nearby towns.

**Service areas (20):** Kissimmee, St. Cloud, Celebration, Poinciana, Hunters Creek, Orlando, Lake Nona, Dr. Phillips, Windermere, Winter Garden, Horizon West, Clermont, Ocoee, Winter Park, Oviedo, Davenport, ChampionsGate, Lake Mary, Sanford, Apopka

## Profile 2 — Sarasota

| Field | Value |
|---|---|
| Name | Opera Concrete & Pavers |
| Phone | (941) 207-7585 |
| Website | https://operaconcretepavers.com/sarasota-manatee/?utm_source=gbp&utm_medium=organic&utm_campaign=sarasota |
| Appointment link | https://operaconcretepavers.com/contact/?utm_source=gbp&utm_medium=organic&utm_campaign=sarasota |
| Base | Sarasota, FL (address hidden) |
| Business card | brand/business-cards/card-sarasota.pdf |

**Description (704 characters):**

> Opera Concrete & Pavers is a paver and concrete company based in Sarasota, serving homeowners in Sarasota and Manatee counties. We install paver driveways, patios and pool decks in concrete pavers, travertine and shell stone, and we restore existing pavers: cleaning, releveling sunken areas, replacing broken pavers, re-sanding joints and sealing, with the sealer chosen for salt air near the coast. We also pour concrete driveways, patios and pool decks, build retaining walls and install artificial turf. Estimates are free and done on site, followed by a written scope and price. We work in Sarasota, Lakewood Ranch, Bradenton, Venice, Siesta Key, Longboat Key, Osprey, Nokomis, Parrish and Palmetto.

**Service areas (16):** Sarasota, Lakewood Ranch, Bradenton, Venice, Siesta Key, Longboat Key, Osprey, Nokomis, North Port, Parrish, Palmetto, Ellenton, Anna Maria, Englewood, South Venice, Myakka City

## Services (same list on both profiles, pavers first)

| Service | Short description (Google allows up to 300 characters) |
|---|---|
| Paver driveway installation | Driveways in vehicle-rated pavers over a compacted aggregate base, with edge restraint that keeps the field from spreading. |
| Paver patios & walkways | Patios, walkways, fire-pit areas and lanai extensions in concrete pavers or travertine. |
| Pool deck pavers | Pool decks in travertine, shell stone and concrete pavers, including overlays on an old deck. |
| Paver sealing | Wet-look or natural sealer, water- or solvent-based, applied to a clean, dry, re-sanded paver surface. |
| Paver restoration | Deep cleaning, stripping failed sealer, releveling sunken areas, swapping broken pavers and re-sanding joints. |
| Concrete driveways | New, widened and replacement driveways poured to a thickness and joint plan that fits Florida soil. |
| Concrete patios | Back patios, lanai extensions and outdoor-kitchen pads, broom, stamped or decorative. |
| Concrete pool decks | Pool decks with cooler textures, slope to the drains and expansion joints at the coping. |
| Stamped concrete | Slate, ashlar, wood-plank and cobble patterns with integral color, release and sealer. |
| Concrete repair & resurfacing | Crack repair, resurfacing overlays, slab leveling, and tear-out and replace when repair won't hold. |
| Retaining walls | Segmental block walls, raised planters and seat walls, with drainage behind the wall. |
| Artificial turf | Lawns, pet areas, putting greens and turf between pavers, built on a washed-rock base. |

## After both profiles are live

1. Bing Places: import from Google (same name, phone, website per unit).
2. Apple Business Connect: one location per unit, same data.
3. Ask every finished client for a review that names the service and the town ("paver sealing in Lakewood Ranch").
4. Post monthly on each profile with a real job photo; link the matching page (/paver-sealing/, /paver-restoration/ or the city page).
