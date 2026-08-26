"""v17.8 — hard all-domain Concept Check curation audit."""

from collections import Counter
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

    if result.get("unresolved"):
        failures.append("runtime_unresolved=" + ",".join(str(x) for x in result["unresolved"]))

    for q in checks:
        qid = q.get("id")
        domain = q.get("domain")
        domains[domain] += 1
        prompt = text(q)

        if not q.get("reviewed_all_domains_v178"):
            failures.append(f"{qid}:not_reviewed_v178")
        if domain not in EXPECTED_DOMAINS:
            failures.append(f"{qid}:unknown_domain:{domain}")
        if "?" not in prompt or not CLINICAL.search(prompt):
            failures.append(f"{qid}:not_clinical_board_stem")
        if not answer_present(q):
            failures.append(f"{qid}:missing_reveal_answer")
        if not str(q.get("explanation") or "").strip():
            failures.append(f"{qid}:missing_explanation")
        if not q.get("review_basis_v178"):
            failures.append(f"{qid}:missing_review_basis")

        choices = list(q.get("choices") or [])
        if choices:
            if len(choices) != 4:
                failures.append(f"{qid}:mcq_not_four_choices")
            why = list(q.get("why_wrong") or [])
            if len(why) != len(choices):
                failures.append(f"{qid}:why_wrong_misaligned")
            try:
                a = int(q.get("answer"))
            except (TypeError, ValueError):
                a = -1
            for i, reason in enumerate(why):
                if i != a and len(str(reason).split()) < 5:
                    failures.append(f"{qid}:weak_why_wrong:{i}")

        if str(q.get("curveball") or "").strip() and not str(q.get("curveball_answer") or "").strip():
            failures.append(f"{qid}:curveball_without_answer")

    missing_domains = EXPECTED_DOMAINS - set(domains)
    if missing_domains:
        failures.append("missing_domains=" + ",".join(sorted(missing_domains)))

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
