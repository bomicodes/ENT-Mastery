"""v38.2: Replace two vague OR-prep indication fields with explicit criteria.

Clinical criteria updated against Fifth International Workshop (2022) PHPT
recommendations and AAO-HNSF 2019 pediatric tonsillectomy guideline.
Only replace exact preexisting placeholder text; preserve edited records.
"""

PARATHYROID_OLD = (
    "Biochemically confirmed primary hyperparathyroidism in an appropriate surgical "
    "candidate; apply symptom/end-organ/age criteria and shared decision-making."
)

PARATHYROID_NEW = (
    "Biochemically confirmed primary hyperparathyroidism: offer parathyroidectomy for "
    "symptomatic disease (e.g., nephrolithiasis or skeletal complications) if medically "
    "appropriate. For asymptomatic hypercalcemic PHPT, the 2022 Fifth International Workshop "
    "recommends surgery when ANY ONE criterion is present: serum calcium >1 mg/dL above "
    "the laboratory upper limit of normal; vertebral fracture on imaging or DXA T-score "
    "<=-2.5 at the lumbar spine, hip/femoral neck, or distal one-third radius; eGFR or "
    "creatinine clearance <60 mL/min; nephrolithiasis/nephrocalcinosis on imaging; "
    "24-hour urine calcium >250 mg/day in women or >300 mg/day in men; or age <50 years. "
    "The >400 mg/day urine calcium plus stone-risk-analysis criterion comes from an older "
    "workshop, not the 2022 guideline. Surgery may also be chosen with patient/clinician "
    "agreement when surveillance is not desired or feasible and no contraindication exists. "
    "Exclude familial hypocalciuric hypercalcemia when appropriate; recommendations for "
    "normocalcemic PHPT are less established."
)

PEDS_TONSIL_OLD = (
    "Appropriate recurrent throat infection or obstructive sleep-disordered "
    "breathing/OSA indications after guideline-based assessment, modifying factors, "
    "comorbidities, and shared decision-making."
)

PEDS_TONSIL_NEW = (
    "Recurrent throat infection: consider tonsillectomy for >=7 documented episodes in "
    "the preceding year, >=5/year in each of the preceding 2 years, or >=3/year in each "
    "of the preceding 3 years. Each qualifying episode should have sore throat plus "
    "at least one of temperature >38.3 C, cervical adenopathy, tonsillar exudate, or "
    "positive group A streptococcal testing. Below these frequencies, recommend watchful "
    "waiting unless modifying factors such as multiple antibiotic allergies/intolerance, "
    "PFAPA, or >1 peritonsillar abscess favor surgery. Obstructive indication: recommend "
    "tonsillectomy for children with OSA documented on overnight polysomnography; an AHI "
    ">=5 is NOT required as a universal surgical threshold (pediatric OSA can be present "
    "at obstructive AHI >=1). When PSG is unavailable in otherwise low-risk children, "
    "consider the clinical obstructive picture, tonsillar hypertrophy, comorbidities and "
    "shared decision-making. Obtain PSG before surgery for oSDB in children <2 years "
    "or with obesity, Down syndrome, craniofacial abnormalities, neuromuscular disorders, "
    "sickle cell disease, or mucopolysaccharidoses; advocate PSG when the indication is "
    "uncertain or history and examination disagree. Arrange overnight inpatient monitoring "
    "after tonsillectomy if age <3 or severe OSA (AHI >=10 or oxygen nadir <80%)."
)


def apply_or_prep_indications_fix_v382(registry):
    if not registry:
        raise RuntimeError("v38.2: OR_PREP_REGISTRY not found")

    patched = []
    skipped = []
    targets = (
        ("parathyroidectomy", PARATHYROID_OLD, PARATHYROID_NEW),
        ("tonsillectomy-adenoidectomy", PEDS_TONSIL_OLD, PEDS_TONSIL_NEW),
    )
    for slug, old_text, new_text in targets:
        entry = registry.get(slug)
        if entry is None:
            matches = [e for e in registry.values()
                       if (e.get("indications") or "").strip() == old_text.strip()]
            if len(matches) != 1:
                raise RuntimeError(
                    f"v38.2: expected one matching OR-prep entry for '{slug}', found {len(matches)}"
                )
            entry = matches[0]
        current = (entry.get("indications") or "").strip()
        if current == old_text.strip():
            entry["indications"] = new_text
            patched.append(entry.get("title", slug))
        elif current == new_text.strip():
            pass
        else:
            skipped.append(entry.get("title", slug))

    return {"patched": patched, "count": len(patched), "skipped_already_edited": skipped}
