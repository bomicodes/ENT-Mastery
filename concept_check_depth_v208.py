"""v20.8 — deepen the exact live General ENT / Emergencies Epistaxis Concept Check.

Durable nasal vascular anatomy and operative hemostasis principles are cross-checked against the
connected textbook corpus. Cummings 7e is present in Drive as the master volume; its Chapter 47
(Epistaxis) identity was verified against the publisher table of contents because the 765-MB Drive
object exceeds connector text-extraction limits. Pasha 6e and K.J. Lee 12e were directly text-
queried in Drive. Management is updated to the current AAO-HNSF Nosebleed CPG and 2026 evidence.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V208 = [
 {"type":"textbook","citation":"Flint PW, et al. Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), Ch 47 Epistaxis. Connected Drive master copy verified; chapter identity cross-checked against Elsevier 7e TOC because the 765-MB Drive PDF exceeds connector extraction limits.","role":"durable foundation/operative cross-reference: nasal vascular anatomy, endoscopic source localization, arterial control and escalation principles; management timing is superseded where newer guidance is more specific"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), Epistaxis pp 28-34; connected Drive copy directly queried.","role":"foundation/application: Kiesselbach anatomy, ABC/IV-access assessment, topical vasoconstrictor temporization, systematic bleeding history and acute-control ladder"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), Ch 26/31 nasal vascular anatomy and disease; connected Drive copy directly queried.","role":"foundation/operative: Kiesselbach arterial contributors, Woodruff plexus anatomy, internal-versus-external carotid anastomotic implications and ethmoidal landmarks"},
 {"type":"society_guideline","citation":"Tunkel DE, et al. Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020;162(1 Suppl):S1-S38. doi:10.1177/0194599819890327. AAO-HNSF guideline confirmed current on Academy site 2026-09-04.","role":"current management: compression, vasoconstrictor/cautery/packing sequence, endoscopy, resorbable packing in bleeding-risk patients, ligation/embolization escalation, anticoagulation and HHT recommendations"},
 {"type":"current_review","citation":"Valencia-Sanchez BA, Donaldson AM. Epistaxis. Med Clin North Am. 2026;110(1):17-30. doi:10.1016/j.mcna.2025.05.003.","role":"2026 evidence-based diagnostic and management review spanning conservative through advanced interventions"},
 {"type":"systematic_review","citation":"Zheng W, et al. Anterior Ethmoid Artery Ligation for Epistaxis: A Systematic Review. Laryngoscope Investig Otolaryngol. 2026;11(2):e70314. doi:10.1002/lio2.70314.","role":"current senior-decision evidence for anterior ethmoidal source control when bleeding is not explained by the sphenopalatine territory"},
 {"type":"systematic_review","citation":"Management of uncontrolled/recurrent epistaxis by ligation or cauterization of the sphenopalatine artery: a scoping review. 2024. PMID:39069575.","role":"refractory posterior epistaxis: endoscopic SPA control efficacy, rebleeding and complication context"},
 {"type":"consensus_guideline","citation":"Second International Guidelines for the Diagnosis and Management of Hereditary Hemorrhagic Telangiectasia. Ann Intern Med. 2020; current guideline portal verified 2026-09-04.","role":"recurrent bilateral epistaxis/telangiectasia phenotype and longitudinal HHT management distinction"},
]

CONCEPT_ID="v6-general-ent-emergencies-epistaxis"
TOPIC="Epistaxis"
Q_REC="cc-v112-rec-general-ent-emergencies-epistaxis"

ANSWER="""Foundation — severe epistaxis is first an airway and hemorrhage problem, not a nose-packing problem. Sit the stable patient forward, suction clot, assess airway protection and hemodynamics, obtain IV access when bleeding is substantial, and compress the soft cartilaginous lower third of the nose continuously rather than pinching the nasal bones. A topical vasoconstrictor such as oxymetazoline can improve visualization and temporize bleeding while resuscitation and definitive control are organized. Massive ongoing hemorrhage, inability to protect the airway, shock, syncope, brisk blood filling the pharynx, or rapidly falling hemoglobin changes the sequence toward airway control, blood-product/resuscitation planning, and urgent operative/interventional help.

Anatomy — most routine anterior bleeds arise from Kiesselbach/Little's area on the anterior septum, where branches from the sphenopalatine, anterior ethmoidal, greater palatine and superior labial systems anastomose. K.J. Lee emphasizes that this is an internal/external carotid-system anastomotic region. Posterior bleeding is commonly supplied through sphenopalatine/posterior lateral nasal branches of the internal maxillary artery; do not use 'Woodruff plexus' as a synonym for a posterior arterial source because K.J. Lee describes Woodruff as predominantly venous. Ethmoidal arteries arise from the ophthalmic/ICA circulation, which matters when a superior/anterior source persists after apparently adequate SPA control and when planning embolization because dangerous ECA-ICA/ophthalmic anastomoses can threaten vision or brain.

Application — after compression and vasoconstriction, clear clot and identify the bleeding site. If a discrete anterior source is visible, perform directed cautery with appropriate topical/local anesthesia; avoid indiscriminate or opposing bilateral septal cautery that increases septal injury/perforation risk. If active bleeding prevents source identification or cautery fails, pack appropriately. Current AAO-HNSF guidance favors resorbable packing for patients with a suspected bleeding disorder or those taking anticoagulant/antiplatelet medication. Packing is a bridge, not proof that the source has been understood.

Do not reflexively reverse or stop antithrombotic therapy for every nosebleed. The AAO-HNSF guideline specifically recommends first-line local measures before transfusion, reversal, or withdrawal of anticoagulant/antiplatelet medication when bleeding is not life-threatening. A life-threatening hemorrhage is different: coordinate reversal/transfusion decisions with the indication for anticoagulation and the patient's physiology rather than using a one-size-fits-all rule.

Escalation — recurrent bleeding after prior packing/cautery, recurrent unilateral bleeding, or difficult-to-control bleeding warrants nasal endoscopy to localize the source and exclude unrecognized pathology. Persistent or recurrent bleeding not controlled by packing or cautery should trigger evaluation for surgical arterial ligation/cauterization or endovascular embolization. Endoscopic sphenopalatine artery control is a key definitive option for refractory posterior epistaxis. The senior resident must expose the sphenopalatine foramen region deliberately and control all relevant branches rather than clipping the first vessel encountered and assuming the case is finished.

Senior decision — when a presumed posterior bleed continues after technically adequate SPA control, reassess the diagnosis. Possibilities include an unrecognized SPA branch, anterior ethmoidal source, collateral supply, tumor, HHT or systemic coagulopathy. Superior bleeding near the skull base should raise the anterior ethmoidal pathway; current 2026 literature supports AEA ligation as a defined rescue strategy in selected refractory cases. Embolization is an alternative or adjunct when surgery is unsuitable, unsuccessful, or localization favors an endovascular approach, but the team must respect ophthalmic and intracranial anastomoses because blindness and stroke are catastrophic failure modes.

Pattern recognition — recurrent bilateral spontaneous epistaxis plus mucocutaneous telangiectasias or a family history should trigger HHT assessment rather than repeated episodic packing alone. Recurrent unilateral epistaxis, nasal obstruction, cranial neuropathy or an atypical mass requires endoscopy and appropriate imaging/tissue diagnosis rather than assuming benign idiopathic bleeding.

Textbook-versus-current distinction — Cummings, Pasha and K.J. Lee supply the durable vascular map, exposure logic and surgical hemostasis principles. The current AAO-HNSF guideline adds explicit quality rules that should govern today's management: sustained compression, targeted local therapy, resorbable packing in bleeding-risk patients, endoscopy for recurrent/failed phenotypes, arterial ligation or embolization after failed packing/cautery, and local first-line measures before routine antithrombotic reversal when hemorrhage is not life-threatening. Contemporary 2026 literature further sharpens rescue thinking around anterior ethmoidal control and failure after SPA surgery.

Senior synthesis — stabilize first, localize second, control the smallest responsible vascular territory third, and escalate without creating a larger problem. The dangerous errors are pinching the nasal bones instead of the soft nose, letting blood pool in the pharynx while the airway deteriorates, blind bilateral cautery, treating packing as definitive after repeated failure, reflexively reversing anticoagulation in a non-life-threatening bleed, and assuming every refractory posterior bleed is still an SPA bleed."""

COHORT={
 Q_REC:{
  "concept_id":CONCEPT_ID,
  "canonical_topic":TOPIC,
  "prompt":"A patient presents with brisk epistaxis that continues despite home pressure. Differentiate a routine anterior bleed from severe/posterior hemorrhage, then walk through airway/hemodynamic priorities, correct compression and localization, cautery versus packing, anticoagulation decisions, and when recurrent or refractory bleeding should escalate to endoscopic arterial control or embolization. What failure pattern should make you question a presumed sphenopalatine source?",
  "answer_text":ANSWER,
  "explanation":"Epistaxis management is a physiology-first escalation ladder: protect airway/circulation, compress and vasoconstrict, localize and treat a visible source, pack when localization/control fails, then use endoscopy and definitive arterial control for recurrent or refractory bleeding while reconsidering alternate vascular or pathologic sources.",
  "board_pearl":"Refractory epistaxis after adequate SPA control is a localization problem, not permission to keep escalating blindly—look for missed branches, anterior ethmoid supply, tumor/HHT or systemic bleeding drivers.",
  "depth_layers_v208":{"foundation":"Kiesselbach versus posterior/ethmoidal vascular anatomy, airway/hemodynamic triage and correct mechanical compression.","application":"Directed cautery, packing selection, anticoagulation nuance, nasal endoscopy and criteria for SPA ligation/embolization.","senior_decision":"Re-localize failed control, recognize anterior ethmoidal and dangerous ICA/ophthalmic pathways, distinguish tumor/HHT phenotypes and choose operative versus endovascular rescue."}
 }
}

TRAPS=[
 "Pinching the nasal bones or bridge instead of compressing the soft cartilaginous nose continuously.",
 "Tilting a briskly bleeding patient backward and allowing blood to pool in the pharynx while airway protection worsens.",
 "Performing blind or opposing bilateral septal cautery rather than treating a visualized source and risking septal necrosis/perforation.",
 "Calling posterior packing definitive after recurrent failure instead of localizing the source and escalating to arterial control.",
 "Reflexively stopping or reversing anticoagulation in a non-life-threatening bleed before appropriate local first-line therapy.",
 "Assuming persistent bleeding after SPA ligation proves the operation simply needs more SPA cautery rather than considering missed branches, AEA supply or another diagnosis.",
 "Forgetting ophthalmic/ICA anastomoses when planning embolization and underestimating blindness or stroke risk.",
 "Repeatedly packing recurrent bilateral telangiectatic bleeding or recurrent unilateral bleeding without evaluating HHT, tumor or other underlying pathology."
]
for _p in COHORT.values():
 _p["common_traps_v208"]=list(TRAPS)
 _p["deliberate_review_v208"]="Selected from the exact successful v20.7 live-canonical backlog: the Epistaxis management check was only 19 answer words despite priority 10 and direct airway, hemorrhage, endoscopic arterial-control and embolization consequences. Clinical risk outranked lexical ordering."
 _p["source_refs_v208"]=SOURCE_REFS_V208

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
