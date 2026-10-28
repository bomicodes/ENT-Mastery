"""Sleep Surgery: mechanism-level teaching content."""


CONTENT = {
"Adult PSG Interpretation": dict(
overview=(
"Polysomnography records sleep stages, breathing, oxygenation, heart rhythm, and limb movements overnight to diagnose OSA and other sleep disorders. "
"Reading the AHI, the oxygen nadir, positional and REM dependence, and the central vs obstructive pattern drives every sleep-surgery decision."),
physiology=(
"**Sleep staging**: EEG, EOG, and chin EMG define wake, N1, N2, N3 (slow-wave), and REM sleep; adults cycle every 90 minutes, with more N3 early and more REM late in the night. "
"**REM atonia**: skeletal muscle tone, including the upper airway dilators, is lowest in REM, so obstruction is often worst in REM. "
"**Respiratory monitoring**: oronasal thermistor (apneas), nasal pressure (hypopneas), thoracoabdominal belts (effort), and pulse oximetry. "
"**Event definitions**: apnea is a 90 percent or greater airflow drop for 10 seconds or more; hypopnea is a 30 percent drop with a 3 percent desaturation or arousal (AASM recommended rule); Medicare still requires the 4 percent desaturation rule, so the same study can give two AHIs. "
"**Effort distinguishes events**: obstructive apneas show continued effort; central apneas show absent effort."),
pathophysiology=(
"**AHI severity**: 5-15 mild, 15-30 moderate, over 30 severe in adults. "
"**Oxygen desaturation burden**: the nadir and time below 90 percent reflect hypoxic stress and cardiovascular risk better than AHI alone. "
"**Arousals**: each obstructive event ends with a cortical arousal that restores dilator tone, fragmenting sleep and causing daytime sleepiness. "
"**Positional OSA**: events concentrate supine because gravity pulls the tongue and soft palate backward. "
"**REM-related OSA**: events cluster in REM due to atonia. "
"**Central apnea index**: a high proportion of central events (above about 25 percent) changes candidacy for HNS and points to cardiac, neurologic, or opioid causes. "
"**Home sleep apnea tests**: measure breathing but not sleep, so they underestimate AHI and are less suited for complex patients."),
),

"DISE": dict(
overview=(
"Drug-induced sleep endoscopy (DISE) visualizes the upper airway under sedation that mimics sleep, identifying the levels and patterns of collapse. "
"It is required before hypoglossal nerve stimulation and guides surgical planning (VOTE classification)."),
physiology=(
"**Pharyngeal collapsibility**: the pharynx is a muscular tube without bony support from the choanae to the larynx; patency depends on the balance between collapsing forces (negative inspiratory pressure, surrounding tissue pressure) and dilating forces (genioglossus and other dilator muscles). "
"**Sedation mimicking sleep**: propofol or dexmedetomidine reduces dilator muscle tone similar to natural sleep. "
"**VOTE levels**: velum, oropharynx (tonsils and lateral walls), tongue base, and epiglottis. "
"**Collapse configurations**: anteroposterior, lateral, and concentric. "
"**Awake vs asleep airway**: awake reflexes maintain patency, so awake exams underestimate collapse."),
pathophysiology=(
"**Multilevel collapse**: most patients collapse at more than one level, so single-level surgery often fails. "
"**Complete concentric collapse at the velum**: predicts poor HNS response because stimulation of the tongue cannot pull open a circumferentially collapsing palate, so it is a contraindication. "
"**Epiglottic collapse**: trapdoor epiglottis prolapse can cause failure of CPAP and HNS. "
"**Lateral wall collapse**: often from tonsils or pharyngeal wall laxity. "
"**Sedation depth**: too deep overcalls collapse; target-controlled infusion improves reliability."),
),

"Hypoglossal Nerve Stimulation": dict(
overview=(
"Hypoglossal nerve stimulation (HNS) is an implanted system that stimulates protrusor branches of CN XII during inspiration to open the airway. "
"It treats moderate-to-severe OSA in CPAP-intolerant patients who meet BMI, AHI, central apnea, and DISE criteria."),
physiology=(
"**Genioglossus**: the main tongue protrusor and largest pharyngeal dilator; it moves the tongue base forward and stiffens the airway. "
"**Hypoglossal nerve branches**: lateral branches mainly retract (hyoglossus, styloglossus); medial branches protrude (genioglossus, geniohyoid). "
"**Respiratory timing**: dilator activity normally increases during inspiration. "
"**Palatoglossal coupling**: tongue protrusion pulls the soft palate forward through the palatoglossus, opening the retropalatal airway in many patients."),
pathophysiology=(
"**Mechanism**: synchronized stimulation of protrusor branches during inspiration reverses sleep-related loss of genioglossus tone. "
"**Candidate selection**: AHI roughly 15-100 and BMI up to about 40 under the current FDA label (the original STAR criteria in the textbooks were AHI 20-50 and BMI under 32), central and mixed apneas under 25 percent, and no complete concentric palatal collapse on DISE. "
"**STAR trial**: 12-month AHI fell from about 29 to 9, with improved sleepiness and quality of life. "
"**Failure modes**: retraction-dominant stimulation, epiglottic collapse, poor palatoglossal coupling, and weight gain. "
"**Adherence**: nightly use is typically higher than CPAP."),
),

"Pediatric PSG Interpretation": dict(
overview=(
"Pediatric polysomnography uses child-specific scoring rules and thresholds; an obstructive AHI of 1 or more is abnormal. "
"It is indicated before adenotonsillectomy in high-risk children and when history is unclear."),
physiology=(
"**Pediatric sleep architecture**: more slow-wave and REM sleep than adults. "
"**Event duration**: a pediatric apnea needs only two breaths' duration, not 10 seconds. "
"**Obstructive hypoventilation**: children often have prolonged partial obstruction with CO2 elevation rather than discrete apneas. "
"**Higher respiratory rate**: and smaller lung volumes lead to faster desaturation."),
pathophysiology=(
"**Thresholds**: obstructive AHI 1-5 mild, 5-10 moderate, over 10 severe in the common convention (some sources grade more leniently). "
"**Hypoventilation**: end-tidal CO2 above 50 mm Hg for more than about 10-25 percent of sleep time (definitions vary) indicates obstructive hypoventilation. "
"**Central apneas**: post-arousal central apneas are common and normal. "
"**High-risk groups**: obesity, Down syndrome, craniofacial anomalies, neuromuscular disease, and age under 2 warrant PSG. "
"**Severity and postoperative risk**: severe OSA predicts postoperative respiratory complications."),
),

"PAP Troubleshooting": dict(
overview=(
"Positive airway pressure is first-line OSA therapy, but adherence is limited by mask discomfort, nasal obstruction, pressure intolerance, and aerophagia. "
"Systematic troubleshooting rescues many patients before surgery."),
physiology=(
"**Pneumatic splint**: PAP raises intraluminal pressure above the critical closing pressure, holding the pharynx open. "
"**Nasal route**: air must traverse the nose; nasal resistance increases required pressure. "
"**Mouth leak**: lets pressure escape. "
"**Adherence definition**: use of 4 hours or more on 70 percent of nights."),
pathophysiology=(
"**Nasal obstruction**: forces mouth breathing, leaks, and higher pressure; treating the nose improves adherence. "
"**Mask problems**: leaks, skin irritation, and claustrophobia. "
"**Pressure intolerance**: auto-PAP, expiratory pressure relief, or bilevel help. "
"**Aerophagia**: swallowed air from high pressure. "
"**Treatment-emergent central apnea**: PAP can unmask central events. "
"**Data download**: shows residual AHI, leak, and usage. **Weight-loss pharmacotherapy**: tirzepatide is FDA-approved (2024) for moderate-to-severe OSA with obesity and lowered AHI substantially in SURMOUNT-OSA, so weight is now a treatable target alongside PAP and surgery."),
),

"Palatal Surgery": dict(
overview=(
"Palatal surgery (UPPP, expansion sphincter pharyngoplasty, lateral pharyngoplasty, and related techniques) reconstructs the retropalatal airway in OSA. "
"Outcomes depend on patient selection (Friedman staging, tonsil size, BMI)."),
physiology=(
"**Pharyngeal collapsibility**: the pharynx is a muscular tube without bony support from the choanae to the larynx; patency depends on the balance between collapsing forces (negative inspiratory pressure, surrounding tissue pressure) and dilating forces (genioglossus and other dilator muscles). "
"**Velopharynx**: the most common site of collapse in OSA. "
"**Lateral pharyngeal walls**: palatopharyngeus and tonsils influence lateral collapse. "
"**Palatal function**: separates the oral and nasal cavities during swallowing and speech."),
pathophysiology=(
"**Retropalatal narrowing**: long soft palate, large tonsils, and lateral wall laxity narrow the airway. "
"**Friedman staging**: palate position, tonsil size, and BMI predict UPPP success (stage I best). "
"**Modern techniques**: expansion sphincter pharyngoplasty repositions the palatopharyngeus to stiffen lateral walls rather than removing tissue. "
"**Complications**: velopharyngeal insufficiency, nasopharyngeal stenosis, and dysphagia from overresection. "
"**Multilevel collapse**: palatal surgery alone often fails when tongue base collapse coexists."),
),

"Tongue Base Surgery": dict(
overview=(
"Tongue base surgery (lingual tonsillectomy, tongue base reduction, genioglossus advancement, hyoid suspension) treats retrolingual obstruction in OSA. "
"Complications include bleeding, lingual nerve and hypoglossal injury, and airway edema."),
physiology=(
"**Retrolingual airway**: between the tongue base and posterior pharyngeal wall. "
"**Genioglossus**: attaches to the genial tubercle, pulling the tongue forward. "
"**Hyoid**: anchors tongue base and supraglottic structures. "
"**Lingual artery and hypoglossal nerve**: run deep in the tongue base."),
pathophysiology=(
"**Tongue base obstruction**: macroglossia, lingual tonsil hypertrophy, and posterior tongue displacement. "
"**Genioglossus advancement**: moves the tongue attachment forward. "
"**Hyoid suspension**: pulls the hyoid forward and up. "
"**Radiofrequency and resection**: reduce tissue volume, risking bleeding and edema. "
"**Lingual artery injury**: hemorrhage."),
),

"Maxillomandibular Advancement": dict(
overview=(
"Maxillomandibular advancement moves the maxilla and mandible forward, enlarging the entire pharyngeal airway. "
"It is the most effective surgical OSA treatment, especially for craniofacial skeletal deficiency."),
physiology=(
"**Skeletal anchorage**: the soft palate attaches to the posterior hard palate (maxilla), and the tongue, hyoid suspensory muscles, and suprahyoid muscles attach to the mandible. "
"**Soft-tissue tension**: moving the bony attachments forward stretches pharyngeal soft tissues, stiffening the pharyngeal walls. "
"**Airway dimensions**: the pharyngeal airway is enlarged in anteroposterior and lateral dimensions at both velopharyngeal and retrolingual levels. "
"**Craniofacial phenotype**: maxillary and mandibular deficiency reduce the bony box containing the tongue."),
pathophysiology=(
"**Skeletal crowding**: a small maxillomandibular framework forces normal-sized soft tissues into a small space, increasing collapsibility. "
"**Mechanism of benefit**: advancement enlarges the bony enclosure and tensions the lateral pharyngeal walls, reducing critical closing pressure at multiple levels at once. "
"**Success**: high surgical success rates in appropriately selected patients, often with advancement of about 10 mm. "
"**Complications**: malocclusion, inferior alveolar nerve paresthesia, relapse, and facial profile change (often favorable in retrognathic patients). "
"**Indications**: severe OSA, skeletal deficiency, and failure of other therapies."),
),

"Oral Appliance Therapy": dict(
overview=(
"Mandibular advancement devices hold the lower jaw forward during sleep, enlarging the airway. "
"They are effective for mild-to-moderate OSA and CPAP-intolerant patients."),
physiology=(
"**Mandibular protrusion**: advancing the mandible pulls the genioglossus, geniohyoid, and hyoid forward. "
"**Lateral wall tension**: protrusion stretches the palatoglossus and lateral pharyngeal walls, enlarging the velopharynx laterally. "
"**Dental anchorage**: the appliance needs enough healthy teeth to hold the mandible forward. "
"**TMJ adaptability**: the joint tolerates sustained protrusion in most people."),
pathophysiology=(
"**Airway enlargement**: protrusion increases the cross-sectional area, mainly laterally at the velopharynx. "
"**Efficacy**: AHI reduction is less than CPAP, but higher nightly adherence makes overall effectiveness comparable for mild-to-moderate OSA. "
"**Predictors of success**: lower AHI, positional OSA, lower BMI, and retrognathia. "
"**Side effects**: TMJ discomfort, excessive salivation, and long-term occlusal changes. "
"**Titration**: progressive advancement until symptoms and AHI improve."),
),

"HNS Activation / Programming": dict(
overview=(
"HNS activation and programming set stimulation amplitude, electrode configuration, and timing after implantation. "
"Titration with in-lab PSG optimizes efficacy."),
physiology=(
"**Electrode cuff**: wraps the distal hypoglossal nerve, targeting medial protrusor branches. "
"**Configurations**: bipolar (+ - +) and unipolar settings change the current field and which fibers are recruited. "
"**Respiratory sensing**: a pressure sensor between intercostal muscles detects inspiration to time stimulation. "
"**Pulse parameters**: amplitude, pulse width, and rate determine recruitment and comfort."),
pathophysiology=(
"**Underpowered stimulation**: insufficient amplitude fails to protrude the tongue enough to open the airway. "
"**Discomfort and arousal**: high amplitude causes tongue discomfort and sleep disruption. "
"**Retractor recruitment**: current spread to retractor branches pulls the tongue back, defeating protrusion; reconfiguration targets protrusors. "
"**Titration logic**: amplitude is increased stepwise in clinic and during in-lab titration PSG to find the lowest effective setting. "
"**Habituation**: patients start at low amplitude and increase over weeks."),
),

"Residual OSA After Surgery": dict(
overview=(
"Residual OSA after surgery is persistent obstruction, often from unaddressed collapse sites, weight gain, or progressive disease. "
"Evaluation with DISE and PSG guides next steps."),
physiology=(
"**Multilevel airway**: the velopharynx, oropharynx, tongue base, and epiglottis each can collapse independently. "
"**Critical closing pressure**: collapsibility depends on the most collapsible segment. "
"**Weight and fat distribution**: parapharyngeal and tongue fat increase collapsibility."),
pathophysiology=(
"**Untreated collapse sites**: tongue base, lateral wall, or epiglottic collapse persists after palatal surgery. "
"**Weight gain**: increases soft-tissue volume and erodes surgical gains. "
"**Scar**: palatal scar can stiffen or narrow the airway. "
"**Aging and disease progression**: dilator function declines. "
"**Evaluation logic**: repeat PSG and DISE define residual sites to choose CPAP retrial, oral appliance, HNS, or MMA."),
),

"Central Events / Hypoventilation": dict(
overview=(
"Central apneas and hypoventilation reflect absent respiratory drive or inadequate ventilation rather than obstruction. "
"They change surgical candidacy and require different treatment."),
physiology=(
"**Chemical control**: central chemoreceptors (medulla) sense CO2 and pH; peripheral chemoreceptors (carotid bodies) sense O2 and CO2. "
"**Apnea threshold**: during sleep, ventilation stops if PaCO2 falls below a threshold a few mm Hg below waking levels. "
"**Loop gain**: the sensitivity of the respiratory control loop; high loop gain overcorrects disturbances. "
"**Sleep-related drive changes**: the wakefulness drive to breathe is lost in sleep."),
pathophysiology=(
"**High loop gain**: overshoot drives CO2 below the apnea threshold, causing central apnea, then CO2 rises and breathing overshoots again (periodic breathing, Cheyne-Stokes in heart failure). "
"**Opioids**: suppress brainstem respiratory drive, causing ataxic breathing and central apneas. "
"**Hypoventilation**: obesity, neuromuscular disease, and chest wall restriction reduce minute ventilation. "
"**Surgical implications**: airway surgery and HNS do not treat central events, so high central apnea burden excludes HNS. "
"**Treatment**: treating the cause, CPAP, bilevel with backup rate, or adaptive servo-ventilation in selected patients."),
),

"Lingual Tonsil / Tongue-Base Obstruction": dict(
overview=(
"Lingual tonsil hypertrophy is a cause of retrolingual obstruction, especially after palatine tonsillectomy, and contributes to residual OSA. "
"Lingual tonsillectomy treats it."),
physiology=(
"**Lingual tonsils**: lymphoid aggregates on the tongue base forming the inferior part of Waldeyer ring. "
"**Retrolingual airway**: between the tongue base and posterior pharyngeal wall. "
"**Lymphoid responsiveness**: lymphoid tissue enlarges with infection, allergy, and reflux. "
"**Tongue base position**: depends on genioglossus tone and mandibular position."),
pathophysiology=(
"**Compensatory hypertrophy**: lingual tonsils may enlarge after palatine tonsillectomy. "
"**Retrolingual obstruction**: hypertrophy narrows the airway, causing residual OSA. "
"**Epiglottic interaction**: enlarged lingual tonsils push the epiglottis backward. "
"**Lingual tonsillectomy**: reduces volume; risks include bleeding, edema, and taste changes. "
"**Down syndrome**: lingual tonsil hypertrophy is common and contributes to persistent OSA."),
),

"HNS Troubleshooting / Nonresponse": dict(
overview=(
"HNS nonresponse is inadequate improvement after implantation, from programming, anatomy, or device problems. "
"Systematic evaluation identifies correctable causes."),
physiology=(
"**Protrusion vs retraction balance**: effective HNS requires predominant protrusor recruitment. "
"**Palatoglossal coupling**: tongue protrusion pulls the soft palate forward via the palatoglossus. "
"**Sensing and timing**: stimulation must coincide with inspiration."),
pathophysiology=(
"**Electrode placement**: including retractor branches in the cuff reduces protrusion. "
"**Epiglottic collapse**: unaffected by tongue protrusion. "
"**Poor palatoglossal coupling**: tongue moves but the palate stays collapsed. "
"**Weight gain**: increases collapsibility. "
"**Device issues**: sensing lead failure, lead migration, or impedance problems. "
"**Evaluation**: device interrogation, awake endoscopy during stimulation, titration PSG, and DISE with stimulation."),
),

"Down Syndrome Pediatric HNS": dict(
overview=(
"HNS is FDA-approved for adolescents with Down syndrome and persistent OSA after adenotonsillectomy, with specific age and AHI criteria. "
"It addresses tongue-base and multilevel collapse common in Down syndrome."),
physiology=(
"**Down syndrome airway**: midface hypoplasia, relative macroglossia, narrow nasopharynx, and generalized hypotonia. "
"**Lymphoid tissue**: lingual tonsil hypertrophy is common. "
"**Hypotonia**: reduces pharyngeal dilator tone during sleep. "
"**Obesity**: more prevalent."),
pathophysiology=(
"**Persistent OSA**: occurs in most children with Down syndrome after adenotonsillectomy because of multilevel collapse. "
"**HNS logic**: increases genioglossus tone, counteracting hypotonia and tongue-base collapse. "
"**Criteria**: FDA approval for ages 13-18 with AHI roughly 10-50 after adenotonsillectomy and CPAP failure. "
"**Outcomes**: significant AHI reduction and improved quality of life. "
"**Behavioral considerations**: tolerance of device and remote control use."),
),

"Central Sleep Apnea / Treatment-Emergent CSA": dict(
overview=(
"Central sleep apnea is apnea without respiratory effort; treatment-emergent CSA appears when CPAP treats obstruction. "
"It is linked to heart failure, opioids, stroke, and high altitude."),
physiology=(
"**CO2-driven breathing**: during sleep, PaCO2 is the dominant driver of ventilation. "
"**Apnea threshold**: breathing stops when PaCO2 falls below a threshold. "
"**Circulation time**: delay between lung gas exchange and chemoreceptor sensing affects stability."),
pathophysiology=(
"**Hyperventilation-related CSA**: excess ventilatory sensitivity drives CO2 below threshold. "
"**Heart failure**: prolonged circulation time and pulmonary congestion cause Cheyne-Stokes respiration. "
"**Treatment-emergent CSA**: when CPAP opens the airway, increased ventilation lowers CO2, unmasking central apneas; it often resolves with continued use. "
"**Opioids**: depress drive. "
"**Adaptive servo-ventilation**: contraindicated in heart failure with reduced ejection fraction (SERVE-HF). **Phrenic nerve stimulation**: transvenous stimulation is an option for moderate-to-severe CSA in the 2025 AASM CSA guideline."),
),

"Sleep-Related Hypoventilation": dict(
overview=(
"Sleep-related hypoventilation is inadequate ventilation during sleep with elevated CO2, from obesity, neuromuscular disease, or chest wall disorders. "
"Bilevel ventilation is often required."),
physiology=(
"**Normal sleep ventilation**: minute ventilation falls slightly and PaCO2 rises a few mm Hg. "
"**REM atonia**: accessory muscles lose tone, leaving the diaphragm to sustain ventilation. "
"**Respiratory load**: obesity and chest wall disease increase work of breathing."),
pathophysiology=(
"**Obesity hypoventilation syndrome**: mass loading, reduced lung volumes, and blunted CO2 responsiveness cause daytime hypercapnia. "
"**Neuromuscular weakness**: diaphragm weakness causes REM hypoventilation first. "
"**Progression**: nocturnal hypoventilation precedes daytime hypercapnia. "
"**Treatment**: bilevel PAP provides ventilatory support beyond CPAP."),
),

"Narcolepsy / Central Hypersomnolence Recognition": dict(
overview=(
"Narcolepsy is a central hypersomnolence disorder with excessive daytime sleepiness, sometimes with cataplexy, from hypocretin deficiency. "
"It must be distinguished from OSA before surgery."),
physiology=(
"**Hypocretin (orexin)**: lateral hypothalamic neurons stabilize wakefulness and suppress inappropriate REM. "
"**REM sleep features**: muscle atonia, dreaming, and rapid eye movements. "
"**Sleep-wake switch**: reciprocal inhibition between wake- and sleep-promoting nuclei."),
pathophysiology=(
"**Hypocretin neuron loss**: likely autoimmune destruction (HLA-DQB1*06:02) causes type 1 narcolepsy with low CSF hypocretin. "
"**REM intrusion**: cataplexy (emotion-triggered atonia), sleep paralysis, and hypnagogic hallucinations. "
"**Diagnosis**: MSLT shows mean sleep latency of 8 minutes or less with two or more sleep-onset REM periods. "
"**Why it matters for surgeons**: persistent sleepiness after OSA treatment may reflect narcolepsy rather than surgical failure."),
),

"Restless Legs / Periodic Limb Movement Disorders": dict(
overview=(
"Restless legs syndrome is an urge to move the legs at rest in the evening; periodic limb movements are repetitive leg movements in sleep. "
"Both fragment sleep and can mimic OSA symptoms."),
physiology=(
"**Dopaminergic systems**: regulate motor control and sensory processing. "
"**Iron**: a cofactor for tyrosine hydroxylase, the rate-limiting enzyme for dopamine synthesis. "
"**Circadian modulation**: dopamine levels fall in the evening."),
pathophysiology=(
"**Brain iron deficiency**: low ferritin is associated with RLS; iron replacement helps when ferritin is low. "
"**Dopaminergic dysfunction**: explains evening symptom worsening. "
"**Secondary causes**: pregnancy, renal failure, neuropathy, and medications (antihistamines, antidepressants). "
"**Periodic limb movements**: fragment sleep, mimicking OSA sleepiness. "
"**Treatment**: iron, alpha-2-delta ligands first-line; dopamine agonists risk augmentation."),
),

"Circadian Rhythm Sleep-Wake Disorders": dict(
overview=(
"Circadian rhythm disorders misalign sleep timing with the desired schedule (delayed or advanced phase, shift work, jet lag). "
"They cause insomnia and sleepiness that can mimic OSA."),
physiology=(
"**Suprachiasmatic nucleus**: the master clock in the hypothalamus, entrained mainly by light via the retinohypothalamic tract. "
"**Melatonin**: secreted by the pineal gland in darkness, signaling biological night. "
"**Two-process model**: sleep pressure (adenosine) and circadian alerting together determine sleep timing."),
pathophysiology=(
"**Delayed sleep phase**: common in adolescents; sleep onset and wake times shift later. "
"**Advanced sleep phase**: common in older adults. "
"**Shift work and jet lag**: misalignment between clock and schedule. "
"**Mimicry**: insomnia and sleepiness can be misattributed to OSA. "
"**Treatment**: timed light exposure and melatonin shift the clock."),
),

"Positional OSA": dict(
overview=(
"Positional OSA is OSA predominantly in the supine position, defined by a supine AHI substantially higher than non-supine AHI. "
"Positional therapy may treat it alone or as an adjunct."),
physiology=(
"**Gravity effects**: supine position lets the tongue and soft palate fall posteriorly, narrowing the airway anteroposteriorly. "
"**Lateral position**: improves airway shape and reduces collapsibility. "
"**Lung volume**: supine position reduces lung volume, reducing tracheal traction on the pharynx."),
pathophysiology=(
"**Supine-predominant collapse**: anteroposterior collapse at the palate and tongue base worsens supine. "
"**Definitions**: Cartwright criteria (supine AHI at least twice non-supine AHI); Amsterdam classification refines categories. "
"**Positional therapy**: vibration devices or positional aids prevent supine sleep. "
"**Adherence**: limited for older devices; newer vibration trainers improve it. "
"**Adjunct role**: improves residual OSA after surgery or HNS."),
),

"Nasal Surgery as a CPAP-Adherence Adjunct": dict(
overview=(
"Nasal surgery rarely cures OSA but reduces CPAP pressure and improves adherence in patients with nasal obstruction. "
"It is also used to improve HNS and oral appliance tolerance."),
physiology=(
"**Nasal resistance**: contributes about two-thirds of total airway resistance during wakefulness (Cummings). "
"**Starling resistor model**: increased upstream resistance creates more negative downstream pharyngeal pressure, promoting collapse. "
"**Nasal breathing during sleep**: stabilizes mandibular position and pharyngeal patency."),
pathophysiology=(
"**Nasal obstruction**: increases negative pharyngeal pressure and mouth breathing. "
"**Mouth breathing**: lets the mandible and tongue fall back. "
"**CPAP effects**: nasal obstruction increases required pressure and mask leak, reducing adherence. "
"**Nasal surgery**: rarely cures OSA but lowers CPAP pressure and improves adherence and tolerance of oral appliances and HNS."),
),

"Adult Epiglottic Collapse / Epiglottopexy": dict(
overview=(
"Adult epiglottic collapse is prolapse of a floppy epiglottis into the airway during sleep, causing CPAP and HNS failure. "
"Epiglottopexy or partial epiglottectomy treats it."),
physiology=(
"**Epiglottis**: elastic cartilage anchored by the hyoepiglottic ligament and lateral pharyngoepiglottic folds. "
"**Supraglottic airway**: normally patent during inspiration. "
"**Tongue base influence**: tongue base position affects epiglottic angle."),
pathophysiology=(
"**Trapdoor collapse**: a floppy or posteriorly displaced epiglottis prolapses into the laryngeal inlet during inspiration. "
"**CPAP failure**: positive pressure can push the epiglottis further closed. "
"**HNS failure**: tongue protrusion does not reliably move the epiglottis. "
"**Diagnosis**: DISE shows epiglottic collapse. "
"**Treatment**: epiglottopexy (suturing the epiglottis to the tongue base) or partial epiglottectomy."),
),

"Tracheostomy as Definitive OSA Therapy": dict(
overview=(
"Tracheostomy bypasses all upper-airway collapse and is nearly 100 percent effective for OSA. "
"It is reserved for severe OSA when other treatments fail."),
physiology=(
"**Upper airway bypass**: air enters below the larynx, bypassing all sites of collapse. "
"**Humidification loss**: tracheostomy bypasses nasal humidification. "
"**Speech**: requires occlusion or a speaking valve."),
pathophysiology=(
"**Complete bypass**: eliminates obstructive events regardless of collapse site. "
"**Central apneas and hypoventilation**: not treated by tracheostomy alone. "
"**Morbid obesity**: technically difficult with stoma complications. "
"**Quality of life**: affects voice and self-image. "
"**Indications**: severe OSA unresponsive to other treatments, often with cardiopulmonary complications."),
),
}
