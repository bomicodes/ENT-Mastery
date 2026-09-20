"""v40.2 -- High-yield depth batch: twelve curriculum topics identified by a
full-curriculum scan as having zero source_basis entries and under ~1400
characters of combined six-stage content (recognize/localize/workup/manage/
operate/teach), the same "thin and unsourced" pattern already fixed for the
trauma domain in depth_content_facial_trauma_extra_v400.py.

Cross-referenced against:
  - AAO-HNS Clinical Practice Guideline: Nosebleed (Epistaxis), 2020
    (Tunkel et al., Otolaryngol Head Neck Surg, PMID 31910111) -- initial
    compression technique/duration, packing vs cautery, anticoagulation
    management, escalation to ligation/embolization.
  - AAO-HNS Clinical Practice Guideline: Tonsillectomy in Children (Update),
    2019 (Mitchell et al.) -- primary (<24h) vs secondary (>24h) hemorrhage
    definition and follow-up/documentation recommendation.
  - Barany Society diagnostic criteria consensus document for superior
    semicircular canal dehiscence syndrome, Ward et al., J Vestib Res 2021
    -- the three-category (symptom / physiologic test / CT) diagnostic
    framework, explicitly without a "definite vs probable" split.
  - Cummings Otolaryngology--Head and Neck Surgery, 7e, and Pasha & Golub
    Clinical Reference Guide, 6e, for the remaining topics (deep-space neck
    infection anatomy, Zenker pathophysiology, spasmodic dysphonia/laryngeal
    dystonia nomenclature, frontal recess anatomy, mucocele pathophysiology,
    congenital neck mass differential, functional nasal obstruction/NOSE
    scale).
"""

DEPTH_V401 = {
    "General ENT / Emergencies": {
        "Epistaxis": {
            "recognize": (
                "Localize bleeding as anterior (>90% of cases, from Kiesselbach's/Little's area on "
                "the anterior septum) versus posterior (from branches of the sphenopalatine artery, "
                "more common in older patients with vascular disease, presenting with bleeding down "
                "the throat despite anterior compression). Ask about anticoagulant/antiplatelet use, "
                "bleeding disorders, prior epistaxis/nasal surgery, and hypertension -- these change "
                "risk and management, but per the AAO-HNS guideline should be documented as risk "
                "factors rather than triggering reflexive medication reversal."
            ),
            "localize": (
                """After initial compression and stabilization, clear clots as appropriate and inspect the nasal cavity to identify a treatable anterior source. Recurrent or difficult-to-control epistaxis is an indication for nasal endoscopy or referral; if ongoing bleeding obscures the site despite compression, packing is appropriate rather than delaying hemostasis for endoscopy. Posterior bleeding is suspected when no anterior focus is seen and blood continues into the pharynx, but localization and management remain guided by the examination and clinical stability."""
            ),
            "workup": (
                "The initial 'workup' is a timed first-aid maneuver: firm, sustained compression of "
                "the lower third (the cartilaginous ala, not the bony bridge) of the nose for at "
                "least 5 minutes, with the patient leaning forward to avoid swallowing blood. If this "
                "fails, examine with a headlight/endoscope after topical vasoconstrictor and "
                "anesthetic to identify a treatable anterior source before deciding between cautery "
                "and packing."
            ),
            "manage": (
                "If a discrete anterior source is identified, treat it directly with topical "
                "vasoconstrictor, chemical (silver nitrate) or electrocautery, or a moisturizing/"
                "lubricating agent for dry mucosal bleeding -- do not pack a nose when the bleeding "
                "point can be treated directly. Reserve nasal packing for when the source cannot be "
                "identified or direct treatment fails; use resorbable packing preferentially in "
                "patients on anticoagulation or with a suspected bleeding disorder to avoid a second "
                "traumatic removal. Per the AAO-HNS guideline, first-line treatment should be "
                "attempted before transfusion, anticoagulation reversal, or medication withdrawal -- "
                "these are not the first response to epistaxis on anticoagulation."
            ),
            "operate": (
                """For persistent/recurrent epistaxis not controlled with compression, appropriate direct treatment or packing, localize bleeding endoscopically and evaluate candidacy for endoscopic sphenopalatine artery control versus endovascular embolization according to anatomy, bleeding source, expertise and patient risk. An endoscopic arterial approach is frequently used for refractory posterior bleeding, but the AAO-HNS guideline recommends evaluation for ligation AND/OR embolization rather than declaring one universally preferred. The orbit/skull base and adjacent arterial anatomy matter when dissection extends beyond the usual sphenopalatine region; embolization carries risk of nontarget ophthalmic or intracranial ischemia. After hemostasis, counsel on packing care, nasal humidification and follow-up; document outcomes, particularly after packing or arterial intervention."""
            ),
            "teach": (
                """For a significant non-life-threatening nosebleed, compress the lower third of the nose for at least five minutes, then inspect and treat an identified source; pack if ongoing bleeding obscures localization. Do not reflexively reverse anticoagulation before first-line treatment. Refractory or recurrent bleeding warrants evaluation for endoscopic ligation and/or embolization rather than a universal mandate for one technique."""
            ),
            "source_basis": [
                "Tunkel DE, et al. Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020;162(1_suppl):S1-S38 (PMID 31910111) -- compression technique/duration, packing vs direct treatment, anticoagulation management, escalation to ligation/embolization",
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- anterior/posterior epistaxis anatomy and endoscopic sphenopalatine artery ligation technique",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
        "Peritonsillar Abscess": {
            "recognize": (
                """Suspect a peritonsillar abscess with progressive unilateral sore throat, odynophagia, muffled voice, asymmetric peritonsillar bulging and sometimes uvular deviation or referred otalgia. Trismus supports a deeper peritonsillar infection but is neither necessary nor sufficient to distinguish an abscess from cellulitis. Evaluate airway and hydration status, and use aspiration or ultrasound when the diagnosis is uncertain."""
            ),
            "localize": (
                "The abscess forms in the peritonsillar space between the tonsillar capsule and the "
                "superior constrictor muscle, most often at the superior pole. Look for asymmetric "
                "soft-palate bulging, uvular deviation away from the affected side, and a displaced, "
                "medially pushed tonsil -- these bedside findings localize the abscess without "
                "imaging in most adults."
            ),
            "workup": (
                "Diagnosis is usually clinical; intraoral/transcervical ultrasound or CT with "
                "contrast helps when the exam is equivocal (especially with trismus limiting visualization), "
                "when a deeper space infection (parapharyngeal, retropharyngeal) is suspected, or "
                "in young children who cannot cooperate with a bedside exam."
            ),
            "manage": (
                """Assess airway, hydration and ability to swallow. Drainage by needle aspiration or incision and drainage plus antibiotics covering streptococci and oral anaerobes is a standard pathway; carefully selected uncomplicated patients can sometimes receive antibiotics alone with reliable reassessment, but evidence is limited. Neither aspiration nor incision and drainage is universally superior: a Cochrane review found very-low-certainty evidence suggesting higher recurrence after aspiration, with potentially less procedural pain. Select the approach based on anatomy, patient cooperation, local expertise and clinical response. Admit for airway concern, dehydration, sepsis, extension into deep spaces or inability to take therapy; interval tonsillectomy is individualized for recurrence or other independent indications."""
            ),
            "operate": (
                """For a confirmed abscess requiring drainage, use appropriately trained personnel and an airway plan for the patient who cannot tolerate secretions. A cooperative patient may undergo appropriately directed needle aspiration or incision and drainage with guarded depth and avoidance of posterolateral advancement toward the internal carotid artery. Ultrasound can guide uncertain or atypically located collections; a dry aspiration should prompt reassessment of diagnosis, location and need for imaging rather than blind deeper probing. General anesthesia and definitive drainage or tonsillectomy may be appropriate for selected pediatric, recurrent, failed-treatment or difficult-airway cases. Reassess swallowing, pain, hydration and response to antibiotics after treatment."""
            ),
            "teach": (
                """A unilateral bulging peritonsillar process with muffled voice and trismus suggests PTA, but no single sign proves an abscess. Prioritize airway and hydration, consider ultrasound or diagnostic aspiration when equivocal, choose aspiration or incision/drainage according to patient and anatomy, and never probe posterolaterally toward the carotid artery. Tonsillectomy is selective, not automatic for a first PTA."""
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- peritonsillar space anatomy, drainage technique and carotid-artery danger zone",
                "Pasha & Golub, Otolaryngology--Head and Neck Surgery Clinical Reference Guide, 6e -- PTA diagnosis and management pathway",
            
                'Chang BA et al. Needle aspiration compared to incision and drainage for peritonsillar abscess. Cochrane Database Syst Rev. 2016;CD006287 -- no high-certainty evidence of technique superiority; recurrence and pain tradeoffs.',],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
        "Ludwig Angina": {
            "recognize": (
                "Suspect Ludwig angina -- a rapidly progressive, bilateral cellulitis of the "
                "submandibular, sublingual and submental spaces, almost always odontogenic in origin "
                "(commonly the second/third mandibular molars) -- with a firm, 'woody' floor-of-mouth "
                "and submandibular swelling, tongue elevation/protrusion, drooling, trismus, and "
                "muffled voice. This is a true airway emergency: the tongue is pushed up and back, "
                "progressively narrowing the airway, and can obstruct with little warning even before "
                "obvious systemic toxicity develops."
            ),
            "localize": (
                "Infection classically spans the bilateral submandibular, sublingual and submental "
                "spaces without forming a discrete, drainable abscess early on -- it is a "
                "brawny, indurated cellulitis/early fasciitis rather than a fluctuant collection, "
                "which is why 'no pus on aspiration' does not mean the process is not dangerous. "
                "Untreated infection can spread posteriorly into the parapharyngeal and retropharyngeal "
                "spaces and into the mediastinum along fascial planes."
            ),
            "workup": (
                "Airway assessment comes first and drives everything else: examine for tongue "
                "elevation, floor-of-mouth induration, stridor and secretions before ordering imaging. "
                "CT with contrast defines extent, identifies a drainable abscess versus diffuse "
                "phlegmon, and screens for mediastinal extension in a patient stable enough to be "
                "scanned; do not send a patient with impending airway obstruction to CT before "
                "securing the airway."
            ),
            "manage": (
                "Early, aggressive airway management is the priority -- awake fiberoptic intubation "
                "or, when the airway is too distorted, a controlled awake tracheostomy under local "
                "anesthesia, performed electively before decompensation rather than as a crash rescue. "
                "Blind oral or nasal intubation attempts can worsen obstruction or fail entirely given "
                "the distorted floor-of-mouth anatomy. Broad-spectrum IV antibiotics covering oral "
                "flora (streptococci, oral anaerobes) and urgent dental/oral surgery evaluation for "
                "source control (extraction of the causative tooth) are started in parallel with "
                "airway management, not instead of it."
            ),
            "operate": (
                """Surgical exploration or drainage is indicated for a drainable abscess, fluctuance, necrotizing infection, failure to improve on appropriate antibiotics, or worsening clinical course; decompression can also be considered for selected progressive cases after multidisciplinary assessment. Diffuse cellulitis without a collection does not automatically require bilateral incision and drainage. If intervention is indicated, secure a threatened airway first with an individualized awake endoscopic or surgical airway plan developed by experienced airway and surgical teams, then drain indicated spaces and obtain odontogenic source control. Protect the lingual and hypoglossal nerves and lingual artery. Continue intensive airway reassessment, IV antimicrobials and surveillance for deep-neck/mediastinal extension."""
            ),
            "teach": (
                """Ludwig angina is rapidly progressive floor-of-mouth cellulitis and a potential difficult-airway emergency even without pus. Airway assessment, early specialist involvement, IV antibiotics and odontogenic source control are priorities; drain a collection or deteriorating/nonresponding disease rather than automatically performing bilateral drainage solely because the diagnosis is present."""
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- deep neck space anatomy, Ludwig angina airway management principles",
                "Pasha & Golub, Otolaryngology--Head and Neck Surgery Clinical Reference Guide, 6e -- odontogenic deep space infection recognition and airway-first management",
            
                'Ludwig Angina. StatPearls/NCBI Bookshelf, accessed September 2026 -- airway priority and selective surgical drainage for abscess or failure of medical therapy; diffuse cellulitis without abscess not universally drained.',],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
        "Post-Tonsillectomy Hemorrhage": {
            "recognize": (
                "Classify oral/pharyngeal bleeding after tonsillectomy by timing: primary bleeding "
                "occurs within 24 hours of surgery and usually reflects an intraoperative technical/"
                "hemostasis issue; secondary bleeding occurs after 24 hours (classically days 5-10, "
                "coinciding with eschar/scab separation from the tonsillar fossa) and is the more "
                "common presentation seen in follow-up or the emergency department. Any reported "
                "bleeding after tonsillectomy, however minor it sounds on the phone, warrants an "
                "in-person exam -- a 'herald bleed' (a small, self-limited episode) can precede a "
                "major one."
            ),
            "localize": (
                "Bleeding originates from the exposed tonsillar fossa vasculature (branches of the "
                "tonsillar, ascending pharyngeal, facial or lingual arteries) as the eschar separates; "
                "examine both fossae with good lighting and suction, since a clot can obscure the "
                "actual bleeding point and swallowed blood can make the volume of bleeding hard to "
                "estimate from history alone."
            ),
            "workup": (
                "Assess airway and hemodynamic stability first; a child who has been swallowing blood "
                "can look deceptively well until decompensating. Obtain IV access, type and screen/"
                "crossmatch for significant bleeding, and examine the fossae directly rather than "
                "relying on reported clot color/volume."
            ),
            "manage": (
                "Active, ongoing bleeding is a surgical emergency requiring a return to the operating "
                "room for hemostasis under general anesthesia in most cases (the AAO-HNS guideline "
                "asks surgeons to track and document primary vs secondary bleeding rates as a quality "
                "measure, underscoring how much this complication is monitored). A patient with a "
                "resolved herald bleed and a normal exam may be observed, but should be counseled that "
                "recurrent bleeding is possible and given clear return precautions, since a small "
                "sentinel bleed can precede a larger one from the same eroding vessel."
            ),
            "operate": (
                "Indication: active or recurrent post-tonsillectomy bleeding. Setup: general "
                "anesthesia with a secured airway (rapid-sequence induction accounting for a "
                "potentially full stomach from swallowed blood), suction immediately available on "
                "induction. Key steps: identify the bleeding point in the fossa and control it with "
                "electrocautery, suture ligation, or a combination; re-inspect the entire fossa "
                "bilaterally, since a second bleeding point is not uncommon. Danger structures: the "
                "carotid sheath contents posterolateral to the fossa. Failure mode: assuming a single "
                "obvious bleeding point is the only source and closing before a full bilateral "
                "re-inspection. Postoperative plan: observe for rebleeding, ensure adequate hydration "
                "and pain control (pain avoidance can itself reduce oral intake and healing), and "
                "counsel that secondary hemorrhage risk continues through eschar separation."
            ),
            "teach": (
                "Primary (<24h) versus secondary (>24h, typically days 5-10 with eschar separation) "
                "is the key timing distinction. Any reported post-tonsillectomy bleeding needs an "
                "in-person exam -- a herald bleed can precede a major one from the same vessel."
            ),
            "source_basis": [
                "Mitchell RB, et al. Clinical Practice Guideline: Tonsillectomy in Children (Update). Otolaryngol Head Neck Surg. 2019 -- primary (<24h) vs secondary (>24h) hemorrhage definition and outcome-tracking recommendation",
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- tonsillar fossa vascular anatomy and operative hemostasis technique",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
    },
    "Otology / Neurotology": {
        "Superior Canal Dehiscence": {
            "recognize": (
                """Superior semicircular canal dehiscence syndrome arises from a true bony defect over the superior canal that forms a third mobile window. In the 2021 Bárány Society criteria, qualifying symptoms include bone-conduction hyperacusis, sound- or pressure-induced vertigo/oscillopsia time-locked to the stimulus, or pulsatile tinnitus. Thin bone or an apparent defect on CT alone is not enough: imaging can overcall dehiscence, and symptoms and physiology must agree."""
            ),
            "localize": (
                "The dehiscence sits in the plane of the superior semicircular canal, so eye "
                "movements provoked by sound or pressure changes occur in that canal's plane -- this "
                "is the physiologic hallmark, distinguishing SCDS from other third-window or "
                "conductive-hearing-loss conditions. A low-frequency air-bone gap with normal middle "
                "ear function (normal tympanogram, present acoustic reflexes) on audiometry, or "
                "abnormally low cervical VEMP thresholds/elevated ocular VEMP amplitudes on the "
                "affected side, are the supporting physiologic (non-imaging) findings."
            ),
            "workup": (
                """The 2021 Bárány Society diagnosis requires ALL of: (1) at least one qualifying third-window symptom; (2) at least one supporting physiologic sign—sound/pressure-evoked superior-canal-plane eye movements, abnormally low-frequency or negative bone-conduction thresholds, or enhanced VEMP responses (low cVEMP threshold/high oVEMP amplitude); (3) high-resolution temporal bone CT reconstructed in and orthogonal to the superior canal plane showing a defect; and (4) no better alternative explanation. A low-frequency air-bone gap with normal tympanometry/reflexes can suggest the mechanism, but is not itself a substitute for the consensus physiologic criteria. Interpret VEMPs using laboratory-specific norms."""
            ),
            "manage": (
                "Observe patients with an incidental radiographic dehiscence and no symptoms. "
                "Counsel symptomatic patients to avoid known triggers (loud sound exposure, straining/"
                "Valsalva maneuvers) where practical. Reserve surgery for patients with symptoms that "
                "are functionally impairing and whose findings meet the full diagnostic criteria, "
                "since symptom severity does not always correlate with dehiscence size on imaging."
            ),
            "operate": (
                "Indication: functionally impairing SCDS symptoms meeting full diagnostic criteria, "
                "refractory to observation/trigger avoidance. Setup: choose middle fossa craniotomy "
                "(direct visualization, better for anteriorly located or larger dehiscences) or "
                "transmastoid approach (less invasive, avoids craniotomy, but more limited exposure of "
                "the canal) based on dehiscence location and surgeon experience. Key steps: repair by "
                "plugging the canal lumen, resurfacing the bony defect over an intact membranous canal, "
                "or a combination -- plugging obliterates canal function and is generally more durable; "
                "resurfacing preserves canal function but has a higher reported recurrence rate. Danger "
                "structures: the superior semicircular canal itself (inadvertent opening into the "
                "membranous labyrinth risks sensorineural hearing loss), the facial nerve, and the "
                "temporal lobe dura during middle fossa exposure. Failure mode: repairing a "
                "radiographically obvious dehiscence in a patient whose symptoms do not actually match "
                "the third-mobile-window pattern, or in whom VEMP/audiometric findings do not "
                "corroborate the diagnosis -- symptoms may then persist post-repair from a different, "
                "unaddressed cause. Postoperative plan: expect resolution of sound/pressure-induced "
                "vertigo when the correct ear is repaired; monitor hearing, since surgery itself "
                "carries a real risk of sensorineural hearing loss."
            ),
            "teach": (
                """SCDS requires concordant third-window symptoms, a qualifying physiologic finding and high-resolution canal-plane CT, with other diagnoses excluded. An air-bone gap is a clue, not a stand-alone consensus criterion; CT dehiscence alone should not trigger surgery."""
            ),
            "source_basis": [
                "Ward BK, van de Berg R, van Rompaey V, et al. Superior semicircular canal dehiscence syndrome: Diagnostic criteria consensus document of the committee for the classification of vestibular disorders of the Barany Society. J Vestib Res. 2021;31(3):131-141 -- the three-category diagnostic framework",
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- SCDS surgical approaches (middle fossa vs transmastoid) and plugging vs resurfacing technique",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
        "Vestibular Neuritis": {
            "recognize": (
                """Acute unilateral vestibulopathy (vestibular neuritis) produces sustained acute vestibular syndrome with continuous vertigo/dizziness, spontaneous peripheral-pattern nystagmus, nausea and gait unsteadiness, without acute cochlear symptoms or focal central neurologic signs. These absences do NOT by themselves rule out posterior-circulation stroke. New hearing loss raises concern for labyrinthine disease AND for an AICA-territory stroke in the appropriate clinical setting; assess hearing rather than assuming it guarantees a benign diagnosis."""
            ),
            "localize": (
                """Vestibular testing can suggest superior-division, inferior-division or combined unilateral vestibular hypofunction. In adults with ongoing acute vestibular syndrome AND spontaneous nystagmus, HINTS is used to distinguish peripheral from central causes ONLY by an examiner trained in the technique; assessment of new hearing loss (HINTS-plus), focal findings and gait instability adds safety. A peripheral pattern typically has an abnormal head impulse toward the affected ear, direction-fixed nystagmus and no skew. A central or equivocal pattern needs a stroke pathway and often MRI, recognizing early MRI may miss posterior fossa infarction. HINTS is not a general test for episodic/positional vertigo or patients without nystagmus."""
            ),
            "workup": (
                """For persistent acute vestibular syndrome, document nystagmus, gait, neurologic and hearing findings. Trained clinicians may use HINTS when spontaneous nystagmus is present; a central or equivocal finding, new unilateral hearing loss or other concerning features warrants urgent stroke-oriented assessment and MRI as indicated. When nystagmus is absent, gait and other findings guide further workup instead of applying HINTS. Early diffusion MRI can be falsely negative for posterior-circulation infarction; persistent concern requires clinical reassessment and appropriate imaging/neurology input. Audiometry can characterize new hearing loss but should not delay time-critical stroke assessment."""
            ),
            "manage": (
                "Symptomatic treatment (vestibular suppressants, antiemetics) is used only briefly in "
                "the acute phase, since prolonged use slows central vestibular compensation. Early "
                "vestibular rehabilitation therapy, started as soon as the acute nausea allows, speeds "
                "compensation and functional recovery. Corticosteroids may modestly speed the rate of "
                "peripheral vestibular recovery in some patients when started early, though evidence "
                "for long-term functional benefit is mixed."
            ),
            "operate": (
                """There is no primary surgical treatment for vestibular neuritis. The important bedside skill is selecting and correctly performing the examination: HINTS is for continuous acute vestibular syndrome with spontaneous nystagmus, in trained hands only. Do not use a seemingly peripheral result in an untrained or inapplicable examination to discharge a patient with possible stroke. Treat the confirmed peripheral disorder with short-term symptom relief and early vestibular rehabilitation."""
            ),
            "teach": (
                """Continuous acute vertigo can be peripheral or stroke. In patients with spontaneous nystagmus, a TRAINED clinician can use HINTS plus hearing assessment; central/equivocal findings or concerning clinical features warrant a stroke workup even if an early MRI is negative. Do not apply HINTS to episodic vertigo or absent nystagmus, and do not treat lack of hearing loss as proof against stroke."""
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- vestibular neuritis pathophysiology and HINTS-based localization",
                "Pasha & Golub, Otolaryngology--Head and Neck Surgery Clinical Reference Guide, 6e -- acute vestibular syndrome workup and vestibular rehabilitation principles",
            
                'Edlow JA et al. GRACE-3: Acute dizziness and vertigo in the emergency department. Acad Emerg Med. 2023;30:442-486 (PMID 37166022) -- trained HINTS only for AVS with nystagmus, add hearing, confirm central/equivocal findings with MRI.',],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
    },
    "Laryngology / Voice / Swallowing": {
        "Zenker Diverticulum": {
            "recognize": (
                "Suspect Zenker diverticulum in an older adult with progressive dysphagia, "
                "regurgitation of undigested food (sometimes hours after eating), halitosis, "
                "gurgling with swallowing, and recurrent aspiration pneumonia; a neck mass that "
                "gurgles on palpation is a classic but inconsistent finding."
            ),
            "localize": (
                "This is a pulsion (false, mucosal-only) diverticulum that herniates through "
                "Killian's triangle, an area of inherent weakness in the posterior pharyngeal wall "
                "between the oblique fibers of the inferior pharyngeal constrictor (thyropharyngeus) "
                "above and the transverse fibers of the cricopharyngeus below. It results from "
                "cricopharyngeal dysfunction/incoordination (failure of the upper esophageal "
                "sphincter to relax normally or excessive muscle tone) that raises pharyngeal pressure "
                "against a closed sphincter, forcing mucosa through the weak point -- the diverticulum "
                "itself is a consequence of the underlying sphincter problem, not the primary disease."
            ),
            "workup": (
                """A contrast barium esophagram is the usual diagnostic study to define the Zenker pouch, its size, retention and relationship to the true esophageal lumen. A modified barium swallow (videofluoroscopic swallowing study) may additionally assess oropharyngeal physiology and aspiration but is not interchangeable with a complete diagnostic esophagram. Endoscopy may be performed carefully when indicated to evaluate associated disease, avoiding entry into or perforation of the sac."""
            ),
            "manage": (
                "Treatment targets the cricopharyngeus, not just the sac -- cricopharyngeal myotomy is "
                "the essential step in every definitive repair, since a diverticulum that is excised "
                "or stapled without addressing the underlying sphincter dysfunction can recur. Small, "
                "asymptomatic diverticula in a poor surgical candidate can be observed."
            ),
            "operate": (
                """Treat symptomatic Zenker diverticulum with endoscopic septotomy (flexible or rigid, using stapler, laser or cutting device as appropriate) or an open transcervical approach depending on pouch size, exposure, anatomy, comorbidity and expertise. Adequate division of the cricopharyngeal septum/myotomy addresses outflow resistance; open options may also include diverticulectomy, inversion or pexy. Risks include mucosal perforation, leak, mediastinitis, bleeding and recurrent laryngeal nerve injury during open surgery. Assess clinically for perforation after treatment; contrast swallow imaging before diet advancement is selective according to technique, procedural findings and local protocol, not a universal requirement after every endoscopic procedure. Advance diet per the operative team and monitor for recurrence."""
            ),
            "teach": (
                "Zenker diverticulum is a symptom of cricopharyngeal dysfunction, not just a "
                "mechanical outpouching -- myotomy, not sac removal, is the essential step in any "
                "durable repair."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- Killian's triangle anatomy, pulsion diverticulum pathophysiology, endoscopic vs open repair technique",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
        "Spasmodic Dysphonia": {
            "recognize": (
                "Spasmodic dysphonia (now often termed laryngeal dystonia in the broader movement-"
                "disorder literature) is a task-specific focal laryngeal dystonia causing involuntary "
                "spasms during specific voicing tasks, classically speech, while other laryngeal "
                "tasks (singing, laughing, coughing) can be relatively spared -- this task-specificity "
                "is itself a diagnostic clue that distinguishes it from a structural or paralytic "
                "voice disorder."
            ),
            "localize": (
                "Adductor spasmodic dysphonia (far more common) produces a strained, strangled, "
                "effortful voice with abrupt voice breaks from excessive thyroarytenoid/lateral "
                "cricoarytenoid (adductor) muscle activity during vowel production. Abductor "
                "spasmodic dysphonia (less common) produces breathy voice breaks from involuntary "
                "posterior cricoarytenoid (abductor) spasm during voiceless consonants. Mixed forms "
                "exist. A coexisting vocal tremor is common and can be mistaken for essential tremor "
                "affecting the voice, but tremor and spasmodic dysphonia often occur together and are "
                "treated somewhat differently."
            ),
            "workup": (
                "Diagnosis is clinical, based on perceptual voice characteristics during connected "
                "speech (not sustained vowels alone, since spasms are task-specific) plus "
                "laryngoscopy to exclude a structural cause (mass, paralysis, scar) that could mimic "
                "the voice quality; a multidisciplinary laryngology/speech-language pathology "
                "evaluation is standard given how easily this is misattributed to a purely "
                "psychogenic or functional voice disorder."
            ),
            "manage": (
                "Botulinum toxin injection into the affected laryngeal muscles (thyroarytenoid for "
                "adductor type, posterior cricoarytenoid for abductor type) is first-line treatment "
                "and provides temporary (typically 3-4 month) symptomatic relief by weakening the "
                "involuntary spasm; it requires repeat injection indefinitely since it does not "
                "address the underlying central dystonic process. Voice therapy alone is generally "
                "insufficient as monotherapy but is a useful adjunct."
            ),
            "operate": (
                "Indication: adductor spasmodic dysphonia inadequately controlled by or intolerant of "
                "botulinum toxin, or seeking a longer-lasting alternative. Setup/key steps: selective "
                "laryngeal adductor denervation-reinnervation (interrupting the recurrent laryngeal "
                "nerve's adductor branches and reinnervating with a branch of the ansa cervicalis) is "
                "the most established surgical alternative, aiming to weaken involuntary adductor "
                "spasm while preserving reinnervated muscle tone; type II thyroplasty (midline "
                "laryngoplasty to widen the glottis) is an alternative for adductor-type disease in "
                "selected patients. Danger structures: the recurrent laryngeal nerve itself (the "
                "target of denervation-reinnervation, so precise identification of the adductor "
                "branches is essential to avoid unintended vocal fold paralysis instead of the "
                "intended selective weakening). Failure mode: treating spasmodic dysphonia as a "
                "structural problem needing vocal fold surgery rather than a dystonic movement "
                "disorder needing neuromodulation (botulinum toxin) or nerve-directed surgery. "
                "Postoperative plan: voice therapy and staged reassessment, since denervation-"
                "reinnervation results evolve over months as reinnervation matures."
            ),
            "teach": (
                "Task-specific voice breaks (worse in connected speech, better singing/laughing) point "
                "toward spasmodic dysphonia/laryngeal dystonia, not a structural lesion. Botulinum "
                "toxin, not phonosurgery, is first-line."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- adductor/abductor spasmodic dysphonia pathophysiology and botulinum toxin/surgical management",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
    },
    "Rhinology / Allergy / Skull Base": {
        "Frontal Recess / Frontal Sinus": {
            "recognize": (
                "The frontal recess is the narrow, hourglass-shaped outflow pathway of the frontal "
                "sinus, not a fixed single 'duct' -- its anatomy is the single most variable and "
                "surgically important region in endoscopic sinus surgery, and most frontal sinus "
                "surgical failures trace back to a misunderstood or incompletely addressed frontal "
                "recess."
            ),
            "localize": (
                "The frontal recess is bounded by the agger nasi cell anteriorly, the anterior "
                "ethmoid skull base/lamina cribrosa posteriorly-superiorly, and the middle turbinate "
                "medially; its actual outflow path curves around the anteriorly-based agger nasi cell "
                "and is shaped by variable pneumatization of surrounding cells (agger nasi, frontal "
                "cells types I-IV by the Kuhn classification, supraorbital ethmoid cells, and frontal "
                "septal cells) -- these cells narrow or redirect the pathway and must be identified on "
                "preoperative CT, since they determine where the true drainage pathway lies."
            ),
            "workup": (
                "High-resolution sinus CT in coronal, axial and sagittal planes is essential before "
                "any frontal sinus surgery, since the recess's course cannot be reliably predicted "
                "from endoscopy alone; identify the agger nasi cell and any frontal/supraorbital "
                "ethmoid cells on the sagittal 'Draf-plane' view to anticipate the drainage pathway "
                "before entering the OR."
            ),
            "manage": (
                "Medical management (topical/systemic steroids, saline irrigation, addressing "
                "underlying chronic rhinosinusitis or allergic disease) is first-line for frontal "
                "sinus disease without a discrete surgical indication (mucocele, refractory chronic "
                "frontal sinusitis, orbital/intracranial complication, tumor)."
            ),
            "operate": (
                """For refractory frontal sinusitis, symptomatic mucocele or complications, map the frontal drainage pathway and neighboring orbit/skull base on multiplanar CT. Draf I/IIa/IIb/III procedures progressively enlarge drainage according to disease and anatomy; remove the obstructing bony partitions and preserve healthy mucosa where feasible to support epithelialization. Avoid treating every frontal sinus failure as a missed cell: residual obstruction, inflammatory disease, osteitis and postoperative scarring can all contribute. Protect the lateral orbit and posterior/superior skull base and provide postoperative topical treatment, surveillance and selective debridement to limit restenosis."""
            ),
            "teach": (
                """The frontal recess is a variable drainage pathway, not a straight duct. Map agger/frontal cells, orbit and skull base in multiple CT planes before surgery; tailor the Draf opening while preserving healthy mucosa. Failure can reflect residual anatomy, chronic inflammatory disease or scarring, not missed cells alone."""
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e, ch 46 (Management of the Frontal Sinuses) -- frontal recess boundaries, Kuhn frontal cell classification, Draf procedure grading",
                "International Consensus Statement on Allergy and Rhinology: Rhinosinusitis (ICAR-RS), 2021 -- frontal sinusotomy indications within chronic rhinosinusitis management",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
        "Mucocele": {
            "recognize": (
                "Suspect a paranasal sinus mucocele -- a mucus-filled, epithelial-lined, expansile "
                "cyst that develops when a sinus outflow tract becomes chronically obstructed -- in a "
                "patient with slowly progressive facial fullness/pressure, proptosis or diplopia "
                "(frontal/ethmoid mucoceles pressing on the orbit), or headache, often with a history "
                "of prior sinus surgery, trauma, chronic sinusitis, or radiation. Frontal and "
                "frontoethmoid mucoceles are most common, but they can occur in any sinus."
            ),
            "localize": (
                """Obstructed sinus outflow produces a slowly expansile, epithelial-lined mucus collection that can remodel and erode adjacent bone, displacing the orbit or reaching the skull base. The benign mechanism does not make an exposed orbit or intracranial extension harmless, and imaging appearance alone cannot reliably distinguish every mucocele from a neoplasm or other expansile lesion; investigate atypical enhancement, solid tissue or rapid destructive growth appropriately."""
            ),
            "workup": (
                """CT maps the expansile sinus lesion and adjacent bony remodeling or dehiscence; MRI is useful for ambiguous tissue characteristics, suspected tumor, or orbital/intracranial extension. Imaging findings should be integrated with history, endoscopy and specialist assessment rather than assuming mucus can always be confidently distinguished from neoplasm by MRI alone."""
            ),
            "manage": (
                """A symptomatic, enlarging or structurally threatening sinus mucocele generally warrants surgical drainage and marsupialization because antibiotics or steroids alone do not correct persistent outflow obstruction. Timing is individualized for a truly incidental, small, stable asymptomatic lesion with no threatened orbit/skull base and reliable surveillance; orbital/visual or intracranial complications warrant urgent specialty evaluation. Avoid stating that every minimally symptomatic radiographic finding requires immediate surgery."""
            ),
            "operate": (
                "Indication: confirmed mucocele. Setup: high-resolution CT (and MRI when orbital/"
                "intracranial extension is suspected) to plan the surgical approach and anticipate "
                "thinned or dehiscent bone over the orbit/skull base. Key steps: endoscopic "
                "marsupialization -- widely opening the mucocele into the nasal cavity so it drains "
                "and epithelializes as part of the sinus rather than needing complete removal of the "
                "cyst wall -- is now the standard approach for most locations, since removing the "
                "entire mucocele lining is unnecessary and often not feasible near critical structures. "
                "External approaches are reserved for anatomy not accessible endoscopically. Danger "
                "structures: the orbit and its periorbita (frontal/ethmoid mucoceles often directly "
                "abut or thin the lamina papyracea/orbital roof) and the anterior skull base/dura, both "
                "of which may already be thinned by the mucocele itself before surgery even begins. "
                "Failure mode: mistaking a mucocele for a sinus tumor (or vice versa) based on "
                "expansile appearance alone without MRI characterization, leading to an inappropriately "
                "aggressive or inappropriately conservative plan. Postoperative plan: endoscopic "
                "surveillance to confirm the marsupialized cavity remains open and does not restenose, "
                "since recurrence is possible if the drainage opening closes."
            ),
            "teach": (
                "A mucocele expands by chronic pressure remodeling of bone, not invasion -- this "
                "benign mechanism can still cause real orbital/skull-base complications if untreated. "
                "Marsupialize, don't try to fully excise, in most locations."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- mucocele pathophysiology, CT/MRI differentiation from neoplasm, endoscopic marsupialization technique",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
    },
    "Pediatric Otolaryngology": {
        "Congenital Neck Masses": {
            "recognize": (
                "Use location and timing as the first sort: a midline mass at or near the hyoid that "
                "elevates with tongue protrusion or swallowing is a thyroglossal duct cyst; a lateral "
                "mass along the anterior border of the sternocleidomastoid is most often a second "
                "branchial cleft anomaly; a soft, compressible, sometimes rapidly enlarging (with "
                "infection or hemorrhage) mass is more consistent with a lymphatic or vascular "
                "malformation; and a firm, ropey lateral neck mass in a newborn, sometimes discovered "
                "after a difficult/breech delivery, suggests fibromatosis colli (sternocleidomastoid "
                "'tumor' of infancy) rather than a true neoplasm."
            ),
            "localize": (
                "Thyroglossal duct cysts arise anywhere along the tract of thyroid descent from the "
                "foramen cecum to the thyroid gland, most commonly at or just below the hyoid; "
                "second branchial cleft anomalies track between the internal and external carotid "
                "arteries toward the tonsillar fossa; dermoid cysts are typically midline but do not "
                "move with tongue protrusion (distinguishing them from thyroglossal duct cysts); "
                "fibromatosis colli is a focal fibrous thickening within the sternocleidomastoid "
                "muscle belly itself, not a separate mass adjacent to it."
            ),
            "workup": (
                "Ultrasound is the first-line, radiation-free imaging study for most pediatric neck "
                "masses and can usually distinguish cystic (thyroglossal duct cyst, branchial "
                "anomaly, lymphatic malformation) from solid (fibromatosis colli, lymphadenopathy, "
                "neoplasm) lesions. Confirm a normal, orthotopic thyroid gland is present before "
                "excising a suspected thyroglossal duct cyst, since it may be the patient's only "
                "functioning thyroid tissue (ectopic thyroid within the tract). Any atypical feature "
                "-- rapid growth, firmness, fixation, systemic symptoms, or a mass persisting/enlarging "
                "beyond the expected congenital pattern -- should prompt workup for a neoplastic "
                "process rather than being assumed congenital."
            ),
            "manage": (
                "Most congenital cystic neck masses are managed surgically when confirmed, given "
                "recurrent infection risk and the rare potential for malignant transformation within "
                "the tract lining (thyroglossal duct carcinoma is rare but real, usually incidental at "
                "pathology). Fibromatosis colli is managed with physical therapy/stretching in "
                "infancy, since most cases resolve without surgery; surgery is reserved for "
                "persistent torticollis unresponsive to conservative therapy."
            ),
            "operate": (
                "Indication: confirmed thyroglossal duct cyst or branchial anomaly, or fibromatosis "
                "colli that fails conservative stretching therapy. Setup: confirm thyroid status by "
                "ultrasound before thyroglossal duct cyst excision; define the branchial tract's "
                "course on imaging when relevant. Key steps: thyroglossal duct cysts are excised via "
                "the Sistrunk procedure (cyst, tract, and central hyoid bone segment together, since "
                "leaving hyoid bone behind is the leading cause of recurrence); branchial anomalies "
                "require complete excision of the cyst and its full tract, not just the visible "
                "external opening. Danger structures: the lingual nerve/hypoglossal nerve near the "
                "hyoid, and the facial nerve or carotid vessels depending on branchial cleft type. "
                "Failure mode: excising a thyroglossal duct cyst without the central hyoid segment, or "
                "excising a branchial cyst without tracing its full tract -- both are the classic "
                "causes of recurrence. Postoperative plan: watch for infection/seroma and counsel that "
                "an incompletely excised tract can recur, sometimes years later."
            ),
            "teach": (
                "Location and movement with swallowing/tongue protrusion, not just 'midline vs "
                "lateral,' sort the congenital neck mass differential. Confirm the thyroid gland is "
                "present and orthotopic before taking out a 'thyroglossal duct cyst.'"
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- congenital neck mass differential, embryology and surgical technique",
                "K.J. Lee's Essential Otolaryngology, 12e -- pediatric neck mass evaluation pathway and fibromatosis colli management",
            ],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
    },
    "Facial Plastics / Trauma": {
        "Functional Nasal Obstruction": {
            "recognize": (
                """Differentiate structural obstruction (septum, turbinates, static/dynamic internal or external nasal valve dysfunction) from inflammatory rhinitis and other contributors, which may coexist. Observe the nasal sidewall/alar rim with quiet and deep inspiration and assess targeted support with modified Cottle or nasal dilator maneuvers. Improvement with standard cheek-traction Cottle suggests a valve contribution but is nonspecific and does not by itself localize the level or predict the best operation."""
            ),
            "localize": (
                "The internal nasal valve -- the angle between the caudal edge of the upper lateral "
                "cartilage and the septum, normally around 10-15 degrees -- is the narrowest, highest-"
                "resistance segment of the nasal airway in most people and a common site of "
                "obstruction after rhinoplasty or trauma that narrows this angle. The external nasal "
                "valve is defined by the nostril rim/alar cartilage and skin, and collapses when "
                "alar cartilage support is weak, particularly on deep inspiration."
            ),
            "workup": (
                "Diagnosis is primarily clinical: anterior rhinoscopy and nasal endoscopy to assess "
                "the septum, turbinates and valve regions, along with dynamic assessment of valve "
                "collapse on inspiration and Cottle/modified Cottle maneuvers. The NOSE (Nasal "
                "Obstruction Symptom Evaluation) scale is a validated, widely used patient-reported "
                "outcome measure to quantify baseline severity and track response to treatment; "
                "objective airflow measures (acoustic rhinometry, rhinomanometry) are used selectively "
                "and correlate imperfectly with patient-reported symptoms, so treatment decisions "
                "should not rest on objective testing alone."
            ),
            "manage": (
                """Treat coexisting inflammatory or mucosal disease when present, but do not require an ineffective septoplasty/turbinate procedure before addressing clearly documented nasal valve dysfunction. Match treatment to the contributing anatomy: septoplasty for obstructing deviation, turbinate management for appropriate hypertrophy, and valve-directed support/reconstruction for static or dynamic valve problems, alone or combined when indicated. Discuss nonoperative dilator devices and shared treatment goals with the patient."""
            ),
            "operate": (
                """Consider surgery when symptomatic obstruction corresponds to documented anatomical findings and conservative treatment appropriate to the cause is insufficient or unwanted. Examine septum, turbinates, internal and external valve separately, using dynamic observation and targeted maneuvers; a positive Cottle maneuver or NOSE score alone is not a surgical indication. Correct obstructing septal deviation and turbinate hypertrophy as indicated, and provide valve-specific support (e.g., spreader, batten or lateral-crural grafting, suture or selected minimally invasive approaches) when the valve contributes. Valve repair may be done simultaneously with other surgery or alone; prior septoplasty is not a prerequisite. Avoid destabilizing septal support or excessive turbinate reduction. Reassess patient-reported symptoms with the NOSE scale and examination, remembering the scale is subjective rather than an objective airflow measurement."""
            ),
            "teach": (
                "Separate structural from mucosal causes before operating, and identify which "
                "structural element is responsible (septum vs turbinate vs which valve) -- "
                "septoplasty does not fix a collapsing valve, and valve surgery does not fix allergic "
                "rhinitis. Track outcomes with the same validated NOSE scale used at baseline."
            ),
            "source_basis": [
                "Cummings Otolaryngology--Head and Neck Surgery, 7e -- internal/external nasal valve anatomy and structural nasal obstruction workup",
                "Stewart MG, et al. Development and validation of the Nasal Obstruction Symptom Evaluation (NOSE) scale. Otolaryngol Head Neck Surg. 2004 -- validated patient-reported outcome measure",
            
                'AAO-HNS Position Statement: Nasal Valve Repair, revised July 2026 -- valve repair as distinct procedure; prior septoplasty/turbinate surgery is not required.',],
            "evidence_calibrated": "v40.2-high-yield-batch",
        },
    },
}


def apply_depth_content_high_yield_batch_v401(data_module):
    enriched = []
    for domain, topics in DEPTH_V401.items():
        modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(domain, [])}
        missing = [t for t in topics if t not in modules]
        if missing:
            raise RuntimeError(f"v40.2: expected {domain} topics not found: {missing}")
        for topic, fields in topics.items():
            modules[topic].update(fields)
            enriched.append(f"{domain} | {topic}")
    return {"enriched": enriched}
