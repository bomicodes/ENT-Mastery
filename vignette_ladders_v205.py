"""v20.5 — deliberate learning-ladder curation, Rhinology pass 1.

Begins systematic review of Rhinology / Allergy / Skull Base with five canonical
v13.6 foundations. Strong foundations are preserved and explicitly staged; new
questions are added only for missing application and senior decision layers.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong,
       pearl, curveball, focus):
    return {
        "id": qid,
        "domain": DOMAIN,
        "topic": topic,
        "learning_stage": stage,
        "stem": stem,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
        "why_wrong": why_wrong,
        "board_pearl": pearl,
        "curveball": curveball,
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "focus": focus,
        "ladder_reviewed": True,
    }


REVIEWED_FOUNDATION_IDS_V205 = {
    "v136_rhi_01",  # AFRS
    "v136_rhi_02",  # Acute Bacterial Rhinosinusitis
    "v136_rhi_03",  # Benign Sinonasal Tumor Framework
    "v136_rhi_04",  # CF / Primary Ciliary Dyskinesia Sinonasal Disease
    "v136_rhi_05",  # CRS Phenotyping
}


VIGNETTES_V205 = [
    _q(
        "v205_rhi_afrs_app", "AFRS", "application",
        "A 23-year-old with asthma and nasal polyps has unilateral-dominant expansile sinus opacification with heterogeneous hyperdensities and smooth bony remodeling. Surgery yields thick eosinophilic mucin with fungal elements, but histology shows no tissue invasion. Which postoperative strategy best matches the disease biology?",
        [
            "Treat as acute invasive fungal rhinosinusitis with indefinite systemic amphotericin",
            "Use ongoing anti-inflammatory therapy, typically topical corticosteroid-based care with close endoscopic surveillance after complete surgical clearance and ventilation",
            "Stop all therapy once fungal elements are seen because surgery is contraindicated",
            "Use antibiotics alone because fungal elements prove bacterial superinfection",
        ], 1,
        "AFRS is a noninvasive, highly inflammatory form of chronic rhinosinusitis. Surgery removes obstructing allergic mucin and restores access for topical therapy, but recurrence prevention depends on postoperative inflammatory control and surveillance rather than treating the patient as though fungi have invaded tissue.",
        [
            "Systemic antifungal therapy for angioinvasive disease is not justified when the host, histology, and operative findings show noninvasive AFRS.",
            "Correct. The long-term problem is recurrent type-2/eosinophilic inflammation after surgical clearance, so topical anti-inflammatory access and follow-up matter.",
            "Fungal elements in allergic mucin do not make surgery contraindicated; clearance is often central to restoring sinus ventilation and topical access.",
            "Antibiotics do not address the eosinophilic inflammatory mechanism that defines AFRS.",
        ],
        "In fungal sinus disease, tissue invasion—not the mere presence of fungal hyphae—changes the emergency and antifungal treatment pathway.",
        "What operative or histopathologic finding would make you abandon the AFRS framework and treat for invasive fungal disease?",
        "boards",
    ),
    _q(
        "v205_rhi_afrs_snr", "AFRS", "senior_decision",
        "A patient with recurrent AFRS has marked orbital displacement and skull-base thinning from expansile disease, but MRI and pathology show no orbital, dural, or vascular tissue invasion. What is the best attending-level principle?",
        [
            "Treat the bony erosion itself as proof of invasive fungal infection",
            "Avoid surgery because skull-base thinning makes all endoscopic treatment unsafe",
            "Plan careful complete endoscopic clearance around the remodeled orbit/skull base, preserve critical mucosa when feasible, and establish intensive postoperative anti-inflammatory surveillance rather than assuming erosion equals invasion",
            "Perform orbital exenteration because the orbit is displaced",
        ], 2,
        "AFRS can cause dramatic pressure remodeling and bony erosion without tissue invasion. The operative challenge is safe clearance from distorted skull-base and orbital anatomy while maintaining a durable cavity for topical therapy. The imaging and histologic distinction from invasive fungal disease prevents unnecessary radical treatment.",
        [
            "Pressure remodeling and erosion can occur in noninvasive AFRS and do not independently establish angioinvasion.",
            "Complex anatomy increases the need for deliberate image-guided planning; it does not make disease clearance categorically inappropriate.",
            "Correct. Senior judgment separates dramatic noninvasive remodeling from true tissue invasion and plans surgery around the altered anatomy.",
            "Orbital displacement without invasive orbital disease is not an indication for exenteration.",
        ],
        "AFRS may look radiographically aggressive while remaining histologically noninvasive; do not equate bone loss with angioinvasion.",
        "How would a focal skull-base defect with CSF leak change reconstruction planning during clearance?",
        "OR_prep",
    ),

    _q(
        "v205_rhi_abrs_app", "Acute Bacterial Rhinosinusitis", "application",
        "A healthy adult develops a viral upper respiratory illness, improves for several days, then develops new fever, purulent nasal drainage, and worsening unilateral facial pressure on day 8. There are no orbital or neurologic findings. Which interpretation is best?",
        [
            "The double-worsening pattern supports acute bacterial rhinosinusitis even though symptoms have not persisted continuously for 10 days",
            "This remains uncomplicated viral rhinosinusitis because bacterial disease cannot occur before day 10",
            "The patient has chronic rhinosinusitis because symptoms recurred",
            "Contrast MRI is mandatory before any treatment discussion",
        ], 0,
        "ABRS can be diagnosed by persistent symptoms without improvement or by a double-worsening pattern after initial viral improvement. The 10-day threshold is not the only qualifying pattern; uncomplicated cases without orbital, neurologic, or other complication signs generally do not need routine imaging.",
        [
            "Correct. Double worsening is a key clinical discriminator for bacterial conversion after an initially improving viral illness.",
            "Waiting for day 10 despite a convincing double-worsening syndrome misapplies the persistence criterion.",
            "CRS requires a much longer symptom duration with objective inflammation rather than a second phase of an acute illness.",
            "Routine advanced imaging is unnecessary in uncomplicated ABRS without complication or alternative-diagnosis red flags.",
        ],
        "For ABRS, know both pathways: persistent symptoms without improvement and double worsening after initial improvement.",
        "Which host factors or severity findings would lower your threshold for immediate antibiotics rather than watchful waiting?",
        "boards",
    ),
    _q(
        "v205_rhi_abrs_snr", "Acute Bacterial Rhinosinusitis", "senior_decision",
        "A patient being treated for presumed ABRS develops progressive periorbital edema, painful restricted extraocular movements, decreased visual acuity, and fever. What is the safest next decision?",
        [
            "Change to a different oral antibiotic and arrange routine clinic follow-up",
            "Continue observation because orbital symptoms are expected during maxillary sinusitis",
            "Give systemic steroids alone before obtaining further evaluation",
            "Treat this as a possible orbital complication with urgent contrast imaging, IV antimicrobial therapy, serial ophthalmologic assessment, and prompt ENT/ophthalmology source-control planning",
        ], 3,
        "Visual change, ophthalmoplegia, proptosis, or progressive orbital findings move the patient out of uncomplicated ABRS. Evaluation and treatment should proceed urgently because subperiosteal/orbital abscess and other complications can threaten vision and spread intracranially.",
        [
            "Oral outpatient escalation is inadequate when vision-threatening orbital extension is suspected.",
            "Painful restricted eye movement and decreased acuity are complication signs, not routine manifestations of uncomplicated sinusitis.",
            "Steroids do not provide infection source control and should not delay imaging and antimicrobial treatment of a possible abscess.",
            "Correct. The management category has changed from routine ABRS to a vision-threatening complicated infection requiring imaging, IV therapy, and multidisciplinary escalation.",
        ],
        "In sinusitis, a deteriorating eye is an emergency even when the original illness began as routine ABRS.",
        "Which CT and serial examination findings would push you from medical therapy to urgent orbital and sinus drainage?",
        "overnight_call",
    ),

    _q(
        "v205_rhi_benign_app", "Benign Sinonasal Tumor Framework", "application",
        "A patient has a unilateral slowly enlarging nasal mass. MRI shows avid enhancement and prominent feeding vessels near the posterior nasal cavity, but there is no destructive invasion. What is the safest next diagnostic principle?",
        [
            "Perform an immediate blind office biopsy because benign-appearing masses cannot bleed significantly",
            "Define vascularity, attachment, and skull-base/orbital relationships before deciding whether and where biopsy can be performed safely",
            "Treat empirically with antibiotics until the mass disappears",
            "Assume bilateral inflammatory polyposis despite the unilateral vascular appearance",
        ], 1,
        "A benign imaging tempo does not make a sinonasal mass safe to biopsy blindly. Hypervascular lesions require anatomic and vascular characterization first because the differential includes entities in which office biopsy can produce severe hemorrhage; tissue diagnosis should be obtained by a route appropriate to the lesion's risk profile.",
        [
            "Vascularity, not just malignant potential, determines biopsy safety in a sinonasal mass.",
            "Correct. Image-defined origin and vascular relationships should precede instrumentation when bleeding or skull-base risk is plausible.",
            "A persistent structural mass should not be managed as infection without evidence supporting that mechanism.",
            "Unilateral focal vascular disease is not the typical phenotype of diffuse inflammatory polyposis.",
        ],
        "For a unilateral sinonasal mass, first ask where it arises and how vascular it is; biopsy comes after those questions when risk is nontrivial.",
        "What demographic and imaging pattern would make juvenile nasopharyngeal angiofibroma sufficiently likely that office biopsy should be avoided entirely?",
        "boards",
    ),
    _q(
        "v205_rhi_benign_snr", "Benign Sinonasal Tumor Framework", "senior_decision",
        "A small incidentally discovered frontal sinus osteoma is not obstructing the frontal outflow tract, has shown no growth on interval imaging, and causes no symptoms. What is the best management principle?",
        [
            "Observe with appropriately selected follow-up rather than operating solely because a benign tumor is present",
            "Perform an immediate Draf III for every frontal sinus osteoma",
            "Obtain chemotherapy because all sinonasal bone tumors are premalignant",
            "Biopsy through the skull base to prove the diagnosis despite classic imaging",
        ], 0,
        "Benign sinonasal tumors are managed according to biology, symptoms, growth, location, and threat to critical drainage or neurovascular structures. An asymptomatic stable osteoma that does not compromise the frontal outflow tract can often be observed, whereas growth, obstruction, mucocele formation, orbital effects, or symptoms can justify surgery.",
        [
            "Correct. Senior management avoids morbidity when the natural history and anatomy support surveillance.",
            "The extent of frontal surgery should be driven by lesion location and access needs, not by the diagnostic label alone.",
            "A classic benign osteoma has no routine indication for systemic chemotherapy.",
            "An unnecessary hazardous biopsy is not justified when imaging is characteristic and management would remain observation.",
        ],
        "Benign does not mean 'must remove'; the decision is whether the lesion threatens function, grows, causes symptoms, or creates future access problems.",
        "Which frontal recess, orbital, or posterior-table relationships would make prophylactic resection more reasonable?",
        "OR_prep",
    ),

    _q(
        "v205_rhi_mucociliary_app", "CF / Primary Ciliary Dyskinesia Sinonasal Disease", "application",
        "A teenager has lifelong nasal congestion, pansinusitis, chronic wet cough, recurrent otitis, bronchiectasis, and situs inversus. Which underlying disorder should rise highest on the differential?",
        [
            "Isolated allergic rhinitis",
            "Cystic fibrosis based on situs inversus alone",
            "Primary ciliary dyskinesia with impaired mucociliary clearance",
            "Acute bacterial rhinosinusitis",
        ], 2,
        "The combination of lifelong upper- and lower-airway disease, chronic wet cough, bronchiectasis, recurrent middle-ear disease, and laterality abnormality strongly supports primary ciliary dyskinesia. CF can also produce severe chronic sinonasal and pulmonary disease, but situs abnormalities are particularly characteristic of motile-cilia dysfunction.",
        [
            "Allergic rhinitis does not explain lifelong suppurative lower-airway disease, bronchiectasis, and laterality abnormality.",
            "CF remains an important alternative in chronic sinopulmonary disease, but situs inversus specifically points toward a motile-cilia disorder rather than diagnosing CF.",
            "Correct. PCD is a multisystem mucociliary disorder, so the sinonasal phenotype should be interpreted together with pulmonary, otologic, and laterality findings.",
            "An acute sinus episode cannot account for the lifelong multisystem pattern.",
        ],
        "Lifelong wet cough plus bronchiectasis and situs abnormality is a mucociliary-disease pattern, not just difficult sinusitis.",
        "What testing pathway helps confirm PCD, and why can no single screening test establish every case?",
        "boards",
    ),
    _q(
        "v205_rhi_mucociliary_snr", "CF / Primary Ciliary Dyskinesia Sinonasal Disease", "senior_decision",
        "A patient with confirmed cystic fibrosis has severe recurrent sinonasal polyposis and obstruction despite optimized medical therapy and coordinated pulmonary care. The family asks whether sinus surgery will cure the underlying disease. What is the best counseling principle?",
        [
            "ESS permanently corrects the CFTR defect and eliminates the need for pulmonary or medical therapy",
            "Sinus surgery is contraindicated in cystic fibrosis because recurrence is inevitable",
            "Repeated antibiotics alone should replace surgery regardless of obstruction or quality-of-life burden",
            "ESS can improve drainage, symptoms, and topical-treatment access in selected patients, but recurrence risk remains high because surgery does not correct the systemic mucociliary disorder",
        ], 3,
        "Surgery in CF or PCD is an adjunct to disease-specific medical and pulmonary management. It can improve sinonasal access and symptom burden when appropriately selected, but the abnormal mucociliary environment persists, so expectations, long-term topical care, and multidisciplinary follow-up are essential.",
        [
            "ESS changes anatomy and drainage but cannot repair the underlying CFTR-mediated systemic disease.",
            "High recurrence risk changes expectations and follow-up; it does not make surgery categorically inappropriate when symptoms and obstruction justify it.",
            "Medical therapy remains important, but persistent structural disease and access limitations can still make surgery useful.",
            "Correct. Senior counseling distinguishes achievable local control from cure of the systemic disease mechanism.",
        ],
        "In mucociliary disorders, surgery can improve the plumbing but cannot normalize the cilia or ion transport driving recurrence.",
        "How would lung-transplant status or unusual airway colonization change perioperative culture and antimicrobial planning?",
        "OR_prep",
    ),

    _q(
        "v205_rhi_crsphen_app", "CRS Phenotyping", "application",
        "Three patients meet symptom and objective criteria for CRS: one has unilateral maxillary disease adjacent to a diseased molar, one has bilateral eosinophilic polyps with asthma, and one has recurrent pneumonias with low immunoglobulins. What is the most important next principle?",
        [
            "Apply the same antibiotic and surgical pathway to all three because objective CRS is already proven",
            "Treat phenotype as a coding detail only after surgery",
            "Identify and address the dominant driver—odontogenic source, type-2 inflammatory disease, or immune deficiency—because it changes treatment and recurrence risk",
            "Avoid further evaluation because CT inflammation identifies the cause",
        ], 2,
        "CRS is a syndrome with multiple primary and secondary drivers. Objective inflammation establishes disease but does not explain why it is present. Odontogenic infection requires dental source control, type-2 polyp disease may change anti-inflammatory/biologic strategy, and immunodeficiency requires host evaluation and treatment.",
        [
            "Identical treatment ignores mechanisms that require fundamentally different source control or systemic therapy.",
            "Phenotype and underlying driver affect the treatment plan before, not merely after, an operation.",
            "Correct. The purpose of phenotyping is to make the management pathway mechanism-specific rather than simply label-specific.",
            "CT demonstrates inflammation and anatomy but cannot by itself establish the causal endotype or systemic driver.",
        ],
        "A CRS diagnosis tells you that chronic inflammation exists; phenotyping tells you why your first-line plan may need to differ.",
        "Which unilateral, systemic, or early-onset features should trigger a secondary-CRS workup rather than routine empiric escalation?",
        "boards",
    ),
    _q(
        "v205_rhi_crsphen_snr", "CRS Phenotyping", "senior_decision",
        "A patient has severe recurrent CRS after technically adequate prior ESS. Endoscopy shows widely patent sinuses but persistent eosinophilic edema and polyposis; the patient also has asthma and repeated systemic-steroid bursts. What is the best senior-level next step?",
        [
            "Repeat the same surgery solely because symptoms recurred despite already patent cavities",
            "Reassess inflammatory phenotype, adherence and comorbid type-2 disease, then select escalation such as optimized topical therapy and biologic or other phenotype-directed treatment rather than assuming another operation fixes the mechanism",
            "Use indefinite broad-spectrum antibiotics because any postoperative inflammation is bacterial",
            "Close the sinus openings surgically to reduce allergen exposure",
        ], 1,
        "When technically adequate sinus surgery has already created access and drainage, recurrence can be driven primarily by uncontrolled inflammatory endotype rather than residual anatomy. Senior management asks why treatment failed and directs the next intervention at that mechanism instead of reflexively repeating a technically successful operation.",
        [
            "A repeat operation without an anatomic failure target is unlikely to correct a predominantly inflammatory recurrence mechanism.",
            "Correct. Phenotype-directed escalation is the point of distinguishing persistent type-2 disease from mechanical surgical failure.",
            "Eosinophilic recurrent polyposis with asthma is not evidence that chronic bacterial infection is the sole driver.",
            "Obliterating drainage reverses the goals of sinus surgery and impairs topical access.",
        ],
        "Revision surgery should fix a defined anatomic failure; persistent inflammation in an already open cavity may require a different treatment axis.",
        "What findings would instead prove a correctable surgical failure such as frontal stenosis, retained partitions, or maxillary recirculation?",
        "boards",
    ),
]


def apply_learning_ladders_v205(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V205:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v20.5: reviewed foundation missing from live registry: {qid}")
        if q.get("domain") != DOMAIN:
            raise RuntimeError(f"v20.5: foundation domain mismatch: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for source in VIGNETTES_V205:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = id_factory(q["domain"], q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1

    return {
        "reviewed_foundations": reviewed,
        "added_questions": added,
        "topics": sorted({q["topic"] for q in VIGNETTES_V205}),
    }
