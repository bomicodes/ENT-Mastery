"""v20.15 — bind/deepen the exact live Four-Gland Parathyroid Exploration Concept Check."""
from concept_check_board_repair_v177 import _find_module
from concept_check_four_gland_parathyroid_v211 import PROMPT as _V211_PROMPT, ANSWER as _V211_ANSWER, COMMON_TRAPS as _V211_TRAPS

QID = "cc-v112-rec-thyroid-parathyroid-salivary-four-gland-parathyroid-exploration"
CID = "v6-thyroid-parathyroid-salivary-four-gland-parathyroid-exploration"
TOPIC = "Four-Gland Parathyroid Exploration"

SOURCE_REFS_V215 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive corpus including Cummings_7e_Part_4_pages_1978-2636.pdf (Drive id 1e6jOBnaay1Msf-aDw-Kf9k2_NtzODQEu) and full Cummings 7e copy (Drive id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t); parathyroid anatomy/exploration cross-reference refreshed 2026-09-07.","role":"durable operative foundation: embryologic migration, superior/inferior gland relationship to the RLN plane, ectopic search strategy, preservation of viable tissue"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy (Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52), Endocrinology/parathyroidectomy material cross-referenced 2026-09-07.","role":"resident/board framework: indications for bilateral exploration, multigland disease, operative complications and postoperative calcium/voice surveillance"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy (Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR), thyroid/parathyroid material cross-referenced 2026-09-07.","role":"operative cross-check: adenoma versus hyperplasia, ioPTH kinetics, subtotal/total parathyroidectomy concepts, persistence/recurrence"},
    {"type":"guideline","citation":"Wilhelm SM, et al. The American Association of Endocrine Surgeons Guidelines for Definitive Management of Primary Hyperparathyroidism. JAMA Surg. 2016;151(10):959-968. PMID: 27532368. DOI: 10.1001/jamasurg.2016.2310.","role":"major surgical-society guidance: routinely consider multigland disease; focused and bilateral exploration can both cure; IPM should use a reliable local protocol; devascularized normal tissue should be autotransplanted"},
    {"type":"international_guideline","citation":"Bilezikian JP, et al. Evaluation and Management of Primary Hyperparathyroidism: Summary Statement and Guidelines from the Fifth International Workshop. J Bone Miner Res. 2022;37(11):2293-2314. DOI: 10.1002/jbmr.4677.","role":"current international PHPT evaluation/management framework and surgical indications; imaging is for localization after biochemical diagnosis"},
    {"type":"consensus_review","citation":"Perrier ND, et al. Surgical Aspects of Primary Hyperparathyroidism. J Bone Miner Res. 2022;37(11):2373-2390. PMID: 36054175. DOI: 10.1002/jbmr.4689.","role":"international operative consensus: selective PTX, reasons for conversion, bilateral exploration for nonlocalized/multigland disease, subtotal/total PTX and hereditary/reoperative strategy"},
    {"type":"systematic_review","citation":"Comparison of efficacy and safety between minimally invasive parathyroidectomy and bilateral neck exploration for primary hyperparathyroidism: a systematic review and meta-analysis. Surgery. 2026. PMID: 42623898.","role":"current evidence reconciliation: comparable cure in selected patients, MIP lower morbidity/resource use, and an 8.5% conversion rate; supports individualized approach rather than routine BNE for every PHPT patient"},
]

PROMPT = _V211_PROMPT
ANSWER = _V211_ANSWER + """

Current-evidence reconciliation — do not teach bilateral exploration as either obsolete or automatically superior. The 2022 international surgical consensus retains bilateral neck exploration for nonlocalized or multigland disease and defines conversion from selective surgery when findings or physiology no longer support a single-gland endpoint. A 2026 systematic review/meta-analysis found comparable cure rates between minimally invasive parathyroidectomy and bilateral exploration in selected PHPT populations, with shorter operations/hospitalization and fewer temporary adverse events after minimally invasive surgery, while about 8.5% required conversion to bilateral exploration. The teaching implication is selection: concordant single-gland disease can appropriately remain focused, whereas negative/discordant localization, hereditary or lithium-associated biology, multiple abnormal glands, an absent expected gland, or an inadequate physiologically interpreted ioPTH response should trigger a systematic multigland strategy.

Intraoperative-PTH nuance — define which baseline your local protocol uses before interpreting the curve. A pre-incision sample can establish a true operating-room baseline before manipulation; a pre-excision/pre-resection sample may capture a manipulation-associated peak and can therefore change the denominator for a percent-drop criterion. Do not mix baselines casually. A >50% decline is commonly used in validated protocols, but the exact endpoint and sampling time must follow the institution's reliable protocol and be reconciled with the final absolute level and clinical setting. If the PTH does not fully fall as expected, first check draw timing, assay/sampling error, baseline choice and renal function. Poor renal function can slow PTH clearance and maintain a higher baseline, so a borderline curve should not provoke indiscriminate removal of normal glands. Conversely, renal dysfunction is not a blanket excuse for a persistently nonresponsive curve when operative findings still suggest residual hyperfunctioning tissue.

Senior bailout — when four credible glands have been accounted for yet physiology still suggests active disease, stop before converting uncertainty into injury. Reconstruct the gland map, specimen identity and ioPTH timeline; reconsider supernumerary/ectopic tissue, intrathymic disease and whether an apparent gland was actually fat/lymph node/thyroid. Use embryology and targeted adjuncts rather than blind deep dissection. If safe cervical exploration is exhausted and the suspected target is mediastinal or otherwise outside a controlled field, end the cervical operation with a documented localization/reoperative plan rather than injuring the RLN, esophagus, great vessels or a viable parathyroid remnant simply to declare that every possible location was searched."""

TRAPS = list(_V211_TRAPS) + [
    "Mixing a pre-incision and pre-excision intraoperative-PTH baseline without recognizing that gland manipulation can change the percent-drop denominator.",
    "Treating renal dysfunction as either irrelevant to PTH clearance or as an automatic excuse for any inadequate curve instead of integrating timing, absolute level and operative findings.",
    "Continuing blind deep cervical/mediastinal dissection after a systematic search is exhausted rather than stopping with a targeted localization/reoperative plan.",
]

COHORT = {QID: {
    "concept_id": CID, "canonical_topic": TOPIC, "prompt": PROMPT, "answer_text": ANSWER,
    "explanation": "Four-gland exploration is a systematic anatomy-and-biology operation: select it for the right disease pattern, use embryology/RLN relationships to account for glands, interpret ioPTH with a defined baseline and renal physiology, preserve perfused tissue, and stop unsafe searching when anatomy is no longer controlled.",
    "board_pearl": "Superior glands are usually posterior to the RLN plane; inferior glands are usually anterior and follow thymic migration. Inadequate ioPTH should trigger protocol/timing/baseline and renal-function checks plus a structured search for residual multigland or ectopic tissue—not random normal-gland excision.",
    "depth_layers_v215": {"foundation":"Indication for focused versus bilateral exploration; superior/inferior embryology, RLN-plane anatomy, expected and ectopic locations.","application":"Systematic four-gland accounting, adenoma versus multigland hyperplasia, subtotal/total-autotransplant decisions, perfusion preservation and protocol-faithful ioPTH interpretation.","senior_decision":"Convert when focused assumptions fail; reconcile pre-incision versus pre-excision baselines, renal clearance and inadequate ioPTH; search for ectopic/supernumerary disease and bail out before unsafe deep dissection."},
    "common_traps_v215": TRAPS,
    "deliberate_review_v215": "Selected from the exact successful v20.14 production artifact (325 canonical topics, 159 untouched shallow checks, 9 residual candidates, 0 failures). Four-Gland Parathyroid Exploration was residual rank 1 and the live rec-ID answer was only 20 words. A strong older v20.11 lesson existed on an obsolete mgt-ID; v20.15 deliberately binds upgraded teaching to the exact live rec-ID rather than assuming the legacy patch covers it.",
    "source_refs_v215": SOURCE_REFS_V215,
}}

def apply_concept_check_task_alignment_v215(checks, deep_modules, v6_item_id):
    by={str(q.get("id") or ""):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
    for qid,p in COHORT.items():
        q=by.get(qid)
        if q is None: missing.append(qid); continue
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        if m is None or topic!=p["canonical_topic"] or cid!=p["concept_id"] or q.get("concept_id")!=cid: link_mismatch.append(qid); continue
        for field in ("prompt","answer_text","explanation","board_pearl","depth_layers_v215","common_traps_v215","deliberate_review_v215","source_refs_v215"): q[field]=p[field]
        q["choices"]=[]; q["answer"]=None; q["task_alignment_v215"]=True; repaired.append(qid)
    return {"repaired":repaired,"missing":missing,"link_mismatch":link_mismatch}
