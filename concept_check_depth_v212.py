"""v20.12 — deepen exact live Tracheomalacia / Bronchomalacia Concept Check.

Durable pediatric-airway anatomy and operative principles are cross-checked against the
connected Cummings 7e, Pasha 6e, and K.J. Lee 12e corpus. Management language is updated
against the ERS pediatric statement and contemporary surgical outcome literature.
"""
from concept_check_board_repair_v177 import _find_module

QID = "cc-v112-rec-pediatric-otolaryngology-tracheomalacia-bronchomalacia"
CID = "v6-pediatric-otolaryngology-tracheomalacia-bronchomalacia"
TOPIC = "Tracheomalacia / Bronchomalacia"

SOURCE_REFS_V212 = [
    {
        "type": "textbook",
        "citation": "Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), pediatric airway evaluation/management and tracheobronchial endoscopy sections; connected Drive split Cummings 7e corpus checked 2026-09-06.",
        "role": "durable foundation/operative: dynamic large-airway collapse, intrinsic versus extrinsic disease, vascular compression, physiologic endoscopic assessment, and anatomy-directed airway planning",
    },
    {
        "type": "textbook",
        "citation": "Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), Ch. 9 Pediatric Otolaryngology, Pediatric Laryngoesophagology; connected Drive copy checked 2026-09-06.",
        "role": "board framework: pediatric dynamic airway evaluation, associated airway/vascular lesions, respiratory support, and escalation for severe disease",
    },
    {
        "type": "textbook",
        "citation": "K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), Ch. 53 Pediatric Otolaryngology, congenital tracheomalacia/airway-obstruction sections; connected Drive copy checked 2026-09-06.",
        "role": "board/operative cross-check: expiratory symptoms, tracheal obstruction differential including vascular compression, bronchoscopy-based evaluation, and airway support",
    },
    {
        "type": "society_statement",
        "citation": "Wallis C, et al. ERS statement on tracheomalacia and bronchomalacia in children. Eur Respir J. 2019;54(3):1900382. PMID: 31320455.",
        "role": "current consensus framework: flexible bronchoscopy in a free-breathing child, dynamic CT/MRI alternatives, no universal severity classification, CPAP support, limited evidence for medications, and anatomy/severity-directed surgery",
    },
    {
        "type": "systematic_review",
        "citation": "Aortopexy for Tracheomalacia in Children: A Systematic Review and Meta-Analysis. 2025. PMID: 40004897.",
        "role": "current surgical evidence: severe-symptom indication, overall favorable outcomes, persistent symptoms remain common, and technique/patient selection matter more than a single universal approach",
    },
    {
        "type": "systematic_review",
        "citation": "Posterior tracheopexy for pediatric tracheomalacia: A global evidence synthesis and meta-analysis. 2026. PMID: 42409109.",
        "role": "current surgical evidence: high symptom-improvement rates with posterior tracheopexy in selected severe disease while emphasizing observational evidence and need for comparative prospective data",
    },
]

PROMPT = """An infant with prior esophageal-atresia/tracheoesophageal-fistula repair has recurrent barking cough, cyanotic spells with agitation, repeated pneumonias, and difficulty weaning from positive-pressure ventilation. CT suggests anterior vascular contact, but the child also appears to have posterior membranous intrusion. How should you prove whether clinically important tracheomalacia, bronchomalacia, or both are present; avoid an anesthetic/endoscopic examination that masks the disease; decide when supportive treatment is enough; and choose an anatomy-directed operation or bailout when symptoms are severe?"""

ANSWER = """Foundation — tracheomalacia and bronchomalacia are dynamic large-airway disorders, not simply a small static lumen. Tracheomalacia involves excessive expiratory collapse of the trachea; bronchomalacia involves one or both main bronchi, and tracheobronchomalacia involves both. Disease may be primary/intrinsic because the cartilaginous framework and posterior membrane do not maintain caliber, or secondary/extrinsic because the airway is compressed or distorted by adjacent cardiovascular, esophageal, skeletal, postoperative, or inflammatory anatomy. Important pediatric associations include prematurity and prolonged airway instrumentation, esophageal atresia/tracheoesophageal fistula, vascular rings or slings, aberrant innominate-artery compression, and other congenital airway abnormalities. The symptom pattern should fit dynamic physiology: barky or brassy cough, expiratory noise or fixed wheeze, recurrent lower-respiratory infections, secretion-retention problems, exercise/feeding intolerance, cyanotic or near-death spells, and inability to wean respiratory support can all occur. A percentage of collapse alone does not define the clinical severity; physiology and consequences matter.

Dynamic diagnosis — the key test is an airway examination that actually allows the airway to demonstrate its native behavior. Current ERS teaching favors flexible bronchoscopy in a free-breathing child for diagnosis, while dynamic CT or MRI can complement endoscopy when distal airway anatomy, vascular compression, or operative planning needs clarification. During bronchoscopy, describe the location and length of collapse, anterior versus posterior versus circumferential geometry, relationship to the carina, and whether the right or left mainstem bronchi are also involved. Inspect the entire tracheobronchial tree rather than stopping after seeing one dramatic tracheal segment. A major OR trap is evaluating the child only under substantial positive-pressure ventilation: positive pressure pneumatically stents a malacic airway and can make the collapse appear much less severe. Coordinate anesthesia so the dynamic portion is assessed under physiologic spontaneous/free breathing when safe, then change ventilation strategy as needed for airway control. Do not create danger merely to preserve spontaneous breathing; if oxygenation or ventilation is failing, stabilize the child first and interpret the study in light of the support being applied.

Separate intrinsic from extrinsic anatomy — bronchoscopy shows what collapses, while cross-sectional dynamic imaging and vascular imaging help explain why. Anterior pulsatile compression should trigger deliberate evaluation for innominate-artery compression, vascular ring/sling, enlarged cardiovascular structures, or postoperative mediastinal relationships. Posterior membranous intrusion points toward a different mechanical problem and may coexist with anterior compression. Left-mainstem or diffuse bronchial disease matters because a trachea-only operation may leave the clinically important obstruction untreated. Before choosing surgery, define the airway geometry rather than equating every severe tracheomalacia case with an automatic aortopexy.

Supportive management — mild disease without dangerous events, major infection burden, failure to thrive, or respiratory-support dependence can often be observed while the airway grows and associated disorders are addressed. Airway-clearance strategies, hydration/secretion management, prompt treatment of bacterial lower-respiratory infection when present, and multidisciplinary pulmonary/ENT care are often more useful than empiric medication lists. If respiratory support is needed, CPAP is the most commonly used noninvasive pneumatic-stenting strategy. The contemporary evidence distinction is important: bronchodilators, antimuscarinic agents, mucolytics, reflux treatment, and other medications may be appropriate for a separate demonstrated indication, but the ERS statement notes limited evidence that medication itself fixes pediatric airway malacia. Do not prescribe chronic acid suppression or systemic steroids merely because malacia exists.

When severity changes the plan — escalation is driven by consequential physiology: recurrent cyanotic/brief-resolved-unexplained-event or near-death spells, recurrent pneumonias with secretion trapping, inability to extubate, persistent need for positive-pressure ventilation, progressive respiratory failure, or major feeding/growth consequences despite appropriate support. These are senior-decision findings because repeated conservative care may simply reproduce the same emergency. The operative goal is not to reach an arbitrary collapse number; it is to relieve the mechanism responsible for clinically important obstruction while preserving adjacent structures.

Choose the operation by geometry. Anterior aortopexy is most logical when the anterior trachea is being compressed by the aorta/innominate relationship and anterior suspension will reliably open the airway. Posterior tracheopexy directly addresses excessive posterior membranous intrusion by fixing the posterior airway to a stable posterior structure; combined anterior and posterior procedures may be required when collapse is multidirectional. Distal or left-mainstem disease may require a descending-aortopexy or bronchus-directed strategy at experienced centers. Contemporary systematic reviews support substantial symptom improvement after both aortopexy and posterior tracheopexy in selected severe pediatric patients, but the evidence is predominantly observational; these procedures should therefore be anatomy- and symptom-directed rather than taught as interchangeable universal cures.

Bailout and special situations — tracheostomy with positive pressure can provide a route for prolonged pneumatic stenting when disease is severe or reconstruction is not immediately feasible, but tracheostomy is not the automatic endpoint for every child with malacia and may not bypass long distal disease. Internal airway stents and external splints/stents can be useful in highly selected complex or rescue situations, but migration, granulation, erosion, infection, growth, and adjacent-structure concerns prevent routine use as a simple first-line solution. Newer external-stent/tracheopexy approaches are promising but should be described as evolving evidence rather than a settled standard.

Failure analysis — persistent symptoms after an operation demand a new dynamic airway map, not reflex repetition of the same procedure. Ask whether the original mechanism was wrong, whether bronchomalacia was missed, whether posterior intrusion remains after anterior aortopexy, whether vascular or esophageal anatomy still compresses the airway, whether fixation failed, and whether infection/aspiration or another airway lesion is driving the current physiology. Acute desaturation or cyanotic spells require immediate airway/oxygenation rescue first; diagnostic purity comes second.

Senior synthesis — use four questions. PHYSIOLOGY: are the spells, infections, secretion problems, or ventilator dependence severe enough to justify intervention? DYNAMICS: was the airway actually observed during free/spontaneous breathing rather than only while positive pressure held it open? GEOMETRY: is the dominant problem anterior vascular compression, posterior membranous intrusion, circumferential collapse, bronchomalacia, or a combination? MATCH: does the proposed treatment actually correct that geometry — CPAP for pneumatic support, aortopexy for appropriate anterior compression, posterior/combined tracheopexy for posterior or multidirectional collapse, and selected rescue strategies for complex refractory disease? The dangerous alternatives are diagnosing from a static airway, letting positive pressure hide the lesion, grading severity by collapse percentage alone, missing vascular compression or bronchomalacia, treating reflux or steroids as a malacia cure, assuming every severe child will simply outgrow the disease, and choosing aortopexy before defining the direction and extent of collapse."""

COHORT = {
    QID: {
        "concept_id": CID,
        "canonical_topic": TOPIC,
        "prompt": PROMPT,
        "answer_text": ANSWER,
        "explanation": "Pediatric tracheobronchomalacia is a dynamic physiology-and-geometry problem: prove clinically important collapse under conditions that do not mask it, map tracheal and bronchial involvement plus vascular compression, support mild disease, and choose surgery by the direction and consequences of collapse rather than by a percentage threshold.",
        "board_pearl": "Positive pressure can splint a malacic airway and understate severity. Map the airway dynamically, including both main bronchi and vascular relationships, then match the operation to geometry: anterior compression may favor aortopexy; posterior intrusion may favor posterior or combined tracheopexy.",
        "depth_layers_v212": {
            "foundation": "Differentiate tracheomalacia, bronchomalacia and tracheobronchomalacia; distinguish intrinsic weakness from extrinsic compression; link symptoms to dynamic expiratory physiology.",
            "application": "Use free-breathing dynamic bronchoscopy plus selective dynamic/vascular imaging, recognize positive-pressure masking, inspect distal bronchi, and apply airway-clearance/CPAP support appropriately.",
            "senior_decision": "Escalate consequential disease and match aortopexy, posterior/combined tracheopexy, bronchus-directed surgery, tracheostomy or selected stenting to the actual collapse geometry and rescue needs.",
        },
        "common_traps_v212": [
            "Diagnosing tracheomalacia from a static airway image without demonstrating dynamic expiratory collapse.",
            "Assessing the airway only under substantial positive-pressure ventilation and falsely concluding that collapse is mild because the pressure has stented it open.",
            "Treating a percentage-collapse threshold as the disease rather than integrating cyanotic spells, infections, growth, extubation failure and respiratory-support dependence.",
            "Stopping bronchoscopy after finding tracheal collapse and missing clinically important right- or left-mainstem bronchomalacia.",
            "Calling every pulsatile anterior indentation intrinsic tracheomalacia without defining vascular-ring, sling, innominate or other cardiovascular compression.",
            "Choosing aortopexy automatically before distinguishing anterior compression from posterior membranous intrusion or multidirectional collapse.",
            "Prescribing chronic reflux medication or systemic steroids specifically to cure malacia without a separate evidence-based indication.",
            "Assuming every symptomatic infant will outgrow the disease despite cyanotic/near-death spells, recurrent pneumonia, failure to extubate or ongoing ventilator dependence.",
            "Using tracheostomy as an automatic definitive endpoint without asking whether distal tracheal or bronchial collapse persists beyond the tube.",
            "Using an intraluminal or external airway stent as a routine first-line shortcut without accounting for migration, granulation, erosion, growth and evolving evidence.",
            "Persisting with a diagnostic spontaneous-breathing plan during dangerous hypoxemia instead of restoring oxygenation/ventilation and interpreting the airway under the support required for safety.",
            "Repeating the same operation after persistent symptoms without remapping for missed bronchomalacia, residual posterior intrusion, persistent vascular compression, aspiration/infection or fixation failure.",
        ],
        "deliberate_review_v212": "Selected from the exact successful v20.11 production backlog, where the live canonical Tracheomalacia / Bronchomalacia Concept Check remained a 16-word shallow candidate despite high resident/board/OR relevance. v20.12 explicitly corrects static-airway and percentage-only teaching, adds free-breathing/positive-pressure physiology, complete tracheobronchial mapping, anatomy-directed aortopexy versus posterior/combined tracheopexy decisions, and rescue/failure analysis.",
        "source_refs_v212": SOURCE_REFS_V212,
    }
}


def apply_concept_check_task_alignment_v212(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, patch in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if module is None or topic != patch["canonical_topic"] or cid != patch["concept_id"] or q.get("concept_id") != cid:
            link_mismatch.append(qid)
            continue
        for field in (
            "prompt", "answer_text", "explanation", "board_pearl", "depth_layers_v212",
            "common_traps_v212", "deliberate_review_v212", "source_refs_v212",
        ):
            q[field] = patch[field]
        q["choices"] = []
        q["answer"] = None
        q["task_alignment_v212"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
