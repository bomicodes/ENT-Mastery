"""v19.7 — deepen the exact live Tumor Immunology / Immunotherapy in HNSCC Concept Check.

This cohort targets a clinically high-yield oncology decision gap rather than lexical
backlog rank. It updates the check for the current perioperative pembrolizumab
indication and teaches treatment-setting, CPS, response-urgency, local-therapy and
immune-toxicity boundaries instead of treating checkpoint inhibition as a generic
biomarker fact.
"""

from concept_check_board_repair_v177 import _find_module

COHORT = {
    "cc-v112-rec-head-neck-oncology-tumor-immunology-immunotherapy-in-hnscc": {
        "concept_id": "v6-head-neck-oncology-tumor-immunology-immunotherapy-in-hnscc",
        "canonical_topic": "Tumor Immunology / Immunotherapy in HNSCC",
        "prompt": (
            "A 61-year-old patient with HNSCC is reviewed at multidisciplinary tumor board. The team is considering "
            "checkpoint inhibition, but the correct role depends on whether disease is newly diagnosed and resectable, "
            "recurrent/metastatic and incurable with local therapy, or progressing after prior platinum exposure. How should "
            "PD-L1 CPS, resectability, disease tempo, prior treatment, performance status, and immune-related risk change the "
            "systemic plan, and which findings should prevent the team from using immunotherapy as a substitute for urgent "
            "airway control, definitive local therapy, or treatment of immediately threatening disease?"
        ),
        "answer_text": (
            "Start by defining the treatment setting before interpreting a biomarker. Checkpoint inhibition is not one generic "
            "HNSCC treatment. Confirm histology and stage, HPV/p16 status when appropriate, sites and burden of disease, prior "
            "platinum and radiation exposure, performance status, organ function, symptoms, resectability, and whether salvage "
            "surgery or radiation could still provide meaningful local control. Obtain PD-L1 testing reported as combined "
            "positive score (CPS) when it is relevant to regimen selection, but do not let CPS replace the clinical assessment.\n\n"
            "For recurrent or metastatic HNSCC that is not curable with local therapy, pembrolizumab-based first-line therapy is "
            "selected according to the approved clinical setting, PD-L1 expression, disease tempo, comorbidity and the need for "
            "rapid cytoreduction. Pembrolizumab monotherapy is an important option for PD-L1-positive disease when a slower "
            "response trajectory is clinically acceptable and avoiding chemotherapy toxicity matters. When tumor burden is high, "
            "symptoms are substantial, or a faster and more reliable response is needed, pembrolizumab plus platinum-based "
            "chemotherapy is generally favored over choosing monotherapy simply because CPS is positive. Prior platinum exposure, "
            "timing of recurrence and prior checkpoint therapy also change subsequent-line choices; do not recycle a first-line "
            "algorithm without reviewing what the patient has already received.\n\n"
            "For newly diagnosed resectable locally advanced HNSCC, immunotherapy must be integrated with—not substituted for—" 
            "definitive surgery and pathology-directed adjuvant treatment. A current perioperative pembrolizumab pathway exists "
            "for appropriately selected adults with PD-L1 CPS at least 1: neoadjuvant pembrolizumab is followed by surgery, then "
            "adjuvant pembrolizumab with radiation with or without cisplatin according to pathologic risk, followed by pembrolizumab "
            "maintenance. Positive margins and extranodal extension still matter because they drive the need for concurrent "
            "cisplatin with postoperative radiation when the patient is eligible. The senior mistake is to hear 'immunotherapy' "
            "and relax the surgical margin, neck-management, or adjuvant-risk framework.\n\n"
            "Before treatment, screen for factors that may make immune checkpoint therapy hazardous or require specialist input, "
            "including active or severe autoimmune disease, solid-organ transplant, prior serious immune-related toxicity, and "
            "other major comorbidity. During therapy, new diarrhea, hepatitis, pneumonitis, endocrinopathy, nephritis, severe rash, "
            "neurologic symptoms, or myocarditis-type symptoms should trigger an immune-related adverse-event evaluation rather "
            "than being dismissed as routine chemotherapy toxicity. Significant suspected immune toxicity may require holding "
            "checkpoint therapy and prompt organ-specific workup and immunosuppression according to severity.\n\n"
            "Finally, immunotherapy does not rescue an unstable airway or an immediately threatening local problem on the timetable "
            "of an emergency. Stridor, impending obstruction, major hemorrhage, threatened carotid involvement, spinal or cranial "
            "neurologic compromise, uncontrolled infection, or rapidly progressive symptomatic disease demands immediate airway, "
            "procedural, radiation, surgical, or other multidisciplinary stabilization as appropriate. Likewise, a technically "
            "resectable recurrence with a meaningful chance of salvage should not be declared systemic-only merely because a "
            "checkpoint agent is available. The senior decision is to match immunotherapy to the disease setting while preserving "
            "curative local options and recognizing problems that cannot safely wait for a systemic response."
        ),
        "explanation": (
            "Board-level immunotherapy questions are treatment-setting questions first and biomarker questions second. PD-L1 CPS "
            "helps select pembrolizumab strategies, but response urgency, prior therapy, resectability and immune-toxicity risk can "
            "change the plan. Current perioperative pembrolizumab is additive to definitive surgery and risk-adapted adjuvant "
            "therapy; it does not erase margin, ENE, airway, hemorrhage or salvage-local-therapy decisions."
        ),
        "board_pearl": (
            "Name the disease setting before naming the checkpoint regimen. A positive CPS supports selection; it does not make "
            "an unstable airway wait, turn resectable disease into systemic-only disease, or replace pathology-directed adjuvant therapy."
        ),
        "depth_layers_v197": {
            "foundation": (
                "PD-1 blockade restores antitumor immune activity, while PD-L1 CPS is a predictive treatment-selection biomarker "
                "rather than a staging system or a stand-alone measure of resectability."
            ),
            "application": (
                "Separate curative local disease from incurable recurrent/metastatic disease, then integrate CPS, prior platinum, "
                "disease tempo, response urgency, performance status and immune-related risk to choose an appropriate systemic pathway."
            ),
            "senior_decision": (
                "Preserve urgent airway/hemorrhage rescue and curative surgery or radiation when indicated; use perioperative "
                "pembrolizumab only as part of the definitive multimodality pathway, and recognize immune toxicity early enough "
                "to hold treatment and escalate workup when clinically significant."
            ),
        },
        "common_traps_v197": [
            (
                "Treating any CPS-positive recurrent/metastatic tumor with pembrolizumab monotherapy without considering response "
                "urgency. A patient with bulky, rapidly progressive, symptomatic disease may need a combination strategy because "
                "the practical need for cytoreduction matters in addition to biomarker eligibility."
            ),
            (
                "Using perioperative checkpoint therapy as permission to de-intensify definitive local treatment. The approved "
                "perioperative pathway still includes surgery and pathology-directed postoperative radiation, with concurrent "
                "cisplatin when high-risk features such as positive margin or extranodal extension warrant it and the patient is eligible."
            ),
            (
                "Calling an airway-threatening or hemorrhagic tumor an 'immunotherapy problem.' Checkpoint response is not an "
                "emergency airway maneuver or hemostatic procedure; stabilize the immediate threat first while the multidisciplinary "
                "team defines definitive local and systemic treatment."
            ),
            (
                "Mistaking immune-related toxicity for ordinary treatment fatigue or infection without targeted evaluation. New "
                "pulmonary, gastrointestinal, hepatic, endocrine, renal, cardiac, dermatologic or neurologic syndromes can represent "
                "immune toxicity and may require prompt treatment interruption and severity-based immunosuppression."
            ),
        ],
        "deliberate_review_v197": (
            "High-yield Head & Neck Oncology concept selected from the live v19.6 canonical backlog because its 35-word answer "
            "did not distinguish recurrent/metastatic treatment selection from the now-approved perioperative pembrolizumab pathway "
            "and did not teach response-urgency, local-salvage, emergency or immune-toxicity boundaries."
        ),
    },
}


def apply_concept_check_task_alignment_v197(checks, deep_modules, v6_item_id):
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, payload in COHORT.items():
        q = by_id.get(qid)
        if q is None:
            missing.append(qid); continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        concept_id = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if module is None or topic != payload["canonical_topic"] or concept_id != payload["concept_id"] or q.get("concept_id") != concept_id:
            link_mismatch.append(qid); continue
        for field in ("prompt", "answer_text", "explanation", "board_pearl", "depth_layers_v197", "common_traps_v197", "deliberate_review_v197"):
            q[field] = payload[field]
        q["task_alignment_v197"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
