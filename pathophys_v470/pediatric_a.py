"""Pediatric Otolaryngology (part A): mechanism-level teaching content."""

CONTENT = {
"AOM / OME / Tympanostomy Decisions": dict(
overview=(
"Acute otitis media (AOM) is acute middle-ear infection with a bulging drum; otitis media with effusion (OME) is middle-ear fluid without acute infection. "
"They are the most common reasons children receive antibiotics and surgery, and guideline criteria decide observation, antibiotics, and tympanostomy tubes."),
physiology=(
"**Pediatric Eustachian tube**: shorter, more horizontal, and floppier than the adult tube, with a less efficient tensor veli palatini, so it opens poorly and lets nasopharyngeal secretions reflux upward. "
"**Middle-ear gas balance**: mucosa absorbs gas continuously; without periodic tube opening, pressure becomes negative. "
"**Adenoids**: nasopharyngeal lymphoid tissue near the tube openings that peaks in early childhood and can harbor bacterial biofilms. "
"**Immune maturation**: young children have immature responses to polysaccharide-encapsulated bacteria such as pneumococcus. "
"**Hearing and language**: the first years are a sensitive period for speech and language development, which depends on consistent auditory input."),
pathophysiology=(
"**AOM sequence**: a viral upper respiratory infection inflames the tube, negative pressure draws nasopharyngeal bacteria (S. pneumoniae, nontypeable H. influenzae, M. catarrhalis) into the middle ear, and pus under pressure bulges the drum. "
"**OME**: persistent effusion after AOM or from tube dysfunction, without acute inflammation; it causes conductive loss of about 25-30 dB. "
"**Biofilms**: bacterial biofilms in the middle ear and adenoid explain persistence and recurrence despite antibiotics. "
"**Risk factors**: daycare, smoke exposure, bottle feeding supine, pacifier use, cleft palate, Down syndrome, and family history. "
"**Why tubes work**: they bypass the dysfunctional tube, ventilating the middle ear and relieving effusion and recurrent infection while the tube matures. "
"**Adenoidectomy role**: removes the infectious reservoir, reducing recurrence in children over about 4 or with repeat tube placement."),
),

"Pediatric OSA / Adenotonsillar Disease": dict(
overview=(
"Pediatric obstructive sleep apnea is most often caused by adenotonsillar hypertrophy and leads to behavioral, growth, and cardiovascular consequences. "
"Adenotonsillectomy is first-line treatment for most children, with polysomnography in high-risk groups."),
physiology=(
"**Upper airway patency in sleep**: during sleep, pharyngeal dilator muscle tone falls, and the collapsible pharynx narrows. "
"**Lymphoid growth**: tonsils and adenoids enlarge relative to the airway between about 2 and 8 years. "
"**Pediatric sleep architecture**: children spend more time in REM and slow-wave sleep, and growth hormone is secreted in slow-wave sleep. "
"**Arousal response**: children are more likely to maintain ventilation with partial obstruction (obstructive hypoventilation) rather than discrete apneas."),
pathophysiology=(
"**Mechanical obstruction**: large tonsils and adenoids narrow the pharynx so that reduced muscle tone in sleep produces collapse. "
"**Pediatric AHI thresholds**: an obstructive AHI of 1 or more is abnormal in children, with 5-10 moderate and over 10 severe in the common convention (some sources grade more leniently), unlike adult thresholds. "
"**Consequences**: fragmented sleep causes inattention, hyperactivity, and learning problems; intermittent hypoxia and hypercapnia increase pulmonary pressures and can cause cor pulmonale; disrupted slow-wave sleep and increased work of breathing impair growth. "
"**Enuresis**: a proposed mechanism is increased atrial natriuretic peptide from negative intrathoracic pressure promotes nocturia. "
"**Residual OSA**: obesity, craniofacial anomalies, Down syndrome, and severe baseline disease increase persistence after adenotonsillectomy. "
"**Postoperative respiratory risk**: children under 3, severe OSA, and comorbidities need inpatient monitoring."),
),

"Congenital Neck Masses": dict(
overview=(
"Congenital neck masses (thyroglossal duct cysts, branchial cleft anomalies, vascular and lymphatic malformations, dermoids, teratomas) arise from embryologic remnants. "
"Location, midline versus lateral, and imaging predict the diagnosis and the operation."),
physiology=(
"**Pharyngeal apparatus**: in weeks 4-7, pharyngeal arches, clefts (ectoderm), and pouches (endoderm) form the structures of the face and neck. "
"**Thyroid descent**: the thyroid originates at the foramen cecum and descends along the thyroglossal duct anterior to the hyoid, which normally involutes. "
"**Cervical sinus**: the second arch overgrows the second through fourth clefts, normally obliterating them. "
"**Lymphatic development**: lymph sacs bud from veins and connect to form the lymphatic system."),
pathophysiology=(
"**Thyroglossal duct cyst**: persistent duct epithelium secretes fluid, forming a midline cyst that moves with swallowing and tongue protrusion. "
"**Branchial anomalies**: incomplete obliteration of clefts or pouches leaves cysts, sinuses, or fistulas along the SCM border; second cleft is most common. "
"**Lymphatic malformation**: sequestered lymphatic sacs fail to connect, producing macrocystic or microcystic masses. "
"**Dermoid cyst**: trapped ectoderm along fusion lines contains skin adnexa. "
"**Infection**: upper respiratory infections enlarge or infect these remnants through lymphoid tissue or tract connections."),
),

"Pediatric Airway Foreign Body": dict(
overview=(
"Airway foreign body aspiration is most common in children 1-3 years old and causes choking, cough, wheeze, and pneumonia. "
"Rigid bronchoscopy is the diagnostic and therapeutic standard."),
physiology=(
"**Developmental behavior**: toddlers explore objects orally and lack molars to grind food. "
"**Protective reflexes**: cough and laryngeal closure protect the airway but are immature. "
"**Airway anatomy**: the right main bronchus is wider and more vertical in older children and adults, though in young children aspiration is more evenly distributed. "
"**Poiseuille law**: small reductions in airway radius cause large increases in resistance."),
pathophysiology=(
"**Penetration syndrome**: sudden choking and cough as the object passes the larynx, often followed by a quiet phase. "
"**Check-valve (often called ball-valve) obstruction**: partial obstruction lets air in but not out, causing hyperinflation on expiratory films. "
"**Stop-valve obstruction**: complete obstruction causes atelectasis. "
"**Organic foreign bodies**: nuts swell and cause inflammation, increasing obstruction over time. "
"**Delayed diagnosis**: recurrent pneumonia, wheeze, or bronchiectasis. "
"**Why rigid bronchoscopy**: allows ventilation and controlled removal."),
),

"Tympanostomy Tube Indications": dict(
overview=(
"Tympanostomy tubes ventilate the middle ear for persistent OME with hearing loss, recurrent AOM with effusion, and at-risk children. "
"AAO-HNS guidelines define indications to avoid unnecessary surgery."),
physiology=(
"**Middle-ear ventilation**: the Eustachian tube normally opens with swallowing to replace gas absorbed by the mucosa; a tympanostomy tube provides a permanent alternative vent through the drum. "
"**Effusion clearance**: once ventilated, mucosal inflammation settles and the effusion drains down the tube or is absorbed. "
"**Tube extrusion**: lateral epithelial migration on the drum surface gradually pushes short-term tubes out over 6-18 months. "
"**Hearing and language**: an effusion produces a mild-to-moderate conductive loss that can reduce speech input during the language-learning years."),
pathophysiology=(
"**Chronic OME**: effusion for 3 months or more with hearing loss impairs language development. "
"**Recurrent AOM**: 3 episodes in 6 months or 4 in a year with effusion. "
"**At-risk children**: developmental delay, speech disorders, Down syndrome, and cleft palate. "
"**Otorrhea**: tubes allow drainage, treated with topical drops. "
"**Complications**: persistent perforation, tympanosclerosis, and cholesteatoma."),
),

"Pediatric Hearing Loss Workup": dict(
overview=(
"Pediatric hearing loss workup identifies the type, degree, and cause of hearing loss in children, from newborn screening failures to acquired loss. "
"Early diagnosis and intervention by 6 months optimize language outcomes."),
physiology=(
"**Newborn screening**: OAE or automated ABR screening by 1 month, diagnosis by 3 months, and intervention by 6 months (1-3-6 goals). "
"**Language development**: depends on auditory input during the critical period. "
"**Inner ear development**: complete at birth."),
pathophysiology=(
"**Genetic causes (about half)**: GJB2 (connexin 26) is the most common nonsyndromic cause; syndromic causes include Pendred, Usher, Waardenburg, Jervell and Lange-Nielsen. "
"**Congenital CMV**: the most common nongenetic cause, often progressive. "
"**Other acquired causes**: meningitis, ototoxicity, NICU complications, and hyperbilirubinemia. "
"**Workup logic**: audiologic confirmation, genetic testing, CMV testing, imaging (CT or MRI), ECG for long QT (Jervell and Lange-Nielsen), and ophthalmology (Usher)."),
),

"Congenital CMV Hearing Loss": dict(
overview=(
"Congenital cytomegalovirus infection is the most common nongenetic cause of congenital SNHL, often progressive or delayed onset. "
"Early detection (within 3 weeks of birth) allows antiviral therapy and close audiologic follow-up."),
physiology=(
"**CMV biology**: a herpesvirus that establishes lifelong latency and reactivates intermittently. "
"**Placental transmission**: maternal primary infection carries the highest fetal transmission risk, but reactivation or reinfection also transmits. "
"**Fetal cochlear development**: the cochlea forms in the first trimester and matures through gestation, so timing of infection influences severity. "
"**Inner-ear targets**: the stria vascularis, hair cells, and spiral ganglion are metabolically active and vulnerable to viral cytopathic effect and inflammation."),
pathophysiology=(
"**Viral injury**: CMV infects cochlear structures (stria vascularis, hair cells, spiral ganglion), causing inflammation and cell death. "
"**Progressive loss**: ongoing viral replication and inflammation cause progression after birth. "
"**Asymptomatic infants**: most infected infants are asymptomatic at birth but some develop hearing loss. "
"**Diagnosis window**: testing must occur within 21 days to distinguish congenital from postnatal infection. "
"**Valganciclovir**: improves hearing and developmental outcomes in symptomatic infants when started within the first month; recent consensus statements (2024) also support considering it for isolated SNHL, and a growing number of US states now screen newborns for CMV."),
),

"Thyroglossal Duct Cyst": dict(
overview=(
"Thyroglossal duct cyst is the most common congenital midline neck mass, moving with swallowing and tongue protrusion. "
"The Sistrunk procedure (including the central hyoid) is curative."),
physiology=(
"**Thyroid origin**: the thyroid begins as an endodermal diverticulum at the foramen cecum (junction of the anterior two-thirds and posterior third of the tongue) in week 3-4. "
"**Descent**: it descends through the tongue base and anterior neck, passing anterior to, through, or behind the developing hyoid, attached by the thyroglossal duct. "
"**Involution**: the duct normally obliterates by about week 8-10, leaving the foramen cecum and sometimes a pyramidal lobe. "
"**Hyoid formation**: the hyoid forms from second and third arch cartilage around the descending tract, which is why the tract is intimate with its central body."),
pathophysiology=(
"**Persistent epithelium**: secretes fluid, forming a cyst anywhere along the tract. "
"**Infection**: oral bacteria reach the cyst via the foramen cecum, causing abscess. "
"**Hyoid relationship**: the tract passes through or around the hyoid, so removing the central hyoid reduces recurrence. "
"**Ectopic thyroid**: rarely the only functioning thyroid tissue, so ultrasound confirms a normal thyroid preoperatively. "
"**Carcinoma**: rare papillary carcinoma within the cyst."),
),

"Branchial Cleft Anomalies": dict(
overview=(
"Branchial cleft anomalies are remnants of the pharyngeal apparatus forming cysts, sinuses, or fistulas, most commonly second cleft. "
"Complete excision of the tract prevents recurrence."),
physiology=(
"**Pharyngeal arches**: six paired mesodermal arches separated externally by ectodermal clefts and internally by endodermal pouches. "
"**Second arch overgrowth**: the second arch grows caudally over the second through fourth clefts, creating the cervical sinus of His, which normally obliterates. "
"**Arch nerves and arteries**: each arch carries a cranial nerve and artery, so a remnant tract runs between the structures of adjacent arches. "
"**Second cleft tract course**: from the anterior SCM border, deep to platysma, between the internal and external carotids, over CN IX and XII, to the tonsillar fossa."),
pathophysiology=(
"**First cleft**: near the EAC and parotid, closely related to the facial nerve. "
"**Second cleft (most common)**: along the anterior SCM border, tract passing between the internal and external carotids to the tonsillar fossa. "
"**Third and fourth**: tracts to the pyriform sinus, often presenting as recurrent left-sided thyroiditis or neck abscess. "
"**Infection**: lymphoid tissue in cyst walls enlarges with respiratory infections. "
"**Adult presentation**: a cystic lateral neck mass in an adult must be considered metastatic HPV-positive SCC until proven otherwise."),
),

"Lymphatic Malformation": dict(
overview=(
"Lymphatic malformations are slow-flow vascular malformations of abnormal lymphatic channels, classified as macrocystic, microcystic, or mixed (ISSVA). "
"They can compromise the airway, and treatment includes sclerotherapy, surgery, and sirolimus."),
physiology=(
"**Lymphatic development**: lymphatic endothelial cells bud from the cardinal veins (PROX1-driven) around weeks 6-7, forming jugular lymph sacs that connect into a network. "
"**VEGF-C/VEGFR3 signaling**: drives lymphatic sprouting and growth. "
"**Lymph function**: returns interstitial fluid and protein to the venous system and carries immune cells. "
"**PI3K/AKT/mTOR pathway**: regulates endothelial cell growth and survival."),
pathophysiology=(
"**Abnormal development**: somatic PIK3CA mutations activate PI3K/mTOR signaling, causing abnormal lymphatic channel growth. "
"**Macrocystic vs microcystic**: macrocystic lesions respond to sclerotherapy; microcystic lesions infiltrate tissue. "
"**Swelling with infection**: lymphoid inflammation enlarges lesions. "
"**Airway compromise**: cervicofacial lesions can obstruct the airway, requiring EXIT procedures prenatally. "
"**Sirolimus**: mTOR inhibitor that reduces lesion size."),
),

"Laryngomalacia": dict(
overview=(
"Laryngomalacia is collapse of supraglottic tissues into the airway during inspiration, the most common cause of infant stridor. "
"Most cases resolve by 12-18 months, and supraglottoplasty treats severe cases."),
physiology=(
"**Infant larynx**: higher, smaller, and with a floppy omega-shaped epiglottis. "
"**Neuromuscular tone**: maintains supraglottic structure. "
"**Bernoulli effect**: fast airflow through a narrow segment lowers pressure, pulling soft tissue inward."),
pathophysiology=(
"**Collapse**: short aryepiglottic folds, redundant arytenoid mucosa, and an omega-shaped epiglottis collapse inward on inspiration. "
"**Neuromuscular immaturity**: impaired laryngeal sensorimotor integration reduces tone. "
"**Inspiratory stridor**: worse with feeding, crying, and supine position. "
"**Reflux contribution**: reflux inflames supraglottic tissues and worsens collapse. "
"**Severe disease**: failure to thrive, apnea, and cyanosis indicate supraglottoplasty."),
),

"Supraglottoplasty": dict(
overview=(
"Supraglottoplasty divides short aryepiglottic folds and removes redundant supraglottic tissue to treat severe laryngomalacia. "
"It relieves obstruction in most infants with a low complication rate."),
physiology=(
"**Supraglottic structure**: the epiglottis, aryepiglottic folds, and arytenoid mucosa frame the laryngeal inlet. "
"**Inspiratory forces**: airflow through a narrow inlet lowers intraluminal pressure (Bernoulli), drawing floppy tissue inward. "
"**Tethering**: short aryepiglottic folds pull the epiglottis into an omega shape and restrict opening. "
"**Neuromuscular tone**: maintains inlet shape and improves with maturation."),
pathophysiology=(
"**Releasing tethering**: dividing short folds lets the epiglottis open. "
"**Removing redundancy**: trimming arytenoid mucosa removes tissue prolapse. "
"**Complications**: supraglottic stenosis from excessive or bilateral resection, and aspiration. "
"**Comorbidities**: neurologic disease and syndromes predict poorer outcomes."),
),

"Pediatric Subglottic Stenosis": dict(
overview=(
"Pediatric subglottic stenosis is narrowing of the subglottis, congenital or acquired after intubation. "
"Severity is graded by Myer-Cotton, and treatment ranges from observation and dilation to reconstruction."),
physiology=(
"**Cricoid ring**: the only complete cartilaginous ring in the airway, so swelling inside it cannot expand outward. "
"**Narrowest point**: in infants the subglottis is the narrowest segment, about 4-5 mm in a full-term neonate (a diameter under 4 mm is stenotic). "
"**Mucosal perfusion**: capillary perfusion pressure is roughly 25-35 mm Hg, so endotracheal tube cuff or tube pressure above this causes ischemia. "
"**Airway resistance**: in laminar flow resistance varies inversely with radius to the fourth power, so 1 mm of edema in a 4 mm airway reduces cross-sectional area by about 75 percent."),
pathophysiology=(
"**Congenital**: incomplete recanalization of the laryngeal lumen, sometimes with an abnormally shaped cricoid. "
"**Acquired**: endotracheal tube pressure causes mucosal ischemia, ulceration, perichondritis, and scar. "
"**Myer-Cotton grading**: I (0-50 percent), II (51-70), III (71-99), IV (no lumen). "
"**Poiseuille physics**: 1 mm of edema reduces the infant subglottic area dramatically."),
),
}
