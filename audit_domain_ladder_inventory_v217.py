"""v21.7 — strict all-domain learning-ladder inventory.

Reports the exact live canonical topics and now fails when any canonical topic is
unreviewed or lacks foundation/application/senior-decision coverage. Review
accounting follows canonical concept_id linkage rather than display-topic strings
so intentional aliases do not create false unreviewed rows. The expected domain
counts intentionally freeze the completed 325-topic curriculum; deliberate
canonical expansion must update this contract rather than silently appearing as a
report-only row.
"""
from collections import defaultdict
import runtime_entry as rt

STAGES = {"foundation", "application", "senior_decision"}
EXPECTED_COUNTS = {
    "Otology / Neurotology": 47,
    "Rhinology / Allergy / Skull Base": 42,
    "Head & Neck Oncology": 43,
    "Thyroid / Parathyroid / Salivary": 32,
    "Pediatric Otolaryngology": 40,
    "Laryngology / Voice / Swallowing": 36,
    "Facial Plastics / Trauma": 32,
    "Sleep Surgery": 21,
    "General ENT / Emergencies": 32,
}
EXPECTED_TOTAL = sum(EXPECTED_COUNTS.values())


def main():
    data = rt.data
    cases = list(data.CLINICAL_CHALLENGES_V119)
    by_cid = defaultdict(list)
    for q in cases:
        cid = q.get("concept_id")
        if cid:
            by_cid[cid].append(q)

    failures = []
    seen_cids = {}
    live_domains = set(data.DEEP_MODULES_V6)
    expected_domains = set(EXPECTED_COUNTS)
    if live_domains != expected_domains:
        failures.append(
            "domain set drift; missing=" + repr(sorted(expected_domains - live_domains))
            + "; extra=" + repr(sorted(live_domains - expected_domains))
        )

    canonical_total = 0
    complete_total = 0
    for domain, modules in data.DEEP_MODULES_V6.items():
        topics = [m.get("topic") for m in modules if m.get("topic")]
        canonical_total += len(topics)
        if domain in EXPECTED_COUNTS and len(topics) != EXPECTED_COUNTS[domain]:
            failures.append(
                f"{domain}: expected {EXPECTED_COUNTS[domain]} canonical topics, found {len(topics)}"
            )
        if len(topics) != len(set(topics)):
            failures.append(f"{domain}: duplicate canonical topic names")

        unreviewed = []
        incomplete = []
        for topic in topics:
            cid = data._v6_item_id(domain, topic)
            if not cid:
                failures.append(f"{domain}|{topic}: canonical ID lookup failed")
                continue
            prior = seen_cids.get(cid)
            if prior and prior != (domain, topic):
                failures.append(
                    f"duplicate canonical ID {cid}: {prior[0]}|{prior[1]} and {domain}|{topic}"
                )
            else:
                seen_cids[cid] = (domain, topic)

            linked = by_cid.get(cid, [])
            stages = {
                q.get("learning_stage") for q in linked
                if q.get("learning_stage") in STAGES
            }
            reviewed = any(q.get("ladder_reviewed") for q in linked)
            if not reviewed:
                unreviewed.append(topic)
                failures.append(f"{domain}|{topic}: no deliberately reviewed ladder row")
            elif stages != STAGES:
                missing = sorted(STAGES - stages)
                incomplete.append((topic, missing))
                failures.append(f"{domain}|{topic}: missing stages {','.join(missing)}")

        reviewed_n = len(topics) - len(unreviewed)
        complete_n = reviewed_n - len(incomplete)
        complete_total += complete_n
        print(f"DOMAIN_LADDER_INVENTORY|{domain}|canonical={len(topics)}|reviewed={reviewed_n}|complete={complete_n}")
        for topic in unreviewed:
            print(f"UNREVIEWED_CANONICAL_TOPIC|{domain}|{topic}")
        for topic, missing in incomplete:
            print(f"INCOMPLETE_REVIEWED_TOPIC|{domain}|{topic}|missing={','.join(missing)}")

    if canonical_total != EXPECTED_TOTAL:
        failures.append(f"expected {EXPECTED_TOTAL} canonical topics globally, found {canonical_total}")

    print(f"CANONICAL_LADDER_TOTAL|canonical={canonical_total}|complete={complete_total}|expected={EXPECTED_TOTAL}")
    print(f"CANONICAL_LADDER_INVENTORY_FAILURES|{len(failures)}")
    if failures:
        for failure in failures:
            print("FAIL|" + failure)
        raise SystemExit(1)
    print(f"PASS: exact {EXPECTED_TOTAL}/{EXPECTED_TOTAL} live canonical topics retain deliberately reviewed three-stage ladders")


if __name__ == "__main__":
    main()
