#!/usr/bin/env python3
"""Fail closed on executable post-thyroidectomy hematoma rescue in final Render assembly."""

import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
app = runtime_entry_pasha.app
TARGETS = ("thyroid-lobectomy", "total-thyroidectomy", "reop-thyroid")


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main():
    failures = 0
    client = app.test_client()
    resolved = []
    for slug in TARGETS:
        op = (data.OR_PREP_REGISTRY or {}).get(slug)
        if not op:
            failures += fail(f"missing live OR Tomorrow target {slug}")
            continue
        resolved.append(slug)
        blob = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        checks = {
            "early recognition": ("neck swelling", "dysphagia", "anxiety", "stridor is a late sign"),
            "immediate oxygen/help": ("supplemental oxygen", "head-up", "senior surgical", "anesthesia"),
            "SCOOP bedside decompression": ("scoop", "cut sutures", "open skin", "open the superficial and deep muscle"),
            "no imaging delay": ("do not wait", "imaging"),
            "definitive OR source control": ("return urgently to the operating room", "identify and control the bleeding source"),
            "failed-decompression airway escalation": ("does not promptly stabilize", "tracheal intubation", "front-of-neck airway"),
            "adjunct-not-substitute rule": ("dexamethasone", "tranexamic", "adjuncts rather than substitutes"),
        }
        for label, tokens in checks.items():
            if not all(token in blob for token in tokens):
                failures += fail(f"{slug}: missing {label}: {tokens}")
        if not op.get("thyroid_hematoma_rescue_v282"):
            failures += fail(f"{slug}: v28.2 marker missing")
        sources = " ".join(str(x) for x in (op.get("sources") or [])).lower()
        for token in ("cummings", "k. j. lee", "pasha", "difficult airway society", "baets", "ent-uk", "iliff"):
            if token not in sources:
                failures += fail(f"{slug}: missing provenance token {token!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures += fail(f"{slug}: /case-tomorrow HTTP {r.status_code}")
        rendered = r.get_data(as_text=True).lower()
        for token in ("scoop", "post-thyroid hematoma", "front-of-neck airway"):
            if token not in rendered:
                failures += fail(f"{slug}: rendered route missing rescue token {token!r}")
    if failures:
        print(f"\nPost-thyroidectomy hematoma rescue gate FAILED with {failures} issue(s).")
        return 1
    print(f"PASS: {len(resolved)} thyroid OR case(s) contain early recognition, bedside SCOOP decompression, airway escalation, definitive hemostasis, route exposure, and source provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
