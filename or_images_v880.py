"""v88.0: intraoperative images and atlas links on the OR cards.

Images are openly licensed figures (CC BY, CC BY-SA or CC0 only; licence read on the article
page) from open-access journals and Wikimedia Commons, hot-linked like the lab images, each with
our own caption, a credit line and, where it fits, the operative step it illustrates. They live in
or_images_v880.json ({slug: [ {image_url, source, credit, license, caption, step} ]}).

Otology and neurotology cards also link to the matching chapters of Jackler's free Stanford
atlases (illustrations are linked, never copied).
"""
import json
import os

_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "or_images_v880.json")
_ALLOWED = ("CC BY", "CC0", "PUBLIC DOMAIN")
_SKIP_LINK = ("fundamentals-of-ear-surgery", "cranial-nerve-monitoring")


def _label(url):
    seg = url.rstrip("/").rsplit("/", 1)[-1]
    seg = seg.replace("-2", "").replace("-", " ")
    words = [w if w in ("of", "the", "to", "and", "in") else w.capitalize() for w in seg.split()]
    return " ".join(words).replace("Iac", "IAC")


def _ok(img):
    import re
    lic = (img.get("license") or "").upper()
    if re.search(r"(^|[-\s])(NC|ND)([-\s]|$)", lic):
        return False
    return lic.startswith(_ALLOWED) and img.get("image_url", "").startswith("https://")


def install_or_images_v880(data):
    registry = data.OR_PREP_REGISTRY
    try:
        with open(_PATH, encoding="utf-8") as fh:
            table = json.load(fh)
    except FileNotFoundError:
        table = {}
    n_img = n_cards = n_links = 0
    for slug, imgs in table.items():
        card = registry.get(slug)
        if not card:
            continue
        keep = [i for i in imgs if _ok(i)]
        steps = card.get("steps_v840") or card.get("steps") or []
        for i in keep:
            s = i.get("step")
            i["step_label"] = (f"Step {s + 1}" if isinstance(s, int) and 0 <= s < len(steps) else "")
        if keep:
            card["images_v880"] = keep
            n_img += len(keep)
            n_cards += 1
    try:
        from or_steps_v840 import ATLAS_URLS_V840
    except ImportError:
        ATLAS_URLS_V840 = {}
    for slug, urls in ATLAS_URLS_V840.items():
        card = registry.get(slug)
        if not card:
            continue
        links = [u for u in urls if not any(x in u for x in _SKIP_LINK)] or list(urls)
        card["atlas_links_v880"] = [{"url": u, "label": _label(u)} for u in links[:5]]
        n_links += 1
    return {"images": n_img, "cards_with_images": n_cards, "cards_with_atlas_links": n_links}
