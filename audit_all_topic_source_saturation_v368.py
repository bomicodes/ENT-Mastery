#!/usr/bin/env python3
"""v37.1 all-topic Deep Curriculum source/core-text saturation non-regression gate.

Inventories the fully assembled learner-facing Deep Curriculum and fails closed if the
327-topic/nine-domain canonical contract drifts, source provenance is malformed, or
either source backlog grows. The ceilings are truthful ratchets from the last validated
census and must only move downward as reviewed clinical/source cohorts land.
"""

from collections import Counter
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
EXPECTED_DOMAIN_COUNTS = {
    "Otology / Neurotology": 48,
    "Rhinology / Allergy / Skull Base": 42,
    "Head & Neck Oncology": 42,
    "Thyroid / Parathyroid / Salivary": 32,
    "Pediatric Otolaryngology": 40,
    "Laryngology / Voice / Swallowing": 36,
    "Facial Plastics / Trauma": 33,
    "Sleep Surgery": 21,
    "General ENT / Emergencies": 33,
}
EXPECTED_TOTAL = sum(EXPECTED_DOMAIN_COUNTS.values())
MAX_MISSING_SOURCE_BASIS = 0
MAX_INCOMPLETE_CORE_TEXTBOOK = 0
CORE_TEXTBOOK_TOKENS = ("cummings", "pasha", "k.j. lee")


def fail(message):
    print(f"FAIL: {message}")
    return 1


def main():
    deep = getattr(data, "DEEP_MODULES_V6", {}) or {}
    rows = [(domain, row) for domain, domain_rows in deep.items() for row in (domain_rows or [])]
    failures = 0

    live_domains = set(deep)
    expected_domains = set(EXPECTED_DOMAIN_COUNTS)
    if live_domains != expected_domains:
        failures += fail(
            "domain set drift; missing=" + repr(sorted(expected_domains - live_domains))
            + "; extra=" + repr(sorted(live_domains - expected_domains))
        )

    for domain, expected_count in EXPECTED_DOMAIN_COUNTS.items():
        found = len(deep.get(domain, []) or [])
        if found != expected_count:
            failures += fail(
                f"{domain}: canonical count drift: expected {expected_count}, found {found}"
            )

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
    malformed = []
    missing_cummings = []
    missing_companion_core = []
    invalid_locator_metadata = []
    inflated_locator_claims = []
    for domain, row in rows:
        topic = str(row.get("topic") or "").strip()
        raw_sources = row.get("source_basis")
        if raw_sources is not None and not isinstance(raw_sources, (list, tuple)):
            malformed.append((domain, topic, type(raw_sources).__name__))
            sources = []
        else:
            sources = [str(x).strip() for x in (raw_sources or []) if str(x).strip()]
        if not sources:
            missing.append((domain, topic))
            continue
        sourced.append((domain, topic))
        joined = " ".join(sources).lower()
        hits = sum(token in joined for token in CORE_TEXTBOOK_TOKENS)
        if hits < 2:
            incomplete.append((domain, topic, hits))
        if "cummings" not in joined:
            missing_cummings.append((domain, topic))
        if "pasha" not in joined and "k.j. lee" not in joined:
            missing_companion_core.append((domain, topic))
        metadata = row.get("source_metadata_v408") or {}
        if not isinstance(metadata, dict) or metadata.get("locator_level") != "domain-foundational":
            invalid_locator_metadata.append((domain, topic))
        if "canonical locator:" in joined:
            inflated_locator_claims.append((domain, topic))

    print(f"SOURCE_SATURATION_TOTAL={len(rows)}")
    print(f"SOURCE_SATURATION_SOURCED={len(sourced)}")
    print(f"SOURCE_SATURATION_MISSING={len(missing)}")
    print(f"SOURCE_SATURATION_PERCENT={(100.0 * len(sourced) / len(rows)) if rows else 0:.1f}")
    print(f"SOURCE_SATURATION_INCOMPLETE_CORE_TEXTBOOK={len(incomplete)}")
    print(f"SOURCE_SATURATION_MALFORMED_SOURCE_BASIS={len(malformed)}")
    print(f"SOURCE_SATURATION_MISSING_CUMMINGS={len(missing_cummings)}")
    print(f"SOURCE_SATURATION_MISSING_PASHA_OR_KJLEE={len(missing_companion_core)}")
    print(f"SOURCE_SATURATION_INVALID_LOCATOR_METADATA={len(invalid_locator_metadata)}")
    print(f"SOURCE_SATURATION_INFLATED_LOCATOR_CLAIMS={len(inflated_locator_claims)}")

    missing_by_domain = Counter(domain for domain, _ in missing)
    incomplete_by_domain = Counter(domain for domain, _, _ in incomplete)
    for domain in EXPECTED_DOMAIN_COUNTS:
        total = len(deep.get(domain, []) or [])
        print(
            "SOURCE_DOMAIN\t"
            f"{domain}\ttotal={total}\tmissing={missing_by_domain[domain]}\t"
            f"incomplete_core_textbooks={incomplete_by_domain[domain]}"
        )

    if malformed:
        failures += fail(
            "source_basis schema drift: expected list/tuple provenance entries; "
            f"found {len(malformed)} malformed canonical row(s)"
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
    if invalid_locator_metadata:
        failures += fail(
            "v40.8 locator metadata missing or overstated on "
            f"{len(invalid_locator_metadata)} canonical row(s)"
        )
    if inflated_locator_claims:
        failures += fail(
            "legacy topic-level canonical-locator claim remains on "
            f"{len(inflated_locator_claims)} canonical row(s)"
        )

    for domain, topic, source_type in malformed:
        print(f"SOURCE_BACKLOG_MALFORMED\t{domain}\t{topic}\ttype={source_type}")
    for domain, topic in missing:
        print(f"SOURCE_BACKLOG_MISSING\t{domain}\t{topic}")
    for domain, topic, hits in incomplete:
        print(f"SOURCE_BACKLOG_INCOMPLETE\t{domain}\t{topic}\tcore_textbook_hits={hits}")

    if failures:
        print(f"All-topic source/core-text saturation v37.1 FAILED with {failures} issue(s).")
        return 1

    print(
        "PASS: exact 327-topic/nine-domain live canonical contract inventoried; source_basis schema, "
        "missing-source and incomplete core-textbook backlogs cannot silently regress."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
