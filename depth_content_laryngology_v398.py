"""v39.8 -- Laryngology / Voice / Swallowing depth repair (content-staleness
sweep, batch 9/9 -- final batch).

Same two defects as prior batches. Muscle Tension Dysphonia already has
distinct, substantive recognize/localize content (not flagged for
duplication) -- only its operate placeholder is replaced. See
thyroglossal_duct_cyst_depth_v389 for the pattern and rationale.
"""

DOMAIN = "Laryngology / Voice / Swallowing"

DEPTH_V398 = {
    "Laryngeal Anatomy": {
        "recognize": (
            "Organize laryngeal anatomy in layers: the cartilaginous framework (thyroid, cricoid, "
            "paired arytenoids, epiglottis) provides the scaffold; the intrinsic muscles (thyroarytenoid, "
            "lateral and posterior cricoarytenoid, interarytenoid, cricothyroid) move the vocal folds "
            "and arytenoids; the cricoarytenoid and cricothyroid joints provide the actual motion "
            "interfaces; and the mucosal layers (Reinke's space/superficial lamina propria over the "
            "vocalis muscle) enable the vibratory mucosal wave that produces voice."
        ),
        "localize": (
            "Innervation splits cleanly by muscle: the cricothyroid muscle (the primary pitch-raising "
            "muscle) is innervated by the external branch of the superior laryngeal nerve (EBSLN), "
            "while every other intrinsic laryngeal muscle is innervated by the recurrent laryngeal "
            "nerve (RLN) -- this single fact explains why EBSLN injury classically causes subtle "
            "pitch/projection problems rather than frank vocal fold immobility, while RLN injury "
            "causes true vocal fold paralysis."
        ),
        "operate": (
            "This module underlies essentially every laryngeal procedure rather than being an "
            "operation itself. Key steps: before any laryngeal surgery, mentally map the cartilage "
            "framework, the joint(s) relevant to the planned procedure (cricoarytenoid joint for "
            "arytenoid procedures, cricothyroid joint for framework surgery), and the nerve(s) at "
            "risk for the specific approach. Danger structures: the RLN (nearly every intrinsic "
            "muscle) and EBSLN (cricothyroid, at risk specifically during superior pole/cricothyroid "
            "region dissection, e.g., in thyroidectomy or cricothyroid approximation). Failure mode: "
            "treating the RLN as the only laryngeal nerve worth protecting and overlooking the EBSLN "
            "during dissection near the superior pole/cricothyroid area, producing a real but easily "
            "missed voice deficit (early vocal fatigue, loss of upper range/projection) that a "
            "standard mobility exam will not detect. Ongoing relevance: accurate framework/nerve "
            "anatomy is the shared foundation for interpreting every subsequent laryngeal finding, "
            "from stroboscopy to postoperative voice change."
        ),
    },
    "Stroboscopy Interpretation": {
        "recognize": (
            "Interpret stroboscopy systematically rather than jumping to a lesion name: describe "
            "glottic closure pattern (complete, posterior gap, hourglass, spindle), symmetry between "
            "sides, periodicity/regularity of vibration, amplitude of the mucosal wave, whether the "
            "mucosal wave itself is present or reduced, and the vertical level of vocal fold "
            "apposition -- this systematic description is the actual clinical data, not a shortcut to "
            "it."
        ),
        "localize": (
            "Each parameter localizes a different physiologic problem: closure pattern reflects "
            "glottic competence (neurologic or structural gap); amplitude/mucosal wave reflects "
            "pliability of the superficial lamina propria (reduced wave suggests scar/stiffness at "
            "that specific site); periodicity irregularity suggests a mass effect or asymmetric "
            "tension; vertical level mismatch suggests a joint or framework-level problem rather than "
            "a mucosal one."
        ),
        "operate": (
            "Stroboscopy itself is diagnostic, not a procedure, but the findings drive the operative "
            "decision that follows. Key steps: use the specific abnormal parameter to direct further "
            "workup or treatment -- a reduced mucosal wave over a discrete lesion points toward "
            "microsurgical excision preserving the superficial lamina propria; a posterior glottic gap "
            "with normal mucosal wave points toward a neurologic/framework problem (injection "
            "laryngoplasty, framework surgery) rather than a mucosal operation. Failure mode: "
            "recognizing a reduced mucosal wave and stopping there -- stiffness tells you a site is "
            "abnormal but not why (scar, deep infiltrative lesion, early malignancy versus benign "
            "lesion all can reduce wave) or what should be done about it, so the finding must be "
            "integrated with history, exam, and sometimes biopsy rather than treated as a complete "
            "diagnosis on its own. Ongoing plan: repeat stroboscopy after treatment to confirm "
            "restored vibratory function, not just resolved bulk/mass on white light exam alone."
        ),
    },
    "Vocal Fold Nodules": {
        "recognize": (
            "Vocal fold nodules are typically bilateral, symmetric, phonotraumatic lesions located at "
            "the junction of the anterior and middle thirds of the membranous vocal fold -- the point "
            "of maximum vibratory amplitude/impact during phonation -- producing a characteristic "
            "hourglass-shaped glottic closure pattern on stroboscopy."
        ),
        "localize": (
            "Because nodules form at the site of maximum mechanical vibratory stress from repetitive "
            "phonotrauma (vocal misuse/overuse, often with a hard glottal attack or excessive "
            "loudness), the causative behavior -- not just the tissue lesion -- is the actual site of "
            "the problem; nodules at this classic location and bilateral symmetric pattern are "
            "strongly suggest nodules, but cyst, polyp, scar and other lesions remain in the "
            "differential if appearance, wave or treatment response is atypical."
        ),
        "operate": (
            "Indication for surgery: rare, and reserved for mature, fibrotic nodules that persist "
            "despite an adequate trial of voice therapy; most nodules, especially early/soft ones, "
            "resolve with behavioral voice therapy alone since the lesion is a direct consequence of "
            "the phonotraumatic behavior. Setup/key steps: voice therapy targeting the underlying "
            "vocal behavior (reducing hard glottal attack, excessive loudness/tension, vocal overuse) "
            "is first-line and should be given adequate time before considering surgery; if surgery is "
            "eventually needed for persistent fibrotic nodules, microlaryngoscopic excision preserving "
            "the superficial lamina propria is the goal, not aggressive tissue removal. Danger "
            "structures: the vibratory mucosa/superficial lamina propria itself -- overly aggressive "
            "resection creates scar, which produces a worse and more permanent voice problem than the "
            "nodules being treated. Failure mode: proceeding to surgery without first treating (or "
            "without the patient adhering to) the causative vocal behavior -- since the behavior "
            "created the lesion, an unaddressed behavior predictably recreates it, making recurrence "
            "essentially expected if therapy is skipped. Postoperative plan (when surgery is done): "
            "voice therapy is still required afterward to prevent recurrence, and voice rest per "
            "surgeon protocol during initial mucosal healing."
        ),
    },
    "Vocal Fold Polyp / Cyst": {
        "recognize": (
            "Unlike nodules, polyps and cysts are usually unilateral, focal lesions producing "
            "asymmetric vibration on stroboscopy; polyps often follow a single traumatic/hemorrhagic "
            "vocal event, while cysts (subepithelial, filled with retained secretions) tend to "
            "produce even greater focal stiffness on stroboscopy because they are embedded within, "
            "rather than sitting on the surface of, the superficial lamina propria."
        ),
        "localize": (
            "Localize the lesion precisely along the membranous vocal fold and note its relationship "
            "to the vibratory margin and superficial lamina propria, since a true cyst is typically "
            "invested within this layer (making it harder to remove without disturbing surrounding "
            "tissue) compared to a polyp, which often sits more superficially and can be dissected "
            "with a cleaner plane."
        ),
        "operate": (
            "Indication: persistent dysphonia from a confirmed polyp or cyst not responding to a "
            "reasonable trial of voice therapy (more likely to help polyps with an inflammatory/"
            "hemorrhagic component than a true retention cyst, which rarely resolves without "
            "excision). Setup: microlaryngoscopy under suspension with magnification, sometimes with "
            "adjuncts (subepithelial infusion) to help define the dissection plane. Key steps: "
            "elevate a microflap preserving the overlying epithelium when feasible, dissect the "
            "lesion from the superficial lamina propria in the correct plane, and remove it intact "
            "without excising surrounding normal tissue as a margin (this is not an oncologic "
            "resection). Danger structures: the superficial lamina propria/vibratory margin itself -- "
            "removing more tissue than the lesion, or working in the wrong plane, creates scar. "
            "Failure mode: prioritizing an aggressive, wide excision to ensure the lesion is fully "
            "gone over preserving surrounding pliable mucosa -- for benign lesions, the resulting scar "
            "can produce a worse and more permanent dysphonia than the original polyp or cyst. "
            "Postoperative plan: voice rest per protocol, then graded return to voice use with "
            "therapy, and stroboscopy at follow-up to confirm restored mucosal wave, not just "
            "resolved bulk."
        ),
    },
    "FEES": {
        "recognize": (
            "Fiberoptic endoscopic evaluation of swallowing (FEES) directly visualizes the pharynx and "
            "larynx during swallowing trials, allowing direct assessment of secretion management, "
            "pooling/residue after the swallow, and penetration or aspiration both before and after "
            "the moment of laryngeal closure ('white-out'), as well as real-time response to "
            "compensatory strategies (postures, bolus modifications)."
        ),
        "localize": (
            "FEES localizes pharyngeal- and laryngeal-level swallowing physiology directly (what "
            "happens to secretions and boluses at the pharynx/larynx), but cannot directly visualize "
            "the oral phase or the moment of laryngeal closure itself (the view is obscured during "
            "the actual swallow, hence 'white-out'), which is a structural limitation compared to "
            "fluoroscopic (MBS) assessment of the same event."
        ),
        "operate": (
            "FEES is a diagnostic procedure, not a treatment, but its findings should drive a specific "
            "physiologic conclusion, not just a numeric score. Key steps: correlate findings across "
            "multiple bolus types/consistencies and volumes, test compensatory strategies in real "
            "time (chin tuck, effortful swallow, bolus modification) to see what actually improves "
            "safety for that patient, and directly visualize secretion management, since silent "
            "aspiration of secretions is itself clinically important information. Failure mode: "
            "reporting only a penetration-aspiration scale (PAS) score without stating the underlying "
            "physiologic impairment driving it (e.g., delayed pharyngeal swallow trigger vs. reduced "
            "laryngeal closure vs. impaired pharyngeal clearance) -- the PAS score is a severity "
            "marker, not a mechanism, and treatment planning requires the mechanism. Ongoing plan: "
            "repeat FEES to assess response to therapy or disease progression, and pair with MBS when "
            "oral-phase or precise timing information is needed that FEES cannot provide."
        ),
    },
    "Modified Barium Swallow": {
        "recognize": (
            "Modified barium swallow (MBS/videofluoroscopic swallow study) is a dynamic fluoroscopic "
            "study of the entire swallow sequence -- oral preparation and transit, pharyngeal swallow "
            "(timing, laryngeal elevation, epiglottic inversion, pharyngeal clearance), and the "
            "upper/cervical esophageal phase -- across multiple bolus consistencies and volumes, "
            "capturing the moment of laryngeal closure that FEES cannot directly see."
        ),
        "localize": (
            "Because MBS visualizes the full oral-through-cervical-esophageal sequence in real time, "
            "it localizes dysfunction to a specific phase and specific structure (delayed swallow "
            "trigger, reduced tongue base retraction, incomplete laryngeal elevation, cricopharyngeal "
            "dysfunction/upper esophageal sphincter opening) rather than just documenting that "
            "aspiration occurred."
        ),
        "operate": (
            "MBS is a diagnostic functional study, not a procedure, and its value comes from testing "
            "hypotheses in real time rather than capturing a single static image. Key steps: test "
            "multiple consistencies (thin liquid through solids) and, critically, test compensatory "
            "strategies and bolus modifications during the study itself to see what actually resolves "
            "the impairment for that patient, rather than inferring it afterward. Failure mode: "
            "treating MBS as a single confirmatory picture ('does this patient aspirate, yes/no') "
            "rather than the dynamic functional experiment it is designed to be -- the study's real "
            "value is identifying which specific phase is impaired and which specific strategy fixes "
            "it, which a single still frame cannot show. Ongoing plan: use findings to guide diet "
            "texture recommendations, therapy targets (specific phase/structure impaired), and, when "
            "a structural cause (cricopharyngeal dysfunction, stricture) is identified, further "
            "targeted workup or treatment."
        ),
    },
    "Microlaryngoscopy": {
        "recognize": (
            "Microlaryngoscopy uses suspension laryngoscopy to obtain a stable, binocular, "
            "magnified view of the larynx for diagnosis (biopsy) or phonomicrosurgery; achieving and "
            "maintaining adequate exposure is as central to the procedure's success as the "
            "instruments used once exposure is obtained."
        ),
        "localize": (
            "Exposure quality depends on patient-specific factors (neck mobility, mandible/tongue "
            "size, prior surgery/radiation) and laryngoscope choice/positioning; the anterior "
            "commissure and undersurface of the vocal folds are the areas most often "
            "under-visualized with standard exposure, which is why difficulty in these specific "
            "regions should prompt a change in strategy rather than forcing the existing view."
        ),
        "operate": (
            "Indication: diagnostic biopsy of a laryngeal lesion or phonomicrosurgical treatment of a "
            "benign or malignant lesion requiring direct magnified access. Setup: choose laryngoscope "
            "size/type and patient positioning (including external laryngeal manipulation) to optimize "
            "exposure before beginning the intended procedure; consider a rigid telescope or "
            "flexible-scope-assisted view when suspension exposure alone is inadequate for a "
            "difficult area (anterior commissure, subglottis). Key steps: work within the stable "
            "suspended exposure with fine instrumentation (microlaryngeal instruments, laser, "
            "cold-steel excision) tailored to the specific lesion and its relationship to the "
            "vibratory margin. Danger structures: teeth/gums (protected with a mouth guard), and the "
            "vibratory mucosa/superficial lamina propria itself during any excisional work. Failure "
            "mode: responding to poor exposure by applying more force or working through a limited, "
            "suboptimal view rather than repositioning, changing laryngoscope, or adding an "
            "adjunct -- poor exposure is a signal to change strategy, not a reason to push through "
            "with more destructive technique, since operating blind or through a bad view directly "
            "increases the risk of injuring normal tissue. Postoperative plan: voice rest per "
            "protocol and staged voice therapy for phonomicrosurgical cases, with pathology results "
            "directing any further treatment for diagnostic biopsies."
        ),
    },
    "Reinke Edema": {
        "recognize": (
            "Reinke edema is diffuse, often bilateral, gelatinous fluid accumulation within the "
            "superficial lamina propria (Reinke's space), producing a characteristically low-pitched, "
            "rough voice; smoking is the dominant driver, and severe cases can produce visible airway "
            "narrowing from bulky, redundant vocal fold tissue."
        ),
        "localize": (
            "The process is localized specifically to Reinke's space -- the potential space just deep "
            "to the vocal fold epithelium and superficial to the vocalis muscle -- distinguishing it "
            "from lesions that arise within the muscle or from focal mucosal lesions; its diffuse, "
            "often fold-length distribution (rather than a discrete focal lesion) is itself a "
            "distinguishing feature on exam."
        ),
        "operate": (
            "Indication: significant dysphonia or airway compromise from Reinke edema, generally "
            "after smoking cessation counseling/attempts, since continued smoking both drives disease "
            "progression and worsens surgical healing. Setup: microlaryngoscopy with a plan to "
            "evacuate the edematous fluid/tissue while preserving the epithelial cover. Key steps: "
            "make a controlled incision (often superior surface, away from the vibratory margin), "
            "evacuate the gelatinous contents, and trim redundant tissue conservatively, generally "
            "staging bilateral surgery to avoid anterior commissure webbing if both sides need "
            "treatment. Danger structures: the vibratory mucosa/epithelial cover -- this must be "
            "preserved and redraped rather than excised, since the epithelium is what will vibrate "
            "again once the underlying edema is removed. Failure mode: over-resecting tissue "
            "(epithelium or superficial lamina propria) rather than conservatively evacuating the "
            "edematous space and preserving the vibratory cover -- over-resection creates scar, which "
            "produces a stiffer, worse-sounding voice than the edema being treated. Postoperative "
            "plan: voice rest, continued smoking cessation support (recurrence is very likely with "
            "continued smoking), and staged treatment of the contralateral side if needed."
        ),
    },
    "Presbyphonia": {
        "recognize": (
            "Presbyphonia refers to age-related vocal fold atrophy causing bowing of the membranous "
            "vocal folds, glottic insufficiency, and a weak, breathy, sometimes tremulous voice; "
            "because these features overlap with vocal fold paresis/paralysis and with certain "
            "neurologic or systemic diseases, presbyphonia is a diagnosis that requires actively "
            "excluding those other causes, not simply attributing any elderly patient's weak voice to "
            "age."
        ),
        "localize": (
            "The atrophic process localizes to the thyroarytenoid/vocalis muscle bulk and superficial "
            "lamina propria, producing bilateral, generally symmetric bowing; asymmetry, or a "
            "unilateral pattern, should prompt evaluation for paresis/paralysis rather than being "
            "assumed to be simple age-related atrophy."
        ),
        "operate": (
            "Indication: functionally significant glottic insufficiency from confirmed age-related "
            "atrophy (paresis/systemic disease excluded) that has not adequately responded to voice "
            "therapy. Setup: voice therapy is first-line and should be trialed before considering an "
            "augmentative procedure. Key steps: when a procedure is needed, injection laryngoplasty "
            "(temporary or longer-lasting material) or, for durable correction, medialization "
            "thyroplasty can improve glottic closure by augmenting the atrophic fold. Danger "
            "structures: as for any injection/framework laryngoplasty -- avoid overinjection or an "
            "asymmetric result. Failure mode: treating the complaint as an inevitable, untreatable "
            "consequence of aging and not offering functional intervention -- the goal is treating "
            "the specific functional complaint (voice weakness/fatigue, inadequate volume/"
            "projection) the patient actually has, not the patient's chronological age. Postoperative "
            "plan: voice therapy alongside any procedural intervention, since behavioral optimization "
            "and augmentation are complementary, not alternative, treatments."
        ),
    },
    "Muscle Tension Dysphonia": {
        "operate": (
            "This is a functional, not surgical, diagnosis, and no procedure treats muscle tension "
            "dysphonia (MTD) directly. Key steps: the essential decision-making step is distinguishing "
            "primary MTD (no identifiable organic driver) from secondary/compensatory MTD (excess "
            "tension compensating for an underlying glottic lesion, paresis, reflux, or another "
            "organic process) before committing to a treatment plan, since primary MTD responds to "
            "voice therapy alone while secondary MTD will recur or plateau unless the underlying "
            "driver is also treated. This requires a full laryngeal exam/stroboscopy to actively look "
            "for an organic cause, not just observation of supraglottic squeeze. Failure mode: "
            "treating visible supraglottic squeeze as the primary diagnosis and endpoint of workup, "
            "rather than as a behavioral finding that may be compensating for something else -- "
            "referring a patient for voice therapy alone without ruling out an underlying organic "
            "driver risks incomplete or recurring symptoms. Ongoing plan: voice therapy targeting the "
            "excess tension pattern for primary MTD, combined with treatment of the identified "
            "underlying cause for secondary MTD (e.g., addressing reflux, treating the causative "
            "lesion, or managing paresis)."
        ),
    },
    "Vocal Tremor": {
        "recognize": (
            "Vocal tremor is a rhythmic oscillation of pitch/loudness during sustained phonation and "
            "can involve not just the vocal folds but the palate, pharynx, and supraglottic "
            "structures; it is a movement disorder distinct from spasmodic dysphonia, a task-specific "
            "focal laryngeal dystonia that produces strained or breathy voice breaks rather than a "
            "rhythmic oscillation."
        ),
        "localize": (
            "Because tremor can involve structures beyond the true vocal folds, a full examination "
            "(and often collaboration with neurology) should assess the palate, pharyngeal "
            "constrictors, and supraglottis, not just glottic closure, since essential tremor with "
            "vocal involvement classically affects this broader set of structures and can coexist "
            "with tremor elsewhere in the body (hands, head)."
        ),
        "operate": (
            "This is primarily a medically/neurologically managed condition rather than a surgical "
            "one, though botulinum toxin injection into the intrinsic laryngeal muscles is used for "
            "tremor with prominent laryngeal/vocal fold involvement, similar to its use in spasmodic "
            "dysphonia. Key steps: confirm the diagnosis and distinguish it from spasmodic dysphonia "
            "(oscillatory vs. task-specific strained/breathy breaks) before choosing treatment, "
            "coordinate with neurology for systemic tremor management (medications) when appropriate, "
            "and consider laryngeal botulinum toxin for patients with significant vocal fold "
            "involvement not adequately controlled by systemic treatment. Failure mode: examining "
            "only the true vocal folds and missing supraglottic/pharyngeal/palatal tremor "
            "contribution, or conflating vocal tremor with spasmodic dysphonia and choosing the wrong "
            "injection targets/dosing strategy as a result. Ongoing plan: periodic reassessment and "
            "re-dosing of botulinum toxin when used, since effect is temporary, similar to its use in "
            "other laryngeal movement disorders."
        ),
    },
    "Leukoplakia / Laryngeal Dysplasia": {
        "recognize": (
            "'Leukoplakia' is a purely visual/descriptive term for a white mucosal plaque and spans a "
            "wide histologic range from benign hyperkeratosis through varying grades of dysplasia to "
            "invasive carcinoma -- the term itself carries no diagnostic or prognostic information "
            "until tissue is examined, so it should never be treated as if it were itself a histologic "
            "diagnosis."
        ),
        "localize": (
            "Associated features on exam/stroboscopy raise or lower concern independent of the white "
            "color itself: an irregular, friable, or ulcerated surface, associated abnormal "
            "vascularity, reduced mucosal wave over the lesion, or a fixed/immobile segment all "
            "increase suspicion for higher-grade dysplasia or invasive disease, while a thin, smooth, "
            "mobile-appearing plaque is more suggestive of benign keratosis -- though appearance alone "
            "cannot substitute for biopsy."
        ),
        "operate": (
            "Indication: biopsy persistent, changing, irregular, vascular, stiff or otherwise "
            "suspicious leukoplakia to establish histology; selected thin, smooth, low-risk lesions "
            "may first receive risk-factor treatment with a defined short-interval exam and "
            "biopsy if they persist. Appearance alone never establishes histologic grade. Setup: microlaryngoscopy for biopsy or, when the "
            "lesion is amenable, complete microflap excision that serves as both diagnosis and "
            "treatment. Key steps: excise or biopsy with attention to obtaining adequate tissue for "
            "grading while preserving as much normal vibratory mucosa as possible, since many lesions "
            "ultimately prove benign or low-grade. Danger structures: the vibratory "
            "mucosa/superficial lamina propria, particularly relevant when repeat excisions are "
            "needed for recurrent or persistent disease. Failure mode: managing a lesion based on its "
            "visual appearance ('leukoplakia' as a working diagnosis) without histologic confirmation, "
            "or assuming a single benign biopsy result means no further surveillance is needed for a "
            "persistent or recurrent lesion. Postoperative plan: pathology-directed follow-up -- "
            "close surveillance (serial laryngoscopy) for dysplasia given recurrence and progression "
            "risk, and standard oncologic management if invasive carcinoma is found."
        ),
    },
    "Injection Laryngoplasty": {
        "recognize": (
            "Injection laryngoplasty augments the paralyzed or atrophic vocal fold to improve glottic "
            "closure, using either a temporary material (for early paralysis when spontaneous "
            "recovery is still possible, or as an in-office diagnostic/therapeutic trial) or a more "
            "durable material (for confirmed permanent paralysis or as definitive treatment); it does "
            "not restore nerve function or vocal fold motion -- it only improves closure of the "
            "existing, immobile position."
        ),
        "localize": (
            "Material is placed lateral to the vocalis muscle, within or just deep to the "
            "paraglottic space, at a level and volume calculated to bring the immobile fold to a more "
            "medial resting position; injection depth and location (too superficial risks placing "
            "material within the vibratory mucosa itself, which stiffens the vibratory margin) "
            "determine both efficacy and voice quality outcome."
        ),
        "operate": (
            "Indication: glottic insufficiency from vocal fold paralysis/paresis or atrophy causing "
            "dysphonia and/or aspiration; can be performed in-office (awake, transoral or "
            "transcutaneous) or under general anesthesia, and with temporary or long-lasting material "
            "depending on whether recovery is still possible or the deficit is established. Setup: "
            "confirm mobility status and glottic gap pattern (stroboscopy) before selecting material "
            "and approach. Key steps: inject at the appropriate depth (lateral to vocalis, avoiding "
            "the superficial lamina propria/vibratory margin) and volume, titrating to visual "
            "closure and, when awake, real-time voice quality feedback, since overinjection creates "
            "its own asymmetry and airway/voice problems. Danger structures: the vibratory "
            "mucosa/superficial lamina propria (avoid superficial placement) and, for transcutaneous "
            "approaches, surrounding neurovascular structures at the injection entry site. Failure "
            "mode: overinjection (producing a stiff, asymmetric-sounding voice or even airway "
            "compromise from excess bulk) or too-superficial injection (stiffening the vibratory "
            "margin itself) -- both are avoidable technical errors rather than inherent limitations of "
            "the procedure. Postoperative plan: reassess voice and, if temporary material was used, "
            "plan for repeat injection or transition to a durable procedure (framework surgery, "
            "long-lasting injection) once recovery potential is clarified."
        ),
    },
    "Arytenoid Adduction / Reinnervation": {
        "recognize": (
            "When glottic insufficiency includes a significant posterior glottic gap or a vertical "
            "level mismatch between the two vocal folds (not just a simple medial-lateral gap), "
            "injection or medialization thyroplasty alone may be insufficient, and arytenoid "
            "repositioning (adduction) is needed to correct the arytenoid's rotational/vertical "
            "malposition; laryngeal reinnervation, by contrast, aims to restore muscle tone gradually "
            "over months rather than producing an immediate mechanical change."
        ),
        "localize": (
            "Arytenoid adduction acts at the cricoarytenoid joint level, mechanically rotating and "
            "repositioning the arytenoid to close a posterior gap and correct vertical mismatch; "
            "reinnervation (e.g., ansa cervicalis to recurrent laryngeal nerve) acts at the "
            "neuromuscular level, restoring tone and bulk to the paralyzed musculature over time "
            "rather than directly repositioning any structure."
        ),
        "operate": (
            "Indication: arytenoid adduction for a posterior glottic gap or significant vertical level "
            "mismatch not correctable by medialization alone; reinnervation for patients (especially "
            "younger patients with longer expected survival) with unilateral paralysis where restoring "
            "durable, dynamic muscle tone is preferred over a purely static procedure. Setup: these "
            "framework/reinnervation procedures are chosen based on which specific physiologic defect "
            "(medial-lateral gap, posterior gap, vertical mismatch, or overall muscle tone/bulk loss) "
            "is present -- they are not interchangeable, and a patient may need a combination "
            "(e.g., thyroplasty plus arytenoid adduction). Key steps: for arytenoid adduction, expose "
            "and reposition the muscular process of the arytenoid via suture technique to simulate "
            "lateral cricoarytenoid muscle action, typically combined with medialization thyroplasty; "
            "for reinnervation, coapt a donor nerve (e.g., ansa cervicalis) to the recurrent laryngeal "
            "nerve or directly to the thyroarytenoid muscle, accepting that functional improvement "
            "develops over months as reinnervation matures, not immediately. Danger structures: the "
            "recurrent laryngeal nerve and cricoarytenoid joint capsule during arytenoid manipulation. "
            "Failure mode: choosing thyroplasty alone for a defect that is truly a posterior gap or "
            "vertical mismatch problem, or expecting reinnervation to produce immediate mechanical "
            "improvement the way a framework procedure does -- framework surgery, injection, and "
            "reinnervation solve different physiologic problems and are matched to the specific "
            "defect present, not chosen interchangeably. Postoperative plan: voice therapy and serial "
            "reassessment, with reinnervation outcomes specifically evaluated only after adequate time "
            "for reinnervation to mature."
        ),
    },
    "Posterior Cordotomy / Arytenoidectomy": {
        "recognize": (
            "Posterior cordotomy and arytenoidectomy are airway-widening procedures for bilateral "
            "vocal fold immobility, and every version of this trade-off widens the glottic airway at "
            "some cost to glottic closure -- meaning voice quality and, at the extremes, aspiration "
            "risk during swallowing -- so the procedure is chosen and its extent titrated based on how "
            "much airway improvement is actually needed, not simply performed to a fixed template."
        ),
        "localize": (
            "Posterior cordotomy widens the airway by dividing/lateralizing the posterior vocal fold "
            "and vocal process region on one side; arytenoidectomy (partial or complete) removes some "
            "or all of the arytenoid cartilage on one side, producing a generally larger airway gain "
            "than cordotomy alone but a correspondingly greater impact on voice and glottic closure "
            "for swallowing."
        ),
        "operate": (
            "Indication: symptomatic bilateral vocal fold immobility causing airway obstruction, after "
            "an adequate observation period for potential recovery has passed (or immediately if "
            "airway compromise is too severe to wait) and after tracheostomy has been considered as "
            "an alternative that avoids permanent glottic alteration. Setup: endoscopic approach under "
            "suspension laryngoscopy, typically starting unilaterally (leaving the option to treat the "
            "other side only if needed) since bilateral aggressive widening at once is more likely to "
            "produce dysphonia/aspiration than staged, conservative treatment. Key steps: perform the "
            "least extensive procedure expected to achieve an adequate airway -- cordotomy before "
            "arytenoidectomy, unilateral before bilateral -- and reassess before escalating. Danger "
            "structures: the remaining functional glottic closure mechanism and airway protection "
            "during swallowing; every additional millimeter of surgically created airway gap comes "
            "with a corresponding voice and/or aspiration consequence, so this is not a "
            "free trade. Failure mode: performing an unnecessarily extensive procedure "
            "(bilateral or complete arytenoidectomy) when a smaller unilateral cordotomy would have "
            "achieved an adequate airway, sacrificing more voice/swallow function than the clinical "
            "situation required. Postoperative plan: reassess airway, voice, and swallow function "
            "together (not airway alone) before considering the procedure complete, and stage further "
            "widening only if the initial, more conservative procedure proves inadequate."
        ),
    },
}


def apply_depth_content_laryngology_v398(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V398 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.8: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V398.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V398.keys())}
