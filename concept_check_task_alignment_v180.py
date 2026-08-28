"""v18.0 — focused Concept Check task/answer alignment repair.

The post-completion v17.8 artifact identified a sentinel set of older oral-board
conversions whose stems were clinically framed but whose reveal answers were too
short or merely repeated a recognition sentence.  This file deliberately repairs
only those confirmed weak items.  Canonical topic/concept linkage is untouched.

Each repair asks for a decision a resident/chief actually has to make and supplies
an answer that covers the requested action plus the escalation/anatomic discriminator.
"""


def _payloads():
    return {
        "cc-v112-rec-rhinology-allergy-skull-base-ethmoidectomy": {
            "prompt": (
                "A patient with medically refractory chronic rhinosinusitis is scheduled for complete ethmoidectomy. "
                "Preoperative CT shows a low asymmetric skull base and a focal area of lamina papyracea dehiscence. "
                "How should those findings change operative planning, and which intraoperative findings require immediate escalation rather than routine continuation?"
            ),
            "answer_text": (
                "Review the CT in all planes before entering the ethmoid, define the skull-base height/slope, lamina papyracea, basal lamella, anterior ethmoidal artery course, and any Onodi or frontal-recess variants, then proceed cell-by-cell while maintaining known boundaries. "
                "Orbital fat violation, extraocular-movement change, brisk bleeding near the anterior ethmoidal artery/skull base, or suspected CSF leak should stop routine dissection and trigger direct assessment and complication-specific rescue before further instrumentation."
            ),
            "explanation": "Ethmoidectomy safety depends on translating patient-specific CT anatomy into operative boundaries; orbital injury, skull-base injury, and vascular injury are stop-and-reassess events rather than findings to work past blindly.",
            "board_pearl": "In ethmoid surgery, the safest landmark is the one you have continuously identified—not the one you assume should be present.",
        },
        "cc-v112-mgt-thyroid-parathyroid-salivary-submandibular-gland-excision": {
            "prompt": (
                "A patient has a firm submandibular-gland mass for which excision is planned after appropriate imaging and tissue evaluation. "
                "Which anatomic structures must be deliberately identified/protected during a transcervical excision, and what preoperative or intraoperative finding should change a routine benign-gland plan?"
            ),
            "answer_text": (
                "Plan around the marginal mandibular branch of the facial nerve, facial vein/artery, lingual nerve, hypoglossal nerve, and Wharton duct while staying in the appropriate gland/fascial plane. "
                "Suspicion for malignancy, fixation, perineural symptoms, pathologic nodes, or gross nerve/adjacent-structure invasion should convert the case from simple inflammatory-gland excision to oncologic planning with adequate margins, nodal assessment as indicated, and explicit nerve-management strategy rather than unexpected piecemeal removal."
            ),
            "explanation": "Submandibular excision is not just removal of the gland; operative risk is defined by adjacent cranial nerves and the facial vessels, and suspected malignancy changes the extent and oncologic objectives of surgery.",
            "board_pearl": "A submandibular mass with neural symptoms or fixation is not a routine sialadenitis operation until proven otherwise.",
        },
        "cc-v112-mgt-thyroid-parathyroid-salivary-secondary-tertiary-hyperparathyroidism": {
            "prompt": (
                "A dialysis patient has markedly elevated PTH despite optimized medical therapy and is referred for surgery; another patient with a functioning renal transplant remains hypercalcemic with persistently autonomous PTH secretion. "
                "How do you distinguish the operative physiology in these two scenarios, and what perioperative issue must be anticipated after successful surgery?"
            ),
            "answer_text": (
                "Secondary hyperparathyroidism is usually diffuse multigland hyperplasia driven by chronic kidney disease, whereas tertiary disease is autonomous PTH secretion after prolonged stimulation and typically presents with hypercalcemia. "
                "Surgical planning therefore assumes multigland disease rather than a single adenoma and may use subtotal parathyroidectomy or total parathyroidectomy with autotransplantation according to the clinical context. After successful correction, anticipate profound calcium demand/hungry-bone physiology and monitor calcium closely with proactive replacement when indicated."
            ),
            "explanation": "The key distinction is stimulus-driven multigland hyperplasia versus autonomous secretion; both are multigland surgical problems, and postoperative hypocalcemia can be clinically significant after high-turnover bone disease is abruptly deprived of PTH.",
            "board_pearl": "In renal hyperparathyroidism, a 'focused adenoma' mental model is usually the wrong starting point.",
        },
        "cc-v112-rec-head-neck-oncology-hypopharyngeal-cancer": {
            "prompt": (
                "A patient with progressive dysphagia, weight loss, referred otalgia, and a pyriform-sinus lesion has biopsy-proven squamous cell carcinoma with ipsilateral cervical adenopathy. "
                "What must be defined before choosing definitive therapy, and which findings most strongly change whether organ-preservation treatment or primary surgery is reasonable?"
            ),
            "answer_text": (
                "Complete endoscopic examination and cross-sectional staging should define subsite extent, laryngeal function, cartilage/prevertebral or major-vessel involvement, nodal burden, distant disease risk, nutrition, pulmonary reserve, and baseline swallowing. "
                "Treatment is stage- and function-dependent: potentially functional organs may be treated with appropriately selected chemoradiation or surgery, while grossly destructive disease, nonfunctional larynx, major structural invasion, salvage setting, or inability to tolerate organ-preservation therapy can favor primary surgery with planned reconstruction and swallowing rehabilitation."
            ),
            "explanation": "Hypopharyngeal cancer decisions are not made from T stage alone; disease extent, nodal burden, baseline laryngopharyngeal function, comorbidity, and the functional cost of each modality determine the plan.",
            "board_pearl": "An anatomic 'organ-preservation' plan is not functional preservation if the larynx is already unsafe or nonfunctional.",
        },
        "cc-v112-rec-pediatric-otolaryngology-laryngotracheal-reconstruction": {
            "prompt": (
                "A tracheostomy-dependent child with subglottic stenosis is being considered for laryngotracheal reconstruction after prior endoscopic treatment. "
                "What information must be established before committing to reconstruction, and which findings would make you delay, stage, or choose a different airway strategy?"
            ),
            "answer_text": (
                "Map the entire airway endoscopically, including stenosis grade/length, glottic mobility, posterior glottis, trachea, and any multilevel disease, while assessing pulmonary reserve, aspiration/swallowing, reflux or inflammatory contributors, infection, and the child's ability to tolerate postoperative airway management. "
                "Poor pulmonary reserve, uncontrolled aspiration/infection, severe multilevel obstruction, significant glottic dysfunction, or an airway that cannot safely support the planned postoperative course should prompt optimization, staged reconstruction, or an alternative approach rather than forcing a single-stage plan."
            ),
            "explanation": "Successful pediatric airway reconstruction depends on complete airway mapping and host readiness; stenosis caliber alone does not determine candidacy or staging.",
            "board_pearl": "Before LTR, know the airway above and below the stenosis and know whether the child can physiologically tolerate the reconstruction you are planning.",
        },
        "cc-v112-rec-sleep-surgery-tongue-base-surgery": {
            "prompt": (
                "An adult with persistent obstructive sleep apnea despite PAP intolerance has retroglossal narrowing on awake examination. "
                "What evidence should confirm that tongue-base surgery is an appropriate target, and what findings should redirect you away from isolated tongue-base treatment?"
            ),
            "answer_text": (
                "Confirm that the residual sleep phenotype is predominantly obstructive and that dynamic evaluation demonstrates clinically meaningful tongue-base or lingual-tonsil contribution rather than assuming a static narrow airway is causal. "
                "Procedure choice depends on the actual mechanism and tissue target, prior surgery, BMI/comorbidity, and multilevel collapse. Central or hypoventilation physiology, dominant palatal/lateral-wall collapse, severe multilevel disease, or a nonanatomic cause of PAP failure should redirect treatment rather than lead to isolated tongue-base surgery."
            ),
            "explanation": "Tongue-base surgery is a phenotype-directed treatment. Dynamic collapse pattern and PSG physiology must agree with the proposed target, especially in revision or multilevel disease.",
            "board_pearl": "Do not operate on a narrow tongue base; operate on a demonstrated obstructive mechanism that the proposed procedure can actually correct.",
        },
        "cc-v112-rec-general-ent-emergencies-deep-neck-abscess-drainage": {
            "prompt": (
                "A patient with fever, trismus, neck swelling, and odynophagia has CT evidence of a rim-enhancing parapharyngeal collection with inflammatory change approaching the carotid sheath. "
                "How do you decide the airway and drainage strategy, and which findings require broader source control or escalation beyond a routine neck-space drainage?"
            ),
            "answer_text": (
                "Secure the airway early if there is progressive obstruction, floor-of-mouth/tongue-base displacement, inability to handle secretions, or a trajectory likely to make later airway control more difficult. Choose transoral versus transcervical drainage from the involved space, access, size, and relationship to the carotid sheath and other critical structures, while obtaining cultures and giving appropriate IV antibiotics. "
                "Multispace spread, mediastinal extension, vascular complication, persistent sepsis despite drainage, or an inadequately accessed compartment should trigger repeat imaging and additional cervical/thoracic or endovascular source-control planning rather than simply broadening antibiotics."
            ),
            "explanation": "Deep-neck infection management is airway plus anatomic source control. The dangerous error is to focus on the abscess volume while missing a worsening airway, vascular involvement, or descending infection.",
            "board_pearl": "If the airway is becoming harder by the hour, 'wait for antibiotics to work' is not an airway plan.",
        },
        "cc-v112-rec-laryngology-voice-swallowing-reinke-edema": {
            "prompt": (
                "A long-term smoker has progressive low-pitched dysphonia and bilateral polypoid vocal-fold swelling. One side has a focal epithelial irregularity and the airway is becoming increasingly narrow. "
                "What is the next evaluation and management priority, and which findings should prevent treatment as routine symmetric Reinke edema?"
            ),
            "answer_text": (
                "Perform complete laryngeal visualization with stroboscopic assessment when feasible, document airway caliber and vocal-fold mobility, and scrutinize any focal epithelial abnormality rather than assuming all swelling is benign. Smoking cessation and voice optimization are foundational; surgery is considered for significant dysphonia, airway compromise, or concerning/asymmetric disease. "
                "A focal suspicious lesion, impaired mobility, progressive airway symptoms, or other cancer red flags should prompt oncologic evaluation/biopsy planning instead of routine bilateral debulking alone."
            ),
            "explanation": "Classic Reinke edema is usually bilateral and benign, but smoking-related cancer risk and progressive airway narrowing change the priority from elective voice improvement to exclusion of malignancy and airway safety.",
            "board_pearl": "Do not let a familiar benign smoking-related diagnosis explain away a focal irregular lesion or impaired mobility.",
        },
        "cc-v112-rec-thyroid-parathyroid-salivary-men2-ret": {
            "prompt": (
                "A patient with a pathogenic RET variant is referred for thyroid management and reports episodic headaches and palpitations. "
                "What must be addressed before thyroid surgery, and how does the RET diagnosis change counseling and operative timing?"
            ),
            "answer_text": (
                "Evaluate for pheochromocytoma before thyroid surgery and treat a catecholamine-secreting tumor first when present, because unrecognized pheochromocytoma creates major anesthetic risk. RET genotype and age-specific medullary-thyroid-cancer risk guide timing/extent of thyroid surgery, while biochemical evaluation for medullary thyroid carcinoma and hyperparathyroidism informs the operative plan. "
                "The diagnosis also requires genetic counseling and cascade testing of at-risk relatives rather than treating the index thyroid lesion as an isolated sporadic cancer."
            ),
            "explanation": "MEN2 management is sequence-sensitive: pheochromocytoma safety comes before elective thyroid surgery, and RET genotype drives prophylactic/therapeutic planning and family screening.",
            "board_pearl": "In MEN2, rule out and control pheochromocytoma before taking the patient to the OR for thyroid disease.",
        },
        "cc-v112-rec-thyroid-parathyroid-salivary-sialendoscopy": {
            "prompt": (
                "A patient has recurrent meal-related submandibular swelling and imaging shows an obstructing ductal stone. "
                "Which features determine whether sialendoscopy is likely to be gland-preserving and successful, and when should you plan a combined or alternative approach?"
            ),
            "answer_text": (
                "Use history, examination, ultrasound or other appropriate imaging to define stone size, mobility, depth/location, duct caliber/stricture, and gland condition. Small accessible intraductal stones and focal strictures are favorable for endoscopic treatment. "
                "A large impacted hilar or intraparenchymal stone, unfavorable duct anatomy, severe fixed stenosis, suspected tumor, or repeated failure may require a combined endoscopic-open approach or another operation rather than repeated traumatic endoscopic attempts."
            ),
            "explanation": "Sialendoscopy is a gland-preservation strategy whose success depends on stone and duct anatomy; the correct escalation is driven by accessibility and pathology, not simply by symptom severity.",
            "board_pearl": "Know the stone's location and mobility before promising a purely endoscopic extraction.",
        },
    }


def apply_concept_check_task_alignment_v180(checks):
    payloads = _payloads()
    repaired = []
    missing = []
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    for qid, patch in payloads.items():
        q = by_id.get(qid)
        if q is None:
            missing.append(qid)
            continue
        q.update(patch)
        q["choices"] = []
        q["answer"] = None
        q["task_alignment_v180"] = True
        q["task_alignment_basis_v180"] = "manual resident/chief decision audit of v17.8 artifact"
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "expected": list(payloads)}
