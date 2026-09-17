#!/usr/bin/env python3
"""v37.0 all-topic Deep Curriculum source/core-text saturation non-regression gate.

This gate inventories all 325 exact canonical topics and fails closed if either the
missing-source backlog or the incomplete core-textbook backlog grows. The ceilings are
truthful ratchets from the last validated census and must only move downward as reviewed
clinical/source cohorts land.
"""

from collections import Counter
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
EXPECTED_TOTAL = 325
MAX_MISSING_SOURCE_BASIS = 139
MAX_INCOMPLETE_CORE_TEXTBOOK = 69
CORE_TEXTBOOK_TOKENS = ("cummings", "pasha", "k.j. lee")


def fail(message):
    print(f"FAIL: {message}")
    return 1


def main():
    deep = getattr(data, "DEEP_MODULES_V6", {}) or {}
    rows = [(domain, row) for domain, domain_rows in deep.items() for row in (domain_rows or [])]
    failures = 0

    if len(rows) != EXPECTED_TOTAL:
        failures += fail(f"strict canonical count changed: expected {EXPECTED_TOTAL}, found {len(rows)}")

    keys = [(domain, str(row.get("topic") or "").strip()) for domain, row in rows]
    if len(set(keys)) != len(keys):
        failures += fail("duplicate exact domain/topic canonical rows detected")
    if any(not topic for _, topic in keys):
        failures += fail("one or more canonical rows has an empty topic")

    missing = []
    incomplete = []
    sourced = []
    for domain, row in rows:
        topic = str(row.get("topic") or "").strip()
        sources = [str(x).strip() for x in (row.get("source_basis") or []) if str(x).strip()]
        if not sources:
            missing.append((domain, topic))
            continue
        sourced.append((domain, topic))
        joined = " ".join(sources).lower()
        hits = sum(token in joined for token in CORE_TEXTBOOK_TOKENS)
        if hits < 2:
            incomplete.append((domain, topic, hits))

    print(f"SOURCE_SATURATION_TOTAL={len(rows)}")
    print(f"SOURCE_SATURATION_SOURCED={len(sourced)}")
    print(f"SOURCE_SATURATION_MISSING={len(missing)}")
    print(f"SOURCE_SATURATION_PERCENT={(100.0 * len(sourced) / len(rows)) if rows else 0:.1f}")
    print(f"SOURCE_SATURATION_INCOMPLETE_CORE_TEXTBOOK={len(incomplete)}")

    missing_by_domain = Counter(domain for domain, _ in missing)
    incomplete_by_domain = Counter(domain for domain, _, _ in incomplete)
    for domain in deep:
        total = len(deep.get(domain, []) or [])
        print(
            "SOURCE_DOMAIN\t"
            f"{domain}\ttotal={total}\tmissing={missing_by_domain[domain]}\t"
            f"incomplete_core_textbooks={incomplete_by_domain[domain]}"
        )

    if len(missing) > MAX_MISSING_SOURCE_BASIS:
        failures += fail(
            f"missing-source backlog regressed: expected <= {MAX_MISSING_SOURCE_BASIS}, found {len(missing)}"
        )
    if len(incomplete) > MAX_INCOMPLETE_CORE_TEXTBOOK:
        failures += fail(
            "incomplete core-textbook backlog regressed: "
            f"expected <= {MAX_INCOMPLETE_CORE_TEXTBOOK}, found {len(incomplete)}"
        )

    for domain, topic in missing:
        print(f"SOURCE_BACKLOG_MISSING\t{domain}\t{topic}")
    for domain, topic, hits in incomplete:
        print(f"SOURCE_BACKLOG_INCOMPLETE\t{domain}\t{topic}\tcore_textbook_hits={hits}")

    if failures:
        print(f"All-topic source/core-text saturation v37.0 FAILED with {failures} issue(s).")
        return 1

    print(
        "PASS: all 325 exact live canonical topics were inventoried; missing-source and "
        "incomplete core-textbook backlogs cannot regress above their validated ratchets."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
