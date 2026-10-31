"""Laryngology / Voice / Swallowing (part C): mechanism-level teaching content."""

CONTENT = {
"Posterior Cordotomy / Arytenoidectomy": dict(
overview=(
"Posterior cordotomy and partial arytenoidectomy widen the posterior glottic airway for bilateral vocal fold immobility, often avoiding or allowing removal of a tracheostomy. "
"They trade some voice quality and aspiration risk for a better airway."),
physiology=(
"**Posterior glottis**: the cartilaginous glottis between the vocal processes provides most of the respiratory airway, while the membranous glottis produces most of the voice. "
"**Airway resistance**: small increases in glottic radius greatly reduce resistance. "
"**Vocal process**: the attachment of the vocal ligament to the arytenoid; dividing behind it opens the airway while sparing most of the vibrating fold. "
"**Glottic closure for swallowing**: depends on approximation of the arytenoids and folds."),
pathophysiology=(
"**Airway gain**: a laser cut just anterior to the vocal process lets the fold retract laterally, creating a posterior triangular airway. "
"**Voice tradeoff**: a wider glottis causes breathiness, minimized by limiting the anterior extent. "
"**Aspiration risk**: larger openings and arytenoid resection impair closure during swallowing. "
"**Scar contracture**: granulation and scar can narrow the airway again, sometimes requiring revision. "
"**Patient selection**: confirm no recovery is expected (adults often wait 9-12 months after nerve injury; Bluestone advises longer in children) and distinguish paralysis from fixation."),
),

"Cricopharyngeal Dysfunction": dict(
overview=(
"Cricopharyngeal dysfunction is failure of the upper esophageal sphincter to relax or open fully, causing pharyngeal dysphagia, residue, and aspiration. "
"It is diagnosed by fluoroscopy and manometry and treated with dilation, botulinum toxin, or myotomy."),
physiology=(
"**Upper esophageal sphincter**: the cricopharyngeus is tonically contracted at rest to prevent air entering the esophagus and reflux entering the pharynx. "
"**Opening mechanism**: requires neural inhibition of tone, plus anterior-superior pull by suprahyoid muscles and bolus pressure from pharyngeal contraction. "
"**Compliance**: a healthy sphincter stretches to accommodate the bolus. "
"**Innervation**: vagal motor fibers via the pharyngeal plexus."),
pathophysiology=(
"**Failure to relax**: neurologic disease (stroke, Parkinson) impairs inhibition. "
"**Reduced compliance**: fibrosis and muscle changes (aging, radiation, inflammatory myopathy) prevent opening despite relaxation. "
"**Impaired traction**: weak hyolaryngeal elevation reduces opening even with normal relaxation. "
"**Consequences**: hypopharyngeal residue, aspiration after the swallow, and Zenker diverticulum. "
"**Cricopharyngeal bar**: fluoroscopic posterior indentation. "
"**Treatment logic**: myotomy or dilation helps when the problem is the sphincter and pharyngeal propulsion is adequate; weak pharyngeal contraction predicts poor response."),
),

"Inducible Laryngeal Obstruction / PVFM": dict(
overview=(
"Inducible laryngeal obstruction (paradoxical vocal fold motion) is inappropriate glottic or supraglottic closure during inspiration, triggered by exercise, irritants, or stress. "
"It mimics asthma and is treated with laryngeal control breathing therapy."),
physiology=(
"**Normal respiratory glottic motion**: the folds abduct during inspiration and slightly adduct during expiration. "
"**Laryngeal protective reflexes**: closure protects the airway from irritants and aspiration. "
"**Sensory input**: laryngeal mucosa is richly innervated by the superior laryngeal nerve."),
pathophysiology=(
"**Hypersensitive reflex**: irritants, reflux, postnasal drip, and exercise trigger exaggerated adduction during inspiration. "
"**Exercise-induced**: high airflow and drying provoke inspiratory stridor at peak exertion, resolving quickly with rest, unlike asthma. "
"**Psychological factors**: anxiety and stress contribute. "
"**Diagnosis**: laryngoscopy during symptoms or provocation shows inspiratory adduction with a posterior chink. "
"**Treatment logic**: breathing techniques promote abduction; treat triggers."),
),

"Chronic Cough / Laryngeal Hypersensitivity": dict(
overview=(
"Chronic cough lasting over 8 weeks (the adult guideline definition; some texts use 3 months) without a cause after treatment of asthma, reflux, and upper airway cough syndrome is often a neuropathic laryngeal hypersensitivity. "
"Behavioral cough suppression therapy helps, and neuromodulators such as gabapentin may help selected patients, although K.J. Lee notes inconsistent trial evidence."),
physiology=(
"**Cough reflex**: vagal afferents in the larynx and airways transmit to the nucleus tractus solitarius, triggering a cough motor pattern. "
"**Receptors**: TRPV1, TRPA1, and P2X3 receptors respond to irritants, temperature, and ATP. "
"**Central modulation**: cortical control allows voluntary cough suppression."),
pathophysiology=(
"**Sensory neuropathy**: viral injury or inflammation lowers the threshold of laryngeal afferents, causing cough with trivial triggers (talking, temperature changes). "
"**Central sensitization**: increased brainstem gain amplifies cough responses. "
"**Laryngeal paresthesia**: tickle, globus, and throat clearing. "
"**Treatment logic**: gabapentin, pregabalin, amitriptyline, and P2X3 antagonists reduce afferent sensitivity; speech therapy teaches suppression."),
),

"Vocal Fold Sulcus / Scar": dict(
overview=(
"Vocal fold sulcus and scar are loss of the pliable superficial lamina propria, causing a stiff, adynamic cover with poor vibration. "
"They are among the hardest voice problems to treat."),
physiology=(
"**Superficial lamina propria**: loose, gel-like tissue with hyaluronic acid and sparse fibers that lets the cover move. "
"**Mucosal wave**: requires a pliable cover over a stiffer body. "
"**Glottic closure**: depends on fold contour."),
pathophysiology=(
"**Sulcus vergeture**: a groove where epithelium attaches to the vocal ligament, possibly congenital or from ruptured epidermoid cysts. "
"**Scar**: injury from surgery, phonotrauma, or radiation replaces the superficial lamina propria with dense collagen. "
"**Vibration loss**: stiff cover reduces the mucosal wave and creates a spindle gap. "
"**Treatment limits**: injections improve closure but not pliability; microflap release and grafting have variable results."),
),

"Vocal Process Granuloma": dict(
overview=(
"Vocal process granulomas are benign inflammatory masses on the posterior vocal folds from intubation, reflux, or phonotrauma (throat clearing, harsh voice). "
"Most resolve with treating causes, and recurrence after excision is common."),
physiology=(
"**Vocal process**: the arytenoid cartilage projection covered by thin mucoperichondrium. "
"**Posterior glottic contact**: the vocal processes collide during adduction. "
"**Healing**: perichondrial injury produces granulation."),
pathophysiology=(
"**Mucoperichondrial injury**: endotracheal tube pressure, forceful adduction, or throat clearing ulcerates the thin mucosa. "
"**Granulation**: chronic irritation sustains granulation tissue. "
"**Reflux role**: often treated though evidence is mixed. "
"**Treatment**: voice therapy, reflux management, botulinum toxin to reduce adduction force (Orloff & Goldman, 1999), and steroid injection; excision recurs."),
),

"Radiation-Associated Dysphagia": dict(
overview=(
"Radiation-associated dysphagia is a late effect of head and neck radiation from fibrosis, neuropathy, and muscle atrophy, sometimes years after treatment. "
"Prevention (dose-sparing, exercises) and rehabilitation are key."),
physiology=(
"**Swallowing musculature**: constrictors, tongue base, and suprahyoid muscles generate propulsion. "
"**Lower cranial nerves**: control swallowing. "
"**Radiation biology**: late effects from fibrosis and microvascular injury."),
pathophysiology=(
"**Fibrosis**: TGF-beta driven fibrosis stiffens swallowing muscles, reducing elevation and contraction. "
"**Neuropathy**: late lower cranial nerve neuropathy reduces sensation and motor function. "
"**Stricture**: UES or esophageal stricture. "
"**Disuse atrophy**: NPO status worsens function, so swallowing during treatment is encouraged. "
"**Dose dependence**: higher constrictor doses predict dysphagia."),
),

"Aspiration-Prevention Surgery": dict(
overview=(
"Aspiration-prevention surgery (laryngotracheal separation, laryngeal closure, total laryngectomy) separates the airway from the food passage in intractable aspiration. "
"It is lifesaving when recurrent pneumonia persists despite other measures."),
physiology=(
"**Shared pharynx**: the airway and digestive tract cross at the hypopharynx, so protecting the airway depends on precise laryngeal closure. "
"**Laryngeal protective mechanisms**: elevation, epiglottic inversion, glottic and supraglottic closure, sensation, and cough. "
"**Pulmonary defense**: the lungs tolerate small aspiration if cough and mucociliary clearance are intact. "
"**Secretions**: patients produce about 1-1.5 liters of saliva daily, which is aspirated even without oral intake."),
pathophysiology=(
"**Intractable aspiration**: severe neurologic disease or cancer treatment leaves no protective function. "
"**Separation logic**: diverting the trachea to a stoma removes the path for aspirated material. "
"**Voice loss**: most procedures sacrifice voice. "
"**Reversibility**: laryngotracheal separation is potentially reversible."),
),

"Professional Voice": dict(
overview=(
"Professional voice users (singers, actors, teachers) have high vocal demands and low tolerance for subtle changes. "
"Care emphasizes detailed evaluation, voice hygiene, therapy, and conservative surgery."),
physiology=(
"**Vocal demands**: professional voice users phonate for long periods at high intensities and across wide pitch ranges. "
"**Pitch control**: the cricothyroid lengthens and tenses the folds to raise pitch; the thyroarytenoid adjusts body stiffness and register. "
"**Resonance**: the vocal tract filters the glottal source; trained singers tune resonances to project. "
"**Breath support**: controlled subglottic pressure from respiratory muscles drives efficient phonation. "
"**Vocal dose**: cumulative vibration cycles and collision stress accumulate over a day."),
pathophysiology=(
"**Subtle lesions**: small changes affect upper range and endurance. "
"**Hemorrhage**: from phonotrauma, especially with anticoagulants or premenstrual vascular changes; requires voice rest. "
"**Reflux and allergies**: worsen voice. "
"**Surgical risk**: scar can end careers, so surgery is conservative."),
),

"Acute / Chronic Laryngopharyngitis": dict(
overview=(
"Laryngitis is inflammation of the larynx: acute (usually viral) or chronic (smoking, reflux, voice abuse, inhaled steroids, fungal infection). "
"Persistent hoarseness over 4 weeks warrants laryngoscopy."),
physiology=(
"**Laryngeal mucosa**: respiratory epithelium above and below the folds with squamous epithelium on the vibrating edge. "
"**Mucus layer**: a thin, well-hydrated mucus film lubricates the folds and lowers the effort of phonation. "
"**Mucociliary clearance**: moves secretions from the lower airway up to the larynx. "
"**Immune defenses**: the mucosa contains lymphoid cells that respond rapidly to viral infection."),
pathophysiology=(
"**Acute viral laryngitis**: viral infection causes edema and inflammation of the folds, increasing mass and stiffness, producing hoarseness or aphonia that resolves in 1-2 weeks. "
"**Voice use during inflammation**: raises the risk of vocal fold hemorrhage, which is why voice rest is advised. "
"**Chronic laryngitis**: persistent irritants (smoking, reflux, voice abuse, inhaled pollutants) sustain inflammation and epithelial thickening. "
"**Fungal laryngitis**: inhaled corticosteroids and immunosuppression allow Candida, producing white plaques that can mimic leukoplakia. "
"**Red flag**: hoarseness persisting beyond 4 weeks warrants laryngoscopy to exclude neoplasm."),
),

"Esophageal Disease for the Otolaryngologist": dict(
overview=(
"Esophageal diseases (GERD, EoE, achalasia, strictures, rings, webs, cancer) commonly present to otolaryngologists as dysphagia or throat symptoms. "
"Distinguishing oropharyngeal from esophageal dysphagia guides workup."),
physiology=(
"**Esophageal muscle**: the upper third is striated (vagal motor), the middle mixed, and the lower two-thirds smooth muscle controlled by the myenteric plexus. "
"**Peristalsis**: coordinated sequential contraction propels a bolus to the stomach in a few seconds (under 1 second through the striated upper third, about 3 seconds through the smooth-muscle remainder). "
"**Lower esophageal sphincter**: tonically contracted, relaxing with swallowing via inhibitory neurons (nitric oxide, VIP). "
"**Mucosal defense**: squamous epithelium with limited acid resistance, protected by clearance and salivary bicarbonate."),
pathophysiology=(
"**Achalasia**: loss of inhibitory neurons in the myenteric plexus prevents LES relaxation and peristalsis. "
"**EoE**: Th2-mediated eosinophilic inflammation causes rings, furrows, and strictures. "
"**GERD**: transient LES relaxations allow acid reflux. "
"**Esophageal cancer**: SCC (smoking, alcohol) and adenocarcinoma (Barrett). "
"**Referred dysphagia**: distal obstruction can be perceived in the neck."),
),

"Transnasal Esophagoscopy": dict(
overview=(
"Transnasal esophagoscopy is unsedated in-office esophageal examination through the nose. "
"It screens for esophagitis, Barrett esophagus, and cancer and allows biopsy."),
physiology=(
"**Nasal route**: passing an ultrathin endoscope through the nose avoids the base of tongue and the strong gag reflex. "
"**Esophageal anatomy**: the scope traverses the UES, the cervical and thoracic esophagus, and the squamocolumnar junction (Z-line). "
"**Mucosal types**: squamous esophageal mucosa normally meets columnar gastric mucosa at the gastroesophageal junction. "
"**Air insufflation**: distends the esophagus for inspection."),
pathophysiology=(
"**Unsedated advantage**: fewer complications and lower cost. "
"**Barrett esophagus**: intestinal metaplasia from chronic reflux. "
"**Second primaries**: screening in head and neck cancer patients. "
"**Limitations**: gastric examination and therapeutics are limited."),
),

"Tracheobronchial Endoscopy Principles": dict(
overview=(
"Tracheobronchial endoscopy (rigid and flexible bronchoscopy) diagnoses and treats airway lesions, stenosis, and foreign bodies. "
"Rigid bronchoscopy allows ventilation and large instruments."),
physiology=(
"**Airway tree**: the trachea divides at the carina into main bronchi, then lobar and segmental bronchi; the right main bronchus is shorter and more vertical in adults. "
"**Dynamic airway**: intrathoracic airways narrow during expiration, so malacia is assessed with spontaneous breathing. "
"**Ventilation during endoscopy**: rigid scopes allow ventilation through the scope, while flexible scopes partially obstruct the airway. "
"**Mucosal sensitivity**: the carina and trachea are highly reflexogenic."),
pathophysiology=(
"**Rigid bronchoscopy**: controlled airway, foreign body removal, and dilation. "
"**Flexible bronchoscopy**: dynamic assessment and distal access. "
"**Complications**: bleeding, perforation, and hypoxia. "
"**Dynamic collapse**: assessed with spontaneous breathing."),
),

"Laryngopharyngeal Reflux (LPR)": dict(
overview=(
"Laryngopharyngeal reflux is retrograde flow of gastric contents to the larynx and pharynx causing throat clearing, globus, hoarseness, and cough. "
"Its diagnosis is controversial, and empiric PPI response is variable."),
physiology=(
"**Antireflux barriers**: the lower esophageal sphincter, esophageal peristalsis, the upper esophageal sphincter, and salivary bicarbonate protect the pharynx and larynx. "
"**Laryngeal mucosa**: lacks the protective mechanisms of the esophagus, such as robust bicarbonate secretion and carbonic anhydrase III, so even small exposures injure it. "
"**Pepsin**: a gastric protease most active at acidic pH that can be taken up into laryngeal cells and reactivated later. "
"**Upright vs supine reflux**: LPR is often upright and daytime, unlike classic GERD."),
pathophysiology=(
"**Pepsin injury**: pepsin persists in laryngeal tissue and is reactivated by acid, causing inflammation. "
"**Non-acid reflux**: may cause symptoms despite PPI therapy. "
"**Findings**: posterior laryngeal erythema and edema, nonspecific. "
"**PPI response**: inconsistent; lifestyle changes and alginates help."),
),

"Laryngeal Electromyography (LEMG)": dict(
overview=(
"Laryngeal electromyography records electrical activity of laryngeal muscles to distinguish paralysis from fixation and predict recovery. "
"It guides timing of permanent interventions."),
physiology=(
"**Motor unit**: a motor neuron and the muscle fibers it innervates; laryngeal motor units are small for fine control. "
"**Recruitment**: as effort increases, more and larger motor units fire. "
"**Normal resting muscle**: electrically silent except for insertional activity. "
"**Target muscles**: thyroarytenoid (RLN) and cricothyroid (SLN) are sampled to localize nerve injury."),
pathophysiology=(
"**Active denervation**: fibrillation potentials and positive sharp waves appear 2-3 weeks after axonal injury. "
"**Reinnervation**: polyphasic, long-duration motor unit potentials indicate regrowing axons. "
"**Prognosis**: absent voluntary motor units with denervation potentials months after injury predict poor recovery, supporting permanent procedures; preserved recruitment predicts recovery. "
"**Synkinesis**: activity in adductors during abduction tasks indicates misdirected reinnervation. "
"**Mechanical fixation**: normal EMG with an immobile fold points to cricoarytenoid joint fixation or posterior glottic stenosis rather than paralysis. "
"**Localization**: cricothyroid involvement implicates the SLN or a high vagal lesion."),
),

"Laryngocele": dict(
overview=(
"A laryngocele is an air-filled dilation of the laryngeal saccule: internal (within the larynx), external (through the thyrohyoid membrane), or mixed. "
"It is associated with increased laryngeal pressure and must be checked for an obstructing cancer."),
physiology=(
"**Laryngeal saccule**: a blind pouch extending upward from the anterior laryngeal ventricle between the false fold and thyroid cartilage, lined by respiratory mucosa with mucous glands that lubricate the vocal folds. "
"**Ventricle**: the space between the true and false folds. "
"**Thyrohyoid membrane**: connects the hyoid and thyroid cartilage and is pierced by the internal branch of the SLN and superior laryngeal vessels. "
"**Intralaryngeal pressure**: rises during coughing, straining, and blowing against resistance."),
pathophysiology=(
"**Increased pressure**: glassblowers, wind instrument players, and coughing increase intralaryngeal pressure. "
"**Obstruction**: tumor at the saccule neck can cause laryngocele, so cancer must be excluded. "
"**Pyolaryngocele**: infection. "
"**External extension**: through the thyrohyoid membrane, presenting as a neck mass enlarging with Valsalva."),
),
}
