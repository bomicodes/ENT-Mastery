"""v20.29 exact-live Radiation-Associated Dysphagia depth cohort.

Durable swallowing physiology and late radiation-injury principles are cross-referenced to
Cummings 7e, Pasha 6e and K.J. Lee 12e in the user's connected Google Drive. Current evaluation,
rehabilitation and surveillance decisions are anchored to AAO-HNS expert consensus, AHNS
survivorship guidance, and contemporary peer-reviewed radiation-associated dysphagia evidence.
"""
from copy import deepcopy
from concept_check_board_repair_v177 import _find_module

QIDS = ["cc-v112-rec-laryngology-voice-swallowing-radiation-associated-dysphagia"]
CID = "v6-laryngology-voice-swallowing-radiation-associated-dysphagia"
TOPIC = "Radiation-Associated Dysphagia"
PROMPT = (
    "A head-and-neck cancer survivor develops progressive solid/liquid dysphagia, coughing with meals, pharyngeal residue, "
    "weight loss, or recurrent pneumonia months to years after radiation. How should a resident distinguish late radiation "
    "fibrosis/neuropathy and reduced hyolaryngeal or pharyngeal function from xerostomia, stricture, recurrent cancer, and other "
    "structural causes; choose FEES versus modified barium swallow and additional workup; initiate mechanism-directed therapy; "
    "and recognize when aspiration, malnutrition, stenosis, or failed rehabilitation requires senior procedural escalation?"
)

ANSWER = r'''Radiation-associated dysphagia (RAD) is not simply “scar tissue after radiation.” It is a **time-dependent, mechanism-specific swallowing disorder in a cancer survivor**, and the first senior-resident obligation is to protect the patient from aspiration and malnutrition while refusing to attribute every new symptom to treatment effect. Head-and-neck cancer recurrence, a second primary, infection, cranial neuropathy, structural stenosis, dental/oral dysfunction, xerostomia and unrelated neurologic disease can coexist with radiation fibrosis.

**1. Start with swallowing anatomy and the time course.** Normal swallowing depends on coordinated oral propulsion, pharyngeal contraction, tongue-base retraction, laryngeal elevation/closure, upper-esophageal-sphincter opening, sensation and timely airway-protective responses. Radiation can injure several of these systems simultaneously. Acute mucositis, edema, odynophagia and taste change dominate during and shortly after treatment. Chronic and late RAD may reflect progressive fibrosis, reduced tissue compliance, weakness/disuse, lymphedema, sensory loss, cranial neuropathy, xerostomia, dental loss, trismus, impaired tongue-base/pharyngeal drive, reduced hyolaryngeal excursion, glottic insufficiency or pharyngoesophageal stenosis.

The 2026 systematic review of 99 studies and 15,578 patients is useful for counseling: swallowing-related outcomes often worsen early and improve by roughly 6 months, but clinically meaningful dysphagia, aspiration and stricture persist in a subset at 2 years and beyond. Late symptoms therefore deserve active evaluation rather than reassurance that radiation effects should have “already healed.” AHNS likewise describes radiation fibrosis as potentially emerging months or years later and progressively impairing swallowing.

**2. Triage danger before refining the mechanism.** Ask about coughing/choking, wet voice, prolonged meals, food sticking, avoidance of textures, weight trajectory, dehydration, feeding-tube dependence, fever and recurrent pneumonia. Measure weight and nutritional trajectory and involve dietetics early when intake is falling. Aspiration may be silent after sensory injury, so absence of coughing does not prove safety. Recurrent pneumonias, inability to maintain hydration/nutrition, rapidly progressive dysphagia, hemoptysis, new pain, otalgia, neck mass, focal cranial neuropathy or unexplained weight loss should accelerate endoscopic and oncologic reassessment.

A patient with acute respiratory compromise or severe aspiration pneumonia needs stabilization first. A patient who cannot safely or adequately sustain nutrition may require temporary enteral support, but feeding-tube placement is **not the endpoint of dysphagia care**. When medically safe, preserving functional swallowing and continuing an individualized exercise/therapy program may reduce disuse; tube feeding should not automatically mean “nothing by mouth forever.”

**3. Never diagnose late RAD by history alone.** Perform complete head-and-neck examination and flexible laryngoscopy, looking for recurrent/new tumor, secretion burden, pooling, vocal-fold motion/glottic closure, mucosal injury and structural narrowing. The cancer history matters: primary site, surgery, radiation field/dose, concurrent systemic therapy, pretreatment swallowing status and time since treatment all change the differential.

Instrumental swallowing assessment should answer a specific question. **FEES** directly evaluates pharyngeal/laryngeal anatomy, secretion management, residue, penetration/aspiration patterns, sensation and response to maneuvers using real foods without ionizing radiation; it can be repeated and is valuable for biofeedback. It does not visualize the oral phase or the actual moment of the swallow during white-out and is less suited to defining distal esophageal obstruction. **Modified barium swallow/videofluoroscopic swallowing study (MBS/VFSS)** shows bolus flow across oral and pharyngeal phases, timing, hyolaryngeal excursion, residue, penetration/aspiration and opening of the pharyngoesophageal segment across tested consistencies. Neither study is universally “better”; choose based on the suspected mechanism, local expertise and the decision the result must support.

If symptoms suggest a fixed pharyngoesophageal/esophageal stenosis—progressive solids then liquids, clear hold-up, poor UES opening, inability to pass the bolus—or if MBS suggests narrowing, add appropriate esophageal evaluation such as contrast esophagram and/or endoscopic assessment. If recurrence is plausible, pursue oncologic imaging and biopsy rather than repeatedly dilating an unexplained narrowing. A key trap is treating a presumed radiation stricture before excluding recurrent malignancy.

**4. Treat the mechanism, not the label.** Speech-language pathology is central. Therapy may include compensatory posture/maneuvers, bolus modification, strengthening or range-of-motion work, airway-protection strategies and exercises selected from the measured deficit. The 2023 AAO-HNS expert consensus statement on dysphagia in head-and-neck cancer reached consensus across risk factors, screening, evaluation, prevention, intervention and surveillance, supporting structured longitudinal care rather than symptom-only rescue. AHNS survivorship resources similarly recommend speech/swallow evaluation and rehabilitation and monitoring for aspiration.

Maintain oral hygiene and dental care because poor oral health increases the pathogenic burden aspirated into the lungs. Treat xerostomia with hydration, saliva-support strategies and indicated dental preventive care rather than assuming thicker secretions are a purely pharyngeal motor problem. Address trismus and neck fibrosis/lymphedema with appropriate therapy when they limit oral preparation or mechanics. Optimize pain control and nutrition sufficiently for the patient to participate in rehabilitation.

**5. Prevention and maintenance swallowing activity are useful, but evidence should not be oversold.** “Use it or lose it” captures a real disuse component, yet prophylactic exercise does not abolish radiation fibrosis or neuropathy. Contemporary studies associate adherence to swallowing exercises during radiation with better later patient-reported swallow function and diet measures; the 2026 one-year cohort found better MDADI and diet scores among adherent patients. That supports early SLP involvement and adherence coaching, but observational/adherence associations are not a guarantee against late RAD. Distinguish a modifiable behavioral component from irreversible or progressive tissue injury.

Likewise, encourage oral intake during treatment **to the extent that it is medically safe and feasible**, but do not turn oral intake into a moral test or withhold a feeding tube from a patient who cannot meet nutrition/hydration needs. The senior decision balances preservation of swallowing activity against aspiration risk, mucositis severity, pain, metabolic needs and oncologic treatment completion.

**6. Escalate structural disease deliberately.** A clinically important pharyngoesophageal stricture may benefit from endoscopic dilation, often requiring serial procedures. Before dilation, define the level/length when possible, consider recurrence, and anticipate irradiated-tissue fragility. Perforation is a real bailout risk; severe or near-complete stenosis may require advanced endoscopic techniques and experienced support rather than repeated blind force. Refractory stenosis should prompt reconsideration of diagnosis, technique, interval, reflux/inflammatory contributors where relevant and whether reconstruction or alternative nutrition is needed.

Glottic insufficiency that materially worsens airway protection may merit selected laryngeal intervention after confirming that closure failure is an important mechanism. Cricopharyngeal/UES-directed dilation, botulinum toxin or myotomy is **not** appropriate simply because residue exists; it requires evidence that outflow obstruction or dysfunctional UES relaxation is a meaningful limiting lesion. Poor pharyngeal driving force can make an apparently tight UES secondary rather than primary, and cutting or dilating the sphincter will not restore absent propulsion.

**7. Aspiration decisions require more than a penetration-aspiration score.** Integrate frequency/volume of aspiration, sensation and ability to clear, pulmonary reserve, oral hygiene, nutritional status, prior pneumonias, cognition and adherence. Some patients can remain on modified oral intake with strategies; others need temporary or durable enteral supplementation. Recurrent aspiration pneumonia despite maximal rehabilitation and appropriate structural treatment is a senior multidisciplinary problem. Selected patients with profound, irreversible aspiration and a nonfunctional larynx may eventually require aspiration-prevention surgery, including laryngectomy or laryngotracheal separation-type strategies in exceptional circumstances. That is not first-line RAD treatment; it is a quality-of-life and pulmonary-survival decision after realistic counseling about voice and anatomy.

**8. Maintain oncologic vigilance.** Progressive late dysphagia is a symptom, not a diagnosis. New unilateral pain, bleeding, mucosal lesion, neck mass, worsening trismus, cranial neuropathy, rapidly progressive obstruction or unexplained weight loss should trigger recurrence/second-primary workup. Radiation fibrosis and cancer recurrence can coexist. A prior “normal swallow study” does not clear a patient indefinitely, and a prior history of radiation does not make a new lesion benign.

**9. Senior-resident synthesis.** The useful sequence is: **stabilize aspiration/nutrition risk → exclude recurrent or new structural disease → instrument the swallow to identify physiology → treat measured deficits with SLP/diet/dental/xerostomia/fibrosis support → dilate or perform targeted laryngeal/UES intervention only when the mechanism supports it → reassess objectively when symptoms, pulmonary status or nutrition fail to improve**. Assign longitudinal ownership because late RAD can evolve years after treatment.

The quality endpoint is not merely “able to swallow something.” It is durable oral function when achievable, adequate nutrition/hydration, minimized pneumonia risk, preserved cancer surveillance, and a mechanism-based escalation plan that recognizes both the reversible and irreversible components of radiation injury.'''

TRAPS = [
    "Calling every new post-radiation swallowing complaint fibrosis without excluding recurrent or second-primary cancer.",
    "Assuming absence of cough excludes aspiration despite post-radiation sensory loss and silent aspiration.",
    "Ordering FEES and MBS interchangeably without defining what physiologic question the study must answer.",
    "Using FEES to claim normal oral-phase or distal esophageal function it cannot directly assess.",
    "Treating a suspected stricture with repeated dilation before excluding an unexplained recurrent malignant obstruction.",
    "Equating feeding-tube placement with completion of dysphagia management.",
    "Forcing oral intake despite unsafe aspiration or inadequate hydration/nutrition.",
    "Conversely making a patient permanently NPO solely because a tube was placed when safe swallowing activity remains possible.",
    "Promising prophylactic swallowing exercises will prevent late fibrosis or neuropathy.",
    "Ignoring adherence and disuse as modifiable contributors because radiation injury can be progressive.",
    "Treating xerostomia, trismus, dental disease, lymphedema and pain as unrelated to swallowing function.",
    "Assuming a high UES residual means primary cricopharyngeal dysfunction when weak pharyngeal driving force may be causal.",
    "Performing UES myotomy, Botox or dilation without mechanism-specific evidence.",
    "Underestimating perforation risk during dilation of irradiated or near-obliterated pharyngoesophageal stenosis.",
    "Using a single penetration-aspiration score without pulmonary reserve, pneumonia history, oral hygiene and clearance ability.",
    "Waiting for aspiration pneumonia before involving speech-language pathology in a symptomatic survivor.",
    "Ignoring weight trajectory and nutrition because the airway study is the most visually dramatic part of the evaluation.",
    "Failing to establish longitudinal follow-up because late RAD can emerge or progress years after treatment.",
]

SOURCE_REFS_V229 = [
    {"type": "textbook", "citation": "Cummings Otolaryngology–Head and Neck Surgery, 7th ed (2021). Connected Google Drive file ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t. Durable head-and-neck cancer, swallowing rehabilitation and radiation-injury principles cross-referenced at the source-identity level; the 765 MB compressed file exceeds connector full-text fetch limits, so current management claims are not inferred from inaccessible text."},
    {"type": "textbook", "citation": "Pasha R, Golub JS. Otolaryngology—Head and Neck Surgery: Clinical Reference Guide, 6th ed (2022). Connected Google Drive file ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Laryngology chapter: Esophageal and Swallowing Disorders / Dysphagia and Aspiration; H&N malignancy and radiation therapy are recognized contributors, with weight loss, choking and recurrent pneumonia as important symptoms."},
    {"type": "textbook", "citation": "K.J. Lee's Essential Otolaryngology, 12th ed (2019). Connected Google Drive file ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Cross-referenced against Chapter 36 oral cavity/pharynx/esophagus and Chapter 47 radiation therapy for head and neck cancer for durable anatomy, dysphagia and radiation-treatment foundations."},
    {"type": "consensus", "citation": "Kuhn MA et al. Expert Consensus Statement: Management of Dysphagia in Head and Neck Cancer Patients. Otolaryngol Head Neck Surg. 2023;168:571-592. PMID 36965195. AAO-HNSF expert consensus: risk factors, screening, evaluation, prevention, interventions and surveillance; 48 statements reached consensus and 12 did not."},
    {"type": "society", "citation": "American Head and Neck Society survivorship guidance: Dysphagia, Aspiration and Stricture; Radiation Fibrosis; and Head and Neck Cancer Survivorship Consensus Statement. Supports SLP-directed evaluation/rehabilitation, nutrition surveillance, oral swallowing activity when safe, stricture evaluation/dilation, and recognition of late progressive fibrosis."},
    {"type": "systematic_review", "citation": "Shah AH et al. Longitudinal Patterns of Radiation-Associated Dysphagia in Patients With Head and Neck Cancer: A Systematic Review. Head Neck. 2026;48:597-623. PMID 41340588. 99 studies / 15,578 patients; early peak with improvement by 6 months but persistent clinically significant dysphagia, aspiration and stricture at later follow-up."},
    {"type": "peer_reviewed", "citation": "Starmer HM et al. One-year Swallowing Outcomes in a Head and Neck Cancer Cohort: Impact of Adherence to Swallowing Exercises and Feeding Tube Use. Dysphagia. 2026;41:650-656. PMID 41348337. Exercise adherence associated with better one-year patient-reported swallow function and diet scores; interpreted as supportive association, not proof that exercise prevents all late fibrosis."},
    {"type": "peer_reviewed", "citation": "Bradshaw J et al. Radiation-associated dysphagia in head and neck cancer: narrative review of surgical management, diagnosis, and emerging directions. Oral Oncol. 2026;181:108118. PMID 42636603. Current synthesis used to verify procedural escalation framing for late RAD."},
]

COHORT = {
    QIDS[0]: {
        "canonical_topic": TOPIC,
        "concept_id": CID,
        "prompt": PROMPT,
        "answer_text": ANSWER,
        "depth_layers_v229": {
            "foundation": "Swallowing phases, airway protection, radiation fibrosis/neuropathy, xerostomia, sensory loss, pharyngoesophageal stenosis and oncologic differential.",
            "application": "Choose FEES versus MBS by question, assess aspiration/nutrition, exclude recurrence, and match SLP, diet, dental/xerostomia, dilation or laryngeal/UES treatment to measured physiology.",
            "senior_decision": "Escalate failed rehabilitation, recurrent aspiration, near-complete stenosis or suspicious progressive obstruction while balancing feeding support, procedural risk, pulmonary protection and long-term cancer surveillance.",
        },
        "common_traps_v229": TRAPS,
        "deliberate_review_v229": {
            "priority": "high",
            "review_after_days": [2, 7, 21, 60],
            "reason": "high-yield laryngology/head-and-neck survivorship problem with silent aspiration, recurrence, nutrition, stenosis and mechanism-specific procedural traps",
        },
        "source_refs_v229": SOURCE_REFS_V229,
        "evidence_distinction_v229": (
            "Durable textbook principles define swallowing anatomy, dysphagia mechanisms and radiation injury. The 2023 AAO-HNSF expert consensus and AHNS survivorship guidance govern contemporary screening, longitudinal evaluation and rehabilitation framing. "
            "The 2026 systematic review updates the time course and persistent burden of RAD, while 2026 adherence data support but do not prove universal prevention from swallowing exercise. "
            "Where exercise/continued oral use is encouraged, it is explicitly conditioned on safety and nutrition; where dilation or UES/laryngeal procedures are considered, they are mechanism-specific rather than reflexive."
        ),
        "task_alignment_v229": True,
    }
}


def apply_concept_check_task_alignment_v229(checks, deep_modules, v6_item_id):
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
        if topic != patch["canonical_topic"] or cid != patch["concept_id"]:
            link_mismatch.append(qid)
            continue
        for key, val in patch.items():
            if key != "canonical_topic":
                q[key] = deepcopy(val)
        q["choices"] = []
        q["answer"] = None
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
