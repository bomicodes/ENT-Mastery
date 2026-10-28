"""Laryngology / Voice / Swallowing (part B): mechanism-level teaching content."""

CONTENT = {
"Modified Barium Swallow": dict(
overview=(
"The modified barium swallow (videofluoroscopic swallow study) shows all phases of swallowing in real time with barium of different consistencies. "
"It is the reference test for aspiration during the swallow and for testing compensatory strategies."),
physiology=(
"**Fluoroscopic view**: lateral and AP views show bolus flow, hyolaryngeal elevation, epiglottic inversion, pharyngeal contraction, and UES opening. "
"**Timing**: the swallow reflex normally triggers as the bolus head reaches the ramus of the mandible or valleculae. "
"**Consistencies**: thin liquids move fastest and are most likely aspirated; thicker consistencies slow flow (IDDSI framework). "
"**Biomechanics**: anterior-superior hyoid movement and laryngeal elevation pull open the UES."),
pathophysiology=(
"**Aspiration timing**: before (delayed trigger), during (poor laryngeal closure), or after (residue spillage) the swallow, which guides treatment. "
"**Residue patterns**: vallecular residue implies reduced tongue base retraction; pyriform residue implies pharyngeal weakness or UES dysfunction. "
"**Cricopharyngeal bar**: a posterior indentation reflecting a noncompliant UES. "
"**Penetration-Aspiration Scale**: grades severity. "
"**Strategy testing**: chin tuck, head turn, and effortful swallow are tested for effectiveness. "
"**Advantage over FEES**: sees aspiration during the swallow and the oral and esophageal phases."),
),

"Medialization Thyroplasty": dict(
overview=(
"Medialization (type I) thyroplasty places an implant through a window in the thyroid cartilage to push a paralyzed or atrophic vocal fold toward midline. "
"It is a permanent, reversible, awake procedure that allows voice tuning during surgery."),
physiology=(
"**Paraglottic space**: lies between the thyroid cartilage and the thyroarytenoid muscle, allowing an implant to medialize the fold without touching the vibrating cover. "
"**Window position**: placed at the level of the vocal fold, roughly at the midpoint of the thyroid cartilage height, a few millimeters from the anterior midline. "
"**Glottic closure**: complete closure improves voice, cough, and swallow. "
"**Vibratory cover preservation**: the superficial lamina propria stays untouched."),
pathophysiology=(
"**Closing the gap**: medializing the membranous fold reduces air escape. "
"**Posterior gap limit**: thyroplasty does not rotate the arytenoid, so large posterior gaps or level mismatch need arytenoid adduction. "
"**Awake tuning**: patients phonate during surgery so implant size and position optimize voice. "
"**Implant materials**: silastic, Gore-Tex, or hydroxyapatite. "
"**Complications**: airway edema, hematoma, implant extrusion, and overmedialization."),
),

"Microlaryngoscopy": dict(
overview=(
"Microlaryngoscopy is suspension laryngoscopy with an operating microscope for diagnosis and precise phonosurgery. "
"Its core principle is preserving the superficial lamina propria to protect the mucosal wave."),
physiology=(
"**Suspension laryngoscopy**: a laryngoscope suspended from a chest support exposes the larynx for two-handed microsurgery. "
"**Superficial lamina propria**: the gel-like layer that allows the cover to vibrate. "
"**Vocal ligament**: deeper layers that should not be violated in benign surgery."),
pathophysiology=(
"**Microflap technique**: an incision lateral to the lesion allows elevation and removal while preserving overlying epithelium and lamina propria. "
"**Scar**: injury to the superficial lamina propria replaces pliable tissue with collagen, stiffening the cover permanently. "
"**Exposure difficulty**: retrognathia, limited neck extension, and large teeth. "
"**Complications**: dental injury, tongue numbness, and taste change from pressure."),
),

"Reinke Edema": dict(
overview=(
"Reinke edema is diffuse, polypoid swelling of the superficial lamina propria, almost always in smokers, producing a low-pitched voice. "
"Smoking cessation is essential, and microflap reduction treats symptomatic disease."),
physiology=(
"**Reinke space**: the superficial lamina propria, a loose, gel-like layer bounded by the vocal ligament and epithelium. "
"**Fold mass and pitch**: increased fold mass lowers fundamental frequency. "
"**Lymphatic drainage**: limited in the superficial lamina propria."),
pathophysiology=(
"**Smoking injury**: chronic irritation increases vascular permeability and fluid accumulation in Reinke space. "
"**Voice change**: added mass lowers pitch, often making women's voices sound masculine. "
"**Airway**: severe edema can obstruct the airway. "
"**Surgery**: microflap suctioning of gelatinous material preserves the epithelium. "
"**Recurrence**: with continued smoking."),
),

"Presbyphonia": dict(
overview=(
"Presbyphonia is voice change from aging of the larynx: vocal fold atrophy and bowing cause weak, breathy, effortful voice. "
"Voice therapy, injection, or thyroplasty improve closure."),
physiology=(
"**Lamina propria aging**: with age, the superficial lamina propria loses elastin and hyaluronic acid while collagen becomes disorganized and denser, reducing pliability. "
"**Thyroarytenoid muscle aging**: fiber loss, reduced motor units, and slower contraction thin the vocal fold body. "
"**Respiratory driving pressure**: reduced lung elastic recoil and chest wall compliance lower subglottic pressure available for voice. "
"**Hormonal effects**: menopause thickens and lowers women's voices, while declining androgens can thin men's folds. "
"**Cartilage ossification**: laryngeal cartilages progressively ossify, stiffening the framework."),
pathophysiology=(
"**Vocal fold bowing**: muscle atrophy and lamina propria thinning leave a concave fold edge and a spindle-shaped glottic gap. "
"**Air escape**: incomplete closure produces a weak, breathy voice that fatigues by the end of the day. "
"**Pitch shift**: women's pitch usually falls (especially after menopause), while men's pitch may rise as fold mass decreases. "
"**Reduced endurance and projection**: patients struggle to be heard in noise, with social withdrawal. "
"**Diagnosis of exclusion**: paralysis, paresis, Parkinson disease, and lesions must be excluded. "
"**Treatment logic**: strengthening therapy (Phonation Resistance Training Exercise) builds muscle bulk and closure; injection or bilateral thyroplasty adds bulk when therapy is insufficient."),
),

"Muscle Tension Dysphonia": dict(
overview=(
"Muscle tension dysphonia is voice disorder from excessive or poorly regulated laryngeal and paralaryngeal muscle tension without structural pathology, or compensating for one. "
"Voice therapy with circumlaryngeal massage is the main treatment."),
physiology=(
"**Laryngeal posture**: suspended by extrinsic muscles that position the larynx. "
"**Efficient phonation**: balanced airflow and glottic adduction. "
"**Supraglottic structures**: false folds do not normally participate in phonation."),
pathophysiology=(
"**Excess tension**: extrinsic and intrinsic muscle hyperfunction elevates the larynx and squeezes supraglottic structures. "
"**Primary vs secondary**: primary without lesion; secondary compensating for paresis, lesion, or reflux. "
"**Symptoms**: strained voice, neck pain, and fatigue. "
"**Laryngoscopy**: supraglottic compression and posterior gap. "
"**Therapy**: rebalances muscle use."),
),

"Vocal Tremor": dict(
overview=(
"Vocal tremor is rhythmic oscillation of pitch and loudness from involuntary laryngeal and pharyngeal movements, often part of essential tremor. "
"Botulinum toxin and medications reduce symptoms."),
physiology=(
"**Motor control loops**: smooth voluntary movement depends on cerebellar-thalamocortical and basal ganglia loops that dampen oscillation. "
"**Physiologic tremor**: everyone has a small, high-frequency tremor that is normally inaudible. "
"**Voice production structures**: the larynx, pharynx, palate, tongue, and respiratory muscles all contribute to sustained phonation. "
"**Pitch and loudness control**: cricothyroid and thyroarytenoid activity set pitch; subglottic pressure sets loudness."),
pathophysiology=(
"**Essential tremor**: abnormal rhythmic oscillation in cerebellar-thalamocortical circuits produces 4-8 Hz tremor in the hands, head, and voice. "
"**Laryngeal involvement**: rhythmic adduction-abduction or vertical laryngeal movement modulates pitch and loudness, most audible on sustained vowels. "
"**Multisite tremor**: palate, pharynx, and tongue tremor contribute, limiting botulinum toxin to the folds alone. "
"**Overlap with spasmodic dysphonia**: dystonic tremor and SD coexist, complicating diagnosis. "
"**Treatment logic**: botulinum toxin weakens tremulous muscles; propranolol and primidone reduce central oscillation; deep brain stimulation helps some patients."),
),

"Leukoplakia / Laryngeal Dysplasia": dict(
overview=(
"Laryngeal leukoplakia is a clinical white patch that may represent hyperkeratosis, dysplasia, or carcinoma. "
"Biopsy grades dysplasia, which predicts malignant transformation."),
physiology=(
"**Vocal fold epithelium**: stratified nonkeratinizing squamous epithelium over the true folds, renewing from basal cells. "
"**Maturation sequence**: basal cells divide and differentiate as they rise, flattening at the surface without keratin. "
"**Mucosal pliability**: the epithelium and superficial lamina propria must remain pliable for the mucosal wave. "
"**Field exposure**: inhaled carcinogens and refluxate bathe the entire laryngeal mucosa."),
pathophysiology=(
"**Keratinization**: chronic irritation (smoking, reflux) causes keratin production, producing the white appearance. "
"**Dysplasia**: disordered maturation and cellular atypia graded mild, moderate, severe; severe dysplasia has substantial transformation risk. "
"**Stroboscopic clue**: preserved mucosal wave suggests superficial disease. "
"**Treatment**: excisional biopsy, laser, and surveillance with smoking cessation."),
),

"Posterior Glottic Stenosis / Arytenoid Fixation": dict(
overview=(
"Posterior glottic stenosis is scar in the interarytenoid region or cricoarytenoid joints after prolonged intubation, limiting abduction. "
"It mimics bilateral vocal fold paralysis and is classified by Bogdasarian."),
physiology=(
"**Posterior glottis**: the cartilaginous glottis between the arytenoids forms most of the respiratory airway area. "
"**Cricoarytenoid joint**: a synovial joint that lets the arytenoid rock and glide to abduct the vocal fold. "
"**Interarytenoid mucosa**: covers the interarytenoid muscle and lies where an endotracheal tube rests. "
"**Mucosal perfusion**: pressure from a tube exceeding capillary perfusion pressure causes ischemia."),
pathophysiology=(
"**Endotracheal tube pressure**: the tube rests in the posterior glottis, causing ulceration and scar. "
"**Bogdasarian types**: I (interarytenoid synechia), II (posterior commissure scar), III (scar with one joint fixed), IV (both joints fixed). "
"**Mechanical fixation vs paralysis**: palpation and EMG distinguish. "
"**Treatment**: scar division, posterior cricoid grafts, or cordotomy."),
),

"Injection Laryngoplasty": dict(
overview=(
"Injection laryngoplasty adds material lateral to the vocal fold to medialize it, improving closure in paralysis, paresis, atrophy, and scar. "
"It can be done in clinic or the OR, temporary or long-lasting."),
physiology=(
"**Paraglottic space**: the fat-containing space lateral to the thyroarytenoid muscle, deep to the vibrating cover, where injected material medializes the fold. "
"**Glottic closure**: complete closure is needed for efficient voice, effective cough, and airway protection. "
"**Superficial lamina propria**: must remain uninvolved so the mucosal wave is preserved. "
"**Access routes**: peroral, transthyrohyoid, transcricothyroid, and transthyroid cartilage approaches reach the same plane."),
pathophysiology=(
"**Closing a glottic gap**: added volume pushes the paralyzed or atrophic fold toward midline, reducing air escape and aspiration. "
"**Material choice by duration**: hyaluronic acid and carboxymethylcellulose last weeks to months (bridging recovery); calcium hydroxylapatite and fat last longer. "
"**Early injection**: in acute paralysis, early medialization improves voice and swallowing and may reduce the later need for permanent surgery by positioning the fold favorably during reinnervation. "
"**Overinjection and superficial injection**: overinjection causes strained voice or airway compromise; superficial injection stiffens the cover. "
"**Limitations**: injection does not correct large posterior gaps or level mismatch."),
),

"Arytenoid Adduction / Reinnervation": dict(
overview=(
"Arytenoid adduction rotates the arytenoid medially to close a posterior glottic gap and correct level mismatch; reinnervation (ansa cervicalis to RLN) restores tone and bulk. "
"Both complement medialization thyroplasty."),
physiology=(
"**Arytenoid mechanics**: the lateral cricoarytenoid pulls the muscular process anteriorly, rotating the vocal process medially and downward to close the posterior glottis. "
"**Vertical level**: the arytenoid position sets the height of the vocal fold. "
"**Ansa cervicalis**: a motor nerve loop from C1-C3 supplying the strap muscles, which can be sacrificed to donate axons. "
"**Muscle bulk and tone**: depend on continued innervation; denervated muscle atrophies over months."),
pathophysiology=(
"**Posterior gap**: thyroplasty alone medializes the membranous fold but not the arytenoid. "
"**Arytenoid adduction**: a suture mimics the lateral cricoarytenoid pull. "
"**Reinnervation**: restores thyroarytenoid bulk and tone over months but not purposeful motion. "
"**Candidates**: younger patients with long-term paralysis benefit from reinnervation."),
),
}
