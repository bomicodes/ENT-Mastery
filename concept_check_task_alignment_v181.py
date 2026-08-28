"""v18.1 — second focused Concept Check task/answer alignment repair.

The v17.8 all-domain artifact identified a second cohort of oral-board conversions
whose prompts were clinically framed but whose reveals were still only 9–12 words
or inherited generic domain-danger language that did not answer the actual task.
This pass manually repairs ten confirmed outliers. It does not relabel topics,
invent canonical aliases, or blanket-rewrite the Concept Check bank.
"""


def _payloads():
    return {
        "cc-v112-rec-rhinology-allergy-skull-base-olfactory-dysfunction": {
            "prompt": (
                "An adult reports six months of persistent smell loss after a viral illness. Nasal endoscopy shows no obstructing polyps or mass, but the patient also describes intermittent parosmia. "
                "How should you localize and evaluate the olfactory deficit, and which findings would justify imaging or broader neurologic/skull-base evaluation rather than routine postviral counseling?"
            ),
            "answer_text": (
                "First separate conductive loss from sensorineural/postviral, traumatic, medication-related, or neurodegenerative dysfunction using focused history, nasal endoscopy, and validated smell testing when it will affect counseling or follow-up. "
                "Routine imaging is not required for every otherwise typical postviral loss, but unilateral findings, epistaxis or a nasal mass, cranial neuropathy, significant head trauma, progressive unexplained loss, or other focal neurologic/skull-base features should redirect evaluation toward targeted CT or MRI and the relevant specialty workup. Counsel on smoke/gas/food-safety precautions and olfactory training when appropriate."
            ),
            "explanation": "Olfactory loss is a localization problem before it is an imaging problem. A typical postviral pattern is managed differently from unilateral obstructive, skull-base, traumatic, or neurologic disease.",
            "board_pearl": "Do not order the same imaging for every anosmia patient; let unilateral anatomy, neurologic findings, trauma, and the endoscopic exam determine whether cross-sectional imaging adds value.",
        },
        "cc-v112-rec-laryngology-voice-swallowing-vocal-fold-nodules": {
            "prompt": (
                "A teacher has months of effortful dysphonia that worsens through the workday. Stroboscopy shows bilateral symmetric lesions at the midpoint of the membranous vocal folds with an hourglass closure pattern and preserved mucosal wave away from the lesions. "
                "What is the best initial treatment strategy, and what finding should make you reconsider a routine vocal-nodule pathway?"
            ),
            "answer_text": (
                "Begin with behavioral voice therapy, vocal-load and technique modification, hydration, and treatment of contributing irritants or inefficient phonation rather than routine excision. True nodules are usually bilateral and phonotraumatic and often improve without surgery. "
                "Marked asymmetry, focal stiffness or loss of mucosal wave, impaired mobility, a discrete cyst/polyp-like lesion, hemorrhage, or failure to improve despite appropriate therapy should prompt diagnostic reassessment and selective microlaryngoscopic intervention rather than repeatedly labeling the lesion as simple nodules."
            ),
            "explanation": "The board-level distinction is not just recognizing bilateral lesions; it is knowing that voice therapy is first-line and that asymmetric or stiff lesions may represent a different pathology requiring a different strategy.",
            "board_pearl": "Bilateral midpoint nodules are usually treated with behavior first; a unilateral stiff lesion is a reason to question the diagnosis, not a reason to intensify generic voice therapy indefinitely.",
        },
        "cc-v112-rec-facial-plastics-trauma-otoplasty": {
            "prompt": (
                "An adolescent requests correction of prominent ears. Examination shows bilateral antihelical underfolding with moderate conchal excess and mild asymmetry, without active infection or auricular skin disease. "
                "How should the deformity be analyzed before surgery, and which operative principles reduce the risk of an artificial or overcorrected result?"
            ),
            "answer_text": (
                "Analyze each ear separately for antihelical definition, conchal depth, concha-mastoid angle, lobular position, skin/cartilage quality, symmetry, and the patient's goals before choosing maneuvers. "
                "Antihelix creation may use mattress sutures or selective cartilage modification, while conchal excess may require setback or limited reduction; the operation should correct the actual components rather than applying one technique to every ear. Preserve a smooth helical contour, avoid excessive posteriorization or sharp cartilage edges, and recognize postoperative hematoma promptly because untreated hematoma can lead to cartilage injury and deformity."
            ),
            "explanation": "Otoplasty planning is deformity-specific. Antihelical underfolding and conchal excess are different mechanical problems and may require different or combined corrections.",
            "board_pearl": "Prominent-ear surgery starts with component analysis; overcorrection is often the result of treating every prominence as the same deformity.",
        },
        "cc-v112-rec-sleep-surgery-hns-activation-programming": {
            "prompt": (
                "A patient returns after uncomplicated hypoglossal nerve stimulator implantation with healed incisions and intact tongue motion. The patient asks why the device is not simply turned to maximal amplitude at the first postoperative visit. "
                "How should activation and subsequent programming be approached, and how do you distinguish a programming problem from a reason to reconsider anatomy or hardware?"
            ),
            "answer_text": (
                "Activate only after appropriate postoperative healing and confirm tongue motion, wound/device status, and patient readiness. Establish functional sensation and motor thresholds, choose a tolerable starting amplitude and electrode configuration, teach nightly use, and advance gradually rather than maximizing stimulation immediately. "
                "Persistent symptoms should be assessed with adherence and device data, awake tongue response, programming parameters, and follow-up sleep testing when appropriate. Inadequate physiologic response despite reasonable programming may require reassessment of collapse pattern, electrode configuration, or anatomy, whereas abrupt loss of previously effective stimulation, abnormal impedances, pain, or absent expected tongue movement raises concern for hardware or lead dysfunction."
            ),
            "explanation": "HNS success depends on staged activation, tolerable titration, and separating use/programming problems from persistent anatomic collapse or true hardware failure.",
            "board_pearl": "HNS implantation and HNS optimization are different phases of care; nonresponse should be phenotyped before revision is considered.",
        },
        "cc-v112-rec-head-neck-oncology-tep-and-alaryngeal-speech": {
            "prompt": (
                "A total-laryngectomy patient is considering tracheoesophageal puncture for voice rehabilitation. The stoma is well healed, but the patient has limited hand dexterity and intermittent dysphagia. "
                "What factors determine candidacy for TEP speech, and how should new leakage or loss of previously effective voice be evaluated rather than automatically replacing the prosthesis?"
            ),
            "answer_text": (
                "Assess motivation, cognition, vision and dexterity, caregiver support when needed, stoma access, pulmonary reserve for airflow, pharyngoesophageal segment function, swallowing, and the ability to maintain the prosthesis with speech-language pathology. "
                "For dysfunction, distinguish leakage through the prosthesis from leakage around it and separate prosthesis failure from tract enlargement, candidal biofilm, poor pulmonary airflow, pharyngoesophageal spasm/stenosis, recurrent tumor, or other structural disease. New dysphagia, progressive loss of voice, bleeding, pain, or unexplained tract change should trigger endoscopic or imaging evaluation as indicated rather than repeated blind prosthesis exchange."
            ),
            "explanation": "TEP rehabilitation requires both patient capability and a functioning pulmonary-pharyngoesophageal system. Leakage and voice failure have different mechanisms and should not be managed as a single prosthesis problem.",
            "board_pearl": "First ask whether leakage is through or around the TEP; the answer changes the differential and the fix.",
        },
        "cc-v112-mgt-thyroid-parathyroid-salivary-reoperative-hyperparathyroidism": {
            "prompt": (
                "A patient remains hypercalcemic with elevated PTH after prior parathyroid surgery, but the prior operative note is incomplete and current ultrasound is nondiagnostic. "
                "What must be established before reoperative exploration, and which steps reduce the risk of an unsuccessful or unnecessarily hazardous scarred-neck operation?"
            ),
            "answer_text": (
                "First reconfirm true biochemical primary hyperparathyroidism and review the prior operative report, pathology, intraoperative PTH data, and any imaging to understand what glands were found or left behind. Obtain preoperative laryngeal examination and pursue high-quality localization with complementary studies such as ultrasound, sestamibi-based imaging, or 4D CT according to the case; selective venous sampling is reserved for difficult nonlocalizing situations. "
                "Reoperation should be targeted when benefit justifies the higher recurrent-laryngeal-nerve and hypoparathyroidism risk, with explicit consideration of ectopic or supernumerary glands, mediastinal disease, parathyromatosis, and hereditary/multigland physiology rather than blind bilateral scarred-neck exploration."
            ),
            "explanation": "Reoperative parathyroid surgery is localization-dependent and riskier than first-time exploration. Biochemical confirmation and reconstruction of prior anatomy come before another neck operation.",
            "board_pearl": "A scarred neck is not an indication for more aggressive exploration; it is an indication for better localization and better reconstruction of what happened before.",
        },
        "cc-v112-rec-laryngology-voice-swallowing-muscle-tension-dysphonia": {
            "prompt": (
                "A singer has progressive vocal effort and supraglottic squeeze on phonation. Stroboscopy also suggests a subtle unilateral glottic insufficiency. "
                "How do you distinguish primary muscle tension dysphonia from compensatory hyperfunction, and how does that distinction change treatment?"
            ),
            "answer_text": (
                "Use a complete voice history, perceptual and acoustic assessment when useful, flexible or rigid laryngoscopy with stroboscopy, and response to stimulability/voice-therapy maneuvers to determine whether excessive tension is primary or compensation for an underlying lesion, paresis, scar, bowing, or other glottic insufficiency. "
                "Behavioral voice therapy is central for primary muscle tension dysphonia, but persistent compensation will often recur unless the underlying structural or neurologic driver is also treated. Focal stiffness, progressive unilateral findings, impaired mobility, bleeding, weight loss, or other malignancy/neurologic red flags should prompt further diagnostic evaluation rather than attributing everything to tension."
            ),
            "explanation": "Supraglottic hyperfunction is a finding, not always the primary diagnosis. Management fails when compensatory tension is treated without addressing the glottic problem that generated it.",
            "board_pearl": "Do not stop at 'muscle tension' when the patient is squeezing to compensate for a real glottic insufficiency.",
        },
        "cc-v112-mgt-facial-plastics-trauma-scar-management": {
            "prompt": (
                "A patient presents four months after facial laceration repair with an erythematous raised scar that is still evolving and causes mild tension near the oral commissure but no major contracture. "
                "How should scar age, phenotype, and functional distortion guide treatment now, and when is surgical revision preferable to continued nonsurgical maturation therapy?"
            ),
            "answer_text": (
                "Classify the scar as hypertrophic, keloid, widened, depressed, tethered, or contracted and assess orientation, tension vectors, symptoms, pigmentation, vascularity, and distortion of nearby free margins. Early evolving scars are usually managed with sun protection, massage/silicone when appropriate, and targeted steroid, 5-FU, vascular/pigment laser, or resurfacing based on phenotype rather than immediate excision. "
                "Revision becomes more appropriate after adequate maturation when persistent width, contour deformity, poor orientation, or functional contracture will not respond to conservative therapy; Z-plasty, local tissue rearrangement, grafting, or flap reconstruction is chosen according to the specific tension and tissue deficit."
            ),
            "explanation": "Scar treatment is time- and phenotype-dependent. Premature revision can recreate the same biology unless tension and orientation are corrected.",
            "board_pearl": "A red four-month scar is not automatically a failed scar; determine whether the problem is active biology, tension, orientation, or true contracture before revising it.",
        },
        "cc-v112-rec-facial-plastics-trauma-local-flap-reconstruction": {
            "prompt": (
                "After Mohs excision, a patient has a cheek defect approaching the lower eyelid with exposed subcutaneous tissue but intact periosteum. "
                "Which defect and patient factors determine whether a local flap is preferable to a graft or larger regional reconstruction, and how should flap design avoid functional distortion?"
            ),
            "answer_text": (
                "Analyze defect size, depth, aesthetic subunit, exposed cartilage/bone/nerve, skin color and thickness, local laxity, vascular territories, prior radiation or surgery, and the position of free margins before choosing the reconstructive rung. "
                "A local flap is useful when adjacent tissue provides a good match and adequate vascularity, but its movement and closure vectors must not pull the eyelid, alar rim, lip, or brow out of position. Design incisions along favorable boundaries and relaxed tension lines when possible, use a broad reliable blood supply, distribute closure tension away from free margins, and escalate to graft, regional flap, or free tissue when local tissue cannot safely provide coverage without distortion."
            ),
            "explanation": "Local-flap selection is defect analysis plus vector control. A flap that closes the hole but creates ectropion or alar retraction is not a successful reconstruction.",
            "board_pearl": "Before moving tissue, decide where the closure tension will go; free-margin distortion is often predictable from the vector you create.",
        },
        "cc-v112-rec-rhinology-allergy-skull-base-endoscopic-maxillary-antrostomy": {
            "prompt": (
                "A patient with refractory maxillary sinus disease is scheduled for endoscopic maxillary antrostomy. CT shows a prominent Haller cell and the natural ostium is difficult to appreciate. "
                "Which landmarks must be confirmed before enlarging the drainage pathway, and what technical error commonly causes persistent recirculation or avoidable orbital/nasolacrimal injury?"
            ),
            "answer_text": (
                "Review multiplanar CT for the uncinate process, infundibulum, natural maxillary ostium, Haller cells, orbital floor/lamina, and nasolacrimal relationship, then identify the natural ostium endoscopically rather than relying on an accessory opening. "
                "The antrostomy should incorporate the natural ostium into a common drainage pathway; creating or enlarging only an accessory ostium can leave separate openings and promote mucus recirculation. Avoid blind superior or anterior instrumentation when anatomy is uncertain because the orbit and nasolacrimal system define important boundaries. Orbital fat exposure, unexpected ocular change, or concerning bleeding is a stop-and-reassess event rather than a reason to continue enlarging the opening."
            ),
            "explanation": "The operative objective is physiologic drainage through a common opening that includes the natural ostium while respecting orbital and nasolacrimal boundaries.",
            "board_pearl": "An antrostomy that misses the natural ostium can look large and still fail because it creates recirculation instead of a single drainage pathway.",
        },
    }


def apply_concept_check_task_alignment_v181(checks):
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
        q["task_alignment_v181"] = True
        q["task_alignment_basis_v181"] = "manual resident/chief audit of confirmed short or task-mismatched v17.8 reveals"
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "expected": list(payloads)}
