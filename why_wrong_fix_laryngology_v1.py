"""
why_wrong_fix_laryngology_v1.py

Replaces the generic/duplicate `why_wrong` text for the 30 Laryngology /
Voice / Swallowing items flagged by audit_question_quality.py
(GENERIC_WHY_WRONG). Each wrong choice gets its own specific clinical
reasoning. The correct choice's own slot is "Correct." to match schema.

Usage: same pattern as why_wrong_fix_general_ent_v1.py.

    from why_wrong_fix_laryngology_v1 import apply_why_wrong_fix_laryngology_v1
    WHY_WRONG_FIX_LARYNGOLOGY_V1 = apply_why_wrong_fix_laryngology_v1(runtime_entry.data)
"""

WHY_WRONG_FIXES = {
    "v141_lar_01": [
        "Total laryngectomy is an extreme, irreversible intervention reserved for "
        "intractable aspiration that fails all conservative measures; applying it to "
        "every aspiration event ignores that most aspiration, including this "
        "delayed-initiation pattern, responds to targeted rehabilitation.",
        "Correct.",
        "Silent aspiration (aspiration without a cough response) is not benign -- it "
        "still carries pneumonia risk and, if anything, deserves more vigilance since the "
        "usual protective warning sign is absent.",
        "Prophylactic antibiotics do not address the underlying swallowing physiology "
        "causing aspiration and do not prevent aspiration itself; they lead to resistance "
        "and side effects without treating the mechanism.",
    ],
    "v141_lar_02": [
        "Correct.",
        "Open resection is a major operation best reserved for long, mature, or "
        "cartilage-involving stenoses; applying it as first-line therapy to a short, "
        "thin, web-like stenosis exposes the patient to unnecessary morbidity when a "
        "simpler endoscopic approach is likely to succeed.",
        "Severe dyspnea from an airway-narrowing lesion should prompt intervention, not "
        "observation; deferring treatment risks acute decompensation.",
        "Injection laryngoplasty augments the glottis for glottic insufficiency (e.g., "
        "vocal fold paralysis); it does not address a fixed subglottic/tracheal narrowing "
        "and would not improve this stenosis.",
    ],
    "v141_lar_03": [
        "Stripping the vocal-fold mucosa treats a structural lesion, not a neurologic "
        "movement disorder; spasmodic dysphonia arises from abnormal central motor "
        "control, so removing tissue would not correct the dystonic muscle activity and "
        "would risk permanent voice damage.",
        "There is no infectious component to spasmodic dysphonia; antibiotics have no "
        "mechanism of action against a focal laryngeal dystonia.",
        "Correct.",
        "Tracheostomy bypasses the larynx for airway problems; it does not address voice "
        "production and is not indicated for a purely phonatory disorder with a normal "
        "airway.",
    ],
    "v141_lar_04": [
        "Reinke edema is a benign, smoking-related process, not a malignancy; radiation "
        "therapy is not indicated and would expose the patient to unnecessary risk and "
        "morbidity.",
        "Reinke edema is not an infectious process, so antibiotics have no role in "
        "treating the underlying smoking- and phonotrauma-related lamina propria change.",
        "Smokers are at risk for coexistent malignant or premalignant laryngeal lesions, "
        "so the larynx should always be carefully inspected for other pathology rather "
        "than assuming the diffuse edema is the only finding present.",
        "Correct.",
    ],
    "v141_lar_05": [
        "A wide cordectomy removes far more tissue than necessary for a focal benign "
        "cyst, sacrificing vibratory cover and voice quality when a precise, "
        "tissue-preserving microflap excision can address the lesion with far less "
        "morbidity.",
        "This is a benign cyst, not a malignancy; radiation is not indicated and would "
        "expose healthy laryngeal tissue to unnecessary damage.",
        "Correct.",
        "A true vocal fold cyst that has persisted despite voice therapy often does "
        "respond to careful surgical excision; saying no intervention can help ignores an "
        "established, effective treatment option.",
    ],
    "v141_lar_06": [
        "Correct.",
        "Tonsillectomy addresses oropharyngeal tonsillar tissue and has no effect on "
        "upper esophageal sphincter opening or cricopharyngeal muscle function.",
        "Vocal-fold injection treats glottic insufficiency from vocal fold immobility or "
        "atrophy; it does not act on the cricopharyngeus muscle or the upper esophageal "
        "sphincter and would not improve UES opening.",
        "Confirmed impaired UES opening with significant pharyngeal residue causes real "
        "aspiration and nutritional risk; declining any treatment ignores effective "
        "options like dilation, botulinum toxin, or myotomy.",
    ],
    "v142_lar_01": [
        "Correct.",
        "Bilateral cordotomy is an airway-widening procedure for bilateral vocal-fold "
        "immobility causing obstruction; this patient has unilateral paralysis with a "
        "closure/aspiration problem, so a bilateral airway-enlarging procedure is the "
        "wrong operation and would worsen voice and swallowing.",
        "Temporary injection augmentation does not interfere with nerve regeneration; "
        "withholding treatment and tolerating ongoing aspiration risks pneumonia while "
        "gaining no benefit, since intervention and recovery are not mutually exclusive.",
        "Total laryngectomy is an irreversible, drastic procedure reserved for situations "
        "like unsalvageable cancer or intractable aspiration after all else fails; it is "
        "wildly disproportionate for a potentially recoverable unilateral paralysis.",
    ],
    "v142_lar_02": [
        "Posterior cordotomy widens the airway by cutting into the vocal fold "
        "posteriorly for bilateral immobility with obstruction; it works against, not "
        "for, glottic closure and would worsen the breathy voice and gap described here.",
        "Correct.",
        "Cricotracheal resection treats subglottic/tracheal stenosis by removing a "
        "segment of the airway; it has no role in improving posterior glottic closure "
        "from unilateral vocal-fold paralysis.",
        "Tonsillectomy addresses oropharyngeal tissue and has no anatomic or physiologic "
        "relationship to glottic closure or vocal-fold position.",
    ],
    "v142_lar_04": [
        "Correct.",
        "A persistent focal absence of mucosal wave is, by definition, an abnormal "
        "stroboscopic finding, not a sign of normal vibration.",
        "Nasal obstruction affects airflow through the nose and has no direct effect on "
        "vocal-fold mucosal wave, which reflects the vibratory properties of the fold "
        "itself.",
        "Bilateral RLN paralysis would be expected to affect both vocal folds' motion and "
        "position, not produce a unilateral focal loss of mucosal wave with a normal "
        "contralateral side; this pattern instead localizes to a focal lesion on the "
        "affected fold.",
    ],
    "v143_lar_01": [
        "Correct.",
        "FEES visualizes the pharynx and larynx via a transnasal scope; it does not "
        "directly visualize the oral preparatory phase or the esophageal phase of "
        "swallowing at all.",
        "FEES has an inherent brief white-out moment during the pharyngeal swallow "
        "itself, when the pharyngeal walls close around the endoscope; this is a known "
        "limitation, not something the test eliminates.",
        "Measuring lower esophageal sphincter pressure requires manometry, not FEES, "
        "which is an endoscopic visualization technique of the pharynx and larynx, not a "
        "pressure-measurement study.",
    ],
    "v143_lar_02": [
        "A deep full-thickness cordectomy removes far more of the vibratory layers than "
        "needed for most benign lesions, creating scar and permanent voice impairment "
        "when superficial, tissue-preserving dissection would achieve the same "
        "diagnostic/therapeutic goal with better voice outcome.",
        "Broad thermal injury from cautery spreads heat beyond the intended target, "
        "damaging adjacent superficial lamina propria and increasing scar formation -- "
        "the opposite of the precision this surgery requires.",
        "Correct.",
        "Suspension microlaryngoscopy places significant pressure on the teeth, gums, and "
        "tongue base; ignoring these risks can cause dental injury or lingual "
        "nerve/tongue numbness, which are recognized, preventable complications of the "
        "exposure itself.",
    ],
    "v143_lar_03": [
        "Candidiasis typically presents as removable white plaques without the irregular "
        "vascularity and reduced mucosal wave described here; assuming a benign "
        "infectious cause without biopsy risks missing a malignant or premalignant "
        "lesion.",
        "Tonsillectomy addresses oropharyngeal tonsillar tissue and has no role in "
        "evaluating or treating a vocal-fold surface lesion.",
        "Correct.",
        "Leukoplakia is a descriptive term spanning a spectrum from benign keratosis to "
        "invasive carcinoma; reassurance without tissue diagnosis in a smoker with "
        "concerning features (irregular vascularity, reduced mucosal wave) could miss an "
        "early cancer.",
    ],
    "v143_lar_04": [
        "Posterior cordotomy/arytenoidectomy is a static, tissue-removing procedure that "
        "widens the fixed glottic opening; it does not restore neural function or normal "
        "vocal-fold motion, which remains immobile.",
        "Enlarging the posterior glottis to improve airway inevitably reduces glottic "
        "closure, which typically makes the voice breathier -- the procedure has a real "
        "and often significant effect on voice, not none at all.",
        "This is a laryngeal airway procedure targeting the glottis, not a nasal "
        "procedure; it has no direct effect on nasal airflow.",
        "Correct.",
    ],
    "v143_lar_05": [
        "Late radiation-associated dysphagia can be progressive and multifactorial "
        "(fibrosis, neuropathy, stenosis, or recurrent disease); assuming it is always "
        "stable without evaluation risks missing a treatable or dangerous cause, "
        "including tumor recurrence.",
        "Correct.",
        "Vocal-fold injection treats glottic insufficiency, not the fibrosis, neuropathy, "
        "or stricture that more commonly drives radiation-associated dysphagia; "
        "performing it without first characterizing the mechanism could miss the actual "
        "problem.",
        "Antibiotics treat infection, not the structural and neuromuscular changes from "
        "radiation fibrosis; treating with antibiotics alone would leave the underlying "
        "cause of progressive dysphagia unaddressed.",
    ],
    "v145_lar_01": [
        "Most acute laryngitis after a viral URI is viral or inflammatory, not "
        "bacterial; prolonged antibiotics would not address the cause and contribute to "
        "unnecessary resistance and side effects.",
        "Correct.",
        "There is no suggestion of fungal infection (such as in an immunocompromised "
        "host or after inhaled steroid use); empiric antifungal therapy is not warranted "
        "for typical post-viral laryngitis.",
        "Thyroplasty is a structural procedure for glottic insufficiency (e.g., vocal "
        "fold paralysis or atrophy); it is not indicated for self-limited post-viral "
        "laryngitis and would be a drastic, unnecessary intervention at this stage.",
    ],
    "v145_lar_02": [
        "Tonsillectomy addresses oropharyngeal tissue and has no anatomic relationship to "
        "arytenoid position or posterior glottic closure.",
        "Correct.",
        "Septoplasty corrects nasal septal deviation and has no effect on laryngeal "
        "geometry or vocal-fold closure.",
        "Myringotomy creates an opening in the tympanic membrane for middle-ear fluid; it "
        "is unrelated to laryngeal function or glottic closure.",
    ],
    "v145_lar_03": [
        "Correct.",
        "Aspiration-prevention procedures like laryngotracheal separation or glottic "
        "closure are designed to protect the airway from contamination, not to modify "
        "vocal pitch, which is a separate and, in this context, secondary consideration.",
        "Reflux treatment alone does not address severe, life-threatening aspiration that "
        "has already failed maximal rehabilitation; when aspiration is this severe, a "
        "mechanical solution separating the airway from the alimentary tract is needed, "
        "not medical reflux management alone.",
        "These procedures act on the larynx/trachea to prevent aspiration into the "
        "lungs; they have no relationship to nasal airflow.",
    ],
    "v145_lar_04": [
        "A negative pulmonary workup and non-infectious trigger pattern (talking, odors, "
        "temperature) point away from an infectious cause; repeated antibiotics would not "
        "address a sensory hyperresponsiveness disorder.",
        "Total laryngectomy is an irreversible, drastic procedure for conditions like "
        "intractable aspiration or malignancy; it is entirely disproportionate for a "
        "functional cough hypersensitivity syndrome and would not resolve the cough "
        "mechanism.",
        "There are effective, described treatments for laryngeal hypersensitivity and "
        "chronic cough, including behavioral cough suppression therapy and selected "
        "neuromodulators; stating no treatment exists is inaccurate.",
        "Correct.",
    ],
    "v145_lar_05": [
        "Globus is typically a sensation of a lump in the throat without progressive "
        "dysphagia or weight loss; the presence of these red-flag features makes "
        "reassurance inappropriate without first ruling out structural esophageal "
        "disease.",
        "Voice therapy addresses laryngeal/phonatory function, not esophageal transit; it "
        "does not evaluate or treat a structural cause of progressive solid-food "
        "dysphagia and weight loss.",
        "Intranasal steroids treat nasal/sinus inflammation and have no role in "
        "evaluating or treating esophageal dysphagia and weight loss.",
        "Correct.",
    ],
    "v145_lar_06": [
        "The false vocal fold (vestibular fold) lies superior to the ventricle, not "
        "inferior to it, and does not contain the vocal ligament.",
        "The aryepiglottic fold forms the lateral boundary of the laryngeal inlet "
        "superiorly, well above the ventricle, and has no relationship to the vocal "
        "ligament.",
        "Correct.",
        "The epiglottic petiole is the inferior attachment point of the epiglottis to the "
        "thyroid cartilage; it is unrelated to the ventricle's inferior boundary or the "
        "vocal ligament.",
    ],
    "v145_lar_07": [
        "MBS is a fluoroscopic imaging study of swallowing, not a tissue-sampling "
        "procedure; it cannot obtain a biopsy.",
        "MBS assesses swallowing physiology via radiographic bolus tracking; it has no "
        "capability to measure acoustic voice parameters like pitch.",
        "MBS and endoscopic studies like FEES each have distinct strengths (radiographic "
        "timing/anatomy versus direct mucosal/secretion visualization); MBS does not "
        "replace endoscopic evaluation, and the two are often complementary.",
        "Correct.",
    ],
    "v145_lar_08": [
        "There is no structural airway obstruction or mass in this case; a permanent "
        "tracheostomy is an airway-bypass procedure and is entirely unrelated to "
        "treating a functional voice-production disorder.",
        "There is no mass or malignancy described -- normal mobility and no structural "
        "lesion argue against an oncologic process, so oncologic resection has no target "
        "and is not indicated.",
        "Correct.",
        "Cochlear implantation restores hearing input for severe sensorineural hearing "
        "loss; it has no relationship to voice production or muscle tension dysphonia.",
    ],
    "v145_lar_09": [
        "Correct.",
        "Presbyphonia results from age-related tissue and muscular atrophy, not "
        "infection; indefinite antibiotics would not address the underlying bowing and "
        "glottic insufficiency.",
        "Total laryngectomy is a drastic, irreversible procedure reserved for situations "
        "like cancer or intractable aspiration; it is entirely disproportionate for "
        "age-related glottic insufficiency, which has far less invasive, effective "
        "treatment options.",
        "Presbyphonia is a treatable condition -- voice therapy, injection augmentation, "
        "or framework surgery can meaningfully improve glottic closure and voice "
        "quality, so declining any treatment ignores established, effective options.",
    ],
    "v145_lar_10": [
        "Bilateral hypoglossal paralysis would cause tongue weakness and "
        "dysarthria/dysphagia, not an isolated loss of upper vocal register with normal "
        "speaking voice and normal vocal-fold mobility; it does not match this "
        "presentation.",
        "Conductive hearing loss affects sound transmission through the outer/middle "
        "ear; it has no relationship to vocal pitch production or cricothyroid muscle "
        "function.",
        "Correct.",
        "Inferior turbinate hypertrophy affects nasal airflow and has no relationship to "
        "laryngeal pitch control or the cricothyroid muscle governed by the external "
        "branch of the superior laryngeal nerve.",
    ],
    "v145_lar_11": [
        "Correct.",
        "Ventilation must be actively managed throughout a shared-airway procedure; "
        "ignoring it while manipulating a foreign body in the airway risks hypoxia and "
        "cardiac arrest before removal is even achieved.",
        "Using forceps blindly, without direct visualization through the scope, risks "
        "pushing the object further into the airway, causing mucosal trauma, or "
        "converting a partial obstruction into a complete one.",
        "Pushing a foreign body distally can lodge it more centrally or in a more "
        "dangerous location and does not accomplish the goal of removal; it converts a "
        "retrievable object into a more complex problem.",
    ],
    "v145_lar_12": [
        "An unstable airway requires controlled, monitored management in the operating "
        "room, not an awake office procedure that could precipitate further airway "
        "compromise.",
        "Removing a sharp esophageal foreign body, especially in a child, requires "
        "controlled sedation/anesthesia and rigid or flexible endoscopy with full "
        "therapeutic capability in a monitored setting, not an unsedated office "
        "transnasal exam.",
        "Correct.",
        "TNE requires transnasal passage of an endoscope; a patient who cannot tolerate "
        "any nasal instrumentation is, by definition, not a candidate for this specific "
        "technique.",
    ],
    "v145_lar_13": [
        "Wide surgical excision of bilateral phonotraumatic nodules skips the "
        "first-line, less invasive treatment (voice therapy) that resolves most nodules, "
        "and risks unnecessary scarring when behavioral modification alone is often "
        "effective.",
        "Correct.",
        "Vocal fold nodules are benign, phonotraumatic lesions, not malignancy; "
        "chemoradiation is an oncologic treatment with no role here and would cause "
        "significant unnecessary harm.",
        "There is no airway obstruction described in this presentation; tracheostomy "
        "bypasses the airway and has no role in treating a benign phonotraumatic voice "
        "lesion.",
    ],
    "v145_lar_14": [
        "Scar tissue is a structural change in the lamina propria, not an infectious "
        "process; antibiotics have no mechanism to reverse fibrosis and do not resolve "
        "sulcus/scar.",
        "Sulcus and scar are localized changes to the vocal-fold cover and lamina "
        "propria; they do not involve or require transection of the recurrent laryngeal "
        "nerve, which governs motion, not the pliability of the mucosal layers.",
        "Hearing loss has no physiologic connection to vocal-fold vibration or "
        "dysphonia; it does not cause or contribute to the breathy voice seen with vocal "
        "fold scar.",
        "Correct.",
    ],
    "v145_lar_15": [
        "Wide arytenoidectomy is an aggressive, airway-altering procedure "
        "disproportionate to a benign, often self-limited granuloma; excision alone -- "
        "without addressing underlying trauma/reflux triggers -- frequently leads to "
        "recurrence, so this drastic approach is not appropriate as a universal first "
        "step.",
        "Granulomas frequently recur if contributing factors (reflux, phonotrauma, "
        "cough, ongoing intubation injury) are not addressed and monitored; no follow-up "
        "risks missing recurrence or a lesion that fails to resolve and needs "
        "escalation.",
        "Vocal process granuloma is a benign reactive lesion from mechanical/phonatory "
        "trauma or reflux, not a malignancy; chemotherapy has no role and would cause "
        "unnecessary harm.",
        "Correct.",
    ],
    "v145_lar_16": [
        "Correct.",
        "A fixed vocal-fold mass would suggest a structural lesion (e.g., malignancy or "
        "scar), not a movement/tremor disorder; it would not explain the rhythmic, "
        "task-independent voice breaks described here.",
        "Complete bilateral immobility describes a static motion deficit, such as "
        "bilateral vocal-fold paralysis, not a dynamic, rhythmic oscillation across "
        "laryngeal and pharyngeal subsites, which is the hallmark of tremor.",
        "Adductor spasmodic dysphonia's strained voice breaks classically diminish with "
        "whispering because whispered speech reduces vocal-fold adduction, whereas "
        "essential tremor persists across all voicing tasks including whispering; "
        "\"only whispering difficulty\" does not capture the distinguishing pattern.",
    ],
}


def apply_why_wrong_fix_laryngology_v1(data_module):
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
        print(f"why_wrong_fix_laryngology_v1: {len(missing)} ids not found: {missing}")
    return updated
