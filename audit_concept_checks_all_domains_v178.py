"""v17.8 — hard all-domain Concept Check curation audit.

Post-completion hardening: in addition to clinical-board quality, verify that every
reviewed Concept Check resolves back to the live canonical Deep Curriculum and
that any persisted canonical_topic/concept_id agrees exactly with that live
canonical target. Duplicate Concept Check IDs are forbidden.

v20.6 teaching-alignment note: foundation/anatomy/physiology concepts may use the
explicit "clinical or operative context" teaching frame rather than an artificial
patient vignette. That exception is accepted only when the curation metadata marks
the item as a v20.6-aligned foundation concept; all other items still require the
original clinical-stem markers.
"""

from collections import Counter
import json
import re

import runtime_entry
from concept_check_board_repair_v177 import _find_module


data = runtime_entry.data
result = runtime_entry.CONCEPT_CHECK_DOMAIN_CURATION_V178

EXPECTED_DOMAINS = {
    "Otology / Neurotology",
    "Rhinology / Allergy / Skull Base",
    "Head & Neck Oncology",
    "Thyroid / Parathyroid / Salivary",
    "Pediatric Otolaryngology",
    "Laryngology / Voice / Swallowing",
    "Facial Plastics / Trauma",
    "Sleep Surgery",
    "General ENT / Emergencies",
}

CLINICAL = re.compile(
    r"\b(patient|child|infant|adult|man|woman|boy|girl|presents|returns|develops|"
    r"postoperative|exam|otoscopy|endoscopy|ct|mri|ultrasound|audiogram|psg)\b",
    re.I,
)

FOUNDATION_FRAME = "in the clinical or operative context of"


def text(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "")


def foundation_teaching_stem(q, prompt):
    return (
        q.get("teaching_aligned_v206") is True
        and q.get("concept_kind_v206") == "foundation"
        and FOUNDATION_FRAME in prompt.lower()
    )


def answer_present(q):
    if q.get("choices"):
        try:
            a = int(q.get("answer"))
        except (TypeError, ValueError):
            return False
        return 0 <= a < len(q["choices"])
    return bool(str(q.get("answer_text") or q.get("model_answer") or q.get("correct_answer") or "").strip())


def main():
    checks = list(data.CONCEPT_CHECKS_V112)
    failures = []
    domains = Counter()
    ids = Counter(str(q.get("id") or "") for q in checks)
    item_rows = []

    if result.get("unresolved"):
        failures.append("runtime_unresolved=" + ",".join(str(x) for x in result["unresolved"]))

    for qid, count in ids.items():
        if not qid:
            failures.append("missing_id")
        elif count > 1:
            failures.append(f"duplicate_id:{qid}:count={count}")

    canonical_topics = {
        domain: {m.get("topic") for m in modules if m.get("topic")}
        for domain, modules in data.DEEP_MODULES_V6.items()
    }

    for q in checks:
        qid = q.get("id")
        domain = q.get("domain")
        domains[domain] += 1
        prompt = text(q)
        item_failures = []

        def fail(reason):
            failures.append(f"{qid}:{reason}")
            item_failures.append(reason)

        if not q.get("reviewed_all_domains_v178"):
            fail("not_reviewed_v178")
        if domain not in EXPECTED_DOMAINS:
            fail(f"unknown_domain:{domain}")
        if "?" not in prompt or not (CLINICAL.search(prompt) or foundation_teaching_stem(q, prompt)):
            fail("not_clinical_board_stem")
        if not answer_present(q):
            fail("missing_reveal_answer")
        if not str(q.get("explanation") or "").strip():
            fail("missing_explanation")
        if not q.get("review_basis_v178"):
            fail("missing_review_basis")

        # Resolve through the same live canonical Deep Curriculum used by the
        # curation layer, then require all persisted linkage metadata to agree
        # exactly with that canonical target. This catches reviewed orphans and
        # stale aliases without guessing canonical IDs in the audit itself.
        module = _find_module(q, data.DEEP_MODULES_V6, data._v6_item_id)
        canonical_topic = module.get("topic") if module else None
        expected_cid = data._v6_item_id(domain, canonical_topic) if module and domain else None
        if not module or canonical_topic not in canonical_topics.get(domain, set()):
            fail("reviewed_orphan_no_canonical_module")
        else:
            persisted_topic = q.get("canonical_topic")
            persisted_cid = q.get("concept_id")
            if persisted_topic is not None and persisted_topic != canonical_topic:
                fail(f"canonical_topic_mismatch:{persisted_topic!r}!={canonical_topic!r}")
            if persisted_cid is not None and persisted_cid != expected_cid:
                fail(f"concept_id_mismatch:{persisted_cid!r}!={expected_cid!r}")

        choices = list(q.get("choices") or [])
        if choices:
            if len(choices) != 4:
                fail("mcq_not_four_choices")
            why = list(q.get("why_wrong") or [])
            if len(why) != len(choices):
                fail("why_wrong_misaligned")
            try:
                a = int(q.get("answer"))
            except (TypeError, ValueError):
                a = -1
            for i, reason in enumerate(why):
                if i != a and len(str(reason).split()) < 5:
                    fail(f"weak_why_wrong:{i}")

        if str(q.get("curveball") or "").strip() and not str(q.get("curveball_answer") or "").strip():
            fail("curveball_without_answer")

        item_rows.append({
            "id": qid,
            "domain": domain,
            "topic": q.get("topic"),
            "canonical_topic": canonical_topic,
            "concept_id": q.get("concept_id"),
            "expected_concept_id": expected_cid,
            "prompt": prompt,
            "choices": choices,
            "answer": q.get("answer"),
            "answer_text": q.get("answer_text"),
            "converted": bool(q.get("converted_to_oral_board_v178")),
            "curated": q.get("curated_v177"),
            "failures": item_failures,
        })

    missing_domains = EXPECTED_DOMAINS - set(domains)
    if missing_domains:
        failures.append("missing_domains=" + ",".join(sorted(missing_domains)))

    report = {
        "total": len(checks),
        "domains": dict(domains),
        "runtime_result": result,
        "duplicate_ids": {qid: n for qid, n in ids.items() if qid and n > 1},
        "failures": failures,
        "items": item_rows,
        "distinct_entities": getattr(runtime_entry, "DISTINCT_ENTITIES_V178", {}),
    }
    with open("V178_ALL_DOMAIN_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V178_TOTAL|{len(checks)}")
    for domain in sorted(domains):
        print(f"V178_DOMAIN|{domain}|{domains[domain]}")
    for k, v in sorted(result.get("stats", {}).items()):
        print(f"V178_STAT|{k}|{v}")
    print(f"V178_DUPLICATE_IDS|{sum(1 for qid, n in ids.items() if qid and n > 1)}")
    print(f"V178_FAILURES|{len(failures)}")
    for f in failures[:200]:
        print("FAIL|" + f)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
