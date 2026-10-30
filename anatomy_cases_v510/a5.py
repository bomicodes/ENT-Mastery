"""Surgical anatomy reviews for OR cases, batch a5."""

CASES = {
"transnasal-esophagoscopy": {
 "title": "Transnasal Esophagoscopy",
 "region": "Laryngology / Voice / Swallowing",
 "summary": "TNE passes an ultrathin flexible scope from the nasal floor through the pharynx, the upper esophageal sphincter and the full esophagus to the gastroesophageal junction in an awake patient. Safety depends on a nontraumatic nasal path and on entering the cricopharyngeus under vision behind the cricoid, lateral to the midline, rather than pushing into the posterior hypopharyngeal wall (Killian dehiscence) or a Zenker pouch.",
 "layers": [
  {"step": "Nasal passage", "structures": ["nasal vestibule", "nasal septum (medial)", "inferior turbinate (lateral)", "nasal floor / inferior meatus", "middle turbinate (alternate, higher route)"],
   "note": "Pass along the nasal floor between septum and inferior turbinate; if a spur or narrow floor blocks, use the corridor between the inferior and middle turbinates rather than forcing past a spur."},
  {"step": "Nasopharynx", "structures": ["choana", "posterior end of inferior turbinate", "torus tubarius and Eustachian tube orifice (lateral)", "fossa of Rosenmuller (posterior to torus)", "adenoid pad (posterosuperior)"],
   "note": "Flex the tip inferiorly at the choana to follow the dorsum of the soft palate; the posterior choana is a common site of contact bleeding."},
  {"step": "Oropharynx and larynx", "structures": ["dorsum of soft palate", "tongue base and vallecula", "epiglottis", "aryepiglottic folds", "true and false vocal folds"],
   "note": "Survey the larynx without touching the epiglottis or glottis; contact with the glottis can trigger cough or laryngospasm."},
  {"step": "Hypopharynx", "structures": ["piriform sinuses (lateral to AE folds)", "postcricoid region (anterior wall, behind cricoid lamina)", "posterior pharyngeal wall"],
   "note": "Inspect both piriform apices and the postcricoid area before entering the esophagus; these are blind spots on routine laryngoscopy."},
  {"step": "Upper esophageal sphincter", "structures": ["cricopharyngeus (horizontal fibers, roughly C5-C6 level)", "Killian dehiscence (posterior, above cricopharyngeus)", "esophageal inlet"],
   "note": "Approach the closed sphincter just off midline behind an arytenoid and advance as the patient swallows; never push against the posterior midline wall above the sphincter."},
  {"step": "Cervical and thoracic esophagus", "structures": ["cervical esophagus (posterior to trachea)", "aortic arch impression (left lateral wall, pulsatile)", "left main bronchus impression (anterior wall, just below the arch)", "left atrial pulsation (anterior, lower thoracic)"],
   "note": "Record lesions by distance from the nasal ala; nasal distances run about 5 cm longer on average than the oral (incisor) distances used in GI reports (individual differences vary)."},
  {"step": "Gastroesophageal junction and stomach", "structures": ["squamocolumnar junction (Z-line)", "top of gastric folds", "diaphragmatic hiatus pinch", "proximal stomach / cardia"],
   "note": "Compare Z-line, top of gastric folds and hiatal pinch to detect Barrett mucosa or hiatal hernia; retroflexion is limited with some ultrathin scopes."}
 ],
 "landmarks": [
  {"structure": "Nasal floor corridor", "how_to_find": "Keep the scope low, with the septum medial and the inferior turbinate lateral; the choana opens as a dark arch with the vomer in the midline", "why": "The widest, least vascular path and the best predictor of a comfortable pass"},
  {"structure": "Esophageal inlet", "how_to_find": "Follow the posterior surface of an arytenoid into the postcricoid area just off midline; the cricopharyngeus appears as a closed horizontal slit that opens on swallow", "why": "Entering under vision avoids the Killian dehiscence and a Zenker pouch"},
  {"structure": "Zenker diverticulum", "how_to_find": "A pouch in the posterior midline above the sphincter; the true lumen lies anterior to the pouch septum (the cricopharyngeal bar)", "why": "The scope tends to slide into the pouch, where perforation risk is highest"},
  {"structure": "Aortic arch indentation", "how_to_find": "Pulsatile extrinsic bulge on the left lateral wall in the upper thoracic esophagus, roughly 22-27 cm from the incisors", "why": "Second physiologic narrowing; avoid deep biopsy of pulsatile extrinsic compression"},
  {"structure": "Squamocolumnar junction (Z-line)", "how_to_find": "Pale pink squamous mucosa meets salmon red columnar mucosa near the hiatal pinch (sniff test helps); normally at or near the top of the gastric folds", "why": "Displacement above the gastric folds suggests Barrett esophagus; separation from the hiatus suggests hiatal hernia"}
 ],
 "danger": [
  {"structure": "Killian dehiscence / posterior hypopharyngeal wall", "where": "Posterior midline triangle between the oblique thyropharyngeus and the horizontal cricopharyngeus", "protect": "Enter the inlet off midline under vision during a swallow; never advance against resistance", "injury": "Cervical esophageal perforation, neck abscess, mediastinitis"},
  {"structure": "Nasal mucosa (septal spurs, inferior turbinate)", "where": "Lateral and medial walls of the nasal floor corridor; septal spurs at the maxillary crest", "protect": "Topical decongestion and anesthesia, small scope, choose the wider side, steer around spurs", "injury": "Epistaxis, pain, aborted study"},
  {"structure": "Glottis", "where": "Anterior to the esophageal inlet", "protect": "Avoid touching the epiglottis and cords; limit topical anesthetic volume", "injury": "Laryngospasm, cough, aspiration of anesthetic"},
  {"structure": "Thoracic esophagus beside aorta and left atrium", "where": "Upper thoracic esophagus at the arch; lower thoracic esophagus behind the left atrium", "protect": "Minimal insufflation, no blind force, no deep biopsy into pulsatile extrinsic masses", "injury": "Perforation, mediastinitis, rarely major hemorrhage"},
  {"structure": "Esophageal or gastric varices", "where": "Distal esophagus and cardia (portosystemic anastomosis via left gastric vein)", "protect": "Recognize bluish tortuous columns; do not biopsy", "injury": "Major hemorrhage"}
 ],
 "variants": [
  "Septal deviation or spur narrowing one nasal floor",
  "Cricopharyngeal bar or Zenker diverticulum (posterior pulsion pouch through Killian dehiscence)",
  "Cervical osteophytes (e.g., DISH) indenting the posterior hypopharynx",
  "Aberrant right subclavian artery passing posterior to the esophagus (posterior extrinsic compression, dysphagia lusoria)",
  "Hiatal hernia with the Z-line displaced above the diaphragmatic pinch"
 ],
 "imaging_check": [
  "Not routinely imaged: check nasal patency (anterior rhinoscopy or prior endoscopy) and bleeding risk/anticoagulation",
  "Review any barium swallow for Zenker diverticulum, web, stricture or extrinsic compression before passing the scope",
  "Review prior CT/MRI for mediastinal mass or vascular anomaly if extrinsic compression is suspected"
 ],
 "blood_nerve": [
  ["Arterial supply of esophagus", "Cervical: inferior thyroid artery; thoracic: esophageal branches of the aorta and bronchial arteries; abdominal: left gastric and inferior phrenic arteries"],
  ["Venous drainage", "Inferior thyroid veins; azygos/hemiazygos; left gastric vein to portal system (site of varices)"],
  ["Motor innervation", "Vagus: pharyngeal plexus and recurrent laryngeal nerves to the cricopharyngeus and upper striated esophagus; vagal esophageal plexus to distal smooth muscle"],
  ["Nasal sensation", "Anterior ethmoidal nerve (V1) anterosuperiorly; nasopalatine and posterior nasal branches of V2 via the pterygopalatine ganglion"]
 ],
 "pimp": [
  {"q": "What are the three physiologic narrowings of the esophagus?", "a": "Cricopharyngeus (about 15 cm from incisors), aortic arch/left main bronchus crossing (about 22-27 cm), and the diaphragmatic hiatus/LES (about 38-40 cm)"},
  {"q": "What are the boundaries of the Killian dehiscence?", "a": "Oblique fibers of the thyropharyngeus (inferior constrictor) above and the horizontal cricopharyngeus below, in the posterior midline"},
  {"q": "Where is the Killian-Jamieson area?", "a": "Anterolateral wall of the proximal cervical esophagus just below the cricopharyngeus, lateral to the longitudinal muscle, near where the RLN enters the larynx"},
  {"q": "Where is the Laimer (Laimer-Haeckermann) triangle?", "a": "Posterior wall below the cricopharyngeus, between it and the diverging longitudinal esophageal muscle"},
  {"q": "What is the muscle type along the esophagus?", "a": "Upper third mostly striated, middle third mixed, distal third smooth muscle"},
  {"q": "Why does an esophageal perforation spread quickly?", "a": "The esophagus has no serosa (only adventitia), so infection tracks directly into the retrovisceral space and mediastinum"},
  {"q": "What does the Z-line represent?", "a": "The squamocolumnar junction between esophageal squamous and gastric columnar epithelium"},
  {"q": "What vascular anomaly causes posterior extrinsic compression of the esophagus?", "a": "Aberrant right subclavian artery (arteria lusoria) passing posterior to the esophagus"}
 ],
 "atlas_topics": ["Pharynx / UES / Cervical Esophagus", "Mediastinal Continuity of Deep Neck Spaces"],
 "sources": [["Cummings Otolaryngology 7e — Transnasal esophagoscopy and esophageal anatomy chapters", ""], ["K.J. Lee Essential Otolaryngology 12e — Esophagus", ""], ["Bailey's Head and Neck Surgery — Otolaryngology, office endoscopy chapter", ""]]
},
"rigid-tracheobronchoscopy": {
 "title": "Rigid Tracheobronchoscopy",
 "region": "Laryngology / Voice / Swallowing",
 "summary": "Rigid bronchoscopy places a straight ventilating tube from the mouth through the glottis into the trachea and mainstem bronchi, giving airway control, large-channel suction and therapeutic access. Safety depends on protecting the maxillary teeth and arytenoids on entry, keeping orientation to the posterior membranous wall, and knowing what lies outside the wall you are working on: the innominate artery anterior to the lower cervical trachea, the esophagus behind the membranous wall, and the pulmonary arteries around the distal bronchi.",
 "layers": [
  {"step": "Positioning and oral entry", "structures": ["maxillary incisors (fulcrum risk)", "lips", "tongue", "oropharynx"],
   "note": "Sniffing/Boyce-Jackson position (neck flexed on chest, head extended on neck) aligns the oral, pharyngeal and laryngeal axes; protect the upper teeth with a guard and the left thumb, never lever on them."},
  {"step": "Supraglottis", "structures": ["vallecula", "epiglottis (laryngeal surface)", "aryepiglottic folds", "arytenoids"],
   "note": "Lift the epiglottis with the bronchoscope tip (or use a laryngoscope first); the arytenoids are posterior and are the structures most often injured on entry."},
  {"step": "Glottis", "structures": ["true vocal folds", "anterior commissure", "posterior glottis / interarytenoid area"],
   "note": "Rotate the bevel about 90 degrees so its leading edge lines up with one vocal fold, pass through the glottis, then rotate back to the midline."},
  {"step": "Subglottis and cricoid", "structures": ["conus elasticus", "cricoid ring (only complete cartilage ring)", "first tracheal ring"],
   "note": "The cricoid cannot expand; an oversized scope here causes mucosal injury and edema."},
  {"step": "Trachea", "structures": ["C-shaped cartilage rings (anterior and lateral)", "posterior membranous wall (trachealis)", "innominate artery pulsation (anterior, lower cervical/upper thoracic trachea)", "aortic arch impression (left anterolateral, distal trachea)"],
   "note": "With the patient supine and the surgeon at the head, the membranous wall is at the bottom of the view and the patient's right is on the surgeon's right."},
  {"step": "Carina and mainstem bronchi", "structures": ["main carina (about T4-T5, sternal angle level)", "right main bronchus (shorter, wider, more vertical)", "right upper lobe orifice (lateral wall, close to carina)", "bronchus intermedius", "left main bronchus (longer, passes under the aortic arch)"],
   "note": "Turn the patient's head to the left to align the scope with the right bronchus and to the right for the left bronchus."},
  {"step": "Lobar and segmental bronchi", "structures": ["right middle and lower lobe orifices", "superior segment orifices of both lower lobes (posterior wall)", "left upper lobe and lingula", "pulmonary arteries adjacent to lobar bronchi"],
   "note": "Use telescopes or a flexible scope through the rigid barrel for upper lobe and segmental views; distal biopsy risks pulmonary artery bleeding and pneumothorax."}
 ],
 "landmarks": [
  {"structure": "Glottic entry", "how_to_find": "Track the epiglottis tip, lift it, then find the arytenoids posteriorly and the dark glottic chink between the folds; turn the bevel so its edge parallels one fold", "why": "Atraumatic passage without arytenoid dislocation or cord laceration"},
  {"structure": "Posterior membranous wall", "how_to_find": "Smooth wall without cartilage rings at the bottom of the view (supine patient, surgeon at head); longitudinal elastic folds are often visible", "why": "Fixed orientation reference and the wall most prone to tear"},
  {"structure": "Main carina", "how_to_find": "Sharp vertical ridge at the end of the trachea, roughly 12-15 cm below the cords in adults (the trachea itself is about 10-13 cm); widened or blunted carina suggests subcarinal nodes", "why": "Reference point for measuring lesions and choosing bronchus"},
  {"structure": "Right upper lobe orifice", "how_to_find": "On the lateral wall of the right main bronchus within about 1-2.5 cm of the carina; may need an angled telescope", "why": "Short right main bronchus makes RUL easy to miss or to occlude"},
  {"structure": "Innominate artery", "how_to_find": "Pulsation on the anterior tracheal wall, generally in the lower cervical/upper thoracic trachea (can ride high, at or above the sternal notch)", "why": "Avoid laser, deep debridement or prolonged pressure on this segment"}
 ],
 "danger": [
  {"structure": "Maxillary incisors and lips", "where": "Fulcrum for the bronchoscope", "protect": "Tooth guard, left-hand support, never lever on the teeth; note loose or capped teeth before induction", "injury": "Dental fracture, avulsion and aspiration of a tooth, lip laceration"},
  {"structure": "Arytenoids and vocal folds", "where": "Posterior glottis at entry", "protect": "Pass under vision with the bevel rotated; do not force a large scope", "injury": "Arytenoid dislocation, cord laceration, posterior glottic scar"},
  {"structure": "Posterior membranous wall and esophagus", "where": "Directly posterior to trachea and left main bronchus", "protect": "Keep scope axis central, no blind advancement, gentle dilation", "injury": "Tracheal tear, pneumomediastinum, mediastinitis, tracheoesophageal fistula"},
  {"structure": "Innominate artery", "where": "Crosses the anterior trachea from left to right in the lower neck/upper chest", "protect": "Limit laser/coring of the anterior wall here; avoid prolonged anterior pressure", "injury": "Massive hemorrhage (tracheoinnominate fistula pattern)"},
  {"structure": "Pulmonary arteries and visceral pleura", "where": "Beside lobar and segmental bronchi", "protect": "Avoid deep distal biopsy; keep forceps in view; low-pressure ventilation", "injury": "Hemorrhage, pneumothorax"},
  {"structure": "Airway in an oxygen-rich field", "where": "Entire lumen during laser or electrocautery", "protect": "Lowest FiO2 tolerated (generally under 30-40%), no combustible material in beam path, saline ready", "injury": "Airway fire"}
 ],
 "variants": [
  "Tracheal (pig) bronchus: right upper lobe or apical segment bronchus arising from the trachea above the carina",
  "Tracheobronchomalacia with dynamic collapse of the membranous wall",
  "Saber-sheath trachea (narrow transverse diameter, COPD)",
  "Distorted carina or bronchi from mediastinal nodes, goiter or prior resection"
 ],
 "imaging_check": [
  "CT neck/chest with airway reconstruction: lesion level, length, distance from the vocal folds and carina",
  "Relationship of lesion to innominate artery, aortic arch and pulmonary arteries",
  "Extrinsic compression (thyroid, mediastinal mass) versus intraluminal disease",
  "Cervical spine mobility and dentition (clinical) for rigid scope passage"
 ],
 "blood_nerve": [
  ["Tracheal arterial supply", "Segmental lateral branches: inferior thyroid artery to the upper trachea; bronchial arteries to the lower trachea and carina"],
  ["Bronchial arteries", "From the descending aorta or intercostal arteries; source of hemoptysis"],
  ["Nerves", "Vagus/RLN (sensory, cough, bronchoconstriction) and sympathetic trunk"],
  ["Adjacent great vessels", "Innominate artery anterior; aortic arch over the left main bronchus; pulmonary arteries anterior/lateral to bronchi"]
 ],
 "pimp": [
  {"q": "Why do aspirated objects favor the right main bronchus in adults?", "a": "It is shorter, wider and more vertical (roughly 20-30 degrees from the tracheal axis versus roughly 40-50 degrees on the left)"},
  {"q": "At what vertebral level is the carina?", "a": "About T4-T5, at the sternal angle"},
  {"q": "How many segmental bronchi are there on each side?", "a": "Usually 10 on the right; 8-10 on the left because of combined apicoposterior and anteromedial basal segments"},
  {"q": "Which structure lies over the left main bronchus?", "a": "The aortic arch, with the esophagus posterior"},
  {"q": "How is the trachea supplied, and why does it matter for resection?", "a": "Segmental vessels enter laterally (inferior thyroid above, bronchial below), so circumferential dissection is avoided to prevent devascularization"},
  {"q": "What is the only complete cartilaginous ring of the airway?", "a": "The cricoid"},
  {"q": "What is the Boyce-Jackson position?", "a": "Neck flexed on the chest and head extended at the atlanto-occipital joint to align the oral, pharyngeal and laryngeal axes"},
  {"q": "What are the lobar divisions of the right bronchial tree?", "a": "Right upper lobe bronchus, then bronchus intermedius dividing into the middle and lower lobe bronchi"}
 ],
 "atlas_topics": ["Tracheostomy / Cervical Trachea Anatomy", "Thoracic Inlet / Root of Neck", "Laryngeal Framework / Intrinsic Muscles"],
 "sources": [["Cummings Otolaryngology 7e — Tracheobronchial endoscopy chapter", ""], ["K.J. Lee Essential Otolaryngology 12e — Bronchoesophagology", ""], ["Myers Operative Otolaryngology — Bronchoscopy", ""]]
},
"adult-ltr": {
 "title": "Adult Laryngotracheal Reconstruction",
 "region": "Laryngology / Voice / Swallowing",
 "summary": "Adult LTR expands a stenotic cricoid and upper trachea by splitting the framework in the midline and inserting costal cartilage, instead of resecting the segment. Safety turns on staying in the midline: the recurrent laryngeal nerves enter the larynx just behind the cricothyroid joints laterally, the esophagus lies directly behind the posterior cricoid plate, and the anterior commissure sits just above any anterior split of the thyroid cartilage.",
 "layers": [
  {"step": "Incision and flaps", "structures": ["skin", "platysma", "anterior jugular veins"],
   "note": "Horizontal incision at about the cricoid level (or around an existing stoma); raise subplatysmal flaps from the hyoid to the sternal notch."},
  {"step": "Strap muscles", "structures": ["midline raphe", "sternohyoid (superficial)", "sternothyroid (deep, inserts on thyroid cartilage oblique line)", "thyrohyoid"],
   "note": "Separate the straps in the midline and retract laterally; avoid lateral dissection beyond the cricoid arch."},
  {"step": "Thyroid isthmus and airway exposure", "structures": ["thyroid isthmus (over rings 2-4)", "pyramidal lobe (variable)", "cricothyroid muscles (anterolateral)", "cricothyroid membrane", "cricoid arch", "upper tracheal rings"],
   "note": "Divide and suture-ligate the isthmus; expose the thyroid cartilage, cricoid and upper trachea in the midline only."},
  {"step": "Anterior split", "structures": ["lower thyroid cartilage (below the anterior commissure)", "cricothyroid membrane", "anterior cricoid arch", "upper tracheal rings", "stenotic scar"],
   "note": "Vertical midline incision through scar and cartilage; open the thyroid cartilage only as high as needed and stay below the anterior commissure unless a laryngofissure is planned."},
  {"step": "Posterior split (when needed)", "structures": ["posterior cricoid lamina", "interarytenoid muscle and scar", "postcricoid tissue", "anterior wall of hypopharynx/esophageal inlet"],
   "note": "Divide the posterior cricoid plate exactly in the midline through full cartilage thickness until the postcricoid soft tissue bulges; do not enter hypopharyngeal or esophageal mucosa."},
  {"step": "Costal cartilage harvest", "structures": ["skin", "pectoralis major / rectus abdominis fibers", "costal cartilage (commonly 5th-7th)", "outer perichondrium", "inner perichondrium", "parietal pleura"],
   "note": "Preserve the inner perichondrium over the pleura; check for air leak with a saline-filled wound and positive-pressure breath."},
  {"step": "Graft inset and stenting", "structures": ["graft flanges", "cut cartilage edges", "perichondrium facing the lumen", "stent or endotracheal tube"],
   "note": "Shape the graft with flanges so it cannot prolapse into the lumen; secure with absorbable sutures outside the mucosa; confirm lumen endoscopically."},
  {"step": "Closure", "structures": ["strap muscles over graft", "drain", "platysma and skin"],
   "note": "Reapproximate straps over the graft for vascularized cover; drain to avoid fluid around the graft."}
 ],
 "landmarks": [
  {"structure": "Cricoid arch", "how_to_find": "Firm ring palpable just below the thyroid cartilage lower border and cricothyroid membrane; first complete ring above the trachea", "why": "Central element of the stenosis and the reference for the split"},
  {"structure": "Midline", "how_to_find": "Thyroid notch above, anterior cricoid midpoint, and tracheal midline below; confirm with the endoscopic light or a needle seen from inside", "why": "Off-midline splits risk RLN injury and asymmetric expansion"},
  {"structure": "Anterior commissure", "how_to_find": "Roughly the midpoint of the vertical height of the thyroid cartilage in the midline (varies by sex/age); confirm with transillumination or a needle from inside", "why": "Splitting through it causes anterior web and dysphonia"},
  {"structure": "RLN entry point", "how_to_find": "Posterior to the cricothyroid joint, deep to the lower edge of the inferior constrictor; ascends in or near the tracheoesophageal groove", "why": "Stay medial to the cricothyroid joints and do not skeletonize the lateral cricoid"},
  {"structure": "Posterior cricoid midline", "how_to_find": "Viewed from inside after the anterior split: midline between the arytenoids, in line with the interarytenoid notch", "why": "Off-midline posterior split risks cricoarytenoid joint injury"}
 ],
 "danger": [
  {"structure": "Recurrent laryngeal nerves", "where": "Tracheoesophageal grooves, entering the larynx just posterior to the cricothyroid joints", "protect": "Midline dissection only; no lateral dissection around the cricoid", "injury": "Vocal fold paralysis; bilateral injury causes airway obstruction"},
  {"structure": "Esophagus / hypopharynx", "where": "Directly posterior to the posterior cricoid lamina", "protect": "Controlled full-thickness cartilage cut only, stop at the bulging soft tissue; feel for the nasogastric tube", "injury": "Pharyngoesophageal perforation, fistula, graft infection"},
  {"structure": "Anterior commissure", "where": "Midline thyroid cartilage at about mid-height", "protect": "Limit superior extent of the anterior split; precise midline closure if a laryngofissure is needed", "injury": "Anterior glottic web, voice change"},
  {"structure": "Cricoarytenoid joints", "where": "Posterior-superior cricoid lamina on each side of midline", "protect": "Exact midline posterior split", "injury": "Arytenoid fixation, posterior glottic dysfunction"},
  {"structure": "Pleura", "where": "Deep to the inner perichondrium of the costal cartilage", "protect": "Subperichondrial harvest leaving inner perichondrium; leak test", "injury": "Pneumothorax"},
  {"structure": "Innominate artery", "where": "Anterior to the lower cervical/upper thoracic trachea", "protect": "Avoid low dissection and stent/tube pressure against the anterior wall", "injury": "Hemorrhage, tracheoinnominate fistula"}
 ],
 "variants": [
  "High-riding innominate artery or low-lying thyroid isthmus",
  "Ossified laryngeal cartilage in older adults (needs saw or drill to split)",
  "Calcified costal cartilage in older patients limiting graft carving",
  "Prior tracheostomy with distorted anterior wall and suprastomal collapse"
 ],
 "imaging_check": [
  "CT neck/chest with airway reconstruction: stenosis length, distance from the vocal folds and carina, cartilage loss",
  "Laryngoscopy with vocal fold mobility (clinical): posterior glottic stenosis versus bilateral paralysis",
  "Chest CT or plain imaging of costal cartilage calcification if age suggests",
  "Position of innominate artery relative to the planned work"
 ],
 "blood_nerve": [
  ["Laryngeal arteries", "Superior laryngeal artery (from superior thyroid) through the thyrohyoid membrane; cricothyroid artery across the membrane; inferior laryngeal artery (from inferior thyroid) with the RLN"],
  ["Tracheal supply", "Lateral segmental branches of the inferior thyroid and bronchial arteries"],
  ["Motor", "RLN to all intrinsic muscles except cricothyroid; external branch of SLN to cricothyroid"],
  ["Rib graft site", "Intercostal neurovascular bundle runs along the inferior border of each rib"]
 ],
 "pimp": [
  {"q": "What is the McCaffrey staging of adult laryngotracheal stenosis?", "a": "I: subglottis or trachea under 1 cm; II: subglottic over 1 cm within cricoid, not glottis or trachea; III: subglottic extending into trachea, not glottis; IV: glottic involvement with vocal fold fixation"},
  {"q": "What is the Cotton-Myer grading scale?", "a": "Grade I 0-50%, II 51-70%, III 71-99% obstruction, IV no detectable lumen"},
  {"q": "Where does the RLN enter the larynx?", "a": "Posterior to the cricothyroid joint, deep to the inferior border of the inferior constrictor"},
  {"q": "Which intrinsic laryngeal muscle is not innervated by the RLN?", "a": "Cricothyroid (external branch of the superior laryngeal nerve)"},
  {"q": "Which way does the perichondrium of a costal graft usually face?", "a": "Toward the airway lumen"},
  {"q": "What lies immediately posterior to the posterior cricoid plate?", "a": "The postcricoid hypopharynx/esophageal inlet with the cricopharyngeus"},
  {"q": "Which muscle is divided in a posterior split for posterior glottic stenosis?", "a": "The interarytenoid (transverse/oblique arytenoid) muscle and scar along with the posterior cricoid lamina"},
  {"q": "What lies along the inferior border of a rib?", "a": "The intercostal vein, artery and nerve (VAN, superior to inferior)"}
 ],
 "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Tracheostomy / Cervical Trachea Anatomy", "Laryngeal Neurovascular Anatomy"],
 "sources": [["Cummings Otolaryngology 7e — Chronic laryngotracheal stenosis chapter", ""], ["Pasha Otolaryngology-Head and Neck Surgery Clinical Reference Guide 6e — Laryngeal/tracheal stenosis", ""], ["McCaffrey TV. Classification of laryngotracheal stenosis. Laryngoscope 1992", ""]]
},
"direct-laryngoscopy-bronchoscopy": {
 "title": "Direct Laryngoscopy & Bronchoscopy / Airway Evaluation",
 "region": "Pediatric Otolaryngology",
 "summary": "DLB is a level-by-level survey of the airway from the supraglottis to the bronchi, so the anatomy is a checklist read in order. In a child the cricoid is the narrowest complete ring and cannot expand, so oversized instruments injure it; key hidden findings sit in the interarytenoid area (cleft), the subglottis (stenosis, cysts, hemangioma) and the distal trachea (vascular compression, complete rings, fistula).",
 "layers": [
  {"step": "Oral cavity and laryngoscope placement", "structures": ["lips and alveolar ridges/teeth", "tongue", "vallecula", "epiglottis (omega-shaped, floppy in infants)"],
   "note": "Place the laryngoscope tip in the vallecula or under the epiglottis and lift; the infant larynx is high and anterior, so less neck extension is needed than in adults."},
  {"step": "Supraglottis", "structures": ["epiglottis", "aryepiglottic folds", "cuneiform and corniculate cartilages", "false vocal folds", "laryngeal ventricles"],
   "note": "Look for laryngomalacia features, saccular cysts and supraglottic masses before the scope distorts them."},
  {"step": "Glottis and posterior commissure", "structures": ["true vocal folds", "anterior commissure", "vocal processes", "interarytenoid region", "posterior commissure"],
   "note": "Assess mobility during light anesthesia; palpate the interarytenoid area with a probe to exclude a laryngeal cleft and palpate the arytenoids for fixation."},
  {"step": "Subglottis", "structures": ["conus elasticus", "cricoid ring (narrowest complete ring)", "subglottic mucosa"],
   "note": "Inspect circumferentially with a telescope placed just above the folds and then through them; record stenosis, cysts, hemangioma or granulation and its distance below the folds."},
  {"step": "Cervical and thoracic trachea", "structures": ["C-shaped tracheal rings", "posterior membranous wall", "innominate artery pulsation (anterior, distal trachea in children)", "tracheostomy site if present"],
   "note": "Look for complete rings (no membranous wall), anterior pulsatile compression, malacia and an H-type fistula opening on the posterior wall."},
  {"step": "Carina and bronchi", "structures": ["main carina", "right main bronchus and right upper lobe orifice", "bronchus intermedius", "left main bronchus"],
   "note": "Look for tracheal bronchus above the carina and left main bronchus compression by vascular anomalies or the left atrium."},
  {"step": "Sizing and intervention", "structures": ["subglottic lumen", "calibrated endotracheal tubes", "leak pressure"],
   "note": "Size with the largest tube that leaks at a standard pressure (Myer-Cotton used a leak at 10-25 cm H2O; many centers use about 20 cm H2O) and compare with age-expected size to grade stenosis."}
 ],
 "landmarks": [
  {"structure": "Interarytenoid area", "how_to_find": "Posterior glottis between the arytenoid apices; spread the arytenoids or probe the notch to see how far the mucosal defect extends toward or below the vocal folds", "why": "Laryngeal cleft is missed unless palpated"},
  {"structure": "Cricoid ring", "how_to_find": "Complete cartilage ring seen just below the conus, roughly a few mm to 1 cm below the true folds in infants; a fixed narrowing that does not move with respiration", "why": "Narrowest complete ring; site of subglottic stenosis"},
  {"structure": "Posterior membranous wall", "how_to_find": "Smooth, ringless posterior tracheal wall; with the child supine and surgeon at the head it is at the bottom of the view", "why": "Orientation reference; absent in complete tracheal rings"},
  {"structure": "Innominate artery compression", "how_to_find": "Pulsatile anterior compression of the distal trachea, from the lower left toward the upper right; lifting the anterior wall with the scope tip may diminish the right radial/temporal pulse", "why": "Common extrinsic cause of tracheal compression in infants"},
  {"structure": "H-type tracheoesophageal fistula", "how_to_find": "Small opening in the posterior membranous wall, usually at the cervicothoracic junction or upper thoracic trachea; may need a probe or catheter", "why": "Easily missed; changes surgical plan"}
 ],
 "danger": [
  {"structure": "Alveolar ridges, teeth, lips", "where": "Laryngoscope fulcrum", "protect": "Gum or tooth guard and lift along the axis of the handle, not rotation", "injury": "Tooth injury, lip laceration"},
  {"structure": "Arytenoids", "where": "Posterior glottis", "protect": "Gentle telescope passage in the midline; do not use the arytenoid as a fulcrum", "injury": "Arytenoid dislocation, posterior glottic scar"},
  {"structure": "Subglottic mucosa", "where": "Inside the cricoid ring", "protect": "Use age-appropriate scope and tube sizes; stop sizing at a leak", "injury": "Edema, acquired subglottic stenosis"},
  {"structure": "Posterior membranous wall and distal bronchi", "where": "Behind the trachea (esophagus) and in small bronchi", "protect": "Under-vision advancement, avoid force in small airways", "injury": "Perforation, pneumomediastinum, pneumothorax"},
  {"structure": "Larynx in light anesthesia", "where": "Glottis", "protect": "Topical lidocaine to the larynx at an accepted weight-based dose and adequate depth before instrumentation", "injury": "Laryngospasm, hypoxia"}
 ],
 "variants": [
  "Laryngeal cleft (Benjamin-Inglis types I-IV)",
  "Complete tracheal rings, often with pulmonary artery sling",
  "Tracheal (pig) bronchus to the right upper lobe",
  "Vascular rings (double aortic arch, right arch with aberrant left subclavian and ligamentum) compressing trachea and esophagus",
  "Subglottic hemangioma (often posterior-lateral, left-sided more often in many series) or subglottic cysts in former preterm infants"
 ],
 "imaging_check": [
  "Airway films or CT for subglottic narrowing, mass or tracheal narrowing when the history suggests it",
  "CT angiography or MRI when pulsatile compression, complete rings or vascular ring is suspected",
  "Esophagram for vascular ring or H-type fistula when suspected",
  "Clinical: dentition, cervical spine stability (e.g., Down syndrome) and prior intubation history"
 ],
 "blood_nerve": [
  ["Laryngeal sensation", "Internal branch of SLN above the vocal folds; RLN below the folds"],
  ["Laryngeal motor", "RLN to all intrinsic muscles except cricothyroid (external SLN)"],
  ["Laryngeal arteries", "Superior laryngeal artery (superior thyroid) and inferior laryngeal artery (inferior thyroid)"],
  ["Adjacent great vessels", "Innominate artery anterior to the distal trachea; aortic arch to the left; pulmonary arteries at the carina"]
 ],
 "pimp": [
  {"q": "What subglottic diameter defines stenosis in neonates?", "a": "4 mm or less in a full-term neonate and about 3-3.5 mm or less in a preterm neonate (sources vary between 3 and 3.5 mm)"},
  {"q": "What is the Benjamin-Inglis classification of laryngeal clefts?", "a": "I interarytenoid above the folds; II partial cricoid; III through the cricoid into the cervical trachea; IV into the thoracic trachea"},
  {"q": "Why is the infant subglottis vulnerable?", "a": "The cricoid is a complete, nonexpandable ring and the narrowest part of the infant airway, so small mucosal edema greatly reduces lumen"},
  {"q": "Where is the infant larynx relative to the cervical spine?", "a": "Higher than in adults: the infant larynx spans roughly C1-C4 (cricoid near C4) versus roughly C3-C6 in adults (cricoid at C6), descending with growth"},
  {"q": "What is a pulmonary artery sling?", "a": "Left pulmonary artery arising from the right PA and passing between trachea and esophagus; associated with complete tracheal rings"},
  {"q": "What is the usual cause of anterior pulsatile compression of the distal trachea in infants?", "a": "Innominate artery compression"},
  {"q": "What is the usual sensory and motor innervation of the larynx?", "a": "Sensory: internal SLN above and RLN below the folds; motor: RLN except the cricothyroid (external SLN)"},
  {"q": "What does a leak at a low pressure around an age-appropriate tube indicate?", "a": "Adequate subglottic lumen; failure to leak at a standard pressure implies relative stenosis that is graded against an age-based chart"}
 ],
 "atlas_topics": ["Pediatric Laryngotracheal Airway", "Laryngeal Framework / Intrinsic Muscles"],
 "sources": [["Cummings Otolaryngology 7e — Pediatric airway evaluation and congenital laryngeal anomalies", ""], ["Myer CM, O'Connor DM, Cotton RT. Proposed grading system for subglottic stenosis. Ann Otol Rhinol Laryngol 1994", ""], ["Benjamin B, Inglis A. Minor congenital laryngeal clefts. Ann Otol Rhinol Laryngol 1989", ""]]
},
"supraglottoplasty": {
 "title": "Supraglottoplasty for Severe Laryngomalacia",
 "region": "Pediatric Otolaryngology",
 "summary": "Supraglottoplasty relieves inspiratory collapse of the supraglottis by dividing short aryepiglottic folds and trimming redundant arytenoid mucosa. Safety comes from limited, superficial cuts that stay medial to the piriform sinus floor (internal SLN, sensation) and away from the interarytenoid mucosa (supraglottic or posterior glottic stenosis).",
 "layers": [
  {"step": "Suspension and survey", "structures": ["vallecula", "epiglottis (tubular or omega shape)", "aryepiglottic folds", "arytenoids", "true vocal folds", "subglottis and trachea"],
   "note": "Complete DLB first to exclude synchronous lesions; inspect dynamic collapse with spontaneous breathing before suspension when possible."},
  {"step": "Identify the collapsing components", "structures": ["supra-arytenoid mucosa over cuneiform and corniculate cartilages (anterior prolapse)", "short AE folds tethering the epiglottis", "posteriorly displaced epiglottis"],
   "note": "Classify the dominant pattern (Olney type 1 mucosal prolapse, type 2 short AE folds, type 3 epiglottic retroflexion) because each needs a different cut."},
  {"step": "Aryepiglottic fold division", "structures": ["aryepiglottic fold (mucosa, aryepiglottic muscle fibers)", "lateral edge of epiglottis", "piriform sinus (lateral)"],
   "note": "Divide the fold with cold scissors or CO2 laser near its epiglottic end, releasing the epiglottis; keep the cut superficial and medial to the piriform sinus."},
  {"step": "Arytenoid mucosal trim", "structures": ["redundant mucosa over cuneiform and corniculate cartilages", "lateral (posterolateral) arytenoid mucosa", "interarytenoid mucosa (preserve)"],
   "note": "Excise only mucosa that prolapses into the glottis on inspiration; leave the cartilage and interarytenoid mucosa intact."},
  {"step": "Contralateral side", "structures": ["opposite AE fold", "opposite arytenoid mucosa"],
   "note": "Repeat symmetrically or stage the second side in high-risk patients to limit raw surfaces."},
  {"step": "Epiglottopexy if indicated", "structures": ["lingual surface of epiglottis", "vallecula", "tongue base"],
   "note": "Denude opposing vallecular and lingual epiglottic mucosa and suture the epiglottis forward to the tongue base for posterior epiglottic collapse."},
  {"step": "Final inspection", "structures": ["true vocal folds", "subglottis", "cut edges"],
   "note": "Check hemostasis and absence of thermal injury to the folds."}
 ],
 "landmarks": [
  {"structure": "Aryepiglottic fold", "how_to_find": "Mucosal fold running from the lateral edge of the epiglottis posteriorly to the arytenoid apex; the cuneiform bulge sits in its posterior part and the corniculate at its end", "why": "Short folds are the main target of release"},
  {"structure": "Piriform sinus", "how_to_find": "Gutter lateral to the AE fold, bounded laterally by the thyroid cartilage and thyrohyoid membrane", "why": "The internal SLN runs submucosally in its lateral wall/floor; deep lateral cuts denervate the supraglottis"},
  {"structure": "Interarytenoid mucosa", "how_to_find": "Midline posterior mucosa between the corniculate cartilages, directly above the posterior commissure", "why": "Preserve it to prevent posterior glottic and supraglottic stenosis"},
  {"structure": "Cuneiform cartilages", "how_to_find": "Small rounded elevations within the posterior AE folds, anterior and lateral to the corniculates", "why": "Redundant mucosa over them prolapses into the airway; trim mucosa, not cartilage support"}
 ],
 "danger": [
  {"structure": "Internal branch of the superior laryngeal nerve", "where": "Pierces the thyrohyoid membrane and runs submucosally in the lateral wall/floor of the piriform sinus to the supraglottis", "protect": "Keep AE fold cuts superficial and medial; avoid lateral extension into the piriform sinus", "injury": "Supraglottic sensory loss, aspiration and feeding difficulty"},
  {"structure": "Interarytenoid / posterior commissure mucosa", "where": "Posterior midline between the arytenoids", "protect": "Leave an intact mucosal bridge; avoid circumferential or bilateral contiguous raw surfaces", "injury": "Supraglottic or posterior glottic stenosis"},
  {"structure": "True vocal folds", "where": "Just below the arytenoid trim area", "protect": "Laser shielding, low power and short pulses, cold technique where possible", "injury": "Thermal injury, web, scarring"},
  {"structure": "Epiglottis", "where": "Free margin and lateral edges", "protect": "Avoid overresection of epiglottic edge", "injury": "Aspiration, epiglottic deformity"}
 ],
 "variants": [
  "Olney type 1 (anterior prolapse of arytenoid/cuneiform mucosa), type 2 (short AE folds), type 3 (posterior epiglottic displacement); mixed patterns are common",
  "Tubular or omega-shaped epiglottis",
  "Synchronous airway lesions (subglottic stenosis, tracheomalacia)",
  "State-dependent (sleep-only) or late-onset laryngomalacia, often with neurologic disease"
 ],
 "imaging_check": [
  "Not routinely imaged: flexible awake laryngoscopy showing inspiratory supraglottic collapse",
  "Clinical: feeding and swallow assessment (consider instrumental swallow study) because aspiration may worsen after surgery",
  "Polysomnography or oximetry when sleep-related obstruction is the indication",
  "Assess for neurologic disease, syndromes and reflux that predict poorer outcomes"
 ],
 "blood_nerve": [
  ["Supraglottic sensation", "Internal branch of SLN (from vagus) through the thyrohyoid membrane with the superior laryngeal artery"],
  ["Arterial supply", "Superior laryngeal artery (from superior thyroid artery)"],
  ["Motor", "Aryepiglottic and interarytenoid muscles: RLN"],
  ["Reflex arc", "Laryngeal adductor reflex: afferent internal SLN, efferent RLN"]
 ],
 "pimp": [
  {"q": "What is the most common cause of inspiratory stridor in infants?", "a": "Laryngomalacia"},
  {"q": "Which nerve carries supraglottic sensation, and where does it enter the larynx?", "a": "Internal branch of the superior laryngeal nerve, through the thyrohyoid membrane with the superior laryngeal artery"},
  {"q": "Which cartilages lie within the aryepiglottic fold?", "a": "Cuneiform cartilages, with the corniculates at the arytenoid apices"},
  {"q": "What are the Olney types of laryngomalacia?", "a": "Type 1 arytenoid mucosal prolapse, type 2 short aryepiglottic folds, type 3 posterior epiglottic displacement"},
  {"q": "What feature of supraglottoplasty most raises stenosis risk?", "a": "Removing interarytenoid mucosa or creating bilateral contiguous raw surfaces"},
  {"q": "What are the afferent and efferent limbs of the laryngeal adductor reflex?", "a": "Afferent internal SLN; efferent RLN"},
  {"q": "What is the embryologic origin of the epiglottis?", "a": "Hypobranchial eminence (third/fourth arch mesenchyme)"}
 ],
 "atlas_topics": ["Pediatric Laryngotracheal Airway", "Laryngeal Framework / Intrinsic Muscles", "Superior Laryngeal Nerve / Cricothyroid Space"],
 "sources": [["Cummings Otolaryngology 7e — Congenital disorders of the larynx (laryngomalacia)", ""], ["Olney DR, Greinwald JH, Smith RJ, Bauman NM. Laryngomalacia and its treatment. Laryngoscope 1999", ""], ["Bailey's Head and Neck Surgery — Otolaryngology, pediatric larynx chapter", ""]]
},
"DLB": {
 "title": "Direct Laryngoscopy / Bronchoscopy",
 "region": "Pediatric Otolaryngology",
 "summary": "Pediatric DLB is a shared-airway survey from the supraglottis to the bronchi, done under spontaneous or controlled ventilation. The anatomy that decides safety is the small, nonexpandable cricoid ring (risk of edema with oversized instruments), the posterior glottis where clefts and interarytenoid scar hide, and in tracheotomized children the suprastomal segment and stoma where granulation and collapse occur.",
 "layers": [
  {"step": "Oral entry", "structures": ["lips", "alveolar ridges or primary teeth", "tongue", "vallecula"],
   "note": "Protect gums and teeth; lift along the laryngoscope axis. A large, posteriorly placed tongue (micrognathia, macroglossia) narrows the view."},
  {"step": "Supraglottis", "structures": ["epiglottis", "aryepiglottic folds", "arytenoids", "false folds and ventricles"],
   "note": "Document dynamic collapse with spontaneous breathing before suspension changes the anatomy."},
  {"step": "Glottis", "structures": ["true vocal folds", "anterior commissure", "vocal processes", "posterior commissure / interarytenoid area"],
   "note": "Evaluate mobility in light anesthesia; probe the interarytenoid area for cleft and the arytenoids for fixation versus paralysis."},
  {"step": "Subglottis", "structures": ["conus elasticus", "cricoid ring", "first tracheal ring"],
   "note": "Measure lesion distance below the vocal folds and its length; note whether the stenosis is cartilaginous (firm) or soft."},
  {"step": "Trachea and tracheostomy region", "structures": ["suprastomal anterior wall", "tracheostomy stoma", "tracheal rings", "posterior membranous wall"],
   "note": "In tracheotomized children, remove or pass beside the tube to see suprastomal collapse and granulation and the tube tip site."},
  {"step": "Carina and bronchi", "structures": ["main carina", "right and left main bronchi", "lobar orifices"],
   "note": "Look for malacia, compression and secretions; avoid pushing the telescope into small bronchi."},
  {"step": "Sizing", "structures": ["cricoid lumen", "endotracheal tube outer diameter"],
   "note": "Use the largest tube that leaks at a standard pressure (10-25 cm H2O in the Myer-Cotton system; many centers use about 20 cm H2O); express the result as a Myer-Cotton grade."}
 ],
 "landmarks": [
  {"structure": "Vocal folds as the zero point", "how_to_find": "Use the free edge of the true folds as the reference and measure distances along the telescope or tube to the lesion and the carina", "why": "Reproducible levels for planning reconstruction"},
  {"structure": "Cricoid ring", "how_to_find": "Complete ring just below the conus; firm, round narrowing that does not change with respiration", "why": "Site of congenital and acquired subglottic stenosis"},
  {"structure": "Posterior glottis", "how_to_find": "Spread or probe the arytenoids to expose the interarytenoid notch and posterior commissure; check passive arytenoid mobility by palpation", "why": "Distinguishes posterior glottic scar or fixation from paralysis and finds clefts"},
  {"structure": "Tracheostomy suprastomal segment", "how_to_find": "Anterior tracheal wall just above the stoma, seen from above with the tube withdrawn or from the stoma upward", "why": "Suprastomal collapse and granulation affect decannulation"}
 ],
 "danger": [
  {"structure": "Teeth, alveolar ridges, lips", "where": "Laryngoscope fulcrum", "protect": "Guard and correct lifting technique", "injury": "Dental and soft tissue injury"},
  {"structure": "Glottis in light anesthesia", "where": "Larynx", "protect": "Topical anesthetic at an accepted weight-based dose, adequate depth, coordinated ventilation", "injury": "Laryngospasm, desaturation"},
  {"structure": "Subglottic mucosa", "where": "Within the cricoid ring", "protect": "Age-appropriate instruments, stop sizing at leak, no forced tubes", "injury": "Postoperative edema, stridor, iatrogenic stenosis"},
  {"structure": "Arytenoids", "where": "Posterior glottis", "protect": "Gentle telescope passage", "injury": "Dislocation, scar"},
  {"structure": "Small bronchi and membranous wall", "where": "Distal airway", "protect": "Under-vision movement only", "injury": "Perforation, pneumothorax"}
 ],
 "variants": [
  "Laryngeal cleft or posterior glottic stenosis presenting as aspiration or stridor",
  "Bilateral vocal fold paralysis (check for Arnold-Chiari or other neurologic cause)",
  "Complete tracheal rings, tracheal bronchus, vascular compression",
  "Subglottic cyst or hemangioma"
 ],
 "imaging_check": [
  "Airway films or CT when stenosis, mass or compression is suspected",
  "CT angiography or MRI when vascular compression or complete rings are suspected",
  "Clinical: tracheostomy tube size and length, cervical spine stability and syndromic features"
 ],
 "blood_nerve": [
  ["Laryngeal sensation", "Internal SLN above the folds; RLN below the folds"],
  ["Laryngeal motor", "RLN to all intrinsic muscles except the cricothyroid (external SLN)"],
  ["Arterial supply", "Superior laryngeal artery (superior thyroid) and inferior laryngeal artery (inferior thyroid); tracheal branches from inferior thyroid and bronchial arteries"]
 ],
 "pimp": [
  {"q": "What is the narrowest point of the pediatric airway, and why does it matter?", "a": "The subglottis at the cricoid; it is a complete ring, so edema cannot be accommodated by expansion"},
  {"q": "What uncuffed ETT size formula is used for children over about 2 years?", "a": "Internal diameter (mm) = age/4 + 4"},
  {"q": "What grades make up the Myer-Cotton scale?", "a": "I 0-50%, II 51-70%, III 71-99%, IV no lumen"},
  {"q": "Which intrinsic muscle abducts the vocal folds?", "a": "Posterior cricoarytenoid"},
  {"q": "How do you separate arytenoid fixation from paralysis at DLB?", "a": "Palpate the arytenoid: a paralyzed arytenoid moves passively, a fixed joint or posterior glottic scar does not"},
  {"q": "What is suprastomal collapse?", "a": "Anterior tracheal wall collapse just above a tracheostomy stoma from cartilage weakening"},
  {"q": "Which nerve supplies sensation to the subglottis?", "a": "The recurrent laryngeal nerve"}
 ],
 "atlas_topics": ["Pediatric Laryngotracheal Airway", "Tracheostomy / Cervical Trachea Anatomy"],
 "sources": [["Cummings Otolaryngology 7e — Evaluation of the pediatric airway", ""], ["Myer CM, O'Connor DM, Cotton RT. Ann Otol Rhinol Laryngol 1994", ""], ["Pasha Clinical Reference Guide 6e — Pediatric airway", ""]]
},
"peds-ltr": {
 "title": "Pediatric Laryngotracheal Reconstruction",
 "region": "Pediatric Otolaryngology",
 "summary": "Pediatric LTR enlarges a stenotic subglottis by splitting the cricoid anteriorly, posteriorly or both and holding the split open with carved costal cartilage. The structures that decide safety are the recurrent laryngeal nerves just behind the cricothyroid joints, the esophagus immediately behind the posterior cricoid plate, the anterior commissure above the anterior split, and the pleura during rib harvest.",
 "layers": [
  {"step": "Incision and flaps", "structures": ["skin (horizontal at cricoid level or around stoma)", "platysma", "anterior jugular veins"],
   "note": "Excise or encircle the tracheostomy stoma if present; raise subplatysmal flaps from hyoid to sternal notch."},
  {"step": "Midline exposure", "structures": ["strap muscles (sternohyoid, sternothyroid)", "thyroid isthmus", "cricothyroid muscles", "thyroid cartilage", "cricoid arch", "upper tracheal rings"],
   "note": "Separate straps at the midline raphe, divide the isthmus; expose only the anterior framework and stay medial to the cricothyroid muscles."},
  {"step": "Anterior split", "structures": ["anterior cricoid", "cricothyroid membrane", "lower thyroid cartilage", "first 1-2 tracheal rings", "subglottic scar"],
   "note": "Vertical midline cut through the cricoid and upper rings; extend into the lower thyroid cartilage only as needed and stay below the anterior commissure."},
  {"step": "Posterior split", "structures": ["posterior cricoid lamina", "interarytenoid muscle (if posterior glottic stenosis)", "postcricoid tissue", "hypopharyngeal/esophageal wall"],
   "note": "From inside the airway, cut the posterior lamina in the exact midline through its full height and thickness until the postcricoid tissue bulges; do not breach the esophageal mucosa."},
  {"step": "Costal cartilage harvest", "structures": ["inframammary skin (avoid the breast bud)", "chest wall muscle", "costal cartilage (commonly 5th-7th)", "perichondrium", "pleura"],
   "note": "Harvest cartilage leaving inner perichondrium on the pleura; leak test with saline and a sustained positive-pressure breath."},
  {"step": "Graft carving and inset", "structures": ["anterior boat-shaped graft with flanges", "posterior rectangular graft with flanges", "perichondrium (toward lumen)", "cut cricoid edges"],
   "note": "Flanges rest outside the cut edges so the graft cannot prolapse; sutures are placed outside the mucosa."},
  {"step": "Stent or tube and closure", "structures": ["stent or nasotracheal tube", "suprastomal segment", "strap muscles over graft", "drain"],
   "note": "Single-stage repair uses an endotracheal tube as stent; double-stage uses a stent with a tracheostomy. Cover the graft with straps and drain the wound."}
 ],
 "landmarks": [
  {"structure": "Cricoid arch", "how_to_find": "Ring palpable just below the thyroid cartilage and cricothyroid membrane; in infants it lies very close beneath the thyroid lamina edge", "why": "Center of the anterior split"},
  {"structure": "Anterior commissure", "how_to_find": "Roughly at mid-height of the thyroid cartilage in the midline; confirm by viewing from inside or with a needle through the cartilage", "why": "Keep the anterior split below it to avoid a web"},
  {"structure": "Posterior cricoid midline", "how_to_find": "From the opened airway, the midline between the arytenoids in line with the interarytenoid notch; an NG tube behind it helps feel the depth", "why": "Exact midline protects the cricoarytenoid joints and esophagus"},
  {"structure": "RLN entry", "how_to_find": "Posterior to the cricothyroid joint (palpable on the posterolateral cricoid), deep to the inferior constrictor lower edge", "why": "Avoid all lateral cricoid dissection"},
  {"structure": "Costal cartilage", "how_to_find": "Palpate the bony-cartilaginous junction of the chosen rib below the inframammary crease; cartilage is white, rubbery and blends into the costal margin", "why": "Adequate straight segment for the graft"}
 ],
 "danger": [
  {"structure": "Recurrent laryngeal nerves", "where": "Tracheoesophageal grooves, entering the larynx behind the cricothyroid joints", "protect": "Midline-only dissection; posterior split exactly midline", "injury": "Vocal fold paralysis, airway compromise if bilateral"},
  {"structure": "Esophagus", "where": "Immediately posterior to the posterior cricoid lamina", "protect": "Controlled cartilage-only cut; palpate the NG tube", "injury": "Perforation, fistula, graft infection"},
  {"structure": "Anterior commissure", "where": "Midline thyroid cartilage at about mid-height", "protect": "Limit superior extent of the split; precise closure if laryngofissure is needed", "injury": "Anterior glottic web, dysphonia"},
  {"structure": "Pleura", "where": "Deep to the inner perichondrium", "protect": "Subperichondrial harvest; leak test", "injury": "Pneumothorax"},
  {"structure": "Innominate artery and brachiocephalic vein", "where": "Can lie at or above the sternal notch in infants and children", "protect": "Avoid low dissection; palpate before working near the notch", "injury": "Major hemorrhage"},
  {"structure": "Graft", "where": "Within the split framework", "protect": "Flanged design and secure inset; check endoscopically", "injury": "Graft prolapse into the lumen, displacement, restenosis"}
 ],
 "variants": [
  "High-riding innominate artery or brachiocephalic vein in infants",
  "Thymus extending into the lower neck in infants",
  "Associated posterior glottic stenosis or laryngeal cleft",
  "Syndromic airway with additional tracheal stenosis or complete rings"
 ],
 "imaging_check": [
  "Operative DLB findings are the key study: grade, length, distance from vocal folds, glottic involvement",
  "CT neck/chest when tracheal extension or extrinsic compression is suspected",
  "Clinical: vocal fold mobility, reflux and eosinophilic esophagitis control, pulmonary status for single-stage repair",
  "Swallow assessment when posterior work or aspiration risk is planned"
 ],
 "blood_nerve": [
  ["Laryngeal arteries", "Superior laryngeal (superior thyroid), cricothyroid branch, inferior laryngeal (inferior thyroid)"],
  ["Tracheal supply", "Lateral segmental vessels from the inferior thyroid and bronchial arteries"],
  ["Motor nerves", "RLN to intrinsic muscles except cricothyroid; external SLN to cricothyroid"],
  ["Rib site", "Intercostal vein, artery and nerve along the inferior rib border"]
 ],
 "pimp": [
  {"q": "What are the Myer-Cotton grades?", "a": "I 0-50%, II 51-70%, III 71-99%, IV no lumen"},
  {"q": "Why must the posterior cricoid split be midline?", "a": "To avoid the cricoarytenoid joints and keep symmetric expansion; the esophagus lies directly behind"},
  {"q": "What is the difference between single-stage and double-stage LTR?", "a": "Single-stage stents with an endotracheal tube and removes the tracheostomy; double-stage keeps a tracheostomy with a stent"},
  {"q": "Where does the RLN enter the larynx?", "a": "Posterior to the cricothyroid joint, beneath the inferior constrictor"},
  {"q": "What embryologic arch gives rise to the cricoid?", "a": "Sixth arch in most board texts (the laryngeal cartilages other than the epiglottis arise from fused fourth and sixth arch mesenchyme, so some sources say fourth and sixth)"},
  {"q": "What incision consideration applies to rib harvest in girls?", "a": "Place the incision below and away from the breast bud (inframammary)"},
  {"q": "Which way is the perichondrium oriented on the graft?", "a": "Toward the airway lumen"}
 ],
 "atlas_topics": ["Pediatric Laryngotracheal Airway", "Tracheostomy / Cervical Trachea Anatomy", "Laryngeal Framework / Intrinsic Muscles"],
 "sources": [["Cummings Otolaryngology 7e — Glottic and subglottic stenosis in children", ""], ["Myers Operative Otolaryngology — Laryngotracheal reconstruction", ""], ["Cotton RT. Management of subglottic stenosis. Otolaryngol Clin North Am", ""]]
},
"airway-fb": {
 "title": "Rigid Bronchoscopy for Airway Foreign Body",
 "region": "Pediatric Otolaryngology",
 "summary": "Rigid bronchoscopy in children passes a ventilating scope through a small, high larynx into a short trachea to retrieve aspirated objects, most often from a main bronchus. The anatomy that decides safety is the size of the subglottis relative to the object, and the fact that an object lost at the glottis or subglottis can block the whole airway; if that happens, push it back into a main bronchus so one lung can be ventilated.",
 "layers": [
  {"step": "Oral entry and laryngeal exposure", "structures": ["lips and teeth", "tongue", "vallecula", "epiglottis", "arytenoids"],
   "note": "Expose the larynx with a laryngoscope; check for a laryngeal or supraglottic object before passing the bronchoscope."},
  {"step": "Glottic passage", "structures": ["true vocal folds", "posterior glottis"],
   "note": "Rotate the bronchoscope bevel to align with a fold, pass under vision, then return to midline."},
  {"step": "Subglottis and trachea", "structures": ["cricoid ring", "tracheal rings", "posterior membranous wall"],
   "note": "The cricoid limits both scope size and the size of object that can be withdrawn through it."},
  {"step": "Carina survey", "structures": ["main carina", "right main bronchus", "left main bronchus"],
   "note": "Survey both sides, starting with the uninvolved side when possible, before manipulating the object; note edema, granulation and pus."},
  {"step": "Object capture", "structures": ["object", "bronchial wall", "granulation tissue", "distal secretions"],
   "note": "Use optical forceps matched to the object; grasp the leading edge and protect the wall from sharp edges."},
  {"step": "Withdrawal through the glottis", "structures": ["bronchoscope tip", "subglottis", "glottis"],
   "note": "Withdraw object, forceps and scope as a unit when the object is larger than the scope lumen; the glottis is where objects are stripped off."},
  {"step": "Second look", "structures": ["both bronchial trees", "lobar orifices", "mucosa"],
   "note": "Reinsert to check for additional fragments, retained pieces (especially nuts), bleeding and distal secretions."}
 ],
 "landmarks": [
  {"structure": "Main carina", "how_to_find": "Sharp ridge at the end of the trachea; in a supine child with the surgeon at the head, the right bronchus is on the surgeon's right", "why": "Starting point to assign the object side"},
  {"structure": "Right main bronchus", "how_to_find": "Turn the head to the left to align the scope; the right upper lobe orifice sits on the lateral wall just beyond the carina", "why": "Common site of aspirated objects"},
  {"structure": "Left main bronchus", "how_to_find": "Turn the head to the right; longer bronchus passing under the aortic arch before dividing into upper and lower lobe bronchi", "why": "Objects here may need a longer scope or telescope"},
  {"structure": "Subglottis", "how_to_find": "Complete cricoid ring a short distance below the vocal folds", "why": "Narrowest point; a dropped object here causes complete obstruction"}
 ],
 "danger": [
  {"structure": "Subglottis / glottis during withdrawal", "where": "Cricoid ring and vocal folds", "protect": "Withdraw as a unit; if the object drops and obstructs, push it distally into a main bronchus and ventilate", "injury": "Complete airway obstruction, cardiac arrest"},
  {"structure": "Bronchial wall", "where": "Around the impacted object, often inflamed with granulation", "protect": "Gentle grasp, no blind forceps closure, control granulation bleeding", "injury": "Perforation, pneumothorax, pneumomediastinum, bleeding"},
  {"structure": "Distal airway", "where": "Beyond the object", "protect": "Avoid pushing the object deeper; use telescopes for view", "injury": "Object migration to a smaller bronchus, lobar collapse"},
  {"structure": "Teeth and arytenoids", "where": "Entry route", "protect": "Guard, gentle passage", "injury": "Dental injury, arytenoid dislocation"},
  {"structure": "Laryngeal and subglottic mucosa", "where": "Within the cricoid", "protect": "Appropriate scope size and limited passes; steroids if edema", "injury": "Postoperative stridor and edema"}
 ],
 "variants": [
  "Bilateral or multiple foreign bodies (fragmenting nuts, seeds)",
  "Laryngeal or tracheal objects, which carry the highest risk of complete obstruction",
  "Tracheal bronchus or other branching variants altering the expected route",
  "Chronic retained object with granulation, stricture or bronchiectasis"
 ],
 "imaging_check": [
  "Inspiratory/expiratory or lateral decubitus films for air trapping (ball-valve) on the affected side",
  "Most objects (nuts, food) are radiolucent; a normal film does not exclude aspiration",
  "CT in selected stable patients with unclear history",
  "Clinical: choking episode, unilateral decreased breath sounds or wheeze"
 ],
 "blood_nerve": [
  ["Bronchial arteries", "From the descending aorta or intercostal arteries; bleeding from inflamed mucosa"],
  ["Airway sensation", "Internal SLN above the folds; RLN and vagal pulmonary branches below (cough reflex)"],
  ["Adjacent great vessels", "Innominate artery anterior to the distal trachea; aortic arch over the left main bronchus; pulmonary arteries beside the lobar bronchi"]
 ],
 "pimp": [
  {"q": "What do you do if a foreign body drops and obstructs the subglottis during removal?", "a": "Push it back into a main bronchus to restore ventilation of at least one lung, then retry"},
  {"q": "Which side do airway foreign bodies favor in children?", "a": "Right main bronchus overall, though the difference is smaller in young children than in adults"},
  {"q": "What radiographic sign suggests a bronchial foreign body?", "a": "Air trapping (hyperinflation) on the affected side on expiratory or decubitus films"},
  {"q": "Why are peanuts particularly harmful?", "a": "They fragment and their oils cause marked mucosal inflammation"},
  {"q": "What does a rigid bronchoscope size number indicate?", "a": "A nominal size that equals neither the internal nor the outer diameter (e.g., a Storz 3.5 has about 5.0 mm ID and 5.7 mm OD); check the manufacturer's chart against the child's age"},
  {"q": "Which way do you turn the head to enter the right main bronchus?", "a": "To the left"},
  {"q": "At what level is the carina in an adult, and how long is the trachea?", "a": "About T4-T5; the adult trachea is about 10-13 cm long"}
 ],
 "atlas_topics": ["Pediatric Laryngotracheal Airway", "Tracheostomy / Cervical Trachea Anatomy"],
 "sources": [["Cummings Otolaryngology 7e — Foreign bodies of the airway and esophagus", ""], ["K.J. Lee Essential Otolaryngology 12e — Pediatric airway foreign bodies", ""], ["Pasha Clinical Reference Guide 6e — Foreign bodies", ""]]
},
"tonsillectomy": {
 "title": "Tonsillectomy",
 "region": "Pediatric Otolaryngology",
 "summary": "Tonsillectomy removes the palatine tonsil in the areolar plane between its capsule and the superior constrictor. Safety depends on staying on the capsule: lateral to the constrictor lie the parapharyngeal space and the carotid arteries, and at the lower pole the glossopharyngeal nerve and the main arterial supply (tonsillar branch of the facial artery) sit just deep to the fossa.",
 "layers": [
  {"step": "Mouth gag and exposure", "structures": ["maxillary teeth", "tongue (under gag blade)", "uvula and soft palate", "anterior and posterior tonsillar pillars", "posterior pharyngeal wall"],
   "note": "Seat the blade in the midline with the endotracheal tube in its groove; suspend without excess tongue compression. Palpate the posterior wall for an aberrant pulsatile carotid when syndromic (e.g., 22q11 deletion)."},
  {"step": "Superior pole mucosal incision", "structures": ["anterior pillar (palatoglossus muscle)", "supratonsillar fossa", "tonsillar capsule"],
   "note": "Retract the tonsil medially and incise the mucosa just lateral to the anterior pillar at the superior pole to find the white capsule."},
  {"step": "Capsular plane", "structures": ["tonsillar capsule (pharyngobasilar fascia condensation)", "loose areolar plane", "superior constrictor muscle (lateral bed)", "paratonsillar (external palatine) vein"],
   "note": "Stay on the capsule with traction medially; the constrictor fibers are horizontal and should stay in the fossa."},
  {"step": "Posterior pillar and mid-fossa", "structures": ["posterior pillar (palatopharyngeus muscle)", "tonsillar bed vessels"],
   "note": "Separate the tonsil from the posterior pillar without cutting palatopharyngeus, preserving palatal function."},
  {"step": "Lower pole", "structures": ["plica triangularis", "lingual tonsil junction", "tonsillar branch of facial artery", "dorsal lingual vessels", "glossopharyngeal nerve (deep, at the lower pole lateral to the constrictor)"],
   "note": "Release the lower pole under vision; avoid deep cautery and deep suture ligatures here."},
  {"step": "Hemostasis and inspection", "structures": ["superior pole", "mid-fossa", "lower pole", "pillars"],
   "note": "Use targeted cautery only; release the gag and recheck at normal venous pressure."}
 ],
 "landmarks": [
  {"structure": "Capsular plane", "how_to_find": "At the superior pole incise just inside the anterior pillar; the capsule is a white, smooth fibrous layer and the plane opens with blunt pressure", "why": "The bloodless plane that keeps you off the constrictor"},
  {"structure": "Superior constrictor", "how_to_find": "Horizontal, pink muscle fibers forming the lateral wall of the fossa after the tonsil is lifted", "why": "Fibers on the specimen mean you are too deep"},
  {"structure": "Lower pole vascular pedicle", "how_to_find": "At the lower pole near the tongue base junction, where the tonsillar branch of the facial artery enters the lateral surface", "why": "Main bleeding point; controlled precisely"},
  {"structure": "Paratonsillar (external palatine) vein", "how_to_find": "Descends from the soft palate on the lateral surface of the capsule near the superior pole", "why": "Common source of superior pole bleeding"},
  {"structure": "Internal carotid artery position", "how_to_find": "Posterolateral to the fossa, classically about 2-2.5 cm away in adults but much closer in children (MRI means under about 1 cm, minimum about 2 mm); palpate the lateral and posterior pharyngeal walls for pulsation", "why": "Medial displacement in syndromic children changes risk"}
 ],
 "danger": [
  {"structure": "Glossopharyngeal nerve", "where": "Lateral to the superior constrictor at the lower pole of the fossa, entering the tongue base", "protect": "Stay on the capsule, minimize deep lower-pole cautery and deep sutures", "injury": "Loss of taste and sensation to the posterior third of the tongue, pharyngeal pain"},
  {"structure": "Internal and external carotid arteries", "where": "Parapharyngeal space lateral to the constrictor; ICA posterolateral, ECA anterolateral to the fossa", "protect": "No dissection lateral to the constrictor, no deep suture ligatures, palpate for aberrant pulsation", "injury": "Massive hemorrhage, pseudoaneurysm"},
  {"structure": "Palatopharyngeus and soft palate", "where": "Posterior pillar and superior pole", "protect": "Preserve pillars and uvula; avoid cautery burns of the palate", "injury": "Velopharyngeal insufficiency, nasopharyngeal stenosis"},
  {"structure": "Lingual and hypoglossal nerves; teeth", "where": "Under the gag blade and tongue base", "protect": "Limit suspension time and pressure; check teeth", "injury": "Temporary taste disturbance or tongue numbness/weakness, dental injury"},
  {"structure": "Atlantoaxial region", "where": "Prevertebral space behind the posterior wall", "protect": "Avoid deep posterior wall cautery; caution with neck extension in Down syndrome", "injury": "Grisel syndrome (atlantoaxial subluxation)"}
 ],
 "variants": [
  "Medialized or tortuous internal carotid (22q11.2 deletion, velocardiofacial syndrome)",
  "Elongated styloid process palpable in the fossa (Eagle syndrome)",
  "Submucous cleft palate (bifid uvula, zona pellucida, notched hard palate) affecting VPI risk",
  "Tonsil extending low into the lingual tonsil or high into the soft palate"
 ],
 "imaging_check": [
  "Not routinely imaged: check for bleeding disorder history, loose teeth, cleft or submucous cleft signs",
  "Palpate or inspect for pulsatile posterior pharyngeal wall in syndromic children; CT angiography if suspected",
  "Cervical spine assessment per local protocol in Down syndrome"
 ],
 "blood_nerve": [
  ["Arterial supply (five arteries)", "Tonsillar branch of facial (main, lower pole), ascending palatine (facial), dorsal lingual (lingual), ascending pharyngeal (ECA), lesser palatine (descending palatine of maxillary)"],
  ["Venous", "Paratonsillar (external palatine) vein to the pharyngeal plexus and facial vein"],
  ["Sensory", "Glossopharyngeal nerve tonsillar branches and lesser palatine nerves (V2)"],
  ["Lymphatics", "Jugulodigastric (level II) nodes"]
 ],
 "pimp": [
  {"q": "Name the five arteries of the palatine tonsil.", "a": "Tonsillar branch of facial, ascending palatine, dorsal lingual, ascending pharyngeal, lesser palatine"},
  {"q": "Which artery is the main supply?", "a": "Tonsillar branch of the facial artery, entering the lower pole"},
  {"q": "What muscles form the tonsillar pillars?", "a": "Anterior: palatoglossus; posterior: palatopharyngeus"},
  {"q": "What forms the lateral wall of the tonsillar fossa?", "a": "Superior constrictor muscle (with the pharyngobasilar fascia)"},
  {"q": "Through which nerve is post-tonsillectomy otalgia referred?", "a": "Glossopharyngeal nerve, via its tympanic (Jacobson) branch"},
  {"q": "From which pharyngeal pouch does the palatine tonsil develop?", "a": "Second pharyngeal pouch"},
  {"q": "Which syndrome has medialized internal carotid arteries?", "a": "22q11.2 deletion (velocardiofacial) syndrome"},
  {"q": "What is Grisel syndrome?", "a": "Nontraumatic atlantoaxial subluxation from inflammation after pharyngeal infection or surgery"}
 ],
 "atlas_topics": ["Palatal / Lateral Pharyngeal Wall Anatomy for Sleep Surgery", "Parapharyngeal / Retropharyngeal Spaces", "External Carotid Artery Branches / Major Hemorrhage Anatomy"],
 "sources": [["Cummings Otolaryngology 7e — Pharyngitis and tonsillectomy chapters", ""], ["K.J. Lee Essential Otolaryngology 12e — Adenotonsillar disease", ""], ["Bailey's Head and Neck Surgery — Otolaryngology, tonsillectomy chapter", ""]]
},
"adenoidectomy": {
 "title": "Adenoidectomy",
 "region": "Pediatric Otolaryngology",
 "summary": "Adenoidectomy clears lymphoid tissue from the nasopharynx to open the choanae and the Eustachian tube orifices. Safety depends on staying in the midline posterior wall, preserving the torus tubarius laterally and leaving an inferior band in children at risk of velopharyngeal insufficiency (submucous cleft, neuromuscular disease).",
 "layers": [
  {"step": "Gag and palate check", "structures": ["hard palate", "soft palate", "uvula"],
   "note": "Look for bifid uvula and zona pellucida and palpate for a notch in the posterior hard palate (submucous cleft) before removing tissue."},
  {"step": "Palatal retraction", "structures": ["soft palate", "red rubber catheters through the nose"],
   "note": "Retract the soft palate anteriorly with catheters; avoid tearing the palate."},
  {"step": "Nasopharyngeal survey", "structures": ["choanae", "vomer posterior edge", "adenoid pad (posterosuperior wall)", "torus tubarius", "Eustachian tube orifices", "fossae of Rosenmuller"],
   "note": "Use a mirror or endoscope to see the full pad and both tori before starting."},
  {"step": "Central removal", "structures": ["adenoid pad", "pharyngobasilar fascia / prevertebral fascia (deep)", "longus capitis muscle (deep)"],
   "note": "Remove tissue in the midline from the choanae downward; stay superficial to the prevertebral fascia."},
  {"step": "Lateral and inferior limits", "structures": ["torus tubarius", "salpingopharyngeal fold", "Passavant ridge region", "inferior adenoid band"],
   "note": "Spare the torus and its mucosa; leave an inferior band of tissue when VPI risk exists."},
  {"step": "Hemostasis and inspection", "structures": ["adenoid bed", "choanae", "posterior nasal cavity"],
   "note": "Suction cautery or packs; remove every pack; check choanal patency."}
 ],
 "landmarks": [
  {"structure": "Torus tubarius", "how_to_find": "Cartilaginous ridge on the lateral nasopharyngeal wall just behind the inferior turbinate's posterior end, framing the Eustachian tube orifice", "why": "Lateral limit of resection"},
  {"structure": "Fossa of Rosenmuller", "how_to_find": "Recess posterior and superior to the torus", "why": "Residual lateral tissue may persist here; deep work risks the ET and parapharyngeal space"},
  {"structure": "Choanae and vomer", "how_to_find": "Paired openings separated by the vomer's posterior edge in the midline anteriorly", "why": "Endpoint of airway clearance"},
  {"structure": "Prevertebral plane", "how_to_find": "Smooth firm surface deep to the adenoid bed overlying the atlas; the anterior arch of C1 is palpable inferiorly", "why": "Do not cauterize deeply here"}
 ],
 "danger": [
  {"structure": "Eustachian tube orifice and torus", "where": "Lateral nasopharyngeal walls", "protect": "Keep instruments medial to the torus; limited lateral cautery", "injury": "Scarring, ET dysfunction, otitis media"},
  {"structure": "Velopharyngeal valve", "where": "Inferior nasopharynx at the level of palatal closure", "protect": "Assess for submucous cleft; leave an inferior band or do partial (superior) adenoidectomy", "injury": "Hypernasality, nasal regurgitation (VPI)"},
  {"structure": "Prevertebral fascia and C1-C2", "where": "Deep to the adenoid bed", "protect": "Avoid deep curettage and extensive cautery; caution with neck extension in Down syndrome", "injury": "Grisel syndrome, cervical instability"},
  {"structure": "Soft palate", "where": "Retracted anteriorly", "protect": "Gentle retraction, avoid thermal injury", "injury": "Palatal injury, nasopharyngeal stenosis (more with concurrent tonsillectomy)"},
  {"structure": "Aberrant internal carotid", "where": "Rarely medialized near the lateral nasopharyngeal wall", "protect": "Look for pulsation; stay midline", "injury": "Hemorrhage"}
 ],
 "variants": [
  "Submucous cleft palate (Calnan triad: bifid uvula, zona pellucida, notched posterior hard palate)",
  "Thornwaldt cyst in the midline (notochordal remnant)",
  "Choanal stenosis or atresia",
  "Large tubal tonsils near the torus"
 ],
 "imaging_check": [
  "Not routinely imaged: lateral neck film or flexible endoscopy may confirm adenoid size",
  "Clinical: speech and palate exam for VPI risk; cleft history",
  "Cervical spine screening per protocol in Down syndrome",
  "Bleeding history"
 ],
 "blood_nerve": [
  ["Arterial supply", "Ascending pharyngeal artery, ascending palatine artery, pharyngeal branch of the maxillary artery, artery of the pterygoid canal, tonsillar branch of facial"],
  ["Venous", "Pharyngeal venous plexus"],
  ["Sensory", "Pharyngeal branch of V2 (via the pterygopalatine ganglion) and glossopharyngeal nerve"],
  ["Lymphatics", "Retropharyngeal (node of Rouviere) and level II nodes"]
 ],
 "pimp": [
  {"q": "What are the boundaries of the nasopharynx?", "a": "Anterior choanae; superior/posterior basisphenoid, basiocciput and C1; lateral Eustachian tube openings and fossae of Rosenmuller; inferior soft palate"},
  {"q": "What is the Calnan triad?", "a": "Bifid uvula, zona pellucida, notched posterior hard palate (submucous cleft)"},
  {"q": "Which muscle opens the Eustachian tube?", "a": "Tensor veli palatini (CN V3), assisted by levator veli palatini (vagus via pharyngeal plexus)"},
  {"q": "What is a Thornwaldt cyst?", "a": "Midline nasopharyngeal cyst from a notochordal remnant"},
  {"q": "What is Passavant ridge?", "a": "A bulge of the posterior pharyngeal wall during velopharyngeal closure formed by superior constrictor/palatopharyngeus fibers"},
  {"q": "What is the first-echelon node draining the nasopharynx?", "a": "Lateral retropharyngeal node (node of Rouviere)"},
  {"q": "What is Grisel syndrome?", "a": "Atlantoaxial subluxation after inflammation of the pharynx, including after adenoidectomy"}
 ],
 "atlas_topics": ["Eustachian Tube / Tensor–Levator Relationships", "Parapharyngeal / Retropharyngeal Spaces", "Cleft Palate Levator Sling / Tensor / Eustachian Tube"],
 "sources": [["Cummings Otolaryngology 7e — Adenotonsillar disease in children", ""], ["K.J. Lee Essential Otolaryngology 12e — Adenoidectomy", ""], ["Pasha Clinical Reference Guide 6e — Adenotonsillar disease", ""]]
},
"thyroglossal": {
 "title": "Sistrunk Procedure",
 "region": "Pediatric Otolaryngology",
 "summary": "The Sistrunk procedure removes a thyroglossal duct cyst with the central hyoid body and a core of tongue-base tissue toward the foramen cecum, following the descent path of the thyroid. Safety and cure depend on taking only the central hyoid (medial to the lesser cornua) so the hypoglossal nerves and lingual arteries lateral to the greater cornua are safe, and on confirming normal thyroid tissue in the neck first.",
 "layers": [
  {"step": "Incision and flaps", "structures": ["skin crease over the cyst", "platysma", "anterior jugular veins"],
   "note": "Horizontal incision over the cyst, often at hyoid level; ellipse around any sinus or prior scar. Raise subplatysmal flaps to above the hyoid."},
  {"step": "Cyst and strap muscles", "structures": ["sternohyoid (superficial)", "thyrohyoid and sternothyroid (deeper)", "thyrohyoid membrane", "cyst wall"],
   "note": "The cyst usually lies in the midline over the thyrohyoid membrane, deep to or between the straps; free it without rupture."},
  {"step": "Hyoid body", "structures": ["hyoid body", "lesser cornua", "mylohyoid and geniohyoid (superior attachments)", "sternohyoid and thyrohyoid (inferior attachments)"],
   "note": "Detach muscles from the central hyoid and divide the bone on each side of the tract, medial to the lesser cornua (about 1-1.5 cm central segment)."},
  {"step": "Suprahyoid core", "structures": ["geniohyoid", "genioglossus", "tongue base toward foramen cecum"],
   "note": "Take a core of tissue angled upward and backward toward the foramen cecum; a finger in the mouth on the foramen cecum guides direction."},
  {"step": "Pharyngeal limit", "structures": ["vallecula / tongue base mucosa", "foramen cecum"],
   "note": "Divide the core just short of mucosa; close any mucosal entry primarily."},
  {"step": "Closure", "structures": ["strap muscles", "platysma", "drain (selective)"],
   "note": "Reapproximate straps over the hyoid gap; the hyoid ends do not need to be wired."}
 ],
 "landmarks": [
  {"structure": "Hyoid body", "how_to_find": "Palpable horizontal bar above the thyroid notch; the thyroid cartilage is below the thyrohyoid membrane. In infants the hyoid may sit close to or overlap the thyroid cartilage", "why": "Avoid mistaking the thyroid cartilage for the hyoid"},
  {"structure": "Lesser cornua", "how_to_find": "Small upward projections at the junction of the hyoid body and greater cornua", "why": "Lateral limit of the bone cut"},
  {"structure": "Foramen cecum", "how_to_find": "Midline pit at the apex of the sulcus terminalis (junction of anterior two thirds and posterior third of the tongue); press on it from the mouth", "why": "Target of the suprahyoid core"},
  {"structure": "Cyst tract", "how_to_find": "Midline fibrous cord from the cyst upward to the hyoid, passing anterior to, through or posterior to the bone", "why": "Must be removed en bloc for cure"}
 ],
 "danger": [
  {"structure": "Hypoglossal nerves", "where": "Lateral, running above the greater cornua of the hyoid between hyoglossus and mylohyoid", "protect": "Keep the bone cut medial to the lesser cornua and the core in the midline", "injury": "Tongue weakness, dysarthria, dysphagia"},
  {"structure": "Lingual arteries", "where": "Deep to hyoglossus just above the greater cornua", "protect": "Midline dissection", "injury": "Bleeding, tongue base hematoma"},
  {"structure": "Pharynx at the vallecula", "where": "Deep and superior to the core", "protect": "Stop short of mucosa; close any entry in layers", "injury": "Pharyngocutaneous fistula, infection"},
  {"structure": "Internal branch of SLN", "where": "Pierces the thyrohyoid membrane laterally", "protect": "Avoid lateral dissection on the membrane", "injury": "Supraglottic sensory loss"},
  {"structure": "Thyroid cartilage / airway", "where": "Just below the hyoid, especially in infants", "protect": "Confirm the hyoid before cutting", "injury": "Laryngeal framework injury"}
 ],
 "variants": [
  "Ectopic thyroid in the cyst may be the only functioning thyroid tissue",
  "Lingual thyroid at the foramen cecum",
  "Pyramidal lobe extending up toward the hyoid",
  "Off-midline or suprahyoid/intralingual cysts",
  "Papillary carcinoma in a small percentage (about 1%) of adult cysts"
 ],
 "imaging_check": [
  "Ultrasound to confirm a normal thyroid gland in the neck and cyst character",
  "Thyroid function tests or scintigraphy if no normal gland is seen",
  "CT or MRI for atypical, recurrent or suspicious solid lesions",
  "Fine-needle aspiration of solid components in adults"
 ],
 "blood_nerve": [
  ["Arterial", "Branches of the superior thyroid and lingual arteries near the hyoid"],
  ["Venous", "Anterior jugular veins superficially"],
  ["Nerves at risk", "Hypoglossal (lateral above the hyoid), internal SLN (lateral thyrohyoid membrane)"],
  ["Hyoid muscles", "Suprahyoid: mylohyoid, geniohyoid, digastric, stylohyoid; infrahyoid: sternohyoid, omohyoid, thyrohyoid"]
 ],
 "pimp": [
  {"q": "Where does the thyroid originate?", "a": "Foramen cecum, at the junction of the anterior two thirds and posterior third of the tongue"},
  {"q": "What is the embryology of the hyoid?", "a": "Second arch: lesser cornua and upper body; third arch: greater cornua and lower body"},
  {"q": "Why is the central hyoid removed?", "a": "The duct descends in close relation to the developing hyoid and may pass through it; leaving it raises recurrence"},
  {"q": "What is the recurrence rate after Sistrunk versus simple excision?", "a": "Roughly 3-5% after Sistrunk (most series under 10%) versus about 40-70% after cyst excision alone in commonly cited series"},
  {"q": "What is the most common congenital neck mass in children?", "a": "Thyroglossal duct cyst"},
  {"q": "Why does a thyroglossal duct cyst elevate with tongue protrusion?", "a": "The tract attaches to the foramen cecum and hyoid"},
  {"q": "What must be confirmed before excision?", "a": "Presence of a normal thyroid gland in the neck"},
  {"q": "What is the most common malignancy in a thyroglossal duct cyst?", "a": "Papillary thyroid carcinoma"}
 ],
 "atlas_topics": ["Tongue Base / Hyoid / Suprahyoid Relationships", "Neck Levels / Fascial Compartments", "Submandibular Triangle / Floor of Mouth"],
 "sources": [["Cummings Otolaryngology 7e — Congenital neck masses", ""], ["Sistrunk WE. The surgical treatment of cysts of the thyroglossal tract. Ann Surg 1920", ""], ["K.J. Lee Essential Otolaryngology 12e — Pediatric neck masses", ""]]
},
"branchial": {
 "title": "Branchial Cleft Anomaly Excision",
 "region": "Pediatric Otolaryngology",
 "summary": "Branchial anomalies follow the course of their arch: each tract runs deep to the derivatives of its own arch and superficial to those of the next arch. Complete removal therefore means following the tract past predictable structures: the facial nerve for first-cleft lesions, the carotid bifurcation and hypoglossal and glossopharyngeal nerves for second-cleft lesions, and the thyrohyoid membrane and SLN for third and fourth pouch tracts to the piriform sinus.",
 "layers": [
  {"step": "Incision", "structures": ["skin crease over the lesion", "ellipse around the fistula opening at the anterior SCM border", "platysma"],
   "note": "For a long second-cleft tract use stepladder (stacked) incisions; for first-cleft lesions use a parotidectomy-type incision."},
  {"step": "Superficial dissection", "structures": ["platysma", "superficial layer of deep cervical fascia", "anterior border of SCM", "external jugular vein and great auricular nerve (high lesions)"],
   "note": "Free the cyst wall without rupture; retract SCM posteriorly."},
  {"step": "First-cleft anomaly", "structures": ["parotid gland", "facial nerve trunk and branches", "cartilaginous EAC", "bony-cartilaginous EAC junction"],
   "note": "Find the facial nerve trunk first; Work type II tracts pass through the parotid and may run superficial to, deep to or between facial nerve branches toward the EAC."},
  {"step": "Second-cleft tract", "structures": ["carotid sheath", "hypoglossal nerve", "glossopharyngeal nerve", "external and internal carotid arteries", "posterior belly of digastric and stylohyoid", "tonsillar fossa"],
   "note": "The tract ascends along the carotid sheath, superficial to CN XII and IX, between ECA and ICA, deep to the posterior belly of digastric and stylohyoid, to the tonsillar fossa."},
  {"step": "Third/fourth pouch tracts", "structures": ["thyrohyoid membrane", "internal branch of SLN", "piriform sinus", "thyroid lobe (often left)"],
   "note": "Third tracts pass posterior to the ICA and enter the piriform sinus through the thyrohyoid membrane above the internal SLN; fourth tracts run below the SLN. Endoscopic cautery of the piriform opening is often combined or used alone."},
  {"step": "Tract endpoint and closure", "structures": ["pharyngeal opening", "carotid sheath contents", "wound layers"],
   "note": "Ligate the tract at the pharyngeal wall; inspect vessels and nerves; close in layers."}
 ],
 "landmarks": [
  {"structure": "Facial nerve trunk (first-cleft)", "how_to_find": "Tragal pointer (about 1 cm deep, anterior-inferior), tympanomastoid suture (about 6-8 mm deep to its outer end), at the depth of the posterior belly of digastric", "why": "Identify before following the tract"},
  {"structure": "Carotid bifurcation", "how_to_find": "Usually near the upper border of the thyroid cartilage (range about C3-C4); ECA has branches and lies anteromedial, ICA has none in the neck", "why": "Second-cleft tract passes through the fork"},
  {"structure": "Hypoglossal nerve", "how_to_find": "Crosses superficial to ICA and ECA just below the posterior belly of digastric, looping around the occipital artery's SCM branch; follow the descendens hypoglossi upward", "why": "Lies deep to the second-cleft tract"},
  {"structure": "Glossopharyngeal nerve", "how_to_find": "Runs with the stylopharyngeus, between ICA and ECA, deep to the styloid process, toward the tonsil bed", "why": "At risk near the upper tract"},
  {"structure": "Piriform sinus opening", "how_to_find": "On direct laryngoscopy, a pit at the apex or anterolateral wall of the piriform sinus; cannulate to guide external dissection", "why": "Endpoint of third/fourth pouch tracts"}
 ],
 "danger": [
  {"structure": "Facial nerve", "where": "Within the parotid in relation to first-cleft tracts, sometimes medial to the tract", "protect": "Identify the trunk first and dissect antegrade, monitor", "injury": "Facial paralysis"},
  {"structure": "Internal and external carotid arteries", "where": "Second-cleft tract between them; third tract posterior to ICA", "protect": "Dissect on the tract wall, no traction avulsion", "injury": "Hemorrhage, stroke"},
  {"structure": "Hypoglossal nerve", "where": "Deep to the second-cleft tract, superficial to the carotids", "protect": "Identify before dividing tissue near the bifurcation", "injury": "Tongue weakness"},
  {"structure": "Glossopharyngeal nerve", "where": "Between ICA and ECA near the stylopharyngeus", "protect": "Stay on the tract near its upper end", "injury": "Dysphagia, posterior tongue sensory loss"},
  {"structure": "SLN and RLN", "where": "Near third/fourth pouch tracts at the thyrohyoid membrane and tracheoesophageal groove", "protect": "Endoscopic cannulation of the tract, limited dissection", "injury": "Aspiration or vocal fold paralysis"},
  {"structure": "Marginal mandibular and spinal accessory nerves", "where": "Below the mandible (marginal) and posterior to upper SCM (XI)", "protect": "Subplatysmal plane, identify when dissection is high or posterior", "injury": "Lip weakness or shoulder dysfunction"}
 ],
 "variants": [
  "First cleft: Work type I (ectodermal, duplication of membranous EAC, usually lateral to facial nerve) versus type II (ectoderm and mesoderm, at the angle of the mandible, variable relation to the nerve)",
  "Second cleft (most common, often cited around 90%): cyst, sinus or complete fistula; Bailey types I-IV by depth",
  "Third and fourth pouch sinuses: left-sided predominance, present as recurrent neck abscess or suppurative thyroiditis",
  "Bilateral anomalies or syndromic association (branchio-oto-renal syndrome)"
 ],
 "imaging_check": [
  "CT or MRI with contrast: cyst location relative to SCM, carotids and parotid; tract course",
  "Ultrasound for simple cysts in children",
  "Barium swallow, CT with oral contrast, or direct laryngoscopy for piriform sinus tract",
  "In adults, exclude cystic nodal metastasis (HPV-related oropharyngeal or thyroid carcinoma) before labeling a cyst branchial"
 ],
 "blood_nerve": [
  ["Arterial relations", "Carotid bifurcation; tract vessels from the ECA branches"],
  ["Nerve relations", "Facial (first cleft); XII and IX (second); SLN (third/fourth); RLN (fourth)"],
  ["Arch derivatives (third arch)", "Glossopharyngeal nerve, common/internal carotid artery, stylopharyngeus"],
  ["Arch derivatives (second arch)", "Facial nerve, stapedius, stylohyoid, posterior belly of digastric"]
 ],
 "pimp": [
  {"q": "What is the general rule for a branchial tract's course?", "a": "It runs deep to derivatives of its own arch and superficial to derivatives of the next arch"},
  {"q": "Describe the second branchial cleft fistula course.", "a": "From anterior SCM border, along the carotid sheath, superficial to XII and IX, between ECA and ICA, to the tonsillar fossa"},
  {"q": "Where does a third pouch sinus enter the pharynx?", "a": "Piriform sinus, through the thyrohyoid membrane above the internal SLN, after passing posterior to the ICA"},
  {"q": "How does a fourth pouch tract relate to the SLN?", "a": "It runs inferior and deep to the superior laryngeal nerve (4th arch) and superficial to the RLN (6th arch)"},
  {"q": "Distinguish Work type I and type II first-cleft anomalies.", "a": "Type I: ectoderm only, duplicate membranous EAC, usually lateral to VII. Type II: ectoderm and mesoderm, near the angle of the mandible, variable relation to VII"},
  {"q": "What syndrome combines branchial anomalies, hearing loss and renal anomalies?", "a": "Branchio-oto-renal syndrome (often EYA1)"},
  {"q": "Which side do third and fourth pouch sinuses favor?", "a": "Left"},
  {"q": "What is the nerve of the second arch?", "a": "Facial nerve (CN VII)"}
 ],
 "atlas_topics": ["Parotid / Facial Nerve Anatomy", "Vagus / Sympathetic Chain / Carotid Space", "Neck Levels / Fascial Compartments"],
 "sources": [["Cummings Otolaryngology 7e — Congenital neck masses", ""], ["Work WP. Newer concepts of first branchial cleft defects. Laryngoscope 1972", ""], ["K.J. Lee Essential Otolaryngology 12e — Embryology and branchial anomalies", ""]]
},
"esophageal-fb": {
 "title": "Esophageal Foreign-Body Endoscopy",
 "region": "General ENT / Emergencies",
 "summary": "Swallowed objects lodge at the physiologic narrowings of the esophagus, most often at the cricopharyngeus in children. Safe removal depends on entering the cricopharyngeus under vision without pushing on the posterior hypopharyngeal wall, on protecting the thin, serosa-free esophageal wall from sharp edges during withdrawal, and on knowing the airway and great vessels next to each level.",
 "layers": [
  {"step": "Positioning and oral entry", "structures": ["teeth and lips", "tongue", "oropharynx", "posterior pharyngeal wall"],
   "note": "Neck flexed and head extended; protect the maxillary teeth and advance the rigid scope along the posterior pharyngeal wall."},
  {"step": "Hypopharynx", "structures": ["epiglottis", "arytenoids", "piriform sinuses", "postcricoid region"],
   "note": "Pass behind the arytenoids; lift the larynx gently forward with the scope tip to open the postcricoid space."},
  {"step": "Cricopharyngeus", "structures": ["cricopharyngeus (horizontal sphincter)", "Killian dehiscence (posterior, just above)", "esophageal inlet"],
   "note": "The sphincter appears as a closed slit; wait for it to relax under gentle steady pressure rather than forcing. Most pediatric coins stop here or just below at the thoracic inlet."},
  {"step": "Cervical and upper thoracic esophagus", "structures": ["esophageal wall (mucosa, submucosa, muscularis, adventitia)", "trachea and membranous wall (anterior)", "aortic arch and left main bronchus impression (left/anterior)"],
   "note": "Check the second narrowing at the arch and bronchus; objects here lie close to the trachea and aorta."},
  {"step": "Object assessment and capture", "structures": ["object", "impaction site mucosa", "lumen distal to the object"],
   "note": "Assess orientation and edges; sheathe sharp points inside the scope or trail them, and use the overtube or hood for broad sharp objects."},
  {"step": "Distal esophagus and LES", "structures": ["lower esophageal sphincter", "diaphragmatic hiatus", "GEJ"],
   "note": "Survey the rest of the esophagus when safe for second objects or underlying stricture or eosinophilic esophagitis."},
  {"step": "Second look", "structures": ["impaction site", "full esophageal circumference"],
   "note": "Reinspect for laceration, perforation, bleeding or retained fragments."}
 ],
 "landmarks": [
  {"structure": "Cricopharyngeus", "how_to_find": "Closed horizontal slit behind the cricoid lamina at the lower hypopharynx; opens with gentle sustained pressure or patient relaxation", "why": "Most common lodgment site in children"},
  {"structure": "Aortic arch / left main bronchus narrowing", "how_to_find": "Pulsatile indentation on the left anterolateral wall in the upper thoracic esophagus (adults roughly 22-27 cm from incisors)", "why": "Second narrowing; objects here are near the trachea and aorta"},
  {"structure": "Lower esophageal sphincter", "how_to_find": "Narrowing at the diaphragmatic hiatus (adults roughly 38-40 cm from incisors), with the Z-line nearby", "why": "Third narrowing; food bolus impaction often reveals stricture or EoE"},
  {"structure": "Sharp point direction", "how_to_find": "Rotate the object until the point trails or sheathe it within the scope barrel before withdrawal", "why": "Avoids lacerating the wall on the way out"}
 ],
 "danger": [
  {"structure": "Posterior hypopharynx / Killian dehiscence", "where": "Posterior midline above the cricopharyngeus", "protect": "No blind force; enter under vision with the larynx lifted", "injury": "Perforation, retropharyngeal abscess, mediastinitis"},
  {"structure": "Esophageal wall at the impaction site", "where": "Thin wall without serosa, often ulcerated", "protect": "Gentle grasp, sharp edges sheathed, withdraw with scope as a unit", "injury": "Laceration, perforation"},
  {"structure": "Trachea", "where": "Anterior to the cervical and upper thoracic esophagus; soft and compressible in infants", "protect": "Secure airway (intubation); watch ventilation during manipulation", "injury": "Airway compression, dislodgement into the airway, TEF from chronic impaction"},
  {"structure": "Aorta and great vessels", "where": "Left lateral to the esophagus at the arch level", "protect": "Avoid traumatic manipulation of chronically impacted objects at this level; image first", "injury": "Aortoesophageal fistula, hemorrhage"},
  {"structure": "Recurrent laryngeal nerves", "where": "Tracheoesophageal grooves", "protect": "Recognize risk with chronic impaction and perforation", "injury": "Vocal fold paralysis"}
 ],
 "variants": [
  "Underlying esophageal stricture (prior TE fistula/atresia repair, caustic injury)",
  "Eosinophilic esophagitis causing food bolus impaction",
  "Vascular ring or aberrant subclavian causing extrinsic narrowing",
  "Multiple or stacked coins and magnets"
 ],
 "imaging_check": [
  "AP and lateral neck/chest radiographs: coin in the esophagus appears en face on AP and edge-on on lateral (trachea is the reverse)",
  "Double-ring (halo) or step-off sign suggests a button battery, which is an emergency",
  "Radiolucent objects (food, plastic, fish bone) may require CT",
  "CT for suspected perforation or long-standing impaction near the aorta"
 ],
 "blood_nerve": [
  ["Arterial", "Inferior thyroid artery (cervical), aortic esophageal and bronchial branches (thoracic), left gastric and inferior phrenic (abdominal)"],
  ["Venous", "Inferior thyroid veins, azygos/hemiazygos, left gastric vein"],
  ["Motor", "Vagus: pharyngeal plexus/RLN to striated upper esophagus and cricopharyngeus; vagal plexus to smooth muscle distally"],
  ["Wall layers", "Mucosa, submucosa, muscularis propria (inner circular, outer longitudinal), adventitia (no serosa)"]
 ],
 "pimp": [
  {"q": "Where do esophageal foreign bodies lodge most often in children?", "a": "At the cricopharyngeus / thoracic inlet"},
  {"q": "What are the three narrowings of the esophagus?", "a": "Cricopharyngeus, aortic arch/left main bronchus crossing, and lower esophageal sphincter at the hiatus"},
  {"q": "How does a coin in the esophagus look on AP film?", "a": "Round (en face), because the esophagus is wider side to side; a tracheal coin tends to appear edge-on on AP"},
  {"q": "Why does an esophageal perforation spread rapidly?", "a": "The esophagus has no serosa, so contamination tracks into the retrovisceral space and mediastinum"},
  {"q": "What is the Killian dehiscence?", "a": "Posterior weak area between the thyropharyngeus and cricopharyngeus parts of the inferior constrictor"},
  {"q": "What is the most dangerous radiopaque object that resembles a coin?", "a": "A button battery (double-ring sign on AP, step-off on lateral)"},
  {"q": "How do you remove an open safety pin pointing upward?", "a": "Sheathe the point within the scope or convert it so the point trails (e.g., push into the stomach to turn it) before withdrawal"}
 ],
 "atlas_topics": ["Pharynx / UES / Cervical Esophagus", "Mediastinal Continuity of Deep Neck Spaces"],
 "sources": [["Cummings Otolaryngology 7e — Foreign bodies of the airway and esophagus", ""], ["K.J. Lee Essential Otolaryngology 12e — Esophageal foreign bodies", ""], ["Pasha Clinical Reference Guide 6e — Foreign bodies", ""]]
},
"button-battery": {
 "title": "Esophageal Button-Battery Emergency",
 "region": "Pediatric Otolaryngology",
 "summary": "A lodged button battery generates hydroxide at its negative pole and causes liquefactive necrosis within hours, so the anatomy that matters is what lies next to the battery at its level: the trachea anteriorly and the aorta at the arch level, plus the recurrent laryngeal nerves. Remove it urgently along the esophageal axis, then grade the injury by depth and by which wall the negative pole faced, because that wall predicts delayed fistula.",
 "layers": [
  {"step": "Airway and positioning", "structures": ["trachea (anterior to the esophagus, compressible in infants)", "teeth and lips"],
   "note": "Intubate and secure the airway; the battery may compress the soft infant trachea."},
  {"step": "Hypopharynx and cricopharyngeus", "structures": ["postcricoid region", "cricopharyngeus", "esophageal inlet"],
   "note": "Most pediatric batteries lodge at or below the cricopharyngeus near the thoracic inlet; enter under vision."},
  {"step": "Battery exposure", "structures": ["battery faces (negative pole narrower)", "surrounding necrotic mucosa", "impaction wall"],
   "note": "Identify which face is the negative pole and which wall it is against; that wall has the worst injury."},
  {"step": "Removal", "structures": ["esophageal lumen axis", "cricopharyngeus"],
   "note": "Grasp the rim with forceps or a basket/magnet and withdraw along the axis without fragmenting or pushing distally."},
  {"step": "Injury survey", "structures": ["mucosa", "submucosa", "muscularis", "adjacent trachea (anterior)", "aortic arch level (left lateral/anterolateral)"],
   "note": "Re-scope and grade injury depth and circumference; note the level relative to the incisors and to the aortic arch and whether the injury faces the trachea."},
  {"step": "Second objects and airway", "structures": ["remaining esophagus", "trachea (bronchoscopy if anterior injury)"],
   "note": "Survey for additional batteries; consider bronchoscopy when the injury faces the trachea."},
  {"step": "Debridement limits", "structures": ["adherent eschar"],
   "note": "Do not aggressively debride adherent necrosis; it may unroof a contained perforation or vascular injury."}
 ],
 "landmarks": [
  {"structure": "Negative pole", "how_to_find": "On the lateral film the narrower face is the negative pole; at endoscopy it is the face without the plus marking", "why": "The tissue against it has the deepest necrosis"},
  {"structure": "Aortic arch level", "how_to_find": "Upper thoracic esophagus at the second narrowing, roughly the T3-T4 level on imaging, just above the carina; pulsatile left-sided impression", "why": "Injury here risks aortoesophageal fistula"},
  {"structure": "Trachea", "how_to_find": "Directly anterior to the cervical and upper thoracic esophagus; anterior-wall injury faces it", "why": "Risk of tracheoesophageal fistula"},
  {"structure": "Tracheoesophageal grooves", "how_to_find": "Lateral margins between the esophagus and trachea, where the RLNs ascend", "why": "Lateral injury risks vocal fold paralysis"}
 ],
 "danger": [
  {"structure": "Aorta", "where": "Left lateral/anterolateral to the esophagus at the arch level and posterior-left in the descending segment", "protect": "Avoid deep debridement; obtain vascular imaging (CTA or MRA per protocol) when injury is near the aorta; observe before feeding", "injury": "Aortoesophageal fistula with delayed massive hemorrhage, often days to weeks after removal"},
  {"structure": "Trachea / membranous wall", "where": "Directly anterior", "protect": "Grade anterior injury; bronchoscopy; delayed imaging before feeding", "injury": "Tracheoesophageal fistula"},
  {"structure": "Esophageal wall", "where": "At the impaction site", "protect": "Remove quickly along the axis; no aggressive debridement", "injury": "Perforation, mediastinitis, stricture"},
  {"structure": "Recurrent laryngeal nerves", "where": "Tracheoesophageal grooves", "protect": "Document vocal fold mobility after deep lateral injury", "injury": "Unilateral or bilateral vocal fold paralysis"},
  {"structure": "Vertebral column", "where": "Posterior to the esophagus", "protect": "Recognize deep posterior injury", "injury": "Spondylodiscitis"}
 ],
 "variants": [
  "Battery lodged at the cricopharyngeus versus mid-esophagus versus distal esophagus (level determines adjacent structure)",
  "Stacked batteries or battery with magnets",
  "Underlying esophageal narrowing (repaired atresia) causing impaction of a smaller battery",
  "Batteries of 20 mm or larger (e.g., lithium coin cells) carry the highest risk in young children"
 ],
 "imaging_check": [
  "AP and lateral radiographs: double-ring or halo sign on AP, step-off on lateral; differentiates from a coin",
  "Locate the level relative to the clavicles, carina and arch",
  "After removal with significant injury, cross-sectional vascular imaging (MRI/MRA or CTA) per institutional protocol to assess the aorta and tracheal wall",
  "Esophagram or repeat imaging before resuming feeds when injury was deep"
 ],
 "blood_nerve": [
  ["Esophageal arterial supply", "Inferior thyroid (cervical), aortic and bronchial branches (thoracic), left gastric (abdominal)"],
  ["Adjacent vessels", "Aortic arch and descending aorta; innominate and subclavian arteries near the thoracic inlet"],
  ["Nerves", "RLNs in the tracheoesophageal grooves; vagal esophageal plexus distally"],
  ["Wall", "No serosa; adventitia only"]
 ],
 "pimp": [
  {"q": "Which pole of a button battery causes the most injury?", "a": "The negative pole (narrower side), where hydroxide forms"},
  {"q": "What is the mechanism of injury?", "a": "Current through moist tissue generates hydroxide at the negative pole, causing alkaline liquefactive necrosis; pressure necrosis contributes"},
  {"q": "How do you tell a battery from a coin on AP film?", "a": "Double ring (halo) on AP and a step-off on lateral"},
  {"q": "What pre-removal measure is recommended for a child over 1 year within 12 hours of ingestion?", "a": "Honey 10 mL by mouth every 10 minutes up to 6 doses if it does not delay removal; in hospital, sucralfate (1 g/10 mL) 10 mL every 10 minutes up to 3 doses (National Capital Poison Center; also endorsed by ESPGHAN 2021)"},
  {"q": "Which delayed complication is most feared?", "a": "Aortoesophageal fistula with massive hemorrhage"},
  {"q": "What lies anterior to the cervical esophagus?", "a": "The trachea (membranous wall), with the RLNs in the grooves between them"},
  {"q": "Why avoid aggressive debridement of eschar?", "a": "It may unroof a contained perforation or vascular injury"}
 ],
 "atlas_topics": ["Pharynx / UES / Cervical Esophagus", "Thoracic Inlet / Root of Neck", "Mediastinal Continuity of Deep Neck Spaces"],
 "sources": [["National Capital Poison Center Button Battery Ingestion Triage and Treatment Guideline", ""], ["Cummings Otolaryngology 7e — Foreign bodies of the airway and esophagus", ""], ["Mubarak A et al. Diagnosis, management, and prevention of button battery ingestion in childhood: an ESPGHAN position paper. J Pediatr Gastroenterol Nutr 2021;73(1):129-136", ""]]
},
"orbital-floor": {
 "title": "Orbital Floor Repair",
 "region": "Facial Plastics / Trauma",
 "summary": "Orbital floor repair restores the floor between the orbit and maxillary sinus to free entrapped tissue and correct enophthalmos. The relationships that decide safety are the infraorbital nerve in its groove and canal on the floor, the inferior rectus and inferior oblique close above the floor, and the posterior ledge and optic canal, which set how far back the implant can go.",
 "layers": [
  {"step": "Lower eyelid approach", "structures": ["conjunctiva", "lower lid retractors (capsulopalpebral fascia)", "orbital septum", "orbicularis oculi", "lateral canthal tendon (inferior crus, if cantholysis)"],
   "note": "Transconjunctival: preseptal route between septum and orbicularis, or retroseptal route through the fornix behind the septum (orbital fat seen). Subciliary: skin-muscle flap to the septum. Add lateral canthotomy and inferior cantholysis for wide exposure."},
  {"step": "Orbital rim and periosteum", "structures": ["arcus marginalis", "periosteum of anterior maxilla", "infraorbital rim"],
   "note": "Incise periosteum a few mm below the rim on the anterior face of the maxilla, avoiding the septum attachment, and elevate over the rim."},
  {"step": "Subperiosteal floor dissection", "structures": ["periorbita", "orbital floor (maxilla, zygoma laterally, palatine posteriorly)", "infraorbital groove and canal", "inferior orbital fissure (lateral)"],
   "note": "Elevate periorbita off the floor medially and laterally around the defect; the infraorbital nerve runs anteroposteriorly in the groove/canal."},
  {"step": "Defect and herniated contents", "structures": ["herniated orbital fat", "inferior rectus and its sheath", "maxillary sinus mucosa"],
   "note": "Reduce herniated tissue hand over hand from the sinus; enlarge a trapdoor gently if needed."},
  {"step": "Posterior ledge", "structures": ["posterior intact floor", "medial floor-wall junction (inferomedial strut)", "orbital process of palatine bone"],
   "note": "Identify stable bone around the entire defect, especially the posterior ledge where the floor rises; the floor slopes upward going back and medially."},
  {"step": "Implant placement", "structures": ["implant", "posterior ledge", "medial and lateral bony margins", "inferior orbital fissure"],
   "note": "Seat the implant on stable bone with no tissue trapped beneath; keep it well anterior to the optic canal."},
  {"step": "Confirmation and closure", "structures": ["globe position", "forced duction", "periosteum", "conjunctiva/lid"],
   "note": "Repeat forced ductions; resuspend the canthus if cantholysis was done; close periosteum when feasible."}
 ],
 "landmarks": [
  {"structure": "Infraorbital nerve", "how_to_find": "Foramen on the anterior maxilla roughly 6-10 mm below the rim, near the line of the pupil; on the floor it runs in a groove that becomes a canal anteriorly", "why": "Avoid stretch and cautery; the defect usually lies medial to it"},
  {"structure": "Inferior orbital fissure", "how_to_find": "Posterolateral floor, a slit running posterolaterally between floor and lateral wall", "why": "Contents (zygomatic nerve, venous connections) can be cauterized and divided; a lateral landmark for orientation"},
  {"structure": "Posterior ledge", "how_to_find": "Follow the floor back until stable bone rises upward; behind the central and medial floor it is commonly about 25-30 mm from the rim (range up to about 37-39 mm) and much closer laterally", "why": "Implant must rest on it for support"},
  {"structure": "Inferior oblique origin", "how_to_find": "Anteromedial floor, just lateral to the lacrimal fossa, behind the rim", "why": "Avoid detaching it during medial exposure"},
  {"structure": "Forced duction", "how_to_find": "Grasp conjunctiva and inferior rectus insertion near the inferior limbus (insertion about 6.5 mm from the limbus) and rotate the globe up", "why": "Confirms release of entrapment"}
 ],
 "danger": [
  {"structure": "Optic nerve", "where": "Optic canal at the orbital apex, posterior and superomedial to the end of the floor; about 40-45 mm from the infraorbital rim (range about 37-49 mm)", "protect": "Do not dissect beyond the posterior ledge; avoid long implants pressed backward", "injury": "Blindness"},
  {"structure": "Globe", "where": "Above the dissection", "protect": "Corneal shield; malleable retractor with gentle intermittent pressure", "injury": "Corneal abrasion, globe injury"},
  {"structure": "Inferior rectus and inferior oblique", "where": "Inferior rectus lies directly above the floor; IO arises anteromedially", "protect": "Free entrapped muscle gently; avoid trapping it under the implant", "injury": "Persistent diplopia"},
  {"structure": "Infraorbital nerve", "where": "Groove and canal on the floor", "protect": "Avoid compression by implant edges and retraction", "injury": "Cheek, upper lip, lateral nose and upper teeth numbness"},
  {"structure": "Retrobulbar space", "where": "Behind the globe", "protect": "Hemostasis; check vision and pupils immediately after", "injury": "Retrobulbar hematoma with vision loss; treat with lateral canthotomy and cantholysis"},
  {"structure": "Lower lid structures", "where": "Approach layers", "protect": "Choose plane carefully; canthal resuspension", "injury": "Ectropion (subciliary) or entropion and lid malposition"}
 ],
 "variants": [
  "Pediatric trapdoor fracture with muscle entrapment and a white eye (minimal external signs); oculocardiac reflex with bradycardia",
  "Combined medial wall fracture with loss of the inferomedial strut",
  "Infraorbital nerve dehiscent in the floor or running in an open groove",
  "Enlarged maxillary sinus or low orbital floor variations"
 ],
 "imaging_check": [
  "Fine-cut CT orbits with coronal and sagittal reformats: defect size and location, inferior rectus position and shape, posterior ledge integrity",
  "Assess the inferomedial strut and medial wall involvement",
  "Look for retrobulbar hematoma, optic canal fracture or globe injury",
  "Clinical: acuity, pupils (RAPD), color vision, EOM, Hertel exophthalmometry"
 ],
 "blood_nerve": [
  ["Arterial", "Infraorbital artery (branch of the third part of the maxillary artery) with the nerve; ophthalmic artery branches in the orbit"],
  ["Venous", "Inferior ophthalmic vein connecting to the pterygoid plexus through the inferior orbital fissure"],
  ["Sensory", "Infraorbital nerve (V2): lower lid, cheek, lateral nose, upper lip, and anterior/middle superior alveolar branches to upper teeth"],
  ["Motor", "Oculomotor (inferior division) to inferior rectus and inferior oblique"]
 ],
 "pimp": [
  {"q": "Which bones form the orbital floor?", "a": "Maxilla (most), zygoma (lateral) and the orbital process of the palatine (posterior)"},
  {"q": "Where is the orbital floor thinnest?", "a": "Medial to the infraorbital groove"},
  {"q": "What is the oculocardiac reflex?", "a": "Bradycardia, nausea or syncope from traction on extraocular muscles; afferent V1 (trigeminal), efferent vagus"},
  {"q": "What is the spiral of Tillaux?", "a": "Rectus insertions from the limbus: medial about 5.5 mm, inferior 6.5, lateral 6.9, superior 7.7"},
  {"q": "What is the 24-12-6 rule?", "a": "From the anterior lacrimal crest along the medial wall: about 24 mm to the anterior ethmoidal foramen, 12 mm more to the posterior ethmoidal foramen, 6 mm more to the optic canal"},
  {"q": "What nerve innervates the inferior oblique?", "a": "Inferior division of the oculomotor nerve"},
  {"q": "What is the emergency treatment for retrobulbar hematoma?", "a": "Lateral canthotomy with inferior cantholysis"},
  {"q": "What passes through the inferior orbital fissure?", "a": "Infraorbital and zygomatic nerves (V2), infraorbital artery, branches of the inferior ophthalmic vein to the pterygoid plexus"}
 ],
 "atlas_topics": ["Orbit — Compartments / Canthi / Lacrimal System", "Facial Buttresses / Midface Trauma"],
 "sources": [["Cummings Otolaryngology 7e — Orbital fractures", ""], ["AO Surgery Reference — Orbital floor fractures", "https://surgeryreference.aofoundation.org"], ["Bailey's Head and Neck Surgery — Otolaryngology, orbital trauma chapter", ""]]
},
"mandible-orif": {
 "title": "Mandible ORIF",
 "region": "Facial Plastics / Trauma",
 "summary": "Mandible ORIF restores occlusion first and then fixes the fracture along lines of tension so muscle pull cannot distract it. Safety depends on the inferior alveolar canal and tooth roots inside the bone, the mental nerve exiting below the premolars for intraoral approaches, and the marginal mandibular and other facial nerve branches for external approaches.",
 "layers": [
  {"step": "Occlusion and MMF", "structures": ["dentition", "maxillary and mandibular arches", "first molars (Angle relationship)", "wear facets"],
   "note": "Set preinjury occlusion with arch bars or MMF screws placed in interradicular bone near the mucogingival junction, clear of root apices."},
  {"step": "Intraoral vestibular approach (symphysis, body, angle)", "structures": ["gingivobuccal mucosa (leave a cuff for closure)", "mentalis muscle (anterior)", "mental nerve branches (premolar region)", "buccinator and masseter (posterior)", "periosteum"],
   "note": "Incise in the vestibule leaving cuff on the gingival side; reapproximate mentalis anteriorly to prevent chin ptosis; identify the mental nerve before extending past the canine."},
  {"step": "External submandibular approach (angle, ramus, body)", "structures": ["skin about 2 cm below the mandible", "platysma", "superficial layer of deep cervical fascia", "facial vein and artery", "marginal mandibular nerve", "pterygomasseteric sling", "periosteum"],
   "note": "Incise the fascia low and lift it with the facial vein (Hayes Martin maneuver) to protect the marginal nerve; divide the sling at the inferior border to reach bone."},
  {"step": "Retromandibular / preauricular approach (condyle, subcondyle)", "structures": ["parotid gland", "facial nerve branches (cervicofacial division)", "retromandibular vein", "superficial temporal vessels and auriculotemporal nerve (preauricular)", "frontal branch (preauricular)", "TMJ capsule"],
   "note": "Dissect through or around the parotid bluntly in line with nerve branches; nerve monitoring helps."},
  {"step": "Reduction", "structures": ["fracture segments", "condyles in the glenoid fossae", "lingual cortex"],
   "note": "Reduce with condyles seated and occlusion held; check the lingual cortex for splay at symphysis fractures."},
  {"step": "Fixation", "structures": ["tension band (superior/alveolar border)", "compression zone (inferior border)", "tooth roots", "inferior alveolar canal", "mental foramen"],
   "note": "Miniplates follow Champy lines: below root apices and above the canal in the body, along the external oblique ridge at the angle, two plates at the symphysis/parasymphysis. Load-bearing reconstruction plates at the inferior border for comminution or atrophy."},
  {"step": "Check and closure", "structures": ["occlusion", "hardware", "mucosa and mentalis", "external layers"],
   "note": "Release MMF and confirm reproducible occlusion; close mentalis and mucosa in layers."}
 ],
 "landmarks": [
  {"structure": "Mental foramen", "how_to_find": "Below the second premolar or between the premolars, roughly midway between alveolar crest and inferior border in dentate adults", "why": "Mental nerve exits here; screws and incisions must avoid it"},
  {"structure": "Inferior alveolar canal", "how_to_find": "Runs from the mandibular foramen (behind the lingula on the medial ramus) forward below the molar roots to the mental foramen; on CT/panorex it is the radiolucent line with cortical borders; may loop anteriorly before exiting", "why": "Body miniplates sit in the zone between root apices and the canal; bicortical screws belong at the inferior border below the canal"},
  {"structure": "Marginal mandibular nerve", "how_to_find": "Deep to platysma and within/under the superficial layer of deep cervical fascia, crossing superficial to the facial artery and vein near the antegonial notch; may dip up to about 1-2 cm below the inferior border posterior to the facial artery", "why": "Protect during submandibular and retromandibular approaches"},
  {"structure": "External oblique ridge", "how_to_find": "Palpable bony ridge on the lateral mandible running up from the molar region to the anterior ramus", "why": "Site for the angle tension-band plate"},
  {"structure": "Tooth root apices", "how_to_find": "Estimate root length from CT/panorex; canine roots are longest; place subapical plates below them", "why": "Avoid screw injury to roots"}
 ],
 "danger": [
  {"structure": "Inferior alveolar nerve", "where": "Within the mandibular canal from the ramus to the mental foramen", "protect": "Monocortical screws between apices and canal, bicortical only at the inferior border; drill guides and length checks", "injury": "Lower lip and chin numbness"},
  {"structure": "Mental nerve", "where": "Exits the mental foramen below the premolars; branches fan into the lower lip just under the mucosa", "protect": "Identify before extending the incision; avoid stretching with retractors", "injury": "Lower lip and chin numbness"},
  {"structure": "Tooth roots", "where": "Alveolar bone above the canal", "protect": "Monocortical screws below apices; MMF screws between roots", "injury": "Devitalized teeth, root fracture"},
  {"structure": "Marginal mandibular nerve", "where": "Below and along the inferior border, superficial to the facial vessels", "protect": "Incise 2 cm below the mandible, subfascial plane, Hayes Martin maneuver", "injury": "Lower lip depressor weakness"},
  {"structure": "Facial nerve trunk and branches", "where": "Within the parotid during retromandibular and preauricular approaches", "protect": "Blunt dissection parallel to branches; nerve monitor", "injury": "Facial weakness"},
  {"structure": "Facial artery and retromandibular vein", "where": "Antegonial notch and behind the ramus", "protect": "Identify and ligate as needed", "injury": "Hemorrhage"}
 ],
 "variants": [
  "Anterior loop of the inferior alveolar nerve before the mental foramen",
  "Accessory mental foramina",
  "Bifid mandibular canal",
  "Edentulous atrophic mandible with the canal and mental foramen near the alveolar crest"
 ],
 "imaging_check": [
  "CT face (or panorex plus additional views): all fracture sites, as mandible fractures are frequently multiple",
  "Teeth in the line of fracture, root fractures, impacted third molars",
  "Condylar position and displacement",
  "Relation of the fracture to the inferior alveolar canal and mental foramen"
 ],
 "blood_nerve": [
  ["Arterial", "Inferior alveolar artery (maxillary artery) within the canal plus periosteal supply from muscle attachments"],
  ["Sensory", "Inferior alveolar nerve (V3) to lower teeth; mental nerve to lower lip and chin; lingual nerve medial to the third molar"],
  ["Motor to elevators", "V3: masseter, temporalis, medial pterygoid; lateral pterygoid protrudes and pulls the condyle anteromedially"],
  ["Facial nerve branches", "Marginal mandibular and cervical branches near the inferior border; cervicofacial division in the parotid"]
 ],
 "pimp": [
  {"q": "What are Champy lines?", "a": "Ideal lines for monocortical miniplates along the tension zone: subapical in the body, along the external oblique ridge at the angle, two plates in the symphysis"},
  {"q": "Which mandibular border is in tension and which in compression?", "a": "Superior (alveolar) border tension, inferior border compression"},
  {"q": "Which muscle displaces a condylar fracture anteromedially?", "a": "Lateral pterygoid"},
  {"q": "What is Angle class I occlusion?", "a": "Mesiobuccal cusp of the maxillary first molar sits in the buccal groove of the mandibular first molar"},
  {"q": "Where is the mental foramen?", "a": "Below the second premolar or between the premolars"},
  {"q": "What does the Hayes Martin maneuver do?", "a": "Ligates and elevates the facial vein with the overlying fascia to protect the marginal mandibular nerve"},
  {"q": "What is a favorable fracture?", "a": "One whose orientation resists displacement by the masseter, temporalis and medial pterygoid pull"},
  {"q": "What nerve runs medial to the third molar?", "a": "Lingual nerve"}
 ],
 "atlas_topics": ["Mandible / TMJ / Masticator Space", "TMJ / Occlusion / Infratemporal Functional Anatomy", "Superficial Face — Vessels / Facial Nerve / SMAS"],
 "sources": [["Cummings Otolaryngology 7e — Mandibular fractures", ""], ["AO Surgery Reference — Mandible", "https://surgeryreference.aofoundation.org"], ["Champy M et al. Mandibular osteosynthesis by miniature screwed plates via a buccal approach. J Maxillofac Surg 1978", ""]]
},
}
