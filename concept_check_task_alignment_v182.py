"""v18.2 — third focused Concept Check task/answer alignment repair.

Selected from the remaining shortest free-response reveals in the v17.8 all-domain
artifact after excluding the v18.0/v18.1 repaired cohorts. These ten topics are
high-yield resident decisions where a 11-13 word reveal was materially weaker than
the clinical prompt. Canonical linkage and existing review metadata are preserved.
"""


def _payloads():
    return {
        "cc-v112-rec-head-neck-oncology-floor-of-mouth-scc": {
            "prompt": (
                "A patient with tobacco and alcohol exposure has a painful ulcerative floor-of-mouth lesion, tongue numbness, and a palpable ipsilateral level I node. Examination suggests fixation near the mandibular periosteum. "
                "What must be defined before treatment, and which anatomic findings most strongly change the resection, neck, and reconstruction plan?"
            ),
            "answer_text": (
                "Confirm squamous cell carcinoma with biopsy and define the full oral-cavity primary by inspection and bimanual palpation, including depth, relationship to the mandible, tongue musculature, Wharton ducts, lingual nerve, and crossing of midline. Cross-sectional imaging should assess deep soft-tissue and mandibular invasion and characterize the neck; staging should include nodal and distant evaluation appropriate to disease burden. "
                "Mandibular cortical or medullary invasion changes marginal-versus-segmental mandibulectomy planning, while deep tongue/floor involvement changes functional resection and reconstructive requirements. A clinically involved neck requires therapeutic nodal management, and even a cN0 neck may require elective treatment based on pathologic risk such as depth of invasion. Reconstruction should restore tongue mobility, oral competence, and separation from the neck rather than simply close the defect."
            ),
            "explanation": "Floor-of-mouth SCC is an anatomic and functional planning problem: mandibular involvement, depth, midline extension, and nodal risk determine the operation and reconstruction.",
            "board_pearl": "Do not decide marginal versus segmental mandibulectomy from proximity alone; define actual mandibular invasion and the oncologic margin required.",
        },
        "cc-v112-rec-laryngology-voice-swallowing-arytenoid-adduction-reinnervation": {
            "prompt": (
                "An adult with unilateral vocal-fold paralysis has a large posterior glottic gap and vertical height mismatch despite a prior temporary injection. The nerve injury is not expected to recover quickly. "
                "How do arytenoid adduction, medialization, and reinnervation solve different problems, and what patient factors determine which strategy is appropriate?"
            ),
            "answer_text": (
                "Define the glottic insufficiency with laryngoscopy/stroboscopy, voice and swallowing assessment, and the expected prognosis for neural recovery. Medialization primarily improves the membranous glottic gap; arytenoid adduction is particularly useful when posterior gap or vertical-level mismatch remains important. Reinnervation aims to restore long-term tone and bulk rather than provide immediate static medialization, so benefit is delayed and depends on viable target muscle and patient factors such as age and denervation duration. "
                "Large gaps may need combined framework surgery, and aspiration risk can alter urgency. A potentially recoverable recent palsy favors temporary augmentation while prognosis evolves, whereas stable chronic paralysis may justify definitive framework surgery, reinnervation, or a combination tailored to gap geometry and goals."
            ),
            "explanation": "These procedures are complementary rather than interchangeable: gap geometry, recovery prognosis, timing, and functional goals determine the choice.",
            "board_pearl": "Posterior gap and vertical mismatch are classic reasons a simple implant may not fully solve unilateral paralysis.",
        },
        "cc-v112-mgt-rhinology-allergy-skull-base-frontal-recess-frontal-sinus": {
            "prompt": (
                "A patient with persistent frontal sinusitis is scheduled for revision endoscopic surgery. CT shows prior partial ethmoidectomy, residual frontal recess cells, a low skull base, and an anterior ethmoid artery close to the skull base. "
                "How should the CT drive the frontal recess dissection, and which findings should make you stop or change the planned extent rather than continue a routine frontal sinusotomy?"
            ),
            "answer_text": (
                "Review thin-cut multiplanar CT systematically to reconstruct the true frontal drainage pathway, residual agger/frontal cells, frontal beak, orbit, skull-base contour, anterior ethmoid artery, and prior surgical defects. In revision surgery, preserve orientation by working from known landmarks and removing the specific partitions obstructing the pathway rather than blindly enlarging superiorly. "
                "The chosen frontal procedure should match disease, anatomy, and prior failure; more extensive drill-out is not automatically better. Orbital fat exposure, suspected CSF leak, loss of a reliable skull-base boundary, significant bleeding near the anterior ethmoid artery, or anatomy that no longer matches the preoperative map should stop routine progression and trigger direct complication assessment or a revised approach."
            ),
            "explanation": "Frontal surgery succeeds when the surgeon reconstructs patient-specific drainage anatomy before operating; revision anatomy magnifies skull-base, orbital, and vascular risk.",
            "board_pearl": "In the frontal recess, identify which wall belongs to which cell before removing it; superior is not a safe substitute for anatomic orientation.",
        },
        "cc-v112-rec-head-neck-oncology-glottic-cancer": {
            "prompt": (
                "A smoker has persistent dysphonia and biopsy-proven glottic squamous cell carcinoma. Endoscopy shows a lesion approaching the anterior commissure with reduced but not absent vocal-fold mobility. "
                "What must be defined for staging and treatment selection, and how do mobility, subglottic extension, cartilage involvement, and baseline laryngeal function change the plan?"
            ),
            "answer_text": (
                "Define the exact vocal-fold and commissure extent endoscopically and with imaging when deeper spread or cartilage involvement is a concern, and document true vocal-fold mobility before treatment. Early superficial disease with preserved function may be treated with appropriately selected transoral surgery or radiation, with modality choice based on exposure, expected voice, extent, and patient preference. "
                "Impaired or fixed mobility, meaningful subglottic or paraglottic extension, cartilage invasion, bulky disease, or a nonfunctional larynx moves the problem beyond a simple early-glottic paradigm and may require more extensive surgery or nonsurgical organ-preservation therapy according to stage and function. The neck is generally lower risk in truly early glottic disease than in supraglottic disease, but nodal management follows actual stage and extension rather than the subsite label alone."
            ),
            "explanation": "Glottic cancer treatment hinges on deep extent and function, not merely the visible mucosal footprint; mobility is both a staging and functional clue.",
            "board_pearl": "A small-looking glottic lesion with impaired mobility is not automatically an 'early' cancer from a management standpoint.",
        },
        "cc-v112-rec-head-neck-oncology-parapharyngeal-space-tumor": {
            "prompt": (
                "An adult has a slowly enlarging parapharyngeal-space mass causing medial tonsillar displacement. MRI shows a well-circumscribed lesion, but the relationship to the carotid space and deep-lobe parotid is not yet clear. "
                "How should you localize the tumor before biopsy or surgery, and which imaging features change the differential and operative risk?"
            ),
            "answer_text": (
                "Use cross-sectional imaging to determine whether the lesion is prestyloid or poststyloid and to define its relationship to the deep parotid, carotid artery, internal jugular vein, sympathetic chain, and lower cranial nerves. Direction of fat displacement, carotid/jugular displacement, continuity with the parotid, and vascular flow characteristics help distinguish salivary tumors, nerve-sheath tumors, and paragangliomas. "
                "A hypervascular lesion should not undergo routine transoral needle manipulation without appropriate vascular consideration, and encasement or major-vessel displacement changes surgical planning. Approach selection should provide safe neurovascular control and adequate exposure for the tumor's size and origin; the apparent oropharyngeal bulge alone is not sufficient reason to choose a transoral approach."
            ),
            "explanation": "Parapharyngeal tumors are localized by compartment and displacement pattern before intervention because origin predicts both diagnosis and the structures placed at risk.",
            "board_pearl": "Prestyoid versus poststyloid is not trivia—it predicts whether you are mainly planning around salivary anatomy or the carotid/lower-cranial-nerve compartment.",
        },
        "cc-v112-rec-head-neck-oncology-total-laryngectomy": {
            "prompt": (
                "A patient with advanced laryngeal cancer is being considered for total laryngectomy after multidisciplinary review. The patient asks what changes permanently after surgery and what must be planned before the operation. "
                "What preoperative assessment and counseling are essential, and which postoperative complications require immediate escalation?"
            ),
            "answer_text": (
                "Confirm oncologic extent and resectability while assessing nutrition, pulmonary reserve, swallowing, thyroid status when relevant, prior radiation, dental and reconstructive needs, and the patient's ability to participate in rehabilitation. Counsel explicitly that the airway becomes permanently separated from the mouth and nose: the patient will breathe only through the neck stoma and requires a new communication strategy such as TEP, electrolarynx, or esophageal speech with speech-language pathology involvement. "
                "Plan pharyngeal closure/reconstruction according to defect and tissue quality and protect major vessels in high-risk salvage settings. Postoperatively, airway problems are managed through the stoma—not by oral or nasal intubation. Neck swelling or bleeding, salivary leak/pharyngocutaneous fistula, wound breakdown, hypocalcemia when thyroid/parathyroid tissue is affected, or signs of carotid exposure/infection require prompt evaluation and source-specific rescue."
            ),
            "explanation": "Total laryngectomy is both an oncologic resection and a permanent airway/communication reconstruction; safe care depends on planning rehabilitation and recognizing stoma-specific emergencies.",
            "board_pearl": "After total laryngectomy, the mouth and nose no longer connect to the lungs—oxygenation and intubation must be through the neck stoma.",
        },
        "cc-v112-rec-laryngology-voice-swallowing-vocal-fold-polyp-cyst": {
            "prompt": (
                "A professional voice user has persistent unilateral dysphonia. Stroboscopy shows a focal mid-membranous lesion with asymmetric vibration; the mucosal wave is markedly reduced over the lesion. "
                "How do you distinguish a polyp from a cyst or other focal lesion, and how does that distinction change treatment and surgical counseling?"
            ),
            "answer_text": (
                "Use high-quality laryngoscopy with stroboscopy to define lesion laterality, depth, vascularity, contralateral reactive change, and mucosal-wave behavior. Polyps are often superficial and may have a hemorrhagic or translucent appearance, whereas an intracordal cyst more often creates focal stiffness and reduced mucosal wave because it is embedded in the superficial lamina propria. The differential also includes fibrous lesions, scar, sulcus, and neoplasm when the pattern is atypical. "
                "Voice therapy and correction of phonotraumatic behaviors are useful before or around surgery, but a persistent symptomatic structural lesion may need phonomicrosurgery. Counsel that cyst dissection requires preservation of the layered cover and carries scar/stiffness risk; aggressive removal of surrounding lamina propria can worsen voice even if the lesion is completely excised."
            ),
            "explanation": "The key management distinction is lesion depth and mucosal-wave effect, because phonomicrosurgery succeeds by preserving vibratory tissue rather than simply removing a bump.",
            "board_pearl": "A focal absent mucosal wave should make you think about a deeper/stiffer lesion and the risk of trading the lesion for scar.",
        },
        "cc-v112-rec-otology-neurotology-ototoxic-noise-induced-hearing-loss": {
            "prompt": (
                "An adult receiving a potentially ototoxic medication reports new bilateral tinnitus and difficulty understanding speech in noise. Another worker has chronic occupational noise exposure. "
                "How should you distinguish and monitor ototoxic injury from noise-induced loss, and what findings require a change in exposure or treatment rather than routine reassurance?"
            ),
            "answer_text": (
                "Establish a detailed medication and acoustic-exposure timeline and compare current audiometry with a reliable baseline when available. Ototoxic injury often begins in the high frequencies and may progress with cumulative exposure; monitoring programs may use extended high-frequency audiometry and/or otoacoustic emissions when appropriate. Noise injury classically produces a high-frequency sensorineural pattern, but the individual audiogram, exposure history, asymmetry, and competing causes must be considered rather than relying on a single textbook notch. "
                "New threshold shift, worsening tinnitus with objective change, vestibular symptoms, or functional decline during ototoxic therapy should prompt coordination with the treating team to reduce dose, alter schedule, substitute therapy when medically feasible, and strengthen hearing-conservation/rehabilitation measures. Marked asymmetry, unilateral neurologic signs, or a pattern inconsistent with the exposure should trigger evaluation for another cause."
            ),
            "explanation": "Both conditions are exposure-related SNHL, but management depends on baseline comparison, trajectory, reversibility of the exposure, and recognition of atypical features.",
            "board_pearl": "Do not wait for conversational-frequency hearing loss before acting on ototoxic change; early high-frequency or symptom changes may be the first warning.",
        },
        "cc-v112-rec-pediatric-otolaryngology-congenital-neck-masses": {
            "prompt": (
                "A child has a recurrent lateral neck swelling that becomes tender during upper-respiratory infections. The family reports that it has been present intermittently since infancy. "
                "How should location and embryology guide the differential and workup, and when should infection be controlled before definitive surgery?"
            ),
            "answer_text": (
                "Start with age, exact midline-versus-lateral location, relationship to the hyoid and sternocleidomastoid, movement with swallowing or tongue protrusion, skin pits/drainage, compressibility, and history of infection. Ultrasound is often a useful first study for superficial cystic lesions, while CT or MRI is selected when deep extent, airway relationship, vascular anatomy, or a complex malformation must be defined. The differential includes thyroglossal duct cyst, branchial anomalies, dermoid, lymphatic/vascular malformation, thymic lesions, and neoplasm depending on anatomy. "
                "Treat acute cellulitis or abscess first when feasible rather than performing elective tract dissection through uncontrolled infection. Definitive surgery should remove the relevant embryologic tract/relationship—not merely the visible cyst—to reduce recurrence; vascular or lymphatic malformations may instead require observation, sclerotherapy, surgery, or combined treatment according to symptoms and anatomy."
            ),
            "explanation": "Congenital neck masses are best approached by embryologic pathway and anatomic location; acute infection can distort planes and increase recurrence or complication risk.",
            "board_pearl": "For a recurrent congenital cyst, ask what tract or embryologic remnant you must remove—not just how to drain the current swelling.",
        },
        "cc-v112-rec-pediatric-otolaryngology-pediatric-reflux-eosinophilic-esophagitis": {
            "prompt": (
                "A child has chronic throat clearing, feeding difficulty, intermittent solid-food dysphagia, and poor weight gain. Empiric acid suppression has not resolved symptoms, and there is a history of atopy. "
                "How should you distinguish reflux-related symptoms from eosinophilic esophagitis or oropharyngeal swallowing dysfunction, and what findings require GI or multidisciplinary evaluation rather than repeated empiric reflux treatment?"
            ),
            "answer_text": (
                "Do not diagnose reflux from nonspecific laryngeal symptoms alone. Clarify whether symptoms occur during the pharyngeal swallow, after swallowing, or specifically with solids; assess aspiration symptoms, growth, atopy, food impaction, chest discomfort, and response to prior therapy. Instrumental swallow evaluation is appropriate when airway protection or oropharyngeal dysphagia is suspected, while persistent solid-food dysphagia, food impaction, feeding aversion, poor growth, or strong atopic features should raise concern for esophageal disease such as eosinophilic esophagitis and prompt gastroenterology evaluation with endoscopy/biopsy when indicated. "
                "Repeated empiric acid suppression should not substitute for localization. Management then follows the demonstrated mechanism—swallow therapy and airway protection for oropharyngeal dysfunction, reflux-directed treatment for documented reflux disease, and coordinated dietary/pharmacologic therapy for confirmed eosinophilic esophagitis."
            ),
            "explanation": "Pediatric throat and feeding symptoms cross ENT, swallow, and GI domains; symptom localization prevents prolonged empiric reflux treatment from delaying EoE or aspiration diagnosis.",
            "board_pearl": "Solid-food dysphagia plus atopy or food impaction is an esophageal red flag, not a reason to keep escalating empiric laryngopharyngeal-reflux therapy.",
        },
    }


def apply_concept_check_task_alignment_v182(checks):
    payloads = _payloads()
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing = [], []
    for qid, patch in payloads.items():
        q = by_id.get(qid)
        if q is None:
            missing.append(qid)
            continue
        q.update(patch)
        q["choices"] = []
        q["answer"] = None
        q["task_alignment_v182"] = True
        q["task_alignment_basis_v182"] = "manual resident/chief decision audit of remaining short v17.8 free-response reveals"
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "expected": list(payloads)}
