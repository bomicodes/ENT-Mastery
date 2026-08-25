"""v16.3 — Cross-domain Deep Curriculum enrichment, pass 4.

Continues the in-place depth audit with one additional high-yield, decision-heavy
module in each non-Otology domain. The goal is not topic-count inflation; it is
to make each six-layer card function as an actual resident/chief reference:
pathogenesis, discriminating workup, management pivots, operative strategy,
complications, and declarative board teaching.
"""


def _entry(candidates, recognize, localize, workup, manage, operate, teach, tags, sources=None):
    return {
        "candidates": tuple(candidates),
        "fields": {
            "recognize": recognize,
            "localize": localize,
            "workup": workup,
            "manage": manage,
            "operate": operate,
            "teach": teach,
            "tags": list(tags),
            **({"source_basis": list(sources)} if sources else {}),
        },
    }


PATCHES_V163 = {
    "Rhinology / Allergy / Skull Base": [
        _entry(
            ["Sinonasal Inverted Papilloma", "Inverted Papilloma"],
            "Inverted papilloma is a benign but locally aggressive Schneiderian epithelial tumor, classically presenting as a unilateral nasal mass with obstruction, epistaxis, or recurrent unilateral sinus disease. It matters because recurrence can be substantial if the attachment is not cleared and because synchronous or metachronous squamous cell carcinoma can occur. Unilateral polyposis in an adult should therefore not be presumed inflammatory until neoplasm is excluded.",
            "These tumors commonly arise from the lateral nasal wall or sinus mucosa and grow by endophytic epithelial inversion. The operative problem is the site of attachment, not the visible bulk of the mass. Maxillary sinus attachment may require angled endoscopic access or medial maxillectomy-type exposure; frontal, sphenoid, skull-base, or orbital-adjacent attachment changes both access and morbidity. Bone hyperostosis on CT can point toward the attachment site.",
            "Perform nasal endoscopy and obtain tissue diagnosis before definitive treatment when feasible. CT defines bony anatomy, hyperostosis, sinus remodeling, and surgical corridors; MRI can distinguish tumor from retained secretions/inflammation and is particularly useful with skull-base/orbital extension or concern for malignancy. Assess for focal bone destruction, cranial neuropathy, severe pain, or rapid change that raises concern for carcinoma. Preoperative imaging should be read specifically to predict the attachment site so surgery can be planned around it.",
            "Definitive therapy is complete surgical excision with treatment of the attachment site rather than simple debulking. Endoscopic resection is preferred for most accessible disease, with open or combined approaches reserved for anatomy/extension that cannot be safely controlled endonasally. Long-term endoscopic surveillance is required because recurrence may be delayed. If SCC is present, treatment follows sinonasal cancer principles and may require wider resection and adjuvant therapy rather than the benign-tumor pathway.",
            "Debulk only enough to expose the true attachment, then remove involved mucosa/periosteum and drill or otherwise treat underlying hyperostotic bone when appropriate. Choose the corridor that provides direct visualization of the attachment rather than forcing a narrow approach that leaves hidden disease. Preserve orbit, lacrimal system, skull base, infraorbital nerve, and major vascular structures when oncologically safe. The key intraoperative endpoint is confidence that the attachment—not merely the exophytic tumor—has been eradicated.",
            "Boards/chief framework: unilateral mass + inverted papilloma means think attachment, recurrence, and SCC risk. CT hyperostosis can localize the attachment; MRI helps separate tumor from obstructed secretions. Surgery fails when the bulk is removed but the attachment is left behind, so approach selection is driven by the ability to expose and clear the attachment completely.",
            ["inverted papilloma", "Schneiderian", "hyperostosis", "attachment site", "medial maxillectomy", "SCC", "unilateral nasal mass"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],

    "Head & Neck Oncology": [
        _entry(
            ["Laryngeal Preservation Decision", "Organ Preservation in Advanced Laryngeal Cancer", "Larynx Preservation"],
            "Laryngeal preservation is not synonymous with keeping the anatomic larynx at any cost. The real goal is oncologic control plus a functional airway, voice, and swallow. Advanced laryngeal/hypopharyngeal SCC may be treated with surgery or nonsurgical organ-preservation therapy, but patients with a nonfunctional larynx, major cartilage destruction, extensive extralaryngeal spread, severe aspiration, or poor likelihood of completing chemoradiation may be better served by primary total laryngectomy rather than a nominally preserved but unusable organ.",
            "Subsite and spread pattern drive both staging and function. Glottic tumors tend to present early through hoarseness and initially have sparse lymphatics; supraglottic tumors have richer bilateral lymphatic drainage and often present with nodal disease. Paraglottic/pre-epiglottic space invasion, cartilage involvement, fixation, subglottic extension, and extralaryngeal spread alter resectability and the probability of durable functional preservation.",
            "Workup includes flexible laryngoscopy with vocal-fold mobility, airway and aspiration assessment; cross-sectional contrast imaging for cartilage/deep-space/extralaryngeal extent; tissue diagnosis; chest/distant staging when appropriate; and careful baseline swallowing, pulmonary, nutritional, performance, renal, and hearing assessment before chemoradiation. A technically stage-eligible patient may still be a poor organ-preservation candidate if pretreatment function is already severely compromised.",
            "Early disease may be treated with radiation or transoral/open partial laryngeal surgery according to site and functional goals. For appropriately selected advanced disease, concurrent chemoradiation is a standard organ-preservation strategy. Primary total laryngectomy remains appropriate when tumor extent, airway compromise, aspiration/nonfunctional larynx, contraindication to definitive chemoradiation, or expected salvage risk makes preservation unlikely to achieve a useful organ. Salvage laryngectomy after radiation failure carries substantially higher wound and fistula risk than primary surgery.",
            "When surgery is chosen, partial-laryngeal procedures require adequate residual framework, pulmonary reserve, swallowing potential, and clear margins; violating these functional prerequisites converts a 'voice-saving' operation into prolonged aspiration or airway dependence. Total laryngectomy requires deliberate separation of airway and alimentary tract, secure pharyngeal closure, stomal construction, thyroid/parathyroid and carotid awareness, and a voice-rehabilitation plan (TEP/electrolarynx/esophageal speech). In salvage settings, consider vascularized tissue reinforcement when fistula risk is high.",
            "Boards/chief framework: organ preservation means functional organ preservation. Chemoradiation is not automatically superior because the larynx remains anatomically present. Ask three questions: can the tumor be controlled, can the patient tolerate treatment, and is the larynx likely to remain functional afterward? A severely aspirating, fixed, destroyed larynx may be better treated with primary laryngectomy than with a preservation strategy that preserves only anatomy.",
            ["larynx preservation", "organ preservation", "chemoradiation", "total laryngectomy", "salvage laryngectomy", "aspiration", "cartilage invasion"],
            ["NCCN Head & Neck v2.2026", "Pasha 6e", "KJ Lee 12e"],
        ),
    ],

    "Thyroid / Parathyroid / Salivary": [
        _entry(
            ["Hungry Bone / Post-Thyroid Calcium Management", "Hungry Bone Syndrome", "Postoperative Hypocalcemia"],
            "Postoperative hypocalcemia after thyroid/parathyroid surgery has several mechanisms and should not be treated as one diagnosis. After thyroidectomy, transient hypoparathyroidism from devascularization/manipulation is common; permanent hypoparathyroidism is less common. After parathyroidectomy for severe hyperparathyroid bone disease, hungry-bone syndrome causes rapid skeletal uptake of calcium, phosphate, and magnesium despite removal of the PTH source. Symptoms include perioral/fingertip paresthesias, cramps, carpopedal spasm, QT prolongation, seizures, or laryngospasm in severe cases.",
            "Parathyroid glands depend on delicate vascular supply, commonly from inferior-thyroid-artery branches, so capsular dissection and preservation of viable tissue matter during thyroid surgery. Hungry bone is a systemic skeletal remineralization phenomenon rather than failure to identify a missing gland. The biochemical pattern helps localize the physiology: low calcium with inappropriately low PTH after thyroidectomy suggests hypoparathyroidism; hungry bone after parathyroidectomy often features prolonged hypocalcemia with low phosphate/magnesium and a clinical context of high preoperative bone turnover.",
            "Check postoperative calcium and use early PTH when your institutional pathway supports risk stratification after thyroidectomy. In symptomatic/severe hypocalcemia obtain ionized calcium, magnesium, phosphate, creatinine, ECG when clinically indicated, and serial trends rather than a single value. Before parathyroid surgery, severe hypercalcemia, very high PTH/alkaline phosphatase, osteitis fibrosa/bone disease, and vitamin-D deficiency increase hungry-bone risk and should affect counseling and replacement planning.",
            "Mild/asymptomatic postoperative hypocalcemia is managed with oral calcium, often plus calcitriol when PTH is low or risk is high. Severe symptomatic hypocalcemia requires monitored IV calcium with magnesium correction as needed, followed by oral replacement. Hungry-bone syndrome can require large and prolonged calcium/calcitriol replacement because the sink is the skeleton; do not mistake the ongoing requirement for immediate operative failure. After thyroidectomy, taper replacement according to recovering PTH/calcium rather than leaving every transient patient on indefinite therapy.",
            "Prevention is operative as well as medical: preserve parathyroid blood supply, avoid unnecessary devascularization, and autotransplant clearly devascularized glands when appropriate. After parathyroidectomy, confirm that the intended abnormal gland(s) were addressed using the planned exploration/ioPTH strategy, but distinguish persistent hyperparathyroidism from postoperative hungry bone before rushing back to the neck. Reoperation for a low calcium level alone is inappropriate without biochemical evidence that hyperfunction persists.",
            "Boards/chief framework: postoperative low calcium is a physiology question. Low PTH after thyroidectomy = hypoparathyroid pathway; high-turnover skeleton after successful parathyroidectomy = hungry-bone pathway. Check magnesium because refractory hypocalcemia may not correct until magnesium is restored. Hungry bone can be profound and prolonged even after a technically successful operation.",
            ["hypocalcemia", "hungry bone", "hypoparathyroidism", "PTH", "calcitriol", "magnesium", "parathyroid blood supply"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],

    "Pediatric Otolaryngology": [
        _entry(
            ["AOM / OME / Tympanostomy Decisions", "Acute Otitis Media / Otitis Media with Effusion", "Tympanostomy Tube Decisions"],
            "Separate acute otitis media (AOM) from otitis media with effusion (OME). AOM requires acute symptoms plus middle-ear inflammation/effusion, classically a bulging tympanic membrane or new otorrhea not from OE; OME is fluid without the acute inflammatory syndrome. Recurrent AOM and chronic OME are different decision pathways. In children with speech/language risk, craniofacial disorders, permanent hearing loss, developmental delay, or other at-risk features, the consequence of persistent effusion is greater even when symptoms look mild.",
            "The Eustachian tube ventilates and clears the middle ear; pediatric anatomy and adenoid reservoir/inflammation predispose to dysfunction. Conductive loss from OME reflects impaired tympanic-membrane/ossicular mechanics rather than cochlear injury. Tympanometry helps distinguish pressure/effusion patterns, while a large ear-canal volume with a flat tracing after tube placement suggests a patent tube/perforation rather than persistent closed middle-ear fluid.",
            "Diagnose AOM by pneumatic otoscopy/otoscopy rather than symptoms alone. For persistent OME, document duration, laterality, hearing status, tympanic-membrane structural change, speech/language/developmental risk and school/listening impact. Audiology is important when OME persists or hearing impact is suspected. Do not obtain routine CT for uncomplicated middle-ear effusion. Recurrent AOM candidacy for tubes depends importantly on whether middle-ear effusion is present at the time of assessment rather than episode count alone.",
            "Many uncomplicated AOM episodes can be observed or treated with appropriate antibiotics according to age/severity/follow-up; analgesia matters in all cases. OME is usually observed initially because spontaneous resolution is common. Tympanostomy tubes are favored for chronic bilateral OME with documented hearing difficulty and may be offered for chronic symptomatic OME or recurrent AOM with effusion at assessment; children at developmental risk may merit earlier intervention. Adenoidectomy has a selective role, especially with nasal obstruction/adenoid disease or in older children requiring repeat tube strategies.",
            "Myringotomy should be placed where tube function is durable while avoiding ossicles/chorda and allowing postoperative visualization. Suction only what is needed; thick mucoid fluid may be present but absence of fluid at surgery does not retroactively invalidate the longitudinal indication. Counsel on otorrhea, blockage, premature extrusion, persistent perforation, tympanosclerosis and need for repeat tubes. For uncomplicated acute tube otorrhea, topical drops are generally preferred to routine systemic antibiotics.",
            "Boards/chief framework: do not collapse AOM, recurrent AOM, and chronic OME into one disease. AOM is acute infection/inflammation; OME is fluid without acute infection. Tube decisions are driven by effusion persistence, hearing/developmental impact, and whether recurrent-AOM patients actually have effusion when assessed—not by a memorized episode count alone.",
            ["AOM", "OME", "tympanostomy", "recurrent AOM", "hearing loss", "tympanometry", "tube otorrhea"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],

    "Laryngology / Voice / Swallowing": [
        _entry(
            ["Inducible Laryngeal Obstruction / PVFM", "Paradoxical Vocal Fold Motion / Inducible Laryngeal Obstruction", "PVFM"],
            "Inducible laryngeal obstruction (ILO), historically called paradoxical vocal-fold motion (PVFM), causes inappropriate transient laryngeal narrowing, often during inspiration, producing episodic dyspnea, throat tightness, stridor/noisy breathing, and rapid reversibility. It is commonly mistaken for asthma; clues include inspiratory symptoms, throat localization, abrupt onset/offset, poor response to bronchodilators, and triggers such as exercise, irritants, stress, reflux-associated irritation, or upper-airway hypersensitivity. Asthma and ILO can coexist.",
            "The obstruction is functional/dynamic rather than fixed scar or paralysis. Glottic ILO classically shows inappropriate adduction during inspiration, but supraglottic collapse can also contribute, especially in exercise-induced disease. Because symptoms are intermittent, a normal resting laryngeal exam does not exclude the diagnosis. Fixed bilateral vocal-fold immobility, posterior glottic stenosis, subglottic stenosis, tracheomalacia and neurologic disease must be separated from ILO before labeling symptoms functional.",
            "Flexible laryngoscopy during symptoms is the diagnostic cornerstone; continuous laryngoscopy during exercise is particularly useful for exercise-induced ILO. Spirometry may show inspiratory loop flattening but can be normal between attacks and is not definitive. Evaluate asthma objectively when suspected rather than assuming all wheeze/shortness of breath is pulmonary or all stridor is ILO. History should identify triggers, voice use, reflux/rhinitis, anxiety/stress physiology, prior intubation, and red flags for fixed airway disease.",
            "First-line treatment is education plus respiratory retraining/laryngeal control therapy with a speech-language pathologist, including relaxed-throat and rescue-breathing techniques. Treat relevant comorbid contributors such as asthma, rhinitis, reflux-associated irritation, or behavioral stress without implying the disorder is imaginary. Acute episodes usually respond to coached breathing and removal of trigger; unnecessary intubation can be avoided when oxygenation is preserved and the diagnosis is secure. Refractory cases require reassessment of the diagnosis before escalating therapy.",
            "ILO is generally not a surgical disease. Surgery is reserved for a different demonstrated structural problem or selected supraglottic exercise-induced collapse, not for classic glottic PVFM. Botox has been used in highly selected refractory cases but is not routine because transient weakness can worsen voice/swallowing. The operative/chief-level pivot is recognizing when 'refractory PVFM' actually represents posterior glottic stenosis, bilateral paresis, SGS, mass, or another fixed lesion that needs a different pathway.",
            "Boards/chief framework: episodic inspiratory obstruction with rapid reversibility and poor bronchodilator response should trigger ILO, but prove the dynamic narrowing when possible. Laryngoscopy during symptoms is more valuable than a normal resting exam. Treat with breathing retraining and comorbidity control; do not repeatedly intubate or operate on a functional dynamic disorder without evidence of fixed obstruction.",
            ["ILO", "PVFM", "vocal cord dysfunction", "exercise", "continuous laryngoscopy", "stridor", "speech therapy"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],

    "Facial Plastics / Trauma": [
        _entry(
            ["Frontal Sinus Fracture Decision Model", "Frontal Sinus Fracture"],
            "Frontal-sinus fracture management is driven by four questions: anterior-table contour injury, posterior-table/dural injury, frontal sinus outflow-tract (FSOT) injury, and CSF leak—not by the label 'frontal sinus fracture' alone. Anterior-table injury mainly threatens contour; posterior-table injury raises intracranial/dural risk; FSOT obstruction creates long-term mucocele/mucopyocele risk. Pneumocephalus, CSF rhinorrhea, neurologic injury, or severe comminution changes urgency and multidisciplinary needs.",
            "The frontal sinus drains through the frontal recess into the middle meatus; trauma can disrupt this narrow outflow pathway even when the sinus itself remains aerated initially. Posterior table separates sinus from anterior cranial fossa and dura. Interfrontal septum, supraorbital rims, nasofrontal region, anterior ethmoid/frontal recess and skull base should be reviewed together because associated NOE/skull-base injuries often determine the actual operation.",
            "Thin-cut CT with multiplanar review defines table displacement/comminution, FSOT region, pneumocephalus and associated facial/skull-base fractures. Examine forehead contour, frontal-branch function, ocular status and CSF leak. Persistent leak or concern for intracranial injury requires neurosurgical/skull-base coordination. Because FSOT injury can be difficult to infer from one scan, follow-up imaging/endoscopy is part of observation strategies to confirm sinus ventilation rather than assuming patency.",
            "Observation is appropriate for many nondisplaced fractures with a functioning outflow tract and no significant CSF/intracranial issue. Anterior-table repair is mainly for meaningful cosmetic deformity or selected open/comminuted injuries. FSOT injury may require endoscopic frontal-sinus management, sinus obliteration, or other drainage strategy depending on anatomy and ability to maintain long-term ventilation. Severe posterior-table/dural injury may require cranialization, but not every posterior-table fracture automatically needs it.",
            "If repairing the anterior table, restore stable forehead contour while protecting the supraorbital nerves and avoiding hardware exposure. When obliterating a sinus, remove mucosa meticulously and permanently exclude/occlude the outflow tract because retained mucosa can form a mucocele. Cranialization removes the posterior table and incorporates the sinus into the intracranial space after complete mucosal removal and dural separation/repair. Modern endoscopic frontal-sinus techniques have reduced the need for automatic obliteration/cranialization in selected injuries, so choose the least morbid strategy that reliably addresses contour, CSF/dura, and drainage.",
            "Boards/chief framework: anterior table = contour; posterior table = dura/brain; FSOT = future sinus function. A normal-looking forehead does not rule out a dangerous posterior/FSOT injury, and a posterior-table fracture does not automatically mandate cranialization. Long-term mucocele risk is why surveillance/ventilation matters even after the acute trauma has healed.",
            ["frontal sinus fracture", "anterior table", "posterior table", "FSOT", "cranialization", "obliteration", "CSF leak", "mucocele"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],

    "Sleep Surgery": [
        _entry(
            ["Residual OSA After Surgery", "Pediatric Residual OSA", "Residual OSA"],
            "Residual OSA means clinically meaningful obstructive disease persists after an intervention that was expected to improve it; it is especially common after adenotonsillectomy in children with obesity, craniofacial disorders, neuromuscular disease, Down syndrome, severe baseline OSA, or multilevel obstruction. Persistent snoring alone does not quantify residual disease, and symptom improvement does not prove normalization. In adults, residual disease after palate/tongue-base/skeletal surgery likewise requires objective reassessment.",
            "Residual obstruction is often multilevel. Potential sites include adenoid regrowth, residual tonsillar tissue, velum, lateral pharyngeal walls, tongue base/lingual tonsils, epiglottis/supraglottis, nasal obstruction and craniofacial restriction. Obesity and low neuromuscular tone can worsen collapsibility without a single surgically removable lesion. The key localization question is whether persistent OSA is driven by a correctable anatomic site, global collapsibility, weight, or a combination.",
            "Repeat polysomnography when severity/risk or persistent symptoms warrant objective assessment; interpret more than AHI alone, including oxygen burden, CO2/hypoventilation, REM/position effects and central events. Perform targeted awake endoscopy and consider DISE when another procedure is contemplated and the collapse site is uncertain. In children, assess lingual tonsils, nasal/adenoid status, craniofacial anatomy and obesity; in syndromic patients, avoid assuming adenotonsillectomy was expected to cure multilevel disease.",
            "Management is phenotype-directed: PAP remains highly effective when tolerated; weight management and medical treatment of nasal inflammation are important adjuncts; orthodontic/craniofacial therapy, lingual tonsillectomy, supraglottoplasty, palate/tongue-base procedures, HNS in appropriately selected populations, or skeletal surgery are considered when a corresponding obstruction is demonstrated. Do not automatically repeat the same operation because the first surgery helped only partially.",
            "Before revision surgery, identify the residual collapse mechanism and decide what success means—cure, clinically meaningful AHI reduction, oxygen improvement, PAP-pressure reduction, or symptom benefit. DISE-directed surgery should target the observed site while preserving swallowing/voice. In pediatric residual OSA, lingual tonsillectomy is reasonable when hypertrophy contributes; supraglottoplasty is for demonstrated sleep-dependent laryngomalacia, not generic residual OSA. Multilevel disease may require staged or combined treatment.",
            "Boards/chief framework: residual OSA is not 'failed surgery'; it is a new phenotype-assessment problem. Re-measure severity, re-localize obstruction, and choose the next therapy from the residual mechanism. AHI improvement without normalization can still matter clinically, but you should never assume cure from symptoms alone.",
            ["residual OSA", "adenotonsillectomy", "DISE", "lingual tonsil", "PAP", "multilevel obstruction", "polysomnography"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],

    "General ENT / Emergencies": [
        _entry(
            ["Esophageal Perforation / Cervical Mediastinitis", "Esophageal Perforation", "Cervical Esophageal Perforation"],
            "Cervical esophageal perforation should be suspected after instrumentation, foreign body, trauma, difficult intubation, surgery, or spontaneous rupture when neck/chest pain, odynophagia, dysphagia, fever, crepitus, tachycardia, drainage of saliva, or rapid systemic toxicity develops. Early findings can be subtle. Delay matters because leaked saliva/bacteria can track through deep cervical fascial planes into the mediastinum, converting a local injury into life-threatening descending infection.",
            "The cervical esophagus lies posterior to the trachea and communicates with retropharyngeal/danger-space pathways into the mediastinum. Perforation size, location, containment and surrounding tissue health determine whether contamination remains localized. Prior radiation, malignancy, surgery, caustic injury and delayed diagnosis reduce the chance that a leak will seal uneventfully.",
            "Keep the patient NPO, obtain IV access/labs and start broad-spectrum IV antibiotics covering oral flora when perforation is strongly suspected. Contrast-enhanced CT neck/chest with oral contrast when safe helps define air, fluid collections, mediastinal extension and source; a water-soluble esophagram can demonstrate leak but a negative study does not completely exclude a small perforation when clinical suspicion remains high. Flexible endoscopy is selective because insufflation/manipulation can enlarge an unstable defect, but it can be useful when diagnosis/source remains uncertain and expertise is available.",
            "Small, contained cervical perforations in stable patients without sepsis, distal obstruction or uncontrolled contamination may be managed nonoperatively with NPO, antibiotics, nutritional support and close serial reassessment. Uncontained leak, clinical deterioration, abscess, mediastinal spread, foreign body/obstruction, devitalized tissue or failure of conservative therapy requires source control. Nutrition should bypass the injured segment until healing is established; the exact enteral/parenteral strategy depends on expected duration and operative plan.",
            "Operative priorities are exposure, drainage/debridement of contaminated spaces, closure of a repairable defect without tension, and separation/reinforcement with healthy vascularized tissue when tissue quality is poor or the leak is high risk. SCM or other regional flaps may buttress cervical repairs. Descending mediastinitis can require combined cervical and thoracic drainage. In delayed/radiated/malignant defects, primary closure may be unreliable, so diversion, flap reconstruction, or staged management may be safer than forcing a tenuous repair.",
            "Boards/chief framework: suspected esophageal perforation is a time-to-source-control problem. NPO + antibiotics + imaging happen early, but management hinges on contained versus free leak, sepsis, tissue quality and mediastinal extension. A normal first esophagram does not overrule a toxic patient with cervical emphysema and CT evidence of contamination.",
            ["esophageal perforation", "cervical mediastinitis", "danger space", "NPO", "esophagram", "source control", "SCM flap"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
}


def apply_cross_domain_depth_v163(deep_modules):
    applied, missing = [], []
    for domain, patches in PATCHES_V163.items():
        modules = deep_modules.get(domain, [])
        for patch in patches:
            found = next((m for m in modules if m.get("topic") in patch["candidates"]), None)
            if found is None:
                missing.append((domain, patch["candidates"]))
                continue
            found.update(patch["fields"])
            applied.append((domain, found.get("topic")))
    return {"applied": applied, "missing": missing}
