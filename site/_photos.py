# -*- coding: utf-8 -*-
"""Photo registry. site/_photos_registry.json is written by brand/make_photos.py from images/stock (temporary stock
photos, licence recorded) and, later, images/incoming (the owner's job photos). Stock photos are never described as
our work: alt text says only what is visible, and schema gives them no creator."""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
PHOTO_DIR = "/static/img/photos/"
try:
    PHOTOS = json.loads((ROOT / "_photos_registry.json").read_text(encoding="utf-8"))
except FileNotFoundError:
    PHOTOS = {}
ORDER = list(PHOTOS)


def has(pid):
    return pid in PHOTOS


def info(pid):
    d = dict(PHOTOS[pid])
    d["id"] = pid
    return d


def for_service(service, n=1, skip=()):
    """Photo ids tagged for a service, best first."""
    got = [p for p in ORDER if service in PHOTOS[p].get("services", []) and p not in skip]
    return got[:n]


def url(pid, w=None, thumb=False, kind="webp"):
    d = info(pid)
    if kind == "og":
        return f"{PHOTO_DIR}{d['stem']}-og.jpg"
    if thumb:
        return f"{PHOTO_DIR}{d['stem']}-t{w or d['thumbs'][-1]}.webp"
    return f"{PHOTO_DIR}{d['stem']}-{w or d['widths'][-1]}.webp"
