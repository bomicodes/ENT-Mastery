"""v20.7 — deliberate learning-ladder curation, Rhinology pass 3.

Reviews five more canonical Rhinology foundations. The existing Draf III
second-pass OR case is reused as the application layer; remaining questions are
added only where application or senior judgment is materially missing.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong,
       pearl, curveball, focus):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic,
        "learning_stage": stage, "stem": stem, "choices": choices,
        "answer": answer, "explanation": explanation, "why_wrong": why_wrong,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette",
        "focus": focus, "ladder_reviewed": True,
    }


REVIEWED_FOUNDATION_IDS_V207 = {
    "v136_rhi_11",  # Facial Pain / Headache vs Rhinogenic Disease
    "v136_rhi_12",  # Frontal Recess / Frontal Sinus
    "v136_rhi_13",  # Frontal Sinusotomy / Draf Procedures
    "v136_rhi_14",  # Fungal Ball
    "v136_rhi_15",  # Immunodeficiency-Associated Chronic Rhinosinusitis
}

REUSED_APPLICATION_IDS_V207 = {
    "v142_rhi_02": "Frontal Sinusotomy / Draf Procedures",
}


VIGNETTES_V207 = [
    _q(
        "v207_rhi_pain_app", "Facial Pain / Headache vs Rhinogenic Disease", "application",
        "A patient reports recurrent 'sinus headaches' with throbbing unilateral pressure, photophobia, nausea, and worsening with activity. Nasal endoscopy is normal during symptoms and prior sinus CT is normal. What is the best next step?",
        [
            "Treat the symptom pattern as likely migraine/nonrhinogenic headache and direct evaluation accordingly rather than diagnosing sinus disease from pain location alone",
            "Schedule ESS because maxillary-region pain reliably localizes maxillary sinus inflammation",
            "Give repeated antibiotics whenever the headache occurs",
            "Diagnose chronic rhinosinusitis even without objective inflammation",
        ], 0,
        "Migraine commonly presents with facial pressure and can include nasal autonomic symptoms, which is why patients often label it sinus headache. Objective sinonasal inflammation is required before attributing chronic or recurrent pain to CRS; normal endoscopy and CT plus a migrainous symptom cluster should redirect the diagnostic frame.",
        [
            "Correct. Headache phenotype and the absence of objective sinonasal disease argue for a nonrhinogenic diagnosis rather than surgery.",
            "Pain location is not a reliable map of sinus pathology, and ESS without objective disease has no defined target.",
            "Antibiotics do not treat a recurrent migrainous syndrome and expose the patient to unnecessary medication risk.",
            "CRS requires objective inflammatory evidence in addition to symptoms; pain alone does not establish it.",
        ],
        "The face can hurt where the sinuses live without the sinuses being the cause; objective disease must match the symptom story.",
        "Which autonomic nasal symptoms can occur during migraine and falsely reinforce a patient's belief that the pain is sinus-generated?",
        "boards",
    ),
    _q(
        "v207_rhi_pain_snr", "Facial Pain / Headache vs Rhinogenic Disease", "senior_decision",
        "A patient with migraine also has a small incidental maxillary retention cyst on CT and asks for sinus surgery to cure years of headaches. Endoscopy is normal and there are no infectious or obstructive sinus symptoms. What is the best senior-level counseling principle?",
        [
            "Remove any radiographic sinus abnormality because incidental findings usually cause headache",
            "Explain that the incidental cyst does not establish causality, avoid surgery without a concordant rhinologic target, and continue headache-directed evaluation/treatment",
            "Perform bilateral maxillary antrostomies to prevent future migraine attacks",
            "Prescribe long-term oral decongestants as definitive therapy",
        ], 1,
        "Incidental mucosal changes and retention cysts are common. Senior decision-making requires separating radiographic coincidence from disease that explains the patient's symptoms. Surgery should target a defined obstructive, inflammatory, infectious, or structural mechanism—not an imaging finding that does not fit the clinical syndrome.",
        [
            "An incidental cyst is not proof of a pain generator and does not justify operative morbidity by itself.",
            "Correct. Concordance between symptom phenotype, objective disease, and a surgically correctable mechanism is required before operating for facial pain.",
            "Maxillary surgery does not treat the neurovascular mechanism of migraine when no sinus target is present.",
            "Chronic decongestant exposure is not a definitive treatment for migraine or an incidental retention cyst.",
        ],
        "Do not operate on coincidence: an imaging abnormality must plausibly explain the symptom before it becomes a surgical target.",
        "What rare contact-point or pressure-related scenarios would make a rhinogenic contribution more plausible, and what cautions remain before surgery?",
        "boards",
    ),

    _q(
        "v207_rhi_frontal_app", "Frontal Recess / Frontal Sinus", "application",
        "Coronal and sagittal CT show a frontal drainage pathway narrowed by an agger nasi cell and a large supra-agger frontal cell immediately adjacent to the skull base. What is the best operative planning principle?",
        [
            "Use the cell relationships on multiplanar CT to predict the drainage pathway and remove only the partitions necessary to open it while preserving mucosa",
            "Ignore CT cell anatomy because frontal drainage follows a constant straight vertical tract",
            "Strip all mucosa circumferentially to prevent recurrence",
            "Enter the frontal sinus by drilling blindly through the skull base",
        ], 0,
        "Modern frontal surgery is based on patient-specific cell anatomy rather than a fixed tubular model. Multiplanar CT allows the surgeon to understand which cells push the drainage pathway medially, laterally, anteriorly, or posteriorly and to choose a targeted mucosa-preserving dissection around the orbit and skull base.",
        [
            "Correct. Cell-based CT analysis determines the safe path and the minimum dissection needed to restore drainage.",
            "Frontal recess anatomy is highly variable, and assuming a constant tract is a setup for incomplete surgery or injury.",
            "Circumferential mucosal stripping promotes osteitis and restenosis in an already narrow outflow tract.",
            "Blind superior drilling risks intracranial injury and ignores the available anatomic roadmap.",
        ],
        "Frontal recess surgery is solved on CT before it is solved with an instrument: map the cells that define the drainage pathway.",
        "How does an anterior ethmoid artery hanging below the skull base alter the safe dissection around posterior frontal cells?",
        "OR_prep",
    ),
    _q(
        "v207_rhi_frontal_snr", "Frontal Recess / Frontal Sinus", "senior_decision",
        "During frontal recess surgery, the natural frontal outflow is open but narrow after targeted cell removal. Further drilling would require circumferential denudation near the skull base and orbit. What is the best attending-level principle?",
        [
            "Keep drilling until the opening is maximally large regardless of mucosal injury",
            "Accept a functionally patent mucosa-lined pathway when further enlargement adds more restenosis and complication risk than benefit",
            "Convert automatically to a Draf III in every narrow frontal recess",
            "Pack the frontal recess tightly with permanent material to keep it open",
        ], 1,
        "The goal of frontal surgery is durable drainage, not maximal diameter at any cost. Excessive drilling and mucosal loss can promote scar and neo-osteogenesis, so senior judgment includes stopping when the disease target is corrected and additional enlargement would trade healthy mucosa and safety for little functional gain.",
        [
            "Maximal bony diameter is not synonymous with durable function when the price is circumferential mucosal injury.",
            "Correct. The best endpoint is a safe, patent, maintainable pathway with preserved mucosa whenever possible.",
            "Draf III is an escalation reserved for selected refractory disease/anatomy, not a default response to any narrow recess.",
            "Permanent tight packing can traumatize mucosa and does not substitute for a well-constructed drainage pathway.",
        ],
        "In the frontal recess, bigger is not always better if enlargement destroys the mucosa that must keep the pathway open.",
        "Which postoperative debridement and topical-therapy principles help maintain frontal patency after technically adequate surgery?",
        "OR_prep",
    ),

    _q(
        "v207_rhi_draf_snr", "Frontal Sinusotomy / Draf Procedures", "senior_decision",
        "A patient with prior Draf III has recurrent frontal obstruction from focal neo-osteogenesis and scar, but most of the common frontal neo-ostium remains patent and healthy. What is the best revision principle?",
        [
            "Recreate the entire Draf III from the beginning regardless of the focal failure",
            "Perform an external frontal sinus obliteration automatically after any Draf III restenosis",
            "Target the focal stenotic bone/scar, preserve functioning mucosa and patent portions of the neo-ostium, and address the reason for restenosis rather than indiscriminately enlarging everything",
            "Avoid all postoperative topical therapy because it causes restenosis",
        ], 2,
        "Revision frontal surgery should be mechanism-specific. A focal scar or neo-osteogenic segment can often be addressed selectively while preserving already functional mucosa and drainage. Repeating the maximal operation without identifying the cause of failure may add trauma and create more restenosis.",
        [
            "Removing healthy reconstructed anatomy can increase morbidity without correcting the focal failure mechanism.",
            "External obliteration is not automatically required when an endoscopically correctable focal stenosis remains accessible.",
            "Correct. Revision surgery should preserve what works and repair what failed.",
            "Topical anti-inflammatory therapy and postoperative care are often important for maintaining patency rather than causing the failure.",
        ],
        "A revision Draf is not a reset button; preserve the parts of the neo-ostium that are already doing their job.",
        "How do neo-osteogenesis, exposed drill bone, inflammatory phenotype, and postoperative care each contribute to restenosis risk?",
        "OR_prep",
    ),

    _q(
        "v207_rhi_fungalball_app", "Fungal Ball", "application",
        "An immunocompetent patient has isolated sphenoid sinus opacification with internal calcific hyperdensities and progressive retro-orbital headache. Endoscopy is otherwise unremarkable. What is the best next management principle?",
        [
            "Treat with prolonged systemic amphotericin without obtaining sinus drainage",
            "Perform endoscopic sphenoidotomy with complete removal of noninvasive fungal debris and restoration of drainage while evaluating adjacent neurovascular anatomy",
            "Observe indefinitely because noninvasive fungal disease cannot cause complications",
            "Treat as AFRS with systemic steroids alone",
        ], 1,
        "A sphenoid fungal ball is usually treated surgically by opening the involved sinus, removing the dense fungal concretions, and restoring ventilation. Systemic antifungal therapy is generally unnecessary without tissue invasion, but sphenoid location warrants respect for the optic nerve, carotid artery, and potential visual or cranial-neuropathy symptoms.",
        [
            "Systemic amphotericin is not routine treatment for a noninvasive fungal ball in an immunocompetent patient.",
            "Correct. The treatment is local source removal and drainage, with careful attention to sphenoid neurovascular anatomy.",
            "Sphenoid disease can produce severe headache and threaten adjacent structures, so symptomatic persistent disease should not be ignored simply because it is noninvasive.",
            "AFRS is a diffuse eosinophilic inflammatory phenotype with allergic mucin, not an isolated clay-like fungal concretion.",
        ],
        "Noninvasive does not mean irrelevant: a sphenoid fungal ball sits beside the optic nerve and carotid and is usually a surgical drainage problem.",
        "What visual symptom or cranial neuropathy would make sphenoid fungal disease an urgent rather than elective problem?",
        "OR_prep",
    ),
    _q(
        "v207_rhi_fungalball_snr", "Fungal Ball", "senior_decision",
        "During removal of a presumed sphenoid fungal ball, the mucosa is unexpectedly necrotic and frozen section demonstrates fungal invasion of tissue. What is the best next decision?",
        [
            "Continue treating it as a routine fungal ball because the preoperative CT was noninvasive-appearing",
            "Stop after simple debris removal and await final pathology before changing therapy",
            "Give topical steroid alone because the fungus has already been removed",
            "Escalate immediately to an invasive fungal rhinosinusitis pathway with urgent debridement as appropriate, systemic antifungal therapy, host-factor optimization, and multidisciplinary evaluation of orbital/skull-base extent",
        ], 3,
        "The defining distinction between fungal ball and invasive fungal rhinosinusitis is tissue invasion. Once histology demonstrates invasion, the management category changes immediately: disease extent, systemic antifungal treatment, repeated debridement needs, and reversal of immunosuppression or metabolic risk become time-critical.",
        [
            "A preoperative label cannot override direct histologic evidence of invasion.",
            "Waiting for final pathology can dangerously delay treatment of an angioinvasive process when frozen section is convincing.",
            "Steroids alone can worsen uncontrolled invasive fungal disease and do not address tissue invasion.",
            "Correct. Histologic invasion is the switch that converts a local noninvasive problem into an emergency pathway.",
        ],
        "In fungal sinus disease, pathology can change the operation in real time: tissue invasion is the emergency switch.",
        "Which host factors and orbital or cranial-nerve findings most strongly increase concern for rapidly progressive angioinvasive disease?",
        "overnight_call",
    ),

    _q(
        "v207_rhi_immune_app", "Immunodeficiency-Associated Chronic Rhinosinusitis", "application",
        "A patient has refractory CRS, recurrent bacterial pneumonias, and poor response to standard vaccination. Which initial immune evaluation is most appropriate?",
        [
            "Serum quantitative immunoglobulins with assessment of functional antibody responses, guided further by the infection history",
            "ANA alone because humoral immune disorders are diagnosed by autoantibodies",
            "No laboratory evaluation because CRS cannot reflect systemic immune deficiency",
            "Immediate repeat ESS before evaluating the host",
        ], 0,
        "Recurrent sinopulmonary bacterial infections should prompt evaluation of humoral immunity, including quantitative immunoglobulins and functional antibody responses to vaccines when appropriate. The exact workup expands according to infection pattern and specialist assessment, but host defense should be evaluated before assuming every recurrence is an anatomic surgical failure.",
        [
            "Correct. Quantitative levels plus functional antibody responses address common humoral immune defects that can present with recurrent sinopulmonary infection.",
            "ANA is a marker used in selected autoimmune evaluations and does not establish humoral immune competence.",
            "CRS can be a manifestation of immune deficiency, especially when accompanied by recurrent pneumonia or unusual infections.",
            "Another operation may not succeed if the dominant failure mechanism is untreated systemic immune dysfunction.",
        ],
        "When CRS travels with recurrent pneumonia, evaluate the host—not just the holes in the sinus CT.",
        "How do specific-antibody deficiency and common variable immunodeficiency differ in quantitative immunoglobulin findings and vaccine responses?",
        "boards",
    ),
    _q(
        "v207_rhi_immune_snr", "Immunodeficiency-Associated Chronic Rhinosinusitis", "senior_decision",
        "A patient with CVID has persistent CRS symptoms despite immunology-directed treatment and optimized topical therapy. CT and endoscopy show obstructed sinuses with retained purulence, and cultures repeatedly grow resistant organisms. What is the best senior-level principle?",
        [
            "Immune deficiency makes ESS categorically contraindicated",
            "Coordinate immunologic optimization and culture-informed antimicrobial planning, while considering ESS when persistent obstructed disease has a correctable anatomic/source-control target",
            "Ignore cultures because all postoperative antibiotics should be identical",
            "Stop immunoglobulin replacement before surgery to improve wound healing",
        ], 1,
        "Immune deficiency changes perioperative risk, microbiology, and expectations but does not eliminate the role of surgery when there is persistent obstructed disease that can benefit from drainage and topical access. Best care integrates host optimization, culture data, and a clear surgical target rather than choosing between systemic and local treatment as though only one can matter.",
        [
            "CVID increases complexity and recurrence risk but does not prohibit surgery when anatomy and source control justify it.",
            "Correct. Senior management integrates immune therapy, microbiology, and anatomy into one plan.",
            "Resistant or unusual organisms make culture information more, not less, relevant to antimicrobial planning.",
            "Interrupting indicated immune replacement can worsen infection risk and should not be done reflexively for sinus surgery.",
        ],
        "In immune-deficient CRS, surgery can improve local source control, but durable success depends on treating the host and the sinus together.",
        "What perioperative microbiology or prophylaxis considerations would you discuss with immunology and infectious disease for a patient colonized with resistant organisms?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v207(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed_foundations = 0
    for qid in REVIEWED_FOUNDATION_IDS_V207:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v20.7: reviewed foundation missing from live registry: {qid}")
        if q.get("domain") != DOMAIN:
            raise RuntimeError(f"v20.7: foundation domain mismatch: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed_foundations += 1

    reused_applications = 0
    for qid, topic in REUSED_APPLICATION_IDS_V207.items():
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v20.7: reused application missing from live registry: {qid}")
        if q.get("domain") != DOMAIN or q.get("topic") != topic:
            raise RuntimeError(f"v20.7: reused application mapping mismatch: {qid}")
        q["learning_stage"] = "application"
        q["ladder_reviewed"] = True
        reused_applications += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for source in VIGNETTES_V207:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = id_factory(q["domain"], q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1

    return {
        "reviewed_foundations": reviewed_foundations,
        "reused_applications": reused_applications,
        "added_questions": added,
        "topics": sorted({q["topic"] for q in VIGNETTES_V207}),
    }
