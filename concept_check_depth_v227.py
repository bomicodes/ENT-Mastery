"""v20.27 exact-live Pain Management in the Head & Neck Patient depth cohort.

Durable ENT pain mechanisms and postoperative warning patterns are cross-referenced to
Cummings 7e, Pasha 6e and K.J. Lee 12e in the user's connected Google Drive. Current
opioid, cancer-pain and pediatric tonsillectomy management is intentionally separated
from textbook principles and anchored to current CDC, ASCO, AAO-HNS and FDA guidance.
"""
from copy import deepcopy
from concept_check_board_repair_v177 import _find_module

QIDS = ["cc-v112-rec-general-ent-emergencies-pain-management-in-the-head-neck-patient"]
CID = "v6-general-ent-emergencies-pain-management-in-the-head-neck-patient"
TOPIC = "Pain Management in the Head & Neck Patient"
PROMPT = (
    "A postoperative or oncology patient on the ENT service reports escalating head-and-neck pain. "
    "Before increasing analgesics, distinguish expected acute nociceptive pain from neuropathic pain, "
    "mucositis/odynophagia, chronic treatment-related pain, and active-cancer pain, while asking whether "
    "the change in pain is actually a warning sign of hematoma, airway compromise, infection, ischemia, "
    "CSF complication, perineural tumor spread, or recurrence. How should you build a multimodal analgesic "
    "plan, when are opioids appropriate, which pediatric and OSA safety rules change prescribing, and what "
    "findings should make a senior resident stop treating the pain score and escalate the underlying problem?"
)

ANSWER = r'''Pain in otolaryngology is a **diagnostic signal first and a symptom second**. A safe resident-level approach starts by asking *why the pain is occurring, whether its trajectory is expected, and whether treating the number could mask a surgical complication*. The same numeric pain score can represent routine incisional inflammation, a compressive neck hematoma, deep-space infection, mucosal injury from radiation, neuropathic pain after nerve injury, recurrent cancer, or opioid withdrawal. The first senior decision is therefore not “which opioid next?” but “is this still the pain syndrome I thought I was treating?”

**1. Define the pain phenotype and urgency before prescribing.** Acute postoperative nociceptive pain is usually temporally linked to tissue injury and should generally improve in trajectory as healing progresses. Neuropathic pain is suggested by burning, electric, lancinating, allodynic, or dermatomal/nerve-distribution symptoms and may follow neck dissection, skull-base surgery, radiation, chemotherapy, or direct tumor involvement. Mucositis and odynophagia have a different treatment logic from an incision. Chronic post-treatment pain may combine fibrosis, neuropathy, musculoskeletal dysfunction, xerostomia-related mucosal injury, dental disease, and recurrence anxiety. Active-cancer pain is its own clinical context and should not be forced into the same opioid rules used for uncomplicated outpatient musculoskeletal pain.

Severe **new**, rapidly worsening, focal, or out-of-proportion pain is a red flag. After thyroidectomy, parathyroidectomy, neck dissection, free-flap reconstruction, or other cervical surgery, pain plus neck pressure, swelling, voice change, stridor, dyspnea, dysphagia, agitation, or rapidly increasing drain output should trigger immediate evaluation for **neck hematoma and airway compromise**. Analgesic escalation is not the rescue; airway control and hemorrhage control are. After deep neck infection treatment, worsening pain with fever, trismus, toxic appearance, crepitus, neurologic change, or failure to improve should prompt reassessment for undrained infection, necrotizing infection, mediastinal spread, or another source. After flap reconstruction, disproportionate pain, color/temperature change, bleeding abnormality, congestion, or loss of Doppler signal raises concern for vascular compromise and requires flap evaluation rather than sedation. After sinus or skull-base surgery, severe headache or pain accompanied by clear rhinorrhea, meningismus, fever, neurologic deficit, orbital change, visual symptoms, or mental-status change changes the pathway. In a cancer survivor, progressive focal pain, cranial neuropathy, otalgia without an otologic source, trismus, bone pain, or pain out of proportion to a benign exam should raise concern for recurrence or perineural disease.

**2. Use multimodal analgesia when safe.** The foundation for most acute postoperative ENT pain is scheduled or appropriately timed **acetaminophen and an NSAID** when not contraindicated, plus procedure-specific nonpharmacologic measures and a limited rescue strategy. Multimodal therapy is not a slogan: each drug should have a role, contraindication screen, and reassessment plan. Acetaminophen requires attention to total daily exposure from all combination products and to significant liver disease or heavy alcohol use. NSAIDs require individualized consideration of renal function, dehydration, active gastrointestinal bleeding/ulcer disease, platelet dysfunction, selected anticoagulation situations, and procedure-specific bleeding concerns. A blanket “NSAIDs always cause surgical bleeding” rule is not appropriate; neither is reflexive NSAID use in a patient with clear contraindications.

For adult acute pain, the current CDC framework supports maximizing nonopioid pharmacologic and nonpharmacologic therapy when appropriate. If the operation or injury predictably produces moderate-to-severe pain and an opioid is warranted, use an **immediate-release** opioid at the **lowest effective dose** and prescribe no greater quantity than needed for the expected period of severe pain. This is a starting framework, not a rigid pill-count law. Reassess function, sedation, respiratory risk, bowel function, concomitant sedatives, and whether pain is following the expected clinical course. Do not continue escalating simply because the patient still reports pain if the phenotype or trajectory has changed.

**3. Treat respiratory risk as an ENT issue, not merely a pharmacy issue.** Patients with OSA, obesity hypoventilation, craniofacial restriction, neuromuscular disease, significant pulmonary disease, frailty, or concomitant sedatives are more vulnerable to opioid-related ventilatory impairment. Shared-airway operations and recent upper-airway surgery further narrow the safety margin. Repeated opioid dosing in a somnolent, obstructing, or hypoventilating patient can convert treatable pain into an airway emergency. Senior reasoning means checking sedation and ventilation, not just oxygen saturation, because supplemental oxygen can obscure hypoventilation. Escalate monitoring and level of care when clinical risk warrants it; do not “chase the pain score” through progressive sedation.

Whenever opioids extend beyond very short rescue use, build an adverse-effect plan: nausea treatment when needed, constipation prevention with an appropriate bowel regimen, counseling about driving/alcohol/sedatives, safe storage and disposal, and a clear stop or taper plan. Abrupt discontinuation of established long-term opioid therapy can cause harm; chronic therapy changes require individualized assessment rather than reflex cessation.

**4. Pediatric tonsillectomy is a specific high-yield exception with strong safety rules.** Current AAO-HNS guidance supports **ibuprofen, acetaminophen, or both** for post-tonsillectomy pain in children. Codeine is not an acceptable “stronger backup” after pediatric tonsillectomy: AAO-HNS strongly recommends against codeine after tonsillectomy in children younger than 12, and FDA labeling carries the broader contraindication for postoperative pain management in pediatric patients after tonsillectomy/adenoidectomy because CYP2D6 ultra-rapid metabolism can generate unexpectedly high morphine exposure and fatal respiratory depression. Children with OSA are particularly vulnerable. This is an example where contemporary pharmacogenetic and regulatory evidence supersedes older prescribing habits. Poor oral intake after tonsillectomy should also trigger assessment of hydration and bleeding, not simply more analgesic.

**5. Cancer pain must be separated explicitly from routine CDC outpatient opioid guidance.** The CDC opioid guideline does **not** apply to cancer-related pain treatment, palliative care, or end-of-life care. Applying its acute outpatient framework as an absolute ceiling to a patient with painful active head-and-neck cancer is an evidence error. ASCO recommends offering opioids to adults with **moderate-to-severe pain from cancer or active cancer treatment** unless contraindicated, beginning PRN at the lowest dose that achieves acceptable analgesia and patient goals, followed by early reassessment and titration. Monitor and proactively manage adverse effects. When substance-use disorder, complex opioid tolerance, severe psychosocial distress, or difficult escalation is present, collaborate with palliative care, pain medicine, addiction medicine, and oncology rather than abandoning analgesia or escalating without structure.

Cancer pain itself is heterogeneous. Nociceptive pain from primary tumor or bony invasion may respond differently from neuropathic pain caused by perineural invasion or treatment-related nerve injury. Mucositis pain may require meticulous oral care, treatment of candidiasis or superinfection when present, topical/local measures in selected patients, systemic analgesia, and nutrition/hydration support. Persistent unilateral otalgia, facial pain, jaw pain, or cranial neuropathic pain should not automatically be labeled “post-radiation pain” without recurrence evaluation when the clinical pattern warrants it.

**6. Match adjuvant therapy to mechanism rather than layering sedating medications indiscriminately.** Neuropathic pain may benefit from agents such as gabapentinoids, selected antidepressants, topical/local approaches, or specialist-directed therapies depending on the syndrome, but these drugs also have sedation, dizziness, renal-dosing, drug-interaction, and fall risks. The goal is not to prescribe every modality simultaneously. Identify the dominant mechanism, start deliberately, reassess, and stop ineffective therapy. Myofascial pain, shoulder dysfunction after neck dissection, TMJ-related pain, cervical stiffness after radiation, and lymphedema-related discomfort often require rehabilitation, physical therapy, stretching, posture/shoulder mechanics, or targeted procedural treatment rather than escalating systemic opioids.

**7. Reassessment is part of the prescription.** For uncomplicated acute postoperative pain, define what improvement should look like over the next hours to days. If rescue dosing is repeatedly required, ask whether the base multimodal plan is inadequate, the diagnosis is wrong, absorption is impaired, the patient cannot swallow, an interaction is occurring, or a complication is evolving. A patient whose pain suddenly changes character or severity deserves re-examination. A patient with persistent severe pain after the expected healing window deserves mechanism-based reassessment rather than automatic refills.

Useful senior-resident questions are: Is the airway safe? Is there bleeding, infection, ischemia, obstruction, CSF leak, or another surgical complication? Is this expected nociceptive pain, neuropathic pain, mucositis, chronic treatment toxicity, or active-cancer pain? Which nonopioid modalities are safe here? If an opioid is needed, what is the minimum effective rescue plan and what respiratory risks exist? Does this patient fall under routine acute-pain guidance, or under cancer/palliative guidance instead? What follow-up interval and stop criteria have I defined?

**8. Know the bailout points.** Stop routine analgesic escalation and **reassess/escalate** when pain is accompanied by airway symptoms, expanding swelling, hemorrhage, neurologic or visual change, flap concern, sepsis physiology, mental-status change, disproportionate pain, unexpected persistent tachycardia, inability to hydrate, or a new focal cancer warning sign. The correct rescue may be bedside wound opening for a life-threatening postoperative neck hematoma, return to the OR, drainage/source control, flap exploration, imaging, cancer workup, or higher-acuity respiratory monitoring—not another dose of medication. The quality endpoint is not a pain score of zero; it is adequate analgesia and function **without missing the dangerous cause of pain or producing treatment-related harm**.'''

TRAPS = [
    "Treating a new severe postoperative pain score before re-examining the airway and surgical site.",
    "Assuming escalating neck pressure after thyroid or neck surgery is routine incisional pain rather than possible hematoma.",
    "Using opioid escalation to mask pain from an ischemic or congested free flap instead of checking flap viability.",
    "Applying CDC outpatient opioid limits as if they governed active-cancer or palliative pain.",
    "Using codeine after pediatric tonsillectomy despite the pharmacogenetic respiratory-depression risk and FDA contraindication.",
    "Withholding ibuprofen after pediatric tonsillectomy solely because of a blanket belief that all NSAIDs are prohibited.",
    "Giving NSAIDs without checking renal function, dehydration, GI bleeding risk, platelet/coagulation context, and procedure-specific concerns.",
    "Forgetting total acetaminophen exposure from combination products.",
    "Chasing pain scores with repeated opioids in a somnolent patient with OSA or upper-airway compromise.",
    "Using oxygen saturation alone to judge opioid safety while supplemental oxygen masks hypoventilation.",
    "Failing to prescribe or discuss constipation prevention when opioids extend beyond brief rescue use.",
    "Labeling progressive focal pain in a cancer survivor as treatment effect without considering recurrence or perineural disease.",
    "Treating neuropathic pain as purely nociceptive and escalating opioids without mechanism-directed therapy.",
    "Stacking sedating adjuvants without reassessing cumulative respiratory and cognitive effects.",
    "Treating radiation mucositis pain without addressing hydration, nutrition, oral care, infection, and the treatment context.",
    "Refilling opioids after the expected healing interval without defining why pain persists.",
    "Abruptly stopping established long-term opioid therapy without assessing withdrawal and individualized risk-benefit.",
    "Ignoring severe pain with fever, trismus, toxicity, or failure to improve after deep-neck infection treatment.",
]

SOURCE_REFS_V227 = [
    {"type": "textbook", "citation": "Cummings Otolaryngology–Head and Neck Surgery, 7th ed. Durable perioperative, oncology, cranial-nerve and complication principles. Connected Google Drive file identity reconfirmed 2026-09-11 (CUMMINGS OTOLARYNGOLOGY–HEAD AND NECK 7th Ed 2021_compressed.pdf)."},
    {"type": "textbook", "citation": "Pasha R, Golub JS. Otolaryngology—Head and Neck Surgery: Clinical Reference Guide, 6th ed. Medication safety and common ENT postoperative management cross-reference. Connected Google Drive file identity and readable text reconfirmed 2026-09-11."},
    {"type": "textbook", "citation": "K.J. Lee's Essential Otolaryngology, 12th ed. Core pain mechanisms, postoperative complications and head-and-neck oncology principles. Connected Google Drive file identity reconfirmed 2026-09-11."},
    {"type": "guideline", "citation": "CDC Clinical Practice Guideline for Prescribing Opioids for Pain — United States, 2022. MMWR 71(RR-3):1-95. Current CDC clinical guidance pages remain active in 2026; cancer-related pain, palliative and end-of-life care are excluded from its scope."},
    {"type": "guideline", "citation": "Paice JA et al. Use of Opioids for Adults With Pain From Cancer or Cancer Treatment: ASCO Guideline. J Clin Oncol. 2023;41:914-930. doi:10.1200/JCO.22.02198; PMID 36469839."},
    {"type": "society", "citation": "AAO-HNS AAO40: Tonsillectomy: Post-Tonsillectomy Pain Management in Pediatric Patients+, 2026. Ibuprofen/acetaminophen supported; codeine strongly recommended against after tonsillectomy in children <12."},
    {"type": "regulatory", "citation": "U.S. FDA Drug Safety Communication and labeling: codeine contraindicated for postoperative pain management in pediatric patients after tonsillectomy and/or adenoidectomy because of life-threatening respiratory depression risk, including CYP2D6 ultra-rapid metabolism."},
]

COHORT = {
    QIDS[0]: {
        "canonical_topic": TOPIC,
        "concept_id": CID,
        "prompt": PROMPT,
        "answer_text": ANSWER,
        "depth_layers_v227": {
            "foundation": "Pain phenotype, multimodal analgesic pharmacology, opioid respiratory physiology, pediatric pharmacogenetics and red-flag complication recognition.",
            "application": "Build safe acute postoperative, pediatric tonsillectomy, neuropathic, mucositis and active-cancer pain plans with contraindication and monitoring logic.",
            "senior_decision": "Recognize when worsening pain is a diagnostic alarm; distinguish routine acute-pain guidance from cancer/palliative guidance; stop medication escalation and rescue airway, hemorrhage, infection, ischemia or oncologic failure modes.",
        },
        "common_traps_v227": TRAPS,
        "deliberate_review_v227": {
            "priority": "high",
            "review_after_days": [2, 7, 21, 60],
            "reason": "high-frequency prescribing with high-consequence airway, hematoma, pediatric codeine, OSA and active-cancer evidence-boundary traps",
        },
        "source_refs_v227": SOURCE_REFS_V227,
        "evidence_distinction_v227": (
            "Durable textbook principles define pain mechanisms, postoperative anatomy, complication recognition and multimodal reasoning. "
            "Current CDC guidance governs many adult outpatient acute/subacute/chronic pain decisions but explicitly excludes cancer-related pain, palliative care and end-of-life care. "
            "ASCO therefore governs the active-cancer opioid boundary used here. AAO-HNS 2026 and FDA labeling govern pediatric tonsillectomy analgesic safety. "
            "Textbook medication details are not treated as current regulatory authority when contemporary society or FDA guidance differs."
        ),
        "task_alignment_v227": True,
    }
}


def apply_concept_check_task_alignment_v227(checks, deep_modules, v6_item_id):
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
