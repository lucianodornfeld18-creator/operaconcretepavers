# -*- coding: utf-8 -*-
"""Process photos into site/static/img/photos and write site/_photos_registry.json.
Sources: images/stock (temporary, licence in images/stock/stock.json) and images/incoming (owner's job photos, later).
EXIF-transpose, strip metadata, WebP q66 at 480/800/1200/1600, 4:3 thumbs at 480/672/1024 (q60), and a 1200x630 OG JPEG.
Run from the project root: python brand/make_photos.py"""
import json
import pathlib

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "static" / "img" / "photos"
OUT.mkdir(parents=True, exist_ok=True)
WIDTHS = (480, 800, 1200, 1600)
THUMBS = (480, 672, 1024)
BRAND = "opera"

# id -> (source file, seo stem, focal (x,y), alt override or None, short name, services)
STOCK = {
    "home-hero": ("s18.jpg", "florida-homes-paver-driveways-palms", (0.5, 0.6), None, "Florida street with paver driveways and palms", ["paver-driveways"]),
    "concrete-driveway-modern": ("s01.jpg", "broom-finish-concrete-driveway-modern-home", (0.5, 0.6), None, "Broom-finish concrete driveway", ["concrete-driveways"]),
    "concrete-driveway-two-car": ("s02.jpg", "two-car-concrete-driveway-white-house", (0.5, 0.6), None, "Two-car concrete driveway", ["concrete-driveways", "concrete-slabs"]),
    "concrete-driveway-joints": ("s03.jpg", "concrete-driveway-control-joints-garage", (0.5, 0.55), None, "Concrete driveway with control joints", ["concrete-driveways", "concrete-repair"]),
    "stamped-flagstone": ("s04.jpg", "stamped-concrete-flagstone-pattern", (0.5, 0.5), None, "Stamped concrete in a flagstone pattern", ["stamped-concrete", "concrete-patios"]),
    "paver-patio-circle": ("s05.jpg", "circular-paver-patio-garden", (0.5, 0.55), None, "Circular paver patio", ["paver-patios", "retaining-walls"]),
    "covered-patio": ("s06.jpg", "covered-patio-outdoor-dining", (0.5, 0.55), None, "Covered patio with dining set", ["concrete-patios", "paver-patios"]),
    "paver-patio-firepit": ("s07.jpg", "paver-patio-stone-fire-pit", (0.5, 0.6), None, "Paver patio with a fire pit", ["paver-patios", "paver-sealing"]),
    "paver-driveway-herringbone": ("s08.jpg", "herringbone-paver-driveway-walkway", (0.5, 0.6), None, "Herringbone paver driveway", ["paver-driveways", "paver-sealing"]),
    "pool-deck-pavers": ("s09.jpg", "paver-pool-deck-palms-fire-pit", (0.5, 0.6), None, "Paver pool deck with palms", ["pool-deck-pavers"]),
    "concrete-pool-deck": ("s10.jpg", "concrete-pool-deck-modern-home", (0.5, 0.6), None, "Concrete pool deck and spa", ["concrete-pool-decks"]),
    "interlocking-pavers": ("s11.jpg", "interlocking-concrete-pavers-close-up", (0.5, 0.5), None, "Interlocking concrete pavers, close up", ["paver-driveways", "paver-sealing", "pool-deck-pavers"]),
    "finishing-concrete": ("s12.jpg", "finishing-fresh-concrete-slab", (0.5, 0.5), None, "Finishing a freshly poured slab", ["concrete-slabs", "concrete-repair", "concrete-walkways"]),
    "retaining-wall-crib": ("s13.jpg", "modular-concrete-retaining-wall-slope", (0.5, 0.5), None, "Modular concrete retaining wall on a slope", ["retaining-walls"]),
    "turf-pavers-pool": ("s14.jpg", "artificial-turf-concrete-pavers-pool", (0.5, 0.6), None, "Artificial turf between large pavers by a pool", ["artificial-turf", "pool-deck-pavers"]),
    "green-lawn-patio": ("s15.jpg", "green-lawn-covered-patio-home", (0.5, 0.6), None, "Green lawn beside a covered patio", ["artificial-turf", "concrete-patios"]),
    "stepping-stone-walkway": ("s16.jpg", "paver-stepping-stone-front-walkway", (0.5, 0.6), None, "Stepping-stone walkway to a front door", ["concrete-walkways", "paver-patios"]),
    "pressure-washing-pavers": ("s17.jpg", "pressure-washing-paver-patio", (0.5, 0.55), None, "Pressure-washing a paver patio", ["paver-sealing"]),
}


def resize_w(im, w):
    return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)


def main():
    meta = {x["file"]: x for x in json.loads((ROOT / "images" / "stock" / "stock.json").read_text(encoding="utf-8"))}
    for old in OUT.glob("*"):
        old.unlink()
    reg, total = {}, 0
    for pid, (fn, stem, focal, alt, name, services) in STOCK.items():
        im = ImageOps.exif_transpose(Image.open(ROOT / "images" / "stock" / fn)).convert("RGB")
        if im.width > 1600:
            im = resize_w(im, 1600)
        stem = f"{BRAND}-{stem}"
        widths = sorted({w for w in WIDTHS if w < im.width} | {im.width})
        for w in widths:
            out = OUT / f"{stem}-{w}.webp"
            (im if w == im.width else resize_w(im, w)).save(out, "WEBP", quality=66, method=6)
            total += out.stat().st_size
        for w in THUMBS:
            out = OUT / f"{stem}-t{w}.webp"
            ImageOps.fit(im, (w, round(w * 3 / 4)), Image.LANCZOS, centering=focal).save(out, "WEBP", quality=60, method=6)
            total += out.stat().st_size
        og = ImageOps.fit(im, (1200, 630), Image.LANCZOS, centering=focal)
        og.save(OUT / f"{stem}-og.jpg", "JPEG", quality=80, optimize=True, progressive=True)
        m = meta.get(fn, {})
        reg[pid] = {"stem": stem, "alt": alt or m.get("alt", name), "name": name, "services": services, "w": im.width, "h": im.height,
                    "widths": widths, "thumbs": list(THUMBS), "stock": True, "license": m.get("license"), "source_page": m.get("source_page"), "photographer": m.get("photographer")}
        print(f"{pid:<28} {im.width}x{im.height}")
    (ROOT / "site" / "_photos_registry.json").write_text(json.dumps(reg, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\n{len(reg)} photos, {total / 1024:.0f} KB")


if __name__ == "__main__":
    main()
