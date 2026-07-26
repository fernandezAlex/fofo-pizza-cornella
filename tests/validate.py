#!/usr/bin/env python3
"""Small dependency-free validation suite for the static site."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.h1 = 0
        self.images = []
        self.json_ld = []
        self._json_script = False
        self._json_buffer = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.images.append(attrs.get("src", ""))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._json_script = True
            self._json_buffer = []

    def handle_data(self, data):
        if self._json_script:
            self._json_buffer.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._json_script:
            self.json_ld.append(json.loads("".join(self._json_buffer)))
            self._json_script = False

v = Validator()
v.feed(HTML)
errors = []
if v.h1 != 1:
    errors.append(f"Expected one h1, found {v.h1}")
for href in v.links:
    if href.startswith("#") and href[1:] not in v.ids:
        errors.append(f"Broken internal link: {href}")
if v.images:
    errors.append(f"Third-party/raster images are not allowed: {v.images}")
if not v.json_ld or v.json_ld[0].get("@type") != "Restaurant":
    errors.append("Valid Restaurant JSON-LD not found")

items = re.findall(r"\['(?:clasicas|especialidades|blancas|postres|bebidas|extras)'\s*,", HTML)
if len(items) != 29:
    errors.append(f"Expected 29 menu products, found {len(items)}")

for forbidden in ("672 98 52 82", "Reservar", "WhatsApp", "Masa artesana", "terraza ·", "assets/"):
    if forbidden.lower() in HTML.lower():
        errors.append(f"Forbidden or unverified content found: {forbidden}")

required = ("+34931451225", "Uber Eats", "Proyecto web conceptual no oficial", "contaminación cruzada")
for value in required:
    if value not in HTML:
        errors.append(f"Required content missing: {value}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("VALIDATION OK: HTML, links, JSON-LD, 29 products and content safeguards")
