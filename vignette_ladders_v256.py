"""v25.6 — Laryngology / Voice / Swallowing deliberate ladder pass 7.

Closes the final six exact canonical Laryngology topics with complete foundation ->
application -> senior-decision ladders. The cases emphasize late radiation injury,
professional-voice tissue preservation, appropriate chronic-laryngitis escalation,
esophageal red flags and ENT/GI boundaries, office TNE selection, and safe shared-
airway tracheobronchial endoscopy.
"""
DOMAIN = "Laryngology / Voice / Swallowing"


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl,
       curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True, "_coverage_reviewed_v211": True,
    }


VIGNETTES_V256 = [
    _q("v256_lar_rad_dys_fnd", "Radiation-Associated Dysphagia", "foundation",
       "A patient treated with chemoradiation for oropharyngeal cancer 6 years ago develops slowly progressive coughing with meals, prolonged meal times, and weight loss. Surveillance has shown no known recurrence. Which mechanism is most characteristic of late radiation-associated dysphagia?",
       ["Progressive fibrosis and neuromuscular dysfunction that can reduce pharyngeal propulsion, hyolaryngeal excursion, and airway protection", "Isolated acute bacterial epiglottitis", "A recurrent laryngeal nerve injury that must have occurred during the original radiation fractions", "A normal aging change that does not require instrumental assessment"], 0,
       "Late radiation-associated dysphagia is often multifactorial. Fibrosis, reduced tissue compliance, muscle atrophy, sensory change, and late cranial neuropathy can impair bolus propulsion and airway protection years after treatment.",
       ["Correct. Late fibrosis and neuromuscular injury can progressively impair several swallowing subsystems long after oncologic treatment.", "Acute epiglottitis causes a rapidly evolving infectious syndrome rather than years-later progressive dysphagia.", "Radiation-related swallowing dysfunction is not explained by a required single RLN injury and may involve multiple muscles, nerves, and fibrotic tissue planes.", "Progressive coughing, prolonged meals, and weight loss after radiation are clinically important and warrant objective evaluation rather than attribution to normal aging."],
       "Late radiation dysphagia can worsen years after treatment; a previously safe swallow does not permanently establish future safety.",
       "Which additional symptoms or examination findings would make recurrent tumor or chondroradionecrosis a competing diagnosis rather than assuming fibrosis alone?"),
    _q("v256_lar_rad_dys_app", "Radiation-Associated Dysphagia", "application",
       "A head-and-neck cancer survivor has recurrent pneumonia and suspected late radiation dysphagia. What is the most useful next principle for evaluation?",
       ["Obtain instrumental swallowing assessment with FEES and/or modified barium swallow chosen to phenotype the suspected problem, while separately evaluating structural recurrence or stenosis when indicated", "Place a feeding tube and assume aspiration risk is thereby eliminated", "Begin repeated empiric antibiotics without defining swallowing physiology", "Perform cricopharyngeal myotomy solely because the patient previously received radiation"], 0,
       "Instrumental assessment defines whether impairment is driven by residue, reduced airway protection, timing, secretion burden, reduced excursion, or upper-esophageal opening. Structural disease such as recurrent tumor or a focal stenosis requires separate targeted evaluation when the history suggests it.",
       ["Correct. Treatment should follow an objective physiologic and structural phenotype rather than the label 'post-radiation dysphagia.'", "A feeding tube can support nutrition but does not prevent aspiration of secretions or refluxate and does not by itself define swallowing safety.", "Antibiotics may treat a pneumonia but do not diagnose or correct the swallowing mechanism causing recurrence.", "Cricopharyngeal intervention helps selected focal UES obstruction; radiation history alone is not an indication and global pharyngeal weakness may predict poor benefit."],
       "Do not equate tube feeding with aspiration prevention, and do not equate every post-radiation swallow problem with a cricopharyngeal bar.",
       "How would severe pharyngeal weakness plus only modest UES narrowing change the expected value of dilation or myotomy?", "senior_management"),
    _q("v256_lar_rad_dys_snr", "Radiation-Associated Dysphagia", "senior_decision",
       "A disease-free cancer survivor has profound late radiation-associated dysphagia despite rehabilitation, repeated aspiration pneumonias, and aspiration of secretions. A gastrostomy has stabilized nutrition but pulmonary events continue. What is the best senior-level planning principle?",
       ["Reconfirm oncologic and structural status, define residual swallow physiology and goals, then discuss aspiration-prevention options—including irreversible procedures only for intractable life-threatening aspiration after multidisciplinary counseling", "Assume gastrostomy failure means another feeding tube will eliminate secretion aspiration", "Perform empiric cricopharyngeal myotomy regardless of pharyngeal function", "Avoid discussing definitive aspiration-control surgery because preserved laryngeal speech must always outweigh pulmonary survival"], 0,
       "When aspiration is persistent and life-threatening despite optimized rehabilitation and nutrition, selected patients may need definitive aspiration-prevention surgery. These operations can sacrifice normal laryngeal voice or alter airway anatomy, so decision-making requires confirmation of disease status, mechanism, prognosis, pulmonary burden, and patient priorities.",
       ["Correct. The escalation threshold is driven by refractory pulmonary danger and patient goals after reversible contributors and anatomy are carefully reassessed.", "A different enteral tube does not stop aspiration of saliva or other nonoral material.", "Myotomy is not a universal aspiration operation and can be ineffective when the dominant problem is global pharyngeal weakness or airway-protection failure.", "Senior counseling must explicitly weigh voice against recurrent pneumonia, hospitalization, and survival rather than treating one functional domain as automatically dominant."],
       "Aspiration-prevention surgery is a goals-of-care and physiology decision, not simply the next procedure after a feeding tube.",
       "Which findings would make laryngotracheal separation or another definitive aspiration-control procedure more rational than further swallow-rehabilitation trials?", "senior_management"),

    _q("v256_lar_prof_voice_fnd", "Professional Voice", "foundation",
       "A professional singer develops persistent loss of upper range and vocal fatigue after a demanding performance week. The speaking voice is nearly normal. What is the best initial specialty evaluation?",
       ["Detailed history plus laryngeal examination with videostroboscopy to assess subtle vibratory pathology and technique-related compensation", "Empiric repeated systemic steroids without visualizing the vocal folds", "Immediate vocal-fold biopsy solely because the patient is a professional singer", "Reassurance because a near-normal speaking voice excludes meaningful pathology"], 0,
       "Professional voice users can have functionally important abnormalities that are subtle in conversational speech. Stroboscopy helps assess mucosal wave, closure, symmetry, focal lesions, edema, hemorrhage, and compensatory behavior before treatment is chosen.",
       ["Correct. High-demand voice complaints require visualization of vibration and a history tied to the patient's actual occupational tasks.", "Steroids can mask symptoms and carry adverse effects; repeated empiric use without examination can delay recognition of hemorrhage or structural lesions.", "Biopsy is not the first step for an otherwise undiagnosed performance-related complaint and can create scar if used indiscriminately.", "Loss of range and endurance can be career-limiting even when conversational voice sounds nearly normal."],
       "For a professional voice user, 'normal speaking voice' is not the same as normal occupational function.",
       "What stroboscopic finding would immediately change your advice about continued performance because of risk of further tissue injury?"),
    _q("v256_lar_prof_voice_app", "Professional Voice", "application",
       "A singer has bilateral phonotraumatic swelling without hemorrhage or a suspicious lesion. A major performance is approaching. Which management strategy best protects long-term function?",
       ["Use targeted voice conservation and specialized voice therapy, address hydration/irritants and technique, and reserve medication or surgery for a defined indication rather than treating the calendar", "Prescribe systemic steroids repeatedly so the singer can perform through worsening symptoms", "Recommend complete permanent voice rest", "Perform bilateral aggressive stripping of the superficial lamina propria"], 0,
       "Most phonotraumatic inflammatory problems are managed by reducing injurious load, optimizing technique, and treating contributing factors. Time pressure does not justify repeated empiric steroids or tissue-destructive surgery when the pathology does not require it.",
       ["Correct. The goal is to preserve the vibratory cover while restoring efficient voice use and reducing the mechanism that produced injury.", "Repeated steroids may temporarily reduce edema while encouraging continued overload and expose the patient to systemic risk; they should not substitute for diagnosis and load modification.", "Permanent complete voice rest is neither necessary nor compatible with rehabilitation; controlled voice use and therapy are usually more useful once acute injury risk is addressed.", "Stripping the vocal-fold cover risks permanent scar and is inappropriate for uncomplicated phonotraumatic edema."],
       "The performance schedule matters, but the mucosal injury and long-term career matter more.",
       "How would an acute vocal-fold hemorrhage alter activity recommendations and the urgency of follow-up?", "senior_management"),
    _q("v256_lar_prof_voice_snr", "Professional Voice", "senior_decision",
       "A professional vocalist has a small persistent unilateral benign lesion with reproducible loss of range despite optimized technique and expert voice therapy. Stroboscopy shows a focal vibratory defect, and career demands are substantial. What is the best senior-level approach?",
       ["Use shared decision-making about tissue-preserving phonomicrosurgery versus continued conservative care, with the smallest effective intervention and postoperative rehabilitation if surgery is chosen", "Remove a broad segment of normal epithelium to guarantee the lesion cannot recur", "Operate solely because the patient earns income with the voice, regardless of vibratory findings", "Refuse surgery because professional voice users should never undergo microlaryngoscopy"], 0,
       "When a persistent discrete lesion remains function-limiting despite appropriate therapy, carefully selected phonomicrosurgery may be reasonable. The operative objective is maximal preservation of epithelium and superficial lamina propria, because scar can be more disabling than the original lesion.",
       ["Correct. The threshold for surgery integrates objective vibration, symptom burden, treatment response, career needs, and the risk that intervention itself can injure the vibratory cover.", "Broad tissue removal increases scar and stiffness and violates phonomicrosurgical principles.", "Occupation affects the functional threshold for intervention but does not replace diagnosis or justify unnecessary surgery.", "Professional voice users can benefit from appropriately selected tissue-preserving surgery; an absolute prohibition is not evidence-based."],
       "In elite voice, the operation succeeds only if the treatment does less harm to the vibratory cover than the lesion itself.",
       "How would diffuse stiffness rather than a discrete lesion change your confidence that excision will improve the voice?", "OR_prep"),

    _q("v256_lar_laryngitis_fnd", "Acute / Chronic Laryngopharyngitis", "foundation",
       "An otherwise healthy adult develops hoarseness after an upper-respiratory infection, with mild sore throat, no stridor, no respiratory distress, and no concerning neck findings. What is the most appropriate initial management?",
       ["Supportive care and voice-load reduction; routine antibiotics are not indicated for uncomplicated acute viral laryngitis", "Immediate prolonged broad-spectrum antibiotics for every case of hoarseness", "Urgent tracheostomy despite a stable airway", "Microlaryngoscopic biopsy during the first uncomplicated viral week"], 0,
       "Most acute laryngitis in immunocompetent adults is viral or irritative and self-limited. Treatment is supportive unless the history or examination suggests airway compromise, bacterial supraglottitis, fungal disease, trauma, or another specific cause.",
       ["Correct. Uncomplicated acute viral laryngitis is generally managed conservatively while monitoring for features that suggest a different diagnosis.", "Routine antibiotics do not improve a typical viral syndrome and expose the patient to unnecessary adverse effects and resistance.", "A stable patient without obstruction does not need a surgical airway.", "Biopsy is not indicated for a short, uncomplicated infectious presentation without a lesion or red flag."],
       "Hoarseness is a symptom; acute viral laryngitis is a diagnosis supported by the whole clinical context and absence of airway red flags.",
       "Which airway symptoms would convert this from routine outpatient laryngitis into an urgent laryngeal evaluation?"),
    _q("v256_lar_laryngitis_app", "Acute / Chronic Laryngopharyngitis", "application",
       "A smoker has 6 weeks of persistent dysphonia repeatedly treated as 'chronic laryngitis' with empiric antibiotics and reflux medication, but the larynx has never been visualized. What is the best next step?",
       ["Perform laryngeal visualization rather than continuing empiric therapy, with stroboscopy or biopsy added according to the findings", "Continue antibiotics indefinitely because chronic hoarseness is usually bacterial", "Add repeated systemic steroids without examination", "Wait a full year because chronic laryngeal symptoms rarely represent structural disease"], 0,
       "Persistent dysphonia requires visualization to identify structural lesions, malignancy, fungal disease, phonotrauma, paresis, and other causes. Tobacco exposure increases the importance of examining the larynx rather than perpetuating an empiric label.",
       ["Correct. Visualization is the decisive next step when symptoms persist, especially with a cancer risk factor.", "Chronic dysphonia is not usually a bacterial infection and indefinite antibiotics can delay diagnosis.", "Steroids without a defined indication can mask symptoms and add harm without establishing the diagnosis.", "Long delay is inappropriate when persistent dysphonia and smoking raise concern for a structural lesion or malignancy."],
       "Do not let 'laryngitis' become a chronic placeholder diagnosis when the vocal folds have never been seen.",
       "What endoscopic features would lower your threshold for direct laryngoscopy and biopsy rather than another empiric medical trial?", "senior_management"),
    _q("v256_lar_laryngitis_snr", "Acute / Chronic Laryngopharyngitis", "senior_decision",
       "A patient treated for presumed chronic laryngopharyngitis now reports unilateral throat pain, progressive odynophagia, hemoptysis, and weight loss. Flexible examination shows an irregular unilateral supraglottic lesion. What is the best management principle?",
       ["Abandon the nonspecific inflammatory label and perform oncologic evaluation with appropriate imaging and tissue diagnosis while protecting the airway as needed", "Escalate empiric proton-pump inhibitor therapy and reassess in 6 months", "Treat with repeated oral antibiotics without biopsy", "Assume the lesion is benign because symptoms began as hoarseness"], 0,
       "Progressive focal symptoms and an irregular unilateral lesion require evaluation for malignancy or another structural process. A prior working diagnosis of inflammation must not delay tissue diagnosis or airway planning when the phenotype changes.",
       ["Correct. Red flags and focal abnormality supersede the previous empiric diagnosis and require definitive structural evaluation.", "Reflux therapy is not an adequate response to a suspicious lesion with systemic and bleeding symptoms.", "Antibiotics do not establish the diagnosis and can delay appropriate oncologic care.", "The evolution of symptoms and the lesion itself are more important than the initial nonspecific presentation."],
       "Senior clinical judgment includes knowing when a common diagnosis no longer fits and must be discarded.",
       "How would impending airway compromise change the sequence of imaging, biopsy, and airway control?", "senior_management"),

    _q("v256_lar_esoph_fnd", "Esophageal Disease for the Otolaryngologist", "foundation",
       "A patient says food 'sticks' several seconds after the swallow, especially solid meat and bread, while liquids initially pass more easily. There is no coughing at swallow initiation. Which localization is most likely?",
       ["Esophageal dysphagia, which warrants evaluation for a structural or motility disorder rather than assuming an oropharyngeal problem", "Isolated oral-phase dysphagia", "Pure vocal-fold paralysis", "Normal swallowing because the sensation is below the neck"], 0,
       "Difficulty after swallow initiation, particularly progressive solid-food sticking, localizes more strongly to the esophagus and raises concern for ring, stricture, eosinophilic disease, neoplasm, or other obstruction. Oropharyngeal dysphagia more often causes difficulty initiating, coughing, choking, or nasal regurgitation.",
       ["Correct. Timing and symptom pattern help separate esophageal transit symptoms from oropharyngeal airway-protection problems.", "Oral-phase dysfunction usually causes impaired bolus preparation or initiation rather than delayed solid-food sticking.", "Vocal-fold paralysis can impair airway protection but does not typically produce isolated delayed esophageal solid-food impaction symptoms.", "A lower perceived location does not make the symptom normal; esophageal pathology may be clinically important and sometimes urgent."],
       "Ask when the problem occurs—before, during, or after swallow initiation—and whether solids, liquids, or both are affected.",
       "How would dysphagia to solids and liquids from the outset shift the differential toward a motility disorder?"),
    _q("v256_lar_esoph_app", "Esophageal Disease for the Otolaryngologist", "application",
       "A young adult has recurrent solid-food impactions and atopy. Endoscopy previously looked nearly normal, but no biopsies were obtained. Which diagnosis and next principle are most important?",
       ["Eosinophilic esophagitis remains possible and requires esophageal biopsy for diagnosis even when mucosa is not dramatically abnormal", "Normal-appearing mucosa excludes eosinophilic esophagitis", "The pattern proves laryngeal reflux and needs no esophageal workup", "Recurrent food impaction is best managed with voice therapy"], 0,
       "Eosinophilic esophagitis commonly presents with solid-food dysphagia and impaction, especially in patients with atopy. Endoscopic appearance can be subtle or even normal, so diagnosis depends on appropriately obtained biopsies in the right clinical context.",
       ["Correct. Failure to biopsy can miss eosinophilic esophagitis despite a suggestive history.", "A visually normal esophagus does not reliably exclude eosinophilic inflammation.", "Recurrent food impaction is an esophageal red flag and should not be reduced to a reflux label without appropriate evaluation.", "Voice therapy treats selected voice and laryngeal behaviors, not esophageal inflammatory disease causing food impaction."],
       "For EoE, 'looked normal' is not the same as 'biopsies were negative.'",
       "Why is repeated dilation without treating active inflammatory disease an incomplete long-term strategy in a patient with fibrostenotic EoE?", "senior_management"),
    _q("v256_lar_esoph_snr", "Esophageal Disease for the Otolaryngologist", "senior_decision",
       "An adult presents unable to swallow saliva after a steak became impacted. The patient is drooling but currently oxygenating and ventilating adequately. What is the best senior-level management principle?",
       ["Treat this as a complete esophageal obstruction requiring urgent endoscopic removal with airway-aware planning rather than outpatient observation", "Send the patient home to wait for spontaneous passage because oxygenation is normal", "Force additional solid food or effervescent material despite complete obstruction", "Schedule elective voice therapy because drooling indicates oropharyngeal weakness"], 0,
       "Inability to handle secretions after food impaction indicates complete esophageal obstruction and requires urgent endoscopic management. Airway protection, location, suspected sharp components, duration, and perforation risk inform whether GI and/or ENT operative expertise is needed.",
       ["Correct. Complete obstruction is time-sensitive even when the patient is not yet hypoxemic.", "Persistent complete obstruction risks aspiration, pressure injury, and perforation; outpatient waiting is unsafe.", "Uncontrolled attempts to push the bolus distally can worsen obstruction or injury and are inappropriate in complete impaction.", "Drooling here reflects inability to pass secretions beyond an obstruction, not an indication for behavioral voice therapy."],
       "A patient can have an esophageal emergency with a temporarily stable airway; inability to handle secretions is the key escalation sign.",
       "How would suspected sharp bone, subcutaneous emphysema, or severe chest pain change the urgency and imaging/operative plan?", "overnight_call"),

    _q("v256_lar_tne_fnd", "Transnasal Esophagoscopy", "foundation",
       "Which statement best describes transnasal esophagoscopy (TNE) in appropriately selected patients?",
       ["It permits office-based flexible visualization of the pharynx and esophagus, often without general anesthesia, and can allow targeted biopsy while preserving spontaneous ventilation", "It is a rigid operation that always requires general anesthesia", "It replaces every indication for sedated EGD or operative rigid esophagoscopy", "It cannot visualize the cervical esophagus"], 0,
       "TNE uses a slim flexible scope passed through the nose, commonly in an awake patient with topical anesthesia. It can assess selected dysphagia, reflux-related questions, surveillance findings, and mucosal lesions, but it does not replace higher-acuity or therapeutic endoscopy when those are needed.",
       ["Correct. The major advantages are office access, avoidance of routine general anesthesia, and direct esophageal mucosal visualization in selected patients.", "TNE is flexible and is commonly performed without general anesthesia.", "Therapeutic needs, unstable patients, some foreign bodies, complex strictures, and other high-risk problems may require sedated or operative endoscopy instead.", "The cervical esophagus is part of the examination and is particularly relevant to otolaryngologic practice."],
       "Know what TNE adds—direct mucosal visualization—and what it does not replace: all therapeutic or high-risk esophageal endoscopy.",
       "Which patient factors would make office TNE technically difficult or less safe despite an otherwise reasonable indication?"),
    _q("v256_lar_tne_app", "Transnasal Esophagoscopy", "application",
       "During office TNE for persistent dysphagia, a focal irregular esophageal mucosal lesion is identified. What is the most appropriate next principle?",
       ["Obtain an appropriately targeted biopsy if safe and within the procedure's capabilities, then route subsequent staging or therapeutic endoscopy according to pathology and lesion features", "A visually abnormal lesion needs no tissue diagnosis", "Ablate the lesion blindly without histology", "Ignore the finding because office endoscopy cannot reveal meaningful pathology"], 0,
       "TNE can permit biopsy of selected mucosal abnormalities. Suspicious findings should trigger tissue diagnosis and an appropriate downstream pathway rather than either dismissal or unplanned definitive therapy in an office setting.",
       ["Correct. TNE is useful because a diagnostic finding can be converted into a structured pathology and referral plan.", "Appearance alone often cannot establish histology, particularly for dysplasia or malignancy.", "Blind ablation risks undertreating malignancy, obscuring pathology, and causing avoidable injury.", "Office TNE can identify clinically important esophageal lesions and should be acted upon when abnormal."],
       "The value of office endoscopy is not just seeing an abnormality; it is knowing when the finding changes the diagnostic and treatment pathway.",
       "What lesion characteristics would make you stop at diagnosis and refer for sedated therapeutic endoscopy rather than attempting further office intervention?", "senior_management"),
    _q("v256_lar_tne_snr", "Transnasal Esophagoscopy", "senior_decision",
       "A patient with severe chest pain, fever, tachycardia, and subcutaneous emphysema after recent esophageal instrumentation is referred for office TNE to 'look for a tear.' What is the best senior-level response?",
       ["Do not use routine office TNE as the next step; treat suspected esophageal perforation as an emergency requiring resuscitation, appropriate cross-sectional/contrast evaluation, antibiotics, and urgent multidisciplinary surgical/endoscopic planning", "Perform office TNE immediately because any suspected perforation should be probed directly", "Give reassurance if the patient can still speak", "Delay evaluation until an elective clinic slot is available"], 0,
       "Systemic toxicity, severe pain, and subcutaneous emphysema after instrumentation are classic perforation red flags. Further routine office instrumentation can worsen contamination or delay definitive management; the patient needs emergency-level imaging, resuscitation, antimicrobial therapy, and coordinated surgical/GI care.",
       ["Correct. Choosing not to perform an available office procedure is part of safe endoscopy when the physiology demands emergency management.", "Routine probing can extend injury or contamination and is not the first diagnostic maneuver in an unstable perforation syndrome.", "Ability to phonate does not exclude mediastinal contamination or evolving sepsis.", "Delay can allow rapid progression to mediastinitis and shock."],
       "A key endoscopic skill is recognizing when not to scope in clinic.",
       "How would cervical versus thoracic perforation location and contained versus free leak influence the definitive management discussion?", "overnight_call"),

    _q("v256_lar_tb_end_fnd", "Tracheobronchial Endoscopy Principles", "foundation",
       "Which statement best captures the complementary roles of flexible and rigid tracheobronchial endoscopy?",
       ["Flexible bronchoscopy is excellent for diagnostic inspection and distal airway mapping, whereas rigid bronchoscopy provides a large working channel, airway control, ventilation options, and powerful therapeutic access when significant obstruction or foreign-body extraction is expected", "Flexible and rigid bronchoscopy are interchangeable in every airway emergency", "Rigid bronchoscopy is used only for nasal disease", "Flexible bronchoscopy always provides better control of a critically obstructed central airway"], 0,
       "Flexible and rigid bronchoscopy are complementary. Flexible scopes provide excellent reach and diagnostic visualization; rigid bronchoscopy offers superior working-channel capacity, suction, ventilation, and mechanical control for many central-airway therapeutic problems.",
       ["Correct. Procedure selection should reflect whether the primary task is diagnosis/mapping or major airway intervention and control.", "The two techniques differ materially in working channel, ventilation, instrumentation, and rescue capacity.", "Rigid bronchoscopy is an airway procedure, not a nasal operation.", "A small flexible scope may be valuable diagnostically but can be inadequate as the sole platform for a critically obstructed central airway requiring major intervention."],
       "Choose the scope for the airway problem you expect to encounter—and for the rescue you may need, not just the image you want.",
       "What airway lesion or foreign-body scenario would make you want rigid capability immediately available even if flexible inspection is planned first?"),
    _q("v256_lar_tb_end_app", "Tracheobronchial Endoscopy Principles", "application",
       "A child has a witnessed choking event followed by persistent unilateral wheeze and hyperinflation on chest imaging. The object is likely removable but could shift during induction. What is the best procedural principle?",
       ["Plan controlled operative airway endoscopy with a team prepared for rigid bronchoscopy, ventilation, extraction, and distal reinspection after removal", "Schedule routine outpatient flexible laryngoscopy only", "Give bronchodilators for several weeks before deciding whether an aspirated object exists", "Attempt blind extraction at the bedside"], 0,
       "A convincing pediatric airway foreign body requires prompt endoscopic evaluation and a controlled extraction plan. Rigid bronchoscopy remains a key therapeutic platform because it allows ventilation, robust instrumentation, and management of a moving obstructing object; the distal airway should be inspected after removal for additional material or injury.",
       ["Correct. The procedure is an airway operation, so extraction strategy, ventilation, backup instruments, and post-removal inspection should be planned before induction.", "Flexible laryngoscopy does not adequately inspect or treat the lower tracheobronchial tree in this scenario.", "Delaying a convincing retained foreign body risks pneumonia, granulation, migration, and acute obstruction.", "Blind extraction can push the object distally, traumatize the airway, or precipitate complete obstruction."],
       "Foreign-body bronchoscopy is won before the scope enters: know the object, location, instruments, ventilation strategy, and rescue plan.",
       "How would a sharp object, friable organic material, or object lodged at the carina change instrument and extraction planning?", "OR_prep"),
    _q("v256_lar_tb_end_snr", "Tracheobronchial Endoscopy Principles", "senior_decision",
       "An adult has severe fixed central-airway narrowing from an intraluminal tumor and becomes markedly dyspneic when supine. Biopsy and possible debulking are being considered. What is the safest senior-level planning principle?",
       ["Treat induction as a high-risk shared-airway event: define the narrowest lumen and distal airway, coordinate anesthesia and interventional airway expertise, preserve a rescue strategy, and avoid committing to loss of spontaneous ventilation until the team can manage complete obstruction", "Perform routine induction and paralysis before the airway team or rigid equipment is available", "Obtain a large biopsy first and decide how to ventilate afterward", "Assume an endotracheal tube can always be passed beyond any central-airway tumor"], 0,
       "Critical central-airway obstruction can deteriorate catastrophically with supine positioning, sedation, or loss of spontaneous ventilation. Senior planning requires review of imaging and endoscopy, a shared ventilation/intervention strategy, immediate rigid therapeutic capability when appropriate, and escalation to advanced rescue support in selected extreme cases.",
       ["Correct. The airway and rescue plan must precede biopsy or debulking because induction itself can convert partial obstruction into complete obstruction.", "Routine paralysis without a rescue-capable team can remove the patient's remaining airway tone and ventilation reserve.", "Biopsy can provoke bleeding, edema, or obstruction; airway control cannot be deferred until afterward.", "Tumor location and lumen may make passage impossible or dangerous, so an endotracheal tube is not a universal rescue."],
       "In critical central-airway disease, the most dangerous step may be induction—not the tumor debulking itself.",
       "Which imaging or physiologic findings would make you discuss extracorporeal rescue capability before entering the operating room?", "senior_management"),
]


def apply_learning_ladders_v256(challenges, concept_id_fn):
    """Append only missing v25.6 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V256:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["choices"] = list(source.get("choices") or [])
        q["why_wrong"] = list(source.get("why_wrong") or [])
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
