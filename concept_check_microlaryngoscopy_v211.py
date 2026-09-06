"""Focused v20.11 depth patch for exact-live Microlaryngoscopy Concept Checks.

Durable exposure, laryngeal microanatomy, palpation, and phonomicrosurgical principles
are grounded in connected Cummings 7e, Pasha 6e, and K.J. Lee 12e. Current evidence
updates patient selection and suspension-force safety without weakening the existing
shared-airway/laser rescue lineage.
"""
from concept_check_board_repair_v177 import _find_module

CID="v6-laryngology-voice-swallowing-microlaryngoscopy"
TOPIC="Microlaryngoscopy"
QIDS=(
 "cc-v112-mgt-laryngology-voice-swallowing-microlaryngoscopy",
 "cc-v112-rec-laryngology-voice-swallowing-microlaryngoscopy",
)

SOURCE_REFS_V211_MICROLARYNGOSCOPY=[
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive split copy; laryngeal examination/microlaryngoscopy material reviewed 2026-09-06.","role":"foundation/operative: direct inspection beyond office examination, lesion palpation, biopsy, and angled-optic assessment of the anterior commissure, ventricle, and undersurface of the true vocal fold"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy; laryngology and pediatric airway microlaryngoscopy sections reviewed 2026-09-06.","role":"resident framework: indications for direct examination/lesion removal and airway assessment when office examination is insufficient"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy; phonomicrosurgery material reviewed 2026-09-06.","role":"operative cross-check: preoperative endoscopy/stroboscopy, conservative treatment for selected benign lesions, lesion depth, microflap technique, and scar risk near the vocal ligament"},
 {"type":"guideline","citation":"Stachler RJ, et al. Clinical Practice Guideline: Hoarseness (Dysphonia) (Update). Otolaryngol Head Neck Surg. 2018;158(1_suppl):S1-S42. DOI 10.1177/0194599817751030.","role":"society guidance: visualize the larynx before voice therapy; reserve surgery for malignancy or appropriate symptomatic benign lesions when conservative care is inadequate rather than treating surgery as first-line for most dysphonia"},
 {"type":"prospective_trial","citation":"Feng AL, et al. Laryngeal Force Sensor for Suspension Microlaryngoscopy: A Prospective Controlled Trial. Otolaryngol Head Neck Surg. 2021;165(2):320-327. PMID 33399514.","role":"current operative safety: maximum suspension force predicted postoperative extralaryngeal complications and active force monitoring reduced force exposure/complications"},
 {"type":"prospective_study","citation":"Risk Factors for Lingual Nerve Injury Associated With Suspension Laryngoscopy. PMID 30841712 (2019).","role":"operative risk: difficult suspension/intubation and longer operative time were associated with postoperative lingual-nerve symptoms"},
 {"type":"systematic_review","citation":"Miri M, et al. Surgical and Voice Outcomes of Office-Based Laser Therapy for Benign Lesions of the Vocal Folds: A Systematic Review of the Literature. J Voice. 2025. DOI 10.1016/j.jvoice.2025.09.035; PMID 41162263.","role":"current selection nuance: selected benign vocal-fold lesions may be treated effectively in-office, with heterogeneous low-to-moderate-quality evidence, so suspension microlaryngoscopy is not obligatory for every benign lesion"},
]

PROMPT="""An adult with persistent dysphonia has a small subepithelial true-vocal-fold lesion on office endoscopy/stroboscopy and is scheduled for suspension microlaryngoscopy. How should you decide whether the lesion actually needs OR intervention, obtain exposure without causing avoidable dental/tongue injury, use palpation and microanatomic depth to choose biopsy versus phonomicrosurgery, preserve the vibratory cover, and know when poor exposure or shared-airway risk should make you change or stop the plan rather than force the operation?"""

ANSWER="""Foundation — microlaryngoscopy is not simply 'put in a laryngoscope and remove the lesion.' Start by defining the clinical question before the patient reaches the OR. Correlate the history, perceptual voice complaint, office flexible/rigid laryngoscopy and—when the question is vibratory function—stroboscopy. Decide whether you are trying to exclude malignancy, obtain tissue diagnosis, characterize a lesion that cannot be adequately assessed in clinic, restore voice by phonomicrosurgery, treat recurrent disease, or evaluate an airway. A benign-appearing phonotraumatic lesion should not automatically become an operation: current dysphonia guidance supports laryngeal visualization and appropriate conservative/voice therapy first when the lesion and patient goals make that reasonable. Suspicion for malignancy, an indeterminate lesion, failure of appropriate conservative treatment, or a lesion whose depth/behavior requires direct examination changes that threshold.

Know what direct microlaryngoscopy adds. Compared with office visualization, suspension under anesthesia permits stable binocular magnification, bimanual instrumentation, careful palpation, precise biopsy/excision and use of angled optics to inspect regions that may be incompletely seen straight-on. Cummings specifically preserves the value of palpation and angled-endoscope inspection of areas such as the anterior commissure, ventricle and undersurface of the true fold. A lesion that looks superficially similar in clinic may feel firm, tethered, cystic or deep at microlaryngoscopy, and that tactile information can change the operation.

Exposure is a safety problem, not a contest. Before suspension, inspect dentition and identify loose teeth, crowns, implants, prominent incisors and limited mandibular/neck mobility. Protect teeth and lips; avoid trapping the lip between scope and incisors. Choose the laryngoscope to match the target and patient anatomy rather than repeatedly forcing one scope. Optimize head/neck position, tongue placement, external counterpressure when appropriate and suspension vector. If the anterior commissure or lesion remains poorly seen, change the scope, position, assistant-applied laryngeal pressure, telescope angle or operative strategy before escalating force.

Current-evidence distinction — traditional textbooks correctly teach suspension exposure as the platform for precise laryngeal microsurgery, but newer prospective evidence makes the force itself part of the risk calculation. Maximum suspension force predicts postoperative extralaryngeal complications, and difficult suspension plus longer operative time increases lingual-nerve injury risk. Therefore 'I can eventually expose it if I crank harder' is not a senior endpoint. Excessive force, progressive tongue compression, dental loading or a deteriorating risk/benefit ratio should trigger repositioning, a different laryngoscope/optic, a staged/alternative approach, or abandonment of an elective maneuver.

Shared-airway plan — agree with anesthesia before suspension about the ventilation strategy, endotracheal-tube position/size, whether intermittent apnea or another tubeless technique is contemplated, and what event mandates immediate loss of suspension so ventilation can be restored. The exact technique is individualized to lesion, airway, equipment and team expertise. Oxygenation outranks exposure. If ventilation becomes unreliable, saturation falls, airway pressures become unsafe or an airway fire/energy emergency occurs, stop the laryngeal maneuver and execute the existing shared-airway rescue plan rather than protecting the surgical view.

Map the vocal-fold layers before cutting. The epithelium and superficial lamina propria form the pliable vibratory cover over deeper intermediate/deep lamina propria and vocal ligament, with thyroarytenoid muscle deeper still. For voice-preserving surgery, the objective is not maximal tissue removal; it is removal or treatment of pathology while preserving as much normal epithelium and superficial lamina propria as possible. Violating or stripping the vocal ligament, creating opposing raw surfaces, thermal injury or excessive normal-tissue resection can convert a small benign lesion into permanent stiffness/scar.

Palpate before committing. Use fine instrumentation to determine whether the lesion is epithelial, subepithelial, cystic, fibrous, vascular, infiltrative or tethered to deeper tissue. A superficial polyp may permit a limited microflap/excision that preserves surrounding cover. A cyst can extend deeper than it appears and may be adherent near the ligament; chasing every fragment at the cost of ligament or cover injury can produce worse voice than a deliberately conservative endpoint. A firm infiltrative or suspicious lesion changes the goal from cosmetic voice surgery to oncologically appropriate biopsy with adequate depth and orientation.

Biopsy versus phonomicrosurgery — if malignancy is a real concern, obtain diagnostically useful tissue and do not let a voice-preservation maneuver under-sample an infiltrative lesion. Conversely, when treating a benign lesion for voice, avoid an unnecessarily broad or deep 'biopsy' that sacrifices normal cover. The senior decision is driven by the diagnostic probability and depth: oncologic adequacy when cancer is plausible; microstructural preservation when benign disease is established. Label specimens and communicate exact site/laterality so pathology can be reconciled with the operative map.

Microflap principles — create only the exposure required, elevate in the safest tissue plane, preserve viable epithelium, dissect the lesion away from normal superficial lamina propria/ligament with fine cold instruments when appropriate, control bleeding without indiscriminate thermal spread, and redrape the cover without excess tension or missing epithelium. Avoid grasping the free edge of normal vocal fold when a less traumatic point of manipulation exists. When energy devices are used, the already-validated laser/energy-safety rules remain active: wavelength-specific eye protection, smoke control, oxidizer coordination, lowest effective energy and explicit airway-fire rescue.

Anterior commissure and bilateral disease require restraint. Opposing raw surfaces risk web formation. If bilateral lesions or disease near the anterior commissure would require broad opposing denudation, consider staged treatment or a tissue-preserving plan rather than creating a predictable scar bridge. Difficult anterior exposure is also a reason to use angled optics or alter the approach—not a reason to lever harder on the teeth/tongue.

Current alternatives — office-based procedures have expanded. Selected cooperative patients with appropriate benign lesions may be candidates for office-based laser or other interventions, and 2025 systematic-review data report generally favorable lesion/voice outcomes but heterogeneous low-to-moderate-quality evidence. This does not eliminate OR microlaryngoscopy: suspension remains valuable when precise bimanual dissection, palpation, definitive biopsy, airway control, difficult location or patient tolerance requires it. The updated teaching is selection by task, not an automatic hierarchy in which every benign lesion must go to the OR.

Postoperative/rescue assessment — new tongue numbness, dysgeusia, severe tongue pain or weakness after suspension suggests compression/lingual-nerve injury and should be documented and followed rather than dismissed. Dental pain or a loose/chipped tooth warrants examination. New stridor, respiratory distress, expanding edema, significant bleeding, aspiration or inability to manage secretions requires urgent airway/laryngeal reassessment. Persistent or worsened dysphonia after healing should prompt repeat visualization/stroboscopic assessment for residual lesion, hemorrhage, stiffness/scar, web or an incorrect initial diagnosis rather than reflex repeat excision.

Senior synthesis — use six checks. INDICATION: what question requires the OR and could conservative/office management answer it more safely? EXPOSURE: can I see the target with acceptable dental/tongue force, and what will I change before adding more force? AIRWAY: how will we ventilate and what triggers immediate rescue? DEPTH: is pathology in epithelium, superficial lamina propria, ligament or deeper tissue? GOAL: is this oncologic biopsy or voice-preserving phonomicrosurgery? PRESERVATION: what normal cover/ligament can I leave untouched, and am I creating opposing raw surfaces or thermal injury? The dangerous errors are operating without adequate preoperative laryngeal characterization, forcing exposure despite escalating suspension injury, under-biopsying suspected cancer, over-resecting a benign lesion into the vocal ligament, creating an anterior web, and valuing exposure over oxygenation."""

COMMON_TRAPS=[
 "Scheduling OR excision of every benign-appearing vocal-fold lesion without first defining the diagnosis, patient goal, stroboscopic findings and whether appropriate voice/conservative therapy could avoid surgery.",
 "Treating suspension exposure as a contest and escalating force on teeth, tongue and floor of mouth instead of changing scope, position, counterpressure, optics or operative plan.",
 "Failing to document vulnerable dentition and protect teeth/lips before suspension, then discovering a crown or incisor injury after the case.",
 "Accepting prolonged tongue compression during difficult suspension despite the association of difficult/long suspension with lingual-nerve symptoms and dysgeusia.",
 "Skipping lesion palpation and assuming the depth/consistency seen in the office is the same as the operative microanatomy.",
 "Using a deep or broad biopsy for an established benign voice lesion and sacrificing normal superficial lamina propria or vocal ligament that determines postoperative vibration.",
 "Performing an overly superficial voice-preserving biopsy when malignancy is plausible and leaving pathology without diagnostically adequate tissue.",
 "Creating opposing raw surfaces at the anterior commissure or on bilateral folds and producing avoidable web/scar instead of staging or preserving epithelium.",
 "Using laser/energy without carrying forward the validated oxidizer, eye-protection, plume and airway-fire rescue rules because the case is labeled 'microlaryngoscopy.'",
 "Continuing an elective laryngeal maneuver when ventilation/oxygenation becomes unreliable rather than immediately releasing the shared-airway conflict and restoring ventilation.",
]

COHORT_MICROLARYNGOSCOPY_V211={qid:{
 "concept_id":CID,"canonical_topic":TOPIC,"prompt":PROMPT,"answer_text":ANSWER,
 "explanation":"Microlaryngoscopy is a task-selected, microanatomy-preserving shared-airway operation: characterize the lesion first, obtain the least-traumatic adequate exposure, palpate and map depth, distinguish oncologic biopsy from phonomicrosurgery, preserve vibratory cover, and stop force escalation or surgery when exposure/oxygenation risk exceeds benefit.",
 "board_pearl":"Poor exposure is not permission to increase suspension force indefinitely. Change scope/position/optics or abandon an elective maneuver; preserve epithelium and superficial lamina propria for benign voice surgery, but obtain adequate depth when malignancy is plausible.",
 "depth_layers_v211":{"foundation":"Preoperative laryngeal/stroboscopic characterization, direct-exam advantages, vocal-fold layered microanatomy, and suspension/shared-airway fundamentals.","application":"Protect teeth/tongue, optimize exposure, palpate lesion depth, choose biopsy versus microflap/phonomicrosurgery, and preserve vibratory cover/ligament.","senior_decision":"Recognize force/time as safety variables, choose OR versus conservative/office management, stop or change strategy for poor exposure/oxygenation, avoid anterior web/scar and rescue postoperative airway, dental or lingual-nerve complications."},
 "common_traps_v211":COMMON_TRAPS,
 "deliberate_review_v211":"Selected from the exact live post-v35.1 production backlog because both exact Microlaryngoscopy Concept Checks remained approximately 11-word reveals despite high resident/board/OR value. Depth was intentionally prioritized over higher lexical ranks. The patch preserves textbook operative microanatomy while adding current evidence that suspension force/duration are modifiable safety variables and that selected benign lesions may have conservative or office-based alternatives.",
 "source_refs_v211":SOURCE_REFS_V211_MICROLARYNGOSCOPY,
} for qid in QIDS}


def apply_microlaryngoscopy_v211(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT_MICROLARYNGOSCOPY_V211.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v211','common_traps_v211','deliberate_review_v211','source_refs_v211'): q[field]=p[field]
  q['choices']=[]; q['answer']=None; q['task_alignment_v211']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
