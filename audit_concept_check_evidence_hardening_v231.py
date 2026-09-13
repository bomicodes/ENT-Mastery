"""Fail-closed evidence-hardening gate for the exact-live v20.31 cleft cohort."""
import runtime_entry

QID = "cc-v112-rec-pediatric-otolaryngology-cleft-craniofacial-otologic-airway-care"
REQUIRED_SOURCES = (
    "cummings",
    "pasha",
    "k.j. lee",
    "pmid 41930721",
    "pmid 42213516",
)
REQUIRED_EVIDENCE = (
    "durable textbook",
    "individualized rather than universal",
    "pmid 41930721",
    "pmid 42213516",
    "guideline-based",
)


def main():
    checks = list(runtime_entry.data.CONCEPT_CHECKS_V112)
    q = next((x for x in checks if str(x.get("id") or "") == QID), None)
    failures = []
    if q is None:
        failures.append("missing_exact_live_qid")
    else:
        refs = list(q.get("source_refs_v231") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in REQUIRED_SOURCES:
            if anchor not in reftext:
                failures.append("missing_source:" + anchor)
        evidence = str(q.get("evidence_distinction_v231") or "").lower()
        for anchor in REQUIRED_EVIDENCE:
            if anchor not in evidence:
                failures.append("missing_evidence_boundary:" + anchor)
        answer = str(q.get("answer_text") or "").lower()
        for anchor in ("tensor veli palatini tenopexy", "did not reduce ome", "otologic surveillance"):
            if anchor not in answer:
                failures.append("missing_answer_boundary:" + anchor)

    print("V231H_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.31 evidence hardening is live and traceable")


if __name__ == "__main__":
    main()
