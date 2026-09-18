"""v37.4: vestibular schwannoma practical grading and treatment selection.
Reference: EANO vestibular schwannoma guideline, Neuro-Oncology 2020;22:31-45.
https://pmc.ncbi.nlm.nih.gov/articles/PMC6954440/
"""

TOPIC = "Vestibular Schwannoma"
WORKUP_ADDENDUM = (
    " GRADING FOR DOCUMENTATION AND COMPARISON: Koos I = intracanalicular; II = CPA extension "
    "without brainstem contact; III = occupies the CPA cistern without brainstem displacement; "
    "IV = brainstem/cranial-nerve displacement, often with compression or hydrocephalus. "
    "AAO-HNS hearing classes use pure-tone average (PTA) and speech discrimination/word recognition: "
    "A = PTA <=30 dB and score >=70%; B = PTA 31-50 dB and score >=50%; "
    "C = PTA >50 dB and score >=50%; D = score <50%. A/B are generally serviceable. "
    "Measure tumor diameter on comparable contrast MRI sequences and monitor serial audiograms; "
    "reproducible growth around >=2 mm on serial imaging or meaningful hearing decline warrants "
    "reconsideration of observation, but no single annual growth threshold automatically mandates "
    "treatment. Account for measurement error, interval, symptoms, age and tumor volume."
)
MANAGE_ADDENDUM = (
    " SIZE-DRIVEN DEFAULTS: observation with serial MRI and audiometry is reasonable for "
    "small asymptomatic Koos I-II tumors; SRS is an alternative for selected small/medium "
    "growing or symptomatic tumors without significant mass effect. Contemporary single-fraction "
    "SRS marginal doses are commonly 11-14 Gy (often 12-13 Gy); selected series report about "
    "90-99% five-year tumor control and 95-100% facial-nerve preservation, while hearing "
    "preservation varies substantially with baseline hearing, size, cochlear dose and follow-up. "
    "Large tumors causing substantial brainstem compression or hydrocephalus generally require "
    "microsurgical decompression; an intentionally retained remnant may be observed or treated "
    "with subsequent SRS. Koos grade or a 2.5-cm cutoff alone is not a treatment mandate. "
    "NF2-related schwannomatosis requires multidisciplinary bilateral-hearing planning; "
    "bevacizumab is an option in selected progressive NF2-related tumors."
)
OPERATE_ADDENDUM = (
    " APPROACH SELECTION BY HEARING AND EXTENT: middle fossa is a hearing-preservation "
    "option chiefly for appropriately selected small intracanalicular tumors with good "
    "preoperative hearing; retrosigmoid may permit hearing preservation in selected small "
    "CPA tumors. Translabyrinthine surgery sacrifices hearing, offers broad IAC exposure, "
    "and is appropriate when ipsilateral hearing is nonserviceable or preservation is not "
    "a realistic goal. Tumor anatomy, fundal extension, brainstem effect, facial-nerve "
    "course and team experience, not Koos class alone, determine approach."
)


def apply_vestibular_schwannoma_criteria_v374(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            if module.get("topic") != TOPIC:
                continue
            for field, marker, addition in (
                ("workup", "GRADING FOR DOCUMENTATION AND COMPARISON", WORKUP_ADDENDUM),
                ("manage", "SIZE-DRIVEN DEFAULTS", MANAGE_ADDENDUM),
                ("operate", "APPROACH SELECTION BY HEARING AND EXTENT", OPERATE_ADDENDUM),
            ):
                current = module.get(field, "") or ""
                if marker not in current:
                    module[field] = current.rstrip() + addition
            tags = module.setdefault("tags", [])
            for tag in ("Koos grade", "AAO-HNS hearing class", "serviceable hearing", "SRS marginal dose", "serial MRI growth"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(TOPIC)
    if not patched:
        raise RuntimeError("v37.4: could not find the canonical Vestibular Schwannoma topic")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
