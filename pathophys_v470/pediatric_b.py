"""Pediatric Otolaryngology (part B): mechanism-level teaching content."""

CONTENT = {
"Laryngotracheal Reconstruction": dict(
overview=(
"Laryngotracheal reconstruction (LTR) expands a stenotic pediatric airway with cartilage grafts (anterior, posterior, or both), as a single- or double-stage procedure. "
"It is chosen for higher-grade subglottic stenosis, with cricotracheal resection reserved for severe isolated subglottic disease."),
physiology=(
"**Cricoid ring**: the only complete ring in the airway, so it cannot expand on its own; widening requires dividing and grafting it. "
"**Cartilage graft biology**: costal cartilage is avascular and survives by diffusion from the vascularized wound bed while it integrates. "
"**Mucosal healing**: respiratory epithelium resurfaces the graft over weeks; a stent or endotracheal tube maintains shape during healing. "
"**Glottic relationships**: the posterior cricoid plate supports the arytenoids, so posterior grafts also widen the posterior glottis. "
"**Growth**: the pediatric airway enlarges with age, so a borderline airway may outgrow mild stenosis."),
pathophysiology=(
"**Mature scar**: stenosis is collagen scar replacing mucosa and cartilage; dilation alone fails when scar is firm or the cartilage framework is deficient. "
"**Expansion logic**: anterior grafts widen the anterior subglottis, and posterior grafts split the cricoid plate to widen posteriorly. "
"**Restenosis drivers**: active reflux, eosinophilic esophagitis, infection, and graft failure provoke granulation and scar, so these are treated beforehand. "
"**Single vs double stage**: single-stage uses postoperative intubation as a stent; double-stage keeps the tracheostomy with a stent for longer support. "
"**Functional tradeoffs**: voice changes and aspiration can occur, especially with posterior grafts that alter arytenoid position."),
),

"Choanal Atresia": dict(
overview=(
"Choanal atresia is congenital obstruction of the posterior nasal aperture; bilateral atresia causes neonatal respiratory distress and is an emergency. "
"About half are associated with syndromes, especially CHARGE."),
physiology=(
"**Preferential nasal breathing**: neonates breathe mainly through the nose for the first weeks because the larynx sits high and the epiglottis approximates the soft palate. "
"**Embryology**: the bucconasal (oronasal) membrane separating the primitive nasal cavity from the mouth must rupture around week 6-7 to form the choanae. "
"**Choanal boundaries**: vomer medially, medial pterygoid plate laterally, sphenoid body superiorly, and horizontal plate of the palatine bone inferiorly. "
"**Feeding coordination**: infants suck and breathe through the nose simultaneously."),
pathophysiology=(
"**Failed rupture**: persistence of the bucconasal membrane or abnormal mesodermal migration produces an atretic plate, most often mixed bony-membranous. "
"**Bilateral atresia**: cyclical cyanosis relieved by crying (mouth breathing) and worsened by feeding; a McGovern nipple or oral airway bridges to surgery. "
"**Unilateral atresia**: often missed until childhood, presenting with unilateral mucoid rhinorrhea. "
"**Diagnosis**: inability to pass a catheter and CT showing the atretic plate and a medialized lateral nasal wall (medial pterygoid plate) with a thickened vomer. "
"**CHARGE association**: coloboma, heart defects, atresia choanae, growth retardation, genital anomalies, ear anomalies (CHD7). "
"**Restenosis**: circumferential mucosal injury causes scar, so mucosal flaps and wide posterior septectomy reduce recurrence."),
),

"Pediatric Deep Neck Infection": dict(
overview=(
"Pediatric deep neck infections (retropharyngeal, parapharyngeal, peritonsillar abscesses) arise from lymph node suppuration after upper respiratory infections. "
"Many small abscesses respond to IV antibiotics, while larger ones and airway compromise need drainage."),
physiology=(
"**Retropharyngeal nodes**: prominent in young children and involute by about age 5, which explains the age distribution of retropharyngeal abscess. "
"**Fascial spaces**: the retropharyngeal space (between buccopharyngeal and alar fascia, ending at about T2) and the danger space (behind the alar fascia, extending to the diaphragm). "
"**Lymphatic drainage**: the nasopharynx, adenoids, sinuses, and middle ear drain to retropharyngeal nodes. "
"**Airway size**: the small pediatric airway tolerates little edema or mass effect."),
pathophysiology=(
"**Node suppuration**: a viral or bacterial upper respiratory infection inflames retropharyngeal or parapharyngeal nodes, which necrose into a phlegmon and then an abscess. "
"**Presentation**: fever, neck stiffness or torticollis, reduced neck extension, drooling, and muffled voice; stridor is late. "
"**Microbiology**: Group A strep, S. aureus (including MRSA), and oral anaerobes. "
"**Phlegmon vs abscess**: CT shows ring enhancement in an abscess; smaller collections often resolve with antibiotics. "
"**Complications**: airway obstruction, mediastinitis via the danger space, jugular thrombophlebitis (Lemierre), and carotid erosion."),
),

"Velopharyngeal Insufficiency": dict(
overview=(
"Velopharyngeal insufficiency is incomplete closure between the soft palate and pharynx during speech, causing hypernasality and nasal air emission. "
"It occurs after cleft palate repair, after adenoidectomy in at-risk children, and with neuromuscular disease."),
physiology=(
"**Velopharyngeal valve**: the levator veli palatini elevates and retracts the velum to contact the posterior pharyngeal wall while the lateral walls move medially. "
"**Closure patterns**: coronal (most common in classic series), sagittal, circular, and circular with a Passavant ridge, which guide surgical choice. "
"**Speech requirement**: oral pressure consonants (p, b, s) require a sealed velopharynx to build oral pressure. "
"**Adenoid contribution**: in young children, the adenoid pad helps the velum achieve closure."),
pathophysiology=(
"**Structural insufficiency**: a short velum or abnormally oriented levator sling (cleft palate, submucous cleft with bifid uvula, notched hard palate, and zona pellucida). "
"**Post-adenoidectomy VPI**: removing an adenoid that compensated for a marginal velum unmasks the gap, so at-risk children get partial adenoidectomy. "
"**Neuromuscular incompetence**: weak or poorly coordinated movement (e.g., 22q11 deletion, neurologic disease). "
"**Speech consequences**: hypernasality, nasal air emission, and compensatory articulation (glottal stops). "
"**Treatment logic**: speech therapy for mislearning; surgery (palatoplasty, pharyngeal flap, sphincter pharyngoplasty) for anatomic gaps, chosen by closure pattern; OSA is the key surgical risk."),
),

"Recurrent Tonsillitis Decision-Making": dict(
overview=(
"Tonsillectomy for recurrent throat infection is indicated by Paradise criteria: 7 episodes in 1 year, 5 per year for 2 years, or 3 per year for 3 years, with documented features. "
"Benefits are modest and must be weighed against surgical risks, so watchful waiting is reasonable for many."),
physiology=(
"**Tonsil immunology**: tonsils are secondary lymphoid organs that sample oral antigens through crypt epithelium and produce IgA and other antibodies. "
"**Crypts**: deep branching invaginations increase surface area but also trap debris and bacteria. "
"**Age-related activity**: tonsillar immune activity peaks in childhood and declines with age. "
"**Antibody redundancy**: removing tonsils does not measurably impair systemic immunity."),
pathophysiology=(
"**Recurrent infection**: Group A streptococcus and viruses repeatedly infect crypts; bacterial biofilms within crypts persist despite antibiotics. "
"**Documentation requirement**: each episode should include fever over 38.3 C, cervical adenopathy, tonsillar exudate, or a positive strep test. "
"**Natural history**: episode frequency declines over time, so many children improve without surgery. "
"**Modifying factors**: peritonsillar abscess, PFAPA, multiple antibiotic allergies, and missed school favor surgery. "
"**Risk side**: post-tonsillectomy hemorrhage (about 1-5 percent, varying widely by series), dehydration, and anesthesia risks."),
),

"Pediatric Tracheostomy / Decannulation": dict(
overview=(
"Pediatric tracheostomy is performed for airway obstruction, prolonged ventilation, or pulmonary toilet. "
"Decannulation requires resolution of the underlying need and a patent upper airway."),
physiology=(
"**Pediatric trachea**: small, soft, mobile, and difficult to palpate; small tube lumens obstruct easily. "
"**Upper airway functions bypassed**: humidification, filtering, voice, and effective cough (requires glottic closure). "
"**Speech and language**: airflow through the larynx is needed for vocalization during the language-learning period. "
"**Stoma maturation**: the tract takes about a week to mature, which is why stay sutures and first tube change timing matter."),
pathophysiology=(
"**Life-threatening events**: accidental decannulation and mucus plugging cause most deaths, especially in small tubes; humidification and caregiver training reduce them. "
"**Suprastomal collapse and granulation**: anterior wall collapse and granulomas obstruct the airway above the stoma, which matters at decannulation. "
"**Speaking valve**: a one-way valve redirects expired air through the larynx, restoring voice and improving swallowing. "
"**Decannulation readiness**: airway endoscopy, successful capping trials, and sometimes polysomnography confirm a safe airway. "
"**Persistent tracheocutaneous fistula**: may require closure after long-term tracheostomy."),
),

"Pediatric Vocal Fold Immobility": dict(
overview=(
"Pediatric vocal fold immobility is the second or third most common cause of neonatal stridor (after laryngomalacia, with congenital subglottic stenosis ranked ahead of it by Bluestone). "
"Unilateral immobility is often iatrogenic after cardiac surgery, and bilateral immobility is often neurologic, classically Chiari malformation."),
physiology=(
"**Nucleus ambiguus**: the brainstem motor nucleus for the larynx, vulnerable to pressure from hindbrain herniation or hydrocephalus. "
"**Left RLN course**: loops under the aortic arch beside the ductus arteriosus, exposing it during PDA ligation and arch surgery. "
"**Glottic airway**: in infants the glottis is a major portion of total airway resistance. "
"**Abduction and adduction**: posterior cricoarytenoid is the only abductor; other intrinsic muscles adduct."),
pathophysiology=(
"**Unilateral immobility**: left RLN injury causes weak cry, feeding difficulty, and aspiration, with a usually adequate airway. "
"**Bilateral immobility**: brainstem compression (Arnold-Chiari, hydrocephalus) or birth injury leaves folds near midline, causing inspiratory stridor with a good cry. "
"**Neurologic evaluation**: MRI of the brain and brainstem is required for bilateral immobility; shunting or decompression can restore motion. "
"**Airway vs voice tradeoff**: severe bilateral immobility often needs tracheostomy or glottic widening. "
"**Recovery**: many children recover function within the first 1-2 years, so irreversible procedures are delayed."),
),

"Recurrent Respiratory Papillomatosis": dict(
overview=(
"Recurrent respiratory papillomatosis is HPV-6 and HPV-11 driven benign papillomas of the airway that recur repeatedly. "
"Treatment is surgical debulking with adjuvants such as bevacizumab, and HPV vaccination is primary prevention."),
physiology=(
"**Squamociliary junctions**: transition zones between ciliated and squamous epithelium (limen vestibuli, ventricle, undersurface of the vocal folds, carina, tracheostomy site) are natural infection sites. "
"**Basal cell reservoir**: HPV infects and persists in basal epithelial cells that continuously renew the epithelium. "
"**Cell-mediated immunity**: T cells normally clear HPV-infected cells. "
"**Airway caliber**: the small pediatric larynx is quickly obstructed by exophytic growth."),
pathophysiology=(
"**Transmission**: juvenile-onset disease usually reflects vertical transmission from maternal genital HPV during birth. "
"**Viral latency**: HPV DNA persists in normal-appearing mucosa, so surgery removes lesions but not the virus, explaining recurrence. "
"**Aggressive juvenile course**: earlier onset and HPV-11 are associated with more frequent surgery. "
"**Distal spread**: tracheal and pulmonary involvement increases morbidity, and malignant transformation is rare. "
"**Surgical principle**: debulk to maintain an airway and voice while avoiding scar, especially at the anterior commissure. "
"**Adjuvants**: bevacizumab blocks VEGF-driven angiogenesis that papillomas depend on; HPV vaccination prevents new cases and may reduce recurrence."),
),

"Subglottic Hemangioma": dict(
overview=(
"Subglottic hemangioma is an infantile hemangioma of the airway causing progressive biphasic stridor in the first months of life. "
"Propranolol is first-line, and beard-distribution cutaneous hemangiomas raise suspicion."),
physiology=(
"**Infantile hemangioma life cycle**: absent or subtle at birth, rapid proliferation over the first months, plateau, then involution over years. "
"**GLUT1 expression**: infantile hemangioma endothelial cells express GLUT1, distinguishing them from vascular malformations. "
"**Subglottic geometry**: the narrowest point of the infant airway, where small lesions cause large resistance increases. "
"**Angiogenesis signaling**: VEGF and related factors drive endothelial proliferation."),
pathophysiology=(
"**Proliferation**: clonal endothelial expansion during the first months enlarges the lesion, typically posterolateral in the subglottis. "
"**Progressive stridor**: biphasic stridor worsens with crying or infection, often mistaken for croup. "
"**Beard distribution**: cutaneous hemangiomas over the mandible, chin, and neck predict airway involvement. "
"**Propranolol mechanism**: beta-blockade causes vasoconstriction, decreased VEGF and bFGF expression, and endothelial apoptosis. "
"**PHACE screening**: large segmental facial hemangiomas require evaluation for associated anomalies before beta-blockers."),
),

"Tracheomalacia / Bronchomalacia": dict(
overview=(
"Tracheomalacia is excessive collapse of the tracheal wall during expiration, primary (cartilage weakness) or secondary (vascular compression, tracheoesophageal fistula). "
"It causes expiratory wheeze and a barking cough and often improves with growth."),
physiology=(
"**Tracheal structure**: C-shaped cartilage rings anteriorly and a membranous posterior wall with trachealis muscle; the normal cartilage-to-membrane ratio is about 4.5:1. "
"**Pressure dynamics**: intrathoracic airways widen during inspiration and narrow during expiration as pleural pressure rises. "
"**Extrathoracic vs intrathoracic**: extrathoracic airway collapse is inspiratory; intrathoracic collapse is expiratory. "
"**Growth**: cartilage stiffens and airway diameter increases with age."),
pathophysiology=(
"**Primary malacia**: deficient or soft cartilage and a widened posterior membrane collapse during expiration and cough. "
"**Secondary malacia**: external compression by the innominate artery, vascular rings, or cardiac enlargement, and esophageal atresia with tracheoesophageal fistula. "
"**Symptoms**: expiratory wheeze and stridor, barking (seal) cough, recurrent infections from poor clearance, and dying spells in severe cases. "
"**Diagnosis**: dynamic airway endoscopy (spontaneous breathing) or dynamic CT shows collapse. "
"**Treatment logic**: observation for mild cases; CPAP provides a pneumatic stent; aortopexy or posterior tracheopexy for severe cases."),
),

"Microtia / Aural Atresia": dict(
overview=(
"Microtia is congenital malformation of the external ear, often with aural atresia (absent canal). "
"Management combines early hearing rehabilitation (bone conduction) with auricular reconstruction, and atresiaplasty for favorable anatomy."),
physiology=(
"**Auricle development**: six hillocks of His from the first and second branchial arches appear around weeks 5-6 and fuse by about week 12. "
"**EAC development**: the first pharyngeal cleft canalizes late (around week 28), after the auricle forms. "
"**Separate inner ear origin**: the inner ear develops from the otic placode, so it is usually normal in microtia. "
"**Facial nerve**: develops alongside second-arch structures and is often displaced in atresia."),
pathophysiology=(
"**Arrested development**: abnormal first and second arch development produces auricle deformity, canal atresia, and ossicular malformation (fused malleus-incus). "
"**Conductive loss**: about 50-60 dB in atresia with a normal cochlea. "
"**Jahrsdoerfer scale**: a CT and appearance-based score (ossicles, windows, middle ear space, facial nerve, mastoid pneumatization) predicts atresiaplasty success. "
"**Facial nerve displacement**: the nerve often runs more anterior and lateral, raising surgical risk. "
"**Canal stenosis**: a narrow canal (under about 4 mm) carries cholesteatoma risk. "
"**Hearing first**: bone-conduction devices in infancy support language while reconstruction waits for rib growth."),
),
}
