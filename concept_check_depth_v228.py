"""v20.28 exact-live Hemostasis / Coagulopathy / Antithrombotic Management in ENT depth cohort.

Durable clotting physiology, surgical hemostasis and ENT bleeding principles are cross-referenced
to Cummings 7e, Pasha 6e and K.J. Lee 12e in the user's connected Google Drive. Current
perioperative antithrombotic and reversal decisions are intentionally separated from textbook
principles and anchored to current ACC/AHA, CHEST, AAO-HNS and FDA guidance/status.
"""
from copy import deepcopy
from concept_check_board_repair_v177 import _find_module

QIDS = ["cc-v112-rec-general-ent-emergencies-hemostasis-coagulopathy-antithrombotic-management-in-ent"]
CID = "v6-general-ent-emergencies-hemostasis-coagulopathy-antithrombotic-management-in-ent"
TOPIC = "Hemostasis / Coagulopathy / Antithrombotic Management in ENT"
PROMPT = (
    "An ENT patient with active postoperative or mucosal bleeding is taking an antithrombotic drug, or a patient on chronic "
    "anticoagulation needs an urgent or elective head-and-neck procedure. How should a resident distinguish surgical-source "
    "bleeding from systemic coagulopathy, interpret platelet/coagulation tests without falsely excluding a DOAC effect, decide "
    "when local control and airway rescue outrank laboratory normalization, choose agent-specific reversal when truly indicated, "
    "and balance perioperative interruption, bridging, and restart against the patient's thrombotic risk?"
)

ANSWER = r'''Hemostasis in ENT is not an INR problem; it is a **patient + drug + bleeding source + procedure + thrombotic-risk problem**. The senior resident must run two tracks in parallel: control a dangerous anatomic source while identifying any correctable systemic contribution. A brisk tonsillar-bed vessel, expanding neck hematoma, posterior epistaxis, injured named vessel, or tracheostomy-related arterial bleed is not made safe merely by improving a laboratory number. Conversely, repeated cautery or packing will fail if severe thrombocytopenia, residual anticoagulant effect, hypothermia, acidosis, or another major coagulopathy is ignored.

**1. Start with physiology and the phenotype of bleeding.** Primary hemostasis is platelet adhesion/activation/aggregation at the injured vessel wall; von Willebrand factor and platelet receptors are central to forming the initial platelet plug. Secondary hemostasis generates fibrin through the coagulation cascade and stabilizes that plug. This distinction helps interpret the bedside phenotype: mucocutaneous oozing, petechiae, easy bruising and recurrent epistaxis suggest a platelet/von-Willebrand problem, whereas deep tissue bleeding and delayed rebleeding can suggest coagulation-factor deficiency. Real patients can have both, and major surgical bleeding itself can create dilutional, consumptive, hypothermic and acidotic coagulopathy.

K.J. Lee 12e explicitly emphasizes that PT and aPTT are artificial screening reflections of hemostasis and that some drugs, including direct oral anticoagulants, do **not consistently affect these screening tests**. That remains a key board and OR trap: a normal PT/INR or aPTT does not reliably prove absence of clinically important apixaban, rivaroxaban, edoxaban, or dabigatran effect. Ask the exact agent, dose, **time of last dose**, renal function, hepatic function, indication, adherence, concomitant antiplatelets and whether a calibrated drug-specific or anti-Xa assay is available. Do not delay lifesaving source control waiting for a perfect assay.

**2. In active major ENT bleeding, airway/resuscitation/source control run before and alongside reversal.** Define severity clinically. Airway compromise, hemodynamic instability, ongoing transfusion requirement, bleeding into a critical space, or hemorrhage requiring urgent procedural control is major regardless of a deceptively reassuring first hemoglobin. Secure appropriate IV access and blood-bank support, correct hypothermia and major metabolic derangements, stop the responsible antithrombotic when appropriate, and call for senior/anesthesia/hematology/interventional support early when the anatomy or drug makes failure costly.

For an expanding post-thyroidectomy or post-neck-dissection hematoma with respiratory compromise, the bailout is immediate decompression/airway management and definitive operative hemostasis; reversal must not become a reason to wait. For post-tonsillectomy hemorrhage, suction, airway planning, volume resuscitation, operative control when indicated and recognition that swallowed blood can hide severity are central. For posterior epistaxis, directed topical/packing/cautery/endoscopic or endovascular source control follows the anatomy and severity. The AAO-HNS epistaxis guideline specifically includes patients using anticoagulant or antiplatelet medications and supports using local first-line measures before reflexively reversing or withdrawing therapy when bleeding is not life-threatening. The lesson is not “never reverse”; it is **do not substitute systemic reversal for local hemostasis when local control is appropriate**.

**3. Reverse the actual drug only when the clinical benefit justifies thrombosis risk.** Reversal/hemostatic products carry real thrombotic risk, so they are not routine for every minor nosebleed or every mildly abnormal test. Current ACC bleeding guidance reserves reversal/hemostatic agents for life-threatening or major bleeding that is not controlled with initial measures, while source control and resuscitation proceed. Drug identity and timing matter.

For **warfarin/VKA-associated major bleeding or urgent surgery**, vitamin K restores synthesis of vitamin-K-dependent factors but is not instant. FDA-approved four-factor PCC products provide rapid replacement for urgent VKA reversal; Kcentra's FDA indication includes adult patients with acute major bleeding or need for urgent surgery/invasive procedure. In major VKA bleeding, vitamin K and rapid factor replacement are complementary rather than competing ideas. FFP is a fallback when appropriate PCC is unavailable but requires substantially more volume and slower administration. Do not give vitamin K as a generic antidote to a DOAC.

For **unfractionated heparin**, protamine is the classic reversal agent; dose must account for the amount and recency of heparin exposure because excess protamine itself has adverse effects. Protamine only partially neutralizes the anti-Xa effect of **LMWH**, so do not promise complete normalization. For **dabigatran**, idarucizumab (Praxbind) is FDA-labeled when reversal is needed for emergency surgery/urgent procedures or life-threatening/uncontrolled bleeding. Renal dysfunction can prolong dabigatran exposure and should raise concern for persistence or rebound.

For **factor-Xa inhibitors**, old teaching must be updated. Andexanet alfa (Andexxa) had been FDA-approved for rivaroxaban/apixaban-associated life-threatening or uncontrolled bleeding, but FDA reported in December 2025 that postmarketing/confirmatory safety data showed increased thrombotic events and that the agency considered the risks to outweigh the benefits; AstraZeneca ended U.S. commercial sales on **December 22, 2025**. Therefore a 2026 ENT curriculum must not teach andexanet as an ordinarily available U.S. rescue drug. When clinically important apixaban/rivaroxaban effect is suspected and life-threatening bleeding requires hemostatic reversal, use the institution's current hematology/pharmacy protocol; four-factor PCC is commonly used as a nonspecific/off-label strategy when a specific antidote is unavailable, but it is not an FDA-approved specific antidote for factor-Xa inhibitors. Explicitly separate historical guideline recommendations from current U.S. availability.

**4. Antiplatelet therapy requires indication-aware reasoning, not automatic platelet transfusion.** Aspirin and P2Y12 inhibitors can materially increase surgical bleeding, but the danger of stopping them varies dramatically. A patient with a recent coronary stent is not equivalent to a patient taking aspirin for low-value primary prevention. Before an elective interruption, identify why the drug exists, date/type of PCI or recent acute coronary syndrome, procedure bleeding risk, and whether surgery can be delayed. Current ACC/AHA perioperative guidance emphasizes multidisciplinary decisions in high-risk cardiovascular patients. Do not reflexively stop dual antiplatelet therapy or transfuse platelets simply because a patient is bleeding; treat the source, assess severity and involve the relevant teams for high-stakes reversal/interruption decisions.

**5. Elective perioperative anticoagulation is a risk-balancing exercise.** Ask two independent questions: how dangerous is bleeding for this ENT procedure, and how dangerous is temporary thrombosis for this patient? A small mucosal procedure and a large skull-base, airway, neck, or reconstructive operation have different consequences. For DOAC interruption, renal function and procedure bleeding risk determine how long drug effect may persist. CHEST 2022 suggests stopping most DOACs before elective procedures and resuming roughly 24 hours after low/moderate-bleeding-risk procedures versus 48–72 hours after high-bleeding-risk procedures when hemostasis is secure; dabigatran needs special attention to renal clearance.

**Bridging is not routine.** CHEST recommends against heparin bridging for atrial-fibrillation patients requiring VKA interruption and suggests against bridging for many mechanical-valve/VTE patients and for DOAC interruption. The 2024 ACC/AHA perioperative guideline similarly notes that bridging most patients on therapeutic anticoagulation can cause harm from increased bleeding, while recognizing selected very-high-thrombotic-risk situations—such as certain mechanical mitral valves, recent left-ventricular thrombus or AF with recent stroke—where bridging may be reasonable. This is a genuine nuance rather than a contradiction: broad routine bridging is discouraged, but an individualized high-risk exception may exist. ENT should coordinate those exceptions with cardiology/hematology rather than inventing a universal rule.

**6. Restart timing is an active senior decision.** Once hemostasis is achieved, continuing to hold anticoagulation indefinitely is not benign. Reassess the reason for anticoagulation, source control, rebleeding consequence, renal function and whether a critical-site bleed or unidentified source argues for delay. Most patients with ongoing thromboembolic indication should restart when medically safe; exact timing is procedure- and patient-specific. Document who owns the restart decision. A vague discharge instruction to “ask your doctor later” can convert perioperative bleeding avoidance into preventable stroke, valve thrombosis or VTE.

**7. Build a differential for unexpected operative bleeding.** If diffuse oozing persists despite technically sound surgical control, reassess platelet count, fibrinogen, PT/INR, aPTT, medication exposure, liver disease, renal/uremic platelet dysfunction, massive-transfusion dilution, DIC, inherited bleeding history and temperature/acidosis. A patient with previously unexplained recurrent epistaxis, menorrhagia, dental bleeding or family history may need von Willebrand/platelet-disorder evaluation rather than being labeled “just a bleeder.” Conversely, an isolated abnormal screening test without a compatible clinical problem should not trigger indiscriminate plasma or factor products.

Tranexamic acid can be a useful **adjunct** in selected mucosal or perioperative bleeding pathways, but it does not ligate a vessel, decompress a neck hematoma, repair a carotid injury, or replace operative/endovascular control. The same principle applies to topical hemostatic agents and fibrin sealants: they are adjuncts when standard technique is difficult or insufficient, not permission to abandon anatomy and surgical judgment.

**8. Senior-resident bailout sequence.** When confronted with major ENT bleeding, say the priorities out loud: **airway → resuscitation → expose/localize/control the source → identify the antithrombotic/coagulopathy → give indication-appropriate reversal without delaying definitive control → reassess for continued bleeding and thrombosis → make a deliberate restart plan**. Escalate to the OR or endovascular rescue when packing/cautery is failing or the bleeding anatomy demands it. Escalate immediately for sentinel tracheostomy bleeding/TIF concern, expanding neck hematoma, uncontrolled post-tonsillectomy hemorrhage, carotid blowout risk, or hemodynamic instability.

The quality endpoint is not a normal INR. It is a living patient with a protected airway, controlled bleeding source, corrected clinically important coagulopathy, minimized reversal-related thrombosis risk, and a safe plan for resuming the antithrombotic therapy that was prescribed for a reason.'''

TRAPS = [
    "Treating the INR instead of the airway, hemodynamics and bleeding source.",
    "Assuming a normal PT/INR or aPTT excludes clinically important DOAC effect.",
    "Forgetting that last dose and renal function are essential to estimating residual DOAC activity.",
    "Delaying decompression or return to the OR for an expanding neck hematoma while waiting for laboratory normalization.",
    "Using vitamin K as if it reverses apixaban, rivaroxaban or dabigatran.",
    "Giving a reversal product for a minor controlled bleed without weighing thrombosis risk.",
    "Teaching andexanet as routinely available in the United States after commercial sales ended December 22, 2025.",
    "Calling four-factor PCC an FDA-approved specific antidote for factor-Xa inhibitors rather than a nonspecific/off-label strategy.",
    "Forgetting that protamine only partially reverses LMWH anti-Xa activity.",
    "Assuming FFP is equivalent in speed and volume to four-factor PCC for urgent VKA reversal.",
    "Stopping dual antiplatelet therapy reflexively without identifying a recent coronary stent or ACS indication.",
    "Reflexively transfusing platelets for any antiplatelet-associated ENT bleed without a severity- and indication-based plan.",
    "Bridging every interrupted warfarin patient despite contemporary guidance against routine bridging.",
    "Never considering a selected very-high-thrombotic-risk bridging exception when current cardiovascular guidance supports individualized use.",
    "Restarting anticoagulation on a calendar without confirming hemostasis and rebleeding consequence.",
    "Failing to restart indicated anticoagulation because nobody was assigned ownership of the postoperative decision.",
    "Using tranexamic acid or topical hemostatic material as a substitute for named-vessel source control.",
    "Ignoring hypothermia, acidosis, thrombocytopenia, low fibrinogen, liver disease or DIC during persistent diffuse operative bleeding.",
]

SOURCE_REFS_V228 = [
    {"type": "textbook", "citation": "Cummings Otolaryngology–Head and Neck Surgery, 7th ed. Connected Google Drive file ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; durable ENT operative hemostasis, hemorrhage-source and complication principles. File identity reconfirmed 2026-09-12; the 765 MB compressed PDF exceeds connector full-text fetch limits, so current drug/reversal claims are not inferred from it."},
    {"type": "textbook", "citation": "Pasha R, Golub JS. Otolaryngology—Head and Neck Surgery: Clinical Reference Guide, 6th ed (2022). Connected Google Drive file ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Epistaxis chapter pp. 29-31 cross-referenced for anticoagulant/antiplatelet and systemic coagulopathy contributors; publisher notice explicitly requires current verification of medication indications/doses."},
    {"type": "textbook", "citation": "K.J. Lee's Essential Otolaryngology, 12th ed. Connected Google Drive file ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Chapter 5, Surgical Hemostasis and Clotting Mechanisms, pp. 104-119; pp. 107-113 cross-referenced for primary/secondary hemostasis, screening-test limitations, DOAC assay caveats and antithrombotic principles."},
    {"type": "guideline", "citation": "2024 AHA/ACC/ACS/ASNC/HRS/SCA/SCCT/SCMR/SVM Guideline for Perioperative Cardiovascular Management for Noncardiac Surgery. Current perioperative anticoagulation, selected high-thrombotic-risk bridging and multidisciplinary cardiovascular decision boundary."},
    {"type": "guideline", "citation": "Douketis JD et al. Perioperative Management of Antithrombotic Therapy: CHEST Clinical Practice Guideline. Chest. 2022;162:e207-e243. doi:10.1016/j.chest.2022.07.025. Routine bridging generally discouraged; DOAC hold/restart recommendations are procedure-bleeding-risk dependent."},
    {"type": "society", "citation": "Tunkel DE et al. AAO-HNSF Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020. Multidisciplinary guideline includes anticoagulant/antiplatelet patients and local-first management logic for non-life-threatening epistaxis."},
    {"type": "regulatory", "citation": "U.S. FDA Kcentra product information: urgent reversal of VKA-associated acquired coagulation factor deficiency in adults with acute major bleeding or need for urgent surgery/invasive procedure. Current FDA page reconfirmed 2026-09-12."},
    {"type": "regulatory", "citation": "U.S. FDA Praxbind (idarucizumab) prescribing information: dabigatran reversal for emergency surgery/urgent procedures or life-threatening/uncontrolled bleeding."},
    {"type": "regulatory", "citation": "U.S. FDA Safety Communication, Dec 18/22 2025: FDA concluded Andexxa risks outweigh benefits after thromboembolic safety findings; AstraZeneca ended U.S. commercial sales December 22, 2025. This supersedes older availability assumptions."},
    {"type": "consensus", "citation": "2020 ACC Expert Consensus Decision Pathway on Management of Bleeding in Patients on Oral Anticoagulants. Source control, reversal threshold, VKA/dabigatran/FXa strategies and restart framework; factor-Xa section interpreted in light of FDA's 2025 Andexxa safety/availability update."},
]

COHORT = {
    QIDS[0]: {
        "canonical_topic": TOPIC,
        "concept_id": CID,
        "prompt": PROMPT,
        "answer_text": ANSWER,
        "depth_layers_v228": {
            "foundation": "Primary/secondary hemostasis, bleeding phenotype, coagulation-test limitations, antithrombotic mechanism and drug-clearance reasoning.",
            "application": "Run airway/source control and agent-specific reversal in parallel; plan elective interruption, local epistaxis control, laboratory evaluation and safe postoperative restart.",
            "senior_decision": "Decide when reversal benefit exceeds thrombosis risk, when not to delay OR/endovascular rescue for laboratory normalization, when routine bridging is harmful versus a selected exception, and how 2025 FDA Andexxa safety/availability changes alter 2026 practice.",
        },
        "common_traps_v228": TRAPS,
        "deliberate_review_v228": {
            "priority": "high",
            "review_after_days": [2, 7, 21, 60],
            "reason": "cross-cutting OR/postoperative hemorrhage topic with high-consequence airway, reversal, DOAC-assay, coronary-stent, bridging and restart traps",
        },
        "source_refs_v228": SOURCE_REFS_V228,
        "evidence_distinction_v228": (
            "Durable textbook principles define primary/secondary hemostasis, surgical source control, bleeding phenotype and screening-test limitations. "
            "Current ACC/AHA and CHEST guidance governs perioperative interruption/bridging/restart; AAO-HNS governs the ENT-specific epistaxis local-control boundary; FDA labeling governs Kcentra and Praxbind indications. "
            "Older guideline statements that assumed U.S. andexanet availability are explicitly superseded operationally by the December 2025 FDA safety communication and end of U.S. commercial sales. "
            "Where CHEST broadly discourages bridging and ACC/AHA recognizes selected very-high-thrombotic-risk exceptions, the disagreement is presented as an individualized risk boundary rather than silently harmonized."
        ),
        "task_alignment_v228": True,
    }
}


def apply_concept_check_task_alignment_v228(checks, deep_modules, v6_item_id):
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
