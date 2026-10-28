"""Otology / Neurotology (part B): mechanism-level teaching content."""

CONTENT = {
"Petrous Apex Lesions": dict(
overview=(
"Petrous apex lesions range from benign incidental findings (asymmetric pneumatization, effusion) to cholesterol granuloma, cholesteatoma, mucocele, apicitis, and tumors. "
"The key skill is distinguishing them by CT and MRI signal so that only lesions that need treatment get it."),
physiology=(
"**Location**: the petrous apex is the medial part of the temporal bone, anteromedial to the inner ear, between the IAC, carotid canal, Meckel cave, and Dorello canal (CN VI). "
"**Pneumatization**: about a third of people have pneumatized apices, often asymmetric; marrow-filled apices appear bright on T1 MRI due to fat. "
"**Drainage**: apex air cells drain through narrow tracts toward the middle ear and mastoid."),
pathophysiology=(
"**Cholesterol granuloma**: obstruction of a pneumatized apex causes negative pressure, mucosal hemorrhage, and breakdown of red cells into cholesterol crystals that incite a foreign-body reaction and slow expansion; it is bright on both T1 and T2. "
"**Cholesteatoma or epidermoid**: trapped squamous epithelium is T1 dark, T2 bright, and restricts diffusion. "
"**Effusion and asymmetric marrow**: trapped fluid or fat without bone expansion is usually incidental and should not be treated. "
"**Apicitis**: infection spreading from the mastoid into apex cells produces Gradenigo syndrome (otorrhea, retro-orbital pain from CN V, abducens palsy). "
"**Symptoms from neighbors**: expanding lesions compress CN V, CN VI, VII and VIII, or the IAC, causing facial pain, diplopia, facial weakness, and hearing loss. "
"**Treatment logic**: symptomatic expansile lesions are drained (cholesterol granuloma) or removed (cholesteatoma) through approaches chosen to protect hearing and the carotid."),
),

"Age-Related Hearing Loss / Presbycusis": dict(
overview=(
"Presbycusis is gradual, bilateral, symmetric, high-frequency sensorineural loss with aging. "
"It is the most common cause of hearing loss in adults, is linked to cognitive decline and social isolation, and is managed with amplification and communication strategies."),
physiology=(
"**Base-to-apex vulnerability**: high-frequency basal hair cells are exposed to more cumulative mechanical and metabolic stress. "
"**Stria vascularis**: generates the endocochlear potential, the battery of the cochlea, and depends on rich microvasculature. "
"**Central processing**: understanding speech in noise depends on temporal processing and cognition, not just thresholds."),
pathophysiology=(
"**Sensory (hair cell) type**: basal outer hair-cell loss produces a steep high-frequency slope. "
"**Strial (metabolic) type**: atrophy of the stria reduces the endocochlear potential across the cochlea, producing a flat loss with relatively good word recognition. "
"**Neural type**: loss of spiral ganglion neurons and synapses produces word recognition worse than expected from thresholds. "
"**Cumulative contributors**: noise exposure, genetics, vascular disease, diabetes, smoking, and ototoxic medications add to aging changes. "
"**Speech-in-noise difficulty**: high-frequency consonant information is lost first, and central temporal processing declines, so patients say they hear but do not understand. "
"**Cognitive link**: reduced auditory input increases listening effort and may reduce cognitive reserve; Cummings 7e states there is not yet definitive evidence that treatment prevents decline; the later ACHIEVE trial (2023) found slower decline only in older adults at higher baseline risk."),
),

"Acute Mastoiditis / Petrous Apicitis": dict(
overview=(
"Acute mastoiditis is spread of acute otitis media into the mastoid air cells, sometimes with bone destruction (coalescence) and subperiosteal abscess. "
"It is most common in young children and can spread to intracranial, neck, and petrous apex compartments."),
physiology=(
"**Continuity**: the mastoid air cells connect to the middle ear through the aditus ad antrum, so middle-ear infection commonly extends to the mastoid mucosa (radiographic mastoid opacification often accompanies AOM or OME and is not itself mastoiditis). "
"**Bony septations**: thin septa divide air cells; the cortex overlying the antrum is thin in children (Macewen triangle). "
"**Venous connections**: emissary veins connect the mastoid to the sigmoid sinus."),
pathophysiology=(
"**Obstruction**: mucosal swelling at the aditus traps pus in the mastoid under pressure. "
"**Coalescence**: inflammation and pressure cause osteitis and resorption of the septa, forming an abscess cavity. "
"**Subperiosteal abscess**: pus erodes through the lateral cortex, pushing the pinna forward and outward (postauricular swelling and erythema). "
"**Other paths**: Bezold abscess (through the tip into the SCM sheath), petrous apicitis (Gradenigo triad), sigmoid sinus thrombosis via emissary veins, epidural or brain abscess via the tegmen, meningitis, and facial palsy. "
"**Why tubes and mastoidectomy**: myringotomy drains the middle ear and gives culture; mastoidectomy is needed when coalescent disease, abscess, or complications do not resolve with antibiotics."),
),

"Persistent Postural-Perceptual Dizziness (PPPD)": dict(
overview=(
"PPPD is chronic (3 months or more) non-spinning dizziness or unsteadiness, worsened by upright posture, motion, and complex visual environments, usually triggered by an earlier vestibular or medical event. "
"It is a functional disorder of how the brain controls balance, treated with vestibular rehabilitation, SSRIs/SNRIs, and CBT."),
physiology=(
"**Postural control strategies**: after a vestibular insult, the brain shifts toward vision and stiff, high-vigilance postural control. "
"**Normal recovery**: once the insult resolves or is compensated, the brain returns to relaxed, automatic balance control. "
"**Threat networks**: anxiety and attention networks interact with vestibular and visual processing."),
pathophysiology=(
"**Failure to readapt**: the brain stays locked in high-threat postural control and visual dependence after the precipitating event resolves. "
"**Visual dependence**: overreliance on vision makes busy patterns, scrolling screens, and supermarkets provocative. "
"**Maintenance cycle**: anxiety and hypervigilance about balance increase the abnormal strategy, which increases symptoms. "
"**Normal tests**: the vestibular battery is usually normal or shows only a compensated old lesion, which is why it is a positive diagnosis based on criteria rather than exclusion alone. "
"**Treatment logic**: habituation-based rehabilitation retrains automatic balance, serotonergic medications reduce threat sensitivity, and CBT addresses avoidance."),
),

"Patulous Eustachian Tube Dysfunction": dict(
overview=(
"Patulous Eustachian tube dysfunction is failure of the tube to close, so the middle ear stays open to the nasopharynx. "
"It causes autophony and hearing one's own breathing, and it is often mistaken for dilatory ETD or superior canal dehiscence."),
physiology=(
"**Normal closure**: the cartilaginous tube is held closed by elastic recoil, the Ostmann fat pad, and surrounding tissue tension. "
"**Protective role**: closure shields the middle ear from voice and breathing pressures."),
pathophysiology=(
"**Loss of closing tissue**: weight loss shrinks the Ostmann fat pad; pregnancy, hormonal changes, radiation, and neuromuscular disease reduce closing forces. "
"**Symptoms**: voice and breathing sounds transmit directly into the middle ear, causing autophony, a sense of fullness, and audible breathing. "
"**Positional relief**: lying down or lowering the head increases venous congestion around the tube, temporarily closing it. "
"**Exam clue**: the tympanic membrane moves with nasal respiration, especially with ipsilateral nostril breathing. "
"**Sniffing habit**: patients learn to sniff to lock the tube closed with negative pressure, which can cause retraction and even cholesteatoma. "
"**Distinguishing SCD**: SCD autophony includes eye movements and footsteps and has third-window audiometric findings; patulous tubes do not."),
),

"Perilymph Fistula / Inner-Ear Window Leak": dict(
overview=(
"A perilymph fistula is an abnormal leak of perilymph from the inner ear into the middle ear, usually at the oval or round window, after barotrauma, stapes surgery, or trauma. "
"It causes fluctuating hearing loss and pressure-related vertigo and remains a controversial, hard-to-prove diagnosis."),
physiology=(
"**Window membranes**: the round window membrane and the annular ligament of the oval window are the thin barriers between perilymph and the middle-ear air space. "
"**Perilymph continuity**: perilymph connects with CSF through the cochlear aqueduct."),
pathophysiology=(
"**Implosive pathway**: sudden middle-ear pressure increase (Valsalva against a closed nose, airplane descent, diving) pushes the windows inward and ruptures them. "
"**Explosive pathway**: sudden CSF pressure increase (straining, lifting) is transmitted through the cochlear aqueduct, blowing the window out. "
"**Fluid loss effects**: loss of perilymph and air entry alter inner-ear mechanics and hair-cell function, causing SNHL, tinnitus, and imbalance. "
"**Pressure sensitivity**: changes in middle-ear pressure move fluid through the leak, producing a positive fistula test or Hennebert sign. "
"**Diagnosis difficulty**: no reliable noninvasive test exists; exploration and window patching are both diagnostic and therapeutic, and spontaneous closure occurs."),
),

"Cochlear Implant Failure / Revision": dict(
overview=(
"Cochlear implant failure is any loss of benefit requiring evaluation and possible reimplantation, from hard device failure to soft failure, migration, infection, or extrusion. "
"Knowing the categories guides the workup and reimplantation decision."),
physiology=(
"**Device components**: an internal receiver-stimulator in a bony well and an electrode array in the scala tympani, linked to an external processor. "
"**Neural interface**: stable impedances and thresholds reflect the electrode-tissue interface over time."),
pathophysiology=(
"**Hard failure**: a demonstrable device malfunction (lost communication, short or open circuits) from trauma or component failure. "
"**Soft failure**: declining performance, unpleasant sensations, or facial stimulation with normal integrity testing, diagnosed after excluding programming and medical causes. "
"**Electrode migration or extrusion**: array movement out of the cochlea from fibrosis, growth in children, or poor fixation. "
"**Biofilm infection**: implanted material supports biofilm, so infections may require explantation. "
"**Skin flap breakdown**: thin flaps, pressure, or excessive magnet strength cause ischemia and extrusion. "
"**Reimplantation**: usually restores performance, but ossification or fibrosis along the old array tract can complicate insertion."),
),

"Congenital Inner-Ear Malformations": dict(
overview=(
"Congenital inner-ear malformations are developmental anomalies of the labyrinth, from complete aplasia to enlarged vestibular aqueduct, that cause congenital or progressive SNHL. "
"Classification matters for cochlear implant planning, gusher risk, and counseling."),
physiology=(
"**Development**: the otic placode becomes the otocyst around week 4; the cochlea reaches two and a half turns by about week 10. "
"**Timing logic**: earlier developmental arrest produces more severe malformations. "
"**Vestibular aqueduct**: contains the endolymphatic duct connecting the inner ear to the endolymphatic sac; it is called enlarged at 1.5 mm or more at the midpoint (Valvassori), or more than 1 mm at the midpoint or 2 mm or more at the operculum (Cincinnati criteria)."),
pathophysiology=(
"**Michel aplasia**: complete absence of inner-ear structures; implantation is contraindicated. "
"**Common cavity and cochlear aplasia**: very early arrest, often with abnormal nerve. "
"**Incomplete partition I**: cystic cochlea without a modiolus, high gusher risk. "
"**Incomplete partition II (Mondini)**: basal turn normal but apical turns fused, with enlarged vestibular aqueduct; often associated with SLC26A4/Pendred syndrome. "
"**Incomplete partition III**: X-linked, cochlea lacks a modiolus and communicates widely with the IAC, causing severe gushers. "
"**Enlarged vestibular aqueduct**: transmits CSF pressure fluctuations, so minor head trauma can cause stepwise SNHL drops; contact sports counseling matters. "
"**Cochlear nerve deficiency**: a small or absent nerve (narrow IAC) predicts poor implant outcome."),
),

"Auditory Neuroanatomy / Cochlear Physiology": dict(
overview=(
"Understanding how the cochlea converts sound into neural code and how that code ascends the brainstem explains every audiometric pattern and auditory test. "
"It is the foundation for audiology, electrophysiology, implants, and hearing-loss mechanisms."),
physiology=(
"**Traveling wave**: stapes motion creates a wave along the basilar membrane that peaks at a frequency-specific place, high frequencies at the base and low at the apex. "
"**Outer hair cells**: their electromotility (prestin) amplifies basilar-membrane motion by about 40-60 dB and sharpens tuning; their byproduct is otoacoustic emissions. "
"**Inner hair cells**: the true sensory cells; stereocilia deflection opens mechanotransduction channels, potassium flows in from endolymph, and glutamate is released onto spiral ganglion neurons. "
"**Endocochlear potential**: about +80 mV generated by the stria vascularis, creating a large driving force for transduction. "
"**Ascending pathway (ABR waves)**: auditory nerve (I and II), cochlear nucleus (III), superior olivary complex (IV), lateral lemniscus (V; any inferior colliculus contribution is debated), then medial geniculate and auditory cortex. "
"**Binaural processing**: the superior olive compares timing and level between ears for localization."),
pathophysiology=(
"**OHC loss**: removes the amplifier, raising thresholds by about 40-60 dB, broadening tuning, and eliminating OAEs. "
"**IHC or synapse loss**: causes worse clarity and difficulty in noise beyond what thresholds show. "
"**Strial failure**: lowers the endocochlear potential across all frequencies, producing a flat loss. "
"**Retrocochlear lesion**: preserves OAEs but distorts or delays neural responses (prolonged ABR latencies, poor word recognition). "
"**Recruitment**: OHC loss removes compressive amplification, so loudness grows abnormally fast above threshold."),
),

"Audiologic Electrophysiology / ABR-OAE-ECoG": dict(
overview=(
"Electrophysiologic and objective tests (ABR, OAEs, ECoG) measure the auditory system without a behavioral response. "
"They are essential for newborn screening, infants, nonorganic loss, auditory neuropathy, retrocochlear screening, and Ménière evaluation."),
physiology=(
"**OAEs**: sounds produced by active outer-hair-cell motion and recorded in the canal; present OAEs mean outer hair cells and the middle ear are functional. "
"**ABR**: averaged neural responses to clicks or tone bursts in the first 10 ms, waves I-V from nerve to midbrain. "
"**Latency and threshold**: wave V threshold estimates hearing threshold; interpeak latencies reflect neural conduction. "
"**ECoG**: records the summating potential (hair-cell receptor response) and action potential (compound nerve response) near the cochlea."),
pathophysiology=(
"**Conductive loss**: delays all ABR waves equally and may abolish OAEs (middle-ear blockage). "
"**Cochlear loss**: abolishes OAEs and raises ABR thresholds with normal interpeak intervals. "
"**Retrocochlear lesions**: prolong the I-V interpeak interval or the interaural wave V difference (more than 0.2 ms). "
"**ANSD**: present OAEs or cochlear microphonic with absent or abnormal ABR, showing intact outer hair cells but dyssynchronous neural firing. "
"**Ménière disease**: hydrops increases the summating potential relative to the action potential, giving an elevated SP/AP ratio on ECoG. "
"**Newborn screening**: OAEs miss ANSD, so NICU infants are screened with automated ABR."),
),

"Cortical Neuroplasticity in Hearing Loss": dict(
overview=(
"The auditory cortex reorganizes in response to deprivation and restored input. "
"This explains critical periods for implantation in children, why long-deafened adults do worse with implants, and why tinnitus and hyperacusis develop."),
physiology=(
"**Experience-dependent development**: auditory cortex circuits mature in response to sound, with a sensitive period in the first few years of life. "
"**Cross-modal plasticity**: unused auditory cortex can be recruited by visual and somatosensory input. "
"**Adult plasticity**: the adult brain still reorganizes, though more slowly, which underlies auditory training."),
pathophysiology=(
"**Congenital deafness**: without sound input, auditory cortex fails to mature (delayed P1 latency of cortical evoked potentials) and is recruited by vision. "
"**Critical period**: implantation before about 3.5 years produces normal cortical maturation; after about 7 years, outcomes decline. "
"**Adult deprivation**: long-duration deafness leads to central reorganization, reducing implant benefit. "
"**Maladaptive plasticity**: increased central gain after peripheral loss underlies tinnitus and hyperacusis. "
"**Single-sided deafness in children**: reorganizes toward the hearing ear, reducing binaural processing, which supports early intervention."),
),

"Otologic Manifestations of Systemic Disease": dict(
overview=(
"Many systemic diseases first present in the ear, including vasculitis, granulomatous disease, autoimmune and metabolic disorders, infection, and malignancy. "
"Recognizing unusual patterns (bilateral, rapidly progressive, granulation, cranial neuropathy) prevents missed diagnoses."),
physiology=(
"**Shared tissues**: middle-ear mucosa resembles respiratory mucosa, so diseases of the airway (GPA, sarcoid) can involve it. "
"**Inner-ear vascular and immune targets**: the stria vascularis and labyrinthine vasculature are vulnerable to vasculitis and immune complexes. "
"**Bone metabolism**: the otic capsule responds to systemic bone disorders."),
pathophysiology=(
"**GPA**: granulomatous vasculitis causes serous otitis, refractory granulation, conductive and sensorineural loss, and facial palsy. "
"**Relapsing polychondritis**: autoimmune attack on cartilage spares the cartilage-free lobule and can cause SNHL and vertigo. "
"**Cogan syndrome**: interstitial keratitis with audiovestibular dysfunction from autoimmune vasculitis. "
"**Paget disease and osteogenesis imperfecta**: disordered bone remodeling causes conductive and sensorineural loss. "
"**Sickle cell, diabetes, renal failure**: microvascular and metabolic injury to the cochlea. "
"**Langerhans cell histiocytosis, leukemia, metastasis**: infiltrate the temporal bone, mimicking mastoiditis or chronic otitis. "
"**Infection**: syphilis and tuberculosis cause otitis or inner-ear disease that responds to specific therapy."),
),

"Hyperacusis / Decreased Sound Tolerance": dict(
overview=(
"Hyperacusis is reduced tolerance to ordinary sound levels, often with pain or fear of sound, and frequently coexists with tinnitus. "
"It is a central gain disorder treated with sound therapy and counseling rather than ear protection overuse."),
physiology=(
"**Loudness growth**: normal loudness rises predictably with sound intensity, with discomfort near 90-100 dB HL. "
"**Central gain control**: the auditory system tunes sensitivity to the input level. "
"**Efferent control**: olivocochlear and middle-ear reflexes modulate input."),
pathophysiology=(
"**Increased central gain**: after cochlear injury, central neurons become hyperresponsive, so moderate sounds feel loud. "
"**Overprotection**: constant earplug use reduces input further, increasing gain and worsening sensitivity. "
"**Pain hyperacusis**: a research hypothesis (not in the core texts) is that type II cochlear afferents, which respond to tissue-damaging noise, and inflammatory pathways mediate sound-induced pain. "
"**Associated conditions**: Bell palsy (loss of stapedius reflex), SCD, migraine, autism, Williams syndrome, and noise exposure. "
"**Treatment logic**: gradual sound enrichment lowers central gain, and CBT reduces the threat response."),
),

"Labyrinthitis / Infections of the Labyrinth": dict(
overview=(
"Labyrinthitis is inflammation of the inner ear that causes vertigo with hearing loss. "
"It may be viral, serous (toxic) from adjacent otitis, or suppurative bacterial infection that can destroy the labyrinth and lead to meningitis or ossification."),
physiology=(
"**Barriers**: the round window membrane and annular ligament separate the middle ear from perilymph. "
"**CSF connections**: perilymph connects with CSF through the cochlear aqueduct and the IAC fundus. "
"**Combined end organs**: the labyrinth contains both cochlear and vestibular sensory epithelium."),
pathophysiology=(
"**Viral labyrinthitis**: like vestibular neuritis but involving the cochlea, producing acute vertigo plus SNHL. "
"**Serous labyrinthitis**: bacterial toxins and inflammatory mediators diffuse through the round window from otitis media, causing hair-cell dysfunction that is often, but not always, reversible. "
"**Suppurative labyrinthitis**: bacteria enter the labyrinth (from otitis, cholesteatoma fistula, or meningitis), destroying hair cells and producing permanent anacusis. "
"**Meningogenic spread**: bacterial meningitis enters through the cochlear aqueduct or IAC, typically bilaterally. "
"**Labyrinthitis ossificans**: inflammation triggers fibrosis then new bone formation within weeks to months, which is why early cochlear implantation is pursued after meningitis-related deafness."),
),

"Central Vestibular Disorders": dict(
overview=(
"Central vestibular disorders arise in the brainstem, cerebellum, or cortex: stroke, demyelination, tumors, degenerative and migrainous disease. "
"The essential otolaryngology skill is recognizing central signs so that stroke is not sent home as vestibular neuritis."),
physiology=(
"**Vestibular nuclei**: integrate canal and otolith input and connect to the oculomotor nuclei, cerebellum, thalamus, and spinal cord. "
"**Cerebellar flocculus and nodulus**: calibrate the VOR, hold gaze, and suppress nystagmus with fixation. "
"**Blood supply**: the posterior circulation (vertebrobasilar, PICA, AICA) supplies the brainstem, cerebellum, and labyrinth."),
pathophysiology=(
"**Stroke**: PICA infarcts cause vertigo with ataxia and often no hearing loss; AICA infarcts can cause vertigo plus SNHL because AICA supplies the labyrinth. "
"**HINTS logic**: a normal head impulse in acute vertigo, direction-changing nystagmus, or vertical skew indicates a central lesion. "
"**Gaze-holding failure**: cerebellar injury causes direction-changing gaze-evoked nystagmus. "
"**Fixation**: central nystagmus does not suppress with visual fixation, whereas peripheral nystagmus does. "
"**Pure vertical or torsional nystagmus**: downbeat (cervicomedullary or cerebellar) and upbeat nystagmus are central. "
"**Truncal ataxia**: inability to sit or stand unaided out of proportion to vertigo suggests cerebellar involvement."),
),

"Vestibular Rehabilitation": dict(
overview=(
"Vestibular rehabilitation is exercise-based therapy that promotes central compensation, substitution, and habituation after vestibular injury. "
"It is first-line for uncompensated unilateral or bilateral loss, PPPD, and chronic dizziness."),
physiology=(
"**Adaptation**: the cerebellum adjusts VOR gain when retinal slip (image motion during head movement) signals an error. "
"**Substitution**: vision, proprioception, and alternative eye-movement strategies replace lost vestibular function. "
"**Habituation**: repeated exposure to provocative stimuli reduces the central response."),
pathophysiology=(
"**Uncompensated loss**: persistent asymmetry between vestibular nuclei causes dizziness with head movement and oscillopsia. "
"**Avoidance prevents recovery**: limiting head movement removes the error signal needed for adaptation, prolonging symptoms. "
"**Vestibular suppressants**: prolonged use of meclizine or benzodiazepines blunts central compensation, so they should be limited to the acute phase. "
"**Bilateral loss**: little to adapt, so therapy relies on substitution and fall prevention. "
"**Exercise logic**: gaze stabilization (head movement while fixating a target) drives adaptation; balance and gait training builds substitution."),
),

"Neurotologic Intraoperative Cranial-Nerve Monitoring": dict(
overview=(
"Intraoperative cranial nerve monitoring (facial EMG, ABR and cochlear nerve action potentials, lower cranial nerves) helps identify nerves and predict function during otologic and skull-base surgery. "
"It supplements anatomic knowledge; it does not replace it."),
physiology=(
"**Facial EMG**: needle electrodes in the orbicularis oculi and oris record motor responses to mechanical or electrical stimulation. "
"**Threshold**: a proximal nerve that responds to low stimulation (e.g., 0.05-0.1 mA) at the end of surgery predicts good function. "
"**Hearing monitoring**: ABR and direct cochlear nerve action potentials track auditory function during hearing-preservation surgery. "
"**Anesthesia**: neuromuscular blockade abolishes EMG responses, so it must be avoided after induction."),
pathophysiology=(
"**Mechanical irritation**: traction or manipulation produces spontaneous EMG activity (bursts and trains); sustained trains warn of injury. "
"**Thermal injury**: drill heat and cautery can injure nerves without immediate EMG warning. "
"**Proximal-to-distal ratio**: a rising proximal threshold indicates conduction block at the dissection site. "
"**False reassurance**: a stimulator response proves only conduction distal to the stimulation point, not that the nerve is uninjured proximally. "
"**ABR changes**: wave V latency prolongation or amplitude loss during dissection signals cochlear nerve or vascular compromise."),
),

"Lateral Skull-Base Tumor Framework": dict(
overview=(
"Lateral skull-base tumors (vestibular schwannoma, meningioma, paraganglioma, epidermoid, chondrosarcoma, and others) are managed by matching tumor biology, location, and hearing status to observation, radiation, or a surgical approach. "
"The framework is a decision tool built on anatomy and natural history."),
physiology=(
"**Key compartments**: IAC and CPA, jugular foramen, petrous apex, middle fossa floor, and infratemporal fossa. "
"**Approach anatomy**: translabyrinthine (sacrifices hearing, wide CPA access), retrosigmoid (hearing preservation, posterior fossa), middle fossa (small intracanalicular tumors, hearing preservation), and infratemporal fossa (jugular foramen). "
"**Neighbors**: CN VII and VIII, lower cranial nerves IX-XII, carotid, jugular bulb, sigmoid sinus, and brainstem."),
pathophysiology=(
"**Tumor biology drives timing**: many schwannomas and meningiomas grow slowly, so observation with serial MRI is valid; malignant or rapidly growing tumors need treatment. "
"**Imaging signatures**: schwannoma (enhances, centered on the IAC, acute angle), meningioma (broad dural base, dural tail, obtuse angle, hyperostosis), epidermoid (restricted diffusion, no enhancement), paraganglioma (salt-and-pepper, flow voids). "
"**Approach selection**: depends on hearing status, tumor size and location, and patient factors. "
"**Radiation logic**: stereotactic radiosurgery arrests growth in most small-to-medium tumors, but does not remove them and complicates later surgery. "
"**Cranial nerve outcomes**: lower cranial nerve deficits with jugular foramen tumors are poorly tolerated, which favors subtotal resection or radiation."),
),

"External Auditory Canal Cholesteatoma": dict(
overview=(
"EAC cholesteatoma is keratinizing squamous epithelium invading the bony canal wall, usually the floor, causing focal bone erosion. "
"It differs from keratosis obturans and is treated with debridement or canalplasty."),
physiology=(
"**Bony canal skin**: thin (about 0.2 mm), without adnexa, and bound directly to periosteum, so it has little reserve when its blood supply is injured. "
"**Self-cleaning**: epithelium migrates from the tympanic membrane laterally along the canal, carrying keratin out; disease appears wherever that conveyor belt fails. "
"**Blood supply**: the bony canal wall depends on periosteal vessels, and the inferior and posterior walls are the most exposed to minor trauma and ischemia. "
"**Canal relationships**: the mastoid lies posterior, the TMJ anterior, and the facial nerve deep to the posterior-inferior canal wall."),
pathophysiology=(
"**Focal periostitis**: local injury or ischemia of the inferior/posterior canal wall allows squamous epithelium to invade bone. "
"**Unilateral and older patients**: typically presents with dull chronic otalgia and otorrhea, with normal hearing. "
"**Bone sequestrum**: erosion creates a pocket containing keratin and necrotic bone. "
"**Spread**: rarely erodes into the mastoid, facial canal, or temporomandibular joint. "
"**Contrast with keratosis obturans**: keratosis obturans is a dense keratin plug from abnormal migration, usually bilateral, causing acute pain and conductive loss with smooth circumferential widening rather than focal erosion."),
),

"Keratosis Obturans": dict(
overview=(
"Keratosis obturans is accumulation of a dense keratin plug in the bony canal from failed epithelial migration. "
"It causes acute pain and conductive loss and is associated with bronchiectasis and sinusitis in younger patients."),
physiology=(
"**Epithelial migration**: canal epithelium normally migrates centrifugally from the drum and laterally along the canal, clearing keratin without help. "
"**Bony canal**: tightly adherent periosteal skin without glands or hair, so keratin there can only leave by migration. "
"**Cerumen**: produced only in the lateral cartilaginous canal; it lubricates and carries debris outward. "
"**Failed migration**: the core defect is failure of normal lateral epithelial migration, so keratin accumulates as a dense plug."),
pathophysiology=(
"**Migration failure**: abnormal epithelial migration lets keratin layers accumulate in an onion-skin plug. "
"**Pressure effects**: the plug causes circumferential widening of the bony canal, acute severe pain, and conductive hearing loss. "
"**Bilateral pattern**: it is often bilateral and may be associated with respiratory conditions such as bronchiectasis and chronic sinusitis; the mechanism is unknown. "
"**Management logic**: regular debridement and keeping the ear dry, since the migration defect persists."),
),

"EAC Exostoses / Osteoma (Canalplasty)": dict(
overview=(
"Exostoses are broad-based, often multiple bony growths of the EAC from cold-water exposure; osteomas are solitary pedunculated benign bone tumors. "
"They cause trapped keratin, recurrent otitis externa, and conductive loss when obstructive, and are treated with canalplasty."),
physiology=(
"**Bony canal periosteum**: thin skin directly over bone; the periosteum responds to repeated cold stimuli by laying down new bone. "
"**Sutures**: the tympanosquamous suture (anterosuperior) and tympanomastoid suture (posteroinferior) are landmarks and common origin sites. "
"**Canal clearance**: lateral epithelial migration and a patent lumen allow water and keratin to escape; narrowing defeats both. "
"**Deep relations**: the facial nerve (mastoid segment) lies deep to the posterior canal wall and the drum and annulus lie medially."),
pathophysiology=(
"**Exostoses**: repeated cold-water exposure stimulates periosteal osteoblastic activity, producing broad-based, multiple, usually bilateral lesions medial in the canal (\"surfer's ear\"). "
"**Osteoma**: a benign neoplasm, usually solitary and pedunculated, often lateral at the tympanosquamous suture. "
"**Obstruction effects**: narrowing traps water, keratin, and debris, causing infections and conductive loss once nearly occlusive. "
"**Surgical risk**: the facial nerve lies just deep to the posterior canal wall and the TM medially, so drilling must preserve skin and avoid deep posterior work."),
),

"Ramsay Hunt Syndrome (Herpes Zoster Oticus)": dict(
overview=(
"Ramsay Hunt syndrome is varicella-zoster reactivation in the geniculate ganglion causing facial paralysis, painful vesicular eruption of the ear, and often hearing loss and vertigo. "
"It has a worse prognosis than Bell palsy and is treated with antivirals plus steroids."),
physiology=(
"**Geniculate ganglion**: contains sensory cell bodies of CN VII (nervus intermedius), including general sensation from the concha and posterior canal skin and taste from the anterior two-thirds of the tongue. "
"**Proximity**: CN VII and VIII run together in the IAC, so inflammation can spread between them. "
"**Varicella-zoster latency**: after primary chickenpox, VZV stays latent in sensory ganglia, held in check by cell-mediated immunity. "
"**Narrow canal**: as in Bell palsy, swelling within the bony fallopian canal compresses the nerve."),
pathophysiology=(
"**Reactivation**: latent VZV in the geniculate ganglion reactivates with declining cell-mediated immunity. "
"**Neural inflammation**: inflammation spreads along CN VII and to CN VIII, causing paralysis, SNHL, and vertigo; other cranial nerves may be involved. "
"**Vesicles**: in the sensory distribution of CN VII (concha, canal, auricle) and sometimes the palate or tongue; zoster sine herpete occurs without vesicles. "
"**Worse prognosis**: more extensive neural destruction and degeneration than Bell palsy, so complete recovery is less common. "
"**Treatment logic**: antivirals reduce viral replication and steroids reduce inflammation; vaccination reduces zoster risk."),
),

"Facial Nerve Schwannoma": dict(
overview=(
"Facial nerve schwannoma is a benign Schwann-cell tumor that can arise anywhere along CN VII, most often near the geniculate ganglion. "
"It causes slowly progressive or recurrent facial weakness, and management usually favors observation to preserve function."),
physiology=(
"**Segments**: CPA, IAC, labyrinthine, geniculate, tympanic, mastoid, and extratemporal segments; the geniculate region is the most common tumor site. "
"**Schwann cells**: myelinate the peripheral nerve along its entire length beyond the Obersteiner-Redlich zone. "
"**Nerve tolerance**: motor fibers tolerate slow compression with preserved function, so a large tumor can coexist with a normal face. "
"**Bony expansion**: the fallopian canal and geniculate fossa remodel around slow-growing lesions, which CT shows as smooth enlargement."),
pathophysiology=(
"**Slow growth**: tumors grow slowly, and facial function may remain normal until late. "
"**Presentation by location**: geniculate tumors cause facial weakness; IAC and CPA tumors mimic vestibular schwannoma; tympanic segment tumors cause conductive loss. "
"**Imaging clue**: a tubular enhancing mass following multiple segments of the facial nerve, with geniculate fossa enlargement on CT. "
"**Treatment logic**: resection usually requires nerve sacrifice and grafting, with outcomes no better than House-Brackmann III, so observation or decompression is favored until function deteriorates."),
),

"Auditory Neuropathy Spectrum Disorder": dict(
overview=(
"ANSD is hearing loss with normal outer-hair-cell function (present OAEs or cochlear microphonic) but abnormal or absent ABR, reflecting dyssynchronous neural transmission. "
"It is common in NICU graduates, and its speech outcomes can be worse than thresholds suggest."),
physiology=(
"**Synchrony**: speech perception depends on precisely timed, phase-locked firing of many auditory nerve fibers. "
"**Outer vs inner hair cells**: outer hair cells amplify (and generate OAEs and the cochlear microphonic), while inner hair cells release glutamate onto the auditory nerve. "
"**Ribbon synapse**: specialized inner hair cell synapses (requiring otoferlin) release transmitter quickly and precisely. "
"**Lesion sites**: inner hair cells, ribbon synapses, or the auditory nerve itself, each preserving outer-hair-cell function."),
pathophysiology=(
"**Dyssynchrony**: neural impulses are poorly timed, so the ABR (which needs synchronous firing) is absent while OAEs are preserved. "
"**Causes**: prematurity, hyperbilirubinemia, hypoxia, genetic mutations (OTOF), and cochlear nerve deficiency. "
"**Disproportionate speech deficit**: poor timing degrades speech understanding, especially in noise, beyond what audiogram thresholds predict. "
"**Treatment logic**: hearing aids help some children, while cochlear implants often succeed when the lesion is presynaptic (e.g., OTOF), restoring synchrony through electrical stimulation."),
),

"Vernet Syndrome (Jugular Foramen Syndrome)": dict(
overview=(
"Vernet syndrome is paralysis of CN IX, X, and XI from a lesion at the jugular foramen. "
"It is a localizing pattern pointing to paraganglioma, schwannoma, meningioma, metastasis, or skull-base infection."),
physiology=(
"**Jugular foramen contents**: the pars nervosa holds CN IX and the inferior petrosal sinus; the pars vascularis holds CN X, CN XI, and the jugular bulb. "
"**Functions**: CN IX (posterior tongue taste, pharyngeal sensation), CN X (palate, pharynx, larynx), CN XI (SCM and trapezius)."),
pathophysiology=(
"**Combined palsy**: dysphagia, hoarseness from vocal fold paralysis, loss of gag, palatal deviation toward the healthy side, and shoulder weakness. "
"**Extension**: involvement of CN XII via the hypoglossal canal produces Collet-Sicard syndrome; involvement of sympathetics (retroparotid) produces Villaret syndrome. "
"**Lower cranial nerve tolerance**: sudden loss causes severe aspiration, while slow tumor growth allows compensation, which shapes treatment choices."),
),

"Gradenigo Syndrome (Petrous Apicitis)": dict(
overview=(
"Gradenigo syndrome is the triad of otorrhea, retro-orbital pain, and abducens palsy from petrous apex infection. "
"It is a complication of otitis media or mastoiditis requiring imaging, antibiotics, and drainage."),
physiology=(
"**Petrous apex**: medial temporal bone, pneumatized in about a third of people. "
"**Dorello canal**: CN VI passes under the petroclinoid ligament adjacent to the apex. "
"**Meckel cave**: the trigeminal ganglion lies over the apex."),
pathophysiology=(
"**Spread**: infection extends from the middle ear and mastoid through air cell tracts into the pneumatized apex. "
"**CN VI palsy**: inflammation compresses or irritates the abducens nerve in Dorello canal, causing lateral rectus weakness and diplopia. "
"**Retro-orbital pain**: inflammation of the trigeminal ganglion or dura. "
"**Further spread**: meningitis, cavernous sinus thrombosis, and carotid involvement."),
),

"Glomus Tumor / Paraganglioma": dict(
overview=(
"Temporal bone paragangliomas (glomus tympanicum and glomus jugulare) are vascular neuroendocrine tumors that cause pulsatile tinnitus, conductive loss, and lower cranial nerve deficits. "
"Their genetics, vascularity, and location guide workup and treatment."),
physiology=(
"**Paraganglia**: neural crest-derived chemoreceptor cells along Jacobson (CN IX) and Arnold (CN X) nerves and the jugular bulb adventitia. "
"**Vascular supply**: mainly the ascending pharyngeal artery (inferior tympanic branch)."),
pathophysiology=(
"**Hypervascular tumor**: rich vascularity produces pulsatile tinnitus and a red retrotympanic mass that blanches with pressure (Brown sign). "
"**Glomus tympanicum**: confined to the promontory, causing conductive loss. "
"**Glomus jugulare**: grows from the jugular bulb, eroding the jugular foramen and involving CN IX-XI (Vernet). "
"**Genetics**: succinate dehydrogenase (SDHx) mutations cause hereditary, multifocal tumors, so genetic testing is recommended. "
"**Catecholamines**: a minority secrete catecholamines, which must be screened before surgery. "
"**Imaging**: salt-and-pepper MRI appearance from flow voids and moth-eaten bone erosion on CT."),
),
}
