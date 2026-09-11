"""v20.24 — deepen exact-live Intraoperative Nerve Monitoring Parameters.

Durable facial-nerve anatomy, EMG physiology and operative rescue principles are
cross-referenced against connected Cummings 7e, Pasha 6e and K.J. Lee 12e texts.
Contemporary society guidance and non-retracted current evidence are explicitly
separated from manufacturer- and procedure-specific numeric thresholds.
"""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-otology-neurotology-facial-nerve-intraoperative-nerve-monitoring-parameters",)
CID = "v6-otology-neurotology-facial-nerve-intraoperative-nerve-monitoring-parameters"
TOPIC = "Intraoperative Nerve Monitoring Parameters"

SOURCE_REFS_V224 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive split corpus; facial nerve, parotid surgery, otologic/neurotologic surgery and intraoperative monitoring sections; cross-referenced 2026-09-10.","role":"durable anatomy/operative physiology: facial-nerve identification remains anatomy-led; monitoring is an adjunct; free-running and stimulated EMG must be interpreted in operative context"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; facial nerve, parotid and otologic operative sections; cross-referenced 2026-09-10.","role":"resident/board cross-check: facial nerve monitoring setup, anatomy, stimulation and operative protection principles"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; facial nerve and otologic/head-and-neck operative sections; cross-referenced 2026-09-10.","role":"operative cross-check: facial-nerve course, branch anatomy and monitoring as an adjunct rather than a substitute for identification"},
    {"type":"society","citation":"American Academy of Otolaryngology-Head and Neck Surgery. Intra-Operative Cranial Nerve Monitoring in Otolaryngology-Head and Neck Surgery. Originally published 2018; reviewed October 2024.","role":"current society boundary: otolaryngologists use cranial-nerve monitoring/stimulation strategically as an adjunct to anatomic knowledge and surgical technique"},
    {"type":"consensus_statement","citation":"Scharpf J, Liu JC, Sinclair C, et al. Critical Review and Consensus Statement for Neural Monitoring in Otolaryngologic Head, Neck, and Endocrine Surgery. Otolaryngol Head Neck Surg. 2022;166(2):233-248. PMID: 34000898.","role":"AAO-HNS task-force consensus: education, anesthesia, setup, troubleshooting and documentation are core monitoring competencies; extratemporal facial nerve monitoring may be considered when CN VII is at risk"},
    {"type":"systematic_review","citation":"Zhao Y, Chen H, Xue S, Feng G. Intraoperative facial nerve monitoring in parotidectomy: a systematic review of its predictive value. J Int Med Res. 2025. PMID: 41371257.","role":"parameter boundary: amplitude decrease and threshold increase may correlate with dysfunction, but heterogeneous evidence does not establish a universal predictive cutoff"},
    {"type":"systematic_review_meta_analysis","citation":"Buntain H, Thompson M, Perry CF, et al. The Impact of Intraoperative Facial Nerve Monitoring During Parotidectomy on Postoperative Facial Nerve Function: A Systematic Review and Meta-Analysis. ANZ J Surg. 2026 Jul 30. PMID: 42533397. DOI: 10.1111/ans.70861.","role":"current non-retracted outcomes evidence: monitoring was associated with lower odds of immediate facial nerve dysfunction overall and in superficial parotidectomy, but not a significant reduction in permanent dysfunction; benefit remains procedure- and context-dependent"},
    {"type":"physiology_study","citation":"Electromyographic Response of Facial Nerve Stimulation Under Partial Neuromuscular Blockade During Resection of Vestibular Schwannoma. PMID: 31521756.","role":"anesthesia confounder: partial neuromuscular blockade increases stimulation threshold and changes interpretation of facial EMG"},
    {"type":"retraction_notice","citation":"RETRACTION: Efficacy of Intraoperative Facial Nerve Monitoring in Parotidectomy: A Systematic Review and Meta-Analysis (1970-2025). Otolaryngol Head Neck Surg. Published 2026-07-28. PMID: 42520282. Retracts PMID 41353726.","role":"evidence hygiene: the retracted 2026 parotid meta-analysis must not be used to support benefit estimates or clinical recommendations"},
]

PROMPT = """During a parotid/skull-base case, the facial nerve monitor that previously produced a robust response becomes quiet after traction near the nerve. As the senior resident, explain how you set up and interpret facial nerve monitoring, what free-running EMG and triggered stimulation can and cannot tell you, how anesthesia and technical factors alter thresholds/amplitudes, which numeric parameters are procedure- and system-dependent rather than universal, and exactly how you troubleshoot and rescue a sudden loss or deterioration of signal before assuming the nerve has been injured."""

ANSWER = """Foundation — the facial nerve monitor is an adjunct to anatomy, not a substitute for anatomy. The operative goal remains visual/anatomic identification and atraumatic handling of the facial nerve when the procedure permits it. Monitoring adds two complementary streams of information: spontaneous or free-running EMG can warn that an innervated facial muscle is being activated during manipulation, and triggered stimulation tests whether applied current can evoke a compound muscle response through the monitored pathway. Neither modality independently proves that the nerve is anatomically intact, predicts final function with certainty, or makes blind dissection safe.

SETUP — decide which facial divisions matter for the operation and place recording electrodes in representative facial muscles, commonly including upper- and lower-division targets such as orbicularis oculi and orbicularis oris/mentalis depending on the system and case. Verify electrode contact/impedance and secure leads before draping. Obtain a baseline response before the highest-risk dissection when feasible. The surgeon, anesthesia team and monitoring personnel should agree that facial EMG is required before paralytic dosing changes occur. A monitor that was never proven functional is not a reliable safety net.

ANESTHESIA — neuromuscular blockade is a major confounder because facial monitoring records muscle activity downstream from the motor nerve. A dense block can suppress or abolish the EMG response despite an intact nerve; even partial blockade can increase the current needed to evoke a response. Therefore a rising stimulation threshold is not automatically nerve injury if the anesthetic state changed. Volatile/intravenous anesthetic details matter less than preserving the neuromuscular response required by the chosen monitoring strategy. Always interpret a new signal change alongside train-of-four or the anesthesia team's assessment of residual blockade, timing of additional paralytic, temperature and physiologic changes.

FREE-RUNNING EMG — brief spikes/bursts can occur with mechanical stimulation and should be correlated with what the surgeon is doing. Repetitive or sustained neurotonic activity during traction, drilling, cautery or manipulation near the facial nerve is a warning to STOP the provoking maneuver, relax traction, irrigate if thermal injury is plausible, and reassess the field. The dangerous error is treating every audible burst as meaningless background or, conversely, treating any single transient burst as proof of permanent injury. Pattern, persistence, operative timing and subsequent stimulated function matter.

TRIGGERED STIMULATION — stimulation can help identify nerve tissue, map an obscured course, and test conduction across a segment. Use the lowest current appropriate to the clinical task and system rather than escalating blindly. Very low currents near an exposed nerve may evoke responses, whereas higher currents may be required through tissue, scar, tumor, bone or with partial neuromuscular blockade. Current can spread through fluid or adjacent tissue. Therefore the number displayed in milliamps is not a universal distance meter and is not a universal injury threshold.

NUMERIC PARAMETERS — record baseline and trend, not just an isolated number. Commonly followed variables include stimulation current, response threshold, EMG amplitude and sometimes latency or proximal-to-distal response relationships. Published skull-base and parotid studies use different techniques, muscles, currents, devices and endpoints. Lower stimulation thresholds and preserved amplitudes are generally reassuring in the appropriate context; a rising threshold or substantial amplitude loss can be concerning. But current systematic review evidence specifically does not support teaching one universal amplitude-drop percentage, one universal mA threshold, or one latency cutoff as a cross-procedure rule. Manufacturer defaults are device settings, not board-level physiologic laws.

SUDDEN SIGNAL LOSS — treat an unexpected loss as a rescue problem before labeling it nerve transection. First STOP traction, drilling, cautery or dissection at the danger zone. Keep the field stable and identify whether the change was temporally linked to a maneuver. Then troubleshoot from the whole system inward: confirm the monitor is powered/unmuted and leads remain connected; inspect recording and ground/reference electrodes; check impedance if available; confirm the stimulating probe/cable is connected and working; remove pooled fluid that may shunt current when relevant; verify the probe is actually contacting the intended tissue; and ask anesthesia immediately about neuromuscular blockade or other relevant physiologic changes.

Next establish whether any facial response remains. Stimulate a known intact accessible segment or an appropriate control point using the case-specific strategy. If a distal segment responds but a proximal segment does not after dissection across an intervening zone, local neural compromise becomes more concerning. If nothing responds anywhere after a previously robust baseline, a system/anesthetic failure rises on the differential. Do not repeatedly traumatize the nerve or escalate current without understanding why the signal was lost.

If the technical/anesthetic system checks out, inspect the operative danger zone. Release traction or compression, remove a retractor or instrument that may be loading the nerve, irrigate after possible thermal stress, control but do not blindly cauterize near the nerve, and evaluate for direct injury. In skull-base surgery, reassess proximal and distal stimulation when anatomically safe. In parotid surgery, reassess the trunk/known branches and the exact segment just manipulated. If the nerve has been visibly divided, monitoring is no longer a diagnostic debate: preserve ends and proceed to the appropriate immediate repair/reconstruction strategy when feasible.

A deteriorating signal with an anatomically intact nerve should change behavior. Stop the injurious maneuver, reduce traction and thermal/mechanical stress, and consider leaving adherent tumor or staging/altering the surgical objective when functional preservation outweighs aggressive removal. Monitoring is most valuable when its information changes the next maneuver; continuing the same dissection while an actionable warning persists defeats its purpose.

PROGNOSIS — end-of-case proximal stimulation and preserved amplitude can provide prognostic information in vestibular schwannoma surgery, but published thresholds are technique-specific. Similarly, parotid studies report associations between amplitude loss or threshold increase and postoperative weakness, yet the 2025 systematic review of predictive parameters found the evidence too heterogeneous for a conclusive universal cutoff. Teach directional physiology and within-case change before memorizing an isolated number.

CURRENT EVIDENCE — AAO-HNS society guidance and the AAO-HNS task-force consensus support strategic neural monitoring as an adjunct to anatomic knowledge and surgical technique, with explicit attention to education, anesthesia, setup, troubleshooting and documentation. For the extratemporal facial nerve, the consensus states monitoring may be considered when CN VII is at risk, while the evidence quality is lower than for some endocrine applications. The 2025 parotid systematic review found that amplitude decreases and threshold increases may correlate with postoperative dysfunction, but heterogeneity prevents a universal predictive cutoff. The current non-retracted 2026 Buntain systematic review/meta-analysis (PMID 42533397; published July 30, 2026) found lower odds of immediate facial nerve dysfunction with monitoring overall and in superficial parotidectomy, but no significant reduction in permanent dysfunction and no demonstrated benefit in total parotidectomy; this supports individualized use rather than a universal outcome guarantee. A separate 2026 parotid meta-analysis (PMID 41353726) reported lower weakness rates but was formally retracted on July 28, 2026 (PMID 42520282); those pooled benefit estimates must not be taught or used to justify practice. Monitoring therefore complements meticulous surgery; it does not guarantee facial function and does not excuse unsafe dissection.

FDA/SOCIETY BOUNDARY — facial nerve monitors are regulated medical devices with manufacturer-specific labeling and settings; there is no single FDA clinical indication that creates a universal stimulation threshold or amplitude alarm for all parotid, otologic and skull-base operations. Likewise, current major-society guidance supports strategic use of monitoring but does not prescribe one cross-platform numeric cutoff. The durable teaching is physiology, anatomy, setup, trend interpretation and immediate troubleshooting; current literature refines prognostication and outcome evidence without converting heterogeneous numbers into universal rules.

Senior synthesis — use the sequence BASELINE, WARNING, STOP, SYSTEM, ANESTHESIA, LOCALIZE, RESCUE, DECIDE. BASELINE: prove the system works before danger-zone dissection. WARNING: correlate spontaneous activity or deteriorating triggered response with the maneuver. STOP: halt traction/drilling/cautery. SYSTEM: check electrodes, leads, probe, impedance, mute/settings and current shunting. ANESTHESIA: exclude residual or newly administered neuromuscular blockade and relevant physiologic confounders. LOCALIZE: stimulate known proximal/distal segments when safe to distinguish global technical failure from focal neural dysfunction. RESCUE: release traction/compression and reduce thermal/mechanical injury. DECIDE: if function remains threatened, change the surgical maneuver or goal rather than trusting the monitor to protect a nerve you continue to injure."""

TRAPS = [
    "Using the monitor as a substitute for facial-nerve anatomy or visual identification.",
    "Failing to prove a baseline response before entering the highest-risk portion of the operation.",
    "Accepting poorly secured or high-impedance recording electrodes and later interpreting silence as nerve injury.",
    "Allowing dense neuromuscular blockade when muscle EMG is required and then calling the absent response a neural event.",
    "Interpreting a higher stimulation threshold after partial paralysis as proof that the nerve was injured.",
    "Treating every transient free-running EMG burst as permanent injury rather than correlating it with the maneuver and subsequent function.",
    "Ignoring repetitive or sustained neurotonic activity during traction, drilling or thermal manipulation.",
    "Memorizing one stimulation current as a universal nerve-localization distance rule despite tissue, scar, fluid and device effects.",
    "Teaching a single amplitude-drop percentage or mA threshold as universally prognostic across parotid and skull-base operations.",
    "Blindly escalating stimulation current when the probe, cable, electrodes or anesthetic state have not been checked.",
    "Forgetting that pooled fluid can shunt current and alter stimulation behavior.",
    "Assuming complete nerve transection when all channels become silent simultaneously without first checking the system and anesthesia.",
    "Continuing traction or drilling while troubleshooting an actionable signal deterioration instead of stopping the provoking maneuver.",
    "Repeatedly stimulating or manipulating an already threatened nerve in an attempt to force a reassuring response.",
    "Failing to compare proximal and distal responses when anatomy safely permits localization of a new conduction problem.",
    "Continuing aggressive tumor removal despite persistent functional deterioration when changing the surgical objective may better preserve facial function.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Facial nerve monitoring is an anatomy-led adjunct: establish a baseline, interpret free-running and triggered EMG as within-case trends, control anesthesia/technical confounders, and treat abrupt deterioration as an immediate stop-troubleshoot-localize-rescue event.",
    "board_pearl": "A lost facial EMG response is not synonymous with transection. Stop the provoking maneuver, check the circuit and neuromuscular blockade, then localize with known proximal/distal stimulation before deciding whether the problem is technical or neural.",
    "depth_layers_v224": {
        "foundation":"Facial-nerve anatomy, EMG physiology, recording/stimulation setup, and neuromuscular-blockade effects.",
        "application":"Within-case baseline/trend interpretation, free-running warning patterns, triggered stimulation, and procedure-specific parameter interpretation.",
        "senior_decision":"Immediate stop-and-rescue response to signal loss, technical/anesthetic troubleshooting, proximal-distal localization, and changing the surgical objective when functional preservation is threatened.",
    },
    "common_traps_v224": TRAPS,
    "deliberate_review_v224": {
        "why_review":"High-yield OR danger-zone concept where a resident must distinguish equipment/anesthesia failure from real facial-nerve injury while stopping ongoing mechanical or thermal harm.",
        "retrieval_prompts":["What are the two complementary facial monitoring modalities?","How does neuromuscular blockade alter facial EMG interpretation?","Why is there no universal mA or amplitude-drop cutoff?","What is the immediate sequence after sudden signal loss?","How do proximal/distal responses help localize a problem?"],
        "spacing":"Revisit before parotid, mastoid and skull-base cases; repeat whenever numeric thresholds are being recalled as universal rather than procedure/system-specific.",
    },
    "source_refs_v224": SOURCE_REFS_V224,
    "evidence_distinction_v224": "Durable textbook principles are anatomy-led facial-nerve identification, monitoring as an adjunct, EMG physiology, control of neuromuscular-blockade/technical confounders, and immediate stop/troubleshoot/rescue when a signal deteriorates. Current AAO-HNS guidance and consensus support strategic cranial-nerve monitoring as an adjunct to anatomy and technique, with procedure-specific evidence strength. The non-retracted 2025 parameter review remains heterogeneous for predictive numeric parameters, while the current non-retracted 2026 Buntain meta-analysis (PMID 42533397) found lower odds of immediate dysfunction but no significant permanent-function benefit and did not establish universal benefit across parotidectomy types. No universal amplitude-loss percentage, stimulation threshold or latency cutoff should be taught across procedures/devices. The 2026 Barrameda meta-analysis (PMID 41353726) was retracted July 28, 2026 (PMID 42520282), so its pooled benefit estimates are excluded. FDA device regulation and manufacturer settings do not create a universal clinical alarm threshold.",
    "choices": [],
    "answer": None,
}}


def apply_concept_check_task_alignment_v224(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, spec in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid); continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != spec["canonical_topic"] or cid != spec["concept_id"]:
            link_mismatch.append(qid); continue
        q.update(spec)
        q["task_alignment_v224"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
