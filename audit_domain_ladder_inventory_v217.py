"""v21.7 — explicit all-domain learning-ladder inventory.

Prints the exact canonical topics that have not yet been deliberately reviewed.
Review accounting follows canonical concept_id linkage rather than display-topic
strings so intentional aliases do not create false unreviewed rows.
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

    for domain, modules in data.DEEP_MODULES_V6.items():
        topics = [m.get("topic") for m in modules if m.get("topic")]
        unreviewed = []
        incomplete = []
        for topic in topics:
            cid = data._v6_item_id(domain, topic)
            linked = by_cid.get(cid, [])
            stages = {
                q.get("learning_stage") for q in linked
                if q.get("learning_stage") in STAGES
            }
            reviewed = any(q.get("ladder_reviewed") for q in linked)
            if not reviewed:
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
