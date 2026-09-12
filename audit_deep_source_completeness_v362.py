#!/usr/bin/env python3
"""v36.2 exact-live Vestibular Schwannoma source/depth and source-backlog regression."""

from pathlib import Path
import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Otology / Neurotology"
TOPIC = "Vestibular Schwannoma"


def fail(message):
    print(f"FAIL: {message}")
    return 1


def main():
    deep = getattr(data, "DEEP_MODULES_V6", {}) or {}
    all_rows = [(domain, row) for domain, rows in deep.items() for row in (rows or [])]
    failures = 0
    if len(all_rows) != 325:
        failures += fail(f"canonical Deep Curriculum count changed: expected 325, found {len(all_rows)}")

    matches = [row for row in (deep.get(DOMAIN, []) or []) if row.get("topic") == TOPIC]
    if len(matches) != 1:
        failures += fail(f"expected exactly one exact live {DOMAIN}/{TOPIC}; found {len(matches)}")
    else:
        row = matches[0]
        if not row.get("source_grounded_v362"):
            failures += fail("Vestibular Schwannoma exact-live record did not receive v36.2 source patch")
        sources = [str(x) for x in (row.get("source_basis") or []) if str(x).strip()]
        joined = " ".join(sources).lower()
        for token in (
            "cummings", "pasha", "k.j. lee",
            "18qgoaazhvh", "14e4iy4xcj", "112c9y0fb1",
            "10.1227/neu.0000000000003473",
            "10.1227/neu.0000000000003551",
            "10.1227/neu.0000000000003419",
            "10.1227/neu.0000000000003416",
            "10.1007/s11060-025-04990-6",
            "10.3171/2025.8.jns25829",
        ):
            if token not in joined:
                failures += fail(f"Vestibular Schwannoma source trail missing {token!r}")
        meta = row.get("source_metadata_v362") or {}
        if meta.get("canonical_link") != {"domain": DOMAIN, "topic": TOPIC}:
            failures += fail("Vestibular Schwannoma canonical source metadata link is wrong")
        if "fda" not in str(meta.get("fda_scope") or "").lower():
            failures += fail("Vestibular Schwannoma source metadata does not explicitly bound FDA/drug-indication claims")
        review = row.get("deliberate_review_v362") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(review.get(layer) or "").strip():
                failures += fail(f"Vestibular Schwannoma deliberate review missing {layer}")
        if len(review.get("traps") or []) < 8:
            failures += fail("Vestibular Schwannoma individualized trap set too shallow")
        combined = " ".join(str(row.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        for token in (
            "asymmetric", "speech discrimination", "mri", "observation",
            "stereotactic radiosurgery", "middle fossa", "retrosigmoid",
            "translabyrinthine", "pseudoprogression", "facial nerve",
            "brainstem", "aica", "intentional residual",
        ):
            if token not in combined:
                failures += fail(f"Vestibular Schwannoma clinical depth missing {token!r}")

    template = Path("templates/curriculum_depth.html").read_text(encoding="utf-8")
    compact = re.sub(r"\s+", " ", template)
    if "m.source_basis" not in compact or "for s in m.source_basis" not in compact or "Source basis" not in compact:
        failures += fail("Deep Curriculum renderer does not surface source_basis")

    missing = []
    incomplete = []
    for domain, row in all_rows:
        sources = [str(x).strip() for x in (row.get("source_basis") or []) if str(x).strip()]
        if not sources:
            missing.append((domain, str(row.get("topic") or "")))
            continue
        joined = " ".join(sources).lower()
        hits = sum(token in joined for token in ("cummings", "pasha", "k.j. lee"))
        if hits < 2:
            incomplete.append((domain, str(row.get("topic") or ""), hits))
    print(f"SOURCE_COMPLETENESS_TOTAL={len(all_rows)}")
    print(f"SOURCE_MISSING_COUNT={len(missing)}")
    print(f"SOURCE_INCOMPLETE_TEXTBOOK_COUNT={len(incomplete)}")
    if any(domain == DOMAIN and topic == TOPIC for domain, topic in missing):
        failures += fail("patched Vestibular Schwannoma topic remains in missing-source backlog")
    if len(missing) > 142:
        failures += fail(f"source missing backlog regressed: expected <=142 after v36.2, found {len(missing)}")

    if failures:
        print(f"Deep Curriculum source-completeness v36.2 FAILED with {failures} issue(s).")
        return 1
    print("PASS: exact-live Vestibular Schwannoma has rendered, traceable textbook/current-evidence provenance and senior observation/SRS/operative reasoning; global source backlog cannot regress.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
