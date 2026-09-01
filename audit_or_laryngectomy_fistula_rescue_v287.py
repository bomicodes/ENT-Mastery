#!/usr/bin/env python3
"""Fail closed on live post-total-laryngectomy PCF/salivary-leak rescue."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
app = runtime_entry_pasha.app


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def contains_all(blob, tokens):
    hay = norm(blob)
    return all(norm(token) in hay for token in tokens)


def resolve(reg):
    if "total-laryngectomy" in reg:
        return "total-laryngectomy", reg["total-laryngectomy"]
    for slug, op in reg.items():
        hay = norm(f"{slug} {(op or {}).get('title', '')}")
        if "total laryngectomy" in hay:
            return slug, op
    return None, None


def main():
    failures = 0
    slug, op = resolve(data.OR_PREP_REGISTRY or {})
    if not op:
        return fail("no live total-laryngectomy OR target resolved")

    postop = " ".join(str(x) for x in (op.get("postop") or []))
    checks = {
        "PCF recognition": ("salivary", "wound", "pharyngocutaneous fistula"),
        "neck-only airway": ("neck-only airway", "laryngectomy stoma", "will not ventilate"),
        "nutrition/physiology": ("stop oral intake", "enteral nutritional support", "protein-calorie", "hypothyroidism"),
        "wound/source control": ("cross-sectional imaging", "infected collection", "drain", "conservative management"),
        "great-vessel danger": ("carotid", "sentinel", "hemorrhage", "blind deep packing"),
        "revision commitment": ("failure", "reconstructive reassessment", "well-vascularized tissue", "durable"),
        "equipoise protection": ("salivary-bypass tubes", "negative-pressure wound therapy", "single postoperative day", "not universal"),
    }
    for label, tokens in checks.items():
        if not contains_all(postop, tokens):
            failures += fail(f"{slug}: missing {label}: {tokens}")

    if not op.get("laryngectomy_fistula_rescue_v287"):
        failures += fail(f"{slug}: v28.7 live marker missing")

    sources = " ".join(str(x) for x in (op.get("sources") or []))
    for token in ("Cummings", "K. J. Lee", "Pasha", "IFOS", "Gomis-Lleal", "Williamson"):
        if norm(token) not in norm(sources):
            failures += fail(f"{slug}: missing provenance token {token!r}")

    r = app.test_client().get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
    if r.status_code >= 500:
        failures += fail(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    rendered = r.get_data(as_text=True)
    for token in ("PHARYNGOCUTANEOUS FISTULA", "neck-only airway", "DANGER-ZONE / CAROTID BAILOUT", "EQUIPOISE / LOCAL-PROTOCOL POINT"):
        if norm(token) not in norm(rendered):
            failures += fail(f"{slug}: rendered route missing rescue token {token!r}")

    if failures:
        print(f"\nLaryngectomy fistula rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: live total-laryngectomy OR Tomorrow exposes PCF recognition, neck-only airway safety, nutrition/drainage, vessel danger, revision thresholds, current equipoise and traceable provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
