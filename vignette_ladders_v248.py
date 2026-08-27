"""v24.8 — Pediatric Otolaryngology deliberate ladder pass 8.

Closes the five remaining exact canonical Pediatric topics with complete
foundation -> application -> senior-decision ladders. Senior decisions emphasize
recognition of atypical disease, multidisciplinary escalation, avoiding unsupported
ENT surgery, and high-stakes neurologic/feeding differentials.
"""
DOMAIN="Pediatric Otolaryngology"


def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}


VIGNETTES_V248=[
_q("v248_ped_jrp_fnd","Juvenile Recurrent Parotitis","foundation",
"An otherwise healthy 7-year-old has had four self-limited episodes of painful unilateral parotid swelling over two years. Between episodes the gland is normal, and there is no persistent mass or facial weakness. What diagnosis best fits?",
["Juvenile recurrent parotitis","Parotid malignancy","Obstructing salivary stone as the only plausible diagnosis","Acute bacterial parotitis with abscess during every episode"],0,
"Juvenile recurrent parotitis causes recurrent inflammatory parotid swelling in children, often without a fixed obstructing lesion and with symptom-free intervals. The diagnosis is clinical after excluding atypical infectious, obstructive, autoimmune, and neoplastic features.",
["Correct. Recurrent self-limited parotid inflammation with normal intervals is the classic pattern.","A persistent or progressive mass, facial weakness, or other concerning findings would be much more worrisome for neoplasm.","A stone can cause recurrent symptoms but is not the only cause; many children with JRP have no fixed calculus.","Toxic appearance, purulence, fluctuance, or an abscess would support acute suppurative infection rather than explain every stereotyped self-limited episode."],
"JRP is a recurrent inflammatory syndrome; a persistent mass or facial nerve deficit is not part of the reassuring pattern.","Which atypical findings should make you stop calling recurrent swelling JRP and reopen the differential?"),
_q("v248_ped_jrp_app","Juvenile Recurrent Parotitis","application",
"A child with known juvenile recurrent parotitis develops another typical episode of gland pain and swelling but is afebrile, well hydrated, and has no purulence or abscess. What is the best initial management?",
["Supportive care with hydration, analgesia, gland massage/oral hygiene, reserving antibiotics for evidence of bacterial infection","Immediate superficial parotidectomy","Prolonged broad-spectrum intravenous antibiotics for every recurrence","Urgent radiation therapy to suppress the gland"],0,
"Most uncomplicated JRP flares are managed conservatively. Antibiotics are not automatically required in a well child without convincing suppurative infection, while imaging can be used when the pattern is atypical or complications/obstruction are suspected.",
["Correct. Conservative treatment is appropriate for an uncomplicated stereotyped flare.","Parotidectomy carries facial-nerve and other morbidity and is not first-line treatment for typical JRP.","Routine prolonged IV antibiotics over-treat non-suppurative inflammatory episodes.","Radiation has no role in routine pediatric recurrent parotitis."],
"Do not equate every swollen pediatric parotid with bacterial suppuration.","When would ultrasound or cross-sectional imaging add value during a recurrence?","overnight_call"),
_q("v248_ped_jrp_snr","Juvenile Recurrent Parotitis","senior_decision",
"A 10-year-old has frequent JRP attacks that are disrupting school despite appropriate conservative care. There is no concerning mass, immunologic diagnosis, or fixed stone. What is the best next senior-level management principle?",
["Discuss salivary endoscopy with duct evaluation, irrigation and/or dilation in an experienced center before considering destructive gland surgery","Proceed directly to total parotidectomy because recurrence proves conservative failure","Continue antibiotics indefinitely between attacks","Ignore the burden because JRP can never justify procedural treatment"],0,
"For burdensome recurrent disease, sialendoscopy can provide minimally invasive ductal evaluation and treatment and is commonly considered before parotidectomy. Senior care also rechecks the diagnosis when the course becomes atypical rather than escalating blindly.",
["Correct. Sialendoscopy offers a gland-preserving escalation strategy for selected refractory cases.","Parotidectomy is a high-morbidity option, particularly because of facial-nerve risk, and is rarely the next step for otherwise typical JRP.","Chronic suppressive antibiotics do not address the usual inflammatory mechanism and add antimicrobial harm.","Quality-of-life burden can justify escalation even when the disease is benign."],
"Escalate JRP with a gland-preserving strategy before a gland-sacrificing one.","How would persistent unilateral enlargement, facial weakness, xerostomia, or systemic inflammatory symptoms change your workup?","senior_management"),

_q("v248_ped_speech_fnd","Pediatric Speech Disorders","foundation",
"A child produces age-inappropriate sound substitutions but has normal resonance and no audible nasal air escape. Which category best describes the primary problem?",
["An articulation or phonologic speech-sound disorder","Velopharyngeal insufficiency by definition","Bilateral vocal-fold paralysis","Obstructive sleep apnea"],0,
"Speech-sound disorders involve production or organization of sounds, whereas resonance disorders such as hypernasality raise different structural or functional questions. ENT assessment should distinguish these categories rather than treating all abnormal speech as an anatomic surgical problem.",
["Correct. Sound substitutions with normal resonance fit a speech-sound disorder more than a structural velopharyngeal problem.","VPI typically causes resonance and nasal-emission abnormalities; it is not defined by isolated sound substitution.","Bilateral vocal-fold paralysis primarily threatens airway and voice rather than causing a classic phonologic pattern.","OSA is a sleep-breathing disorder and does not explain isolated articulation errors."],
"First classify the speech problem: articulation/phonology, language, voice, fluency, or resonance.","Which speech findings specifically raise concern for velopharyngeal dysfunction rather than learned articulation?"),
_q("v248_ped_speech_app","Pediatric Speech Disorders","application",
"A 3-year-old is referred to ENT for delayed speech after passing the newborn hearing screen. Otoscopy is unremarkable. What is the best next principle?",
["Obtain age-appropriate audiologic assessment and coordinate speech-language/developmental evaluation rather than assuming normal hearing from the newborn screen","Reassure without testing because a passed newborn screen excludes later hearing loss","Perform frenotomy solely because speech is delayed","Recommend adenotonsillectomy before defining the type of speech disorder"],0,
"A newborn screen is a time-point screen, not lifelong proof of normal hearing. Speech delay warrants current hearing assessment plus speech-language and developmental characterization so reversible auditory or structural contributors are not missed.",
["Correct. Current audiology is part of the basic workup of speech delay even after a passed newborn screen.","Progressive, acquired, conductive, and delayed-onset hearing loss can all occur after newborn screening.","Frenotomy should be based on demonstrated functional restriction, not nonspecific speech delay.","Upper-airway surgery does not treat an undefined speech disorder and may itself affect resonance in susceptible children."],
"A passed newborn hearing screen does not close the hearing question when speech later falls behind.","What history would make you prioritize recurrent effusion, progressive SNHL, or a broader developmental disorder?"),
_q("v248_ped_speech_snr","Pediatric Speech Disorders","senior_decision",
"A child has persistent hypernasality after cleft repair despite speech therapy. What should happen before selecting a secondary speech operation?",
["Combine expert perceptual speech assessment with targeted dynamic evaluation of velopharyngeal closure and distinguish structural VPI from compensatory articulation","Choose a pharyngeal flap based on hypernasality alone","Continue articulation therapy indefinitely without evaluating anatomy","Remove additional adenoid tissue to enlarge the velopharyngeal gap"],0,
"Secondary surgery should match the demonstrated closure pattern and gap while accounting for airway risk. Learned compensatory errors require therapy, whereas structural VPI may require surgery; many children have both.",
["Correct. Dynamic localization plus speech assessment is necessary before choosing a VPI operation.","Hypernasality does not define the gap size or closure pattern needed to select a procedure.","Therapy cannot correct a clinically important structural closure defect by itself.","Further adenoid removal can worsen velopharyngeal competence in a vulnerable child."],
"Operate on a proven velopharyngeal mechanism, not on the word 'hypernasal.'",
"How would severe baseline OSA change your tolerance for a pharyngeal flap versus other VPI strategies?","senior_management"),

_q("v248_ped_sleep_fnd","Nonobstructive Pediatric Sleep Disorders","foundation",
"A school-aged child has prolonged sleep-onset difficulty and inconsistent bedtimes but no snoring, witnessed apneas, or gasping. Which principle is most appropriate?",
["Consider behavioral insomnia or circadian/sleep-hygiene causes rather than assuming upper-airway obstruction","Adenotonsillar hypertrophy is proven even without obstructive symptoms","Polysomnography-confirmed OSA is present by definition","Tonsillectomy is the first-line diagnostic test"],0,
"Pediatric sleep complaints are broader than OSA. Sleep-onset and schedule problems without obstructive symptoms should prompt evaluation of behavioral, circadian, medical, medication, neurologic, and other sleep causes.",
["Correct. The symptom pattern is nonobstructive and should not be forced into an OSA pathway.","Adenotonsillar size cannot be inferred from insomnia symptoms and would not establish causality.","OSA requires evidence of obstructive sleep-disordered breathing, not isolated difficulty initiating sleep.","Surgery is neither a diagnostic test nor a treatment for undefined nonobstructive insomnia."],
"Not every sleepy child—or every child who sleeps poorly—has an upper-airway surgical problem.","Which history points toward restless legs, parasomnia, circadian delay, medication effect, or narcolepsy?"),
_q("v248_ped_sleep_app","Nonobstructive Pediatric Sleep Disorders","application",
"A child remains markedly sleepy after adenotonsillectomy. Repeat polysomnography shows resolution of obstructive events. What is the best next step?",
["Broaden the evaluation to nonobstructive sleep and medical causes and involve pediatric sleep medicine as indicated rather than repeating airway surgery","Perform revision adenotonsillectomy despite normalized obstruction","Assume persistent sleepiness proves occult tongue-base obstruction even without supporting data","Stop evaluation because a normal AHI means the symptom cannot be real"],0,
"When obstruction has objectively resolved but symptoms persist, the residual complaint should be re-phenotyped. Insufficient sleep, circadian disorders, restless legs/periodic limb movement, hypersomnia, medication effects, mood disorders, seizures, and systemic disease may require different testing and treatment.",
["Correct. Persistent symptoms after successful airway treatment are a signal to broaden, not simply intensify, surgery.","Repeat surgery without residual obstruction lacks a target and adds morbidity.","Tongue-base obstruction should be demonstrated through the appropriate obstructive evaluation rather than assumed from sleepiness alone.","Objective normalization of breathing does not invalidate persistent symptoms from another cause."],
"When the airway endpoint is fixed but the child is not, reopen the diagnosis.","Which symptoms would prompt MSLT or neurologic evaluation rather than another airway study?","senior_management"),
_q("v248_ped_sleep_snr","Nonobstructive Pediatric Sleep Disorders","senior_decision",
"A teenager has disabling daytime sleepiness, sleep paralysis and episodes of emotion-triggered loss of muscle tone. Examination shows large tonsils but there is no convincing snoring history. What is the best chief-level response?",
["Prioritize evaluation for a central hypersomnolence disorder such as narcolepsy with sleep-medicine testing rather than attributing symptoms to tonsil size","Recommend tonsillectomy because large tonsils explain cataplexy","Diagnose behavioral insomnia without further evaluation","Treat empirically for reflux because reflux commonly causes cataplexy"],0,
"Cataplexy-like episodes with profound daytime sleepiness are a major clue to narcolepsy. Incidental tonsillar size should not override a syndrome pointing to a central sleep disorder; appropriate overnight sleep assessment followed by specialized testing is coordinated through sleep medicine.",
["Correct. The clinical syndrome, not an anatomic incidental finding, should drive the next diagnostic pathway.","Tonsillar hypertrophy can contribute to OSA but does not explain cataplexy.","The symptom cluster warrants evaluation for central hypersomnolence rather than a default behavioral label.","Reflux does not cause the characteristic emotion-triggered loss of tone described."],
"Chief-level sleep care includes knowing when a large tonsil is not the diagnosis.","Why must insufficient sleep and untreated OSA be addressed before interpreting a multiple sleep latency test?","senior_management"),

_q("v248_ped_vest_fnd","Pediatric Vestibular Disorders","foundation",
"Which statement best describes vestibular disease in children?",
["Children may present with imbalance, delayed motor milestones, falls, motion intolerance or vague episodic symptoms rather than using the word 'vertigo'","A child who cannot describe spinning cannot have vestibular dysfunction","Vestibular disorders occur only after temporal-bone surgery","Normal hearing excludes vestibular disease"],0,
"Pediatric vestibular symptoms are often developmentally expressed. History from caregivers, gait and ocular-motor examination, hearing assessment and appropriately selected vestibular testing are therefore important when symptoms or motor development suggest imbalance.",
["Correct. Young children often communicate vestibular dysfunction through behavior and motor performance rather than adult symptom vocabulary.","Limited vocabulary does not exclude a physiologic vestibular deficit.","Congenital, migraine-associated, infectious, genetic and other vestibular disorders occur without surgery.","Many vestibular disorders occur with normal hearing."],
"In children, vestibular dysfunction may look like delayed walking or recurrent falls before it sounds like 'vertigo.'",
"What developmental history would make bilateral vestibular hypofunction more likely?"),
_q("v248_ped_vest_app","Pediatric Vestibular Disorders","application",
"A 12-year-old has recurrent episodes of vertigo with photophobia and headache, normal neurologic examination between attacks, and no progressive unilateral hearing loss. What diagnosis should be high on the differential?",
["Vestibular migraine","Acoustic neuroma is proven","Acute bacterial labyrinthitis during every attack","Benign positional vertigo is certain without positional testing"],0,
"Vestibular migraine is an important cause of episodic vertigo in older children and adolescents. Diagnosis remains clinical after an appropriate history and examination while red flags or atypical auditory findings prompt broader evaluation.",
["Correct. Episodic vestibular symptoms with migraine features and a normal interval examination strongly support this consideration.","A tumor is not established by this episodic migraine phenotype and would usually require additional focal/auditory evidence.","Bacterial labyrinthitis generally presents as an acute severe illness rather than recurrent stereotyped migraine-associated episodes.","BPPV has a characteristic positional trigger and examination and should not be declared without it."],
"Vestibular migraine is common enough to recognize, but it remains a diagnosis made in the context of a reassuring neurologic pattern.","Which red flags would override a migraine history and trigger urgent neurologic evaluation?"),
_q("v248_ped_vest_snr","Pediatric Vestibular Disorders","senior_decision",
"A child with congenital severe bilateral hearing loss is being considered for cochlear implantation. Vestibular testing suggests one ear provides most of the child's residual vestibular function. What is the best senior-level planning principle?",
["Integrate vestibular reserve with cochlear anatomy, auditory candidacy and rehabilitation goals when selecting side and counseling, rather than treating vestibular testing as irrelevant or as the sole determinant","Ignore vestibular function because cochlear implantation can never affect balance","Implant the better-functioning vestibular ear automatically regardless of cochlear anatomy","Cancel cochlear implantation permanently because any residual vestibular function is an absolute contraindication"],0,
"Cochlear implantation can affect vestibular function in some patients. When asymmetric vestibular reserve is clinically important, it should inform side selection and counseling alongside auditory and anatomic factors, while postoperative vestibular rehabilitation is available when needed.",
["Correct. Senior planning integrates hearing benefit and balance risk rather than optimizing one system in isolation.","Vestibular consequences are possible and can matter greatly in a child with limited reserve.","No single vestibular test overrides cochlear anatomy, hearing performance and the overall rehabilitation plan.","Residual vestibular function is not an absolute contraindication to implantation."],
"For a child with little vestibular reserve, side selection is a hearing-and-balance decision.","How would new inability to walk, focal neurologic deficits, severe headache or direction-changing nystagmus change the urgency of your evaluation?","senior_management"),

_q("v248_ped_reflux_eoe_fnd","Pediatric Reflux / Eosinophilic Esophagitis","foundation",
"A school-aged child with eczema and food allergies develops progressive solid-food dysphagia and two food impactions. Which diagnosis must be specifically considered?",
["Eosinophilic esophagitis","Isolated laryngopharyngeal reflux is proven by the atopic history","Adenoid hypertrophy","Uncomplicated otitis media"],0,
"Eosinophilic esophagitis commonly presents with age-dependent feeding problems, dysphagia and food impaction and is associated with atopy. Diagnosis requires gastroenterologic evaluation with esophageal endoscopy and biopsies interpreted in clinical context.",
["Correct. Recurrent solid-food dysphagia/impaction in an atopic child is a classic EoE signal.","Atopy does not prove reflux, and food impaction should not be dismissed as nonspecific laryngeal reflux.","Adenoid hypertrophy does not explain esophageal food impactions.","Middle-ear disease does not explain progressive solid-food dysphagia."],
"Food impaction plus atopy should put EoE on the ENT resident's radar even though the definitive diagnosis lives in the esophagus.","Why can a normal laryngeal examination neither diagnose nor exclude EoE?"),
_q("v248_ped_reflux_eoe_app","Pediatric Reflux / Eosinophilic Esophagitis","application",
"A child has chronic throat clearing and hoarseness. Flexible laryngoscopy shows mild nonspecific posterior erythema, but there is no dysphagia, weight loss, aspiration history, or other alarm feature. What is the best principle?",
["Avoid diagnosing reflux from nonspecific laryngeal erythema alone; use the history to consider competing voice, allergy, habit, airway and gastrointestinal causes before prolonged empiric therapy","Posterior erythema definitively proves pathologic reflux","Start indefinite high-dose acid suppression without reassessment","Refer directly for antireflux surgery based only on the laryngoscopy"],0,
"Many laryngeal findings attributed to reflux are nonspecific. Pediatric management should avoid turning a low-specificity visual finding into a definitive diagnosis and should reassess if empiric management does not match the clinical phenotype.",
["Correct. Clinical context and competing diagnoses matter because laryngeal erythema alone has poor specificity for reflux.","Erythema can occur from multiple irritative, infectious, behavioral and technical causes.","Indefinite medication without a clear indication or response assessment exposes the child to treatment without diagnostic discipline.","Antireflux surgery requires a far stronger physiologic and clinical indication than isolated nonspecific erythema."],
"Do not let a red posterior larynx become a reflex diagnosis of pediatric reflux.","Which alarm features should prompt swallowing, GI, pulmonary, or neurologic evaluation instead of simply escalating acid suppression?"),
_q("v248_ped_reflux_eoe_snr","Pediatric Reflux / Eosinophilic Esophagitis","senior_decision",
"A child has recurrent solid-food dysphagia and food impaction despite months of empiric acid suppression prescribed for presumed 'LPR.' What is the best chief-level next step?",
["Stop escalating an unproven laryngeal-reflux diagnosis and coordinate pediatric GI evaluation with endoscopy and esophageal biopsies for EoE or other structural/inflammatory disease","Double acid suppression indefinitely without further testing","Perform tonsillectomy because tonsils are a common cause of esophageal food impaction","Conclude symptoms are behavioral because reflux treatment failed"],0,
"Failure of empiric reflux therapy plus true esophageal alarm symptoms requires diagnostic re-framing. EoE, stricture and other esophageal disorders need direct GI evaluation; ENT should also address coexisting airway or swallowing concerns without substituting laryngoscopy for esophageal diagnosis.",
["Correct. Persistent dysphagia/impaction is an alarm phenotype that deserves definitive esophageal evaluation.","More empiric acid suppression delays diagnosis when the original reflux attribution is unsupported.","Tonsillar surgery does not treat esophageal food impaction.","Treatment failure is not evidence that symptoms are behavioral and should not short-circuit investigation of structural/inflammatory disease."],
"When the symptom is food sticking in the esophagus, escalate the diagnostic pathway—not the reflux label.","How would aspiration, recurrent pneumonia, weight loss, or neurologic disease broaden the parallel swallow/airway evaluation?","senior_management"),
]


def apply_learning_ladders_v248(challenges, concept_id_fn):
    existing={q.get("id") for q in challenges}
    added=[]
    for src in VIGNETTES_V248:
        if src["id"] in existing:
            continue
        q=dict(src)
        q["concept_id"]=concept_id_fn(DOMAIN,q["topic"])
        challenges.append(q)
        added.append(q)
        existing.add(q["id"])
    return added
