"""v17.8 — hard all-domain Concept Check curation audit."""

from collections import Counter
import json
import re

import runtime_entry


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


def text(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "")


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
    item_rows = []

    if result.get("unresolved"):
        failures.append("runtime_unresolved=" + ",".join(str(x) for x in result["unresolved"]))

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
        if "?" not in prompt or not CLINICAL.search(prompt):
            fail("not_clinical_board_stem")
        if not answer_present(q):
            fail("missing_reveal_answer")
        if not str(q.get("explanation") or "").strip():
            fail("missing_explanation")
        if not q.get("review_basis_v178"):
            fail("missing_review_basis")

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
    print(f"V178_FAILURES|{len(failures)}")
    for f in failures[:200]:
        print("FAIL|" + f)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
