"""v21.9 — preserve rationale alignment when reusing an upstream-shuffled case."""

REASONS = {
    "HPV-associated OPSCC uses a distinct prognostic staging system, but treatment still depends on anatomic extent and multidisciplinary modality selection":
        "Correct. HPV-associated OPSCC has distinct prognostic staging, but treatment still follows anatomic extent, function, and evidence-based modality selection.",
    "p16 positivity means no treatment is needed":
        "p16 positivity improves prognosis but does not make an invasive nodal cancer safe to observe.",
    "All patients require total laryngectomy":
        "Total laryngectomy is not a routine treatment for a small oropharyngeal primary.",
    "Cystic nodes are benign by definition":
        "Cystic level-II nodes in an adult can be a classic presentation of HPV-associated oropharyngeal metastasis rather than benign disease.",
}


def apply_ladder_reuse_alignment_v219(challenges):
    for q in challenges:
        if q.get("id") != "v143_hno_02":
            continue
        choices = list(q.get("choices") or [])
        q["why_wrong"] = [REASONS.get(str(choice), "This choice does not match the oncologic staging and treatment principle in the case.") for choice in choices]
        return {"repaired": q["id"], "answer": q.get("answer")}
    raise RuntimeError("v21.9: reused HPV application case v143_hno_02 missing")
