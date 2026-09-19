"""Replace generic v138 vignette distractor explanations without overwriting edits."""

GENERIC_MARKER_V138 = 'Compare this option with the decision rule and anatomy described in the explanation.'

WHY_WRONG_FIXES_V138 = {
    'v138_hn_01': [
        'Correct.',
        'Observation is inappropriate for a biopsy-proven malignancy with ill-defined borders in a cosmetically critical subunit; delay allows the tumor to enlarge and increases the eventual tissue sacrifice needed for clearance.',
        'Empiric antibiotics treat infection, not neoplasm; a BCC is not an infectious process and will not respond to or be controlled by antimicrobial therapy.',
        'Neck dissection addresses regional lymphatic metastasis, but BCC has an exceedingly low rate of nodal spread, so treatment should target complete excision of the primary skin lesion, not the neck.',
    ],
    'v138_hn_03': [
        'Open biopsy of a hypervascular carotid body tumor risks brisk, difficult-to-control hemorrhage and potential injury to the carotid vessels; diagnosis should rest on imaging (CTA/MRA showing the classic vessel splaying) rather than direct incisional biopsy.',
        "A well-defined, slow-growing mass splaying the internal and external carotid arteries (the 'lyre sign') is the classic appearance of a paraganglioma, not metastatic SCC, which typically presents as a rounded/matted nodal mass without vessel splaying and usually has an identifiable mucosal primary.",
        'Incision and drainage is a technique for fluid collections/abscesses; this is a solid hypervascular tumor, and incising it could precipitate uncontrolled bleeding rather than draining anything.',
        'Correct.',
    ],
    'v138_hn_04': [
        'Hypoglossal nerve (CN XII) injury causes tongue deviation toward the affected side and dysarthria, not shoulder weakness or scapular winging.',
        'Correct.',
        'The lingual nerve carries general sensation to the anterior two-thirds of the tongue and taste fibers via the chorda tympani; injury causes tongue numbness and taste change, not shoulder or scapular dysfunction.',
        'Recurrent laryngeal nerve injury produces vocal fold paralysis with hoarseness and possible aspiration, not shoulder abduction weakness or scapular winging.',
    ],
    'v138_hn_05': [
        'Clark level, based on the anatomic layer of dermal invasion, has been largely abandoned in staging because it correlates far less reliably with prognosis than Breslow thickness.',
        'Correct.',
        'Tumor color/pigmentation does not correlate with depth of invasion, T category, or metastatic risk and is not part of AJCC melanoma staging criteria.',
        'Serum TSH reflects thyroid function and has no role in melanoma staging or sentinel-node decision-making.',
    ],
    'v138_hn_06': [
        'Segmental mandibulectomy is reserved for cases with gross cortical or medullary bone invasion; performing it routinely without proven invasion causes needless functional and cosmetic morbidity when a marginal resection would achieve adequate margins.',
        'Correct.',
        'Floor-of-mouth SCC carries a well-established risk of occult nodal metastasis, including contralateral spread near the midline, so elective neck management based on depth of invasion and other risk factors is routinely indicated, not omitted.',
        'Floor-of-mouth SCC is an oral cavity primary with its own staging system and lymphatic drainage pattern (primarily levels I-III); it should not be staged or treated using laryngeal cancer protocols.',
    ],
    'v138_hn_07': [
        'Correct.',
        'Venous congestion can progress to thrombosis within hours; delaying evaluation until morning risks flap loss, since salvage rates fall sharply the longer the pedicle remains compromised.',
        'Ice causes vasoconstriction, which would further impair perfusion of an already congested flap and is contraindicated in flap monitoring.',
        'Arterial insufficiency classically produces a pale, cool flap with no bleeding or slow, thin, bright-red bleeding on pinprick; a tense, blue flap with brisk dark bleeding is the textbook picture of venous outflow obstruction, not arterial thrombosis.',
    ],
    'v138_hn_09': [
        'Correct.',
        'Stopping all follow-up after one negative scan ignores that recurrence risk persists for years and that a single imaging study cannot capture emerging second primaries or late functional/endocrine effects.',
        'Monthly PET/CT is not evidence-based, exposes the patient to unnecessary cumulative radiation and cost, and carries a high false-positive rate driven by post-treatment inflammatory change.',
        'New pulmonary symptoms in a tobacco-associated HNSCC survivor raise concern for a second primary lung malignancy or metastatic disease and warrant prompt evaluation, not dismissal.',
    ],
    'v138_hn_10': [
        'Attributing every late symptom to recurrent cancer without evaluation risks missing treatable non-oncologic causes, such as hypothyroidism, fibrosis, and xerostomia, and could prompt unnecessary invasive workup.',
        'Late radiation effects are frequently modifiable -- thyroid hormone replacement, swallowing therapy, saliva substitutes, and fibrosis-directed rehabilitation are established interventions -- so asserting no intervention is possible is inaccurate.',
        'Total laryngectomy is a drastic, irreversible step reserved for a nonfunctional, unsafe larynx after rehabilitation has failed; it is not an automatic response to radiation-related symptoms in a patient with an intact, functioning larynx.',
        'Correct.',
    ],
    'v138_hn_12': [
        'Merkel cell carcinoma is an aggressive neuroendocrine carcinoma with substantial regional and distant metastatic potential, unlike a benign cyst, which requires no oncologic workup or treatment.',
        'Merkel cell carcinoma has a high rate of occult nodal metastasis even in a clinically N0 neck, making sentinel lymph node biopsy or other nodal staging a standard part of workup, not something that can be skipped.',
        'Correct.',
        'This is a malignant neuroendocrine tumor, not an infectious process, and will not respond to antibiotics; delaying definitive oncologic treatment allows disease progression and metastasis.',
    ],
    'v138_hn_13': [
        'Correct.',
        'FNA cytology disrupts nodal architecture and generally cannot provide the immunophenotyping and architectural pattern needed for complete lymphoma subclassification, even though it may suggest the diagnosis.',
        'Lymphoma is a systemic disease treated with chemotherapy, immunotherapy, or radiation; an oncologic neck dissection has no therapeutic role and would add morbidity without benefit.',
        'Radiating before tissue diagnosis eliminates the chance to obtain undistorted tissue for classification and risks treating with the wrong modality before the specific lymphoma subtype and stage are known.',
    ],
    'v138_hn_14': [
        'Oral tongue SCC drains predictably to levels I-III (and beyond with advanced disease) via a rich lymphatic network, so the claim that it never drains to cervical nodes is factually incorrect.',
        'Correct.',
        'Elective neck management decisions are based primarily on depth of invasion and other tumor-specific risk factors, not on patient age alone.',
        'Sentinel lymph node biopsy has been validated as an alternative to elective neck dissection in early oral cavity cancer, so sentinel nodes clearly exist and are used clinically in this setting.',
    ],
    'v138_hn_15': [
        'Surveillance alone ignores an immediately life-threatening functional problem -- recurrent aspiration pneumonia -- since anatomic presence of the larynx does not equal a safe, functioning larynx.',
        'Correct.',
        'Repeated antibiotics treat individual pneumonia episodes but do not address the underlying anatomic/functional cause of chronic aspiration and will not prevent recurrence.',
        'Surgical options for chronic aspiration, such as laryngeal closure procedures or total laryngectomy, exist independent of cancer recurrence and are indicated whenever the larynx is unsafe, regardless of oncologic status.',
    ],
    'v138_hn_16': [
        'Bilateral cricoarytenoid joint fixation impairs vocal fold mobility and is generally a contraindication to conservation laryngeal surgery because it threatens airway and swallowing outcomes.',
        'Extensive subglottic invasion is a relative contraindication to open partial laryngectomy because the subglottis is difficult to access and margin control there is limited.',
        'Correct.',
        'Inability to protect the airway is a contraindication to conservation surgery, not a prerequisite, since a partial laryngectomy still requires enough residual laryngeal function to prevent chronic aspiration.',
    ],
    'v138_hn_17': [
        "Offering maximal surgery irrespective of the patient's goals, frailty, and expected benefit disregards shared decision-making and can inflict treatment burden that does not align with a palliative-intent situation.",
        'Avoiding prognosis discussion denies the patient the information needed to make informed, values-based decisions about remaining time and treatment intensity.',
        'Stopping all symptom treatment abandons palliation of bleeding, pain, and dysphagia, which remain treatable even when cure is no longer achievable.',
        'Correct.',
    ],
    'v138_hn_19': [
        'Cisplatin increases mucosal and hematologic toxicity rather than preventing mucositis; it does not protect the mucosa from radiation-induced injury.',
        'Correct.',
        'Concurrent chemotherapy does not substitute for accurate pretreatment staging, which remains essential for treatment planning regardless of the systemic agent used.',
        'Cisplatin is ototoxic and nephrotoxic, not otoprotective, and can contribute to sensorineural hearing loss -- the opposite of protecting hearing.',
    ],
    'v138_hn_20': [
        'A skin graft provides only thin soft-tissue coverage and cannot restore bony continuity of a segmental mandibular defect, leaving facial contour and dental rehabilitation compromised.',
        'Correct.',
        'Local mucosal advancement lacks the bulk, vascularity, and reach to close a large composite defect and provides no bone replacement at all.',
        "Leaving a segmental mandibular defect unreconstructed results in an 'Andy Gump' deformity with severe functional and cosmetic morbidity, oral incompetence, and impaired mastication and speech.",
    ],
    'v138_hn_21': [
        'Correct.',
        'Unresectable disease by definition cannot be adequately addressed with primary-site surgery; forcing resection would not achieve clear margins and would add morbidity without oncologic benefit.',
        'Radioactive iodine treats iodine-avid thyroid malignancies, not squamous cell carcinoma, which does not concentrate iodine and would not respond to RAI.',
        'Observation alone in symptomatic unresectable/recurrent disease forgoes available options -- immunotherapy, chemotherapy, or local palliation -- that can improve survival or quality of life in appropriately selected patients.',
    ],
    'v138_hn_22': [
        'Correct.',
        'Neoadjuvant, concurrent, and adjuvant therapy have distinct timing, goals, and biologic rationale (cytoreduction/organ-preservation testing versus radiosensitization versus eradicating micrometastatic disease) and are not interchangeable labels.',
        "Concurrent chemotherapy, particularly cisplatin, potentiates radiation's cytotoxic effect through radiosensitization, so systemic therapy clearly does affect radiation efficacy and toxicity.",
        'By definition, adjuvant therapy is given after primary local therapy such as surgery to eradicate residual microscopic disease, not before it.',
    ],
    'v138_hn_23': [
        'Whispering or other non-pulmonary alaryngeal speech alternatives produce very limited, effortful, low-volume communication and are not considered fluent voice rehabilitation options.',
        'Cochlear implantation restores hearing in sensorineural deafness and has no role in voice production after laryngectomy.',
        'Nasal valve surgery addresses nasal airflow obstruction and has no relationship to voice restoration after laryngeal removal.',
        'Correct.',
    ],
    'v138_hn_24': [
        'Correct.',
        'Tonsil SCC arises from the oropharynx, not the oral cavity, and should be staged using oropharyngeal, HPV-stratified staging criteria rather than oral cavity staging.',
        'A clinically apparent nodal metastasis, such as this palpable mobile level II node, requires neck treatment as part of the oncologic plan; it cannot simply be omitted.',
        'HPV status is highly prognostic in oropharyngeal SCC, correlating with markedly better treatment response and survival, which is why AJCC 8th edition created a separate p16-based staging system.',
    ],
    'v138_hn_25': [
        'After total laryngectomy the airway is surgically separated from the nasal and oral passages, so normal nasal breathing is lost; the patient breathes solely through the neck stoma.',
        'Because the airway and swallowing tract are permanently separated, food or liquid can no longer enter the trachea through the native route, so laryngectomy actually eliminates the risk of aspiration through the larynx.',
        'Correct.',
        'Removal of the larynx, the organ of phonation, eliminates the native laryngeal voice source; any subsequent voice must come from an alaryngeal method such as TEP, electrolarynx, or esophageal speech.',
    ],
    'v138_hn_26': [
        'Tracheal resection length is limited by the ability to achieve a tension-free anastomosis, even with release maneuvers; attempting unlimited-length resection risks anastomotic dehiscence and restenosis.',
        'Correct.',
        'The recurrent laryngeal nerves run in the tracheoesophageal grooves immediately adjacent to the trachea and must be carefully identified and preserved to avoid bilateral vocal fold paralysis and airway compromise.',
        'A primary tracheal adenoid cystic carcinoma is an airway malignancy, anatomically and biologically distinct from thyroid cancer, and should not be managed using thyroid cancer protocols.',
    ],
    'v138_hn_27': [
        'Correct.',
        'TLM still causes mechanical/thermal injury to the vibratory mucosa, and voice outcomes depend on the depth and extent of resection; some voice change is expected, particularly with deeper cordectomies.',
        'Adequate transoral surgical exposure of the glottis is a prerequisite for TLM; poor exposure precludes safe laser resection with clear margins.',
        'TLM is appropriate for selected early (T1-T2, and select T3) glottic tumors with adequate exposure; advanced T4 disease with cartilage invasion or extralaryngeal extension is generally not amenable to transoral laser resection.',
    ],
    'v138_hn_28': [
        'Checkpoint inhibitors are immunomodulatory antibodies, not a form of ionizing radiation, and do not work by directly ablating tumor tissue.',
        'Checkpoint inhibitors are designed to unleash, not suppress, antitumor T-cell activity; global T-cell suppression would be the opposite of their intended mechanism and would worsen cancer control.',
        'Radioactive iodine is used for iodine-avid differentiated thyroid carcinoma and has no relationship to immune checkpoint biology or HNSCC treatment.',
        'Correct.',
    ],
    'v138_lar_01': [
        'Immediate microlaryngoscopic biopsy is invasive and unwarranted for a brief, self-limited post-viral dysphonia without red flags such as hemoptysis, a visible mass, or hoarseness persisting beyond 2-3 weeks.',
        'Correct.',
        'Empiric antifungals are reserved for laryngeal candidiasis, typically seen with inhaled corticosteroid use or immunosuppression; there is no indication of fungal infection here.',
        'Months of total voice rest is excessive for a brief post-viral laryngitis and offers no proven benefit over relative voice conservation for this severity and duration.',
    ],
    'v138_lar_02': [
        'Correct.',
        'Posterior cordotomy widens the airway by excising posterior vocal fold/cartilage tissue for bilateral vocal fold immobility; it would worsen, not improve, glottic closure in a unilateral paralysis.',
        'Botulinum toxin weakens muscle activity and is used for hyperfunctional conditions like spasmodic dysphonia; it does not medialize a paralyzed fold or correct a posterior glottic gap.',
        'Adenoidectomy addresses nasopharyngeal lymphoid tissue and has no relationship to glottic closure or vocal fold position.',
    ],
    'v138_lar_03': [
        'Nasal airflow is unrelated to the goal of aspiration-prevention surgery, which targets separation of the lower airway from the swallowing tract, not the nasal passage.',
        'Correct.',
        'Cochlear hearing restoration addresses sensorineural hearing loss and has no bearing on aspiration or airway protection.',
        'Reflux treatment alone does not correct the underlying structural or neurologic inability to protect the airway and would not resolve aspiration that has already failed maximal rehabilitation.',
    ],
    'v138_lar_04': [
        'Correct.',
        'Indefinite antibiotics are inappropriate for a non-infectious neurogenic cough syndrome and would not address underlying laryngeal hypersensitivity.',
        'Tracheostomy bypasses the larynx for airway obstruction or ventilatory need; it has no role in treating a hypersensitive cough reflex and is not justified for this indication.',
        'Ignoring identified triggers such as talking and odors misses an opportunity for behavioral desensitization, a mainstay of managing laryngeal hypersensitivity syndromes.',
    ],
    'v138_lar_05': [
        'Reassurance without workup ignores alarm features -- progressive dysphagia and weight loss -- that are classic warning signs of an obstructing esophageal lesion, including malignancy.',
        'Correct.',
        'Voice therapy addresses phonatory function and has no role in evaluating structural esophageal obstruction causing solid-food dysphagia and weight loss.',
        'BPPV is a vestibular/balance disorder unrelated to swallowing function and would not explain progressive solid-food dysphagia.',
    ],
    'v138_lar_06': [
        "This describes a limitation of FEES, not an advantage over MBS -- FEES actually has a brief 'white-out' at the moment of the pharyngeal swallow, whereas fluoroscopy on MBS continues to visualize bolus flow through that instant.",
        'FEES only visualizes the pharynx and larynx endoscopically; it cannot directly assess the esophagus, so it does not provide complete esophageal evaluation.',
        'FEES is an endoscopic tool for assessing swallowing function, not a stroboscopic instrument, and does not measure vocal fold vibratory characteristics.',
        'Correct.',
    ],
    'v138_lar_07': [
        'Permanent bilateral cordotomy is an airway-widening procedure used for bilateral vocal fold immobility; applying it to unilateral paralysis with breathy voice and aspiration would worsen glottic closure, not improve it.',
        'Correct.',
        'Total laryngectomy is an irreversible, drastic procedure entirely disproportionate to a single unilateral paralysis with uncertain but still possible nerve recovery.',
        'Withholding treatment for up to 12 months forces the patient to tolerate ongoing aspiration risk and poor voice when a temporary injection can safely bridge the recovery period.',
    ],
    'v138_lar_08': [
        'The quadrangular membrane is the superior fibroelastic membrane, extending between the epiglottis and arytenoid to form the aryepiglottic fold above and the vestibular (false) fold below; it does not give rise to the vocal ligament.',
        'Correct.',
        'The thyrohyoid membrane connects the thyroid cartilage to the hyoid bone superiorly and has no relationship to the vocal ligament.',
        'The cricotracheal ligament connects the cricoid cartilage to the first tracheal ring and is unrelated to the fibroelastic membrane that forms the vocal ligament.',
    ],
    'v138_lar_09': [
        'Leukoplakia can represent anything from benign keratosis to carcinoma in situ or invasive cancer, so assuming benignity without tissue diagnosis risks missing malignancy, especially with irregular vascularity and impaired mucosal wave suggesting possible invasion.',
        'Antibiotics have no role in leukoplakia, which is not an infectious process, and would only delay the tissue diagnosis this presentation requires.',
        'Deferring follow-up ignores concerning features -- impaired mucosal wave and abnormal vascularity -- that raise suspicion for dysplasia or malignancy requiring prompt evaluation.',
        'Correct.',
    ],
    'v138_lar_10': [
        'Posterior cordotomy widens the glottis for bilateral immobility and would worsen closure in a patient with unilateral paralysis and glottic insufficiency, the opposite of the desired effect here.',
        'Tracheostomy addresses airway obstruction, not glottic insufficiency from unilateral paralysis, and would not improve voice or aspiration caused by an incompetent glottis.',
        'Vocal fold stripping removes mucosa and is a treatment for surface lesions like leukoplakia, not paralysis; bilateral stripping would be inappropriate here and would worsen both voice and glottic closure.',
        'Correct.',
    ],
    'v138_lar_11': [
        'Correct.',
        'Increasing inspired oxygen to 100% during laser use raises the risk of an airway fire, since combustion risk rises sharply with higher FiO2; low inspired oxygen should be used when clinically feasible instead.',
        'Flammable materials such as dry, non-laser-safe pledgets are a direct fire hazard during laser use and must be avoided, not used.',
        'Dental protection prevents injury to the teeth and gums from the rigid laryngoscope during suspension and must be addressed before proceeding, not ignored.',
    ],
    'v138_lar_12': [
        'Correct.',
        'MBS is a fluoroscopic functional study, not a tissue-sampling procedure, and cannot obtain mucosal biopsies.',
        'Prolonged esophageal pH monitoring is a separate study, such as 24-hour pH-impedance testing with a probe or wireless capsule, and is not part of a modified barium swallow.',
        'Vocal fold mucosal wave analysis requires laryngeal stroboscopy during phonation; MBS assesses swallowing physiology, not voice production.',
    ],
    'v138_lar_13': [
        'Medialization thyroplasty narrows the glottis to improve voice in unilateral paralysis; in bilateral immobility it would worsen the already narrow airway and is not used to enlarge it.',
        'Injection augmentation adds bulk to bulge the fold medially, further narrowing the airway; it is appropriate for unilateral glottic insufficiency, not for widening a bilaterally obstructed airway.',
        'TEP creates a tracheoesophageal voice prosthesis tract after laryngectomy and has no role in improving airway caliber in bilateral vocal fold immobility.',
        'Correct.',
    ],
    'v138_lar_14': [
        'Reassurance based only on the conversational voice ignores that professional voice users can have a normal speaking voice while harboring vibratory lesions or technique deficits that only manifest during singing, particularly in the upper range.',
        'CT neck evaluates soft tissue and bony anatomy but would not identify a subtle vibratory or vocal fold cover abnormality; it is not the appropriate first test for this presentation.',
        'Correct.',
        'There is no indication of infection here, and antibiotics would not address a vibratory or technique-based cause of subtle range loss.',
    ],
    'v138_lar_15': [
        'Correct.',
        'Assuming symptoms are untreatable forgoes rehabilitative options -- swallowing therapy, dilation for strictures, compensatory maneuvers -- that can meaningfully improve function even with radiation fibrosis present.',
        'There is no described infectious process; antibiotics would not address fibrosis-related dysphagia, reduced tongue-base retraction, or cranial neuropathy.',
        'Nasal surgery addresses nasal airway obstruction and has no role in pharyngeal or laryngeal dysphagia caused by radiation fibrosis.',
    ],
    'v138_lar_16': [
        'Normal vibration would show a symmetric, intact mucosal wave on both folds; an absent wave over the lesion is specifically abnormal, not a normal finding.',
        'Bilateral vocal fold paralysis is characterized by immobility of both folds on abduction and adduction, not by an isolated focal loss of mucosal wave with a pliable contralateral fold.',
        'Hearing loss is unrelated to vocal fold vibratory characteristics assessed on stroboscopy, which evaluates phonatory biomechanics, not auditory function.',
        'Correct.',
    ],
    'v138_lar_17': [
        'Flexible nasopharyngoscopy only visualizes the nasal passages, nasopharynx, and larynx; it cannot reach the distal airway or provide instrumentation to retrieve a foreign body lodged in a bronchus.',
        'Correct.',
        'Esophagoscopy examines the esophagus, not the tracheobronchial tree, and would not address unilateral hyperinflation caused by a bronchial foreign body.',
        'An airway foreign body causing unilateral hyperinflation is potentially life-threatening from air trapping and obstruction and requires prompt endoscopic evaluation and retrieval, not avoidance of endoscopy.',
    ],
    'v138_lar_18': [
        'Correct.',
        'Complete airway obstruction is an emergency requiring immediate airway management, not an office-based, unsedated esophageal procedure.',
        'A button battery in the esophagus is a true emergency requiring urgent rigid esophagoscopy under general anesthesia given the risk of rapid tissue necrosis; it is never appropriate for office TNE, especially in a child.',
        'An unstable GI bleed requires resuscitation and often therapeutic endoscopy under controlled conditions with sedation, airway protection, and blood availability, not an awake office-based transnasal exam.',
    ],
    'v138_lar_19': [
        'Immediate surgery is not first-line for classic phonotraumatic nodules, since most resolve or markedly improve with behavioral voice therapy addressing the underlying vocal misuse.',
        'Correct.',
        'Radiation has no role in benign, phonotrauma-related vocal fold lesions and would cause unnecessary harm to normal laryngeal tissue.',
        'Tracheostomy addresses airway obstruction and is irrelevant to bilateral benign vocal fold lesions causing dysphonia without airway compromise.',
    ],
    'v138_lar_20': [
        'Correct.',
        'Adductor spasmodic dysphonia produces task-specific, irregular strained voice breaks during speech from involuntary laryngeal muscle spasms, not the continuous rhythmic oscillation across multiple subsites described here.',
        'Unilateral vocal fold paralysis presents with breathy dysphonia from glottic insufficiency, not rhythmic oscillatory movement of the palate and pharynx.',
        'A vocal fold cyst is a focal structural lesion that alters mucosal vibration locally, not a cause of rhythmic movement across multiple laryngeal and pharyngeal subsites.',
    ],
}


def apply_why_wrong_fix_vignettes_v138_v1(data_module):
    """Overwrite only untouched generic v138 explanations; return count updated."""
    byid = {q.get('id'): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get('id')}
    updated = 0
    skipped_already_edited = []
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES_V138.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        current = q.get('why_wrong') or []
        is_untouched_generic = bool(current) and all(
            str(w).strip() in (GENERIC_MARKER_V138, 'Correct.') for w in current
        ) and any(str(w).strip() == GENERIC_MARKER_V138 for w in current)
        if is_untouched_generic:
            if len(new_why_wrong) != len(q.get('choices') or []):
                raise ValueError(f"{qid}: fix has {len(new_why_wrong)} entries but question has {len(q.get('choices') or [])} choices")
            q['why_wrong'] = new_why_wrong
            updated += 1
        elif current == new_why_wrong:
            pass
        else:
            skipped_already_edited.append(qid)
    if missing:
        print(f'why_wrong_fix_vignettes_v138_v1: {len(missing)} ids not found: {missing}')
    if skipped_already_edited:
        print(f'why_wrong_fix_vignettes_v138_v1: {len(skipped_already_edited)} ids already edited, skipped: {skipped_already_edited}')
    return updated
