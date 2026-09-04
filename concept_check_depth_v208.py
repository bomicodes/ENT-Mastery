"""v20.8 — deepen the exact live General ENT / Emergencies Epistaxis Concept Check.

Durable nasal vascular anatomy and operative control principles are cross-checked against the
connected ENT Boards Library copies of Cummings 7e, Pasha 6e, and K.J. Lee 12e. Management is
aligned to the current AAO-HNSF Clinical Practice Guideline: Nosebleed (Epistaxis).
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V208 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed., epistaxis/nasal vascular anatomy and endoscopic control sections (connected ENT Boards Library).","role":"foundation/operative: septal and lateral-wall vascular anatomy, anterior versus posterior source localization, endoscopic control and complications"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed., epistaxis sections (connected ENT Boards Library).","role":"foundation/management: initial compression, topical therapy, cautery, packing, posterior bleeding and operative escalation"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed., epistaxis and nasal vascular anatomy sections (connected ENT Boards Library).","role":"foundation/operative: Kiesselbach/Little area, posterior arterial supply, packing and surgical control principles"},
 {"type":"guideline","citation":"Tunkel DE, et al. Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020;162(1_suppl):S1-S38. PMID:31910111. Current AAO-HNSF guideline listing rechecked 2026-09-04.","role":"current management: sustained compression, packing when source cannot be identified, resorbable packing in anticoagulated/bleeding-risk patients, endoscopy indications, targeted treatment, ligation/embolization escalation, and anticoagulation boundary"},
]

QID="cc-v112-rec-general-ent-emergencies-epistaxis"
CID="v6-general-ent-emergencies-epistaxis"
TOPIC="Epistaxis"

ANSWER="""Foundation — treat active epistaxis as a localization-and-control problem while first deciding whether the patient is physiologically unstable. Start with airway, breathing and circulation when bleeding is brisk, bilateral, posterior into the pharynx, or associated with hemodynamic compromise. Suction clots so you can actually see the nasal cavity; do not confuse blood coating the nose with the bleeding source. Ask about anticoagulants/antiplatelets, bleeding disorders, prior nasal surgery or trauma, recurrent unilateral bleeding, intranasal drug use, hypertension as a contributor to severity, and a personal/family history suggesting hereditary hemorrhagic telangiectasia.

First-line control — for an active nosebleed without immediate airway/hemodynamic catastrophe, apply firm sustained compression to the lower third of the nose for at least 5 minutes. Topical vasoconstrictor and local anesthetic can improve visualization and control. The key teaching point is that compression is a real therapeutic step, not a few seconds of pinching while assembling instruments.

Localize before cauterizing — after clot evacuation and topical preparation, inspect the anterior septum and then the remainder of the cavity. Most routine anterior bleeds arise around Little/Kiesselbach area, but persistent blood in the posterior nasal cavity or nasopharynx, failure of appropriate anterior control, or inability to visualize an anterior source should raise concern for a posterior source. If the site is identified, treat that site with an appropriate intervention such as topical vasoconstrictor, chemical/electrocautery, or moisturizing/lubricating therapy according to the lesion and clinical context. Cauterize only the active or suspected bleeding site rather than broadly injuring opposing septal surfaces.

Packing — if ongoing bleeding prevents identification of the source despite compression and suction, nasal packing is appropriate. Choose the packing strategy to the suspected location and patient risk. In a patient on anticoagulants/antiplatelets or with a bleeding disorder, current AAO-HNS guidance favors resorbable packing. Packing is not the endpoint: document what was placed, whether it is resorbable, the removal/follow-up plan, and symptoms that require urgent reassessment. Posterior packing can compromise the airway, cause significant pain and cardiopulmonary stress, and generally warrants closer monitoring than a simple anterior pack.

Endoscopy — recurrent bleeding despite prior packing/cautery, recurrent unilateral epistaxis, difficult-to-control bleeding, or concern for an unrecognized lesion should trigger nasal endoscopy or referral to someone who can perform it. The purpose is not merely to label the bleed 'posterior'; it is to identify a specific source or pathology and choose targeted therapy. A unilateral recurrent bleed with obstruction or a mass deserves evaluation for tumor rather than repeated empiric packing.

Escalation — persistent or recurrent bleeding not controlled by packing and targeted cautery should prompt evaluation for surgical arterial ligation or endovascular embolization. In the OR, endoscopic sphenopalatine-artery control is a common definitive strategy for posterior epistaxis; success depends on exposing the relevant posterior lateral nasal wall/foramen region and controlling the arterial branches rather than clipping a presumed single trunk without verifying hemostasis. Embolization is an alternative or complementary option when anatomy, comorbidity, surgical access, recurrence, or institutional expertise favors it. The choice is patient- and source-specific, not a reflex hierarchy in every case.

Anticoagulation boundary — anticoagulants and antiplatelet drugs increase bleeding severity, but they do not automatically become the first treatment target. In the absence of life-threatening bleeding, AAO-HNS guidance recommends first-line local measures before transfusion, reversal, or withdrawal of anticoagulation/antiplatelet therapy. For life-threatening hemorrhage, reversal and resuscitation decisions become multidisciplinary and depend on the drug, indication, timing and thrombotic risk.

HHT and recurrent disease — recurrent bilateral epistaxis or a family history of recurrent nosebleeds should prompt examination for nasal/oral telangiectasias and consideration of hereditary hemorrhagic telangiectasia. This is different from the isolated adult with a single anterior septal vessel and prevents the Concept Check from teaching every recurrent bleed as simply 'needs cautery.'

Senior synthesis — use STABILIZE, COMPRESS, SUCTION/LOCALIZE, TARGET, PACK, SCOPE, ESCALATE. Stabilize true major hemorrhage; use sustained compression; clear clot and localize the source; target visible bleeding rather than blind bilateral cautery; pack when visualization fails; use endoscopy for recurrent/unilateral/difficult bleeding; and escalate persistent disease to ligation or embolization. The major errors are skipping adequate compression, packing without a follow-up/removal plan, repeatedly treating a unilateral recurrent bleed without looking for pathology, reversing anticoagulation before appropriate local measures in non-life-threatening bleeding, and allowing repeated posterior packing to substitute indefinitely for definitive source control."""

COHORT={QID:{
 "concept_id":CID,
 "canonical_topic":TOPIC,
 "prompt":"An older adult on apixaban presents with brisk spontaneous epistaxis. He is protecting his airway and is not hypotensive, but blood continues despite several brief attempts at pinching the nose and the ED cannot identify a source. As the ENT resident, walk through the sequence from effective first-line compression and localization through cautery or packing, when nasal endoscopy is indicated, how anticoagulation changes packing/reversal decisions, and when to move to arterial ligation or embolization?",
 "answer_text":ANSWER,
 "explanation":"Epistaxis care should progress from physiology and effective compression to source localization and targeted control. The important resident distinctions are when packing is needed because visualization fails, when recurrent/unilateral disease requires endoscopy, when anticoagulation should not distract from local first-line treatment, and when persistent bleeding has crossed the threshold for definitive arterial control.",
 "board_pearl":"Do not call compression a failure until it has been firm and sustained. If bleeding prevents localization, pack; if recurrent or difficult bleeding persists, scope; if packing/cautery fail, evaluate for ligation or embolization. In non-life-threatening bleeding, treat locally before reflex anticoagulant reversal.",
 "depth_layers_v208":{
  "foundation":"Know anterior versus posterior nasal vascular anatomy, effective compression, clot evacuation, topical vasoconstriction and source-directed cautery.",
  "application":"Choose packing when the source cannot be seen, use resorbable material for increased bleeding risk, and use endoscopy for recurrent unilateral or difficult-to-control bleeding.",
  "senior_decision":"Recognize failure of packing/cautery, select SPA ligation versus embolization, manage anticoagulation proportionally to bleeding severity, and investigate recurrent disease such as HHT or neoplasm."
 },
 "common_traps_v208":[
  "Declaring compression ineffective after a few seconds. Effective first-line compression is firm and sustained over the lower third of the nose for at least 5 minutes.",
  "Cauterizing broadly without identifying a likely site. Excess mucosal injury can worsen crusting and septal injury while still missing a posterior source.",
  "Using nonresorbable packing by default in a patient with an anticoagulant or bleeding disorder when current guidance favors resorbable packing for increased bleeding risk.",
  "Treating packing as definitive follow-through. Patients need the packing type, removal plan when applicable, aftercare and clear return precautions documented.",
  "Calling recurrent unilateral epistaxis 'posterior' and repeatedly packing without nasal endoscopy or evaluation for an unrecognized lesion.",
  "Reversing anticoagulation immediately in a stable non-life-threatening bleed before applying appropriate local first-line treatments and considering the thrombotic indication for the drug.",
  "Repeating posterior packs indefinitely after failed cautery/packing instead of evaluating for definitive surgical arterial ligation or endovascular embolization.",
  "Assuming all recurrent epistaxis is local trauma and missing HHT clues such as recurrent bilateral bleeding, family history, and nasal/oral telangiectasias."
 ],
 "deliberate_review_v208":"Prioritized from the residual shallow Concept Check backlog because Epistaxis is common, high-yield, and management errors frequently arise from sequence failure: inadequate compression, poor localization, inappropriate packing/reversal, delayed endoscopy, and delayed definitive arterial control.",
 "source_refs_v208":SOURCE_REFS_V208,
}}

def apply_concept_check_task_alignment_v208(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v208','common_traps_v208','deliberate_review_v208','source_refs_v208'): q[field]=p[field]
  q['task_alignment_v208']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
