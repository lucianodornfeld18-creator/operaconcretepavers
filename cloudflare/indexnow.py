# -*- coding: utf-8 -*-
"""Submit every sitemap URL to IndexNow. Retries while the key file is still being verified.
Run from the project root: python cloudflare/indexnow.py"""
import json
import pathlib
import re
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
key = (ROOT / "site" / "indexnow-key.txt").read_text().strip()
urls = []
for sm in sorted((ROOT / "site" / "dist").glob("sitemap-*.xml")):
    urls += re.findall(r"<loc>(.*?)</loc>", sm.read_text(encoding="utf-8"))
body = json.dumps({"host": "operaconcretepavers.com", "key": key, "keyLocation": f"https://operaconcretepavers.com/{key}.txt", "urlList": urls}).encode()
for attempt in range(8):
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={
        "Content-Type": "application/json; charset=utf-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0"})
    try:
        print(len(urls), "urls ->", urllib.request.urlopen(req, timeout=60).status)
        break
    except urllib.error.HTTPError as e:
        print("attempt", attempt + 1, e.code, e.read()[:120])
        time.sleep(60)
