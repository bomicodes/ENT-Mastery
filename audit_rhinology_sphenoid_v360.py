#!/usr/bin/env python3
"""v36.0 exact-live isolated sphenoid disease semantic/source regression."""

import sys
import runtime_entry_pasha

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Sphenoidotomy"
EXPECTED_RHINOLOGY = 42
EXPECTED_GLOBAL = 325


def fail(message):
    print(f"FAIL: {message}")
    return 1


def main():
    data = runtime_entry_pasha.runtime_entry.data
    deep = getattr(data, "DEEP_MODULES_V6", {}) or {}
    all_rows = [(domain, row) for domain, rows in deep.items() for row in (rows or [])]
    rhino = deep.get(DOMAIN, []) or []
    failures = 0

    if len(all_rows) != EXPECTED_GLOBAL:
        failures += fail(f"canonical Deep Curriculum count changed: expected {EXPECTED_GLOBAL}, found {len(all_rows)}")
    if len(rhino) != EXPECTED_RHINOLOGY or len({r.get('topic') for r in rhino}) != EXPECTED_RHINOLOGY:
        failures += fail(f"Rhinology inventory drifted: expected 42 exact unique rows, found rows={len(rhino)} unique={len({r.get('topic') for r in rhino})}")

    matches = [row for row in rhino if row.get("topic") == TOPIC]
    if len(matches) != 1:
        failures += fail(f"expected exactly one exact live {DOMAIN}/{TOPIC}; found {len(matches)}")
    else:
        row = matches[0]
        if not row.get("source_grounded_v360"):
            failures += fail("exact Sphenoidotomy row did not receive v36.0 source/depth patch")
        meta = row.get("source_metadata_v360") or {}
        if meta.get("canonical_link") != {"domain": DOMAIN, "topic": TOPIC}:
            failures += fail("canonical source metadata link is wrong")
        ids = meta.get("textbook_drive_ids") or {}
        for key, expected in {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        }.items():
            if ids.get(key) != expected:
                failures += fail(f"source metadata missing exact connected Drive id for {key}")
        preserved = set(meta.get("preserved_ladder_ids") or [])
        for qid in ("v136_rhi_26", "v144_rh_21", "v209_rhi_sphenoid_snr"):
            if qid not in preserved:
                failures += fail(f"v36.0 did not explicitly preserve historical ladder id {qid}")

        sources = [str(x) for x in (row.get("source_basis") or []) if str(x).strip()]
        joined_sources = " ".join(sources).lower()
        for token in ("cummings", "pasha", "k.j. lee", "29024448", "40040258"):
            if token not in joined_sources:
                failures += fail(f"Sphenoidotomy source trail missing {token!r}")

        combined = " ".join(str(row.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        semantic_groups = {
            "broad differential": ("fungal ball", "mucocele", "tumor"),
            "normal-endoscopy pitfall": ("endoscopy", "normal"),
            "urgent neuro-ophthalmic boundary": ("visual", "cranial neurop"),
            "imaging escalation": ("ct", "mri"),
            "vascular bailout": ("vascular", "biopsy"),
            "operative danger anatomy": ("optic", "carotid"),
            "noninvasive fungal management": ("systemic antifungal", "surgical clearance"),
            "senior stop rule": ("stop", "re-localize"),
        }
        for label, tokens in semantic_groups.items():
            if not all(token in combined for token in tokens):
                failures += fail(f"Sphenoidotomy clinical depth missing {label}: expected {tokens}")

        review = row.get("deliberate_review_v360") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(review.get(layer) or "").strip():
                failures += fail(f"deliberate review missing {layer}")
        if len(review.get("traps") or []) < 8:
            failures += fail("individualized sphenoid trap set too shallow")

    if failures:
        print(f"Rhinology sphenoid v36.0 FAILED with {failures} issue(s).")
        return 1
    print("PASS: exact-live Sphenoidotomy preserves the 42/325 contracts and now includes source-grounded isolated-sphenoid disease recognition, imaging, urgency, pathology-specific management and optic/carotid bailout depth.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
