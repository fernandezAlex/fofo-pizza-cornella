#!/usr/bin/env python3
"""Dependency-free preservation checks for the Fofó Pizza snapshot."""
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
EXPECTED_IMAGES = {
    "71452652.jpg": "bb34c342328f4a33b582804a1001ad2c1303f87a05a1b8e63005a16579b326ae",
    "71452656.jpg": "392d880788432743f75068246753c5c4646f7d4ee7d308364e82c184a54a007c",
    "71452657.jpg": "ae2c64cb4fe1f32cb6951616995d75a54981f6c55e6b2562ed7b8228d39d5190",
    "71452659.jpg": "60f4b187be6047330f71188957bdd179d115c28f6c8fc0206de2bb6f2a24699d",
    "71452661.jpg": "3bed497e940ce79f338ffc9151c84ab9828a418786907db2e271ca17616e29ec",
    "71452663.jpg": "2029298528c4053d95275cb2b651a863f294dce00b5f80f4dc4a3383f4c3f6dc",
    "71452667.jpg": "26707067d2c9632d71ed475d06d977d79505ec1be78d76a4dcebc7fa1b25e9b7",
}
EXPECTED_LOGO = "11b63fe399c971cf1a4ed0acf5647655c8670de307dcb9c1076398ed84afef76"

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.images = []
        self.h1 = 0
        self.menu_items = 0
        self.local_refs = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "id" in data:
            self.ids.add(data["id"])
        classes = set(data.get("class", "").split())
        if tag == "h1":
            self.h1 += 1
        if tag == "article" and "menu-item" in classes:
            self.menu_items += 1
        if tag == "img" and data.get("src"):
            self.images.append(data["src"])
            self.local_refs.append(data["src"])
        if tag in {"script", "link"}:
            ref = data.get("src") or data.get("href")
            if ref and not ref.startswith(("http://", "https://", "data:", "#")):
                self.local_refs.append(ref)

def fail(message):
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)

text = HTML.read_text(encoding="utf-8")
audit = Audit()
audit.feed(text)

if audit.h1 != 1:
    fail(f"expected one h1, found {audit.h1}")
if audit.menu_items != 20:
    fail(f"expected 20 original menu items, found {audit.menu_items}")
required_ids = {"inicio", "contenido", "historia", "carta", "galeria", "visitanos"}
if missing := required_ids - audit.ids:
    fail(f"missing original anchors: {sorted(missing)}")
if len(audit.images) != 8:
    fail(f"expected seven photos and one logo placement, found {len(audit.images)} image references")
names = [Path(p).name for p in audit.images]
if set(names) != set(EXPECTED_IMAGES) | {"logo-fofo.png"}:
    fail("image references differ from the expected photos and official logo")
if names.count("logo-fofo.png") != 1:
    fail("official logo must appear once in the header")
for ref in audit.local_refs:
    if not (ROOT / ref).exists():
        fail(f"missing local reference: {ref}")
for name, expected in EXPECTED_IMAGES.items():
    actual = hashlib.sha256((ROOT / "assets" / name).read_bytes()).hexdigest()
    if actual != expected:
        fail(f"asset checksum changed: {name}")
logo_hash = hashlib.sha256((ROOT / "assets" / "logo-fofo.png").read_bytes()).hexdigest()
if logo_hash != EXPECTED_LOGO:
    fail("transparent corporate logo checksum changed")
for phrase in [
    "Pizza con<br><em>carácter.</em>",
    "Pocas reglas.<br>Mucho oficio.",
    "La Mortadella.",
    "Sin filtros.<br>Recién hechas.",
    "Tu mesa, tu caja<br>o tu sofá.",
]:
    if phrase not in text:
        fail(f"missing original phrase: {phrase}")
if "new IntersectionObserver" not in text or "data-filter" not in text:
    fail("original interactions are missing")
for token in ["--green:#4faa36", "--green-bright:#74ec4a", "--green-dark:#245c32"]:
    if token not in text:
        fail(f"missing corporate palette token: {token}")
for marker in [
    'id="pizza-modal"',
    'class="pizza-modal-image"',
    '@keyframes pizza-open',
    'const PIZZA_PLACEHOLDER="assets/71452652.jpg"',
    "pizzaModal.showModal()",
    "document.querySelectorAll('.menu-item').forEach((item,index)",
]:
    if marker not in text:
        fail(f"missing pizza thumbnail/modal behavior: {marker}")
if re.search(r"(gho_|github_pat_|BEGIN (RSA|OPENSSH) PRIVATE KEY|AKIA[0-9A-Z]{16})", text):
    fail("possible secret in published HTML")

print("VALIDATION OK: original content and 7 photos preserved; logo, brand palette, 20 thumbnails and circular pizza modal present")
