"""v51.2 atlas cross-reference for the anatomy-by-OR-case pages and OR cards.

A reviewer checked every claim in textbook_xref/atlas_review/ against the Atlas of Head and Neck
Surgery (Simo, Pracy & Fernandes, 2024) and Janfaza, Surgical Anatomy of the Head and Neck. Their
verdicts are textbook_xref/atlas_corrections/*.csv. This module:

* applies the corrections, which are recorded as exact text replacements in
  textbook_xref/atlas_corrections/fixes_*.py (ANATOMY_FIXES and OR_FIXES = [(slug, old, new), ...]);
* adds the confirmed atlas pages to each anatomy page's sources.

install_anatomy_atlas_fixes_v512 runs before the anatomy section installs; install_or_atlas_fixes_v512
runs after the OR card repairs.
"""
import csv
import glob
import importlib.util
import os

_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "textbook_xref", "atlas_corrections")
SHORT = (("Simo", "Atlas of Head and Neck Surgery (Simo, Pracy & Fernandes 2024)"),
         ("Atlas of Head", "Atlas of Head and Neck Surgery (Simo, Pracy & Fernandes 2024)"),
         ("Janfaza", "Janfaza, Surgical Anatomy of the Head and Neck"),
         ("Surgical Anatomy", "Janfaza, Surgical Anatomy of the Head and Neck"),
         ("Cummings", "Cummings 7e"), ("K.J.", "K.J. Lee 12e"), ("Pasha", "Pasha & Golub 6e"),
         ("Bluestone", "Bluestone & Stool 5e"))
MAX_CITES = 8


def _short(book):
    book = book.strip()
    for k, v in SHORT:
        if book.startswith(k):
            return v
    return book


def _split(v):
    return [x.strip() for x in str(v or "").split("|")]


def _load_fixes():
    anatomy, orc = [], []
    for path in sorted(glob.glob(os.path.join(_DIR, "fixes_*.py"))):
        spec = importlib.util.spec_from_file_location("atlas_fix_" + os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        anatomy += list(getattr(mod, "ANATOMY_FIXES", []))
        orc += list(getattr(mod, "OR_FIXES", []))
    return anatomy, orc


def _citations():
    cites = {}
    for path in sorted(glob.glob(os.path.join(_DIR, "*.csv"))):
        with open(path, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r.get("verdict", "").strip() not in ("OK", "CORRECT", "CONFLICT"):
                    continue
                iid = r.get("item_id", "").strip()
                if not (iid.startswith("A-") or iid.startswith("OR-")):
                    continue
                slug = iid.split("-", 1)[1].rsplit(".", 1)[0]
                books, chaps, pages = _split(r.get("book")), _split(r.get("edition_chapter")), _split(r.get("printed_page"))
                for i, page in enumerate(pages):
                    if not page:
                        continue
                    book = _short(books[min(i, len(books) - 1)])
                    chap = chaps[min(i, len(chaps) - 1)]
                    chap = chap.split(",", 1)[-1].strip() if "," in chap else chap
                    label = "%s, %s, p %s" % (book, chap, page)
                    lst = cites.setdefault(slug, [])
                    if label not in lst:
                        lst.append(label)
    return cites


def _replace(obj, old, new):
    """Replace old with new in every string inside obj (dicts and lists mutated in place)."""
    n = 0
    if isinstance(obj, dict):
        for k, v in list(obj.items()):
            if isinstance(v, str):
                if old in v:
                    obj[k] = v.replace(old, new)
                    n += 1
            else:
                n += _replace(v, old, new)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str):
                if old in v:
                    obj[i] = v.replace(old, new)
                    n += 1
            else:
                n += _replace(v, old, new)
    return n


def _case_modules():
    import anatomy_cases_v510
    import pkgutil
    mods = []
    for info in sorted(pkgutil.iter_modules(anatomy_cases_v510.__path__), key=lambda i: i.name):
        mods.append(importlib.import_module("anatomy_cases_v510." + info.name))
    return mods


def install_anatomy_atlas_fixes_v512(data):
    anatomy_fixes, _ = _load_fixes()
    cases = {}
    for mod in _case_modules():
        cases.update(getattr(mod, "CASES", {}))
    applied, missed = 0, []
    for slug, old, new in anatomy_fixes:
        c = cases.get(slug)
        n = _replace(c, old, new) if c is not None else 0
        if n:
            applied += 1
        else:
            missed.append((slug, old[:60]))
    cited = 0
    for slug, labels in _citations().items():
        c = cases.get(slug)
        if c is None:
            continue
        src = c.setdefault("sources", [])
        have = {s[0] if isinstance(s, (list, tuple)) else s for s in src}
        added = 0
        for label in labels:
            if label not in have and added < MAX_CITES:
                src.append([label, ""])
                have.add(label)
                added += 1
        cited += bool(added)
    result = {"anatomy_fixes": applied, "anatomy_missed": missed, "cases_cited": cited}
    data.ANATOMY_ATLAS_V512 = result
    return result


def install_or_atlas_fixes_v512(data):
    _, or_fixes = _load_fixes()
    reg = getattr(data, "OR_PREP_REGISTRY", None) or {}
    applied, missed = 0, []
    for slug, old, new in or_fixes:
        card = reg.get(slug)
        n = _replace(card, old, new) if card is not None else 0
        if n:
            applied += 1
        else:
            missed.append((slug, old[:60]))
    result = {"or_fixes": applied, "or_missed": missed}
    data.OR_ATLAS_V512 = result
    return result
