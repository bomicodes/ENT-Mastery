#!/usr/bin/env python3
"""Fail closed if v41.4 loses its textbook + current-guidance reconciliation."""
import runtime_entry_pasha
from deep_source_claim_backfill_v414 import CLAIM_SOURCES_V414


STALE_OR_INCORRECT = (
    "Carniol ET et al. Traumatic tympanic membrane perforations: a systematic review",
    "Trozzi M et al. Pediatric vocal fold paralysis",
    "Vestibular migraine: diagnostic criteria. Bárány Society/IHS consensus. J Vestib Res. 2012",
    "Suárez-Quintanilla J et al. The laryngeal framework and spaces",
)


def main():
    deep = runtime_entry_pasha.runtime_entry.data.DEEP_MODULES_V6
    index = {(domain, row.get("topic")): row for domain, rows in deep.items() for row in rows}
    failures = []
    for key, expected in CLAIM_SOURCES_V414.items():
        row = index.get(key)
        if row is None:
            failures.append(f"missing topic: {key!r}")
            continue
        sources = row.get("source_basis") or []
        joined = "\n".join(sources)
        if not all(source in sources for source in expected):
            failures.append(f"missing v41.4 claim source: {key!r}")
        if "Cummings Otolaryngology" not in joined:
            failures.append(f"missing Cummings cross-reference: {key!r}")
        if not ("Pasha & Golub" in joined or "K.J. Lee" in joined):
            failures.append(f"missing board-text cross-reference: {key!r}")
        for stale in STALE_OR_INCORRECT:
            if stale in joined:
                failures.append(f"stale/incorrect citation retained: {key!r}: {stale}")

    print(f"CLAIM_SOURCE_TARGETS={len(CLAIM_SOURCES_V414)}")
    print(f"CLAIM_SOURCE_RECONCILIATION_FAILURES={len(failures)}")
    for failure in failures:
        print("FAIL:", failure)
    if failures:
        return 1
    print("PASS: all v41.4 targets retain connected-textbook provenance plus corrected claim-level guidance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
