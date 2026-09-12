#!/usr/bin/env python3
"""v36.1 exact-live Pediatric Chronic Rhinosinusitis semantic/source regression."""

import sys
import runtime_entry_pasha

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Pediatric Chronic Rhinosinusitis"
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
        if not row.get("source_grounded_v361"):
            failures += fail("exact Pediatric Chronic Rhinosinusitis row did not receive v36.1 source/depth patch")
        meta = row.get("source_metadata_v361") or {}
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
        for qid in ("v136_rhi_21", "v144_rh_17", "v208_rhi_pedscrs_snr"):
            if qid not in preserved:
                failures += fail(f"v36.1 did not explicitly preserve historical ladder id {qid}")

        sources = [str(x) for x in (row.get("source_basis") or []) if str(x).strip()]
        joined_sources = " ".join(sources).lower()
        for token in ("cummings", "pasha", "k.j. lee", "25274375", "33236525", "38400707", "39392410"):
            if token not in joined_sources:
                failures += fail(f"Pediatric CRS source trail missing {token!r}")

        combined = " ".join(str(row.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        semantic_groups = {
            "objective phenotype": ("objective", "viral"),
            "adenoid mechanism": ("adenoid", "reservoir"),
            "host-disorder escalation": ("pcd", "immune"),
            "imaging restraint": ("ct", "reflex"),
            "first surgical sequence": ("adenoidectomy", "first surgical"),
            "post-adenoid reassessment": ("persist", "reassess"),
            "selective ess": ("ess", "defined"),
            "child-specific extent": ("developed", "adult-style"),
            "balloon boundary": ("balloon", "not a default"),
            "complication override": ("orbital", "urgent"),
        }
        for label, tokens in semantic_groups.items():
            if not all(token in combined for token in tokens):
                failures += fail(f"Pediatric CRS clinical depth missing {label}: expected {tokens}")

        review = row.get("deliberate_review_v361") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(review.get(layer) or "").strip():
                failures += fail(f"deliberate review missing {layer}")
        if len(review.get("traps") or []) < 10:
            failures += fail("individualized Pediatric CRS trap set too shallow")

    if failures:
        print(f"Rhinology Pediatric CRS v36.1 FAILED with {failures} issue(s).")
        return 1
    print("PASS: exact-live Pediatric Chronic Rhinosinusitis preserves 42/325 contracts and now includes source-grounded pediatric phenotype, adenoid-first sequencing, host evaluation, selective imaging/ESS, balloon boundary and complication escalation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
