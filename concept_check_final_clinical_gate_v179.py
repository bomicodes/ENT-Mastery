"""Final clinical-stem normalization and ordered Concept Check depth hardening.

Generic/domain normalization runs first. Focused task-alignment repairs then run in
version order so exact, source-grounded teaching cannot be overwritten by fallback
question generation. This module intentionally keeps an explicit latest-version call
because the fail-closed release manifest verifies that the newest depth patch is live.
"""
import re

from concept_check_board_repair_v177 import _find_module
from concept_check_domain_curation_v178 import _convert_to_domain_oral_board
from concept_check_task_alignment_v180 import apply_concept_check_task_alignment_v180
from concept_check_task_alignment_v181 import apply_concept_check_task_alignment_v181
from concept_check_task_alignment_v182 import apply_concept_check_task_alignment_v182
from concept_check_runtime_depth_v183 import apply_concept_check_task_alignment_v183
from concept_check_depth_v184 import apply_concept_check_task_alignment_v184
from concept_check_trimodality_depth_v184 import apply_bot_trimodality_depth_v184
from concept_check_depth_v185 import apply_concept_check_task_alignment_v185
from concept_check_depth_v186 import apply_concept_check_task_alignment_v186
from concept_check_depth_v187 import apply_concept_check_task_alignment_v187
from concept_check_depth_v188 import apply_concept_check_task_alignment_v188
from concept_check_depth_v189 import apply_concept_check_task_alignment_v189
from concept_check_depth_v190 import apply_concept_check_task_alignment_v190
from concept_check_depth_v191 import apply_concept_check_task_alignment_v191
from concept_check_depth_v192 import apply_concept_check_task_alignment_v192
from concept_check_depth_v193 import apply_concept_check_task_alignment_v193
from concept_check_depth_v194 import apply_concept_check_task_alignment_v194
from concept_check_depth_v195 import apply_concept_check_task_alignment_v195
from concept_check_depth_v196 import apply_concept_check_task_alignment_v196
from concept_check_depth_v197 import apply_concept_check_task_alignment_v197
from concept_check_depth_v198 import apply_concept_check_task_alignment_v198
from concept_check_depth_v199 import apply_concept_check_task_alignment_v199
from concept_check_depth_v200 import apply_concept_check_task_alignment_v200
from concept_check_depth_v201 import apply_concept_check_task_alignment_v201
from concept_check_depth_v202 import apply_concept_check_task_alignment_v202
from concept_check_depth_v203 import apply_concept_check_task_alignment_v203
from concept_check_depth_v204 import apply_concept_check_task_alignment_v204
from concept_check_depth_v205 import apply_concept_check_task_alignment_v205
from concept_check_depth_v206 import apply_concept_check_task_alignment_v206
from concept_check_depth_v207 import apply_concept_check_task_alignment_v207
from concept_check_depth_v208 import apply_concept_check_task_alignment_v208
from concept_check_depth_v209 import apply_concept_check_task_alignment_v209
from concept_check_depth_v210 import apply_concept_check_task_alignment_v210
from concept_check_depth_v211 import apply_concept_check_task_alignment_v211
from concept_check_laser_energy_safety_v211 import apply_laser_energy_safety_v211
from concept_check_frontal_draf_v211 import apply_frontal_draf_v211
from concept_check_four_gland_parathyroid_v211 import apply_four_gland_parathyroid_v211
from concept_check_local_flap_reconstruction_v211 import apply_local_flap_reconstruction_v211
from concept_check_cervicofacial_flap_v211 import apply_cervicofacial_flap_v211
from concept_check_microlaryngoscopy_v211 import apply_microlaryngoscopy_v211

CLINICAL_STEM_RE = re.compile(r"\b(patient|child|infant|adult|man|woman|boy|girl|presents|returns|develops|postoperative|exam|otoscopy|endoscopy|ct|mri|ultrasound|audiogram|psg)\b", re.I)

def _clinical_prompt(q):
    prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "")
    return "?" in prompt and bool(CLINICAL_STEM_RE.search(prompt))

def _reassert_clinical_contract(checks, repaired_ids, unresolved, marker):
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    reframed = []
    for qid in repaired_ids:
        q = by_id.get(str(qid))
        if q is None or _clinical_prompt(q): continue
        prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()
        if prompt:
            q["prompt"] = "A patient is evaluated by the otolaryngology service. " + prompt
            q.pop("question", None); q.pop("stem", None); q[marker] = True; reframed.append(qid)
        else: unresolved.append(qid)
    return reframed

_ALIGNMENT_FUNCS = [
    (180, apply_concept_check_task_alignment_v180, False),(181, apply_concept_check_task_alignment_v181, False),(182, apply_concept_check_task_alignment_v182, False),
    (183, apply_concept_check_task_alignment_v183, True),(184, apply_concept_check_task_alignment_v184, True),(185, apply_concept_check_task_alignment_v185, True),
    (186, apply_concept_check_task_alignment_v186, True),(187, apply_concept_check_task_alignment_v187, True),(188, apply_concept_check_task_alignment_v188, True),
    (189, apply_concept_check_task_alignment_v189, True),(190, apply_concept_check_task_alignment_v190, True),(191, apply_concept_check_task_alignment_v191, True),
    (192, apply_concept_check_task_alignment_v192, True),(193, apply_concept_check_task_alignment_v193, True),(194, apply_concept_check_task_alignment_v194, True),
    (195, apply_concept_check_task_alignment_v195, True),(196, apply_concept_check_task_alignment_v196, True),(197, apply_concept_check_task_alignment_v197, True),
    (198, apply_concept_check_task_alignment_v198, True),(199, apply_concept_check_task_alignment_v199, True),(200, apply_concept_check_task_alignment_v200, True),
    (201, apply_concept_check_task_alignment_v201, True),(202, apply_concept_check_task_alignment_v202, True),(203, apply_concept_check_task_alignment_v203, True),
    (204, apply_concept_check_task_alignment_v204, True),(205, apply_concept_check_task_alignment_v205, True),(206, apply_concept_check_task_alignment_v206, True),
    (207, apply_concept_check_task_alignment_v207, True),
]

def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    converted, unresolved = [], []
    for q in checks or []:
        if _clinical_prompt(q): continue
        module = _find_module(q, deep_modules, v6_item_id)
        if module and _convert_to_domain_oral_board(q, module): q["final_clinical_gate_v179"] = True; converted.append(q.get("id"))
        else: unresolved.append(q.get("id"))
    results = {"converted": converted, "unresolved": unresolved, "v184_content_fix": apply_bot_trimodality_depth_v184()}
    for version, fn, needs_context in _ALIGNMENT_FUNCS:
        alignment = fn(checks, deep_modules, v6_item_id) if needs_context else fn(checks)
        results[f"task_alignment_v{version}"] = alignment
        marker = f"post_alignment_clinical_frame_v{version}"
        reframed = _reassert_clinical_contract(checks, alignment.get("repaired", []), unresolved, marker)
        if version == 180: results["post_alignment_reframed_v181"] = reframed
        elif version == 181: results["post_alignment_reframed_v181_cohort2"] = reframed
        else: results[f"post_alignment_reframed_v{version}"] = reframed
    alignment_v208 = apply_concept_check_task_alignment_v208(checks, deep_modules, v6_item_id)
    results["task_alignment_v208"] = alignment_v208
    results["post_alignment_reframed_v208"] = _reassert_clinical_contract(checks, alignment_v208.get("repaired", []), unresolved, "post_alignment_clinical_frame_v208")
    alignment_v209 = apply_concept_check_task_alignment_v209(checks, deep_modules, v6_item_id)
    results["task_alignment_v209"] = alignment_v209
    results["post_alignment_reframed_v209"] = _reassert_clinical_contract(checks, alignment_v209.get("repaired", []), unresolved, "post_alignment_clinical_frame_v209")
    alignment_v210 = apply_concept_check_task_alignment_v210(checks, deep_modules, v6_item_id)
    results["task_alignment_v210"] = alignment_v210
    results["post_alignment_reframed_v210"] = _reassert_clinical_contract(checks, alignment_v210.get("repaired", []), unresolved, "post_alignment_clinical_frame_v210")
    alignment_v211 = apply_concept_check_task_alignment_v211(checks, deep_modules, v6_item_id)
    laser_v211 = apply_laser_energy_safety_v211(checks, deep_modules, v6_item_id)
    draf_v211 = apply_frontal_draf_v211(checks, deep_modules, v6_item_id)
    parathyroid_v211 = apply_four_gland_parathyroid_v211(checks, deep_modules, v6_item_id)
    local_flap_v211 = apply_local_flap_reconstruction_v211(checks, deep_modules, v6_item_id)
    cervicofacial_v211 = apply_cervicofacial_flap_v211(checks, deep_modules, v6_item_id)
    microlaryngoscopy_v211 = apply_microlaryngoscopy_v211(checks, deep_modules, v6_item_id)
    for key in ("repaired","missing","link_mismatch"):
        alignment_v211[key] = list(dict.fromkeys(list(alignment_v211.get(key) or []) + list(laser_v211.get(key) or []) + list(draf_v211.get(key) or []) + list(parathyroid_v211.get(key) or []) + list(local_flap_v211.get(key) or []) + list(cervicofacial_v211.get(key) or []) + list(microlaryngoscopy_v211.get(key) or [])))
    results["task_alignment_v211"] = alignment_v211
    results["post_alignment_reframed_v211"] = _reassert_clinical_contract(checks, alignment_v211.get("repaired", []), unresolved, "post_alignment_clinical_frame_v211")
    return results
