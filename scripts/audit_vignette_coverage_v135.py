"""ENT Mastery canonical vignette coverage + depth audit.

Reports exact per-domain coverage against the live runtime curriculum after all
runtime patches have been applied. Integrity defects (orphans, duplicate IDs,
malformed cases) fail the process. It also reports a depth proxy: canonical
topics with at least two independently linked vignettes. This is intentionally
separate from the 100% canonical-coverage milestone so shallow one-case topics
remain visible for the board/call/OR depth pass.
"""
from collections import Counter, defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import wsgi


data = wsgi.data


def main():
    modules = data.DEEP_MODULES_V6
    cases = data.CLINICAL_CHALLENGES_V119

    canonical_by_domain = {
        domain: {m.get("topic") for m in topic_list if m.get("topic")}
        for domain, topic_list in modules.items()
    }
    canonical_ids = {
        data._v6_item_id(domain, topic): (domain, topic)
        for domain, topics in canonical_by_domain.items()
        for topic in topics
    }
    covered_ids = {q.get("concept_id") for q in cases if q.get("concept_id")}

    by_concept = defaultdict(list)
    for q in cases:
        by_concept[q.get("concept_id")].append(q)

    print("=== ENT MASTERY CANONICAL VIGNETTE COVERAGE + DEPTH ===")
    print(f"Total curriculum topics: {sum(len(x) for x in canonical_by_domain.values())}")
    print(f"Total vignettes: {len(cases)}")
    print()

    total_topics = 0
    total_covered = 0
    total_depth2 = 0
    missing_all = []
    singleton = []
    for domain, topics in canonical_by_domain.items():
        covered = sorted(t for t in topics if data._v6_item_id(domain, t) in covered_ids)
        missing = sorted(topics - set(covered))
        depth2 = sorted(
            t for t in topics
            if len(by_concept.get(data._v6_item_id(domain, t), [])) >= 2
        )
        domain_singletons = sorted(
            t for t in topics
            if len(by_concept.get(data._v6_item_id(domain, t), [])) == 1
        )
        total_topics += len(topics)
        total_covered += len(covered)
        total_depth2 += len(depth2)
        pct = 100.0 * len(covered) / len(topics) if topics else 100.0
        depth_pct = 100.0 * len(depth2) / len(topics) if topics else 100.0
        print(f"DOMAIN|{domain}|{len(covered)}|{len(topics)}|{pct:.1f}%")
        print(f"DEPTH2_DOMAIN|{domain}|{len(depth2)}|{len(topics)}|{depth_pct:.1f}%")
        for topic in missing:
            print(f"MISSING|{domain}|{topic}")
            missing_all.append((domain, topic))
        singleton.extend((domain, topic) for topic in domain_singletons)

    print()
    overall = 100.0 * total_covered / total_topics if total_topics else 100.0
    depth_overall = 100.0 * total_depth2 / total_topics if total_topics else 100.0
    print(f"OVERALL|{total_covered}|{total_topics}|{overall:.1f}%")
    print(f"DEPTH2_OVERALL|{total_depth2}|{total_topics}|{depth_overall:.1f}%")
    print(f"MISSING_TOTAL|{len(missing_all)}")

    ids = [q.get("id") for q in cases]
    duplicate_ids = sorted(k for k, n in Counter(ids).items() if k and n > 1)
    orphaned = [q for q in cases if q.get("concept_id") not in canonical_ids]
    malformed = []
    required = ("id", "domain", "topic", "stem", "choices", "answer", "explanation")
    for q in cases:
        absent = [k for k in required if q.get(k) is None]
        choices = q.get("choices") or []
        answer = q.get("answer")
        if absent or not isinstance(choices, list) or len(choices) < 2 or not isinstance(answer, int) or not (0 <= answer < len(choices)):
            malformed.append((q.get("id"), absent))

    print(f"ORPHANED|{len(orphaned)}")
    for q in orphaned:
        print(f"ORPHAN|{q.get('id')}|{q.get('domain')}|{q.get('topic')}|{q.get('concept_id')}")
    print(f"DUPLICATE_IDS|{len(duplicate_ids)}")
    for qid in duplicate_ids:
        print(f"DUPLICATE|{qid}")
    print(f"MALFORMED|{len(malformed)}")
    for qid, absent in malformed:
        print(f"BAD_SCHEMA|{qid}|missing={','.join(absent)}")

    print(f"SINGLETON_TOPICS|{len(singleton)}")
    for domain, topic in sorted(singleton):
        print(f"SINGLETON|{domain}|{topic}")

    # Focus-tag visibility for second-pass call/OR content. Older cases predate
    # the field, so zero here means "not explicitly tagged," not necessarily
    # absent content; this guides future curation rather than acting as failure.
    focus_counts = Counter(q.get("focus") for q in cases if q.get("focus"))
    for focus, count in sorted(focus_counts.items()):
        print(f"FOCUS|{focus}|{count}")

    if orphaned or duplicate_ids or malformed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
