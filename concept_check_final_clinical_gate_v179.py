"""Final clinical-stem normalization plus exact-live Rhinology successor alignment.

The validated v20.30 implementation remains the complete predecessor. Later bounded successors add
learner-experience repairs without changing Deep Curriculum identities: AR/LAR, Unilateral Sinonasal
Disease, Facial Pain / Headache vs Rhinogenic Disease, Systemic Disease of the Nose / Sinuses, and the
paired CSF Rhinorrhea -> Endoscopic CSF Leak Repair pathway receive exact-canonical resident-facing
Concept Checks after inherited normalization has completed.
"""
import concept_check_final_clinical_gate_v179_source_v228 as _base
from concept_check_final_clinical_gate_v179_source_v228 import *
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v229 import apply_concept_check_task_alignment_v229
from concept_check_depth_v230 import apply_concept_check_task_alignment_v230
from concept_check_rhinology_allergy_v231 import apply_rhinology_allergy_concept_checks_v231
from concept_check_rhinology_unilateral_v232 import (
    SOURCE_REFS as UNILATERAL_SOURCE_REFS_V232,
    apply_rhinology_unilateral_concept_check_v232,
)
from concept_check_rhinology_facial_pain_v233 import apply_rhinology_facial_pain_concept_check_v233
from concept_check_rhinology_systemic_v234 import apply_rhinology_systemic_concept_check_v234
from concept_check_rhinology_csf_leak_v235 import apply_rhinology_csf_leak_concept_checks_v235


_V231_ALLERGY_QIDS = {
    "cc-v231-rhinology-allergic-rhinitis-ar",
    "cc-v231-rhinology-local-allergic-rhinitis-lar",
}


def _reassert_onb_search_aliases_v230(checks, deep_modules, v6_item_id):
    qid = "cc-v112-rec-rhinology-allergy-skull-base-sinonasal-malignancy"
    q = next((x for x in checks if str(x.get("id") or "") == qid), None)
    module = _find_module(q, deep_modules, v6_item_id) if q else None
    if not module:
        return False
    addition = (
        "ONB terminology: esthesioneuroblastoma and olfactory neuroblastoma are synonyms for the "
        "same olfactory-neuroepithelial malignancy; the historical alias esthesioblastoma may also "
        "appear in older literature and should resolve to this same canonical topic."
    )
    current = str(module.get("recognize") or "")
    if "esthesioblastoma" not in current.lower():
        module["recognize"] = (current.rstrip() + ("\n\n" if current.strip() else "") + addition).strip()
    return True


def _curate_new_allergy_checks_v231(checks):
    normalized = []
    for q in checks or []:
        qid = str(q.get("id") or "")
        if qid not in _V231_ALLERGY_QIDS:
            continue
        q["reviewed_all_domains_v178"] = True
        q["review_basis_v178"] = (
            "Dedicated v20.31 Rhinology learner-path repair; exact live canonical linkage, clinical "
            "board-style stem, visible reveal answer, source-grounded management, and Deep-to-Daily "
            "continuity reviewed against the same all-domain curation contract."
        )
        if not str(q.get("explanation") or "").strip():
            q["explanation"] = str(q.get("answer_text") or "").strip()
        q["curated_v177"] = True
        q["converted_to_oral_board_v178"] = True
        normalized.append(qid)
    return normalized


def _reassert_unilateral_visible_sources_v232(checks, deep_modules, v6_item_id):
    repaired = []
    for q in checks or []:
        if str(q.get("domain") or "") != "Rhinology / Allergy / Skull Base":
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        if not module or str(module.get("topic") or "") != "Unilateral Sinonasal Disease":
            continue
        refs = list(q.get("source_refs_v230") or [])
        existing = {str(ref.get("citation") or "").strip().lower() for ref in refs if isinstance(ref, dict)}
        changed = False
        for ref in UNILATERAL_SOURCE_REFS_V232:
            citation = str(ref.get("citation") or "").strip().lower()
            if citation and citation not in existing:
                refs.append(dict(ref))
                existing.add(citation)
                changed = True
        if changed:
            q["source_refs_v230"] = refs
            repaired.append(str(q.get("id") or ""))
    return repaired


def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    results = _base.apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id)
    alignment_v229 = apply_concept_check_task_alignment_v229(checks, deep_modules, v6_item_id)
    results["task_alignment_v229"] = alignment_v229
    results["post_alignment_reframed_v229"] = _base._reassert_clinical_contract(
        checks, alignment_v229.get("repaired", []), results.get("unresolved", []), "post_alignment_clinical_frame_v229"
    )
    alignment_v230 = apply_concept_check_task_alignment_v230(checks, deep_modules, v6_item_id)
    results["task_alignment_v230"] = alignment_v230
    results["post_alignment_reframed_v230"] = _base._reassert_clinical_contract(
        checks, alignment_v230.get("repaired", []), results.get("unresolved", []), "post_alignment_clinical_frame_v230"
    )
    results["onb_search_aliases_v230"] = _reassert_onb_search_aliases_v230(checks, deep_modules, v6_item_id)
    results["rhinology_allergy_concept_checks_v231"] = apply_rhinology_allergy_concept_checks_v231(checks, deep_modules, v6_item_id)
    results["rhinology_allergy_curation_v231"] = _curate_new_allergy_checks_v231(checks)
    results["rhinology_unilateral_concept_check_v232"] = apply_rhinology_unilateral_concept_check_v232(checks, deep_modules, v6_item_id)
    results["rhinology_unilateral_visible_sources_v232"] = _reassert_unilateral_visible_sources_v232(checks, deep_modules, v6_item_id)
    results["rhinology_facial_pain_concept_check_v233"] = apply_rhinology_facial_pain_concept_check_v233(checks, deep_modules, v6_item_id)
    results["rhinology_systemic_concept_check_v234"] = apply_rhinology_systemic_concept_check_v234(checks, deep_modules, v6_item_id)
    results["rhinology_csf_leak_concept_checks_v235"] = apply_rhinology_csf_leak_concept_checks_v235(checks, deep_modules, v6_item_id)
    return results
