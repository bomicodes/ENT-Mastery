"""v20.17 — deepen the exact live Endoscopic Maxillary Antrostomy Concept Check."""
from concept_check_board_repair_v177 import _find_module

QIDS = (
    "cc-v112-mgt-rhinology-allergy-skull-base-endoscopic-maxillary-antrostomy",
)
CID = "v6-rhinology-allergy-skull-base-endoscopic-maxillary-antrostomy"
TOPIC = "Endoscopic Maxillary Antrostomy"

SOURCE_REFS_V217 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive split Part 2 copy, Drive id 1_PCclrEVhvetv14xawyW2LBlLeqKMLW-, Part IV Sinus, Rhinology, and Allergy/Immunology; maxillary ostium/infundibulum anatomy and sinus-surgery failure passages cross-referenced 2026-09-08.","role":"durable anatomy/operative foundation: infundibulum lies between uncinate and orbit; posteroinferior uncinate overlies the natural maxillary ostium; failure to incorporate the natural ostium causes recirculation and revision failure"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy, Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; Allergy and Rhinology / Sinus Surgery cross-referenced 2026-09-08.","role":"resident/board framework: functional ESS preserves physiologic mucociliary drainage and proceeds from anatomic identification through uncinectomy to maxillary antrostomy"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy, Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; Chapter 33 Endoscopic Sinus Surgery / Middle Meatal Antrostomy cross-referenced 2026-09-08.","role":"operative cross-check: natural versus accessory ostium, recirculation, angled-scope confirmation, orbital hazard from direct-lateral probing, and disease-tailored antrostomy extent"},
    {"type":"clinical_practice_guideline","citation":"AAO-HNSF. Shin JJ, et al. Clinical Practice Guideline: Surgical Management of Chronic Rhinosinusitis. Otolaryngol Head Neck Surg. 2025;172 Suppl 2:S1-S47. PMID: 40424072. DOI: 10.1002/ohn.1287.","role":"current AAO-HNSF evidence layer: ESS candidacy and extent should be individualized to disease, patient goals, prior therapy and expected benefit rather than using a one-size-fits-all extent"},
    {"type":"revision_series","citation":"Bewick J, Egro FM, Masterson L, Javer AR, Philpott CM. Anatomic findings in revision endoscopic sinus surgery: Case series and review of contributory factors. Allergy Rhinol (Providence). 2016;7(3):151-157. PMID: 28107148.","role":"revision evidence: residual uncinate and antrostomy not based on the natural maxillary ostium are common remediable anatomic findings in revision ESS"},
    {"type":"peer_reviewed_case_literature","citation":"Missed Maxillary Sinus Ostium Syndrome and its Management. Indian J Otolaryngol Head Neck Surg. 2024. PMID: 38566669.","role":"modern illustration of missed-ostium sequence and mucus recirculation when natural and surgical openings remain disconnected"},
]

ANSWER = """Foundation — a middle meatal antrostomy is not simply a hole in the medial maxillary wall. The operation should restore a controlled pathway that incorporates the true natural maxillary ostium and respects the surrounding uncinate, orbit, nasolacrimal system, and mucociliary physiology. The maxillary sinus drains through its natural ostium into the inferior portion of the ethmoidal infundibulum. The uncinate forms the medial wall of that infundibulum; the orbit/lamina papyracea forms its lateral boundary. Cummings emphasizes that the posteroinferior uncinate overlies the maxillary ostium and must be addressed to identify it. This is why an apparently generous opening posterior to a retained uncinate can still be the wrong opening.

Natural versus accessory ostium — distinguish them deliberately. An accessory ostium is a fontanelle defect and may be visible in the middle meatus, but it does not replace the physiologic natural ostium. Native mucociliary transport directs mucus toward the natural ostium. If a surgeon creates or enlarges an accessory opening without connecting it to the natural ostium, mucus can exit the natural ostium and be drawn back into the sinus through the separate surgical/accessory opening. That recirculation loop can produce persistent symptoms despite an apparently patent postoperative antrostomy. K.J. Lee and Cummings both identify failure to incorporate the natural ostium as an important technical cause of ESS failure.

Preoperative application — read the CT as a surgical map rather than merely as an inflammation score. Identify the uncinate orientation and attachment, maxillary sinus size, orbital floor and lamina position, Haller cells, prior antrostomy, residual uncinate, middle-turbinate position, and any anatomy suggesting silent-sinus-type atelectasis or a low orbit. A hypoplastic or atelectatic maxillary sinus can bring the orbit into an unexpectedly inferior/medial position. Previous surgery may erase familiar landmarks. Disease burden, phenotype, access needs, prior surgery, and the treatment goal determine how much opening is actually required; a standard antrostomy, extended/mega-antrostomy, and medial maxillectomy are not interchangeable procedures.

Uncinectomy and true-ostium identification — expose before enlarging. Adequately mobilize/remove the portion of uncinate obscuring the infundibulum and natural ostium while maintaining orientation to the orbit. Use direct visualization and an angled endoscope when necessary; K.J. Lee specifically notes that 30-, 45-, or 70-degree optics may be required to confirm the true ostium. Do not infer that the first opening seen is natural. Trace the anatomy and, when probing is appropriate, keep the probe trajectory controlled. Direct-lateral probing is dangerous because the lamina/orbit is lateral to the infundibulum; K.J. Lee explicitly warns that directing the probe directly lateral can cause orbital injury.

Creating the antrostomy — once the natural ostium is identified, enlarge it under vision so the operative opening incorporates the native drainage pathway. Preserve healthy mucosa when possible and use cutting instruments in a way that avoids uncontrolled stripping or blind bites. The opening can be expanded posteriorly, inferiorly, or selectively superiorly according to disease and access. Do not make 'bigger is better' the rule. The 2025 AAO-HNSF surgical CRS guideline supports tailoring ESS extent to the patient's disease and expected benefit. A routine inflammatory CRS case does not automatically need a mega-antrostomy or medial maxillectomy merely because those create a larger window.

Danger zones — lateral is orbit. Anterior extension approaches the lacrimal pathway and should be deliberate rather than reflexive. Superior work must remain oriented to ethmoid/orbital anatomy, and posterior enlargement should stay controlled around mucosa and vascular structures. The senior principle is that loss of visualization converts ordinary instrumentation into dangerous instrumentation. If bleeding, edema, scar, or distorted anatomy prevents confident identification of the true ostium and orbital boundary, stop active enlargement, suction and decongest, restore a recognizable landmark, switch optics, review navigation/CT when available and indicated, or stage/limit the procedure rather than taking a blind lateral bite.

Application — persistent maxillary disease after prior ESS should trigger a structured failure analysis. Look for retained uncinate, a surgical antrostomy separated from the natural ostium, stenosis, scar/synechiae, middle-turbinate lateralization, residual cells such as Haller cells, recurrent inflammatory disease, odontogenic disease, fungal pathology, tumor, or a mucociliary disorder. A large postoperative opening does not prove that the physiology is correct. In a revision series, residual uncinate and an antrostomy not based on the natural ostium were among common anatomic findings, reinforcing that technical geometry matters in addition to size.

Revision recirculation decision — if endoscopy demonstrates two separated openings with mucus cycling between them, identify which is the natural ostium and connect the openings in a controlled fashion while removing the residual partition/uncinate that perpetuates the loop. Do not simply enlarge the wrong posterior opening further. If the natural ostium cannot be confidently identified because of scar or altered anatomy, pause and remap from fixed landmarks and imaging before proceeding. Revision surgery has less margin for assumption because landmarks may be missing and the orbit may be closer than expected.

Senior extent decision — the indication determines the operation. Standard middle meatal antrostomy is appropriate for many routine ESS cases. A larger extended or mega-antrostomy may be useful for selected recalcitrant maxillary disease or when dependent access/irrigation/instrumentation is specifically needed. Endoscopic medial maxillectomy and other extended approaches have different anatomic costs and indications and should not be taught as simply 'an even larger antrostomy.' The decision balances disease clearance and access against mucosal injury, altered physiology, lacrimal/inferior-turbinate consequences, and future surveillance.

Senior rescue — suspected orbital entry requires an immediate change in behavior: stop the injuring maneuver and assess the eye/orbit rather than continuing ESS as though nothing happened. New orbital fat, extraocular muscle concern, brisk orbital bleeding, acute proptosis, pupillary change, vision complaint in an awake patient, or a tense orbit can signal escalating injury. The exact rescue depends on the injury, but continued blind instrumentation is never the answer. Preserve vision first, obtain appropriate ophthalmic help when needed, and manage an orbital compartment emergency without delay. Likewise, unexpected clear fluid or skull-base concern during more extensive adjacent ESS demands cessation, localization, and repair planning rather than finishing the planned sinus sequence by momentum.

Bailout synthesis — before every irreversible bite, know whether the structure in view is the natural ostium, accessory ostium, residual uncinate, lamina/orbit, or a scarred prior opening. If you cannot say which one it is, do not take the bite. Re-establish exposure, use angled visualization, correlate CT/navigation, and deliberately limit or defer the maneuver if orientation cannot be restored. The board-level answer is 'incorporate the natural ostium.' The resident-level answer is how to prove you found it. The senior-level answer is when not to enlarge, when to revise a missed-ostium/recirculation problem, when an extended procedure is actually justified, and when uncertainty should trigger a bailout rather than an orbital or lacrimal injury."""

COHORT = {
    QIDS[0]: {
        "concept_id": CID,
        "canonical_topic": TOPIC,
        "prompt": "A patient with persistent unilateral maxillary symptoms after prior endoscopic sinus surgery has a widely patent-appearing posterior middle-meatal opening, residual uncinate anteriorly, and mucus seen cycling between two openings. As the resident planning revision surgery, explain how you would identify the true natural maxillary ostium, distinguish it from an accessory or prior surgical opening, correct recirculation, choose the appropriate antrostomy extent, and avoid orbital and nasolacrimal injury. What senior bailout should occur if scar, bleeding, or distorted anatomy prevents confident identification of the ostium and orbit?",
        "answer_text": ANSWER,
        "explanation": "A successful maxillary antrostomy is anatomy- and physiology-based: expose and incorporate the true natural ostium, tailor the opening to disease, and stop rather than instrument blindly when the orbit or ostium cannot be confidently localized.",
        "board_pearl": "A patent hole is not necessarily a functional antrostomy: failure to connect the natural maxillary ostium to the surgical/accessory opening creates recirculation; direct-lateral probing risks the orbit.",
        "depth_layers_v217": {"foundation":"Natural ostium, infundibulum, uncinate, accessory ostium, mucociliary drainage, orbit/lamina and lacrimal relationships.","application":"CT/endoscopic mapping, complete ostium exposure, angled-scope confirmation, recirculation recognition, revision failure analysis and disease-tailored antrostomy extent.","senior_decision":"Choose standard versus extended access by indication; stop and remap when anatomy is uncertain; recognize and rescue orbital injury rather than continuing blind instrumentation."},
        "common_traps_v217": [
            "Calling the first visible posterior middle-meatal opening the natural ostium without tracing the infundibular anatomy.",
            "Mistaking an accessory ostium for the natural ostium and creating a disconnected surgical opening.",
            "Leaving residual posteroinferior uncinate that hides the natural ostium.",
            "Enlarging a prior opening while failing to connect it with the true natural ostium, perpetuating mucus recirculation.",
            "Assuming a large antrostomy proves technically adequate drainage physiology.",
            "Directing a probe or instrument directly lateral in the infundibulum and entering the orbit.",
            "Failing to recognize a low/inferior orbit in a hypoplastic or atelectatic maxillary sinus.",
            "Extending anteriorly without deliberate awareness of the nasolacrimal pathway.",
            "Continuing powered or biting instrumentation after bleeding or scar has destroyed reliable visualization.",
            "Teaching a mega-antrostomy or medial maxillectomy as routine escalation rather than an indication-specific extended procedure.",
            "Using 'bigger is better' instead of tailoring antrostomy extent to disease, access, physiology, and morbidity.",
            "Attributing persistent postoperative disease only to inflammation without checking residual uncinate, missed natural ostium, stenosis, synechiae, or recirculation.",
            "Using navigation as permission for blind instrumentation rather than as an adjunct to direct anatomic orientation.",
            "Continuing the planned sinus sequence after suspected orbital entry instead of stopping, assessing vision/orbit, and initiating the appropriate rescue.",
        ],
        "deliberate_review_v217": "Selected from the exact successful v20.16 live-canonical backlog because this OR-heavy Rhinology concept remained shallow despite high resident/board value. Review is deliberately centered on natural-versus-accessory ostium discrimination, revision recirculation, disease-tailored extent and an explicit orbital bailout rather than lexical rank or generic FESS sequencing.",
        "source_refs_v217": SOURCE_REFS_V217,
        "evidence_distinction_v217": "Durable anatomy and operative principles are grounded in Cummings 7e, Pasha 6e and K.J. Lee 12e. The current 2025 AAO-HNSF CRS surgical guideline updates candidacy/extent reasoning and supports individualized ESS rather than a universal maximal opening. Revision literature reinforces missed-natural-ostium/retained-uncinate failure mechanisms. No FDA product indication supersedes these anatomy-based operative principles.",
        "audit_profile_v217": "endoscopic_maxillary_antrostomy",
    },
}

def apply_concept_check_task_alignment_v217(checks, deep_modules, v6_item_id):
    by={str(q.get("id") or ""):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
    for qid,p in COHORT.items():
        q=by.get(qid)
        if q is None: missing.append(qid); continue
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        persisted_cid=q.get("concept_id")
        if m is None or topic!=p["canonical_topic"] or cid!=p["concept_id"] or (persisted_cid is not None and persisted_cid!=cid): link_mismatch.append(qid); continue
        q["concept_id"]=cid; q["canonical_topic"]=topic
        for field in ("prompt","answer_text","explanation","board_pearl","depth_layers_v217","common_traps_v217","deliberate_review_v217","source_refs_v217","evidence_distinction_v217","audit_profile_v217"): q[field]=p[field]
        q["choices"]=[]; q["answer"]=None; q["task_alignment_v217"]=True; repaired.append(qid)
    return {"repaired":repaired,"missing":missing,"link_mismatch":link_mismatch}
