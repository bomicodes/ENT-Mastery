"""General ENT / Emergencies (part B): mechanism-level teaching content."""

CONTENT = {
"ENT Fluids / Electrolytes / Nutrition": dict(
overview=(
"Fluid, electrolyte, and nutrition management matters in head and neck surgery, where patients often start malnourished and may develop SIADH, diabetes insipidus, refeeding syndrome, or hypocalcemia. "
"Getting these right prevents wound breakdown, fistula, and arrhythmia."),
physiology=(
"**Body water compartments**: about 60 percent of body weight is water, two-thirds intracellular and one-third extracellular. "
"**Sodium and water balance**: ADH from the posterior pituitary controls free water reabsorption; serum sodium reflects water balance more than sodium content. "
"**Calcium regulation**: PTH and vitamin D maintain ionized calcium. "
"**Nutritional needs**: roughly 25-30 kcal/kg/day and 1.2-1.5 g/kg/day of protein after major surgery. "
"**Gut function**: enteral feeding maintains gut barrier and immunity."),
pathophysiology=(
"**Malnutrition**: head and neck cancer impairs swallowing and increases catabolism, raising fistula and wound complications. "
"**Refeeding syndrome**: after starvation, carbohydrates trigger insulin release and intracellular shift of phosphate, potassium, and magnesium, causing hypophosphatemia, arrhythmia, and heart failure. "
"**SIADH**: inappropriate ADH after pituitary surgery, pain, or medications causes hyponatremia. "
"**Diabetes insipidus**: ADH deficiency after skull-base surgery causes dilute polyuria and hypernatremia. "
"**Post-thyroidectomy hypocalcemia**: parathyroid injury. "
"**Enteral over parenteral**: whenever the gut works, enteral nutrition reduces infection."),
),

"Antimicrobial Stewardship in Otolaryngology": dict(
overview=(
"Antimicrobial stewardship applies the right drug, dose, and duration to reduce resistance, adverse effects, and C. difficile. "
"Otolaryngology prescribes many antibiotics, especially for otitis, sinusitis, and pharyngitis, much of which is unnecessary."),
physiology=(
"**Microbiome**: normal flora protect against pathogens through colonization resistance. "
"**Antibiotic pharmacology**: time-dependent killing (beta-lactams) vs concentration-dependent killing (aminoglycosides, fluoroquinolones). "
"**Topical delivery**: achieves high local concentrations."),
pathophysiology=(
"**Resistance selection**: antibiotics kill susceptible bacteria, selecting resistant organisms. "
"**Viral infections**: most sore throats, colds, and acute rhinosinusitis are viral. "
"**Collateral damage**: C. difficile infection and microbiome disruption. "
"**Stewardship strategies**: watchful waiting in AOM and ABRS, topical over oral therapy for otitis externa and tube otorrhea, narrow-spectrum agents, and short courses. "
"**Perioperative prophylaxis**: single preoperative dose for clean-contaminated cases."),
),

"Cranial Nerve Examination / Skull Base Localization": dict(
overview=(
"Combinations of cranial nerve deficits localize lesions to the brainstem, skull base foramina, or extracranial spaces. "
"Recognizing patterns is essential in otolaryngology."),
physiology=(
"**Cranial nerve exits**: cribriform plate (I), optic canal (II), superior orbital fissure (III, IV, V1, VI), foramen rotundum (V2), foramen ovale (V3), IAC (VII, VIII), jugular foramen (IX, X, XI), hypoglossal canal (XII). "
"**Brainstem organization**: midbrain (III, IV), pons (V-VIII), medulla (IX-XII)."),
pathophysiology=(
"**Cavernous sinus syndrome**: III, IV, V1, V2, VI and sympathetics. "
"**Orbital apex syndrome**: II plus III, IV, V1, VI. "
"**Gradenigo syndrome**: V and VI with otitis. "
"**CPA syndrome**: V, VII, VIII. "
"**Vernet syndrome**: IX, X, XI at the jugular foramen. "
"**Collet-Sicard**: IX-XII. "
"**Villaret**: IX-XII plus Horner."),
),

"ENT Imaging Fundamentals": dict(
overview=(
"CT, MRI, ultrasound, and PET each answer different questions in otolaryngology. "
"Choosing the right test and reading key findings drives diagnosis."),
physiology=(
"**CT**: X-ray attenuation, excellent for bone (temporal bone, sinuses, fractures). "
"**MRI**: proton relaxation, excellent for soft tissue, nerves, and marrow; T1 shows fat bright; T2 shows fluid bright; gadolinium shows enhancement. "
"**Ultrasound**: sound wave reflection, excellent for thyroid and superficial lesions. "
"**PET**: FDG uptake reflects glucose metabolism."),
pathophysiology=(
"**Bone erosion vs remodeling**: aggressive erosion suggests malignancy or infection; smooth remodeling suggests slow growth. "
"**Restricted diffusion**: cholesteatoma, epidermoid, and abscess. "
"**Enhancement**: tumors and inflammation. "
"**Signal patterns**: cholesterol granuloma T1 and T2 bright; fungal concretions T2 dark. "
"**PET false positives**: inflammation after radiation."),
),

"Wound Healing / Scar Biology in Head & Neck Surgery": dict(
overview=(
"Wound healing in the head and neck is generally favorable due to rich blood supply, but radiation, malnutrition, diabetes, smoking, and hypothyroidism impair it. "
"Understanding healing phases guides closure and scar management."),
physiology=(
"**Hemostasis**: platelets form a plug and release growth factors. "
"**Inflammation**: neutrophils then macrophages clear debris and orchestrate repair. "
"**Proliferation**: fibroblasts lay down collagen III, angiogenesis, and epithelialization. "
"**Remodeling**: collagen I replaces III over months; scars reach about 80 percent strength. "
"**Oxygen dependence**: collagen synthesis requires oxygen."),
pathophysiology=(
"**Radiation**: endarteritis and fibrosis impair healing. "
"**Smoking**: vasoconstriction and carbon monoxide reduce oxygen delivery. "
"**Malnutrition**: protein and vitamin C deficiency impair collagen. "
"**Diabetes**: impaired immunity and microvascular disease. "
"**Hypothyroidism**: increases fistula risk. "
"**Steroids**: impair inflammation; vitamin A partly reverses."),
),

"Grafts / Implants / Biomaterials in ENT": dict(
overview=(
"Autografts, allografts, xenografts, and alloplastic implants are used to reconstruct cartilage, bone, and soft tissue in otolaryngology. "
"Choice balances biocompatibility, resorption, infection, and extrusion."),
physiology=(
"**Graft take**: grafts survive by plasmatic imbibition, then inosculation and revascularization from the recipient bed. "
"**Cartilage biology**: avascular, nourished by diffusion; chondrocytes survive transplantation if not crushed. "
"**Bone healing**: osteoconduction (scaffold), osteoinduction (growth signals such as BMPs), and osteogenesis (living cells). "
"**Foreign body response**: implants are encapsulated by fibrous tissue."),
pathophysiology=(
"**Autografts**: lowest infection and rejection but donor morbidity. "
"**Alloplasts**: silicone, porous polyethylene, and titanium; risk of infection and extrusion, especially in thin or irradiated tissue. "
"**Resorption**: crushed cartilage and nonvascularized bone resorb. "
"**Biofilms**: form on implants."),
),

"Systemic / Granulomatous Disease Manifestations in ENT": dict(
overview=(
"Granulomatous and systemic diseases (GPA, sarcoidosis, EGPA, TB, syphilis, relapsing polychondritis, IgG4-related disease) often present in the head and neck. "
"Biopsy and serology guide systemic therapy."),
physiology=(
"**Granuloma formation**: macrophages aggregate and transform into epithelioid and giant cells in response to persistent antigens. "
"**Small-vessel supply**: nasal mucosa, middle ear, and larynx have rich microvasculature."),
pathophysiology=(
"**GPA**: ANCA (PR3) necrotizing vasculitis causes sinonasal crusting, saddle nose, otitis, subglottic stenosis. "
"**Sarcoidosis**: noncaseating granulomas; parotid and facial nerve involvement (Heerfordt syndrome). "
"**EGPA**: asthma, eosinophilia, and polyps. "
"**TB**: caseating granulomas; scrofula. "
"**IgG4-related disease**: fibroinflammatory enlargement of salivary glands."),
),

"Laser / Energy Safety in Otolaryngology": dict(
overview=(
"Lasers and electrosurgical devices are common in airway and head and neck surgery, creating risks of airway fire, eye injury, and tissue damage. "
"Safety protocols prevent catastrophic events."),
physiology=(
"**Wavelength and chromophore**: CO2 laser (10,600 nm) is absorbed by water, KTP (532 nm) by hemoglobin, and Nd:YAG (1064 nm) penetrates deeply. "
"**Thermal zones**: tissue is vaporized at the center, coagulated around it, and heated at the periphery. "
"**Electrosurgery**: monopolar current passes through the patient to a return pad; bipolar current passes between tips. "
"**Combustion**: requires fuel, oxidizer, and ignition."),
pathophysiology=(
"**Fire triangle**: fuel (endotracheal tube, drapes), oxidizer (oxygen, nitrous oxide), and ignition. "
"**Airway fire**: laser strikes an endotracheal tube in an oxygen-rich environment. "
"**Prevention**: lowest oxygen concentration, laser-safe tubes, saline-filled cuffs. "
"**Eye protection**: wavelength-specific goggles."),
),

"Common ENT Consult Triage / Disposition": dict(
overview=(
"ENT consult triage prioritizes airway threats, bleeding, vision-threatening and intracranial complications, and time-sensitive conditions such as SSNHL. "
"Recognizing red flags determines disposition."),
physiology=(
"**Airway geometry**: the narrowest points are the glottis in adults and the subglottis in children, where small changes cause obstruction. "
"**Time-critical tissues**: the cochlea, optic nerve, and facial nerve tolerate ischemia or compression poorly. "
"**Blood volume**: children have small blood volumes, making bleeding more dangerous. "
"**Infection spread**: fascial planes and valveless veins allow rapid spread."),
pathophysiology=(
"**Airway red flags**: stridor, drooling, tripod positioning, voice change, and inability to handle secretions point to supraglottic or laryngeal obstruction. "
"**Vision threats**: proptosis, reduced acuity, afferent pupillary defect, and ophthalmoplegia in sinusitis or trauma. "
"**Bleeding**: posterior epistaxis and post-tonsillectomy bleeding cause hypovolemia and aspiration. "
"**Time-sensitive**: SSNHL (steroids), Bell palsy (steroids within 72 hours), button battery (minutes to hours), septal hematoma (cartilage necrosis), and retrobulbar hematoma. "
"**Disposition logic**: unstable airway or progressive infection requires admission and OR; uncomplicated cases can be managed outpatient."),
),

"Evidence Interpretation / Outcomes Research": dict(
overview=(
"Evidence interpretation (study design, bias, statistics, and clinical practice guidelines) lets clinicians evaluate literature and apply it. "
"It is tested on boards and essential for practice."),
physiology=(
"**Evidence hierarchy**: systematic reviews of randomized trials sit at the top, then RCTs, cohort studies, case-control studies, case series, and expert opinion. "
"**Test characteristics**: sensitivity (true positive rate) and specificity (true negative rate) are properties of the test. "
"**Predictive values**: positive and negative predictive values depend on disease prevalence. "
"**Likelihood ratios**: combine sensitivity and specificity to update pretest probability."),
pathophysiology=(
"**Bias**: selection bias, measurement bias, and confounding distort associations; randomization and blinding reduce them. "
"**Prevalence effect**: in low-prevalence populations, even good tests produce many false positives. "
"**Absolute vs relative risk**: relative risk reductions can exaggerate benefit; NNT equals 1 divided by absolute risk reduction. "
"**Type I and type II errors**: false positives (alpha) and false negatives (beta, related to power). "
"**Guidelines**: AAO-HNS CPGs grade evidence and strength of recommendation."),
),

"Pain Management in the Head & Neck Patient": dict(
overview=(
"Pain management in head and neck patients combines multimodal analgesia, neuropathic agents, and opioid stewardship. "
"Post-tonsillectomy, cancer, and post-radiation pain each need tailored approaches."),
physiology=(
"**Nociception**: tissue injury activates peripheral nociceptors that signal through trigeminal, glossopharyngeal, vagal, and cervical nerves. "
"**Central processing**: the trigeminal nucleus caudalis and dorsal horn modulate pain. "
"**Neuropathic pain**: arises from nerve injury or tumor invasion with abnormal firing. "
"**Drug metabolism**: codeine and tramadol are activated by CYP2D6."),
pathophysiology=(
"**Multimodal analgesia**: acetaminophen, NSAIDs, and local anesthetics reduce opioid needs. "
"**Codeine and tramadol in children**: ultrarapid CYP2D6 metabolizers risk fatal respiratory depression; contraindicated after pediatric tonsillectomy. "
"**Neuropathic pain**: gabapentinoids. "
"**Opioid stewardship**: limit prescriptions."),
),

"Geriatric Otolaryngology / Frailty": dict(
overview=(
"Older adults have presbycusis, presbyphonia, dysphagia, balance disorders, and higher surgical risk from frailty. "
"Frailty assessment predicts outcomes better than age."),
physiology=(
"**Declining physiologic reserve**: cardiopulmonary, renal, and muscle reserve fall with age, reducing tolerance of surgical stress. "
"**Sensory aging**: hearing (presbycusis), vision, vestibular function, and proprioception decline together. "
"**Swallowing aging (presbyphagia)**: slower swallow triggering and reduced pharyngeal strength. "
"**Pharmacology**: altered drug metabolism and polypharmacy increase adverse effects."),
pathophysiology=(
"**Frailty phenotype**: unintentional weight loss, weakness, exhaustion, slow gait, and low activity predict complications, delirium, and mortality better than age. "
"**Postoperative delirium**: anesthesia, opioids, sleep disruption, and sensory deprivation precipitate it. "
"**Aspiration**: presbyphagia and neurologic disease increase pneumonia risk. "
"**Falls**: vestibular and sensory loss combine with medications to increase fall risk. "
"**Hearing loss**: linked to social isolation and cognitive decline. "
"**Care logic**: frailty screening, prehabilitation, and shared decision-making."),
),

"Immunocompromised Host in Otolaryngology": dict(
overview=(
"Immunocompromised patients (transplant, chemotherapy, HIV, diabetes) face unusual and aggressive ENT infections and malignancies. "
"Lower thresholds for imaging and biopsy are needed."),
physiology=(
"**Innate immunity**: neutrophils and macrophages kill bacteria and fungi; neutropenia is the main risk for invasive fungal infection. "
"**Cell-mediated immunity**: T cells control viruses (HSV, VZV, CMV), mycobacteria, and tumor surveillance. "
"**Humoral immunity**: antibodies opsonize encapsulated bacteria. "
"**Barriers**: intact mucosa and skin."),
pathophysiology=(
"**Invasive fungal sinusitis**: neutropenia and DKA allow angioinvasive fungi. "
"**Necrotizing otitis externa**: diabetic microangiopathy and neutrophil dysfunction. "
"**Cutaneous SCC and lymphoma**: transplant immunosuppression impairs tumor surveillance. "
"**Viral reactivation**: zoster and HSV cause severe mucositis and cranial neuropathies. "
"**Atypical presentations**: blunted inflammatory signs delay diagnosis, so imaging and biopsy thresholds are lower."),
),

"Oral Manifestations of Systemic Disease": dict(
overview=(
"The oral cavity reflects systemic disease: vitamin deficiencies, autoimmune disease, infections, hematologic disorders, and medications. "
"Recognizing patterns prompts systemic workup."),
physiology=(
"**Oral mucosa turnover**: oral epithelium renews every 1-2 weeks, so nutritional deficiencies and drugs show early. "
"**Saliva**: lubricates, buffers, and contains antimicrobial proteins. "
"**Immune surveillance**: oral mucosa is constantly exposed to microbes. "
"**Vascular supply**: rich mucosal vessels reflect systemic hematologic changes."),
pathophysiology=(
"**Nutritional deficiencies**: B12, folate, and iron deficiency cause atrophic glossitis and angular cheilitis. "
"**Autoimmune blistering disease**: pemphigus vulgaris (intraepithelial, desmoglein antibodies) and mucous membrane pemphigoid (subepithelial) cause erosions. "
"**Lichen planus**: T-cell-mediated with reticular white striae. "
"**Infections**: candidiasis with immunosuppression or xerostomia; herpes simplex. "
"**Hematologic disease**: leukemia causes gingival infiltration and bleeding. "
"**Medications**: phenytoin, cyclosporine, and calcium channel blockers cause gingival hyperplasia; bisphosphonates cause osteonecrosis."),
),

"Lemierre Syndrome": dict(
overview=(
"Lemierre syndrome is septic thrombophlebitis of the internal jugular vein after oropharyngeal infection, usually with Fusobacterium necrophorum. "
"It causes septic pulmonary emboli and requires prolonged antibiotics."),
physiology=(
"**Internal jugular vein**: drains the brain, face, and neck, running in the carotid sheath. "
"**Parapharyngeal space**: lies just lateral to the tonsillar fossa and adjacent to the carotid sheath. "
"**Venous drainage of the tonsils**: peritonsillar veins connect to the internal jugular system. "
"**Pulmonary filter**: venous emboli lodge in the lungs."),
pathophysiology=(
"**Spread**: pharyngitis or peritonsillar infection extends to the parapharyngeal space and causes septic thrombophlebitis of the internal jugular vein. "
"**Fusobacterium necrophorum**: an anaerobe whose virulence factors promote platelet aggregation and thrombosis. "
"**Septic emboli**: seed the lungs (cavitary nodules) and sometimes joints. "
"**Presentation**: persistent fever and neck tenderness after a sore throat in a young adult. "
"**Treatment**: prolonged antibiotics (often several weeks); anticoagulation is debated; drainage for abscesses."),
),

"Penetrating and Blunt Neck Trauma": dict(
overview=(
"Penetrating and blunt neck trauma threatens the airway, vessels, aerodigestive tract, and nerves. "
"Hard signs mandate surgery; modern practice favors a no-zone approach with CT angiography."),
physiology=(
"**Neck zones**: zone I (clavicles to cricoid), zone II (cricoid to angle of mandible), zone III (angle to skull base). "
"**Platysma**: penetration beyond it defines significant penetrating injury. "
"**Compartments at risk**: vascular (carotid, jugular, vertebral), aerodigestive (larynx, trachea, pharynx, esophagus), and neural (vagus, phrenic, brachial plexus, spinal cord)."),
pathophysiology=(
"**Hard signs**: expanding or pulsatile hematoma, active bleeding, bruit, air bubbling, airway compromise, and neurologic deficit require operative exploration. "
"**Soft signs**: dysphagia, hoarseness, subcutaneous emphysema, and stable hematoma prompt imaging. "
"**No-zone approach**: stable patients are evaluated by CT angiography regardless of zone. "
"**Blunt cerebrovascular injury**: carotid or vertebral dissection can cause delayed stroke. "
"**Esophageal injury**: easily missed and causes mediastinitis."),
),

"Cervical Necrotizing Fasciitis": dict(
overview=(
"Cervical necrotizing fasciitis is rapidly spreading infection along fascial planes with tissue necrosis, usually from odontogenic or pharyngeal sources. "
"Aggressive debridement and antibiotics are lifesaving."),
physiology=(
"**Fascial planes**: the superficial and deep cervical fascia form low-resistance channels. "
"**Skin perfusion**: skin depends on perforators passing through fascia. "
"**Anaerobic environment**: necrotic tissue supports anaerobes."),
pathophysiology=(
"**Polymicrobial synergy**: streptococci and anaerobes release toxins and enzymes (hyaluronidase) that spread along fascia. "
"**Perforator thrombosis**: causes skin necrosis, often with dusky skin and crepitus. "
"**Gas formation**: anaerobes produce gas visible on CT. "
"**Spread**: descending infection into the mediastinum. "
"**Systemic toxicity**: sepsis develops rapidly. "
"**Treatment**: early radical debridement, broad antibiotics, and repeated debridement."),
),

"Ear and Nasal Foreign Body Removal": dict(
overview=(
"Ear and nasal foreign bodies are common in children; button batteries and magnets require urgent removal. "
"Technique depends on object type and location."),
physiology=(
"**External auditory canal**: narrowest at the bony-cartilaginous junction, with thin, sensitive skin over the bony canal. "
"**Tympanic membrane**: lies medially and can be injured during removal. "
"**Nasal cavity**: the inferior meatus and anterior septum trap objects. "
"**Nasopharynx**: objects pushed backward can be aspirated."),
pathophysiology=(
"**Button batteries**: cause liquefactive necrosis within hours, threatening septal perforation and canal injury. "
"**Magnets**: paired magnets across the septum cause pressure necrosis. "
"**Organic objects**: swell with moisture, making removal harder. "
"**Unilateral foul discharge**: suggests a retained nasal foreign body. "
"**Removal risk**: canal trauma and posterior displacement into the airway."),
),
}
