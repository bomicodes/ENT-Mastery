"""v20.12 — deepen exact live Tracheomalacia / Bronchomalacia Concept Check.

Durable pediatric-airway anatomy and operative principles are cross-checked against the
connected Cummings 7e, Pasha 6e, and K.J. Lee 12e corpus. Management language is updated
against the ERS pediatric statement and contemporary surgical outcome literature.

Compatibility note: this revision intentionally preserves the clinically meaningful
v20.11 semantic anchors while retaining the richer v20.12 reasoning, so the older
fail-closed cohort cannot be silently invalidated by a newer runtime answer replacement.
"""
from concept_check_board_repair_v177 import _find_module

QID = "cc-v112-rec-pediatric-otolaryngology-tracheomalacia-bronchomalacia"
CID = "v6-pediatric-otolaryngology-tracheomalacia-bronchomalacia"
TOPIC = "Tracheomalacia / Bronchomalacia"

SOURCE_REFS_V212 = [
    {
        "type": "textbook",
        "citation": "Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), pediatric airway evaluation/management and tracheobronchial endoscopy sections; connected Drive Cummings 7e corpus rechecked 2026-09-07.",
        "role": "durable foundation/operative: dynamic large-airway collapse, intrinsic versus extrinsic disease, vascular compression, physiologic endoscopic assessment, positive-pressure splinting, and anatomy-directed airway planning",
    },
    {
        "type": "textbook",
        "citation": "Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), pediatric otolaryngology/airway sections; connected Drive copy rechecked 2026-09-07.",
        "role": "resident framework: pediatric dynamic airway evaluation, associated airway/vascular lesions, respiratory support, and escalation for severe disease",
    },
    {
        "type": "textbook",
        "citation": "K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), pediatric otolaryngology congenital tracheomalacia/airway-obstruction sections; connected Drive copy rechecked 2026-09-07.",
        "role": "board/operative cross-check: expiratory symptoms, tracheal obstruction differential including vascular compression, bronchoscopy-based evaluation, positive-pressure support, and historical tracheostomy/aortopexy principles",
    },
    {
        "type": "society_statement",
        "citation": "Wallis C, et al. ERS statement on tracheomalacia and bronchomalacia in children. Eur Respir J. 2019;54(3):1900382. PMID: 31320455.",
        "role": "current consensus framework: flexible bronchoscopy in a free-breathing child, dynamic CT/MRI alternatives, no universal severity classification, CPAP support, limited evidence for medications, and anatomy/severity-directed surgery",
    },
    {
        "type": "systematic_review",
        "citation": "Aortopexy for Tracheomalacia in Children: A Systematic Review and Meta-Analysis. J Clin Med. 2025. PMID: 40004897.",
        "role": "current surgical evidence: severe-symptom indication, overall favorable outcomes, persistent symptoms remain common, and technique/patient selection matter more than a single universal approach",
    },
    {
        "type": "systematic_review",
        "citation": "Singh S, et al. Posterior tracheopexy for pediatric tracheomalacia: A global evidence synthesis and meta-analysis. J Pediatr Surg. 2026 Jul 6:163285. PMID: 42409109.",
        "role": "current surgical evidence: high symptom-improvement rates with posterior tracheopexy in selected severe disease while emphasizing observational evidence and need for prospective comparative data",
    },
]

PROMPT = """An infant with prior esophageal-atresia/tracheoesophageal-fistula repair has recurrent barking cough, cyanotic spells with agitation, repeated pneumonias, and difficulty weaning from positive-pressure ventilation. CT suggests anterior vascular contact, but the child also appears to have posterior membranous intrusion. How should you prove whether clinically important tracheomalacia, bronchomalacia, or both are present; avoid an anesthetic/endoscopic examination that masks the disease; decide when supportive treatment is enough; and choose an anatomy-directed operation or bailout when symptoms are severe?"""

ANSWER = """Foundation — tracheomalacia and bronchomalacia are dynamic large-airway disorders, not simply a small static lumen. Tracheomalacia involves excessive expiratory collapse of the trachea; bronchomalacia involves one or both main bronchi, and tracheobronchomalacia involves both. Disease may be primary or intrinsic because the cartilaginous framework and posterior membrane do not maintain caliber, or secondary/extrinsic because the airway is compressed or distorted by adjacent cardiovascular, esophageal, skeletal, postoperative, or inflammatory anatomy. Important pediatric associations include prematurity and prolonged airway instrumentation, esophageal atresia/tracheoesophageal fistula, vascular rings or slings, aberrant innominate-artery compression, and other congenital airway abnormalities. The symptom pattern should fit dynamic physiology: barky or brassy cough, expiratory noise or fixed wheeze, recurrent lower-respiratory infections or pneumonia, secretion-retention problems, feeding intolerance, failure to thrive, cyanotic or near-death spells, and inability to wean a ventilator or other respiratory support can all occur. A percentage of collapse alone does not define clinical severity; physiology and consequences matter.

Dynamic diagnosis — the key reference examination is dynamic flexible bronchoscopy in a spontaneously or free-breathing child when this can be performed safely. This preserves native airway mechanics rather than examining only an airway already splinted open by anesthesia and pressure. Dynamic CT or other dynamic imaging can complement bronchoscopy when distal airway anatomy, vascular compression, or operative planning needs clarification, but static inspiratory imaging cannot reliably exclude malacia. During bronchoscopy, inspect the entire tracheobronchial tree and map the full trachea plus the right and left mainstem bronchi. Describe location and longitudinal extent, relationship to the carina, anterior versus posterior versus circumferential geometry, secretion burden, and any pulsatile vascular or other extrinsic compression. Do not stop after finding one dramatic tracheal segment because clinically important distal bronchomalacia may determine the operation and the outcome.

The anesthetic itself can create a false-negative study. Positive airway pressure acts as a pneumatic stent: CPAP or PEEP can splint a malacic airway and make collapse appear less severe. Coordinate anesthesia so the dynamic portion is observed during physiologic spontaneous/free breathing when safe, then change the ventilation strategy as needed for airway control. Diagnostic purity never outranks oxygenation. If the child develops dangerous desaturation, hypercarbia, severe obstruction, or loss of effective ventilation, stop the provocative maneuver, withdraw or reposition the bronchoscope as needed, restore ventilation, and apply positive pressure with PEEP or CPAP. The response to pressure is useful physiology; it is not evidence that the disease is absent.

Application — separate intrinsic weakness from extrinsic compression and define the geometry before choosing treatment. Bronchoscopy shows what collapses; dynamic cross-sectional and vascular imaging help explain why. Anterior pulsatile compression should trigger deliberate evaluation for innominate compression, vascular ring or sling, enlarged cardiovascular structures, or postoperative mediastinal relationships. Excessive posterior membranous intrusion is a different mechanical problem and may coexist with anterior compression. A child with significant left- or right-mainstem disease has more than an isolated tracheal problem. Associated aspiration/swallow dysfunction, recurrent infection, secretion-clearance difficulty, reflux when independently demonstrated, and foregut anatomy can magnify symptoms and should be addressed without falsely presenting those treatments as cures for malacia.

Supportive management — mild disease without dangerous events, major infection burden, failure to thrive, or respiratory-support dependence can often be observed while the airway grows and associated disease is managed. Airway clearance strategies, hydration and secretion management, prompt treatment of bacterial infection when present, nutrition support, and multidisciplinary pulmonary/ENT care are often more useful than empiric medication lists. CPAP/PEEP can provide noninvasive positive airway pressure and pneumatic stenting as a bridge through growth, acute illness, or ventilator weaning. The evidence distinction matters: the ERS statement notes limited evidence that bronchodilators, antimuscarinic agents, mucolytics, reflux therapy, or other medications directly treat pediatric airway malacia. Use those therapies for a separate demonstrated indication, not because malacia itself is presumed to require them.

Senior decision — escalate when the physiology is consequential despite optimized support: recurrent cyanotic or life-threatening spells, recurrent pneumonias with secretion trapping, failure to extubate or inability to wean meaningful positive-pressure ventilation, progressive respiratory failure, or major feeding and growth consequences. The operative goal is not to reach an arbitrary collapse percentage. It is to correct the mechanism causing clinically important obstruction while protecting adjacent structures.

Choose the operation by geometry. Aortopexy or related anterior suspension is most logical when anterior vascular-related compression/collapse is the dominant mechanism and anterior displacement will reliably open the airway. Posterior tracheopexy directly addresses excessive posterior membranous intrusion by fixing the posterior airway to a stable posterior structure. Combined anterior and posterior stabilization may be required when collapse is multidirectional. When clinically important mainstem bronchomalacia is present, bronchopexy or another bronchus-directed strategy may be required rather than treating the trachea alone; selected left-mainstem compression can also require descending-aortic or other anatomy-directed decompression at experienced centers. Contemporary systematic reviews report substantial symptom improvement after both aortopexy and posterior tracheopexy in carefully selected severe pediatric patients, but the evidence remains predominantly observational. These operations therefore should not be taught as interchangeable universal cures.

Bailout and special situations — tracheostomy with positive pressure can provide a stable airway interface and a route for prolonged pneumatic stenting when disease is severe or reconstruction is not immediately feasible, but tracheostomy is not the automatic endpoint for every child and may not bypass distal tracheomalacia or bronchomalacia beyond the tube tip. Before choosing it as the mechanical solution, map the distal airway and define what the tube will actually bypass. Intraluminal airway stents or external splints/stents can be useful in highly selected complex or rescue situations, but migration, granulation, erosion, infection, growth, and adjacent-structure concerns prevent routine use as a simple first-line solution. Newer external-stent/tracheopexy approaches are promising but remain evolving evidence rather than a settled universal standard.

Failure analysis — persistent symptoms after an operation demand a new dynamic airway map and remap of the mechanism, not reflex repetition of the same procedure. Ask whether the original geometry was wrong, whether bronchomalacia was missed, whether posterior intrusion remains after anterior aortopexy, whether vascular or esophageal anatomy still compresses the airway, whether fixation failed, and whether aspiration, infection, or another airway lesion is driving the current physiology. A technically successful tracheal operation can fail clinically if important mainstem disease was never addressed. Acute deterioration always returns to first principles: restore oxygenation and ventilation first, then reassess the anatomy.

Textbook-versus-current-evidence distinction — Cummings, Pasha, and K.J. Lee preserve the durable principles: recognize dynamic expiratory disease, understand associated foregut and vascular anatomy, use bronchoscopy to define the airway, use positive pressure as an airway splint, and reserve major intervention for important physiology. Current society and peer-reviewed literature refine rather than erase those principles. The ERS statement favors flexible bronchoscopy under free breathing and recognizes dynamic imaging as an adjunct while emphasizing the absence of a universal severity scale. Modern specialty centers increasingly select aortopexy, posterior tracheopexy, bronchopexy, or combinations according to the actual direction and extent of collapse. A 2026 posterior-tracheopexy meta-analysis reported high symptom-improvement rates, but its 14 included studies were observational; comparative prospective evidence is still needed, so the curriculum must explicitly avoid claiming universal superiority for one technique.

Senior synthesis — use five questions. PHYSIOLOGY: are the spells, infections, secretion problems, growth effects, or ventilator dependence truly produced by dynamic central-airway collapse? DYNAMICS: was the airway actually observed during free/spontaneous breathing rather than only while positive pressure held it open? MAP: were the whole trachea and both mainstem bronchi examined? GEOMETRY: is the dominant problem anterior vascular compression, posterior membranous intrusion, circumferential weakness, bronchomalacia, or a combination? MATCH: does the treatment actually correct that geometry — observation and airway clearance for mild disease, CPAP/PEEP for pneumatic support, aortopexy for appropriate anterior compression, posterior/combined tracheopexy for posterior or multidirectional collapse, bronchopexy for meaningful bronchial disease, and selected tracheostomy/stenting only when their mechanics truly solve the problem? The dangerous alternatives are diagnosing from static imaging, allowing positive pressure to hide the lesion, grading severity by collapse percentage alone, missing vascular compression or bronchomalacia, treating reflux or steroids as a malacia cure, forcing a diagnostic maneuver through deteriorating oxygenation, and choosing an operation before defining the direction and extent of collapse."""

COHORT = {
    QID: {
        "concept_id": CID,
        "canonical_topic": TOPIC,
        "prompt": PROMPT,
        "answer_text": ANSWER,
        "explanation": "Pediatric tracheobronchomalacia is a dynamic physiology-and-geometry problem: prove clinically important collapse under conditions that do not mask it, map tracheal and bronchial involvement plus vascular compression, preserve oxygenation during assessment, support mild disease, and choose surgery by the direction and consequences of collapse rather than by a percentage threshold.",
        "board_pearl": "Positive pressure can splint a malacic airway and understate severity. Map the airway dynamically, including both main bronchi and vascular relationships; oxygenation outranks diagnostic purity; then match the operation to geometry rather than reflexively choosing aortopexy or tracheostomy.",
        "depth_layers_v212": {
            "foundation": "Differentiate tracheomalacia, bronchomalacia and tracheobronchomalacia; distinguish intrinsic weakness from extrinsic compression; link symptoms to dynamic expiratory physiology.",
            "application": "Use free-breathing dynamic flexible bronchoscopy plus selective dynamic/vascular imaging, recognize positive-pressure masking, inspect distal bronchi, and apply airway-clearance/CPAP/PEEP support appropriately.",
            "senior_decision": "Escalate consequential disease and match aortopexy, posterior/combined tracheopexy, bronchopexy or other bronchus-directed surgery, tracheostomy, or selected stenting to the actual collapse geometry and rescue needs.",
        },
        "common_traps_v212": [
            "Diagnosing tracheomalacia from a static airway image without demonstrating dynamic expiratory collapse.",
            "Assessing the airway only under substantial positive-pressure ventilation and falsely concluding that collapse is mild because the pressure has stented it open.",
            "Treating a percentage-collapse threshold as the disease rather than integrating cyanotic spells, infections, growth, extubation failure and respiratory-support dependence.",
            "Stopping bronchoscopy after finding tracheal collapse and missing clinically important right- or left-mainstem bronchomalacia.",
            "Calling every pulsatile anterior indentation intrinsic tracheomalacia without defining vascular-ring, sling, innominate or other cardiovascular compression.",
            "Choosing aortopexy automatically before distinguishing anterior compression from posterior membranous intrusion, bronchomalacia, or multidirectional collapse.",
            "Prescribing chronic reflux medication or systemic steroids specifically to cure malacia without a separate evidence-based indication.",
            "Assuming every symptomatic infant will outgrow the disease despite cyanotic/near-death spells, recurrent pneumonia, failure to extubate or ongoing ventilator dependence.",
            "Using tracheostomy as an automatic definitive endpoint without asking whether distal tracheal or bronchial collapse persists beyond the tube.",
            "Using an intraluminal or external airway stent as a routine first-line shortcut without accounting for migration, granulation, erosion, growth and evolving evidence.",
            "Persisting with a diagnostic spontaneous-breathing plan during dangerous hypoxemia instead of restoring oxygenation/ventilation and positive pressure, then interpreting the airway under the support required for safety.",
            "Repeating the same operation after persistent symptoms without remapping for missed bronchomalacia, residual posterior intrusion, persistent vascular compression, aspiration/infection or fixation failure.",
        ],
        "deliberate_review_v212": "Reconciled on 2026-09-07 after the combined v20.11/v20.12 production lineage exposed a fail-closed semantic regression. The exact live canonical concept retains the richer v20.12 free-breathing/positive-pressure physiology, complete tracheobronchial mapping, anatomy-directed aortopexy versus posterior/combined tracheopexy/bronchopexy decisions, rescue and failure analysis, while explicitly preserving the earlier validated v20.11 safety semantics rather than weakening that gate.",
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
