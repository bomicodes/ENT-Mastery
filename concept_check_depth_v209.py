"""v20.9 — deepen the exact live Laryngology Posterior Cordotomy / Arytenoidectomy Concept Check.

Durable bilateral-vocal-fold-immobility and airway-widening principles are cross-checked
against the connected ENT Boards Library copies of Cummings 7e, Pasha 6e, and K.J. Lee
12e. Contemporary outcome/tradeoff teaching is updated against the 2024 systematic review
of adult bilateral vocal fold paralysis management.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V209 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed., bilateral vocal fold immobility and endoscopic airway-widening sections (connected ENT Boards Library).","role":"foundation/operative: distinguish paralysis from fixation/posterior glottic stenosis, irreversible nature of cordotomy/arytenoidectomy, airway-voice-swallow tradeoffs, endoscopic alternatives and revision risk"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed., laryngology upper-airway obstruction and bilateral vocal fold immobility sections (connected ENT Boards Library).","role":"foundation/management: airway assessment, observation versus tracheotomy, lateralization/arytenoidectomy/posterior cordotomy options, swallow assessment when aspiration is a concern"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed., larynx chapter, bilateral vocal fold paralysis treatment section (connected ENT Boards Library).","role":"operative: tracheotomy as reliable airway, medial/partial arytenoidectomy principles, transverse posterior cordotomy at the vocal process, graded extension according to airway need, suture lateralization alternative"},
 {"type":"systematic_review","citation":"Lechien JR, Hans S, Mau T. Management of Bilateral Vocal Fold Paralysis: A Systematic Review. Otolaryngol Head Neck Surg. 2024;170(3):724-735. PMID:38123531. DOI:10.1002/ohn.616.","role":"current evidence: adult BVFP etiology, tracheotomy burden, high decannulation after cordotomy, airway benefit with expected voice tradeoff, arytenoidectomy outcomes, revision/edema/granuloma/fibrosis complications, and absence of evidence proving one procedure universally superior"},
]

QID="cc-v112-rec-laryngology-voice-swallowing-posterior-cordotomy-arytenoidectomy"
CID="v6-laryngology-voice-swallowing-posterior-cordotomy-arytenoidectomy"
TOPIC="Posterior Cordotomy / Arytenoidectomy"

ANSWER="""Foundation — posterior cordotomy and arytenoidectomy are airway-enlarging operations, not treatments for every immobile vocal fold. Their classic role is persistent bilateral vocal fold immobility with clinically important glottic airway restriction when a durable increase in posterior glottic aperture is needed. The resident must first decide whether the problem is true neurogenic bilateral paralysis, mechanical cricoarytenoid fixation/posterior glottic stenosis, or a mixed process, because the operation and prognosis differ. Review the onset and cause, flexible laryngoscopy, prior intubation or laryngeal surgery, expected chance of neurologic recovery, swallowing status, and airway severity. Examination under anesthesia with palpation of the cricoarytenoid joints can be decisive when fixation is suspected; laryngeal EMG may be useful selectively when prognosis or diagnosis remains uncertain.

Timing and reversibility — if the airway is acutely unsafe, secure it first; tracheotomy remains the most reliable immediately reversible airway. When recent nerve injury still has a meaningful chance of recovery, avoid automatically destroying phonatory tissue. Observation, tracheotomy, or a lateralization strategy may preserve options while recovery declares itself. Posterior cordotomy and arytenoidectomy should be framed as intentionally irreversible enlargement procedures whose benefit is purchased with some loss of glottic competence. The decision is therefore not simply 'can I make the airway larger?' but 'how much permanent enlargement does this patient need, and what voice/swallow cost can this patient tolerate?'

Posterior cordotomy — the operation enlarges the posterior glottis by creating a transverse opening through the posterior vocal fold at approximately the level of the vocal process. The opening can be enlarged in a graded fashion according to airway need. Preserve as much anterior membranous vocal fold as possible because unnecessary anterior extension sacrifices voice without adding proportionate posterior airway. The goal is a stable posterior respiratory aperture, not maximal tissue removal. CO2 laser is commonly used, but the board-level principle is controlled tissue removal with protection from airway fire, thermal injury, excessive cartilage exposure and circumferential scarring.

Arytenoidectomy — partial or medial arytenoidectomy removes the portion of arytenoid that mechanically limits the posterior airway while trying to preserve useful phonatory and swallowing function. Total arytenoid removal is rarely required. Arytenoidectomy can be added when cordotomy alone does not create adequate posterior space, when bulky arytenoid anatomy or fixation is a major component, or when revision anatomy requires more posterior enlargement. Removing more tissue is not automatically better: aggressive resection can worsen breathy dysphonia, aspiration risk and scar formation.

Choose and titrate — start with the least destructive operation likely to meet the airway requirement. In many adults, unilateral posterior enlargement is preferred initially; bilateral destructive surgery should not be reflexive because airway gain must be balanced against voice and swallowing. Baseline aspiration, poor pulmonary reserve, professional voice dependence, prior radiation/scarring, posterior glottic stenosis, and the likelihood of spontaneous/reinnervation recovery all change the choice. Suture lateralization can be attractive when a less-destructive or potentially reversible enlargement is desired and the cricoarytenoid joint is mobile.

Expected outcomes — contemporary adult literature supports substantial airway improvement and high decannulation rates after posterior transverse cordotomy, but voice generally becomes rougher or breathier. Partial arytenoidectomy also improves airway and may have a different voice/revision profile; current studies are heterogeneous and do not establish a universally superior technique. Do not quote a single procedure as 'best' without acknowledging that patients, definitions of bilateral paralysis, concomitant posterior glottic stenosis, and outcome measures vary substantially across studies.

Failure and revision — postoperative edema can transiently worsen the airway. Granulation tissue, fibrosis, restenosis, inadequate initial opening, and scar contracture can recreate obstruction and may require revision. If the patient remains stridulous or cannot be decannulated, reassess the entire mechanism rather than simply removing more vocal fold: confirm the size/location of the posterior aperture, look for granulation or posterior glottic stenosis, reassess arytenoid mobility, and consider whether the original diagnosis was incomplete. Revision should correct the actual limiting structure while preserving remaining voice and swallow function.

Swallow/voice counseling — airway, voice and swallowing are coupled. A larger posterior gap lowers airway resistance but usually reduces glottic closure for phonation and can impair airway protection in selected patients. Document baseline voice and dysphagia/aspiration risk before surgery and reassess afterward. New coughing with liquids, recurrent pneumonia, weight loss, or pulmonary decline warrants formal swallowing evaluation rather than assuming postoperative aspiration is an unavoidable tradeoff.

Senior synthesis — use five questions: MECHANISM asks paralysis versus fixation/posterior scar; URGENCY asks whether a tracheotomy or other immediate airway is needed; RECOVERY asks whether irreversible surgery should wait; APERTURE asks how much unilateral posterior enlargement is actually required; TRADEOFF asks what voice/swallow cost is acceptable. The dangerous mistakes are performing destructive widening before confirming the mechanism, doing bilateral aggressive resection when unilateral titration would suffice, confusing posterior glottic stenosis with pure neurogenic paralysis, and treating restenosis by blindly removing more tissue without identifying why the airway failed."""

PROMPT="""An adult with persistent bilateral vocal fold immobility remains exercise-limited and cannot be decannulated despite a stable medical course. The folds rest near the paramedian position, but prior prolonged intubation also raises concern for posterior glottic fixation. Before recommending posterior cordotomy or arytenoidectomy, how do you distinguish paralysis from fixation, decide whether an irreversible airway-widening procedure is appropriate now, choose and titrate cordotomy versus partial arytenoidectomy, and counsel the patient about airway, voice, swallowing, and revision tradeoffs?"""

COHORT={QID:{
 "concept_id":CID,
 "canonical_topic":TOPIC,
 "prompt":PROMPT,
 "answer_text":ANSWER,
 "explanation":"Posterior cordotomy/arytenoidectomy is a mechanism-confirmation and tradeoff problem. Confirm bilateral paralysis versus posterior fixation, secure an unsafe airway first, preserve recovery options when appropriate, and titrate the least destructive posterior enlargement that achieves the patient's airway goal while explicitly accepting voice/swallow consequences.",
 "board_pearl":"Do not equate bilateral immobility with bilateral RLN paralysis. Palpate the joints when fixation is plausible, preserve reversibility while recovery is possible, and enlarge the posterior glottis only as much as the airway requires.",
 "depth_layers_v209":{"foundation":"Differentiate neurogenic bilateral paralysis from cricoarytenoid fixation/posterior glottic stenosis and understand the airway-voice-swallow coupling.","application":"Choose tracheotomy/lateralization versus irreversible posterior cordotomy or partial arytenoidectomy based on urgency, recovery potential, joint mobility and required posterior aperture.","senior_decision":"Titrate unilateral versus more extensive widening, manage restenosis/granulation, and reassess mechanism rather than reflexively sacrificing more phonatory tissue when the airway result fails."},
 "common_traps_v209":[
  "Calling every bilateral immobile larynx bilateral recurrent-laryngeal-nerve paralysis without considering posterior glottic stenosis or cricoarytenoid fixation after prolonged intubation.",
  "Performing an irreversible cordotomy immediately after a potentially recoverable nerve injury when a tracheotomy or lateralization strategy could preserve future glottic function.",
  "Treating tracheotomy as a failure. In an acutely threatened airway it is the most reliable way to secure ventilation while diagnosis and recovery potential are clarified.",
  "Removing the maximum amount of posterior vocal fold or arytenoid at the first operation. Airway enlargement should be titrated because every additional loss of glottic tissue has voice and potentially swallow consequences.",
  "Extending cordotomy unnecessarily into the anterior membranous fold rather than preserving phonatory tissue once an adequate posterior respiratory aperture has been created.",
  "Assuming arytenoidectomy is always superior to cordotomy or vice versa. Current comparative evidence is heterogeneous and does not establish one universally best operation.",
  "Ignoring baseline dysphagia or pulmonary reserve when choosing how aggressively to enlarge the posterior glottis.",
  "Responding to restenosis by blindly removing more tissue without checking for edema, granulation, fibrosis, posterior glottic stenosis, arytenoid fixation or an incorrect initial diagnosis.",
  "Calling postoperative coughing or recurrent pneumonia an acceptable inevitable tradeoff instead of formally reassessing swallowing and aspiration risk."
 ],
 "deliberate_review_v209":"Selected as the highest-ranked residual live Concept Check after v20.8. The prior reveal was only 13 words and omitted mechanism confirmation, recovery timing, irreversible-procedure selection, operative titration, airway/voice/swallow tradeoffs and revision reasoning.",
 "source_refs_v209":SOURCE_REFS_V209,
}}


def apply_concept_check_task_alignment_v209(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v209','common_traps_v209','deliberate_review_v209','source_refs_v209'): q[field]=p[field]
  q['choices']=[]; q['answer']=None; q['task_alignment_v209']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
