"""v24.7 — exact remaining Pediatric Otolaryngology ladder inventory.

This is intentionally read-only. It derives remaining topics from the live canonical
DEEP_MODULES_V6 registry and runtime concept-id linkage, using the same deliberate
review/stage contract as the all-domain ladder inventory.

The audit emits both completed and remaining canonical topic names so CI logs can be
used as the source of truth for the next curation batch instead of relying on aliases
or stale hand-maintained inventories.
"""
from collections import defaultdict
import runtime_entry as rt

DOMAIN = "Pediatric Otolaryngology"
STAGES = {"foundation", "application", "senior_decision"}


def main():
    data = rt.data
    modules = data.DEEP_MODULES_V6.get(DOMAIN, [])
    topics = [m.get("topic") for m in modules if m.get("topic")]

    by_cid = defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid = q.get("concept_id")
        if cid:
            by_cid[cid].append(q)

    complete = []
    remaining = []
    incomplete = []
    for topic in topics:
        cid = data._v6_item_id(DOMAIN, topic)
        linked = by_cid.get(cid, [])
        stages = {q.get("learning_stage") for q in linked if q.get("learning_stage") in STAGES}
        reviewed = any(q.get("ladder_reviewed") for q in linked)
        if reviewed and stages == STAGES:
            complete.append(topic)
        elif reviewed:
            incomplete.append((topic, sorted(STAGES - stages)))
        else:
            remaining.append(topic)

    print(f"PEDIATRIC_LADDER_INVENTORY|canonical={len(topics)}|complete={len(complete)}|remaining={len(remaining)}|incomplete={len(incomplete)}")
    for topic in complete:
        print(f"PEDIATRIC_COMPLETE_CANONICAL_TOPIC|{topic}")
    for topic in remaining:
        print(f"PEDIATRIC_REMAINING_CANONICAL_TOPIC|{topic}")
    for topic, missing in incomplete:
        print(f"PEDIATRIC_INCOMPLETE_REVIEWED_TOPIC|{topic}|missing={','.join(missing)}")

    if len(topics) != 40:
        raise AssertionError(f"Expected 40 canonical Pediatric topics, found {len(topics)}")


if __name__ == "__main__":
    main()
