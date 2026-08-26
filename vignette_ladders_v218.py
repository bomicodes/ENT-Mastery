"""v21.8 — final Rhinology learning-ladder closure.

The live domain inventory identified AERD and CSF Rhinorrhea as the final two
canonical Rhinology / Allergy / Skull Base concepts without deliberate staged
coverage. Both receive only the layers actually missing: recognition,
application/management, and senior decision-making.
"""
DOMAIN = "Rhinology / Allergy / Skull Base"


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": why_wrong,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True,
    }


VIGNETTES_V218 = [
    _q(
        "v218_rhi_aerd_fnd", "AERD", "foundation",
        "A 39-year-old with asthma and recurrent bilateral nasal polyps reports wheezing, nasal congestion, and flushing within an hour of taking aspirin or ibuprofen. Which diagnosis best unifies the presentation?",
        ["Aspirin-exacerbated respiratory disease", "Isolated IgE-mediated aspirin allergy", "Allergic fungal rhinosinusitis", "Granulomatosis with polyangiitis"], 0,
        "AERD is the clinical syndrome of asthma, chronic rhinosinusitis with nasal polyps, and respiratory reactions to aspirin or other cyclooxygenase-1 inhibitors. The reaction history is part of the phenotype and should be sought specifically in patients with asthma plus recurrent polyposis.",
        ["Correct. Asthma, CRSwNP, and reproducible respiratory reactions to COX-1 inhibitors form the classic AERD phenotype.", "A selective drug allergy does not explain the characteristic cross-reactive respiratory phenotype with asthma and nasal polyposis.", "AFRS can cause polyps but does not characteristically produce COX-1-triggered bronchospasm.", "GPA is a destructive systemic vasculitis and does not fit this reproducible NSAID-triggered triad."],
        "Polyps plus asthma should trigger one additional history question: what happens after aspirin or other NSAIDs?",
        "Why can a patient who previously tolerated aspirin still develop AERD later in adulthood?",
    ),
    _q(
        "v218_rhi_aerd_app", "AERD", "application",
        "A patient with confirmed AERD has undergone appropriate ESS for severe polyp burden and remains highly symptomatic despite topical corticosteroid therapy. Which management discussion is most appropriate?",
        ["Choose one universal treatment because surgery permanently corrects the inflammatory disorder", "Discuss phenotype-directed postoperative options such as aspirin desensitization/maintenance therapy when appropriate or biologic therapy, while continuing topical anti-inflammatory care and asthma management", "Use repeated antibiotics indefinitely even without bacterial exacerbations", "Avoid all asthma-directed treatment because the disease is confined to the sinuses"], 1,
        "ESS improves access, ventilation, and inflammatory burden but does not cure AERD. Persistent disease is managed longitudinally with topical therapy and coordinated asthma care; selected patients may benefit from aspirin desensitization followed by maintenance aspirin therapy or from a biologic, depending on contraindications, prior response, comorbidities, treatment goals, and shared decision-making.",
        ["Surgery treats anatomy and inflammatory load but does not eliminate the underlying AERD biology.", "Correct. AERD care is multimodal and individualized rather than a single mandatory postoperative pathway.", "Antibiotics treat bacterial infection, not the underlying type-2/arachidonic-acid inflammatory phenotype.", "Upper- and lower-airway disease are linked; asthma control is an essential part of management."],
        "In AERD, ESS is often one component of long-term inflammatory control, not the finish line.",
        "What comorbidities or medication risks could make maintenance aspirin therapy unattractive and shift the balance toward another strategy?",
    ),
    _q(
        "v218_rhi_aerd_snr", "AERD", "senior_decision",
        "A patient labeled as having AERD reports a single episode of urticaria after naproxen but has no asthma, no nasal polyps, and has subsequently tolerated aspirin. They request aspirin desensitization because they were told it is standard for 'NSAID allergy.' What is the best attending-level decision?",
        ["Proceed with desensitization because every NSAID reaction is AERD", "Schedule ESS first even though there is no sinonasal disease", "Reconsider the diagnosis and characterize the drug-reaction phenotype rather than exposing the patient to an AERD-specific treatment without the clinical syndrome", "Start a biologic solely because naproxen caused hives once"], 2,
        "AERD is not a synonym for any NSAID hypersensitivity. It requires the appropriate respiratory phenotype—typically asthma and CRSwNP with COX-1-triggered upper/lower-airway reactions. A history suggesting a selective cutaneous drug reaction should be evaluated on its own terms rather than automatically routed to aspirin desensitization for AERD.",
        ["AERD-specific desensitization should not be offered simply because an NSAID reaction occurred.", "There is no surgical target without sinonasal inflammatory disease.", "Correct. Senior decision-making starts by validating the phenotype before committing the patient to a disease-specific intervention.", "Biologics require an appropriate inflammatory indication; one isolated drug reaction does not establish one."],
        "Before treating AERD, prove the patient actually has the AERD phenotype rather than another form of NSAID hypersensitivity.",
        "When the history is suggestive but uncertain, what role can supervised aspirin challenge have in expert allergy care?",
    ),

    _q(
        "v218_rhi_csf_fnd", "CSF Rhinorrhea", "foundation",
        "An adult develops persistent unilateral clear watery rhinorrhea that increases with bending forward and has a salty taste after head trauma. Which test is most specific for confirming that the nasal fluid is cerebrospinal fluid?",
        ["Routine bacterial culture", "Nasal-fluid glucose testing", "Beta-2 transferrin or beta-trace protein testing", "Serum total IgE"], 2,
        "Suspected CSF rhinorrhea should be confirmed with a CSF-specific protein assay such as beta-2 transferrin or beta-trace protein. Bedside glucose testing is insufficiently reliable and should not be used to establish or exclude the diagnosis.",
        ["Culture can identify infection but does not establish that the fluid is CSF.", "Glucose measurements are vulnerable to false results and are not the preferred confirmatory test.", "Correct. CSF-specific protein testing provides biochemical confirmation before anatomic localization and repair planning.", "Total IgE evaluates allergic sensitization rather than a skull-base leak."],
        "Unilateral positional watery rhinorrhea is not automatically rhinitis—confirm CSF with a CSF-specific assay.",
        "Why does intermittent leakage sometimes make specimen collection and localization difficult?",
    ),
    _q(
        "v218_rhi_csf_app", "CSF Rhinorrhea", "application",
        "Beta-2 transferrin confirms CSF rhinorrhea. The patient has no acute neurologic deficit. What is the best next localization strategy before repair?",
        ["Treat empirically with antihistamines and skip imaging", "Use high-resolution thin-cut skull-base CT to identify bony defects and MRI when needed to assess meningoencephalocele/soft tissue, integrating both with endoscopic findings", "Perform blind intranasal cautery at the suspected side", "Use a plain sinus radiograph as definitive localization"], 1,
        "After biochemical confirmation, high-resolution CT defines skull-base bony anatomy and potential defects, while MRI adds information about meningocele/encephalocele and soft tissue. Localization should integrate imaging, history, and endoscopy; specialized intrathecal studies are reserved for selected difficult cases rather than routine first-line use.",
        ["Antihistamines do not localize or repair a skull-base defect.", "Correct. CT and MRI provide complementary bony and soft-tissue maps for safe repair planning.", "Blind treatment risks missing the defect and injuring normal skull base.", "Plain radiographs lack the detail needed for contemporary skull-base localization."],
        "Confirm the fluid first, then map bone and soft tissue before entering the skull-base repair pathway.",
        "When might CT or MR cisternography or intrathecal fluorescein be considered in a difficult-to-localize leak?",
        "OR_prep",
    ),
    _q(
        "v218_rhi_csf_snr", "CSF Rhinorrhea", "senior_decision",
        "An obese middle-aged patient has a spontaneous cribriform CSF leak with an encephalocele and imaging signs suggestive of chronically elevated intracranial pressure. Endoscopic repair is planned. What additional attending-level issue should be addressed to reduce long-term recurrence risk?",
        ["Treat the skull-base defect as purely local and never reassess intracranial pressure", "Delay repair indefinitely because spontaneous leaks always close with observation", "Prescribe long-term antibiotics instead of repairing the leak", "Evaluate and manage an underlying intracranial-pressure disorder in parallel with definitive leak repair and postoperative surveillance"], 3,
        "Spontaneous anterior skull-base leaks are associated in many patients with chronically elevated intracranial pressure/idiopathic intracranial hypertension physiology. Durable management therefore includes anatomic repair plus assessment and treatment of the pressure driver when clinically appropriate, rather than viewing the defect as an isolated hole.",
        ["Ignoring a persistent pressure driver can contribute to recurrent or new skull-base defects.", "Persistent spontaneous CSF leaks carry meningitis risk and generally require a definitive management plan rather than indefinite observation.", "Antibiotics do not close the defect or correct the underlying pressure physiology.", "Correct. Senior care treats both the leak and the condition that may have produced it."],
        "A spontaneous CSF leak can function as a pressure-release pathway; closing it without considering the pressure physiology can expose the underlying problem.",
        "What postoperative symptoms or ophthalmologic findings would prompt reassessment for intracranial hypertension after successful closure?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v218(challenges, item_id_fn):
    existing = {q.get("id") for q in challenges if q.get("id")}
    added = []
    for row in VIGNETTES_V218:
        if row["id"] in existing:
            continue
        item = dict(row)
        item["concept_id"] = item_id_fn(DOMAIN, item["topic"])
        challenges.append(item)
        existing.add(item["id"])
        added.append(item["id"])
    return {"added": len(added), "ids": added, "topics": ["AERD", "CSF Rhinorrhea"]}
