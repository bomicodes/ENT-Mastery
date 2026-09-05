"""v20.11e focused depth patch for Frontal Sinusotomy / Draf Procedures."""
from concept_check_board_repair_v177 import _find_module

CID="v6-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures"
TOPIC="Frontal Sinusotomy / Draf Procedures"
QIDS=(
 "cc-v112-mgt-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures",
 "cc-v112-rec-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures",
)

SOURCE_REFS_V211_DRAF=[
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive split Part 1 (pages 1-659); frontal sinus disease/surgery material. Current Drive copy reviewed 2026-09-05; selected persistent frontal outflow obstruction may be treated with endoscopic Draf III while alternative open/obliterative strategies remain situation-dependent.","role":"foundation/operative cross-check: frontal sinus outflow anatomy, escalation beyond limited frontal recess surgery, and open/endoscopic alternatives"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), Chapter 1 Allergy and Rhinology, Sinus Surgery pp. 61-64; frontal sinusotomy figure/classification reviewed in connected Google Drive 2026-09-05.","role":"board framework: Draf I/IIa/IIb/III extent and frontal sinus operative taxonomy"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), Chapter 33 Endoscopic Sinus Surgery, pp. 575-596; connected Google Drive text reviewed 2026-09-05.","role":"operative framework: Draf boundaries, angled instrumentation, drill-out indications, trephination and osteoplastic-flap alternatives"},
 {"type":"consensus","citation":"Lucidi D, et al. Surgical Adequacy in Endoscopic Sinus Surgery for Primary Diffuse Chronic Rhinosinusitis: Expert Consensus Recommendations. Laryngoscope. Published online 2026-01-14. DOI 10.1002/lary.70365.","role":"current management: at least Draf I in primary diffuse CRS when frontal disease is addressed; Draf III should not be routine first-line surgery even in recurrence-risk patients"},
 {"type":"meta_analysis","citation":"Shahid MS, et al. Comparative Restenosis and Revision Rates of Draf IIB Versus Draf III Frontal Sinusotomy in Chronic Rhinosinusitis: A Meta-Analysis Stratified by Endotype. OTO Open. Published online 2026-06-16. DOI 10.1177/19458924261456359.","role":"current outcomes: procedure extent and inflammatory endotype affect restenosis/revision risk; supports individualized escalation rather than automatic maximal drill-out"},
 {"type":"meta_analysis","citation":"Lein A, et al. Mucosal Grafts and Flaps in Draf IIb and Draf III: A Systematic Review and Meta-analysis. Otolaryngol Head Neck Surg. Published 2025-08-04. DOI 10.1002/ohn.1374.","role":"current technical evidence: mucosal reconstruction may improve Draf III neo-ostium patency and reduce neo-ostium area loss"},
 {"type":"systematic_review","citation":"Chiari F, et al. Clinical features, operative management and surgical results of first Draf III procedure, revision Draf III approach and the use of mucosal flaps and stents: a systematic review. Eur Arch Otorhinolaryngol. 2024. PMID 39237772.","role":"current outcome cross-check: common indications, primary versus revision success, restenosis risk and mucosal-flap versus stent considerations"},
]

ANSWER="""Foundation — the Draf classification describes how much of the frontal recess and frontal sinus floor is opened, but the senior decision is not “which number is bigger?” It is: what disease must be reached, what anatomy limits safe access, and how much durable drainage is needed without creating unnecessary morbidity. Review the CT in three planes before surgery. Identify the frontal beak, agger nasi and frontal cells, skull-base slope, lamina papyracea, anterior ethmoid artery region, interfrontal sinus septum, middle turbinate attachment, and the narrowest anteroposterior dimension available for instruments. The orbit is lateral, the skull base is superior/posterior, and loss of orientation in a scarred frontal recess can convert a drainage operation into orbital or intracranial injury.

Draf I — this is frontal recess clearance below the frontal ostium rather than a formal drill-out of the frontal sinus floor. Superior ethmoid partitions obstructing drainage are removed while preserving the frontal sinus ostium/floor. It fits disease in which restoring the natural pathway is adequate. The mistake is to call every frontal recess dissection a Draf II simply because the frontal sinus becomes visible.

Draf IIa — widen one frontal outflow tract from the lamina papyracea laterally to the middle turbinate medially. This is a unilateral frontal sinusotomy that enlarges the natural opening without extending to the nasal septum. It is a common escalation for frontal CRS when standard recess clearance is inadequate. The operative endpoint is a wide mucosa-respecting drainage pathway, not a small circular hole surrounded by stripped bone.

Draf IIb — extend the unilateral opening medially to the nasal septum, generally requiring removal/drilling of the frontal sinus floor medial to the middle turbinate attachment. This is useful when unilateral disease needs a larger aperture, when the ostium is stenotic or osteitic, or when access is needed for selected unilateral pathology. It provides substantially more access than IIa without obligating a bilateral common cavity. The surgeon must understand the first olfactory fiber/ventral olfactory fossa region and avoid drifting superiorly or laterally while drilling.

Draf III, or endoscopic modified Lothrop — create a common bilateral frontal neo-ostium by joining bilateral IIb cavities, removing the superior anterior nasal septum and interfrontal sinus septum and drilling the frontal sinus floor from orbit toward orbit. This is not simply “the best Draf.” It is an extended drill-out used for refractory frontal disease after lesser approaches, severe scarring/osteitis in selected cases, mucoceles, access to selected tumors or skull-base pathology, and other situations in which a large common cavity provides a meaningful advantage. Contemporary expert consensus argues against routine first-line Draf III for primary diffuse CRS; extent should match the disease and prior treatment history.

Application — choose the least extensive operation that reliably treats the actual pathology. A primary patient with inflammatory CRS and usable anatomy usually deserves mucosa-preserving frontal recess/limited frontal sinusotomy before maximal drill-out. A unilateral scarred or osteitic frontal outflow tract may be better served by IIb than by automatically creating a bilateral III. A patient with recurrent bilateral frontal obstruction after adequate prior surgery, a difficult mucocele, or pathology requiring broad bilateral access may justify III. Far-lateral disease that cannot be reached safely endonasally can require trephination or a combined approach; recalcitrant disease, osteomyelitis, tumors, or anatomy outside the endoscopic corridor may still require an osteoplastic or other open strategy. “Endoscopic” is not synonymous with “always sufficient.”

Technique and danger zones — expose anatomy before drilling. Angled endoscopes and curved frontal instruments are often necessary; extended IIb/III work may require an angled high-speed drill. Keep the drill controlled and directed away from the skull base and orbit. In revision surgery, do not trust absent landmarks: use fixed boundaries, image review, navigation when appropriate, and deliberate exposure from known safe anatomy. Preserve mucosa wherever possible. Circumferential denudation and excessive thermal injury promote osteitis, granulation and restenosis. A small neo-ostium under tension is not a successful Draf III simply because the interfrontal septum was removed.

Current evidence and restenosis — restenosis is not merely a technical failure; inflammatory endotype matters. A 2026 meta-analysis found higher pooled restenosis and revision in Type-2 CRS and lower pooled rates after IIb than III, although patient selection and disease severity differ between procedures and the data do not prove IIb is universally superior. The practical lesson is to avoid escalating to III solely because it is wider and to optimize the inflammatory disease that will determine long-term healing. Mucosal grafts/flaps over exposed bone after drill-out may improve neo-ostium patency; a 2025 meta-analysis found improved patency and less loss of neo-ostium area with mucosal reconstruction in Draf III data. Stents are not a substitute for a well-created, mucosalized drainage pathway and should be selective rather than routine.

Postoperative strategy — extended frontal surgery requires surveillance. Debridement, saline irrigation and disease-specific topical anti-inflammatory therapy support healing; recurrent polyposis or uncontrolled Type-2 inflammation should be treated as a biologic disease problem rather than answered only with progressively larger drills. Follow the neo-ostium for edema, crusting, scar contraction and early restenosis. A narrowing opening that can be treated while still accessible is preferable to waiting for complete closure and another revision.

Rescue and complications — suspected CSF leak means stop, identify the defect, protect intracranial structures and repair appropriately rather than continuing blind drilling. Orbital fat exposure or bleeding demands immediate orientation to the lamina/orbit and assessment for orbital injury; postoperative visual loss, proptosis or an afferent pupillary defect is an emergency. Significant arterial bleeding near the skull base requires controlled hemostasis with awareness that blind cautery can worsen injury. If the frontal sinus cannot be safely reached because anatomy is too narrow, scarred, lateral or distorted, change the approach—trephination, combined access or open surgery can be safer than forcing a drill through an unsafe corridor.

Senior synthesis — make five decisions. DISEASE: unilateral versus bilateral, inflammatory versus mucocele/tumor/other focal pathology, primary versus revision. MAP: define frontal cells, skull base, orbit, frontal beak, septum and instrument corridor on CT. EXTENT: Draf I restores the recess; IIa opens to the middle turbinate; IIb extends to the septum; III creates a bilateral common cavity. HEALING: preserve/reconstruct mucosa and control the inflammatory endotype because patency is a biologic as well as technical outcome. BAILOUT: if safe orientation or access is lost, stop and change the corridor rather than converting uncertainty into an orbital or intracranial complication."""

PROMPTS={
 QIDS[0]:"""A patient with chronic frontal sinus disease has persistent symptoms and radiographic frontal outflow obstruction despite appropriate medical therapy. CT shows a scarred frontal recess, and the surgeon is deciding between a Draf IIa, IIb, or III procedure. How should the surgeon choose the extent of frontal sinusotomy, what are the operative boundaries and danger zones, and when should a combined or open approach be chosen instead?""",
 QIDS[1]:"""During preoperative review for revision frontal sinus surgery, a resident is asked to explain the Draf classification and why the most extensive procedure is not automatically the best procedure. How do Draf I, IIa, IIb, and III differ anatomically, what pathology typically justifies escalation, and what findings should make the surgeon stop or choose another corridor?""",
}

COMMON_TRAPS=[
 "Treating the Draf classification as a memorized number sequence without connecting each procedure to anatomic boundaries and indication.",
 "Calling simple frontal recess clearance a Draf II because the frontal ostium becomes visible.",
 "Escalating primary diffuse CRS directly to Draf III merely because a larger opening seems more durable.",
 "Performing bilateral Draf III for unilateral disease that can be adequately treated with a IIb approach.",
 "Drilling in a revision frontal recess before re-establishing fixed skull-base and orbital landmarks.",
 "Creating a technically wide opening while stripping circumferential mucosa and thereby promoting osteitis and restenosis.",
 "Ignoring Type-2 inflammatory disease and interpreting every recurrent frontal stenosis as a problem solved only by more drilling.",
 "Using a stent routinely as a substitute for adequate neo-ostium creation, mucosal preservation and postoperative surveillance.",
 "Forcing endonasal access to far-lateral or dangerously narrow disease instead of using trephination, a combined corridor or open surgery.",
 "Continuing drilling after suspected CSF leak, orbital entry, major bleeding or loss of orientation instead of stopping and executing a rescue plan.",
]

COHORT_DRAF_V211={}
for qid in QIDS:
 COHORT_DRAF_V211[qid]={
  "concept_id":CID,"canonical_topic":TOPIC,"prompt":PROMPTS[qid],"answer_text":ANSWER,
  "explanation":"Draf selection is an anatomy- and disease-matched escalation decision: preserve mucosa, choose the least extent that reliably treats pathology, anticipate restenosis biology and retain combined/open bailout options.",
  "board_pearl":"Draf IIa opens from lamina papyracea to middle turbinate; IIb extends medially to septum; III joins bilateral IIb cavities into one common frontal neo-ostium. Draf III is an escalation tool, not routine first-line maximal ESS.",
  "depth_layers_v211":{"foundation":"Map the frontal recess, skull base, orbit, middle turbinate, septum and Draf boundaries.","application":"Match I/IIa/IIb/III or combined/open access to unilateral/bilateral disease, scarring, prior surgery and access needs.","senior_decision":"Balance access against mucosal injury and restenosis biology, recognize unsafe endonasal anatomy, and stop for orbital/intracranial danger or loss of orientation."},
  "common_traps_v211":COMMON_TRAPS,
  "deliberate_review_v211":"Expanded after the exact-head post-v20.11d live backlog ranked both management and recognition Frontal Sinusotomy / Draf Procedures questions among the highest remaining clinically valuable shallow concepts. The prior 16-word reveals tested taxonomy rather than operative selection, boundaries, inflammatory restenosis, complication rescue or when not to perform Draf III.",
  "source_refs_v211":SOURCE_REFS_V211_DRAF,
 }

def apply_frontal_draf_v211(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT_DRAF_V211.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v211','common_traps_v211','deliberate_review_v211','source_refs_v211'): q[field]=p[field]
  q['choices']=[]; q['answer']=None; q['task_alignment_v211']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
