#!/usr/bin/env python3
"""v35.9 exact-live cholesteatoma source/depth and source-backlog regression."""

from pathlib import Path
import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Otology / Neurotology"
TOPIC = "Chronic Otitis Media / Cholesteatoma"


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
        if not row.get("source_grounded_v359"):
            failures += fail("cholesteatoma exact-live record did not receive v35.9 source patch")
        sources = [str(x) for x in (row.get("source_basis") or []) if str(x).strip()]
        joined = " ".join(sources).lower()
        if len(sources) < 7:
            failures += fail(f"cholesteatoma source_basis too shallow: {len(sources)}")
        for token in ("cummings", "pasha", "k.j. lee", "18qgoaazhvh", "14e4iy4xcj", "112c9y0fb1", "eaono/jos", "10.5152/iao.2017.3363", "10.1177/00034894241250253", "10.1002/ohn.70204", "diffusion"):
            if token not in joined:
                failures += fail(f"cholesteatoma source trail missing {token!r}")
        meta = row.get("source_metadata_v359") or {}
        if meta.get("canonical_link") != {"domain": DOMAIN, "topic": TOPIC}:
            failures += fail("cholesteatoma canonical source metadata link is wrong")
        if "2026" not in str(meta.get("management_currency") or ""):
            failures += fail("cholesteatoma management-currency metadata does not record current 2026 evidence review")
        review = row.get("deliberate_review_v359") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(review.get(layer) or "").strip():
                failures += fail(f"cholesteatoma deliberate review missing {layer}")
        if len(review.get("traps") or []) < 8:
            failures += fail("cholesteatoma individualized trap set too shallow")
        combined = " ".join(str(row.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        for token in ("sinus tympani", "facial nerve", "labyrinthine fistula", "canal-wall-up", "canal-wall-down", "non-epi", "second-look", "surveillance"):
            if token not in combined:
                failures += fail(f"cholesteatoma clinical depth missing {token!r}")

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
        failures += fail("patched cholesteatoma topic remains in missing-source backlog")
    if len(missing) > 146:
        failures += fail(f"source missing backlog regressed: expected <=146 after v35.9, found {len(missing)}")
    for domain, topic in missing:
        print(f"SOURCE_BACKLOG_MISSING\t{domain}\t{topic}")
    for domain, topic, hits in incomplete:
        print(f"SOURCE_BACKLOG_INCOMPLETE\t{domain}\t{topic}\tcore_textbook_hits={hits}")

    if failures:
        print(f"Deep Curriculum source-completeness v35.9 FAILED with {failures} issue(s).")
        return 1
    print("PASS: exact-live Chronic Otitis Media / Cholesteatoma has rendered, traceable textbook/current-evidence provenance and senior operative/surveillance depth; global source backlog cannot regress.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
