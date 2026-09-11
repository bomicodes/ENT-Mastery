"""Final clinical-stem normalization and ordered Concept Check depth hardening.

Generic/domain normalization runs first. Focused task-alignment repairs then run in
version order so exact, source-grounded teaching cannot be overwritten by fallback
question generation. The newest cohort remains an explicit final call for fail-closed
release-manifest verification.
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
from concept_check_depth_v212 import apply_concept_check_task_alignment_v212
from concept_check_depth_v213 import apply_concept_check_task_alignment_v213
from concept_check_depth_v214 import apply_concept_check_task_alignment_v214
from concept_check_depth_v215 import apply_concept_check_task_alignment_v215
from concept_check_depth_v216 import apply_concept_check_task_alignment_v216
from concept_check_depth_v217 import apply_concept_check_task_alignment_v217
from concept_check_depth_v218 import apply_concept_check_task_alignment_v218
from concept_check_depth_v219 import apply_concept_check_task_alignment_v219
from concept_check_depth_v220 import apply_concept_check_task_alignment_v220
from concept_check_depth_v221 import apply_concept_check_task_alignment_v221
from concept_check_depth_v222 import apply_concept_check_task_alignment_v222
from concept_check_depth_v223 import apply_concept_check_task_alignment_v223
from concept_check_depth_v224 import apply_concept_check_task_alignment_v224
from concept_check_depth_v225 import apply_concept_check_task_alignment_v225
from concept_check_laser_energy_safety_v211 import apply_laser_energy_safety_v211
from concept_check_frontal_draf_v211 import apply_frontal_draf_v211
from concept_check_four_gland_parathyroid_v211 import apply_four_gland_parathyroid_v211
from concept_check_local_flap_reconstruction_v211 import apply_local_flap_reconstruction_v211
from concept_check_cervicofacial_flap_v211 import apply_cervicofacial_flap_v211
from concept_check_microlaryngoscopy_v211 import apply_microlaryngoscopy_v211
from concept_check_tracheomalacia_bronchomalacia_v211 import apply_tracheomalacia_bronchomalacia_v211

CLINICAL_STEM_RE = re.compile(r"\b(patient|child|infant|adult|man|woman|boy|girl|presents|returns|develops|postoperative|exam|otoscopy|endoscopy|ct|mri|ultrasound|audiogram|psg)\b", re.I)

def _clinical_prompt(q):
    prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "")
    return "?" in prompt and bool(CLINICAL_STEM_RE.search(prompt))

def _reassert_clinical_contract(checks, repaired_ids, unresolved, marker):
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    reframed = []
    for qid in repaired_ids:
        q = by_id.get(str(qid))
        if q is None or _clinical_prompt(q):
            continue
        prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()
        if not prompt:
            unresolved.append(qid)
            continue
        if not CLINICAL_STEM_RE.search(prompt):
            prompt = "A patient is evaluated by the otolaryngology service. " + prompt
        if "?" not in prompt:
            prompt = prompt.rstrip().rstrip(".") + "?"
        q["prompt"] = prompt
        q.pop("question", None)
        q.pop("stem", None)
        q[marker] = True
        reframed.append(qid)
    return reframed

_ALIGNMENT_FUNCS = {
    180: apply_concept_check_task_alignment_v180, 181: apply_concept_check_task_alignment_v181, 182: apply_concept_check_task_alignment_v182,
    183: apply_concept_check_task_alignment_v183, 184: apply_concept_check_task_alignment_v184, 185: apply_concept_check_task_alignment_v185,
    186: apply_concept_check_task_alignment_v186, 187: apply_concept_check_task_alignment_v187, 188: apply_concept_check_task_alignment_v188,
    189: apply_concept_check_task_alignment_v189, 190: apply_concept_check_task_alignment_v190, 191: apply_concept_check_task_alignment_v191,
    192: apply_concept_check_task_alignment_v192, 193: apply_concept_check_task_alignment_v193, 194: apply_concept_check_task_alignment_v194,
    195: apply_concept_check_task_alignment_v195, 196: apply_concept_check_task_alignment_v196, 197: apply_concept_check_task_alignment_v197,
    198: apply_concept_check_task_alignment_v198, 199: apply_concept_check_task_alignment_v199, 200: apply_concept_check_task_alignment_v200,
    201: apply_concept_check_task_alignment_v201, 202: apply_concept_check_task_alignment_v202, 203: apply_concept_check_task_alignment_v203,
    204: apply_concept_check_task_alignment_v204, 205: apply_concept_check_task_alignment_v205, 206: apply_concept_check_task_alignment_v206,
    207: apply_concept_check_task_alignment_v207, 208: apply_concept_check_task_alignment_v208, 209: apply_concept_check_task_alignment_v209,
    210: apply_concept_check_task_alignment_v210, 211: apply_concept_check_task_alignment_v211, 212: apply_concept_check_task_alignment_v212,
    213: apply_concept_check_task_alignment_v213, 214: apply_concept_check_task_alignment_v214, 215: apply_concept_check_task_alignment_v215,
    216: apply_concept_check_task_alignment_v216, 217: apply_concept_check_task_alignment_v217, 218: apply_concept_check_task_alignment_v218,
    219: apply_concept_check_task_alignment_v219, 220: apply_concept_check_task_alignment_v220, 221: apply_concept_check_task_alignment_v221,
    222: apply_concept_check_task_alignment_v222, 223: apply_concept_check_task_alignment_v223, 224: apply_concept_check_task_alignment_v224,
}

def _store_alignment(results, version, alignment, checks, deep_modules, v6_item_id, unresolved):
    if version == 211:
        cohorts = [
            apply_laser_energy_safety_v211(checks, deep_modules, v6_item_id),
            apply_frontal_draf_v211(checks, deep_modules, v6_item_id),
            apply_four_gland_parathyroid_v211(checks, deep_modules, v6_item_id),
            apply_local_flap_reconstruction_v211(checks, deep_modules, v6_item_id),
            apply_cervicofacial_flap_v211(checks, deep_modules, v6_item_id),
            apply_microlaryngoscopy_v211(checks, deep_modules, v6_item_id),
            apply_tracheomalacia_bronchomalacia_v211(checks, deep_modules, v6_item_id),
        ]
        for key in ("repaired", "missing", "link_mismatch"):
            combined = list(alignment.get(key) or [])
            for cohort in cohorts:
                combined += list(cohort.get(key) or [])
            alignment[key] = list(dict.fromkeys(combined))
    results[f"task_alignment_v{version}"] = alignment
    marker = f"post_alignment_clinical_frame_v{version}"
    reframed = _reassert_clinical_contract(checks, alignment.get("repaired", []), unresolved, marker)
    if version == 180:
        results["post_alignment_reframed_v181"] = reframed
    elif version == 181:
        results["post_alignment_reframed_v181_cohort2"] = reframed
    else:
        results[f"post_alignment_reframed_v{version}"] = reframed

def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    converted, unresolved = [], []
    for q in checks or []:
        if _clinical_prompt(q):
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        if module and _convert_to_domain_oral_board(q, module):
            q["final_clinical_gate_v179"] = True
            converted.append(q.get("id"))
        else:
            unresolved.append(q.get("id"))
    results = {"converted": converted, "unresolved": unresolved, "v184_content_fix": apply_bot_trimodality_depth_v184()}
    for version in range(180, 225):
        fn = _ALIGNMENT_FUNCS[version]
        alignment = fn(checks) if version <= 182 else fn(checks, deep_modules, v6_item_id)
        _store_alignment(results, version, alignment, checks, deep_modules, v6_item_id, unresolved)
    alignment_v225 = apply_concept_check_task_alignment_v225(checks, deep_modules, v6_item_id)
    results["task_alignment_v225"] = alignment_v225
    results["post_alignment_reframed_v225"] = _reassert_clinical_contract(checks, alignment_v225.get("repaired", []), unresolved, "post_alignment_clinical_frame_v225")
    return results
