"""v21.7 — explicit all-domain learning-ladder inventory.

Prints the exact canonical topics that have not yet been deliberately reviewed.
This is informational rather than a release gate; completed-domain hard gates
remain in audit_learning_ladders_runtime_v204.py.
"""
from collections import defaultdict
import runtime_entry as rt

STAGES = {"foundation", "application", "senior_decision"}


def main():
    data = rt.data
    cases = list(data.CLINICAL_CHALLENGES_V119)
    by_cid = defaultdict(list)
    for q in cases:
        cid = q.get("concept_id")
        if cid:
            by_cid[cid].append(q)

    reviewed_pairs = {
        (q.get("domain"), q.get("topic"))
        for q in cases if q.get("ladder_reviewed")
    }

    for domain, modules in data.DEEP_MODULES_V6.items():
        topics = [m.get("topic") for m in modules if m.get("topic")]
        unreviewed = []
        incomplete = []
        for topic in topics:
            pair = (domain, topic)
            cid = data._v6_item_id(domain, topic)
            stages = {
                q.get("learning_stage") for q in by_cid.get(cid, [])
                if q.get("learning_stage") in STAGES
            }
            if pair not in reviewed_pairs:
                unreviewed.append(topic)
            elif stages != STAGES:
                incomplete.append((topic, sorted(STAGES - stages)))

        reviewed_n = len(topics) - len(unreviewed)
        complete_n = reviewed_n - len(incomplete)
        print(f"DOMAIN_LADDER_INVENTORY|{domain}|canonical={len(topics)}|reviewed={reviewed_n}|complete={complete_n}")
        for topic in unreviewed:
            print(f"UNREVIEWED_CANONICAL_TOPIC|{domain}|{topic}")
        for topic, missing in incomplete:
            print(f"INCOMPLETE_REVIEWED_TOPIC|{domain}|{topic}|missing={','.join(missing)}")


if __name__ == "__main__":
    main()
