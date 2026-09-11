"""v20.24 — deepen exact-live Neurotologic Intraoperative Cranial-Nerve Monitoring.

Durable neurotologic anatomy, facial-nerve EMG physiology, auditory-pathway monitoring,
and operative rescue principles are cross-referenced against connected Cummings 7e,
Pasha 6e and K.J. Lee 12e texts. Contemporary society/guideline evidence is kept
separate from device-, modality- and procedure-specific numeric thresholds.
"""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-otology-neurotology-neurotologic-intraoperative-cranial-nerve-monitoring",)
CID = "v6-otology-neurotology-neurotologic-intraoperative-cranial-nerve-monitoring"
TOPIC = "Neurotologic Intraoperative Cranial-Nerve Monitoring"

SOURCE_REFS_V224 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive split corpus; facial nerve, otologic/neurotologic surgery, vestibular schwannoma and intraoperative monitoring sections; cross-referenced 2026-09-10.","role":"durable anatomy/operative physiology: monitoring is an adjunct to anatomic knowledge; facial, cochlear and other at-risk cranial nerves require modality-specific interpretation"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; facial nerve, otologic and skull-base operative sections; cross-referenced 2026-09-10.","role":"resident/board cross-check: cranial-nerve anatomy, facial nerve stimulation/monitoring, hearing-preservation principles and operative protection"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; facial nerve, otologic and neurotologic operative sections; cross-referenced 2026-09-10.","role":"operative cross-check: facial-nerve course, skull-base anatomy and monitoring as an adjunct rather than a substitute for identification"},
    {"type":"society","citation":"American Academy of Otolaryngology-Head and Neck Surgery. Intra-Operative Cranial Nerve Monitoring in Otolaryngology-Head and Neck Surgery. Originally published 2018; reviewed October 2024.","role":"current society boundary: cranial-nerve monitoring/stimulation is used strategically as an adjunct to anatomic knowledge and surgical technique"},
    {"type":"consensus_statement","citation":"Scharpf J, Liu JC, Sinclair C, et al. Critical Review and Consensus Statement for Neural Monitoring in Otolaryngologic Head, Neck, and Endocrine Surgery. Otolaryngol Head Neck Surg. 2022;166(2):233-248. PMID: 34000898.","role":"AAO-HNS task-force consensus: education, anesthesia, setup, troubleshooting and documentation are core monitoring competencies; evidence strength varies by nerve and operation"},
    {"type":"guideline","citation":"Patel NS, Carlson ML, Sughrue ME, Olson JJ. Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines Update for the Role of Intraoperative Cranial Nerve Monitoring in the Management of Patients With Vestibular Schwannomas. Neurosurgery. 2026;98(2):288-292. PMID: 40470951.","role":"current vestibular-schwannoma guidance: intraoperative cranial-nerve monitoring should be used; facial and hearing monitoring strategies are complementary, while the optimal predictive strategy remains uncertain"},
    {"type":"systematic_review","citation":"Bubeníková A, et al. Intraoperative auditory monitoring in vestibular schwannoma surgery: Diagnostic accuracy and interventional effectiveness - a systematic review. Neurosurg Rev. 2026. PMID: 42036522.","role":"hearing-monitoring evidence boundary: ABR/BAEP and near-field CNAP/DNAP have different temporal resolution and evidence; predictive thresholds should not be treated as universal rescue laws"},
    {"type":"systematic_review","citation":"Zhao Y, Chen H, Xue S, Feng G. Intraoperative facial nerve monitoring in parotidectomy: a systematic review of its predictive value. J Int Med Res. 2025. PMID: 41371257.","role":"parameter boundary: amplitude decrease and threshold increase may correlate with dysfunction, but heterogeneous evidence does not establish a universal predictive cutoff"},
    {"type":"physiology_study","citation":"Electromyographic Response of Facial Nerve Stimulation Under Partial Neuromuscular Blockade During Resection of Vestibular Schwannoma. PMID: 31521756.","role":"anesthesia confounder: partial neuromuscular blockade increases stimulation threshold and changes interpretation of facial EMG"},
    {"type":"retraction_notice","citation":"RETRACTION: Efficacy of Intraoperative Facial Nerve Monitoring in Parotidectomy: A Systematic Review and Meta-Analysis (1970-2025). Otolaryngol Head Neck Surg. Published 2026-07-28. PMID: 42520282. Retracts PMID 41353726.","role":"evidence hygiene: the retracted 2026 parotid meta-analysis must not be used to support benefit estimates or clinical recommendations"},
]

PROMPT = """During a hearing-preservation vestibular schwannoma case, facial EMG has been robust but the auditory brainstem response deteriorates during internal-auditory-canal work; shortly afterward the facial response also becomes less reliable. As the senior resident, explain how neurotologic cranial-nerve monitoring is selected and baselined, what facial free-running/triggered EMG and auditory ABR/BAEP or near-field cochlear responses can and cannot tell you, how anesthesia and technical factors confound each modality, how you troubleshoot a sudden change before declaring neural injury, and when persistent deterioration should change the surgical maneuver or objective."""

ANSWER = """Foundation — neurotologic intraoperative cranial-nerve monitoring is a set of modality-specific adjuncts to anatomy and microsurgical technique, not a single alarm system. The nerve at risk and the function being preserved determine what is monitored. Facial motor function is commonly followed with free-running EMG plus direct electrical stimulation and evoked compound muscle responses. Hearing-preservation surgery may use far-field auditory brainstem response/brainstem auditory evoked potentials (ABR/BAEP), near-field cochlear nerve action potentials (CNAP), electrocochleographic techniques, or selected combinations. Lower cranial motor nerves can be monitored with appropriately placed muscle electrodes when the approach or lesion puts them at meaningful risk. The durable rule is that a waveform is useful only if you know what neural segment and end organ it samples, how quickly it updates, and what non-neural factors can change it.

BASELINE AND TEAM SETUP — before danger-zone dissection, establish that the selected modalities are technically reproducible. Confirm the intended nerves, recording muscles or auditory transducers, electrode integrity/impedance, stimulation hardware, laterality, and a baseline under the anesthetic conditions that will be used for critical dissection. Discuss neuromuscular blockade explicitly with anesthesia whenever motor EMG is needed. For auditory monitoring, confirm adequate stimulus delivery and a stable baseline before drilling/manipulation near the cochlea, labyrinth, internal auditory canal or cochlear nerve. A monitor that was never proven functional cannot later distinguish technical failure from injury.

FACIAL MOTOR MONITORING — free-running EMG is a warning channel. Brief spikes or bursts may reflect mechanical contact, whereas repetitive or sustained neurotonic activity during traction, drilling, cautery or tumor dissection should trigger immediate correlation with the surgical maneuver. Triggered stimulation helps identify or map the facial nerve and tests whether applied current evokes a distal muscle response. Neither modality proves complete anatomic continuity, guarantees normal postoperative function, or licenses blind dissection. A response depends on the stimulated site, current spread, distance/tissue between probe and nerve, electrode quality, muscle selection, anesthetic state and device characteristics.

ANESTHESIA AND MOTOR CONFOUNDERS — facial EMG records downstream muscle activity, so neuromuscular blockade can suppress or abolish a response even when the nerve is intact. Partial blockade can raise the stimulation current needed to obtain a response and alter amplitude. Therefore a rising threshold or falling amplitude is not automatically neural injury if the anesthetic state changed. Correlate with train-of-four or the anesthesia team's assessment, recent paralytic administration, temperature and relevant physiologic changes. Do not memorize a single mA threshold or amplitude-loss percentage as a universal cross-platform injury cutoff.

AUDITORY MONITORING — ABR/BAEP is a far-field averaged response with characteristic waves generated along the auditory pathway. In hearing-preservation vestibular schwannoma surgery, changes in wave morphology, amplitude and latency are interpreted as trends relative to a reproducible baseline. Because far-field responses require averaging, they are not instantaneous; surgical injury can occur faster than a slowly updating averaged waveform. Near-field CNAP/DNAP-type techniques can provide larger/faster responses in selected settings but require different electrodes/exposure and are not interchangeable with ABR. The current literature does not justify treating one absolute latency shift, amplitude percentage or waveform rule as a universal rescue threshold across every device, approach and baseline hearing level.

AUDITORY TECHNICAL DIFFERENTIAL — when ABR worsens, STOP the provoking maneuver first, then consider both biologic and technical causes. Verify the acoustic stimulus and ear insert/transducer, recording leads and impedance, masking/noise assumptions, electrical interference and whether drilling artifact or irrigation conditions are degrading the tracing. Check blood pressure, temperature and other systemic changes that can affect neural conduction. In otologic surgery, also think specifically about cochlear perfusion, labyrinthine trauma, excessive traction on CN VIII, thermal/mechanical injury during internal-auditory-canal drilling, and local fluid/blood effects. A deteriorating auditory signal is not automatically cochlear-nerve transection, but it is not something to ignore while continuing the same maneuver.

SUDDEN FACIAL SIGNAL LOSS — treat unexpected loss as a rescue problem before labeling it transection. First STOP traction, drilling, cautery or dissection. Keep the field stable and identify whether the change was temporally linked to a specific maneuver. Then troubleshoot the system: power/mute/settings, recording and reference electrodes, impedance, lead connections, stimulating probe/cable, current shunting through fluid, and whether the probe is contacting the intended tissue. Ask anesthesia immediately about neuromuscular blockade. Stimulate a known intact accessible segment or appropriate control point when safe. If nothing responds anywhere after a previously robust baseline, technical/anesthetic failure rises on the differential; if responses are preserved distally but fail across a newly manipulated segment, focal neural compromise becomes more concerning.

LOCALIZE, RESCUE, DECIDE — once technical and anesthetic causes have been addressed, inspect the operative danger zone. Release traction or compression, stop thermal/mechanical stress, irrigate when appropriate, and avoid blind cautery near a threatened nerve. In skull-base surgery, compare proximal/distal facial responses when anatomy safely permits. For hearing deterioration, stop the causative maneuver, reassess drilling/traction/irrigation and hemodynamic conditions, and allow the signal an opportunity to recover rather than repeatedly reproducing the insult. Monitoring has value only if its warning changes behavior.

If the nerve is visibly divided, the problem is no longer one of waveform interpretation: protect the ends and proceed to the appropriate immediate repair/reconstruction strategy when feasible. If anatomy appears intact but monitoring remains meaningfully degraded, the senior decision may be to alter the dissection plane, leave adherent tumor, accept subtotal/near-total resection, stage, or otherwise change the surgical objective when functional preservation outweighs additional tumor removal. The 2026 CNS vestibular-schwannoma guideline update supports intraoperative cranial-nerve monitoring in all vestibular schwannoma cases and emphasizes functional preservation; it also notes that no single facial or hearing monitoring strategy has emerged as universally superior and that the evidence base remains largely lower-level comparative evidence.

HEARING-VERSUS-FACIAL DISAGREEMENT — signals can disagree because they sample different nerves/functions and have different temporal resolution. A stable facial EMG does not reassure you about cochlear-nerve or cochlear injury. Conversely, an ABR change does not establish facial injury. When both deteriorate during the same maneuver, consider a common mechanical, vascular, thermal or technical event but still troubleshoot each channel independently. The mistake is collapsing all monitoring into one binary 'monitor is good/bad' interpretation.

LOWER CRANIAL NERVES — in selected jugular-foramen, lower-skull-base or CPA operations, motor EMG/stimulation of IX/X/XI/XII-related targets may be used when the nerve and end-organ recording strategy are appropriate. These modalities require procedure-specific setup and have their own anesthesia/technical constraints. The resident-level principle is to know why a nerve is being monitored, what muscle or physiologic output represents it, and what change would make the surgeon stop or alter the maneuver; do not extrapolate facial-nerve numeric thresholds to another cranial nerve.

NUMERIC PARAMETERS — record baseline and within-case trend rather than worshiping an isolated number. Facial monitoring commonly follows stimulation current/threshold and evoked amplitude; ABR follows waveform presence, morphology, amplitude and latency; near-field auditory techniques follow their own response characteristics. Published series use different devices, electrode sites, averaging schemes, muscles, stimulation techniques, tumor sizes and outcome definitions. Directional changes can be clinically useful, but a single universal stimulation threshold, amplitude-drop percentage, latency shift or alarm cutoff across neurotologic procedures is not supported. Manufacturer presets and device labeling are not universal physiologic laws.

EVIDENCE BOUNDARY — AAO-HNS guidance and its task-force consensus support strategic cranial-nerve monitoring as an adjunct to anatomy, with emphasis on setup, anesthesia, troubleshooting and documentation. Current CNS evidence-based guidance for vestibular schwannoma specifically recommends intraoperative cranial-nerve monitoring and recognizes combined strategies for facial and hearing preservation while acknowledging uncertainty over the optimal modality. A 2026 systematic review of auditory monitoring (PMID 42036522) separates diagnostic/predictive threshold performance from proof that an intervention triggered by the monitor improves hearing; those are not the same evidence question. Heterogeneous facial-monitoring parameter studies likewise do not create a universal predictive cutoff.

RETRACTION HYGIENE — a 2026 parotid facial-monitoring meta-analysis, PMID 41353726, was formally retracted July 28, 2026; the retraction notice is PMID 42520282. Its pooled benefit estimates must not be taught as affirmative evidence. This matters because a superficially impressive effect estimate can persist in notes after the underlying paper has been withdrawn. Current teaching should rely on non-retracted sources and explicitly label procedure-specific evidence strength.

FDA/SOCIETY BOUNDARY — intraoperative monitoring systems are regulated devices with manufacturer-specific indications, warnings, electrode configurations and settings. There is no single FDA indication or major society statement that converts one stimulation current, amplitude percentage or latency value into a universal alarm criterion for all neurotologic cranial nerves and operations. Society recommendations define appropriate use and evidence boundaries; anatomy, procedure, baseline function, modality and device instructions determine implementation.

Senior synthesis — use NERVE, BASELINE, CHANGE, STOP, SYSTEM, PHYSIOLOGY, LOCALIZE, RESCUE, DECIDE. NERVE: identify the function at risk and choose the matching modality. BASELINE: prove the channel is reproducible before danger-zone work. CHANGE: correlate a trend with the exact maneuver and modality. STOP: halt traction/drilling/cautery before troubleshooting. SYSTEM: check electrodes, transducers, leads, probe, impedance, noise and current shunting. PHYSIOLOGY: assess neuromuscular blockade for motor channels and systemic/hemodynamic/temperature factors for all channels. LOCALIZE: use known facial segments or modality-specific controls when safe. RESCUE: release mechanical/thermal stress and correct reversible causes. DECIDE: if meaningful deterioration persists, change the operative maneuver or objective rather than trusting the monitor to protect a function you continue to endanger."""

TRAPS = [
    "Treating neurotologic cranial-nerve monitoring as a single generic alarm rather than modality-specific monitoring of different nerves and functions.",
    "Using facial EMG as a substitute for facial-nerve anatomy or visual identification.",
    "Failing to establish reproducible facial and auditory baselines before entering the highest-risk portion of the operation.",
    "Allowing dense neuromuscular blockade when motor EMG is required and then calling the absent response a neural event.",
    "Interpreting a higher facial stimulation threshold after partial paralysis as proof of nerve injury.",
    "Treating every transient free-running facial EMG burst as permanent injury rather than correlating it with the maneuver and subsequent function.",
    "Ignoring repetitive neurotonic facial activity during traction, drilling or thermal manipulation.",
    "Assuming a stable facial signal means hearing is safe despite deterioration of ABR/BAEP.",
    "Treating an ABR/BAEP change as instantaneous even though far-field responses require averaging and may lag the surgical event.",
    "Memorizing one ABR latency shift or amplitude-loss percentage as a universal hearing-preservation bailout threshold.",
    "Equating ABR/BAEP and near-field CNAP/DNAP as if they have identical temporal resolution, setup and evidence.",
    "Continuing internal-auditory-canal drilling while troubleshooting an actionable auditory deterioration instead of stopping the provoking maneuver first.",
    "Blindly escalating facial stimulation current when the probe, cable, electrodes, current shunting and anesthetic state have not been checked.",
    "Assuming simultaneous silence across channels proves multiple cranial nerves were transected before checking shared technical or physiologic causes.",
    "Failing to compare proximal and distal facial responses when anatomy safely permits localization of a new conduction problem.",
    "Continuing aggressive tumor removal despite persistent functional deterioration when changing the surgical objective may better preserve facial or hearing function.",
    "Extrapolating facial-nerve numeric stimulation thresholds to lower cranial nerves.",
    "Using the retracted PMID 41353726 as affirmative evidence for monitoring benefit.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Neurotologic monitoring is anatomy-led and modality-specific: establish facial/auditory baselines, interpret within-case trends, control anesthetic/technical confounders, and make deterioration trigger an immediate stop-troubleshoot-localize-rescue decision.",
    "board_pearl": "A monitoring change is not a diagnosis. Stop the provoking maneuver, verify the modality and reversible confounders, localize when possible, then change the operative plan if meaningful deterioration persists.",
    "depth_layers_v224": {
        "foundation":"Cranial-nerve anatomy, facial EMG physiology, ABR/BAEP versus near-field auditory monitoring, setup and anesthetic/technical confounders.",
        "application":"Within-case facial and auditory trend interpretation, modality-specific warning patterns, triggered stimulation, and procedure-specific parameter limits.",
        "senior_decision":"Immediate stop-and-rescue response to signal deterioration, technical/physiologic troubleshooting, neural localization, hearing/facial preservation and changing the surgical objective when function is threatened.",
    },
    "common_traps_v224": TRAPS,
    "deliberate_review_v224": {
        "why_review":"High-yield neurotologic OR danger-zone concept: residents must distinguish facial versus auditory warning signals, technical/anesthetic artifact and true neural injury while stopping ongoing mechanical or thermal harm.",
        "retrieval_prompts":["What does facial free-running EMG tell you versus triggered stimulation?","Why can neuromuscular blockade mimic facial signal loss?","How do ABR/BAEP and near-field cochlear responses differ?","What is the immediate sequence after sudden facial or hearing-monitor deterioration?","When should persistent monitoring change alter vestibular-schwannoma resection goals?"],
        "spacing":"Revisit before mastoid, CPA/vestibular-schwannoma and skull-base cases; repeat whenever a numeric threshold is being recalled as universal rather than modality/procedure/device-specific.",
    },
    "source_refs_v224": SOURCE_REFS_V224,
    "evidence_distinction_v224": "Durable textbook principles are anatomy-led cranial-nerve preservation, monitoring as an adjunct, modality-specific physiology, control of anesthesia/technical confounders and immediate stop/troubleshoot/rescue when a signal deteriorates. Current AAO-HNS guidance/consensus and the 2026 CNS vestibular-schwannoma guideline support strategic intraoperative cranial-nerve monitoring, while current auditory and facial literature does not establish one universal cross-platform predictive threshold. FDA device regulation and manufacturer settings do not create a universal clinical alarm criterion. The 2026 Barrameda meta-analysis (PMID 41353726) was retracted July 28, 2026 (PMID 42520282) and is excluded as affirmative evidence.",
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
