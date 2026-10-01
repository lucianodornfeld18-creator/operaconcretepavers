# -*- coding: utf-8 -*-
"""Logo assets from the owner's logo (brand/opera-logo-source.png): python brand/make_logo.py
Outputs to site/static/img: logo-header.webp/png (transparent, dark ink), logo-light.webp/png (white ink for dark
backgrounds), the triangle mark as icon/favicons, and og.jpg."""
import pathlib
from collections import Counter

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "brand" / "opera-logo-source.png"
OUT = ROOT / "site" / "static" / "img"
OUT.mkdir(parents=True, exist_ok=True)


def alpha_from_white(im):
    """White background -> transparency, keeping anti-aliased edges (alpha = distance from white)."""
    im = im.convert("RGB")
    px = im.load()
    w, h = im.size
    out = Image.new("RGBA", (w, h))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            a = 255 - min(r, g, b)
            if a < 12:
                op[x, y] = (0, 0, 0, 0)
                continue
            a = min(255, int(a * 1.08))
            # un-premultiply against white
            k = a / 255.0
            rr = int(max(0, min(255, (r - 255 * (1 - k)) / k)))
            gg = int(max(0, min(255, (g - 255 * (1 - k)) / k)))
            bb = int(max(0, min(255, (b - 255 * (1 - k)) / k)))
            op[x, y] = (rr, gg, bb, a)
    return out


def is_gold(r, g, b):
    return r > 90 and r - b > 45 and r >= g


def recolor_dark_to(im, rgb):
    """Neutral (black) ink -> rgb; gold stays gold."""
    im = im.copy()
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a and not is_gold(r, g, b):
                px[x, y] = (*rgb, a)
    return im


def main():
    src = Image.open(SRC).convert("RGB")
    # trim white margins
    gray = src.convert("L").point(lambda v: 255 if v < 235 else 0)
    box = gray.getbbox()
    pad = 10
    box = (max(0, box[0] - pad), max(0, box[1] - pad), min(src.width, box[2] + pad), min(src.height, box[3] + pad))
    crop = src.crop(box)
    print("trimmed", crop.size)
    golds = Counter()
    for r, g, b in crop.resize((300, 150)).getdata():
        if is_gold(r, g, b):
            golds[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += 1
    print("gold samples", golds.most_common(6))
    t = alpha_from_white(crop)
    t.save(ROOT / "brand" / "opera-logo-transparent.png")
    light = recolor_dark_to(t, (255, 255, 255))
    light.save(ROOT / "brand" / "opera-logo-light.png")
    for name, im in (("logo-header", t), ("logo-light", light)):
        for hgt in (64, 128):
            w = round(im.width * hgt / im.height)
            r = im.resize((w, hgt), Image.LANCZOS)
            r.save(OUT / f"{name}-{hgt}.webp", "WEBP", quality=92, method=6)
            r.save(OUT / f"{name}-{hgt}.png", optimize=True)
        print(name, round(im.width * 64 / im.height), "x 64")
    full = t.resize((round(t.width * 512 / t.height), 512), Image.LANCZOS)
    full.save(OUT / "logo-512.png", optimize=True)
    # wordmark-only region (top part, OPERA) for the mark: the A triangle is the right ~22% of the top block
    W, H = t.size
    top = t.crop((0, 0, W, int(H * 0.60)))
    tb = top.getbbox()
    top = top.crop(tb)
    tw, th = top.size
    mark = top.crop((int(tw * 0.765), 0, tw, th))
    mb = mark.getbbox()
    mark = mark.crop(mb)
    side = max(mark.size) + 40
    sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    sq.paste(mark, ((side - mark.width) // 2, (side - mark.height) // 2 + 6), mark)
    sq.save(ROOT / "brand" / "opera-mark.png")
    # favicon/app icons: mark on black rounded square, light version of the black facet
    for size, name in ((192, "icon-192.png"), (180, "apple-touch-icon.png"), (512, "icon-512.png"), (48, "fav-48.png")):
        bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(bg)
        d.rounded_rectangle((0, 0, size - 1, size - 1), radius=int(size * 0.2), fill=(17, 17, 17, 255))
        m = recolor_dark_to(sq, (255, 255, 255)).resize((int(size * 0.82), int(size * 0.82)), Image.LANCZOS)
        bg.paste(m, ((size - m.width) // 2, (size - m.height) // 2), m)
        bg.save(OUT / name, optimize=True)
    Image.open(OUT / "fav-48.png").save(ROOT / "site" / "static" / "img" / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    (OUT / "fav-48.png").unlink()
    # OG image 1200x630: white card with the logo
    og = Image.new("RGB", (1200, 630), (255, 255, 255))
    lg = t.resize((900, round(t.height * 900 / t.width)), Image.LANCZOS)
    og.paste(lg, ((1200 - lg.width) // 2, (630 - lg.height) // 2 - 20), lg)
    d = ImageDraw.Draw(og)
    d.rectangle((0, 600, 1200, 630), fill=(17, 17, 17))
    og.save(OUT / "og.jpg", "JPEG", quality=86, optimize=True, progressive=True)
    print("done")


if __name__ == "__main__":
    main()
