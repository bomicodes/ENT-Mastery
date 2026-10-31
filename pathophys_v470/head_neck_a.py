"""Head & Neck Oncology (part A): mechanism-level teaching content."""

CONTENT = {
"HPV-Associated Oropharyngeal SCC": dict(
overview=(
"HPV-associated oropharyngeal squamous cell carcinoma arises in the tonsils and base of tongue, driven by high-risk HPV (mostly HPV-16). "
"It is now the most common HPV-related cancer in the US (CDC cancer registry data; Van Dyne et al., MMWR 2018), often presents as a cystic neck mass in a younger nonsmoker, and has a much better prognosis than HPV-negative disease, which is why it has its own staging (AJCC Version 9, current since 2026, which replaced AJCC 8th)."),
physiology=(
"**Lymphoid oropharynx**: the palatine and lingual tonsils make up Waldeyer ring, lymphoid tissue that samples antigens from food and air. "
"**Reticulated crypt epithelium**: tonsillar crypts are lined by a thin, discontinuous epithelium whose basal cells are directly exposed, unlike the intact squamous lining elsewhere. "
"**Tumor suppressors**: p53 halts the cell cycle and triggers apoptosis after DNA damage; Rb holds E2F transcription factors in check, blocking entry into S phase. "
"**Lymphatic drainage**: the tonsils and base of tongue drain mainly to level II, then III, and to retropharyngeal nodes; the base of tongue drains bilaterally."),
pathophysiology=(
"**Viral entry**: HPV reaches the exposed basal cells of reticulated crypt epithelium, largely through oral sexual exposure, where it can persist. "
"**Oncoproteins**: viral E6 degrades p53 and E7 inactivates Rb, releasing E2F and driving uncontrolled proliferation without the mutational burden of tobacco cancers. "
"**p16 surrogate**: Rb loss produces a feedback overexpression of p16INK4a, so strong diffuse p16 immunostaining is a surrogate marker for HPV-driven tumors. "
"**Cystic nodal metastases**: small primaries hidden in crypts metastasize early, producing cystic level II nodes that can be mistaken for branchial cleft cysts. "
"**Better prognosis biology**: tumors have fewer mutations, intact apoptosis pathways that respond to radiation, and an immune-infiltrated microenvironment. "
"**Why separate staging**: traditional nodal staging overestimated risk for HPV-positive disease, so HPV-specific staging groups nodes differently; AJCC Version 9 (in use for diagnoses from 2026) also upstages N1 and N2 by one level for unequivocal clinical or imaging-detected ENE and for pathologic ENE; smoking history still worsens outcomes. "
"**De-escalation questions**: excellent survival has driven trials of reduced-intensity therapy, though cisplatin remains standard over cetuximab."),
),

"Laryngeal SCC": dict(
overview=(
"Laryngeal squamous cell carcinoma is strongly linked to tobacco and alcohol and is divided by subsite: supraglottic, glottic, and subglottic. "
"Subsite determines symptoms, nodal risk, and whether larynx-preserving therapy is possible."),
physiology=(
"**Three functions**: the larynx protects the airway during swallowing, regulates airflow, and produces voice. "
"**Subsites**: supraglottis (epiglottis, aryepiglottic folds, arytenoids, false folds, ventricle), glottis (true folds and commissures), and subglottis (below the glottis to the cricoid). "
"**Embryology and lymphatics**: the supraglottis (from the buccopharyngeal anlage) has rich bilateral lymphatics, the glottis has almost none, and the subglottis drains to paratracheal and prelaryngeal (Delphian) nodes. "
"**Barriers and spaces**: the conus elasticus and quadrangular membrane, the paraglottic and pre-epiglottic spaces, and thyroid cartilage shape tumor spread."),
pathophysiology=(
"**Field cancerization**: tobacco carcinogens and alcohol cause widespread mucosal genetic damage (TP53, CDKN2A, and others), so second primaries are common. "
"**Progression**: hyperplasia, dysplasia, carcinoma in situ, and invasive carcinoma. "
"**Glottic tumors**: cause early hoarseness and rarely spread to nodes, so they are found early and cured at high rates. "
"**Supraglottic tumors**: grow silently until large, causing dysphagia, referred otalgia (through CN X), and early bilateral nodal spread. "
"**Fixed vocal fold**: indicates invasion of the thyroarytenoid muscle, paraglottic space, or cricoarytenoid joint (T3). "
"**Cartilage invasion**: through the outer cortex of thyroid cartilage defines T4a, which favors total laryngectomy over organ preservation."),
),

"Unknown Primary with Cervical Metastasis": dict(
overview=(
"Carcinoma of unknown primary is a metastatic neck node (usually SCC) with no primary found on exam and imaging. "
"Most are hidden HPV-positive oropharyngeal cancers, and a systematic workup finds the primary in a majority."),
physiology=(
"**Predictable drainage**: each mucosal site drains to specific nodal levels, so the involved level points to the likely primary. "
"**Hiding places**: tonsillar crypts and base-of-tongue lymphoid tissue are irregular and deep, where small cancers escape visual inspection. "
"**Nodal levels**: level II and III suggest oropharynx, larynx, or hypopharynx; level V suggests nasopharynx or skin; level IV and supraclavicular suggest below-clavicle or thyroid sources."),
pathophysiology=(
"**Small primary, early nodes**: HPV-positive tumors metastasize while the primary is still tiny. "
"**Biomarkers on the node**: p16/HPV positivity points to the oropharynx; EBV positivity points to the nasopharynx; thyroglobulin points to thyroid. "
"**Workup logic**: PET-CT before biopsy, then examination under anesthesia with directed biopsies, palatine tonsillectomy, and lingual tonsillectomy (often by TORS) increase detection. "
"**Why finding the primary matters**: it allows narrower radiation fields and less mucosal toxicity."),
),

"Neck Dissection": dict(
overview=(
"Neck dissection removes cervical lymph nodes for staging and treatment of head and neck cancer, from selective dissections of specific levels to radical dissection. "
"Its classification is based on which levels and non-lymphatic structures are removed."),
physiology=(
"**Nodal levels**: I (submental and submandibular), II-IV (upper, middle, lower jugular), V (posterior triangle), VI (central), and VII (superior mediastinal). "
"**Key structures**: spinal accessory nerve (crosses level II and V), internal jugular vein, sternocleidomastoid, marginal mandibular nerve, hypoglossal nerve, vagus, phrenic nerve, and thoracic duct. "
"**Lymph flow**: lymph moves in a stepwise, predictable fashion along the jugular chain from upper to lower levels."),
pathophysiology=(
"**Stepwise spread**: tumors seed first-echelon nodes before more distant levels, which justifies selective dissection in the clinically N0 neck. "
"**Occult metastasis risk**: when the risk of hidden nodal disease exceeds about 15-20 percent, elective treatment is recommended. "
"**Extranodal extension**: tumor breaking through the capsule signals aggressive biology and is an indication for adjuvant chemoradiation. "
"**Morbidity follows structures**: spinal accessory nerve injury causes shoulder dysfunction; thoracic duct injury causes chyle leak; bilateral jugular ligation causes facial edema and raised intracranial pressure."),
),

"Oral Tongue SCC": dict(
overview=(
"Oral tongue SCC is one of the most common oral cavity cancers (the most common site in young patients), linked to tobacco and alcohol, but increasingly seen in younger nonsmokers. "
"Depth of invasion drives T-stage and the decision for elective neck dissection, and surgery is primary therapy."),
physiology=(
"**Intrinsic muscle mass**: the oral tongue is a highly mobile muscular organ essential for speech articulation, bolus formation, and swallowing. "
"**Lymphatics**: rich lymphatics drain to levels I-III, and the tip can drain directly to lower levels (skip metastases); near-midline tumors drain bilaterally. "
"**Nerves**: lingual nerve (sensation and taste via chorda tympani) and hypoglossal nerve (motor)."),
pathophysiology=(
"**Depth of invasion**: deeper tumors reach the rich lymphatic network in the muscle, sharply increasing nodal risk, which is why DOI was incorporated into AJCC 8th staging. "
"**Elective neck dissection**: DOI over about 3-4 mm predicts occult nodal disease high enough to justify elective neck dissection, supported by randomized evidence. "
"**Perineural invasion**: spread along the lingual or hypoglossal nerve increases local recurrence and calls for adjuvant therapy. "
"**Function**: resections that remove large tongue volume impair speech and swallowing, guiding reconstruction choice."),
),

"Floor of Mouth SCC": dict(
overview=(
"Floor of mouth SCC arises between the tongue and mandible, near the submandibular ducts and periosteum. "
"Its proximity to bone determines whether marginal or segmental mandibulectomy is needed, and early bilateral nodal spread is common."),
physiology=(
"**Anatomy**: the floor of mouth contains the sublingual glands, Wharton ducts, lingual nerve, and mylohyoid muscle diaphragm. "
"**Mandible relationship**: the alveolar periosteum is close; in edentulous patients, alveolar resorption brings the inferior alveolar canal closer to the surface. "
"**Lymphatics**: drain to level I and II, often bilaterally because of midline position."),
pathophysiology=(
"**Bone invasion routes**: tumor enters the mandible at the alveolar crest (dentate) or through the occlusal surface of resorbed bone (edentulous). "
"**Marginal vs segmental**: periosteal involvement without medullary invasion allows marginal mandibulectomy; frank invasion requires segmental resection. "
"**Duct obstruction**: involvement of Wharton duct causes submandibular swelling that can mimic nodal disease. "
"**Bilateral neck risk**: midline tumors require evaluation of both necks."),
),

"Tonsil SCC": dict(
overview=(
"Tonsil SCC is the most common oropharyngeal cancer subsite, most often HPV-associated. "
"It often presents as a neck mass, and treatment is radiation-based or transoral surgery with adjuvant therapy based on pathology."),
physiology=(
"**Tonsillar fossa**: bounded by anterior and posterior pillars, overlying the superior constrictor muscle. "
"**Parapharyngeal space**: lies just lateral to the constrictor, containing the carotid and cranial nerves. "
"**Lymphatics**: primary drainage to level II (jugulodigastric node), then III and retropharyngeal."),
pathophysiology=(
"**HPV-driven tumors**: arise in crypts and spread early to nodes, with excellent radiation response. "
"**Lateral spread**: invasion through the constrictor into the parapharyngeal space increases morbidity and may preclude TORS. "
"**Pterygoid invasion**: causes trismus and indicates advanced disease. "
"**Bilateral nodes**: unusual for well-lateralized tonsil cancers, which allows ipsilateral radiation in selected cases."),
),

"Base of Tongue SCC": dict(
overview=(
"Base of tongue SCC arises behind the circumvallate papillae, often HPV-associated, and frequently presents with a neck mass or referred otalgia. "
"Its bilateral lymphatics and functional importance in swallowing shape treatment."),
physiology=(
"**Swallowing role**: the base of tongue drives the bolus into the pharynx by retracting against the posterior pharyngeal wall. "
"**Lymphoid tissue**: lingual tonsils, deep and irregular. "
"**Lymphatics**: rich, bilateral drainage. "
"**Sensory innervation**: CN IX supplies sensation and taste, with referred pain to the ear through Jacobson nerve."),
pathophysiology=(
"**Hidden growth**: tumors grow in deep tissue with few early symptoms. "
"**Bilateral nodal spread**: requires bilateral neck treatment. "
"**Dysphagia**: invasion of the tongue base and vallecula impairs bolus propulsion and airway protection. "
"**Extrinsic muscle invasion**: deep muscle invasion indicates T4a disease. "
"**Treatment balance**: radiation or TORS outcomes are similar for survival, so functional outcomes guide choice."),
),

"Supraglottic Cancer": dict(
overview=(
"Supraglottic cancer involves the epiglottis, aryepiglottic folds, false cords, and arytenoids. "
"It presents late with dysphagia and neck nodes because of rich bilateral lymphatics, and treatment ranges from transoral resection to chemoradiation or total laryngectomy."),
physiology=(
"**Airway protection**: during swallowing the epiglottis tilts down, the aryepiglottic folds and false folds close, and the larynx elevates under the tongue base. "
"**Pre-epiglottic space**: a fat-filled space anterior to the epiglottis, connected to the epiglottis by natural cartilage fenestrations. "
"**Paraglottic space**: fat lateral to the ventricle and folds, continuous with the pre-epiglottic space, allowing spread from supraglottis to glottis without mucosal involvement. "
"**Lymphatics**: the supraglottis has rich, bilateral lymphatic channels that drain to levels II and III."),
pathophysiology=(
"**Late symptoms**: tumors grow in a wide airway before obstructing, so dysphagia and otalgia appear late. "
"**Pre-epiglottic invasion**: tumor passes through fenestrations of the epiglottic cartilage into the pre-epiglottic space (T3). "
"**Nodal spread**: early and often bilateral, requiring bilateral neck treatment. "
"**Supraglottic laryngectomy limits**: requires preserved glottic function and adequate pulmonary reserve to tolerate aspiration during recovery."),
),

"Glottic Cancer": dict(
overview=(
"Glottic cancer involves the true vocal folds and presents early with hoarseness. "
"It rarely spreads to nodes, and early disease is cured at very high rates by transoral laser surgery or radiation."),
physiology=(
"**Vocal fold layers**: epithelium, superficial lamina propria (Reinke space), intermediate and deep lamina propria (vocal ligament), and vocalis muscle. "
"**Mucosal wave**: vibration of the cover over the body produces voice. "
"**Lymphatic sparseness**: the true folds have few lymphatics. "
"**Anterior commissure**: Broyles ligament inserts directly into thyroid cartilage."),
pathophysiology=(
"**Early hoarseness**: even small lesions disrupt the mucosal wave, so tumors are found early. "
"**Low nodal risk**: sparse lymphatics mean early glottic cancer rarely needs neck treatment. "
"**Anterior commissure**: Broyles ligament provides a route to cartilage invasion, complicating treatment. "
"**Vocal fold fixation**: indicates paraglottic or thyroarytenoid invasion (T3). "
"**Voice outcomes**: depend on depth of resection or radiation fibrosis."),
),

"Hypopharyngeal Cancer": dict(
overview=(
"Hypopharyngeal cancer arises in the pyriform sinus, postcricoid region, or posterior pharyngeal wall. "
"It presents late, has a high rate of nodal and distant spread, and has the poorest prognosis of laryngopharyngeal cancers."),
physiology=(
"**Subsites**: the pyriform sinuses (lateral gutters beside the larynx), the postcricoid area (behind the cricoid), and the posterior pharyngeal wall. "
"**Swallowing pathway**: food is channeled around the larynx through the pyriform sinuses into the upper esophageal sphincter. "
"**Distensibility**: the hypopharynx is a collapsible muscular tube with loose submucosa, so tumors can grow large before obstructing. "
"**Lymphatics**: very rich, draining to levels II-IV, retropharyngeal, and paratracheal nodes."),
pathophysiology=(
"**Silent spread**: tumors grow submucosally in a distensible space, with symptoms appearing late (dysphagia, otalgia, neck mass). "
"**Submucosal extension**: tumors spread well beyond visible margins, complicating resection. "
"**Nodal and distant metastasis**: common at presentation. "
"**Postcricoid cancer**: associated with iron deficiency (Plummer-Vinson syndrome). "
"**Organ preservation**: induction chemotherapy and chemoradiation can preserve the larynx in selected patients."),
),

"Nasopharyngeal Carcinoma": dict(
overview=(
"Nasopharyngeal carcinoma arises in the fossa of Rosenmüller, is strongly associated with EBV, and is endemic in Southern China and Southeast Asia. "
"It presents with neck nodes, unilateral effusion, or cranial neuropathies, and is treated with chemoradiation."),
physiology=(
"**Fossa of Rosenmüller**: lateral recess behind the torus tubarius, the most common origin. "
"**Eustachian tube**: opens on the lateral nasopharyngeal wall. "
"**Skull-base neighbors**: foramen lacerum, foramen ovale, and cavernous sinus. "
"**Lymphatics**: retropharyngeal (node of Rouvière) and level II and V nodes, often bilateral."),
pathophysiology=(
"**EBV**: viral latent proteins drive proliferation, especially in nonkeratinizing types; plasma EBV DNA tracks tumor burden and response. "
"**Dietary and genetic factors**: salted fish nitrosamines and HLA types contribute in endemic regions. "
"**ET obstruction**: tumor blocks the tube, causing unilateral effusion in an adult. "
"**Cranial nerve involvement**: spread through foramina causes CN V and VI palsies. "
"**Radiosensitivity**: high radiosensitivity makes radiation (with chemotherapy) the primary treatment; induction gemcitabine-cisplatin before chemoradiation improves survival in locoregionally advanced disease, and PD-1 blockade (toripalimab with gemcitabine-cisplatin) is first-line for recurrent or metastatic disease."),
),

"Laryngeal Preservation Decision": dict(
overview=(
"Laryngeal preservation uses chemoradiation or induction chemotherapy to treat advanced laryngeal cancer without total laryngectomy, when a functional larynx is expected. "
"The choice depends on T-stage, cartilage invasion, pretreatment function, and patient priorities."),
physiology=(
"**A functional larynx does three jobs**: it protects the airway during swallowing, allows breathing through the mouth and nose, and produces voice; preservation only makes sense if all three survive treatment. "
"**Radiation biology**: radiation kills dividing tumor cells but also injures mucosa, muscle, nerve, and microvasculature, with late fibrosis and edema emerging over months to years. "
"**Cartilage framework**: the thyroid and cricoid cartilages are relatively radioresistant when intact but are poorly vascularized, so tumor-invaded cartilage responds poorly and is prone to chondronecrosis. "
"**Swallow mechanics**: laryngeal elevation, pharyngeal constriction, and upper esophageal sphincter opening are all vulnerable to radiation-induced fibrosis."),
pathophysiology=(
"**Evidence base**: the VA larynx trial and RTOG 91-11 established that chemoradiation preserves the larynx in many patients without compromising survival. "
"**Cartilage invasion**: T4a disease with cartilage destruction has poor organ preservation outcomes, favoring laryngectomy. "
"**Dysfunctional larynx**: severe pretreatment aspiration or airway compromise means a preserved larynx may be nonfunctional. "
"**Salvage**: failure requires salvage laryngectomy in irradiated tissue, with higher complication rates."),
),

"Total Laryngectomy": dict(
overview=(
"Total laryngectomy removes the larynx and permanently separates the airway from the digestive tract, creating an end tracheostoma. "
"It is used for advanced or recurrent laryngeal and hypopharyngeal cancer, and for a nonfunctional larynx."),
physiology=(
"**Upper airway conditioning**: the nose and pharynx warm, humidify, and filter inspired air before it reaches the trachea. "
"**Glottic functions**: the larynx generates voice, permits a strong cough by closing against subglottic pressure, and stabilizes the chest for lifting (Valsalva). "
"**Separate tracts**: normally the airway and food passage share the pharynx; laryngectomy permanently separates them, so breathing is through the stoma and eating through the neopharynx. "
"**Thyroid and parathyroid neighbors**: the thyroid isthmus and lobes lie on the trachea and are often partially removed or irradiated."),
pathophysiology=(
"**Lost upper airway conditioning**: stoma breathing dries secretions, so heat-moisture exchangers are required. "
"**Lost voice**: requires tracheoesophageal puncture, electrolarynx, or esophageal speech. "
"**Pharyngocutaneous fistula**: impaired healing in irradiated tissue, hypothyroidism, and malnutrition increase fistula rates; vascularized flap reinforcement reduces it in salvage. "
"**Hypothyroidism**: from hemithyroidectomy, radiation, or both; worsens healing. "
"**Stomal stenosis**: wound contracture narrows the stoma."),
),

"Parapharyngeal Space Tumor": dict(
overview=(
"Parapharyngeal space tumors are usually benign: pleomorphic adenomas of the deep parotid (prestyloid) and neurogenic tumors or paragangliomas (poststyloid). "
"Imaging location relative to the styloid predicts histology and surgical approach."),
physiology=(
"**Shape**: an inverted pyramid from the skull base to the hyoid. "
"**Compartments**: the tensor-styloid fascia divides the prestyloid compartment (fat, deep parotid lobe) from the poststyloid compartment (carotid, jugular, CN IX-XII, sympathetic chain). "
"**Neighbors**: tonsil medially, pterygoid muscles laterally."),
pathophysiology=(
"**Prestyloid tumors**: pleomorphic adenoma of deep lobe or minor salivary origin displaces the parapharyngeal fat medially and the carotid posteriorly. "
"**Poststyloid tumors**: schwannomas (vagus, sympathetic) and paragangliomas displace the carotid anteriorly. "
"**Presentation**: oropharyngeal bulge or incidental imaging finding. "
"**Surgical approach**: transcervical for most, with transparotid or mandibulotomy for larger tumors; FNA through the mouth is avoided."),
),

"Carotid Body Paraganglioma": dict(
overview=(
"Carotid body paraganglioma is a vascular neuroendocrine tumor at the carotid bifurcation that splays the internal and external carotids. "
"It is often hereditary (SDH mutations), and management balances observation, surgery, and radiation."),
physiology=(
"**Carotid body**: a small chemoreceptor organ in the adventitia of the carotid bifurcation, among the most highly perfused tissues in the body. "
"**Glomus (type I) cells**: neural crest-derived chief cells sense low oxygen, high CO2, and acidosis and release neurotransmitters onto Hering nerve (CN IX) to increase ventilation. "
"**Sustentacular (type II) cells**: support cells surrounding chief cells in nests (Zellballen). "
"**Hypoxia response**: chronic hypoxia (high altitude, COPD) causes carotid body hyperplasia, linking oxygen sensing to tumor formation."),
pathophysiology=(
"**Pseudohypoxic signaling**: SDH mutations accumulate succinate, stabilizing HIF and driving tumor growth. "
"**Splaying**: tumors grow between the carotids (lyre sign) and wrap vessels. "
"**Shamblin classification**: relationship to the carotid predicts vascular and cranial nerve injury risk. "
"**Catecholamines**: rarely secreting; screening is done before surgery. "
"**Cranial nerve risk**: vagus and hypoglossal injuries are the major surgical morbidity."),
),

"Adverse Pathology and Adjuvant Therapy": dict(
overview=(
"After surgery for head and neck cancer, pathology determines adjuvant therapy: extranodal extension and positive margins call for chemoradiation; other risk factors call for radiation alone. "
"This is one of the most testable decisions in head and neck oncology."),
physiology=(
"**Lymph node capsule**: early metastases grow within the node; breaching the capsule (extranodal extension) places tumor cells in soft tissue outside any surgical plane. "
"**Margins**: the distance from tumor to the cut edge reflects the chance microscopic tumor remains in the patient. "
"**Perineural and lymphovascular spaces**: nerves and lymphatic channels are low-resistance routes along which tumor cells travel beyond visible disease. "
"**Radiosensitization**: cisplatin forms DNA adducts that prevent repair of radiation damage, increasing tumor kill in the radiation field."),
pathophysiology=(
"**High-risk features**: extranodal extension and positive margins predict recurrence; postoperative chemoradiation improves outcomes (RTOG 9501 and EORTC 22931). "
"**Intermediate-risk features**: pT3-T4, N2 or greater, perineural invasion, lymphovascular invasion, and close margins indicate adjuvant radiation. "
"**Timing**: adjuvant therapy should start within about 6 weeks of surgery to prevent repopulation. **Perioperative immunotherapy**: for resectable locally advanced HNSCC with PD-L1 CPS 1 or greater, KEYNOTE-689 (Uppaluri et al., NEJM 2025; FDA-approved 2025) adds neoadjuvant pembrolizumab before surgery and continues it with adjuvant radiation or chemoradiation. "
"**HPV-positive disease**: some risk features carry less weight, which is under study."),
),

"Head & Neck Radiation Toxicity / Survivorship": dict(
overview=(
"Radiation toxicity is acute (mucositis, dermatitis) or late (xerostomia, fibrosis, dysphagia, osteoradionecrosis, hypothyroidism, carotid disease). "
"Survivorship care manages these effects and surveils for recurrence."),
physiology=(
"**Radiation biology**: radiation causes DNA damage that kills dividing cells. "
"**Early-responding tissues**: rapidly dividing mucosa and skin. "
"**Late-responding tissues**: slowly dividing tissues such as connective tissue and vessels. "
"**Salivary glands**: serous acinar cells are especially radiosensitive."),
pathophysiology=(
"**Mucositis**: epithelial cell death outpaces renewal, causing ulceration and pain. "
"**Xerostomia**: acinar cell loss and fibrosis reduce saliva, increasing dental caries and dysphagia. "
"**Fibrosis**: TGF-beta driven fibroblast activation (Martin et al., Int J Radiat Oncol Biol Phys 2000) causes trismus, neck stiffness, and dysphagia. "
"**Endarteritis**: small-vessel damage reduces tissue perfusion and healing (osteoradionecrosis). "
"**Hypothyroidism**: thyroid gland damage. "
"**Prevention**: IMRT spares salivary glands, swallowing exercises preserve function, and fluoride protects teeth."),
),

"TEP and Alaryngeal Speech": dict(
overview=(
"Tracheoesophageal puncture with a voice prosthesis is the most effective method of voice restoration after total laryngectomy. "
"Electrolarynx and esophageal speech are alternatives."),
physiology=(
"**Normal phonation**: lung air passes through adducted vocal folds, which vibrate to create sound that the pharynx, mouth, and nose then shape into speech. "
"**After laryngectomy**: the vocal folds are gone and the trachea opens at the stoma, so lung air no longer reaches the pharynx. "
"**Pharyngoesophageal (PE) segment**: the reconstructed cricopharyngeus and inferior constrictor can vibrate like a substitute glottis when air passes through it. "
"**Power source**: lung air provides a large, sustained airflow, which is why TEP voice is more fluent than esophageal speech that uses only a small swallowed air reservoir."),
pathophysiology=(
"**TEP mechanism**: a one-way valve between trachea and esophagus lets lung air flow into the pharynx when the stoma is occluded, vibrating the pharyngoesophageal segment. "
"**Pharyngeal spasm**: hypertonicity of the PE segment prevents fluent speech; treated with botulinum toxin or myotomy. "
"**Prosthesis leakage**: valve failure or puncture enlargement allows aspiration. "
"**Fungal colonization**: Candida degrades the valve."),
),

"Neck Lymphoma": dict(
overview=(
"Lymphoma is a common cause of neck masses, especially in younger patients (Hodgkin) and older patients (non-Hodgkin). "
"Diagnosis requires tissue architecture, usually by core or excisional biopsy rather than FNA alone."),
physiology=(
"**Lymph node architecture**: an outer cortex with B-cell follicles and germinal centers, a paracortex rich in T cells, and a medulla with plasma cells, all fed by afferent lymphatics. "
"**Germinal centers**: B cells undergo somatic hypermutation and class switching, a process that occasionally produces oncogenic errors (translocations). "
"**Waldeyer ring**: tonsils, adenoids, and lingual tonsil are extranodal lymphoid tissue in direct contact with antigens. "
"**Reactive vs neoplastic**: reactive nodes contain mixed polyclonal cells, whereas lymphoma is a clonal population that effaces normal architecture."),
pathophysiology=(
"**Clonal proliferation**: B or T lymphocytes proliferate clonally from genetic alterations. "
"**Hodgkin lymphoma**: Reed-Sternberg cells in an inflammatory background, often contiguous spread. "
"**Non-Hodgkin lymphoma**: diverse subtypes with extranodal involvement. "
"**B symptoms**: fevers, night sweats, and weight loss from cytokines. "
"**Why architecture matters**: classification requires node structure plus flow cytometry."),
),
}
