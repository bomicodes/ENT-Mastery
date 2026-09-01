#!/usr/bin/env python3
"""Fail closed on post-septoplasty septal hematoma/abscess rescue."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
app = runtime_entry_pasha.app
TARGET = "septoplasty"


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def contains_all(blob, tokens):
    hay = norm(blob)
    return all(norm(token) in hay for token in tokens)


def main():
    failures = 0
    op = (data.OR_PREP_REGISTRY or {}).get(TARGET)
    if not op:
        matches = [(slug, row) for slug, row in (data.OR_PREP_REGISTRY or {}).items() if "septoplasty" in norm(str(slug) + " " + str((row or {}).get("title", "")))]
        if len(matches) != 1:
            return fail(f"expected one live septoplasty target, found {len(matches)}")
        _, op = matches[0]

    postop = " ".join(str(x) for x in (op.get("postop") or []))
    checks = {
        "urgent recognition": ("boggy", "septal hematoma", "abscess", "urgent"),
        "cartilage danger": ("mucoperichondrium", "cartilage", "necrosis", "saddle-nose"),
        "definitive drainage": ("prompt evacuation", "intranasal mucosal incision", "loculations", "irrigate"),
        "culture without drainage delay": ("culture", "must not delay drainage"),
        "dead-space control": ("re-oppose", "quilting", "packing", "re-collection"),
        "infection treatment": ("systemic antimicrobial", "tailored to cultures"),
        "post-rescue surveillance": ("re-examine", "perforation", "saddle deformity"),
    }
    for label, tokens in checks.items():
        if not contains_all(postop, tokens):
            failures += fail(f"missing {label}: {tokens}")

    if not op.get("septal_hematoma_rescue_v284"):
        failures += fail("v28.4 live marker missing")

    sources = " ".join(str(x) for x in (op.get("sources") or []))
    for token in ("Cummings", "K. J. Lee", "Pasha", "Jackson", "Nanu"):
        if norm(token) not in norm(sources):
            failures += fail(f"missing provenance token {token!r}")

    client = app.test_client()
    r = client.get("/case-tomorrow", query_string={"q": op.get("title", TARGET)}, follow_redirects=True)
    if r.status_code >= 500:
        failures += fail(f"/case-tomorrow HTTP {r.status_code}")
    rendered = r.get_data(as_text=True)
    for token in ("septal hematoma", "prompt evacuation", "quilting", "re-collection"):
        if norm(token) not in norm(rendered):
            failures += fail(f"rendered septoplasty route missing rescue token {token!r}")

    if failures:
        print(f"\nSeptal hematoma/abscess rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: live septoplasty OR case converts septal-collection recognition into urgent drainage, dead-space control, infection treatment, early recheck, route exposure, and source provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
