#!/usr/bin/env python3
"""v36.2 exact-live Revision FESS semantic/source regression."""

import sys
import runtime_entry_pasha

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Revision FESS"
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
    unique = {r.get("topic") for r in rhino}
    if len(rhino) != EXPECTED_RHINOLOGY or len(unique) != EXPECTED_RHINOLOGY:
        failures += fail(f"Rhinology inventory drifted: expected 42 exact unique rows, found rows={len(rhino)} unique={len(unique)}")

    matches = [row for row in rhino if row.get("topic") == TOPIC]
    if len(matches) != 1:
        failures += fail(f"expected exactly one exact live {DOMAIN}/{TOPIC}; found {len(matches)}")
    else:
        row = matches[0]
        if not row.get("source_grounded_v362"):
            failures += fail("exact Revision FESS row did not receive v36.2 source/depth patch")

        meta = row.get("source_metadata_v362") or {}
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
        for qid in ("v136_rhi_23", "v142_rhi_04", "v209_rhi_revision_snr"):
            if qid not in preserved:
                failures += fail(f"v36.2 did not explicitly preserve historical ladder id {qid}")

        sources = " ".join(str(x) for x in (row.get("source_basis") or [])).lower()
        for token in ("cummings", "pasha", "k.j. lee", "40424072", "40437675", "28107148", "37442058"):
            if token not in sources:
                failures += fail(f"Revision FESS source trail missing {token!r}")

        combined = " ".join(str(row.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        semantic_groups = {
            "mechanism-first failure taxonomy": ("failure mechanism", "nonrhinogenic"),
            "prior-operation reconstruction": ("operative note", "pathology"),
            "fine-cut CT and endoscopy": ("fine-cut", "endoscopy"),
            "maxillary recirculation": ("natural maxillary ostium", "recirculation"),
            "residual anatomy": ("residual uncinate", "frontal-recess"),
            "scar and turbinate failure": ("synechiae", "middle-turbinate lateralization"),
            "focal/host/phenotype reassessment": ("odontogenic", "aerd"),
            "do-not-revise patent anatomy": ("patent", "do not revise"),
            "altered danger zones": ("orbit", "skull base", "carotid", "optic nerve"),
            "stop-and-reorient bailout": ("stop dissection", "re-localize"),
            "outcome follow-up": ("3–12 month", "endoscopic outcome"),
        }
        for label, tokens in semantic_groups.items():
            if not all(token in combined for token in tokens):
                failures += fail(f"Revision FESS clinical depth missing {label}: expected {tokens}")

        review = row.get("deliberate_review_v362") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(review.get(layer) or "").strip():
                failures += fail(f"deliberate review missing {layer}")
        if len(review.get("traps") or []) < 10:
            failures += fail("individualized Revision FESS trap set too shallow")

    if failures:
        print(f"Rhinology Revision FESS v36.2 FAILED with {failures} issue(s).")
        return 1
    print("PASS: exact-live Revision FESS preserves 42/325 contracts and now includes source-grounded mechanism-first failure analysis, fine-cut CT/endoscopy mapping, residual anatomy/recirculation, focal-host reassessment, hypothesis-driven reoperation and altered-landmark danger-zone bailout.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
