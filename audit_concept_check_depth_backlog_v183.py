"""v18.3 — deterministic post-completion Concept Check depth backlog audit.

All nine canonical learning-ladder domains are hard-gated complete.  The next safe
unit of work is therefore not a guessed topic alias: it is the weakest reviewed
Concept Check attached to a live canonical Deep Curriculum ID.

This audit is intentionally read-only.  It:
- rebuilds the canonical ID inventory from DEEP_MODULES_V6 + _v6_item_id;
- rejects duplicate Concept Check IDs and reviewed canonical-link orphans;
- excludes the already hand-deepened v18.0-v18.2 cohorts;
- considers only reviewed free-response reveals whose answers remain <75 words;
- ranks candidates deterministically by resident/chief clinical priority, then
  answer depth, prompt depth, canonical ID, and question ID;
- writes the exact current prompt/answer/canonical module material to an artifact
  so the next content patch can reuse strong material before adding anything.

The ranking never manufactures aliases and never mutates runtime content.
"""

from collections import Counter
import json
import re

import runtime_entry
from concept_check_board_repair_v177 import _find_module


data = runtime_entry.data

DEEPENED_MARKERS = (
    "task_alignment_v180",
    "task_alignment_v181",
    "task_alignment_v182",
)

# Stable clinical-priority terms.  They score the exact live canonical topic and
# prompt; they do not resolve aliases or substitute for concept_id linkage.
PRIORITY_GROUPS = (
    (5, ("airway", "hemorrhage", "bleed", "hematoma", "carotid", "epistaxis", "foreign body", "deep neck", "abscess")),
    (4, ("complication", "postoperative", "post-op", "rescue", "emergency", "escalat", "unstable", "aspiration")),
    (3, ("surgery", "operative", "operation", "resection", "dissection", "laryngoscopy", "cordotomy", "arytenoid", "flap", "skull base", "sphenoid", "parathyroid")),
    (2, ("physiology", "nerve", "vascular", "anatom", "staging", "margin", "radiation", "chemotherapy", "systemic therapy")),
    (1, ("management", "treatment", "workup", "diagnostic", "imaging", "surveillance")),
)


def _words(value):
    return len(re.findall(r"\b\w+[\w'-]*\b", str(value or "")))


def _prompt(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()


def _answer(q):
    return str(q.get("answer_text") or q.get("model_answer") or q.get("correct_answer") or "").strip()


def _priority(topic, prompt):
    haystack = f"{topic} {prompt}".lower()
    score = 0
    hits = []
    for weight, terms in PRIORITY_GROUPS:
        group_hits = [term for term in terms if term in haystack]
        if group_hits:
            score += weight
            hits.extend(group_hits)
    return score, sorted(set(hits))


def main():
    checks = list(data.CONCEPT_CHECKS_V112)
    failures = []
    ids = Counter(str(q.get("id") or "") for q in checks)

    for qid, count in ids.items():
        if not qid:
            failures.append("missing_concept_check_id")
        elif count > 1:
            failures.append(f"duplicate_concept_check_id:{qid}:count={count}")

    canonical = {}
    duplicate_canonical_ids = []
    for domain, modules in data.DEEP_MODULES_V6.items():
        for module in modules:
            topic = str(module.get("topic") or "").strip()
            if not topic:
                continue
            cid = data._v6_item_id(domain, topic)
            if cid in canonical:
                duplicate_canonical_ids.append(cid)
            canonical[cid] = {"domain": domain, "topic": topic, "module": module}
    if duplicate_canonical_ids:
        failures.extend(f"duplicate_canonical_id:{cid}" for cid in sorted(set(duplicate_canonical_ids)))

    candidates = []
    reviewed_free_response = 0
    excluded_deepened = 0

    for q in checks:
        qid = str(q.get("id") or "")
        if not q.get("reviewed_all_domains_v178"):
            continue

        # Resolve with the production canonical resolver first, then insist that
        # persisted concept_id agrees with the exact live canonical target.
        module = _find_module(q, data.DEEP_MODULES_V6, data._v6_item_id)
        if not module:
            failures.append(f"reviewed_orphan:{qid}:no_canonical_module")
            continue
        domain = str(q.get("domain") or "")
        topic = str(module.get("topic") or "")
        expected_cid = data._v6_item_id(domain, topic)
        persisted_cid = q.get("concept_id")
        if persisted_cid is not None and persisted_cid != expected_cid:
            failures.append(f"canonical_link_mismatch:{qid}:{persisted_cid!r}!={expected_cid!r}")
            continue
        if expected_cid not in canonical:
            failures.append(f"reviewed_orphan:{qid}:expected_id_not_live:{expected_cid}")
            continue

        if q.get("choices"):
            continue
        answer = _answer(q)
        if not answer:
            continue
        reviewed_free_response += 1
        if any(q.get(marker) for marker in DEEPENED_MARKERS):
            excluded_deepened += 1
            continue
        answer_words = _words(answer)
        if answer_words >= 75:
            continue

        prompt = _prompt(q)
        priority_score, priority_hits = _priority(topic, prompt)
        canonical_module = canonical[expected_cid]["module"]
        candidates.append({
            "id": qid,
            "concept_id": expected_cid,
            "domain": domain,
            "canonical_topic": topic,
            "board_dimension": q.get("board_dimension_v178"),
            "prompt_words": _words(prompt),
            "answer_words": answer_words,
            "priority_score": priority_score,
            "priority_hits": priority_hits,
            "prompt": prompt,
            "answer_text": answer,
            "explanation": q.get("explanation"),
            "board_pearl": q.get("board_pearl"),
            "review_basis": q.get("review_basis_v178"),
            "canonical_layers": {
                key: canonical_module.get(key)
                for key in ("recognize", "localize", "workup", "manage", "operate", "teach", "source_basis")
                if canonical_module.get(key) is not None
            },
        })

    candidates.sort(key=lambda row: (
        -row["priority_score"],
        row["answer_words"],
        row["prompt_words"],
        row["concept_id"],
        row["id"],
    ))
    for rank, row in enumerate(candidates, 1):
        row["rank"] = rank

    report = {
        "canonical_count": len(canonical),
        "concept_check_count": len(checks),
        "reviewed_free_response_count": reviewed_free_response,
        "excluded_v180_v182_count": excluded_deepened,
        "candidate_count": len(candidates),
        "selection_contract": "exact live canonical concept_id; priority desc; answer words asc; prompt words asc; concept_id; question id",
        "failures": failures,
        "candidates": candidates,
    }
    with open("V183_DEPTH_BACKLOG_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V183_CANONICAL|{len(canonical)}")
    print(f"V183_CONCEPT_CHECKS|{len(checks)}")
    print(f"V183_REVIEWED_FREE_RESPONSE|{reviewed_free_response}")
    print(f"V183_EXCLUDED_ALREADY_DEEPENED|{excluded_deepened}")
    print(f"V183_CANDIDATES_UNDER_75_WORDS|{len(candidates)}")
    for row in candidates[:12]:
        print(
            "V183_CANDIDATE|{rank}|priority={priority_score}|answer={answer_words}|prompt={prompt_words}|{domain}|{canonical_topic}|{id}|{concept_id}".format(**row)
        )
        print("V183_EXISTING_ANSWER|" + row["id"] + "|" + " ".join(row["answer_text"].split()))
    print(f"V183_FAILURES|{len(failures)}")
    for failure in failures[:200]:
        print("FAIL|" + failure)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
