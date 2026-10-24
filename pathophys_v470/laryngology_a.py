"""Laryngology / Voice / Swallowing (part A): mechanism-level teaching content."""


CONTENT = {
"Unilateral Vocal Fold Paralysis": dict(
overview=(
"Unilateral vocal fold paralysis causes a breathy, weak voice, vocal fatigue, and aspiration from incomplete glottic closure. "
"It is iatrogenic (thyroid, cardiothoracic, cervical spine surgery), neoplastic, or idiopathic, and is treated with injection, medialization thyroplasty, arytenoid adduction, or reinnervation."),
physiology=(
"**Recurrent laryngeal nerve**: supplies all intrinsic laryngeal muscles except the cricothyroid; the left RLN loops under the aortic arch, the right under the subclavian, which is why the left is injured more often (longer intrathoracic course). "
"**Adduction and abduction**: the lateral cricoarytenoid, interarytenoid, and thyroarytenoid adduct; the posterior cricoarytenoid alone abducts. "
"**Glottic closure for voice**: the folds must meet in the midline to set up vibration; for cough and swallow, firm closure builds subglottic pressure and protects the airway. "
"**Superior laryngeal nerve**: provides supraglottic sensation (internal branch) and cricothyroid motor (external branch, pitch). "
"**Synkinetic reinnervation**: after injury, regrowing axons often reinnervate both adductors and abductors, producing a fold with tone but no purposeful motion."),
pathophysiology=(
"**Glottic gap**: a paralyzed fold sits in a paramedian or lateral position, so air escapes during phonation (breathy voice, short phonation time). "
"**Muscle atrophy**: denervated thyroarytenoid muscle thins, bowing the fold and widening the gap over months; synkinetic reinnervation can preserve bulk and position. "
"**Vertical level mismatch**: the paralyzed fold may sit higher or lower, further impairing closure. "
"**Aspiration**: glottic incompetence plus reduced supraglottic sensation (if the vagus is injured high) cause aspiration of thin liquids. "
"**Lesion level matters**: high vagal lesions (skull base) also paralyze the pharynx and reduce sensation, causing worse dysphagia than isolated RLN injury. "
"**Treatment logic**: injection or thyroplasty medializes the fold to close the gap; arytenoid adduction corrects a large posterior gap and level mismatch; reinnervation restores tone and bulk. "
"**Workup**: imaging from skull base to aortic arch when no iatrogenic cause, to exclude tumor along the nerve course."),
),

"Benign Vocal Fold Lesions": dict(
overview=(
"Benign vocal fold lesions (nodules, polyps, cysts, Reinke edema, pseudocysts, granulomas) are the most common causes of dysphonia in voice users. "
"Most arise in the superficial lamina propria from phonotrauma, and therapy precedes microsurgery for most."),
physiology=(
"**Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. "
"**Mucosal wave**: the cover ripples over the body from inferior to superior during each vibratory cycle, producing a periodic sound source. "
"**Vibratory midpoint**: maximal collision forces occur at the junction of the anterior and middle thirds of the membranous fold. "
"**Basement membrane zone**: anchors epithelium to the lamina propria and absorbs shear forces. "
"**Hydration**: adequate surface and tissue hydration reduce phonation threshold pressure and collision injury."),
pathophysiology=(
"**Phonotrauma**: repetitive collision and shear forces injure the basement membrane zone and superficial lamina propria. "
"**Nodules**: bilateral, symmetric thickening at the midpoint from chronic overuse, mainly epithelial and basement membrane changes. "
"**Polyps**: usually unilateral, often after acute hemorrhage or a single phonotraumatic event, gelatinous or hemorrhagic. "
"**Cysts**: mucus retention (gland obstruction) or epidermoid (trapped epithelium), deep in the lamina propria and less responsive to therapy. "
"**Effect on voice**: added mass and stiffness disrupt the mucosal wave and prevent complete closure (hourglass gap with nodules). "
"**Microflap principle**: preserve the superficial lamina propria and epithelium to avoid scar, which permanently stiffens the cover."),
),

"Dysphagia / Aspiration": dict(
overview=(
"Dysphagia is difficulty moving a bolus from mouth to stomach; aspiration is entry of material below the vocal folds. "
"Localizing the phase (oral, pharyngeal, esophageal) and mechanism directs instrumental testing and treatment."),
physiology=(
"**Oral phase (voluntary)**: lips seal, the tongue forms and propels the bolus posteriorly. "
"**Pharyngeal phase (reflexive)**: triggered as the bolus passes the faucial pillars; the velum closes the nasopharynx, the hyoid and larynx elevate and move anteriorly, the epiglottis inverts, the vocal folds close, the pharyngeal constrictors squeeze, and the upper esophageal sphincter (cricopharyngeus) relaxes and opens. "
"**UES opening**: requires cricopharyngeal relaxation plus anterior traction from suprahyoid muscles and bolus pressure. "
"**Esophageal phase**: peristalsis moves the bolus to the stomach through a relaxing lower esophageal sphincter. "
"**Central control**: brainstem swallowing centers (nucleus tractus solitarius, nucleus ambiguus) coordinate the sequence."),
pathophysiology=(
"**Delayed swallow trigger**: bolus enters the pharynx before airway closure, causing aspiration before the swallow (common after stroke). "
"**Reduced laryngeal elevation and closure**: aspiration during the swallow. "
"**Pharyngeal weakness**: residue in the valleculae and pyriform sinuses spills into the airway after the swallow. "
"**UES dysfunction**: cricopharyngeal hypertonicity or fibrosis causes residue and Zenker diverticulum. "
"**Silent aspiration**: absent cough from reduced laryngeal sensation, which is why bedside screening misses aspiration. "
"**Penetration-Aspiration Scale**: grades depth of airway entry and whether it is cleared. "
"**Consequences**: aspiration pneumonia, malnutrition, dehydration, and reduced quality of life."),
),

"Subglottic / Tracheal Stenosis": dict(
overview=(
"Adult subglottic and tracheal stenosis is narrowing from intubation injury, idiopathic subglottic stenosis, granulomatosis with polyangiitis, or trauma. "
"Treatment ranges from endoscopic dilation and steroid injection to cricotracheal or tracheal resection."),
physiology=(
"**Cricoid ring**: complete and nonexpansile, so mucosal swelling or scar directly narrows the lumen. "
"**Mucosal perfusion pressure**: about 25-35 mm Hg; cuff pressures above this cause ischemia. "
"**Airflow physics**: resistance rises steeply as the radius falls, so symptoms appear late, then progress quickly. "
"**Normal healing**: respiratory mucosa regenerates over denuded areas if the underlying perichondrium is preserved."),
pathophysiology=(
"**Intubation injury**: tube or cuff pressure causes ischemia, ulceration, perichondritis, granulation, and contracting scar. "
"**Tracheostomy-related**: stoma site granulation, A-frame deformity, and cuff injury. "
"**Idiopathic subglottic stenosis**: occurs almost exclusively in women, with estrogen-related fibroinflammatory scar of the subglottis and upper trachea. "
"**GPA**: necrotizing granulomatous inflammation causes subglottic stenosis, often the presenting site. "
"**Symptoms**: exertional dyspnea and stridor, often misdiagnosed as asthma. "
"**Classification**: Myer-Cotton (percent obstruction) and McCaffrey (location and length) guide treatment. "
"**Recurrence**: dilation often needs repeating; resection with anastomosis offers durable results for appropriate lesions."),
),

"Laryngeal Anatomy": dict(
overview=(
"Laryngeal anatomy (cartilage framework, joints, muscles, nerves, and layered vocal folds) explains every voice, airway, and swallowing problem. "
"It underlies stroboscopy, laryngeal EMG, phonosurgery, and airway surgery."),
physiology=(
"**Cartilage framework**: thyroid (shield), cricoid (complete ring), paired arytenoids (vocal process and muscular process), epiglottis, and smaller corniculate and cuneiform cartilages. "
"**Joints**: the cricoarytenoid joint allows rocking and gliding of the arytenoids to open and close the glottis; the cricothyroid joint allows tilting that lengthens the folds. "
"**Intrinsic muscles**: posterior cricoarytenoid (only abductor), lateral cricoarytenoid and interarytenoid (adductors), thyroarytenoid (shortens, adducts, adjusts body stiffness), and cricothyroid (lengthens and tenses). "
"**Innervation**: RLN to all intrinsic muscles except the cricothyroid; external branch of the SLN to the cricothyroid; internal branch of the SLN for supraglottic sensation. "
"**Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. "
"**Spaces**: the pre-epiglottic and paraglottic spaces are fat-filled compartments that guide tumor spread."),
pathophysiology=(
"**Nerve injury patterns**: RLN injury causes immobility with breathy voice; EBSLN injury reduces pitch range and projection; SLN internal branch injury causes reduced sensation and silent aspiration. "
"**Joint fixation**: cricoarytenoid ankylosis mimics paralysis, distinguished by palpation and laryngeal EMG. "
"**Layer-specific lesions**: nodules and polyps live in the superficial lamina propria; scar and sulcus involve deeper layers; cancer invades the vocalis and paraglottic space. "
"**Presbylarynx**: thinning of the lamina propria and muscle atrophy with age cause bowing. "
"**Airway landmarks**: the cricothyroid membrane is the emergency surgical airway site."),
),

"Stroboscopy Interpretation": dict(
overview=(
"Videostroboscopy uses flashing light slightly out of phase with vocal fold vibration to create an apparent slow-motion view of the mucosal wave. "
"It is essential for diagnosing subtle lesions, scar, and paresis, and pairs with perceptual ratings (GRBAS, CAPE-V) and patient-reported VHI-10."),
physiology=(
"**Stroboscopic principle**: the eye fuses images; a light flashing at a frequency slightly different from vibration samples successive points of different cycles, creating an illusion of slow motion. "
"**Periodicity requirement**: stroboscopy needs reasonably periodic vibration; severely aperiodic voices are better assessed with high-speed imaging. "
"**Parameters**: glottic closure pattern, symmetry, periodicity, amplitude, mucosal wave, vertical level, and nonvibrating segments. "
"**Mucosal wave**: reflects the pliability of the superficial lamina propria."),
pathophysiology=(
"**Reduced or absent mucosal wave**: stiffness from scar, sulcus, or invasive cancer (adynamic segment). "
"**Asymmetry**: unilateral stiffness, mass, or paresis. "
"**Closure patterns**: hourglass (bilateral nodules), anterior gap (presbylarynx), posterior gap (normal in many women), spindle (bowing). "
"**Cyst vs nodule**: cysts dampen the wave locally and are often unilateral with a reactive contralateral lesion. "
"**Malignancy clue**: a nonvibrating segment in a leukoplakic lesion suggests invasion."),
),

"Vocal Fold Nodules": dict(
overview=(
"Vocal fold nodules are bilateral, symmetric benign thickenings at the junction of the anterior and middle thirds of the membranous folds. "
"They are caused by chronic phonotrauma, common in children, teachers, and singers, and are treated primarily with voice therapy."),
physiology=(
"**Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. "
"**Maximal collision zone**: the midpoint of the membranous fold experiences the greatest impact stress during vibration. "
"**Basement membrane zone**: type IV collagen and anchoring fibers resist shear. "
"**Vocal hygiene**: hydration and efficient phonation lower collision forces."),
pathophysiology=(
"**Repetitive impact**: chronic loud or effortful voice use repeatedly stresses the midpoint. "
"**Tissue response**: basement membrane thickening, edema, and fibronectin deposition produce symmetric bumps. "
"**Hourglass closure**: nodules prevent full closure anterior and posterior to them, causing breathiness and hoarseness. "
"**Reversibility**: early soft nodules regress with behavior change; mature fibrotic nodules may need surgery. "
"**Children**: nodules often improve at puberty."),
),

"Vocal Fold Polyp / Cyst": dict(
overview=(
"Vocal fold polyps are usually unilateral, exophytic lesions often after vocal hemorrhage; cysts are subepithelial mucus retention or epidermoid lesions. "
"Both disrupt vibration and are often treated with microsurgery after therapy."),
physiology=(
"**Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. "
"**Microvasculature**: superficial lamina propria vessels run parallel to the fold edge and are fragile. "
"**Mucous glands**: located in the ventricle and subglottis, not the free edge."),
pathophysiology=(
"**Hemorrhagic polyp**: vessel rupture during phonotrauma causes hemorrhage into Reinke space, organizing into a polyp; anticoagulants increase risk. "
"**Mucus retention cyst**: obstruction of a gland duct. "
"**Epidermoid cyst**: trapped epithelium, possibly congenital or from healing. "
"**Contact reaction**: the opposite fold develops a reactive lesion. "
"**Surgery**: microflap excision preserves the superficial lamina propria."),
),

"Bilateral Vocal Fold Immobility": dict(
overview=(
"Bilateral vocal fold immobility causes airway obstruction because both folds rest near the midline, usually with a near-normal voice. "
"Causes include bilateral RLN injury, posterior glottic stenosis, and neurologic disease, and treatment balances airway against voice and aspiration."),
physiology=(
"**Abduction**: the posterior cricoarytenoid is the only abductor; both must work for an adequate airway during exercise and sleep. "
"**Airway vs voice tradeoff**: a wider glottis improves breathing but worsens voice and aspiration. "
"**Posterior glottis**: provides most of the respiratory airway."),
pathophysiology=(
"**Bilateral RLN paralysis**: after thyroidectomy or neurologic disease, folds sit paramedian, causing stridor. "
"**Posterior glottic stenosis**: interarytenoid scar after intubation tethers the arytenoids, mimicking paralysis. "
"**Cricoarytenoid ankylosis**: rheumatoid arthritis or trauma fixes the joints. "
"**Diagnosis**: palpation and EMG distinguish neurogenic from mechanical fixation. "
"**Treatment**: tracheostomy, posterior cordotomy, arytenoidectomy, or reinnervation."),
),

"Spasmodic Dysphonia": dict(
overview=(
"Spasmodic dysphonia is a focal laryngeal dystonia causing task-specific, involuntary spasms during speech: adductor (strained, strangled breaks) or abductor (breathy breaks). "
"Botulinum toxin injection is first-line treatment."),
physiology=(
"**Basal ganglia circuits**: modulate motor control and inhibit unwanted movements. "
"**Task specificity**: laryngeal motor control differs for speech, laughing, and singing. "
"**Neuromuscular junction**: acetylcholine release triggers muscle contraction."),
pathophysiology=(
"**Dystonia**: abnormal sensorimotor integration and reduced inhibition in basal ganglia and cortex. "
"**Adductor SD**: thyroarytenoid spasms cause strained voice breaks on vowels. "
"**Abductor SD**: posterior cricoarytenoid spasms cause breathy breaks on voiceless consonants. "
"**Task specificity**: laughing and singing are often spared. "
"**Botulinum toxin**: blocks acetylcholine release, weakening the dystonic muscle temporarily."),
),

"Zenker Diverticulum": dict(
overview=(
"Zenker diverticulum is a posterior pharyngoesophageal pulsion diverticulum through Killian dehiscence above the cricopharyngeus. "
"It causes dysphagia, regurgitation of undigested food, and aspiration, and is treated with endoscopic or open cricopharyngeal myotomy."),
physiology=(
"**Killian dehiscence**: a weak area between the oblique fibers of the inferior constrictor (thyropharyngeus) and the transverse cricopharyngeus. "
"**UES opening**: requires cricopharyngeal relaxation and hyolaryngeal elevation. "
"**Pharyngeal pressure**: swallow generates high pressure above the UES."),
pathophysiology=(
"**Noncompliant UES**: fibrotic, poorly relaxing cricopharyngeus increases hypopharyngeal pressure during swallowing. "
"**Pulsion**: pressure pushes mucosa and submucosa out through Killian dehiscence. "
"**Symptoms**: dysphagia, regurgitation, halitosis, gurgling, and aspiration. "
"**Myotomy logic**: dividing the cricopharyngeus relieves outflow resistance, and the common wall division drains the pouch."),
),

"FEES": dict(
overview=(
"Fiberoptic endoscopic evaluation of swallowing (FEES) views the pharynx and larynx before and after the swallow with a transnasal scope. "
"It is portable, radiation-free, and excellent for assessing secretions, residue, and laryngeal sensation."),
physiology=(
"**Viewing window**: the scope sees pharyngeal and laryngeal anatomy before and after the swallow. "
"**White-out**: pharyngeal contraction obscures the view at the moment of swallow. "
"**Laryngeal sensation**: touch or air-pulse tests the laryngeal adductor reflex."),
pathophysiology=(
"**Residue**: pooled material in the valleculae and pyriform sinuses indicates weakness. "
"**Penetration and aspiration**: seen before and after the swallow. "
"**Secretions**: pooled secretions predict aspiration risk. "
"**Sensation**: absent cough response suggests silent aspiration. "
"**Limitation**: white-out hides aspiration during the swallow."),
),
}
