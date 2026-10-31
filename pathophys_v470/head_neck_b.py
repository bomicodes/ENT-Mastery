"""Head & Neck Oncology (part B): mechanism-level teaching content."""

CONTENT = {
"Cutaneous Squamous Cell Carcinoma of the Head & Neck": dict(
overview=(
"Cutaneous SCC is the second most common skin cancer, driven by UV exposure and dramatically more aggressive in transplant and immunosuppressed patients. "
"High-risk features (size, depth, perineural invasion, poor differentiation, location) predict nodal spread to the parotid and neck."),
physiology=(
"**Epidermal renewal**: basal keratinocytes divide and mature upward into keratinized squames over about a month. "
"**UV defenses**: melanin absorbs UV, and nucleotide excision repair corrects UV-induced pyrimidine dimers before they become fixed mutations. "
"**Immune surveillance**: cytotoxic T cells and NK cells eliminate keratinocytes carrying mutations; this is why immune competence matters so much for skin cancer. "
"**Lymphatic drainage**: scalp, forehead, temple, cheek, and ear skin drain to intraparotid and periparotid nodes, then to levels II-V and occipital nodes. "
"**Cutaneous nerves**: sensory branches of V1-V3 and the facial nerve run in the subcutaneous plane and connect directly to the skull base."),
pathophysiology=(
"**UV mutagenesis**: UVB causes signature C-to-T transitions in TP53, NOTCH1, and other genes, producing actinic keratosis, SCC in situ (Bowen disease), then invasive SCC. "
"**Immunosuppression**: solid-organ transplant recipients have a 65- to 250-fold higher risk because surveillance fails; reducing immunosuppression (or switching to an mTOR inhibitor) is part of treatment. "
"**High mutational burden**: UV-driven tumors carry many neoantigens, which explains why PD-1 blockade (cemiplimab) works well in advanced disease and, since 2025, as adjuvant therapy after surgery and radiation for high-risk disease (C-POST). "
"**Perineural invasion**: tumor tracks along V2, V3, or VII toward the skull base, causing numbness, formication, or facial weakness and late recurrence; MRI neurography maps it. "
"**Parotid metastasis**: periauricular and scalp primaries spread first to parotid nodes, which then require parotidectomy plus neck dissection. "
"**Adjuvant radiation logic**: microscopic disease along nerves and in nodal beds is not removed by surgery, so radiation is added for PNI of named nerves, close margins, and nodal disease."),
),

"Basal Cell Carcinoma of the Head & Neck": dict(
overview=(
"Basal cell carcinoma is the most common cancer in humans, arising on sun-exposed facial skin. "
"It rarely metastasizes but is locally destructive, and Mohs surgery offers the highest cure with tissue sparing."),
physiology=(
"**Basal keratinocytes**: the proliferating layer at the base of the epidermis and hair follicle. "
"**Hedgehog pathway**: a developmental growth signal; the PTCH1 receptor normally inhibits SMO, keeping the pathway off in adult skin. "
"**Embryonic fusion planes**: the nasal ala, nasolabial fold, periorbital and periauricular regions sit where facial processes fused, leaving tissue planes of least resistance. "
"**Tumor-stroma interaction**: epithelial cells depend on signals from surrounding dermal stroma for survival."),
pathophysiology=(
"**Hedgehog activation**: loss-of-function PTCH1 or gain-of-function SMO mutations switch the pathway on; germline PTCH1 causes basal cell nevus (Gorlin) syndrome with jaw keratocysts and early multiple BCCs. "
"**Stromal dependence**: BCC cells need their specific stroma, which is thought to explain the extremely low metastatic rate. "
"**Fusion-plane spread**: tumors extend deeply and silently along embryonic planes, so central-face (\"H-zone\") tumors recur more often after standard excision. "
"**Aggressive histology**: morpheaform, infiltrative, and micronodular subtypes grow in thin strands beyond visible margins, which is why Mohs margin control matters. "
"**Targeted therapy**: SMO inhibitors (vismodegib, sonidegib) shrink locally advanced or metastatic tumors; resistance develops through downstream mutations."),
),

"Cutaneous Melanoma of the Head & Neck": dict(
overview=(
"Cutaneous melanoma of the head and neck has less predictable lymphatic drainage than other sites and is staged by Breslow thickness, ulceration, and nodal status. "
"Sentinel node biopsy and immunotherapy have transformed management."),
physiology=(
"**Melanocytes**: neural crest-derived cells in the basal epidermis that transfer melanin to keratinocytes to shield DNA from UV. "
"**Head and neck lymphatics**: dense and bilateral, draining to parotid, preauricular, occipital, and cervical nodes in patterns that often defy clinical prediction. "
"**Immune checkpoints**: CTLA-4 (during T-cell priming) and PD-1 (in tissues) normally restrain T cells to prevent autoimmunity."),
pathophysiology=(
"**MAPK pathway mutations**: BRAF V600E (about half), NRAS, or NF1 drive proliferation; UV exposure adds a very high mutational burden. "
"**Growth phases**: radial growth along the epidermis (low metastatic risk) gives way to vertical growth into the dermis (metastatic potential). "
"**Breslow thickness and ulceration**: the strongest predictors of nodal and distant spread, which is why they define T-stage. "
"**Sentinel node logic**: drainage is unpredictable, so lymphoscintigraphy identifies the true first-echelon node; it is offered at about 0.8 mm or with ulceration. "
"**Immunotherapy**: the neoantigen load makes melanoma highly responsive to PD-1 and CTLA-4 blockade, now used adjuvantly, neoadjuvantly for resectable stage III disease (SWOG S1801), and in advanced disease; BRAF/MEK inhibitors target BRAF-mutant tumors. "
"**Desmoplastic melanoma**: neurotropic and locally aggressive, often amelanotic on sun-damaged head and neck skin."),
),

"Merkel Cell Carcinoma": dict(
overview=(
"Merkel cell carcinoma is a rare, aggressive neuroendocrine skin cancer of the head and neck in older, sun-exposed, or immunosuppressed patients. "
"It spreads early to nodes and responds well to radiation and immunotherapy."),
physiology=(
"**Merkel cells**: slowly adapting touch-receptor cells in the basal epidermis that synapse with sensory nerve endings. "
"**Neuroendocrine features**: they contain dense-core granules and express neuroendocrine markers. "
"**Viral control**: cellular immunity normally keeps common skin viruses such as Merkel cell polyomavirus in a harmless state. "
"**Immune surveillance**: T cells also eliminate UV-mutated cells."),
pathophysiology=(
"**Two pathways**: about 80 percent are driven by clonally integrated Merkel cell polyomavirus whose truncated large T antigen inactivates Rb; the rest are UV-driven with very high mutational burden. "
"**Rapid growth**: a painless, red-violet, fast-growing nodule (AEIOU: asymptomatic, expanding rapidly, immunosuppressed, older, UV-exposed). "
"**Early nodal spread**: microscopic nodal disease is common even with small primaries, so sentinel node biopsy is standard. "
"**Immunosuppression**: raises risk and worsens prognosis, consistent with immune control of the virus. "
"**Treatment logic**: tumors are highly radiosensitive and respond well to PD-1/PD-L1 inhibitors because of viral antigens or neoantigens; CK20 perinuclear dot staining confirms the diagnosis."),
),

"Recurrent / Metastatic HNSCC": dict(
overview=(
"Recurrent or metastatic HNSCC not amenable to curative surgery or radiation is treated with systemic therapy (immunotherapy with or without chemotherapy) with a focus on quality of life. "
"Selected recurrences remain curable with salvage surgery or reirradiation."),
physiology=(
"**Immune surveillance**: T cells recognize tumor neoantigens presented on MHC class I. "
"**PD-1/PD-L1 checkpoint**: PD-L1 on tumor and immune cells binds PD-1 on activated T cells, switching them off; this normally limits tissue damage during inflammation. "
"**Combined positive score**: counts PD-L1-positive tumor and immune cells relative to tumor cells and predicts benefit from PD-1 blockade. "
"**Treatment-naive vs pretreated tissue**: prior radiation and surgery alter blood supply and immune infiltration."),
pathophysiology=(
"**Immune escape**: tumors upregulate PD-L1, lose MHC, and recruit suppressive cells, allowing progression after initial therapy. "
"**First-line therapy**: pembrolizumab alone (CPS 1 or greater) or with platinum-5-FU improved survival over the EXTREME regimen (KEYNOTE-048). "
"**Durable responses**: a minority achieve long-lasting control because restored T-cell immunity has memory. "
"**Resistance mechanisms**: DNA repair upregulation, EGFR signaling, and anti-apoptotic pathways reduce chemotherapy and cetuximab effectiveness. "
"**Patterns of failure**: locoregional recurrence dominates; distant spread most often goes to lung, then bone and liver. "
"**Curative salvage**: limited locoregional recurrences can be resected, and reirradiation is used selectively."),
),

"Tumor Immunology / Immunotherapy in HNSCC": dict(
overview=(
"Tumor immunology explains how head and neck cancers evade immune attack and how checkpoint inhibitors restore it. "
"Immunotherapy is standard for recurrent and metastatic disease and is moving into neoadjuvant and curative settings."),
physiology=(
"**Cancer-immunity cycle**: antigen release, uptake and presentation by dendritic cells, T-cell priming in nodes, trafficking to tumor, infiltration, recognition, and killing. "
"**Checkpoints**: CTLA-4 dampens priming in lymph nodes; PD-1 dampens effector T cells in tissue. "
"**Tolerance**: checkpoints prevent autoimmunity, which is why blocking them can cause autoimmune toxicity. "
"**Regional nodes**: are where anti-tumor T cells are primed, a reason neoadjuvant immunotherapy before neck dissection is being studied."),
pathophysiology=(
"**Evasion strategies**: PD-L1 upregulation, MHC class I loss, regulatory T cells, myeloid-derived suppressor cells, and immunosuppressive cytokines (TGF-beta, IL-10). "
"**Hot vs cold tumors**: T-cell-inflamed tumors respond better; HPV-positive tumors carry viral antigens and are often more inflamed. "
"**Checkpoint blockade**: anti-PD-1 antibodies (pembrolizumab, nivolumab) release suppressed T cells. "
"**Neoadjuvant rationale**: giving immunotherapy while the tumor and nodes are intact maximizes antigen presentation; KEYNOTE-689 (Uppaluri et al., NEJM 2025) established perioperative pembrolizumab for resectable locally advanced disease with CPS 1 or greater (FDA-approved 2025). "
"**Immune-related adverse events**: thyroiditis and hypothyroidism are among the most common in head and neck patients; colitis, pneumonitis, hepatitis, and hypophysitis are less common but serious."),
),

"Salvage Surgery After Radiation / Chemoradiation": dict(
overview=(
"Salvage surgery treats persistent or recurrent cancer after radiation or chemoradiation. "
"It offers a chance of cure but carries high complication rates because irradiated tissue heals poorly."),
physiology=(
"**Wound healing phases**: hemostasis, inflammation, proliferation (fibroblasts, angiogenesis), and remodeling, all dependent on oxygen delivery. "
"**Angiogenesis**: new capillaries must grow into a wound to support collagen synthesis. "
"**Radiation effects**: progressive obliterative endarteritis, fibroblast dysfunction, and loss of stem cells develop over months to years. "
"**Tissue oxygen**: fibroblast collagen production and neutrophil killing both require adequate oxygen tension."),
pathophysiology=(
"**Hypoxic-hypocellular-hypovascular tissue**: irradiated beds cannot mount normal angiogenesis or collagen deposition, so incisions and mucosal closures break down. "
"**Fistula risk**: pharyngocutaneous fistula occurs in about 29 percent of salvage laryngectomies (Cummings), substantially more often than after primary surgery. "
"**Vascularized flap logic**: pectoralis or free flaps bring nonirradiated tissue with its own blood supply, lowering fistula rates in salvage (meta-analyses support onlay reinforcement). "
"**Detection challenge**: post-radiation edema and fibrosis mask recurrence, so PET-CT around 12 weeks and biopsy of suspicious findings guide timing. "
"**Prognosis**: early recurrence, advanced recurrent stage, and positive margins predict poor outcome after salvage."),
),

"Neck Management by Primary Site": dict(
overview=(
"Neck management depends on the primary site's drainage pattern and occult metastasis risk. "
"Knowing which levels to treat for each site is a core oncologic principle."),
physiology=(
"**Oral cavity**: drains to levels I-III, with the oral tongue capable of skipping to III-IV. "
"**Oropharynx, larynx, hypopharynx**: drain to levels II-IV, plus retropharyngeal (oropharynx, hypopharynx) and VI (hypopharynx, subglottis). "
"**Thyroid**: drains first to the central compartment (VI), then the lateral neck (III-IV) and mediastinum. "
"**Nasopharynx**: drains to retropharyngeal nodes and levels II-V, often bilaterally. "
"**Scalp and posterior skin**: drain to parotid, occipital, and level V nodes."),
pathophysiology=(
"**Elective treatment threshold**: when occult metastasis risk exceeds about 15-20 percent, elective neck dissection or radiation is justified. "
"**Skip metastases**: oral tongue cancers can bypass level I-II, which is why levels III (and IV for tongue) are included. "
"**Bilateral risk**: midline or base-of-tongue, soft palate, supraglottic, and nasopharyngeal primaries require bilateral neck treatment. "
"**Level IIb and V**: rarely involved without level IIa disease in mucosal cancers, so they can be omitted to spare the accessory nerve in the N0 neck. "
"**Extranodal extension**: changes adjuvant therapy rather than the extent of dissection."),
),

"Reconstruction Selection After Head & Neck Ablation": dict(
overview=(
"Reconstruction after head and neck ablation ranges from primary closure to local, regional, and free flaps. "
"Selection depends on defect size, tissue type needed, function, prior radiation, and patient factors."),
physiology=(
"**Reconstructive ladder and elevator**: options range from secondary intention to free tissue transfer; modern practice chooses the simplest option that restores function, sometimes jumping straight to a free flap. "
"**Tissue matching**: replace like with like: thin pliable skin for mucosa, bulk for volume, vascularized bone for mandible continuity. "
"**Axial blood supply**: flaps built on named vessels (radial artery, descending branch of lateral circumflex femoral, peroneal) survive transfer. "
"**Recipient vessels**: facial artery, superior thyroid artery, and internal or external jugular tributaries supply free flaps in the neck."),
pathophysiology=(
"**Free flap advantages**: composite tissue, reliable blood supply, and two-team surgery; success rates exceed 95 percent. "
"**Radial forearm**: thin, pliable, sensate (lateral antebrachial cutaneous nerve) for tongue and floor of mouth. "
"**Anterolateral thigh**: variable bulk for total glossectomy and large defects. "
"**Fibula**: up to about 25 cm of bone for mandible reconstruction, allowing dental implants; requires assessment of leg vascularity. "
"**Irradiated beds**: vascularized tissue resists breakdown and covers exposed vessels. "
"**Patient factors**: peripheral vascular disease, prior surgery, and functional goals determine donor site."),
),

"Osteoradionecrosis of the Jaw": dict(
overview=(
"Osteoradionecrosis is exposed, nonhealing irradiated bone, usually the mandible, persisting for 3 months or more. "
"It is triggered by dental extraction or trauma and managed from conservative care to segmental resection with free fibula reconstruction."),
physiology=(
"**Bone remodeling**: osteoclasts resorb and osteoblasts rebuild bone continuously, directed by osteocytes. "
"**Mandible blood supply**: the inferior alveolar artery provides endosteal flow, supplemented by periosteal vessels; the dense cortical mandible has less collateral supply than the maxilla. "
"**Dentition and mucosa**: thin mucosa over the mandible and teeth that breach it create entry points for injury and infection."),
pathophysiology=(
"**Radiation-induced fibroatrophy**: radiation activates TGF-beta-driven fibrosis, endarteritis, and osteocyte death. "
"**Hypoxic, hypocellular, hypovascular bone (Marx)**: the bone cannot remodel after injury. "
"**Trigger**: extraction, trauma, or ill-fitting dentures expose bone that never heals. "
"**Risk factors**: dose above about 50-60 Gy, mandible within the high-dose field, poor dentition, and smoking. "
"**Progression**: pain, exposed bone, orocutaneous fistula, and pathologic fracture. "
"**Treatment logic**: pentoxifylline-tocopherol (with clodronate) targets the fibrotic process; advanced disease requires resection of all necrotic bone and replacement with vascularized bone. "
"**Prevention**: dental evaluation and extractions before radiation, and fluoride."),
),

"Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy": dict(
overview=(
"A nonfunctional larynx after cancer therapy causes chronic aspiration and recurrent pneumonia. "
"When rehabilitation fails, laryngectomy or laryngotracheal separation can be lifesaving."),
physiology=(
"**Airway protection sequence**: laryngeal elevation, epiglottic inversion, vocal fold and false fold closure, and arytenoid tilting close the airway during each swallow. "
"**Sensory trigger**: superior laryngeal nerve sensation triggers protective cough and the swallow reflex. "
"**Pharyngeal clearance**: base-of-tongue retraction and pharyngeal constriction clear the bolus so residue does not spill into the airway. "
"**Cough clearance**: an effective cough expels aspirated material."),
pathophysiology=(
"**Radiation fibrosis**: stiffens the larynx and pharynx, reducing elevation and constrictor contraction. "
"**Neuropathy**: radiation-induced lower cranial neuropathy reduces sensation and cough, causing silent aspiration. "
"**Chronic aspiration**: leads to pneumonia, malnutrition, and tube dependence. "
"**Surgical logic**: when the larynx cannot protect the airway, separating the airway from the food passage (laryngectomy or laryngotracheal separation) eliminates aspiration."),
),

"Head & Neck Cancer Surveillance / Second Primaries": dict(
overview=(
"Surveillance after head and neck cancer looks for recurrence (most within 2-3 years) and second primaries, especially in smokers. "
"It includes exam, imaging, thyroid function, and survivorship care."),
physiology=(
"**Field cancerization**: carcinogen exposure damages the entire aerodigestive mucosa, creating patches of genetically altered cells. "
"**Clonal expansion**: mutated clones spread across the mucosal field, so cancers can arise at distant sites. "
"**Post-treatment tissue**: radiation and surgery create scar and inflammation that confuse imaging."),
pathophysiology=(
"**Recurrence timing**: most recurrences occur within 2 years, prompting frequent early visits. "
"**Second primary risk**: about 3-5 percent per year, mainly lung, esophagus, and head and neck mucosa, highest in persistent smokers. "
"**Smoking cessation**: reduces second primary risk and improves treatment outcomes. "
"**Post-treatment PET-CT**: a scan around 12 weeks after chemoradiation guides neck management (PET-NECK). "
"**Hypothyroidism**: common after radiation and laryngectomy, requiring TSH monitoring."),
),

"Sinonasal Malignancies": dict(
overview=(
"Sinonasal malignancies include SCC, adenocarcinoma, esthesioneuroblastoma, SNUC, mucosal melanoma, and others; each has distinct behavior. "
"They present late, and treatment combines surgery and radiation with histology-specific systemic therapy."),
physiology=(
"**Anatomic compartments**: nasal cavity, maxillary, ethmoid, frontal, and sphenoid sinuses, separated from orbit and brain by thin bone. "
"**Olfactory epithelium**: specialized neuroepithelium at the cribriform plate, source of esthesioneuroblastoma. "
"**Neural pathways**: V2 runs through the pterygopalatine fossa to foramen rotundum; perineural routes lead to the cavernous sinus. "
"**Lymphatic drainage**: retropharyngeal and level I-II nodes, with relatively low early nodal spread."),
pathophysiology=(
"**Late presentation**: tumors fill air spaces silently, presenting with unilateral obstruction, epistaxis, or neuro-ophthalmic signs. "
"**Spread**: to orbit, skull base, brain, and perineural pathways. "
"**Histology-driven treatment**: esthesioneuroblastoma (Kadish/Hyams grading), SNUC and SMARCB1-deficient carcinomas (WHO 2022; aggressive, induction chemotherapy), and mucosal melanoma (poor prognosis). "
"**Occupational exposure**: wood dust strongly associated with ethmoid adenocarcinoma. "
"**Endoscopic resection**: comparable outcomes to open surgery for selected tumors with negative margins."),
),

"Tracheal Malignancy": dict(
overview=(
"Primary tracheal malignancies are rare, mostly SCC and adenoid cystic carcinoma, and present with progressive dyspnea often misdiagnosed as asthma. "
"Resection with primary anastomosis is preferred when possible."),
physiology=(
"**Structure**: about 10-12 cm of C-shaped cartilage rings with a posterior membranous wall. "
"**Segmental blood supply**: inferior thyroid, bronchial, and other arteries enter laterally in a segmental pattern, so circumferential dissection devascularizes it. "
"**Resectable length**: about half the adult trachea can be resected with neck flexion and release maneuvers. "
"**Airflow physics**: resistance rises steeply as the radius narrows."),
pathophysiology=(
"**Airway narrowing**: symptoms (dyspnea, stridor) appear only when the lumen is reduced by about 50-75 percent. "
"**Misdiagnosis**: wheezing unresponsive to bronchodilators is misread as asthma. "
"**SCC**: smoking-related, often with nodal and distant spread. "
"**Adenoid cystic carcinoma**: slow growing with submucosal and perineural spread beyond visible margins. "
"**Anastomotic tension**: excessive tension causes dehiscence, limiting resection length."),
),

"Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer": dict(
overview=(
"Palliative care addresses symptoms and goals in advanced head and neck cancer, alongside or instead of cancer-directed therapy. "
"Airway, bleeding, pain, nutrition, and communication needs are central."),
physiology=(
"**Function concentration**: breathing, swallowing, speech, and facial identity are all served by the head and neck. "
"**Pain pathways**: nociceptive pain from tissue invasion and neuropathic pain from nerve involvement travel through different mechanisms. "
"**Vascular anatomy**: major vessels lie close to tumor beds and irradiated tissue."),
pathophysiology=(
"**Symptom burden**: pain, dysphagia, airway obstruction, bleeding, secretions, and disfigurement. "
"**Carotid blowout**: sentinel bleeding often precedes major hemorrhage. "
"**Neuropathic pain**: requires agents such as gabapentinoids in addition to opioids. "
"**Goals-concordant care**: early palliative involvement improves quality of life. "
"**Decision-making**: tracheostomy and feeding tubes should match patient goals rather than default."),
),

"Radiation Therapy Principles for Head & Neck Surgeons": dict(
overview=(
"Radiation therapy kills cancer cells through DNA damage, delivered in fractions to exploit differences between tumor and normal tissue. "
"Surgeons need to understand dose, fractionation, IMRT, and toxicity to make joint decisions."),
physiology=(
"**DNA damage**: radiation ionizes water to create free radicals that cause double-strand breaks; cells die mainly at their next mitosis. "
"**Cell-cycle sensitivity**: G2/M cells are most sensitive and late S phase most resistant. "
"**Oxygen effect**: oxygen fixes radical damage, so well-oxygenated cells are 2-3 times more sensitive than hypoxic ones. "
"**Dose units**: definitive head and neck courses deliver about 70 Gy in 2 Gy daily fractions; postoperative courses about 60-66 Gy."),
pathophysiology=(
"**The 4 Rs**: repair (normal tissue repairs between fractions), reassortment (cells move into sensitive phases), repopulation (tumor regrows during gaps), and reoxygenation (hypoxic cells become oxygenated). "
"**Hypoxic resistance**: hypoxic tumor cores resist radiation, contributing to failure. "
"**Treatment interruptions**: allow accelerated repopulation, reducing control by roughly 1 percent per day of prolongation (classic radiobiology estimate; Cummings notes worse outcomes once treatment exceeds about 42 days). "
"**Concurrent cisplatin**: sensitizes tumor cells and improves control. "
"**IMRT**: sculpts dose to spare parotids and swallowing structures, reducing xerostomia. "
"**Late effects**: slowly dividing tissues show damage months to years later."),
),

"Systemic Therapy Foundations in Head & Neck Cancer": dict(
overview=(
"Systemic therapies in head and neck cancer include cytotoxic chemotherapy (cisplatin, carboplatin, taxanes, 5-FU), targeted therapy (cetuximab), and immunotherapy. "
"Knowing mechanisms and toxicities guides patient selection."),
physiology=(
"**Cell division**: cytotoxic drugs target DNA synthesis or mitosis in rapidly dividing cells, including bone marrow, mucosa, and hair follicles. "
"**EGFR signaling**: overexpressed in most HNSCC, driving proliferation through MAPK and PI3K pathways. "
"**Drug clearance**: cisplatin is renally cleared, making kidney function a key eligibility factor. "
"**Cochlear vulnerability**: outer hair cells are sensitive to platinum-induced oxidative stress."),
pathophysiology=(
"**Cisplatin**: forms DNA crosslinks; dose-limiting toxicities are nephrotoxicity, ototoxicity, neuropathy, and nausea. "
"**Carboplatin**: less nephrotoxic and more myelosuppressive; it is less ototoxic than cisplatin, but Cummings notes its ototoxicity is greater than once thought. "
"**Cetuximab**: blocks EGFR; inferior to cisplatin with radiation in HPV-positive disease (De-ESCALaTE, RTOG 1016); causes acneiform rash. "
"**Taxanes**: stabilize microtubules; induction TPF is used in larynx preservation and bulky disease. "
"**Checkpoint inhibitors**: now first-line in recurrent or metastatic disease."),
),

"Free-Flap Monitoring / Compromise / Salvage": dict(
overview=(
"Free-flap monitoring detects vascular compromise early, when take-back can salvage the flap. "
"Venous thrombosis is more common than arterial, and most failures occur within the first 72 hours."),
physiology=(
"**Microvascular anastomosis**: flap artery and vein are sutured or coupled to recipient vessels. "
"**Flap perfusion**: depends on arterial inflow, venous outflow, and systemic pressure. "
"**Endothelial healing**: the anastomosis is most thrombogenic in the first days until endothelium covers it. "
"**Monitoring tools**: color, capillary refill, temperature, pinprick bleeding, and implantable or external Doppler."),
pathophysiology=(
"**Venous congestion**: outflow obstruction makes the flap swollen, purple, with brisk dark bleeding; it progresses to arterial thrombosis. "
"**Arterial insufficiency**: pale, cool flap without bleeding. "
"**Causes**: technical anastomosis errors, kinking, compression by hematoma or tight dressings, and hypotension. "
"**Time dependence**: salvage succeeds when compromise is detected within hours. "
"**No-reflow phenomenon**: prolonged ischemia causes endothelial swelling and leukocyte plugging so flow fails despite revision. "
"**Salvage options**: revision, thrombectomy, thrombolytics, and leeches for venous congestion."),
),

"Open Partial / Conservation Laryngectomy": dict(
overview=(
"Open partial laryngectomy (vertical hemilaryngectomy, supraglottic laryngectomy, supracricoid laryngectomy) removes cancer while preserving speech and swallowing without a permanent stoma. "
"Candidacy depends on tumor extent and pulmonary reserve."),
physiology=(
"**Cricoarytenoid unit**: the cricoid cartilage, an arytenoid, and its muscles and nerves form the minimal functional unit for speech, swallowing, and breathing. "
"**Laryngeal sphincters**: the epiglottis, false folds, and true folds form layered airway protection. "
"**Pulmonary reserve**: patients must cough effectively to clear expected postoperative aspiration. "
"**Horizontal vs vertical anatomy**: the supraglottis and glottis develop separately, so horizontal resections can remove one while preserving the other."),
pathophysiology=(
"**Expected aspiration**: removal of part of the sphincter causes temporary aspiration during swallowing relearning. "
"**COPD**: patients with poor pulmonary reserve cannot tolerate aspiration, making partial laryngectomy contraindicated. "
"**Supraglottic laryngectomy contraindications**: true vocal fold involvement, impaired cord mobility, or anterior commissure extension, since the operation spares the glottis. "
"**Supracricoid laryngectomy**: requires at least one functional cricoarytenoid unit. "
"**Cartilage invasion**: limits partial procedures."),
),

"Transoral Laser Microsurgery for Laryngeal Cancer": dict(
overview=(
"Transoral laser microsurgery removes laryngeal cancers through the mouth with a CO2 laser, preserving function without external incisions. "
"It is used for early glottic and supraglottic cancers and selected advanced tumors."),
physiology=(
"**CO2 laser**: 10,600 nm wavelength absorbed by water, cutting and coagulating with minimal thermal spread. "
"**Laryngeal exposure**: requires a straight line of sight from the mouth to the larynx. "
"**Tissue planes**: the vocal ligament and thyroarytenoid muscle define depth of resection. "
"**Airway fire triangle**: fuel, oxygen, and an ignition source."),
pathophysiology=(
"**Piecemeal resection**: tumors are cut through to see depth, which is oncologically sound when margins are clear. "
"**Exposure limits**: trismus, retrognathia, and limited neck extension prevent adequate exposure. "
"**Airway fire**: laser with oxygen and the endotracheal tube; laser-safe tubes and low oxygen reduce risk. "
"**Anterior commissure**: difficult to expose and margins can be close. "
"**Voice outcomes**: depend on resection depth."),
),

"Complications of Neck Surgery": dict(
overview=(
"Neck surgery complications include hematoma, chyle leak, nerve injuries (spinal accessory, marginal mandibular, hypoglossal, vagus, phrenic), carotid injury, and wound infection. "
"Recognizing them early prevents harm."),
physiology=(
"**Carotid sheath**: carotid artery, internal jugular vein, and vagus nerve. "
"**Thoracic duct**: carries chyle (lymph with chylomicrons) to the left venous angle; it can be bilateral or variable. "
"**Nerves at risk**: spinal accessory (level II and V), marginal mandibular (under platysma near the mandible), hypoglossal (deep to the posterior belly of digastric), phrenic (on anterior scalene). "
"**Venous drainage**: bilateral internal jugular veins drain the brain and face."),
pathophysiology=(
"**Hematoma**: venous and lymphatic obstruction causes laryngeal edema and airway compromise beyond simple compression. "
"**Chyle leak**: thoracic duct injury produces milky drainage high in triglycerides, worsened by dietary fat. "
"**Accessory nerve injury**: trapezius weakness causes shoulder droop and pain. "
"**Bilateral IJV ligation**: facial edema and raised intracranial pressure. "
"**Carotid blowout**: after radiation, infection, or fistula exposure."),
),

"Sentinel Lymph Node Biopsy in Oral Cavity Cancer": dict(
overview=(
"Sentinel lymph node biopsy maps the first draining nodes of early oral cavity cancer and removes only them for staging. "
"It is an alternative to elective neck dissection in the clinically N0 neck."),
physiology=(
"**Lymphatic drainage**: lymph from a tumor travels first to one or a few sentinel nodes. "
"**Radiotracer mapping**: technetium-labeled colloid injected around the primary is taken up by lymphatics and concentrates in sentinel nodes. "
"**Imaging**: lymphoscintigraphy and SPECT-CT localize sentinel nodes before surgery. "
"**Gamma probe**: guides intraoperative identification."),
pathophysiology=(
"**Stepwise spread**: metastases seed the sentinel node first, so a negative sentinel node predicts a negative neck. "
"**Accuracy**: high negative predictive value in early oral cancer, comparable to elective neck dissection for survival in trials. "
"**Shine-through**: radiotracer at the primary obscures nearby nodes, especially floor-of-mouth tumors. "
"**Positive sentinel**: requires completion neck dissection."),
),

"Villaret Syndrome (Retroparotid Space Syndrome)": dict(
overview=(
"Villaret syndrome is CN IX-XII palsies plus Horner syndrome from a lesion in the retroparotid (poststyloid parapharyngeal) space. "
"It points to tumors, infection, or trauma at the skull base."),
physiology=(
"**Retrostyloid space**: contains the internal carotid artery, internal jugular vein, CN IX-XII, and the cervical sympathetic chain. "
"**Sympathetic pathway**: third-order sympathetic fibers travel with the internal carotid to the eye and face. "
"**Lower cranial nerves**: control swallowing, voice, shoulder elevation, and tongue movement."),
pathophysiology=(
"**Combined lower cranial neuropathies**: dysphagia, hoarseness, shoulder weakness, tongue deviation toward the lesion. "
"**Sympathetic involvement**: Horner syndrome (ptosis, miosis, anhidrosis). "
"**Localization**: the combination localizes outside the skull base, distinguishing it from jugular foramen (Vernet) and Collet-Sicard syndromes. "
"**Causes**: metastasis, nasopharyngeal carcinoma, paraganglioma, schwannoma, carotid dissection, and trauma."),
),

"Lip Cancer": dict(
overview=(
"Lip cancer is usually SCC of the lower lip from UV exposure, with BCC more common on the upper lip skin. "
"It has a favorable prognosis, and reconstruction aims to preserve oral competence."),
physiology=(
"**Vermilion**: modified mucosa with thin epithelium, little melanin, and no sweat glands, so it has little UV protection. "
"**Orbicularis oris**: circular sphincter muscle essential for oral competence and speech. "
"**Sensation**: the mental nerve (V3) supplies the lower lip. "
"**Lymphatics**: lower lip drains to submental and submandibular nodes; central lesions drain bilaterally."),
pathophysiology=(
"**UV exposure**: the lower lip receives more direct sun, explaining SCC predominance there. "
"**Actinic cheilitis**: precursor lesion with dysplasia. "
"**Nodal spread**: uncommon but increased in larger or recurrent tumors. "
"**Perineural spread**: along the mental nerve into the mandible. "
"**Reconstruction**: up to about one third of the lip can close primarily; larger defects need flaps (Abbe, Estlander, Karapandzic) that preserve sphincter function."),
),
}
