"""v24.7 — exact remaining Pediatric Otolaryngology ladder inventory.

This derives progress from the live canonical DEEP_MODULES_V6 registry and runtime
concept-id linkage, using the same deliberate review/stage contract as the all-domain
ladder inventory. It emits both completed and remaining canonical topic names so CI
logs are the source of truth for the next curation batch rather than aliases or stale
hand-maintained inventories.

A deliberately reviewed topic is not allowed to be partially staged: once review is
claimed, foundation, application, and senior_decision must all remain present.
"""
from collections import defaultdict
import runtime_entry as rt

DOMAIN = "Pediatric Otolaryngology"
STAGES = {"foundation", "application", "senior_decision"}


def main():
    data = rt.data
    modules = data.DEEP_MODULES_V6.get(DOMAIN, [])
    topics = [m.get("topic") for m in modules if m.get("topic")]

    if len(topics) != 40:
        raise AssertionError(f"Expected 40 canonical Pediatric topics, found {len(topics)}")
    if len(set(topics)) != len(topics):
        raise AssertionError("Duplicate canonical Pediatric topic names detected in DEEP_MODULES_V6")

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
        reviewed = [q for q in linked if q.get("ladder_reviewed")]
        stages = {q.get("learning_stage") for q in reviewed if q.get("learning_stage") in STAGES}
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

    if incomplete:
        details = "; ".join(f"{topic}: missing {','.join(missing)}" for topic, missing in incomplete)
        raise AssertionError(f"Partially reviewed Pediatric ladders are not allowed: {details}")
    if len(complete) + len(remaining) != len(topics):
        raise AssertionError("Pediatric inventory accounting mismatch")


if __name__ == "__main__":
    main()
