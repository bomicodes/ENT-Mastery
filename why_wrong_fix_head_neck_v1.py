"""
why_wrong_fix_head_neck_v1.py

Replaces the generic/duplicate `why_wrong` text for the 30 Head & Neck
Oncology items flagged by audit_question_quality.py (GENERIC_WHY_WRONG).
Each wrong choice gets its own specific clinical reasoning. The correct
choice's own slot is "Correct." to match schema.

Usage: same pattern as why_wrong_fix_general_ent_v1.py.

    from why_wrong_fix_head_neck_v1 import apply_why_wrong_fix_head_neck_v1
    WHY_WRONG_FIX_HEAD_NECK_V1 = apply_why_wrong_fix_head_neck_v1(runtime_entry.data)
"""

WHY_WRONG_FIXES = {
    "v140_hn_01": [
        "Correct.",
        "Venous congestion classically presents with a flap that is swollen, "
        "dusky/blue, and bleeds briskly with dark blood on pinprick; the pale, cool "
        "flap with absent bleeding described here points to inflow (arterial) failure, "
        "not venous outflow obstruction.",
        "Normal postoperative edema would not produce pallor, coolness, and an absent "
        "Doppler signal; these findings indicate a genuine perfusion problem, not benign "
        "swelling.",
        "A chyle leak produces milky lymphatic drainage from the wound bed, not flap "
        "pallor, coolness, or loss of Doppler signal; it does not explain this vascular "
        "examination.",
    ],
    "v140_hn_02": [
        "Correct.",
        "Otitis externa is an external ear canal infection with no anatomic connection "
        "to a neck wound or pharyngeal reconstruction after laryngectomy.",
        "BPPV is a vestibular disorder causing positional vertigo; it has no "
        "relationship to salivary drainage or neck wound findings.",
        "A parotid fistula would drain saliva from the parotid gland region, typically "
        "after parotid surgery; it does not explain salivary leakage from a neck drain "
        "following pharyngeal closure after laryngectomy, which is the classic "
        "presentation of pharyngocutaneous fistula.",
    ],
    "v140_hn_03": [
        "An uncontrolled thoracic duct injury produces a high-output chyle leak that "
        "drains will not resolve on their own; the leak needs active intraoperative "
        "control (clipping/ligation) to prevent major postoperative morbidity.",
        "The vagus nerve has no role in lymphatic drainage and is not implicated in a "
        "thoracic duct injury; sacrificing it would cause an unrelated, unnecessary, and "
        "serious complication (vocal-fold paralysis) without addressing the leak.",
        "Correct.",
        "Bone wax is used to control bleeding from bone surfaces; it does not seal a "
        "lymphatic duct injury and would not reliably stop chyle leakage.",
    ],
    "v140_hn_04": [
        "Anatomic presence of the larynx does not equal functional preservation "
        "potential; gross cartilage invasion and a poorly functional, aspirating larynx "
        "predict a low chance that chemoradiation will yield a useful, functioning "
        "organ, favoring surgery instead.",
        "A T4a tumor with cartilage invasion is an advanced, life-threatening cancer; "
        "observation without definitive treatment would allow progression and is not an "
        "appropriate option.",
        "Correct.",
        "Endoscopic excision alone is suited to limited, early-stage disease; it cannot "
        "adequately address a T4a tumor with cartilage invasion and extralaryngeal "
        "extension into strap muscles.",
    ],
    "v140_hn_05": [
        "Correct.",
        "The true vocal folds have sparse, largely unilateral lymphatic drainage, which "
        "is exactly why early glottic cancer has a much lower nodal risk than "
        "supraglottic cancer -- this statement describes the opposite of glottic "
        "lymphatic behavior.",
        "Not all laryngeal tumors require radical neck dissection; treatment is tailored "
        "to primary site, stage, and nodal risk, and radical neck dissection specifically "
        "is reserved for extensive nodal disease.",
        "Elective neck treatment addresses lymphatic spread of cancer, not swallowing "
        "function; it has no role in preventing aspiration.",
    ],
    "v140_hn_06": [
        "Primary tumor size (T stage) alone does not capture nodal risk in oral cavity "
        "cancer; depth of invasion is an independent predictor of occult metastasis, so "
        "even a small-diameter tumor with substantial depth (9 mm here) carries "
        "meaningful nodal risk.",
        "Correct.",
        "This is an oral tongue (oral cavity) cancer, not an oropharyngeal cancer, and "
        "HPV/p16 staging paradigms apply specifically to oropharyngeal SCC, not oral "
        "cavity SCC; treating it under that framework would misapply staging and "
        "management principles.",
        "Radioactive iodine is used for thyroid tissue/differentiated thyroid cancer; it "
        "has no role in squamous cell carcinoma of the oral tongue.",
    ],
    "v140_hn_07": [
        "Positive margins and extranodal extension are classic high-risk pathologic "
        "features associated with high locoregional recurrence risk; observation alone "
        "would leave this risk unaddressed in a patient fit enough for further "
        "treatment.",
        "This statement is categorically false -- postoperative radiation, and "
        "specifically concurrent chemoradiation with positive margins or extranodal "
        "extension, is a well-established, evidence-based adjuvant strategy that "
        "improves outcomes.",
        "Radioactive iodine treats thyroid tissue and differentiated thyroid cancer; it "
        "has no role in squamous cell carcinoma of the oral cavity.",
        "Correct.",
    ],
    "v140_hn_08": [
        "A thin skin graft provides minimal bulk and no independent blood supply; it "
        "does not protect an exposed, irradiated carotid from ongoing salivary "
        "contamination or mechanical injury, leaving blowout risk essentially "
        "unchanged.",
        "Correct.",
        "Packing infected material against the vessel perpetuates the very "
        "infectious/inflammatory process that erodes the vessel wall, increasing rather "
        "than decreasing blowout risk.",
        "An exposed carotid artery in an infected, irradiated field is a recognized "
        "precursor to catastrophic hemorrhage; declining any reconstruction leaves the "
        "vessel unprotected against exactly the risk factors described.",
    ],
    "v140_hn_09": [
        "Avoiding surgery as an absolute rule ignores that further surgery "
        "(aspiration-prevention procedures) may be exactly what improves this patient's "
        "pulmonary health and quality of life when the larynx cannot protect the "
        "airway.",
        "Correct.",
        "Voice quality is only one component of laryngeal function; a patient who "
        "aspirates recurrently and needs a feeding tube has failed the more fundamental "
        "goal of airway protection and safe swallowing, regardless of voice.",
        "An intact-appearing larynx on imaging does not equal functional preservation; "
        "imaging cannot capture whether the organ is actually protecting the airway and "
        "allowing safe oral intake, which is the true measure of success here.",
    ],
    "v140_hn_10": [
        "The mandible is preserved in this scenario, so there is no bony defect "
        "requiring bone reconstruction; the missing structure is soft tissue (tongue "
        "volume), which bone alone cannot replace.",
        "A thin skin graft lacks the bulk needed to fill a large tongue-volume defect or "
        "assist with bolus propulsion and oral containment; it would leave the patient "
        "without adequate structure for functional swallowing.",
        "Leaving a large glossectomy defect unreconstructed would result in an open oral "
        "cavity/pharyngeal communication, severe functional impairment, and poor "
        "healing; reconstruction is necessary to restore form and function.",
        "Correct.",
    ],
    "v145_hn_01": [
        "Infiltrative BCC with poorly defined margins on a critical site like the nasal "
        "ala can cause significant local tissue destruction and cosmetic/functional "
        "morbidity if left untreated; BCC is not universally indolent, especially with "
        "aggressive histologic subtypes.",
        "Correct.",
        "BCC metastasizes to regional nodes only rarely; elective neck dissection is not "
        "a standard or appropriate component of routine BCC management.",
        "Chemoradiation is not standard first-line therapy for BCC; most BCC, including "
        "high-risk lesions, is managed surgically with margin control, reserving "
        "radiation for select cases where surgery is not feasible.",
    ],
    "v145_hn_03": [
        "Correct.",
        "Carotid body tumors are highly vascular; blind biopsy risks significant "
        "hemorrhage and is generally avoided since the diagnosis can be made from "
        "characteristic imaging findings alone.",
        "Radical neck dissection is a cancer-nodal-clearance operation; it is not the "
        "appropriate approach to a paraganglioma, which requires a specific "
        "vascular-surgical strategy tailored to its splaying of the carotid vessels, not "
        "lymphadenectomy.",
        "This is a vascular tumor, not an infectious process; antibiotics have no role "
        "in its management.",
    ],
    "v145_hn_04": [
        "Hypoglossal nerve injury causes tongue weakness and deviation toward the "
        "affected side on protrusion, not shoulder droop or impaired arm abduction.",
        "Correct.",
        "Lingual nerve injury causes tongue sensory/taste disturbance, not shoulder or "
        "arm dysfunction; it has no relationship to trapezius function.",
        "Recurrent laryngeal nerve injury causes vocal-fold paralysis with voice and "
        "airway symptoms, not shoulder droop; it does not innervate the trapezius.",
    ],
    "v145_hn_06": [
        "Second primary and recurrence risk persists well beyond two years, especially "
        "with continued tobacco use; stopping surveillance at an arbitrary time point "
        "ignores ongoing risk.",
        "Correct.",
        "Monthly PET/CT is far more frequent than any evidence-based surveillance "
        "protocol, exposes the patient to unnecessary radiation and cost, and is not "
        "supported by guidelines.",
        "Continued tobacco/alcohol exposure raises risk for second primary malignancies "
        "throughout the aerodigestive tract, not just at the original laryngeal subsite; "
        "surveillance must consider the whole field at risk.",
    ],
    "v145_hn_07": [
        "This patient has multiple distinct toxicities (dysphagia, xerostomia, dental "
        "decay, hypothyroidism); treating only the thyroid ignores the swallowing, "
        "dental, and salivary problems that also need active, targeted management.",
        "Many late radiation toxicities -- dysphagia, xerostomia, dental disease, and "
        "hypothyroidism among them -- have effective interventions (swallowing therapy, "
        "dental prevention protocols, saliva substitutes, thyroid hormone replacement); "
        "assuming they cannot be treated leads to unnecessary, preventable morbidity.",
        "Correct.",
        "Speech-language pathology plays a central role in evaluating and treating "
        "radiation-associated dysphagia; avoiding it would remove one of the most "
        "effective tools for this patient's swallowing problem.",
    ],
    "v145_hn_09": [
        "Merkel cell carcinoma is an aggressive malignant neuroendocrine tumor with "
        "substantial risk of nodal and distant spread, particularly in an "
        "immunosuppressed patient; treating it like a benign cyst dramatically "
        "understates its biologic behavior and risk.",
        "Correct.",
        "Given the meaningful nodal metastatic risk of Merkel cell carcinoma, regional "
        "nodal evaluation (such as sentinel node biopsy) is a standard and important "
        "part of staging, not something that should be skipped.",
        "Mere observation after biopsy leaves this aggressive cancer untreated; wide "
        "local control and consideration of nodal staging and adjuvant therapy are "
        "needed given its metastatic potential.",
    ],
    "v145_hn_10": [
        "Correct.",
        "Radical neck dissection is a therapeutic cancer operation for squamous cell "
        "carcinoma nodal disease, not a diagnostic procedure; it would not provide the "
        "intact tissue architecture needed to classify lymphoma and would be an "
        "inappropriately aggressive operation before a diagnosis is even established.",
        "Treating with radiation before establishing a tissue diagnosis risks treating "
        "the wrong disease entirely and precludes accurate lymphoma subtyping, which is "
        "essential for choosing the correct systemic therapy.",
        "Progressive adenopathy with B symptoms and nondiagnostic FNA suggests "
        "malignancy, not an infectious process; indefinite antibiotics would delay the "
        "tissue diagnosis this presentation actually requires.",
    ],
    "v145_hn_11": [
        "Correct.",
        "A larynx that requires a feeding tube and causes repeated aspiration pneumonia "
        "despite maximal therapy is not functioning successfully, regardless of "
        "oncologic control; labeling this \"successful organ preservation\" without "
        "reassessing function ignores the patient's actual quality of life and safety.",
        "Recurrent aspiration pneumonia reflects an anatomic/functional swallowing "
        "problem, not simply an infection to be suppressed; antibiotics alone do not "
        "address the underlying mechanism causing repeated aspiration.",
        "Oncologic control does not guarantee functional safety; ignoring ongoing "
        "life-threatening aspiration because the cancer itself is controlled overlooks a "
        "serious, potentially fatal ongoing problem.",
    ],
    "v145_hn_12": [
        "There is no age cutoff that determines candidacy for conservation laryngeal "
        "surgery; what matters is tumor extent, pulmonary reserve, and the patient's "
        "ability to tolerate the functional recovery process, not a specific age "
        "threshold.",
        "Correct.",
        "Conservation laryngeal surgery inherently requires postoperative swallowing "
        "rehabilitation and tolerance of a temporary recovery period; a patient "
        "unwilling to participate in any rehabilitation is a poor candidate, not an "
        "ideal one, for this approach.",
        "Allergic rhinitis is an unrelated nasal/sinus condition with no bearing on "
        "laryngeal cancer extent, pulmonary reserve, or candidacy for conservation "
        "surgery.",
    ],
    "v145_hn_13": [
        "Continuing tumor-directed therapy without regard to symptom burden or patient "
        "goals can prolong suffering without meaningful benefit in a patient with poor "
        "performance status and incurable disease; treatment intensity should match "
        "expected benefit and the patient's own priorities.",
        "Avoiding prognosis discussion denies the patient the information needed to make "
        "informed decisions about their remaining time and care preferences, which runs "
        "counter to good goals-of-care practice.",
        "Feeding tube placement is not automatically mandatory; it is one option among "
        "several that should be discussed in the context of the patient's goals, "
        "prognosis, and quality-of-life priorities, not a default requirement.",
        "Correct.",
    ],
    "v145_hn_14": [
        "Defaulting to the most invasive option ignores this patient's explicitly stated "
        "preference to avoid procedural burden and ICU-level care; the plan should match "
        "the patient's own stated goals, not maximize intervention.",
        "While family input matters, the patient's own stated preferences should drive "
        "decision-making when the patient can express them; family preference alone, if "
        "it overrides the patient's wishes, is not the appropriate primary driver.",
        "Tracheostomy is not automatically indicated simply because obstruction exists; "
        "in a terminal patient who prioritizes avoiding invasive procedures, the airway "
        "plan must weigh expected symptom benefit against procedural and hospitalization "
        "burden rather than being applied reflexively.",
        "Correct.",
    ],
    "v145_hn_15": [
        "Correct.",
        "Mild dysplasia at an unrelated, remote site is not one of the recognized "
        "high-risk pathologic features (like positive margins or extranodal extension) "
        "that drive the decision to add concurrent systemic therapy to postoperative "
        "radiation.",
        "A normal chest x-ray is a reassuring but unrelated finding regarding distant "
        "metastatic disease; it does not influence the decision about adding concurrent "
        "chemotherapy based on the primary/nodal pathology.",
        "Seasonal allergies are an unrelated, benign condition with no bearing on "
        "postoperative radiation or systemic therapy decisions.",
    ],
    "v145_hn_16": [
        "Correct.",
        "Systemic therapy selection in recurrent/metastatic HNSCC is individualized "
        "based on biomarkers (like PD-L1), prior treatment, and clinical urgency; using "
        "the same regimen for every patient ignores these clinically meaningful "
        "differences.",
        "Chronologic age alone does not capture a patient's actual fitness, symptom "
        "burden, or biomarker status, all of which more directly inform systemic therapy "
        "choice.",
        "Primary tumor subsite does not by itself determine appropriate systemic therapy "
        "in the recurrent/metastatic setting; factors like biomarker status, prior "
        "treatment, and disease tempo are the more relevant drivers.",
    ],
    "v145_hn_17": [
        "Pathology review (margin assessment, histologic subtype) is essential to "
        "oncologic resection and would never be something to omit based on preference; "
        "it is a necessary part of appropriately treating a malignancy.",
        "Middle turbinate size is an incidental anatomic variant unrelated to whether an "
        "oncologically adequate margin can be achieved or whether the tumor threatens "
        "the skull base, orbit, or vasculature.",
        "Correct.",
        "Allergy testing evaluates for allergic disease and has no bearing on tumor "
        "resectability, margin control, or proximity to critical structures in sinonasal "
        "malignancy.",
    ],
    "v145_hn_18": [
        "Correct.",
        "This is factually incorrect -- concurrent chemoradiation has well-established "
        "evidence for improving locoregional control and is standard practice when the "
        "patient can tolerate it; the issue here is patient-specific toxicity risk, not "
        "a lack of overall efficacy.",
        "HPV-positive oropharyngeal cancer patients can still be candidates for "
        "concurrent systemic therapy depending on staging and risk factors; HPV status "
        "does not categorically eliminate the role of systemic therapy.",
        "Concurrent chemoradiation is a well-established, standard treatment strategy; "
        "it is not physically or clinically impossible to combine radiation and "
        "chemotherapy -- the actual issue is whether a specific patient can tolerate "
        "cisplatin specifically.",
    ],
    "v145_hn_19": [
        "Whispering does not use pulmonary air to generate voiced sound and produces "
        "very limited, effortful communication; it is not a fluent, pulmonary-powered "
        "speech rehabilitation method.",
        "A cochlear implant restores hearing input for sensorineural hearing loss; it "
        "has no role in voice production after laryngectomy and does not address "
        "alaryngeal speech.",
        "A palatal obturator addresses velopharyngeal insufficiency or palatal defects; "
        "it is unrelated to voice generation after laryngectomy and does not create a "
        "sound source.",
        "Correct.",
    ],
    "v145_hn_20": [
        "Tumor color has no established role in staging, prognosis, or the decision "
        "between surgical and radiation-based treatment strategies for oropharyngeal "
        "cancer.",
        "A remote history of tonsillitis is an incidental past infectious history "
        "unrelated to current tumor biology, staging, or the choice between TORS and "
        "radiation-based treatment.",
        "Treatment selection should be based on objective factors like expected "
        "morbidity and likelihood of needing adjuvant therapy, discussed with the "
        "patient -- surgeon preference alone, without weighing these outcome-relevant "
        "factors, is not an appropriate sole basis for this decision.",
        "Correct.",
    ],
    "v145_hn_21": [
        "Hair color is an irrelevant physical characteristic with no bearing on tumor "
        "resectability or airway reconstruction feasibility.",
        "Allergic rhinitis is an unrelated nasal/sinus condition and has no effect on "
        "tracheal tumor extent or the feasibility of a tension-safe anastomosis.",
        "Correct.",
        "Chest x-ray visibility does not determine surgical resectability; "
        "cross-sectional imaging and direct assessment of tumor length, location, and "
        "margins relative to anastomotic tension actually determine whether segmental "
        "resection is feasible, not plain radiograph appearance.",
    ],
    "v145_hn_22": [
        "Vaporizing tumor without preserving orientation destroys the ability to assess "
        "margins pathologically, undermining the oncologic control that depends on "
        "knowing whether resection margins are clear.",
        "Accurate staging remains essential before and regardless of surgical approach; "
        "choosing TLM does not eliminate the need to know the extent of disease, which "
        "guides both the surgical plan and any adjuvant treatment decisions.",
        "Correct.",
        "Not every glottic cancer requires open laryngectomy; selected early lesions are "
        "well suited to transoral laser microsurgery, which can achieve oncologic "
        "control while preserving more laryngeal tissue and function than an open total "
        "laryngectomy.",
    ],
    "v145_hn_23": [
        "Correct.",
        "Tumor response on imaging does not mean the new symptoms are benign; "
        "immune-related adverse events like hepatitis and colitis can be serious or "
        "life-threatening and require prompt evaluation and management regardless of how "
        "well the tumor itself is responding.",
        "New diarrhea, hepatitis, and fatigue in a patient on checkpoint inhibitor "
        "therapy should first raise suspicion for immune-related toxicity, since these "
        "agents are well known to cause autoimmune-type organ inflammation; assuming "
        "infection without considering this possibility could delay appropriate "
        "immunosuppressive treatment.",
        "Significant immune-related adverse events often require holding therapy and "
        "initiating immunosuppression (such as corticosteroids); continuing therapy "
        "unchanged in every case ignores the need for severity-based, individualized "
        "management.",
    ],
}


def apply_why_wrong_fix_head_neck_v1(data_module):
    """Overwrite why_wrong for the fixed ids. Returns count actually updated."""
    byid = {q.get("id"): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")}
    updated = 0
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        if len(new_why_wrong) != len(q.get("choices") or []):
            raise ValueError(
                f"{qid}: fix has {len(new_why_wrong)} entries but question has "
                f"{len(q.get('choices') or [])} choices"
            )
        q["why_wrong"] = new_why_wrong
        updated += 1
    if missing:
        print(f"why_wrong_fix_head_neck_v1: {len(missing)} ids not found: {missing}")
    return updated
