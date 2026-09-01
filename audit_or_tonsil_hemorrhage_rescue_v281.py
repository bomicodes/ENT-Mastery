#!/usr/bin/env python3
"""Fail closed on executable post-tonsillectomy hemorrhage rescue in final Render assembly."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
app = runtime_entry_pasha.app


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def is_target(slug, op):
    text = norm(str(slug) + " " + str((op or {}).get("title", "")))
    if "lingual tonsil" in text:
        return False
    return any(term in text for term in ("tonsillectomy", "adenotonsillectomy", "tonsillectomy and adenoidectomy"))


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main():
    rows = [(slug, op) for slug, op in (data.OR_PREP_REGISTRY or {}).items() if is_target(slug, op)]
    if not rows:
        return fail("no live tonsillectomy/adenotonsillectomy OR Tomorrow case resolved")

    failures = 0
    client = app.test_client()
    for slug, op in rows:
        blob = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        checks = {
            "airway-hemorrhage commitment": (("airway",), ("hemorrhage", "bleeding"), ("npo",), ("suction",)),
            "resuscitation and OR escalation": (("iv access",), ("type-and-screen", "crossmatch"), ("anesthesia",), ("operative control", "or support")),
            "occult swallowed blood awareness": (("swallow",), ("hemoglobin",)),
            "targeted source control": (("identify the actual bleeding point",), ("targeted",), ("cautery", "suture ligation")),
            "no blind deep-lateral treatment": (("blind",), ("deep lateral", "lateral fossa"), ("major vessels",)),
            "TXA adjunct not substitute": (("tranexamic",), ("adjunct",), ("must not delay",)),
            "pseudoaneurysm bailout": (("gushing", "arterial hemorrhage"), ("pseudoaneurysm",), ("angiography",), ("neurointerventional", "vascular")),
        }
        for label, groups in checks.items():
            if not all(any(token in blob for token in group) for group in groups):
                failures += fail(f"{slug}: missing {label}")

        if not op.get("tonsil_hemorrhage_rescue_v281"):
            failures += fail(f"{slug}: v28.1 marker missing")

        sources = " ".join(str(x) for x in (op.get("source_basis") or [])).lower()
        for token in ("cummings", "k.j. lee", "pasha", "aao-hnsf", "casey", "tranexamic", "pseudoaneurysm"):
            if token not in sources:
                failures += fail(f"{slug}: missing provenance token {token!r}")

        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures += fail(f"{slug}: /case-tomorrow HTTP {r.status_code}")
        rendered = r.get_data(as_text=True).lower()
        for token in ("post-tonsillectomy hemorrhage", "pseudoaneurysm", "tranexamic"):
            if token not in rendered:
                failures += fail(f"{slug}: rendered route missing rescue token {token!r}")

    if failures:
        print(f"\nPost-tonsillectomy hemorrhage rescue gate FAILED with {failures} issue(s).")
        return 1
    print(f"PASS: {len(rows)} live tonsillectomy case(s) contain airway/resuscitation, operative source control, TXA-as-adjunct, vascular bailout, route exposure, and source provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
