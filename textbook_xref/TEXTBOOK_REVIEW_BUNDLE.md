# ENT Mastery v47 textbook review bundle

Contents: 356 topics, 310 concept checks.
Reviewer instructions:
- Check every factual statement below against Cummings 7e, Pasha & Golub 6e, K.J. Lee 12e, and (pediatric) Bluestone & Stool 5e.
- Item IDs: `T-<domain>-<n>.<field>` for topic text (field = overview / physiology / pathophysiology) and `CC-<domain>-<n>.<k>` for concept checks.
- Return results as `textbook_xref/corrections.csv` with columns:
  `item_id, verdict (OK|CORRECT|UNSUPPORTED|CONFLICT), quoted_claim, book, edition_chapter, printed_page, book_text_excerpt (<=40 words), suggested_fix`
- Only rows that need action are required; one OK row per topic with its best citation is enough to add the source.
- `CONFLICT` = books disagree with each other; quote both. `UNSUPPORTED` = none of the four books covers it.
- Do not edit the Python files; corrections.csv will be applied in the repo.


---

# Otology / Neurotology

## T-otology-1 — Acute Mastoiditis / Petrous Apicitis
_source: pathophys_v470/otology_b.py_

**T-otology-1.overview**

Acute mastoiditis is spread of acute otitis media into the mastoid air cells, sometimes with bone destruction (coalescence) and subperiosteal abscess. It is most common in young children and can spread to intracranial, neck, and petrous apex compartments.

**T-otology-1.physiology**

**Continuity**: the mastoid air cells connect to the middle ear through the aditus ad antrum, so middle-ear infection always involves mastoid mucosa to some degree. **Bony septations**: thin septa divide air cells; the cortex overlying the antrum is thin in children (Macewen triangle). **Venous connections**: emissary veins connect the mastoid to the sigmoid sinus.

**T-otology-1.pathophysiology**

**Obstruction**: mucosal swelling at the aditus traps pus in the mastoid under pressure. **Coalescence**: inflammation and pressure cause osteitis and resorption of the septa, forming an abscess cavity. **Subperiosteal abscess**: pus erodes through the lateral cortex, pushing the pinna forward and outward (postauricular swelling and erythema). **Other paths**: Bezold abscess (through the tip into the SCM sheath), petrous apicitis (Gradenigo triad), sigmoid sinus thrombosis via emissary veins, epidural or brain abscess via the tegmen, meningitis, and facial palsy. **Why tubes and mastoidectomy**: myringotomy drains the middle ear and gives culture; mastoidectomy is needed when coalescent disease, abscess, or complications do not resolve with antibiotics.

### CC-otology-1.1 (concept check)

Stem: A 3-year-old with AOM develops postauricular swelling that pushes the pinna forward and outward. CT shows coalescence and a subperiosteal collection. What produced the collection?

- **Correct:** Pus eroding through the mastoid cortex
- Distractor: Suppuration of postauricular nodes — _why wrong:_ Reactive nodes can mimic mastoiditis but do not explain coalescence on CT.
- Distractor: Spread down the Eustachian tube — _why wrong:_ The tube connects to the nasopharynx; the collection is lateral to the mastoid.
- Distractor: Thrombosis of the sigmoid sinus — _why wrong:_ Sinus thrombosis is a separate intracranial complication.

Explanation: Aditus obstruction traps pus; osteitis and pressure cause coalescence, and pus breaks through the thin cortex over the antrum. Treatment is IV antibiotics plus myringotomy with tube and drainage or mastoidectomy.

Pearl: Postauricular swelling pushing the ear forward = subperiosteal abscess until proven otherwise.

## T-otology-2 — Acute Otitis Externa
_source: pathophys_v470/otology_a.py_

**T-otology-2.overview**

Acute otitis externa (AOE) is diffuse bacterial cellulitis of the external auditory canal skin, usually Pseudomonas aeruginosa or Staphylococcus aureus. It matters because it is among the most common ear complaints, it is treated topically, and its look-alike in a diabetic or immunocompromised patient (necrotizing otitis externa) is a skull-base osteomyelitis.

**T-otology-2.physiology**

**Canal structure**: the canal is about 2.5 cm long; the lateral one-third is cartilaginous and the medial two-thirds is bony. **Lateral canal skin**: it is thick and carries hair follicles plus ceruminous and sebaceous glands. **Medial canal skin**: over bone it is thin, tightly bound to periosteum, and has no adnexa, which is why swelling there is so painful. **Cerumen is a barrier**: it is hydrophobic, mildly acidic (pH about 6), and contains lysozyme and long-chain fatty acids that inhibit bacterial growth. **Self-cleaning**: canal epithelium migrates outward from the tympanic membrane at roughly 0.05 mm per day, carrying keratin and cerumen laterally. **Innervation**: sensory supply comes from V3 (auriculotemporal), CN X (Arnold nerve), CN VII and the great auricular nerve, which explains referred otalgia and the cough reflex with canal instrumentation.

**T-otology-2.pathophysiology**

**Barrier breakdown starts it**: water exposure ("swimmer's ear"), cotton swabs, hearing-aid occlusion, or dermatitis remove cerumen and raise canal pH. **Maceration**: moist, alkaline skin loses its acid mantle and stratum corneum integrity, letting Pseudomonas or Staphylococcus invade. **Edema and pain**: inflammation of skin bound tightly to periosteum produces pain out of proportion to the visible findings, and tragal or pinna traction stretches the inflamed skin. **Canal occlusion**: edema narrows the lumen, causing conductive hearing loss and blocking drops from reaching the medial canal (the reason for a wick). **Spread**: cellulitis can extend to the pinna and periauricular tissues; in a diabetic or immunocompromised host, extension through the fissures of Santorini toward the skull base marks necrotizing otitis externa. **Why topical therapy wins**: drops deliver antibiotic concentrations hundreds of times higher than systemic therapy directly to the infected skin, so oral antibiotics add little unless infection extends beyond the canal.

### CC-otology-2.1 (concept check)

Stem: A 22-year-old swimmer has 3 days of severe otalgia, pain with tragal pressure, and a swollen, debris-filled canal; the drum cannot be seen. He is not diabetic and has no cranial neuropathy. Why are topical drops preferred over oral antibiotics?

- **Correct:** They reach far higher drug levels in canal skin
- Distractor: Oral agents do not cover Pseudomonas aeruginosa — _why wrong:_ Oral fluoroquinolones do cover Pseudomonas; the advantage of drops is delivery, not spectrum.
- Distractor: They prevent progression to skull-base osteomyelitis — _why wrong:_ Necrotizing otitis externa depends on host factors such as diabetes; drops do not specifically prevent it.
- Distractor: Systemic therapy is unsafe when the drum is not seen — _why wrong:_ An unseen drum changes the choice of drop (non-ototoxic), not whether systemic therapy is allowed.

Explanation: Uncomplicated AOE is cellulitis of canal skin. Drops reach concentrations hundreds of times higher than oral dosing at the infection site; a wick is added when edema blocks delivery. Systemic therapy is reserved for spread beyond the canal or a high-risk host.

Pearl: AOE: clean it, drop it, wick it if swollen; go systemic only for spread or a vulnerable host.

## T-otology-3 — Age-Related Hearing Loss / Presbycusis
_source: pathophys_v470/otology_b.py_

**T-otology-3.overview**

Presbycusis is gradual, bilateral, symmetric, high-frequency sensorineural loss with aging. It is the most common cause of hearing loss in adults, is linked to cognitive decline and social isolation, and is managed with amplification and communication strategies.

**T-otology-3.physiology**

**Base-to-apex vulnerability**: high-frequency basal hair cells are exposed to more cumulative mechanical and metabolic stress. **Stria vascularis**: generates the endocochlear potential, the battery of the cochlea, and depends on rich microvasculature. **Central processing**: understanding speech in noise depends on temporal processing and cognition, not just thresholds.

**T-otology-3.pathophysiology**

**Sensory (hair cell) type**: basal outer hair-cell loss produces a steep high-frequency slope. **Strial (metabolic) type**: atrophy of the stria reduces the endocochlear potential across the cochlea, producing a flat loss with relatively good word recognition. **Neural type**: loss of spiral ganglion neurons and synapses produces word recognition worse than expected from thresholds. **Cumulative contributors**: noise exposure, genetics, vascular disease, diabetes, smoking, and ototoxic medications add to aging changes. **Speech-in-noise difficulty**: high-frequency consonant information is lost first, and central temporal processing declines, so patients say they hear but do not understand. **Cognitive link**: reduced auditory input increases listening effort and may reduce cognitive reserve; treating hearing loss may slow cognitive decline in at-risk older adults.

### CC-otology-3.1 (concept check)

Stem: A 78-year-old has a flat, moderate bilateral sensorineural loss with surprisingly good word recognition. Which presbycusis type best fits?

- **Correct:** Strial presbycusis
- Distractor: Sensory presbycusis — _why wrong:_ Sensory presbycusis from basal outer hair cell loss produces a steep high-frequency slope.
- Distractor: Neural presbycusis — _why wrong:_ Neural loss causes word recognition worse than thresholds predict.
- Distractor: Conductive presbycusis — _why wrong:_ The loss is sensorineural, not conductive.

Explanation: The stria vascularis generates the endocochlear potential for the whole cochlea, so strial atrophy produces a flat loss while hair cells and neurons function, preserving clarity.

Pearl: Shape tells the site: steep slope sensory, flat strial, poor clarity neural.

## T-otology-4 — Audiogram Interpretation
_source: pathophys_v470/otology_a.py_

**T-otology-4.overview**

The pure-tone audiogram, with speech testing, is the foundational test in otology: it classifies hearing loss as conductive, sensorineural, or mixed, and grades severity. Every downstream decision (imaging, surgery, amplification, implantation) starts from reading it correctly, including masking.

**T-otology-4.physiology**

**Air conduction**: sound through headphones tests the whole pathway: outer ear, middle ear, cochlea, and nerve. **Bone conduction**: a vibrator on the mastoid stimulates the cochlea directly, largely bypassing the outer and middle ear. **Air-bone gap**: the difference between air and bone thresholds represents conductive loss; a gap of 10 dB or less is within test variability. **Decibels HL**: 0 dB HL is average normal hearing at each frequency; normal adult thresholds are 25 dB HL or better. **Interaural attenuation**: about 40 dB for supra-aural headphones and essentially 0 dB for bone conduction, so the non-test ear can hear the stimulus (crossover) unless masked. **Speech testing**: the speech reception threshold should agree with the pure-tone average, and word recognition measures clarity, which reflects cochlear and neural function.

**T-otology-4.pathophysiology**

**Conductive pattern**: normal bone conduction with elevated air conduction means sound is blocked before the cochlea (wax, effusion, perforation, fixation, discontinuity). **Sensorineural pattern**: air and bone are equally elevated, meaning the cochlea or nerve is the problem. **Characteristic shapes**: noise injury produces a 4 kHz notch with recovery at 8 kHz; presbycusis is bilateral, symmetric, and high-frequency sloping; Ménière disease classically starts as a fluctuating low-frequency loss. **Retrocochlear warning signs**: asymmetry, unilateral tinnitus, or word recognition disproportionately poor for the pure-tone loss suggest a nerve problem and call for MRI. **Masking dilemma**: with large bilateral conductive losses, masking noise loud enough to cover the non-test ear may itself cross over to the test ear, making thresholds uncertain. **Pseudohypacusis**: thresholds that disagree with the speech reception threshold, absent reflexes, or OAEs suggest a nonorganic loss.

### CC-otology-4.1 (concept check)

Stem: A 40-year-old has right air-conduction thresholds of 50 dB HL with bone conduction of 5 dB HL; the left ear is normal. The right tympanogram is flat with normal canal volume. What is the best interpretation?

- **Correct:** Right conductive loss from middle-ear fluid
- Distractor: Right sensorineural loss with unreliable bone scores — _why wrong:_ Bone conduction at 5 dB HL shows a normal cochlea, so the 45 dB gap is conductive.
- Distractor: Right mixed loss with cochlear involvement — _why wrong:_ A mixed loss requires elevated bone conduction in addition to an air-bone gap.
- Distractor: Normal hearing with a collapsing ear canal — _why wrong:_ A collapsed canal elevates air thresholds but would not produce a flat tympanogram with normal volume.

Explanation: Normal bone conduction with elevated air conduction defines conductive loss. A flat (type B) tympanogram with normal canal volume indicates fluid behind an intact drum.

Pearl: Air-bone gap over 10 dB with normal bone conduction = conductive; tympanometry tells you where.

## T-otology-5 — Audiologic Electrophysiology / ABR-OAE-ECoG
_source: pathophys_v470/otology_b.py_

**T-otology-5.overview**

Electrophysiologic and objective tests (ABR, OAEs, ECoG) measure the auditory system without a behavioral response. They are essential for newborn screening, infants, nonorganic loss, auditory neuropathy, retrocochlear screening, and Ménière evaluation.

**T-otology-5.physiology**

**OAEs**: sounds produced by active outer-hair-cell motion and recorded in the canal; present OAEs mean outer hair cells and the middle ear are functional. **ABR**: averaged neural responses to clicks or tone bursts in the first 10 ms, waves I-V from nerve to midbrain. **Latency and threshold**: wave V threshold estimates hearing threshold; interpeak latencies reflect neural conduction. **ECoG**: records the summating potential (hair-cell receptor response) and action potential (compound nerve response) near the cochlea.

**T-otology-5.pathophysiology**

**Conductive loss**: delays all ABR waves equally and may abolish OAEs (middle-ear blockage). **Cochlear loss**: abolishes OAEs and raises ABR thresholds with normal interpeak intervals. **Retrocochlear lesions**: prolong the I-V interpeak interval or the interaural wave V difference (more than 0.2 ms). **ANSD**: present OAEs or cochlear microphonic with absent or abnormal ABR, showing intact outer hair cells but dyssynchronous neural firing. **Ménière disease**: hydrops increases the summating potential relative to the action potential, giving an elevated SP/AP ratio on ECoG. **Newborn screening**: OAEs miss ANSD, so NICU infants are screened with automated ABR.

### CC-otology-5.1 (concept check)

Stem: A NICU graduate has present otoacoustic emissions but an absent ABR with a visible cochlear microphonic. What is the diagnosis?

- **Correct:** Auditory neuropathy
- Distractor: Middle-ear effusion — _why wrong:_ Effusion abolishes otoacoustic emissions.
- Distractor: Outer hair cell loss — _why wrong:_ Outer hair cell loss abolishes otoacoustic emissions.
- Distractor: Delayed ABR maturation only — _why wrong:_ Immaturity delays ABR waves; it does not abolish them while OAEs are present.

Explanation: Present OAEs and cochlear microphonic show working outer hair cells, while an absent ABR shows dyssynchronous neural firing. NICU graduates are screened with automated ABR because OAE screening misses ANSD.

Pearl: OAE present + ABR absent = ANSD.

## T-otology-6 — Auditory Neuroanatomy / Cochlear Physiology
_source: pathophys_v470/otology_b.py_

**T-otology-6.overview**

Understanding how the cochlea converts sound into neural code and how that code ascends the brainstem explains every audiometric pattern and auditory test. It is the foundation for audiology, electrophysiology, implants, and hearing-loss mechanisms.

**T-otology-6.physiology**

**Traveling wave**: stapes motion creates a wave along the basilar membrane that peaks at a frequency-specific place, high frequencies at the base and low at the apex. **Outer hair cells**: their electromotility (prestin) amplifies basilar-membrane motion by about 40-50 dB and sharpens tuning; their byproduct is otoacoustic emissions. **Inner hair cells**: the true sensory cells; stereocilia deflection opens mechanotransduction channels, potassium flows in from endolymph, and glutamate is released onto spiral ganglion neurons. **Endocochlear potential**: about +80 mV generated by the stria vascularis, creating a large driving force for transduction. **Ascending pathway (ABR waves)**: auditory nerve (I and II), cochlear nucleus (III), superior olivary complex (IV), lateral lemniscus and inferior colliculus (V), then medial geniculate and auditory cortex. **Binaural processing**: the superior olive compares timing and level between ears for localization.

**T-otology-6.pathophysiology**

**OHC loss**: removes the amplifier, raising thresholds by up to about 50 dB, broadening tuning, and eliminating OAEs. **IHC or synapse loss**: causes worse clarity and difficulty in noise beyond what thresholds show. **Strial failure**: lowers the endocochlear potential across all frequencies, producing a flat loss. **Retrocochlear lesion**: preserves OAEs but distorts or delays neural responses (prolonged ABR latencies, poor word recognition). **Recruitment**: OHC loss removes compressive amplification, so loudness grows abnormally fast above threshold.

### CC-otology-6.1 (concept check)

Stem: A drug abolishes outer hair cell electromotility but spares inner hair cells. Which audiologic change is expected?

- **Correct:** Moderate loss, absent OAEs
- Distractor: Complete loss of all hearing — _why wrong:_ Inner hair cells still transduce sound, so hearing is reduced, not absent.
- Distractor: Normal thresholds with an absent ABR — _why wrong:_ That pattern suggests neural dyssynchrony, not outer hair cell loss.
- Distractor: Better hearing in background noise — _why wrong:_ Outer hair cell loss worsens frequency selectivity and hearing in noise.

Explanation: Outer hair cells amplify basilar membrane motion by about 40-50 dB through prestin, sharpen tuning, and generate otoacoustic emissions. Their loss removes the cochlear amplifier.

Pearl: Outer hair cells amplify; inner hair cells transmit.

## T-otology-7 — Auditory Neuropathy Spectrum Disorder
_source: pathophys_v470/otology_b.py_

**T-otology-7.overview**

ANSD is hearing loss with normal outer-hair-cell function (present OAEs or cochlear microphonic) but abnormal or absent ABR, reflecting dyssynchronous neural transmission. It is common in NICU graduates, and its speech outcomes can be worse than thresholds suggest.

**T-otology-7.physiology**

**Synchrony**: speech perception depends on precisely timed, phase-locked firing of many auditory nerve fibers. **Outer vs inner hair cells**: outer hair cells amplify (and generate OAEs and the cochlear microphonic), while inner hair cells release glutamate onto the auditory nerve. **Ribbon synapse**: specialized inner hair cell synapses (requiring otoferlin) release transmitter quickly and precisely. **Lesion sites**: inner hair cells, ribbon synapses, or the auditory nerve itself, each preserving outer-hair-cell function.

**T-otology-7.pathophysiology**

**Dyssynchrony**: neural impulses are poorly timed, so the ABR (which needs synchronous firing) is absent while OAEs are preserved. **Causes**: prematurity, hyperbilirubinemia, hypoxia, genetic mutations (OTOF), and cochlear nerve deficiency. **Disproportionate speech deficit**: poor timing degrades speech understanding, especially in noise, beyond what audiogram thresholds predict. **Treatment logic**: hearing aids help some children, while cochlear implants often succeed when the lesion is presynaptic (e.g., OTOF), restoring synchrony through electrical stimulation.

### CC-otology-7.1 (concept check)

Stem: A 3-year-old with auditory neuropathy from biallelic OTOF mutations gets little benefit from hearing aids. Why might a cochlear implant help?

- **Correct:** It bypasses the defective synapse
- Distractor: It replaces lost outer hair cells — _why wrong:_ Outer hair cells are intact in ANSD.
- Distractor: It improves middle-ear transmission — _why wrong:_ The middle ear is normal.
- Distractor: It treats cortical processing deficits — _why wrong:_ OTOF disease is a synaptic problem, not a cortical one.

Explanation: Otoferlin is required for transmitter release at inner hair cell ribbon synapses. Electrical stimulation of the auditory nerve bypasses the synapse and restores synchronous firing.

Pearl: Presynaptic ANSD responds well to cochlear implants.

## T-otology-8 — Autoimmune Inner Ear Disease
_source: pathophys_v470/otology_a.py_

**T-otology-8.overview**

Autoimmune inner ear disease (AIED) is bilateral, asymmetric sensorineural loss progressing over weeks to months, often with vestibular symptoms, that responds to steroids. It is one of the few treatable causes of progressive SNHL, so recognizing the tempo matters.

**T-otology-8.physiology**

**Immune privilege**: the inner ear has a blood-labyrinth barrier, but the endolymphatic sac contains immune-competent cells and acts as its immunologic organ. **Stria vascularis**: its vascular structure is a likely target for immune complex deposition and vasculitis. **Steroid responsiveness**: glucocorticoid receptors are present in cochlear tissues, and steroids reduce inflammation there.

**T-otology-8.pathophysiology**

**Immune-mediated injury**: autoantibodies and T cells target inner-ear antigens (e.g., heat shock protein 70 has been studied), with immune complex deposition and inflammation. **Tempo is the clue**: faster than presbycusis and slower than sudden loss, typically progressing over weeks to months and often bilaterally. **Primary vs secondary**: about a third is associated with systemic autoimmune disease such as granulomatosis with polyangiitis, lupus, Cogan syndrome, rheumatoid arthritis, or relapsing polychondritis. **Vestibular involvement**: similar immune injury of the vestibular end organs causes imbalance or episodic vertigo, overlapping with bilateral Ménière disease. **Steroid response as diagnosis**: improvement with high-dose corticosteroids supports the diagnosis; steroid-sparing agents (methotrexate, biologics) are used for maintenance when steroid dependence develops.

## T-otology-9 — BPPV
_source: pathophys_v470/otology_a.py_

**T-otology-9.overview**

Benign paroxysmal positional vertigo (BPPV) is brief vertigo triggered by head position change, caused by otoconia displaced into a semicircular canal. It is the most common cause of peripheral vertigo and is cured at the bedside with canalith repositioning (Epley for posterior canal).

**T-otology-9.physiology**

**Otolith organs**: the utricle and saccule contain otoconia, calcium carbonate crystals embedded on a gelatinous membrane, that sense linear acceleration and gravity. **Canals sense rotation**: each semicircular canal's cupula is normally the same density as endolymph, so it ignores gravity and responds only to angular acceleration. **Canal geometry**: the posterior canal is the most dependent canal when upright and supine, so free debris settles there most often. **Ewald laws**: eye movements occur in the plane of the stimulated canal; excitation of the posterior canal produces upbeating torsional nystagmus toward the affected ear.

**T-otology-9.pathophysiology**

**Canalithiasis**: otoconia dislodged from the utricle (aging, head trauma, inner-ear disease, prolonged bed rest) float freely in the canal. **Mechanism of vertigo**: when the head moves the canal into a gravity-dependent position, the debris falls and drags endolymph, deflecting the cupula. **Latency and fatigue**: the clump takes a few seconds to start moving (latency), the response lasts under a minute, and repeated testing disperses particles (fatigability). **Posterior canal (most common)**: Dix-Hallpike produces upbeating, torsional nystagmus toward the dependent ear. **Horizontal canal**: supine roll test produces horizontal nystagmus; geotropic nystagmus suggests canalithiasis and apogeotropic suggests cupulolithiasis (debris stuck on the cupula, making it gravity sensitive). **Repositioning logic**: the Epley maneuver rotates the head so debris travels around the canal and exits into the utricle, where it no longer stimulates the cupula.

## T-otology-10 — CSF Otorrhea / Temporal Encephalocele
_source: pathophys_v470/otology_a.py_

**T-otology-10.overview**

CSF otorrhea is CSF leaking into the middle ear and mastoid through a tegmen or posterior fossa defect, often with brain or meninges herniating (encephalocele). It causes clear drainage or effusion and carries meningitis risk, so it is repaired surgically.

**T-otology-10.physiology**

**Tegmen**: the thin bony roof of the mastoid and middle ear separates them from the middle cranial fossa dura and temporal lobe. **CSF pressure**: normal intracranial pressure is roughly 5-15 cm H2O and transmits pulsatile force to the skull base. **Arachnoid granulations**: aberrant granulations can erode skull-base bone over time.

**T-otology-10.pathophysiology**

**Spontaneous leaks**: elevated intracranial pressure (often in obese patients with idiopathic intracranial hypertension physiology) gradually thins the tegmen, and arachnoid pits form multiple small defects. **Herniation**: once bone is breached, dura and brain herniate into the mastoid or middle ear (encephalocele or meningoencephalocele), and CSF leaks. **Clinical mimicry**: with an intact drum, CSF collects as an effusion and drains down the Eustachian tube, producing unilateral effusion or clear rhinorrhea; after tube placement it presents as persistent clear otorrhea. **Acquired causes**: trauma, chronic ear disease, cholesteatoma erosion, and prior surgery. **Meningitis risk**: a direct path from the nasopharynx and middle ear to the subarachnoid space allows bacterial spread, which is why repair is recommended. **Recurrence**: untreated elevated ICP raises the risk of recurrence or new leaks after repair, so ICP management is part of care.

### CC-otology-10.1 (concept check)

Stem: An obese 52-year-old woman with a persistent unilateral effusion has continuous clear watery drainage after tube placement. What is the most likely underlying mechanism?

- **Correct:** High ICP thinning the tegmen
- Distractor: Serous effusion from tube dysfunction — _why wrong:_ Serous effusion would not produce continuous clear drainage after a tube.
- Distractor: Perilymph leak at the round window — _why wrong:_ Perilymph volume is tiny; continuous drainage suggests CSF.
- Distractor: Allergic reaction to the tube material — _why wrong:_ Allergy causes inflammation, not continuous clear drainage.

Explanation: Idiopathic intracranial hypertension physiology thins the tegmen and creates arachnoid pits and encephaloceles. CSF collects in the middle ear and drains through the tube. Beta-2 transferrin confirms CSF, and repair plus ICP management prevents meningitis.

Pearl: Clear persistent drainage after a tube in an obese adult: send beta-2 transferrin.

## T-otology-11 — Central Vestibular Disorders
_source: pathophys_v470/otology_b.py_

**T-otology-11.overview**

Central vestibular disorders arise in the brainstem, cerebellum, or cortex: stroke, demyelination, tumors, degenerative and migrainous disease. The essential otolaryngology skill is recognizing central signs so that stroke is not sent home as vestibular neuritis.

**T-otology-11.physiology**

**Vestibular nuclei**: integrate canal and otolith input and connect to the oculomotor nuclei, cerebellum, thalamus, and spinal cord. **Cerebellar flocculus and nodulus**: calibrate the VOR, hold gaze, and suppress nystagmus with fixation. **Blood supply**: the posterior circulation (vertebrobasilar, PICA, AICA) supplies the brainstem, cerebellum, and labyrinth.

**T-otology-11.pathophysiology**

**Stroke**: PICA infarcts cause vertigo with ataxia and often no hearing loss; AICA infarcts can cause vertigo plus SNHL because AICA supplies the labyrinth. **HINTS logic**: a normal head impulse in acute vertigo, direction-changing nystagmus, or vertical skew indicates a central lesion. **Gaze-holding failure**: cerebellar injury causes direction-changing gaze-evoked nystagmus. **Fixation**: central nystagmus does not suppress with visual fixation, whereas peripheral nystagmus does. **Pure vertical or torsional nystagmus**: downbeat (cervicomedullary or cerebellar) and upbeat nystagmus are central. **Truncal ataxia**: inability to sit or stand unaided out of proportion to vertigo suggests cerebellar involvement.

### CC-otology-11.1 (concept check)

Stem: A 68-year-old has acute continuous vertigo and nystagmus. The head impulse test is normal, nystagmus changes direction with gaze, and there is vertical skew. What is the most likely diagnosis?

- **Correct:** Posterior circulation stroke
- Distractor: Acute vestibular neuritis — _why wrong:_ Neuritis gives an abnormal head impulse and direction-fixed nystagmus.
- Distractor: Horizontal canal BPPV — _why wrong:_ BPPV causes brief positional vertigo, not continuous vertigo.
- Distractor: First Ménière attack — _why wrong:_ Ménière attacks are episodic with hearing changes.

Explanation: HINTS: in acute continuous vertigo, a normal head impulse, direction-changing nystagmus, or skew indicates a central lesion and requires urgent MRI.

Pearl: In acute vestibular syndrome, a normal head impulse is the dangerous finding.

## T-otology-12 — Chronic Otitis Media / Cholesteatoma
_source: pathophys_v470/otology_a.py_

**T-otology-12.overview**

Chronic otitis media is persistent middle-ear inflammation with or without a tympanic membrane perforation; cholesteatoma is keratinizing squamous epithelium trapped in the middle ear and mastoid. Cholesteatoma matters because it is locally destructive (ossicles, labyrinth, facial nerve, tegmen) and is treated surgically.

**T-otology-12.physiology**

**Middle-ear mucosa**: the middle ear and mastoid are lined by respiratory-type mucosa that clears secretions toward the Eustachian tube and exchanges gas with the blood. **Pressure regulation**: the mucosa continuously absorbs nitrogen and oxygen, so middle-ear pressure would fall unless the Eustachian tube periodically opens (swallowing, yawning) to re-equalize it. **Tympanic membrane layers**: lateral squamous epithelium, a middle fibrous layer, and medial mucosa; the pars flaccida lacks the organized fibrous layer, making it the weakest point. **Epithelial migration**: TM squamous epithelium normally migrates centrifugally outward into the canal, so keratin never accumulates on the drum. **Spaces at risk**: Prussak space (between pars flaccida and malleus neck) drains toward the epitympanum and aditus ad antrum; the sinus tympani and facial recess lie posterior and are hard to see surgically.

**T-otology-12.pathophysiology**

**Retraction theory (primary acquired)**: chronic Eustachian tube dysfunction creates negative pressure that sucks the weak pars flaccida or posterior pars tensa inward into a retraction pocket. **Trapping**: once the pocket deepens, migrating keratin can no longer clear and accumulates as a sac of desquamated keratin (the cholesteatoma matrix plus perimatrix). **Secondary acquired**: squamous epithelium migrates through a marginal perforation or is implanted by trauma or surgery. **Congenital**: an epithelial rest behind an intact drum, classically anterosuperior in a child with no history of otitis. **Bone erosion**: the perimatrix releases inflammatory cytokines and osteoclast-activating factors (with pressure and infection), resorbing ossicles (incus long process first), the lateral semicircular canal (fistula), the fallopian canal, and the tegmen. **Infection**: keratin debris is an ideal culture medium for Pseudomonas and anaerobes, so the classic symptom is painless, foul, recurrent otorrhea resistant to drops. **Why surgery**: the matrix keeps producing keratin and does not involute, so medical therapy only quiets infection; removal (canal wall up or down) is the cure.

### CC-otology-12.1 (concept check)

Stem: A 34-year-old has years of painless, foul otorrhea that returns after every course of drops. A pars flaccida retraction pocket is filled with white keratin. What mechanism makes this lesion progressively erode bone?

- **Correct:** Perimatrix inflammation activating osteoclasts
- Distractor: Pseudomonas enzymes dissolving the ossicles — _why wrong:_ Infection amplifies inflammation, but the self-perpetuating erosion comes from the cholesteatoma matrix and perimatrix.
- Distractor: Negative middle-ear pressure crushing bone — _why wrong:_ Negative pressure creates the retraction pocket; it does not account for progressive resorption.
- Distractor: Granulation tissue maturing into fibrous scar — _why wrong:_ Granulation may accompany disease, but scar formation does not resorb bone.

Explanation: Once a retraction pocket cannot self-clean, migrating keratin accumulates. The perimatrix releases cytokines and osteoclast-activating factors, eroding the incus long process, lateral canal, fallopian canal, and tegmen. The matrix keeps producing keratin, so surgery rather than drops is curative.

Pearl: Painless foul otorrhea plus a keratin-filled attic retraction is cholesteatoma until proven otherwise.

## T-otology-13 — Cochlear Implant Candidacy
_source: pathophys_v470/otology_a.py_

**T-otology-13.overview**

Cochlear implants restore access to sound for people with severe-to-profound sensorineural loss who get limited benefit from well-fitted hearing aids. Candidacy has expanded (single-sided deafness, asymmetric loss, younger children), so knowing the criteria and the anatomic and neural prerequisites matters.

**T-otology-13.physiology**

**What the implant replaces**: lost hair cells; it electrically stimulates surviving spiral ganglion neurons directly. **Tonotopy**: electrodes along the scala tympani stimulate base (high pitch) to apex (low pitch) neurons, mimicking place coding. **Neural requirements**: a cochlear nerve must be present and the auditory pathway must be functional; cochlear nerve aplasia is a contraindication. **Critical period**: the auditory cortex organizes around sound input in early childhood, so early implantation in congenitally deaf children produces better language outcomes.

**T-otology-13.pathophysiology**

**Why aids fail**: once inner hair cells are lost, amplification produces distorted, unintelligible input; aided speech recognition scores therefore guide candidacy. **Ossification after meningitis**: labyrinthitis ossificans can fill the scala tympani within weeks, making urgent imaging and early implantation important. **Auditory deprivation**: long duration of deafness leads to neural degeneration and cortical reorganization by other senses, reducing outcomes, especially in prelingual adults implanted late. **Anatomic barriers**: malformations (common cavity, incomplete partition), cochlear nerve deficiency, and ossification change electrode choice and expected benefit, and are mapped on CT and MRI. **ANSD and CMV**: in auditory neuropathy and congenital CMV, implants may help because they bypass dyssynchronous inner hair cell or synapse function.

### CC-otology-13.1 (concept check)

Stem: A 2-year-old became profoundly deaf after pneumococcal meningitis 3 weeks ago. Why are urgent imaging and early implantation planned?

- **Correct:** New bone may fill the scala tympani
- Distractor: Hearing usually returns within months — _why wrong:_ Profound post-meningitic loss rarely recovers; waiting risks ossification.
- Distractor: The cochlear nerve degenerates within days — _why wrong:_ Neural loss is slower; the urgent issue is new bone in the cochlea.
- Distractor: Implants are approved only before age 3 — _why wrong:_ Earlier is better, but the specific urgency here is ossification.

Explanation: Meningitis spreads into the cochlea through the cochlear aqueduct or IAC, triggering fibrosis and then labyrinthitis ossificans. MRI shows lost fluid signal early, and implanting before ossification allows full insertion.

Pearl: Deaf after meningitis: image now and implant before the cochlea ossifies.

## T-otology-14 — Cochlear Implant Failure / Revision
_source: pathophys_v470/otology_b.py_

**T-otology-14.overview**

Cochlear implant failure is any loss of benefit requiring evaluation and possible reimplantation, from hard device failure to soft failure, migration, infection, or extrusion. Knowing the categories guides the workup and reimplantation decision.

**T-otology-14.physiology**

**Device components**: an internal receiver-stimulator in a bony well and an electrode array in the scala tympani, linked to an external processor. **Neural interface**: stable impedances and thresholds reflect the electrode-tissue interface over time.

**T-otology-14.pathophysiology**

**Hard failure**: a demonstrable device malfunction (lost communication, short or open circuits) from trauma or component failure. **Soft failure**: declining performance, unpleasant sensations, or facial stimulation with normal integrity testing, diagnosed after excluding programming and medical causes. **Electrode migration or extrusion**: array movement out of the cochlea from fibrosis, growth in children, or poor fixation. **Biofilm infection**: implanted material supports biofilm, so infections may require explantation. **Skin flap breakdown**: thin flaps, pressure, or excessive magnet strength cause ischemia and extrusion. **Reimplantation**: usually restores performance, but ossification or fibrosis along the old array tract can complicate insertion.

### CC-otology-14.1 (concept check)

Stem: A 20-year-old implant user has gradually declining performance and painful sensations. Integrity testing is normal and reprogramming does not help. What is the working diagnosis?

- **Correct:** Soft failure of the device
- Distractor: Hard failure of the device — _why wrong:_ Hard failure is malfunction demonstrated on integrity testing.
- Distractor: New auditory neuropathy — _why wrong:_ New neuropathy would not explain painful stimulation with a normal device test.
- Distractor: Confirmed electrode migration — _why wrong:_ Migration is a separate diagnosis shown on imaging, not presumed.

Explanation: Soft failure is a suspected device problem that testing cannot confirm, diagnosed after excluding programming and medical causes. Reimplantation often restores performance.

Pearl: Declining performance with normal integrity testing = soft failure, after excluding other causes.

## T-otology-15 — Cochlear Implant Surgery
_source: pathophys_v470/otology_a.py_

**T-otology-15.overview**

Cochlear implant surgery places an electrode array in the scala tympani through a mastoidectomy and facial recess approach. The goals are complete atraumatic insertion, preserving residual hearing, and avoiding facial nerve injury, CSF gusher, and device extrusion.

**T-otology-15.physiology**

**Facial recess**: the triangle bounded by the facial nerve (medially/posteriorly), the chorda tympani (laterally), and the incus buttress (superiorly) provides access to the round window. **Round window niche**: it lies on the promontory, inferior to the oval window, and is often partly obscured by a bony overhang. **Scala tympani**: the target chamber, below the basilar membrane, communicates with the round window membrane. **Residual hearing**: surviving apical hair cells can be preserved for combined electric-acoustic stimulation if the basilar membrane is not damaged.

**T-otology-15.pathophysiology**

**Insertion trauma**: forcing the array can translocate it from scala tympani into scala vestibuli, rupture the basilar membrane, and destroy residual hearing and neurons. **Soft-surgery principles**: round window insertion, slow insertion, perioperative steroids, and lubrication reduce inflammation and fibrosis that destroy residual hearing. **Gusher**: abnormal communication between the IAC and the cochlea (e.g., incomplete partition type III, X-linked) lets CSF pour out at cochleostomy. **Meningitis risk**: implanted ears, especially with malformations and positioners in older devices, carry higher pneumococcal meningitis risk, so vaccination is required. **Facial nerve stimulation**: current spread from electrodes near the labyrinthine segment can stimulate the facial nerve, especially with otosclerosis or malformations.

### CC-otology-15.1 (concept check)

Stem: During implantation through the facial recess in a patient with residual low-frequency hearing, why is a slow, atraumatic round-window insertion preferred?

- **Correct:** It protects the basilar membrane
- Distractor: It eliminates any risk to the facial nerve — _why wrong:_ Facial nerve risk comes from drilling the recess, not the cochleostomy site.
- Distractor: A cochleostomy always enters scala vestibuli — _why wrong:_ A well-placed cochleostomy can enter scala tympani; the goal is atraumatic insertion.
- Distractor: The round window regrows to seal the array — _why wrong:_ The opening is sealed with tissue; regeneration is not the rationale.

Explanation: Residual hearing depends on intact apical hair cells and basilar membrane. Atraumatic insertion into scala tympani, steroids, and slow insertion reduce inflammation and fibrosis, allowing electric-acoustic stimulation.

Pearl: Hearing-preservation implantation is about the basilar membrane: stay in scala tympani and go slow.

## T-otology-16 — Congenital Inner-Ear Malformations
_source: pathophys_v470/otology_b.py_

**T-otology-16.overview**

Congenital inner-ear malformations are developmental anomalies of the labyrinth, from complete aplasia to enlarged vestibular aqueduct, that cause congenital or progressive SNHL. Classification matters for cochlear implant planning, gusher risk, and counseling.

**T-otology-16.physiology**

**Development**: the otic placode becomes the otocyst around week 4; the cochlea reaches two and a half turns by about week 10. **Timing logic**: earlier developmental arrest produces more severe malformations. **Vestibular aqueduct**: contains the endolymphatic duct connecting the inner ear to the endolymphatic sac; normal midpoint width is under about 1.5 mm.

**T-otology-16.pathophysiology**

**Michel aplasia**: complete absence of inner-ear structures; implantation is contraindicated. **Common cavity and cochlear aplasia**: very early arrest, often with abnormal nerve. **Incomplete partition I**: cystic cochlea without a modiolus, high gusher risk. **Incomplete partition II (Mondini)**: basal turn normal but apical turns fused, with enlarged vestibular aqueduct; often associated with SLC26A4/Pendred syndrome. **Incomplete partition III**: X-linked, cochlea lacks a modiolus and communicates widely with the IAC, causing severe gushers. **Enlarged vestibular aqueduct**: transmits CSF pressure fluctuations, so minor head trauma can cause stepwise SNHL drops; contact sports counseling matters. **Cochlear nerve deficiency**: a small or absent nerve (narrow IAC) predicts poor implant outcome.

### CC-otology-16.1 (concept check)

Stem: A child with progressive hearing loss has stepwise drops after minor head bumps. CT shows an enlarged vestibular aqueduct. Why does minor trauma worsen hearing?

- **Correct:** Pressure surges reach the inner ear via the aqueduct
- Distractor: A missing modiolus lets the cochlea fracture — _why wrong:_ Modiolar deficiency is a feature of IP-I and IP-III, not trauma sensitivity.
- Distractor: Perilymph drains into the middle ear — _why wrong:_ The mechanism is pressure transmission through the aqueduct, not middle-ear leakage.
- Distractor: Trauma triggers autoimmune inner-ear injury — _why wrong:_ There is no autoimmune mechanism here.

Explanation: An enlarged vestibular aqueduct transmits intracranial pressure changes to the inner ear, so minor trauma can cause stepwise SNHL. Counsel about contact sports and test for SLC26A4 (Pendred syndrome).

Pearl: EVA: avoid contact sports and test for Pendred syndrome.

## T-otology-17 — Cortical Neuroplasticity in Hearing Loss
_source: pathophys_v470/otology_b.py_

**T-otology-17.overview**

The auditory cortex reorganizes in response to deprivation and restored input. This explains critical periods for implantation in children, why long-deafened adults do worse with implants, and why tinnitus and hyperacusis develop.

**T-otology-17.physiology**

**Experience-dependent development**: auditory cortex circuits mature in response to sound, with a sensitive period in the first few years of life. **Cross-modal plasticity**: unused auditory cortex can be recruited by visual and somatosensory input. **Adult plasticity**: the adult brain still reorganizes, though more slowly, which underlies auditory training.

**T-otology-17.pathophysiology**

**Congenital deafness**: without sound input, auditory cortex fails to mature (delayed P1 latency of cortical evoked potentials) and is recruited by vision. **Critical period**: implantation before about 3.5 years produces normal cortical maturation; after about 7 years, outcomes decline. **Adult deprivation**: long-duration deafness leads to central reorganization, reducing implant benefit. **Maladaptive plasticity**: increased central gain after peripheral loss underlies tinnitus and hyperacusis. **Single-sided deafness in children**: reorganizes toward the hearing ear, reducing binaural processing, which supports early intervention.

### CC-otology-17.1 (concept check)

Stem: Why do children born deaf who are implanted before about age 3.5 develop more typical spoken language than those implanted after age 7?

- **Correct:** Auditory cortex has a sensitive period
- Distractor: Older children have more cochlear ossification — _why wrong:_ Ossification is not the main reason for age-related outcome differences.
- Distractor: Implant arrays do not fit older cochleae — _why wrong:_ The cochlea is adult-sized at birth.
- Distractor: Spiral ganglion cells vanish by age 7 — _why wrong:_ Neural survival matters, but cortical plasticity is the dominant explanation.

Explanation: Without sound, the auditory cortex fails to mature and is recruited by vision and touch (cross-modal plasticity). Cortical evoked P1 latency normalizes with early implantation.

Pearl: Early implantation uses the auditory sensitive period.

## T-otology-18 — EAC Exostoses / Osteoma (Canalplasty)
_source: pathophys_v470/otology_b.py_

**T-otology-18.overview**

Exostoses are broad-based, often multiple bony growths of the EAC from cold-water exposure; osteomas are solitary pedunculated benign bone tumors. They cause trapped keratin, recurrent otitis externa, and conductive loss when obstructive, and are treated with canalplasty.

**T-otology-18.physiology**

**Bony canal periosteum**: thin skin directly over bone; the periosteum responds to repeated cold stimuli by laying down new bone. **Sutures**: the tympanosquamous suture (anterosuperior) and tympanomastoid suture (posteroinferior) are landmarks and common origin sites. **Canal clearance**: lateral epithelial migration and a patent lumen allow water and keratin to escape; narrowing defeats both. **Deep relations**: the facial nerve (mastoid segment) lies deep to the posterior canal wall and the drum and annulus lie medially.

**T-otology-18.pathophysiology**

**Exostoses**: repeated cold-water exposure stimulates periosteal osteoblastic activity, producing broad-based, multiple, usually bilateral lesions medial in the canal ("surfer's ear"). **Osteoma**: a benign neoplasm, usually solitary and pedunculated, often lateral at the tympanosquamous suture. **Obstruction effects**: narrowing traps water, keratin, and debris, causing infections and conductive loss once nearly occlusive. **Surgical risk**: the facial nerve lies just deep to the posterior canal wall and the TM medially, so drilling must preserve skin and avoid deep posterior work.

### CC-otology-18.1 (concept check)

Stem: A surfer has multiple broad-based bony growths in both medial canals and recurrent otitis externa. Why do these lesions cause infections?

- **Correct:** Canal narrowing traps water and keratin
- Distractor: They secrete pro-inflammatory mediators — _why wrong:_ Exostoses are inert bone.
- Distractor: They are chronically infected bone — _why wrong:_ They are benign periosteal growths, not osteomyelitis.
- Distractor: They obstruct the Eustachian tube — _why wrong:_ They are in the external canal, not near the tube.

Explanation: Exostoses are periosteal reactions to repeated cold water, narrowing the canal so water and debris are trapped. Canalplasty widens the canal while protecting the facial nerve and drum.

Pearl: Exostoses are multiple and broad; osteomas are single and pedunculated.

## T-otology-19 — Eustachian Tube Dysfunction
_source: pathophys_v470/otology_a.py_

**T-otology-19.overview**

Eustachian tube dysfunction (ETD) is failure of the tube to open (dilatory ETD) or close (patulous ETD) normally. Dilatory ETD underlies otitis media with effusion, retraction pockets, and much acquired cholesteatoma, so it is a root cause in otology.

**T-otology-19.physiology**

**Structure**: the tube runs about 36 mm in adults from the anterior middle ear to the nasopharynx; the lateral third is bony and the medial two-thirds cartilaginous. **Default state**: the cartilaginous portion is normally closed, protecting the middle ear from nasopharyngeal pressure, secretions, and sound of one's own voice. **Active opening**: the tensor veli palatini (CN V3) pulls the lateral cartilaginous wall open during swallowing and yawning; the levator veli palatini assists. **Functions**: ventilation (equalizing pressure), protection, and clearance of middle-ear secretions by mucociliary transport. **Children**: their tube is shorter, more horizontal, and less rigid, and the tensor is less efficient, so ETD and otitis media are much more common.

**T-otology-19.pathophysiology**

**Gas absorption**: the middle-ear mucosa constantly absorbs gas; if the tube fails to open, pressure becomes negative. **Negative pressure consequences**: retraction of the tympanic membrane, transudation of fluid (effusion), and mucosal edema. **Causes of dilatory failure**: mucosal inflammation (allergy, infection, reflux), adenoid hypertrophy or mass, cleft palate (abnormal tensor insertion), and barotrauma. **Barotrauma**: on airplane descent, external pressure rises faster than a closed tube can equalize, locking the tube shut and producing pain, effusion, or hemotympanum. **Chronic sequelae**: long-standing negative pressure thins and retracts the drum (atelectasis, retraction pockets), which can evolve into cholesteatoma. **Unilateral adult effusion**: always examine the nasopharynx, because a mass such as nasopharyngeal carcinoma can obstruct the tube.

### CC-otology-19.1 (concept check)

Stem: A 58-year-old with no prior ear disease has a persistent unilateral middle-ear effusion for 2 months. Which evaluation is mandatory?

- **Correct:** Endoscopy of the nasopharynx
- Distractor: Allergy skin testing — _why wrong:_ Allergy may contribute, but a new unilateral adult effusion requires excluding a nasopharyngeal mass first.
- Distractor: Immediate tympanostomy tube — _why wrong:_ A tube may relieve symptoms but does not exclude the tumor causing the effusion.
- Distractor: Temporal bone CT scan — _why wrong:_ CT is not the first step; direct nasopharyngoscopy evaluates the most important cause.

Explanation: The Eustachian tube must open to replace gas absorbed by middle-ear mucosa. A mass at the torus tubarius (classically nasopharyngeal carcinoma in the fossa of Rosenmüller) blocks it, producing negative pressure and effusion.

Pearl: New unilateral adult effusion = scope the nasopharynx.

## T-otology-20 — External Auditory Canal Cholesteatoma
_source: pathophys_v470/otology_b.py_

**T-otology-20.overview**

EAC cholesteatoma is keratinizing squamous epithelium invading the bony canal wall, usually the floor, causing focal bone erosion. It differs from keratosis obturans and is treated with debridement or canalplasty.

**T-otology-20.physiology**

**Bony canal skin**: thin (about 0.2 mm), without adnexa, and bound directly to periosteum, so it has little reserve when its blood supply is injured. **Self-cleaning**: epithelium migrates from the tympanic membrane laterally along the canal, carrying keratin out; disease appears wherever that conveyor belt fails. **Blood supply**: the bony canal wall depends on periosteal vessels, and the inferior and posterior walls are the most exposed to minor trauma and ischemia. **Canal relationships**: the mastoid lies posterior, the TMJ anterior, and the facial nerve deep to the posterior-inferior canal wall.

**T-otology-20.pathophysiology**

**Focal periostitis**: local injury or ischemia of the inferior/posterior canal wall allows squamous epithelium to invade bone. **Unilateral and older patients**: typically presents with dull chronic otalgia and otorrhea, with normal hearing. **Bone sequestrum**: erosion creates a pocket containing keratin and necrotic bone. **Spread**: rarely erodes into the mastoid, facial canal, or temporomandibular joint. **Contrast with keratosis obturans**: keratosis obturans is a dense keratin plug from abnormal migration, usually bilateral, causing acute pain and conductive loss with smooth circumferential widening rather than focal erosion.

### CC-otology-20.1 (concept check)

Stem: An 80-year-old has unilateral dull otalgia and otorrhea. The inferior bony canal wall shows focal erosion with keratin and a bone sequestrum, and hearing is normal. What is the diagnosis?

- **Correct:** Canal cholesteatoma
- Distractor: Keratosis obturans — _why wrong:_ Keratosis obturans causes a dense plug with circumferential widening, acute pain, and conductive loss, usually bilateral.
- Distractor: Necrotizing otitis externa — _why wrong:_ NOE has granulation, severe pain, and host risk factors.
- Distractor: Exostoses of the canal — _why wrong:_ Exostoses are bony growths, not erosion.

Explanation: EAC cholesteatoma is focal periostitis with squamous invasion of bone, typically the inferior wall in older adults.

Pearl: Focal erosion + keratin in an older adult = EAC cholesteatoma.

## T-otology-21 — Facial Nerve Schwannoma
_source: pathophys_v470/otology_b.py_

**T-otology-21.overview**

Facial nerve schwannoma is a benign Schwann-cell tumor that can arise anywhere along CN VII, most often near the geniculate ganglion. It causes slowly progressive or recurrent facial weakness, and management usually favors observation to preserve function.

**T-otology-21.physiology**

**Segments**: CPA, IAC, labyrinthine, geniculate, tympanic, mastoid, and extratemporal segments; the geniculate region is the most common tumor site. **Schwann cells**: myelinate the peripheral nerve along its entire length beyond the Obersteiner-Redlich zone. **Nerve tolerance**: motor fibers tolerate slow compression with preserved function, so a large tumor can coexist with a normal face. **Bony expansion**: the fallopian canal and geniculate fossa remodel around slow-growing lesions, which CT shows as smooth enlargement.

**T-otology-21.pathophysiology**

**Slow growth**: tumors grow slowly, and facial function may remain normal until late. **Presentation by location**: geniculate tumors cause facial weakness; IAC and CPA tumors mimic vestibular schwannoma; tympanic segment tumors cause conductive loss. **Imaging clue**: a tubular enhancing mass following multiple segments of the facial nerve, with geniculate fossa enlargement on CT. **Treatment logic**: resection usually requires nerve sacrifice and grafting, with outcomes no better than House-Brackmann III, so observation or decompression is favored until function deteriorates.

### CC-otology-21.1 (concept check)

Stem: A patient has slowly progressive facial weakness (House-Brackmann II) and a tubular enhancing mass along the geniculate and tympanic segments. Why is observation often preferred?

- **Correct:** Resection usually sacrifices the nerve
- Distractor: These tumors are usually malignant — _why wrong:_ Facial nerve schwannomas are benign.
- Distractor: They regress spontaneously — _why wrong:_ They grow slowly; they do not regress.
- Distractor: Radiation reliably cures them — _why wrong:_ Radiation may control growth but does not remove the tumor.

Explanation: The tumor arises from the nerve itself, so resection typically requires nerve sacrifice and grafting, with function no better than House-Brackmann III. Observation or decompression preserves function until it deteriorates.

Pearl: Do not trade a good face for tumor removal.

## T-otology-22 — Facial Paralysis
_source: pathophys_v470/otology_a.py_

**T-otology-22.overview**

Facial paralysis is weakness of the muscles of facial expression from a CN VII lesion; Bell palsy (idiopathic, acute) is the most common cause but is a diagnosis of exclusion. Management hinges on whether the lesion is central or peripheral, complete or incomplete, and what the cause is.

**T-otology-22.physiology**

**Motor nucleus**: the upper face portion receives bilateral cortical input, while the lower face receives mainly contralateral input. **Branches by segment**: GSPN at the geniculate (lacrimation), nerve to stapedius in the mastoid segment (stapedial reflex), and chorda tympani before the stylomastoid foramen (taste, submandibular/sublingual secretion). **Labyrinthine segment**: the narrowest portion of the fallopian canal, at about 0.7 mm, with a thin vascular supply. **Nerve injury grades (Sunderland/Seddon)**: neurapraxia (conduction block), axonotmesis (axon loss with intact sheath), and neurotmesis (complete transection). **Electrophysiology**: after axonal loss, Wallerian degeneration makes the distal nerve inexcitable within 3-5 days, which is why ENoG is timed 3-14 days after onset.

**T-otology-22.pathophysiology**

**Central vs peripheral**: a central (upper motor neuron) lesion spares the forehead because of bilateral cortical input; peripheral lesions paralyze the whole hemiface. **Bell palsy mechanism**: presumed viral (HSV-1) reactivation causes nerve inflammation and edema; swelling within the tight labyrinthine segment produces compression, ischemia, and conduction block or degeneration. **Why steroids early**: they reduce edema in the bony canal and improve complete recovery when started within 72 hours. **Prognosis tracks injury degree**: neurapraxia recovers completely; axonal loss recovers slowly and incompletely, with risk of synkinesis from misdirected regenerating axons. **ENoG logic**: more than 90 percent degeneration within 14 days of onset in complete paralysis predicts poor recovery and underlies the controversial middle fossa decompression. **Topognosis**: whether tearing, stapedial reflex, and taste are affected localizes the lesion relative to the GSPN, nerve to stapedius, and chorda tympani. **Red flags against Bell**: slowly progressive weakness, recurrence on the same side, involvement of individual branches, or other cranial neuropathies suggest tumor.

### CC-otology-22.1 (concept check)

Stem: A 30-year-old develops right facial weakness over 24 hours and cannot raise the right brow, close the right eye, or smile on the right. Why does forehead involvement indicate a peripheral lesion?

- **Correct:** Upper-face neurons get bilateral cortical input
- Distractor: The frontal branch leaves the skull separately — _why wrong:_ The frontal branch arises from the main trunk within the parotid.
- Distractor: Trigeminal fibers supply the forehead centrally — _why wrong:_ Forehead muscles are always innervated by the facial nerve.
- Distractor: Central lesions affect only eye closure — _why wrong:_ Central lesions spare the upper face and weaken the lower face.

Explanation: Bilateral cortical input to the upper facial nucleus means a stroke spares the forehead. Whole-hemiface weakness indicates a peripheral lesion such as Bell palsy, treated with steroids within 72 hours.

Pearl: Forehead spared = central until proven otherwise; forehead involved = peripheral.

## T-otology-23 — Glomus Tumor / Paraganglioma
_source: pathophys_v470/otology_b.py_

**T-otology-23.overview**

Temporal bone paragangliomas (glomus tympanicum and glomus jugulare) are vascular neuroendocrine tumors that cause pulsatile tinnitus, conductive loss, and lower cranial nerve deficits. Their genetics, vascularity, and location guide workup and treatment.

**T-otology-23.physiology**

**Paraganglia**: neural crest-derived chemoreceptor cells along Jacobson (CN IX) and Arnold (CN X) nerves and the jugular bulb adventitia. **Vascular supply**: mainly the ascending pharyngeal artery (inferior tympanic branch).

**T-otology-23.pathophysiology**

**Hypervascular tumor**: rich vascularity produces pulsatile tinnitus and a red retrotympanic mass that blanches with pressure (Brown sign). **Glomus tympanicum**: confined to the promontory, causing conductive loss. **Glomus jugulare**: grows from the jugular bulb, eroding the jugular foramen and involving CN IX-XI (Vernet). **Genetics**: succinate dehydrogenase (SDHx) mutations cause hereditary, multifocal tumors, so genetic testing is recommended. **Catecholamines**: a minority secrete catecholamines, which must be screened before surgery. **Imaging**: salt-and-pepper MRI appearance from flow voids and moth-eaten bone erosion on CT.

## T-otology-24 — Gradenigo Syndrome (Petrous Apicitis)
_source: pathophys_v470/otology_b.py_

**T-otology-24.overview**

Gradenigo syndrome is the triad of otorrhea, retro-orbital pain, and abducens palsy from petrous apex infection. It is a complication of otitis media or mastoiditis requiring imaging, antibiotics, and drainage.

**T-otology-24.physiology**

**Petrous apex**: medial temporal bone, pneumatized in about a third of people. **Dorello canal**: CN VI passes under the petroclinoid ligament adjacent to the apex. **Meckel cave**: the trigeminal ganglion lies over the apex.

**T-otology-24.pathophysiology**

**Spread**: infection extends from the middle ear and mastoid through air cell tracts into the pneumatized apex. **CN VI palsy**: inflammation compresses or irritates the abducens nerve in Dorello canal, causing lateral rectus weakness and diplopia. **Retro-orbital pain**: inflammation of the trigeminal ganglion or dura. **Further spread**: meningitis, cavernous sinus thrombosis, and carotid involvement.

### CC-otology-24.1 (concept check)

Stem: A child with persistent otorrhea develops retro-orbital pain and horizontal diplopia with a lateral gaze palsy. Which nerve is affected, and where?

- **Correct:** Abducens nerve in Dorello canal
- Distractor: Oculomotor nerve in the cavernous sinus — _why wrong:_ CN III palsy causes ptosis and a down-and-out eye.
- Distractor: Trochlear nerve at the orbital fissure — _why wrong:_ CN IV palsy causes vertical diplopia.
- Distractor: Optic nerve in the optic canal — _why wrong:_ Optic nerve involvement causes vision loss, not gaze palsy.

Explanation: Petrous apex infection inflames CN VI in Dorello canal and the trigeminal ganglion, producing the Gradenigo triad.

Pearl: Otorrhea + retro-orbital pain + CN VI palsy = petrous apicitis.

## T-otology-25 — Hearing Aids and Bone-Conduction Devices
_source: pathophys_v470/otology_a.py_

**T-otology-25.overview**

Hearing aids amplify sound for the cochlea, while bone-conduction devices bypass the outer and middle ear by vibrating the skull. Matching the device to the type of loss, the ear canal, and the patient's goals is a core part of otology.

**T-otology-25.physiology**

**Air-conduction aids**: a microphone, processor, and receiver deliver frequency-specific gain into the ear canal, with compression to keep loud sounds tolerable. **Dynamic range**: sensorineural loss raises thresholds but not discomfort levels, narrowing the usable range (recruitment), so wide dynamic range compression is required. **Bone conduction**: skull vibration stimulates both cochleae with very little interaural attenuation. **CROS**: routes sound from a deaf ear to the better ear through a microphone on the deaf side.

**T-otology-25.pathophysiology**

**Why conductive loss amplifies well**: the cochlea is healthy, so amplification restores clarity; bone-conduction devices are ideal when the canal cannot hold an aid (atresia, chronic drainage). **Why severe SNHL amplifies poorly**: damaged inner hair cells and neurons distort sound, so loudness improves more than clarity, which pushes toward cochlear implants. **Occlusion effect**: blocking the canal traps bone-conducted low-frequency sound, making one's own voice boomy; open fittings reduce it. **Feedback**: sound leaking from the canal back to the microphone causes whistling, worsened by a loose fit or wax. **Single-sided deafness**: a bone-anchored device or CROS transfers sound to the hearing ear but cannot restore binaural localization, whereas a cochlear implant can partially restore it. **Untreated hearing loss**: it is associated with cognitive decline, social isolation, and falls, which is part of why amplification matters.

### CC-otology-25.1 (concept check)

Stem: A patient has single-sided deafness after vestibular schwannoma surgery. A bone-conduction device improves hearing of speakers on his deaf side. What can it not restore?

- **Correct:** Binaural sound localization
- Distractor: Hearing for sounds on the deaf side — _why wrong:_ That is exactly what CROS and bone-conduction devices improve.
- Distractor: Access to low-frequency sounds — _why wrong:_ Frequency range is not the main limitation of these devices.
- Distractor: Speech understanding in quiet — _why wrong:_ Speech in quiet is usually good with one normal ear.

Explanation: Bone conduction crosses the skull to the hearing cochlea, overcoming the head shadow. Localization requires comparing input between two ears, so only a cochlear implant in the deaf ear can partially restore it.

Pearl: CROS and bone conduction beat the head shadow; only a cochlear implant can partially restore localization.

## T-otology-26 — Hyperacusis / Decreased Sound Tolerance
_source: pathophys_v470/otology_b.py_

**T-otology-26.overview**

Hyperacusis is reduced tolerance to ordinary sound levels, often with pain or fear of sound, and frequently coexists with tinnitus. It is a central gain disorder treated with sound therapy and counseling rather than ear protection overuse.

**T-otology-26.physiology**

**Loudness growth**: normal loudness rises predictably with sound intensity, with discomfort near 90-100 dB HL. **Central gain control**: the auditory system tunes sensitivity to the input level. **Efferent control**: olivocochlear and middle-ear reflexes modulate input.

**T-otology-26.pathophysiology**

**Increased central gain**: after cochlear injury, central neurons become hyperresponsive, so moderate sounds feel loud. **Overprotection**: constant earplug use reduces input further, increasing gain and worsening sensitivity. **Pain hyperacusis**: type II cochlear afferent fibers and inflammatory pathways may mediate sound-induced pain. **Associated conditions**: Bell palsy (loss of stapedius reflex), SCD, migraine, autism, Williams syndrome, and noise exposure. **Treatment logic**: gradual sound enrichment lowers central gain, and CBT reduces the threat response.

### CC-otology-26.1 (concept check)

Stem: A 29-year-old developed sensitivity to everyday sounds after a concert and now wears earplugs whenever she leaves home. Her symptoms are steadily worsening. Why does constant ear protection make hyperacusis worse?

- **Correct:** It further raises central auditory gain
- Distractor: It promotes canal infection and pain — _why wrong:_ Infection is not the mechanism of worsening hyperacusis.
- Distractor: It damages outer hair cells over time — _why wrong:_ Earplugs protect hair cells; they do not damage them.
- Distractor: It raises static middle-ear pressure — _why wrong:_ Earplugs do not meaningfully change middle-ear pressure.

Explanation: Hyperacusis reflects increased central auditory gain. Overprotection deprives the system of input, raising gain further. Gradual sound enrichment and counseling lower gain.

Pearl: In hyperacusis, constant protection worsens sensitivity: enrich sound instead.

## T-otology-27 — Keratosis Obturans
_source: pathophys_v470/otology_b.py_

**T-otology-27.overview**

Keratosis obturans is accumulation of a dense keratin plug in the bony canal from failed epithelial migration. It causes acute pain and conductive loss and is associated with bronchiectasis and sinusitis in younger patients.

**T-otology-27.physiology**

**Epithelial migration**: canal epithelium normally migrates centrifugally from the drum and laterally along the canal, clearing keratin without help. **Bony canal**: tightly adherent periosteal skin without glands or hair, so keratin there can only leave by migration. **Cerumen**: produced only in the lateral cartilaginous canal; it lubricates and carries debris outward. **Sympathetic influence**: autonomic input modulates glandular secretion and epithelial turnover in the canal.

**T-otology-27.pathophysiology**

**Migration failure**: abnormal epithelial migration lets keratin layers accumulate in an onion-skin plug. **Pressure effects**: the plug causes circumferential widening of the bony canal, acute severe pain, and conductive hearing loss. **Bilateral pattern**: it is often bilateral and may be associated with respiratory conditions such as bronchiectasis and chronic sinusitis, possibly through sympathetic reflex hypersecretion. **Management logic**: regular debridement and keeping the ear dry, since the migration defect persists.

### CC-otology-27.1 (concept check)

Stem: A 30-year-old with bronchiectasis has bilateral acute ear pain and conductive loss. Both canals contain dense keratin plugs with smooth circumferential widening. What is the mechanism?

- **Correct:** Failed epithelial migration
- Distractor: Focal squamous invasion of bone — _why wrong:_ That describes EAC cholesteatoma.
- Distractor: Cold-water periosteal bone growth — _why wrong:_ That describes exostoses.
- Distractor: Fungal overgrowth in the canal — _why wrong:_ Otomycosis produces fungal debris, not keratin plugs with widening.

Explanation: Abnormal epithelial migration produces an onion-skin keratin plug that widens the canal. It is often bilateral and associated with bronchiectasis and sinusitis.

Pearl: Bilateral keratin plugs in a younger patient with bronchiectasis = keratosis obturans.

## T-otology-28 — Labyrinthitis / Infections of the Labyrinth
_source: pathophys_v470/otology_b.py_

**T-otology-28.overview**

Labyrinthitis is inflammation of the inner ear that causes vertigo with hearing loss. It may be viral, serous (toxic) from adjacent otitis, or suppurative bacterial infection that can destroy the labyrinth and lead to meningitis or ossification.

**T-otology-28.physiology**

**Barriers**: the round window membrane and annular ligament separate the middle ear from perilymph. **CSF connections**: perilymph connects with CSF through the cochlear aqueduct and the IAC fundus. **Combined end organs**: the labyrinth contains both cochlear and vestibular sensory epithelium.

**T-otology-28.pathophysiology**

**Viral labyrinthitis**: like vestibular neuritis but involving the cochlea, producing acute vertigo plus SNHL. **Serous labyrinthitis**: bacterial toxins and inflammatory mediators diffuse through the round window from otitis media, causing usually reversible hair-cell dysfunction. **Suppurative labyrinthitis**: bacteria enter the labyrinth (from otitis, cholesteatoma fistula, or meningitis), destroying hair cells and producing permanent anacusis. **Meningogenic spread**: bacterial meningitis enters through the cochlear aqueduct or IAC, typically bilaterally. **Labyrinthitis ossificans**: inflammation triggers fibrosis then new bone formation within weeks to months, which is why early cochlear implantation is pursued after meningitis-related deafness.

### CC-otology-28.1 (concept check)

Stem: A 40-year-old with untreated cholesteatoma develops acute vertigo and complete hearing loss in that ear, with fever. CT shows a lateral canal fistula. What distinguishes suppurative from serous labyrinthitis?

- **Correct:** Bacterial invasion causing permanent sensory loss
- Distractor: Toxin diffusion causing reversible dysfunction — _why wrong:_ That describes serous labyrinthitis.
- Distractor: Viral injury limited to the vestibular nerve — _why wrong:_ That describes vestibular neuritis.
- Distractor: Hydrops causing fluctuating hearing — _why wrong:_ That describes Ménière disease.

Explanation: In suppurative labyrinthitis, bacteria enter the inner ear (here through a fistula) and destroy sensory cells, producing a dead ear and risk of meningitis and labyrinthitis ossificans.

Pearl: Serous labyrinthitis can recover; suppurative labyrinthitis usually leaves a dead ear.

## T-otology-29 — Lateral Skull-Base Tumor Framework
_source: pathophys_v470/otology_b.py_

**T-otology-29.overview**

Lateral skull-base tumors (vestibular schwannoma, meningioma, paraganglioma, epidermoid, chondrosarcoma, and others) are managed by matching tumor biology, location, and hearing status to observation, radiation, or a surgical approach. The framework is a decision tool built on anatomy and natural history.

**T-otology-29.physiology**

**Key compartments**: IAC and CPA, jugular foramen, petrous apex, middle fossa floor, and infratemporal fossa. **Approach anatomy**: translabyrinthine (sacrifices hearing, wide CPA access), retrosigmoid (hearing preservation, posterior fossa), middle fossa (small intracanalicular tumors, hearing preservation), and infratemporal fossa (jugular foramen). **Neighbors**: CN VII and VIII, lower cranial nerves IX-XII, carotid, jugular bulb, sigmoid sinus, and brainstem.

**T-otology-29.pathophysiology**

**Tumor biology drives timing**: many schwannomas and meningiomas grow slowly, so observation with serial MRI is valid; malignant or rapidly growing tumors need treatment. **Imaging signatures**: schwannoma (enhances, centered on the IAC, acute angle), meningioma (broad dural base, dural tail, obtuse angle, hyperostosis), epidermoid (restricted diffusion, no enhancement), paraganglioma (salt-and-pepper, flow voids). **Approach selection**: depends on hearing status, tumor size and location, and patient factors. **Radiation logic**: stereotactic radiosurgery arrests growth in most small-to-medium tumors, but does not remove them and complicates later surgery. **Cranial nerve outcomes**: lower cranial nerve deficits with jugular foramen tumors are poorly tolerated, which favors subtotal resection or radiation.

### CC-otology-29.1 (concept check)

Stem: An enhancing CPA mass has a broad dural base, a dural tail, and an obtuse angle with the petrous bone, and it does not enter the IAC. What is it most likely to be?

- **Correct:** Meningioma
- Distractor: Vestibular schwannoma — _why wrong:_ Schwannomas are centered on the IAC with an acute angle.
- Distractor: Epidermoid cyst — _why wrong:_ Epidermoids do not enhance and restrict diffusion.
- Distractor: Arachnoid cyst — _why wrong:_ Arachnoid cysts follow CSF signal and do not enhance.

Explanation: Imaging signatures predict histology: meningioma has a broad dural base, tail, and hyperostosis; schwannoma is IAC-centered.

Pearl: IAC-centered = schwannoma; broad base with dural tail = meningioma.

## T-otology-30 — Ménière Disease
_source: pathophys_v470/otology_a.py_

**T-otology-30.overview**

Ménière disease is episodic vertigo lasting 20 minutes to 12 hours with fluctuating low-frequency sensorineural hearing loss, tinnitus, and aural fullness in the same ear. Its pathologic hallmark is endolymphatic hydrops, and management escalates from diet and diuretics to intratympanic therapy and ablation.

**T-otology-30.physiology**

**Two fluids**: endolymph (high potassium, low sodium) fills the membranous labyrinth; perilymph (high sodium, like CSF) surrounds it. **Production and resorption**: the stria vascularis and vestibular dark cells secrete endolymph; the endolymphatic duct and sac are thought to regulate volume and resorb fluid. **Reissner membrane**: it separates potassium-rich endolymph in the scala media from sodium-rich perilymph in the scala vestibuli. **Apical sensitivity**: the cochlear apex is the most compliant region, so pressure changes affect low frequencies first.

**T-otology-30.pathophysiology**

**Endolymphatic hydrops**: excess endolymph distends the cochlear duct and saccule, seen consistently on histopathology and gadolinium MRI. **Why the low frequencies go first**: the compliant apex is distorted earliest by hydrops, producing low-frequency loss and fullness. **Attack mechanism (rupture/leak theory)**: membranes may rupture or leak, mixing potassium-rich endolymph into perilymph, depolarizing hair cells and vestibular nerve fibers (initial excitation, then paralysis), then healing. **Fluctuation and progression**: each attack can recover, but repeated episodes cause permanent hair-cell loss and a flattening hearing loss over years, with eventual burnout of vestibular function. **Contributing factors**: endolymphatic sac hypoplasia, autoimmune and allergic factors, migraine overlap, and genetic predisposition; hydrops is necessary but not sufficient, since not all hydrops produces symptoms. **Therapeutic logic**: salt restriction and diuretics aim to reduce endolymph volume; intratympanic gentamicin works by chemically ablating vestibular hair cells (dark cells), while steroids are anti-inflammatory and hearing-sparing.

## T-otology-31 — Necrotizing Otitis Externa
_source: pathophys_v470/otology_a.py_

**T-otology-31.overview**

Necrotizing (malignant) otitis externa is an invasive infection of the external canal that spreads to the skull base, usually Pseudomonas in older diabetics or immunocompromised patients. It causes severe pain, granulation tissue at the bony-cartilaginous junction, and cranial neuropathies, and requires prolonged systemic antibiotics.

**T-otology-31.physiology**

**Fissures of Santorini**: natural gaps in the cartilaginous canal allow spread inferiorly toward the parotid and skull base. **Bony-cartilaginous junction**: the classic site of granulation tissue and early invasion. **Skull-base neighbors**: the stylomastoid foramen (CN VII) and jugular foramen (CN IX-XI), plus the hypoglossal canal (CN XII), lie close to the infection's route. **Host defense**: neutrophil function and microvascular perfusion are essential to contain Pseudomonas.

**T-otology-31.pathophysiology**

**Host susceptibility**: diabetic microangiopathy reduces tissue perfusion, and hyperglycemia impairs neutrophil chemotaxis and phagocytosis; immunosuppression and HIV play similar roles. **Pseudomonas virulence**: exotoxins and proteases cause necrotizing vasculitis and tissue invasion. **Spread**: infection extends from the canal floor through Santorini fissures and the tympanomastoid suture into the temporal bone and skull base, producing osteomyelitis. **Cranial neuropathies**: CN VII is most often involved first at the stylomastoid foramen; spread medially affects CN IX-XII and can cause sigmoid or cavernous sinus thrombosis. **Pain out of proportion**: periosteal and skull-base involvement explains deep, nocturnal pain. **Fungal and resistant forms**: Aspergillus and resistant organisms occur, which is why cultures and biopsy guide therapy, along with exclusion of carcinoma.

### CC-otology-31.1 (concept check)

Stem: A 74-year-old diabetic has 6 weeks of severe night-time otalgia, granulation at the floor of the bony-cartilaginous junction, and new facial weakness. Why is the facial nerve often the first cranial nerve involved?

- **Correct:** Spread reaches the stylomastoid foramen first
- Distractor: It runs within the canal skin itself — _why wrong:_ The facial nerve lies deep to the posterior canal wall, not in canal skin.
- Distractor: Pseudomonas toxin selectively hits motor neurons — _why wrong:_ Toxins cause vasculitis and necrosis, not selective motor neuron injury.
- Distractor: Swelling compresses its labyrinthine segment — _why wrong:_ That is the Bell palsy mechanism; NOE spreads along the skull base.

Explanation: Pseudomonas spreads through the fissures of Santorini and along the skull base to the stylomastoid foramen, then the jugular foramen (IX-XI). Diabetic microangiopathy and neutrophil dysfunction allow spread.

Pearl: Diabetic + pain out of proportion + granulation at the bony-cartilaginous junction = necrotizing otitis externa.

## T-otology-32 — Neurotologic Intraoperative Cranial-Nerve Monitoring
_source: pathophys_v470/otology_b.py_

**T-otology-32.overview**

Intraoperative cranial nerve monitoring (facial EMG, ABR and cochlear nerve action potentials, lower cranial nerves) helps identify nerves and predict function during otologic and skull-base surgery. It supplements anatomic knowledge; it does not replace it.

**T-otology-32.physiology**

**Facial EMG**: needle electrodes in the orbicularis oculi and oris record motor responses to mechanical or electrical stimulation. **Threshold**: a proximal nerve that responds to low stimulation (e.g., 0.05-0.1 mA) at the end of surgery predicts good function. **Hearing monitoring**: ABR and direct cochlear nerve action potentials track auditory function during hearing-preservation surgery. **Anesthesia**: neuromuscular blockade abolishes EMG responses, so it must be avoided after induction.

**T-otology-32.pathophysiology**

**Mechanical irritation**: traction or manipulation produces spontaneous EMG activity (bursts and trains); sustained trains warn of injury. **Thermal injury**: drill heat and cautery can injure nerves without immediate EMG warning. **Proximal-to-distal ratio**: a rising proximal threshold indicates conduction block at the dissection site. **False reassurance**: a stimulator response proves only conduction distal to the stimulation point, not that the nerve is uninjured proximally. **ABR changes**: wave V latency prolongation or amplitude loss during dissection signals cochlear nerve or vascular compromise.

### CC-otology-32.1 (concept check)

Stem: At the end of a vestibular schwannoma resection, the facial nerve responds to 0.05 mA stimulation at the brainstem. What does this predict?

- **Correct:** Good postoperative facial function
- Distractor: Complete postoperative facial paralysis — _why wrong:_ A low proximal threshold predicts good function.
- Distractor: Need for immediate cable grafting — _why wrong:_ Grafting is reserved for transection or discontinuity.
- Distractor: Residual neuromuscular blockade — _why wrong:_ Blockade abolishes responses rather than lowering thresholds.

Explanation: A low stimulation threshold at the proximal nerve shows conduction across the dissection zone, predicting good facial outcome.

Pearl: Low proximal threshold at the end of surgery predicts a good face.

## T-otology-33 — Ossicular Discontinuity
_source: pathophys_v470/otology_a.py_

**T-otology-33.overview**

Ossicular discontinuity is a break in the malleus-incus-stapes chain, most often erosion of the incus long process or a traumatic incudostapedial separation. It produces a maximal conductive loss with an intact drum and is repaired by ossiculoplasty.

**T-otology-33.physiology**

**Lever system**: the malleus handle and incus long process form a lever (about 1.3:1) that drives the stapes. **Joints**: the incudomalleolar and incudostapedial joints are synovial; the incudostapedial joint is the most delicate link. **Blood supply**: the incus long process and lenticular process have a tenuous end-arterial mucosal blood supply. **Suspension**: ligaments and the tensor tympani and stapedius tendons hold the chain in place.

**T-otology-33.pathophysiology**

**Maximal conductive loss**: with an intact drum and a broken chain, the drum shields the cochlea and transmits nothing, producing a gap up to about 60 dB, larger than a simple perforation. **Erosion**: chronic otitis media and cholesteatoma erode the incus long process first because of its poor blood supply and inflammatory osteitis. **Trauma**: temporal bone fractures and head injuries separate the incudostapedial joint or dislocate the incus. **Tympanometry clue**: a disconnected, flaccid system produces a very high-compliance (Ad) tympanogram, the opposite of the stiff system in otosclerosis. **Reflexes**: stapedius contraction cannot change drum compliance when the chain is broken, so reflexes recorded in that ear are absent.

### CC-otology-33.1 (concept check)

Stem: After a head injury, a patient has a 55 dB conductive loss in an ear with a normal-appearing drum. Tympanometry shows an unusually tall peak. What is the most likely cause?

- **Correct:** Incudostapedial joint separation
- Distractor: Otosclerotic fixation of the stapes — _why wrong:_ Fixation stiffens the system (shallow As peak) and is not caused by trauma.
- Distractor: Hemotympanum filling the middle ear — _why wrong:_ Blood or fluid produces a flat type B tracing.
- Distractor: A pinpoint tympanic membrane perforation — _why wrong:_ The drum is intact; a perforation gives a flat tracing with large volume.

Explanation: A disconnected chain lets the drum move freely (type Ad) while transmitting nothing to the stapes, producing a maximal conductive loss of up to about 60 dB.

Pearl: Intact drum + maximal conductive loss + very tall tympanogram = discontinuity.

## T-otology-34 — Otologic Manifestations of Systemic Disease
_source: pathophys_v470/otology_b.py_

**T-otology-34.overview**

Many systemic diseases first present in the ear, including vasculitis, granulomatous disease, autoimmune and metabolic disorders, infection, and malignancy. Recognizing unusual patterns (bilateral, rapidly progressive, granulation, cranial neuropathy) prevents missed diagnoses.

**T-otology-34.physiology**

**Shared tissues**: middle-ear mucosa resembles respiratory mucosa, so diseases of the airway (GPA, sarcoid) can involve it. **Inner-ear vascular and immune targets**: the stria vascularis and labyrinthine vasculature are vulnerable to vasculitis and immune complexes. **Bone metabolism**: the otic capsule responds to systemic bone disorders.

**T-otology-34.pathophysiology**

**GPA**: granulomatous vasculitis causes serous otitis, refractory granulation, conductive and sensorineural loss, and facial palsy. **Relapsing polychondritis**: autoimmune attack on cartilage spares the cartilage-free lobule and can cause SNHL and vertigo. **Cogan syndrome**: interstitial keratitis with audiovestibular dysfunction from autoimmune vasculitis. **Paget disease and osteogenesis imperfecta**: disordered bone remodeling causes conductive and sensorineural loss. **Sickle cell, diabetes, renal failure**: microvascular and metabolic injury to the cochlea. **Langerhans cell histiocytosis, leukemia, metastasis**: infiltrate the temporal bone, mimicking mastoiditis or chronic otitis. **Infection**: syphilis and tuberculosis cause otitis or inner-ear disease that responds to specific therapy.

### CC-otology-34.1 (concept check)

Stem: A 50-year-old has bilateral serous otitis media unresponsive to tubes, a saddle nose, and hematuria. Which test is most likely to confirm the unifying diagnosis?

- **Correct:** ANCA (PR3) testing
- Distractor: Sweat chloride testing — _why wrong:_ That tests for cystic fibrosis.
- Distractor: Serum ACE level — _why wrong:_ ACE is used for sarcoidosis, which rarely causes this triad.
- Distractor: Temporal bone CT — _why wrong:_ CT shows the effusion but not the systemic diagnosis.

Explanation: Granulomatosis with polyangiitis is a necrotizing granulomatous vasculitis of the airways and kidneys. Middle-ear involvement causes refractory effusion, and nasal involvement causes saddle nose.

Pearl: Refractory otitis plus nasal destruction plus kidney involvement = check ANCA.

## T-otology-35 — Otosclerosis / Stapes Fixation
_source: pathophys_v470/otology_a.py_

**T-otology-35.overview**

Otosclerosis is abnormal remodeling of the otic capsule that most often fixes the stapes footplate, causing progressive conductive hearing loss in young adults. It is a classic boards and OR topic because it is diagnosed by audiometry and reflexes and corrected by stapedotomy or amplification.

**T-otology-35.physiology**

**Otic capsule**: the bony labyrinth is normally among the densest bone in the body and essentially does not remodel after childhood. **Stapes footplate**: it sits in the oval window held by the annular ligament, which allows piston-like motion into the vestibule. **Middle-ear impedance matching**: the area ratio of the tympanic membrane to the footplate (about 17:1) and the ossicular lever (about 1.3:1) recover roughly 25-30 dB that would otherwise be lost moving sound from air to inner-ear fluid. **Acoustic reflex**: loud sound contracts the stapedius (CN VII), stiffening the chain; the reflex is measured as a change in compliance.

**T-otology-35.pathophysiology**

**Abnormal remodeling**: foci of osteoclastic resorption (active, vascular "otospongiosis") are replaced by dense sclerotic bone (inactive otosclerosis). **Site of predilection**: the fissula ante fenestram, just anterior to the oval window, is the classic first site, so the anterior footplate is fixed first. **Conductive loss**: a fixed footplate cannot transmit sound energy into the vestibule, producing a progressive low-frequency-predominant air-bone gap. **Carhart notch**: bone conduction dips at 2000 Hz because fixation removes the ossicular-chain resonance contribution to bone conduction; it is a mechanical artifact, not true cochlear loss, and improves after surgery. **Reflexes absent**: the stapedius cannot move a fixed stapes, so acoustic reflexes are absent; early on an on-off pattern may appear. **Cochlear otosclerosis**: foci involving the cochlear endosteum can release toxic enzymes that cause sensorineural loss. **Risk factors**: autosomal dominant inheritance with incomplete penetrance, female predominance, worsening with pregnancy (hormonal influence), and measles virus association. **Schwartze sign**: a reddish promontory blush reflects hypervascular active otospongiosis.

### CC-otology-35.1 (concept check)

Stem: A 32-year-old woman has progressive left hearing loss that worsened during pregnancy. The drum is normal, there is a 30 dB air-bone gap with a bone-conduction dip at 2000 Hz, and acoustic reflexes are absent. What explains the 2000 Hz dip?

- **Correct:** A mechanical bone-conduction artifact of fixation
- Distractor: Cochlear hair-cell loss at the 2 kHz place — _why wrong:_ True cochlear loss would not improve after surgery, whereas the Carhart notch usually does.
- Distractor: Masking crossover elevating that threshold — _why wrong:_ Overmasking is a testing error at any frequency; the Carhart notch is a reproducible fixation effect.
- Distractor: Pregnancy-related strial dysfunction — _why wrong:_ Pregnancy can accelerate otosclerosis, but the notch reflects ossicular mechanics, not the stria.

Explanation: The Carhart notch reflects loss of the ossicular-chain resonance contribution to bone-conducted sound when the stapes is fixed. Absent reflexes and an air-bone gap with a normal drum complete the picture. Because it is mechanical, it often closes after stapedotomy.

Pearl: Normal drum + air-bone gap + absent reflexes = otosclerosis; present reflexes should make you think third window.

## T-otology-36 — Ototoxic / Noise-Induced Hearing Loss
_source: pathophys_v470/otology_a.py_

**T-otology-36.overview**

Ototoxic hearing loss comes from drugs such as aminoglycosides and cisplatin; noise-induced loss comes from acoustic overexposure. Both are largely preventable, typically start in the high frequencies, and require monitoring in at-risk patients.

**T-otology-36.physiology**

**Outer hair cells are vulnerable**: they have high metabolic demand and are the first to fail with toxic or mechanical stress, beginning at the high-frequency base. **Antioxidant defenses**: glutathione and related systems protect hair cells from reactive oxygen species. **Ribbon synapses**: inner hair cells connect to auditory nerve fibers through glutamatergic synapses that can be injured independently of hair cells. **Middle ear reflex**: the stapedius reflex dampens sustained loud low-frequency sound but is too slow to protect against impulse noise.

**T-otology-36.pathophysiology**

**Aminoglycosides**: accumulate in hair cells, generate free radicals by forming iron complexes, and trigger apoptosis; gentamicin is more vestibulotoxic and amikacin more cochleotoxic. **Mitochondrial susceptibility**: the m.1555A>G mitochondrial rRNA mutation makes ribosomes resemble bacterial ones, causing profound loss after a single aminoglycoside dose. **Cisplatin**: produces reactive oxygen species in outer hair cells and the stria vascularis, causing dose-dependent, bilateral, permanent high-frequency loss; sodium thiosulfate can reduce it in children with localized cancer. **Loop diuretics**: inhibit the Na-K-2Cl transporter in the stria vascularis, reducing the endocochlear potential (usually reversible, but synergistic with aminoglycosides). **Noise**: intense sound causes metabolic exhaustion and oxidative stress (temporary threshold shift), and with repeated exposure, permanent hair-cell loss maximal near 4 kHz (the notch). **Acoustic trauma**: very loud impulse noise mechanically tears cochlear structures. **Hidden hearing loss**: noise can destroy synapses before thresholds change, causing difficulty hearing in noise with a normal audiogram.

### CC-otology-36.1 (concept check)

Stem: A patient receiving cisplatin develops bilateral tinnitus. Why do the first audiometric changes usually appear at the highest frequencies?

- **Correct:** Basal outer hair cells are injured first
- Distractor: Apical inner hair cells encode high pitch — _why wrong:_ The base encodes high frequencies and the apex low frequencies.
- Distractor: Cisplatin targets the auditory nerve first — _why wrong:_ Cisplatin mainly injures outer hair cells and the stria vascularis.
- Distractor: High tones are tested at louder levels — _why wrong:_ Test intensity does not explain the injury pattern.

Explanation: Basal outer hair cells have high metabolic demand and lower antioxidant capacity, so cisplatin and aminoglycosides injure them first. Extended high-frequency monitoring detects loss before speech frequencies are affected.

Pearl: Ototoxicity starts at the base: monitor high frequencies before and during therapy.

## T-otology-37 — Patulous Eustachian Tube Dysfunction
_source: pathophys_v470/otology_b.py_

**T-otology-37.overview**

Patulous Eustachian tube dysfunction is failure of the tube to close, so the middle ear stays open to the nasopharynx. It causes autophony and hearing one's own breathing, and it is often mistaken for dilatory ETD or superior canal dehiscence.

**T-otology-37.physiology**

**Normal closure**: the cartilaginous tube is held closed by elastic recoil, the Ostmann fat pad, and surrounding tissue tension. **Protective role**: closure shields the middle ear from voice and breathing pressures.

**T-otology-37.pathophysiology**

**Loss of closing tissue**: weight loss shrinks the Ostmann fat pad; pregnancy, hormonal changes, radiation, and neuromuscular disease reduce closing forces. **Symptoms**: voice and breathing sounds transmit directly into the middle ear, causing autophony, a sense of fullness, and audible breathing. **Positional relief**: lying down or lowering the head increases venous congestion around the tube, temporarily closing it. **Exam clue**: the tympanic membrane moves with nasal respiration, especially with ipsilateral nostril breathing. **Sniffing habit**: patients learn to sniff to lock the tube closed with negative pressure, which can cause retraction and even cholesteatoma. **Distinguishing SCD**: SCD autophony includes eye movements and footsteps and has third-window audiometric findings; patulous tubes do not.

### CC-otology-37.1 (concept check)

Stem: A 25-year-old who lost 20 kg hears her own breathing and an echo of her voice; symptoms vanish when she lies down. What explains relief when supine?

- **Correct:** Peritubal venous congestion closes the tube
- Distractor: Middle-ear fluid drains with gravity — _why wrong:_ There is no fluid; the problem is an abnormally open tube.
- Distractor: Tensor veli palatini tone increases — _why wrong:_ Tensor tone does not change meaningfully with position.
- Distractor: Intracranial pressure falls when supine — _why wrong:_ ICP rises when supine; the mechanism is venous engorgement.

Explanation: Weight loss shrinks the Ostmann fat pad, leaving the tube patent. Supine positioning engorges peritubal veins, closing it. A drum that moves with nasal breathing confirms the diagnosis.

Pearl: Autophony relieved by lying down suggests patulous ETD; autophony of footsteps and eye movements suggests SCD.

## T-otology-38 — Perilymph Fistula / Inner-Ear Window Leak
_source: pathophys_v470/otology_b.py_

**T-otology-38.overview**

A perilymph fistula is an abnormal leak of perilymph from the inner ear into the middle ear, usually at the oval or round window, after barotrauma, stapes surgery, or trauma. It causes fluctuating hearing loss and pressure-related vertigo and remains a controversial, hard-to-prove diagnosis.

**T-otology-38.physiology**

**Window membranes**: the round window membrane and the annular ligament of the oval window are the thin barriers between perilymph and the middle-ear air space. **Perilymph continuity**: perilymph connects with CSF through the cochlear aqueduct.

**T-otology-38.pathophysiology**

**Implosive pathway**: sudden middle-ear pressure increase (Valsalva against a closed nose, airplane descent, diving) pushes the windows inward and ruptures them. **Explosive pathway**: sudden CSF pressure increase (straining, lifting) is transmitted through the cochlear aqueduct, blowing the window out. **Fluid loss effects**: loss of perilymph and air entry alter inner-ear mechanics and hair-cell function, causing SNHL, tinnitus, and imbalance. **Pressure sensitivity**: changes in middle-ear pressure move fluid through the leak, producing a positive fistula test or Hennebert sign. **Diagnosis difficulty**: no reliable noninvasive test exists; exploration and window patching are both diagnostic and therapeutic, and spontaneous closure occurs.

### CC-otology-38.1 (concept check)

Stem: A scuba diver develops sudden hearing loss and vertigo after a difficult descent with forceful Valsalva. What mechanism describes an implosive window rupture?

- **Correct:** Middle-ear pressure surge pushing the window inward
- Distractor: CSF pressure surge via the cochlear aqueduct — _why wrong:_ That is the explosive mechanism, typically from straining or lifting.
- Distractor: Nitrogen bubbles forming in endolymph — _why wrong:_ Inner-ear decompression sickness occurs on ascent, not descent barotrauma.
- Distractor: Fracture of an otosclerotic stapes footplate — _why wrong:_ Otosclerosis does not cause acute window rupture.

Explanation: Forceful Valsalva against a blocked Eustachian tube abruptly raises middle-ear pressure, rupturing the windows inward. Perilymph loss disrupts cochlear and vestibular function.

Pearl: Separate inner-ear barotrauma (descent) from decompression sickness (ascent): treatment differs.

## T-otology-39 — Persistent Postural-Perceptual Dizziness (PPPD)
_source: pathophys_v470/otology_b.py_

**T-otology-39.overview**

PPPD is chronic (3 months or more) non-spinning dizziness or unsteadiness, worsened by upright posture, motion, and complex visual environments, usually triggered by an earlier vestibular or medical event. It is a functional disorder of how the brain controls balance, treated with vestibular rehabilitation, SSRIs/SNRIs, and CBT.

**T-otology-39.physiology**

**Postural control strategies**: after a vestibular insult, the brain shifts toward vision and stiff, high-vigilance postural control. **Normal recovery**: once the insult resolves or is compensated, the brain returns to relaxed, automatic balance control. **Threat networks**: anxiety and attention networks interact with vestibular and visual processing.

**T-otology-39.pathophysiology**

**Failure to readapt**: the brain stays locked in high-threat postural control and visual dependence after the precipitating event resolves. **Visual dependence**: overreliance on vision makes busy patterns, scrolling screens, and supermarkets provocative. **Maintenance cycle**: anxiety and hypervigilance about balance increase the abnormal strategy, which increases symptoms. **Normal tests**: the vestibular battery is usually normal or shows only a compensated old lesion, which is why it is a positive diagnosis based on criteria rather than exclusion alone. **Treatment logic**: habituation-based rehabilitation retrains automatic balance, serotonergic medications reduce threat sensitivity, and CBT addresses avoidance.

### CC-otology-39.1 (concept check)

Stem: A 44-year-old had vestibular neuritis 6 months ago. Testing is now compensated, but she has daily unsteadiness worse in supermarkets and when scrolling her phone. What best explains her symptoms?

- **Correct:** Persistent visual dependence
- Distractor: Recurrent viral vestibular neuritis — _why wrong:_ Recurrence would cause acute vertigo and new test abnormalities.
- Distractor: Undiagnosed bilateral vestibular loss — _why wrong:_ Testing is compensated, and bilateral loss causes oscillopsia rather than visual triggers.
- Distractor: Benign paroxysmal positional vertigo — _why wrong:_ BPPV causes brief positional vertigo, not constant unsteadiness.

Explanation: PPPD is a functional disorder in which balance control stays locked in a stiff, visually dependent, high-threat strategy after the trigger resolves. Habituation-based rehabilitation, SSRIs or SNRIs, and CBT retrain it.

Pearl: Chronic non-spinning dizziness worse with visual motion after a vestibular event = PPPD.

## T-otology-40 — Petrous Apex Lesions
_source: pathophys_v470/otology_b.py_

**T-otology-40.overview**

Petrous apex lesions range from benign incidental findings (asymmetric pneumatization, effusion) to cholesterol granuloma, cholesteatoma, mucocele, apicitis, and tumors. The key skill is distinguishing them by CT and MRI signal so that only lesions that need treatment get it.

**T-otology-40.physiology**

**Location**: the petrous apex is the medial part of the temporal bone, anteromedial to the inner ear, between the IAC, carotid canal, Meckel cave, and Dorello canal (CN VI). **Pneumatization**: about a third of people have pneumatized apices, often asymmetric; marrow-filled apices appear bright on T1 MRI due to fat. **Drainage**: apex air cells drain through narrow tracts toward the middle ear and mastoid.

**T-otology-40.pathophysiology**

**Cholesterol granuloma**: obstruction of a pneumatized apex causes negative pressure, mucosal hemorrhage, and breakdown of red cells into cholesterol crystals that incite a foreign-body reaction and slow expansion; it is bright on both T1 and T2. **Cholesteatoma or epidermoid**: trapped squamous epithelium is T1 dark, T2 bright, and restricts diffusion. **Effusion and asymmetric marrow**: trapped fluid or fat without bone expansion is usually incidental and should not be treated. **Apicitis**: infection spreading from the mastoid into apex cells produces Gradenigo syndrome (otorrhea, retro-orbital pain from CN V, abducens palsy). **Symptoms from neighbors**: expanding lesions compress CN V, CN VI, VII and VIII, or the IAC, causing facial pain, diplopia, facial weakness, and hearing loss. **Treatment logic**: symptomatic expansile lesions are drained (cholesterol granuloma) or removed (cholesteatoma) through approaches chosen to protect hearing and the carotid.

### CC-otology-40.1 (concept check)

Stem: An MRI shows an expansile petrous apex lesion that is bright on both T1 and T2 and does not restrict diffusion. What is the most likely diagnosis?

- **Correct:** Cholesterol granuloma
- Distractor: Epidermoid cyst — _why wrong:_ Epidermoids are T1 dark and T2 bright with restricted diffusion.
- Distractor: Asymmetric fatty marrow — _why wrong:_ Marrow is T1 bright but not expansile and suppresses with fat saturation.
- Distractor: Trapped apical effusion — _why wrong:_ Effusion is T1 dark and T2 bright without expansion.

Explanation: Obstruction of a pneumatized apex leads to hemorrhage and cholesterol crystal formation, which is bright on T1 and T2. Expansion separates it from incidental findings that should not be treated.

Pearl: Bright on T1 and T2 in the petrous apex = cholesterol granuloma.

## T-otology-41 — Ramsay Hunt Syndrome (Herpes Zoster Oticus)
_source: pathophys_v470/otology_b.py_

**T-otology-41.overview**

Ramsay Hunt syndrome is varicella-zoster reactivation in the geniculate ganglion causing facial paralysis, painful vesicular eruption of the ear, and often hearing loss and vertigo. It has a worse prognosis than Bell palsy and is treated with antivirals plus steroids.

**T-otology-41.physiology**

**Geniculate ganglion**: contains sensory cell bodies of CN VII (nervus intermedius), including general sensation from the concha and posterior canal skin and taste from the anterior two-thirds of the tongue. **Proximity**: CN VII and VIII run together in the IAC, so inflammation can spread between them. **Varicella-zoster latency**: after primary chickenpox, VZV stays latent in sensory ganglia, held in check by cell-mediated immunity. **Narrow canal**: as in Bell palsy, swelling within the bony fallopian canal compresses the nerve.

**T-otology-41.pathophysiology**

**Reactivation**: latent VZV in the geniculate ganglion reactivates with declining cell-mediated immunity. **Neural inflammation**: inflammation spreads along CN VII and to CN VIII, causing paralysis, SNHL, and vertigo; other cranial nerves may be involved. **Vesicles**: in the sensory distribution of CN VII (concha, canal, auricle) and sometimes the palate or tongue; zoster sine herpete occurs without vesicles. **Worse prognosis**: more extensive neural destruction and degeneration than Bell palsy, so complete recovery is less common. **Treatment logic**: antivirals reduce viral replication and steroids reduce inflammation; vaccination reduces zoster risk.

### CC-otology-41.1 (concept check)

Stem: A 65-year-old has facial paralysis, vesicles in the concha, hearing loss, and vertigo. Why is the prognosis worse than in Bell palsy?

- **Correct:** Greater viral nerve destruction
- Distractor: The lesion is central rather than peripheral — _why wrong:_ Ramsay Hunt is a peripheral facial nerve lesion.
- Distractor: Antiviral therapy is ineffective here — _why wrong:_ Antivirals plus steroids are standard treatment.
- Distractor: Steroids are contraindicated in zoster — _why wrong:_ Steroids are used with antivirals.

Explanation: VZV reactivation in the geniculate ganglion causes more extensive neural inflammation and degeneration than Bell palsy, often involving CN VIII.

Pearl: Vesicles + facial palsy + hearing loss = Ramsay Hunt; treat with antivirals and steroids.

## T-otology-42 — Sudden Sensorineural Hearing Loss
_source: pathophys_v470/otology_a.py_

**T-otology-42.overview**

Sudden sensorineural hearing loss (SSNHL) is at least a 30 dB loss in three consecutive frequencies developing within 72 hours. It is an otologic urgency: most cases are idiopathic, treatment works best early, and a small but important fraction hide a vestibular schwannoma or other retrocochlear cause.

**T-otology-42.physiology**

**Cochlear transduction**: outer hair cells amplify basilar-membrane motion (the cochlear amplifier) and inner hair cells convert vibration into spiral ganglion firing. **Endocochlear potential**: the stria vascularis pumps potassium into endolymph, generating a +80 mV potential that drives hair-cell transduction current; this is metabolically demanding. **Blood supply**: the labyrinthine artery (usually from AICA) is an end artery with no collateral supply, so the cochlea is very sensitive to ischemia. **Tonotopy**: the base encodes high frequencies and the apex low frequencies, which explains audiometric patterns such as low-frequency or flat losses.

**T-otology-42.pathophysiology**

**Idiopathic in about 90 percent**: leading hypotheses are viral cochleitis, microvascular compromise, and immune-mediated injury; none is proven for an individual patient. **Vascular theory**: the cochlea's end-artery supply and high metabolic demand mean brief ischemia can damage the stria and hair cells abruptly. **Viral/inflammatory theory**: inflammation and cytokine release disrupt hair cells and strial function; this is the rationale for corticosteroids, which reduce cochlear inflammation and stabilize the stria. **Membrane rupture**: rarely, a break between perilymph and endolymph (or a window leak) mixes potassium-rich fluid and depolarizes hair cells. **Retrocochlear causes**: vestibular schwannoma can present as sudden loss through acute compression or vascular compromise of the cochlear nerve or artery, which is why MRI is part of the workup. **Why timing matters**: steroid benefit is greatest in the first two weeks, and intratympanic steroid achieves far higher perilymph concentrations than oral dosing, making it the salvage route.

### CC-otology-42.1 (concept check)

Stem: A 48-year-old wakes with right-sided hearing loss and tinnitus. Otoscopy is normal, Weber lateralizes left, and Rinne is positive bilaterally. Which anatomic fact best explains the cochlea's vulnerability under the vascular theory?

- **Correct:** Its labyrinthine artery is an end artery
- Distractor: It is supplied by both carotid systems — _why wrong:_ The labyrinthine artery (usually from AICA) is a single end artery, which is why ischemia is poorly tolerated.
- Distractor: Its hair cells depend on endolymph capillaries — _why wrong:_ Endolymph is avascular; the stria vascularis depends entirely on labyrinthine flow.
- Distractor: Its spiral ganglion lies outside the otic capsule — _why wrong:_ The spiral ganglion lies within the modiolus of the otic capsule.

Explanation: Weber to the opposite side with positive Rinne confirms a right sensorineural loss. The stria vascularis has very high metabolic demand and a single end-artery supply, so brief ischemia can injure it. Treatment is time-sensitive steroids plus MRI to exclude a retrocochlear lesion.

Pearl: Normal ear exam plus sudden unilateral SNHL is urgent: treat promptly and image for retrocochlear disease.

## T-otology-43 — Superior Canal Dehiscence
_source: pathophys_v470/otology_a.py_

**T-otology-43.overview**

Superior canal dehiscence (SCD) is absent bone over the superior semicircular canal, creating a third mobile window into the inner ear. It explains sound- or pressure-induced vertigo, autophony, and a conductive-appearing loss with normal middle-ear function.

**T-otology-43.physiology**

**Two-window system**: normally the inner ear has only two mobile windows, the oval window (input) and round window (pressure release), so stapes motion drives fluid along the cochlea. **Superior canal position**: it arches toward the middle cranial fossa floor and is covered by a thin bony layer under the temporal lobe dura. **Canal stimulation**: semicircular canals sense angular acceleration through endolymph flow deflecting the cupula. **Bone conduction physiology**: cochlear bone-conduction sensitivity depends partly on the impedance difference between the two windows.

**T-otology-43.pathophysiology**

**Third window**: a dehiscence lets sound energy and pressure shunt away from the cochlea into the superior canal. **Sound- and pressure-induced vertigo**: shunted energy moves endolymph in the canal, deflecting its cupula (Tullio phenomenon with sound, Hennebert sign with pressure), with eye movements in the plane of the superior canal. **Air-bone gap with normal middle ear**: air conduction worsens because energy leaks away from the cochlea, while bone conduction improves (can be better than 0 dB) because the third window lowers inner-ear impedance on that side. **Reflexes present**: unlike otosclerosis, the stapes moves normally, so acoustic reflexes are present, which is a key discriminator. **Autophony**: patients hear their own voice, eye movements, footsteps, or pulse loudly through the bone-conduction pathway. **VEMP changes**: cervical VEMP thresholds are abnormally low and ocular VEMP amplitudes are high because the third window increases vestibular sensitivity to sound.

### CC-otology-43.1 (concept check)

Stem: A 45-year-old hears her own footsteps and eye movements, and loud sounds make the room tilt. Audiometry shows a low-frequency air-bone gap with bone conduction better than 0 dB, and acoustic reflexes are present. What is the mechanism?

- **Correct:** A third window that shunts acoustic energy
- Distractor: Stapes fixation at the oval window — _why wrong:_ Fixation would abolish reflexes and would not cause sound-induced vertigo.
- Distractor: Hydrops distorting the cochlear apex — _why wrong:_ Hydrops causes low-frequency SNHL and episodic vertigo, not supranormal bone conduction.
- Distractor: A patulous Eustachian tube — _why wrong:_ Patulous ETD causes autophony of voice and breathing, but not of footsteps or eye movements.

Explanation: A dehiscent superior canal creates a third mobile window. Air-conducted energy leaks into the canal (worse air thresholds, Tullio phenomenon) while bone conduction improves. Present reflexes distinguish it from otosclerosis, and VEMP thresholds are abnormally low.

Pearl: Air-bone gap with present reflexes and supranormal bone conduction = look for a third window.

## T-otology-44 — Temporal Bone Anatomy
_source: pathophys_v470/otology_a.py_

**T-otology-44.overview**

Temporal bone anatomy is the map behind every otologic diagnosis and operation, from reading a CT to drilling a mastoid safely. Mastering it means knowing the landmarks that protect the facial nerve, labyrinth, sigmoid sinus, jugular bulb, carotid, and dura.

**T-otology-44.physiology**

**Five parts**: squamous, mastoid, petrous, tympanic, and styloid portions. **Facial nerve course**: labyrinthine segment (narrowest, no collaterals), geniculate ganglion (GSPN exits), tympanic segment above the oval window, second genu at the lateral canal, and mastoid segment to the stylomastoid foramen. **Labyrinth**: cochlea (two and a half turns), vestibule (utricle and saccule), and three semicircular canals; the lateral canal is the key mastoid landmark. **Middle-ear walls**: tegmen superiorly, jugular bulb inferiorly, carotid anteriorly, promontory and windows medially, aditus and pyramidal eminence posteriorly. **Mastoid landmarks**: Macewen triangle overlies the antrum; the sinodural angle, digastric ridge (leads to stylomastoid foramen), and Trautmann triangle guide dissection. **Pneumatization**: air cells develop from the antrum after birth, driven by middle-ear ventilation; poor ventilation leaves a sclerotic mastoid.

**T-otology-44.pathophysiology**

**Why the labyrinthine segment matters**: it is the narrowest part of the fallopian canal, so inflammatory edema (Bell palsy) or fracture compression there causes ischemic nerve injury. **Dehiscence**: the tympanic segment is naturally dehiscent in a substantial minority of ears, which is why it is vulnerable during middle-ear surgery and cholesteatoma removal. **Spread of disease follows anatomy**: infection travels through air-cell tracts to the petrous apex (Gradenigo), through the tegmen to the dura and temporal lobe, and medial to the sigmoid sinus causing thrombosis. **Fracture patterns**: otic-capsule-violating fractures cross the labyrinth and cause SNHL and vertigo, while sparing fractures more often disrupt the ossicles and cause conductive loss. **Third windows**: missing bone over the superior canal or other labyrinth segments creates abnormal fluid mechanics (superior canal dehiscence physiology).

### CC-otology-44.1 (concept check)

Stem: During a canal-wall-up mastoidectomy the resident has identified the lateral semicircular canal. Which structure lies just inferior to it and is most at risk while opening the facial recess?

- **Correct:** The second genu of VII
- Distractor: The sigmoid sinus — _why wrong:_ The sigmoid sinus forms the posterior boundary of the mastoid, not the area just below the lateral canal.
- Distractor: The jugular bulb — _why wrong:_ The jugular bulb lies far inferior, in the hypotympanum and infralabyrinthine region.
- Distractor: The tegmen mastoideum — _why wrong:_ The tegmen is the superior boundary of the mastoid, above the lateral canal.

Explanation: The lateral semicircular canal is the key mastoid landmark: the facial nerve's second genu lies just inferior to it before descending as the mastoid segment. The facial recess is opened lateral to the nerve and medial to the chorda tympani.

Pearl: Find the lateral canal and you have found the level of the second genu.

## T-otology-45 — Temporal Bone Fracture
_source: pathophys_v470/otology_a.py_

**T-otology-45.overview**

Temporal bone fractures result from high-energy head trauma and threaten hearing, balance, the facial nerve, and the dura. Modern classification by otic capsule involvement predicts complications better than the old longitudinal/transverse scheme.

**T-otology-45.physiology**

**Otic capsule density**: the labyrinthine bone is very dense, so fractures often travel around it through weaker pneumatized bone. **Neighbors at risk**: the facial nerve (especially perigeniculate region), ossicular chain, tegmen and dura, carotid canal, sigmoid sinus, and jugular bulb. **Otic capsule healing**: it heals by fibrous union rather than bone, leaving a permanent path for infection to the meninges.

**T-otology-45.pathophysiology**

**Otic capsule-sparing fractures** (most common, lateral blows): run through the squama and EAC, causing hemotympanum, TM tears, and conductive loss from ossicular disruption. **Otic capsule-violating fractures** (occipital blows): cross the cochlea or vestibule, causing profound SNHL and vertigo and carry higher rates of facial paralysis and CSF leak. **Facial nerve injury**: the perigeniculate area is most often injured, through edema, compression by bone fragments, or transection; immediate complete paralysis implies a severe injury, while delayed onset implies edema and a good prognosis. **CSF leak**: tegmen and dural tears let CSF drain through the middle ear into the canal (otorrhea) or down the Eustachian tube (rhinorrhea); most close spontaneously within 7-10 days. **Meningitis risk**: persistent communication and fibrous-only otic capsule healing create long-term meningitis risk, relevant to pneumococcal vaccination. **Labyrinthine concussion and BPPV**: even without a fracture line, trauma can damage hair cells or dislodge otoconia.

### CC-otology-45.1 (concept check)

Stem: A motorcyclist with an occipital blow has profound right sensorineural loss, spontaneous nystagmus, and immediate complete right facial paralysis. Which fracture pattern best explains this?

- **Correct:** Otic capsule-violating fracture
- Distractor: Otic capsule-sparing fracture — _why wrong:_ Capsule-sparing fractures usually cause conductive loss and hemotympanum with lower facial nerve risk.
- Distractor: Isolated incus dislocation — _why wrong:_ Ossicular injury causes conductive loss, not profound SNHL with nystagmus.
- Distractor: Labyrinthine concussion alone — _why wrong:_ Concussion does not explain immediate complete facial paralysis.

Explanation: Capsule-violating fractures cross the cochlea or vestibule, destroying hearing and balance, and carry higher rates of facial paralysis and CSF leak. Immediate complete paralysis suggests transection or severe compression and prompts evaluation for exploration.

Pearl: Immediate complete facial paralysis after trauma is a surgical question; delayed onset usually recovers.

## T-otology-46 — Tinnitus
_source: pathophys_v470/otology_a.py_

**T-otology-46.overview**

Tinnitus is the perception of sound without an external source; most is subjective and linked to hearing loss. The clinical job is to identify red flags (unilateral, pulsatile, objective) and then manage bothersome tinnitus with counseling, amplification, and CBT.

**T-otology-46.physiology**

**Central gain**: the auditory system adjusts its sensitivity to match input; reduced cochlear input increases gain in the cochlear nucleus, inferior colliculus, and cortex. **Spontaneous activity**: auditory neurons fire spontaneously even in silence, and the brain normally filters this out. **Limbic and attention networks**: the amygdala, prefrontal cortex, and autonomic systems determine whether a sound is perceived as threatening or distressing.

**T-otology-46.pathophysiology**

**Deafferentation model**: hair-cell or synaptic loss reduces input in a frequency region; central neurons increase gain and spontaneous synchronous firing, which is perceived as sound, often matching the hearing-loss frequency. **Why distress varies**: limbic and attentional networks amplify perception and emotional response, explaining why CBT and counseling reduce bother without changing loudness. **Somatic modulation**: neck and jaw inputs to the dorsal cochlear nucleus explain tinnitus changes with jaw clenching or neck movement. **Pulsatile tinnitus**: a vascular sound reaching the cochlea (paraganglioma, dural AV fistula, sigmoid sinus diverticulum or dehiscence, idiopathic intracranial hypertension, carotid disease) and requires imaging. **Objective tinnitus**: audible to the examiner, from vascular sources or muscle (palatal or middle-ear myoclonus). **Unilateral tinnitus**: asymmetric neural pathology such as vestibular schwannoma must be excluded with MRI when accompanied by asymmetric hearing.

### CC-otology-46.1 (concept check)

Stem: A 62-year-old has bilateral high-pitched tinnitus that matches a bilateral 4-8 kHz sensorineural loss. Why does the tinnitus pitch match the hearing-loss region?

- **Correct:** Central gain rises in deafferented channels
- Distractor: Damaged hair cells emit audible tones — _why wrong:_ Spontaneous emissions rarely cause clinical tinnitus, and damaged hair cells emit less, not more.
- Distractor: The stapedius muscle is in tonic spasm — _why wrong:_ Middle-ear myoclonus causes clicking objective tinnitus, not steady tones.
- Distractor: Turbulent cochlear blood flow is heard — _why wrong:_ Vascular sounds cause pulsatile tinnitus, not steady high-pitched tones.

Explanation: Reduced cochlear input leads central auditory neurons to increase gain and synchronous firing in those frequency channels, perceived as sound. Limbic and attention networks shape distress, which is why counseling, amplification, and CBT help.

Pearl: Most tinnitus is the brain's response to hearing loss: treat the loss and the distress.

## T-otology-47 — Tympanic Membrane Perforation
_source: pathophys_v470/otology_a.py_

**T-otology-47.overview**

A tympanic membrane perforation is a hole in the drum from infection, trauma, or prior tube placement. Most traumatic perforations heal on their own; persistent ones cause conductive loss and recurrent otorrhea and are repaired by tympanoplasty.

**T-otology-47.physiology**

**Layers**: lateral squamous epithelium, middle fibrous lamina propria (radial and circular fibers), and medial mucosa. **Pars tensa vs flaccida**: the tensa has an organized fibrous layer and is anchored by the fibrous annulus; the flaccida is above the lateral process of the malleus and lacks organized fibers. **Healing**: epithelium migrates across the defect from the edges, using a scaffold; the fibrous layer often does not regenerate fully, leaving a thin monomeric scar. **Sound transmission**: the drum collects sound over a large area and couples it to the malleus; it also shields the round window so sound reaches the two windows out of phase.

**T-otology-47.pathophysiology**

**Conductive loss**: loss of surface area reduces the hydraulic ratio, and sound reaching the round window directly diminishes the phase difference between the windows. **Size and location**: larger and posterior-inferior perforations (near the round window) cause greater loss; loss over 40 dB suggests an additional ossicular problem. **Why some fail to heal**: infection, large size, marginal location involving the annulus, and squamous epithelium turning in over the edge (preventing migration across the gap). **Marginal perforations**: they involve the annulus and can allow squamous epithelium to migrate into the middle ear, causing secondary acquired cholesteatoma. **Otorrhea**: an open middle ear is exposed to water and canal bacteria, leading to recurrent drainage. **Traumatic perforations**: slap or blast injuries usually heal within weeks if kept dry; vertigo or sensorineural loss signals possible stapes subluxation or perilymph fistula.

### CC-otology-47.1 (concept check)

Stem: A 25-year-old has a small central perforation 2 weeks after a slap injury, with a 15 dB conductive loss and no vertigo. Which feature most predicts healing without surgery?

- **Correct:** A small defect with healthy, intact edges
- Distractor: Extension of the defect to the annulus — _why wrong:_ Marginal perforations heal less reliably and can let squamous epithelium into the middle ear.
- Distractor: Vertigo with sensorineural loss after injury — _why wrong:_ Vertigo or SNHL suggests stapes or inner-ear injury, not a better prognosis.
- Distractor: Persistent otorrhea from the perforation — _why wrong:_ Infection impairs epithelial migration and healing.

Explanation: Traumatic central perforations usually heal because epithelium migrates across from healthy edges if the ear stays dry. Large, marginal, infected, or long-standing perforations are less likely to close.

Pearl: A traumatic perforation with vertigo or SNHL is no longer simple: think inner-ear injury.

## T-otology-48 — Tympanometry / Acoustic Reflexes
_source: pathophys_v470/otology_a.py_

**T-otology-48.overview**

Tympanometry measures how the tympanic membrane and middle ear accept sound energy as canal pressure changes; acoustic reflexes test the stapedius reflex arc. Together they identify effusion, perforation, fixation, discontinuity, and some retrocochlear or facial nerve problems in minutes.

**T-otology-48.physiology**

**Admittance**: a probe tone (226 Hz in adults) is played while canal pressure is swept; admittance peaks when canal pressure equals middle-ear pressure. **Key measures**: peak pressure (middle-ear pressure), peak height (static admittance or compliance), and ear-canal volume. **Reflex arc**: CN VIII to the cochlear nucleus, to both superior olivary complexes, to both facial motor nuclei, and out CN VII to the stapedius in both ears. **Ipsilateral and contralateral reflexes**: stimulating one ear normally triggers the reflex in both ears, so the pattern of present and absent reflexes localizes the lesion. **Infant probe tone**: a 1000 Hz probe is used under about 6 months because the infant canal wall is compliant and distorts 226 Hz results.

**T-otology-48.pathophysiology**

**Type A**: normal peak and pressure. **Type As**: shallow peak from a stiff system such as otosclerosis or a thick drum. **Type Ad**: a very tall peak from a flaccid drum or ossicular discontinuity. **Type B with normal volume**: no peak because fluid fills the middle ear (effusion) and the drum cannot move. **Type B with large volume**: the probe measures the canal plus middle ear through a perforation or patent tube. **Type B with small volume**: the probe is against wax or the canal wall. **Type C**: negative peak pressure from Eustachian tube dysfunction and gas absorption. **Reflex logic**: a conductive loss in the probe ear abolishes reflexes recorded there; a retrocochlear lesion abolishes reflexes when the affected ear is stimulated; a facial nerve lesion proximal to the stapedius abolishes reflexes recorded on that side. **Reflex decay**: inability to sustain the reflex for 10 seconds at 10 dB above threshold suggests retrocochlear disease.

### CC-otology-48.1 (concept check)

Stem: A child has a flat (type B) tympanogram in the right ear. Measured canal volume is 2.5 mL, versus 0.8 mL on the left. What does this combination indicate?

- **Correct:** An open perforation or patent tube
- Distractor: Effusion behind an intact drum — _why wrong:_ Effusion gives a flat tracing with normal canal volume, not an enlarged one.
- Distractor: Cerumen blocking the probe tip — _why wrong:_ Wax or probe-against-wall gives a flat tracing with an abnormally small volume.
- Distractor: Disarticulation of the ossicles — _why wrong:_ Discontinuity produces a very tall (type Ad) peak, not a flat tracing.

Explanation: Read every flat tympanogram by its volume: normal volume means effusion, large volume means perforation or patent tube, small volume means wax or poor probe placement.

Pearl: Flat tympanogram? Read the volume before calling it fluid.

## T-otology-49 — Vernet Syndrome (Jugular Foramen Syndrome)
_source: pathophys_v470/otology_b.py_

**T-otology-49.overview**

Vernet syndrome is paralysis of CN IX, X, and XI from a lesion at the jugular foramen. It is a localizing pattern pointing to paraganglioma, schwannoma, meningioma, metastasis, or skull-base infection.

**T-otology-49.physiology**

**Jugular foramen contents**: the pars nervosa holds CN IX and the inferior petrosal sinus; the pars vascularis holds CN X, CN XI, and the jugular bulb. **Functions**: CN IX (posterior tongue taste, pharyngeal sensation), CN X (palate, pharynx, larynx), CN XI (SCM and trapezius).

**T-otology-49.pathophysiology**

**Combined palsy**: dysphagia, hoarseness from vocal fold paralysis, loss of gag, palatal deviation toward the healthy side, and shoulder weakness. **Extension**: involvement of CN XII via the hypoglossal canal produces Collet-Sicard syndrome; involvement of sympathetics (retroparotid) produces Villaret syndrome. **Lower cranial nerve tolerance**: sudden loss causes severe aspiration, while slow tumor growth allows compensation, which shapes treatment choices.

### CC-otology-49.1 (concept check)

Stem: A patient has dysphagia, hoarseness, an absent gag, and ipsilateral shoulder weakness. Which location explains this combination?

- **Correct:** Jugular foramen
- Distractor: Internal auditory canal — _why wrong:_ IAC lesions affect CN VII and VIII.
- Distractor: Cavernous sinus — _why wrong:_ Cavernous lesions affect CN III, IV, V1, V2, and VI.
- Distractor: Hypoglossal canal — _why wrong:_ A hypoglossal canal lesion affects CN XII alone.

Explanation: The jugular foramen contains CN IX, X, and XI. Paragangliomas, schwannomas, meningiomas, and metastases cause Vernet syndrome.

Pearl: IX + X + XI = jugular foramen.

## T-otology-50 — Vestibular Migraine
_source: pathophys_v470/otology_a.py_

**T-otology-50.overview**

Vestibular migraine is recurrent vestibular symptoms (5 minutes to 72 hours) in a person with migraine, with migraine features during at least half of episodes. It is one of the most common causes of recurrent vertigo and is often mistaken for Ménière disease.

**T-otology-50.physiology**

**Shared circuits**: the trigeminal nociceptive system and vestibular nuclei are interconnected, and both project to the thalamus and cortex. **Multisensory integration**: balance depends on integrating vestibular, visual, and proprioceptive signals in the vestibular nuclei, cerebellum, and cortex. **Inner-ear vasculature**: the labyrinth is innervated by trigeminal fibers that can release vasoactive neuropeptides.

**T-otology-50.pathophysiology**

**Central hyperexcitability**: migraine brains show altered cortical and brainstem excitability; cortical spreading depression and brainstem activation can involve vestibular pathways. **Neurogenic inflammation**: trigeminal release of CGRP and substance P may alter inner-ear blood flow and sensory function, explaining occasional auditory symptoms. **Variable presentation**: symptoms include spontaneous or positional vertigo, motion intolerance, and visual vertigo, with or without simultaneous headache. **Why hearing is usually stable**: unlike Ménière disease, progressive low-frequency hearing loss is not expected; significant progressive loss should prompt reconsideration. **Treatment rationale**: trigger management, sleep and stress regularity, and migraine preventives (tricyclics, beta-blockers, calcium-channel blockers, topiramate, CGRP pathway agents) reduce central excitability.

### CC-otology-50.1 (concept check)

Stem: A 36-year-old with lifelong migraine has recurrent attacks of vertigo lasting 2-6 hours, with photophobia during most attacks. Serial audiograms are normal. Which feature best separates this from Ménière disease?

- **Correct:** No fluctuating low-frequency hearing loss
- Distractor: Attacks lasting longer than 20 minutes — _why wrong:_ Both conditions produce attacks lasting minutes to hours.
- Distractor: Tinnitus present during the attacks — _why wrong:_ Tinnitus can occur in vestibular migraine and does not discriminate.
- Distractor: Symptoms worsened by head position — _why wrong:_ Positional sensitivity occurs in both and does not discriminate.

Explanation: Vestibular migraine is a central sensory-processing disorder linked to migraine. Documented fluctuating low-frequency SNHL points to Ménière disease, while normal serial audiograms plus migraine features support vestibular migraine.

Pearl: Serial audiograms: Ménière moves the audiogram, vestibular migraine usually does not.

## T-otology-51 — Vestibular Neuritis
_source: pathophys_v470/otology_a.py_

**T-otology-51.overview**

Vestibular neuritis is acute, continuous vertigo lasting days from sudden unilateral loss of peripheral vestibular function, presumed viral. The key bedside task is separating it from posterior-circulation stroke using HINTS.

**T-otology-51.physiology**

**Tonic balance**: each vestibular nerve fires at a resting rate; the brain senses rotation from the difference between the two sides. **Vestibulo-ocular reflex**: head rotation excites the ipsilateral horizontal canal and drives eye movement opposite the head to keep gaze stable. **Nerve divisions**: the superior vestibular nerve supplies the superior and horizontal canals and utricle; the inferior nerve supplies the posterior canal and saccule. **Central compensation**: the cerebellum and brainstem rebalance resting activity over days to weeks after a unilateral loss.

**T-otology-51.pathophysiology**

**Unilateral loss creates false rotation**: when one nerve goes silent, the intact side's resting activity is interpreted as rotation toward it, causing vertigo and nystagmus beating away from the affected ear. **Viral reactivation hypothesis**: herpes simplex type 1 latent in Scarpa ganglion is thought to reactivate, inflaming the nerve. **Superior division predominance**: the superior nerve travels in a longer, narrower bony canal, so it is affected more often, sparing the posterior canal and saccule. **Hearing spared**: the cochlear nerve is uninvolved; added hearing loss means labyrinthitis or a vascular (AICA) event. **Head impulse test**: a rapid turn toward the affected side shows a corrective catch-up saccade because the VOR is lost; a normal head impulse in acute vertigo is worrisome for stroke. **Compensation and steroids**: central compensation, accelerated by early vestibular rehabilitation, drives recovery; steroids may improve caloric recovery but not clearly long-term symptoms.

## T-otology-52 — Vestibular Rehabilitation
_source: pathophys_v470/otology_b.py_

**T-otology-52.overview**

Vestibular rehabilitation is exercise-based therapy that promotes central compensation, substitution, and habituation after vestibular injury. It is first-line for uncompensated unilateral or bilateral loss, PPPD, and chronic dizziness.

**T-otology-52.physiology**

**Adaptation**: the cerebellum adjusts VOR gain when retinal slip (image motion during head movement) signals an error. **Substitution**: vision, proprioception, and alternative eye-movement strategies replace lost vestibular function. **Habituation**: repeated exposure to provocative stimuli reduces the central response.

**T-otology-52.pathophysiology**

**Uncompensated loss**: persistent asymmetry between vestibular nuclei causes dizziness with head movement and oscillopsia. **Avoidance prevents recovery**: limiting head movement removes the error signal needed for adaptation, prolonging symptoms. **Vestibular suppressants**: prolonged use of meclizine or benzodiazepines blunts central compensation, so they should be limited to the acute phase. **Bilateral loss**: little to adapt, so therapy relies on substitution and fall prevention. **Exercise logic**: gaze stabilization (head movement while fixating a target) drives adaptation; balance and gait training builds substitution.

### CC-otology-52.1 (concept check)

Stem: Five days after vestibular neuritis, a 50-year-old is improving but still takes meclizine three times daily and avoids moving her head. Why should the suppressant be tapered and head movement encouraged?

- **Correct:** Suppressants blunt signals driving compensation
- Distractor: Meclizine is toxic to vestibular hair cells — _why wrong:_ Meclizine is not ototoxic.
- Distractor: Meclizine dislodges utricular otoconia — _why wrong:_ Meclizine does not cause BPPV.
- Distractor: Meclizine triggers later Ménière disease — _why wrong:_ There is no such link.

Explanation: Central compensation depends on error signals such as retinal slip during head movement. Suppressants and avoidance dampen these signals and delay recovery; early rehabilitation speeds it.

Pearl: Suppress only the acute phase; then move.

## T-otology-53 — Vestibular Schwannoma
_source: pathophys_v470/otology_a.py_

**T-otology-53.overview**

Vestibular schwannoma is a benign Schwann-cell tumor of the vestibular nerve in the internal auditory canal and cerebellopontine angle. It is the classic cause of asymmetric sensorineural hearing loss and the prototype lateral skull-base tumor for observation, radiation, or microsurgery decisions.

**T-otology-53.physiology**

**IAC anatomy**: the canal carries CN VII (anterosuperior), the cochlear nerve (anteroinferior), and the superior and inferior vestibular nerves (posterior), separated by the transverse crest and Bill's bar ("7-up, Coke down"). **Obersteiner-Redlich zone**: the transition between central (oligodendrocyte) and peripheral (Schwann cell) myelin lies in the IAC, near where most schwannomas arise. **Vascular supply**: the cochlea depends on the labyrinthine artery running with the nerves in the IAC. **Central compensation**: the brainstem and cerebellum recalibrate continuously when one vestibular input slowly declines.

**T-otology-53.pathophysiology**

**Genetics**: loss of the NF2 tumor-suppressor gene product (merlin) in Schwann cells removes contact inhibition; sporadic tumors are unilateral, while NF2 causes bilateral tumors. **Hearing loss mechanism**: compression of the cochlear nerve, compromise of the labyrinthine artery, and biochemical changes in inner-ear fluid explain why hearing loss does not track tumor size. **Why vertigo is uncommon**: slow vestibular loss is centrally compensated, so imbalance is more typical than vertigo. **Growth pattern**: tumors expand within the IAC then into the CPA, where large tumors compress the brainstem, CN V (facial numbness, lost corneal reflex) and the fourth ventricle (hydrocephalus). **Facial nerve tolerance**: CN VII is stretched and thinned around the tumor but motor function is usually preserved preoperatively; facial weakness at presentation suggests another diagnosis such as facial nerve schwannoma or malignancy. **Retrocochlear signs**: ABR shows prolonged wave I-V interpeak latency, and word recognition is often worse than the pure-tone loss predicts.

### CC-otology-53.1 (concept check)

Stem: A 55-year-old has slowly progressive left hearing loss and tinnitus. Thresholds are mildly asymmetric, but left word recognition is only 40 percent. He has no vertigo. Why is vertigo uncommon despite a tumor of the vestibular nerve?

- **Correct:** Central compensation keeps pace with slow vestibular loss
- Distractor: The tumor usually arises from the cochlear nerve instead — _why wrong:_ Most tumors arise from the vestibular nerves.
- Distractor: Schwann-cell tumors secrete factors that stabilize firing — _why wrong:_ Schwannomas are not hormonally active.
- Distractor: The dense otic capsule shields the vestibular nerve — _why wrong:_ The tumor sits in the IAC and CPA, outside the capsule, and still damages the nerve.

Explanation: Vestibular input declines so gradually that the brainstem and cerebellum rebalance, so patients report imbalance rather than vertigo. Word recognition worse than thresholds predict reflects cochlear nerve dysfunction and warrants contrast MRI.

Pearl: Word recognition out of proportion to thresholds is a retrocochlear red flag.

## T-otology-54 — Vestibular Test Battery
_source: pathophys_v470/otology_a.py_

**T-otology-54.overview**

The vestibular test battery (VNG/ENG with calorics, rotary chair, video head impulse testing, and VEMPs) measures each part of the vestibular system across frequencies. It localizes peripheral versus central dysfunction, identifies the affected side and organ, and documents compensation.

**T-otology-54.physiology**

**Frequency coverage**: calorics test very low-frequency horizontal canal function, rotary chair tests low-to-mid frequencies, and head impulse testing tests high-frequency natural head movement. **Calorics**: warm or cool irrigation creates a temperature gradient that moves endolymph convectively in the horizontal canal; warm water produces nystagmus toward the irrigated ear and cool water away (COWS). **VEMPs**: loud sound stimulates otolith organs; cervical VEMP (saccule, inferior vestibular nerve) is recorded from the SCM and ocular VEMP (utricle, superior vestibular nerve) from the inferior oblique. **Oculomotor testing**: saccades, pursuit, and optokinetic testing evaluate central pathways.

**T-otology-54.pathophysiology**

**Unilateral weakness**: reduced caloric response (asymmetry over about 25 percent) indicates peripheral hypofunction on that side. **Caloric-vHIT dissociation**: Ménière disease often shows reduced calorics with a normal head impulse, while vestibular neuritis abnormalities appear on both. **Bilateral vestibulopathy**: reduced responses on both sides (ototoxicity) produce oscillopsia and imbalance, confirmed by rotary chair. **Third-window physiology**: low cVEMP thresholds and high oVEMP amplitudes indicate superior canal dehiscence. **Central signs**: abnormal pursuit, dysmetric saccades, direction-changing gaze-evoked nystagmus, or failure of fixation suppression point to brainstem or cerebellar lesions. **Division localization**: an absent oVEMP with a normal cVEMP suggests superior vestibular nerve involvement, as in most vestibular neuritis.

### CC-otology-54.1 (concept check)

Stem: A patient with suspected Ménière disease has a 45 percent caloric weakness on the affected side but a normal video head impulse test. What explains the dissociation?

- **Correct:** The tests sample different frequency ranges
- Distractor: The caloric water temperature was wrong — _why wrong:_ A consistent result with valid controls is real; the dissociation has a physiologic basis.
- Distractor: Head impulses assess the otolith organs — _why wrong:_ vHIT measures high-frequency semicircular canal VOR, not otoliths.
- Distractor: The lesion must be in the brainstem — _why wrong:_ Unilateral caloric weakness with normal vHIT is a recognized peripheral pattern in Ménière disease.

Explanation: Calorics test very low-frequency canal function, whereas head impulses test high-frequency function. Hydrops can impair caloric responses while high-frequency hair-cell function is preserved, unlike vestibular neuritis, where both are abnormal.

Pearl: Caloric-vHIT dissociation points toward Ménière disease.


---

# Rhinology / Allergy / Skull Base

## T-rhinology-1 — AERD
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-1.overview**

Aspirin-exacerbated respiratory disease (AERD, Samter triad) is CRS with nasal polyps, asthma, and respiratory reactions to aspirin and other COX-1 inhibitors. It produces the most aggressive, recurrent polyp disease and is treated with complete surgery followed by aspirin desensitization or biologics.

**T-rhinology-1.physiology**

**Arachidonic acid pathways**: cyclooxygenase (COX) makes prostaglandins and thromboxane; 5-lipoxygenase makes leukotrienes. **Prostaglandin E2 brake**: PGE2 normally inhibits mast cells and 5-lipoxygenase, restraining leukotriene production. **Cysteinyl leukotrienes**: potent mediators of bronchoconstriction, mucus secretion, and eosinophil recruitment.

**T-rhinology-1.pathophysiology**

**Baseline dysregulation**: patients overproduce cysteinyl leukotrienes and underproduce PGE2, with upregulated leukotriene receptors. **COX-1 inhibition reaction**: aspirin or NSAIDs remove the remaining PGE2 brake, causing a surge of leukotrienes and mast-cell mediators within 30-120 minutes, producing congestion, rhinorrhea, and bronchospasm. **Platelet contribution**: platelet-adherent leukocytes supply extra leukotriene production. **Type 2 inflammation**: dense eosinophilic polyps with high IL-5 and IL-13 drive rapid recurrence and anosmia. **Desensitization logic**: controlled aspirin exposure followed by daily high-dose aspirin downregulates leukotriene receptors and reduces polyp regrowth. **Leukotriene modifiers**: montelukast or zileuton blunt the pathway; alcohol sensitivity is a common clue.

### CC-rhinology-1.1 (concept check)

Stem: A 40-year-old with nasal polyps and asthma develops nasal congestion, rhinorrhea, and wheezing 45 minutes after taking ibuprofen. She tolerates acetaminophen at usual doses. What is the core mechanism of this reaction?

- **Correct:** COX-1 inhibition unleashing leukotrienes
- Distractor: IgE antibodies against ibuprofen — _why wrong:_ AERD is not IgE-mediated drug allergy; it is a pharmacologic reaction shared by all COX-1 inhibitors.
- Distractor: Direct mast-cell toxicity of NSAIDs — _why wrong:_ The reaction reflects arachidonic-acid pathway imbalance, not a toxic effect on mast cells.
- Distractor: Basophil histamine release alone — _why wrong:_ Cysteinyl leukotrienes, not histamine alone, dominate the reaction and the chronic disease.

Explanation: Patients overproduce cysteinyl leukotrienes and underproduce protective PGE2. Blocking COX-1 removes the remaining PGE2 brake, causing a leukotriene surge. Acetaminophen is a weak COX-1 inhibitor and is usually tolerated at standard doses. Aspirin desensitization downregulates leukotriene receptors.

Pearl: Polyps + asthma + NSAID reaction = AERD: complete surgery, then desensitization or a biologic.

## T-rhinology-2 — AFRS
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-2.overview**

Allergic fungal rhinosinusitis (AFRS) is a noninvasive, intensely allergic reaction to fungi colonizing the sinuses, producing eosinophilic mucin and expansile polyposis. It occurs in immunocompetent, atopic young patients, often in warm humid climates, and needs complete surgery plus postoperative steroids.

**T-rhinology-2.physiology**

**Universal fungal exposure**: everyone inhales fungal spores that deposit on sinonasal mucus. **Mucociliary clearance**: removes spores within hours in a healthy sinus. **Immune tolerance**: healthy mucosa does not mount IgE responses to fungal antigens. **Th2 immunity**: in atopic individuals, IL-4, IL-5, and IL-13 drive IgE production and eosinophil recruitment. **Sinus expansion**: sinus walls remodel under sustained pressure.

**T-rhinology-2.pathophysiology**

**Hypersensitivity**: fungi (often dematiaceous species such as Bipolaris and Curvularia, and Aspergillus) trigger IgE-mediated (type I) and immune complex (type III) reactions. **Allergic mucin**: thick, peanut-butter-like mucin full of eosinophils, Charcot-Leyden crystals (eosinophil breakdown), and fungal hyphae without tissue invasion. **Expansion**: mucin accumulates under pressure and expands sinuses, thinning bone and causing proptosis or telecanthus. **Imaging**: heterogeneous hyperdensity on CT (metallic and protein concentrations) and signal void on T2 MRI. **Why surgery is essential**: removing mucin and fungal antigen reduces the antigen load; recurrence is common without postoperative steroids and close follow-up.

### CC-rhinology-2.1 (concept check)

Stem: A 19-year-old from Louisiana with allergic rhinitis has unilateral polyps, mild proptosis, and CT showing expansile opacification with heterogeneous hyperdensity. Surgery reveals thick, peanut-butter-like mucin. What is the mechanism?

- **Correct:** Hypersensitivity to non-invasive fungi
- Distractor: Angioinvasive fungal infection — _why wrong:_ Invasive disease occurs in immunocompromised hosts and causes necrosis, not expansile mucin.
- Distractor: Fungal ball in a poorly draining sinus — _why wrong:_ Fungal balls are non-allergic, usually single-sinus, and do not expand sinuses with eosinophilic mucin.
- Distractor: Bacterial biofilm producing thick pus — _why wrong:_ Allergic mucin is eosinophil-rich with Charcot-Leyden crystals, not purulent.

Explanation: AFRS is IgE-mediated and immune-complex hypersensitivity to colonizing fungi in atopic, immunocompetent hosts. Eosinophilic mucin accumulates under pressure and expands sinuses. Treatment is complete removal of mucin plus postoperative steroids.

Pearl: Young, atopic, warm humid climate, expansile hyperdense sinuses = AFRS.

## T-rhinology-3 — Acute Bacterial Rhinosinusitis
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-3.overview**

Acute bacterial rhinosinusitis (ABRS) is bacterial sinus infection, usually after a viral cold, diagnosed by symptoms lasting 10 days or more, severe onset, or worsening after improvement (double worsening). Most acute rhinosinusitis is viral, so diagnostic criteria guide antibiotic use.

**T-rhinology-3.physiology**

**Sterility and clearance**: the sinuses are normally kept nearly sterile by mucociliary clearance and patent ostia. **Viral colds**: most cause transient sinus mucosal inflammation visible on CT, which resolves within 7-10 days.

**T-rhinology-3.pathophysiology**

**Viral phase**: rhinovirus and other viruses damage cilia, cause edema, and block ostia. **Bacterial superinfection**: stasis allows S. pneumoniae, H. influenzae, and M. catarrhalis to proliferate in a minority of colds. **Time course logic**: symptoms persisting beyond 10 days or a second worsening indicate bacterial infection rather than a resolving virus. **Complications**: spread through thin bone or valveless veins causes orbital (via the lamina papyracea) and intracranial complications. **Treatment logic**: amoxicillin-clavulanate covers beta-lactamase-producing H. influenzae and M. catarrhalis; watchful waiting is valid for uncomplicated cases.

### CC-rhinology-3.1 (concept check)

Stem: A 35-year-old's cold symptoms improved by day 6, but on day 8 she developed fever, facial pain, and purulent discharge. Which diagnostic pattern for bacterial sinusitis does this meet?

- **Correct:** Double worsening
- Distractor: Persistent symptoms for 10 days — _why wrong:_ That pattern requires 10 or more days without improvement.
- Distractor: Severe onset for 3-4 days — _why wrong:_ That pattern requires high fever and purulence from the start.
- Distractor: Uncomplicated viral rhinosinusitis — _why wrong:_ Worsening after initial improvement suggests bacterial superinfection.

Explanation: ABRS is diagnosed clinically by symptoms lasting 10 days or more without improvement, severe onset, or double worsening. Most acute rhinosinusitis is viral and resolves within 7-10 days.

Pearl: Ten days, severe onset, or double worsening suggests bacterial.

## T-rhinology-4 — Allergen Immunotherapy — SCIT / SLIT
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-4.overview**

Allergen immunotherapy (subcutaneous or sublingual) is the only disease-modifying treatment for allergic rhinitis, reducing symptoms and medication needs and sustaining benefit after stopping. It requires correct allergen selection and monitoring for systemic reactions.

**T-rhinology-4.physiology**

**Tolerance is the default**: most people inhale pollen without reacting because regulatory T cells (Tregs) and IL-10 and TGF-beta actively suppress responses to harmless antigens. **Antigen-presenting route**: subcutaneous dosing presents allergen through skin dendritic cells, whereas sublingual dosing uses oral mucosal dendritic cells, which are naturally tolerogenic. **Antibody classes**: IgE arms mast cells, whereas IgG4 is a non-inflammatory antibody that binds antigen without triggering mast cells or complement. **Dose dependence**: tolerance requires reaching and sustaining an adequate maintenance dose over years.

**T-rhinology-4.pathophysiology**

**Immune deviation**: repeated controlled exposure shifts the response from Th2 toward regulatory and Th1 responses. **Blocking IgG4**: binds allergen before it reaches mast-cell IgE. **Reduced mast-cell and eosinophil recruitment**: lowers both early and late phase reactions. **Duration**: 3-5 years of therapy produces benefit lasting years after stopping. **Safety**: SCIT carries risk of systemic reactions and anaphylaxis, requiring observation and epinephrine availability; SLIT has mainly local oral side effects. **Uncontrolled asthma**: increases risk of severe reactions.

### CC-rhinology-4.1 (concept check)

Stem: A 30-year-old receiving subcutaneous allergen immunotherapy asks why she must wait in the clinic for 30 minutes after each injection. What is the reason?

- **Correct:** Risk of a systemic allergic reaction
- Distractor: Risk of injection-site abscess — _why wrong:_ Infection at the injection site is rare and does not require observation.
- Distractor: Risk of vasovagal syncope — _why wrong:_ Syncope can occur, but the observation period exists for anaphylaxis.
- Distractor: Time for local swelling to settle — _why wrong:_ Local reactions are common but not dangerous enough to require observation.

Explanation: Injected allergen can trigger systemic reactions, including anaphylaxis, most within 30 minutes. Observation with epinephrine available is required; uncontrolled asthma increases risk.

Pearl: SCIT requires observation and epinephrine on hand.

## T-rhinology-5 — Allergic Rhinitis
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-5.overview**

Allergic rhinitis is IgE-mediated inflammation of the nasal mucosa after allergen exposure, causing sneezing, itching, rhinorrhea, and congestion. It affects up to a third of adults, worsens asthma and sinus disease, and is managed by avoidance, intranasal steroids, antihistamines, and immunotherapy.

**T-rhinology-5.physiology**

**Nasal functions**: the nose warms, humidifies, and filters about 10,000 liters of air daily. **Mucosa**: pseudostratified ciliated columnar epithelium with goblet cells and seromucous glands, over a rich venous erectile system in the turbinates. **Nasal cycle**: alternating sympathetic tone causes cyclical congestion and decongestion between sides every few hours. **Autonomic control**: sympathetic tone constricts venous sinusoids (decongestion); parasympathetic (vidian nerve) input drives glandular secretion. **Immune surveillance**: dendritic cells sample inhaled antigens and present them to T cells in regional lymphoid tissue.

**T-rhinology-5.pathophysiology**

**Sensitization**: in atopic individuals, dendritic cells present allergen to naive T cells that differentiate into Th2 cells; IL-4 and IL-13 drive B cells to make allergen-specific IgE that binds mast cells and basophils. **Early phase (minutes)**: re-exposure cross-links IgE on mast cells, releasing histamine, tryptase, leukotrienes, and prostaglandins; histamine stimulates sensory nerves (itch, sneeze), glands (rhinorrhea), and vessels (congestion). **Late phase (4-8 hours)**: cytokines (IL-4, IL-5, IL-13) recruit eosinophils, basophils, and Th2 cells, producing sustained congestion. **Priming**: repeated exposure lowers the threshold for later reactions, so symptoms build across a pollen season. **Unified airway**: the same Th2 inflammation affects the lower airway, so uncontrolled rhinitis worsens asthma. **Drug logic**: antihistamines block early-phase itch and sneeze but help congestion less; intranasal steroids suppress both phases and are the most effective single therapy; immunotherapy shifts the response toward tolerance (regulatory T cells, IgG4).

### CC-rhinology-5.1 (concept check)

Stem: A 26-year-old with seasonal sneezing and nasal itch controls those symptoms with a second-generation antihistamine, but daily nasal congestion persists through the season. Which single therapy best treats both the early- and late-phase allergic response?

- **Correct:** Intranasal corticosteroid
- Distractor: Daily oral pseudoephedrine — _why wrong:_ Decongestants shrink venous sinusoids but do not treat allergic inflammation, and they raise blood pressure and cause insomnia.
- Distractor: Double-dose oral antihistamine — _why wrong:_ Antihistamines block histamine-driven itch and sneeze (early phase) but do little for congestion from the late-phase eosinophilic response.
- Distractor: Intranasal ipratropium spray — _why wrong:_ Ipratropium blocks cholinergic glandular secretion, reducing watery rhinorrhea, but has no anti-inflammatory effect on congestion.

Explanation: Allergen cross-links IgE on mast cells, releasing histamine (early phase: itch, sneeze, rhinorrhea). Cytokines then recruit eosinophils and Th2 cells over hours (late phase: congestion). Intranasal steroids suppress both phases and are the most effective single agent.

Pearl: Antihistamines for itch and sneeze; intranasal steroids for congestion and the late phase.

## T-rhinology-6 — Allergy Testing & Interpretation
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-6.overview**

Allergy testing (skin prick, intradermal, and serum specific IgE) identifies sensitization, which becomes clinical allergy only when it matches symptoms and exposure. Correct interpretation drives avoidance and immunotherapy decisions.

**T-rhinology-6.physiology**

**IgE arming**: allergen-specific IgE binds high-affinity FcεRI receptors on mast cells and basophils. **Skin mast cells**: introducing allergen into the epidermis cross-links IgE, releasing histamine within minutes. **Wheal and flare**: histamine causes local edema (wheal) and an axon-reflex vasodilation (flare). **Serum specific IgE**: measures circulating IgE independent of mast-cell function or antihistamines. **Controls**: histamine (positive) and saline (negative) confirm skin reactivity.

**T-rhinology-6.pathophysiology**

**Sensitization vs allergy**: a positive test without matching symptoms is sensitization only. **Skin testing interference**: antihistamines suppress the histamine-mediated wheal, so they are held before testing; positive (histamine) and negative (saline) controls validate the test. **Serum testing role**: useful with dermatographism, extensive skin disease, inability to stop antihistamines, or anaphylaxis risk. **Intradermal testing**: more sensitive but less specific, with more false positives. **Component testing**: distinguishes cross-reactive proteins (e.g., pollen-food) from primary sensitization.

### CC-rhinology-6.1 (concept check)

Stem: A 25-year-old has a 6 mm wheal to cat on skin prick testing, but has lived with a cat for years without nasal, eye, or chest symptoms. What does this result indicate?

- **Correct:** Sensitization without clinical allergy
- Distractor: Clinically significant cat allergy — _why wrong:_ A positive test means allergy only when it matches symptoms with exposure.
- Distractor: A false-positive test from dermatographism — _why wrong:_ Dermatographism is excluded by a negative saline control, which is not described.
- Distractor: An indication for cat immunotherapy — _why wrong:_ Immunotherapy treats symptomatic allergy, not sensitization alone.

Explanation: A positive test shows allergen-specific IgE on mast cells. Clinical allergy requires symptoms on exposure that match the sensitization.

Pearl: Treat the patient, not the test.

## T-rhinology-7 — Anaphylaxis
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-7.overview**

Anaphylaxis is a severe, rapid systemic hypersensitivity reaction causing airway, breathing, circulatory, and skin involvement. Intramuscular epinephrine is the first and most important treatment, relevant to allergy testing, immunotherapy, and perioperative care.

**T-rhinology-7.physiology**

**Mast cells and basophils**: store histamine and tryptase and synthesize leukotrienes and prostaglandins on activation. **Epinephrine receptors**: alpha-1 (vasoconstriction), beta-1 (cardiac output), and beta-2 (bronchodilation, mast-cell stabilization).

**T-rhinology-7.pathophysiology**

**Trigger**: IgE-mediated (foods, venom, drugs, immunotherapy) or non-IgE (contrast, opioids) mast-cell activation. **Mediator release**: histamine and leukotrienes cause vasodilation, capillary leak, bronchospasm, and edema. **Shock**: distributive vasodilation plus fluid shift reduce preload, causing hypotension. **Airway compromise**: laryngeal and tongue edema obstruct the upper airway. **Biphasic reactions**: symptoms can recur hours later. **Why epinephrine first**: it reverses vasodilation and bronchospasm and stabilizes mast cells; antihistamines and steroids are adjuncts only. **Beta-blockers**: blunt epinephrine response, sometimes requiring glucagon.

### CC-rhinology-7.1 (concept check)

Stem: Ten minutes after an immunotherapy injection, a patient develops diffuse urticaria, wheezing, and a blood pressure of 78/40. What is the first treatment?

- **Correct:** Intramuscular epinephrine
- Distractor: Intravenous diphenhydramine — _why wrong:_ Antihistamines are adjuncts that do not reverse hypotension or bronchospasm.
- Distractor: Intravenous methylprednisolone — _why wrong:_ Steroids act over hours and do not treat acute shock.
- Distractor: Nebulized albuterol alone — _why wrong:_ Albuterol helps bronchospasm but does not treat distributive shock.

Explanation: Epinephrine reverses vasodilation (alpha-1), supports cardiac output (beta-1), relieves bronchospasm (beta-2), and stabilizes mast cells. Delay increases mortality.

Pearl: Anaphylaxis: epinephrine first, everything else second.

## T-rhinology-8 — Benign Sinonasal Tumor Framework
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-8.overview**

Benign sinonasal tumors (inverted papilloma, osteoma, fibrous dysplasia, ossifying fibroma, hemangioma, schwannoma, JNA) are classified by tissue of origin and treated by complete resection when symptomatic or growing. Imaging helps predict histology before surgery.

**T-rhinology-8.physiology**

**Tissue types**: the sinonasal tract contains respiratory epithelium, bone, fibro-osseous tissue, vessels, nerves, and minor salivary glands, each of which can give rise to benign tumors. **Craniofacial bone growth**: facial bones grow through childhood and adolescence, influencing fibro-osseous lesion behavior. **Confined spaces**: sinuses are bony boxes, so slow growth causes obstruction and remodeling before symptoms. **Imaging signatures**: CT shows bone characteristics, while MRI separates tumor from retained secretions.

**T-rhinology-8.pathophysiology**

**Osteoma**: slow-growing dense bone, most often frontal or ethmoid; obstruction or growth toward the orbit or skull base indicates removal. **Fibrous dysplasia**: GNAS mutation replaces bone with fibro-osseous tissue (ground-glass on CT); usually stabilizes after puberty. **Ossifying fibroma**: well-circumscribed, more aggressive fibro-osseous neoplasm requiring complete removal. **Lobular capillary hemangioma**: friable bleeding septal lesion, often in pregnancy. **Treatment logic**: endoscopic resection is guided by attachment site and extent; observation suits asymptomatic stable lesions.

### CC-rhinology-8.1 (concept check)

Stem: A 20-year-old has painless left cheek fullness. CT shows expansion of the maxilla with a ground-glass matrix and indistinct margins; serial imaging shows growth stopped after puberty. What is the most likely diagnosis?

- **Correct:** Fibrous dysplasia
- Distractor: Ossifying fibroma — _why wrong:_ Ossifying fibroma is well-circumscribed and continues to grow.
- Distractor: Osteoma — _why wrong:_ Osteomas are dense, well-defined bone, not ground glass.
- Distractor: Inverted papilloma — _why wrong:_ Inverted papilloma is a soft-tissue epithelial tumor.

Explanation: Fibrous dysplasia (GNAS mutation) replaces bone with fibro-osseous tissue that appears ground-glass on CT with indistinct margins and often stabilizes after puberty. Surgery is reserved for deformity or compression.

Pearl: Ground-glass expansion that stops at puberty = fibrous dysplasia.

## T-rhinology-9 — CF / Primary Ciliary Dyskinesia Sinonasal Disease
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-9.overview**

Cystic fibrosis and primary ciliary dyskinesia cause universal, lifelong CRS from failed mucociliary clearance. Sinus disease reseeds the lungs, so sinus care is part of lung care, and CFTR modulators have changed the disease course.

**T-rhinology-9.physiology**

**CFTR channel**: chloride and bicarbonate channel that hydrates airway surface liquid. **Mucociliary escalator**: needs normal cilia beating in a properly hydrated periciliary layer. **Ciliary structure**: 9+2 microtubules with dynein arms that power beating.

**T-rhinology-9.pathophysiology**

**CF mechanism**: defective CFTR dehydrates airway surface liquid, producing thick mucus that cilia cannot clear, leading to obstruction, chronic infection (Pseudomonas), and polyps. **PCD mechanism**: structural defects in cilia (often dynein arm mutations) impair beating despite normal mucus, causing neonatal respiratory distress, chronic wet cough, otitis, and situs inversus in about half (Kartagener). **Lung reservoir**: the sinuses act as a reservoir for Pseudomonas, which seeds the lungs after transplant. **CFTR modulators**: elexacaftor-tezacaftor-ivacaftor improves channel function, reducing sinus disease severity. **Diagnostics**: sweat chloride and genetics for CF; nasal nitric oxide (low in PCD), ciliary electron microscopy, and genetics for PCD.

### CC-rhinology-9.1 (concept check)

Stem: A 9-year-old has bilateral nasal polyps, chronic purulent rhinorrhea, and poor weight gain. What should be excluded first?

- **Correct:** Cystic fibrosis
- Distractor: Allergic rhinitis — _why wrong:_ Allergy alone rarely causes nasal polyps in children.
- Distractor: Aspirin-exacerbated respiratory disease — _why wrong:_ AERD presents in adults, not children.
- Distractor: Antrochoanal polyp — _why wrong:_ An antrochoanal polyp is usually single and unilateral.

Explanation: Defective CFTR dehydrates airway surface liquid, producing thick mucus, impaired clearance, chronic Pseudomonas infection, and polyps. Sweat chloride and genetic testing confirm the diagnosis.

Pearl: Polyps in a child = test for cystic fibrosis.

## T-rhinology-10 — CRS Phenotyping
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-10.overview**

Chronic rhinosinusitis (CRS) is 12 weeks or more of sinonasal inflammation confirmed by endoscopy or CT. Phenotyping (with or without polyps) and endotyping (type 2 versus non-type 2 inflammation) predict response to steroids, surgery, and biologics.

**T-rhinology-10.physiology**

**Mucociliary clearance**: cilia beat at about 10-15 Hz, moving the mucus blanket toward natural ostia and then the nasopharynx. **Ostiomeatal complex**: the shared drainage pathway of the maxillary, anterior ethmoid, and frontal sinuses through the middle meatus. **Epithelial barrier**: tight junctions and innate defenses (antimicrobial peptides, nitric oxide) keep microbes and allergens out. **Immune tone**: healthy sinonasal mucosa maintains low-level, balanced immune surveillance.

**T-rhinology-10.pathophysiology**

**Multifactorial inflammation**: CRS is not simply blocked ostia or infection; barrier dysfunction, dysregulated immunity, and microbial factors interact. **Type 2 endotype**: eosinophils, IL-4, IL-5, IL-13, and high IgE; associated with polyps, asthma, AERD, recurrence, and good response to steroids and biologics. **Non-type 2 endotypes**: neutrophilic (type 3, IL-17) or type 1 (interferon-gamma) inflammation, more common in CRSsNP and some Asian populations. **Barrier breakdown**: impaired tight junctions allow antigen and bacterial products to penetrate and perpetuate inflammation. **Biofilms and S. aureus**: biofilms resist antibiotics, and S. aureus enterotoxins can act as superantigens that amplify type 2 inflammation. **Why phenotype matters**: type 2 disease recurs after surgery without ongoing topical steroid, while biologics target specific type 2 cytokines.

### CC-rhinology-10.1 (concept check)

Stem: A 45-year-old with CRS with nasal polyps has asthma, blood eosinophils of 650/µL, and anosmia, and her polyps recurred within 18 months of complete endoscopic sinus surgery. Which biological feature best explains the early recurrence?

- **Correct:** Persistent type 2 inflammation
- Distractor: Retained bacterial biofilm alone — _why wrong:_ Biofilms contribute to CRS, but rapid recurrence with eosinophilia, asthma, and anosmia reflects type 2 immune biology.
- Distractor: Incompletely opened sinus ostia — _why wrong:_ The surgery was complete; recurrence here is driven by mucosal inflammation, not residual anatomic obstruction.
- Distractor: Neutrophilic type 3 inflammation — _why wrong:_ Neutrophil-predominant disease is more typical of CRSsNP and does not fit this eosinophilic profile.

Explanation: Type 2 endotypes (IL-4, IL-5, IL-13, eosinophils, IgE) associate with polyps, asthma, AERD, and recurrence, but respond well to topical steroids and biologics. The endotype, not the operation, determines long-term control.

Pearl: Polyps + asthma + eosinophilia = type 2 disease: plan maintenance steroid and consider a biologic.

## T-rhinology-11 — CRSsNP
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-11.overview**

CRS without nasal polyps (CRSsNP) is chronic sinonasal inflammation with congestion, discharge, pressure, or smell loss and no polyps. It is more often non-type 2 and is managed with saline, topical steroids, culture-directed antibiotics when infected, and sinus surgery when medical therapy fails.

**T-rhinology-11.physiology**

**Drainage and ventilation**: each sinus depends on a patent natural ostium and mucociliary clearance moving mucus toward it. **Ostiomeatal complex**: the shared middle-meatal outflow for the maxillary, anterior ethmoid, and frontal sinuses, where small amounts of swelling cause obstruction. **Epithelial barrier**: tight junctions and antimicrobial peptides keep microbes and antigens out of the submucosa. **Balanced mucosal immunity**: healthy mucosa maintains low-level surveillance without chronic inflammation. **Sinus bone**: thin bone beneath the mucosa remodels in response to chronic inflammation.

**T-rhinology-11.pathophysiology**

**Inflammatory profile**: often neutrophilic and type 1 inflammation with fibrosis and basement membrane thickening rather than edema. **Ostial obstruction cycle**: inflammation narrows ostia, stasis promotes infection, and infection deepens inflammation. **Osteitis**: chronically inflamed bone thickens and may itself perpetuate inflammation and resist medical therapy. **Contributors**: anatomic obstruction, odontogenic sources, biofilms, immunodeficiency, and environmental exposures. **Surgical logic**: surgery restores drainage and creates access for topical therapy, which is critical for long-term control.

### CC-rhinology-11.1 (concept check)

Stem: A 50-year-old has 4 months of facial pressure, congestion, and discolored drainage despite saline. Endoscopy shows purulence in the middle meatus without polyps, and CT shows mucosal thickening with thickened bony septa. Which tissue pattern is typical of this phenotype?

- **Correct:** Fibrosis with neutrophils
- Distractor: Edematous stroma with eosinophils — _why wrong:_ Edematous eosinophilic stroma is the typical pattern of CRS with nasal polyps.
- Distractor: Fungal hyphae invading vessel walls — _why wrong:_ Angioinvasion defines acute invasive fungal sinusitis in immunocompromised hosts.
- Distractor: Eosinophilic mucin with fungal hyphae — _why wrong:_ Allergic mucin with Charcot-Leyden crystals defines allergic fungal rhinosinusitis.

Explanation: CRSsNP more often shows non-type 2 inflammation with fibrosis and basement membrane thickening. Thickened bony septa reflect osteitis, which can perpetuate inflammation. Surgery restores drainage and topical access when medical therapy fails.

Pearl: No polyps does not mean no CRS; endoscopy and CT confirm the diagnosis.

## T-rhinology-12 — CRSwNP
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-12.overview**

CRS with nasal polyps (CRSwNP) is chronic sinonasal inflammation with edematous polyps arising from the middle meatus and ethmoids. In Western patients it is usually type 2 (eosinophilic), associated with asthma and AERD, and treated with steroids, complete surgery, and biologics.

**T-rhinology-12.physiology**

**Ethmoid origin**: polyps arise most often from the ethmoid and middle meatus mucosa. **Mucosal homeostasis**: epithelial barrier integrity and balanced immune signals prevent excessive tissue edema.

**T-rhinology-12.pathophysiology**

**Type 2 inflammation**: epithelial alarmins (TSLP, IL-33, IL-25) activate ILC2s and Th2 cells; IL-5 recruits and sustains eosinophils, while IL-4 and IL-13 drive IgE and tissue remodeling. **Edema formation**: albumin and fibrin accumulate in the stroma, and reduced tissue plasminogen activator impairs fibrin breakdown, trapping fluid and forming polyps. **Symptoms**: mechanical obstruction plus olfactory cleft inflammation cause congestion and anosmia. **S. aureus enterotoxins**: act as superantigens driving local polyclonal IgE. **Recurrence**: inflammation continues after surgery, so long-term topical steroid (often high-volume irrigation) is required. **Biologic targets**: dupilumab (IL-4Ralpha), omalizumab (IgE), mepolizumab (IL-5), and tezepelumab (TSLP) interrupt specific steps of type 2 inflammation.

### CC-rhinology-12.1 (concept check)

Stem: A 48-year-old with bilateral nasal polyps has a biopsy showing edematous, sparsely cellular stroma with abundant eosinophils. What mechanism explains why the polyps are soft, edematous masses?

- **Correct:** Fibrin deposits trap fluid in the stroma
- Distractor: Obstructed glands form mucous cysts — _why wrong:_ Polyps are stromal edema, not collections of cystic glands.
- Distractor: Smooth muscle proliferates beneath mucosa — _why wrong:_ Polyps contain little smooth muscle and are not muscular growths.
- Distractor: Lymphoid follicles expand like tonsils — _why wrong:_ Polyps are edema-driven, not lymphoid hyperplasia.

Explanation: Type 2 cytokines increase vascular permeability while reduced tissue plasminogen activator impairs fibrin breakdown. Plasma proteins and fibrin accumulate, trapping water. Inflammation continues after surgery, so long-term topical steroid is required.

Pearl: Polyps are type 2 edema: surgery opens the sinuses, steroids and biologics control the disease.

## T-rhinology-13 — CSF Rhinorrhea
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-13.overview**

CSF rhinorrhea is cerebrospinal fluid leaking into the nose through a skull-base defect, from trauma, surgery, elevated intracranial pressure, tumor, or congenital defects. It carries a lifetime risk of meningitis and needs confirmation with beta-2 transferrin, localization, and usually endoscopic repair.

**T-rhinology-13.physiology**

**CSF dynamics**: about 500 mL is produced daily by the choroid plexus and absorbed by arachnoid granulations; normal opening pressure is about 10-20 cm H2O. **Weak skull-base sites**: the lateral lamella of the cribriform plate (thinnest bone, Keros classification), the cribriform plate itself, the ethmoid roof, the sphenoid lateral recess, and the frontal sinus posterior table. **Meningeal barrier**: dura and arachnoid separate CSF from the sinonasal tract.

**T-rhinology-13.pathophysiology**

**Traumatic leaks**: skull-base fractures tear dura; many close within 7-10 days with conservative care. **Iatrogenic leaks**: injury to the lateral lamella or skull base during sinus or skull-base surgery. **Spontaneous leaks**: idiopathic intracranial hypertension transmits chronically elevated pressure through thin bone, creating arachnoid pits and meningoencephaloceles, often at the cribriform plate or a pneumatized sphenoid lateral recess; patients are often obese women. **Positional drainage**: leakage increases with leaning forward or straining (Valsalva). **Meningitis risk**: an open path from the nasal cavity to the subarachnoid space allows bacterial ascent, so closure is recommended. **Repair failure**: untreated elevated ICP raises recurrence risk, so ICP management (acetazolamide, weight loss, shunting) accompanies repair in spontaneous leaks.

## T-rhinology-14 — Empty Nose Syndrome
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-14.overview**

Empty nose syndrome is paradoxical nasal obstruction and suffocation sensation after turbinate reduction, despite a widely patent airway. It reflects lost airflow sensation and conditioning rather than physical blockage.

**T-rhinology-14.physiology**

**Airflow sensation**: TRPM8 cold receptors in turbinate mucosa sense cooling from airflow, which the brain interprets as breathing freely. **Air conditioning**: turbinates warm and humidify air and direct flow.

**T-rhinology-14.pathophysiology**

**Loss of sensory surface**: aggressive turbinate resection removes cold receptors, so airflow is not perceived despite low resistance. **Abnormal airflow**: altered flow patterns and dryness cause crusting and discomfort. **Psychological overlay**: anxiety, depression, and sleep disturbance are common and amplify symptoms. **Diagnosis**: cotton test (placing cotton in the space temporarily relieves symptoms) and questionnaires. **Treatment logic**: humidification, and implants to restore airway volume and redirect flow toward mucosa.

### CC-rhinology-14.1 (concept check)

Stem: A 50-year-old reports a sense of suffocation and dryness 2 years after aggressive bilateral turbinate reduction. Endoscopy shows a widely patent nasal cavity. Which bedside test supports empty nose syndrome?

- **Correct:** A cotton test that relieves symptoms
- Distractor: Acoustic rhinometry showing narrowing — _why wrong:_ The airway is wide; rhinometry would not show narrowing.
- Distractor: Skin prick testing for allergens — _why wrong:_ Allergy testing does not diagnose empty nose syndrome.
- Distractor: Positive Cottle maneuver — _why wrong:_ The Cottle maneuver tests the internal valve, not lost turbinate sensation.

Explanation: Placing moistened cotton in the turbinate space temporarily redirects airflow over remaining mucosa and improves the sense of breathing, supporting the diagnosis.

Pearl: Empty nose syndrome is lost sensation, not obstruction.

## T-rhinology-15 — Endoscopic CSF Leak Repair / Nasoseptal Flap
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-15.overview**

Endoscopic CSF leak repair closes skull-base defects with grafts (fat, fascia, mucosa) or vascularized flaps, most commonly the pedicled nasoseptal flap. Vascularized reconstruction dramatically lowered leak rates after endoscopic skull-base surgery.

**T-rhinology-15.physiology**

**Nasoseptal flap supply**: the posterior septal artery, a branch of the sphenopalatine artery, enters across the sphenoid face. **Healing**: vascularized tissue heals faster and resists CSF pressure better than free grafts. **Layered closure**: inlay and onlay grafts reconstruct dura and skull base.

**T-rhinology-15.pathophysiology**

**High-flow vs low-flow leaks**: opening a cistern or ventricle creates high-flow leaks that need vascularized flaps. **Pressure and failure**: elevated ICP, obesity, and high-flow leaks increase failure. **Flap viability**: the pedicle must be protected during sphenoidotomy and posterior septectomy, or the flap may be lost. **Donor-site morbidity**: crusting and septal changes, with a small risk of perforation. **Lumbar drains**: used selectively to reduce CSF pressure in high-risk leaks.

### CC-rhinology-15.1 (concept check)

Stem: After endoscopic resection of a large pituitary macroadenoma, the surgeon finds a high-flow CSF leak from an opened suprasellar cistern. Why is a pedicled nasoseptal flap preferred over a free mucosal graft for the reconstruction?

- **Correct:** Its own blood supply heals faster and resists pressure
- Distractor: It is harvested without any donor-site morbidity — _why wrong:_ Nasoseptal flaps do cause donor-site crusting and septal changes; the advantage is vascularity.
- Distractor: It removes the need to control raised ICP — _why wrong:_ Untreated raised intracranial pressure still causes repair failure regardless of flap type.
- Distractor: It can be raised after the sphenoidotomy is widened — _why wrong:_ The pedicle must be protected before posterior septectomy and wide sphenoidotomy or the flap may be lost.

Explanation: The nasoseptal flap is pedicled on the posterior septal artery, a branch of the sphenopalatine artery. Vascularized tissue heals more reliably over a high-flow defect than free grafts, which is why it lowered leak rates after extended endoscopic skull-base surgery.

Pearl: High-flow leak: reconstruct in layers and cover with vascularized tissue.

## T-rhinology-16 — Endoscopic Maxillary Antrostomy
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-16.overview**

Endoscopic maxillary antrostomy widens the natural maxillary ostium after uncinectomy to restore drainage and access for topical therapy. Its key principle is incorporating the natural ostium to prevent mucus recirculation.

**T-rhinology-16.physiology**

**Natural ostium**: located in the posterior ethmoid infundibulum, behind the uncinate, angled superiorly and medially. **Mucociliary direction**: cilia drive maxillary mucus toward the natural ostium regardless of any accessory openings. **Fontanelles**: anterior and posterior membranous areas of the medial maxillary wall may contain accessory ostia.

**T-rhinology-16.pathophysiology**

**Recirculation**: an antrostomy not joined to the natural ostium (or an accessory ostium left separate) lets mucus exit the natural ostium and re-enter through the other opening, causing persistent infection. **Ostial obstruction**: inflammation or anatomic variants block the natural ostium, causing stasis and infection. **Complication anatomy**: the orbit lies superior, the nasolacrimal duct anterior (risk of epiphora if the antrostomy is extended too far forward), and the sphenopalatine vessels posterior. **Surgical logic**: removing the uncinate and widening the natural ostium posteriorly and inferiorly restores physiologic drainage.

## T-rhinology-17 — Endoscopic Pituitary / Anterior Skull Base Approach
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-17.overview**

The endoscopic endonasal approach reaches the sella and anterior skull base through the nose and sphenoid. It requires precise sphenoid anatomy, vascularized reconstruction, and care of the carotids and optic nerves.

**T-rhinology-17.physiology**

**Sella**: sits in the sphenoid roof, bordered by the cavernous sinuses and carotids laterally and the optic chiasm superiorly. **Pituitary function**: the anterior pituitary secretes ACTH, TSH, GH, prolactin, LH, and FSH; the posterior releases ADH and oxytocin. **Sphenoid landmarks**: sellar floor, carotid prominences, optic protuberances, opticocarotid recesses, and clival recess.

**T-rhinology-17.pathophysiology**

**Tumor effects**: macroadenomas compress the chiasm (bitemporal hemianopia) and cause hypopituitarism; functional adenomas cause hormonal syndromes. **Carotid injury**: catastrophic hemorrhage from lateral dissection, especially with dehiscent carotid canals. **Diabetes insipidus**: posterior pituitary or stalk manipulation reduces ADH. **SIADH**: can occur later, causing hyponatremia. **CSF leak**: from opening the arachnoid; reconstruction with a nasoseptal flap reduces leak rates.

### CC-rhinology-17.1 (concept check)

Stem: On postoperative day 1 after endoscopic pituitary adenoma resection, a patient passes large volumes of dilute urine and his serum sodium rises to 148 mmol/L. What is the cause?

- **Correct:** Diabetes insipidus from low ADH
- Distractor: SIADH from posterior pituitary injury — _why wrong:_ SIADH causes concentrated urine and hyponatremia.
- Distractor: Osmotic diuresis from hyperglycemia — _why wrong:_ Glucose-driven diuresis produces glycosuria, not dilute urine with hypernatremia from ADH loss.
- Distractor: Cerebral salt wasting — _why wrong:_ Salt wasting causes hyponatremia with volume depletion.

Explanation: Manipulation of the posterior pituitary or stalk reduces ADH release, causing dilute polyuria and hypernatremia. A delayed SIADH phase can follow, so sodium is monitored for days.

Pearl: Polyuria + rising sodium after pituitary surgery = diabetes insipidus.

## T-rhinology-18 — Epistaxis Surgical Control
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-18.overview**

Surgical control of epistaxis (endoscopic sphenopalatine artery ligation, anterior ethmoid artery ligation, or embolization) is used when packing fails. Choosing the target depends on bleeding location and arterial anatomy.

**T-rhinology-18.physiology**

**External carotid supply**: the sphenopalatine artery (from the internal maxillary) supplies the posterior lateral wall and septum; the greater palatine and superior labial arteries contribute anteriorly. **Internal carotid supply**: anterior and posterior ethmoid arteries (from the ophthalmic) supply the superior septum and lateral wall. **Kiesselbach plexus**: anterior septal anastomosis (Little area), source of most anterior bleeds. **Woodruff plexus**: posterior lateral venous plexus implicated in posterior bleeds.

**T-rhinology-18.pathophysiology**

**Posterior bleeding**: from sphenopalatine branches, harder to pack, common in older and hypertensive or anticoagulated patients. **Why SPA ligation works**: clipping the artery and its branches at the crista ethmoidalis reduces flow to the posterior nose with high success. **Collateral failure**: ethmoid artery bleeding (internal carotid territory) is not controlled by SPA ligation or external carotid embolization. **Embolization risks**: external carotid embolization can spread emboli to the internal circulation through anastomoses, causing stroke or blindness, which is why ethmoid arteries are ligated surgically instead.

### CC-rhinology-18.1 (concept check)

Stem: A 70-year-old has recurrent bleeding from high on the septum and superior lateral wall after a technically successful endoscopic sphenopalatine artery ligation. Which vessel is most likely responsible?

- **Correct:** Anterior ethmoid artery
- Distractor: Greater palatine artery — _why wrong:_ The greater palatine artery supplies the anterior nasal floor and septum via the incisive canal, not the high septum.
- Distractor: Superior labial artery — _why wrong:_ The superior labial artery supplies the anterior septum at Kiesselbach plexus, low and anterior.
- Distractor: Descending palatine artery — _why wrong:_ This branch runs in the palate and is not a source of high septal bleeding.

Explanation: The anterior ethmoid artery (internal carotid territory, via the ophthalmic artery) supplies the superior nose and is not controlled by SPA ligation or external carotid embolization. It is ligated surgically.

Pearl: Bleeding persists after SPA ligation? Think ethmoid arteries.

## T-rhinology-19 — Ethmoidectomy
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-19.overview**

Endoscopic ethmoidectomy removes ethmoid air-cell partitions to restore drainage and open the ethmoid sinus for topical therapy and surveillance. It requires precise knowledge of the skull base, lamina papyracea, and ethmoid arteries.

**T-rhinology-19.physiology**

**Labyrinth**: multiple air cells divided by lamellae; the middle turbinate basal lamella separates anterior and posterior cells. **Boundaries**: lamina papyracea laterally, skull base superiorly, middle turbinate medially, sphenoid face posteriorly. **Skull base slope**: it descends from anterior to posterior and is lowest medially at the lateral lamella.

**T-rhinology-19.pathophysiology**

**Disease reservoir**: obstructed cells harbor inflammation and polyps and block frontal and maxillary drainage. **Complications**: orbital injury through the lamina (orbital fat exposure, medial rectus injury), anterior ethmoid artery injury (retro-orbital hematoma), and skull-base injury (CSF leak). **Retro-orbital hematoma mechanism**: an injured anterior ethmoid artery retracts into the orbit and bleeds, raising orbital pressure and compressing the optic nerve. **Mucosal preservation**: stripping mucosa causes osteitis and scarring; complete but mucosa-sparing dissection improves outcomes.

### CC-rhinology-19.1 (concept check)

Stem: During anterior ethmoidectomy, brisk bleeding occurs near the skull base. Minutes later the eye becomes proptotic, the orbit firm, and the pupil sluggish. What is the mechanism?

- **Correct:** Retracted ethmoid artery bleeding into the orbit
- Distractor: Orbital fat herniating through the lamina — _why wrong:_ Fat herniation does not cause rising pressure or a sluggish pupil.
- Distractor: Contusion of the medial rectus — _why wrong:_ Muscle injury causes diplopia, not tense proptosis.
- Distractor: CSF tracking into the orbit — _why wrong:_ CSF leak does not produce tense proptosis.

Explanation: A transected anterior ethmoid artery can retract into the orbit and bleed, creating a retrobulbar hematoma that compresses the optic nerve and its blood supply. Lateral canthotomy and cantholysis are emergent.

Pearl: Tense proptosis during FESS = retrobulbar hematoma: decompress now.

## T-rhinology-20 — Facial Pain / Headache vs Rhinogenic Disease
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-20.overview**

Many patients with "sinus headache" have migraine or tension-type headache rather than sinus disease. Distinguishing them prevents unnecessary antibiotics and surgery.

**T-rhinology-20.physiology**

**Trigeminal convergence**: sinus, dural, and facial pain all converge on the trigeminal nucleus caudalis. **Autonomic symptoms**: migraine activates trigeminal-autonomic reflexes, causing nasal congestion and rhinorrhea.

**T-rhinology-20.pathophysiology**

**Misattribution**: migraine-related facial pain, congestion, and weather triggers mimic sinus disease. **Rhinogenic pain**: true sinus pain usually accompanies purulence, obstruction, smell loss, and objective findings on endoscopy or CT. **Contact point headache**: controversial; mucosal contact points are common in asymptomatic people. **Diagnostic logic**: facial pain without endoscopic or CT evidence of inflammation should prompt headache evaluation and treatment.

### CC-rhinology-20.1 (concept check)

Stem: A 38-year-old has monthly episodes of facial pressure with nasal congestion, worse with weather changes. Endoscopy is normal and a CT obtained during an episode is clear. What is the most likely cause?

- **Correct:** Migraine
- Distractor: Chronic rhinosinusitis — _why wrong:_ CRS requires objective evidence on endoscopy or CT.
- Distractor: Recurrent acute bacterial sinusitis — _why wrong:_ A clear CT during symptoms argues strongly against it.
- Distractor: Fungal ball — _why wrong:_ A clear CT excludes a fungal ball.

Explanation: Migraine activates trigeminal-autonomic reflexes, producing facial pain, congestion, and rhinorrhea. Without objective sinus findings, migraine treatment is appropriate rather than antibiotics or surgery.

Pearl: No objective sinus disease = treat the headache.

## T-rhinology-21 — Frontal Recess / Frontal Sinus
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-21.overview**

The frontal recess is the narrow, cell-crowded hourglass-shaped pathway draining the frontal sinus into the middle meatus. It is the most technically demanding area of endoscopic sinus surgery and the most common site of iatrogenic stenosis and revision.

**T-rhinology-21.physiology**

**Development**: the frontal sinus pneumatizes from the anterior ethmoids after early childhood, reaching adult size in adolescence. **Drainage path**: the frontal ostium narrows into the recess, bounded by the agger nasi anteriorly, the ethmoid bulla and skull base posteriorly, the lamina papyracea laterally, and the middle turbinate medially. **Uncinate attachment**: whether the uncinate attaches to the lamina papyracea, skull base, or middle turbinate determines whether drainage enters the ethmoid infundibulum or middle meatus. **Frontal cells**: agger nasi, supra-agger, supra-bullar, and frontal septal cells (IFAC classification) shape the pathway. **Mucociliary pattern**: frontal sinus mucus circulates up the medial wall, across the roof, and down the lateral wall to exit the ostium.

**T-rhinology-21.pathophysiology**

**Obstruction**: cells, edema, polyps, or scar narrowing the recess block drainage and ventilation, causing frontal sinusitis. **Mucocele formation**: long-standing obstruction lets mucus accumulate under pressure, slowly expanding and remodeling bone. **Iatrogenic stenosis**: stripping mucosa circumferentially exposes bone, leading to osteitis and scar contracture across the narrow outflow. **Complication routes**: the posterior table and skull base lie directly behind (CSF leak, intracranial spread), and the anterior ethmoid artery runs along the posterior recess boundary. **Why mucosal preservation matters**: preserved mucosa heals with functional cilia, whereas denuded bone heals with fibrosis and neo-osteogenesis.

## T-rhinology-22 — Frontal Sinusotomy / Draf Procedures
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-22.overview**

Draf procedures progressively widen frontal drainage: Draf I (recess clearance), Draf IIa and IIb (ostium widening), and Draf III (endoscopic modified Lothrop, connecting both frontal sinuses). They match the size of the opening to the severity of disease.

**T-rhinology-22.physiology**

**Frontal outflow**: narrow, variable, and surrounded by the skull base, orbit, and ethmoid cells. **Frontal beak**: the anterior bony boundary of the outflow tract, drilled in extended procedures. **Mucosal healing**: openings shrink as they heal, most with circumferential mucosal loss.

**T-rhinology-22.pathophysiology**

**Restenosis**: circumferential mucosal stripping and exposed bone lead to fibrosis and new bone that close the neo-ostium. **Rationale for Draf III**: a common frontal opening is large enough to stay patent despite scarring and allows high-volume irrigation access. **Indications follow failure**: recalcitrant frontal disease, mucoceles, tumors, and failed prior surgery. **Complications**: CSF leak at the first olfactory neuron, orbital injury, and restenosis.

## T-rhinology-23 — Fungal Ball
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-23.overview**

A fungal ball (mycetoma) is a noninvasive mass of densely packed fungal hyphae in a sinus, usually maxillary, in an immunocompetent person. It is cured by endoscopic removal and does not need antifungals.

**T-rhinology-23.physiology**

**Spore exposure is universal**: everyone inhales Aspergillus and other spores daily, and they land on sinus mucus. **Mucociliary clearance**: cilia move the mucus blanket and trapped spores to the natural ostium within minutes to hours, so spores never stay long enough to grow. **Ventilation**: an open ostium keeps the sinus aerated and near atmospheric oxygen tension, which is unfavorable for dense fungal growth in stagnant secretions. **Maxillary drainage**: the maxillary ostium sits high on the medial wall, so drainage depends entirely on ciliary transport rather than gravity, making the maxillary sinus the most vulnerable site.

**T-rhinology-23.pathophysiology**

**Poor clearance**: impaired drainage allows spores to accumulate and grow into a mass (usually Aspergillus). **Dental association**: root canal sealers containing zinc may promote fungal growth in the maxillary sinus. **No invasion**: hyphae stay in the lumen without tissue or vascular invasion and without a strong allergic response. **Imaging**: a single sinus opacification with central hyperdensities or calcifications on CT. **Why surgery cures**: removal of the mass and restoring drainage eliminates it; antifungals are unnecessary.

### CC-rhinology-23.1 (concept check)

Stem: An immunocompetent 60-year-old has unilateral maxillary opacification with central calcifications on CT. Endoscopic removal reveals a dense fungal mass with no tissue invasion. What further treatment is needed?

- **Correct:** None beyond removal and drainage
- Distractor: Six weeks of systemic antifungals — _why wrong:_ Fungal balls are noninvasive; systemic therapy adds toxicity without benefit.
- Distractor: Months of topical antifungal rinses — _why wrong:_ Topical antifungals are unnecessary once the mass is removed and drainage restored.
- Distractor: Oral steroids to prevent recurrence — _why wrong:_ Steroids are used for AFRS, an allergic disease, not for a fungal ball.

Explanation: A fungal ball is a noninvasive mass of hyphae that grows in a poorly draining sinus. Removing it and widening the ostium cures it.

Pearl: Fungal ball: remove it and restore drainage; no antifungals.

## T-rhinology-24 — Immunodeficiency-Associated Chronic Rhinosinusitis
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-24.overview**

Immunodeficiency underlies a meaningful share of refractory or recurrent rhinosinusitis, especially antibody deficiencies. Recognizing it changes treatment (immunoglobulin replacement, vaccines, prophylaxis).

**T-rhinology-24.physiology**

**Antibody defense**: IgA protects mucosal surfaces; IgG opsonizes encapsulated bacteria. **Specific antibody response**: vaccine responses to polysaccharide antigens test functional antibody production.

**T-rhinology-24.pathophysiology**

**Common variable immunodeficiency**: low IgG, IgA, and often IgM with poor vaccine responses, causing recurrent sinopulmonary infections. **Specific antibody deficiency**: normal immunoglobulin levels but poor responses to pneumococcal polysaccharides. **Selective IgA deficiency**: common, often mild, but can raise sinopulmonary infection risk. **Encapsulated organisms**: S. pneumoniae and H. influenzae require antibody opsonization, explaining recurrent infections. **HIV and iatrogenic immunosuppression**: increase both bacterial and fungal sinusitis risk.

### CC-rhinology-24.1 (concept check)

Stem: A 30-year-old has recurrent sinusitis and two pneumonias in a year. IgG, IgA, and IgM levels are normal, but titers do not rise after pneumococcal polysaccharide vaccination. What is the diagnosis?

- **Correct:** Specific antibody deficiency
- Distractor: Common variable immunodeficiency — _why wrong:_ CVID requires low IgG with low IgA or IgM.
- Distractor: Selective IgA deficiency — _why wrong:_ That diagnosis requires a low IgA level.
- Distractor: Normal humoral immunity — _why wrong:_ Failure to respond to polysaccharide vaccine is abnormal.

Explanation: Specific antibody deficiency has normal immunoglobulin levels but poor polysaccharide responses, impairing opsonization of encapsulated bacteria. Treatment includes conjugate vaccines, prophylaxis, or immunoglobulin replacement.

Pearl: Recurrent sinopulmonary infections: check immunoglobulins and vaccine responses.

## T-rhinology-25 — Inferior Turbinate Hypertrophy
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-25.overview**

Inferior turbinate hypertrophy is enlargement of the turbinate mucosa or bone that obstructs nasal airflow, often from rhinitis. Treatment balances airway improvement against preserving the turbinate's warming and humidifying function to avoid empty nose syndrome.

**T-rhinology-25.physiology**

**Erectile tissue**: venous sinusoids in the submucosa engorge and shrink under autonomic control, regulating airway resistance. **Internal valve region**: the head of the inferior turbinate sits near the internal nasal valve, the narrowest point of the airway. **Air conditioning**: the turbinates create turbulence that maximizes mucosal contact for warming, humidification, and particle deposition. **Sensation of airflow**: TRPM8 cold receptors in the mucosa sense airflow cooling, which is perceived as nasal patency.

**T-rhinology-25.pathophysiology**

**Mucosal hypertrophy**: chronic allergic, nonallergic, or medication-induced inflammation causes submucosal edema, fibrosis, and glandular hyperplasia. **Bony hypertrophy**: a large conchal bone contributes in some patients and does not respond to medical therapy. **Compensatory hypertrophy**: the turbinate opposite a septal deviation enlarges to fill the extra space. **Rhinitis medicamentosa**: rebound vasodilation after topical decongestant overuse causes persistent swelling. **Surgical rationale**: submucosal reduction shrinks the erectile tissue or bone while preserving the mucosal surface; aggressive resection destroys airflow sensation and conditioning.

### CC-rhinology-25.1 (concept check)

Stem: A 34-year-old with chronic nasal obstruction from inferior turbinate hypertrophy that persists despite steroid sprays asks the surgeon to remove both turbinates completely. Why is mucosa-sparing submucosal reduction preferred?

- **Correct:** Turbinate mucosa senses and conditions airflow
- Distractor: Full resection causes uncontrollable bleeding — _why wrong:_ Bleeding risk exists, but it is manageable and is not the main reason to preserve the turbinate.
- Distractor: The turbinate bone regrows after resection — _why wrong:_ The concern is the opposite: lost mucosal function is permanent.
- Distractor: The turbinate supports the nasal sidewall — _why wrong:_ The inferior turbinate does not structurally support the external nasal valve.

Explanation: Turbinate mucosa warms and humidifies air and carries TRPM8 cold receptors that signal patency. Aggressive resection can cause empty nose syndrome: a wide airway that feels blocked.

Pearl: Reduce the turbinate; do not remove it.

## T-rhinology-26 — Intracranial Complications of Sinusitis
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-26.overview**

Intracranial complications of sinusitis (epidural, subdural, and brain abscess, meningitis, venous sinus thrombosis, and Pott puffy tumor) are most common in adolescent boys with frontal sinusitis. They require neurosurgical and sinus drainage plus prolonged IV antibiotics.

**T-rhinology-26.physiology**

**Frontal sinus posterior table**: separates the sinus from the frontal lobe dura. **Diploic veins of Breschet**: valveless veins connect the sinus mucosa, frontal bone marrow, and dural venous system. **Adolescent frontal sinus**: rapidly pneumatizing with a rich diploic venous supply.

**T-rhinology-26.pathophysiology**

**Spread**: retrograde thrombophlebitis through valveless diploic veins or direct erosion through bone. **Osteomyelitis**: frontal bone infection with subperiosteal abscess produces Pott puffy tumor (forehead swelling). **Intracranial collections**: epidural abscess, subdural empyema (rapidly progressive), and frontal lobe abscess, often with subtle early symptoms (headache, behavior change). **Microbiology**: Streptococcus anginosus group and anaerobes. **Treatment logic**: drainage of the intracranial collection and the source sinus plus prolonged antibiotics.

### CC-rhinology-26.1 (concept check)

Stem: A 15-year-old boy with frontal sinusitis develops a soft forehead swelling and severe headache. CT shows frontal bone osteomyelitis with a subperiosteal abscess and a small epidural collection. Which anatomic feature explains this spread?

- **Correct:** Valveless diploic veins
- Distractor: A dehiscent cribriform plate — _why wrong:_ The cribriform plate is not the route for frontal bone osteomyelitis.
- Distractor: Hematogenous seeding from the lungs — _why wrong:_ The source is contiguous frontal sinus infection.
- Distractor: Lymphatic channels to the dura — _why wrong:_ Spread is venous and direct, not lymphatic.

Explanation: Adolescent frontal sinuses have rich diploic venous drainage (veins of Breschet) that lets infection reach bone (Pott puffy tumor) and the intracranial space by retrograde thrombophlebitis.

Pearl: Frontal sinusitis + forehead swelling in a teen = Pott puffy tumor: image the brain.

## T-rhinology-27 — Invasive Fungal Rhinosinusitis
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-27.overview**

Acute invasive fungal rhinosinusitis is angioinvasive fungal infection (Mucorales, Aspergillus) in immunocompromised hosts that spreads in hours to days. It is a surgical emergency requiring early biopsy, debridement, antifungals, and reversal of immunosuppression.

**T-rhinology-27.physiology**

**Neutrophil defense**: neutrophils and macrophages kill inhaled spores and hyphae. **Iron sequestration**: transferrin binds free iron, limiting fungal growth. **Vascular supply**: rich mucosal blood supply of the turbinates, septum, and palate.

**T-rhinology-27.pathophysiology**

**Host susceptibility**: neutropenia, uncontrolled diabetes with ketoacidosis, steroids, and transplant immunosuppression impair killing. **Ketoacidosis**: acidosis releases iron from transferrin, and Mucorales use iron to grow; these fungi also have ketone reductase. **Angioinvasion**: hyphae invade vessel walls, causing thrombosis, infarction, and necrotic tissue, which appears pale or black and insensate. **Early sign**: loss of mucosal sensation and pallor of the middle turbinate or septum precede black eschar. **Spread**: through vessels and perineural routes to the orbit (vision loss, ophthalmoplegia), cavernous sinus, and brain. **Treatment logic**: necrotic tissue has no blood supply so antifungals cannot reach it, which is why debridement to bleeding tissue is essential.

### CC-rhinology-27.1 (concept check)

Stem: A neutropenic patient with leukemia has fever and facial pain. Endoscopy shows a pale, insensate middle turbinate without black eschar yet. What is the most important next step?

- **Correct:** Urgent biopsy with frozen section
- Distractor: Repeat sinus CT in 48 hours — _why wrong:_ Waiting allows hours-to-days spread into the orbit and brain.
- Distractor: Topical antifungal irrigations — _why wrong:_ Topical therapy cannot reach angioinvasive disease in thrombosed tissue.
- Distractor: Oral antibiotics for bacterial sinusitis — _why wrong:_ This is presumed invasive fungal disease until biopsy excludes it.

Explanation: Angioinvasive fungi thrombose vessels, so mucosa becomes pale and insensate before black eschar appears. Biopsy confirms the diagnosis and guides debridement to bleeding tissue, systemic antifungals, and reversal of immunosuppression.

Pearl: Pale, insensate mucosa in an immunocompromised host is invasive fungal sinusitis until biopsy says otherwise.

## T-rhinology-28 — Juvenile Nasopharyngeal Angiofibroma
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-28.overview**

Juvenile nasopharyngeal angiofibroma (JNA) is a benign but locally aggressive, highly vascular tumor in adolescent males, arising near the sphenopalatine foramen. It presents with unilateral obstruction and severe epistaxis and is resected endoscopically after embolization.

**T-rhinology-28.physiology**

**Sphenopalatine foramen region**: connects the nasal cavity to the pterygopalatine fossa, where the internal maxillary artery branches. **Pterygoid base**: the vidian canal and pterygoid plates lie just below.

**T-rhinology-28.pathophysiology**

**Hormonal influence**: androgen receptors in tumor cells explain occurrence in adolescent males. **Vascular malformation component**: irregular vessels without smooth muscle cannot contract, causing severe bleeding. **Spread**: grows along paths of least resistance into the nasopharynx, pterygopalatine fossa, infratemporal fossa, sphenoid, orbit, and middle cranial fossa. **Imaging signs**: anterior bowing of the posterior maxillary wall (Holman-Miller sign) and widening of the pterygopalatine fossa. **Recurrence**: residual tumor in the vidian canal and pterygoid base causes recurrence, so drilling the basisphenoid matters. **No biopsy in clinic**: biopsy can cause life-threatening bleeding.

### CC-rhinology-28.1 (concept check)

Stem: A 15-year-old boy has unilateral nasal obstruction and recurrent severe epistaxis. CT shows a mass centered at the sphenopalatine foramen with anterior bowing of the posterior maxillary wall. Why should biopsy not be performed in clinic?

- **Correct:** Its vessels cannot constrict
- Distractor: Biopsy seeds malignant cells — _why wrong:_ JNA is benign; the danger of biopsy is hemorrhage.
- Distractor: The mass is cystic and collapses — _why wrong:_ JNA is a solid vascular tumor.
- Distractor: Biopsy triggers rapid tumor growth — _why wrong:_ Biopsy does not accelerate growth.

Explanation: JNA vessels lack a normal smooth muscle layer and cannot vasoconstrict, so biopsy can cause life-threatening bleeding. Imaging is characteristic, and treatment is embolization followed by endoscopic resection.

Pearl: Adolescent male + unilateral obstruction + epistaxis = JNA: image, do not biopsy.

## T-rhinology-29 — Local Allergic Rhinitis
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-29.overview**

Local allergic rhinitis is allergic-type rhinitis with negative skin and serum testing but local nasal IgE production and a positive nasal allergen challenge. It explains some patients labeled nonallergic who respond to allergy treatments.

**T-rhinology-29.physiology**

**Mucosal immune tissue**: the nasal mucosa contains dendritic cells, T cells, B cells, and mast cells that sample inhaled allergens directly. **Local class switching**: B cells in the nasal mucosa can switch to IgE production in place, without that IgE reaching the bloodstream in measurable amounts. **Mast-cell arming**: locally produced IgE binds FcεRI receptors on nasal mast cells, which is all that is needed for an allergic response at that site. **Systemic tests sample elsewhere**: skin prick tests sample skin mast cells and serum tests sample circulating IgE, so a purely mucosal process can be missed.

**T-rhinology-29.pathophysiology**

**Local sensitization**: specific IgE is produced in the nasal mucosa without systemic sensitization. **Same effector pathway**: mast-cell activation produces typical allergic symptoms on exposure. **Diagnosis**: nasal allergen provocation testing, as systemic tests are negative. **Treatment**: responds to standard allergic rhinitis medications and possibly immunotherapy.

## T-rhinology-30 — Mucocele
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-30.overview**

A mucocele is an epithelium-lined, mucus-filled sac that expands a sinus after outflow obstruction, most often frontal or frontoethmoid. It remodels bone slowly and can push into the orbit or cranium, and is treated by endoscopic marsupialization.

**T-rhinology-30.physiology**

**Ventilation and drainage**: sinus mucus is constantly produced and cleared through patent ostia. **Bone remodeling**: bone responds to pressure by resorption on one side and new formation on the other.

**T-rhinology-30.pathophysiology**

**Obstruction**: prior surgery, trauma, polyps, tumor, or chronic inflammation block an outflow tract. **Expansion**: continued mucus secretion into a closed space raises pressure and stimulates bone remodeling through osteoclast-activating factors. **Mass effect**: frontoethmoid mucoceles cause proptosis, diplopia, and orbital displacement; sphenoid mucoceles can compress the optic nerve. **Mucopyocele**: infection adds urgency, with pain and orbital or intracranial complications. **Treatment logic**: marsupialization opens the sac widely into the nasal cavity, restoring drainage; the lining can be left in place.

### CC-rhinology-30.1 (concept check)

Stem: A 60-year-old who had frontal sinus fracture repair 20 years ago now has slowly progressive proptosis and diplopia. CT shows an expanded frontoethmoid sinus with thinned, remodeled bone. What drives the expansion?

- **Correct:** Mucus secretion into an obstructed sinus
- Distractor: Tumor growth within the sinus — _why wrong:_ A mucocele is an epithelium-lined sac of mucus, not a neoplasm.
- Distractor: Allergic fungal mucin accumulation — _why wrong:_ AFRS expands sinuses with eosinophilic mucin in atopic patients, not after remote trauma.
- Distractor: Gas-forming bacterial infection — _why wrong:_ Gas is not the mechanism; pressure from trapped mucus is.

Explanation: Prior trauma or surgery obstructs the outflow tract. Continued mucus secretion into a closed space raises pressure and drives bone remodeling. Endoscopic marsupialization restores drainage.

Pearl: Expansile sinus years after trauma or surgery = mucocele.

## T-rhinology-31 — Nasal Anatomy for Endoscopy
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-31.overview**

Endoscopic nasal anatomy (septum, turbinates, meatuses, ostiomeatal complex, sphenoethmoidal recess, and skull base) is the map behind every rhinology diagnosis and procedure. Knowing the landmarks and variants is what keeps sinus surgery safe.

**T-rhinology-31.physiology**

**Lateral wall**: the inferior, middle, and superior turbinates overlie meatuses; the nasolacrimal duct opens in the inferior meatus. **Middle meatus**: holds the uncinate process, ethmoid infundibulum, maxillary ostium, ethmoid bulla, and hiatus semilunaris. **Basal lamellae**: the middle turbinate basal lamella divides anterior from posterior ethmoid cells. **Posterior drainage**: posterior ethmoids drain to the superior meatus; the sphenoid drains to the sphenoethmoidal recess medial to the superior turbinate. **Skull base**: slopes downward from anterior to posterior; the lamina papyracea forms the lateral wall of the ethmoids. **Arteries**: the sphenopalatine artery enters behind the middle turbinate; anterior and posterior ethmoid arteries cross the ethmoid roof.

**T-rhinology-31.pathophysiology**

**Variants that obstruct**: concha bullosa, paradoxical middle turbinate, Haller (infraorbital) cells, and large agger nasi cells narrow drainage pathways. **Variants that endanger**: Onodi (sphenoethmoidal) cells can surround the optic nerve; dehiscent carotid or optic canals in the sphenoid; a deep Keros type III olfactory fossa makes the lateral lamella vulnerable; a dehiscent lamina papyracea risks orbital entry. **Maxillary ostium location**: the natural ostium is hidden behind the uncinate; accessory ostia cause recirculation if not joined to it. **Why the CT checklist**: preoperative review of each danger variant (e.g., CLOSE: cribriform, lamina, Onodi, sphenoid, ethmoid arteries) prevents complications.

## T-rhinology-32 — Nonallergic Rhinitis / Rhinitis Medicamentosa
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-32.overview**

Nonallergic rhinitis is chronic nasal symptoms without allergic sensitization: vasomotor, gustatory, drug-induced, hormonal, and atrophic types. Rhinitis medicamentosa is rebound congestion from overuse of topical decongestants.

**T-rhinology-32.physiology**

**Autonomic balance**: sympathetic tone keeps venous sinusoids constricted; parasympathetic tone drives secretion and congestion. **Sensory nerves**: trigeminal C fibers with TRPV1 receptors respond to irritants, temperature, and chemicals. **Adrenergic receptors**: alpha receptors on vessels mediate decongestion.

**T-rhinology-32.pathophysiology**

**Vasomotor rhinitis**: neural hyperreactivity to irritants, temperature, and odors through TRPV1 and parasympathetic reflexes. **Gustatory rhinitis**: eating triggers vagal cholinergic reflexes, producing watery rhinorrhea (responsive to ipratropium). **Rhinitis medicamentosa**: repeated alpha-agonist use downregulates receptors and causes rebound vasodilation and tolerance, creating a cycle of escalating use. **Drug-induced rhinitis**: antihypertensives, PDE5 inhibitors, and hormones alter vascular tone. **Hormonal rhinitis**: estrogen increases vascular congestion in pregnancy. **Atrophic rhinitis**: loss of mucosa and glands after aggressive surgery or radiation causes crusting and paradoxical obstruction.

### CC-rhinology-32.1 (concept check)

Stem: A 32-year-old has used oxymetazoline spray several times daily for 2 months. Each dose works for a shorter time, and her congestion is now worse than before she started. What is the mechanism?

- **Correct:** Rebound vasodilation
- Distractor: Allergic sensitization to the spray — _why wrong:_ This is a pharmacologic effect, not an allergy to the drug.
- Distractor: Chronic bacterial rhinosinusitis — _why wrong:_ Infection does not explain shortening response and rebound congestion.
- Distractor: Septal perforation from the spray — _why wrong:_ Vasoconstrictor overuse can injure mucosa, but perforation does not cause rebound congestion.

Explanation: Repeated alpha-agonist use downregulates adrenergic receptors and causes rebound vasodilation, creating escalating use. Treatment is stopping the decongestant with intranasal steroid support.

Pearl: Topical decongestants: no more than a few days.

## T-rhinology-33 — Objective Assessment of Nasal Function
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-33.overview**

Objective tests (acoustic rhinometry, rhinomanometry, peak nasal inspiratory flow, and smell testing) supplement symptoms and exam in nasal obstruction and olfactory loss. They help explain discordance between what patients feel and what clinicians see.

**T-rhinology-33.physiology**

**Airflow and resistance**: nasal resistance accounts for about half of total airway resistance, concentrated at the internal valve. **Cross-sectional area**: acoustic rhinometry uses reflected sound to map area along the nasal cavity. **Pressure-flow relationship**: rhinomanometry measures transnasal pressure and flow to calculate resistance.

**T-rhinology-33.pathophysiology**

**Mismatch of perception and measurement**: patency sensation depends on mucosal cooling (TRPM8 receptors) as much as on actual resistance, so measurements and symptoms often correlate poorly. **Decongestion testing**: comparing before and after decongestant distinguishes mucosal (reversible) from structural (fixed) obstruction. **Smell testing**: validated scratch-and-sniff tests (UPSIT) and threshold-discrimination-identification tests quantify loss and detect malingering. **Empty nose context**: patients with large airways may still report obstruction because of lost sensation.

### CC-rhinology-33.1 (concept check)

Stem: A 45-year-old reports severe nasal obstruction 3 years after bilateral total inferior turbinectomy. Acoustic rhinometry shows a very large nasal cross-sectional area. What explains the mismatch?

- **Correct:** Loss of mucosal cold receptors
- Distractor: Inaccurate rhinometry measurement — _why wrong:_ Rhinometry is accurate here; the problem is perception.
- Distractor: A missed posterior septal deviation — _why wrong:_ A large measured airway argues against significant structural obstruction.
- Distractor: Purely psychogenic symptoms — _why wrong:_ A physiologic sensory loss explains the symptoms.

Explanation: Patency is sensed by mucosal cooling detected by TRPM8 receptors. Removing turbinate mucosa reduces this sensation, so a wide airway can feel blocked.

Pearl: Feeling blocked is not the same as being blocked.

## T-rhinology-34 — Odontogenic Sinusitis
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-34.overview**

Odontogenic sinusitis is maxillary sinus infection from a dental source: periapical infection, oroantral fistula, or dental implant and graft complications. It is often unilateral and foul-smelling, and it fails unless the dental source is treated.

**T-rhinology-34.physiology**

**Root proximity**: the roots of the maxillary premolars and molars (especially the first and second molars) lie just beneath, and sometimes project into, the maxillary sinus floor, separated by thin bone or only mucosa. **Schneiderian membrane**: lines the sinus floor and is all that separates some roots from the sinus. **Drainage path**: maxillary mucus must climb to the natural ostium high on the medial wall, so floor infections drain poorly. **Oral vs sinus flora**: normally separated by bone and mucosa.

**T-rhinology-34.pathophysiology**

**Spread**: periapical abscess or periodontal infection erodes the thin floor and spreads to the sinus. **Polymicrobial anaerobes**: oral anaerobes cause foul-smelling, unilateral purulent drainage. **Iatrogenic routes**: extractions creating oroantral fistulas, implants, or bone grafts in the sinus. **Why ENT treatment alone fails**: an ongoing dental source reseeds the sinus, so coordinated dental treatment and often endoscopic surgery are needed. **Imaging clue**: unilateral maxillary disease with periapical lucency or dental pathology on CT.

### CC-rhinology-34.1 (concept check)

Stem: A 50-year-old has unilateral foul-smelling maxillary sinusitis that keeps relapsing after antibiotics. CT shows periapical lucency around the left upper first molar root, which projects into the sinus floor. What is required for cure?

- **Correct:** Treatment of the dental source
- Distractor: A longer course of antibiotics alone — _why wrong:_ An untreated dental source keeps reseeding the sinus regardless of antibiotic duration.
- Distractor: Allergen immunotherapy — _why wrong:_ Allergy does not cause unilateral foul odontogenic infection.
- Distractor: Septoplasty to improve drainage — _why wrong:_ The septum is not the source; the infected tooth is.

Explanation: Maxillary molar roots lie next to or within the sinus floor, so periapical infection spreads directly into the sinus with polymicrobial anaerobes (foul odor). Coordinated dental treatment, often with endoscopic sinus drainage, is needed.

Pearl: Unilateral foul maxillary sinusitis: look at the teeth.

## T-rhinology-35 — Olfactory Dysfunction
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-35.overview**

Olfactory dysfunction ranges from reduced smell (hyposmia) to total loss (anosmia) and distorted smell (parosmia). It is common after viral infection, with CRS, after head trauma, and in neurodegenerative disease, and it affects safety, nutrition, and quality of life.

**T-rhinology-35.physiology**

**Olfactory epithelium**: high in the nasal vault (olfactory cleft) along the cribriform plate, superior septum, and superior turbinate. **Receptor neurons**: bipolar neurons with cilia carrying odorant receptors (about 400 functional types); each neuron expresses one receptor type. **Regeneration**: olfactory neurons are replaced from basal stem cells throughout life, which is unusual for neurons. **Pathway**: axons pass through the cribriform plate to glomeruli in the olfactory bulb, then to piriform cortex, amygdala, and entorhinal cortex without a thalamic relay. **Retronasal smell**: odors from the mouth reach the epithelium through the nasopharynx and create most of what we call flavor.

**T-rhinology-35.pathophysiology**

**Conductive loss**: polyps, edema, or obstruction prevent odorants from reaching the olfactory cleft; this is often reversible with steroids or surgery. **Post-viral loss**: viruses damage supporting (sustentacular) cells and receptor neurons; SARS-CoV-2 targets sustentacular cells, and recovery depends on regeneration. **Parosmia**: miswired regenerating neurons produce distorted, often unpleasant perceptions during recovery. **Post-traumatic loss**: shearing of olfactory axons at the cribriform plate or contusion of the bulbs and frontal lobes; recovery is less likely. **Neurodegenerative link**: early smell loss precedes Parkinson and Alzheimer disease because pathology involves olfactory structures early. **Olfactory training**: repeated structured exposure to odors may promote neural regeneration and plasticity.

### CC-rhinology-35.1 (concept check)

Stem: A 40-year-old lost her sense of smell after a viral infection 4 months ago. She now reports that coffee and onions smell like garbage. What best explains the distortion?

- **Correct:** Imprecise rewiring of regenerating neurons
- Distractor: Atrophy of the olfactory bulbs — _why wrong:_ Bulb atrophy reduces smell but does not specifically cause distortion.
- Distractor: Polyps blocking the olfactory cleft — _why wrong:_ Conductive loss reduces smell; it does not distort it.
- Distractor: Temporal lobe seizure activity — _why wrong:_ Seizure-related phantosmia is rarer, episodic, and occurs without an odor stimulus.

Explanation: Olfactory receptor neurons regenerate from basal stem cells. During recovery, new neurons form imprecise glomerular connections, distorting odors (parosmia). It often signals recovery, and olfactory training may help.

Pearl: Parosmia after a viral loss often signals regeneration.

## T-rhinology-36 — Oral Allergy Syndrome (Pollen-Food Syndrome)
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-36.overview**

Oral allergy syndrome is itching and swelling of the mouth and throat after eating raw fruits or vegetables in pollen-allergic patients. It results from cross-reactivity between pollen and heat-labile food proteins.

**T-rhinology-36.physiology**

**Pan-allergens**: plants share conserved defense proteins (PR-10 proteins such as Bet v 1, profilins, lipid transfer proteins) with similar three-dimensional shapes. **Conformational epitopes**: IgE recognizes the folded shape of a protein, so a related protein from a different plant can bind the same IgE. **Heat and digestion**: PR-10 proteins and profilins unfold with cooking and are degraded quickly by saliva and gastric acid, while lipid transfer and storage proteins are stable. **Oral mast cells**: the oropharyngeal mucosa contains mast cells that react on first contact with food protein.

**T-rhinology-36.pathophysiology**

**Cross-reactivity**: birch pollen (Bet v 1) antibodies cross-react with apple, cherry, carrot, and others; ragweed with melon and banana. **Heat-labile proteins**: cooking denatures these proteins, so cooked foods are tolerated. **Localized reaction**: proteins are digested quickly, limiting symptoms mainly to the mouth. **Risk of systemic reactions**: stable proteins (lipid transfer proteins, storage proteins) can cause systemic reactions, which component testing identifies.

### CC-rhinology-36.1 (concept check)

Stem: A 28-year-old with birch pollen allergy gets itching and tingling of the mouth within minutes of eating raw apples, but tolerates apple pie. Why?

- **Correct:** Heat-labile cross-reactive proteins
- Distractor: Cooking removes surface pesticides — _why wrong:_ Pesticides are not the cause of the reaction.
- Distractor: Pie contains less apple per bite — _why wrong:_ Dose does not explain tolerance of cooked apple.
- Distractor: Raw apple skin carries bacteria — _why wrong:_ Bacteria do not cause IgE-mediated oral itching.

Explanation: Apple PR-10 proteins (Mal d 1) resemble birch Bet v 1, so birch IgE cross-reacts. These proteins are destroyed by heat and digested quickly, limiting symptoms to the mouth.

Pearl: Raw-fruit mouth itching in pollen allergy = oral allergy syndrome.

## T-rhinology-37 — Orbital Apex Syndrome
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-37.overview**

Orbital apex syndrome is dysfunction of the optic nerve plus cranial nerves III, IV, V1, and VI from a lesion at the orbital apex. Causes include invasive fungal sinusitis, inflammation, tumor, and trauma.

**T-rhinology-37.physiology**

**Superior orbital fissure**: transmits CN III, IV, V1 branches, VI, and the superior ophthalmic vein. **Optic canal**: transmits the optic nerve and ophthalmic artery. **Proximity**: both lie at the posterior orbit adjacent to the sphenoid and posterior ethmoid sinuses.

**T-rhinology-37.pathophysiology**

**Combined deficits**: vision loss, ophthalmoplegia, ptosis, and V1 numbness. **Superior orbital fissure syndrome**: the same deficits without vision loss. **Cavernous sinus extension**: adds V2 and sympathetic involvement. **Causes**: invasive fungal sinusitis (especially in diabetes and immunosuppression), bacterial infection, IgG4-related or idiopathic inflammation, malignancy, and fractures. **Urgency**: optic nerve compression causes irreversible vision loss, so rapid diagnosis is needed.

### CC-rhinology-37.1 (concept check)

Stem: A diabetic patient with sinusitis develops ophthalmoplegia, ptosis, forehead numbness, and decreasing vision in the right eye. Why does the vision loss localize the lesion to the orbital apex rather than the superior orbital fissure alone?

- **Correct:** The optic canal is also involved
- Distractor: The optic nerve runs through the fissure — _why wrong:_ The optic nerve passes through the optic canal, not the superior orbital fissure.
- Distractor: All fissure lesions cause vision loss — _why wrong:_ Superior orbital fissure syndrome spares vision.
- Distractor: Forehead numbness indicates apex disease — _why wrong:_ V1 involvement occurs in both apex and fissure syndromes.

Explanation: Orbital apex syndrome combines superior orbital fissure involvement (III, IV, V1, VI) with optic canal involvement. In a diabetic with sinusitis, invasive fungal sinusitis must be excluded urgently.

Pearl: Superior orbital fissure syndrome plus vision loss = orbital apex syndrome.

## T-rhinology-38 — Orbital Complications of Sinusitis
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-38.overview**

Orbital complications of sinusitis range from preseptal cellulitis to orbital cellulitis, subperiosteal abscess, orbital abscess, and cavernous sinus thrombosis (Chandler classification). They are most common in children with ethmoiditis and threaten vision.

**T-rhinology-38.physiology**

**Lamina papyracea**: the paper-thin lateral ethmoid wall, with natural dehiscences and neurovascular foramina. **Orbital septum**: separates preseptal tissues from the orbit proper. **Valveless veins**: ophthalmic veins connect the face, sinuses, orbit, and cavernous sinus without valves.

**T-rhinology-38.pathophysiology**

**Spread**: infection crosses the lamina papyracea or travels through valveless veins from the ethmoids into the orbit. **Preseptal cellulitis**: anterior to the septum, eyelid swelling with normal vision and eye movement. **Orbital cellulitis**: postseptal, causing chemosis, proptosis, painful or limited eye movement. **Subperiosteal abscess**: pus collects between the lamina and periorbita, displacing the globe. **Vision threat**: rising orbital pressure compresses the optic nerve and its blood supply; decreased acuity, color vision loss, or an afferent pupillary defect demand urgent drainage. **Cavernous sinus thrombosis**: bilateral findings, cranial neuropathies (III, IV, V1, V2, VI), and sepsis.

### CC-rhinology-38.1 (concept check)

Stem: A 7-year-old with ethmoid sinusitis has eyelid swelling, proptosis, and painful limited eye movement with normal vision. CT shows a small medial subperiosteal abscess. Why is the ethmoid sinus the usual source?

- **Correct:** Its thin, dehiscent lamina papyracea
- Distractor: Its ostium opens directly into the orbit — _why wrong:_ The ethmoids drain into the nose; infection reaches the orbit across bone or through veins.
- Distractor: Its mucosa lacks cilia in children — _why wrong:_ Ethmoid mucosa is ciliated in children.
- Distractor: Its veins have valves that fail with infection — _why wrong:_ Orbital and facial veins are valveless, which is what allows spread.

Explanation: Infection crosses the thin, naturally dehiscent lamina papyracea or travels through valveless veins into the orbit. Small medial abscesses in young children with normal vision may respond to IV antibiotics with close monitoring; vision changes demand drainage.

Pearl: Vision change in orbital cellulitis demands urgent drainage.

## T-rhinology-39 — Pediatric Chronic Rhinosinusitis
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-39.overview**

Pediatric CRS is chronic sinonasal inflammation in children, where adenoids play a central role and immune, ciliary, and genetic disorders must be considered. Treatment escalates from medical therapy to adenoidectomy, then sinus surgery.

**T-rhinology-39.physiology**

**Sinus development**: maxillary and ethmoid sinuses are present at birth, the sphenoid pneumatizes in early childhood, and the frontal sinus in later childhood and adolescence. **Adenoids**: nasopharyngeal lymphoid tissue that peaks in size at about 4-7 years.

**T-rhinology-39.pathophysiology**

**Adenoid reservoir**: adenoids harbor bacterial biofilms that seed the sinuses and obstruct the posterior nasal airway. **Why adenoidectomy first**: removing the reservoir resolves many cases, especially in younger children. **Underlying conditions**: allergy, immunodeficiency, cystic fibrosis, and primary ciliary dyskinesia are more likely in children with severe or refractory disease. **Polyps in children**: suggest cystic fibrosis until proven otherwise. **Facial growth concerns**: early concerns that sinus surgery impairs facial growth have not been strongly confirmed, but surgery remains limited.

### CC-rhinology-39.1 (concept check)

Stem: A 5-year-old has 4 months of purulent rhinorrhea, cough, and congestion despite saline, nasal steroids, and a 3-week antibiotic course. What is usually the first surgical step?

- **Correct:** Adenoidectomy
- Distractor: Complete endoscopic sinus surgery — _why wrong:_ FESS is reserved for children who fail adenoidectomy.
- Distractor: Septoplasty — _why wrong:_ The septum is rarely the problem in young children.
- Distractor: Inferior turbinate reduction — _why wrong:_ Turbinate surgery does not address the infectious reservoir.

Explanation: The adenoid harbors bacterial biofilms that seed the sinuses and obstruct the posterior nasal airway. Adenoidectomy, often with maxillary irrigation, resolves many cases in young children.

Pearl: In young children with CRS, start with the adenoid.

## T-rhinology-40 — Recurrent Acute Rhinosinusitis
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-40.overview**

Recurrent acute rhinosinusitis is four or more episodes of acute bacterial rhinosinusitis per year with symptom-free intervals. Evaluation looks for anatomic obstruction, allergy, and immune deficiency, and selected patients benefit from targeted sinus surgery.

**T-rhinology-40.physiology**

**Normal recovery**: after a viral cold, mucociliary clearance and ostial patency restore within days to weeks. **Ostial narrowness**: natural maxillary ostia are small, so modest edema can close them. **Host defenses**: secretory IgA, antimicrobial proteins, and intact cilia clear bacteria.

**T-rhinology-40.pathophysiology**

**Viral trigger**: each episode usually starts with a viral infection that inflames mucosa, impairs cilia, and blocks ostia. **Bacterial superinfection**: stasis allows S. pneumoniae, H. influenzae, and M. catarrhalis to multiply. **Predisposing anatomy**: Haller cells, concha bullosa, uncinate variants, and septal deviations narrow the ostiomeatal complex so normal edema causes obstruction. **Host factors**: allergy, immunodeficiency (low IgA, IgG subclass, specific antibody deficiency), and ciliary disorders raise episode frequency. **Why surgery helps selected patients**: widening the outflow tract means the same mucosal swelling no longer closes the ostium.

### CC-rhinology-40.1 (concept check)

Stem: A 30-year-old has 5 episodes per year of acute bacterial sinusitis, with a clear CT between episodes. The CT shows a large Haller (infraorbital ethmoid) cell narrowing the maxillary infundibulum. Why does this anatomy matter?

- **Correct:** Ordinary viral swelling closes a narrow outflow
- Distractor: Haller cells harbor chronic infection — _why wrong:_ Haller cells narrow the outflow tract; they are not reservoirs of chronic infection.
- Distractor: Haller cells erode the orbital floor — _why wrong:_ They lie beneath the orbit but do not erode it.
- Distractor: Haller cells block the nasolacrimal duct — _why wrong:_ They narrow the maxillary infundibulum, not the nasolacrimal duct.

Explanation: Every cold causes mucosal edema. In a narrow ostiomeatal complex, that edema closes the ostium, causing stasis and bacterial superinfection. Surgery widens the outflow so normal swelling no longer obstructs it. Immune deficiency and allergy should also be evaluated.

Pearl: Recurrent ABRS with a clear interval CT: look for obstructing anatomy and immune deficiency.

## T-rhinology-41 — Revision FESS
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-41.overview**

Revision endoscopic sinus surgery treats persistent or recurrent CRS after prior surgery, most often from incomplete dissection, scarring, or uncontrolled type 2 inflammation. Success depends on identifying why the first operation failed.

**T-rhinology-41.physiology**

**Healing**: sinus mucosa regenerates with functional cilia if preserved; exposed bone heals with fibrosis. **Stable landmarks**: in revision cases, the skull base, lamina, maxillary sinus roof, and medial orbital wall remain reliable even when turbinates are gone.

**T-rhinology-41.pathophysiology**

**Common failure patterns**: residual uncinate, unopened agger nasi or frontal cells, missed maxillary ostium with recirculation, lateralized middle turbinate, retained ethmoid partitions. **Scar and synechiae**: adhesions between the middle turbinate and lateral wall obstruct drainage. **Osteitis and neo-osteogenesis**: inflamed bone thickens and narrows outflow tracts, especially the frontal recess. **Disease biology**: eosinophilic CRSwNP, AERD, and AFRS recur despite good surgery, so medical maintenance and biologics matter. **Revision risk**: distorted landmarks increase the danger of skull-base and orbital injury, which favors image guidance.

### CC-rhinology-41.1 (concept check)

Stem: A patient has persistent maxillary sinusitis after FESS. Endoscopy shows an antrostomy in the posterior fontanelle, separate from the natural ostium hidden behind a retained uncinate. What problem does this cause?

- **Correct:** Mucus recirculation
- Distractor: Excess airflow drying the sinus — _why wrong:_ Airflow is not the mechanism of persistent infection here.
- Distractor: Collapse of the orbital floor — _why wrong:_ Separate openings do not collapse the orbit.
- Distractor: Obstruction of the nasolacrimal duct — _why wrong:_ The duct lies anterior; a posterior fontanelle opening does not block it.

Explanation: Cilia carry mucus to the natural ostium regardless of other openings. Mucus exits there and re-enters through the separate antrostomy, keeping the sinus infected. Revision removes the uncinate remnant and joins the openings.

Pearl: Always incorporate the natural ostium.

## T-rhinology-42 — Septal Deviation
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-42.overview**

Septal deviation is displacement of the cartilaginous or bony septum causing nasal obstruction when it narrows the valve or airway. It is extremely common; it needs correction only when it causes symptoms or blocks access, and septoplasty preserves an L-strut for support.

**T-rhinology-42.physiology**

**Components**: quadrangular cartilage anteriorly, perpendicular plate of the ethmoid posterosuperiorly, vomer posteroinferiorly, and the maxillary crest inferiorly. **Support**: the caudal and dorsal septum form an L-shaped strut that supports the nasal dorsum and tip. **Internal valve**: the angle between the septum and upper lateral cartilage (normally 10-15 degrees) is the narrowest airway segment. **Poiseuille physics**: airway resistance rises steeply as radius falls (to the fourth power in laminar flow), so small narrowing at the valve matters greatly.

**T-rhinology-42.pathophysiology**

**Origins**: developmental asymmetry or trauma (including birth trauma) displaces cartilage, often with spurs at the vomer-cartilage junction. **Obstruction**: anterior and caudal deviations near the valve produce more obstruction than posterior deviations. **Secondary effects**: compensatory turbinate hypertrophy, sinus outflow obstruction, mucosal drying and crusting on the convex side, and epistaxis. **Septal cartilage memory**: cartilage tends to return to its deviated shape unless intrinsic stresses are released. **Support loss**: overresection of the L-strut causes saddle nose and columellar retraction, which is why at least about 1 cm of dorsal and caudal strut is preserved.

### CC-rhinology-42.1 (concept check)

Stem: A 28-year-old has a deviated septum causing nasal obstruction and undergoes septoplasty. During cartilage resection, why must at least about 1 cm of dorsal and caudal septal cartilage be preserved?

- **Correct:** It supports the nasal dorsum and tip
- Distractor: It carries the septal blood supply — _why wrong:_ Blood supply runs in the mucoperichondrium, not in the cartilage strut itself.
- Distractor: It anchors the inferior turbinates — _why wrong:_ The turbinates attach to the lateral nasal wall, not the septum.
- Distractor: It prevents postoperative hematoma — _why wrong:_ Hematoma is prevented by closure and quilting sutures, not by strut width.

Explanation: The L-shaped dorsal and caudal strut is the main support of the cartilaginous dorsum and tip. Overresection causes saddle nose, columellar retraction, and tip ptosis.

Pearl: Preserve the L-strut.

## T-rhinology-43 — Silent Sinus Syndrome
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-43.overview**

Silent sinus syndrome is painless, progressive enophthalmos and hypoglobus from collapse of the maxillary sinus after chronic ostial obstruction. It is treated by maxillary antrostomy, with orbital floor repair if needed.

**T-rhinology-43.physiology**

**Orbital floor = sinus roof**: the maxillary sinus roof is a thin plate that forms the orbital floor and carries the infraorbital nerve. **Gas exchange**: sinus mucosa continuously absorbs oxygen and nitrogen into the bloodstream, just as middle-ear mucosa does. **Ostial ventilation**: an open natural ostium lets nasal air replace absorbed gas, holding the sinus near atmospheric pressure. **Wall compliance**: the sinus walls are thin bone that can remodel under sustained pressure differences, in either direction.

**T-rhinology-43.pathophysiology**

**Ostial occlusion**: closure traps the sinus. **Negative pressure**: gas absorption creates sustained negative pressure, pulling the sinus walls inward. **Atelectasis**: the walls thin and retract, and the orbital floor sags into the sinus. **Eye findings**: enophthalmos and hypoglobus develop without pain or diplopia early. **Treatment logic**: restoring ventilation stops progression; floor reconstruction corrects persistent globe malposition.

### CC-rhinology-43.1 (concept check)

Stem: A 40-year-old notices her left eye looks sunken. She has no pain or diplopia. CT shows a small, completely opacified left maxillary sinus with inward-bowed walls and a lowered orbital floor. What is the mechanism?

- **Correct:** Negative pressure after ostial occlusion
- Distractor: Remote orbital floor blowout fracture — _why wrong:_ No trauma history, and the sinus walls are bowed inward rather than fractured.
- Distractor: Expansile mucocele — _why wrong:_ Mucoceles expand sinus walls outward, not inward.
- Distractor: Fibrous dysplasia of the maxilla — _why wrong:_ Fibrous dysplasia expands bone rather than collapsing the sinus.

Explanation: Ostial occlusion lets mucosa absorb gas, creating sustained negative pressure that collapses the sinus walls and pulls the orbital floor down. Maxillary antrostomy stops progression.

Pearl: Painless enophthalmos with a small collapsed maxillary sinus = silent sinus syndrome.

## T-rhinology-44 — Sinonasal Inverted Papilloma
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-44.overview**

Inverted papilloma is a benign but locally aggressive epithelial tumor of the lateral nasal wall with a recurrence risk and about 5-10 percent association with squamous cell carcinoma. Treatment is complete endoscopic resection including the attachment site.

**T-rhinology-44.physiology**

**Schneiderian membrane**: the ectodermally derived ciliated respiratory mucosa lining the nose and sinuses, distinct from the endodermal mucosa of the lower airway. **Epithelial turnover**: basal cells continuously renew the epithelium, a process that viral infection and carcinogens can dysregulate. **Basement membrane**: a structural barrier between epithelium and stroma; benign tumors respect it, while invasive carcinoma crosses it. **Lateral wall**: the middle meatus and maxillary sinus are exposed to the highest inhaled particle and viral load.

**T-rhinology-44.pathophysiology**

**Endophytic growth**: epithelium grows inward (inverts) into the stroma while keeping an intact basement membrane. **Origin site**: usually the lateral nasal wall or maxillary sinus; the attachment pedicle often shows focal hyperostosis on CT, which helps locate it. **HPV association**: low-risk HPV types are found in some; high-risk types and EGFR mutations are linked to malignant transformation. **Recurrence mechanism**: residual disease at the attachment site regrows, so subperiosteal dissection and drilling of the attachment bone matter. **Malignancy**: synchronous or metachronous SCC occurs, so all tissue is sent for pathology and surveillance is long-term.

### CC-rhinology-44.1 (concept check)

Stem: A 55-year-old has a unilateral lobulated nasal mass. CT shows opacification of the maxillary sinus with a focal cone of hyperostosis on its anterolateral wall. Why is that finding surgically useful?

- **Correct:** It marks the tumor's attachment site
- Distractor: It proves malignant transformation — _why wrong:_ Focal hyperostosis is common in benign inverted papilloma; bone destruction is more concerning for malignancy.
- Distractor: It indicates superimposed fungal disease — _why wrong:_ Fungal balls show central calcifications, not focal wall hyperostosis.
- Distractor: It predicts response to radiation — _why wrong:_ Hyperostosis has no bearing on radiosensitivity.

Explanation: Inverted papilloma recurs from residual disease at its attachment. Focal hyperostosis localizes that pedicle, guiding subperiosteal dissection and drilling of the underlying bone.

Pearl: Find the hyperostosis, find the pedicle.

## T-rhinology-45 — Sinonasal Malignancy
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-45.overview**

Sinonasal malignancies are a diverse group (SCC, adenocarcinoma, esthesioneuroblastoma, SNUC, mucosal melanoma, and others) that present late with unilateral symptoms. Histology drives treatment more than in most head and neck sites.

**T-rhinology-45.physiology**

**Confined spaces**: the sinuses are bony boxes adjacent to the orbit, skull base, and pterygopalatine fossa. **Lymphatics**: the sinonasal tract drains to retropharyngeal and level II nodes, but early nodal spread is uncommon. **Olfactory epithelium**: specialized neuroepithelium at the cribriform plate.

**T-rhinology-45.pathophysiology**

**Occupational exposures**: wood dust (intestinal-type adenocarcinoma, ethmoid), leather dust, nickel, and formaldehyde. **Silent growth**: tumors fill air spaces before causing symptoms, so they present late with unilateral obstruction, epistaxis, facial numbness, proptosis, or trismus. **Spread paths**: orbital invasion, skull base and dural invasion, and perineural spread along V2 into the pterygopalatine fossa. **Histology matters**: esthesioneuroblastoma arises from olfactory neuroepithelium (Kadish/Hyams grading); SNUC and SMARCB1-deficient carcinomas are aggressive and often treated with induction chemotherapy; mucosal melanoma has poor survival. **Treatment logic**: complete resection (often endoscopic) with adjuvant radiation for most, guided by histology.

### CC-rhinology-45.1 (concept check)

Stem: A 62-year-old cabinetmaker has 6 months of unilateral nasal obstruction and intermittent epistaxis. Biopsy of an ethmoid mass shows intestinal-type adenocarcinoma. Why do these tumors usually present at an advanced stage?

- **Correct:** They fill air spaces before causing symptoms
- Distractor: They are slow, benign-behaving lesions — _why wrong:_ Sinonasal adenocarcinoma is a malignancy capable of skull base and orbital invasion.
- Distractor: They first metastasize to the neck — _why wrong:_ Early nodal spread is uncommon; local growth dominates.
- Distractor: They produce only allergy-like symptoms — _why wrong:_ Unilateral obstruction and bleeding are not typical allergy symptoms.

Explanation: The sinuses are air-filled boxes, so tumors grow silently until they obstruct, bleed, or invade the orbit, skull base, or nerves. Wood dust exposure is strongly linked to ethmoid adenocarcinoma.

Pearl: Unilateral sinonasal symptoms in an adult warrant endoscopy and imaging.

## T-rhinology-46 — Sphenoidotomy
_source: pathophys_v470/rhinology_a.py_

**T-rhinology-46.overview**

Endoscopic sphenoidotomy opens the sphenoid sinus through its natural ostium (transnasal) or through the posterior ethmoids (transethmoidal). The sphenoid's walls carry the optic nerve and carotid artery, making anatomic precision essential.

**T-rhinology-46.physiology**

**Natural ostium**: in the sphenoethmoidal recess, medial to the superior turbinate, about 1.5 cm above the choana. **Lateral wall**: optic nerve superolaterally and internal carotid inferolaterally, with the opticocarotid recess between. **Pneumatization**: conchal, presellar, or sellar types; extensive pneumatization can involve the pterygoid processes and lateral recess. **Septations**: intersinus septa often insert onto the carotid canal.

**T-rhinology-46.pathophysiology**

**Isolated sphenoid disease**: fungal ball, mucocele, inflammation, or tumor causes deep headache and, with lateral extension, optic or cranial nerve symptoms. **Danger**: dehiscent carotid or optic canals (in a meaningful minority) and septations attached to the carotid mean twisting a septum can lacerate the artery. **Onodi cell**: a posterior ethmoid cell lateral and superior to the sphenoid can carry the optic nerve, misleading the surgeon. **Safe entry**: opening medially and inferiorly at the natural ostium avoids the lateral wall structures.

## T-rhinology-47 — Systemic Disease of the Nose / Sinuses
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-47.overview**

Systemic diseases (granulomatosis with polyangiitis, sarcoidosis, EGPA, lymphoma, and infections) can present with sinonasal symptoms, crusting, septal perforation, or saddle nose. They require biopsy, labs, and systemic therapy rather than routine sinus surgery.

**T-rhinology-47.physiology**

**Septal cartilage nutrition**: septal cartilage is avascular and depends on diffusion from the overlying mucoperichondrium, so anything that damages that blood supply destroys cartilage. **Small-vessel richness**: the nasal mucosa has a dense submucosal microvasculature, a natural target for small-vessel vasculitis. **Shared airway mucosa**: the same respiratory epithelium lines the nose, sinuses, middle ear, larynx, and bronchi, which is why systemic airway diseases appear in several sites at once. **Mucosal healing**: crusting and bleeding reflect epithelium that cannot regenerate over inflamed or ischemic tissue.

**T-rhinology-47.pathophysiology**

**GPA**: ANCA-associated necrotizing granulomatous vasculitis causes crusting, bleeding, septal perforation, and saddle nose from cartilage ischemia. **EGPA**: eosinophilic vasculitis with asthma and polyps. **Sarcoidosis**: noncaseating granulomas produce crusting and nodularity. **NK/T-cell lymphoma**: angiocentric destructive lesions of the midline face that mimic GPA; biopsy must be deep and repeated if needed. **Cocaine**: vasoconstriction and cutting agents (levamisole) cause midline destruction and false-positive ANCA.

### CC-rhinology-47.1 (concept check)

Stem: A 35-year-old has nasal crusting, a large septal perforation, and early saddle deformity. Biopsies are nondiagnostic, ANCA is positive, and he admits to regular cocaine use. Why must the ANCA result be interpreted cautiously?

- **Correct:** Levamisole-cut cocaine induces ANCA
- Distractor: Cocaine suppresses ANCA production — _why wrong:_ Cocaine adulterants induce ANCA rather than suppress it.
- Distractor: ANCA is never positive in GPA — _why wrong:_ ANCA is positive in most patients with active GPA.
- Distractor: ANCA reflects allergic disease — _why wrong:_ ANCA are antineutrophil antibodies, not markers of allergy.

Explanation: Cocaine causes midline destructive lesions through vasoconstriction and ischemia, and levamisole adulteration can produce positive ANCA, mimicking granulomatosis with polyangiitis.

Pearl: Midline destruction: ask about cocaine before diagnosing GPA.

## T-rhinology-48 — Unilateral Sinonasal Disease
_source: pathophys_v470/rhinology_b.py_

**T-rhinology-48.overview**

Unilateral sinonasal disease (one-sided obstruction, epistaxis, discharge, or opacification) must be considered neoplastic until proven otherwise. The differential includes inverted papilloma, malignancy, fungal ball, odontogenic sinusitis, AFRS, mucocele, CSF leak, and foreign body.

**T-rhinology-48.physiology**

**Symmetric inflammation**: inflammatory CRS is usually bilateral because the drivers (immune dysregulation, environment) affect both sides. **Localized causes**: unilateral findings imply a local process.

**T-rhinology-48.pathophysiology**

**Neoplasms**: tumors grow from one site, causing progressive one-sided obstruction, bleeding, and later neuro-ophthalmic findings. **Local infection**: dental sources and fungal balls are unilateral. **Imaging clues**: bone erosion suggests malignancy; focal hyperostosis suggests inverted papilloma attachment; central calcifications suggest fungal ball; expansion suggests mucocele or AFRS. **Why MRI is added**: it distinguishes tumor from retained secretions and shows orbital, dural, and perineural involvement.

### CC-rhinology-48.1 (concept check)

Stem: A 55-year-old has 3 months of right nasal obstruction and blood-tinged discharge. CT shows unilateral opacification of the right maxillary and ethmoid sinuses with erosion of the medial orbital wall. What is the most important next step?

- **Correct:** MRI and endoscopic biopsy
- Distractor: Antibiotics and a repeat CT in 6 weeks — _why wrong:_ Bone erosion with bloody discharge suggests malignancy; delay is inappropriate.
- Distractor: Allergy testing and nasal steroids — _why wrong:_ Unilateral disease with erosion is not explained by allergy.
- Distractor: Complete endoscopic sinus surgery — _why wrong:_ Operating before tissue diagnosis and staging risks inappropriate treatment of a malignancy.

Explanation: Unilateral sinonasal disease is neoplastic until proven otherwise. Bone erosion suggests malignancy; MRI separates tumor from retained secretions and defines orbital, dural, and perineural extent before biopsy.

Pearl: Unilateral disease plus bone erosion = malignancy until proven otherwise.


---

# Head & Neck Oncology

## T-head_neck-1 — Adverse Pathology and Adjuvant Therapy
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-1.overview**

After surgery for head and neck cancer, pathology determines adjuvant therapy: extranodal extension and positive margins call for chemoradiation; other risk factors call for radiation alone. This is one of the most testable decisions in head and neck oncology.

**T-head_neck-1.physiology**

**Lymph node capsule**: early metastases grow within the node; breaching the capsule (extranodal extension) places tumor cells in soft tissue outside any surgical plane. **Margins**: the distance from tumor to the cut edge reflects the chance microscopic tumor remains in the patient. **Perineural and lymphovascular spaces**: nerves and lymphatic channels are low-resistance routes along which tumor cells travel beyond visible disease. **Radiosensitization**: cisplatin forms DNA adducts that prevent repair of radiation damage, increasing tumor kill in the radiation field.

**T-head_neck-1.pathophysiology**

**High-risk features**: extranodal extension and positive margins predict recurrence; postoperative chemoradiation improves outcomes (RTOG 9501 and EORTC 22931). **Intermediate-risk features**: pT3-T4, N2 or greater, perineural invasion, lymphovascular invasion, and close margins indicate adjuvant radiation. **Timing**: adjuvant therapy should start within about 6 weeks of surgery to prevent repopulation. **HPV-positive disease**: some risk features carry less weight, which is under study.

### CC-head_neck-1.1 (concept check)

Stem: After resection and neck dissection for a pT2 oral tongue SCC, pathology shows a 2.5 cm node with extranodal extension; margins are clear. What adjuvant treatment is recommended?

- **Correct:** Concurrent cisplatin with radiation
- Distractor: Postoperative radiation alone — _why wrong:_ Radiation alone is appropriate for intermediate-risk features, not ENE.
- Distractor: Observation with close surveillance — _why wrong:_ ENE carries a high recurrence risk that warrants adjuvant therapy.
- Distractor: Adjuvant immunotherapy alone — _why wrong:_ Immunotherapy alone is not standard adjuvant treatment for ENE.

Explanation: Extranodal extension and positive margins are the high-risk features for which adding cisplatin to postoperative radiation improves outcomes (RTOG 9501, EORTC 22931). Treatment should start within about 6 weeks of surgery.

Pearl: ENE or a positive margin = add chemotherapy to adjuvant radiation.

## T-head_neck-2 — Basal Cell Carcinoma of the Head & Neck
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-2.overview**

Basal cell carcinoma is the most common cancer in humans, arising on sun-exposed facial skin. It rarely metastasizes but is locally destructive, and Mohs surgery offers the highest cure with tissue sparing.

**T-head_neck-2.physiology**

**Basal keratinocytes**: the proliferating layer at the base of the epidermis and hair follicle. **Hedgehog pathway**: a developmental growth signal; the PTCH1 receptor normally inhibits SMO, keeping the pathway off in adult skin. **Embryonic fusion planes**: the nasal ala, nasolabial fold, periorbital and periauricular regions sit where facial processes fused, leaving tissue planes of least resistance. **Tumor-stroma interaction**: epithelial cells depend on signals from surrounding dermal stroma for survival.

**T-head_neck-2.pathophysiology**

**Hedgehog activation**: loss-of-function PTCH1 or gain-of-function SMO mutations switch the pathway on; germline PTCH1 causes basal cell nevus (Gorlin) syndrome with jaw keratocysts and early multiple BCCs. **Stromal dependence**: BCC cells need their specific stroma, which is thought to explain the extremely low metastatic rate. **Fusion-plane spread**: tumors extend deeply and silently along embryonic planes, so central-face ("H-zone") tumors recur more often after standard excision. **Aggressive histology**: morpheaform, infiltrative, and micronodular subtypes grow in thin strands beyond visible margins, which is why Mohs margin control matters. **Targeted therapy**: SMO inhibitors (vismodegib, sonidegib) shrink locally advanced or metastatic tumors; resistance develops through downstream mutations.

### CC-head_neck-2.1 (concept check)

Stem: A 70-year-old has a slowly enlarging pearly nodule on the nasal ala that has been present for 2 years. Biopsy shows basal cell carcinoma. Why does this tumor almost never metastasize?

- **Correct:** It depends on its specific stroma
- Distractor: It carries no driver mutations — _why wrong:_ BCC carries Hedgehog pathway mutations (PTCH1 or SMO).
- Distractor: It is fully encapsulated — _why wrong:_ BCC is not encapsulated and spreads locally along tissue planes.
- Distractor: It is always found while small — _why wrong:_ Neglected BCCs can become large and destructive.

Explanation: BCC cells depend on signals from their own stroma, which is thought to explain the very low metastatic rate. They are locally destructive and spread along embryonic fusion planes, so central-face tumors benefit from Mohs surgery.

Pearl: BCC: locally destructive, rarely metastatic.

## T-head_neck-3 — Base of Tongue SCC
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-3.overview**

Base of tongue SCC arises behind the circumvallate papillae, often HPV-associated, and frequently presents with a neck mass or referred otalgia. Its bilateral lymphatics and functional importance in swallowing shape treatment.

**T-head_neck-3.physiology**

**Swallowing role**: the base of tongue drives the bolus into the pharynx by retracting against the posterior pharyngeal wall. **Lymphoid tissue**: lingual tonsils, deep and irregular. **Lymphatics**: rich, bilateral drainage. **Sensory innervation**: CN IX supplies sensation and taste, with referred pain to the ear through Jacobson nerve.

**T-head_neck-3.pathophysiology**

**Hidden growth**: tumors grow in deep tissue with few early symptoms. **Bilateral nodal spread**: requires bilateral neck treatment. **Dysphagia**: invasion of the tongue base and vallecula impairs bolus propulsion and airway protection. **Extrinsic muscle invasion**: deep muscle invasion indicates T4a disease. **Treatment balance**: radiation or TORS outcomes are similar for survival, so functional outcomes guide choice.

### CC-head_neck-3.1 (concept check)

Stem: A 57-year-old has 3 months of right ear pain. Otoscopy and tympanometry are normal. Flexible laryngoscopy shows a firm base-of-tongue mass. Which nerve explains the referred otalgia?

- **Correct:** Glossopharyngeal nerve (Jacobson branch)
- Distractor: Facial nerve via the chorda tympani — _why wrong:_ The chorda carries taste from the anterior tongue, not base-of-tongue sensation.
- Distractor: Auriculotemporal branch of the trigeminal — _why wrong:_ This refers pain from the oral cavity and TMJ, not the base of tongue.
- Distractor: Hypoglossal nerve — _why wrong:_ CN XII is purely motor and carries no sensation.

Explanation: CN IX supplies base-of-tongue sensation and, through its tympanic branch (Jacobson nerve), the middle ear, so base-of-tongue tumors refer pain to the ear. Otalgia with a normal ear exam warrants a full head and neck examination.

Pearl: Unexplained otalgia with a normal ear: examine the pharynx and larynx.

## T-head_neck-4 — Carotid Body Paraganglioma
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-4.overview**

Carotid body paraganglioma is a vascular neuroendocrine tumor at the carotid bifurcation that splays the internal and external carotids. It is often hereditary (SDH mutations), and management balances observation, surgery, and radiation.

**T-head_neck-4.physiology**

**Carotid body**: a small chemoreceptor organ in the adventitia of the carotid bifurcation, among the most highly perfused tissues in the body. **Glomus (type I) cells**: neural crest-derived chief cells sense low oxygen, high CO2, and acidosis and release neurotransmitters onto Hering nerve (CN IX) to increase ventilation. **Sustentacular (type II) cells**: support cells surrounding chief cells in nests (Zellballen). **Hypoxia response**: chronic hypoxia (high altitude, COPD) causes carotid body hyperplasia, linking oxygen sensing to tumor formation.

**T-head_neck-4.pathophysiology**

**Pseudohypoxic signaling**: SDH mutations accumulate succinate, stabilizing HIF and driving tumor growth. **Splaying**: tumors grow between the carotids (lyre sign) and wrap vessels. **Shamblin classification**: relationship to the carotid predicts vascular and cranial nerve injury risk. **Catecholamines**: rarely secreting; screening is done before surgery. **Cranial nerve risk**: vagus and hypoglossal injuries are the major surgical morbidity.

### CC-head_neck-4.1 (concept check)

Stem: A 45-year-old has a painless, pulsatile neck mass. Imaging shows a hypervascular tumor splaying the internal and external carotid arteries. Why is germline genetic testing recommended?

- **Correct:** SDH mutations are common and multifocal
- Distractor: Most of these tumors are malignant — _why wrong:_ Most carotid body tumors are benign; genetics guide screening.
- Distractor: Genetics predict radiation sensitivity — _why wrong:_ Genetic results guide surveillance and family screening, not radiation response.
- Distractor: Testing replaces the need for imaging — _why wrong:_ Whole-body imaging is still required to find other tumors.

Explanation: Succinate dehydrogenase (SDHx) mutations cause hereditary, often multifocal paragangliomas. Testing guides whole-body screening, catecholamine evaluation, and testing of relatives.

Pearl: Splayed carotids = carotid body tumor: test for SDHx.

## T-head_neck-5 — Complications of Neck Surgery
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-5.overview**

Neck surgery complications include hematoma, chyle leak, nerve injuries (spinal accessory, marginal mandibular, hypoglossal, vagus, phrenic), carotid injury, and wound infection. Recognizing them early prevents harm.

**T-head_neck-5.physiology**

**Carotid sheath**: carotid artery, internal jugular vein, and vagus nerve. **Thoracic duct**: carries chyle (lymph with chylomicrons) to the left venous angle; it can be bilateral or variable. **Nerves at risk**: spinal accessory (level II and V), marginal mandibular (under platysma near the mandible), hypoglossal (above the posterior digastric), phrenic (on anterior scalene). **Venous drainage**: bilateral internal jugular veins drain the brain and face.

**T-head_neck-5.pathophysiology**

**Hematoma**: venous and lymphatic obstruction causes laryngeal edema and airway compromise beyond simple compression. **Chyle leak**: thoracic duct injury produces milky drainage high in triglycerides, worsened by dietary fat. **Accessory nerve injury**: trapezius weakness causes shoulder droop and pain. **Bilateral IJV ligation**: facial edema and raised intracranial pressure. **Carotid blowout**: after radiation, infection, or fistula exposure.

### CC-head_neck-5.1 (concept check)

Stem: Two days after left modified radical neck dissection, drain output becomes milky and rises from 80 mL to 600 mL per day after the patient starts eating. What is the diagnosis?

- **Correct:** Chyle leak from thoracic duct injury
- Distractor: Seroma in the dissection bed — _why wrong:_ Seroma fluid is clear, not milky, and does not rise with meals.
- Distractor: Salivary fistula from the pharynx — _why wrong:_ Salivary leaks are not milky and do not depend on dietary fat.
- Distractor: Delayed hematoma — _why wrong:_ A hematoma produces blood, not milky fluid.

Explanation: The thoracic duct enters the left venous angle in level IV. Chyle carries chylomicrons, so output rises with dietary fat. Medium-chain triglyceride diet, octreotide, pressure, and re-exploration or embolization for high output are used.

Pearl: Milky drain after left neck dissection = chyle leak.

## T-head_neck-6 — Cutaneous Melanoma of the Head & Neck
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-6.overview**

Cutaneous melanoma of the head and neck has less predictable lymphatic drainage than other sites and is staged by Breslow thickness, ulceration, and nodal status. Sentinel node biopsy and immunotherapy have transformed management.

**T-head_neck-6.physiology**

**Melanocytes**: neural crest-derived cells in the basal epidermis that transfer melanin to keratinocytes to shield DNA from UV. **Head and neck lymphatics**: dense and bilateral, draining to parotid, preauricular, occipital, and cervical nodes in patterns that often defy clinical prediction. **Immune checkpoints**: CTLA-4 (during T-cell priming) and PD-1 (in tissues) normally restrain T cells to prevent autoimmunity.

**T-head_neck-6.pathophysiology**

**MAPK pathway mutations**: BRAF V600E (about half), NRAS, or NF1 drive proliferation; UV exposure adds a very high mutational burden. **Growth phases**: radial growth along the epidermis (low metastatic risk) gives way to vertical growth into the dermis (metastatic potential). **Breslow thickness and ulceration**: the strongest predictors of nodal and distant spread, which is why they define T-stage. **Sentinel node logic**: drainage is unpredictable, so lymphoscintigraphy identifies the true first-echelon node; it is offered at about 0.8 mm or with ulceration. **Immunotherapy**: the neoantigen load makes melanoma highly responsive to PD-1 and CTLA-4 blockade, now used adjuvantly and in advanced disease; BRAF/MEK inhibitors target BRAF-mutant tumors. **Desmoplastic melanoma**: neurotropic and locally aggressive, often amelanotic on sun-damaged head and neck skin.

### CC-head_neck-6.1 (concept check)

Stem: A 1.2 mm thick, nonulcerated melanoma of the posterior scalp is excised. Why is lymphoscintigraphy with sentinel node biopsy especially useful in this location?

- **Correct:** Head and neck drainage is unpredictable
- Distractor: Scalp melanoma drains only to level I — _why wrong:_ Scalp drainage can go to parotid, occipital, posterior triangle, or contralateral nodes.
- Distractor: Melanoma does not spread to the parotid — _why wrong:_ Periauricular and scalp melanomas commonly drain to parotid nodes.
- Distractor: Sentinel node biopsy cures most patients — _why wrong:_ Sentinel biopsy is a staging tool, not curative treatment.

Explanation: Head and neck lymphatics are dense and variable, so clinical prediction of the first-echelon node is unreliable. Lymphoscintigraphy finds the true sentinel node, which guides staging and adjuvant therapy.

Pearl: Head and neck melanoma drainage is unpredictable: map it.

## T-head_neck-7 — Cutaneous Squamous Cell Carcinoma of the Head & Neck
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-7.overview**

Cutaneous SCC is the second most common skin cancer, driven by UV exposure and dramatically more aggressive in transplant and immunosuppressed patients. High-risk features (size, depth, perineural invasion, poor differentiation, location) predict nodal spread to the parotid and neck.

**T-head_neck-7.physiology**

**Epidermal renewal**: basal keratinocytes divide and mature upward into keratinized squames over about a month. **UV defenses**: melanin absorbs UV, and nucleotide excision repair corrects UV-induced pyrimidine dimers before they become fixed mutations. **Immune surveillance**: cytotoxic T cells and NK cells eliminate keratinocytes carrying mutations; this is why immune competence matters so much for skin cancer. **Lymphatic drainage**: scalp, forehead, temple, cheek, and ear skin drain to intraparotid and periparotid nodes, then to levels II-V and occipital nodes. **Cutaneous nerves**: sensory branches of V1-V3 and the facial nerve run in the subcutaneous plane and connect directly to the skull base.

**T-head_neck-7.pathophysiology**

**UV mutagenesis**: UVB causes signature C-to-T transitions in TP53, NOTCH1, and other genes, producing actinic keratosis, SCC in situ (Bowen disease), then invasive SCC. **Immunosuppression**: solid-organ transplant recipients have a 65- to 250-fold higher risk because surveillance fails; reducing immunosuppression (or switching to an mTOR inhibitor) is part of treatment. **High mutational burden**: UV-driven tumors carry many neoantigens, which explains why PD-1 blockade (cemiplimab) works well in advanced disease. **Perineural invasion**: tumor tracks along V2, V3, or VII toward the skull base, causing numbness, formication, or facial weakness and late recurrence; MRI neurography maps it. **Parotid metastasis**: periauricular and scalp primaries spread first to parotid nodes, which then require parotidectomy plus neck dissection. **Adjuvant radiation logic**: microscopic disease along nerves and in nodal beds is not removed by surgery, so radiation is added for PNI of named nerves, close margins, and nodal disease.

### CC-head_neck-7.1 (concept check)

Stem: A kidney transplant recipient on tacrolimus has developed five aggressive cutaneous SCCs of the scalp in 2 years, one with perineural invasion. Why is her risk so high?

- **Correct:** Immunosuppression impairs tumor surveillance
- Distractor: Tacrolimus is directly mutagenic only — _why wrong:_ Some agents are carcinogenic, but loss of T-cell surveillance is the dominant mechanism.
- Distractor: Transplant patients get more sun exposure — _why wrong:_ Sun exposure is not greater; immune function is reduced.
- Distractor: Renal failure itself causes skin cancer — _why wrong:_ The risk comes from immunosuppression, not kidney disease.

Explanation: T cells normally eliminate UV-mutated keratinocytes. Immunosuppression lets tumors arise and behave aggressively. Reducing immunosuppression or switching to an mTOR inhibitor, plus aggressive surveillance, lowers risk.

Pearl: Transplant + cutaneous SCC = aggressive disease: involve the transplant team.

## T-head_neck-8 — Floor of Mouth SCC
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-8.overview**

Floor of mouth SCC arises between the tongue and mandible, near the submandibular ducts and periosteum. Its proximity to bone determines whether marginal or segmental mandibulectomy is needed, and early bilateral nodal spread is common.

**T-head_neck-8.physiology**

**Anatomy**: the floor of mouth contains the sublingual glands, Wharton ducts, lingual nerve, and mylohyoid muscle diaphragm. **Mandible relationship**: the alveolar periosteum is close; in edentulous patients, alveolar resorption brings the inferior alveolar canal closer to the surface. **Lymphatics**: drain to level I and II, often bilaterally because of midline position.

**T-head_neck-8.pathophysiology**

**Bone invasion routes**: tumor enters the mandible at the alveolar crest (dentate) or through the occlusal surface of resorbed bone (edentulous). **Marginal vs segmental**: periosteal involvement without medullary invasion allows marginal mandibulectomy; frank invasion requires segmental resection. **Duct obstruction**: involvement of Wharton duct causes submandibular swelling that can mimic nodal disease. **Bilateral neck risk**: midline tumors require evaluation of both necks.

### CC-head_neck-8.1 (concept check)

Stem: A 66-year-old edentulous man has a floor-of-mouth SCC abutting the mandible. CT shows tumor reaching the alveolar ridge without medullary invasion. Why is the edentulous mandible at higher risk of direct tumor invasion?

- **Correct:** Resorbed alveolar bone exposes the ridge
- Distractor: Edentulous bone is more vascular — _why wrong:_ Vascularity is not the reason; loss of alveolar height is.
- Distractor: Dental roots normally block tumor spread — _why wrong:_ Tumor enters through the occlusal surface of resorbed bone, not via missing roots.
- Distractor: The inferior alveolar nerve is absent — _why wrong:_ The nerve remains and can be a route of perineural spread.

Explanation: After tooth loss the alveolus resorbs, bringing tumor into contact with the occlusal cortex and the inferior alveolar canal. Periosteal involvement allows marginal mandibulectomy; medullary invasion requires segmental resection.

Pearl: Marginal mandibulectomy for periosteum; segmental for medullary invasion.

## T-head_neck-9 — Free-Flap Monitoring / Compromise / Salvage
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-9.overview**

Free-flap monitoring detects vascular compromise early, when take-back can salvage the flap. Venous thrombosis is more common than arterial, and most failures occur within the first 72 hours.

**T-head_neck-9.physiology**

**Microvascular anastomosis**: flap artery and vein are sutured or coupled to recipient vessels. **Flap perfusion**: depends on arterial inflow, venous outflow, and systemic pressure. **Endothelial healing**: the anastomosis is most thrombogenic in the first days until endothelium covers it. **Monitoring tools**: color, capillary refill, temperature, pinprick bleeding, and implantable or external Doppler.

**T-head_neck-9.pathophysiology**

**Venous congestion**: outflow obstruction makes the flap swollen, purple, with brisk dark bleeding; it progresses to arterial thrombosis. **Arterial insufficiency**: pale, cool flap without bleeding. **Causes**: technical anastomosis errors, kinking, compression by hematoma or tight dressings, and hypotension. **Time dependence**: salvage succeeds when compromise is detected within hours. **No-reflow phenomenon**: prolonged ischemia causes endothelial swelling and leukocyte plugging so flow fails despite revision. **Salvage options**: revision, thrombectomy, thrombolytics, and leeches for venous congestion.

### CC-head_neck-9.1 (concept check)

Stem: Twelve hours after a radial forearm free flap to the tongue, the skin paddle is purple and swollen, and pinprick produces rapid dark blood. What is the problem?

- **Correct:** Venous outflow obstruction
- Distractor: Arterial inflow thrombosis — _why wrong:_ Arterial insufficiency makes the flap pale and cool with little or no bleeding on pinprick.
- Distractor: Normal postoperative flap edema — _why wrong:_ Purple discoloration with rapid dark bleeding is not normal.
- Distractor: Early flap infection — _why wrong:_ Infection does not appear this early or in this way.

Explanation: Venous congestion causes a swollen, purple flap with brisk dark bleeding; arterial insufficiency causes a pale, cool flap without bleeding. Early return to the operating room salvages most compromised flaps.

Pearl: Purple and swollen = venous; pale and cool = arterial.

## T-head_neck-10 — Glottic Cancer
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-10.overview**

Glottic cancer involves the true vocal folds and presents early with hoarseness. It rarely spreads to nodes, and early disease is cured at very high rates by transoral laser surgery or radiation.

**T-head_neck-10.physiology**

**Vocal fold layers**: epithelium, superficial lamina propria (Reinke space), intermediate and deep lamina propria (vocal ligament), and vocalis muscle. **Mucosal wave**: vibration of the cover over the body produces voice. **Lymphatic sparseness**: the true folds have few lymphatics. **Anterior commissure**: Broyles ligament inserts directly into thyroid cartilage.

**T-head_neck-10.pathophysiology**

**Early hoarseness**: even small lesions disrupt the mucosal wave, so tumors are found early. **Low nodal risk**: sparse lymphatics mean early glottic cancer rarely needs neck treatment. **Anterior commissure**: Broyles ligament provides a route to cartilage invasion, complicating treatment. **Vocal fold fixation**: indicates paraglottic or thyroarytenoid invasion (T3). **Voice outcomes**: depend on depth of resection or radiation fibrosis.

### CC-head_neck-10.1 (concept check)

Stem: A 62-year-old has a T1a glottic SCC limited to the middle third of one mobile vocal fold. Why is elective treatment of the neck not recommended?

- **Correct:** Vocal fold submucosa has few lymphatics
- Distractor: Glottic tumors are usually carcinoma in situ — _why wrong:_ This is invasive SCC; the reason is low nodal risk, not lack of invasion.
- Distractor: Radiation fields always include the neck — _why wrong:_ Early glottic radiation fields typically exclude the neck.
- Distractor: Occult neck nodes regress after treatment — _why wrong:_ The neck is observed because occult risk is low, not because nodes regress.

Explanation: The vocal fold has sparse lymphatics, so early glottic cancer rarely metastasizes. Hoarseness also brings patients in early, and transoral laser surgery or radiation cures most T1 lesions.

Pearl: Hoarseness finds glottic cancer early; sparse lymphatics keep it local.

## T-head_neck-11 — HPV-Associated Oropharyngeal SCC
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-11.overview**

HPV-associated oropharyngeal squamous cell carcinoma arises in the tonsils and base of tongue, driven by high-risk HPV (mostly HPV-16). It is now the most common HPV-related cancer in the US, often presents as a cystic neck mass in a younger nonsmoker, and has a much better prognosis than HPV-negative disease, which is why it has its own staging (AJCC 8th and Version 9).

**T-head_neck-11.physiology**

**Lymphoid oropharynx**: the palatine and lingual tonsils make up Waldeyer ring, lymphoid tissue that samples antigens from food and air. **Reticulated crypt epithelium**: tonsillar crypts are lined by a thin, discontinuous epithelium whose basal cells are directly exposed, unlike the intact squamous lining elsewhere. **Tumor suppressors**: p53 halts the cell cycle and triggers apoptosis after DNA damage; Rb holds E2F transcription factors in check, blocking entry into S phase. **Lymphatic drainage**: the tonsils and base of tongue drain mainly to level II, then III, and to retropharyngeal nodes; the base of tongue drains bilaterally.

**T-head_neck-11.pathophysiology**

**Viral entry**: HPV reaches the exposed basal cells of reticulated crypt epithelium, largely through oral sexual exposure, where it can persist. **Oncoproteins**: viral E6 degrades p53 and E7 inactivates Rb, releasing E2F and driving uncontrolled proliferation without the mutational burden of tobacco cancers. **p16 surrogate**: Rb loss produces a feedback overexpression of p16INK4a, so strong diffuse p16 immunostaining is a surrogate marker for HPV-driven tumors. **Cystic nodal metastases**: small primaries hidden in crypts metastasize early, producing cystic level II nodes that can be mistaken for branchial cleft cysts. **Better prognosis biology**: tumors have fewer mutations, intact apoptosis pathways that respond to radiation, and an immune-infiltrated microenvironment. **Why separate staging**: traditional nodal staging overestimated risk for HPV-positive disease, so AJCC 8th (and Version 9 pathologic staging) groups nodes differently; smoking history still worsens outcomes. **De-escalation questions**: excellent survival has driven trials of reduced-intensity therapy, though cisplatin remains standard over cetuximab.

### CC-head_neck-11.1 (concept check)

Stem: A 46-year-old nonsmoker has a painless cystic level II neck mass. FNA shows squamous cell carcinoma with strong, diffuse p16 staining. Why is p16 overexpression a reliable surrogate for an HPV-driven tumor?

- **Correct:** E7 inactivates Rb; p16 rises
- Distractor: Viral E6 directly switches on p16 — _why wrong:_ E6 degrades p53; p16 rises because E7 inactivates Rb and removes feedback inhibition.
- Distractor: Tobacco carcinogens upregulate p16 — _why wrong:_ Tobacco-driven tumors usually silence p16 (CDKN2A) rather than overexpress it.
- Distractor: p16 is encoded by the HPV genome — _why wrong:_ p16INK4a is a host cell-cycle inhibitor, not a viral protein.

Explanation: HPV E7 binds and inactivates Rb, releasing E2F and driving proliferation. Loss of Rb removes negative feedback on p16INK4a, which accumulates. Strong, diffuse p16 staining therefore marks HPV-driven oropharyngeal cancer.

Pearl: Cystic level II node in an adult = HPV-positive oropharyngeal SCC until proven otherwise.

## T-head_neck-12 — Head & Neck Cancer Surveillance / Second Primaries
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-12.overview**

Surveillance after head and neck cancer looks for recurrence (most within 2-3 years) and second primaries, especially in smokers. It includes exam, imaging, thyroid function, and survivorship care.

**T-head_neck-12.physiology**

**Field cancerization**: carcinogen exposure damages the entire aerodigestive mucosa, creating patches of genetically altered cells. **Clonal expansion**: mutated clones spread across the mucosal field, so cancers can arise at distant sites. **Post-treatment tissue**: radiation and surgery create scar and inflammation that confuse imaging.

**T-head_neck-12.pathophysiology**

**Recurrence timing**: most recurrences occur within 2 years, prompting frequent early visits. **Second primary risk**: about 3-5 percent per year, mainly lung, esophagus, and head and neck mucosa, highest in persistent smokers. **Smoking cessation**: reduces second primary risk and improves treatment outcomes. **Post-treatment PET-CT**: a scan around 12 weeks after chemoradiation guides neck management (PET-NECK). **Hypothyroidism**: common after radiation and laryngectomy, requiring TSH monitoring.

### CC-head_neck-12.1 (concept check)

Stem: A 64-year-old treated for laryngeal SCC 3 years ago continues to smoke a pack per day. Which organ is the most likely site of a second primary cancer?

- **Correct:** Lung
- Distractor: Thyroid gland — _why wrong:_ Thyroid cancer is not tobacco-driven and is not the most common second primary.
- Distractor: Skin of the face — _why wrong:_ Cutaneous cancers are UV-driven, not part of the tobacco field.
- Distractor: Kidney — _why wrong:_ Renal cancer is not the common second primary after laryngeal cancer.

Explanation: Tobacco exposure creates field cancerization throughout the aerodigestive tract, so second primaries arise at about 3-5 percent per year, most often in the lung. Smoking cessation lowers this risk.

Pearl: Smoker with head and neck cancer: watch the lungs.

## T-head_neck-13 — Head & Neck Radiation Toxicity / Survivorship
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-13.overview**

Radiation toxicity is acute (mucositis, dermatitis) or late (xerostomia, fibrosis, dysphagia, osteoradionecrosis, hypothyroidism, carotid disease). Survivorship care manages these effects and surveils for recurrence.

**T-head_neck-13.physiology**

**Radiation biology**: radiation causes DNA damage that kills dividing cells. **Early-responding tissues**: rapidly dividing mucosa and skin. **Late-responding tissues**: slowly dividing tissues such as connective tissue and vessels. **Salivary glands**: serous acinar cells are especially radiosensitive.

**T-head_neck-13.pathophysiology**

**Mucositis**: epithelial cell death outpaces renewal, causing ulceration and pain. **Xerostomia**: acinar cell loss and fibrosis reduce saliva, increasing dental caries and dysphagia. **Fibrosis**: TGF-beta driven fibroblast activation causes trismus, neck stiffness, and dysphagia. **Endarteritis**: small-vessel damage reduces tissue perfusion and healing (osteoradionecrosis). **Hypothyroidism**: thyroid gland damage. **Prevention**: IMRT spares salivary glands, swallowing exercises preserve function, and fluoride protects teeth.

### CC-head_neck-13.1 (concept check)

Stem: Two years after chemoradiation for oropharyngeal cancer, a patient develops rapidly progressive dental caries along the gum line despite brushing. What is the main mechanism?

- **Correct:** Loss of saliva from acinar cell injury
- Distractor: Radiation directly dissolving enamel — _why wrong:_ Radiation's main effect is on saliva; enamel changes are secondary.
- Distractor: Radiation-induced vitamin D deficiency — _why wrong:_ Vitamin D status does not explain radiation caries.
- Distractor: Radiation causing gingival recession only — _why wrong:_ Recession alone does not explain the rapid caries.

Explanation: Serous acinar cells are highly radiosensitive. Xerostomia removes saliva's buffering, antimicrobial, and remineralizing effects, causing radiation caries. Daily fluoride trays, dental care, and parotid-sparing IMRT reduce risk.

Pearl: Radiation xerostomia means lifelong fluoride and dental surveillance.

## T-head_neck-14 — Hypopharyngeal Cancer
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-14.overview**

Hypopharyngeal cancer arises in the pyriform sinus, postcricoid region, or posterior pharyngeal wall. It presents late, has a high rate of nodal and distant spread, and has the poorest prognosis of laryngopharyngeal cancers.

**T-head_neck-14.physiology**

**Subsites**: the pyriform sinuses (lateral gutters beside the larynx), the postcricoid area (behind the cricoid), and the posterior pharyngeal wall. **Swallowing pathway**: food is channeled around the larynx through the pyriform sinuses into the upper esophageal sphincter. **Distensibility**: the hypopharynx is a collapsible muscular tube with loose submucosa, so tumors can grow large before obstructing. **Lymphatics**: very rich, draining to levels II-IV, retropharyngeal, and paratracheal nodes.

**T-head_neck-14.pathophysiology**

**Silent spread**: tumors grow submucosally in a distensible space, with symptoms appearing late (dysphagia, otalgia, neck mass). **Submucosal extension**: tumors spread well beyond visible margins, complicating resection. **Nodal and distant metastasis**: common at presentation. **Postcricoid cancer**: associated with iron deficiency (Plummer-Vinson syndrome). **Organ preservation**: induction chemotherapy and chemoradiation can preserve the larynx in selected patients.

### CC-head_neck-14.1 (concept check)

Stem: A 63-year-old smoker has a pyriform sinus SCC and a 3 cm ipsilateral neck node at presentation. Why does hypopharyngeal cancer have the poorest prognosis among laryngopharyngeal sites?

- **Correct:** Late symptoms, early spread
- Distractor: It is usually HPV-driven — _why wrong:_ Hypopharyngeal cancer is rarely HPV-driven, which is part of why its prognosis is worse.
- Distractor: It does not respond to radiation — _why wrong:_ It responds to chemoradiation; the problem is late presentation and spread.
- Distractor: It occurs mainly in young adults — _why wrong:_ It occurs mainly in older smokers and drinkers.

Explanation: The distensible hypopharynx lets tumors grow silently, while rich lymphatics and submucosal spread produce nodal and distant metastases by presentation.

Pearl: Hypopharyngeal cancer presents late and spreads early.

## T-head_neck-15 — Laryngeal Preservation Decision
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-15.overview**

Laryngeal preservation uses chemoradiation or induction chemotherapy to treat advanced laryngeal cancer without total laryngectomy, when a functional larynx is expected. The choice depends on T-stage, cartilage invasion, pretreatment function, and patient priorities.

**T-head_neck-15.physiology**

**A functional larynx does three jobs**: it protects the airway during swallowing, allows breathing through the mouth and nose, and produces voice; preservation only makes sense if all three survive treatment. **Radiation biology**: radiation kills dividing tumor cells but also injures mucosa, muscle, nerve, and microvasculature, with late fibrosis and edema emerging over months to years. **Cartilage framework**: the thyroid and cricoid cartilages are relatively radioresistant when intact but are poorly vascularized, so tumor-invaded cartilage responds poorly and is prone to chondronecrosis. **Swallow mechanics**: laryngeal elevation, pharyngeal constriction, and upper esophageal sphincter opening are all vulnerable to radiation-induced fibrosis.

**T-head_neck-15.pathophysiology**

**Evidence base**: the VA larynx trial and RTOG 91-11 established that chemoradiation preserves the larynx in many patients without compromising survival. **Cartilage invasion**: T4a disease with cartilage destruction has poor organ preservation outcomes, favoring laryngectomy. **Dysfunctional larynx**: severe pretreatment aspiration or airway compromise means a preserved larynx may be nonfunctional. **Salvage**: failure requires salvage laryngectomy in irradiated tissue, with higher complication rates.

### CC-head_neck-15.1 (concept check)

Stem: A 60-year-old with glottic SCC and a fixed vocal fold is choosing between total laryngectomy and chemoradiation. Which additional finding most strongly favors primary laryngectomy?

- **Correct:** Thyroid cartilage destruction
- Distractor: Fixation of the vocal fold alone — _why wrong:_ T3 disease with fixation is a standard candidate for organ preservation.
- Distractor: A single ipsilateral neck node — _why wrong:_ Nodal disease does not by itself preclude organ preservation.
- Distractor: A strong wish to preserve voice — _why wrong:_ Patient preference supports a preservation approach.

Explanation: Cartilage destruction (T4a) predicts poor organ preservation and a high risk of a nonfunctional, aspirating larynx after chemoradiation. For many T3 tumors, chemoradiation preserves the larynx without compromising survival (RTOG 91-11).

Pearl: T4a cartilage destruction favors primary laryngectomy.

## T-head_neck-16 — Laryngeal SCC
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-16.overview**

Laryngeal squamous cell carcinoma is strongly linked to tobacco and alcohol and is divided by subsite: supraglottic, glottic, and subglottic. Subsite determines symptoms, nodal risk, and whether larynx-preserving therapy is possible.

**T-head_neck-16.physiology**

**Three functions**: the larynx protects the airway during swallowing, regulates airflow, and produces voice. **Subsites**: supraglottis (epiglottis, aryepiglottic folds, arytenoids, false folds, ventricle), glottis (true folds and commissures), and subglottis (below the glottis to the cricoid). **Embryology and lymphatics**: the supraglottis (from the buccopharyngeal anlage) has rich bilateral lymphatics, the glottis has almost none, and the subglottis drains to paratracheal and prelaryngeal (Delphian) nodes. **Barriers and spaces**: the conus elasticus and quadrangular membrane, the paraglottic and pre-epiglottic spaces, and thyroid cartilage shape tumor spread.

**T-head_neck-16.pathophysiology**

**Field cancerization**: tobacco carcinogens and alcohol cause widespread mucosal genetic damage (TP53, CDKN2A, and others), so second primaries are common. **Progression**: hyperplasia, dysplasia, carcinoma in situ, and invasive carcinoma. **Glottic tumors**: cause early hoarseness and rarely spread to nodes, so they are found early and cured at high rates. **Supraglottic tumors**: grow silently until large, causing dysphagia, referred otalgia (through CN X), and early bilateral nodal spread. **Fixed vocal fold**: indicates invasion of the thyroarytenoid muscle, paraglottic space, or cricoarytenoid joint (T3). **Cartilage invasion**: through the outer cortex of thyroid cartilage defines T4a, which favors total laryngectomy over organ preservation.

### CC-head_neck-16.1 (concept check)

Stem: A 64-year-old smoker has 4 months of hoarseness. Laryngoscopy shows an exophytic lesion of the left true vocal fold extending into the ventricle, and the left fold is fixed. CT shows no cartilage destruction. Which finding makes this T3 disease?

- **Correct:** Fixation of the vocal fold
- Distractor: Extension into the laryngeal ventricle — _why wrong:_ Supraglottic or subglottic extension with normal mobility is T2, not T3.
- Distractor: A tumor diameter greater than 2 cm — _why wrong:_ Laryngeal T-stage is defined by subsites, mobility, and invasion, not diameter.
- Distractor: A heavy smoking history — _why wrong:_ Risk factors do not change T-stage.

Explanation: Fixation indicates invasion of the thyroarytenoid muscle, paraglottic space, or cricoarytenoid joint, which defines T3 glottic cancer. Invasion through the outer cortex of the thyroid cartilage would make it T4a.

Pearl: In glottic cancer, mobility drives staging: impaired is T2, fixed is T3.

## T-head_neck-17 — Lip Cancer
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-17.overview**

Lip cancer is usually SCC of the lower lip from UV exposure, with BCC more common on the upper lip skin. It has a favorable prognosis, and reconstruction aims to preserve oral competence.

**T-head_neck-17.physiology**

**Vermilion**: modified mucosa with thin epithelium, little melanin, and no sweat glands, so it has little UV protection. **Orbicularis oris**: circular sphincter muscle essential for oral competence and speech. **Sensation**: the mental nerve (V3) supplies the lower lip. **Lymphatics**: lower lip drains to submental and submandibular nodes; central lesions drain bilaterally.

**T-head_neck-17.pathophysiology**

**UV exposure**: the lower lip receives more direct sun, explaining SCC predominance there. **Actinic cheilitis**: precursor lesion with dysplasia. **Nodal spread**: uncommon but increased in larger or recurrent tumors. **Perineural spread**: along the mental nerve into the mandible. **Reconstruction**: up to about one third of the lip can close primarily; larger defects need flaps (Abbe, Estlander, Karapandzic) that preserve sphincter function.

## T-head_neck-18 — Merkel Cell Carcinoma
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-18.overview**

Merkel cell carcinoma is a rare, aggressive neuroendocrine skin cancer of the head and neck in older, sun-exposed, or immunosuppressed patients. It spreads early to nodes and responds well to radiation and immunotherapy.

**T-head_neck-18.physiology**

**Merkel cells**: slowly adapting touch-receptor cells in the basal epidermis that synapse with sensory nerve endings. **Neuroendocrine features**: they contain dense-core granules and express neuroendocrine markers. **Viral control**: cellular immunity normally keeps common skin viruses such as Merkel cell polyomavirus in a harmless state. **Immune surveillance**: T cells also eliminate UV-mutated cells.

**T-head_neck-18.pathophysiology**

**Two pathways**: about 80 percent are driven by clonally integrated Merkel cell polyomavirus whose truncated large T antigen inactivates Rb; the rest are UV-driven with very high mutational burden. **Rapid growth**: a painless, red-violet, fast-growing nodule (AEIOU: asymptomatic, expanding rapidly, immunosuppressed, older, UV-exposed). **Early nodal spread**: microscopic nodal disease is common even with small primaries, so sentinel node biopsy is standard. **Immunosuppression**: raises risk and worsens prognosis, consistent with immune control of the virus. **Treatment logic**: tumors are highly radiosensitive and respond well to PD-1/PD-L1 inhibitors because of viral antigens or neoantigens; CK20 perinuclear dot staining confirms the diagnosis.

### CC-head_neck-18.1 (concept check)

Stem: A 78-year-old has a rapidly enlarging, painless violet nodule on the cheek. Biopsy shows small round blue cells with perinuclear dot-like CK20 staining. Which virus drives most of these tumors?

- **Correct:** Merkel cell polyomavirus
- Distractor: Human papillomavirus type 16 — _why wrong:_ HPV-16 drives oropharyngeal and anogenital cancers, not Merkel cell carcinoma.
- Distractor: Epstein-Barr virus — _why wrong:_ EBV is associated with nasopharyngeal carcinoma and some lymphomas.
- Distractor: Human herpesvirus 8 — _why wrong:_ HHV-8 causes Kaposi sarcoma.

Explanation: Most Merkel cell carcinomas carry clonally integrated polyomavirus whose truncated large T antigen inactivates Rb; the rest are UV-driven. Early nodal spread is common, so sentinel node biopsy is standard, and tumors respond to radiation and PD-1/PD-L1 blockade.

Pearl: Fast-growing violet nodule in an older patient: think Merkel cell carcinoma.

## T-head_neck-19 — Nasopharyngeal Carcinoma
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-19.overview**

Nasopharyngeal carcinoma arises in the fossa of Rosenmüller, is strongly associated with EBV, and is endemic in Southern China and Southeast Asia. It presents with neck nodes, unilateral effusion, or cranial neuropathies, and is treated with chemoradiation.

**T-head_neck-19.physiology**

**Fossa of Rosenmüller**: lateral recess behind the torus tubarius, the most common origin. **Eustachian tube**: opens on the lateral nasopharyngeal wall. **Skull-base neighbors**: foramen lacerum, foramen ovale, and cavernous sinus. **Lymphatics**: retropharyngeal (node of Rouvière) and level II and V nodes, often bilateral.

**T-head_neck-19.pathophysiology**

**EBV**: viral latent proteins drive proliferation, especially in nonkeratinizing types; plasma EBV DNA tracks tumor burden and response. **Dietary and genetic factors**: salted fish nitrosamines and HLA types contribute in endemic regions. **ET obstruction**: tumor blocks the tube, causing unilateral effusion in an adult. **Cranial nerve involvement**: spread through foramina causes CN V and VI palsies. **Radiosensitivity**: high radiosensitivity makes radiation (with chemotherapy) the primary treatment; immunotherapy now has a role in recurrent or metastatic disease.

### CC-head_neck-19.1 (concept check)

Stem: A 40-year-old man of Southern Chinese descent has a new unilateral middle-ear effusion and a level V neck node. Biopsy shows nonkeratinizing carcinoma of the fossa of Rosenmüller. Which blood test best tracks his tumor burden?

- **Correct:** Plasma EBV DNA
- Distractor: Serum calcitonin — _why wrong:_ Calcitonin is the tumor marker for medullary thyroid cancer.
- Distractor: Serum thyroglobulin — _why wrong:_ Thyroglobulin monitors differentiated thyroid cancer.
- Distractor: Serum CEA — _why wrong:_ CEA is used in medullary thyroid and GI cancers, not as the standard NPC marker.

Explanation: Nonkeratinizing NPC is EBV-associated, and circulating EBV DNA correlates with tumor burden, treatment response, and relapse. Tumor at the fossa of Rosenmüller blocks the Eustachian tube, causing unilateral effusion.

Pearl: New unilateral adult effusion with a neck node = scope the nasopharynx.

## T-head_neck-20 — Neck Dissection
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-20.overview**

Neck dissection removes cervical lymph nodes for staging and treatment of head and neck cancer, from selective dissections of specific levels to radical dissection. Its classification is based on which levels and non-lymphatic structures are removed.

**T-head_neck-20.physiology**

**Nodal levels**: I (submental and submandibular), II-IV (upper, middle, lower jugular), V (posterior triangle), VI (central), and VII (superior mediastinal). **Key structures**: spinal accessory nerve (crosses level II and V), internal jugular vein, sternocleidomastoid, marginal mandibular nerve, hypoglossal nerve, vagus, phrenic nerve, and thoracic duct. **Lymph flow**: lymph moves in a stepwise, predictable fashion along the jugular chain from upper to lower levels.

**T-head_neck-20.pathophysiology**

**Stepwise spread**: tumors seed first-echelon nodes before more distant levels, which justifies selective dissection in the clinically N0 neck. **Occult metastasis risk**: when the risk of hidden nodal disease exceeds about 15-20 percent, elective treatment is recommended. **Extranodal extension**: tumor breaking through the capsule signals aggressive biology and is an indication for adjuvant chemoradiation. **Morbidity follows structures**: spinal accessory nerve injury causes shoulder dysfunction; thoracic duct injury causes chyle leak; bilateral jugular ligation causes facial edema and raised intracranial pressure.

### CC-head_neck-20.1 (concept check)

Stem: A 60-year-old with a T2 supraglottic cancer and a clinically N0 neck undergoes bilateral selective neck dissection of levels II-IV. Why is level V usually omitted?

- **Correct:** Laryngeal primaries rarely involve it alone
- Distractor: Level V dissection endangers the phrenic nerve — _why wrong:_ The phrenic nerve lies on the anterior scalene; level V is spared mainly to protect the accessory nerve.
- Distractor: Level V drains only the scalp — _why wrong:_ Level V drains the posterior scalp and nasopharynx, but the reason to omit it here is low risk.
- Distractor: Level V contains no lymph nodes — _why wrong:_ Level V contains nodes along the spinal accessory nerve.

Explanation: Lymph from laryngeal primaries flows predictably through levels II-IV. Isolated level V involvement is rare, so omitting it spares the spinal accessory nerve and shoulder function without compromising control.

Pearl: Selective neck dissection follows the primary's drainage map.

## T-head_neck-21 — Neck Lymphoma
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-21.overview**

Lymphoma is a common cause of neck masses, especially in younger patients (Hodgkin) and older patients (non-Hodgkin). Diagnosis requires tissue architecture, usually by core or excisional biopsy rather than FNA alone.

**T-head_neck-21.physiology**

**Lymph node architecture**: an outer cortex with B-cell follicles and germinal centers, a paracortex rich in T cells, and a medulla with plasma cells, all fed by afferent lymphatics. **Germinal centers**: B cells undergo somatic hypermutation and class switching, a process that occasionally produces oncogenic errors (translocations). **Waldeyer ring**: tonsils, adenoids, and lingual tonsil are extranodal lymphoid tissue in direct contact with antigens. **Reactive vs neoplastic**: reactive nodes contain mixed polyclonal cells, whereas lymphoma is a clonal population that effaces normal architecture.

**T-head_neck-21.pathophysiology**

**Clonal proliferation**: B or T lymphocytes proliferate clonally from genetic alterations. **Hodgkin lymphoma**: Reed-Sternberg cells in an inflammatory background, often contiguous spread. **Non-Hodgkin lymphoma**: diverse subtypes with extranodal involvement. **B symptoms**: fevers, night sweats, and weight loss from cytokines. **Why architecture matters**: classification requires node structure plus flow cytometry.

### CC-head_neck-21.1 (concept check)

Stem: A 22-year-old has painless matted cervical lymphadenopathy, drenching night sweats, and 6 kg weight loss. FNA shows atypical lymphoid cells. Why is core or excisional biopsy still needed?

- **Correct:** Classification needs nodal architecture
- Distractor: FNA seeds lymphoma along the tract — _why wrong:_ FNA does not spread lymphoma.
- Distractor: FNA cannot detect malignant lymphocytes — _why wrong:_ FNA can show atypical cells but cannot reliably classify the lymphoma.
- Distractor: Excision of the node is curative — _why wrong:_ Lymphoma is treated systemically; biopsy is diagnostic.

Explanation: Lymphoma subtypes are defined by architecture together with flow cytometry and molecular studies. Treatment depends on the exact subtype, so tissue with preserved architecture is required.

Pearl: Suspected lymphoma: get architecture, not just cells.

## T-head_neck-22 — Neck Management by Primary Site
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-22.overview**

Neck management depends on the primary site's drainage pattern and occult metastasis risk. Knowing which levels to treat for each site is a core oncologic principle.

**T-head_neck-22.physiology**

**Oral cavity**: drains to levels I-III, with the oral tongue capable of skipping to III-IV. **Oropharynx, larynx, hypopharynx**: drain to levels II-IV, plus retropharyngeal (oropharynx, hypopharynx) and VI (hypopharynx, subglottis). **Thyroid**: drains first to the central compartment (VI), then the lateral neck (III-IV) and mediastinum. **Nasopharynx**: drains to retropharyngeal nodes and levels II-V, often bilaterally. **Scalp and posterior skin**: drain to parotid, occipital, and level V nodes.

**T-head_neck-22.pathophysiology**

**Elective treatment threshold**: when occult metastasis risk exceeds about 15-20 percent, elective neck dissection or radiation is justified. **Skip metastases**: oral tongue cancers can bypass level I-II, which is why levels III (and IV for tongue) are included. **Bilateral risk**: midline or base-of-tongue, soft palate, supraglottic, and nasopharyngeal primaries require bilateral neck treatment. **Level IIb and V**: rarely involved without level IIa disease in mucosal cancers, so they can be omitted to spare the accessory nerve in the N0 neck. **Extranodal extension**: changes adjuvant therapy rather than the extent of dissection.

### CC-head_neck-22.1 (concept check)

Stem: A 55-year-old has a T2 oral tongue SCC and a clinically N0 neck. The plan includes elective neck dissection of levels I-III, with level IV often added. Why are lower levels included?

- **Correct:** Tongue cancers can skip to lower levels
- Distractor: Tongue lymphatics drain only to level IV — _why wrong:_ The tongue drains primarily to levels I-III.
- Distractor: Level III contains the thyroid gland — _why wrong:_ The thyroid lies in the central compartment, not level III.
- Distractor: Level IV is involved in every case — _why wrong:_ Level IV is involved in a minority, which is why it is debated.

Explanation: Oral tongue lymphatics can bypass the upper levels and reach level III or IV directly (skip metastases), so the elective dissection extends lower than for other oral cavity sites.

Pearl: Oral tongue: include level III, and consider level IV.

## T-head_neck-23 — Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-23.overview**

A nonfunctional larynx after cancer therapy causes chronic aspiration and recurrent pneumonia. When rehabilitation fails, laryngectomy or laryngotracheal separation can be lifesaving.

**T-head_neck-23.physiology**

**Airway protection sequence**: laryngeal elevation, epiglottic inversion, vocal fold and false fold closure, and arytenoid tilting close the airway during each swallow. **Sensory trigger**: superior laryngeal nerve sensation triggers protective cough and the swallow reflex. **Pharyngeal clearance**: base-of-tongue retraction and pharyngeal constriction clear the bolus so residue does not spill into the airway. **Cough clearance**: an effective cough expels aspirated material.

**T-head_neck-23.pathophysiology**

**Radiation fibrosis**: stiffens the larynx and pharynx, reducing elevation and constrictor contraction. **Neuropathy**: radiation-induced lower cranial neuropathy reduces sensation and cough, causing silent aspiration. **Chronic aspiration**: leads to pneumonia, malnutrition, and tube dependence. **Surgical logic**: when the larynx cannot protect the airway, separating the airway from the food passage (laryngectomy or laryngotracheal separation) eliminates aspiration.

### CC-head_neck-23.1 (concept check)

Stem: Three years after chemoradiation for supraglottic cancer, a patient with no evidence of tumor has had four aspiration pneumonias despite a gastrostomy tube and swallowing therapy. Why might total laryngectomy be offered?

- **Correct:** It separates airway from food
- Distractor: It reverses radiation fibrosis — _why wrong:_ Laryngectomy removes the aspirating larynx; it does not reverse fibrosis.
- Distractor: It restores normal swallowing — _why wrong:_ Swallowing remains affected by pharyngeal fibrosis; the benefit is airway protection.
- Distractor: It prevents cancer recurrence — _why wrong:_ There is no tumor; the indication is aspiration.

Explanation: When radiation fibrosis and neuropathy leave a larynx that cannot protect the airway, aspiration of saliva continues despite tube feeding. Separating the airway eliminates aspiration pneumonia.

Pearl: A nonfunctional larynx can be more dangerous than no larynx.

## T-head_neck-24 — Open Partial / Conservation Laryngectomy
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-24.overview**

Open partial laryngectomy (vertical hemilaryngectomy, supraglottic laryngectomy, supracricoid laryngectomy) removes cancer while preserving speech and swallowing without a permanent stoma. Candidacy depends on tumor extent and pulmonary reserve.

**T-head_neck-24.physiology**

**Cricoarytenoid unit**: the cricoid cartilage, an arytenoid, and its muscles and nerves form the minimal functional unit for speech, swallowing, and breathing. **Laryngeal sphincters**: the epiglottis, false folds, and true folds form layered airway protection. **Pulmonary reserve**: patients must cough effectively to clear expected postoperative aspiration. **Horizontal vs vertical anatomy**: the supraglottis and glottis develop separately, so horizontal resections can remove one while preserving the other.

**T-head_neck-24.pathophysiology**

**Expected aspiration**: removal of part of the sphincter causes temporary aspiration during swallowing relearning. **COPD**: patients with poor pulmonary reserve cannot tolerate aspiration, making partial laryngectomy contraindicated. **Supraglottic laryngectomy contraindications**: true vocal fold involvement, impaired cord mobility, or anterior commissure extension, since the operation spares the glottis. **Supracricoid laryngectomy**: requires at least one functional cricoarytenoid unit. **Cartilage invasion**: limits partial procedures.

### CC-head_neck-24.1 (concept check)

Stem: A 68-year-old with supraglottic SCC and mobile vocal folds has severe COPD (FEV1 35 percent predicted). Why is supraglottic laryngectomy contraindicated?

- **Correct:** He cannot tolerate expected aspiration
- Distractor: COPD prevents laryngeal wound healing — _why wrong:_ Healing is not the main issue; pulmonary reserve is.
- Distractor: COPD causes vocal fold paralysis — _why wrong:_ COPD does not paralyze the vocal folds.
- Distractor: COPD increases tumor spread — _why wrong:_ Lung disease does not change tumor biology.

Explanation: Partial laryngectomy removes part of the protective sphincter, so temporary aspiration is expected while swallowing is relearned. Patients need adequate pulmonary reserve and an effective cough to survive that period.

Pearl: Partial laryngectomy needs good lungs.

## T-head_neck-25 — Oral Tongue SCC
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-25.overview**

Oral tongue SCC is the most common oral cavity cancer, linked to tobacco and alcohol, but increasingly seen in younger nonsmokers. Depth of invasion drives T-stage and the decision for elective neck dissection, and surgery is primary therapy.

**T-head_neck-25.physiology**

**Intrinsic muscle mass**: the oral tongue is a highly mobile muscular organ essential for speech articulation, bolus formation, and swallowing. **Lymphatics**: rich lymphatics drain to levels I-III, and the tip can drain directly to lower levels (skip metastases); near-midline tumors drain bilaterally. **Nerves**: lingual nerve (sensation and taste via chorda tympani) and hypoglossal nerve (motor).

**T-head_neck-25.pathophysiology**

**Depth of invasion**: deeper tumors reach the rich lymphatic network in the muscle, sharply increasing nodal risk, which is why DOI was incorporated into AJCC 8th staging. **Elective neck dissection**: DOI over about 3-4 mm predicts occult nodal disease high enough to justify elective neck dissection, supported by randomized evidence. **Perineural invasion**: spread along the lingual or hypoglossal nerve increases local recurrence and calls for adjuvant therapy. **Function**: resections that remove large tongue volume impair speech and swallowing, guiding reconstruction choice.

### CC-head_neck-25.1 (concept check)

Stem: A 58-year-old has a 2.5 cm lateral oral tongue SCC with a 6 mm depth of invasion on biopsy and imaging, and a clinically N0 neck. Why is elective neck dissection recommended?

- **Correct:** Depth of invasion predicts occult nodes
- Distractor: Lateral tongue cancers usually spread bilaterally — _why wrong:_ Well-lateralized tongue cancers usually drain ipsilaterally.
- Distractor: Radiation cannot treat oral cavity disease — _why wrong:_ Radiation is used adjuvantly; surgery is primary because it gives better control and pathology.
- Distractor: Neck dissection improves speech outcomes — _why wrong:_ Neck dissection does not affect speech; its purpose is staging and control.

Explanation: Deeper tumors reach the rich lymphatics within tongue muscle, sharply increasing occult nodal risk. Randomized evidence supports elective neck dissection in early oral cancer, and depth of invasion is part of AJCC T-stage.

Pearl: Oral tongue cancer deeper than about 3-4 mm: treat the N0 neck.

## T-head_neck-26 — Osteoradionecrosis of the Jaw
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-26.overview**

Osteoradionecrosis is exposed, nonhealing irradiated bone, usually the mandible, persisting for 3 months or more. It is triggered by dental extraction or trauma and managed from conservative care to segmental resection with free fibula reconstruction.

**T-head_neck-26.physiology**

**Bone remodeling**: osteoclasts resorb and osteoblasts rebuild bone continuously, directed by osteocytes. **Mandible blood supply**: the inferior alveolar artery provides endosteal flow, supplemented by periosteal vessels; the dense cortical mandible has less collateral supply than the maxilla. **Dentition and mucosa**: thin mucosa over the mandible and teeth that breach it create entry points for injury and infection.

**T-head_neck-26.pathophysiology**

**Radiation-induced fibroatrophy**: radiation activates TGF-beta-driven fibrosis, endarteritis, and osteocyte death. **Hypoxic, hypocellular, hypovascular bone (Marx)**: the bone cannot remodel after injury. **Trigger**: extraction, trauma, or ill-fitting dentures expose bone that never heals. **Risk factors**: dose above about 60 Gy, mandible within the high-dose field, poor dentition, and smoking. **Progression**: pain, exposed bone, orocutaneous fistula, and pathologic fracture. **Treatment logic**: pentoxifylline-tocopherol (with clodronate) targets the fibrotic process; advanced disease requires resection of all necrotic bone and replacement with vascularized bone. **Prevention**: dental evaluation and extractions before radiation, and fluoride.

### CC-head_neck-26.1 (concept check)

Stem: Eighteen months after 70 Gy to the oral cavity, a patient has a lower molar extracted. The socket never heals and bone remains exposed 4 months later. Why did the extraction trigger this?

- **Correct:** Irradiated bone cannot repair the injury
- Distractor: Extraction seeded residual tumor cells — _why wrong:_ Recurrent tumor must be excluded, but the classic mechanism is failed bone healing.
- Distractor: Extraction severed the inferior alveolar nerve — _why wrong:_ Nerve injury causes numbness, not exposed nonhealing bone.
- Distractor: Extraction fractured the mandible — _why wrong:_ A fracture is a possible late consequence, not the cause.

Explanation: Radiation leaves bone hypoxic, hypocellular, and hypovascular, with fibrosis and lost osteocytes. Trauma exposes bone that cannot remodel. Pre-radiation dental extraction and fluoride reduce risk; advanced disease needs resection and vascularized bone.

Pearl: Fix the teeth before radiation.

## T-head_neck-27 — Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-27.overview**

Palliative care addresses symptoms and goals in advanced head and neck cancer, alongside or instead of cancer-directed therapy. Airway, bleeding, pain, nutrition, and communication needs are central.

**T-head_neck-27.physiology**

**Function concentration**: breathing, swallowing, speech, and facial identity are all served by the head and neck. **Pain pathways**: nociceptive pain from tissue invasion and neuropathic pain from nerve involvement travel through different mechanisms. **Vascular anatomy**: major vessels lie close to tumor beds and irradiated tissue.

**T-head_neck-27.pathophysiology**

**Symptom burden**: pain, dysphagia, airway obstruction, bleeding, secretions, and disfigurement. **Carotid blowout**: sentinel bleeding often precedes major hemorrhage. **Neuropathic pain**: requires agents such as gabapentinoids in addition to opioids. **Goals-concordant care**: early palliative involvement improves quality of life. **Decision-making**: tracheostomy and feeding tubes should match patient goals rather than default.

### CC-head_neck-27.1 (concept check)

Stem: A patient with unresectable recurrent neck cancer after radiation has a small, self-limited bleed from a neck wound overlying the carotid. Why is this event important?

- **Correct:** It may herald a carotid blowout
- Distractor: It is a minor wound complication — _why wrong:_ A bleed from a wound over an exposed carotid should never be dismissed as minor.
- Distractor: It indicates tumor regression — _why wrong:_ Bleeding reflects vessel wall erosion, not tumor response.
- Distractor: It signals wound infection only — _why wrong:_ Infection may contribute, but the main danger is impending arterial rupture.

Explanation: Sentinel bleeds often precede carotid blowout. They should prompt urgent imaging, consideration of endovascular treatment, airway and hemorrhage planning, and a goals-of-care discussion.

Pearl: Sentinel bleed = prepare for blowout and talk about goals.

## T-head_neck-28 — Parapharyngeal Space Tumor
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-28.overview**

Parapharyngeal space tumors are usually benign: pleomorphic adenomas of the deep parotid (prestyloid) and neurogenic tumors or paragangliomas (poststyloid). Imaging location relative to the styloid predicts histology and surgical approach.

**T-head_neck-28.physiology**

**Shape**: an inverted pyramid from the skull base to the hyoid. **Compartments**: the tensor-styloid fascia divides the prestyloid compartment (fat, deep parotid lobe) from the poststyloid compartment (carotid, jugular, CN IX-XII, sympathetic chain). **Neighbors**: tonsil medially, pterygoid muscles laterally.

**T-head_neck-28.pathophysiology**

**Prestyloid tumors**: pleomorphic adenoma of deep lobe or minor salivary origin displaces the parapharyngeal fat medially and the carotid posteriorly. **Poststyloid tumors**: schwannomas (vagus, sympathetic) and paragangliomas displace the carotid anteriorly. **Presentation**: oropharyngeal bulge or incidental imaging finding. **Surgical approach**: transcervical for most, with transparotid or mandibulotomy for larger tumors; FNA through the mouth is avoided.

### CC-head_neck-28.1 (concept check)

Stem: MRI shows a well-circumscribed parapharyngeal mass that displaces the internal carotid artery anteriorly and contains flow voids. Which compartment and tumor are most likely?

- **Correct:** Poststyloid space; paraganglioma
- Distractor: Prestyloid space; pleomorphic adenoma — _why wrong:_ Prestyloid salivary tumors push the carotid posteriorly, not anteriorly.
- Distractor: Retropharyngeal space; lymph node — _why wrong:_ Retropharyngeal masses displace the carotid laterally.
- Distractor: Masticator space; sarcoma — _why wrong:_ Masticator space masses lie lateral to the parapharyngeal fat.

Explanation: The poststyloid compartment contains the carotid sheath, CN IX-XII, and the sympathetic chain, so paragangliomas and schwannomas push the carotid forward. Flow voids suggest a paraganglioma.

Pearl: Carotid pushed forward = poststyloid tumor; pushed back = prestyloid.

## T-head_neck-29 — Radiation Therapy Principles for Head & Neck Surgeons
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-29.overview**

Radiation therapy kills cancer cells through DNA damage, delivered in fractions to exploit differences between tumor and normal tissue. Surgeons need to understand dose, fractionation, IMRT, and toxicity to make joint decisions.

**T-head_neck-29.physiology**

**DNA damage**: radiation ionizes water to create free radicals that cause double-strand breaks; cells die mainly at their next mitosis. **Cell-cycle sensitivity**: G2/M cells are most sensitive and late S phase most resistant. **Oxygen effect**: oxygen fixes radical damage, so well-oxygenated cells are 2-3 times more sensitive than hypoxic ones. **Dose units**: definitive head and neck courses deliver about 70 Gy in 2 Gy daily fractions; postoperative courses about 60-66 Gy.

**T-head_neck-29.pathophysiology**

**The 4 Rs**: repair (normal tissue repairs between fractions), reassortment (cells move into sensitive phases), repopulation (tumor regrows during gaps), and reoxygenation (hypoxic cells become oxygenated). **Hypoxic resistance**: hypoxic tumor cores resist radiation, contributing to failure. **Treatment interruptions**: allow accelerated repopulation, reducing control by roughly 1 percent per day of delay. **Concurrent cisplatin**: sensitizes tumor cells and improves control. **IMRT**: sculpts dose to spare parotids and swallowing structures, reducing xerostomia. **Late effects**: slowly dividing tissues show damage months to years later.

## T-head_neck-30 — Reconstruction Selection After Head & Neck Ablation
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-30.overview**

Reconstruction after head and neck ablation ranges from primary closure to local, regional, and free flaps. Selection depends on defect size, tissue type needed, function, prior radiation, and patient factors.

**T-head_neck-30.physiology**

**Reconstructive ladder and elevator**: options range from secondary intention to free tissue transfer; modern practice chooses the simplest option that restores function, sometimes jumping straight to a free flap. **Tissue matching**: replace like with like: thin pliable skin for mucosa, bulk for volume, vascularized bone for mandible continuity. **Axial blood supply**: flaps built on named vessels (radial artery, descending branch of lateral circumflex femoral, peroneal) survive transfer. **Recipient vessels**: facial artery, superior thyroid artery, and internal or external jugular tributaries supply free flaps in the neck.

**T-head_neck-30.pathophysiology**

**Free flap advantages**: composite tissue, reliable blood supply, and two-team surgery; success rates exceed 95 percent. **Radial forearm**: thin, pliable, sensate (lateral antebrachial cutaneous nerve) for tongue and floor of mouth. **Anterolateral thigh**: variable bulk for total glossectomy and large defects. **Fibula**: up to about 25 cm of bone for mandible reconstruction, allowing dental implants; requires assessment of leg vascularity. **Irradiated beds**: vascularized tissue resists breakdown and covers exposed vessels. **Patient factors**: peripheral vascular disease, prior surgery, and functional goals determine donor site.

### CC-head_neck-30.1 (concept check)

Stem: After segmental mandibulectomy from parasymphysis to angle for oral cancer, the patient wants dental implants. Which reconstruction best meets this goal?

- **Correct:** Fibula free flap
- Distractor: Radial forearm free flap — _why wrong:_ The radial forearm provides thin soft tissue and only a small strip of bone.
- Distractor: Anterolateral thigh free flap — _why wrong:_ The ALT provides soft tissue bulk without bone.
- Distractor: Pectoralis major pedicled flap — _why wrong:_ The pectoralis provides soft tissue but no vascularized bone.

Explanation: The fibula provides up to about 25 cm of strong, vascularized bicortical bone that can be osteotomized to shape and accepts dental implants. Leg vascular status must be assessed first.

Pearl: Segmental mandible defect = fibula.

## T-head_neck-31 — Recurrent / Metastatic HNSCC
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-31.overview**

Recurrent or metastatic HNSCC not amenable to curative surgery or radiation is treated with systemic therapy (immunotherapy with or without chemotherapy) with a focus on quality of life. Selected recurrences remain curable with salvage surgery or reirradiation.

**T-head_neck-31.physiology**

**Immune surveillance**: T cells recognize tumor neoantigens presented on MHC class I. **PD-1/PD-L1 checkpoint**: PD-L1 on tumor and immune cells binds PD-1 on activated T cells, switching them off; this normally limits tissue damage during inflammation. **Combined positive score**: counts PD-L1-positive tumor and immune cells relative to tumor cells and predicts benefit from PD-1 blockade. **Treatment-naive vs pretreated tissue**: prior radiation and surgery alter blood supply and immune infiltration.

**T-head_neck-31.pathophysiology**

**Immune escape**: tumors upregulate PD-L1, lose MHC, and recruit suppressive cells, allowing progression after initial therapy. **First-line therapy**: pembrolizumab alone (CPS 1 or greater) or with platinum-5-FU improved survival over the EXTREME regimen (KEYNOTE-048). **Durable responses**: a minority achieve long-lasting control because restored T-cell immunity has memory. **Resistance mechanisms**: DNA repair upregulation, EGFR signaling, and anti-apoptotic pathways reduce chemotherapy and cetuximab effectiveness. **Patterns of failure**: locoregional recurrence dominates; distant spread most often goes to lung, then bone and liver. **Curative salvage**: limited locoregional recurrences can be resected, and reirradiation is used selectively.

### CC-head_neck-31.1 (concept check)

Stem: A 62-year-old has recurrent oral cavity SCC with lung metastases that is not amenable to surgery or reirradiation. Tumor PD-L1 combined positive score is 20. What is the preferred first-line systemic therapy?

- **Correct:** Pembrolizumab-based therapy
- Distractor: Cetuximab with platinum and 5-FU — _why wrong:_ The EXTREME regimen was the prior standard, but pembrolizumab-based therapy improved survival in CPS-positive disease.
- Distractor: Single-agent methotrexate — _why wrong:_ Methotrexate is a palliative option with lower efficacy, not first-line in CPS-positive disease.
- Distractor: Radioactive iodine therapy — _why wrong:_ RAI treats differentiated thyroid cancer, not squamous cell carcinoma.

Explanation: KEYNOTE-048 established pembrolizumab alone (CPS 1 or more) or with platinum and 5-FU as first-line therapy for recurrent or metastatic HNSCC. Responders can have durable control through restored T-cell immunity.

Pearl: Recurrent or metastatic HNSCC: check CPS, start pembrolizumab-based therapy.

## T-head_neck-32 — Salvage Surgery After Radiation / Chemoradiation
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-32.overview**

Salvage surgery treats persistent or recurrent cancer after radiation or chemoradiation. It offers a chance of cure but carries high complication rates because irradiated tissue heals poorly.

**T-head_neck-32.physiology**

**Wound healing phases**: hemostasis, inflammation, proliferation (fibroblasts, angiogenesis), and remodeling, all dependent on oxygen delivery. **Angiogenesis**: new capillaries must grow into a wound to support collagen synthesis. **Radiation effects**: progressive obliterative endarteritis, fibroblast dysfunction, and loss of stem cells develop over months to years. **Tissue oxygen**: fibroblast collagen production and neutrophil killing both require adequate oxygen tension.

**T-head_neck-32.pathophysiology**

**Hypoxic-hypocellular-hypovascular tissue**: irradiated beds cannot mount normal angiogenesis or collagen deposition, so incisions and mucosal closures break down. **Fistula risk**: pharyngocutaneous fistula rates after salvage laryngectomy are roughly double those after primary surgery. **Vascularized flap logic**: pectoralis or free flaps bring nonirradiated tissue with its own blood supply, lowering fistula rates in salvage (meta-analyses support onlay reinforcement). **Detection challenge**: post-radiation edema and fibrosis mask recurrence, so PET-CT around 12 weeks and biopsy of suspicious findings guide timing. **Prognosis**: early recurrence, advanced recurrent stage, and positive margins predict poor outcome after salvage.

## T-head_neck-33 — Sentinel Lymph Node Biopsy in Oral Cavity Cancer
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-33.overview**

Sentinel lymph node biopsy maps the first draining nodes of early oral cavity cancer and removes only them for staging. It is an alternative to elective neck dissection in the clinically N0 neck.

**T-head_neck-33.physiology**

**Lymphatic drainage**: lymph from a tumor travels first to one or a few sentinel nodes. **Radiotracer mapping**: technetium-labeled colloid injected around the primary is taken up by lymphatics and concentrates in sentinel nodes. **Imaging**: lymphoscintigraphy and SPECT-CT localize sentinel nodes before surgery. **Gamma probe**: guides intraoperative identification.

**T-head_neck-33.pathophysiology**

**Stepwise spread**: metastases seed the sentinel node first, so a negative sentinel node predicts a negative neck. **Accuracy**: high negative predictive value in early oral cancer, comparable to elective neck dissection for survival in trials. **Shine-through**: radiotracer at the primary obscures nearby nodes, especially floor-of-mouth tumors. **Positive sentinel**: requires completion neck dissection.

### CC-head_neck-33.1 (concept check)

Stem: A surgeon plans sentinel lymph node biopsy for a T1 floor-of-mouth SCC. Why is this site technically harder to map than a lateral tongue cancer?

- **Correct:** Injection-site activity obscures nearby nodes
- Distractor: The floor of mouth has no lymphatics — _why wrong:_ The floor of mouth has rich lymphatics; that is not the problem.
- Distractor: Radiotracer is toxic to floor-of-mouth tissue — _why wrong:_ Technetium colloid is not toxic at mapping doses.
- Distractor: Floor-of-mouth cancers never metastasize — _why wrong:_ Floor-of-mouth cancers do metastasize, often bilaterally.

Explanation: Radiotracer at the primary site creates a large signal (shine-through) that can hide sentinel nodes close to it in level I, lowering detection.

Pearl: Floor-of-mouth sentinel biopsy has a shine-through problem.

## T-head_neck-34 — Sinonasal Malignancies
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-34.overview**

Sinonasal malignancies include SCC, adenocarcinoma, esthesioneuroblastoma, SNUC, mucosal melanoma, and others; each has distinct behavior. They present late, and treatment combines surgery and radiation with histology-specific systemic therapy.

**T-head_neck-34.physiology**

**Anatomic compartments**: nasal cavity, maxillary, ethmoid, frontal, and sphenoid sinuses, separated from orbit and brain by thin bone. **Olfactory epithelium**: specialized neuroepithelium at the cribriform plate, source of esthesioneuroblastoma. **Neural pathways**: V2 runs through the pterygopalatine fossa to foramen rotundum; perineural routes lead to the cavernous sinus. **Lymphatic drainage**: retropharyngeal and level I-II nodes, with relatively low early nodal spread.

**T-head_neck-34.pathophysiology**

**Late presentation**: tumors fill air spaces silently, presenting with unilateral obstruction, epistaxis, or neuro-ophthalmic signs. **Spread**: to orbit, skull base, brain, and perineural pathways. **Histology-driven treatment**: esthesioneuroblastoma (Kadish/Hyams grading), SNUC and SMARCB1-deficient carcinomas (aggressive, induction chemotherapy), and mucosal melanoma (poor prognosis). **Occupational exposure**: wood dust strongly associated with ethmoid adenocarcinoma. **Endoscopic resection**: comparable outcomes to open surgery for selected tumors with negative margins.

### CC-head_neck-34.1 (concept check)

Stem: A 45-year-old has unilateral nasal obstruction and anosmia. MRI shows a mass at the cribriform plate extending into the anterior cranial fossa. Biopsy shows small round blue cells in lobules with a neurofibrillary matrix and Homer Wright rosettes. What is the diagnosis?

- **Correct:** Esthesioneuroblastoma
- Distractor: Sinonasal undifferentiated carcinoma — _why wrong:_ SNUC is a high-grade carcinoma without neurofibrillary matrix or rosettes.
- Distractor: Sinonasal mucosal melanoma — _why wrong:_ Melanoma stains for melanocytic markers and lacks neurofibrillary matrix.
- Distractor: Extranodal NK/T-cell lymphoma — _why wrong:_ Lymphoma has angiocentric infiltrates without neurofibrillary matrix.

Explanation: Esthesioneuroblastoma arises from olfactory neuroepithelium at the cribriform plate. It is staged by Kadish and graded by Hyams, and is treated with craniofacial or endoscopic resection plus radiation.

Pearl: Cribriform plate mass with neurofibrillary matrix = esthesioneuroblastoma.

## T-head_neck-35 — Supraglottic Cancer
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-35.overview**

Supraglottic cancer involves the epiglottis, aryepiglottic folds, false cords, and arytenoids. It presents late with dysphagia and neck nodes because of rich bilateral lymphatics, and treatment ranges from transoral resection to chemoradiation or total laryngectomy.

**T-head_neck-35.physiology**

**Airway protection**: during swallowing the epiglottis tilts down, the aryepiglottic folds and false folds close, and the larynx elevates under the tongue base. **Pre-epiglottic space**: a fat-filled space anterior to the epiglottis, connected to the epiglottis by natural cartilage fenestrations. **Paraglottic space**: fat lateral to the ventricle and folds, continuous with the pre-epiglottic space, allowing spread from supraglottis to glottis without mucosal involvement. **Lymphatics**: the supraglottis has rich, bilateral lymphatic channels that drain to levels II and III.

**T-head_neck-35.pathophysiology**

**Late symptoms**: tumors grow in a wide airway before obstructing, so dysphagia and otalgia appear late. **Pre-epiglottic invasion**: tumor passes through fenestrations of the epiglottic cartilage into the pre-epiglottic space (T3). **Nodal spread**: early and often bilateral, requiring bilateral neck treatment. **Supraglottic laryngectomy limits**: requires preserved glottic function and adequate pulmonary reserve to tolerate aspiration during recovery.

### CC-head_neck-35.1 (concept check)

Stem: A 60-year-old has a T2 lateral supraglottic carcinoma of the aryepiglottic fold and a clinically N0 neck. Why are both sides of the neck treated electively?

- **Correct:** Rich, crossing lymphatics
- Distractor: The glottis drains to the opposite neck — _why wrong:_ The glottis has sparse lymphatics and is not the reason for bilateral treatment.
- Distractor: Supraglottic tumors are always midline — _why wrong:_ Even lateral supraglottic tumors carry bilateral occult nodal risk.
- Distractor: The thyroid gland is routinely involved — _why wrong:_ Thyroid involvement is not routine and does not dictate bilateral neck treatment.

Explanation: The supraglottis has rich, crossing lymphatic channels, so occult bilateral nodal metastasis is common. Early glottic cancer, by contrast, rarely spreads to nodes.

Pearl: Supraglottic cancer = treat both necks; early glottic cancer = no elective neck.

## T-head_neck-36 — Systemic Therapy Foundations in Head & Neck Cancer
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-36.overview**

Systemic therapies in head and neck cancer include cytotoxic chemotherapy (cisplatin, carboplatin, taxanes, 5-FU), targeted therapy (cetuximab), and immunotherapy. Knowing mechanisms and toxicities guides patient selection.

**T-head_neck-36.physiology**

**Cell division**: cytotoxic drugs target DNA synthesis or mitosis in rapidly dividing cells, including bone marrow, mucosa, and hair follicles. **EGFR signaling**: overexpressed in most HNSCC, driving proliferation through MAPK and PI3K pathways. **Drug clearance**: cisplatin is renally cleared, making kidney function a key eligibility factor. **Cochlear vulnerability**: outer hair cells are sensitive to platinum-induced oxidative stress.

**T-head_neck-36.pathophysiology**

**Cisplatin**: forms DNA crosslinks; dose-limiting toxicities are nephrotoxicity, ototoxicity, neuropathy, and nausea. **Carboplatin**: less nephrotoxic and ototoxic but more myelosuppressive. **Cetuximab**: blocks EGFR; inferior to cisplatin with radiation in HPV-positive disease (De-ESCALaTE, RTOG 1016); causes acneiform rash. **Taxanes**: stabilize microtubules; induction TPF is used in larynx preservation and bulky disease. **Checkpoint inhibitors**: now first-line in recurrent or metastatic disease.

### CC-head_neck-36.1 (concept check)

Stem: A 55-year-old with HPV-positive oropharyngeal SCC and normal renal function and hearing asks whether cetuximab could replace cisplatin with radiation to reduce side effects. What does the trial evidence show?

- **Correct:** Cetuximab gave worse survival than cisplatin
- Distractor: Cetuximab was equally effective and less toxic — _why wrong:_ RTOG 1016 and De-ESCALaTE showed inferior outcomes without reduced overall toxicity.
- Distractor: Cetuximab is more ototoxic than cisplatin — _why wrong:_ Cisplatin is the ototoxic agent; cetuximab causes acneiform rash.
- Distractor: Cisplatin is contraindicated in HPV-positive disease — _why wrong:_ Cisplatin remains the standard concurrent agent.

Explanation: De-escalation trials replacing cisplatin with cetuximab in HPV-positive oropharyngeal cancer found inferior survival. Cisplatin remains standard for eligible patients.

Pearl: HPV-positive OPSCC: cisplatin remains the standard concurrent agent.

## T-head_neck-37 — TEP and Alaryngeal Speech
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-37.overview**

Tracheoesophageal puncture with a voice prosthesis is the most effective method of voice restoration after total laryngectomy. Electrolarynx and esophageal speech are alternatives.

**T-head_neck-37.physiology**

**Normal phonation**: lung air passes through adducted vocal folds, which vibrate to create sound that the pharynx, mouth, and nose then shape into speech. **After laryngectomy**: the vocal folds are gone and the trachea opens at the stoma, so lung air no longer reaches the pharynx. **Pharyngoesophageal (PE) segment**: the reconstructed cricopharyngeus and inferior constrictor can vibrate like a substitute glottis when air passes through it. **Power source**: lung air provides a large, sustained airflow, which is why TEP voice is more fluent than esophageal speech that uses only a small swallowed air reservoir.

**T-head_neck-37.pathophysiology**

**TEP mechanism**: a one-way valve between trachea and esophagus lets lung air flow into the pharynx when the stoma is occluded, vibrating the pharyngoesophageal segment. **Pharyngeal spasm**: hypertonicity of the PE segment prevents fluent speech; treated with botulinum toxin or myotomy. **Prosthesis leakage**: valve failure or puncture enlargement allows aspiration. **Fungal colonization**: Candida degrades the valve.

### CC-head_neck-37.1 (concept check)

Stem: A laryngectomy patient with a well-fitted voice prosthesis can produce only strained, interrupted voice. Insufflation testing shows high pharyngoesophageal segment pressure. Which treatment helps most?

- **Correct:** Botulinum toxin to the PE segment
- Distractor: Upsizing to a larger prosthesis — _why wrong:_ Prosthesis size does not relieve PE segment spasm.
- Distractor: Removing the prosthesis permanently — _why wrong:_ The prosthesis works; the problem is spasm of the vibrating segment.
- Distractor: Speech therapy alone — _why wrong:_ Therapy helps technique but rarely overcomes true spasm without targeted treatment.

Explanation: Voice after laryngectomy depends on the pharyngoesophageal segment vibrating as air passes through the prosthesis. Spasm prevents vibration; botulinum toxin or myotomy relaxes it.

Pearl: TEP voice failure from spasm: relax the PE segment.

## T-head_neck-38 — Tonsil SCC
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-38.overview**

Tonsil SCC is the most common oropharyngeal cancer subsite, most often HPV-associated. It often presents as a neck mass, and treatment is radiation-based or transoral surgery with adjuvant therapy based on pathology.

**T-head_neck-38.physiology**

**Tonsillar fossa**: bounded by anterior and posterior pillars, overlying the superior constrictor muscle. **Parapharyngeal space**: lies just lateral to the constrictor, containing the carotid and cranial nerves. **Lymphatics**: primary drainage to level II (jugulodigastric node), then III and retropharyngeal.

**T-head_neck-38.pathophysiology**

**HPV-driven tumors**: arise in crypts and spread early to nodes, with excellent radiation response. **Lateral spread**: invasion through the constrictor into the parapharyngeal space increases morbidity and may preclude TORS. **Pterygoid invasion**: causes trismus and indicates advanced disease. **Bilateral nodes**: unusual for well-lateralized tonsil cancers, which allows ipsilateral radiation in selected cases.

### CC-head_neck-38.1 (concept check)

Stem: A 50-year-old has a p16-positive left tonsil SCC. CT shows tumor extending through the superior constrictor into the medial pterygoid muscle, and he has new trismus. Why does this finding matter?

- **Correct:** It signals advanced local extension
- Distractor: It confirms HPV-negative biology — _why wrong:_ The tumor is p16-positive; pterygoid invasion reflects extent, not HPV status.
- Distractor: It predicts bilateral nodal disease — _why wrong:_ Lateralized tonsil cancers usually drain ipsilaterally regardless of pterygoid invasion.
- Distractor: It means the tumor is radioresistant — _why wrong:_ HPV-positive tumors are generally radiosensitive.

Explanation: Spread through the constrictor into the parapharyngeal space and pterygoid muscles indicates advanced local disease, causes trismus, and may preclude transoral resection.

Pearl: Trismus in oropharyngeal cancer implies pterygoid invasion.

## T-head_neck-39 — Total Laryngectomy
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-39.overview**

Total laryngectomy removes the larynx and permanently separates the airway from the digestive tract, creating an end tracheostoma. It is used for advanced or recurrent laryngeal and hypopharyngeal cancer, and for a nonfunctional larynx.

**T-head_neck-39.physiology**

**Upper airway conditioning**: the nose and pharynx warm, humidify, and filter inspired air, supplying about 75 percent of the humidity the lungs need. **Glottic functions**: the larynx generates voice, permits a strong cough by closing against subglottic pressure, and stabilizes the chest for lifting (Valsalva). **Separate tracts**: normally the airway and food passage share the pharynx; laryngectomy permanently separates them, so breathing is through the stoma and eating through the neopharynx. **Thyroid and parathyroid neighbors**: the thyroid isthmus and lobes lie on the trachea and are often partially removed or irradiated.

**T-head_neck-39.pathophysiology**

**Lost upper airway conditioning**: stoma breathing dries secretions, so heat-moisture exchangers are required. **Lost voice**: requires tracheoesophageal puncture, electrolarynx, or esophageal speech. **Pharyngocutaneous fistula**: impaired healing in irradiated tissue, hypothyroidism, and malnutrition increase fistula rates; vascularized flap reinforcement reduces it in salvage. **Hypothyroidism**: from hemithyroidectomy, radiation, or both; worsens healing. **Stomal stenosis**: wound contracture narrows the stoma.

### CC-head_neck-39.1 (concept check)

Stem: A 65-year-old is scheduled for salvage total laryngectomy after failed chemoradiation. Preoperative labs show a TSH of 14 mIU/L. Why should this be addressed before surgery?

- **Correct:** Hypothyroidism raises fistula risk
- Distractor: It causes stomal stenosis directly — _why wrong:_ Hypothyroidism impairs wound healing; it does not directly narrow the stoma.
- Distractor: It prevents use of a voice prosthesis — _why wrong:_ Thyroid status does not affect TEP candidacy.
- Distractor: It causes postoperative hypocalcemia — _why wrong:_ Hypocalcemia relates to parathyroid injury, not TSH.

Explanation: Hypothyroidism impairs wound healing and roughly doubles pharyngocutaneous fistula rates after laryngectomy, especially in irradiated tissue. Correcting it, plus vascularized flap reinforcement in salvage, reduces complications.

Pearl: Check and correct TSH before salvage laryngectomy.

## T-head_neck-40 — Tracheal Malignancy
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-40.overview**

Primary tracheal malignancies are rare, mostly SCC and adenoid cystic carcinoma, and present with progressive dyspnea often misdiagnosed as asthma. Resection with primary anastomosis is preferred when possible.

**T-head_neck-40.physiology**

**Structure**: about 10-12 cm of C-shaped cartilage rings with a posterior membranous wall. **Segmental blood supply**: inferior thyroid, bronchial, and other arteries enter laterally in a segmental pattern, so circumferential dissection devascularizes it. **Resectable length**: about half the adult trachea can be resected with neck flexion and release maneuvers. **Airflow physics**: resistance rises steeply as the radius narrows.

**T-head_neck-40.pathophysiology**

**Airway narrowing**: symptoms (dyspnea, stridor) appear only when the lumen is reduced by about 50-75 percent. **Misdiagnosis**: wheezing unresponsive to bronchodilators is misread as asthma. **SCC**: smoking-related, often with nodal and distant spread. **Adenoid cystic carcinoma**: slow growing with submucosal and perineural spread beyond visible margins. **Anastomotic tension**: excessive tension causes dehiscence, limiting resection length.

### CC-head_neck-40.1 (concept check)

Stem: A 45-year-old has 2 years of progressive exertional dyspnea and wheeze treated as asthma without improvement. CT shows a smooth mass narrowing the trachea by 70 percent; biopsy shows adenoid cystic carcinoma. Why was diagnosis delayed?

- **Correct:** Symptoms need major narrowing
- Distractor: The tumor grows very rapidly — _why wrong:_ Adenoid cystic carcinoma is slow-growing, which delays symptoms.
- Distractor: It always causes early hemoptysis — _why wrong:_ Hemoptysis is inconsistent, especially with submucosal tumors.
- Distractor: It is obvious on plain chest X-ray — _why wrong:_ Tracheal tumors are often missed on chest radiographs.

Explanation: Airway resistance rises steeply with narrowing, but symptoms usually appear only after the lumen is reduced by about 50-75 percent. Fixed wheeze unresponsive to bronchodilators should prompt airway imaging.

Pearl: Asthma that does not respond to treatment: image the trachea.

## T-head_neck-41 — Transoral Laser Microsurgery for Laryngeal Cancer
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-41.overview**

Transoral laser microsurgery removes laryngeal cancers through the mouth with a CO2 laser, preserving function without external incisions. It is used for early glottic and supraglottic cancers and selected advanced tumors.

**T-head_neck-41.physiology**

**CO2 laser**: 10,600 nm wavelength absorbed by water, cutting and coagulating with minimal thermal spread. **Laryngeal exposure**: requires a straight line of sight from the mouth to the larynx. **Tissue planes**: the vocal ligament and thyroarytenoid muscle define depth of resection. **Airway fire triangle**: fuel, oxygen, and an ignition source.

**T-head_neck-41.pathophysiology**

**Piecemeal resection**: tumors are cut through to see depth, which is oncologically sound when margins are clear. **Exposure limits**: trismus, retrognathia, and limited neck extension prevent adequate exposure. **Airway fire**: laser with oxygen and the endotracheal tube; laser-safe tubes and low oxygen reduce risk. **Anterior commissure**: difficult to expose and margins can be close. **Voice outcomes**: depend on resection depth.

### CC-head_neck-41.1 (concept check)

Stem: During CO2 laser excision of a glottic cancer, why does the anesthesiologist keep the inspired oxygen concentration as low as safely possible and use a laser-resistant tube?

- **Correct:** To prevent an airway fire
- Distractor: To improve surgical exposure — _why wrong:_ Oxygen concentration does not change exposure.
- Distractor: To reduce intraoperative bleeding — _why wrong:_ Oxygen level does not control bleeding.
- Distractor: To shorten emergence from anesthesia — _why wrong:_ Oxygen concentration is set for fire safety, not emergence.

Explanation: A laser (ignition), oxygen (oxidizer), and the endotracheal tube or drapes (fuel) complete the fire triangle. Low oxygen, laser-safe tubes, and saline-filled cuffs reduce the risk.

Pearl: Laser + oxygen + fuel = airway fire.

## T-head_neck-42 — Tumor Immunology / Immunotherapy in HNSCC
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-42.overview**

Tumor immunology explains how head and neck cancers evade immune attack and how checkpoint inhibitors restore it. Immunotherapy is standard for recurrent and metastatic disease and is moving into neoadjuvant and curative settings.

**T-head_neck-42.physiology**

**Cancer-immunity cycle**: antigen release, uptake and presentation by dendritic cells, T-cell priming in nodes, trafficking to tumor, infiltration, recognition, and killing. **Checkpoints**: CTLA-4 dampens priming in lymph nodes; PD-1 dampens effector T cells in tissue. **Tolerance**: checkpoints prevent autoimmunity, which is why blocking them can cause autoimmune toxicity. **Regional nodes**: are where anti-tumor T cells are primed, a reason neoadjuvant immunotherapy before neck dissection is being studied.

**T-head_neck-42.pathophysiology**

**Evasion strategies**: PD-L1 upregulation, MHC class I loss, regulatory T cells, myeloid-derived suppressor cells, and immunosuppressive cytokines (TGF-beta, IL-10). **Hot vs cold tumors**: T-cell-inflamed tumors respond better; HPV-positive tumors carry viral antigens and are often more inflamed. **Checkpoint blockade**: anti-PD-1 antibodies (pembrolizumab, nivolumab) release suppressed T cells. **Neoadjuvant rationale**: giving immunotherapy while the tumor and nodes are intact maximizes antigen presentation; KEYNOTE-689 added perioperative pembrolizumab for resectable disease. **Immune-related adverse events**: thyroiditis and hypothyroidism are most common in head and neck patients; colitis, pneumonitis, hepatitis, and hypophysitis are less common but serious.

### CC-head_neck-42.1 (concept check)

Stem: Ten weeks after starting pembrolizumab for recurrent HNSCC, a patient reports fatigue and cold intolerance. TSH is 25 mIU/L with a low free T4. What is the mechanism?

- **Correct:** Immune-related autoimmune thyroiditis
- Distractor: Tumor invasion of the thyroid gland — _why wrong:_ Thyroid invasion would not usually present as a sudden biochemical hypothyroidism.
- Distractor: Iodine deficiency from poor intake — _why wrong:_ Iodine deficiency is rare and not the cause here.
- Distractor: Pituitary metastasis causing low TSH — _why wrong:_ Secondary hypothyroidism would cause a low, not high, TSH.

Explanation: Checkpoint inhibitors remove peripheral tolerance, so T cells attack the thyroid. Thyroiditis and hypothyroidism are the most common endocrine immune-related adverse events and are treated with levothyroxine.

Pearl: Check TSH regularly during checkpoint inhibitor therapy.

## T-head_neck-43 — Unknown Primary with Cervical Metastasis
_source: pathophys_v470/head_neck_a.py_

**T-head_neck-43.overview**

Carcinoma of unknown primary is a metastatic neck node (usually SCC) with no primary found on exam and imaging. Most are hidden HPV-positive oropharyngeal cancers, and a systematic workup finds the primary in a majority.

**T-head_neck-43.physiology**

**Predictable drainage**: each mucosal site drains to specific nodal levels, so the involved level points to the likely primary. **Hiding places**: tonsillar crypts and base-of-tongue lymphoid tissue are irregular and deep, where small cancers escape visual inspection. **Nodal levels**: level II and III suggest oropharynx, larynx, or hypopharynx; level V suggests nasopharynx or skin; level IV and supraclavicular suggest below-clavicle or thyroid sources.

**T-head_neck-43.pathophysiology**

**Small primary, early nodes**: HPV-positive tumors metastasize while the primary is still tiny. **Biomarkers on the node**: p16/HPV positivity points to the oropharynx; EBV positivity points to the nasopharynx; thyroglobulin points to thyroid. **Workup logic**: PET-CT before biopsy, then examination under anesthesia with directed biopsies, palatine tonsillectomy, and lingual tonsillectomy (often by TORS) increase detection. **Why finding the primary matters**: it allows narrower radiation fields and less mucosal toxicity.

### CC-head_neck-43.1 (concept check)

Stem: A 52-year-old has a p16-positive SCC metastasis in a left level IIA node. Office exam, flexible laryngoscopy, and PET-CT show no primary. Which procedure is most likely to identify the primary tumor?

- **Correct:** Palatine and lingual tonsillectomy
- Distractor: Random nasopharyngeal biopsies alone — _why wrong:_ Nasopharyngeal primaries are EBV-associated; p16 positivity points to the oropharynx.
- Distractor: Esophagoscopy with random biopsies — _why wrong:_ Esophageal primaries do not typically present as p16-positive level II nodes.
- Distractor: Excisional biopsy of the neck node — _why wrong:_ The node has already confirmed SCC; the task now is to locate the primary.

Explanation: HPV-positive tumors hide in tonsillar crypts and lingual tonsil tissue. Palatine and lingual tonsillectomy (often by TORS) finds the primary in most p16-positive cases, allowing smaller radiation fields and less mucosal toxicity.

Pearl: p16-positive unknown primary: look in the tonsils and base of tongue.

## T-head_neck-44 — Villaret Syndrome (Retroparotid Space Syndrome)
_source: pathophys_v470/head_neck_b.py_

**T-head_neck-44.overview**

Villaret syndrome is CN IX-XII palsies plus Horner syndrome from a lesion in the retroparotid (poststyloid parapharyngeal) space. It points to tumors, infection, or trauma at the skull base.

**T-head_neck-44.physiology**

**Retrostyloid space**: contains the internal carotid artery, internal jugular vein, CN IX-XII, and the cervical sympathetic chain. **Sympathetic pathway**: third-order sympathetic fibers travel with the internal carotid to the eye and face. **Lower cranial nerves**: control swallowing, voice, shoulder elevation, and tongue movement.

**T-head_neck-44.pathophysiology**

**Combined lower cranial neuropathies**: dysphagia, hoarseness, shoulder weakness, tongue deviation toward the lesion. **Sympathetic involvement**: Horner syndrome (ptosis, miosis, anhidrosis). **Localization**: the combination localizes outside the skull base, distinguishing it from jugular foramen (Vernet) and Collet-Sicard syndromes. **Causes**: metastasis, nasopharyngeal carcinoma, paraganglioma, schwannoma, carotid dissection, and trauma.

### CC-head_neck-44.1 (concept check)

Stem: A patient has dysphagia, hoarseness, ipsilateral shoulder weakness, tongue deviation, and ipsilateral ptosis with miosis. Where is the lesion?

- **Correct:** Retrostyloid space
- Distractor: Jugular foramen — _why wrong:_ A jugular foramen lesion affects IX-XI but spares XII and the sympathetic chain.
- Distractor: Cavernous sinus — _why wrong:_ Cavernous sinus lesions affect III, IV, V, and VI.
- Distractor: Lateral medulla — _why wrong:_ Lateral medullary syndrome spares XI and XII and causes crossed sensory loss.

Explanation: The retrostyloid space contains CN IX-XII and the cervical sympathetic chain together outside the skull base, so a lesion there produces lower cranial neuropathies plus Horner syndrome.

Pearl: IX-XII plus Horner = Villaret syndrome.


---

# Thyroid / Parathyroid / Salivary

## T-thyroid-1 — Acute Sialadenitis / Sjögren
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-1.overview**

Acute suppurative sialadenitis is bacterial infection of a salivary gland, typically the parotid in dehydrated or postoperative patients. Sjögren syndrome is autoimmune exocrinopathy causing dry eyes and mouth, gland swelling, and a higher risk of MALT lymphoma.

**T-thyroid-1.physiology**

**Salivary flow is protective**: continuous flow flushes ducts and contains antimicrobial proteins (lysozyme, lactoferrin, IgA). **Parotid saliva**: serous and less bacteriostatic than mucinous saliva, making the parotid more prone to suppurative infection. **Glandular immune tolerance**: salivary epithelium normally avoids autoimmune attack.

**T-thyroid-1.pathophysiology**

**Acute suppurative parotitis**: dehydration, anticholinergics, and poor oral hygiene reduce flow, allowing retrograde ascent of S. aureus and oral flora through Stensen duct. **Pus at the duct**: massage expresses purulent saliva from the papilla. **Abscess**: the fibrous parotid fascia limits expansion, making it painful; abscesses may need drainage. **Sjögren mechanism**: lymphocytic infiltration (focal sialadenitis) and autoantibodies (anti-Ro/SSA, anti-La/SSB) destroy acinar function. **Lymphoma risk**: chronic B-cell stimulation raises MALT lymphoma risk, so persistent or asymmetric gland enlargement warrants biopsy.

### CC-thyroid-1.1 (concept check)

Stem: A 78-year-old is dehydrated 3 days after hip surgery and receiving an anticholinergic. She develops a painful, swollen parotid, and massage expresses pus from Stensen duct. What is the main predisposing mechanism?

- **Correct:** Low salivary flow permitting ascending bacteria
- Distractor: An allergic reaction to anesthetic agents — _why wrong:_ Allergy causes edema or urticaria, not purulent parotitis.
- Distractor: Viral mumps infection after surgery — _why wrong:_ Mumps causes nonsuppurative viral parotitis, usually bilateral, without pus.
- Distractor: A flare of underlying Sjögren syndrome — _why wrong:_ Sjögren causes chronic gland enlargement and dryness, not acute suppurative infection after surgery.

Explanation: Dehydration and anticholinergic drugs reduce salivary flow, letting S. aureus and oral flora ascend Stensen duct. Parotid saliva is serous and less bacteriostatic than mucinous saliva. Treatment is hydration, sialogogues, massage, and antistaphylococcal antibiotics.

Pearl: Postoperative dehydration + parotid pus = acute suppurative parotitis.

## T-thyroid-2 — Anaplastic Thyroid Cancer
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-2.overview**

Anaplastic thyroid cancer is a rapidly growing, undifferentiated cancer of older adults and one of the most lethal human malignancies. All are stage IV, and BRAF-targeted therapy has changed outcomes for BRAF-mutant tumors.

**T-thyroid-2.physiology**

**Differentiation**: normal thyroid follicular cells express thyroglobulin, TPO, and the iodide symporter. **Tumor progression**: differentiated cancers can dedifferentiate with accumulating mutations. **Airway neighbors**: the trachea, esophagus, recurrent laryngeal nerves, and great vessels surround the gland.

**T-thyroid-2.pathophysiology**

**Dedifferentiation**: TP53 and TERT promoter mutations on top of BRAF or RAS drive loss of follicular features. **Loss of iodine uptake**: RAI is useless. **Rapid local invasion**: compresses or invades the trachea, esophagus, and RLN, causing stridor, dysphagia, and hoarseness within weeks. **BRAF V600E**: present in a substantial subset; dabrafenib-trametinib produces dramatic responses and can make tumors resectable. **Airway management**: tracheostomy through tumor is difficult and may not prolong survival; goals of care are essential.

### CC-thyroid-2.1 (concept check)

Stem: A 72-year-old has a rapidly enlarging, hard thyroid mass over 3 weeks with new hoarseness and stridor. Core biopsy shows anaplastic carcinoma with a BRAF V600E mutation. Why is this mutation clinically important?

- **Correct:** It predicts BRAF/MEK response
- Distractor: It predicts excellent RAI uptake — _why wrong:_ Anaplastic tumors lose iodine uptake regardless of BRAF status.
- Distractor: It indicates a benign course — _why wrong:_ BRAF V600E does not make anaplastic carcinoma less aggressive.
- Distractor: It rules out tracheal invasion — _why wrong:_ Mutation status does not predict local invasion.

Explanation: Anaplastic carcinoma dedifferentiates (TP53, TERT) and loses iodine uptake. Dabrafenib plus trametinib produces dramatic responses in BRAF-mutant tumors and can make some resectable. Goals of care and airway planning are essential.

Pearl: Anaplastic thyroid cancer: test for BRAF immediately.

## T-thyroid-3 — Central Neck Dissection
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-3.overview**

Central neck dissection removes level VI (and often VII) nodes between the carotids, from the hyoid to the innominate artery. It is therapeutic for clinically involved nodes and prophylactic in selected thyroid cancers, at the cost of RLN and parathyroid risk.

**T-thyroid-3.physiology**

**Boundaries**: hyoid superiorly, innominate artery inferiorly, carotids laterally, prevertebral fascia posteriorly. **Contents**: prelaryngeal (Delphian), pretracheal, and paratracheal nodes. **Structures at risk**: RLN (with right-left differences in course), inferior parathyroids and their blood supply (inferior thyroid artery), and the thymus.

**T-thyroid-3.pathophysiology**

**First-echelon drainage**: papillary and medullary thyroid cancers metastasize to the central compartment first. **Prophylactic dissection**: reduces central recurrence but increases hypoparathyroidism and RLN injury, so it is selective. **Hypoparathyroidism mechanism**: devascularization of the inferior glands, which share blood supply and fat with central nodes. **Reoperation risk**: scar after previous central surgery greatly increases complications.

### CC-thyroid-3.1 (concept check)

Stem: After total thyroidectomy with bilateral central neck dissection for papillary carcinoma, a patient develops perioral tingling and a positive Chvostek sign. Why is hypocalcemia more common after central neck dissection?

- **Correct:** Inferior parathyroid blood supply is disrupted
- Distractor: The superior parathyroids are always removed — _why wrong:_ Superior glands are usually preserved; inferior glands are more at risk.
- Distractor: Central dissection removes the thymus only — _why wrong:_ Thymic removal is incidental; parathyroid devascularization causes hypocalcemia.
- Distractor: The recurrent laryngeal nerve controls calcium — _why wrong:_ The RLN has no role in calcium metabolism.

Explanation: Inferior parathyroids share fat and blood supply (inferior thyroid artery) with central nodes, so dissection devascularizes them. Postoperative PTH levels predict hypocalcemia.

Pearl: Central neck dissection trades nodal control for parathyroid risk.

## T-thyroid-4 — Completion Thyroidectomy
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-4.overview**

Completion thyroidectomy removes the remaining lobe after a lobectomy shows cancer that warrants total thyroidectomy or RAI. Timing (early or after healing) balances scar against urgency.

**T-thyroid-4.physiology**

**Thyroid remnant function**: a single lobe produces enough hormone for most patients, so lobectomy often avoids lifelong replacement. **Iodine-avid tissue**: any remaining normal thyroid concentrates radioactive iodine far more than cancer cells, so a large remnant absorbs the dose meant for metastases. **Thyroglobulin**: produced by both normal and malignant follicular cells; it is only a sensitive cancer marker once all normal thyroid is gone. **Wound healing**: the operative bed passes through inflammation in the first days to weeks and fibrosis over the following months.

**T-thyroid-4.pathophysiology**

**Indications**: high-risk pathology (extrathyroidal extension, vascular invasion, nodal disease, aggressive variants) that benefits from RAI or thyroglobulin surveillance. **RAI requirement**: RAI needs complete thyroid removal to target residual cancer. **Timing**: within days or after several months avoids peak inflammation and scarring. **Contralateral RLN and parathyroids**: the remaining side's nerve and glands are at risk; preop laryngoscopy confirms ipsilateral nerve function.

### CC-thyroid-4.1 (concept check)

Stem: Right lobectomy for a 3 cm nodule shows papillary carcinoma with extensive vascular invasion and gross extrathyroidal extension. Why is completion thyroidectomy recommended?

- **Correct:** To allow RAI and thyroglobulin surveillance
- Distractor: The left lobe always contains cancer — _why wrong:_ Multifocality is common but not universal; the reason is adjuvant therapy and surveillance.
- Distractor: It improves postoperative voice outcomes — _why wrong:_ Reoperation adds recurrent laryngeal nerve risk rather than improving voice.
- Distractor: It lowers the risk of hypocalcemia — _why wrong:_ Completion surgery increases, rather than lowers, hypocalcemia risk.

Explanation: High-risk pathology benefits from radioactive iodine and from thyroglobulin as a tumor marker, both of which require removing all normal thyroid tissue. Ipsilateral nerve function is confirmed before operating on the other side.

Pearl: High-risk DTC after lobectomy: complete the thyroidectomy.

## T-thyroid-5 — Differentiated Thyroid Cancer
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-5.overview**

Differentiated thyroid cancer (papillary and follicular, including oncocytic) is the most common endocrine cancer and usually has an excellent prognosis. Treatment is risk-adapted: lobectomy or total thyroidectomy, selective neck dissection, selective radioactive iodine, and TSH suppression.

**T-thyroid-5.physiology**

**Differentiated function**: cancer cells retain follicular functions (iodide uptake, thyroglobulin production, TSH responsiveness), which is why RAI and thyroglobulin monitoring work. **Lymphatic drainage**: central compartment (level VI) first, then lateral levels III-IV and II, and superior mediastinum. **Vascular spread**: follicular carcinoma reaches lung and bone through the blood rather than lymphatics.

**T-thyroid-5.pathophysiology**

**Papillary carcinoma**: driven by MAPK activation (BRAF V600E, RET/PTC, RAS); characteristic nuclear features (grooves, pseudoinclusions, Orphan Annie nuclei) and psammoma bodies; spreads by lymphatics, so nodal metastases are common but rarely lethal. **Follicular carcinoma**: RAS or PAX8-PPARG driven; diagnosis requires capsular or vascular invasion, so it cannot be diagnosed by FNA; spreads hematogenously. **Oncocytic (Hürthle) carcinoma**: mitochondria-rich cells that take up iodine less avidly. **Risk factors**: radiation exposure in childhood is the strongest environmental risk. **Prognostic features**: age, tumor size, extrathyroidal extension, aggressive variants (tall cell, hobnail, columnar), vascular invasion, and BRAF/TERT co-mutation. **TSH dependence**: TSH stimulates growth of residual cancer, which is the rationale for suppression in higher-risk disease.

### CC-thyroid-5.1 (concept check)

Stem: A 38-year-old has a 1.8 cm papillary thyroid carcinoma with two involved ipsilateral central neck nodes. Why does this cancer so often spread to nodes yet rarely cause death?

- **Correct:** Lymphatic spread with retained differentiation
- Distractor: Hematogenous spread with high radiosensitivity — _why wrong:_ Papillary carcinoma spreads mainly through lymphatics; hematogenous spread is typical of follicular carcinoma.
- Distractor: Nodal metastases that regress on their own — _why wrong:_ Nodal disease does not regress; it is treated surgically and sometimes with RAI.
- Distractor: Reliable cure by lobectomy in every case — _why wrong:_ Extent of surgery depends on risk; nodal disease often warrants total thyroidectomy.

Explanation: Papillary carcinoma (MAPK-driven: BRAF V600E, RET/PTC) spreads to central then lateral nodes but keeps follicular functions, so it remains TSH-responsive and often iodine-avid, contributing to excellent survival.

Pearl: Papillary = nodes; follicular = blood (lung and bone).

## T-thyroid-6 — External Branch of the Superior Laryngeal Nerve Injury
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-6.overview**

EBSLN injury during thyroidectomy weakens the cricothyroid muscle, reducing pitch range and vocal projection. It is subtle but career-changing for professional voice users.

**T-thyroid-6.physiology**

**Course**: runs with the superior thyroid artery toward the cricothyroid muscle. **Cricothyroid function**: tilts the thyroid cartilage forward, lengthening and tensing the vocal folds to raise pitch. **Cernea classification**: type 1 crosses the vessels more than 1 cm above the superior pole; type 2a within 1 cm; type 2b below the superior pole.

**T-thyroid-6.pathophysiology**

**Mechanism**: ligation or traction near the superior pole, especially Cernea type 2b. **Voice effects**: reduced pitch range, vocal fatigue, and weak projection; glottic rotation toward the paralyzed side on exam. **Prevention**: dissecting close to the thyroid capsule and ligating superior pole vessels individually. **Neuromonitoring**: stimulating the EBSLN produces cricothyroid twitch.

### CC-thyroid-6.1 (concept check)

Stem: After total thyroidectomy, a professional singer has normal vocal fold mobility on laryngoscopy but cannot reach her upper range and tires quickly. Which nerve was most likely injured?

- **Correct:** External branch of the superior laryngeal nerve
- Distractor: Recurrent laryngeal nerve — _why wrong:_ RLN injury causes vocal fold immobility and a breathy voice.
- Distractor: Internal branch of the superior laryngeal nerve — _why wrong:_ The internal branch is sensory; injury causes supraglottic numbness and aspiration risk, not pitch loss.
- Distractor: Ansa cervicalis branch to the strap muscles — _why wrong:_ Strap muscle denervation does not cause loss of upper vocal range.

Explanation: The EBSLN supplies the cricothyroid, which tilts the thyroid cartilage forward to lengthen and tense the folds and raise pitch. It runs with the superior thyroid vessels and is protected by ligating them close to the capsule.

Pearl: Lost upper range after thyroidectomy with normal mobility = EBSLN injury.

## T-thyroid-7 — Familial Hyperparathyroidism and Parathyromatosis
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-7.overview**

Familial hyperparathyroidism (MEN1, MEN2A, HPT-JT, familial isolated hyperparathyroidism) causes multigland disease and recurrence. Parathyromatosis is seeding of parathyroid tissue in the neck, usually after capsular rupture.

**T-thyroid-7.physiology**

**Tumor suppressors and oncogenes**: menin (MEN1), RET (MEN2A), and parafibromin (CDC73) regulate parathyroid growth. **Parathyroid tissue viability**: parathyroid cells survive and grow when implanted, which is the basis of autotransplantation.

**T-thyroid-7.pathophysiology**

**Multigland disease**: germline mutations affect all glands, causing asynchronous hyperplasia. **Recurrence**: remaining glands grow, so subtotal parathyroidectomy or total with autotransplant is used. **MEN1**: parathyroid, pituitary, and pancreatic tumors. **HPT-JT**: higher carcinoma risk. **Parathyromatosis**: spilled parathyroid cells implant and grow in soft tissue, causing persistent disease.

### CC-thyroid-7.1 (concept check)

Stem: A 30-year-old with MEN1 has primary hyperparathyroidism with calcium 11.4 mg/dL. Sestamibi shows one dominant gland. Why is subtotal (3.5-gland) or total parathyroidectomy with autotransplant preferred over removing the single dominant gland?

- **Correct:** Every gland carries the germline defect
- Distractor: Only one gland is usually abnormal in MEN1 — _why wrong:_ MEN1 causes asynchronous multigland hyperplasia.
- Distractor: Focused surgery cures most MEN1 patients — _why wrong:_ Focused surgery leads to high persistence and recurrence rates in MEN1.
- Distractor: MEN1 parathyroid tumors are usually malignant — _why wrong:_ Parathyroid carcinoma is rare in MEN1.

Explanation: Germline loss of menin affects every parathyroid cell, so remaining glands grow over time. Subtotal parathyroidectomy or total with autotransplant (often with transcervical thymectomy) balances recurrence against permanent hypoparathyroidism.

Pearl: MEN1 hyperparathyroidism is a multigland disease.

## T-thyroid-8 — First-Bite Syndrome
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-8.overview**

First-bite syndrome is severe parotid-region pain with the first bites of each meal after surgery involving the parapharyngeal space or deep parotid. It reflects loss of sympathetic innervation to the parotid.

**T-thyroid-8.physiology**

**Dual autonomic control**: parasympathetic fibers (via otic ganglion and auriculotemporal nerve) drive watery secretion; sympathetic fibers (from the superior cervical ganglion along the external carotid) modulate secretion and myoepithelial contraction. **Myoepithelial cells**: contract to squeeze saliva from acini. **Sympathetic chain**: lies in the poststyloid parapharyngeal space.

**T-thyroid-8.pathophysiology**

**Sympathetic denervation**: surgery damages sympathetic fibers. **Denervation hypersensitivity**: myoepithelial cells upregulate receptors and respond excessively to parasympathetic neurotransmitters. **Pain with first bites**: intense myoepithelial contraction at the start of a meal, improving with continued eating. **Treatment**: botulinum toxin to the parotid reduces contraction.

### CC-thyroid-8.1 (concept check)

Stem: After transcervical resection of a poststyloid parapharyngeal schwannoma, a patient has severe parotid-region pain with the first bites of each meal that fades as eating continues. What explains this?

- **Correct:** Sympathetic denervation of the parotid
- Distractor: Partial injury to the facial nerve trunk — _why wrong:_ Facial nerve injury causes weakness, not mealtime pain.
- Distractor: Aberrant parasympathetic regrowth to skin — _why wrong:_ That is the mechanism of Frey syndrome, which causes gustatory sweating.
- Distractor: An obstructing stone in Stensen duct — _why wrong:_ A stone causes swelling during meals, not first-bite pain after skull-base surgery.

Explanation: Sympathetic fibers from the superior cervical ganglion are injured in the poststyloid space. Denervated myoepithelial cells become hypersensitive to parasympathetic stimulation and contract intensely at meal onset. Botulinum toxin to the parotid helps.

Pearl: Pain with the first bite after parapharyngeal surgery = first-bite syndrome.

## T-thyroid-9 — Four-Gland Parathyroid Exploration
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-9.overview**

Bilateral four-gland exploration identifies all parathyroid glands and removes abnormal ones. It is required for multigland disease, MEN syndromes, discordant or negative localization, and inadequate intraoperative PTH drop.

**T-thyroid-9.physiology**

**Embryology**: superior glands from the fourth pouch (consistent location); inferior glands from the third pouch with thymus (variable, can descend into the mediastinum). **Normal glands**: about 3-5 mm, tan, 30-50 mg. **Blood supply**: mostly the inferior thyroid artery.

**T-thyroid-9.pathophysiology**

**Multigland disease**: hyperplasia or double adenomas missed by focused surgery cause persistent disease. **Ectopic locations**: inferior glands in the thymus, mediastinum, or undescended near the carotid; superior glands tracheoesophageal groove or retroesophageal. **Supernumerary glands**: present in a minority. **Intraoperative PTH**: a drop of more than 50 percent predicts cure.

### CC-thyroid-9.1 (concept check)

Stem: A 60-year-old on long-term lithium has hypercalcemia with elevated PTH. Sestamibi imaging is negative. Why is bilateral four-gland exploration favored over focused parathyroidectomy?

- **Correct:** Multigland hyperplasia is likely
- Distractor: Lithium causes parathyroid carcinoma — _why wrong:_ Lithium raises the calcium set point and is linked to multigland disease, not carcinoma.
- Distractor: Sestamibi is always falsely positive with lithium — _why wrong:_ The issue is multigland disease that localization often misses.
- Distractor: Focused surgery cannot use intraoperative PTH — _why wrong:_ Intraoperative PTH can be used with either approach.

Explanation: Lithium shifts the calcium-sensing set point and is associated with multigland hyperplasia. Negative localization also raises suspicion of multigland disease, so all glands are examined.

Pearl: Negative localization or lithium = explore all four glands.

## T-thyroid-10 — Frey Syndrome
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-10.overview**

Frey syndrome (gustatory sweating) is sweating and flushing of the cheek skin with eating after parotidectomy. It results from aberrant regeneration of parasympathetic fibers to sweat glands.

**T-thyroid-10.physiology**

**Parasympathetic secretomotor fibers**: from CN IX via the otic ganglion and auriculotemporal nerve to the parotid. **Sympathetic cholinergic fibers**: supply facial sweat glands, which use acetylcholine. **Shared transmitter**: both systems use acetylcholine at the target.

**T-thyroid-10.pathophysiology**

**Aberrant regeneration**: severed parasympathetic fibers regrow into skin sweat glands and vessels deprived of their sympathetic supply. **Gustatory sweating**: meals activate parasympathetic fibers, causing sweating and flushing. **Minor starch-iodine test**: confirms it. **Prevention**: interposing a barrier (SMAS flap, fat, or acellular dermis) blocks regrowth. **Treatment**: botulinum toxin injection.

### CC-thyroid-10.1 (concept check)

Stem: Six months after superficial parotidectomy, a patient notices sweating and flushing of the cheek skin whenever he eats. What is the mechanism?

- **Correct:** Misdirected parasympathetic fibers
- Distractor: Regenerating facial nerve motor fibers — _why wrong:_ Facial nerve fibers are motor and do not innervate sweat glands.
- Distractor: Sympathetic denervation hypersensitivity — _why wrong:_ That mechanism explains first-bite syndrome, which causes pain.
- Distractor: A salivary fistula to the skin — _why wrong:_ A fistula drains saliva through a wound, not sweat over intact skin.

Explanation: Severed auriculotemporal parasympathetic secretomotor fibers regrow into the cholinergic sweat glands and vessels of the overlying skin. The Minor starch-iodine test confirms it; botulinum toxin treats it; interposed SMAS or fat prevents it.

Pearl: Gustatory sweating after parotidectomy = Frey syndrome.

## T-thyroid-11 — Graves Disease / Toxic Goiter
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-11.overview**

Graves disease is autoimmune hyperthyroidism caused by TSH receptor-stimulating antibodies; toxic multinodular goiter and toxic adenoma are autonomous nodular causes. Treatment options are antithyroid drugs, radioactive iodine, or thyroidectomy.

**T-thyroid-11.physiology**

**TSH receptor**: G-protein coupled receptor driving thyroid hormone synthesis and growth. **Thyroid hormone effects**: increase metabolic rate, beta-adrenergic sensitivity, and heat production. **Hormone synthesis steps**: iodide trapping, organification by TPO, coupling, and release.

**T-thyroid-11.pathophysiology**

**Stimulating antibodies**: TSI mimic TSH, causing diffuse hyperplasia and hyperthyroidism independent of pituitary control. **Extrathyroidal effects**: orbital fibroblasts express TSH receptor and IGF-1 receptor, explaining thyroid eye disease; pretibial myxedema results from similar mechanisms. **Toxic nodules**: autonomous function from TSH receptor mutations. **Thyroid storm**: decompensated thyrotoxicosis triggered by surgery, infection, or iodine load. **Medication logic**: methimazole and PTU block TPO; PTU also blocks peripheral T4-to-T3 conversion; beta-blockers control symptoms. **Preoperative iodine**: SSKI reduces gland vascularity and hormone release (Wolff-Chaikoff effect).

### CC-thyroid-11.1 (concept check)

Stem: A 30-year-old with Graves disease is scheduled for total thyroidectomy. Why is potassium iodide (SSKI) given for about 10 days before surgery?

- **Correct:** It reduces gland vascularity and hormone release
- Distractor: It replaces thyroid hormone after surgery — _why wrong:_ Levothyroxine replaces hormone; SSKI is preoperative preparation.
- Distractor: It destroys the thyroid like RAI — _why wrong:_ Stable iodide is not radioactive and does not ablate the gland.
- Distractor: It prevents postoperative hypocalcemia — _why wrong:_ SSKI does not affect parathyroid function.

Explanation: High iodide doses acutely inhibit organification and hormone release (Wolff-Chaikoff effect) and reduce gland vascularity, lowering bleeding and thyroid storm risk.

Pearl: Graves surgery: euthyroid with antithyroid drugs, then SSKI.

## T-thyroid-12 — Hashimoto Thyroiditis
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-12.overview**

Hashimoto thyroiditis is chronic autoimmune thyroiditis, the most common cause of hypothyroidism in iodine-sufficient areas. It can cause goiter, and it raises the risk of thyroid lymphoma.

**T-thyroid-12.physiology**

**Central and peripheral tolerance**: thymic deletion and regulatory T cells normally prevent immune attack on thyroid antigens such as TPO and thyroglobulin. **Hormone synthesis**: TPO iodinates thyroglobulin and couples iodotyrosines to form T4 and T3. **HPT axis**: falling thyroid hormone raises TSH, which stimulates thyroid growth and function. **Iodine supply**: adequate iodine is required, but excess iodine can promote thyroid autoimmunity in susceptible people.

**T-thyroid-12.pathophysiology**

**Loss of tolerance**: genetic (HLA, CTLA-4) and environmental factors allow autoreactive T cells and B cells to target the thyroid. **Autoantibodies**: anti-TPO and anti-thyroglobulin antibodies mark the disease and correlate with lymphocytic infiltration. **Tissue destruction**: cytotoxic T cells and apoptosis destroy follicles, which are replaced by lymphoid follicles with germinal centers and oncocytic (Hürthle) cells. **Progressive hypothyroidism**: shrinking functional mass leads first to subclinical (high TSH, normal T4) then overt hypothyroidism. **Goiter**: TSH stimulation and lymphocytic infiltration enlarge the gland, often firm and lobulated. **Lymphoma risk**: chronic B-cell stimulation raises the risk of primary thyroid lymphoma.

### CC-thyroid-12.1 (concept check)

Stem: A 35-year-old woman has a firm, lobulated goiter, fatigue, weight gain, a TSH of 18 mIU/L, and strongly positive anti-TPO antibodies. What is the mechanism of her hypothyroidism?

- **Correct:** Immune destruction of thyroid follicles
- Distractor: Dietary iodine deficiency — _why wrong:_ Positive anti-TPO antibodies point to autoimmunity rather than iodine deficiency.
- Distractor: TSH-receptor stimulating antibodies — _why wrong:_ Stimulating antibodies cause Graves hyperthyroidism, not hypothyroidism.
- Distractor: Failure of pituitary TSH secretion — _why wrong:_ A high TSH indicates primary thyroid failure, not pituitary failure.

Explanation: T-cell mediated destruction and autoantibodies reduce functional thyroid mass, raising TSH, which drives goiter along with lymphocytic infiltration. Chronic lymphoid stimulation raises the risk of thyroid lymphoma.

Pearl: High TSH + anti-TPO = Hashimoto thyroiditis.

## T-thyroid-13 — Hungry Bone / Post-Thyroid Calcium Management
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-13.overview**

Post-thyroidectomy hypocalcemia usually reflects transient parathyroid dysfunction, whereas hungry bone syndrome is severe, prolonged hypocalcemia after parathyroidectomy as demineralized bone avidly takes up calcium. Anticipating, monitoring, and treating hypocalcemia prevents tetany and arrhythmia.

**T-thyroid-13.physiology**

**PTH maintains calcium**: by stimulating bone resorption, renal calcium reabsorption, and calcitriol synthesis. **Bone as a reservoir**: bone holds 99 percent of body calcium and exchanges it with blood under PTH control. **Parathyroid blood supply**: delicate branches mainly from the inferior thyroid artery, easily injured during thyroidectomy. **Neuromuscular excitability**: low ionized calcium lowers the threshold for nerve and muscle depolarization.

**T-thyroid-13.pathophysiology**

**Post-thyroidectomy hypocalcemia**: devascularization, bruising, or removal of parathyroid glands causes a sudden PTH drop; a low postoperative PTH predicts symptomatic hypocalcemia. **Hungry bone syndrome**: after removing a long-standing PTH source, osteoblastic activity outpaces resorption, so bone deposits calcium, phosphate, and magnesium rapidly. **Risk factors**: large adenomas, high preoperative PTH and alkaline phosphatase, and severe bone disease. **Symptoms**: perioral tingling, paresthesias, Chvostek and Trousseau signs, tetany, laryngospasm, seizures, and QT prolongation. **Magnesium matters**: hypomagnesemia impairs PTH secretion and action, so it must be corrected. **Treatment logic**: calcium replaces the deficit and calcitriol bypasses the missing PTH-driven renal activation.

### CC-thyroid-13.1 (concept check)

Stem: After removal of a 4 g parathyroid adenoma in a patient with osteitis fibrosa cystica, serum calcium falls to 6.8 mg/dL on day 2 despite a normal PTH. Phosphate and magnesium are also low. What explains this?

- **Correct:** Avid mineral uptake by demineralized bone
- Distractor: Inadvertent removal of all four glands — _why wrong:_ PTH is normal, so the remaining glands are functioning.
- Distractor: Vitamin D toxicity after surgery — _why wrong:_ Vitamin D toxicity causes hypercalcemia, not hypocalcemia.
- Distractor: Injury to the recurrent laryngeal nerve — _why wrong:_ RLN injury affects the voice, not calcium metabolism.

Explanation: After long-standing PTH excess is removed, osteoblastic activity outpaces resorption, so bone pulls calcium, phosphate, and magnesium from blood. Treatment is aggressive calcium, calcitriol, and magnesium replacement.

Pearl: Low calcium with normal PTH after parathyroidectomy = hungry bone syndrome.

## T-thyroid-14 — Indeterminate Thyroid Cytology / Molecular Testing
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-14.overview**

Indeterminate thyroid cytology (Bethesda III and IV) carries an intermediate risk of malignancy. Molecular testing refines risk and can spare surgery in benign-appearing molecular profiles.

**T-thyroid-14.physiology**

**What FNA samples**: a fine needle aspirates individual follicular cells and colloid; it captures nuclear and cellular features but destroys tissue architecture. **Bethesda categories**: I nondiagnostic, II benign, III atypia of undetermined significance, IV follicular neoplasm, V suspicious for malignancy, VI malignant, each with its own malignancy risk. **Follicular growth patterns**: normal thyroid and many benign nodules contain follicles of varying size; a microfollicular, crowded pattern raises concern for a follicular neoplasm. **Nuclear features of papillary carcinoma**: enlarged, overlapping nuclei with grooves, pseudoinclusions, and chromatin clearing are visible on cytology.

**T-thyroid-14.pathophysiology**

**The architecture problem**: follicular carcinoma is defined by capsular or vascular invasion, which only histology of the whole capsule can show, so a cellular follicular aspirate cannot be called benign or malignant. **Atypia (Bethesda III)**: partial or focal nuclear or architectural atypia that falls short of a diagnosis. **Driver mutations**: BRAF V600E, RET/PTC, and NTRK fusions carry very high cancer risk; RAS mutations are common in follicular adenoma, follicular carcinoma, and NIFTP alike, so they predict a neoplasm rather than cancer. **NIFTP**: a noninvasive follicular-patterned tumor with papillary-like nuclei, reclassified as a neoplasm with very low malignant potential, treated by lobectomy alone. **Molecular test logic**: rule-out tests (high negative predictive value gene expression classifiers) allow surveillance; rule-in panels with high-risk mutations support surgery and inform extent.

### CC-thyroid-14.1 (concept check)

Stem: A 3 cm thyroid nodule has Bethesda IV (follicular neoplasm) cytology. Why can FNA not distinguish follicular adenoma from follicular carcinoma?

- **Correct:** Carcinoma is defined by invasion
- Distractor: Follicular cells cannot be aspirated — _why wrong:_ Cells are easily aspirated; the problem is architecture.
- Distractor: Both have papillary nuclear features — _why wrong:_ Follicular lesions lack papillary nuclear features.
- Distractor: FNA damages the capsule — _why wrong:_ The capsule is not examined in cytology.

Explanation: Follicular carcinoma is defined by invasion of the capsule or vessels, which only histology of the whole capsule shows. Molecular testing refines risk before lobectomy.

Pearl: Follicular neoplasm on FNA: molecular testing or diagnostic lobectomy.

## T-thyroid-15 — MEN2 / RET
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-15.overview**

MEN2 is an autosomal dominant syndrome from germline RET mutations: MEN2A (medullary thyroid cancer, pheochromocytoma, primary hyperparathyroidism) and MEN2B (MTC, pheochromocytoma, mucosal neuromas, marfanoid habitus). Genetic testing drives prophylactic thyroidectomy timing.

**T-thyroid-15.physiology**

**RET receptor**: a transmembrane tyrosine kinase activated by GDNF-family ligands with a co-receptor, essential for neural crest cell migration and survival. **Neural crest derivatives**: thyroid C cells, adrenal medullary chromaffin cells, and enteric neurons all depend on RET signaling during development. **Parathyroid involvement**: the mechanism for parathyroid hyperplasia in MEN2A is less clear but tracks with specific codons. **Inheritance**: autosomal dominant, so each child of a carrier has a 50 percent risk.

**T-thyroid-15.pathophysiology**

**Activating mutations**: germline gain-of-function mutations cause constitutive kinase activity. **Codon-specific risk**: M918T (MEN2B) causes very early aggressive MTC, prompting thyroidectomy in the first year; other codons allow later surgery. **Pheochromocytoma**: must be excluded and treated first. **Hyperparathyroidism**: MEN2A only, often milder. **Hirschsprung association**: loss-of-function RET mutations; some MEN2A mutations also cause Hirschsprung disease.

### CC-thyroid-15.1 (concept check)

Stem: A 3-year-old carries the familial RET M918T mutation. Why is thyroidectomy recommended within the first year of life?

- **Correct:** This codon causes very early aggressive MTC
- Distractor: It causes papillary thyroid cancer — _why wrong:_ RET germline mutations cause medullary carcinoma.
- Distractor: It causes hyperparathyroidism in infancy — _why wrong:_ M918T (MEN2B) is not associated with hyperparathyroidism.
- Distractor: It causes thyroid storm — _why wrong:_ MTC does not cause thyrotoxicosis.

Explanation: MEN2B (M918T) causes medullary carcinoma in infancy, so prophylactic thyroidectomy is done early; other codons allow later surgery based on ATA risk. Pheochromocytoma must be excluded before surgery when age-appropriate.

Pearl: RET codon determines the timing of prophylactic thyroidectomy.

## T-thyroid-16 — Medullary Thyroid Cancer
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-16.overview**

Medullary thyroid cancer arises from calcitonin-secreting C cells; about 25 percent is hereditary through RET mutations (MEN2). It does not take up iodine, so surgery is the primary curative treatment, and calcitonin and CEA are tumor markers.

**T-thyroid-16.physiology**

**C cells**: neural crest-derived parafollicular cells concentrated in the upper two-thirds of the lobes. **Calcitonin**: lowers blood calcium by inhibiting osteoclasts, though its role in adult calcium homeostasis is minor. **RET proto-oncogene**: a receptor tyrosine kinase guiding neural crest development.

**T-thyroid-16.pathophysiology**

**RET activation**: germline (MEN2A, MEN2B) or somatic RET mutations constitutively activate the kinase, driving C-cell hyperplasia then carcinoma. **Genotype-phenotype**: specific codons predict aggressiveness and age of onset, guiding prophylactic thyroidectomy timing (ATA risk levels; M918T is highest risk). **No iodine uptake**: C cells lack the sodium-iodide symporter, so RAI and TSH suppression are ineffective. **Lymphatic spread**: early central and lateral nodal metastasis, guided by calcitonin levels. **Markers**: calcitonin and CEA track disease burden; doubling time predicts prognosis. **Pheochromocytoma**: must be excluded before surgery in MEN2. **Targeted therapy**: selective RET inhibitors (selpercatinib, pralsetinib) treat advanced disease.

### CC-thyroid-16.1 (concept check)

Stem: A 40-year-old has medullary thyroid cancer confirmed by FNA and an elevated calcitonin. Why is radioactive iodine not part of treatment?

- **Correct:** C cells do not concentrate iodine
- Distractor: MTC is too slow-growing to need adjuvant therapy — _why wrong:_ MTC can be aggressive; RAI is ineffective because C cells lack iodide transport.
- Distractor: RAI worsens hypercalcemia in MTC — _why wrong:_ RAI has no effect on calcium in MTC.
- Distractor: MTC is treated only with external radiation — _why wrong:_ Surgery is primary; RET inhibitors treat advanced disease.

Explanation: Medullary carcinoma arises from neural crest-derived C cells that lack the sodium-iodide symporter. Total thyroidectomy with central neck dissection is the main curative treatment, calcitonin and CEA track disease, and pheochromocytoma must be excluded first.

Pearl: MTC: no RAI, no TSH suppression; operate and test for RET.

## T-thyroid-17 — Parathyroid Carcinoma
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-17.overview**

Parathyroid carcinoma is a rare cause of primary hyperparathyroidism with very high calcium and PTH, a palpable firm mass, and invasion of adjacent structures. En bloc resection at first surgery offers the best chance of cure.

**T-thyroid-17.physiology**

**Chief cells**: parathyroid chief cells secrete PTH and sense calcium through the calcium-sensing receptor. **Growth control**: tumor suppressors including parafibromin (CDC73) and menin restrain parathyroid proliferation. **Gland capsule**: normal glands and adenomas are encapsulated and separate cleanly from surrounding tissue. **Set point**: in benign adenomas the calcium set point shifts modestly, so hypercalcemia is usually mild.

**T-thyroid-17.pathophysiology**

**CDC73 inactivation**: loss of parafibromin (somatic or germline in hyperparathyroidism-jaw tumor syndrome) is the dominant driver, and loss of parafibromin staining supports the diagnosis. **Profound hypercalcemia**: autonomous, high-volume PTH secretion produces calcium often above 14 mg/dL and very high PTH, with severe bone and kidney disease at presentation. **Local invasion**: a firm, gray-white mass adherent to the thyroid, RLN, and strap muscles, unlike the soft, tan, easily separated adenoma. **Histologic criteria**: invasion of vessels, perineural spaces, or adjacent tissue, or metastasis, define malignancy. **Why en bloc resection**: capsular rupture seeds tumor cells that implant and recur, so the gland is removed with the adjacent thyroid lobe and any adherent tissue. **Natural history**: morbidity and death usually come from uncontrolled hypercalcemia rather than tumor bulk, so calcimimetics are central in advanced disease.

## T-thyroid-18 — Pleomorphic Adenoma / Warthin Tumor
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-18.overview**

Pleomorphic adenoma is the most common salivary tumor, usually in the parotid tail; Warthin tumor is the second most common, often bilateral or multifocal in older smokers. Both are benign and treated by parotidectomy with facial nerve preservation, but pleomorphic adenoma recurs if enucleated and can become malignant.

**T-thyroid-18.physiology**

**Parotid structure**: a serous gland divided by the facial nerve into superficial and deep lobes, enclosed in the parotid fascia. **Intraparotid lymph nodes**: the parotid develops late and encapsulates lymph nodes, unlike other salivary glands. **Cell lineages**: ductal epithelium and myoepithelial cells interact to form glandular structures.

**T-thyroid-18.pathophysiology**

**Pleomorphic adenoma**: a mixed tumor of epithelial and myoepithelial cells in chondromyxoid stroma, driven by PLAG1 or HMGA2 rearrangements. **Pseudopods and incomplete capsule**: tumor projections extend through a thin capsule, which is why enucleation leaves tumor behind and recurrence is multinodular. **Malignant transformation**: risk rises with duration (carcinoma ex pleomorphic adenoma). **Warthin tumor**: oncocytic epithelium with lymphoid stroma arising from salivary tissue trapped in intraparotid nodes; strongly associated with smoking; hot on technetium scans because oncocytes concentrate pertechnetate. **Surgery**: superficial or partial parotidectomy with a cuff of normal tissue and facial nerve dissection.

### CC-thyroid-18.1 (concept check)

Stem: A 45-year-old had a pleomorphic adenoma of the parotid tail enucleated 8 years ago. She now has multiple small nodules in the parotid bed. Why did the tumor recur?

- **Correct:** Pseudopods left behind by enucleation
- Distractor: Malignant transformation of the original tumor — _why wrong:_ Malignant change is possible but does not explain multinodular recurrence after enucleation.
- Distractor: Seeding along the facial nerve — _why wrong:_ Recurrence comes from residual tumor in the bed, not nerve seeding.
- Distractor: New tumors arising in intraparotid nodes — _why wrong:_ Intraparotid nodes relate to Warthin tumor, not pleomorphic adenoma recurrence.

Explanation: Pleomorphic adenoma has finger-like projections through a thin, incomplete capsule. Enucleation leaves tumor behind, causing multinodular recurrence that is harder to treat. Superficial or partial parotidectomy with a cuff of normal tissue prevents it.

Pearl: Pleomorphic adenoma: never enucleate.

## T-thyroid-19 — Primary Hyperparathyroidism
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-19.overview**

Primary hyperparathyroidism is autonomous PTH overproduction, usually from a single adenoma, causing hypercalcemia with inappropriately normal or high PTH. It causes bones, stones, abdominal groans, and psychiatric moans, and parathyroidectomy is curative.

**T-thyroid-19.physiology**

**Calcium sensing**: the calcium-sensing receptor (CaSR) on chief cells detects ionized calcium and suppresses PTH release when calcium rises. **PTH actions**: increases bone resorption, increases renal calcium reabsorption and phosphate excretion, and stimulates renal 1-alpha-hydroxylase to make calcitriol, which increases intestinal calcium absorption. **Glands**: usually four parathyroids; superior glands (fourth pouch) lie posterior and deep to the RLN near the cricothyroid junction; inferior glands (third pouch, with thymus) are more variable and anterior to the RLN. **Normal feedback**: hypercalcemia from any non-parathyroid cause suppresses PTH.

**T-thyroid-19.pathophysiology**

**Single adenoma (about 85 percent)**: clonal expansion (cyclin D1/PRAD1 or MEN1 mutations) shifts the calcium set point so PTH is secreted despite high calcium. **Multigland hyperplasia (about 10-15 percent)**: more common in MEN syndromes and lithium therapy. **Carcinoma (under 1 percent)**: very high calcium and PTH, palpable mass, CDC73 mutations. **Biochemical signature**: high calcium with nonsuppressed PTH; low phosphate; high urinary calcium (unlike familial hypocalciuric hypercalcemia, where a CaSR mutation raises the set point and urine calcium is low). **End-organ effects**: bone loss (cortical, distal radius), nephrolithiasis and nephrocalcinosis, neuropsychiatric symptoms, and fatigue. **Surgical cure**: removing the autonomous gland restores normal feedback; intraoperative PTH (half-life about 3-5 minutes) confirms removal.

## T-thyroid-20 — Primary Thyroid Lymphoma
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-20.overview**

Primary thyroid lymphoma usually arises in Hashimoto thyroiditis, presenting as a rapidly enlarging neck mass in older women. MALT lymphoma may be treated with radiation alone, while diffuse large B-cell lymphoma needs chemoimmunotherapy; surgery is mainly for diagnosis.

**T-thyroid-20.physiology**

**Normal thyroid**: contains no organized lymphoid tissue, so lymphoma there almost always reflects acquired lymphoid infiltration. **Hashimoto thyroiditis**: introduces lymphocytes and germinal centers into the gland as part of chronic autoimmunity. **Germinal center biology**: B cells mutate their immunoglobulin genes and proliferate rapidly, a process prone to errors such as translocations. **Mucosa-associated lymphoid tissue (MALT)**: acquired lymphoid tissue in epithelial organs can give rise to marginal zone lymphomas.

**T-thyroid-20.pathophysiology**

**Chronic antigenic stimulation**: Hashimoto inflammation drives B-cell proliferation, eventually producing clonal lymphoma. **MALT vs DLBCL**: MALT lymphoma is indolent and localized; DLBCL is aggressive and may arise from MALT. **Rapid enlargement**: compressive symptoms (dysphagia, dyspnea) mimic anaplastic carcinoma. **Diagnosis**: core biopsy with flow cytometry. **Treatment**: R-CHOP for DLBCL; radiation for localized MALT.

### CC-thyroid-20.1 (concept check)

Stem: A 70-year-old woman with long-standing Hashimoto thyroiditis develops a rapidly enlarging goiter over 4 weeks with dysphagia. Core biopsy with flow cytometry shows diffuse large B-cell lymphoma. What is the primary treatment?

- **Correct:** R-CHOP chemoimmunotherapy
- Distractor: Total thyroidectomy with central dissection — _why wrong:_ Surgery is used mainly for diagnosis or airway; it is not primary treatment for DLBCL.
- Distractor: High-dose radioactive iodine — _why wrong:_ Lymphoma does not concentrate iodine.
- Distractor: TSH suppression with levothyroxine — _why wrong:_ TSH suppression does not treat lymphoma.

Explanation: Thyroid lymphoma arises from chronic B-cell stimulation in Hashimoto thyroiditis. DLBCL responds to chemoimmunotherapy (often with radiation); localized MALT lymphoma may be treated with radiation alone.

Pearl: Rapid goiter in Hashimoto thyroiditis: rule out lymphoma with core biopsy.

## T-thyroid-21 — Radioactive Iodine and TSH Suppression in DTC
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-21.overview**

Radioactive iodine (I-131) ablates remnant thyroid tissue and treats iodine-avid metastases in differentiated thyroid cancer, and TSH suppression reduces stimulation of residual cancer. Both are used selectively by recurrence risk.

**T-thyroid-21.physiology**

**Iodide uptake**: the sodium-iodide symporter concentrates iodine in follicular cells under TSH stimulation. **I-131 emission**: beta particles destroy cells over a few millimeters; gamma emission allows imaging. **TSH stimulation**: increases iodide uptake and thyroid cell growth.

**T-thyroid-21.pathophysiology**

**Ablation and adjuvant therapy**: destroys remnant tissue, making thyroglobulin a better marker, and treats microscopic disease. **Preparation**: elevated TSH (withdrawal or recombinant TSH) and low-iodine diet maximize uptake. **TSH suppression**: levothyroxine to suppress TSH limits growth of residual cancer; the degree depends on risk. **Side effects**: sialadenitis, xerostomia, nasolacrimal duct obstruction, and second malignancies. **Risk-adapted use**: low-risk patients often do not need RAI.

### CC-thyroid-21.1 (concept check)

Stem: Six weeks after total thyroidectomy for intermediate-risk papillary carcinoma, a patient is prepared for radioiodine by either stopping levothyroxine or receiving recombinant TSH, plus a low-iodine diet. Why?

- **Correct:** High TSH increases iodine uptake by thyroid cells
- Distractor: High TSH protects the salivary glands — _why wrong:_ TSH does not prevent radiation sialadenitis; hydration and sialogogues are used.
- Distractor: High TSH lowers serum thyroglobulin — _why wrong:_ TSH stimulation raises thyroglobulin, which is why stimulated thyroglobulin is measured.
- Distractor: High TSH prevents postoperative hypocalcemia — _why wrong:_ TSH has no role in calcium balance.

Explanation: TSH stimulates the sodium-iodide symporter in remnant and cancer cells, and a low-iodine diet empties competing iodide stores, maximizing radioiodine uptake.

Pearl: RAI needs high TSH and low iodine.

## T-thyroid-22 — Radioiodine-Refractory Differentiated Thyroid Cancer
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-22.overview**

RAI-refractory DTC no longer concentrates iodine or progresses despite it. Treatment shifts to surveillance, local therapies, and kinase inhibitors for progressive disease.

**T-thyroid-22.physiology**

**Sodium-iodide symporter (NIS)**: the basolateral transporter that concentrates iodide 20- to 40-fold in follicular cells; its expression requires TSH signaling and differentiation transcription factors (PAX8, TTF-1). **Thyroid differentiation program**: the same pathway controls thyroglobulin, TPO, and the TSH receptor. **MAPK pathway**: normally modulates growth; when overactive, it represses differentiation genes. **Glucose metabolism**: differentiated cells rely on oxidative metabolism, whereas dedifferentiated cancer cells increase glucose uptake.

**T-thyroid-22.pathophysiology**

**Dedifferentiation**: BRAF and TERT mutations and MAPK activation suppress NIS, causing loss of iodine uptake. **FDG-avidity**: PET-avid tumors are more aggressive (flip-flop phenomenon). **Kinase inhibitors**: lenvatinib and sorafenib prolong progression-free survival. **Redifferentiation**: MEK or BRAF inhibitors can restore iodine uptake in some tumors. **Targeted therapy**: RET, NTRK, and BRAF inhibitors for actionable alterations.

### CC-thyroid-22.1 (concept check)

Stem: A patient with metastatic papillary carcinoma to the lungs has rising thyroglobulin. Post-treatment scans show no radioiodine uptake in the metastases, which are intensely FDG-avid on PET. What does this pattern indicate?

- **Correct:** Loss of iodine transport
- Distractor: Likely response to a higher RAI dose — _why wrong:_ Absent uptake predicts no benefit from further radioiodine.
- Distractor: Benign inflammatory lung nodules — _why wrong:_ Rising thyroglobulin with FDG-avid nodules indicates active cancer.
- Distractor: Transformation into medullary carcinoma — _why wrong:_ Follicular-derived cancer does not convert into C-cell carcinoma.

Explanation: MAPK activation (BRAF, TERT) suppresses the sodium-iodide symporter and differentiation genes while increasing glucose metabolism, the flip-flop phenomenon. Progressive disease is treated with kinase inhibitors such as lenvatinib or targeted agents.

Pearl: PET-positive, RAI-negative = radioiodine-refractory disease.

## T-thyroid-23 — Ranula
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-23.overview**

A ranula is a mucus extravasation pseudocyst from the sublingual gland, presenting as a floor-of-mouth swelling (simple) or neck mass (plunging). Definitive treatment is excision of the sublingual gland.

**T-thyroid-23.physiology**

**Sublingual gland**: lies in the floor of mouth above the mylohyoid, secreting continuously through multiple small ducts of Rivinus or a common Bartholin duct. **Continuous mucous secretion**: unlike the submandibular gland, it secretes even without stimulation. **Mylohyoid muscle**: forms the floor of mouth diaphragm, sometimes with natural dehiscences.

**T-thyroid-23.pathophysiology**

**Extravasation**: duct injury lets mucus leak into surrounding tissue, forming a pseudocyst without an epithelial lining. **Plunging ranula**: mucus passes through or around the mylohyoid into the submandibular space, presenting as a soft neck mass. **Why marsupialization fails**: the gland keeps secreting, so recurrence is common unless the sublingual gland is removed. **Submandibular gland innocent**: the source is almost always the sublingual gland.

### CC-thyroid-23.1 (concept check)

Stem: A 20-year-old has a soft, painless submandibular neck swelling and a bluish floor-of-mouth cyst that returned after marsupialization. What is the definitive treatment?

- **Correct:** Excision of the sublingual gland
- Distractor: Submandibular gland excision — _why wrong:_ The source is almost always the sublingual gland.
- Distractor: Repeat marsupialization — _why wrong:_ Marsupialization leaves the secreting gland and recurs.
- Distractor: Antibiotic therapy — _why wrong:_ Ranula is an extravasation pseudocyst, not an infection.

Explanation: A ranula is a mucus extravasation pseudocyst from the continuously secreting sublingual gland; a plunging ranula passes through or around the mylohyoid. Removing the sublingual gland prevents recurrence.

Pearl: Ranula = remove the sublingual gland.

## T-thyroid-24 — Recurrent Laryngeal Nerve Injury During Thyroidectomy
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-24.overview**

RLN injury during thyroidectomy causes unilateral vocal fold paralysis (hoarseness, aspiration) or bilateral paralysis (stridor, airway emergency). Visual identification, knowledge of variants, and neuromonitoring reduce injury.

**T-thyroid-24.physiology**

**Course**: the right RLN loops around the subclavian artery and ascends obliquely; the left loops around the aortic arch and ascends in the tracheoesophageal groove. **Entry**: both enter the larynx under the inferior constrictor near the cricothyroid joint, close to Berry ligament. **Function**: supplies all intrinsic laryngeal muscles except the cricothyroid, plus sensation below the vocal folds. **Variants**: a nonrecurrent right laryngeal nerve occurs with an aberrant right subclavian artery; extralaryngeal branching is common.

**T-thyroid-24.pathophysiology**

**Mechanisms**: traction (most common), thermal injury from energy devices, compression, clamping, ligature, and transection. **Unilateral paralysis**: breathy voice and aspiration risk from glottic incompetence. **Bilateral paralysis**: both folds rest near midline, causing stridor and airway obstruction, often requiring reintubation or tracheostomy. **Loss of signal**: during neuromonitoring, loss of signal on the first side should prompt consideration of staging the contralateral side. **Recovery**: neurapraxia recovers over weeks to months; transection needs repair (reinnervation).

### CC-thyroid-24.1 (concept check)

Stem: During right thyroid lobectomy, the surgeon cannot find the RLN in its expected course. Preoperative CT shows an aberrant right subclavian artery. What variant should be expected?

- **Correct:** A nonrecurrent right laryngeal nerve
- Distractor: A duplicated left RLN — _why wrong:_ Duplication on the left is not related to aberrant right subclavian anatomy.
- Distractor: Absence of the right vagus — _why wrong:_ The vagus is present.
- Distractor: RLN running anterior to the trachea — _why wrong:_ The RLN does not run anterior to the trachea.

Explanation: With an aberrant right subclavian artery, there is no vessel for the nerve to loop around, so the right laryngeal nerve branches directly from the vagus in the neck. Recognizing it prevents transection.

Pearl: Aberrant right subclavian = nonrecurrent right laryngeal nerve.

## T-thyroid-25 — Reoperative Hyperparathyroidism
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-25.overview**

Reoperative parathyroid surgery treats persistent (within 6 months) or recurrent (after 6 months) hyperparathyroidism after a failed first operation. Success depends on confirming the diagnosis, precise localization, and knowing where missed glands hide.

**T-thyroid-25.physiology**

**Embryologic migration**: inferior glands descend with the thymus from the third pouch and can stop anywhere from the angle of the mandible to the mediastinum; superior glands from the fourth pouch are more constant but can slide into the tracheoesophageal groove or retroesophageal space. **Gland number**: most people have four glands, but a minority have supernumerary glands, often in the thymus. **Feedback**: normal glands are suppressed by hypercalcemia, so in persistent disease the remaining hyperfunctioning tissue is the source of PTH. **PTH kinetics**: intact PTH has a half-life of a few minutes, allowing intraoperative confirmation.

**T-thyroid-25.pathophysiology**

**Why first operations fail**: a missed ectopic adenoma, unrecognized multigland disease, a supernumerary gland, or parathyromatosis from capsular rupture. **Confirm the diagnosis first**: exclude familial hypocalciuric hypercalcemia and secondary causes such as vitamin D deficiency before reoperating. **Concordant localization**: two concordant studies (sestamibi SPECT-CT, 4D-CT, ultrasound, or venous sampling) are typically required because scar defeats exploration. **Scar risk**: reoperation raises the risk of RLN injury and permanent hypoparathyroidism, so cryopreservation of removed tissue is considered.

## T-thyroid-26 — Reoperative Thyroid Surgery
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-26.overview**

Reoperative thyroid surgery addresses recurrent or persistent disease, completion thyroidectomy, or recurrent goiter in a previously operated neck. Scar distorts planes and raises RLN and parathyroid risk, so planning and alternative approaches matter.

**T-thyroid-26.physiology**

**Virgin-neck planes**: strap muscles, thyroid capsule, and carotid sheath are separated by loose areolar tissue that dissects easily. **Nerve identification**: the RLN is usually found in the tracheoesophageal groove or at its laryngeal entry near the cricothyroid joint. **Parathyroid blood supply**: delicate end-arteries mostly from the inferior thyroid artery. **Healing after surgery**: fibroblasts lay down collagen that obliterates planes over months, gluing structures together.

**T-thyroid-26.pathophysiology**

**Scar**: obliterates planes and fixes structures, increasing RLN and parathyroid injury. **Lateral (back-door) approach**: entering between strap muscles and SCM reaches the thyroid bed through less scarred tissue. **Preoperative laryngoscopy**: identifies existing vocal fold paralysis. **Nerve monitoring**: helps identify a scarred RLN.

### CC-thyroid-26.1 (concept check)

Stem: A patient needs reoperation for recurrent papillary carcinoma in the right thyroid bed. Why do many surgeons use a lateral (back-door) approach between the strap muscles and the SCM?

- **Correct:** It enters through less scarred tissue
- Distractor: It avoids the recurrent laryngeal nerve entirely — _why wrong:_ The nerve is still at risk; the approach helps identify it in less scarred tissue.
- Distractor: It removes the need for nerve monitoring — _why wrong:_ Monitoring remains valuable in reoperative surgery.
- Distractor: It allows access to the contralateral lobe — _why wrong:_ It accesses the ipsilateral thyroid bed.

Explanation: Scar from the first operation obliterates anterior planes. Approaching laterally reaches the thyroid bed and RLN through fresher planes. Preoperative laryngoscopy documents vocal fold function.

Pearl: Reoperative neck: go around the scar, scope the cords first.

## T-thyroid-27 — Salivary Adenoid Cystic Carcinoma and Perineural Spread
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-27.overview**

Adenoid cystic carcinoma is a slow-growing, persistent salivary cancer known for perineural spread and late distant metastasis. Complete resection and adjuvant radiation along nerve paths are key, and patients need long-term follow-up.

**T-thyroid-27.physiology**

**Salivary duct units**: luminal ductal cells surrounded by myoepithelial and basal cells form the functional secretory unit. **Nerve sheaths**: the perineurium and epineurium create continuous low-resistance channels running from the gland to the skull base. **Key nerves**: the facial nerve traverses the parotid; V2 (palate, sinus) and V3 (submandibular, oral) carry minor and major salivary territories back to foramen rotundum and ovale. **Neurotrophic signaling**: nerves release growth factors that tumor cells can exploit.

**T-thyroid-27.pathophysiology**

**MYB-NFIB fusion**: a translocation that drives constitutive MYB transcription factor activity and proliferation. **Growth patterns**: cribriform (Swiss cheese), tubular, and solid patterns; the solid pattern is more aggressive. **Perineural spread**: tumor cells track along nerves, causing pain, numbness, or facial weakness, often far beyond visible margins. **Skip lesions**: discontinuous nerve involvement makes negative margins unreliable, which is why adjuvant radiation covers nerve paths to the skull base. **Late distant metastasis**: lung metastases can appear after 10 years and progress slowly, so follow-up is lifelong. **Outcome logic**: survival is long but cure rates fall over time, reflecting persistent, indolent disease.

### CC-thyroid-27.1 (concept check)

Stem: After resection of a palatal adenoid cystic carcinoma with clear margins, why is adjuvant radiation planned along the course of V2 to the skull base?

- **Correct:** Perineural spread often extends beyond margins
- Distractor: ACC is highly radiosensitive only at the primary — _why wrong:_ Radiation targets nerve pathways because of perineural spread.
- Distractor: ACC metastasizes to neck nodes early — _why wrong:_ Nodal spread is uncommon.
- Distractor: V2 is always cut during surgery — _why wrong:_ Nerve sacrifice is not the rationale.

Explanation: ACC tracks along nerves, often with skip lesions, so negative margins do not guarantee clearance. Radiation along nerve paths reduces recurrence; late lung metastases require long-term follow-up.

Pearl: ACC: think perineural spread and late lung metastases.

## T-thyroid-28 — Salivary Gland Malignancy
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-28.overview**

Salivary gland malignancies are a diverse group (mucoepidermoid, adenoid cystic, acinic cell, salivary duct carcinoma, carcinoma ex pleomorphic adenoma, and others). The smaller the gland, the higher the chance a tumor is malignant, and grade drives treatment and prognosis.

**T-thyroid-28.physiology**

**Salivary unit**: acini (serous, mucous, or mixed) drain through intercalated, striated, and excretory ducts. **Cell types**: acinar, ductal, myoepithelial, and basal cells, each giving rise to distinct tumors. **Glands**: parotid (serous), submandibular (mixed), sublingual and minor glands (mucous). **Facial nerve**: divides the parotid into superficial and deep lobes. **Saliva production**: parasympathetic stimulation (CN IX via otic ganglion for parotid; CN VII via chorda tympani and submandibular ganglion for submandibular and sublingual) drives secretion.

**T-thyroid-28.pathophysiology**

**Gland size rule**: about 20-25 percent of parotid tumors, about 50 percent of submandibular, and most sublingual and minor salivary tumors are malignant. **Mucoepidermoid carcinoma**: most common malignancy; mucous, epidermoid, and intermediate cells; MAML2 fusions; grade determines behavior. **Adenoid cystic carcinoma**: MYB-NFIB fusion; perineural spread and late lung metastasis. **Carcinoma ex pleomorphic adenoma**: malignant transformation of a long-standing benign tumor. **Salivary duct carcinoma**: aggressive, androgen receptor and HER2 positive, offering targeted therapy. **Signs of malignancy**: rapid growth, pain, facial nerve weakness, skin fixation, and nodal disease. **AJCC Version 9**: updated salivary staging, reflecting histology-specific behavior.

### CC-thyroid-28.1 (concept check)

Stem: A 58-year-old has a firm, slowly enlarging 2 cm submandibular gland mass. Why is the chance that it is malignant higher than for a parotid mass of the same size?

- **Correct:** Smaller glands have a higher malignant fraction
- Distractor: Submandibular tumors are mostly lymphomas — _why wrong:_ Lymphoma is possible, but carcinomas are the main malignant tumors of the gland.
- Distractor: The submandibular gland has no myoepithelial cells — _why wrong:_ It contains myoepithelial cells like other salivary glands.
- Distractor: Parotid masses are mostly inflammatory — _why wrong:_ Most parotid masses are benign neoplasms such as pleomorphic adenoma.

Explanation: About 20-25 percent of parotid tumors, about half of submandibular tumors, and most sublingual and minor salivary gland tumors are malignant. The smaller the gland, the higher the malignancy risk.

Pearl: The smaller the salivary gland, the more likely the tumor is malignant.

## T-thyroid-29 — Secondary / Tertiary Hyperparathyroidism
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-29.overview**

Secondary hyperparathyroidism is appropriate PTH elevation in response to low calcium or high phosphate, usually from chronic kidney disease or vitamin D deficiency. Tertiary hyperparathyroidism is autonomous PTH secretion persisting after the stimulus is corrected (often after kidney transplant).

**T-thyroid-29.physiology**

**Kidney role**: kidneys activate vitamin D (1-alpha-hydroxylation) and excrete phosphate. **FGF23**: bone-derived hormone that increases phosphate excretion and lowers calcitriol. **Parathyroid response**: low calcium, high phosphate, and low calcitriol stimulate PTH secretion and gland growth.

**T-thyroid-29.pathophysiology**

**CKD sequence**: phosphate retention and FGF23 rise reduce calcitriol, causing hypocalcemia and parathyroid stimulation. **Gland hyperplasia**: chronic stimulation causes polyclonal then monoclonal (nodular) hyperplasia of all four glands, with reduced CaSR and vitamin D receptor expression. **Tertiary disease**: autonomous nodules continue secreting after transplant, causing hypercalcemia. **Renal osteodystrophy and calciphylaxis**: bone disease and vascular calcification result from mineral imbalance. **Treatment**: phosphate binders, vitamin D analogs, and calcimimetics (cinacalcet) reduce PTH; surgery (subtotal or total with autotransplant) for refractory disease.

## T-thyroid-30 — Sialendoscopy
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-30.overview**

Sialendoscopy is endoscopic examination and treatment of salivary ducts for stones, strictures, and inflammation, preserving the gland. It has reduced the need for gland excision.

**T-thyroid-30.physiology**

**Duct anatomy**: Stensen duct (parotid) is about 5 cm long, piercing the buccinator opposite the upper second molar; Wharton duct (submandibular) is about 5 cm, running from the hilum around the mylohyoid to the sublingual papilla. **Narrowing points**: the papilla, the buccinator bend (Stensen), and the hilum are natural sites where stones and strictures occur. **Ductal epithelium**: can heal after dilation or minor injury if the gland keeps flowing. **Gland reserve**: an obstructed gland often retains secretory capacity, so restoring drainage restores function.

**T-thyroid-30.pathophysiology**

**Stones**: small mobile stones are removed with baskets; larger stones require fragmentation or combined approaches. **Strictures**: dilation treats stenoses. **Inflammation**: irrigation with steroids treats juvenile recurrent parotitis and radioiodine sialadenitis. **Gland recovery**: removing obstruction restores function.

## T-thyroid-31 — Sialolithiasis
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-31.overview**

Sialolithiasis is stone formation in salivary ducts, most often the submandibular (Wharton) duct, causing meal-related swelling and pain. Treatment ranges from conservative care to sialendoscopy and gland excision.

**T-thyroid-31.physiology**

**Saliva composition**: water, electrolytes, mucins, enzymes, and calcium phosphate near saturation. **Submandibular saliva**: more alkaline, more mucinous, and higher in calcium than parotid saliva. **Wharton duct**: long, runs upward against gravity, with an angle around the mylohyoid. **Stimulated flow**: eating triggers a large increase in saliva production.

**T-thyroid-31.pathophysiology**

**Stone formation**: stasis and alkaline, calcium-rich saliva promote precipitation of calcium phosphate around a nidus of mucus or debris. **Submandibular predominance (about 80-90 percent)**: long uphill duct, viscous and calcium-rich saliva. **Meal-related swelling**: obstructed saliva builds up when stimulated. **Infection**: stasis allows retrograde bacteria (S. aureus). **Chronic sialadenitis**: repeated obstruction causes fibrosis and gland dysfunction.

### CC-thyroid-31.1 (concept check)

Stem: A 45-year-old has recurrent painful swelling under the jaw at mealtimes. Why do salivary stones form most often in the submandibular gland?

- **Correct:** Long uphill duct with alkaline, calcium-rich saliva
- Distractor: Its saliva is mainly serous and watery — _why wrong:_ Submandibular saliva is more mucinous and viscous than parotid saliva.
- Distractor: Its duct is the shortest of the major glands — _why wrong:_ Wharton duct is long and angled, favoring stasis.
- Distractor: It lacks parasympathetic innervation — _why wrong:_ It receives parasympathetic supply via the chorda tympani and submandibular ganglion.

Explanation: Wharton duct runs upward against gravity around the mylohyoid, and submandibular saliva is more alkaline, mucinous, and calcium-rich. Stasis lets calcium phosphate precipitate around a nidus.

Pearl: Mealtime swelling = obstructive sialadenitis; look for a stone.

### CC-thyroid-31.2 (concept check)

Stem: A 50-year-old has a 4 mm mobile stone in the distal Wharton duct and a functioning submandibular gland. What is the best initial management?

- **Correct:** Gland-preserving stone removal
- Distractor: Submandibular gland excision — _why wrong:_ Excision is reserved for failed gland-preserving treatment or nonfunctioning glands.
- Distractor: Prolonged antibiotics alone — _why wrong:_ Antibiotics treat infection but do not remove the obstruction.
- Distractor: Radiation to shrink the stone — _why wrong:_ Radiation has no role in stone treatment.

Explanation: Small, mobile distal stones can be removed transorally or by sialendoscopy with baskets, preserving a gland that usually recovers once drainage is restored.

Pearl: Preserve the gland when the stone can be removed.

## T-thyroid-32 — Subacute (de Quervain) Thyroiditis
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-32.overview**

Subacute granulomatous thyroiditis is a painful, likely post-viral inflammation causing transient thyrotoxicosis followed by hypothyroidism and recovery. It is treated with NSAIDs, steroids, and beta-blockers, not antithyroid drugs.

**T-thyroid-32.physiology**

**Colloid storage**: follicles store weeks of preformed thyroid hormone bound to thyroglobulin. **Controlled release**: TSH stimulates endocytosis of colloid and proteolysis to release T4 and T3 at a regulated rate. **Iodine uptake**: functioning follicles take up iodine under TSH stimulation, the basis of the radioactive iodine uptake scan. **Capsular innervation**: the thyroid capsule is innervated, so inflammation causes neck pain radiating to the jaw and ear.

**T-thyroid-32.pathophysiology**

**Post-viral inflammation**: a granulomatous reaction, often weeks after an upper respiratory infection, destroys follicles. **Unregulated release**: ruptured follicles dump preformed hormone, causing thyrotoxicosis with suppressed TSH. **Low uptake**: damaged follicles cannot trap iodine, so the RAI uptake is very low, the key difference from Graves disease. **Inflammatory markers**: ESR and CRP are high and the gland is tender. **Hypothyroid phase**: once stores are depleted and follicles recover, transient hypothyroidism follows before most return to normal. **Treatment logic**: NSAIDs or steroids treat inflammation and beta-blockers control symptoms; antithyroid drugs are useless because no new hormone synthesis is driving the thyrotoxicosis.

### CC-thyroid-32.1 (concept check)

Stem: A 40-year-old has a painful, tender thyroid after a viral illness, with palpitations, low TSH, and low radioactive iodine uptake. Why are antithyroid drugs ineffective?

- **Correct:** Stored hormone is leaking out
- Distractor: The thyroid is producing excess hormone — _why wrong:_ Low uptake shows the gland is not synthesizing excess hormone.
- Distractor: The drugs worsen the inflammation — _why wrong:_ They do not worsen inflammation; they simply do not help.
- Distractor: TSH-stimulating antibodies are present — _why wrong:_ That describes Graves disease.

Explanation: Viral inflammation ruptures follicles and releases stored hormone. NSAIDs or steroids treat inflammation and beta-blockers control symptoms; a hypothyroid phase may follow.

Pearl: Painful thyroid + low uptake = subacute thyroiditis.

## T-thyroid-33 — Submandibular Gland Excision
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-33.overview**

Submandibular gland excision treats chronic sialadenitis, stones not amenable to sialendoscopy, and tumors. It requires protecting the marginal mandibular, lingual, and hypoglossal nerves.

**T-thyroid-33.physiology**

**Location**: in the submandibular triangle, wrapping around the posterior mylohyoid. **Nerves**: marginal mandibular (superficial, under platysma), lingual (superior, connected to the submandibular ganglion), hypoglossal (deep, inferior). **Vessels**: facial artery and vein.

**T-thyroid-33.pathophysiology**

**Chronic sialadenitis**: repeated obstruction and infection replace acini with fibrosis and lymphocytes, making the gland firm and nonfunctional; removal is indicated when sialendoscopy cannot restore drainage. **Tumors**: about half of submandibular tumors are malignant, so firmness, fixation, or nerve symptoms change the operation to an oncologic resection with neck dissection. **Marginal mandibular injury**: lower-lip weakness, avoided by elevating the fascia over the gland deep to the nerve (Hayes Martin maneuver) or ligating the facial vein low. **Lingual nerve injury**: tongue numbness from traction on the submandibular ganglion attachment. **Hypoglossal injury**: tongue weakness from dissection deep and inferior to the gland. **Inflamed planes**: fibrosis from chronic infection increases bleeding and nerve risk.

## T-thyroid-34 — Thyroid Eye Disease / Graves Ophthalmopathy
_source: pathophys_v470/thyroid_b.py_

**T-thyroid-34.overview**

Thyroid eye disease is autoimmune orbital inflammation, usually with Graves disease, causing proptosis, lid retraction, diplopia, and in severe cases optic neuropathy. It has an active inflammatory phase then a stable fibrotic phase, and teprotumumab, steroids, radiation, and decompression surgery are matched to phase and severity.

**T-thyroid-34.physiology**

**Orbital compartments**: the bony orbit contains extraocular muscles, fat, the optic nerve, and vessels in a fixed volume open only anteriorly. **Orbital fibroblasts**: express TSH receptor and IGF-1 receptor. **Glycosaminoglycans**: hydrophilic molecules that retain water when produced in excess.

**T-thyroid-34.pathophysiology**

**Shared antigen**: TSH receptor antibodies activate orbital fibroblasts through TSH receptor and IGF-1 receptor signaling. **Tissue expansion**: fibroblasts produce glycosaminoglycans, causing edema, muscle enlargement (inferior and medial rectus first), and adipogenesis. **Proptosis**: fixed bony walls force expanded tissue forward. **Optic neuropathy**: apical crowding compresses the optic nerve, causing vision loss, an emergency. **Smoking**: worsens disease and treatment response; RAI can worsen it unless covered with steroids. **Teprotumumab**: IGF-1 receptor antibody that reduces proptosis and inflammation in active disease. **Decompression**: removes orbital walls to expand space, relieving optic nerve compression.

### CC-thyroid-34.1 (concept check)

Stem: A 45-year-old smoker with Graves disease has new proptosis and intermittent diplopia. Her thyroid function is controlled with methimazole, and RAI is being considered. Why is smoking cessation especially important?

- **Correct:** Smoking worsens orbital inflammation
- Distractor: Smoking causes the hyperthyroidism itself — _why wrong:_ Smoking is a risk factor for eye disease severity, not the cause of Graves hyperthyroidism.
- Distractor: Smoking blocks the action of methimazole — _why wrong:_ Smoking does not affect antithyroid drug efficacy.
- Distractor: Smoking protects against optic neuropathy — _why wrong:_ Smoking increases the risk of severe disease, including optic neuropathy.

Explanation: Orbital fibroblasts express TSH and IGF-1 receptors. Smoking amplifies fibroblast activation and inflammation, worsens severity, increases RAI-associated flares, and reduces response to steroids and other therapy.

Pearl: Thyroid eye disease: stop smoking, and cover RAI with steroids when active.

## T-thyroid-35 — Thyroid Nodule
_source: pathophys_v470/thyroid_a.py_

**T-thyroid-35.overview**

Thyroid nodules are found by palpation in about 5 percent of adults and by ultrasound in up to two-thirds, but only about 5-10 percent are malignant. The workup (TSH, ultrasound risk stratification, selective FNA with Bethesda reporting) is designed to find the cancers without operating on the benign majority.

**T-thyroid-35.physiology**

**Follicular architecture**: the thyroid is built of follicles, spheres of follicular cells surrounding colloid rich in thyroglobulin. **Hormone synthesis**: follicular cells trap iodide via the sodium-iodide symporter, oxidize and organify it with thyroid peroxidase onto thyroglobulin, and release T4 and T3. **TSH drive**: pituitary TSH stimulates follicular cell growth and hormone synthesis through the TSH receptor; T4 and T3 feed back negatively. **C cells**: parafollicular cells scattered in the upper and middle lobes secrete calcitonin. **Ultrasound anatomy**: normal thyroid is homogeneous and slightly hyperechoic relative to strap muscles.

**T-thyroid-35.pathophysiology**

**Benign nodules**: focal follicular hyperplasia, colloid accumulation, and cyst formation from heterogeneous growth responses to TSH and growth factors. **Autonomous (hot) nodules**: activating TSH receptor or Gs-alpha mutations make follicles produce hormone independent of TSH; a low TSH prompts scintigraphy, and hot nodules are rarely malignant. **Malignant transformation**: BRAF V600E and RET/PTC rearrangements (papillary) or RAS mutations (follicular-patterned lesions) drive cancer. **Ultrasound features of malignancy**: hypoechogenicity, irregular margins, taller-than-wide shape, microcalcifications (psammoma bodies), and extrathyroidal extension reflect the cellular and stromal biology of papillary carcinoma. **Why cysts are reassuring**: purely cystic nodules contain colloid or degenerated fluid without solid neoplastic tissue. **FNA logic**: cytology reveals nuclear features of papillary carcinoma but cannot see capsular or vascular invasion, which is why follicular lesions are indeterminate.

### CC-thyroid-35.1 (concept check)

Stem: A 44-year-old has a 2.2 cm solid thyroid nodule found on a carotid ultrasound. She has mild palpitations and her TSH is 0.1 mIU/L. What is the most appropriate next step before deciding on fine-needle aspiration?

- **Correct:** Radionuclide thyroid scan
- Distractor: Ultrasound-guided FNA of the nodule — _why wrong:_ With a suppressed TSH, scintigraphy comes first because a hyperfunctioning (hot) nodule is rarely malignant and usually does not need FNA.
- Distractor: Repeat ultrasound in 12 months — _why wrong:_ Observation without assessing function skips the key branch point created by the low TSH.
- Distractor: Diagnostic hemithyroidectomy — _why wrong:_ Surgery is premature before function and, if needed, cytology have been assessed.

Explanation: A low TSH suggests an autonomous nodule driven by activating TSH-receptor or Gs-alpha mutations. Hot nodules on scintigraphy are rarely malignant, so FNA is usually unnecessary; cold nodules proceed by ultrasound risk pattern.

Pearl: Low TSH with a nodule: scan before you stick.


---

# Pediatric Otolaryngology

## T-pediatric-1 — AOM / OME / Tympanostomy Decisions
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-1.overview**

Acute otitis media (AOM) is acute middle-ear infection with a bulging drum; otitis media with effusion (OME) is middle-ear fluid without acute infection. They are the most common reasons children receive antibiotics and surgery, and guideline criteria decide observation, antibiotics, and tympanostomy tubes.

**T-pediatric-1.physiology**

**Pediatric Eustachian tube**: shorter, more horizontal, and floppier than the adult tube, with a less efficient tensor veli palatini, so it opens poorly and lets nasopharyngeal secretions reflux upward. **Middle-ear gas balance**: mucosa absorbs gas continuously; without periodic tube opening, pressure becomes negative. **Adenoids**: nasopharyngeal lymphoid tissue near the tube openings that peaks in early childhood and can harbor bacterial biofilms. **Immune maturation**: young children have immature responses to polysaccharide-encapsulated bacteria such as pneumococcus. **Hearing and language**: the first years are a sensitive period for speech and language development, which depends on consistent auditory input.

**T-pediatric-1.pathophysiology**

**AOM sequence**: a viral upper respiratory infection inflames the tube, negative pressure draws nasopharyngeal bacteria (S. pneumoniae, nontypeable H. influenzae, M. catarrhalis) into the middle ear, and pus under pressure bulges the drum. **OME**: persistent effusion after AOM or from tube dysfunction, without acute inflammation; it causes conductive loss of about 25-30 dB. **Biofilms**: bacterial biofilms in the middle ear and adenoid explain persistence and recurrence despite antibiotics. **Risk factors**: daycare, smoke exposure, bottle feeding supine, pacifier use, cleft palate, Down syndrome, and family history. **Why tubes work**: they bypass the dysfunctional tube, ventilating the middle ear and relieving effusion and recurrent infection while the tube matures. **Adenoidectomy role**: removes the infectious reservoir, reducing recurrence in children over about 4 or with repeat tube placement.

### CC-pediatric-1.1 (concept check)

Stem: A 2-year-old in daycare has had four episodes of acute otitis media in 6 months. Why is otitis media so much more common in young children than in adults?

- **Correct:** Their Eustachian tube is immature
- Distractor: Their tympanic membrane is thicker — _why wrong:_ Drum thickness does not drive otitis media; tube function does.
- Distractor: Their middle-ear mucosa lacks cilia — _why wrong:_ Middle-ear mucosa is ciliated in children.
- Distractor: Their adenoids are absent — _why wrong:_ Adenoids are large in young children and can harbor biofilm, which adds to risk.

Explanation: The pediatric Eustachian tube is shorter, more horizontal, and less rigid, with a less efficient tensor veli palatini, so it opens poorly and allows nasopharyngeal reflux. Daycare, smoke exposure, and adenoid biofilms add to risk.

Pearl: Pediatric AOM is a Eustachian tube disease.

## T-pediatric-2 — Ankyloglossia / Maxillary Frenulum
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-2.overview**

Ankyloglossia (tongue-tie) is a restrictive lingual frenulum that may impair breastfeeding. Frenotomy is indicated for documented functional problems rather than appearance.

**T-pediatric-2.physiology**

**Lingual frenulum**: a fold of mucosa and fascia connecting the tongue to the floor of mouth. **Breastfeeding mechanics**: tongue extension, elevation, and peristaltic motion create a seal and negative pressure. **Speech**: most articulation requires limited tongue tip mobility.

**T-pediatric-2.pathophysiology**

**Restricted mobility**: tight frenulum limits tongue extension and elevation, impairing latch. **Feeding consequences**: maternal nipple pain and poor infant weight gain. **Frenotomy benefit**: improves maternal pain and latch in selected infants. **Overtreatment concerns**: rising frenotomy rates without functional problems. **Maxillary frenulum**: rarely needs treatment.

## T-pediatric-3 — Branchial Cleft Anomalies
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-3.overview**

Branchial cleft anomalies are remnants of the pharyngeal apparatus forming cysts, sinuses, or fistulas, most commonly second cleft. Complete excision of the tract prevents recurrence.

**T-pediatric-3.physiology**

**Pharyngeal arches**: six paired mesodermal arches separated externally by ectodermal clefts and internally by endodermal pouches. **Second arch overgrowth**: the second arch grows caudally over the second through fourth clefts, creating the cervical sinus of His, which normally obliterates. **Arch nerves and arteries**: each arch carries a cranial nerve and artery, so a remnant tract runs between the structures of adjacent arches. **Second cleft tract course**: from the anterior SCM border, deep to platysma, between the internal and external carotids, over CN IX and XII, to the tonsillar fossa.

**T-pediatric-3.pathophysiology**

**First cleft**: near the EAC and parotid, closely related to the facial nerve. **Second cleft (most common)**: along the anterior SCM border, tract passing between the internal and external carotids to the tonsillar fossa. **Third and fourth**: tracts to the pyriform sinus, often presenting as recurrent left-sided thyroiditis or neck abscess. **Infection**: lymphoid tissue in cyst walls enlarges with respiratory infections. **Adult presentation**: a cystic lateral neck mass in an adult must be considered metastatic HPV-positive SCC until proven otherwise.

### CC-pediatric-3.1 (concept check)

Stem: A 7-year-old has a draining pit along the anterior border of the lower third of the SCM. The tract passes between the internal and external carotid arteries. Where does it end?

- **Correct:** Tonsillar fossa
- Distractor: External auditory canal — _why wrong:_ First cleft anomalies relate to the EAC and parotid.
- Distractor: Pyriform sinus — _why wrong:_ Third and fourth anomalies end in the pyriform sinus.
- Distractor: Foramen cecum — _why wrong:_ The foramen cecum relates to the thyroglossal duct.

Explanation: Second branchial cleft tracts pass deep to the second arch structures (external carotid, stylohyoid, digastric) and superficial to the third arch structures (internal carotid, CN IX), ending in the tonsillar fossa.

Pearl: Second cleft: SCM border to tonsillar fossa, between the carotids.

## T-pediatric-4 — Button Battery Ingestion
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-4.overview**

Button battery ingestion is a time-critical emergency: a battery lodged in the esophagus causes liquefactive necrosis within 2 hours. It requires emergent endoscopic removal, and honey or sucralfate may be given before arrival in selected cases.

**T-pediatric-4.physiology**

**Esophageal narrowings**: the cricopharyngeus, aortic arch crossing, left main bronchus, and lower esophageal sphincter, where objects lodge (most at the cricopharyngeus in children). **Esophageal wall**: mucosa, submucosa, and muscularis without a serosa, so injury can extend directly to neighboring structures. **Neighbors**: the trachea anteriorly, the aorta and great vessels, and recurrent laryngeal nerves in the tracheoesophageal grooves. **Tissue moisture**: the esophagus is a moist, conductive environment that completes an electrical circuit.

**T-pediatric-4.pathophysiology**

**Electrolysis**: current flows through tissue, generating hydroxide ions at the negative pole, causing alkaline liquefactive necrosis. **Speed**: injury begins within 15 minutes and is significant within 2 hours. **Negative pole injury**: the narrow side (negative pole) causes the most damage. **Complications**: perforation, tracheoesophageal fistula, aortoesophageal fistula (often delayed), and stricture. **Mitigation**: honey and sucralfate coat the battery; acetic acid irrigation neutralizes alkali at removal.

### CC-pediatric-4.1 (concept check)

Stem: A 2-year-old swallowed a coin-sized object 1 hour ago. Chest X-ray shows a round radiopaque object at the thoracic inlet with a double-ring (halo) sign. Why is endoscopic removal an emergency?

- **Correct:** Rapid alkaline necrosis of the esophagus
- Distractor: It will pass harmlessly within hours — _why wrong:_ Esophageal button batteries cause injury within 2 hours.
- Distractor: The main risk is bowel obstruction — _why wrong:_ Obstruction is not the main danger; tissue necrosis is.
- Distractor: The main risk is lead poisoning — _why wrong:_ Toxicity is not the mechanism of injury.

Explanation: The battery's current generates hydroxide at the negative pole, causing liquefactive necrosis that can perforate into the trachea or aorta. Honey or sucralfate before removal and acetic acid irrigation after may reduce injury.

Pearl: Esophageal button battery = emergency endoscopy.

## T-pediatric-5 — Choanal Atresia
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-5.overview**

Choanal atresia is congenital obstruction of the posterior nasal aperture; bilateral atresia causes neonatal respiratory distress and is an emergency. About half are associated with syndromes, especially CHARGE.

**T-pediatric-5.physiology**

**Preferential nasal breathing**: neonates breathe mainly through the nose for the first weeks because the larynx sits high and the epiglottis approximates the soft palate. **Embryology**: the bucconasal (oronasal) membrane separating the primitive nasal cavity from the mouth must rupture around week 6-7 to form the choanae. **Choanal boundaries**: vomer medially, medial pterygoid plate laterally, sphenoid body superiorly, and horizontal plate of the palatine bone inferiorly. **Feeding coordination**: infants suck and breathe through the nose simultaneously.

**T-pediatric-5.pathophysiology**

**Failed rupture**: persistence of the bucconasal membrane or abnormal mesodermal migration produces an atretic plate, most often mixed bony-membranous. **Bilateral atresia**: cyclical cyanosis relieved by crying (mouth breathing) and worsened by feeding; a McGovern nipple or oral airway bridges to surgery. **Unilateral atresia**: often missed until childhood, presenting with unilateral mucoid rhinorrhea. **Diagnosis**: inability to pass a catheter and CT showing the atretic plate and medialized lateral pterygoid wall with a thickened vomer. **CHARGE association**: coloboma, heart defects, atresia choanae, growth retardation, genital anomalies, ear anomalies (CHD7). **Restenosis**: circumferential mucosal injury causes scar, so mucosal flaps and wide posterior septectomy reduce recurrence.

### CC-pediatric-5.1 (concept check)

Stem: A newborn has episodes of cyanosis that improve when she cries and worsen during feeding. A 6 French catheter cannot be passed through either nostril. Why does crying relieve the cyanosis?

- **Correct:** Crying opens the mouth
- Distractor: Crying forces the atretic plates open — _why wrong:_ The bony or membranous plates remain closed regardless of crying.
- Distractor: Crying improves cardiac output — _why wrong:_ The problem is upper airway obstruction, not cardiac function.
- Distractor: Crying clears thick nasal mucus — _why wrong:_ The obstruction is a fixed atretic plate, not secretions.

Explanation: Neonates breathe preferentially through the nose; bilateral choanal atresia blocks airflow, so they are cyanotic at rest and while feeding until crying opens the mouth. An oral airway or McGovern nipple bridges to repair. Screen for CHARGE.

Pearl: Cyclic cyanosis relieved by crying = bilateral choanal atresia.

## T-pediatric-6 — Cleft / Craniofacial Otologic-Airway Care
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-6.overview**

Children with cleft palate and craniofacial syndromes have near-universal Eustachian tube dysfunction and frequent airway obstruction. Coordinated care addresses otitis media, hearing, and airway alongside palate repair.

**T-pediatric-6.physiology**

**Tensor veli palatini**: opens the Eustachian tube; it inserts into the palatal aponeurosis. **Levator veli palatini**: forms the palatal sling and contributes to tube function. **Airway dimensions**: depend on mandibular and midface size.

**T-pediatric-6.pathophysiology**

**Abnormal tensor insertion**: in cleft palate, the tensor inserts on the cleft margin rather than a continuous aponeurosis, impairing tube opening and causing OME in nearly all children. **Tubes**: often placed at palate repair to restore hearing during language development. **Persistent ETD after repair**: tube dysfunction can persist, with cholesteatoma risk. **Airway obstruction**: micrognathia (Pierre Robin), midface hypoplasia (Apert, Crouzon), and adenotonsillar tissue cause OSA. **Post-palatoplasty or pharyngeal flap OSA**: surgery to treat VPI narrows the airway.

### CC-pediatric-6.1 (concept check)

Stem: An infant with an unrepaired complete cleft palate has bilateral middle-ear effusions at 4 months of age. Why do nearly all infants with cleft palate develop effusions?

- **Correct:** The tensor veli palatini cannot open the tube
- Distractor: Cleft palate causes congenital cholesteatoma — _why wrong:_ Cholesteatoma is a later complication, not the cause of infant effusion.
- Distractor: Milk reflux alone fills the middle ear — _why wrong:_ Reflux may contribute, but Eustachian tube dysfunction is the main cause.
- Distractor: Hearing loss leads to fluid formation — _why wrong:_ Fluid causes hearing loss, not the reverse.

Explanation: In cleft palate, the tensor veli palatini inserts on the cleft margin rather than a continuous aponeurosis, so it cannot open the Eustachian tube. Tubes are often placed at palate repair to restore hearing during language development.

Pearl: Cleft palate = Eustachian tube dysfunction: plan for tubes.

## T-pediatric-7 — Cleft Lip / Palate — ENT Surgical Fundamentals
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-7.overview**

Cleft lip and palate result from failed fusion of facial processes and are the most common craniofacial anomalies. Repair timing targets feeding, speech, hearing, and growth.

**T-pediatric-7.physiology**

**Primary palate**: lip and premaxilla from fusion of medial nasal and maxillary processes (weeks 4-7). **Secondary palate**: palatal shelves fuse from anterior to posterior (weeks 8-12). **Levator sling**: crosses the soft palate to elevate it. **Feeding**: requires an intact palate to create suction.

**T-pediatric-7.pathophysiology**

**Failed fusion**: genetic and environmental factors (smoking, folate deficiency, anticonvulsants) disrupt fusion. **Cleft lip with or without palate vs isolated cleft palate**: distinct genetics; isolated cleft palate is more syndromic (22q11, Stickler). **Feeding difficulty**: no suction, requiring special bottles. **Speech**: levator misalignment causes VPI, so palatoplasty reorients the levator around 9-12 months. **Ear disease**: tensor dysfunction causes OME. **Submucous cleft**: bifid uvula, notch in the hard palate, and zona pellucida.

### CC-pediatric-7.1 (concept check)

Stem: An infant with an isolated cleft palate is scheduled for palatoplasty at 10 months. Why is repair timed before about 12-18 months of age?

- **Correct:** To support normal speech development
- Distractor: To restore hearing immediately — _why wrong:_ Hearing is addressed with tubes; the palate repair targets speech.
- Distractor: To allow the lip to fuse — _why wrong:_ Isolated cleft palate does not involve the lip.
- Distractor: Because palatal growth stops at 1 year — _why wrong:_ The palate continues to grow; early repair balances speech against growth.

Explanation: Repair before speech develops, with reorientation of the levator veli palatini sling, reduces velopharyngeal insufficiency and compensatory articulation. Very early repair may affect maxillary growth, so timing is balanced.

Pearl: Repair the palate before speech develops.

## T-pediatric-8 — Congenital CMV Hearing Loss
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-8.overview**

Congenital cytomegalovirus infection is the most common nongenetic cause of congenital SNHL, often progressive or delayed onset. Early detection (within 3 weeks of birth) allows antiviral therapy and close audiologic follow-up.

**T-pediatric-8.physiology**

**CMV biology**: a herpesvirus that establishes lifelong latency and reactivates intermittently. **Placental transmission**: maternal primary infection carries the highest fetal transmission risk, but reactivation or reinfection also transmits. **Fetal cochlear development**: the cochlea forms in the first trimester and matures through gestation, so timing of infection influences severity. **Inner-ear targets**: the stria vascularis, hair cells, and spiral ganglion are metabolically active and vulnerable to viral cytopathic effect and inflammation.

**T-pediatric-8.pathophysiology**

**Viral injury**: CMV infects cochlear structures (stria vascularis, hair cells, spiral ganglion), causing inflammation and cell death. **Progressive loss**: ongoing viral replication and inflammation cause progression after birth. **Asymptomatic infants**: most infected infants are asymptomatic at birth but some develop hearing loss. **Diagnosis window**: testing must occur within 21 days to distinguish congenital from postnatal infection. **Valganciclovir**: improves hearing and developmental outcomes in symptomatic infants.

### CC-pediatric-8.1 (concept check)

Stem: A newborn fails the hearing screen. CMV PCR on saliva is positive at 14 days of age. Why is testing within the first 3 weeks essential?

- **Correct:** It distinguishes congenital from postnatal infection
- Distractor: CMV becomes undetectable after 3 weeks — _why wrong:_ CMV can still be detected later; the issue is timing of acquisition.
- Distractor: Antivirals are only available in the first week — _why wrong:_ Valganciclovir is started within the first month for symptomatic infants.
- Distractor: Hearing loss always appears after 3 weeks — _why wrong:_ Hearing loss can be present at birth or develop later.

Explanation: Positive testing after 3 weeks cannot exclude postnatal acquisition. Congenital CMV is the leading nongenetic cause of SNHL, often progressive, and valganciclovir improves outcomes in symptomatic infants.

Pearl: Failed newborn screen: test for CMV within 21 days.

## T-pediatric-9 — Congenital Hearing Loss Genetics
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-9.overview**

About half of congenital hearing loss is genetic; most is nonsyndromic and autosomal recessive, led by GJB2 (connexin 26). Genetic diagnosis predicts progression, associated findings, recurrence risk, and implant outcomes.

**T-pediatric-9.physiology**

**Potassium recycling**: potassium entering hair cells during transduction is recycled back to the stria vascularis through supporting cells connected by gap junctions (connexin 26 and 30). **Hair-cell machinery**: stereocilia, tip links (cadherin 23, protocadherin 15), and myosins (VIIA) are needed for transduction. **Inheritance**: about 75-80 percent of genetic loss is autosomal recessive, about 20 percent dominant, and a small fraction X-linked or mitochondrial.

**T-pediatric-9.pathophysiology**

**GJB2**: disrupted gap junctions impair potassium recycling, causing potassium toxicity and hair cell failure; loss is usually stable and implants work well. **Pendred (SLC26A4)**: pendrin defect causes enlarged vestibular aqueduct with fluctuating, progressive loss and goiter (organification defect). **Usher syndrome**: hearing loss plus retinitis pigmentosa from ciliary protein defects. **Jervell and Lange-Nielsen**: potassium channel defect (KCNQ1, KCNE1) causes deafness and long QT, requiring ECG. **Waardenburg**: neural crest defect causing pigmentary changes and hearing loss. **Mitochondrial m.1555A>G**: aminoglycoside hypersensitivity.

## T-pediatric-10 — Congenital Neck Masses
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-10.overview**

Congenital neck masses (thyroglossal duct cysts, branchial cleft anomalies, vascular and lymphatic malformations, dermoids, teratomas) arise from embryologic remnants. Location, midline versus lateral, and imaging predict the diagnosis and the operation.

**T-pediatric-10.physiology**

**Pharyngeal apparatus**: in weeks 4-7, pharyngeal arches, clefts (ectoderm), and pouches (endoderm) form the structures of the face and neck. **Thyroid descent**: the thyroid originates at the foramen cecum and descends along the thyroglossal duct anterior to the hyoid, which normally involutes. **Cervical sinus**: the second arch overgrows the second through fourth clefts, normally obliterating them. **Lymphatic development**: lymph sacs bud from veins and connect to form the lymphatic system.

**T-pediatric-10.pathophysiology**

**Thyroglossal duct cyst**: persistent duct epithelium secretes fluid, forming a midline cyst that moves with swallowing and tongue protrusion. **Branchial anomalies**: incomplete obliteration of clefts or pouches leaves cysts, sinuses, or fistulas along the SCM border; second cleft is most common. **Lymphatic malformation**: sequestered lymphatic sacs fail to connect, producing macrocystic or microcystic masses. **Dermoid cyst**: trapped ectoderm along fusion lines contains skin adnexa. **Infection**: upper respiratory infections enlarge or infect these remnants through lymphoid tissue or tract connections.

### CC-pediatric-10.1 (concept check)

Stem: A 4-year-old has a painless midline neck mass just below the hyoid that rises when she sticks out her tongue. Which embryologic structure failed to involute?

- **Correct:** The thyroglossal duct
- Distractor: The second branchial cleft — _why wrong:_ Second cleft remnants are lateral along the SCM, not midline.
- Distractor: The cervical thymic cord — _why wrong:_ Thymic remnants are usually lateral and lower in the neck.
- Distractor: The jugular lymph sac — _why wrong:_ Lymph sac anomalies cause lymphatic malformations, usually lateral.

Explanation: The thyroid descends from the foramen cecum along the thyroglossal duct, which is attached near the hyoid. Persistent duct epithelium forms a midline cyst that moves with tongue protrusion.

Pearl: Midline mass that moves with tongue protrusion = thyroglossal duct cyst.

## T-pediatric-11 — Croup vs Epiglottitis
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-11.overview**

Croup (viral laryngotracheobronchitis) and epiglottitis (bacterial supraglottitis) both cause pediatric stridor but differ in site, cause, tempo, and management. Distinguishing them is a classic emergency skill.

**T-pediatric-11.physiology**

**Subglottis**: the narrowest part of the pediatric airway, surrounded by the complete cricoid ring. **Supraglottis**: loose areolar tissue over the epiglottis allows rapid swelling. **Airway resistance**: small radius changes greatly increase resistance.

**T-pediatric-11.pathophysiology**

**Croup**: parainfluenza virus causes subglottic edema, producing barking cough, inspiratory stridor, and hoarseness; steeple sign on AP film; treated with steroids and racemic epinephrine. **Epiglottitis**: bacterial infection (historically H. influenzae type b; now strep and staph) causes rapidly progressive supraglottic swelling, drooling, tripod posture, and toxic appearance; thumbprint sign on lateral film. **Why not examine the throat in epiglottitis**: agitation can trigger complete obstruction; airway is secured in the OR. **Hib vaccination**: dramatically reduced epiglottitis.

### CC-pediatric-11.1 (concept check)

Stem: A 2-year-old has a barking cough, hoarseness, inspiratory stridor, and a low-grade fever after 2 days of coryza. She is not drooling. An AP neck film shows a steeple sign. What is the diagnosis?

- **Correct:** Viral croup
- Distractor: Bacterial epiglottitis — _why wrong:_ Epiglottitis causes drooling, toxicity, and a thumbprint sign on lateral film.
- Distractor: Airway foreign body — _why wrong:_ A foreign body follows a choking episode and often causes unilateral findings.
- Distractor: Retropharyngeal abscess — _why wrong:_ This causes neck stiffness, drooling, and widened prevertebral tissue.

Explanation: Parainfluenza virus causes subglottic edema inside the rigid cricoid, producing barking cough and stridor; the steeple sign reflects subglottic narrowing. Dexamethasone and racemic epinephrine are the mainstays.

Pearl: Steeple sign = croup; thumbprint sign = epiglottitis.

## T-pediatric-12 — Epiglottitis
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-12.overview**

Epiglottitis is bacterial cellulitis of the supraglottis that can rapidly obstruct the airway. Now more common in adults than children due to Hib vaccination, it requires airway protection and IV antibiotics.

**T-pediatric-12.physiology**

**Supraglottic tissues**: the lingual epiglottis, aryepiglottic folds, and arytenoids have loose areolar submucosa that swells easily. **Airway inlet**: the supraglottic inlet is the entrance to the larynx; swelling here narrows the airway above the glottis. **Swallowing**: the epiglottis tilts over the inlet during swallowing, so inflammation makes swallowing very painful. **Airway reflexes**: manipulation of an inflamed supraglottis can trigger laryngospasm.

**T-pediatric-12.pathophysiology**

**Infection**: bacteria invade supraglottic tissue, causing edema. **Rapid progression**: swelling obstructs the airway over hours. **Symptoms**: severe sore throat, drooling, muffled voice, and odynophagia. **Adults**: often less dramatic, managed with observation in ICU and flexible laryngoscopy. **Children**: secure airway in controlled setting.

### CC-pediatric-12.1 (concept check)

Stem: A 50-year-old has 8 hours of severe sore throat, drooling, and a muffled voice. Oropharyngeal exam is nearly normal, and he prefers to sit upright. What is the most likely diagnosis?

- **Correct:** Adult supraglottitis
- Distractor: Peritonsillar abscess — _why wrong:_ A PTA produces a visible palatal bulge and uvular deviation.
- Distractor: Viral croup — _why wrong:_ Croup is subglottic and occurs in young children.
- Distractor: Streptococcal pharyngitis — _why wrong:_ Pharyngitis causes visible pharyngeal inflammation and rarely drooling.

Explanation: Supraglottic cellulitis swells the epiglottis and aryepiglottic folds below the view of oral exam. Flexible laryngoscopy confirms it; adults are often managed with ICU observation, while airway compromise requires a secured airway.

Pearl: Odynophagia out of proportion to the exam = scope the supraglottis.

## T-pediatric-13 — Infantile Hemangioma / PHACE Syndrome
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-13.overview**

Infantile hemangioma is the most common tumor of infancy, proliferating then involuting. PHACE syndrome accompanies large segmental facial hemangiomas, and propranolol is first-line therapy.

**T-pediatric-13.physiology**

**Vascular development**: blood vessels form by vasculogenesis and angiogenesis under VEGF and related signals. **Hemangioma progenitors**: GLUT1-positive endothelial progenitor cells, possibly of placental-like origin, proliferate after birth. **Hypoxia signaling**: hypoxia-inducible factors increase VEGF, which may initiate proliferation. **Involution biology**: endothelial apoptosis and replacement by fibrofatty tissue occur over years.

**T-pediatric-13.pathophysiology**

**Proliferation**: GLUT1-positive endothelial cells proliferate in the first months. **Involution**: years-long regression with residual fibrofatty tissue. **PHACE**: posterior fossa anomalies, hemangioma, arterial anomalies, cardiac defects, eye anomalies. **Complications**: ulceration, visual obstruction (amblyopia), and airway involvement. **Propranolol**: vasoconstriction, VEGF reduction, and apoptosis.

### CC-pediatric-13.1 (concept check)

Stem: A 6-week-old has a large segmental hemangioma over the forehead and temple that is growing rapidly. Propranolol is planned. Why is evaluation for PHACE needed first?

- **Correct:** Arterial anomalies may raise stroke risk
- Distractor: Propranolol accelerates hemangioma growth — _why wrong:_ Propranolol shrinks hemangiomas.
- Distractor: PHACE is mainly a hearing-loss syndrome — _why wrong:_ PHACE involves the brain, arteries, heart, and eyes.
- Distractor: PHACE hemangiomas always need surgery — _why wrong:_ Most are treated medically.

Explanation: PHACE includes posterior fossa anomalies, hemangioma, arterial anomalies, cardiac defects (coarctation), and eye anomalies. Narrowed cerebral arteries may increase stroke risk with beta-blockade, so MRI/MRA and echocardiography come first.

Pearl: Large segmental facial hemangioma = screen for PHACE.

## T-pediatric-14 — Juvenile Recurrent Parotitis
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-14.overview**

Juvenile recurrent parotitis is repeated nonobstructive parotid inflammation in children, usually resolving by puberty. Sialendoscopy with steroid irrigation reduces episodes.

**T-pediatric-14.physiology**

**Parotid saliva**: serous, flowing through Stensen duct. **Ductal system**: branching ducts with narrow intercalated segments. **Salivary flow and defense**: flow flushes ducts and antimicrobial proteins protect.

**T-pediatric-14.pathophysiology**

**Sialectasis**: punctate dilations of the duct system, possibly congenital ductal malformation, reduce flow. **Ascending infection and inflammation**: stasis allows retrograde infection and immune-mediated inflammation. **Episodes**: unilateral or alternating painful swelling with fever. **Rule out**: Sjögren syndrome, immunodeficiency (HIV), and stones. **Sialendoscopy**: dilation and steroid irrigation reduce inflammation and recurrence.

### CC-pediatric-14.1 (concept check)

Stem: A 6-year-old has had five episodes of painful unilateral parotid swelling with fever over 2 years. Ultrasound between episodes shows multiple small hypoechoic areas; HIV testing and Sjögren antibodies are negative. What is the typical natural history?

- **Correct:** Episodes usually stop by puberty
- Distractor: Progression to Sjögren syndrome in adulthood — _why wrong:_ Most children do not develop Sjögren syndrome; screening helps exclude it.
- Distractor: Malignant transformation of the gland — _why wrong:_ Juvenile recurrent parotitis is not premalignant.
- Distractor: Eventual need for total parotidectomy — _why wrong:_ Gland excision is rarely needed; sialendoscopy is preferred.

Explanation: Sialectasis reduces salivary flow and allows ascending inflammation. Most children outgrow it by puberty. Sialendoscopy with dilation and steroid irrigation reduces episode frequency.

Pearl: JRP improves with age; sialendoscopy reduces attacks.

## T-pediatric-15 — Laryngomalacia
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-15.overview**

Laryngomalacia is collapse of supraglottic tissues into the airway during inspiration, the most common cause of infant stridor. Most cases resolve by 12-18 months, and supraglottoplasty treats severe cases.

**T-pediatric-15.physiology**

**Infant larynx**: higher, smaller, and with a floppy omega-shaped epiglottis. **Neuromuscular tone**: maintains supraglottic structure. **Bernoulli effect**: fast airflow through a narrow segment lowers pressure, pulling soft tissue inward.

**T-pediatric-15.pathophysiology**

**Collapse**: short aryepiglottic folds, redundant arytenoid mucosa, and an omega-shaped epiglottis collapse inward on inspiration. **Neuromuscular immaturity**: impaired laryngeal sensorimotor integration reduces tone. **Inspiratory stridor**: worse with feeding, crying, and supine position. **Reflux contribution**: reflux inflames supraglottic tissues and worsens collapse. **Severe disease**: failure to thrive, apnea, and cyanosis indicate supraglottoplasty.

### CC-pediatric-15.1 (concept check)

Stem: A 6-week-old has inspiratory stridor that worsens with feeding, crying, and lying supine. She feeds well and is gaining weight along her curve. Laryngoscopy shows an omega-shaped epiglottis and short aryepiglottic folds. What is the best management?

- **Correct:** Observation with reflux precautions
- Distractor: Supraglottoplasty now — _why wrong:_ Surgery is reserved for severe disease with failure to thrive, apnea, or cyanosis.
- Distractor: Tracheostomy for airway safety — _why wrong:_ Tracheostomy is rarely needed and not indicated for mild disease.
- Distractor: Microlaryngoscopy and bronchoscopy now — _why wrong:_ Airway endoscopy is reserved for atypical or severe cases.

Explanation: Most laryngomalacia resolves by 12-18 months as laryngeal neuromuscular tone matures. Growth and feeding guide escalation; reflux management may reduce supraglottic edema.

Pearl: Laryngomalacia with good weight gain: watch and wait.

## T-pediatric-16 — Laryngotracheal Cleft
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-16.overview**

A laryngotracheal cleft is incomplete separation of the larynx and trachea from the esophagus posteriorly. It causes aspiration and is classified by depth (Benjamin-Inglis types I-IV).

**T-pediatric-16.physiology**

**Foregut separation**: the respiratory diverticulum buds from the ventral foregut around week 4, and the tracheoesophageal septum grows caudal-to-cranial to separate trachea from esophagus. **Cricoid formation**: the posterior cricoid lamina fuses in the midline, completing the cartilaginous separation at the larynx. **Interarytenoid region**: the posterior glottis between the arytenoids normally sits above an intact cricoid plate and interarytenoid muscle. **Airway protection**: glottic closure depends on an intact posterior wall to seal against the esophagus.

**T-pediatric-16.pathophysiology**

**Failed septation**: incomplete fusion of the cricoid and tracheoesophageal septum. **Aspiration**: food passes through the cleft into the airway. **Classification**: type I (interarytenoid, above vocal folds), II (into cricoid), III (through cricoid into trachea), IV (into thoracic trachea). **Diagnosis**: requires palpation of the interarytenoid area during endoscopy. **Repair**: injection or endoscopic repair for type I; open repair for deeper clefts.

### CC-pediatric-16.1 (concept check)

Stem: A 1-year-old has recurrent aspiration pneumonia and coughing with thin liquids. Flexible laryngoscopy was normal. Why is rigid endoscopy with palpation of the interarytenoid area needed?

- **Correct:** Shallow clefts hide behind redundant mucosa
- Distractor: Clefts are best seen on chest radiographs — _why wrong:_ Plain films cannot show laryngeal clefts.
- Distractor: Flexible scopes can create clefts — _why wrong:_ Flexible endoscopy does not cause clefts.
- Distractor: Palpation repairs small clefts — _why wrong:_ Palpation is diagnostic; repair is by injection or endoscopic suture.

Explanation: Type I clefts sit above the vocal folds in the interarytenoid space and are hidden by redundant mucosa. Probing during rigid endoscopy reveals them; injection or endoscopic repair improves aspiration.

Pearl: Recurrent aspiration with a normal flexible scope: palpate the interarytenoid space.

## T-pediatric-17 — Laryngotracheal Reconstruction
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-17.overview**

Laryngotracheal reconstruction (LTR) expands a stenotic pediatric airway with cartilage grafts (anterior, posterior, or both), as a single- or double-stage procedure. It is chosen for higher-grade subglottic stenosis, with cricotracheal resection reserved for severe isolated subglottic disease.

**T-pediatric-17.physiology**

**Cricoid ring**: the only complete ring in the airway, so it cannot expand on its own; widening requires dividing and grafting it. **Cartilage graft biology**: costal cartilage is avascular and survives by diffusion from the vascularized wound bed while it integrates. **Mucosal healing**: respiratory epithelium resurfaces the graft over weeks; a stent or endotracheal tube maintains shape during healing. **Glottic relationships**: the posterior cricoid plate supports the arytenoids, so posterior grafts also widen the posterior glottis. **Growth**: the pediatric airway enlarges with age, so a borderline airway may outgrow mild stenosis.

**T-pediatric-17.pathophysiology**

**Mature scar**: stenosis is collagen scar replacing mucosa and cartilage; dilation alone fails when scar is firm or the cartilage framework is deficient. **Expansion logic**: anterior grafts widen the anterior subglottis, and posterior grafts split the cricoid plate to widen posteriorly. **Restenosis drivers**: active reflux, eosinophilic esophagitis, infection, and graft failure provoke granulation and scar, so these are treated beforehand. **Single vs double stage**: single-stage uses postoperative intubation as a stent; double-stage keeps the tracheostomy with a stent for longer support. **Functional tradeoffs**: voice changes and aspiration can occur, especially with posterior grafts that alter arytenoid position.

### CC-pediatric-17.1 (concept check)

Stem: A 4-year-old with grade III subglottic stenosis undergoes laryngotracheal reconstruction with anterior and posterior costal cartilage grafts. Why is the airway stented (or kept intubated) afterward?

- **Correct:** To hold the grafts in place as mucosa heals
- Distractor: To deliver steroids into the subglottis — _why wrong:_ Stents are mechanical supports, not drug-delivery devices.
- Distractor: To prevent aspiration during healing — _why wrong:_ Stents do not protect the airway from aspiration.
- Distractor: To replace the resected cricoid — _why wrong:_ Grafts expand the cricoid; the stent only supports them during healing.

Explanation: Cartilage grafts split and expand the complete cricoid ring. Stenting maintains the expanded shape while respiratory mucosa resurfaces the grafts and they integrate; uncontrolled reflux or EoE raises restenosis risk.

Pearl: LTR: expand with grafts, hold with a stent.

## T-pediatric-18 — Lymphatic Malformation
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-18.overview**

Lymphatic malformations are slow-flow vascular malformations of abnormal lymphatic channels, classified as macrocystic, microcystic, or mixed (ISSVA). They can compromise the airway, and treatment includes sclerotherapy, surgery, and sirolimus.

**T-pediatric-18.physiology**

**Lymphatic development**: lymphatic endothelial cells bud from the cardinal veins (PROX1-driven) around weeks 6-7, forming jugular lymph sacs that connect into a network. **VEGF-C/VEGFR3 signaling**: drives lymphatic sprouting and growth. **Lymph function**: returns interstitial fluid and protein to the venous system and carries immune cells. **PI3K/AKT/mTOR pathway**: regulates endothelial cell growth and survival.

**T-pediatric-18.pathophysiology**

**Abnormal development**: somatic PIK3CA mutations activate PI3K/mTOR signaling, causing abnormal lymphatic channel growth. **Macrocystic vs microcystic**: macrocystic lesions respond to sclerotherapy; microcystic lesions infiltrate tissue. **Swelling with infection**: lymphoid inflammation enlarges lesions. **Airway compromise**: cervicofacial lesions can obstruct the airway, requiring EXIT procedures prenatally. **Sirolimus**: mTOR inhibitor that reduces lesion size.

### CC-pediatric-18.1 (concept check)

Stem: An infant has a large, soft, transilluminating left neck mass present since birth. MRI shows several large fluid-filled cysts without solid enhancement. Why is this lesion a good candidate for sclerotherapy?

- **Correct:** Large cysts accept sclerosant directly
- Distractor: It is a malignant lesion needing chemotherapy — _why wrong:_ Lymphatic malformations are benign slow-flow vascular malformations.
- Distractor: It reliably regresses without treatment — _why wrong:_ Spontaneous regression is uncommon, unlike infantile hemangioma.
- Distractor: Microcystic lesions respond better than macrocystic — _why wrong:_ Microcystic, infiltrative lesions respond poorly; macrocystic lesions respond best.

Explanation: Sclerosant injected into large cysts damages the endothelial lining so the cysts collapse and scar. Diffuse microcystic disease infiltrates tissue and responds poorly; sirolimus, which targets the PIK3CA-driven mTOR pathway, helps those lesions.

Pearl: Macrocystic = sclerotherapy; microcystic = harder, consider sirolimus.

## T-pediatric-19 — Microtia / Aural Atresia
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-19.overview**

Microtia is congenital malformation of the external ear, often with aural atresia (absent canal). Management combines early hearing rehabilitation (bone conduction) with auricular reconstruction, and atresiaplasty for favorable anatomy.

**T-pediatric-19.physiology**

**Auricle development**: six hillocks of His from the first and second branchial arches fuse during weeks 6-8. **EAC development**: the first pharyngeal cleft canalizes late (around week 28), after the auricle forms. **Separate inner ear origin**: the inner ear develops from the otic placode, so it is usually normal in microtia. **Facial nerve**: develops alongside second-arch structures and is often displaced in atresia.

**T-pediatric-19.pathophysiology**

**Arrested development**: abnormal first and second arch development produces auricle deformity, canal atresia, and ossicular malformation (fused malleus-incus). **Conductive loss**: about 50-60 dB in atresia with a normal cochlea. **Jahrsdoerfer scale**: a CT and appearance-based score (ossicles, windows, middle ear space, facial nerve, mastoid pneumatization) predicts atresiaplasty success. **Facial nerve displacement**: the nerve often runs more anterior and lateral, raising surgical risk. **Canal stenosis**: a narrow canal (under about 4 mm) carries cholesteatoma risk. **Hearing first**: bone-conduction devices in infancy support language while reconstruction waits for rib growth.

## T-pediatric-20 — Microtia Reconstruction
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-20.overview**

Microtia reconstruction builds an auricle using autologous rib cartilage (Brent, Nagata techniques) or porous polyethylene implants. Timing balances rib growth and psychosocial needs.

**T-pediatric-20.physiology**

**Rib cartilage growth**: sufficient cartilage is usually available around age 6-10. **Auricle shape**: helix, antihelix, concha, tragus, and lobule. **Skin coverage**: thin, well-vascularized temporoparietal skin is required.

**T-pediatric-20.pathophysiology**

**Autologous framework**: rib cartilage carved into a framework grows with the child and resists infection. **Staged reconstruction**: Brent (four stages) vs Nagata (two stages). **Porous polyethylene**: earlier surgery, needs temporoparietal fascia coverage, higher extrusion risk. **Chest wall deformity**: harvesting rib cartilage. **Hearing coordination**: atresiaplasty is done after framework placement to preserve skin.

## T-pediatric-21 — Nasal Dermoid Cyst
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-21.overview**

Nasal dermoid cysts are midline congenital lesions containing skin adnexa, sometimes with a tract to the skull base. Imaging excludes intracranial extension before excision.

**T-pediatric-21.physiology**

**Prenasal space**: an embryonic space between the developing nasal bones and the cartilaginous nasal capsule through which a dural projection briefly contacts the skin. **Fonticulus frontalis**: a temporary gap between the frontal and nasal bones. **Foramen cecum**: an opening anterior to the crista galli that normally closes as the dural projection regresses. **Normal regression**: the dural diverticulum withdraws and the openings close, separating skin from intracranial contents.

**T-pediatric-21.pathophysiology**

**Trapped ectoderm**: dura contacts skin through the prenasal space; incomplete regression leaves an ectodermal tract. **Midline pit with hair**: pathognomonic. **Intracranial extension**: tract through the foramen cecum. **Infection and meningitis**: tract provides a path. **Differential**: glioma and encephalocele (Furstenberg sign).

### CC-pediatric-21.1 (concept check)

Stem: A 3-year-old has a small pit on the nasal dorsum with a hair protruding from it and intermittent drainage. Why is MRI obtained before excision?

- **Correct:** To exclude intracranial extension
- Distractor: To confirm an active infection — _why wrong:_ Infection is diagnosed clinically; MRI looks for intracranial extension.
- Distractor: To plan radiation therapy — _why wrong:_ Dermoids are excised, not irradiated.
- Distractor: To distinguish it from a hemangioma — _why wrong:_ The pit with hair is characteristic; the key question is intracranial extension.

Explanation: Nasal dermoids arise from ectoderm trapped as the dural projection through the prenasal space regresses. A tract may reach the dura through the foramen cecum, requiring a combined approach and risking meningitis.

Pearl: Midline nasal pit with hair = dermoid: image before excision.

## T-pediatric-22 — Nonobstructive Pediatric Sleep Disorders
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-22.overview**

Nonobstructive pediatric sleep disorders (insomnia, parasomnias, narcolepsy, restless legs, circadian disorders) can mimic or coexist with OSA. Recognizing them prevents unnecessary surgery.

**T-pediatric-22.physiology**

**Sleep stages**: NREM (N1-N3) and REM cycle through the night; children have more slow-wave sleep. **Circadian rhythm**: controlled by the suprachiasmatic nucleus and melatonin; adolescents have a delayed phase. **Arousal systems**: hypocretin (orexin) stabilizes wakefulness.

**T-pediatric-22.pathophysiology**

**Parasomnias**: sleepwalking and night terrors arise from partial arousal out of slow-wave sleep. **Narcolepsy**: hypocretin neuron loss causes sleepiness and cataplexy. **Restless legs**: iron deficiency (low ferritin) and dopaminergic dysfunction. **Delayed sleep phase**: adolescent circadian shift. **Behavioral insomnia**: sleep-onset association and limit-setting problems.

### CC-pediatric-22.1 (concept check)

Stem: A 7-year-old has episodes 1-2 hours after falling asleep in which she sits up screaming, appears terrified, and cannot be consoled. She has no memory of them in the morning. What is the diagnosis?

- **Correct:** Sleep terrors (NREM parasomnia)
- Distractor: Nightmares — _why wrong:_ Nightmares arise from REM sleep later in the night, and children recall them.
- Distractor: Obstructive sleep apnea — _why wrong:_ OSA causes snoring and pauses; it can trigger parasomnias but is not this pattern.
- Distractor: Nocturnal frontal lobe seizures — _why wrong:_ Seizures are brief, stereotyped, and can occur at any time of night.

Explanation: Sleep terrors are partial arousals from slow-wave sleep, which dominates the first third of the night, so episodes occur early and without recall. Treating sleep deprivation or OSA can reduce them.

Pearl: Early-night terror without recall = sleep terrors.

## T-pediatric-23 — Pediatric Airway Foreign Body
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-23.overview**

Airway foreign body aspiration is most common in children 1-3 years old and causes choking, cough, wheeze, and pneumonia. Rigid bronchoscopy is the diagnostic and therapeutic standard.

**T-pediatric-23.physiology**

**Developmental behavior**: toddlers explore objects orally and lack molars to grind food. **Protective reflexes**: cough and laryngeal closure protect the airway but are immature. **Airway anatomy**: the right main bronchus is wider and more vertical in older children and adults, though in young children aspiration is more evenly distributed. **Poiseuille law**: small reductions in airway radius cause large increases in resistance.

**T-pediatric-23.pathophysiology**

**Penetration syndrome**: sudden choking and cough as the object passes the larynx, often followed by a quiet phase. **Ball-valve obstruction**: partial obstruction lets air in but not out, causing hyperinflation on expiratory films. **Stop-valve obstruction**: complete obstruction causes atelectasis. **Organic foreign bodies**: nuts swell and cause inflammation, increasing obstruction over time. **Delayed diagnosis**: recurrent pneumonia, wheeze, or bronchiectasis. **Why rigid bronchoscopy**: allows ventilation and controlled removal.

### CC-pediatric-23.1 (concept check)

Stem: A 2-year-old had a choking episode while eating peanuts 2 days ago and now has a cough and right-sided wheeze. Inspiratory chest X-ray is normal, but the expiratory film shows a hyperinflated right lung. What is the mechanism?

- **Correct:** Ball-valve bronchial obstruction
- Distractor: Complete obstruction with collapse — _why wrong:_ Complete obstruction causes atelectasis, not hyperinflation.
- Distractor: Aspiration pneumonia only — _why wrong:_ Pneumonia would not cause unilateral air trapping.
- Distractor: Tracheomalacia with collapse — _why wrong:_ Malacia does not explain sudden unilateral air trapping after choking.

Explanation: Partial obstruction lets air in during inspiration but not out during expiration, trapping air. Rigid bronchoscopy removes it; peanuts swell and inflame the airway over time.

Pearl: Choking history + unilateral air trapping = foreign body until bronchoscopy says otherwise.

## T-pediatric-24 — Pediatric Aspiration
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-24.overview**

Pediatric aspiration is entry of food, liquid, or secretions below the vocal folds, often silent in infants. Causes range from neurologic disease to structural problems (laryngeal cleft, fistula), and it drives recurrent pneumonia and chronic lung disease.

**T-pediatric-24.physiology**

**Infant swallow**: suck-swallow-breathe coordination matures over the first months; the high infant larynx gives natural airway protection. **Airway protection**: laryngeal elevation, epiglottic inversion, vocal fold closure, and the laryngeal adductor reflex protect the airway. **Laryngeal sensation**: superior laryngeal nerve afferents trigger cough and apnea to protect the airway. **Swallow phases**: oral, pharyngeal (reflexive), and esophageal.

**T-pediatric-24.pathophysiology**

**Neurologic causes**: cerebral palsy, prematurity, and brainstem anomalies impair coordination and sensation. **Structural causes**: laryngeal cleft (incomplete separation of larynx and esophagus), tracheoesophageal fistula, and vocal fold immobility. **Silent aspiration**: reduced laryngeal sensation means no cough, so clinical bedside evaluation misses it. **Lung consequences**: recurrent pneumonia, bronchiectasis, and chronic lung disease. **Evaluation**: VFSS or FEES identifies aspiration; airway endoscopy with palpation of the interarytenoid area identifies clefts. **Treatment logic**: thickening feeds, positioning, feeding therapy, treating structural causes, and gastrostomy when oral feeding is unsafe.

### CC-pediatric-24.1 (concept check)

Stem: A 1-year-old with developmental delay has had three pneumonias. She coughs rarely during feeds and a bedside feeding assessment was normal. Why is an instrumental swallow study needed?

- **Correct:** To detect silent aspiration
- Distractor: Bedside tests reliably exclude aspiration — _why wrong:_ Bedside assessments miss aspiration without cough.
- Distractor: To treat aspiration during the study — _why wrong:_ Instrumental studies diagnose and test strategies; they are not treatment.
- Distractor: To screen for gastroesophageal reflux — _why wrong:_ VFSS or FEES evaluate swallow safety, not reflux.

Explanation: Reduced laryngeal sensation means aspirated material triggers no cough. VFSS or FEES shows aspiration and tests thickened feeds and positioning; persistent aspiration also prompts evaluation for a laryngeal cleft.

Pearl: Recurrent pneumonia: look for silent aspiration.

## T-pediatric-25 — Pediatric Deep Neck Infection
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-25.overview**

Pediatric deep neck infections (retropharyngeal, parapharyngeal, peritonsillar abscesses) arise from lymph node suppuration after upper respiratory infections. Many small abscesses respond to IV antibiotics, while larger ones and airway compromise need drainage.

**T-pediatric-25.physiology**

**Retropharyngeal nodes**: prominent in young children and involute by about age 5, which explains the age distribution of retropharyngeal abscess. **Fascial spaces**: the retropharyngeal space (between buccopharyngeal and alar fascia, ending at about T2) and the danger space (behind the alar fascia, extending to the diaphragm). **Lymphatic drainage**: the nasopharynx, adenoids, sinuses, and middle ear drain to retropharyngeal nodes. **Airway size**: the small pediatric airway tolerates little edema or mass effect.

**T-pediatric-25.pathophysiology**

**Node suppuration**: a viral or bacterial upper respiratory infection inflames retropharyngeal or parapharyngeal nodes, which necrose into a phlegmon and then an abscess. **Presentation**: fever, neck stiffness or torticollis, reduced neck extension, drooling, and muffled voice; stridor is late. **Microbiology**: Group A strep, S. aureus (including MRSA), and oral anaerobes. **Phlegmon vs abscess**: CT shows ring enhancement in an abscess; smaller collections often resolve with antibiotics. **Complications**: airway obstruction, mediastinitis via the danger space, jugular thrombophlebitis (Lemierre), and carotid erosion.

### CC-pediatric-25.1 (concept check)

Stem: A 3-year-old has 3 days of fever, drooling, and refuses to extend her neck after a cold. CT shows a rim-enhancing retropharyngeal collection. Why is this infection most common before age 5?

- **Correct:** Retropharyngeal nodes are present and later involute
- Distractor: Young children lack prevertebral fascia — _why wrong:_ The fascial layers are present at all ages.
- Distractor: Young children cannot mount a fever response — _why wrong:_ Fever is common and not the explanation.
- Distractor: The danger space is absent after age 5 — _why wrong:_ The danger space persists throughout life.

Explanation: Retropharyngeal nodes drain the nasopharynx, adenoids, and sinuses and involute by about age 5. Suppuration after upper respiratory infection forms a phlegmon then abscess; large collections or airway compromise need drainage.

Pearl: Toddler with fever and refusal to extend the neck: think retropharyngeal abscess.

## T-pediatric-26 — Pediatric Head & Neck Tumors
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-26.overview**

Pediatric head and neck masses are mostly benign or inflammatory, but malignancies include lymphoma, rhabdomyosarcoma, neuroblastoma, thyroid cancer, and nasopharyngeal carcinoma. Red flags guide biopsy.

**T-pediatric-26.physiology**

**Reactive lymph nodes**: common in children with frequent infections. **Embryonal tissues**: mesenchymal and neural crest cells give rise to childhood sarcomas and neuroblastoma. **Thyroid**: more sensitive to radiation in childhood.

**T-pediatric-26.pathophysiology**

**Red flags**: supraclavicular nodes, nodes over 2-3 cm persisting, firm fixed masses, rapid growth, and B symptoms. **Lymphoma**: Hodgkin in adolescents; non-Hodgkin in younger children. **Rhabdomyosarcoma**: most common pediatric soft-tissue sarcoma, often orbit or parameningeal sites. **Pediatric thyroid cancer**: more nodal and pulmonary spread but excellent survival. **Biopsy logic**: excisional biopsy for architecture in suspected lymphoma.

### CC-pediatric-26.1 (concept check)

Stem: A 12-year-old has a firm, painless 3 cm left supraclavicular node that has persisted for 6 weeks despite antibiotics. She reports night sweats. Why is excisional biopsy recommended?

- **Correct:** Supraclavicular nodes carry high malignancy risk
- Distractor: All enlarged pediatric nodes need biopsy — _why wrong:_ Most pediatric nodes are reactive and are observed.
- Distractor: Antibiotic failure proves bacterial infection — _why wrong:_ Failure of antibiotics raises concern rather than confirming infection.
- Distractor: FNA is never performed in children — _why wrong:_ FNA can be used, but suspected lymphoma needs nodal architecture.

Explanation: Supraclavicular location, size over 2-3 cm, persistence, and B symptoms raise concern for lymphoma or metastatic disease. Excisional biopsy provides architecture for lymphoma classification.

Pearl: Supraclavicular node in a child: biopsy.

## T-pediatric-27 — Pediatric Hearing Loss Workup
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-27.overview**

Pediatric hearing loss workup identifies the type, degree, and cause of hearing loss in children, from newborn screening failures to acquired loss. Early diagnosis and intervention by 6 months optimize language outcomes.

**T-pediatric-27.physiology**

**Newborn screening**: OAE or automated ABR screening by 1 month, diagnosis by 3 months, and intervention by 6 months (1-3-6 goals). **Language development**: depends on auditory input during the critical period. **Inner ear development**: complete at birth.

**T-pediatric-27.pathophysiology**

**Genetic causes (about half)**: GJB2 (connexin 26) is the most common nonsyndromic cause; syndromic causes include Pendred, Usher, Waardenburg, Jervell and Lange-Nielsen. **Congenital CMV**: the most common nongenetic cause, often progressive. **Other acquired causes**: meningitis, ototoxicity, NICU complications, and hyperbilirubinemia. **Workup logic**: audiologic confirmation, genetic testing, CMV testing, imaging (CT or MRI), ECG for long QT (Jervell and Lange-Nielsen), and ophthalmology (Usher).

### CC-pediatric-27.1 (concept check)

Stem: An 18-month-old has newly diagnosed bilateral profound sensorineural hearing loss. Family history includes sudden cardiac death. Which test must be included in the workup?

- **Correct:** Electrocardiogram for long QT
- Distractor: Thyroid ultrasound — _why wrong:_ Thyroid evaluation is relevant to Pendred syndrome, not sudden cardiac death.
- Distractor: Renal ultrasound — _why wrong:_ Renal evaluation relates to branchio-oto-renal or Alport syndromes.
- Distractor: Ophthalmology examination only — _why wrong:_ Eye exams screen for Usher syndrome but do not address cardiac risk.

Explanation: Jervell and Lange-Nielsen syndrome (KCNQ1, KCNE1) causes congenital deafness and prolonged QT with risk of sudden death. ECG is part of the workup for severe congenital SNHL.

Pearl: Profound congenital SNHL: get an ECG.

## T-pediatric-28 — Pediatric OSA / Adenotonsillar Disease
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-28.overview**

Pediatric obstructive sleep apnea is most often caused by adenotonsillar hypertrophy and leads to behavioral, growth, and cardiovascular consequences. Adenotonsillectomy is first-line treatment for most children, with polysomnography in high-risk groups.

**T-pediatric-28.physiology**

**Upper airway patency in sleep**: during sleep, pharyngeal dilator muscle tone falls, and the collapsible pharynx narrows. **Lymphoid growth**: tonsils and adenoids enlarge relative to the airway between about 2 and 8 years. **Pediatric sleep architecture**: children spend more time in REM and slow-wave sleep, and growth hormone is secreted in slow-wave sleep. **Arousal response**: children are more likely to maintain ventilation with partial obstruction (obstructive hypoventilation) rather than discrete apneas.

**T-pediatric-28.pathophysiology**

**Mechanical obstruction**: large tonsils and adenoids narrow the pharynx so that reduced muscle tone in sleep produces collapse. **Pediatric AHI thresholds**: an obstructive AHI of 1 or more is abnormal in children, with 5-10 moderate and over 10 severe, unlike adult thresholds. **Consequences**: fragmented sleep causes inattention, hyperactivity, and learning problems; intermittent hypoxia and hypercapnia increase pulmonary pressures and can cause cor pulmonale; disrupted slow-wave sleep and increased work of breathing impair growth. **Enuresis**: increased atrial natriuretic peptide from negative intrathoracic pressure promotes nocturia. **Residual OSA**: obesity, craniofacial anomalies, Down syndrome, and severe baseline disease increase persistence after adenotonsillectomy. **Postoperative respiratory risk**: children under 3, severe OSA, and comorbidities need inpatient monitoring.

### CC-pediatric-28.1 (concept check)

Stem: A 5-year-old has loud snoring, witnessed pauses, daytime hyperactivity, and 3+ tonsils. Polysomnography shows an obstructive AHI of 6. How is this severity classified in a child?

- **Correct:** Moderate obstructive sleep apnea
- Distractor: Normal for age — _why wrong:_ In children, an obstructive AHI of 1 or more is abnormal.
- Distractor: Mild obstructive sleep apnea — _why wrong:_ Pediatric mild OSA is an AHI of 1 to under 5.
- Distractor: Severe obstructive sleep apnea — _why wrong:_ Pediatric severe OSA is an AHI over 10.

Explanation: Pediatric thresholds are much lower than adult thresholds: 1-5 mild, 5-10 moderate, over 10 severe. Adenotonsillectomy is first-line for most children with adenotonsillar hypertrophy.

Pearl: In children, an AHI of 1 is already abnormal.

## T-pediatric-29 — Pediatric Reflux / Eosinophilic Esophagitis
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-29.overview**

Pediatric reflux and eosinophilic esophagitis affect the larynx and airway, contributing to stridor, subglottic stenosis, cough, and dysphagia. They must be controlled before airway reconstruction.

**T-pediatric-29.physiology**

**Lower esophageal sphincter**: prevents reflux; transient relaxations are normal in infants. **Esophageal mucosa**: squamous epithelium resists acid poorly. **Laryngeal mucosa**: more sensitive to acid and pepsin than the esophagus.

**T-pediatric-29.pathophysiology**

**Physiologic reflux**: common in infants and resolves with growth. **Laryngopharyngeal reflux**: acid and pepsin inflame laryngeal mucosa, worsening laryngomalacia and stenosis. **EoE**: allergic, Th2-driven eosinophilic infiltration causes dysphagia, food impaction, and strictures. **Airway reconstruction failure**: uncontrolled reflux and EoE cause granulation and restenosis. **Diagnosis**: pH-impedance and endoscopic biopsy.

### CC-pediatric-29.1 (concept check)

Stem: A 5-year-old with grade III subglottic stenosis is being planned for laryngotracheal reconstruction. He has dysphagia and occasional food impaction. Why is evaluation for eosinophilic esophagitis done first?

- **Correct:** EoE promotes restenosis
- Distractor: EoE directly causes subglottic stenosis — _why wrong:_ EoE does not cause the stenosis, but it impairs healing after reconstruction.
- Distractor: EoE contraindicates general anesthesia — _why wrong:_ EoE does not prevent anesthesia.
- Distractor: EoE explains his laryngomalacia — _why wrong:_ Laryngomalacia is not described and is not caused by EoE.

Explanation: Eosinophilic esophagitis and active reflux sustain airway inflammation, causing granulation and scar after reconstruction. Controlling them first improves surgical success; biopsy confirms EoE.

Pearl: Control reflux and EoE before airway reconstruction.

## T-pediatric-30 — Pediatric Speech Disorders
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-30.overview**

Pediatric speech disorders include articulation, phonological, resonance, fluency, and voice disorders. Otolaryngologists evaluate structural, hearing, and velopharyngeal contributions.

**T-pediatric-30.physiology**

**Speech subsystems**: respiration, phonation, resonance, and articulation must coordinate. **Hearing feedback**: speech development depends on hearing. **Velopharyngeal valve**: controls oral versus nasal resonance.

**T-pediatric-30.pathophysiology**

**Hearing loss**: impairs speech acquisition. **Resonance disorders**: hypernasality (VPI) or hyponasality (adenoid hypertrophy, nasal obstruction). **Articulation errors**: structural (malocclusion, tongue) or developmental. **Childhood apraxia**: motor planning disorder. **Ankyloglossia**: rarely the cause of articulation problems.

### CC-pediatric-30.1 (concept check)

Stem: A 4-year-old has persistent mouth breathing, snoring, and speech that sounds as if he has a cold, with nasal consonants (m, n) sounding like b and d. What is the most likely cause?

- **Correct:** Adenoid hypertrophy causing hyponasality
- Distractor: Velopharyngeal insufficiency — _why wrong:_ VPI causes hypernasality and nasal air escape, not hyponasality.
- Distractor: Ankyloglossia limiting tongue movement — _why wrong:_ Tongue-tie rarely affects resonance.
- Distractor: Bilateral vocal fold nodules — _why wrong:_ Nodules cause hoarseness, not nasal resonance changes.

Explanation: Nasopharyngeal obstruction blocks nasal resonance, so nasal consonants sound oral (hyponasality). Adenoidectomy improves it, but at-risk children should be screened for velopharyngeal problems first.

Pearl: Hyponasal = obstruction; hypernasal = VPI.

## T-pediatric-31 — Pediatric Subglottic Stenosis
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-31.overview**

Pediatric subglottic stenosis is narrowing of the subglottis, congenital or acquired after intubation. Severity is graded by Myer-Cotton, and treatment ranges from observation and dilation to reconstruction.

**T-pediatric-31.physiology**

**Cricoid ring**: the only complete cartilaginous ring in the airway, so swelling inside it cannot expand outward. **Narrowest point**: in infants the subglottis is the narrowest segment, about 4-5 mm in a full-term neonate (a diameter under 4 mm is stenotic). **Mucosal perfusion**: capillary perfusion pressure is roughly 25-35 mm Hg, so endotracheal tube cuff or tube pressure above this causes ischemia. **Airway resistance**: in laminar flow resistance varies inversely with radius to the fourth power, so 1 mm of edema in a 4 mm airway reduces cross-sectional area by about 75 percent.

**T-pediatric-31.pathophysiology**

**Congenital**: incomplete canalization of the cricoid. **Acquired**: endotracheal tube pressure causes mucosal ischemia, ulceration, perichondritis, and scar. **Myer-Cotton grading**: I (0-50 percent), II (51-70), III (71-99), IV (no lumen). **Poiseuille physics**: 1 mm of edema reduces the infant subglottic area dramatically.

### CC-pediatric-31.1 (concept check)

Stem: A 2-year-old intubated for 3 weeks as a premature neonate has biphasic stridor. Endoscopy shows 60 percent subglottic narrowing. Why does the subglottis narrow after prolonged intubation?

- **Correct:** Tube pressure ischemia and scar
- Distractor: The cricoid cartilage regrows abnormally — _why wrong:_ Narrowing results from scar, not cartilage overgrowth.
- Distractor: Reflux alone causes stenosis — _why wrong:_ Reflux contributes but is not the main mechanism.
- Distractor: Viral infection after extubation — _why wrong:_ Infection does not cause fixed scar.

Explanation: The cricoid is a complete ring, so pressure from the tube causes mucosal ischemia, ulceration, perichondritis, and scar. Myer-Cotton grade II (51-70 percent) may respond to endoscopic treatment.

Pearl: Neonatal intubation + biphasic stridor = subglottic stenosis.

## T-pediatric-32 — Pediatric Tracheostomy / Decannulation
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-32.overview**

Pediatric tracheostomy is performed for airway obstruction, prolonged ventilation, or pulmonary toilet. Decannulation requires resolution of the underlying need and a patent upper airway.

**T-pediatric-32.physiology**

**Pediatric trachea**: small, soft, mobile, and difficult to palpate; small tube lumens obstruct easily. **Upper airway functions bypassed**: humidification, filtering, voice, and effective cough (requires glottic closure). **Speech and language**: airflow through the larynx is needed for vocalization during the language-learning period. **Stoma maturation**: the tract takes about a week to mature, which is why stay sutures and first tube change timing matter.

**T-pediatric-32.pathophysiology**

**Life-threatening events**: accidental decannulation and mucus plugging cause most deaths, especially in small tubes; humidification and caregiver training reduce them. **Suprastomal collapse and granulation**: anterior wall collapse and granulomas obstruct the airway above the stoma, which matters at decannulation. **Speaking valve**: a one-way valve redirects expired air through the larynx, restoring voice and improving swallowing. **Decannulation readiness**: airway endoscopy, successful capping trials, and sometimes polysomnography confirm a safe airway. **Persistent tracheocutaneous fistula**: may require closure after long-term tracheostomy.

### CC-pediatric-32.1 (concept check)

Stem: A 2-year-old with a 3.5 mm tracheostomy tube has sudden respiratory distress at home. The caregiver cannot pass a suction catheter through the tube. What is the most likely cause and response?

- **Correct:** Mucus plug: change the tube immediately
- Distractor: Bronchospasm: give an inhaler first — _why wrong:_ Inability to pass a catheter indicates tube obstruction, not bronchospasm.
- Distractor: Tube cuff overinflation: deflate the cuff — _why wrong:_ Most pediatric tubes are uncuffed, and the catheter test points to an occluded lumen.
- Distractor: Tracheal stenosis: wait for EMS — _why wrong:_ Delay is dangerous; changing the tube restores the airway.

Explanation: Small lumens plug quickly, especially without humidification. If a suction catheter will not pass, the tube is obstructed and must be changed at once. Plugging and accidental decannulation cause most tracheostomy deaths.

Pearl: Can't pass suction = change the tube now.

## T-pediatric-33 — Pediatric Vestibular Disorders
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-33.overview**

Pediatric vestibular disorders (vestibular migraine, benign paroxysmal vertigo of childhood, vestibular neuritis, and vestibular loss with hearing loss) are underrecognized. Vestibular loss delays motor milestones and accompanies many forms of SNHL.

**T-pediatric-33.physiology**

**Vestibular maturation**: vestibular function supports head control, sitting, and walking. **Shared development**: cochlea and vestibule develop together. **Visual-vestibular integration**: matures during childhood.

**T-pediatric-33.pathophysiology**

**Benign paroxysmal vertigo of childhood**: a migraine precursor causing brief vertigo attacks in toddlers. **Vestibular loss**: associated with SNHL (CMV, meningitis, malformations), causing delayed walking. **Vestibular migraine**: most common cause of vertigo in older children. **Central causes**: posterior fossa tumors must be excluded. **Rehabilitation**: promotes compensation.

### CC-pediatric-33.1 (concept check)

Stem: A 3-year-old has sudden brief episodes in which she cries, clings to her parent, and seems unsteady for a few minutes, then returns to normal. Hearing is normal and her mother has migraine. What is the most likely diagnosis?

- **Correct:** Benign paroxysmal vertigo of childhood
- Distractor: Benign paroxysmal positional vertigo — _why wrong:_ BPPV is rare in toddlers and is triggered by head position.
- Distractor: Ménière disease — _why wrong:_ Ménière disease is rare in young children and causes fluctuating hearing loss.
- Distractor: Viral labyrinthitis — _why wrong:_ Labyrinthitis causes prolonged vertigo with hearing loss.

Explanation: Benign paroxysmal vertigo of childhood is a migraine precursor with brief spontaneous attacks and normal hearing and exam between episodes. It usually resolves and may later evolve into migraine.

Pearl: Toddler vertigo attacks + family migraine = benign paroxysmal vertigo of childhood.

## T-pediatric-34 — Pediatric Vocal Fold Immobility
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-34.overview**

Pediatric vocal fold immobility is the second most common cause of neonatal stridor. Unilateral immobility is often iatrogenic after cardiac surgery, and bilateral immobility is often neurologic, classically Chiari malformation.

**T-pediatric-34.physiology**

**Nucleus ambiguus**: the brainstem motor nucleus for the larynx, vulnerable to pressure from hindbrain herniation or hydrocephalus. **Left RLN course**: loops under the aortic arch beside the ductus arteriosus, exposing it during PDA ligation and arch surgery. **Glottic airway**: in infants the glottis is a major portion of total airway resistance. **Abduction and adduction**: posterior cricoarytenoid is the only abductor; other intrinsic muscles adduct.

**T-pediatric-34.pathophysiology**

**Unilateral immobility**: left RLN injury causes weak cry, feeding difficulty, and aspiration, with a usually adequate airway. **Bilateral immobility**: brainstem compression (Arnold-Chiari, hydrocephalus) or birth injury leaves folds near midline, causing inspiratory stridor with a good cry. **Neurologic evaluation**: MRI of the brain and brainstem is required for bilateral immobility; shunting or decompression can restore motion. **Airway vs voice tradeoff**: severe bilateral immobility often needs tracheostomy or glottic widening. **Recovery**: many children recover function within the first 1-2 years, so irreversible procedures are delayed.

### CC-pediatric-34.1 (concept check)

Stem: An infant with a lumbar myelomeningocele has new inspiratory stridor with a normal cry. Laryngoscopy shows both vocal folds resting near midline. What is the most likely cause?

- **Correct:** Chiari brainstem compression
- Distractor: Left RLN injury from cardiac surgery — _why wrong:_ Iatrogenic RLN injury is usually unilateral and causes a weak cry.
- Distractor: Severe laryngomalacia — _why wrong:_ Laryngomalacia causes supraglottic collapse with mobile vocal folds.
- Distractor: Congenital subglottic stenosis — _why wrong:_ Subglottic stenosis narrows below the glottis with mobile folds.

Explanation: Arnold-Chiari malformation and hydrocephalus compress the nucleus ambiguus, leaving both folds paramedian. MRI and neurosurgical decompression or shunting may restore motion; tracheostomy may be needed meanwhile.

Pearl: Bilateral vocal fold immobility in an infant: image the brain.

## T-pediatric-35 — Pierre Robin Sequence
_source: pathophys_v470/pediatric_c.py_

**T-pediatric-35.overview**

Pierre Robin sequence is micrognathia leading to glossoptosis and airway obstruction, often with a U-shaped cleft palate. Management escalates from positioning to nasopharyngeal airway, tongue-lip adhesion, mandibular distraction, or tracheostomy.

**T-pediatric-35.physiology**

**Mandibular growth**: the mandible grows rapidly in late gestation and early infancy, and catch-up growth occurs in many infants. **Tongue position**: the genioglossus attaches to the mandible, so mandibular length determines how far forward the tongue base sits. **Palatal shelf elevation**: palatal shelves rise above the tongue and fuse around weeks 8-12; a high tongue blocks elevation. **Infant airway**: preferential nasal breathing and small pharyngeal dimensions make tongue-base obstruction poorly tolerated.

**T-pediatric-35.pathophysiology**

**Sequence**: early mandibular hypoplasia keeps the tongue high, preventing palatal shelf fusion (U-shaped cleft). **Glossoptosis**: posterior tongue displacement obstructs the airway. **Feeding problems**: obstruction and cleft impair feeding. **Syndromes**: Stickler, 22q11, Treacher Collins. **Mandibular distraction**: advances the mandible and tongue base.

### CC-pediatric-35.1 (concept check)

Stem: A newborn has a small mandible, a U-shaped cleft palate, and obstructive breathing that improves when prone. Why does the cleft form in this sequence?

- **Correct:** The high tongue blocks palatal shelf fusion
- Distractor: The cleft causes the small mandible — _why wrong:_ The sequence runs from mandibular hypoplasia to glossoptosis to cleft, not the reverse.
- Distractor: Maternal smoking alone causes the triad — _why wrong:_ Smoking raises cleft risk but does not explain this sequence.
- Distractor: Teratogen exposure fuses the shelves early — _why wrong:_ The problem is failure of fusion, not premature fusion.

Explanation: Early mandibular hypoplasia keeps the tongue high between the palatal shelves, preventing elevation and fusion (U-shaped cleft) and causing glossoptosis. Treatment escalates from prone positioning to nasopharyngeal airway, tongue-lip adhesion, distraction, or tracheostomy.

Pearl: Micrognathia → glossoptosis → cleft palate.

## T-pediatric-36 — Recurrent Respiratory Papillomatosis
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-36.overview**

Recurrent respiratory papillomatosis is HPV-6 and HPV-11 driven benign papillomas of the airway that recur repeatedly. Treatment is surgical debulking with adjuvants such as bevacizumab, and HPV vaccination is primary prevention.

**T-pediatric-36.physiology**

**Squamociliary junctions**: transition zones between ciliated and squamous epithelium (limen vestibuli, ventricle, undersurface of the vocal folds, carina, tracheostomy site) are natural infection sites. **Basal cell reservoir**: HPV infects and persists in basal epithelial cells that continuously renew the epithelium. **Cell-mediated immunity**: T cells normally clear HPV-infected cells. **Airway caliber**: the small pediatric larynx is quickly obstructed by exophytic growth.

**T-pediatric-36.pathophysiology**

**Transmission**: juvenile-onset disease usually reflects vertical transmission from maternal genital HPV during birth. **Viral latency**: HPV DNA persists in normal-appearing mucosa, so surgery removes lesions but not the virus, explaining recurrence. **Aggressive juvenile course**: earlier onset and HPV-11 are associated with more frequent surgery. **Distal spread**: tracheal and pulmonary involvement increases morbidity, and malignant transformation is rare. **Surgical principle**: debulk to maintain an airway and voice while avoiding scar, especially at the anterior commissure. **Adjuvants**: bevacizumab blocks VEGF-driven angiogenesis that papillomas depend on; HPV vaccination prevents new cases and may reduce recurrence.

### CC-pediatric-36.1 (concept check)

Stem: A 4-year-old with hoarseness needs debridement of laryngeal papillomas every 6-8 weeks despite complete removal each time. Why do they keep recurring?

- **Correct:** HPV persists in normal-looking mucosa
- Distractor: The papillomas are malignant — _why wrong:_ RRP lesions are benign, though rare malignant transformation can occur.
- Distractor: Surgery seeds papillomas into the trachea — _why wrong:_ Distal spread can occur, but it does not explain local recurrence.
- Distractor: Untreated allergy drives regrowth — _why wrong:_ Allergy does not cause papilloma recurrence.

Explanation: HPV-6 and HPV-11 remain latent in basal cells of normal-appearing mucosa, so removing visible lesions does not eradicate the virus. Bevacizumab reduces surgical frequency, and HPV vaccination prevents new cases.

Pearl: RRP is a viral disease: surgery controls it but does not cure it.

## T-pediatric-37 — Recurrent Tonsillitis Decision-Making
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-37.overview**

Tonsillectomy for recurrent throat infection is indicated by Paradise criteria: 7 episodes in 1 year, 5 per year for 2 years, or 3 per year for 3 years, with documented features. Benefits are modest and must be weighed against surgical risks, so watchful waiting is reasonable for many.

**T-pediatric-37.physiology**

**Tonsil immunology**: tonsils are secondary lymphoid organs that sample oral antigens through crypt epithelium and produce IgA and other antibodies. **Crypts**: deep branching invaginations increase surface area but also trap debris and bacteria. **Age-related activity**: tonsillar immune activity peaks in childhood and declines with age. **Antibody redundancy**: removing tonsils does not measurably impair systemic immunity.

**T-pediatric-37.pathophysiology**

**Recurrent infection**: Group A streptococcus and viruses repeatedly infect crypts; bacterial biofilms within crypts persist despite antibiotics. **Documentation requirement**: each episode should include fever over 38.3 C, cervical adenopathy, tonsillar exudate, or a positive strep test. **Natural history**: episode frequency declines over time, so many children improve without surgery. **Modifying factors**: peritonsillar abscess, PFAPA, multiple antibiotic allergies, and missed school favor surgery. **Risk side**: post-tonsillectomy hemorrhage (about 2-4 percent), dehydration, and anesthesia risks.

### CC-pediatric-37.1 (concept check)

Stem: A 9-year-old has had 5 documented streptococcal pharyngitis episodes this year and 6 last year, each with fever over 38.3 C and exudate. Which criterion supports tonsillectomy?

- **Correct:** Paradise frequency criteria are met
- Distractor: Any child with 3 sore throats per year — _why wrong:_ Frequency must meet thresholds and episodes must be documented.
- Distractor: Large tonsil size on examination — _why wrong:_ Tonsil size supports surgery for obstruction, not for infection.
- Distractor: Parental preference without documentation — _why wrong:_ Guidelines require documented, qualifying episodes.

Explanation: Paradise criteria are 7 episodes in 1 year, 5 per year for 2 years, or 3 per year for 3 years, each documented with features such as fever, exudate, adenopathy, or a positive strep test. Five per year for 2 years qualifies.

Pearl: Tonsillectomy for infection needs documented, qualifying episodes.

## T-pediatric-38 — Subglottic Hemangioma
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-38.overview**

Subglottic hemangioma is an infantile hemangioma of the airway causing progressive biphasic stridor in the first months of life. Propranolol is first-line, and beard-distribution cutaneous hemangiomas raise suspicion.

**T-pediatric-38.physiology**

**Infantile hemangioma life cycle**: absent or subtle at birth, rapid proliferation over the first months, plateau, then involution over years. **GLUT1 expression**: infantile hemangioma endothelial cells express GLUT1, distinguishing them from vascular malformations. **Subglottic geometry**: the narrowest point of the infant airway, where small lesions cause large resistance increases. **Angiogenesis signaling**: VEGF and related factors drive endothelial proliferation.

**T-pediatric-38.pathophysiology**

**Proliferation**: clonal endothelial expansion during the first months enlarges the lesion, typically posterolateral in the subglottis. **Progressive stridor**: biphasic stridor worsens with crying or infection, often mistaken for croup. **Beard distribution**: cutaneous hemangiomas over the mandible, chin, and neck predict airway involvement. **Propranolol mechanism**: beta-blockade causes vasoconstriction, decreased VEGF and bFGF expression, and endothelial apoptosis. **PHACE screening**: large segmental facial hemangiomas require evaluation for associated anomalies before beta-blockers.

### CC-pediatric-38.1 (concept check)

Stem: A 3-month-old has progressive biphasic stridor that worsens with crying and a hemangioma covering the chin and jaw. Endoscopy shows a smooth, compressible posterolateral subglottic mass. What is first-line treatment?

- **Correct:** Oral propranolol
- Distractor: Immediate tracheostomy — _why wrong:_ Tracheostomy is reserved for failure of medical therapy or critical airway.
- Distractor: CO2 laser excision — _why wrong:_ Laser or open excision is reserved for refractory lesions because of stenosis risk.
- Distractor: Observation until involution — _why wrong:_ Airway hemangiomas can cause obstruction during the proliferative phase and need treatment.

Explanation: Infantile hemangiomas proliferate in the first months. Propranolol causes vasoconstriction, decreases VEGF, and triggers endothelial apoptosis. Beard-distribution cutaneous hemangiomas predict airway involvement.

Pearl: Beard hemangioma + stridor = subglottic hemangioma.

## T-pediatric-39 — Supraglottoplasty
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-39.overview**

Supraglottoplasty divides short aryepiglottic folds and removes redundant supraglottic tissue to treat severe laryngomalacia. It relieves obstruction in most infants with a low complication rate.

**T-pediatric-39.physiology**

**Supraglottic structure**: the epiglottis, aryepiglottic folds, and arytenoid mucosa frame the laryngeal inlet. **Inspiratory forces**: airflow through a narrow inlet lowers intraluminal pressure (Bernoulli), drawing floppy tissue inward. **Tethering**: short aryepiglottic folds pull the epiglottis into an omega shape and restrict opening. **Neuromuscular tone**: maintains inlet shape and improves with maturation.

**T-pediatric-39.pathophysiology**

**Releasing tethering**: dividing short folds lets the epiglottis open. **Removing redundancy**: trimming arytenoid mucosa removes tissue prolapse. **Complications**: supraglottic stenosis from excessive or bilateral resection, and aspiration. **Comorbidities**: neurologic disease and syndromes predict poorer outcomes.

### CC-pediatric-39.1 (concept check)

Stem: A 3-month-old with severe laryngomalacia has failure to thrive and oxygen desaturations during feeds. Endoscopy shows tight, short aryepiglottic folds pulling the epiglottis into an omega shape. Why does dividing the folds help?

- **Correct:** It releases tethered folds
- Distractor: It removes the entire epiglottis — _why wrong:_ The epiglottis is preserved; only tethering and redundant tissue are addressed.
- Distractor: It widens the cricoid ring — _why wrong:_ Supraglottoplasty does not affect the subglottis.
- Distractor: It cures the underlying reflux — _why wrong:_ Reflux is managed medically; surgery addresses mechanical collapse.

Explanation: Short aryepiglottic folds tether the epiglottis and arytenoid mucosa, so inspiratory airflow pulls them into the airway. Dividing the folds and trimming redundant arytenoid mucosa opens the inlet with low complication rates.

Pearl: Severe laryngomalacia: supraglottoplasty.

## T-pediatric-40 — Thyroglossal Duct Cyst
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-40.overview**

Thyroglossal duct cyst is the most common congenital midline neck mass, moving with swallowing and tongue protrusion. The Sistrunk procedure (including the central hyoid) is curative.

**T-pediatric-40.physiology**

**Thyroid origin**: the thyroid begins as an endodermal diverticulum at the foramen cecum (junction of the anterior two-thirds and posterior third of the tongue) in week 3-4. **Descent**: it descends through the tongue base and anterior neck, passing anterior to, through, or behind the developing hyoid, attached by the thyroglossal duct. **Involution**: the duct normally obliterates by about week 8-10, leaving the foramen cecum and sometimes a pyramidal lobe. **Hyoid formation**: the hyoid forms from second and third arch cartilage around the descending tract, which is why the tract is intimate with its central body.

**T-pediatric-40.pathophysiology**

**Persistent epithelium**: secretes fluid, forming a cyst anywhere along the tract. **Infection**: oral bacteria reach the cyst via the foramen cecum, causing abscess. **Hyoid relationship**: the tract passes through or around the hyoid, so removing the central hyoid reduces recurrence. **Ectopic thyroid**: rarely the only functioning thyroid tissue, so ultrasound confirms a normal thyroid preoperatively. **Carcinoma**: rare papillary carcinoma within the cyst.

### CC-pediatric-40.1 (concept check)

Stem: A 6-year-old has a recurrently infected thyroglossal duct cyst. Why does the Sistrunk procedure remove the central portion of the hyoid bone?

- **Correct:** The tract runs through the hyoid
- Distractor: The hyoid contains thyroid tissue — _why wrong:_ The hyoid is bone; the tract runs through or adjacent to it.
- Distractor: It improves swallowing afterward — _why wrong:_ Removing the central hyoid does not improve swallowing.
- Distractor: It prevents hypothyroidism — _why wrong:_ Hyoid removal does not affect thyroid function.

Explanation: Because the thyroid descends past the developing hyoid, the tract is intimately related to it. Removing the central hyoid and a core of tongue base tissue reduces recurrence from about 50 percent to under 5 percent.

Pearl: Thyroglossal duct cyst: Sistrunk, not simple excision.

## T-pediatric-41 — Tracheomalacia / Bronchomalacia
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-41.overview**

Tracheomalacia is excessive collapse of the tracheal wall during expiration, primary (cartilage weakness) or secondary (vascular compression, tracheoesophageal fistula). It causes expiratory wheeze and a barking cough and often improves with growth.

**T-pediatric-41.physiology**

**Tracheal structure**: C-shaped cartilage rings anteriorly and a membranous posterior wall with trachealis muscle; the normal cartilage-to-membrane ratio is about 4.5:1. **Pressure dynamics**: intrathoracic airways widen during inspiration and narrow during expiration as pleural pressure rises. **Extrathoracic vs intrathoracic**: extrathoracic airway collapse is inspiratory; intrathoracic collapse is expiratory. **Growth**: cartilage stiffens and airway diameter increases with age.

**T-pediatric-41.pathophysiology**

**Primary malacia**: deficient or soft cartilage and a widened posterior membrane collapse during expiration and cough. **Secondary malacia**: external compression by the innominate artery, vascular rings, or cardiac enlargement, and esophageal atresia with tracheoesophageal fistula. **Symptoms**: expiratory wheeze and stridor, barking (seal) cough, recurrent infections from poor clearance, and dying spells in severe cases. **Diagnosis**: dynamic airway endoscopy (spontaneous breathing) or dynamic CT shows collapse. **Treatment logic**: observation for mild cases; CPAP provides a pneumatic stent; aortopexy or posterior tracheopexy for severe cases.

### CC-pediatric-41.1 (concept check)

Stem: An infant who had repair of esophageal atresia with tracheoesophageal fistula has a barking cough and expiratory wheeze that worsen with crying. Why does the trachea collapse mainly during expiration?

- **Correct:** Rising pleural pressure compresses a weak trachea
- Distractor: Inspiration pulls the intrathoracic trachea closed — _why wrong:_ Inspiratory collapse is typical of extrathoracic airway disease.
- Distractor: Mucus plugs form only on expiration — _why wrong:_ Mucus may contribute, but the collapse is dynamic and pressure-driven.
- Distractor: The vocal folds adduct during expiration — _why wrong:_ Glottic motion does not explain tracheal collapse.

Explanation: The intrathoracic trachea narrows when pleural pressure rises during expiration and cough. Deficient cartilage and a wide posterior membrane, common after TEF, collapse. CPAP, aortopexy, or tracheopexy treat severe cases.

Pearl: Intrathoracic malacia = expiratory symptoms.

## T-pediatric-42 — Tympanostomy Tube Indications
_source: pathophys_v470/pediatric_a.py_

**T-pediatric-42.overview**

Tympanostomy tubes ventilate the middle ear for persistent OME with hearing loss, recurrent AOM with effusion, and at-risk children. AAO-HNS guidelines define indications to avoid unnecessary surgery.

**T-pediatric-42.physiology**

**Middle-ear ventilation**: the Eustachian tube normally opens with swallowing to replace gas absorbed by the mucosa; a tympanostomy tube provides a permanent alternative vent through the drum. **Effusion clearance**: once ventilated, mucosal inflammation settles and the effusion drains down the tube or is absorbed. **Tube extrusion**: lateral epithelial migration on the drum surface gradually pushes short-term tubes out over 6-18 months. **Hearing and language**: an effusion produces a mild-to-moderate conductive loss that can reduce speech input during the language-learning years.

**T-pediatric-42.pathophysiology**

**Chronic OME**: effusion for 3 months or more with hearing loss impairs language development. **Recurrent AOM**: 3 episodes in 6 months or 4 in a year with effusion. **At-risk children**: developmental delay, speech disorders, Down syndrome, and cleft palate. **Otorrhea**: tubes allow drainage, treated with topical drops. **Complications**: persistent perforation, tympanosclerosis, and cholesteatoma.

### CC-pediatric-42.1 (concept check)

Stem: A 3-year-old has had bilateral middle-ear effusions for 4 months with a 30 dB conductive hearing loss and speech delay. Why are tubes indicated?

- **Correct:** Chronic effusion with hearing loss
- Distractor: Any effusion lasting more than 2 weeks — _why wrong:_ Many effusions resolve; tubes are indicated for persistence of 3 months or more with hearing loss or at-risk status.
- Distractor: To prevent cholesteatoma in all children — _why wrong:_ Tubes are not placed routinely to prevent cholesteatoma.
- Distractor: To allow topical antibiotics for effusion — _why wrong:_ Effusion is not treated with drops; tubes ventilate the ear.

Explanation: Persistent bilateral effusion for 3 months or more with hearing loss, especially with speech delay, meets guideline criteria. Tubes ventilate the middle ear, restoring hearing during language development.

Pearl: Tubes for chronic effusion with hearing loss or at-risk children.

## T-pediatric-43 — Velopharyngeal Insufficiency
_source: pathophys_v470/pediatric_b.py_

**T-pediatric-43.overview**

Velopharyngeal insufficiency is incomplete closure between the soft palate and pharynx during speech, causing hypernasality and nasal air emission. It occurs after cleft palate repair, after adenoidectomy in at-risk children, and with neuromuscular disease.

**T-pediatric-43.physiology**

**Velopharyngeal valve**: the levator veli palatini elevates and retracts the velum to contact the posterior pharyngeal wall while the lateral walls move medially. **Closure patterns**: coronal (most common), sagittal, circular, and circular with a Passavant ridge, which guide surgical choice. **Speech requirement**: oral pressure consonants (p, b, s) require a sealed velopharynx to build oral pressure. **Adenoid contribution**: in young children, the adenoid pad helps the velum achieve closure.

**T-pediatric-43.pathophysiology**

**Structural insufficiency**: a short velum or abnormally oriented levator sling (cleft palate, submucous cleft with bifid uvula, notched hard palate, and zona pellucida). **Post-adenoidectomy VPI**: removing an adenoid that compensated for a marginal velum unmasks the gap, so at-risk children get partial adenoidectomy. **Neuromuscular incompetence**: weak or poorly coordinated movement (e.g., 22q11 deletion, neurologic disease). **Speech consequences**: hypernasality, nasal air emission, and compensatory articulation (glottal stops). **Treatment logic**: speech therapy for mislearning; surgery (palatoplasty, pharyngeal flap, sphincter pharyngoplasty) for anatomic gaps, chosen by closure pattern; OSA is the key surgical risk.

### CC-pediatric-43.1 (concept check)

Stem: A 6-year-old has new hypernasal speech and nasal air escape after adenoidectomy. Exam shows a bifid uvula and a notch at the posterior edge of the hard palate. What is the underlying problem?

- **Correct:** Submucous cleft with a misaligned levator
- Distractor: Nasopharyngeal stenosis from scar — _why wrong:_ Stenosis causes hyponasal speech and obstruction, not hypernasality.
- Distractor: Residual adenoid tissue blocking closure — _why wrong:_ Residual tissue would reduce, not increase, nasal resonance.
- Distractor: Unilateral vocal fold paralysis — _why wrong:_ Vocal fold paralysis causes breathy voice, not hypernasality.

Explanation: In a submucous cleft, the levator veli palatini inserts abnormally and cannot close the velopharynx; the adenoid pad compensated until it was removed. Speech therapy plus palatal repair or pharyngoplasty restores closure.

Pearl: Bifid uvula + hypernasality after adenoidectomy = submucous cleft.


---

# Laryngology / Voice / Swallowing

## T-laryngology-1 — Acute / Chronic Laryngopharyngitis
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-1.overview**

Laryngitis is inflammation of the larynx: acute (usually viral) or chronic (smoking, reflux, voice abuse, inhaled steroids, fungal infection). Persistent hoarseness over 4 weeks warrants laryngoscopy.

**T-laryngology-1.physiology**

**Laryngeal mucosa**: respiratory epithelium above and below the folds with squamous epithelium on the vibrating edge. **Mucus layer**: a thin, well-hydrated mucus film lubricates the folds and lowers the effort of phonation. **Mucociliary clearance**: moves secretions from the lower airway up to the larynx. **Immune defenses**: the mucosa contains lymphoid cells that respond rapidly to viral infection.

**T-laryngology-1.pathophysiology**

**Acute viral laryngitis**: viral infection causes edema and inflammation of the folds, increasing mass and stiffness, producing hoarseness or aphonia that resolves in 1-2 weeks. **Voice use during inflammation**: raises the risk of vocal fold hemorrhage, which is why voice rest is advised. **Chronic laryngitis**: persistent irritants (smoking, reflux, voice abuse, inhaled pollutants) sustain inflammation and epithelial thickening. **Fungal laryngitis**: inhaled corticosteroids and immunosuppression allow Candida, producing white plaques that can mimic leukoplakia. **Red flag**: hoarseness persisting beyond 4 weeks warrants laryngoscopy to exclude neoplasm.

### CC-laryngology-1.1 (concept check)

Stem: A 30-year-old using a high-dose inhaled corticosteroid for asthma has 3 weeks of hoarseness. Laryngoscopy shows white plaques on both vocal folds that wipe off partially. What is the most likely diagnosis?

- **Correct:** Candida laryngitis
- Distractor: Bilateral vocal fold leukoplakia — _why wrong:_ Leukoplakia is fixed keratosis and does not wipe off; it requires biopsy if persistent.
- Distractor: Viral laryngitis — _why wrong:_ Viral laryngitis causes edema and erythema, not plaques.
- Distractor: Reflux laryngitis — _why wrong:_ Reflux causes posterior erythema and edema, not white plaques.

Explanation: Inhaled steroids deposited on the larynx suppress local immunity and allow Candida overgrowth. Antifungals, spacer use, rinsing, and steroid dose review treat it; lesions that persist need biopsy.

Pearl: White laryngeal plaques in an inhaled-steroid user: think Candida first, biopsy if persistent.

## T-laryngology-2 — Arytenoid Adduction / Reinnervation
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-2.overview**

Arytenoid adduction rotates the arytenoid medially to close a posterior glottic gap and correct level mismatch; reinnervation (ansa cervicalis to RLN) restores tone and bulk. Both complement medialization thyroplasty.

**T-laryngology-2.physiology**

**Arytenoid mechanics**: the lateral cricoarytenoid pulls the muscular process anteriorly, rotating the vocal process medially and downward to close the posterior glottis. **Vertical level**: the arytenoid position sets the height of the vocal fold. **Ansa cervicalis**: a motor nerve loop from C1-C3 supplying the strap muscles, which can be sacrificed to donate axons. **Muscle bulk and tone**: depend on continued innervation; denervated muscle atrophies over months.

**T-laryngology-2.pathophysiology**

**Posterior gap**: thyroplasty alone medializes the membranous fold but not the arytenoid. **Arytenoid adduction**: a suture mimics the lateral cricoarytenoid pull. **Reinnervation**: restores thyroarytenoid bulk and tone over months but not purposeful motion. **Candidates**: younger patients with long-term paralysis benefit from reinnervation.

### CC-laryngology-2.1 (concept check)

Stem: After medialization thyroplasty for long-standing vocal fold paralysis, a patient still has breathy voice. Stroboscopy shows a persistent posterior glottic gap and the paralyzed fold sitting higher than the normal fold. What procedure addresses this?

- **Correct:** Arytenoid adduction
- Distractor: A larger thyroplasty implant — _why wrong:_ A larger implant medializes the membranous fold but does not rotate the arytenoid or fix level.
- Distractor: Bilateral vocal fold injection — _why wrong:_ Injecting the normal fold does not correct the posterior gap or level.
- Distractor: Botulinum toxin to the normal fold — _why wrong:_ Weakening the normal fold worsens closure.

Explanation: Arytenoid adduction places a suture that mimics the lateral cricoarytenoid, rotating the vocal process medially and down to close the posterior gap and correct vertical mismatch. Reinnervation restores tone and bulk over months.

Pearl: Posterior gap after thyroplasty: add arytenoid adduction.

## T-laryngology-3 — Aspiration-Prevention Surgery
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-3.overview**

Aspiration-prevention surgery (laryngotracheal separation, laryngeal closure, total laryngectomy) separates the airway from the food passage in intractable aspiration. It is lifesaving when recurrent pneumonia persists despite other measures.

**T-laryngology-3.physiology**

**Shared pharynx**: the airway and digestive tract cross at the hypopharynx, so protecting the airway depends on precise laryngeal closure. **Laryngeal protective mechanisms**: elevation, epiglottic inversion, glottic and supraglottic closure, sensation, and cough. **Pulmonary defense**: the lungs tolerate small aspiration if cough and mucociliary clearance are intact. **Secretions**: patients produce about 1-1.5 liters of saliva daily, which is aspirated even without oral intake.

**T-laryngology-3.pathophysiology**

**Intractable aspiration**: severe neurologic disease or cancer treatment leaves no protective function. **Separation logic**: diverting the trachea to a stoma removes the path for aspirated material. **Voice loss**: most procedures sacrifice voice. **Reversibility**: laryngotracheal separation is potentially reversible.

### CC-laryngology-3.1 (concept check)

Stem: A 35-year-old with severe cerebral palsy has recurrent aspiration pneumonia from his own saliva despite gastrostomy feeding and glycopyrrolate. He is nonverbal. What is the rationale for laryngotracheal separation?

- **Correct:** It separates airway from pharynx
- Distractor: It restores safe oral feeding — _why wrong:_ Separation protects the lungs; oral intake may remain limited by neurologic disease.
- Distractor: It reduces saliva production — _why wrong:_ Saliva production is unchanged; it simply cannot reach the lungs.
- Distractor: It improves his ability to speak — _why wrong:_ Separation removes phonation through the larynx.

Explanation: When the larynx cannot protect the airway, even tube-fed patients aspirate saliva. Separating the trachea from the larynx (or laryngectomy) eliminates aspiration; separation is potentially reversible.

Pearl: Intractable aspiration with no voice to lose: separation saves the lungs.

## T-laryngology-4 — Benign Vocal Fold Lesions
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-4.overview**

Benign vocal fold lesions (nodules, polyps, cysts, Reinke edema, pseudocysts, granulomas) are the most common causes of dysphonia in voice users. Most arise in the superficial lamina propria from phonotrauma, and therapy precedes microsurgery for most.

**T-laryngology-4.physiology**

**Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. **Mucosal wave**: the cover ripples over the body from inferior to superior during each vibratory cycle, producing a periodic sound source. **Vibratory midpoint**: maximal collision forces occur at the junction of the anterior and middle thirds of the membranous fold. **Basement membrane zone**: anchors epithelium to the lamina propria and absorbs shear forces. **Hydration**: adequate surface and tissue hydration reduce phonation threshold pressure and collision injury.

**T-laryngology-4.pathophysiology**

**Phonotrauma**: repetitive collision and shear forces injure the basement membrane zone and superficial lamina propria. **Nodules**: bilateral, symmetric thickening at the midpoint from chronic overuse, mainly epithelial and basement membrane changes. **Polyps**: usually unilateral, often after acute hemorrhage or a single phonotraumatic event, gelatinous or hemorrhagic. **Cysts**: mucus retention (gland obstruction) or epidermoid (trapped epithelium), deep in the lamina propria and less responsive to therapy. **Effect on voice**: added mass and stiffness disrupt the mucosal wave and prevent complete closure (hourglass gap with nodules). **Microflap principle**: preserve the superficial lamina propria and epithelium to avoid scar, which permanently stiffens the cover.

### CC-laryngology-4.1 (concept check)

Stem: A 32-year-old teacher has 6 months of hoarseness. Stroboscopy shows bilateral, symmetric swellings at the junction of the anterior and middle thirds of the membranous folds. Why do benign phonotraumatic lesions form at this exact location?

- **Correct:** It takes the greatest collision force
- Distractor: It has the thickest epithelium — _why wrong:_ Epithelial thickness is not why lesions concentrate here; impact stress is.
- Distractor: It is where the vocal ligament inserts — _why wrong:_ The ligament inserts at the vocal process and anterior commissure, not the midpoint.
- Distractor: It has the most mucous glands — _why wrong:_ Glands are concentrated in the ventricle and subglottis, not the free edge.

Explanation: The midpoint of the membranous fold has the largest vibratory amplitude, so collision and shear stresses peak there. Repetitive impact injures the basement membrane zone and superficial lamina propria.

Pearl: Phonotrauma lesions sit at the midpoint of the membranous fold.

## T-laryngology-5 — Bilateral Vocal Fold Immobility
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-5.overview**

Bilateral vocal fold immobility causes airway obstruction because both folds rest near the midline, usually with a near-normal voice. Causes include bilateral RLN injury, posterior glottic stenosis, and neurologic disease, and treatment balances airway against voice and aspiration.

**T-laryngology-5.physiology**

**Abduction**: the posterior cricoarytenoid is the only abductor; both must work for an adequate airway during exercise and sleep. **Airway vs voice tradeoff**: a wider glottis improves breathing but worsens voice and aspiration. **Posterior glottis**: provides most of the respiratory airway.

**T-laryngology-5.pathophysiology**

**Bilateral RLN paralysis**: after thyroidectomy or neurologic disease, folds sit paramedian, causing stridor. **Posterior glottic stenosis**: interarytenoid scar after intubation tethers the arytenoids, mimicking paralysis. **Cricoarytenoid ankylosis**: rheumatoid arthritis or trauma fixes the joints. **Diagnosis**: palpation and EMG distinguish neurogenic from mechanical fixation. **Treatment**: tracheostomy, posterior cordotomy, arytenoidectomy, or reinnervation.

### CC-laryngology-5.1 (concept check)

Stem: A 60-year-old has inspiratory stridor at rest but a nearly normal voice the day after total thyroidectomy. Laryngoscopy shows both vocal folds resting near the midline. What is the central tradeoff in definitive management?

- **Correct:** Airway gained, voice lost
- Distractor: Hearing preservation versus airway caliber — _why wrong:_ Glottic surgery does not affect hearing.
- Distractor: Calcium control versus vocal fold motion — _why wrong:_ Hypocalcemia is a separate problem; it does not create the airway tradeoff.
- Distractor: Tracheal stenosis versus vocal nodules — _why wrong:_ These are not the competing outcomes of glottic widening.

Explanation: With both folds paramedian, the voice is good but the airway is narrow. Posterior cordotomy or arytenoidectomy widens the airway but adds breathiness and aspiration risk; tracheostomy preserves voice while bypassing the glottis. Wait for recovery before irreversible surgery if the nerves were not cut.

Pearl: Bilateral immobility trades voice for airway.

## T-laryngology-6 — Chronic Cough / Laryngeal Hypersensitivity
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-6.overview**

Chronic cough lasting over 8 weeks without a cause after treatment of asthma, reflux, and upper airway cough syndrome is often a neuropathic laryngeal hypersensitivity. Neuromodulators and behavioral cough suppression therapy help.

**T-laryngology-6.physiology**

**Cough reflex**: vagal afferents in the larynx and airways transmit to the nucleus tractus solitarius, triggering a cough motor pattern. **Receptors**: TRPV1, TRPA1, and P2X3 receptors respond to irritants, temperature, and ATP. **Central modulation**: cortical control allows voluntary cough suppression.

**T-laryngology-6.pathophysiology**

**Sensory neuropathy**: viral injury or inflammation lowers the threshold of laryngeal afferents, causing cough with trivial triggers (talking, temperature changes). **Central sensitization**: increased brainstem gain amplifies cough responses. **Laryngeal paresthesia**: tickle, globus, and throat clearing. **Treatment logic**: gabapentin, pregabalin, amitriptyline, and P2X3 antagonists reduce afferent sensitivity; speech therapy teaches suppression.

### CC-laryngology-6.1 (concept check)

Stem: A 50-year-old has had a cough for 14 months triggered by talking and cold air, with a tickle in the throat. Asthma, reflux, and postnasal drip were treated without benefit, and imaging is normal. What mechanism best explains the cough?

- **Correct:** Laryngeal sensory neuropathy
- Distractor: Occult bacterial bronchitis — _why wrong:_ Infection would not explain a 14-month cough triggered by talking and temperature.
- Distractor: Undiagnosed interstitial lung disease — _why wrong:_ Normal imaging makes this unlikely.
- Distractor: Psychogenic cough only — _why wrong:_ There is a sensory mechanism; labeling it psychogenic misses effective treatment.

Explanation: After viral injury or inflammation, laryngeal vagal afferents become hypersensitive and brainstem gain increases, so trivial stimuli trigger cough. Gabapentin, pregabalin, amitriptyline, or P2X3 antagonists plus cough-suppression therapy help.

Pearl: Refractory cough triggered by talking and temperature = laryngeal hypersensitivity.

## T-laryngology-7 — Cricopharyngeal Dysfunction
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-7.overview**

Cricopharyngeal dysfunction is failure of the upper esophageal sphincter to relax or open fully, causing pharyngeal dysphagia, residue, and aspiration. It is diagnosed by fluoroscopy and manometry and treated with dilation, botulinum toxin, or myotomy.

**T-laryngology-7.physiology**

**Upper esophageal sphincter**: the cricopharyngeus is tonically contracted at rest to prevent air entering the esophagus and reflux entering the pharynx. **Opening mechanism**: requires neural inhibition of tone, plus anterior-superior pull by suprahyoid muscles and bolus pressure from pharyngeal contraction. **Compliance**: a healthy sphincter stretches to accommodate the bolus. **Innervation**: vagal motor fibers via the pharyngeal plexus.

**T-laryngology-7.pathophysiology**

**Failure to relax**: neurologic disease (stroke, Parkinson) impairs inhibition. **Reduced compliance**: fibrosis and muscle changes (aging, radiation, inflammatory myopathy) prevent opening despite relaxation. **Impaired traction**: weak hyolaryngeal elevation reduces opening even with normal relaxation. **Consequences**: hypopharyngeal residue, aspiration after the swallow, and Zenker diverticulum. **Cricopharyngeal bar**: fluoroscopic posterior indentation. **Treatment logic**: myotomy or dilation helps when the problem is the sphincter and pharyngeal propulsion is adequate; weak pharyngeal contraction predicts poor response.

### CC-laryngology-7.1 (concept check)

Stem: A 72-year-old has pharyngeal residue and aspiration after the swallow. Videofluoroscopy shows a prominent posterior cricopharyngeal bar, and manometry shows incomplete UES relaxation with good pharyngeal contraction. Why is myotomy likely to help?

- **Correct:** Outflow resistance is the barrier
- Distractor: Myotomy strengthens pharyngeal contraction — _why wrong:_ Myotomy reduces outflow resistance; it does not strengthen the pharynx.
- Distractor: Myotomy restores laryngeal sensation — _why wrong:_ Myotomy does not affect sensation.
- Distractor: Myotomy works best when the pharynx is weak — _why wrong:_ Poor pharyngeal contraction predicts a poor response to myotomy.

Explanation: UES opening requires relaxation, hyolaryngeal traction, and bolus pressure. When a noncompliant cricopharyngeus is the barrier and the pharynx pushes well, myotomy or dilation relieves residue and post-swallow aspiration.

Pearl: Cricopharyngeal myotomy needs a strong pharyngeal push.

## T-laryngology-8 — Dysphagia / Aspiration
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-8.overview**

Dysphagia is difficulty moving a bolus from mouth to stomach; aspiration is entry of material below the vocal folds. Localizing the phase (oral, pharyngeal, esophageal) and mechanism directs instrumental testing and treatment.

**T-laryngology-8.physiology**

**Oral phase (voluntary)**: lips seal, the tongue forms and propels the bolus posteriorly. **Pharyngeal phase (reflexive)**: triggered as the bolus passes the faucial pillars; the velum closes the nasopharynx, the hyoid and larynx elevate and move anteriorly, the epiglottis inverts, the vocal folds close, the pharyngeal constrictors squeeze, and the upper esophageal sphincter (cricopharyngeus) relaxes and opens. **UES opening**: requires cricopharyngeal relaxation plus anterior traction from suprahyoid muscles and bolus pressure. **Esophageal phase**: peristalsis moves the bolus to the stomach through a relaxing lower esophageal sphincter. **Central control**: brainstem swallowing centers (nucleus tractus solitarius, nucleus ambiguus) coordinate the sequence.

**T-laryngology-8.pathophysiology**

**Delayed swallow trigger**: bolus enters the pharynx before airway closure, causing aspiration before the swallow (common after stroke). **Reduced laryngeal elevation and closure**: aspiration during the swallow. **Pharyngeal weakness**: residue in the valleculae and pyriform sinuses spills into the airway after the swallow. **UES dysfunction**: cricopharyngeal hypertonicity or fibrosis causes residue and Zenker diverticulum. **Silent aspiration**: absent cough from reduced laryngeal sensation, which is why bedside screening misses aspiration. **Penetration-Aspiration Scale**: grades depth of airway entry and whether it is cleared. **Consequences**: aspiration pneumonia, malnutrition, dehydration, and reduced quality of life.

### CC-laryngology-8.1 (concept check)

Stem: A 70-year-old after a brainstem stroke aspirates thin liquids before the swallow is triggered on videofluoroscopy; the bolus reaches the pyriform sinuses before laryngeal elevation begins. Which phase is primarily impaired?

- **Correct:** Delayed initiation of the pharyngeal swallow
- Distractor: Weak oral bolus formation alone — _why wrong:_ Oral weakness causes premature spillage, but the defining finding here is delayed pharyngeal triggering.
- Distractor: Failure of upper esophageal sphincter opening — _why wrong:_ UES failure causes residue and aspiration after the swallow.
- Distractor: Weak esophageal peristalsis — _why wrong:_ Esophageal dysmotility causes retrosternal dysphagia, not aspiration before the swallow.

Explanation: When the reflexive pharyngeal swallow is delayed, the bolus enters an open airway. Chin tuck, thickened liquids, and sensory strategies help; timing of aspiration (before, during, after) guides treatment.

Pearl: Timing of aspiration localizes the problem.

## T-laryngology-9 — Esophageal Disease for the Otolaryngologist
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-9.overview**

Esophageal diseases (GERD, EoE, achalasia, strictures, rings, webs, cancer) commonly present to otolaryngologists as dysphagia or throat symptoms. Distinguishing oropharyngeal from esophageal dysphagia guides workup.

**T-laryngology-9.physiology**

**Esophageal muscle**: the upper third is striated (vagal motor), the middle mixed, and the lower two-thirds smooth muscle controlled by the myenteric plexus. **Peristalsis**: coordinated sequential contraction propels a bolus in about 8-10 seconds. **Lower esophageal sphincter**: tonically contracted, relaxing with swallowing via inhibitory neurons (nitric oxide, VIP). **Mucosal defense**: squamous epithelium with limited acid resistance, protected by clearance and salivary bicarbonate.

**T-laryngology-9.pathophysiology**

**Achalasia**: loss of inhibitory neurons in the myenteric plexus prevents LES relaxation and peristalsis. **EoE**: Th2-mediated eosinophilic inflammation causes rings, furrows, and strictures. **GERD**: transient LES relaxations allow acid reflux. **Esophageal cancer**: SCC (smoking, alcohol) and adenocarcinoma (Barrett). **Referred dysphagia**: distal obstruction can be perceived in the neck.

### CC-laryngology-9.1 (concept check)

Stem: A 45-year-old has 2 years of dysphagia to both solids and liquids from the start, regurgitation of undigested food, and weight loss. Barium swallow shows a dilated esophagus with a smooth bird-beak narrowing. What is the mechanism?

- **Correct:** Loss of inhibitory neurons
- Distractor: A cricopharyngeal bar — _why wrong:_ A bar causes oropharyngeal dysphagia at the UES, not a dilated esophagus.
- Distractor: Eosinophilic esophagitis — _why wrong:_ EoE causes rings and food impaction, typically solids first.
- Distractor: Esophageal adenocarcinoma — _why wrong:_ Cancer causes progressive solid-food dysphagia first and irregular narrowing.

Explanation: Achalasia results from loss of inhibitory neurons (nitric oxide, VIP) in the myenteric plexus, so the LES fails to relax and peristalsis is lost. Dysphagia to solids and liquids from onset is the clue.

Pearl: Solids and liquids from the start = motility disorder; solids first = mechanical.

## T-laryngology-10 — FEES
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-10.overview**

Fiberoptic endoscopic evaluation of swallowing (FEES) views the pharynx and larynx before and after the swallow with a transnasal scope. It is portable, radiation-free, and excellent for assessing secretions, residue, and laryngeal sensation.

**T-laryngology-10.physiology**

**Viewing window**: the scope sees pharyngeal and laryngeal anatomy before and after the swallow. **White-out**: pharyngeal contraction obscures the view at the moment of swallow. **Laryngeal sensation**: touch or air-pulse tests the laryngeal adductor reflex.

**T-laryngology-10.pathophysiology**

**Residue**: pooled material in the valleculae and pyriform sinuses indicates weakness. **Penetration and aspiration**: seen before and after the swallow. **Secretions**: pooled secretions predict aspiration risk. **Sensation**: absent cough response suggests silent aspiration. **Limitation**: white-out hides aspiration during the swallow.

### CC-laryngology-10.1 (concept check)

Stem: During FEES in a patient after stroke, the scope view goes white at the height of the swallow, and green-dyed puree is then seen below the vocal folds. What limitation of FEES does this illustrate?

- **Correct:** The swallow itself is hidden by white-out
- Distractor: FEES cannot see the larynx before swallowing — _why wrong:_ FEES sees the larynx well before and after the swallow.
- Distractor: FEES cannot assess laryngeal sensation — _why wrong:_ Touching the arytenoid or epiglottis tests sensation during FEES.
- Distractor: FEES cannot use real food — _why wrong:_ FEES uses ordinary foods, often dyed for visibility.

Explanation: Pharyngeal contraction and epiglottic inversion obscure the scope at the moment of swallow, so aspiration during the swallow is inferred from residue found afterward. Modified barium swallow shows that moment directly.

Pearl: FEES sees before and after; videofluoroscopy sees during.

## T-laryngology-11 — Inducible Laryngeal Obstruction / PVFM
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-11.overview**

Inducible laryngeal obstruction (paradoxical vocal fold motion) is inappropriate glottic or supraglottic closure during inspiration, triggered by exercise, irritants, or stress. It mimics asthma and is treated with laryngeal control breathing therapy.

**T-laryngology-11.physiology**

**Normal respiratory glottic motion**: the folds abduct during inspiration and slightly adduct during expiration. **Laryngeal protective reflexes**: closure protects the airway from irritants and aspiration. **Sensory input**: laryngeal mucosa is richly innervated by the superior laryngeal nerve.

**T-laryngology-11.pathophysiology**

**Hypersensitive reflex**: irritants, reflux, postnasal drip, and exercise trigger exaggerated adduction during inspiration. **Exercise-induced**: high airflow and drying provoke inspiratory stridor at peak exertion, resolving quickly with rest, unlike asthma. **Psychological factors**: anxiety and stress contribute. **Diagnosis**: laryngoscopy during symptoms or provocation shows inspiratory adduction with a posterior chink. **Treatment logic**: breathing techniques promote abduction; treat triggers.

### CC-laryngology-11.1 (concept check)

Stem: A 17-year-old runner has throat tightness and inspiratory stridor at peak exercise that resolves within minutes of stopping. Albuterol does not help and spirometry is normal. Laryngoscopy during exercise shows the vocal folds adducting on inspiration. What is the diagnosis?

- **Correct:** Exercise-induced laryngeal closure
- Distractor: Exercise-induced bronchospasm — _why wrong:_ Asthma causes expiratory wheeze and responds to bronchodilators.
- Distractor: Bilateral vocal fold paralysis — _why wrong:_ Paralysis causes fixed folds at rest, not exercise-triggered adduction.
- Distractor: Laryngomalacia of adolescence — _why wrong:_ Supraglottic collapse can occur, but this is glottic paradoxical adduction.

Explanation: Hypersensitive laryngeal reflexes trigger inappropriate glottic closure during inspiration with high airflow. Laryngeal control breathing therapy teaches abduction; triggers such as reflux and postnasal drip are treated.

Pearl: Inspiratory stridor at peak exercise that does not respond to albuterol = ILO.

## T-laryngology-12 — Injection Laryngoplasty
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-12.overview**

Injection laryngoplasty adds material lateral to the vocal fold to medialize it, improving closure in paralysis, paresis, atrophy, and scar. It can be done in clinic or the OR, temporary or long-lasting.

**T-laryngology-12.physiology**

**Paraglottic space**: the fat-containing space lateral to the thyroarytenoid muscle, deep to the vibrating cover, where injected material medializes the fold. **Glottic closure**: complete closure is needed for efficient voice, effective cough, and airway protection. **Superficial lamina propria**: must remain uninvolved so the mucosal wave is preserved. **Access routes**: peroral, transthyrohyoid, transcricothyroid, and transthyroid cartilage approaches reach the same plane.

**T-laryngology-12.pathophysiology**

**Closing a glottic gap**: added volume pushes the paralyzed or atrophic fold toward midline, reducing air escape and aspiration. **Material choice by duration**: hyaluronic acid and carboxymethylcellulose last weeks to months (bridging recovery); calcium hydroxylapatite and fat last longer. **Early injection**: in acute paralysis, early medialization improves voice and swallowing and may reduce the later need for permanent surgery by positioning the fold favorably during reinnervation. **Overinjection and superficial injection**: overinjection causes strained voice or airway compromise; superficial injection stiffens the cover. **Limitations**: injection does not correct large posterior gaps or level mismatch.

### CC-laryngology-12.1 (concept check)

Stem: A 62-year-old has a new left vocal fold paralysis after thoracic surgery 2 weeks ago, with aspiration of thin liquids. Recovery is still possible. Why is early temporary injection laryngoplasty useful?

- **Correct:** It closes the gap during recovery
- Distractor: It permanently restores fold movement — _why wrong:_ Injection adds bulk; it does not restore nerve function.
- Distractor: It replaces the need for swallow evaluation — _why wrong:_ Swallow assessment is still needed.
- Distractor: It treats the cause of the paralysis — _why wrong:_ It improves closure; it does not address the nerve injury.

Explanation: Temporary materials such as hyaluronic acid medialize the fold, improving voice and reducing aspiration. Early injection may also position the fold favorably during reinnervation, reducing later need for permanent surgery.

Pearl: Early temporary injection buys time without burning bridges.

## T-laryngology-13 — Laryngeal Anatomy
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-13.overview**

Laryngeal anatomy (cartilage framework, joints, muscles, nerves, and layered vocal folds) explains every voice, airway, and swallowing problem. It underlies stroboscopy, laryngeal EMG, phonosurgery, and airway surgery.

**T-laryngology-13.physiology**

**Cartilage framework**: thyroid (shield), cricoid (complete ring), paired arytenoids (vocal process and muscular process), epiglottis, and smaller corniculate and cuneiform cartilages. **Joints**: the cricoarytenoid joint allows rocking and gliding of the arytenoids to open and close the glottis; the cricothyroid joint allows tilting that lengthens the folds. **Intrinsic muscles**: posterior cricoarytenoid (only abductor), lateral cricoarytenoid and interarytenoid (adductors), thyroarytenoid (shortens, adducts, adjusts body stiffness), and cricothyroid (lengthens and tenses). **Innervation**: RLN to all intrinsic muscles except the cricothyroid; external branch of the SLN to the cricothyroid; internal branch of the SLN for supraglottic sensation. **Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. **Spaces**: the pre-epiglottic and paraglottic spaces are fat-filled compartments that guide tumor spread.

**T-laryngology-13.pathophysiology**

**Nerve injury patterns**: RLN injury causes immobility with breathy voice; EBSLN injury reduces pitch range and projection; SLN internal branch injury causes reduced sensation and silent aspiration. **Joint fixation**: cricoarytenoid ankylosis mimics paralysis, distinguished by palpation and laryngeal EMG. **Layer-specific lesions**: nodules and polyps live in the superficial lamina propria; scar and sulcus involve deeper layers; cancer invades the vocalis and paraglottic space. **Presbylarynx**: thinning of the lamina propria and muscle atrophy with age cause bowing. **Airway landmarks**: the cricothyroid membrane is the emergency surgical airway site.

## T-laryngology-14 — Laryngeal Electromyography (LEMG)
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-14.overview**

Laryngeal electromyography records electrical activity of laryngeal muscles to distinguish paralysis from fixation and predict recovery. It guides timing of permanent interventions.

**T-laryngology-14.physiology**

**Motor unit**: a motor neuron and the muscle fibers it innervates; laryngeal motor units are small for fine control. **Recruitment**: as effort increases, more and larger motor units fire. **Normal resting muscle**: electrically silent except for insertional activity. **Target muscles**: thyroarytenoid (RLN) and cricothyroid (SLN) are sampled to localize nerve injury.

**T-laryngology-14.pathophysiology**

**Active denervation**: fibrillation potentials and positive sharp waves appear 2-3 weeks after axonal injury. **Reinnervation**: polyphasic, long-duration motor unit potentials indicate regrowing axons. **Prognosis**: absent voluntary motor units with denervation potentials months after injury predict poor recovery, supporting permanent procedures; preserved recruitment predicts recovery. **Synkinesis**: activity in adductors during abduction tasks indicates misdirected reinnervation. **Mechanical fixation**: normal EMG with an immobile fold points to cricoarytenoid joint fixation or posterior glottic stenosis rather than paralysis. **Localization**: cricothyroid involvement implicates the SLN or a high vagal lesion.

## T-laryngology-15 — Laryngocele
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-15.overview**

A laryngocele is an air-filled dilation of the laryngeal saccule: internal (within the larynx), external (through the thyrohyoid membrane), or mixed. It is associated with increased laryngeal pressure and must be checked for an obstructing cancer.

**T-laryngology-15.physiology**

**Laryngeal saccule**: a blind pouch extending upward from the anterior laryngeal ventricle between the false fold and thyroid cartilage, lined by respiratory mucosa with mucous glands that lubricate the vocal folds. **Ventricle**: the space between the true and false folds. **Thyrohyoid membrane**: connects the hyoid and thyroid cartilage and is pierced by the internal branch of the SLN and superior laryngeal vessels. **Intralaryngeal pressure**: rises during coughing, straining, and blowing against resistance.

**T-laryngology-15.pathophysiology**

**Increased pressure**: glassblowers, wind instrument players, and coughing increase intralaryngeal pressure. **Obstruction**: tumor at the saccule neck can cause laryngocele, so cancer must be excluded. **Pyolaryngocele**: infection. **External extension**: through the thyrohyoid membrane, presenting as a neck mass enlarging with Valsalva.

## T-laryngology-16 — Laryngopharyngeal Reflux (LPR)
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-16.overview**

Laryngopharyngeal reflux is retrograde flow of gastric contents to the larynx and pharynx causing throat clearing, globus, hoarseness, and cough. Its diagnosis is controversial, and empiric PPI response is variable.

**T-laryngology-16.physiology**

**Antireflux barriers**: the lower esophageal sphincter, esophageal peristalsis, the upper esophageal sphincter, and salivary bicarbonate protect the pharynx and larynx. **Laryngeal mucosa**: lacks the protective mechanisms of the esophagus, such as robust bicarbonate secretion and carbonic anhydrase III, so even small exposures injure it. **Pepsin**: a gastric protease most active at acidic pH that can be taken up into laryngeal cells and reactivated later. **Upright vs supine reflux**: LPR is often upright and daytime, unlike classic GERD.

**T-laryngology-16.pathophysiology**

**Pepsin injury**: pepsin persists in laryngeal tissue and is reactivated by acid, causing inflammation. **Non-acid reflux**: may cause symptoms despite PPI therapy. **Findings**: posterior laryngeal erythema and edema, nonspecific. **PPI response**: inconsistent; lifestyle changes and alginates help.

### CC-laryngology-16.1 (concept check)

Stem: A 50-year-old has chronic throat clearing, globus, and hoarseness. Laryngoscopy shows posterior laryngeal erythema and edema. Why can the larynx be injured by reflux events too brief to cause heartburn?

- **Correct:** Weaker laryngeal mucosal defenses
- Distractor: The larynx has more acid receptors — _why wrong:_ The difference is defense, not acid receptors.
- Distractor: Reflux is always worse at night — _why wrong:_ LPR is often upright and daytime.
- Distractor: The larynx secretes acid itself — _why wrong:_ The larynx does not secrete acid.

Explanation: Laryngeal epithelium lacks the bicarbonate secretion and carbonic anhydrase defenses of the esophagus, and pepsin taken up into cells can be reactivated later. Findings are nonspecific and response to PPIs is inconsistent.

Pearl: LPR findings are nonspecific: treat thoughtfully and reassess.

## T-laryngology-17 — Leukoplakia / Laryngeal Dysplasia
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-17.overview**

Laryngeal leukoplakia is a clinical white patch that may represent hyperkeratosis, dysplasia, or carcinoma. Biopsy grades dysplasia, which predicts malignant transformation.

**T-laryngology-17.physiology**

**Vocal fold epithelium**: stratified nonkeratinizing squamous epithelium over the true folds, renewing from basal cells. **Maturation sequence**: basal cells divide and differentiate as they rise, flattening at the surface without keratin. **Mucosal pliability**: the epithelium and superficial lamina propria must remain pliable for the mucosal wave. **Field exposure**: inhaled carcinogens and refluxate bathe the entire laryngeal mucosa.

**T-laryngology-17.pathophysiology**

**Keratinization**: chronic irritation (smoking, reflux) causes keratin production, producing the white appearance. **Dysplasia**: disordered maturation and cellular atypia graded mild, moderate, severe; severe dysplasia has substantial transformation risk. **Stroboscopic clue**: preserved mucosal wave suggests superficial disease. **Treatment**: excisional biopsy, laser, and surveillance with smoking cessation.

## T-laryngology-18 — Medialization Thyroplasty
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-18.overview**

Medialization (type I) thyroplasty places an implant through a window in the thyroid cartilage to push a paralyzed or atrophic vocal fold toward midline. It is a permanent, reversible, awake procedure that allows voice tuning during surgery.

**T-laryngology-18.physiology**

**Paraglottic space**: lies between the thyroid cartilage and the thyroarytenoid muscle, allowing an implant to medialize the fold without touching the vibrating cover. **Window position**: placed at the level of the vocal fold, roughly at the midpoint of the thyroid cartilage height, a few millimeters from the anterior midline. **Glottic closure**: complete closure improves voice, cough, and swallow. **Vibratory cover preservation**: the superficial lamina propria stays untouched.

**T-laryngology-18.pathophysiology**

**Closing the gap**: medializing the membranous fold reduces air escape. **Posterior gap limit**: thyroplasty does not rotate the arytenoid, so large posterior gaps or level mismatch need arytenoid adduction. **Awake tuning**: patients phonate during surgery so implant size and position optimize voice. **Implant materials**: silastic, Gore-Tex, or hydroxyapatite. **Complications**: airway edema, hematoma, implant extrusion, and overmedialization.

### CC-laryngology-18.1 (concept check)

Stem: A 58-year-old with permanent left vocal fold paralysis undergoes type I thyroplasty under local anesthesia with sedation. Why is the patient kept awake enough to phonate during implant placement?

- **Correct:** So implant size and position can be tuned by voice
- Distractor: To monitor for airway fire — _why wrong:_ Fire risk relates to lasers and oxygen, not phonation during thyroplasty.
- Distractor: To confirm the recurrent laryngeal nerve is intact — _why wrong:_ The nerve is already paralyzed; phonation guides implant placement.
- Distractor: To avoid any need for imaging — _why wrong:_ Phonation is used for tuning, not to replace imaging.

Explanation: The implant is placed through a thyroid cartilage window into the paraglottic space, medializing the fold without touching the vibrating cover. Listening to the voice as the implant is adjusted prevents under- or overmedialization.

Pearl: Thyroplasty is tuned by ear.

## T-laryngology-19 — Microlaryngoscopy
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-19.overview**

Microlaryngoscopy is suspension laryngoscopy with an operating microscope for diagnosis and precise phonosurgery. Its core principle is preserving the superficial lamina propria to protect the mucosal wave.

**T-laryngology-19.physiology**

**Suspension laryngoscopy**: a laryngoscope suspended from a chest support exposes the larynx for two-handed microsurgery. **Superficial lamina propria**: the gel-like layer that allows the cover to vibrate. **Vocal ligament**: deeper layers that should not be violated in benign surgery.

**T-laryngology-19.pathophysiology**

**Microflap technique**: an incision lateral to the lesion allows elevation and removal while preserving overlying epithelium and lamina propria. **Scar**: injury to the superficial lamina propria replaces pliable tissue with collagen, stiffening the cover permanently. **Exposure difficulty**: retrognathia, limited neck extension, and large teeth. **Complications**: dental injury, tongue numbness, and taste change from pressure.

## T-laryngology-20 — Modified Barium Swallow
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-20.overview**

The modified barium swallow (videofluoroscopic swallow study) shows all phases of swallowing in real time with barium of different consistencies. It is the reference test for aspiration during the swallow and for testing compensatory strategies.

**T-laryngology-20.physiology**

**Fluoroscopic view**: lateral and AP views show bolus flow, hyolaryngeal elevation, epiglottic inversion, pharyngeal contraction, and UES opening. **Timing**: the swallow reflex normally triggers as the bolus head reaches the ramus of the mandible or valleculae. **Consistencies**: thin liquids move fastest and are most likely aspirated; thicker consistencies slow flow (IDDSI framework). **Biomechanics**: anterior-superior hyoid movement and laryngeal elevation pull open the UES.

**T-laryngology-20.pathophysiology**

**Aspiration timing**: before (delayed trigger), during (poor laryngeal closure), or after (residue spillage) the swallow, which guides treatment. **Residue patterns**: vallecular residue implies reduced tongue base retraction; pyriform residue implies pharyngeal weakness or UES dysfunction. **Cricopharyngeal bar**: a posterior indentation reflecting a noncompliant UES. **Penetration-Aspiration Scale**: grades severity. **Strategy testing**: chin tuck, head turn, and effortful swallow are tested for effectiveness. **Advantage over FEES**: sees aspiration during the swallow and the oral and esophageal phases.

### CC-laryngology-20.1 (concept check)

Stem: A head and neck cancer survivor has coughing with meals. Which advantage makes a modified barium swallow the better first study than FEES for this patient?

- **Correct:** It images the moment of swallow
- Distractor: It avoids all radiation exposure — _why wrong:_ Videofluoroscopy uses ionizing radiation; FEES does not.
- Distractor: It can be done at the bedside — _why wrong:_ FEES is portable; videofluoroscopy requires a radiology suite.
- Distractor: It shows secretions on the mucosa better — _why wrong:_ FEES shows pooled secretions and mucosal detail better.

Explanation: Videofluoroscopy shows oral, pharyngeal, and esophageal phases in real time, including hyolaryngeal elevation, UES opening, and aspiration during the swallow, and allows testing of compensatory strategies.

Pearl: Use videofluoroscopy to see biomechanics; use FEES for secretions, sensation, and portability.

## T-laryngology-21 — Muscle Tension Dysphonia
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-21.overview**

Muscle tension dysphonia is voice disorder from excessive or poorly regulated laryngeal and paralaryngeal muscle tension without structural pathology, or compensating for one. Voice therapy with circumlaryngeal massage is the main treatment.

**T-laryngology-21.physiology**

**Laryngeal posture**: suspended by extrinsic muscles that position the larynx. **Efficient phonation**: balanced airflow and glottic adduction. **Supraglottic structures**: false folds do not normally participate in phonation.

**T-laryngology-21.pathophysiology**

**Excess tension**: extrinsic and intrinsic muscle hyperfunction elevates the larynx and squeezes supraglottic structures. **Primary vs secondary**: primary without lesion; secondary compensating for paresis, lesion, or reflux. **Symptoms**: strained voice, neck pain, and fatigue. **Laryngoscopy**: supraglottic compression and posterior gap. **Therapy**: rebalances muscle use.

### CC-laryngology-21.1 (concept check)

Stem: A 35-year-old call-center worker has a strained, effortful voice and neck tension. Laryngoscopy shows anteroposterior supraglottic compression with no structural lesion and normal mobility. What is the first-line treatment?

- **Correct:** Voice therapy with manual therapy
- Distractor: Botulinum toxin to the thyroarytenoid — _why wrong:_ Botox treats spasmodic dysphonia, not primary MTD.
- Distractor: Microlaryngoscopy with excision — _why wrong:_ There is no lesion to remove.
- Distractor: Injection augmentation of both folds — _why wrong:_ Augmentation treats glottic insufficiency, not hyperfunction.

Explanation: Primary MTD is excess or dysregulated laryngeal and paralaryngeal muscle activity. Therapy with circumlaryngeal massage and resonant voice techniques rebalances muscle use. Secondary MTD compensating for a lesion or paresis must be excluded.

Pearl: Strained voice with supraglottic squeeze and no lesion = MTD: therapy first.

## T-laryngology-22 — Posterior Cordotomy / Arytenoidectomy
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-22.overview**

Posterior cordotomy and partial arytenoidectomy widen the posterior glottic airway for bilateral vocal fold immobility, often avoiding or allowing removal of a tracheostomy. They trade some voice quality and aspiration risk for a better airway.

**T-laryngology-22.physiology**

**Posterior glottis**: the cartilaginous glottis between the vocal processes provides most of the respiratory airway, while the membranous glottis produces most of the voice. **Airway resistance**: small increases in glottic radius greatly reduce resistance. **Vocal process**: the attachment of the vocal ligament to the arytenoid; dividing behind it opens the airway while sparing most of the vibrating fold. **Glottic closure for swallowing**: depends on approximation of the arytenoids and folds.

**T-laryngology-22.pathophysiology**

**Airway gain**: a laser cut just anterior to the vocal process lets the fold retract laterally, creating a posterior triangular airway. **Voice tradeoff**: a wider glottis causes breathiness, minimized by limiting the anterior extent. **Aspiration risk**: larger openings and arytenoid resection impair closure during swallowing. **Scar contracture**: granulation and scar can narrow the airway again, sometimes requiring revision. **Patient selection**: confirm no recovery is expected (often wait 9-12 months after nerve injury) and distinguish paralysis from fixation.

## T-laryngology-23 — Posterior Glottic Stenosis / Arytenoid Fixation
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-23.overview**

Posterior glottic stenosis is scar in the interarytenoid region or cricoarytenoid joints after prolonged intubation, limiting abduction. It mimics bilateral vocal fold paralysis and is classified by Bogdasarian.

**T-laryngology-23.physiology**

**Posterior glottis**: the cartilaginous glottis between the arytenoids forms most of the respiratory airway area. **Cricoarytenoid joint**: a synovial joint that lets the arytenoid rock and glide to abduct the vocal fold. **Interarytenoid mucosa**: covers the interarytenoid muscle and lies where an endotracheal tube rests. **Mucosal perfusion**: pressure from a tube exceeding capillary perfusion pressure causes ischemia.

**T-laryngology-23.pathophysiology**

**Endotracheal tube pressure**: the tube rests in the posterior glottis, causing ulceration and scar. **Bogdasarian types**: I (interarytenoid synechia), II (posterior commissure scar), III (scar with one joint fixed), IV (both joints fixed). **Mechanical fixation vs paralysis**: palpation and EMG distinguish. **Treatment**: scar division, posterior cricoid grafts, or cordotomy.

### CC-laryngology-23.1 (concept check)

Stem: A 50-year-old intubated for 3 weeks during COVID pneumonia now has exertional stridor. Both vocal folds barely abduct. On palpation under anesthesia, the arytenoids do not move, and an interarytenoid scar band is present. What distinguishes this from bilateral vocal fold paralysis?

- **Correct:** Fixed arytenoids on palpation
- Distractor: Absent mucosal wave on stroboscopy — _why wrong:_ Mucosal wave findings do not separate fixation from paralysis.
- Distractor: Normal voice at rest — _why wrong:_ Both conditions can preserve a reasonable voice.
- Distractor: History of thyroid surgery — _why wrong:_ Thyroid surgery suggests paralysis; prolonged intubation suggests fixation.

Explanation: The endotracheal tube rests in the posterior glottis, causing ulceration and interarytenoid scar or cricoarytenoid joint fixation. Palpation and laryngeal EMG separate mechanical fixation from neurogenic paralysis, which changes treatment.

Pearl: After prolonged intubation, palpate the arytenoids before calling it paralysis.

## T-laryngology-24 — Presbyphonia
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-24.overview**

Presbyphonia is voice change from aging of the larynx: vocal fold atrophy and bowing cause weak, breathy, effortful voice. Voice therapy, injection, or thyroplasty improve closure.

**T-laryngology-24.physiology**

**Lamina propria aging**: with age, the superficial lamina propria loses elastin and hyaluronic acid while collagen becomes disorganized and denser, reducing pliability. **Thyroarytenoid muscle aging**: fiber loss, reduced motor units, and slower contraction thin the vocal fold body. **Respiratory driving pressure**: reduced lung elastic recoil and chest wall compliance lower subglottic pressure available for voice. **Hormonal effects**: menopause thickens and lowers women's voices, while declining androgens can thin men's folds. **Cartilage ossification**: laryngeal cartilages progressively ossify, stiffening the framework.

**T-laryngology-24.pathophysiology**

**Vocal fold bowing**: muscle atrophy and lamina propria thinning leave a concave fold edge and a spindle-shaped glottic gap. **Air escape**: incomplete closure produces a weak, breathy voice that fatigues by the end of the day. **Pitch shift**: women's pitch tends to fall and men's to rise as fold mass changes. **Reduced endurance and projection**: patients struggle to be heard in noise, with social withdrawal. **Diagnosis of exclusion**: paralysis, paresis, Parkinson disease, and lesions must be excluded. **Treatment logic**: strengthening therapy (Phonation Resistance Training Exercise) builds muscle bulk and closure; injection or bilateral thyroplasty adds bulk when therapy is insufficient.

### CC-laryngology-24.1 (concept check)

Stem: A 78-year-old retired lawyer has a weak, breathy voice that tires by evening. Stroboscopy shows bowed vocal folds with a spindle-shaped glottic gap and normal mobility. What is the main mechanism?

- **Correct:** Age-related fold atrophy
- Distractor: Bilateral recurrent laryngeal nerve injury — _why wrong:_ Mobility is normal, so the nerves are intact.
- Distractor: Reinke edema from smoking — _why wrong:_ Reinke edema adds mass and lowers pitch; it does not cause bowing.
- Distractor: Spasmodic dysphonia of the abductors — _why wrong:_ Abductor SD causes intermittent breathy breaks, not constant bowing.

Explanation: Age-related thyroarytenoid atrophy and loss of elastin and hyaluronic acid thin the folds, leaving a spindle gap and air escape. Strengthening therapy (Phonation Resistance Training) helps, and augmentation is added when needed.

Pearl: Bowed folds with normal mobility in an older adult = presbyphonia.

## T-laryngology-25 — Professional Voice
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-25.overview**

Professional voice users (singers, actors, teachers) have high vocal demands and low tolerance for subtle changes. Care emphasizes detailed evaluation, voice hygiene, therapy, and conservative surgery.

**T-laryngology-25.physiology**

**Vocal demands**: professional voice users phonate for long periods at high intensities and across wide pitch ranges. **Pitch control**: the cricothyroid lengthens and tenses the folds to raise pitch; the thyroarytenoid adjusts body stiffness and register. **Resonance**: the vocal tract filters the glottal source; trained singers tune resonances to project. **Breath support**: controlled subglottic pressure from respiratory muscles drives efficient phonation. **Vocal dose**: cumulative vibration cycles and collision stress accumulate over a day.

**T-laryngology-25.pathophysiology**

**Subtle lesions**: small changes affect upper range and endurance. **Hemorrhage**: from phonotrauma, especially with anticoagulants or premenstrual vascular changes; requires voice rest. **Reflux and allergies**: worsen voice. **Surgical risk**: scar can end careers, so surgery is conservative.

### CC-laryngology-25.1 (concept check)

Stem: A soprano scheduled to perform in 2 days develops sudden hoarseness and loss of her upper range after a strenuous rehearsal. She takes ibuprofen for menstrual cramps. Laryngoscopy shows a vocal fold hemorrhage. What is the correct advice?

- **Correct:** Voice rest; cancel the show
- Distractor: Steroids and perform as scheduled — _why wrong:_ Singing on a hemorrhage risks polyp formation and permanent scar.
- Distractor: Immediate microlaryngoscopy — _why wrong:_ Acute hemorrhage is managed with rest; surgery is reserved for persistent lesions.
- Distractor: Continue ibuprofen and sing lightly — _why wrong:_ NSAIDs impair platelet function and increase bleeding risk.

Explanation: Vocal fold hemorrhage from phonotrauma, worsened by NSAIDs and premenstrual vascular changes, can organize into a polyp or scar if the voice is used. Strict voice rest and avoiding antiplatelet agents allow resorption.

Pearl: Hemorrhage in a professional voice: rest, no NSAIDs, no performance.

## T-laryngology-26 — Radiation-Associated Dysphagia
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-26.overview**

Radiation-associated dysphagia is a late effect of head and neck radiation from fibrosis, neuropathy, and muscle atrophy, sometimes years after treatment. Prevention (dose-sparing, exercises) and rehabilitation are key.

**T-laryngology-26.physiology**

**Swallowing musculature**: constrictors, tongue base, and suprahyoid muscles generate propulsion. **Lower cranial nerves**: control swallowing. **Radiation biology**: late effects from fibrosis and microvascular injury.

**T-laryngology-26.pathophysiology**

**Fibrosis**: TGF-beta driven fibrosis stiffens swallowing muscles, reducing elevation and contraction. **Neuropathy**: late lower cranial nerve neuropathy reduces sensation and motor function. **Stricture**: UES or esophageal stricture. **Disuse atrophy**: NPO status worsens function, so swallowing during treatment is encouraged. **Dose dependence**: higher constrictor doses predict dysphagia.

### CC-laryngology-26.1 (concept check)

Stem: Six years after chemoradiation for base-of-tongue cancer, a patient has progressively worsening dysphagia and aspiration. There is no tumor recurrence. What explains the late onset?

- **Correct:** Late fibrosis and neuropathy
- Distractor: Acute radiation mucositis — _why wrong:_ Mucositis occurs during and shortly after treatment, not years later.
- Distractor: A new primary cancer in every case — _why wrong:_ Recurrence or new primaries must be excluded, but late fibrosis explains this pattern.
- Distractor: Radiation-induced esophageal reflux — _why wrong:_ Reflux does not explain progressive pharyngeal weakness and aspiration.

Explanation: TGF-beta driven fibrosis stiffens the pharyngeal constrictors and tongue base, and late lower cranial neuropathy reduces sensation and motor function. Dose to swallowing structures predicts risk, and swallowing exercises during treatment help prevent it.

Pearl: Late dysphagia years after radiation is common: rehabilitate and exclude recurrence.

## T-laryngology-27 — Reinke Edema
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-27.overview**

Reinke edema is diffuse, polypoid swelling of the superficial lamina propria, almost always in smokers, producing a low-pitched voice. Smoking cessation is essential, and microflap reduction treats symptomatic disease.

**T-laryngology-27.physiology**

**Reinke space**: the superficial lamina propria, a loose, gel-like layer bounded by the vocal ligament and epithelium. **Fold mass and pitch**: increased fold mass lowers fundamental frequency. **Lymphatic drainage**: limited in the superficial lamina propria.

**T-laryngology-27.pathophysiology**

**Smoking injury**: chronic irritation increases vascular permeability and fluid accumulation in Reinke space. **Voice change**: added mass lowers pitch, often making women's voices sound masculine. **Airway**: severe edema can obstruct the airway. **Surgery**: microflap suctioning of gelatinous material preserves the epithelium. **Recurrence**: with continued smoking.

### CC-laryngology-27.1 (concept check)

Stem: A 55-year-old woman who smokes two packs a day has a progressively deeper voice. Laryngoscopy shows bilateral, floppy, translucent swelling along the entire membranous vocal folds. Why is her voice lower in pitch?

- **Correct:** Added mass slows vibration
- Distractor: Recurrent laryngeal nerve weakness — _why wrong:_ Nerve weakness causes breathiness, not a deeper voice from added mass.
- Distractor: Increased cricothyroid tension — _why wrong:_ Increased tension would raise pitch.
- Distractor: Thickened vocal ligaments — _why wrong:_ The fluid accumulates in the superficial lamina propria, above the ligament.

Explanation: Smoking increases vascular permeability in Reinke space (superficial lamina propria), so fluid accumulates and the folds become heavier, lowering fundamental frequency. Smoking cessation is essential; microflap suction reduces bulk.

Pearl: Deep voice in a heavy smoker with floppy folds = Reinke edema.

## T-laryngology-28 — Spasmodic Dysphonia
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-28.overview**

Spasmodic dysphonia is a focal laryngeal dystonia causing task-specific, involuntary spasms during speech: adductor (strained, strangled breaks) or abductor (breathy breaks). Botulinum toxin injection is first-line treatment.

**T-laryngology-28.physiology**

**Basal ganglia circuits**: modulate motor control and inhibit unwanted movements. **Task specificity**: laryngeal motor control differs for speech, laughing, and singing. **Neuromuscular junction**: acetylcholine release triggers muscle contraction.

**T-laryngology-28.pathophysiology**

**Dystonia**: abnormal sensorimotor integration and reduced inhibition in basal ganglia and cortex. **Adductor SD**: thyroarytenoid spasms cause strained voice breaks on vowels. **Abductor SD**: posterior cricoarytenoid spasms cause breathy breaks on voiceless consonants. **Task specificity**: laughing and singing are often spared. **Botulinum toxin**: blocks acetylcholine release, weakening the dystonic muscle temporarily.

### CC-laryngology-28.1 (concept check)

Stem: A 45-year-old has 2 years of strained, strangled voice breaks on vowels during conversation, but she sings and laughs with a normal voice. Laryngoscopy shows normal structure. What is the mechanism?

- **Correct:** Task-specific adductor dystonia
- Distractor: Unilateral vocal fold paralysis — _why wrong:_ Paralysis produces breathiness and is not task-specific.
- Distractor: Primary muscle tension dysphonia — _why wrong:_ MTD is not task-specific and usually responds to voice therapy.
- Distractor: Bilateral vocal fold nodules — _why wrong:_ Nodules cause constant hoarseness and are visible on laryngoscopy.

Explanation: Spasmodic dysphonia is a focal laryngeal dystonia from abnormal basal ganglia and sensorimotor integration. Adductor spasms of the thyroarytenoid break the voice on vowels; singing and laughing use different motor programs and are often spared. Botulinum toxin is first-line.

Pearl: Strangled voice breaks with normal singing = adductor spasmodic dysphonia.

## T-laryngology-29 — Stroboscopy Interpretation
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-29.overview**

Videostroboscopy uses flashing light slightly out of phase with vocal fold vibration to create an apparent slow-motion view of the mucosal wave. It is essential for diagnosing subtle lesions, scar, and paresis, and pairs with perceptual ratings (GRBAS, CAPE-V) and patient-reported VHI-10.

**T-laryngology-29.physiology**

**Stroboscopic principle**: the eye fuses images; a light flashing at a frequency slightly different from vibration samples successive points of different cycles, creating an illusion of slow motion. **Periodicity requirement**: stroboscopy needs reasonably periodic vibration; severely aperiodic voices are better assessed with high-speed imaging. **Parameters**: glottic closure pattern, symmetry, periodicity, amplitude, mucosal wave, vertical level, and nonvibrating segments. **Mucosal wave**: reflects the pliability of the superficial lamina propria.

**T-laryngology-29.pathophysiology**

**Reduced or absent mucosal wave**: stiffness from scar, sulcus, or invasive cancer (adynamic segment). **Asymmetry**: unilateral stiffness, mass, or paresis. **Closure patterns**: hourglass (bilateral nodules), anterior gap (presbylarynx), posterior gap (normal in many women), spindle (bowing). **Cyst vs nodule**: cysts dampen the wave locally and are often unilateral with a reactive contralateral lesion. **Malignancy clue**: a nonvibrating segment in a leukoplakic lesion suggests invasion.

### CC-laryngology-29.1 (concept check)

Stem: A 50-year-old singer has hoarseness. Stroboscopy shows a small leukoplakic lesion on the right vocal fold with an absent mucosal wave over the lesion. Why is this finding concerning?

- **Correct:** It suggests invasion or scar
- Distractor: It is typical of vocal fold nodules — _why wrong:_ Nodules preserve the mucosal wave and are bilateral.
- Distractor: It indicates muscle tension dysphonia — _why wrong:_ MTD does not cause absent mucosal waves.
- Distractor: It means the light was out of phase — _why wrong:_ A focal adynamic segment is real, not an artifact.

Explanation: The mucosal wave depends on a pliable superficial lamina propria. A focal nonvibrating segment in a white lesion suggests invasion or scar and warrants biopsy.

Pearl: Leukoplakia with an adynamic segment needs tissue.

## T-laryngology-30 — Subglottic / Tracheal Stenosis
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-30.overview**

Adult subglottic and tracheal stenosis is narrowing from intubation injury, idiopathic subglottic stenosis, granulomatosis with polyangiitis, or trauma. Treatment ranges from endoscopic dilation and steroid injection to cricotracheal or tracheal resection.

**T-laryngology-30.physiology**

**Cricoid ring**: complete and nonexpansile, so mucosal swelling or scar directly narrows the lumen. **Mucosal perfusion pressure**: about 25-35 mm Hg; cuff pressures above this cause ischemia. **Airflow physics**: resistance rises steeply as the radius falls, so symptoms appear late, then progress quickly. **Normal healing**: respiratory mucosa regenerates over denuded areas if the underlying perichondrium is preserved.

**T-laryngology-30.pathophysiology**

**Intubation injury**: tube or cuff pressure causes ischemia, ulceration, perichondritis, granulation, and contracting scar. **Tracheostomy-related**: stoma site granulation, A-frame deformity, and cuff injury. **Idiopathic subglottic stenosis**: occurs almost exclusively in women, with estrogen-related fibroinflammatory scar of the subglottis and upper trachea. **GPA**: necrotizing granulomatous inflammation causes subglottic stenosis, often the presenting site. **Symptoms**: exertional dyspnea and stridor, often misdiagnosed as asthma. **Classification**: Myer-Cotton (percent obstruction) and McCaffrey (location and length) guide treatment. **Recurrence**: dilation often needs repeating; resection with anastomosis offers durable results for appropriate lesions.

## T-laryngology-31 — Tracheobronchial Endoscopy Principles
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-31.overview**

Tracheobronchial endoscopy (rigid and flexible bronchoscopy) diagnoses and treats airway lesions, stenosis, and foreign bodies. Rigid bronchoscopy allows ventilation and large instruments.

**T-laryngology-31.physiology**

**Airway tree**: the trachea divides at the carina into main bronchi, then lobar and segmental bronchi; the right main bronchus is shorter and more vertical in adults. **Dynamic airway**: intrathoracic airways narrow during expiration, so malacia is assessed with spontaneous breathing. **Ventilation during endoscopy**: rigid scopes allow ventilation through the scope, while flexible scopes partially obstruct the airway. **Mucosal sensitivity**: the carina and trachea are highly reflexogenic.

**T-laryngology-31.pathophysiology**

**Rigid bronchoscopy**: controlled airway, foreign body removal, and dilation. **Flexible bronchoscopy**: dynamic assessment and distal access. **Complications**: bleeding, perforation, and hypoxia. **Dynamic collapse**: assessed with spontaneous breathing.

### CC-laryngology-31.1 (concept check)

Stem: A 1-year-old aspirated a peanut. Why is rigid rather than flexible bronchoscopy preferred for removal?

- **Correct:** It keeps ventilation secure
- Distractor: It avoids the need for general anesthesia — _why wrong:_ Rigid bronchoscopy requires general anesthesia.
- Distractor: It reaches the distal segmental bronchi better — _why wrong:_ Flexible scopes reach more distal airways.
- Distractor: It can be done in the office — _why wrong:_ Rigid bronchoscopy is performed in the operating room.

Explanation: The rigid bronchoscope maintains a secure airway while the patient is ventilated through it, and allows optical forceps to grasp and remove organic material without fragmenting it into a smaller airway.

Pearl: Pediatric airway foreign body: rigid bronchoscopy.

## T-laryngology-32 — Transnasal Esophagoscopy
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-32.overview**

Transnasal esophagoscopy is unsedated in-office esophageal examination through the nose. It screens for esophagitis, Barrett esophagus, and cancer and allows biopsy.

**T-laryngology-32.physiology**

**Nasal route**: passing an ultrathin endoscope through the nose avoids the base of tongue and the strong gag reflex. **Esophageal anatomy**: the scope traverses the UES, the cervical and thoracic esophagus, and the squamocolumnar junction (Z-line). **Mucosal types**: squamous esophageal mucosa normally meets columnar gastric mucosa at the gastroesophageal junction. **Air insufflation**: distends the esophagus for inspection.

**T-laryngology-32.pathophysiology**

**Unsedated advantage**: fewer complications and lower cost. **Barrett esophagus**: intestinal metaplasia from chronic reflux. **Second primaries**: screening in head and neck cancer patients. **Limitations**: gastric examination and therapeutics are limited.

### CC-laryngology-32.1 (concept check)

Stem: A head and neck cancer survivor with reflux needs esophageal screening but does not want sedation. Why is transnasal esophagoscopy well tolerated without sedation?

- **Correct:** The nasal route avoids the gag reflex
- Distractor: It does not enter the esophagus — _why wrong:_ TNE examines the full esophagus.
- Distractor: It uses no air insufflation — _why wrong:_ Air insufflation is used to distend the esophagus.
- Distractor: It is performed under general anesthesia — _why wrong:_ It is performed in the office without sedation.

Explanation: Passing an ultrathin scope through the nose avoids the tongue base and oropharyngeal gag. TNE screens for esophagitis, Barrett esophagus, and second primary cancers and allows biopsy.

Pearl: Unsedated esophageal screening: TNE.

## T-laryngology-33 — Unilateral Vocal Fold Paralysis
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-33.overview**

Unilateral vocal fold paralysis causes a breathy, weak voice, vocal fatigue, and aspiration from incomplete glottic closure. It is iatrogenic (thyroid, cardiothoracic, cervical spine surgery), neoplastic, or idiopathic, and is treated with injection, medialization thyroplasty, arytenoid adduction, or reinnervation.

**T-laryngology-33.physiology**

**Recurrent laryngeal nerve**: supplies all intrinsic laryngeal muscles except the cricothyroid; the left RLN loops under the aortic arch, the right under the subclavian, which is why the left is injured more often (longer intrathoracic course). **Adduction and abduction**: the lateral cricoarytenoid, interarytenoid, and thyroarytenoid adduct; the posterior cricoarytenoid alone abducts. **Glottic closure for voice**: the folds must meet in the midline to set up vibration; for cough and swallow, firm closure builds subglottic pressure and protects the airway. **Superior laryngeal nerve**: provides supraglottic sensation (internal branch) and cricothyroid motor (external branch, pitch). **Synkinetic reinnervation**: after injury, regrowing axons often reinnervate both adductors and abductors, producing a fold with tone but no purposeful motion.

**T-laryngology-33.pathophysiology**

**Glottic gap**: a paralyzed fold sits in a paramedian or lateral position, so air escapes during phonation (breathy voice, short phonation time). **Muscle atrophy**: denervated thyroarytenoid muscle thins, bowing the fold and widening the gap over months; synkinetic reinnervation can preserve bulk and position. **Vertical level mismatch**: the paralyzed fold may sit higher or lower, further impairing closure. **Aspiration**: glottic incompetence plus reduced supraglottic sensation (if the vagus is injured high) cause aspiration of thin liquids. **Lesion level matters**: high vagal lesions (skull base) also paralyze the pharynx and reduce sensation, causing worse dysphagia than isolated RLN injury. **Treatment logic**: injection or thyroplasty medializes the fold to close the gap; arytenoid adduction corrects a large posterior gap and level mismatch; reinnervation restores tone and bulk. **Workup**: imaging from skull base to aortic arch when no iatrogenic cause, to exclude tumor along the nerve course.

### CC-laryngology-33.1 (concept check)

Stem: A 55-year-old has a breathy voice and coughs on thin liquids 3 weeks after a left pneumonectomy. Laryngoscopy shows the left vocal fold immobile in a paramedian position with a glottic gap. Why is the left side injured far more often than the right in chest surgery?

- **Correct:** The left RLN loops under the aortic arch
- Distractor: The left vagus has no cardiac branches — _why wrong:_ Both vagi give cardiac branches; the difference is the left RLN's long intrathoracic course.
- Distractor: The left RLN supplies the cricothyroid — _why wrong:_ The cricothyroid is supplied by the external branch of the superior laryngeal nerve on both sides.
- Distractor: The right RLN is protected by the thyroid — _why wrong:_ The right RLN loops under the subclavian artery in the neck; thyroid position is not the reason.

Explanation: The left recurrent laryngeal nerve descends into the chest and loops under the aortic arch near the ligamentum arteriosum before ascending, so thoracic surgery and mediastinal disease injure it more often. Injection or thyroplasty closes the gap, improving voice and aspiration.

Pearl: Unexplained left vocal fold paralysis: image from skull base to aortic arch.

## T-laryngology-34 — Vocal Fold Nodules
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-34.overview**

Vocal fold nodules are bilateral, symmetric benign thickenings at the junction of the anterior and middle thirds of the membranous folds. They are caused by chronic phonotrauma, common in children, teachers, and singers, and are treated primarily with voice therapy.

**T-laryngology-34.physiology**

**Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. **Maximal collision zone**: the midpoint of the membranous fold experiences the greatest impact stress during vibration. **Basement membrane zone**: type IV collagen and anchoring fibers resist shear. **Vocal hygiene**: hydration and efficient phonation lower collision forces.

**T-laryngology-34.pathophysiology**

**Repetitive impact**: chronic loud or effortful voice use repeatedly stresses the midpoint. **Tissue response**: basement membrane thickening, edema, and fibronectin deposition produce symmetric bumps. **Hourglass closure**: nodules prevent full closure anterior and posterior to them, causing breathiness and hoarseness. **Reversibility**: early soft nodules regress with behavior change; mature fibrotic nodules may need surgery. **Children**: nodules often improve at puberty.

### CC-laryngology-34.1 (concept check)

Stem: A 9-year-old boy who yells on the playground has a hoarse voice. Laryngoscopy shows small, symmetric bilateral midfold nodules. What is the first-line treatment?

- **Correct:** Voice therapy
- Distractor: Microlaryngoscopic excision — _why wrong:_ Surgery is rarely needed in children and is reserved for failure of therapy.
- Distractor: Proton pump inhibitor therapy — _why wrong:_ Reflux is not the main driver of pediatric nodules.
- Distractor: Inhaled corticosteroids — _why wrong:_ Steroids do not treat phonotraumatic nodules.

Explanation: Nodules result from repetitive impact stress; reducing phonotrauma lets early lesions regress. Pediatric nodules often improve at puberty.

Pearl: Nodules: therapy first.

## T-laryngology-35 — Vocal Fold Polyp / Cyst
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-35.overview**

Vocal fold polyps are usually unilateral, exophytic lesions often after vocal hemorrhage; cysts are subepithelial mucus retention or epidermoid lesions. Both disrupt vibration and are often treated with microsurgery after therapy.

**T-laryngology-35.physiology**

**Body-cover model**: the vocal fold is a layered vibrator: epithelium and superficial lamina propria (Reinke space) form a pliable cover; the intermediate and deep lamina propria (vocal ligament) form a transition; the vocalis (thyroarytenoid) muscle forms the body. **Microvasculature**: superficial lamina propria vessels run parallel to the fold edge and are fragile. **Mucous glands**: located in the ventricle and subglottis, not the free edge.

**T-laryngology-35.pathophysiology**

**Hemorrhagic polyp**: vessel rupture during phonotrauma causes hemorrhage into Reinke space, organizing into a polyp; anticoagulants increase risk. **Mucus retention cyst**: obstruction of a gland duct. **Epidermoid cyst**: trapped epithelium, possibly congenital or from healing. **Contact reaction**: the opposite fold develops a reactive lesion. **Surgery**: microflap excision preserves the superficial lamina propria.

### CC-laryngology-35.1 (concept check)

Stem: A 40-year-old on aspirin developed sudden hoarseness after shouting at a sporting event. Laryngoscopy shows a unilateral hemorrhagic polyp on the left vocal fold. What mechanism produced it?

- **Correct:** Ruptured lamina propria vessel
- Distractor: Obstruction of a mucous gland duct — _why wrong:_ That mechanism forms a mucus retention cyst, not a hemorrhagic polyp.
- Distractor: Chronic smoking-related edema — _why wrong:_ Smoking causes diffuse Reinke edema, not an acute focal hemorrhagic polyp.
- Distractor: Viral papilloma infection — _why wrong:_ Papillomas are HPV lesions, not hemorrhage-related.

Explanation: Fragile vessels in the superficial lamina propria rupture during phonotrauma, especially with antiplatelet agents. Hemorrhage organizes into a polyp, which often requires microflap excision.

Pearl: Sudden hoarseness after shouting: think vocal fold hemorrhage and rest the voice.

## T-laryngology-36 — Vocal Fold Sulcus / Scar
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-36.overview**

Vocal fold sulcus and scar are loss of the pliable superficial lamina propria, causing a stiff, adynamic cover with poor vibration. They are among the hardest voice problems to treat.

**T-laryngology-36.physiology**

**Superficial lamina propria**: loose, gel-like tissue with hyaluronic acid and sparse fibers that lets the cover move. **Mucosal wave**: requires a pliable cover over a stiffer body. **Glottic closure**: depends on fold contour.

**T-laryngology-36.pathophysiology**

**Sulcus vergeture**: a groove where epithelium attaches to the vocal ligament, possibly congenital or from ruptured epidermoid cysts. **Scar**: injury from surgery, phonotrauma, or radiation replaces the superficial lamina propria with dense collagen. **Vibration loss**: stiff cover reduces the mucosal wave and creates a spindle gap. **Treatment limits**: injections improve closure but not pliability; microflap release and grafting have variable results.

### CC-laryngology-36.1 (concept check)

Stem: A 40-year-old has had a weak, rough voice since prior vocal fold surgery. Stroboscopy shows a stiff segment of the left fold with an absent mucosal wave and a spindle gap. Why is this so difficult to treat?

- **Correct:** The pliable cover layer is lost
- Distractor: The recurrent laryngeal nerve is cut — _why wrong:_ Mobility is preserved; the problem is the vibrating cover.
- Distractor: The thyroid cartilage is fractured — _why wrong:_ Framework injury is not the problem.
- Distractor: The fold has active infection — _why wrong:_ There is no infection.

Explanation: The superficial lamina propria normally lets the cover ripple. Scar replaces it with dense collagen, so the cover cannot vibrate. Injection improves closure but not pliability; release and grafting have variable results.

Pearl: Protect the superficial lamina propria: scar is hard to fix.

## T-laryngology-37 — Vocal Process Granuloma
_source: pathophys_v470/laryngology_c.py_

**T-laryngology-37.overview**

Vocal process granulomas are benign inflammatory masses on the posterior vocal folds from intubation, reflux, or phonotrauma (throat clearing, harsh voice). Most resolve with treating causes, and recurrence after excision is common.

**T-laryngology-37.physiology**

**Vocal process**: the arytenoid cartilage projection covered by thin mucoperichondrium. **Posterior glottic contact**: the vocal processes collide during adduction. **Healing**: perichondrial injury produces granulation.

**T-laryngology-37.pathophysiology**

**Mucoperichondrial injury**: endotracheal tube pressure, forceful adduction, or throat clearing ulcerates the thin mucosa. **Granulation**: chronic irritation sustains granulation tissue. **Reflux role**: often treated though evidence is mixed. **Treatment**: voice therapy, reflux management, botulinum toxin to reduce adduction force, and steroid injection; excision recurs.

### CC-laryngology-37.1 (concept check)

Stem: A 45-year-old executive who frequently clears his throat and speaks forcefully has a smooth, pale mass on the left vocal process. It recurred 3 months after excision. What is the most effective long-term strategy?

- **Correct:** Reduce the injuring forces
- Distractor: Repeat excision every few months — _why wrong:_ Repeated excision recurs because the cause persists.
- Distractor: Radiation therapy — _why wrong:_ Radiation is not used for benign granulomas.
- Distractor: Long-term antibiotics — _why wrong:_ Granulomas are not infections.

Explanation: The thin mucoperichondrium over the vocal process ulcerates from forceful adduction, throat clearing, or intubation. Voice therapy, reflux management, and botulinum toxin to reduce adduction force let it heal; excision alone recurs.

Pearl: Granuloma: treat the cause, not just the lesion.

## T-laryngology-38 — Vocal Tremor
_source: pathophys_v470/laryngology_b.py_

**T-laryngology-38.overview**

Vocal tremor is rhythmic oscillation of pitch and loudness from involuntary laryngeal and pharyngeal movements, often part of essential tremor. Botulinum toxin and medications reduce symptoms.

**T-laryngology-38.physiology**

**Motor control loops**: smooth voluntary movement depends on cerebellar-thalamocortical and basal ganglia loops that dampen oscillation. **Physiologic tremor**: everyone has a small, high-frequency tremor that is normally inaudible. **Voice production structures**: the larynx, pharynx, palate, tongue, and respiratory muscles all contribute to sustained phonation. **Pitch and loudness control**: cricothyroid and thyroarytenoid activity set pitch; subglottic pressure sets loudness.

**T-laryngology-38.pathophysiology**

**Essential tremor**: abnormal rhythmic oscillation in cerebellar-thalamocortical circuits produces 4-8 Hz tremor in the hands, head, and voice. **Laryngeal involvement**: rhythmic adduction-abduction or vertical laryngeal movement modulates pitch and loudness, most audible on sustained vowels. **Multisite tremor**: palate, pharynx, and tongue tremor contribute, limiting botulinum toxin to the folds alone. **Overlap with spasmodic dysphonia**: dystonic tremor and SD coexist, complicating diagnosis. **Treatment logic**: botulinum toxin weakens tremulous muscles; propranolol and primidone reduce central oscillation; deep brain stimulation helps some patients.

### CC-laryngology-38.1 (concept check)

Stem: A 68-year-old with hand tremor has a voice that wavers rhythmically about 5 times per second, most obvious on a sustained vowel. Laryngoscopy shows rhythmic movement of the larynx, palate, and pharyngeal walls. What is the likely diagnosis?

- **Correct:** Essential voice tremor
- Distractor: Adductor spasmodic dysphonia — _why wrong:_ SD causes irregular, task-specific breaks rather than regular rhythmic oscillation.
- Distractor: Presbyphonia — _why wrong:_ Presbyphonia causes weak breathy voice without rhythmic oscillation.
- Distractor: Muscle tension dysphonia — _why wrong:_ MTD causes strained voice without regular tremor.

Explanation: Essential tremor arises from cerebellar-thalamocortical oscillation and often involves the hands and voice at about 4-8 Hz. Multisite tremor limits botulinum toxin benefit; propranolol and primidone help some patients.

Pearl: Rhythmic voice wavering on sustained vowels = vocal tremor.

## T-laryngology-39 — Zenker Diverticulum
_source: pathophys_v470/laryngology_a.py_

**T-laryngology-39.overview**

Zenker diverticulum is a posterior pharyngoesophageal pulsion diverticulum through Killian dehiscence above the cricopharyngeus. It causes dysphagia, regurgitation of undigested food, and aspiration, and is treated with endoscopic or open cricopharyngeal myotomy.

**T-laryngology-39.physiology**

**Killian dehiscence**: a weak area between the oblique fibers of the inferior constrictor (thyropharyngeus) and the transverse cricopharyngeus. **UES opening**: requires cricopharyngeal relaxation and hyolaryngeal elevation. **Pharyngeal pressure**: swallow generates high pressure above the UES.

**T-laryngology-39.pathophysiology**

**Noncompliant UES**: fibrotic, poorly relaxing cricopharyngeus increases hypopharyngeal pressure during swallowing. **Pulsion**: pressure pushes mucosa and submucosa out through Killian dehiscence. **Symptoms**: dysphagia, regurgitation, halitosis, gurgling, and aspiration. **Myotomy logic**: dividing the cricopharyngeus relieves outflow resistance, and the common wall division drains the pouch.

### CC-laryngology-39.1 (concept check)

Stem: A 74-year-old has progressive dysphagia, regurgitation of undigested food hours after meals, halitosis, and gurgling in the neck. Barium swallow shows a posterior pouch above the cricopharyngeus. What is the underlying mechanism?

- **Correct:** A noncompliant cricopharyngeus
- Distractor: Weakness of the lower esophageal sphincter — _why wrong:_ LES incompetence causes reflux, not a pharyngoesophageal pouch.
- Distractor: Traction from mediastinal lymph nodes — _why wrong:_ Traction diverticula are midesophageal and full-thickness, not Zenker type.
- Distractor: Congenital weakness of the trachea — _why wrong:_ The trachea is not involved in Zenker diverticulum.

Explanation: A poorly compliant cricopharyngeus raises hypopharyngeal pressure during swallowing, pushing mucosa and submucosa out through Killian dehiscence. Dividing the cricopharyngeus (endoscopic or open) relieves the outflow obstruction.

Pearl: Regurgitation of old food in an older adult = Zenker; treat the cricopharyngeus.


---

# Facial Plastics / Trauma

## T-facial_plastics-1 — Aesthetic Facial Analysis
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-1.overview**

Aesthetic facial analysis uses proportions, angles, and landmarks to evaluate faces before surgery. It helps plan rhinoplasty, chin augmentation, and facial rejuvenation.

**T-facial_plastics-1.physiology**

**Facial thirds**: trichion-glabella, glabella-subnasale, subnasale-menton roughly equal. **Facial fifths**: width equal to five eye widths. **Nasal angles**: nasofrontal about 115-130, nasolabial about 90-110 (men) and 95-115 (women).

**T-facial_plastics-1.pathophysiology**

**Disproportion guides treatment**: deviations from ideal proportions point to the anatomic source (e.g., a long lower third, retrusive chin, or overprojected nasal tip). **Chin-nose interplay**: microgenia makes the nose look larger, so chin augmentation is considered alongside rhinoplasty. **Aging changes**: volume loss, ligament laxity, and bony resorption alter proportions over time. **Skin quality**: thickness and elasticity limit what surgery can achieve. **Ethnic variation**: ideal proportions vary across ethnicities, and analysis should respect patient goals rather than a single template.

## T-facial_plastics-2 — Aging Face / Injectables / Resurfacing
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-2.overview**

Facial aging reflects skin changes, volume loss, and soft-tissue descent. Treatment combines neuromodulators, fillers, resurfacing, and surgery.

**T-facial_plastics-2.physiology**

**Skin layers**: epidermis, dermis rich in collagen and elastin, and subcutaneous fat organized into distinct compartments. **Retaining ligaments**: anchor skin and soft tissue to bone. **Muscle action**: repetitive contraction of muscles of expression creates dynamic rhytids perpendicular to muscle pull. **Bone framework**: supports soft tissue projection.

**T-facial_plastics-2.pathophysiology**

**Collagen and elastin loss**: intrinsic aging and photoaging thin the dermis and reduce elasticity. **Fat compartment changes**: deep fat atrophies and superficial fat descends, causing hollowing and jowling. **Bony resorption**: the orbits widen and the maxilla and mandible recede, reducing support. **Ligament laxity**: soft tissues descend. **Botulinum toxin**: blocks acetylcholine release, relaxing dynamic lines. **Fillers**: restore volume; intravascular injection can cause skin necrosis or blindness (via ophthalmic artery anastomoses). **Resurfacing**: controlled injury stimulates collagen remodeling.

### CC-facial_plastics-2.1 (concept check)

Stem: While receiving hyaluronic acid filler to the glabella, a patient suddenly reports severe eye pain and loss of vision in the right eye, with blanching of the overlying skin. What is the mechanism?

- **Correct:** Filler embolized into the ophthalmic circulation
- Distractor: Acute allergic reaction to the filler — _why wrong:_ Allergy causes swelling or urticaria, not sudden monocular vision loss.
- Distractor: Direct filler compression of the optic nerve — _why wrong:_ Filler injected in the glabella does not reach the optic nerve directly.
- Distractor: Retinal detachment from injection pressure — _why wrong:_ Retinal detachment is not caused by superficial facial injection.

Explanation: Filler entering the supratrochlear or dorsal nasal artery can travel retrograde into ophthalmic artery branches and occlude the central retinal artery. Stop injecting, give hyaluronidase, and get emergent ophthalmology care.

Pearl: Glabellar and nasal filler can blind: know the vascular anatomy.

## T-facial_plastics-3 — Alar Retraction / Nasal Vestibular Stenosis
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-3.overview**

Alar retraction and nasal vestibular stenosis are external valve problems from overresection, scar, or congenital deficiency, causing obstruction and cosmetic deformity. Treatment uses cartilage and composite grafts.

**T-facial_plastics-3.physiology**

**External nasal valve**: the vestibule framed by the lateral crus, alar soft tissue, columella, and sill. **Alar-columellar relationship**: on profile, about 2-4 mm of columella shows below the alar rim. **Alar support**: the alar rim itself has no cartilage; support comes from the lateral crus and soft tissue. **Vestibular lining**: skin-lined; scarring narrows the lumen.

**T-facial_plastics-3.pathophysiology**

**Overresection**: excessive cephalic trim of the lateral crura removes support, letting the alar rim retract upward and collapse inward. **Lining deficiency**: trauma, burns, or prior surgery scar the vestibule, shortening the lining and pulling the rim up. **Vestibular stenosis**: circumferential scar narrows the external valve, causing obstruction. **Dynamic collapse**: weak sidewalls collapse on inspiration. **Repair logic**: alar rim grafts and lateral crural strut grafts restore support; composite grafts add lining length; scar release with grafting for stenosis.

### CC-facial_plastics-3.1 (concept check)

Stem: Two years after a reduction rhinoplasty with aggressive cephalic trim, a patient's alar rims have retracted upward, showing too much columella, and collapse inward on deep inspiration. What caused this?

- **Correct:** Overresection of the lateral crura
- Distractor: Excessive resection of septal cartilage — _why wrong:_ Septal overresection weakens dorsal and tip support, not the alar rim.
- Distractor: Aggressive inferior turbinate reduction — _why wrong:_ Turbinates do not support the alar rim or external valve.
- Distractor: Lateral nasal bone osteotomies — _why wrong:_ Osteotomies narrow the bony vault and do not retract the alar rim.

Explanation: The lateral crus supports the alar rim and external valve. Excessive cephalic trim removes that support, so scar contracture retracts the rim and the sidewall collapses on inspiration. Alar rim grafts and lateral crural strut grafts restore support.

Pearl: Retracted, collapsing ala after rhinoplasty = lateral crural overresection.

## T-facial_plastics-4 — Auricular Reconstruction
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-4.overview**

Auricular reconstruction restores the ear after trauma, tumor, or microtia, using cartilage frameworks, flaps, and grafts. Nagata, Brent, and Tanzer techniques shaped modern reconstruction.

**T-facial_plastics-4.physiology**

**Elastic cartilage**: the auricular framework is elastic cartilage that depends on overlying perichondrium for nutrition. **Thin anterior skin**: tightly adherent to cartilage on the lateral surface with little subcutaneous tissue; posterior skin is looser. **Blood supply**: posterior auricular and superficial temporal arteries. **Three-dimensional contour**: helix, antihelix, concha, tragus, and lobule create a complex surface that is hard to recreate.

**T-facial_plastics-4.pathophysiology**

**Cartilage exposure and necrosis**: cartilage without vascularized coverage dies and becomes infected, so exposed cartilage needs coverage by flaps. **Hematoma**: blood separating perichondrium from cartilage causes necrosis and fibrocartilage overgrowth (cauliflower ear). **Partial defects**: helical rim advancement (Antia-Buch), conchal composite grafts, and postauricular flaps preserve contour. **Total reconstruction**: rib cartilage frameworks (Brent, Nagata) or porous polyethylene under temporoparietal fascia. **Infection**: Pseudomonas perichondritis after piercing destroys cartilage.

## T-facial_plastics-5 — Bilobed Flap
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-5.overview**

The bilobed flap is a double transposition flap for nasal defects up to about 1.5 cm, especially on the lower third of the nose. The Zitelli modification reduces the total arc to about 90-100 degrees, minimizing standing cones.

**T-facial_plastics-5.physiology**

**Nasal skin mobility**: upper nasal skin is mobile; lower nasal skin is thick and fixed. **Random blood supply**: subdermal plexus. **Tension redistribution**: each lobe transfers tension further from the defect.

**T-facial_plastics-5.pathophysiology**

**Tension shifting**: the primary lobe fills the defect, the secondary lobe fills the primary donor site, and the donor of the secondary closes primarily in mobile skin. **Zitelli design**: each lobe rotates about 45-50 degrees. **Trapdoor deformity**: curvilinear scar contraction. **Alar distortion**: if tension pulls toward the alar rim.

## T-facial_plastics-6 — Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-6.overview**

Blepharoplasty addresses excess eyelid skin and fat; eyelid malpositions (ptosis, ectropion, entropion) affect function and appearance. Eyelid anatomy and lid laxity testing prevent complications.

**T-facial_plastics-6.physiology**

**Upper eyelid elevation**: the levator palpebrae superioris (CN III) and Müller muscle (sympathetic, 1-2 mm). **Orbital septum**: a fibrous layer separating the eyelid from orbital fat. **Lower lid support**: tarsus and medial and lateral canthal tendons. **Lacrimal pump**: orbicularis contraction drives tears into the drainage system.

**T-facial_plastics-6.pathophysiology**

**Dermatochalasis**: excess skin from aging. **Steatoblepharon**: orbital fat herniation through a weakened septum. **Involutional ptosis**: levator aponeurosis dehiscence with a high lid crease. **Ectropion**: horizontal lid laxity, scar, or facial paralysis. **Entropion**: lid inward rotation. **Retrobulbar hemorrhage**: vision-threatening; lateral canthotomy. **Lower lid malposition after blepharoplasty**: from excessive skin removal.

### CC-facial_plastics-6.1 (concept check)

Stem: A 70-year-old has tearing and irritation from an everted right lower lid. The lid can be pulled more than 6 mm from the globe and snaps back slowly. What is the main mechanism?

- **Correct:** Horizontal laxity of the lower lid
- Distractor: Facial nerve paralysis — _why wrong:_ Paralytic ectropion requires facial weakness, which is not described.
- Distractor: Herniated orbital fat — _why wrong:_ Fat herniation causes lower lid bags, not eversion.
- Distractor: Levator aponeurosis dehiscence — _why wrong:_ Levator dehiscence causes upper lid ptosis.

Explanation: Age-related stretching of the tarsus and canthal tendons lets the lid fall away from the globe, causing exposure and tearing. Lid distraction and snap-back tests confirm it; a lateral tarsal strip tightens the lid.

Pearl: Lax lower lid causing ectropion: tighten it with a lateral tarsal strip.

## T-facial_plastics-7 — Cervicofacial Flap
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-7.overview**

The cervicofacial flap is a large rotation-advancement flap for cheek defects, recruiting lax neck skin. It requires wide undermining in the subcutaneous or sub-SMAS plane.

**T-facial_plastics-7.physiology**

**Laxity reservoir**: the lower cheek and neck have abundant lax skin. **Blood supply**: facial and submental perforators feed the subdermal plexus, and deeper flaps capture SMAS perfusion. **Gravity**: inferiorly based tissue pulled upward tends to descend over time.

**T-facial_plastics-7.pathophysiology**

**Rotation-advancement**: moves cheek and neck skin superiorly and medially. **Ectropion**: lower eyelid tension pulls the lid downward, prevented by anchoring to the orbital rim periosteum. **Distal tip necrosis**: smoking and thin flaps. **Deep-plane flaps**: improve vascularity.

## T-facial_plastics-8 — Facial Nerve Reanimation
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-8.overview**

Facial reanimation restores tone, symmetry, and movement after facial paralysis using nerve repair, grafts, nerve transfers, muscle transfers, and static procedures. The duration of denervation and status of facial muscles drive the choice.

**T-facial_plastics-8.physiology**

**Facial nerve**: motor supply to the muscles of facial expression via five branches. **Wallerian degeneration**: distal axons degenerate after transection. **Neuromuscular junction survival**: denervated facial muscles remain receptive to reinnervation for roughly 12-24 months before fibrosis and atrophy. **Axonal regeneration**: about 1 mm per day. **Cortical plasticity**: allows retraining after nerve transfer.

**T-facial_plastics-8.pathophysiology**

**Primary repair**: tension-free coaptation gives the best results. **Cable grafts**: bridge gaps using great auricular or sural nerve. **Nerve transfers**: masseteric (strong, quick) or hypoglossal donors restore movement when the proximal facial nerve is unavailable, if muscles are still viable (within about 12-24 months). **Free functional muscle transfer**: gracilis transfer for long-standing paralysis when native muscles are atrophied. **Synkinesis**: misdirected regeneration produces involuntary co-contraction. **Static procedures**: brow lift, gold weight, and slings for symmetry and eye protection.

### CC-facial_plastics-8.1 (concept check)

Stem: A 45-year-old had facial nerve sacrifice during parotidectomy 18 months ago. EMG shows fibrillation potentials in facial muscles. Why can a masseteric nerve transfer still work?

- **Correct:** Its muscles are still viable
- Distractor: Facial muscles never atrophy — _why wrong:_ Facial muscles atrophy and fibrose after about 12-24 months.
- Distractor: The masseter replaces facial muscles — _why wrong:_ The masseteric nerve provides axons; facial muscles are reinnervated.
- Distractor: Fibrillation means recovery — _why wrong:_ Fibrillations mean denervated but viable muscle.

Explanation: Fibrillation potentials show muscle that is denervated but still alive. Within about 12-24 months, nerve transfers can reinnervate native muscles; after that, free muscle transfer is needed.

Pearl: Fibrillations = viable muscle; time drives the choice of transfer.

## T-facial_plastics-9 — Facial Soft-Tissue Lacerations / Burns
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-9.overview**

Facial lacerations and burns require careful closure, nerve and duct assessment, and scar optimization. The face's rich blood supply allows conservative debridement and delayed closure.

**T-facial_plastics-9.physiology**

**Facial blood supply**: dense, redundant arterial supply allows survival of tissue that would die elsewhere and permits delayed closure. **Facial nerve depth**: branches lie deep to the SMAS and parotid-masseteric fascia, becoming superficial anterior to the masseter. **Parotid duct**: runs along the middle third of a line from the tragus to the mid upper lip. **Wound healing in the face**: rapid epithelialization and strong vascular support improve outcomes. **Skin tension lines**: guide closure orientation.

**T-facial_plastics-9.pathophysiology**

**Nerve injury**: lacerations lateral to a vertical line through the lateral canthus can injure facial nerve branches large enough to repair; repair within about 72 hours, while distal stimulation still works. **Parotid duct injury**: sialocele or fistula, repaired over a stent. **Bite wounds**: high bacterial load (Pasteurella, Eikenella) requiring irrigation and antibiotics. **Burn depth**: superficial heals without scarring; deep partial and full thickness burns scar and contract, especially around eyelids and lips. **Contracture**: myofibroblasts shorten scars across free margins.

## T-facial_plastics-10 — Facial Synkinesis / Static-Dynamic Rehabilitation
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-10.overview**

Facial synkinesis is involuntary co-contraction of facial muscles after aberrant regeneration of the facial nerve. Treatment includes neuromuscular retraining, botulinum toxin, selective neurectomy, and myectomy.

**T-facial_plastics-10.physiology**

**Facial nerve topography**: fibers for different facial regions are partly organized in fascicles that become distinct distally. **Axon regeneration**: after axonal injury, regrowing axons follow available endoneurial tubes at about 1 mm per day, without guidance to their original target. **Facial nucleus plasticity**: the nucleus and cortex adapt to altered input. **Muscle tone**: depends on baseline motor neuron firing.

**T-facial_plastics-10.pathophysiology**

**Aberrant regeneration**: axons originally destined for one muscle reinnervate another, so a single command (smile) activates unintended muscles (eye closure, platysma). **Hyperkinesis and hypertonicity**: increased resting tone narrows the palpebral fissure and deepens the nasolabial fold. **Crocodile tears**: salivary fibers regrow to the lacrimal gland, causing tearing with eating. **Grading**: the Sunnybrook system scores resting symmetry, voluntary movement, and synkinesis. **Treatment logic**: botulinum toxin weakens unwanted contraction; neuromuscular retraining improves selective control; selective neurectomy or myectomy removes antagonistic pull; static procedures improve symmetry.

### CC-facial_plastics-10.1 (concept check)

Stem: A year after a complete Bell palsy, a 40-year-old's left eye narrows and closes whenever she smiles, and her left cheek feels tight at rest. Facial movement has otherwise largely returned. What is the mechanism?

- **Correct:** Misdirected axonal regeneration
- Distractor: Persistent herpes simplex reactivation — _why wrong:_ Viral reactivation caused the palsy; it does not explain co-contraction during recovery.
- Distractor: Coexisting trigeminal nerve injury — _why wrong:_ Synkinesis is a facial nerve phenomenon; the trigeminal nerve is sensory to the face.
- Distractor: A small contralateral cortical stroke — _why wrong:_ Bell palsy is a peripheral lesion, and a stroke would not cause eye closure with smiling.

Explanation: After axonal injury, regenerating facial nerve fibers grow into the wrong endoneurial tubes, so a smile command also activates orbicularis oculi. Hypertonicity adds resting tightness. Botulinum toxin, neuromuscular retraining, and selective neurectomy help.

Pearl: Eye closing when smiling after facial palsy = synkinesis.

## T-facial_plastics-11 — Forehead Flap / Nasal Reconstruction
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-11.overview**

The paramedian forehead flap is the workhorse for large nasal defects, an axial flap based on the supratrochlear artery transferred in stages. It provides thick skin matching nasal tip and ala.

**T-facial_plastics-11.physiology**

**Supratrochlear artery**: exits the orbit about 1.7-2.2 cm from midline. **Forehead skin**: color and texture match nasal skin. **Staged transfer**: the pedicle remains attached for about 3 weeks until neovascularization from the recipient site.

**T-facial_plastics-11.pathophysiology**

**Axial perfusion**: the supratrochlear artery supports a long narrow pedicle. **Neovascularization**: recipient bed ingrowth allows pedicle division after about 3 weeks. **Three layers**: full-thickness defects need lining, cartilage support, and skin coverage. **Flap necrosis**: smoking and tension. **Donor site**: heals with acceptable scarring.

## T-facial_plastics-12 — Frontal Sinus Fracture
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-12.overview**

Frontal sinus fractures involve the anterior table, posterior table, or nasofrontal outflow tract. Management depends on outflow tract patency, posterior table displacement, and CSF leak, with a trend toward conservative management.

**T-facial_plastics-12.physiology**

**Anterior table**: thick bone forming the forehead contour. **Posterior table**: thinner bone separating the sinus from the frontal lobe dura. **Frontal outflow tract**: drains through the frontal recess into the middle meatus. **Mucosa**: respiratory mucosa that can regrow and form mucoceles if trapped.

**T-facial_plastics-12.pathophysiology**

**Anterior table fracture**: causes contour deformity. **Outflow tract injury**: blocks drainage, causing mucocele, mucopyocele, or chronic sinusitis years later. **Posterior table fracture**: may cause CSF leak, meningitis, and intracranial infection. **Trapped mucosa**: mucosa in fracture lines forms mucoceles. **Management evolution**: preservation and observation with endoscopic follow-up are favored when outflow is functional, versus obliteration or cranialization for severe injuries.

### CC-facial_plastics-12.1 (concept check)

Stem: A patient has a depressed anterior table frontal sinus fracture. CT shows the nasofrontal outflow tract is also disrupted. Why is the outflow tract injury the key decision point?

- **Correct:** Blocked drainage leads to mucoceles
- Distractor: It determines the cosmetic outcome — _why wrong:_ The anterior table determines contour; outflow determines infection risk.
- Distractor: It predicts CSF leak — _why wrong:_ Posterior table injury predicts CSF leak.
- Distractor: It indicates orbital entrapment — _why wrong:_ Outflow injury does not cause entrapment.

Explanation: If the outflow tract cannot drain, mucus is trapped, causing mucocele, mucopyocele, or infection years later. Management ranges from observation with endoscopic follow-up to obliteration or cranialization.

Pearl: Frontal sinus fracture: assess anterior table, posterior table, and outflow.

## T-facial_plastics-13 — Functional Nasal Obstruction
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-13.overview**

Functional nasal obstruction is reduced nasal airflow from structural causes (septal deviation, valve collapse, turbinate hypertrophy) or mucosal disease. Identifying the exact site, especially the internal and external nasal valves, determines whether septoplasty, turbinate reduction, or valve repair will help.

**T-facial_plastics-13.physiology**

**Nasal resistance**: the nose provides about half of total airway resistance, which helps generate negative intrathoracic pressure and lung inflation. **Internal nasal valve**: bounded by the septum, the caudal upper lateral cartilage, the head of the inferior turbinate, and the nasal floor; the septum-upper lateral cartilage angle is normally 10-15 degrees and this is the narrowest cross-section. **External nasal valve**: the nostril vestibule framed by the lateral crus, alar soft tissue, columella, and nasal sill. **Bernoulli effect**: as air accelerates through a narrow valve, lateral pressure drops, pulling weak sidewalls inward. **Poiseuille relationship**: resistance rises steeply with small decreases in radius. **Nasal cycle and mucosa**: turbinate erectile tissue changes valve area minute to minute.

**T-facial_plastics-13.pathophysiology**

**Static obstruction**: fixed narrowing from septal deviation, spurs, or turbinate bone. **Dynamic collapse**: weak or malpositioned lateral cartilages (from aging, trauma, or prior rhinoplasty overresection) collapse inward on inspiration. **Mucosal obstruction**: rhinitis or medication-induced swelling narrows the airway reversibly; decongestion distinguishes it from structural causes. **Cottle and modified Cottle maneuvers**: lateral traction or internal support that improves breathing localizes valve dysfunction. **Treatment logic**: septoplasty straightens the septum, spreader grafts widen the internal valve, lateral crural strut or alar batten grafts stiffen the sidewall, and turbinate reduction enlarges the airway while preserving mucosa.

### CC-facial_plastics-13.1 (concept check)

Stem: A 40-year-old has right nasal obstruction that worsens with deep inspiration. When the right cheek is pulled laterally, breathing improves markedly. The septum is straight. Which structure is most likely failing?

- **Correct:** The internal nasal valve
- Distractor: The inferior turbinate bone — _why wrong:_ Turbinate enlargement causes obstruction that improves with decongestant, not with cheek traction.
- Distractor: The posterior septum — _why wrong:_ The septum is straight, and a posterior deviation would not improve with cheek traction.
- Distractor: The nasopharyngeal airway — _why wrong:_ Nasopharyngeal obstruction is unaffected by lateral cheek traction.

Explanation: The internal valve, bounded by the septum, caudal upper lateral cartilage, and inferior turbinate head, is the narrowest airway segment. Inspiratory airflow lowers lateral pressure (Bernoulli), collapsing a weak sidewall; a positive Cottle maneuver localizes it. Spreader grafts widen it.

Pearl: Positive Cottle plus inspiratory collapse = valve problem; fix structure, not turbinate.

## T-facial_plastics-14 — Functional Septorhinoplasty
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-14.overview**

Functional septorhinoplasty corrects nasal obstruction by addressing the septum, internal and external valves, and nasal framework, often with structural grafts. It combines form and function.

**T-facial_plastics-14.physiology**

**Nasal framework**: bony vault, upper lateral cartilages, lower lateral cartilages, and septum. **Valve function**: internal and external valves control airflow. **Tip support**: major (lateral crura strength, medial crura footplates, scroll area) and minor mechanisms.

**T-facial_plastics-14.pathophysiology**

**Valve collapse**: weak lateral cartilage or narrow valve angle. **Septal deviation**: caudal deviations obstruct the valve. **Spreader grafts**: widen the internal valve. **Batten and lateral crural strut grafts**: support the external valve. **Overresection**: causes collapse and deformity.

### CC-facial_plastics-14.1 (concept check)

Stem: A patient has nasal obstruction from a narrow internal valve with an inverted-V deformity after prior rhinoplasty. Which graft best addresses both function and form?

- **Correct:** Spreader grafts
- Distractor: Columellar strut graft — _why wrong:_ A columellar strut supports the tip, not the internal valve.
- Distractor: Alar rim graft — _why wrong:_ Alar rim grafts support the external valve.
- Distractor: Dorsal onlay graft — _why wrong:_ Onlay grafts add dorsal height, not valve width.

Explanation: Spreader grafts placed between the septum and upper lateral cartilages widen the internal valve angle and restore dorsal width, correcting inverted-V deformity.

Pearl: Internal valve narrowing: spreader grafts.

## T-facial_plastics-15 — Hair Restoration Fundamentals
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-15.overview**

Hair restoration treats androgenetic alopecia with medical therapy (minoxidil, finasteride) and follicular unit transplantation. Planning must anticipate progressive loss.

**T-facial_plastics-15.physiology**

**Hair cycle**: anagen (growth, years), catagen (involution, weeks), and telogen (rest, months). **Follicular units**: natural groupings of 1-4 hairs with sebaceous glands. **Androgen receptors**: frontal and vertex follicles have androgen sensitivity; occipital follicles are resistant. **Dermal papilla**: controls follicle size and cycling.

**T-facial_plastics-15.pathophysiology**

**Androgenetic alopecia**: DHT miniaturizes genetically susceptible follicles, shortening anagen and producing finer hair. **Donor dominance**: transplanted occipital follicles retain resistance to DHT. **Finasteride**: blocks type II 5-alpha reductase, lowering DHT. **Minoxidil**: prolongs anagen and enlarges follicles. **Progressive loss**: planning must anticipate future loss. **Shock loss**: transient telogen effluvium after surgery.

## T-facial_plastics-16 — Laryngeal Fracture / External Laryngeal Trauma
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-16.overview**

Laryngeal fractures from blunt or penetrating trauma threaten the airway and voice. Airway assessment, CT, and endoscopy guide treatment from observation to open repair (Schaefer classification).

**T-facial_plastics-16.physiology**

**Laryngeal framework**: the thyroid and cricoid cartilages form a protective box around the airway. **Natural protection**: the mandible and sternum shield the larynx, and neck flexion moves it out of harm. **Calcification with age**: older laryngeal cartilage becomes brittle and fractures in multiple pieces. **Cricoid**: the only complete ring; injury causes airway collapse.

**T-facial_plastics-16.pathophysiology**

**Mechanism**: dashboard and clothesline injuries crush the larynx against the spine. **Symptoms**: hoarseness, stridor, hemoptysis, subcutaneous emphysema. **Airway**: intubation can worsen injury; tracheostomy under local is preferred for unstable airways. **Repair**: within 24-48 hours for best outcomes.

### CC-facial_plastics-16.1 (concept check)

Stem: After a clothesline injury on a motorcycle, a patient has hoarseness, hemoptysis, crepitus over the larynx, and increasing work of breathing. What is the safest way to secure the airway?

- **Correct:** Awake tracheostomy below the injury
- Distractor: Rapid sequence orotracheal intubation — _why wrong:_ Blind intubation can create a false passage or complete a partial laryngotracheal disruption.
- Distractor: Emergency cricothyroidotomy — _why wrong:_ Cricothyroidotomy passes through or near the injured larynx.
- Distractor: Observation with humidified oxygen — _why wrong:_ Progressive respiratory distress requires a secure airway.

Explanation: Intubating through a fractured larynx risks converting a partial injury into complete separation. Awake tracheostomy under local anesthesia below the injury secures the airway; CT and endoscopy then guide repair, ideally within 24-48 hours.

Pearl: Laryngeal fracture with airway distress: tracheostomy awake.

## T-facial_plastics-17 — Le Fort / Panfacial Trauma
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-17.overview**

Le Fort fractures separate the midface from the skull base at characteristic levels; panfacial fractures involve the upper, middle, and lower face. Repair rebuilds buttresses in sequence to restore facial height, width, projection, and occlusion.

**T-facial_plastics-17.physiology**

**Pterygoid plates**: link the maxilla to the skull base posteriorly; all Le Fort fractures involve them. **Buttress system**: vertical buttresses (nasomaxillary, zygomaticomaxillary, pterygomaxillary) carry chewing forces; horizontal buttresses connect them. **Le Fort levels**: I (above the alveolus), II (pyramidal through nasal bones and orbital rims), III (craniofacial disjunction through zygomatic arches and lateral orbits). **Occlusion**: the maxillary dentition must align with the mandible.

**T-facial_plastics-17.pathophysiology**

**Midface mobility**: palate moves with traction. **Malocclusion**: anterior open bite from posterior displacement. **Airway compromise**: posterior displacement and bleeding. **CSF leak**: Le Fort II and III. **Repair sequencing**: reestablish occlusion, then outer frame (width), then buttresses.

## T-facial_plastics-18 — Local Flap Reconstruction
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-18.overview**

Local flaps move adjacent skin into a defect, matching color and texture better than grafts. Flap design follows tissue biomechanics, blood supply, and relaxed skin tension lines.

**T-facial_plastics-18.physiology**

**Random pattern blood supply**: local flaps rely on the subdermal plexus rather than a named artery, limiting length-to-width ratio (about 3:1 on the face, more in well-vascularized areas). **Axial flaps**: carry a named vessel (e.g., supratrochlear for the forehead flap), allowing longer flaps. **Skin biomechanics**: skin has viscoelastic properties, with creep (elongation under constant load) and stress relaxation. **Relaxed skin tension lines**: lie perpendicular to underlying muscle pull; closures parallel to them heal with less tension and better scars. **Facial aesthetic subunits**: scars at subunit borders are less visible.

**T-facial_plastics-18.pathophysiology**

**Flap necrosis**: excessive length, tension, or kinking compromises distal perfusion; smoking and radiation increase risk. **Tension and scarring**: tension perpendicular to a closure widens scars and distorts free margins (eyelid, lip, ala). **Flap movement types**: advancement (moves forward), rotation (pivots around a point), and transposition (lifts over intervening skin), each with secondary defects and standing cones. **Trapdoor deformity**: curved scars contract, elevating the flap. **Venous congestion**: impaired outflow causes discoloration and loss.

## T-facial_plastics-19 — Mandible Fracture
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-19.overview**

Mandible fractures are common facial fractures; the mandible is a ring, so it often fractures in two places. Treatment restores occlusion and stability with closed reduction or open fixation, guided by biomechanics.

**T-facial_plastics-19.physiology**

**Ring structure**: the mandible behaves like a bone ring articulating with the skull at both TMJs, so a single break commonly has a second fracture. **Weak points**: condylar neck, angle (especially with an impacted third molar), and parasymphysis (canine root). **Muscle forces**: elevators (masseter, temporalis, medial pterygoid) pull the posterior segment up and forward; depressors (digastric, geniohyoid, mylohyoid) pull the anterior segment down. **Tension and compression zones (Champy)**: biting forces create tension along the superior alveolar border and compression along the inferior border. **Inferior alveolar nerve**: runs in the mandibular canal to the mental foramen.

**T-facial_plastics-19.pathophysiology**

**Favorable vs unfavorable**: fractures oriented so muscle pull compresses the segments are favorable; those pulled apart are unfavorable. **Malocclusion**: the cardinal sign, as segments displace with muscle pull. **Lip numbness**: inferior alveolar nerve injury. **Open fractures**: fractures through tooth-bearing areas communicate with the mouth and need antibiotics. **Fixation logic**: Champy miniplates along the line of tension (superior border) neutralize distracting forces; load-bearing plates are used for comminuted or edentulous mandibles. **Condylar fractures**: often treated closed in children to preserve growth; open repair for displacement that prevents occlusion.

### CC-facial_plastics-19.1 (concept check)

Stem: A 25-year-old was punched on the left jaw. He has malocclusion and right lower lip numbness. CT shows a right mandibular angle fracture and a left parasymphyseal fracture. Why are two fractures so common?

- **Correct:** The mandible is a ring joined at both TMJs
- Distractor: Assault always involves two blows — _why wrong:_ A single blow commonly produces two fractures because of mandibular geometry.
- Distractor: The angle is the strongest point — _why wrong:_ The angle is a weak point, especially with an impacted third molar.
- Distractor: Lip numbness causes a second fracture — _why wrong:_ Numbness results from inferior alveolar nerve injury; it does not cause fractures.

Explanation: The mandible behaves like a bony ring articulating at both TMJs, so force at one point often breaks it at a second weak point (angle, condyle, parasymphysis). Numbness reflects inferior alveolar nerve injury in the fractured segment.

Pearl: Find one mandible fracture, look for the second.

## T-facial_plastics-20 — Mandibular Biomechanics and Occlusion
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-20.overview**

Mandibular biomechanics (muscle vectors, tension and compression zones) and dental occlusion (Angle classification) govern how fractures displace and how fixation must be designed. Restoring pre-injury occlusion is the goal of mandible and midface repair.

**T-facial_plastics-20.physiology**

**Muscles of mastication**: masseter, temporalis, and medial pterygoid elevate; lateral pterygoid protrudes and opens; digastric, geniohyoid, and mylohyoid depress. **Champy lines of osteosynthesis**: biting creates tension at the superior (alveolar) border and compression at the inferior border; anteriorly, torsional forces require two points of fixation. **Angle classification**: Class I (mesiobuccal cusp of the maxillary first molar in the buccal groove of the mandibular first molar), Class II (mandible retruded), Class III (mandible protruded). **Occlusal plane and facets**: wear facets reveal the patient's habitual bite. **TMJ**: hinge and glide movements during opening.

**T-facial_plastics-20.pathophysiology**

**Displacement by muscle pull**: posterior segments pull up and medially; anterior segments pull down and back. **Favorable vs unfavorable fractures**: orientation determines whether muscle pull reduces or distracts. **Malocclusion as a sign**: premature contacts or open bite indicate displacement. **Fixation design**: miniplates along the tension band neutralize forces in favorable patterns; load-bearing reconstruction plates for comminution, atrophy, or defects. **Maxillomandibular fixation**: uses intact teeth to restore occlusion before plating.

### CC-facial_plastics-20.1 (concept check)

Stem: Using Champy's principles, where should a single miniplate be placed to fix a favorable mandibular angle fracture?

- **Correct:** Along the superior border, the line of tension
- Distractor: Along the inferior border, the line of compression — _why wrong:_ The inferior border is in compression and needs less fixation.
- Distractor: Across the condylar neck — _why wrong:_ The condyle is not part of an angle fracture repair.
- Distractor: Through the inferior alveolar canal — _why wrong:_ Plates and screws avoid the canal to protect the nerve.

Explanation: Biting forces create tension along the superior (alveolar) border and compression along the inferior border at the angle. A miniplate along the tension band neutralizes distracting forces.

Pearl: Champy: plate the tension band.

## T-facial_plastics-21 — Mohs Defect Reconstruction
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-21.overview**

Mohs surgery removes skin cancer with complete margin control, leaving defects reconstructed by secondary intention, primary closure, grafts, or flaps. Reconstruction is guided by subunits, free margins, and tissue match.

**T-facial_plastics-21.physiology**

**Facial subunits**: nose (dorsum, sidewalls, tip, ala, soft triangles, columella), eyelids, cheeks, lips, and forehead. **Concave vs convex surfaces**: concave areas (medial canthus, alar crease) heal well by secondary intention. **Free margins**: eyelid, lip, and alar rim distort easily under tension. **Skin thickness**: thin dorsal and sidewall skin vs thick sebaceous tip and alar skin.

**T-facial_plastics-21.pathophysiology**

**Secondary intention**: wound contraction is useful in concave areas but distorts free margins. **Grafts**: full-thickness grafts match thin skin better; they need a vascular bed. **Flaps**: bilobed, nasolabial, and forehead flaps restore thick skin and support. **Subunit principle**: replacing an entire subunit when most is lost hides scars. **Support**: cartilage grafts prevent alar collapse.

## T-facial_plastics-22 — NOE Fracture
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-22.overview**

Naso-orbito-ethmoid fractures involve the nasal bones, medial orbital walls, and ethmoids, threatening the medial canthal tendon and nasolacrimal system. Classified by Markowitz type, they require precise repair to prevent telecanthus.

**T-facial_plastics-22.physiology**

**Central fragment**: the bone to which the medial canthal tendon attaches. **Medial canthal tendon**: anchors the eyelids to the medial orbit at the anterior and posterior lacrimal crests. **Nasolacrimal system**: lacrimal sac in the fossa between the crests, draining into the inferior meatus. **Nasal dorsum support**: depends on nasal bones and septum.

**T-facial_plastics-22.pathophysiology**

**Telecanthus**: lateral displacement of the central fragment and medial canthal tendon widens the intercanthal distance (over about 35-40 mm suggests injury). **Markowitz types**: I (large central fragment), II (comminuted but tendon attached to a fragment), III (tendon avulsed or fragment comminuted). **Nasal flattening**: loss of dorsal support. **Epiphora**: nasolacrimal injury. **CSF leak**: cribriform plate and ethmoid roof fractures. **Repair logic**: wiring or plating the central fragment, and transnasal canthopexy for type III.

### CC-facial_plastics-22.1 (concept check)

Stem: After a high-speed collision, a patient has a flattened nasal bridge and widening between the medial canthi. Intercanthal distance is 42 mm. What does this finding indicate?

- **Correct:** Displaced canthal fragment
- Distractor: Simple nasal bone fracture — _why wrong:_ Isolated nasal fractures do not widen the intercanthal distance.
- Distractor: Orbital floor blowout — _why wrong:_ Floor fractures cause enophthalmos or entrapment, not telecanthus.
- Distractor: Normal intercanthal distance — _why wrong:_ Over about 35-40 mm suggests telecanthus.

Explanation: In NOE fractures, the central fragment carrying the medial canthal tendon displaces laterally, widening the intercanthal distance. Markowitz classification guides repair; type III requires transnasal canthopexy.

Pearl: Telecanthus after midface trauma = NOE fracture.

## T-facial_plastics-23 — Nasal Fracture
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-23.overview**

Nasal fractures are the most common facial fracture, causing deformity and obstruction. Closed reduction is best done before bones set (within about 1-2 weeks), and a septal hematoma must always be ruled out.

**T-facial_plastics-23.physiology**

**Nasal bony vault**: paired nasal bones thick superiorly and thin inferiorly, joined to the frontal bone and maxillary frontal processes. **Cartilaginous vault**: upper lateral cartilages attach under the nasal bones at the keystone area. **Septal support**: the septum supports the dorsum and tip. **Healing timeline**: nasal bones become fixed within about 10-14 days in adults.

**T-facial_plastics-23.pathophysiology**

**Lateral blows**: depress the ipsilateral nasal bone and outfracture the contralateral bone (C-shaped deviation). **Frontal blows**: splay or comminute nasal bones and may involve the septum. **Septal injury**: septal fracture or dislocation causes obstruction and persistent deviation if untreated. **Septal hematoma**: blood separates the mucoperichondrium from cartilage, cutting off nutrition; untreated, it causes cartilage necrosis, abscess, and saddle nose. **Timing logic**: edema obscures the shape early; reduction after swelling settles but before bony union.

### CC-facial_plastics-23.1 (concept check)

Stem: A 19-year-old has a deviated nose 3 days after a basketball injury. Exam shows a tense, bluish bilateral swelling of the septum. What is the priority before any fracture reduction?

- **Correct:** Drain the septal hematoma
- Distractor: Wait 5 days for swelling to settle — _why wrong:_ Waiting is reasonable for the bony reduction, not for a hematoma.
- Distractor: Order a CT of the facial bones — _why wrong:_ Imaging does not change urgent management of a septal hematoma.
- Distractor: Start oral steroids — _why wrong:_ Steroids do not treat a hematoma.

Explanation: Septal cartilage depends on the mucoperichondrium for nutrition. A hematoma separates them; within days cartilage necroses, causing abscess and saddle nose. Drainage with bolster or quilting is urgent.

Pearl: Always look for septal hematoma after nasal trauma.

## T-facial_plastics-24 — Open Rhinoplasty Fundamentals
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-24.overview**

Open rhinoplasty uses a transcolumellar incision for direct exposure of the nasal framework, allowing precise graft placement and tip work. It trades a columellar scar and longer edema for visibility.

**T-facial_plastics-24.physiology**

**Skin-soft tissue envelope**: thickness varies from thin over the rhinion to thick over the tip, affecting definition. **Tip support mechanisms**: major (lateral crural strength, medial crural footplate attachment to caudal septum, scroll attachments) and minor (interdomal ligament, dorsal septum, nasal spine). **Lymphatic drainage**: runs in the columella and soft tissue. **Columellar artery**: a branch of the superior labial artery.

**T-facial_plastics-24.pathophysiology**

**Disruption of support**: open approaches release support attachments, requiring reconstruction. **Edema**: prolonged tip edema due to lymphatic disruption. **Columellar necrosis**: rare, more common with prior surgery. **Precision**: direct visualization allows suture techniques and grafts.

### CC-facial_plastics-24.1 (concept check)

Stem: Six months after open rhinoplasty, a patient's nasal tip has drooped and lost projection. The surgeon had divided the medial crural footplate attachments and did not place a strut or septal extension graft. What explains the change?

- **Correct:** Loss of a major tip support mechanism
- Distractor: Excess cartilage resorption from crushing — _why wrong:_ Crushed grafts can resorb, but no grafts were placed; the cause is lost support.
- Distractor: Postoperative infection of the tip — _why wrong:_ Infection causes pain and redness, not gradual loss of projection alone.
- Distractor: Normal settling seen in all patients — _why wrong:_ Some settling occurs, but marked loss of projection reflects lost support.

Explanation: Major tip support comes from lateral crural strength, attachment of the medial crural footplates to the caudal septum, and the scroll attachment. Open approaches release some of these, so support must be rebuilt with a columellar strut, septal extension graft, or sutures.

Pearl: Release support in rhinoplasty and you must rebuild it.

## T-facial_plastics-25 — Otoplasty
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-25.overview**

Otoplasty corrects prominent ears, usually from an underdeveloped antihelical fold and excessive conchal bowl. It is commonly performed after age 5-6 when ear growth is mostly complete.

**T-facial_plastics-25.physiology**

**Normal auricle**: auriculocephalic angle about 20-30 degrees and helical rim 1.5-2 cm from the scalp. **Antihelical fold**: created by cartilage folding. **Ear growth**: reaches about 85 percent adult size by age 5-6.

**T-facial_plastics-25.pathophysiology**

**Absent antihelical fold**: the cartilage does not fold, so the scapha projects outward. **Excess conchal bowl**: a deep concha pushes the ear away from the head. **Mustarde sutures**: horizontal mattress sutures create the antihelical fold. **Furnas sutures**: conchal-mastoid sutures set back the concha. **Hematoma**: the major acute complication. **Telephone ear**: overcorrected middle third. **Recurrence**: cartilage memory.

## T-facial_plastics-26 — Periocular Reconstruction
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-26.overview**

Periocular reconstruction repairs eyelid and canthal defects after trauma or tumor excision, restoring protection of the globe. It requires reconstructing anterior lamella (skin, muscle) and posterior lamella (tarsus, conjunctiva).

**T-facial_plastics-26.physiology**

**Eyelid lamellae**: the anterior lamella (skin and orbicularis oculi) and the posterior lamella (tarsal plate and conjunctiva) each need replacement in full-thickness defects. **Tarsus**: dense connective tissue giving the lid shape and rigidity; it contains meibomian glands. **Canthal tendons**: anchor the lids to the medial and lateral orbital rims, maintaining horizontal tension. **Eyelid function**: blinking spreads tears, and closure protects the cornea from exposure. **Lacrimal drainage**: puncta in the medial lids drain tears through canaliculi to the sac.

**T-facial_plastics-26.pathophysiology**

**Defect size rules**: lid margin defects up to about 25-30 percent often close primarily; 30-50 percent need canthotomy or semicircular (Tenzel) flaps; larger defects need lid-sharing (Hughes, Cutler-Beard) or composite grafts. **Blood supply rule**: each reconstructed lamella needs at least one vascularized layer, so a graft must be paired with a flap. **Ectropion and retraction**: vertical tension and scar pull the lower lid down, exposing the globe. **Corneal exposure**: incomplete closure dries and ulcerates the cornea. **Medial canthal defects**: risk canalicular injury and epiphora.

## T-facial_plastics-27 — Rhinoplasty Graft Selection
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-27.overview**

Rhinoplasty grafts restore support, contour, and airway: spreader, columellar strut, septal extension, alar rim, lateral crural strut, shield, and dorsal onlay grafts. Material selection (septal, auricular, costal) depends on availability and mechanical needs.

**T-facial_plastics-27.physiology**

**Septal cartilage**: straight, strong, and limited in volume. **Auricular cartilage**: curved and flexible, good for alar grafts. **Costal cartilage**: abundant and strong, prone to warping. **Graft integration**: cartilage survives by diffusion and fibrous attachment.

**T-facial_plastics-27.pathophysiology**

**Spreader grafts**: widen the internal valve and straighten the dorsum. **Alar rim and batten grafts**: stiffen collapsing sidewalls. **Septal extension grafts**: control tip projection and rotation. **Costal cartilage warping**: due to release of internal stresses, minimized by balanced carving. **Resorption**: crushed cartilage resorbs.

### CC-facial_plastics-27.1 (concept check)

Stem: A patient needs a long, strong septal extension graft in revision rhinoplasty, but the septum was previously harvested. Which donor is most appropriate, and what is its main drawback?

- **Correct:** Costal cartilage; it can warp
- Distractor: Auricular cartilage; it is too straight — _why wrong:_ Auricular cartilage is curved and flexible, not straight.
- Distractor: Alloplastic implant; it never extrudes — _why wrong:_ Alloplasts carry infection and extrusion risk.
- Distractor: Crushed septal remnants; they never resorb — _why wrong:_ Crushed cartilage resorbs.

Explanation: Costal cartilage provides abundant, strong cartilage for structural grafts but tends to warp as internal stresses release; balanced carving minimizes this.

Pearl: Need strength and quantity: rib, and carve to prevent warping.

## T-facial_plastics-28 — Rhinoplasty Tip Mechanics
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-28.overview**

Nasal tip mechanics explain how tip projection, rotation, and definition depend on the lower lateral cartilages and their attachments. The tripod concept predicts how cartilage changes alter tip position.

**T-facial_plastics-28.physiology**

**Tripod concept (Anderson)**: the conjoined medial crura form one leg and the two lateral crura the other two; changing leg lengths changes projection and rotation. **Major tip support**: lateral crural size, shape, and strength; attachment of medial crural footplates to the caudal septum; attachment of upper to lower lateral cartilages (scroll). **Minor support**: interdomal ligament, cartilaginous dorsum, anterior nasal spine, sesamoid cartilages, skin and soft tissue. **Skin thickness**: thick skin blunts definition; thin skin reveals irregularities.

**T-facial_plastics-28.pathophysiology**

**Shortening lateral legs**: increases rotation and reduces projection. **Shortening the medial leg**: reduces projection and counter-rotates. **Loss of support**: transfixion incisions and footplate release reduce projection unless rebuilt (columellar strut, septal extension graft). **Overresection**: lateral crural resection causes pinching, alar collapse, and retraction. **Suture techniques**: domal and interdomal sutures refine the tip.

### CC-facial_plastics-28.1 (concept check)

Stem: Using the tripod concept, what happens to the nasal tip when the lateral crura (the two lateral legs) are shortened?

- **Correct:** Increased rotation and decreased projection
- Distractor: Decreased rotation and increased projection — _why wrong:_ Shortening the lateral legs rotates the tip upward and reduces projection.
- Distractor: No change in rotation or projection — _why wrong:_ Changing leg lengths changes tip position.
- Distractor: Increased projection only — _why wrong:_ Shortening reduces projection.

Explanation: The tripod is formed by the conjoined medial crura and two lateral crura. Shortening the lateral legs rotates the tip cephalically and reduces projection; shortening the medial leg reduces projection and counter-rotates.

Pearl: Tripod: change a leg, change the tip.

## T-facial_plastics-29 — Scar Management
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-29.overview**

Scar management optimizes wound healing and treats hypertrophic scars, keloids, and contractures with pressure, silicone, steroids, lasers, and revision. Understanding wound biology is key to prevention.

**T-facial_plastics-29.physiology**

**Wound healing phases**: hemostasis, inflammation, proliferation (fibroblasts, collagen III), and remodeling (collagen I, cross-linking). **Remodeling**: continues for months to a year; scars reach about 80 percent of original skin strength. **Tension**: mechanical stress stimulates fibroblast activity.

**T-facial_plastics-29.pathophysiology**

**Hypertrophic scars**: excess collagen within the wound boundaries, often due to tension; may regress. **Keloids**: extend beyond wound margins, genetically predisposed, rarely regress, and recur after excision. **TGF-beta**: drives fibroblast proliferation and collagen deposition. **Contracture**: myofibroblasts shorten scars. **Treatment logic**: silicone hydrates and reduces fibroblast activity; steroids reduce collagen synthesis; revision realigns scars along RSTLs.

## T-facial_plastics-30 — Septal Hematoma
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-30.overview**

Septal hematoma is blood collection between the septal cartilage and mucoperichondrium after trauma. It must be drained urgently to prevent cartilage necrosis, abscess, and saddle nose.

**T-facial_plastics-30.physiology**

**Avascular cartilage**: septal cartilage depends on the mucoperichondrium for oxygen and nutrients by diffusion. **Mucoperichondrium**: carries the septal blood supply. **Dorsal support**: the septum supports the cartilaginous dorsum and tip. **Children**: septal hematoma also threatens growth centers that influence midface development.

**T-facial_plastics-30.pathophysiology**

**Separation**: blood strips mucoperichondrium off cartilage. **Avascular necrosis**: within days, cartilage dies. **Abscess**: infection spreads, rarely intracranially. **Saddle nose**: dorsal support loss. **Treatment**: incision, drainage, and bolster or quilting sutures.

### CC-facial_plastics-30.1 (concept check)

Stem: A 6-year-old has nasal obstruction 2 days after falling onto his face. A bulging, fluctuant, bilateral septal swelling is seen. Why is urgent drainage required?

- **Correct:** The cartilage dies without its blood supply
- Distractor: To prevent malunion of the nasal bones — _why wrong:_ Bony malunion is managed separately and is not the urgent issue.
- Distractor: To relieve pressure in the frontal sinus — _why wrong:_ The hematoma is in the septum and does not affect sinus pressure.
- Distractor: To prevent recurrent anterior epistaxis — _why wrong:_ Bleeding is not the main danger of an untreated hematoma.

Explanation: Septal cartilage depends on diffusion from the mucoperichondrium. A hematoma separates them, so cartilage necroses within days, risking abscess, saddle nose, and, in children, disturbed midface growth.

Pearl: Septal hematoma is a drain-today emergency.

## T-facial_plastics-31 — Septal Perforation
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-31.overview**

Septal perforation is a full-thickness defect of the nasal septum from surgery, trauma, cocaine, nose picking, or systemic disease. Small anterior perforations whistle and crust, and repair requires vascularized flaps.

**T-facial_plastics-31.physiology**

**Cartilage nutrition**: septal cartilage has no blood vessels of its own and survives by diffusion from the mucoperichondrium on each side. **Mucosal function**: septal mucosa humidifies and warms air; airflow over it is normally smooth and largely laminar. **Septal support**: the caudal and dorsal septum (L-strut) supports the dorsum and tip. **Mucosal healing**: epithelium migrates across small defects only if the edges are healthy and moist.

**T-facial_plastics-31.pathophysiology**

**Bilateral mucoperichondrial injury**: opposing mucosal tears (septoplasty, cautery, trauma) leave cartilage without blood supply on both sides, so it necroses and a hole forms. **Other causes**: cocaine (vasoconstriction plus adulterants), nose picking, nasal steroid spray misuse, granulomatosis with polyangiitis, sarcoidosis, syphilis, and malignancy. **Turbulence and drying**: airflow becomes turbulent at the perforation edge, drying mucosa and causing crusting, bleeding, and pain. **Whistling**: small anterior perforations make a whistle. **Posterior perforations**: often asymptomatic because airflow is slower and better humidified. **Saddle deformity**: large perforations involving the dorsal L-strut lose support. **Repair logic**: bilateral vascularized mucosal flaps with an interposition graft; biopsy first when systemic disease is suspected.

### CC-facial_plastics-31.1 (concept check)

Stem: A 35-year-old has a 1 cm anterior septal perforation causing whistling, crusting, and bleeding after septoplasty. Why does the perforation cause these symptoms?

- **Correct:** Turbulent airflow dries the edges
- Distractor: Infection spreading from the sinuses — _why wrong:_ Sinus infection does not explain whistling and edge crusting.
- Distractor: Exposed bone releasing inflammatory mediators — _why wrong:_ The cause is airflow disruption, not bone mediators.
- Distractor: Loss of all nasal humidification — _why wrong:_ Humidification persists; it is disrupted locally at the edge.

Explanation: Airflow becomes turbulent at the perforation edge, drying mucosa, causing crusting, bleeding, and pain; small anterior perforations whistle. Repair uses bilateral vascularized mucosal flaps with an interposition graft.

Pearl: Septal perforation symptoms come from turbulence at the edge.

## T-facial_plastics-32 — Skin Graft Selection
_source: pathophys_v470/facial_plastics_b.py_

**T-facial_plastics-32.overview**

Skin grafts transfer epidermis and part (split-thickness) or all (full-thickness) of the dermis to a vascularized bed. Full-thickness grafts contract less and match facial skin better.

**T-facial_plastics-32.physiology**

**Graft take phases**: plasmatic imbibition (first 48 hours), inosculation (vessel connection, days 2-3), and revascularization. **Dermis**: contains the structure that resists contraction. **Donor sites**: preauricular, postauricular, and supraclavicular for full-thickness face grafts.

**T-facial_plastics-32.pathophysiology**

**Primary contraction**: immediate elastic recoil, greater in full-thickness grafts. **Secondary contraction**: wound contraction after healing, greater in split-thickness grafts because they have less dermis. **Graft failure**: hematoma, seroma, shear, and infection block revascularization. **Color mismatch**: donor site color differs. **Graft bed**: bone without periosteum and cartilage without perichondrium do not support grafts.

### CC-facial_plastics-32.1 (concept check)

Stem: A 70-year-old has a 2 cm Mohs defect of the nasal sidewall. Why is a full-thickness skin graft preferred over a split-thickness graft for this defect?

- **Correct:** It contracts less and matches better
- Distractor: It survives better on bare bone — _why wrong:_ No graft survives on bone without periosteum.
- Distractor: It takes faster with less bed perfusion — _why wrong:_ Thicker grafts are harder to revascularize.
- Distractor: It does not need a vascular bed — _why wrong:_ All grafts need a vascular bed.

Explanation: Full-thickness grafts include the full dermis, which resists secondary contraction and better matches facial skin. Split-thickness grafts take more easily but contract more and look shinier.

Pearl: Face: full-thickness grafts.

## T-facial_plastics-33 — Structured Facial Trauma Examination
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-33.overview**

A structured facial trauma exam after ATLS evaluates airway, vision, occlusion, nerves, and bones systematically. It prevents missed injuries such as retrobulbar hematoma and entrapment.

**T-facial_plastics-33.physiology**

**Facial thirds**: upper (frontal), middle (orbits, zygoma, maxilla, nose), and lower (mandible). **Vision pathway**: optic nerve function is checked by acuity, pupils, and color vision. **Extraocular movements**: CN III, IV, VI and orbital muscle position. **Sensory nerves**: supraorbital, infraorbital, and mental nerves. **Occlusion**: dental relationships reveal midface and mandible displacement.

**T-facial_plastics-33.pathophysiology**

**Retrobulbar hematoma**: rising orbital pressure causes vision loss; lateral canthotomy is emergent. **Entrapment**: restricted gaze. **Occlusion**: indicates mandible or maxilla fractures. **Facial nerve injury**: lacerations lateral to the lateral canthus require exploration. **CSF leak**: clear rhinorrhea.

### CC-facial_plastics-33.1 (concept check)

Stem: After an assault, a patient has a tense, proptotic left eye with decreasing vision, a firm orbit, and an afferent pupillary defect. Facial CT is pending. What is the most appropriate immediate step?

- **Correct:** Lateral canthotomy and cantholysis
- Distractor: Wait for CT before any intervention — _why wrong:_ Optic nerve ischemia is time-critical; decompression should not wait for imaging.
- Distractor: High-dose steroids and observation — _why wrong:_ Steroids do not relieve rising orbital pressure.
- Distractor: Immediate orbital floor exploration — _why wrong:_ Floor repair is not the emergency; decompression of the compartment is.

Explanation: Retrobulbar hematoma raises orbital pressure, compressing the optic nerve and its blood supply. Canthotomy and cantholysis release the compartment within minutes and can save vision.

Pearl: Tense proptosis with vision loss = canthotomy now.

## T-facial_plastics-34 — ZMC / Orbital Trauma
_source: pathophys_v470/facial_plastics_a.py_

**T-facial_plastics-34.overview**

Zygomaticomaxillary complex (ZMC) fractures disrupt the zygoma's four articulations and the orbit, causing flattening, numbness, trismus, and diplopia. Orbital floor fractures can entrap muscle or enlarge the orbit, leading to enophthalmos, and are repaired by indication and timing.

**T-facial_plastics-34.physiology**

**Zygoma articulations**: frontal (zygomaticofrontal suture), temporal (zygomatic arch), maxillary (inferior orbital rim and zygomaticomaxillary buttress), and sphenoid (lateral orbital wall). **Facial buttresses**: vertical buttresses (nasomaxillary, zygomaticomaxillary, pterygomaxillary) transmit chewing forces to the skull base; horizontal buttresses (frontal bar, orbital rims, palate) tie them together. **Orbit**: a cone of bone with a thin floor (maxillary roof) and medial wall (lamina papyracea); the infraorbital nerve runs in the floor. **Globe position**: depends on orbital volume and soft-tissue support (Lockwood ligament). **Masseter and temporalis**: attach to the zygoma and arch.

**T-facial_plastics-34.pathophysiology**

**Fracture pattern**: a blow to the malar eminence separates the zygoma at its sutures, typically displacing it inferomedially and posteriorly. **Malar flattening and trismus**: rotation flattens the cheek, and a depressed arch impinges on the coronoid process. **Infraorbital nerve injury**: numbness of the cheek, upper lip, and lateral nose. **Orbital floor blowout**: increased orbital pressure fractures the thin floor (hydraulic theory) or force is transmitted through the rim (buckling theory). **Entrapment**: inferior rectus or its fascia trapped in a trapdoor fracture (especially in children) causes restricted upgaze and oculocardiac reflex (bradycardia, nausea), an urgent indication. **Enophthalmos**: increased orbital volume lets the globe sink, usually when the defect is large. **Repair logic**: three-point alignment (frontozygomatic, rim, buttress) restores projection; sphenoid alignment confirms rotation.

### CC-facial_plastics-34.1 (concept check)

Stem: A 12-year-old hit in the eye with a ball has nausea, bradycardia, and restricted upgaze. CT shows a minimally displaced orbital floor fracture with a small trapped fragment of soft tissue. Why is urgent repair indicated?

- **Correct:** Entrapped inferior rectus
- Distractor: Large orbital volume increase — _why wrong:_ Enophthalmos from volume change is a delayed indication; this fracture is small.
- Distractor: Infraorbital nerve numbness — _why wrong:_ Numbness alone is not an urgent indication for repair.
- Distractor: Risk of later malar flattening — _why wrong:_ Malar flattening relates to ZMC displacement, not a floor trapdoor.

Explanation: In children, elastic bone snaps back like a trapdoor, trapping the inferior rectus or its fascia. Traction triggers the oculocardiac reflex (bradycardia, nausea) and the muscle can become ischemic, so repair is urgent.

Pearl: Child with restricted upgaze and bradycardia after orbital trauma = white-eyed blowout: operate urgently.


---

# Sleep Surgery

## T-sleep-1 — Adult Epiglottic Collapse / Epiglottopexy
_source: pathophys_v470/sleep.py_

**T-sleep-1.overview**

Adult epiglottic collapse is prolapse of a floppy epiglottis into the airway during sleep, causing CPAP and HNS failure. Epiglottopexy or partial epiglottectomy treats it.

**T-sleep-1.physiology**

**Epiglottis**: elastic cartilage anchored by the hyoepiglottic ligament and lateral pharyngoepiglottic folds. **Supraglottic airway**: normally patent during inspiration. **Tongue base influence**: tongue base position affects epiglottic angle.

**T-sleep-1.pathophysiology**

**Trapdoor collapse**: a floppy or posteriorly displaced epiglottis prolapses into the laryngeal inlet during inspiration. **CPAP failure**: positive pressure can push the epiglottis further closed. **HNS failure**: tongue protrusion does not reliably move the epiglottis. **Diagnosis**: DISE shows epiglottic collapse. **Treatment**: epiglottopexy (suturing the epiglottis to the tongue base) or partial epiglottectomy.

## T-sleep-2 — Adult PSG Interpretation
_source: pathophys_v470/sleep.py_

**T-sleep-2.overview**

Polysomnography records sleep stages, breathing, oxygenation, heart rhythm, and limb movements overnight to diagnose OSA and other sleep disorders. Reading the AHI, the oxygen nadir, positional and REM dependence, and the central vs obstructive pattern drives every sleep-surgery decision.

**T-sleep-2.physiology**

**Sleep staging**: EEG, EOG, and chin EMG define wake, N1, N2, N3 (slow-wave), and REM sleep; adults cycle every 90 minutes, with more N3 early and more REM late in the night. **REM atonia**: skeletal muscle tone, including the upper airway dilators, is lowest in REM, so obstruction is often worst in REM. **Respiratory monitoring**: oronasal thermistor (apneas), nasal pressure (hypopneas), thoracoabdominal belts (effort), and pulse oximetry. **Event definitions**: apnea is a 90 percent or greater airflow drop for 10 seconds or more; hypopnea is a 30 percent drop with a 3 percent desaturation or arousal (AASM recommended rule). **Effort distinguishes events**: obstructive apneas show continued effort; central apneas show absent effort.

**T-sleep-2.pathophysiology**

**AHI severity**: 5-15 mild, 15-30 moderate, over 30 severe in adults. **Oxygen desaturation burden**: the nadir and time below 90 percent reflect hypoxic stress and cardiovascular risk better than AHI alone. **Arousals**: each obstructive event ends with a cortical arousal that restores dilator tone, fragmenting sleep and causing daytime sleepiness. **Positional OSA**: events concentrate supine because gravity pulls the tongue and soft palate backward. **REM-related OSA**: events cluster in REM due to atonia. **Central apnea index**: a high proportion of central events (above about 25 percent) changes candidacy for HNS and points to cardiac, neurologic, or opioid causes. **Home sleep apnea tests**: measure breathing but not sleep, so they underestimate AHI and are less suited for complex patients.

### CC-sleep-2.1 (concept check)

Stem: A 52-year-old with daytime sleepiness has a PSG showing an AHI of 18, mostly hypopneas, with events clustered in REM and an oxygen nadir of 82 percent. Why are events concentrated in REM sleep?

- **Correct:** REM atonia removes dilator muscle tone
- Distractor: REM sleep raises the arousal threshold — _why wrong:_ Arousal threshold changes do not explain the loss of airway patency in REM.
- Distractor: Breathing becomes faster and deeper in REM — _why wrong:_ Breathing in REM is irregular, but faster breathing does not collapse the airway.
- Distractor: Snoring vibrations peak during REM — _why wrong:_ Snoring reflects airway narrowing; it does not cause REM clustering.

Explanation: During REM, skeletal muscle tone, including genioglossus and other pharyngeal dilators, falls to its lowest, so the collapsible pharynx narrows. REM-predominant OSA is common, especially in women.

Pearl: REM-clustered events reflect lost dilator tone.

## T-sleep-3 — Central Events / Hypoventilation
_source: pathophys_v470/sleep.py_

**T-sleep-3.overview**

Central apneas and hypoventilation reflect absent respiratory drive or inadequate ventilation rather than obstruction. They change surgical candidacy and require different treatment.

**T-sleep-3.physiology**

**Chemical control**: central chemoreceptors (medulla) sense CO2 and pH; peripheral chemoreceptors (carotid bodies) sense O2 and CO2. **Apnea threshold**: during sleep, ventilation stops if PaCO2 falls below a threshold a few mm Hg below waking levels. **Loop gain**: the sensitivity of the respiratory control loop; high loop gain overcorrects disturbances. **Sleep-related drive changes**: the wakefulness drive to breathe is lost in sleep.

**T-sleep-3.pathophysiology**

**High loop gain**: overshoot drives CO2 below the apnea threshold, causing central apnea, then CO2 rises and breathing overshoots again (periodic breathing, Cheyne-Stokes in heart failure). **Opioids**: suppress brainstem respiratory drive, causing ataxic breathing and central apneas. **Hypoventilation**: obesity, neuromuscular disease, and chest wall restriction reduce minute ventilation. **Surgical implications**: airway surgery and HNS do not treat central events, so high central apnea burden excludes HNS. **Treatment**: treating the cause, CPAP, bilevel with backup rate, or adaptive servo-ventilation in selected patients.

### CC-sleep-3.1 (concept check)

Stem: A 60-year-old on long-term high-dose methadone has a PSG showing an AHI of 35 with 70 percent central apneas and irregular breathing. Why is this patient not a candidate for hypoglossal nerve stimulation?

- **Correct:** His apneas are not from collapse
- Distractor: Methadone damages the hypoglossal nerve — _why wrong:_ Opioids suppress respiratory drive; they do not injure the nerve.
- Distractor: HNS is contraindicated in anyone over 55 — _why wrong:_ Age alone does not exclude HNS.
- Distractor: The AHI is too low for HNS — _why wrong:_ An AHI of 35 is within typical HNS criteria; the problem is the central proportion.

Explanation: Opioids suppress brainstem respiratory drive, causing ataxic breathing and central apneas. HNS opens the airway but cannot create respiratory effort, so a central or mixed apnea fraction above about 25 percent excludes it.

Pearl: High central apnea burden = treat the drive, not the airway.

## T-sleep-4 — Central Sleep Apnea / Treatment-Emergent CSA
_source: pathophys_v470/sleep.py_

**T-sleep-4.overview**

Central sleep apnea is apnea without respiratory effort; treatment-emergent CSA appears when CPAP treats obstruction. It is linked to heart failure, opioids, stroke, and high altitude.

**T-sleep-4.physiology**

**CO2-driven breathing**: during sleep, PaCO2 is the dominant driver of ventilation. **Apnea threshold**: breathing stops when PaCO2 falls below a threshold. **Circulation time**: delay between lung gas exchange and chemoreceptor sensing affects stability.

**T-sleep-4.pathophysiology**

**Hyperventilation-related CSA**: excess ventilatory sensitivity drives CO2 below threshold. **Heart failure**: prolonged circulation time and pulmonary congestion cause Cheyne-Stokes respiration. **Treatment-emergent CSA**: when CPAP opens the airway, increased ventilation lowers CO2, unmasking central apneas; it often resolves with continued use. **Opioids**: depress drive. **Adaptive servo-ventilation**: contraindicated in heart failure with reduced ejection fraction (SERVE-HF).

### CC-sleep-4.1 (concept check)

Stem: A 62-year-old starts CPAP for OSA. The titration study shows obstructive events resolve, but new central apneas appear (central AHI 12). Why can CPAP unmask central apneas?

- **Correct:** CO2 falls below the apnea threshold
- Distractor: CPAP damages the respiratory center — _why wrong:_ CPAP does not injure the brainstem.
- Distractor: CPAP causes airway collapse at high pressure — _why wrong:_ High pressure can cause other issues but central apneas reflect control instability.
- Distractor: The patient has opioid toxicity — _why wrong:_ No opioid history is described.

Explanation: Opening the airway increases ventilation; in patients with high loop gain, CO2 falls below the apnea threshold and breathing pauses. Treatment-emergent CSA often resolves with continued CPAP use.

Pearl: Treatment-emergent CSA often settles with time on CPAP.

## T-sleep-5 — Circadian Rhythm Sleep-Wake Disorders
_source: pathophys_v470/sleep.py_

**T-sleep-5.overview**

Circadian rhythm disorders misalign sleep timing with the desired schedule (delayed or advanced phase, shift work, jet lag). They cause insomnia and sleepiness that can mimic OSA.

**T-sleep-5.physiology**

**Suprachiasmatic nucleus**: the master clock in the hypothalamus, entrained mainly by light via the retinohypothalamic tract. **Melatonin**: secreted by the pineal gland in darkness, signaling biological night. **Two-process model**: sleep pressure (adenosine) and circadian alerting together determine sleep timing.

**T-sleep-5.pathophysiology**

**Delayed sleep phase**: common in adolescents; sleep onset and wake times shift later. **Advanced sleep phase**: common in older adults. **Shift work and jet lag**: misalignment between clock and schedule. **Mimicry**: insomnia and sleepiness can be misattributed to OSA. **Treatment**: timed light exposure and melatonin shift the clock.

### CC-sleep-5.1 (concept check)

Stem: A 17-year-old cannot fall asleep before 2 AM and struggles to wake for school, but on weekends sleeps soundly from 2 AM to 10 AM and wakes refreshed. What is the most likely diagnosis?

- **Correct:** Delayed sleep phase
- Distractor: Obstructive sleep apnea — _why wrong:_ OSA would cause unrefreshing sleep regardless of schedule.
- Distractor: Narcolepsy type 1 — _why wrong:_ Narcolepsy causes sleepiness even after adequate, well-timed sleep.
- Distractor: Anxiety-related insomnia — _why wrong:_ Insomnia would not resolve when sleep is allowed at the preferred time.

Explanation: Adolescents commonly have a delayed circadian phase. Sleep is normal in quality and length when timing matches the internal clock. Timed morning light and evening melatonin shift the clock earlier.

Pearl: Good sleep at the wrong time = circadian rhythm disorder.

## T-sleep-6 — DISE
_source: pathophys_v470/sleep.py_

**T-sleep-6.overview**

Drug-induced sleep endoscopy (DISE) visualizes the upper airway under sedation that mimics sleep, identifying the levels and patterns of collapse. It is required before hypoglossal nerve stimulation and guides surgical planning (VOTE classification).

**T-sleep-6.physiology**

**Pharyngeal collapsibility**: the pharynx is a muscular tube without bony support from the choanae to the larynx; patency depends on the balance between collapsing forces (negative inspiratory pressure, surrounding tissue pressure) and dilating forces (genioglossus and other dilator muscles). **Sedation mimicking sleep**: propofol or dexmedetomidine reduces dilator muscle tone similar to natural sleep. **VOTE levels**: velum, oropharynx (tonsils and lateral walls), tongue base, and epiglottis. **Collapse configurations**: anteroposterior, lateral, and concentric. **Awake vs asleep airway**: awake reflexes maintain patency, so awake exams underestimate collapse.

**T-sleep-6.pathophysiology**

**Multilevel collapse**: most patients collapse at more than one level, so single-level surgery often fails. **Complete concentric collapse at the velum**: predicts poor HNS response because stimulation of the tongue cannot pull open a circumferentially collapsing palate, so it is a contraindication. **Epiglottic collapse**: trapdoor epiglottis prolapse can cause failure of CPAP and HNS. **Lateral wall collapse**: often from tonsils or pharyngeal wall laxity. **Sedation depth**: too deep overcalls collapse; target-controlled infusion improves reliability.

### CC-sleep-6.1 (concept check)

Stem: A 50-year-old with moderate OSA intolerant of CPAP is being evaluated for hypoglossal nerve stimulation. DISE shows complete concentric collapse at the velum. Why does this finding usually exclude HNS?

- **Correct:** Protrusion cannot open a ring-shaped collapse
- Distractor: Concentric collapse means central sleep apnea — _why wrong:_ Concentric collapse is an obstructive pattern, not a central one.
- Distractor: Concentric collapse only occurs with epiglottic collapse — _why wrong:_ It occurs at the velum independent of epiglottic findings.
- Distractor: Concentric collapse indicates severe obesity only — _why wrong:_ Obesity contributes but the issue is the collapse pattern.

Explanation: HNS opens the airway by protruding the tongue and pulling the palate forward through palatoglossal coupling. A circumferentially collapsing velopharynx is not reliably opened this way, predicting poor response.

Pearl: Complete concentric collapse at the velum on DISE = poor HNS candidate.

## T-sleep-7 — Down Syndrome Pediatric HNS
_source: pathophys_v470/sleep.py_

**T-sleep-7.overview**

HNS is FDA-approved for adolescents with Down syndrome and persistent OSA after adenotonsillectomy, with specific age and AHI criteria. It addresses tongue-base and multilevel collapse common in Down syndrome.

**T-sleep-7.physiology**

**Down syndrome airway**: midface hypoplasia, relative macroglossia, narrow nasopharynx, and generalized hypotonia. **Lymphoid tissue**: lingual tonsil hypertrophy is common. **Hypotonia**: reduces pharyngeal dilator tone during sleep. **Obesity**: more prevalent.

**T-sleep-7.pathophysiology**

**Persistent OSA**: occurs in most children with Down syndrome after adenotonsillectomy because of multilevel collapse. **HNS logic**: increases genioglossus tone, counteracting hypotonia and tongue-base collapse. **Criteria**: FDA approval for ages 13-18 with AHI roughly 10-50 after adenotonsillectomy and CPAP failure. **Outcomes**: significant AHI reduction and improved quality of life. **Behavioral considerations**: tolerance of device and remote control use.

### CC-sleep-7.1 (concept check)

Stem: A 15-year-old with Down syndrome has persistent moderate OSA (AHI 22) after adenotonsillectomy and cannot tolerate CPAP. Why is HNS well suited to his airway?

- **Correct:** It offsets hypotonic tongue collapse
- Distractor: It enlarges the small midface — _why wrong:_ HNS does not change the bony skeleton.
- Distractor: It removes enlarged lingual tonsils — _why wrong:_ HNS stimulates muscle; it does not remove tissue.
- Distractor: It treats central apnea common in Down syndrome — _why wrong:_ HNS treats obstructive events, not central apnea.

Explanation: Down syndrome combines relative macroglossia, hypotonia, and multilevel collapse. Stimulating the genioglossus restores dilator tone during inspiration. FDA approval covers ages 13-18 with AHI roughly 10-50 after adenotonsillectomy.

Pearl: Down syndrome with persistent OSA after T&A: consider HNS.

## T-sleep-8 — HNS Activation / Programming
_source: pathophys_v470/sleep.py_

**T-sleep-8.overview**

HNS activation and programming set stimulation amplitude, electrode configuration, and timing after implantation. Titration with in-lab PSG optimizes efficacy.

**T-sleep-8.physiology**

**Electrode cuff**: wraps the distal hypoglossal nerve, targeting medial protrusor branches. **Configurations**: bipolar (+ - +) and unipolar settings change the current field and which fibers are recruited. **Respiratory sensing**: a pressure sensor between intercostal muscles detects inspiration to time stimulation. **Pulse parameters**: amplitude, pulse width, and rate determine recruitment and comfort.

**T-sleep-8.pathophysiology**

**Underpowered stimulation**: insufficient amplitude fails to protrude the tongue enough to open the airway. **Discomfort and arousal**: high amplitude causes tongue discomfort and sleep disruption. **Retractor recruitment**: current spread to retractor branches pulls the tongue back, defeating protrusion; reconfiguration targets protrusors. **Titration logic**: amplitude is increased stepwise in clinic and during in-lab titration PSG to find the lowest effective setting. **Habituation**: patients start at low amplitude and increase over weeks.

### CC-sleep-8.1 (concept check)

Stem: One month after HNS implantation, a patient reports the tongue pushes to the left and feels uncomfortable, and residual AHI is 22 at the current amplitude. Awake endoscopy shows tongue retraction rather than protrusion on stimulation. What is the best adjustment?

- **Correct:** Change the electrode configuration
- Distractor: Increase the amplitude further — _why wrong:_ More current increases retractor recruitment and discomfort.
- Distractor: Explant the device — _why wrong:_ Programming can often correct retractor recruitment before considering removal.
- Distractor: Switch to positional therapy alone — _why wrong:_ Abandoning HNS ignores a correctable programming problem.

Explanation: Different electrode configurations change which hypoglossal fibers are recruited. Retraction indicates retractor fiber activation; reconfiguring targets protrusors. Titration polysomnography then finds the lowest effective amplitude.

Pearl: HNS retraction on stimulation = reprogram the electrodes.

## T-sleep-9 — HNS Troubleshooting / Nonresponse
_source: pathophys_v470/sleep.py_

**T-sleep-9.overview**

HNS nonresponse is inadequate improvement after implantation, from programming, anatomy, or device problems. Systematic evaluation identifies correctable causes.

**T-sleep-9.physiology**

**Protrusion vs retraction balance**: effective HNS requires predominant protrusor recruitment. **Palatoglossal coupling**: tongue protrusion pulls the soft palate forward via the palatoglossus. **Sensing and timing**: stimulation must coincide with inspiration.

**T-sleep-9.pathophysiology**

**Electrode placement**: including retractor branches in the cuff reduces protrusion. **Epiglottic collapse**: unaffected by tongue protrusion. **Poor palatoglossal coupling**: tongue moves but the palate stays collapsed. **Weight gain**: increases collapsibility. **Device issues**: sensing lead failure, lead migration, or impedance problems. **Evaluation**: device interrogation, awake endoscopy during stimulation, titration PSG, and DISE with stimulation.

## T-sleep-10 — Hypoglossal Nerve Stimulation
_source: pathophys_v470/sleep.py_

**T-sleep-10.overview**

Hypoglossal nerve stimulation (HNS) is an implanted system that stimulates protrusor branches of CN XII during inspiration to open the airway. It treats moderate-to-severe OSA in CPAP-intolerant patients who meet BMI, AHI, central apnea, and DISE criteria.

**T-sleep-10.physiology**

**Genioglossus**: the main tongue protrusor and largest pharyngeal dilator; it moves the tongue base forward and stiffens the airway. **Hypoglossal nerve branches**: lateral branches mainly retract (hyoglossus, styloglossus); medial branches protrude (genioglossus, geniohyoid). **Respiratory timing**: dilator activity normally increases during inspiration. **Palatoglossal coupling**: tongue protrusion pulls the soft palate forward through the palatoglossus, opening the retropalatal airway in many patients.

**T-sleep-10.pathophysiology**

**Mechanism**: synchronized stimulation of protrusor branches during inspiration reverses sleep-related loss of genioglossus tone. **Candidate selection**: AHI roughly 15-100 (labeling has expanded), BMI generally under about 40, central and mixed apneas under 25 percent, and no complete concentric palatal collapse on DISE. **STAR trial**: 12-month AHI fell from about 29 to 9, with improved sleepiness and quality of life. **Failure modes**: retraction-dominant stimulation, epiglottic collapse, poor palatoglossal coupling, and weight gain. **Adherence**: nightly use is typically higher than CPAP.

### CC-sleep-10.1 (concept check)

Stem: Why does an HNS system place its stimulation cuff on the medial (distal) branches of the hypoglossal nerve rather than the main trunk?

- **Correct:** To recruit protrusor fibers
- Distractor: To avoid stimulating the lingual nerve — _why wrong:_ The lingual nerve is separate; the issue is protrusor versus retractor fibers.
- Distractor: Because the main trunk is too deep to reach — _why wrong:_ The trunk is accessible; selective stimulation is the goal.
- Distractor: To stimulate the geniohyoid only — _why wrong:_ Genioglossus protrusion is the main target.

Explanation: Medial branches supply the genioglossus and geniohyoid (protrusors), while lateral branches supply hyoglossus and styloglossus (retractors). Selective protrusor stimulation advances the tongue base during inspiration.

Pearl: HNS works by protruding the tongue: avoid retractors.

## T-sleep-11 — Lingual Tonsil / Tongue-Base Obstruction
_source: pathophys_v470/sleep.py_

**T-sleep-11.overview**

Lingual tonsil hypertrophy is a cause of retrolingual obstruction, especially after palatine tonsillectomy, and contributes to residual OSA. Lingual tonsillectomy treats it.

**T-sleep-11.physiology**

**Lingual tonsils**: lymphoid aggregates on the tongue base forming the inferior part of Waldeyer ring. **Retrolingual airway**: between the tongue base and posterior pharyngeal wall. **Lymphoid responsiveness**: lymphoid tissue enlarges with infection, allergy, and reflux. **Tongue base position**: depends on genioglossus tone and mandibular position.

**T-sleep-11.pathophysiology**

**Compensatory hypertrophy**: lingual tonsils may enlarge after palatine tonsillectomy. **Retrolingual obstruction**: hypertrophy narrows the airway, causing residual OSA. **Epiglottic interaction**: enlarged lingual tonsils push the epiglottis backward. **Lingual tonsillectomy**: reduces volume; risks include bleeding, edema, and taste changes. **Down syndrome**: lingual tonsil hypertrophy is common and contributes to persistent OSA.

### CC-sleep-11.1 (concept check)

Stem: A 16-year-old who had adenotonsillectomy at age 5 still snores loudly with an AHI of 14. Flexible laryngoscopy shows large lingual tonsils filling the vallecula and pushing the epiglottis backward. What is the most likely reason for persistent OSA?

- **Correct:** Lingual tonsil hypertrophy
- Distractor: Regrowth of the palatine tonsils — _why wrong:_ Palatine tonsil regrowth is uncommon and would be visible in the oropharynx.
- Distractor: Primary central sleep apnea — _why wrong:_ A central cause would not explain the visible lingual tonsil obstruction.
- Distractor: Adenoid regrowth alone — _why wrong:_ Adenoid regrowth causes nasal obstruction, not retrolingual narrowing.

Explanation: Lingual tonsil tissue may enlarge after palatine tonsillectomy, narrowing the retrolingual airway and displacing the epiglottis. Lingual tonsillectomy reduces volume; it is common in children with Down syndrome or obesity.

Pearl: Persistent OSA after T&A: look at the tongue base.

## T-sleep-12 — Maxillomandibular Advancement
_source: pathophys_v470/sleep.py_

**T-sleep-12.overview**

Maxillomandibular advancement moves the maxilla and mandible forward, enlarging the entire pharyngeal airway. It is the most effective surgical OSA treatment, especially for craniofacial skeletal deficiency.

**T-sleep-12.physiology**

**Skeletal anchorage**: the soft palate attaches to the posterior hard palate (maxilla), and the tongue, hyoid suspensory muscles, and suprahyoid muscles attach to the mandible. **Soft-tissue tension**: moving the bony attachments forward stretches pharyngeal soft tissues, stiffening the pharyngeal walls. **Airway dimensions**: the pharyngeal airway is enlarged in anteroposterior and lateral dimensions at both velopharyngeal and retrolingual levels. **Craniofacial phenotype**: maxillary and mandibular deficiency reduce the bony box containing the tongue.

**T-sleep-12.pathophysiology**

**Skeletal crowding**: a small maxillomandibular framework forces normal-sized soft tissues into a small space, increasing collapsibility. **Mechanism of benefit**: advancement enlarges the bony enclosure and tensions the lateral pharyngeal walls, reducing critical closing pressure at multiple levels at once. **Success**: high surgical success rates in appropriately selected patients, often with advancement of about 10 mm. **Complications**: malocclusion, inferior alveolar nerve paresthesia, relapse, and facial profile change (often favorable in retrognathic patients). **Indications**: severe OSA, skeletal deficiency, and failure of other therapies.

### CC-sleep-12.1 (concept check)

Stem: A 35-year-old with severe OSA (AHI 55), retrognathia, and a BMI of 26 failed CPAP and palatal surgery. DISE shows multilevel collapse. Why is maxillomandibular advancement especially effective for him?

- **Correct:** It enlarges and tensions the whole pharynx
- Distractor: It removes redundant palatal tissue — _why wrong:_ MMA moves bone; it does not resect soft tissue.
- Distractor: It treats only the retrolingual level — _why wrong:_ Advancing both jaws enlarges velopharyngeal and retrolingual levels.
- Distractor: It works by stimulating the genioglossus — _why wrong:_ That describes hypoglossal nerve stimulation.

Explanation: The soft palate, tongue, and suprahyoid muscles attach to the maxilla and mandible. Advancing both jaws enlarges the bony enclosure and tensions pharyngeal walls at every level, reducing collapsibility. Skeletal deficiency predicts a strong response.

Pearl: Multilevel collapse with skeletal deficiency: think MMA.

## T-sleep-13 — Narcolepsy / Central Hypersomnolence Recognition
_source: pathophys_v470/sleep.py_

**T-sleep-13.overview**

Narcolepsy is a central hypersomnolence disorder with excessive daytime sleepiness, sometimes with cataplexy, from hypocretin deficiency. It must be distinguished from OSA before surgery.

**T-sleep-13.physiology**

**Hypocretin (orexin)**: lateral hypothalamic neurons stabilize wakefulness and suppress inappropriate REM. **REM sleep features**: muscle atonia, dreaming, and rapid eye movements. **Sleep-wake switch**: reciprocal inhibition between wake- and sleep-promoting nuclei.

**T-sleep-13.pathophysiology**

**Hypocretin neuron loss**: likely autoimmune destruction (HLA-DQB1*06:02) causes type 1 narcolepsy with low CSF hypocretin. **REM intrusion**: cataplexy (emotion-triggered atonia), sleep paralysis, and hypnagogic hallucinations. **Diagnosis**: MSLT shows mean sleep latency of 8 minutes or less with two or more sleep-onset REM periods. **Why it matters for surgeons**: persistent sleepiness after OSA treatment may reflect narcolepsy rather than surgical failure.

### CC-sleep-13.1 (concept check)

Stem: A 22-year-old has severe daytime sleepiness despite effective CPAP for mild OSA, and reports episodes of knee buckling when laughing. What test best confirms the suspected diagnosis?

- **Correct:** MSLT after an overnight PSG
- Distractor: Repeat CPAP titration — _why wrong:_ Sleepiness persists despite effective CPAP; the cataplexy history points elsewhere.
- Distractor: Home sleep apnea test — _why wrong:_ This measures breathing, not sleep latency or REM onset.
- Distractor: Drug-induced sleep endoscopy — _why wrong:_ DISE evaluates airway collapse, not hypersomnolence.

Explanation: Narcolepsy type 1 results from hypocretin neuron loss, causing sleepiness and cataplexy. MSLT shows a short mean sleep latency with sleep-onset REM periods.

Pearl: Persistent sleepiness after treating OSA: think beyond the airway.

## T-sleep-14 — Nasal Surgery as a CPAP-Adherence Adjunct
_source: pathophys_v470/sleep.py_

**T-sleep-14.overview**

Nasal surgery rarely cures OSA but reduces CPAP pressure and improves adherence in patients with nasal obstruction. It is also used to improve HNS and oral appliance tolerance.

**T-sleep-14.physiology**

**Nasal resistance**: contributes about half of upper airway resistance. **Starling resistor model**: increased upstream resistance creates more negative downstream pharyngeal pressure, promoting collapse. **Nasal breathing during sleep**: stabilizes mandibular position and pharyngeal patency.

**T-sleep-14.pathophysiology**

**Nasal obstruction**: increases negative pharyngeal pressure and mouth breathing. **Mouth breathing**: lets the mandible and tongue fall back. **CPAP effects**: nasal obstruction increases required pressure and mask leak, reducing adherence. **Nasal surgery**: rarely cures OSA but lowers CPAP pressure and improves adherence and tolerance of oral appliances and HNS.

## T-sleep-15 — Oral Appliance Therapy
_source: pathophys_v470/sleep.py_

**T-sleep-15.overview**

Mandibular advancement devices hold the lower jaw forward during sleep, enlarging the airway. They are effective for mild-to-moderate OSA and CPAP-intolerant patients.

**T-sleep-15.physiology**

**Mandibular protrusion**: advancing the mandible pulls the genioglossus, geniohyoid, and hyoid forward. **Lateral wall tension**: protrusion stretches the palatoglossus and lateral pharyngeal walls, enlarging the velopharynx laterally. **Dental anchorage**: the appliance needs enough healthy teeth to hold the mandible forward. **TMJ adaptability**: the joint tolerates sustained protrusion in most people.

**T-sleep-15.pathophysiology**

**Airway enlargement**: protrusion increases the cross-sectional area, mainly laterally at the velopharynx. **Efficacy**: AHI reduction is less than CPAP, but higher nightly adherence makes overall effectiveness comparable for mild-to-moderate OSA. **Predictors of success**: lower AHI, positional OSA, lower BMI, and retrognathia. **Side effects**: TMJ discomfort, excessive salivation, and long-term occlusal changes. **Titration**: progressive advancement until symptoms and AHI improve.

### CC-sleep-15.1 (concept check)

Stem: A 45-year-old with mild-to-moderate OSA (AHI 14) and good dentition cannot tolerate CPAP. Why does a mandibular advancement device improve the airway?

- **Correct:** It pulls the tongue base forward
- Distractor: It splints the palate upward — _why wrong:_ The device repositions the mandible; it does not lift the palate.
- Distractor: It reduces nasal resistance — _why wrong:_ It does not change nasal airflow.
- Distractor: It increases genioglossus nerve firing — _why wrong:_ It works mechanically, not by stimulating the nerve.

Explanation: Advancing the mandible pulls the genioglossus, geniohyoid, and hyoid forward and stretches the lateral pharyngeal walls, enlarging the airway. AHI reduction is less than CPAP, but better adherence often gives comparable real-world benefit.

Pearl: Oral appliances help mild-to-moderate OSA with adequate teeth.

## T-sleep-16 — PAP Troubleshooting
_source: pathophys_v470/sleep.py_

**T-sleep-16.overview**

Positive airway pressure is first-line OSA therapy, but adherence is limited by mask discomfort, nasal obstruction, pressure intolerance, and aerophagia. Systematic troubleshooting rescues many patients before surgery.

**T-sleep-16.physiology**

**Pneumatic splint**: PAP raises intraluminal pressure above the critical closing pressure, holding the pharynx open. **Nasal route**: air must traverse the nose; nasal resistance increases required pressure. **Mouth leak**: lets pressure escape. **Adherence definition**: use of 4 hours or more on 70 percent of nights.

**T-sleep-16.pathophysiology**

**Nasal obstruction**: forces mouth breathing, leaks, and higher pressure; treating the nose improves adherence. **Mask problems**: leaks, skin irritation, and claustrophobia. **Pressure intolerance**: auto-PAP, expiratory pressure relief, or bilevel help. **Aerophagia**: swallowed air from high pressure. **Treatment-emergent central apnea**: PAP can unmask central events. **Data download**: shows residual AHI, leak, and usage.

### CC-sleep-16.1 (concept check)

Stem: A 58-year-old with severe OSA uses nasal-pillow CPAP 2 hours a night. Download shows high leak and residual AHI of 12; she wakes with a dry mouth because her nose feels blocked. What is the most effective next step?

- **Correct:** Treat the nose and control mouth leak
- Distractor: Raise the fixed CPAP pressure — _why wrong:_ Higher pressure through a blocked nose increases leak, aerophagia, and discomfort.
- Distractor: Stop CPAP and repeat polysomnography — _why wrong:_ Abandoning therapy leaves severe OSA untreated without fixing the cause.
- Distractor: Add a nightly sedative-hypnotic — _why wrong:_ Hypnotics do not address leak and may worsen respiratory events.

Explanation: Nasal obstruction forces mouth breathing, so pressure escapes through the mouth, causing leak, dryness, and residual events. Intranasal steroids or nasal surgery, heated humidification, a chin strap, or a full-face mask restore an effective seal and improve adherence.

Pearl: CPAP failure often starts in the nose.

## T-sleep-17 — Palatal Surgery
_source: pathophys_v470/sleep.py_

**T-sleep-17.overview**

Palatal surgery (UPPP, expansion sphincter pharyngoplasty, lateral pharyngoplasty, and related techniques) reconstructs the retropalatal airway in OSA. Outcomes depend on patient selection (Friedman staging, tonsil size, BMI).

**T-sleep-17.physiology**

**Pharyngeal collapsibility**: the pharynx is a muscular tube without bony support from the choanae to the larynx; patency depends on the balance between collapsing forces (negative inspiratory pressure, surrounding tissue pressure) and dilating forces (genioglossus and other dilator muscles). **Velopharynx**: the most common site of collapse in OSA. **Lateral pharyngeal walls**: palatopharyngeus and tonsils influence lateral collapse. **Palatal function**: separates the oral and nasal cavities during swallowing and speech.

**T-sleep-17.pathophysiology**

**Retropalatal narrowing**: long soft palate, large tonsils, and lateral wall laxity narrow the airway. **Friedman staging**: palate position, tonsil size, and BMI predict UPPP success (stage I best). **Modern techniques**: expansion sphincter pharyngoplasty repositions the palatopharyngeus to stiffen lateral walls rather than removing tissue. **Complications**: velopharyngeal insufficiency, nasopharyngeal stenosis, and dysphagia from overresection. **Multilevel collapse**: palatal surgery alone often fails when tongue base collapse coexists.

### CC-sleep-17.1 (concept check)

Stem: A 40-year-old with moderate OSA has Friedman tongue position I, 3+ tonsils, and a BMI of 27, and DISE shows lateral oropharyngeal collapse. Why is palatal surgery with tonsillectomy likely to succeed?

- **Correct:** Collapse is mainly retropalatal
- Distractor: It reliably corrects tongue-base collapse — _why wrong:_ Palatal surgery does not address retrolingual collapse, which is minimal here.
- Distractor: BMI does not affect surgical outcomes — _why wrong:_ Higher BMI lowers success; his BMI is favorable.
- Distractor: It also treats coexisting central apnea — _why wrong:_ Palatal surgery does not treat central events.

Explanation: Friedman stage I (favorable tongue position, large tonsils, lower BMI) predicts success because obstruction is concentrated at the velum and tonsils. Modern techniques reposition the palatopharyngeus to stiffen lateral walls rather than simply removing tissue.

Pearl: Big tonsils, favorable tongue position, modest BMI = good palatal candidate.

## T-sleep-18 — Pediatric PSG Interpretation
_source: pathophys_v470/sleep.py_

**T-sleep-18.overview**

Pediatric polysomnography uses child-specific scoring rules and thresholds; an obstructive AHI of 1 or more is abnormal. It is indicated before adenotonsillectomy in high-risk children and when history is unclear.

**T-sleep-18.physiology**

**Pediatric sleep architecture**: more slow-wave and REM sleep than adults. **Event duration**: a pediatric apnea needs only two breaths' duration, not 10 seconds. **Obstructive hypoventilation**: children often have prolonged partial obstruction with CO2 elevation rather than discrete apneas. **Higher respiratory rate**: and smaller lung volumes lead to faster desaturation.

**T-sleep-18.pathophysiology**

**Thresholds**: obstructive AHI 1-5 mild, 5-10 moderate, over 10 severe. **Hypoventilation**: end-tidal CO2 above 50 mm Hg for more than 25 percent of sleep time indicates obstructive hypoventilation. **Central apneas**: post-arousal central apneas are common and normal. **High-risk groups**: obesity, Down syndrome, craniofacial anomalies, neuromuscular disease, and age under 2 warrant PSG. **Severity and postoperative risk**: severe OSA predicts postoperative respiratory complications.

### CC-sleep-18.1 (concept check)

Stem: A 4-year-old has an obstructive AHI of 0.8 but end-tidal CO2 above 50 mm Hg for 40 percent of total sleep time, with snoring and paradoxical breathing. How should this be interpreted?

- **Correct:** Obstructive hypoventilation
- Distractor: Normal study because AHI is under 1 — _why wrong:_ Pediatric hypoventilation is abnormal even when the AHI is low.
- Distractor: Central sleep apnea — _why wrong:_ Paradoxical breathing and snoring indicate obstruction.
- Distractor: Primary snoring only — _why wrong:_ Hypercapnia indicates more than simple snoring.

Explanation: Children often maintain partial obstruction rather than discrete apneas, causing CO2 retention. End-tidal CO2 above 50 mm Hg for more than 25 percent of sleep defines obstructive hypoventilation.

Pearl: In children, read the CO2, not just the AHI.

## T-sleep-19 — Positional OSA
_source: pathophys_v470/sleep.py_

**T-sleep-19.overview**

Positional OSA is OSA predominantly in the supine position, defined by a supine AHI substantially higher than non-supine AHI. Positional therapy may treat it alone or as an adjunct.

**T-sleep-19.physiology**

**Gravity effects**: supine position lets the tongue and soft palate fall posteriorly, narrowing the airway anteroposteriorly. **Lateral position**: improves airway shape and reduces collapsibility. **Lung volume**: supine position reduces lung volume, reducing tracheal traction on the pharynx.

**T-sleep-19.pathophysiology**

**Supine-predominant collapse**: anteroposterior collapse at the palate and tongue base worsens supine. **Definitions**: Cartwright criteria (supine AHI at least twice non-supine AHI); Amsterdam classification refines categories. **Positional therapy**: vibration devices or positional aids prevent supine sleep. **Adherence**: limited for older devices; newer vibration trainers improve it. **Adjunct role**: improves residual OSA after surgery or HNS.

### CC-sleep-19.1 (concept check)

Stem: A 48-year-old has an AHI of 30 when supine and 6 in the lateral position, with most sleep spent supine. What does this pattern indicate?

- **Correct:** Positional obstructive sleep apnea
- Distractor: Predominantly central sleep apnea — _why wrong:_ The events change with position, typical of obstructive collapse.
- Distractor: Narcolepsy with secondary apnea — _why wrong:_ Narcolepsy is a disorder of sleep regulation and does not create positional AHI patterns.
- Distractor: A normal study when lateral data are used — _why wrong:_ The overall AHI is abnormal because she sleeps mostly supine.

Explanation: In the supine position, gravity pulls the tongue and soft palate back, narrowing the airway. A supine AHI at least twice the non-supine AHI meets positional criteria; positional devices can treat it alone or as an adjunct.

Pearl: Supine-predominant OSA: try positional therapy.

## T-sleep-20 — Residual OSA After Surgery
_source: pathophys_v470/sleep.py_

**T-sleep-20.overview**

Residual OSA after surgery is persistent obstruction, often from unaddressed collapse sites, weight gain, or progressive disease. Evaluation with DISE and PSG guides next steps.

**T-sleep-20.physiology**

**Multilevel airway**: the velopharynx, oropharynx, tongue base, and epiglottis each can collapse independently. **Critical closing pressure**: collapsibility depends on the most collapsible segment. **Weight and fat distribution**: parapharyngeal and tongue fat increase collapsibility.

**T-sleep-20.pathophysiology**

**Untreated collapse sites**: tongue base, lateral wall, or epiglottic collapse persists after palatal surgery. **Weight gain**: increases soft-tissue volume and erodes surgical gains. **Scar**: palatal scar can stiffen or narrow the airway. **Aging and disease progression**: dilator function declines. **Evaluation logic**: repeat PSG and DISE define residual sites to choose CPAP retrial, oral appliance, HNS, or MMA.

### CC-sleep-20.1 (concept check)

Stem: A patient's AHI fell from 40 to 25 after uvulopalatopharyngoplasty and tonsillectomy, but he gained 9 kg since surgery. Repeat DISE shows tongue-base and epiglottic collapse. What best explains the residual OSA?

- **Correct:** Untreated lower collapse plus weight gain
- Distractor: Palatal scar always causes recurrence — _why wrong:_ Scar can affect mechanics, but the DISE findings point to lower levels.
- Distractor: Central apnea induced by surgery — _why wrong:_ Palatal surgery does not cause central apnea.
- Distractor: Postoperative nasal obstruction — _why wrong:_ Nasal obstruction is not described and does not explain the DISE findings.

Explanation: Palatal surgery addresses retropalatal collapse but not retrolingual or epiglottic levels, and weight gain increases soft-tissue collapsibility. Repeat DISE and PSG guide next steps such as CPAP retrial, HNS, or MMA.

Pearl: Residual OSA after surgery: re-map the airway.

## T-sleep-21 — Restless Legs / Periodic Limb Movement Disorders
_source: pathophys_v470/sleep.py_

**T-sleep-21.overview**

Restless legs syndrome is an urge to move the legs at rest in the evening; periodic limb movements are repetitive leg movements in sleep. Both fragment sleep and can mimic OSA symptoms.

**T-sleep-21.physiology**

**Dopaminergic systems**: regulate motor control and sensory processing. **Iron**: a cofactor for tyrosine hydroxylase, the rate-limiting enzyme for dopamine synthesis. **Circadian modulation**: dopamine levels fall in the evening.

**T-sleep-21.pathophysiology**

**Brain iron deficiency**: low ferritin is associated with RLS; iron replacement helps when ferritin is low. **Dopaminergic dysfunction**: explains evening symptom worsening. **Secondary causes**: pregnancy, renal failure, neuropathy, and medications (antihistamines, antidepressants). **Periodic limb movements**: fragment sleep, mimicking OSA sleepiness. **Treatment**: iron, alpha-2-delta ligands first-line; dopamine agonists risk augmentation.

### CC-sleep-21.1 (concept check)

Stem: A 50-year-old with heavy menses has an uncomfortable urge to move her legs every evening that is relieved by walking. Her PSG shows frequent periodic limb movements with arousals. Which test should be checked first?

- **Correct:** Serum ferritin and iron studies
- Distractor: Serum calcium and PTH — _why wrong:_ Calcium disorders do not cause restless legs syndrome.
- Distractor: Thyroid peroxidase antibodies — _why wrong:_ Thyroid autoimmunity is not the first-line RLS evaluation.
- Distractor: Drug-induced sleep endoscopy — _why wrong:_ DISE evaluates airway collapse, not limb movement disorders.

Explanation: Low brain iron impairs dopamine synthesis (iron is a cofactor for tyrosine hydroxylase), driving RLS. Ferritin below about 75 ng/mL warrants iron replacement; alpha-2-delta ligands are first-line drugs, while dopamine agonists risk augmentation.

Pearl: Restless legs: check ferritin first.

## T-sleep-22 — Sleep-Related Hypoventilation
_source: pathophys_v470/sleep.py_

**T-sleep-22.overview**

Sleep-related hypoventilation is inadequate ventilation during sleep with elevated CO2, from obesity, neuromuscular disease, or chest wall disorders. Bilevel ventilation is often required.

**T-sleep-22.physiology**

**Normal sleep ventilation**: minute ventilation falls slightly and PaCO2 rises a few mm Hg. **REM atonia**: accessory muscles lose tone, leaving the diaphragm to sustain ventilation. **Respiratory load**: obesity and chest wall disease increase work of breathing.

**T-sleep-22.pathophysiology**

**Obesity hypoventilation syndrome**: mass loading, reduced lung volumes, and blunted CO2 responsiveness cause daytime hypercapnia. **Neuromuscular weakness**: diaphragm weakness causes REM hypoventilation first. **Progression**: nocturnal hypoventilation precedes daytime hypercapnia. **Treatment**: bilevel PAP provides ventilatory support beyond CPAP.

### CC-sleep-22.1 (concept check)

Stem: A 40-year-old with a BMI of 48 has a daytime PaCO2 of 52 mm Hg and a PSG showing sustained desaturation in REM without discrete apneas. What best explains this pattern?

- **Correct:** Obesity hypoventilation
- Distractor: Obstructive apneas only — _why wrong:_ Discrete obstructive events are not the main finding.
- Distractor: Central apnea from heart failure — _why wrong:_ Cheyne-Stokes breathing shows cyclic central events, not sustained REM desaturation.
- Distractor: Restless legs syndrome — _why wrong:_ RLS does not cause hypoventilation.

Explanation: Mass loading reduces lung volumes and CO2 responsiveness; during REM, accessory muscles lose tone and the diaphragm alone sustains ventilation. Bilevel PAP supports ventilation beyond CPAP.

Pearl: Daytime hypercapnia in obesity = obesity hypoventilation syndrome.

## T-sleep-23 — Tongue Base Surgery
_source: pathophys_v470/sleep.py_

**T-sleep-23.overview**

Tongue base surgery (lingual tonsillectomy, tongue base reduction, genioglossus advancement, hyoid suspension) treats retrolingual obstruction in OSA. Complications include bleeding, lingual nerve and hypoglossal injury, and airway edema.

**T-sleep-23.physiology**

**Retrolingual airway**: between the tongue base and posterior pharyngeal wall. **Genioglossus**: attaches to the genial tubercle, pulling the tongue forward. **Hyoid**: anchors tongue base and supraglottic structures. **Lingual artery and hypoglossal nerve**: run deep in the tongue base.

**T-sleep-23.pathophysiology**

**Tongue base obstruction**: macroglossia, lingual tonsil hypertrophy, and posterior tongue displacement. **Genioglossus advancement**: moves the tongue attachment forward. **Hyoid suspension**: pulls the hyoid forward and up. **Radiofrequency and resection**: reduce tissue volume, risking bleeding and edema. **Lingual artery injury**: hemorrhage.

### CC-sleep-23.1 (concept check)

Stem: A 48-year-old is undergoing coblation tongue-base reduction for retrolingual collapse. Why does the surgeon keep the resection in the midline of the tongue base?

- **Correct:** Lingual arteries and XII run laterally
- Distractor: The midline holds the most lingual tonsil — _why wrong:_ Lingual tonsil tissue spans the base; the reason for midline work is neurovascular safety.
- Distractor: It keeps the resection away from the epiglottis — _why wrong:_ The epiglottis is inferior, not lateral; safety comes from avoiding lateral vessels and nerves.
- Distractor: It prevents loss of taste entirely — _why wrong:_ Taste changes can still occur; the main reason is hemorrhage and nerve risk.

Explanation: The lingual arteries and hypoglossal nerves travel in the lateral tongue base. Staying midline reduces the risk of major hemorrhage and tongue weakness; postoperative edema can still threaten the airway.

Pearl: Tongue-base surgery: stay midline and watch the airway.

## T-sleep-24 — Tracheostomy as Definitive OSA Therapy
_source: pathophys_v470/sleep.py_

**T-sleep-24.overview**

Tracheostomy bypasses all upper-airway collapse and is nearly 100 percent effective for OSA. It is reserved for severe OSA when other treatments fail.

**T-sleep-24.physiology**

**Upper airway bypass**: air enters below the larynx, bypassing all sites of collapse. **Humidification loss**: tracheostomy bypasses nasal humidification. **Speech**: requires occlusion or a speaking valve.

**T-sleep-24.pathophysiology**

**Complete bypass**: eliminates obstructive events regardless of collapse site. **Central apneas and hypoventilation**: not treated by tracheostomy alone. **Morbid obesity**: technically difficult with stoma complications. **Quality of life**: affects voice and self-image. **Indications**: severe OSA unresponsive to other treatments, often with cardiopulmonary complications.


---

# General ENT / Emergencies

## T-general_ent-1 — Airway Foreign Body
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-1.overview**

Airway foreign bodies in adults and children cause choking, cough, and wheeze, sometimes presenting late as pneumonia. Rigid bronchoscopy remains the standard for removal in children; flexible bronchoscopy is often used in adults.

**T-general_ent-1.physiology**

**Airway branching**: the right main bronchus is wider and more vertical in adults, favoring right-sided aspiration. **Cough reflex**: clears foreign material. **Ventilation**: partial obstruction creates ball-valve effects.

**T-general_ent-1.pathophysiology**

**Ball-valve obstruction**: partial obstruction allows inspiration but traps air on expiration, causing hyperinflation and mediastinal shift away. **Complete obstruction**: distal atelectasis and pneumonia. **Organic materials**: nuts and seeds swell and cause intense inflammation. **Delayed presentation**: recurrent pneumonia, wheeze, or bronchiectasis. **Removal**: rigid bronchoscopy allows ventilation and secure extraction.

## T-general_ent-2 — Angioedema
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-2.overview**

Angioedema is deep dermal or submucosal swelling of the lips, tongue, and larynx; it may be histaminergic (allergic) or bradykinin-mediated (ACE inhibitor, hereditary). Mechanism determines treatment, and airway management is the priority.

**T-general_ent-2.physiology**

**Vascular permeability**: histamine and bradykinin increase postcapillary venule permeability. **Bradykinin metabolism**: angiotensin-converting enzyme degrades bradykinin. **C1 esterase inhibitor**: regulates the kallikrein-kinin and complement systems. **Airway tissues**: loose submucosa of the tongue, floor of mouth, and supraglottis swells easily.

**T-general_ent-2.pathophysiology**

**Histaminergic angioedema**: mast-cell degranulation with urticaria and itching; responds to epinephrine, antihistamines, and steroids. **ACE-inhibitor angioedema**: reduced bradykinin degradation causes swelling (more common in Black patients), often of the tongue and lips, without urticaria; it does not respond to epinephrine or antihistamines; standard care is stopping the drug and airway support, as icatibant showed no benefit in an RCT. **Hereditary angioedema**: C1 inhibitor deficiency or dysfunction causes recurrent episodes; treated with C1 inhibitor, icatibant, or ecallantide. **Airway assessment**: flexible laryngoscopy determines laryngeal involvement; awake fiberoptic intubation or surgical airway for progressive airway swelling.

### CC-general_ent-2.1 (concept check)

Stem: A 58-year-old Black man taking lisinopril for 3 years has rapidly progressive tongue and lip swelling without hives or itching. Why are epinephrine and antihistamines unlikely to reverse it?

- **Correct:** The swelling is bradykinin-mediated
- Distractor: The drug has caused an IgE allergy — _why wrong:_ ACE-inhibitor angioedema is not IgE-mediated, so allergy treatments target the wrong pathway.
- Distractor: Mast-cell tryptase levels are too high — _why wrong:_ Tryptase is typically normal because mast cells are not the driver.
- Distractor: Swelling comes from venous obstruction — _why wrong:_ The mechanism is increased vascular permeability, not venous obstruction.

Explanation: ACE normally breaks down bradykinin. ACE inhibition raises bradykinin, increasing vascular permeability without urticaria, and it can occur years after starting the drug. Management is stopping the ACE inhibitor and protecting the airway, guided by flexible laryngoscopy.

Pearl: Angioedema without hives on an ACE inhibitor = bradykinin: think airway, not epinephrine.

## T-general_ent-3 — Antimicrobial Stewardship in Otolaryngology
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-3.overview**

Antimicrobial stewardship applies the right drug, dose, and duration to reduce resistance, adverse effects, and C. difficile. Otolaryngology prescribes many antibiotics, especially for otitis, sinusitis, and pharyngitis, much of which is unnecessary.

**T-general_ent-3.physiology**

**Microbiome**: normal flora protect against pathogens through colonization resistance. **Antibiotic pharmacology**: time-dependent killing (beta-lactams) vs concentration-dependent killing (aminoglycosides, fluoroquinolones). **Topical delivery**: achieves high local concentrations.

**T-general_ent-3.pathophysiology**

**Resistance selection**: antibiotics kill susceptible bacteria, selecting resistant organisms. **Viral infections**: most sore throats, colds, and acute rhinosinusitis are viral. **Collateral damage**: C. difficile infection and microbiome disruption. **Stewardship strategies**: watchful waiting in AOM and ABRS, topical over oral therapy for otitis externa and tube otorrhea, narrow-spectrum agents, and short courses. **Perioperative prophylaxis**: single preoperative dose for clean-contaminated cases.

### CC-general_ent-3.1 (concept check)

Stem: A 6-year-old with tympanostomy tubes has 3 days of purulent ear drainage without fever. Why are topical antibiotic drops preferred over oral antibiotics?

- **Correct:** Drops give higher local levels
- Distractor: Oral antibiotics cannot reach the middle ear — _why wrong:_ Oral antibiotics reach the middle ear but at much lower concentrations.
- Distractor: Drops cure the underlying tube dysfunction — _why wrong:_ Drops treat infection; they do not fix tube function.
- Distractor: Drops eliminate the need for follow-up — _why wrong:_ Follow-up is still appropriate if drainage persists.

Explanation: Topical quinolone drops reach high concentrations through the tube, are more effective than oral therapy, and avoid systemic side effects and resistance.

Pearl: Tube otorrhea: drops, not pills.

## T-general_ent-4 — Carotid Blowout Syndrome
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-4.overview**

Carotid blowout is rupture of the carotid artery or its branches, usually after radiation, surgery, wound breakdown, or tumor erosion. It is often preceded by a sentinel bleed and is managed with pressure, airway control, and endovascular treatment.

**T-general_ent-4.physiology**

**Arterial wall layers**: intima, media (smooth muscle and elastin, the main strength layer), and adventitia (collagen plus vasa vasorum). **Vasa vasorum**: small vessels in the adventitia that nourish the outer media of large arteries. **Soft-tissue coverage**: healthy, well-vascularized tissue around the carotid protects it from saliva, bacteria, and desiccation. **Pressure load**: the carotid carries high systemic pressure, so any wall weakness can rupture.

**T-general_ent-4.pathophysiology**

**Radiation and surgery**: devascularize the adventitia, weakening the wall. **Wound breakdown and fistula**: saliva and infection erode the exposed artery. **Classification**: threatened (exposed artery), impending (sentinel bleed), and acute (rupture). **Management**: pressure, airway control (cuffed tube), resuscitation, and endovascular stenting or occlusion.

### CC-general_ent-4.1 (concept check)

Stem: A patient with recurrent neck cancer after radiation has a salivary fistula exposing the carotid artery. He has a self-limited bleed of about 50 mL from the wound. What is the best next step?

- **Correct:** Urgent angiography with endovascular planning
- Distractor: Wound packing and discharge home — _why wrong:_ A sentinel bleed predicts catastrophic hemorrhage and needs urgent evaluation.
- Distractor: Observation with daily dressing changes — _why wrong:_ Observation risks a fatal blowout.
- Distractor: Oral antibiotics alone — _why wrong:_ Antibiotics do not address the weakened arterial wall.

Explanation: Radiation and fistula destroy the adventitia and vasa vasorum, weakening the arterial wall. A sentinel bleed often precedes blowout; endovascular stenting or occlusion, airway protection, and goals-of-care discussion are needed.

Pearl: Sentinel bleed from an exposed carotid = act now.

## T-general_ent-5 — Caustic Ingestion
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-5.overview**

Caustic ingestion of alkalis or acids injures the upper aerodigestive tract and esophagus, ranging from mucosal burns to perforation. Endoscopy within 12-48 hours grades injury and predicts stricture.

**T-general_ent-5.physiology**

**Esophageal wall**: mucosa, submucosa, and muscularis without serosa. **Healing**: inflammation, granulation, and collagen deposition over weeks, with stricture formation by 3 weeks onward. **Esophageal narrowings**: sites where caustics pool.

**T-general_ent-5.pathophysiology**

**Alkali**: liquefactive necrosis penetrates deeply, causing full-thickness esophageal injury (drain cleaners, button batteries). **Acid**: coagulative necrosis forms an eschar that limits penetration, but acid causes gastric injury. **Zargar grading**: grade 2b and 3 predict stricture and perforation. **Stricture**: collagen deposition and contraction cause stenosis weeks later. **Long-term risk**: increased esophageal carcinoma risk decades later.

### CC-general_ent-5.1 (concept check)

Stem: A 3-year-old swallowed liquid drain cleaner containing sodium hydroxide. She is drooling and refuses to drink. Why does alkali usually cause deeper esophageal injury than acid?

- **Correct:** Liquefactive necrosis penetrates the wall
- Distractor: Alkali forms a protective surface eschar — _why wrong:_ Acids produce coagulation necrosis with an eschar; alkali does not.
- Distractor: Alkali is rapidly neutralized by saliva — _why wrong:_ Saliva cannot neutralize a strong alkali in meaningful amounts.
- Distractor: Alkali spares the esophagus and injures the stomach — _why wrong:_ Alkali mainly injures the esophagus; acids more often injure the stomach.

Explanation: Alkali saponifies fats and liquefies tissue, penetrating deeply and risking perforation and stricture. Acids cause coagulation necrosis whose eschar limits depth. Endoscopy at 12-48 hours grades the injury (Zargar) and predicts stricture.

Pearl: Alkali burns deep; acid forms an eschar.

## T-general_ent-6 — Cervical Necrotizing Fasciitis
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-6.overview**

Cervical necrotizing fasciitis is rapidly spreading infection along fascial planes with tissue necrosis, usually from odontogenic or pharyngeal sources. Aggressive debridement and antibiotics are lifesaving.

**T-general_ent-6.physiology**

**Fascial planes**: the superficial and deep cervical fascia form low-resistance channels. **Skin perfusion**: skin depends on perforators passing through fascia. **Anaerobic environment**: necrotic tissue supports anaerobes.

**T-general_ent-6.pathophysiology**

**Polymicrobial synergy**: streptococci and anaerobes release toxins and enzymes (hyaluronidase) that spread along fascia. **Perforator thrombosis**: causes skin necrosis, often with dusky skin and crepitus. **Gas formation**: anaerobes produce gas visible on CT. **Spread**: descending infection into the mediastinum. **Systemic toxicity**: sepsis develops rapidly. **Treatment**: early radical debridement, broad antibiotics, and repeated debridement.

### CC-general_ent-6.1 (concept check)

Stem: A diabetic patient with an odontogenic infection has rapidly spreading neck erythema with dusky skin, crepitus, and severe pain out of proportion to the exam. CT shows gas tracking along fascial planes. What is the essential treatment?

- **Correct:** Urgent wide surgical debridement
- Distractor: High-dose IV antibiotics alone — _why wrong:_ Antibiotics cannot reach necrotic tissue without debridement.
- Distractor: Needle aspiration of the gas — _why wrong:_ Necrotizing infection is not a drainable collection.
- Distractor: Hyperbaric oxygen as primary therapy — _why wrong:_ Hyperbaric oxygen is at most an adjunct.

Explanation: Polymicrobial infection spreads along fascia, thrombosing perforating vessels and causing skin necrosis and gas. Early radical debridement, repeated as needed, plus broad antibiotics reduce mortality.

Pearl: Pain out of proportion + crepitus + gas = necrotizing fasciitis: operate.

## T-general_ent-7 — Chyle Leak
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-7.overview**

Chyle leak follows injury to the thoracic duct or its tributaries during neck dissection, typically left level IV. It causes milky drainage that increases with enteral feeding and can lead to malnutrition and immunodeficiency.

**T-general_ent-7.physiology**

**Thoracic duct**: carries lymph and chylomicrons from the intestines, ascending to the left venous angle (internal jugular-subclavian junction). **Chyle composition**: triglycerides, lymphocytes, proteins, and fat-soluble vitamins. **Flow**: up to 2-4 liters per day, increasing after fatty meals.

**T-general_ent-7.pathophysiology**

**Injury**: duct or tributaries injured at the left venous angle, sometimes right-sided. **Diagnosis**: milky drainage with triglycerides over 110 mg/dL or presence of chylomicrons. **Consequences**: fluid and electrolyte loss, hypoproteinemia, lymphopenia, and wound breakdown. **Medium-chain triglycerides**: absorbed directly into the portal vein, bypassing lymphatics, reducing chyle flow. **Treatment**: diet modification, octreotide, pressure, and re-exploration or thoracic duct embolization for high output.

### CC-general_ent-7.1 (concept check)

Stem: Three days after left neck dissection, drain output turns milky and rises to 700 mL/day once tube feeds start. Drain fluid triglycerides are 450 mg/dL. Why does output rise with feeding?

- **Correct:** Dietary fat enters lymph as chylomicrons
- Distractor: Feeding raises venous pressure in the neck — _why wrong:_ Venous pressure does not explain the milky, triglyceride-rich fluid.
- Distractor: Tube feeds leak through a pharyngeal fistula — _why wrong:_ A pharyngeal leak would contain feed or saliva, not chylomicrons.
- Distractor: Feeding stimulates salivary flow into the drain — _why wrong:_ Saliva is not milky and is not triglyceride-rich.

Explanation: Long-chain fats are absorbed into intestinal lymph as chylomicrons and carried by the thoracic duct to the left venous angle. A medium-chain triglyceride diet (absorbed directly into portal blood), octreotide, pressure, and re-exploration or embolization for high output reduce flow.

Pearl: Milky drain after left neck dissection = chyle leak: cut long-chain fat.

## T-general_ent-8 — Common ENT Consult Triage / Disposition
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-8.overview**

ENT consult triage prioritizes airway threats, bleeding, vision-threatening and intracranial complications, and time-sensitive conditions such as SSNHL. Recognizing red flags determines disposition.

**T-general_ent-8.physiology**

**Airway geometry**: the narrowest points are the glottis in adults and the subglottis in children, where small changes cause obstruction. **Time-critical tissues**: the cochlea, optic nerve, and facial nerve tolerate ischemia or compression poorly. **Blood volume**: children have small blood volumes, making bleeding more dangerous. **Infection spread**: fascial planes and valveless veins allow rapid spread.

**T-general_ent-8.pathophysiology**

**Airway red flags**: stridor, drooling, tripod positioning, voice change, and inability to handle secretions point to supraglottic or laryngeal obstruction. **Vision threats**: proptosis, reduced acuity, afferent pupillary defect, and ophthalmoplegia in sinusitis or trauma. **Bleeding**: posterior epistaxis and post-tonsillectomy bleeding cause hypovolemia and aspiration. **Time-sensitive**: SSNHL (steroids), Bell palsy (steroids within 72 hours), button battery (minutes to hours), septal hematoma (cartilage necrosis), and retrobulbar hematoma. **Disposition logic**: unstable airway or progressive infection requires admission and OR; uncomplicated cases can be managed outpatient.

### CC-general_ent-8.1 (concept check)

Stem: Four ENT consults arrive at once: a stable peritonsillar abscess, a closed nasal fracture, uncomplicated otitis externa, and a facial trauma patient with a tense proptotic eye and worsening vision. Which needs attention first?

- **Correct:** The proptotic, failing eye
- Distractor: The stable peritonsillar abscess — _why wrong:_ A stable PTA needs drainage soon, but vision can be lost within minutes.
- Distractor: The closed nasal fracture — _why wrong:_ Nasal fractures are typically reduced days later after swelling settles.
- Distractor: The uncomplicated otitis externa — _why wrong:_ Otitis externa is treated as an outpatient.

Explanation: Retrobulbar hematoma causes optic nerve ischemia and permanent vision loss within about 90 minutes, so lateral canthotomy and cantholysis take priority. Triage by what can be lost irreversibly in minutes: airway, vision, and uncontrolled bleeding.

Pearl: Airway, vision, bleeding: triage by what can be lost in minutes.

## T-general_ent-9 — Cranial Nerve Examination / Skull Base Localization
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-9.overview**

Combinations of cranial nerve deficits localize lesions to the brainstem, skull base foramina, or extracranial spaces. Recognizing patterns is essential in otolaryngology.

**T-general_ent-9.physiology**

**Cranial nerve exits**: cribriform plate (I), optic canal (II), superior orbital fissure (III, IV, V1, VI), foramen rotundum (V2), foramen ovale (V3), IAC (VII, VIII), jugular foramen (IX, X, XI), hypoglossal canal (XII). **Brainstem organization**: midbrain (III, IV), pons (V-VIII), medulla (IX-XII).

**T-general_ent-9.pathophysiology**

**Cavernous sinus syndrome**: III, IV, V1, V2, VI and sympathetics. **Orbital apex syndrome**: II plus III, IV, V1, VI. **Gradenigo syndrome**: V and VI with otitis. **CPA syndrome**: V, VII, VIII. **Vernet syndrome**: IX, X, XI at the jugular foramen. **Collet-Sicard**: IX-XII. **Villaret**: IX-XII plus Horner.

### CC-general_ent-9.1 (concept check)

Stem: A patient has numbness of the forehead and cheek, diplopia on lateral gaze, and ptosis, but normal vision. Where is the lesion most likely?

- **Correct:** Cavernous sinus
- Distractor: Orbital apex — _why wrong:_ Orbital apex lesions cause vision loss from optic nerve involvement.
- Distractor: Jugular foramen — _why wrong:_ Jugular foramen lesions affect IX, X, and XI.
- Distractor: Internal auditory canal — _why wrong:_ IAC lesions affect VII and VIII.

Explanation: The cavernous sinus contains III, IV, V1, V2, VI and the sympathetic plexus, but not the optic nerve. V2 involvement distinguishes it from superior orbital fissure syndrome.

Pearl: V1 + V2 + ophthalmoplegia with normal vision = cavernous sinus.

## T-general_ent-10 — Deep Neck Abscess Drainage
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-10.overview**

Deep neck abscess drainage evacuates pus from neck spaces through transcervical or transoral approaches. It requires airway planning and knowledge of fascial spaces and great vessel relationships.

**T-general_ent-10.physiology**

**Fascial spaces**: contain infection until pressure or erosion spreads it. **Carotid sheath**: lies within the space being drained. **Transoral access**: suitable for medial collections (retropharyngeal, peritonsillar).

**T-general_ent-10.pathophysiology**

**Abscess**: walled-off pus with poor antibiotic penetration requires drainage. **Phlegmon**: may respond to antibiotics. **Approach selection**: medial collections transorally; lateral collections transcervically. **Vessel risk**: carotid and jugular are at risk. **Airway**: often secured before drainage.

### CC-general_ent-10.1 (concept check)

Stem: A 35-year-old has a parapharyngeal abscess lateral to the great vessels on CT, with fever despite 48 hours of IV antibiotics. Why is a transcervical rather than transoral approach chosen?

- **Correct:** Lateral collections are safest reached through the neck
- Distractor: Transoral drainage is never used in adults — _why wrong:_ Transoral drainage is used for medial collections such as peritonsillar abscess.
- Distractor: Transcervical drainage avoids anesthesia — _why wrong:_ Transcervical drainage requires anesthesia and airway planning.
- Distractor: Antibiotics fail only after transoral drainage — _why wrong:_ Approach does not determine antibiotic effectiveness.

Explanation: Collections medial to the great vessels can be drained transorally, but lateral collections require transcervical exposure with control of the carotid sheath. Abscesses that fail antibiotics or threaten the airway need drainage.

Pearl: Medial collection: through the mouth; lateral collection: through the neck.

## T-general_ent-11 — Deep Neck Space Infection
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-11.overview**

Deep neck space infections spread along fascial planes from dental, tonsillar, salivary, or nodal sources. They threaten the airway, mediastinum, and great vessels, and are managed with airway control, antibiotics, and drainage.

**T-general_ent-11.physiology**

**Cervical fascia**: the superficial layer of the deep cervical fascia invests the SCM, trapezius, and glands; the middle layer surrounds the viscera (pretracheal); the deep layer has prevertebral and alar divisions. **Key spaces**: submandibular (sublingual above and submaxillary below the mylohyoid), parapharyngeal (pre- and poststyloid), retropharyngeal, danger, prevertebral, and carotid space. **Danger space**: between alar and prevertebral fascia, extending from skull base to diaphragm. **Dental anatomy**: roots of the second and third mandibular molars lie below the mylohyoid line.

**T-general_ent-11.pathophysiology**

**Source**: odontogenic infection is the most common adult source; tonsillitis and lymphadenitis are common in children. **Fascial spread**: infection follows planes of least resistance, from the submandibular space to parapharyngeal and retropharyngeal spaces, then through the danger space into the mediastinum. **Airway compromise**: floor-of-mouth swelling displaces the tongue upward and backward; pharyngeal wall edema narrows the airway. **Vascular complications**: internal jugular thrombophlebitis (Lemierre), carotid erosion, and septic emboli. **Microbiology**: polymicrobial streptococci, anaerobes, and S. aureus. **Treatment logic**: secure the airway first; CT distinguishes phlegmon from abscess; drainage for abscess and failure of medical therapy.

### CC-general_ent-11.1 (concept check)

Stem: A 45-year-old with a lower molar infection develops neck swelling and fever. CT shows an abscess in the retropharyngeal space extending below the level of T2 into the posterior mediastinum. Which fascial pathway allowed this spread?

- **Correct:** The danger space behind the alar fascia
- Distractor: The carotid sheath to the aortic arch — _why wrong:_ The carotid sheath can carry infection, but posterior mediastinal spread below T2 follows the danger space.
- Distractor: The pretracheal space to the anterior chest — _why wrong:_ Pretracheal spread reaches the anterior mediastinum, not the posterior mediastinum.
- Distractor: The submandibular space directly to the pleura — _why wrong:_ There is no direct path from the submandibular space to the pleura.

Explanation: The retropharyngeal space ends near T2 where the alar and visceral fascia fuse. The danger space, between alar and prevertebral fascia, extends to the diaphragm, letting infection reach the posterior mediastinum. Mediastinitis needs urgent drainage.

Pearl: Retropharyngeal infection below T2 = danger space = mediastinitis risk.

## T-general_ent-12 — ENT Fluids / Electrolytes / Nutrition
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-12.overview**

Fluid, electrolyte, and nutrition management matters in head and neck surgery, where patients often start malnourished and may develop SIADH, diabetes insipidus, refeeding syndrome, or hypocalcemia. Getting these right prevents wound breakdown, fistula, and arrhythmia.

**T-general_ent-12.physiology**

**Body water compartments**: about 60 percent of body weight is water, two-thirds intracellular and one-third extracellular. **Sodium and water balance**: ADH from the posterior pituitary controls free water reabsorption; serum sodium reflects water balance more than sodium content. **Calcium regulation**: PTH and vitamin D maintain ionized calcium. **Nutritional needs**: roughly 25-30 kcal/kg/day and 1.2-1.5 g/kg/day of protein after major surgery. **Gut function**: enteral feeding maintains gut barrier and immunity.

**T-general_ent-12.pathophysiology**

**Malnutrition**: head and neck cancer impairs swallowing and increases catabolism, raising fistula and wound complications. **Refeeding syndrome**: after starvation, carbohydrates trigger insulin release and intracellular shift of phosphate, potassium, and magnesium, causing hypophosphatemia, arrhythmia, and heart failure. **SIADH**: inappropriate ADH after pituitary surgery, pain, or medications causes hyponatremia. **Diabetes insipidus**: ADH deficiency after skull-base surgery causes dilute polyuria and hypernatremia. **Post-thyroidectomy hypocalcemia**: parathyroid injury. **Enteral over parenteral**: whenever the gut works, enteral nutrition reduces infection.

### CC-general_ent-12.1 (concept check)

Stem: A malnourished patient with obstructing oral cancer who ate little for 2 weeks starts full-calorie tube feeds. On day 3 she develops weakness, confusion, and arrhythmia; phosphate is 0.9 mg/dL. What is the mechanism?

- **Correct:** Insulin drives phosphate into cells
- Distractor: Phosphate lost through diarrhea from feeds — _why wrong:_ Diarrhea does not account for this rapid, severe drop with refeeding.
- Distractor: Hypercalcemia from vitamin D in the formula — _why wrong:_ Formula vitamin D does not cause this, and calcium is not the abnormality.
- Distractor: Acute kidney injury retaining phosphate — _why wrong:_ Kidney injury raises phosphate rather than lowering it.

Explanation: After starvation, carbohydrate refeeding triggers insulin release, shifting phosphate, potassium, and magnesium into cells and depleting serum levels. Refeeding syndrome causes weakness, arrhythmia, and heart failure; start feeds slowly and replace electrolytes in high-risk patients.

Pearl: Malnourished head and neck patient: start feeds slowly to avoid refeeding syndrome.

## T-general_ent-13 — ENT Imaging Fundamentals
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-13.overview**

CT, MRI, ultrasound, and PET each answer different questions in otolaryngology. Choosing the right test and reading key findings drives diagnosis.

**T-general_ent-13.physiology**

**CT**: X-ray attenuation, excellent for bone (temporal bone, sinuses, fractures). **MRI**: proton relaxation, excellent for soft tissue, nerves, and marrow; T1 shows fat bright; T2 shows fluid bright; gadolinium shows enhancement. **Ultrasound**: sound wave reflection, excellent for thyroid and superficial lesions. **PET**: FDG uptake reflects glucose metabolism.

**T-general_ent-13.pathophysiology**

**Bone erosion vs remodeling**: aggressive erosion suggests malignancy or infection; smooth remodeling suggests slow growth. **Restricted diffusion**: cholesteatoma, epidermoid, and abscess. **Enhancement**: tumors and inflammation. **Signal patterns**: cholesterol granuloma T1 and T2 bright; fungal concretions T2 dark. **PET false positives**: inflammation after radiation.

### CC-general_ent-13.1 (concept check)

Stem: A 40-year-old with chronic otorrhea and prior mastoidectomy has a middle-ear soft-tissue mass on CT. On MRI, the mass shows bright signal on diffusion-weighted imaging (restricted diffusion). What does this suggest?

- **Correct:** Recurrent cholesteatoma
- Distractor: Postoperative granulation tissue — _why wrong:_ Granulation tissue does not restrict diffusion and enhances on delayed contrast imaging.
- Distractor: Simple serous effusion — _why wrong:_ Fluid does not restrict diffusion.
- Distractor: Cholesterol granuloma — _why wrong:_ Cholesterol granuloma is bright on T1 and T2 rather than restricting diffusion.

Explanation: Keratin in cholesteatoma restricts water diffusion, appearing bright on non-echo-planar DWI. This allows imaging surveillance after canal-wall-up surgery and can avoid some second-look operations.

Pearl: Restricted diffusion in the middle ear after surgery = recurrent cholesteatoma.

## T-general_ent-14 — ENT Perioperative Anesthesia / Difficult Airway Planning
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-14.overview**

Airway planning in ENT anticipates difficult mask ventilation, intubation, and surgical airway, coordinating with anesthesia. Shared airway cases and obstructing pathology demand clear plans.

**T-general_ent-14.physiology**

**Airway assessment**: Mallampati, mouth opening, thyromental distance, neck mobility. **Oxygen reserve**: preoxygenation extends safe apnea time. **Spontaneous ventilation**: maintains airway patency in obstructing lesions.

**T-general_ent-14.pathophysiology**

**Obstructing tumors**: induction removes muscle tone and can convert partial to complete obstruction. **Spontaneous ventilation**: preserved in awake techniques to maintain airway patency. **Awake approaches**: awake fiberoptic intubation or awake tracheostomy under local anesthesia. **Can't intubate, can't oxygenate**: emergency front-of-neck access via cricothyroidotomy. **Shared airway**: surgeon and anesthesiologist coordinate ventilation strategy.

### CC-general_ent-14.1 (concept check)

Stem: A 60-year-old with a large supraglottic tumor has stridor at rest. Why is standard induction with paralysis dangerous?

- **Correct:** It may cause total obstruction
- Distractor: Paralytics cause the tumor to bleed — _why wrong:_ Bleeding is not the main concern of paralysis.
- Distractor: Induction agents enlarge the tumor — _why wrong:_ Drugs do not enlarge the tumor.
- Distractor: Paralysis prevents any later tracheostomy — _why wrong:_ Tracheostomy remains possible but becomes an emergency.

Explanation: Awake patients maintain airway patency with muscle tone; induction removes it, and an obstructing mass can close the airway completely. Awake fiberoptic intubation or awake tracheostomy preserves spontaneous breathing.

Pearl: Stridor from an obstructing tumor: secure the airway awake.

## T-general_ent-15 — Ear and Nasal Foreign Body Removal
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-15.overview**

Ear and nasal foreign bodies are common in children; button batteries and magnets require urgent removal. Technique depends on object type and location.

**T-general_ent-15.physiology**

**External auditory canal**: narrowest at the bony-cartilaginous junction, with thin, sensitive skin over the bony canal. **Tympanic membrane**: lies medially and can be injured during removal. **Nasal cavity**: the inferior meatus and anterior septum trap objects. **Nasopharynx**: objects pushed backward can be aspirated.

**T-general_ent-15.pathophysiology**

**Button batteries**: cause liquefactive necrosis within hours, threatening septal perforation and canal injury. **Magnets**: paired magnets across the septum cause pressure necrosis. **Organic objects**: swell with moisture, making removal harder. **Unilateral foul discharge**: suggests a retained nasal foreign body. **Removal risk**: canal trauma and posterior displacement into the airway.

### CC-general_ent-15.1 (concept check)

Stem: A 3-year-old has had foul-smelling discharge from one nostril for 2 weeks. Exam shows a button battery in the anterior nasal cavity. Why must it be removed urgently?

- **Correct:** It causes rapid tissue necrosis
- Distractor: It will block the Eustachian tube — _why wrong:_ Nasal batteries cause local necrosis rather than ear disease.
- Distractor: It causes sinusitis within minutes — _why wrong:_ Sinusitis is not the main concern.
- Distractor: It will migrate into the brain — _why wrong:_ Migration into the brain is not the mechanism of harm.

Explanation: Button batteries generate hydroxide at the negative pole, causing liquefactive necrosis and septal perforation within hours. Unilateral foul discharge in a child suggests a foreign body.

Pearl: Button battery anywhere = emergency removal.

## T-general_ent-16 — Epistaxis
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-16.overview**

Epistaxis is very common; most is anterior from Kiesselbach plexus and controlled with pressure, vasoconstrictors, cautery, or packing. Posterior bleeding is less common but heavier, often in older and anticoagulated patients, and may need endoscopic ligation or embolization.

**T-general_ent-16.physiology**

**Dual carotid supply**: the external carotid (sphenopalatine, greater palatine, superior labial) and internal carotid (anterior and posterior ethmoid arteries) supply the nose. **Kiesselbach plexus**: anastomosis on the anterior septum of sphenopalatine, anterior ethmoid, greater palatine, and superior labial branches. **Mucosal humidity**: nasal mucosa is thin and highly vascular, protected by humidification. **Hemostasis**: vasoconstriction, platelet plug, and coagulation cascade.

**T-general_ent-16.pathophysiology**

**Anterior bleeds**: mucosal drying, digital trauma, and inflammation expose Kiesselbach vessels. **Posterior bleeds**: sphenopalatine branches in older patients with hypertension and atherosclerosis; harder to visualize and pack. **Systemic factors**: anticoagulants, antiplatelets, coagulopathy, liver disease, and hereditary hemorrhagic telangiectasia. **HHT**: autosomal dominant fragile telangiectasias (ENG, ACVRL1) cause recurrent bleeding. **Unilateral recurrent bleeding with obstruction**: in an adolescent male suggests JNA. **Management logic**: direct pressure and vasoconstrictors; targeted cautery; packing for diffuse bleeding; SPA ligation for refractory posterior bleeding; ethmoid artery ligation for superior bleeding.

### CC-general_ent-16.1 (concept check)

Stem: A 72-year-old on apixaban has brisk bleeding from both nostrils and the posterior pharynx despite well-placed bilateral anterior packing. What is the most likely source?

- **Correct:** Sphenopalatine artery branches posteriorly
- Distractor: Kiesselbach plexus on the anterior septum — _why wrong:_ Anterior bleeding is usually controlled by anterior packing.
- Distractor: The anterior ethmoid artery — _why wrong:_ The anterior ethmoid supplies the superior nose; brisk posterior pharyngeal bleeding points to the SPA.
- Distractor: The superior labial artery — _why wrong:_ The labial artery contributes to Kiesselbach plexus anteriorly.

Explanation: Posterior epistaxis arises from sphenopalatine artery branches on the posterior septum and lateral wall, more common in older and anticoagulated patients. Posterior packing or endoscopic SPA ligation controls it.

Pearl: Bleeding past anterior packing = posterior source.

## T-general_ent-17 — Esophageal Foreign Body
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-17.overview**

Esophageal foreign bodies lodge at narrowings, most often at the cricopharyngeus in children and over strictures or food boluses in adults. Button batteries and sharp objects require urgent removal.

**T-general_ent-17.physiology**

**Physiologic narrowings**: cricopharyngeus, aortic arch, left main bronchus, and lower esophageal sphincter. **Esophageal motility**: peristalsis moves food; reduced in certain disorders. **Esophageal wall**: thin with no serosa.

**T-general_ent-17.pathophysiology**

**Impaction**: objects lodge at narrowings or pathologic strictures (EoE, rings, cancer). **Food bolus impaction**: in adults, often reveals EoE or stricture. **Pressure necrosis**: prolonged impaction injures mucosa and can cause perforation. **Button batteries**: generate hydroxide and cause rapid necrosis. **Sharp objects**: perforation risk.

## T-general_ent-18 — Esophageal Perforation / Cervical Mediastinitis
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-18.overview**

Esophageal perforation (iatrogenic, foreign body, Boerhaave) leaks contents into the neck and mediastinum, causing rapidly progressive infection. Early diagnosis and drainage reduce high mortality.

**T-general_ent-18.physiology**

**No serosa**: unlike the stomach and intestine, the esophagus lacks a serosal layer, so leaks are not contained. **Killian dehiscence**: a weak triangle between the thyropharyngeus and cricopharyngeus, a common site of instrument perforation. **Fascial continuity**: the retropharyngeal and danger spaces connect the neck to the posterior mediastinum. **Saliva and gastric contents**: carry heavy bacterial loads and digestive enzymes.

**T-general_ent-18.pathophysiology**

**Iatrogenic perforation**: endoscopy and dilation, most often near the cricopharyngeus (Killian dehiscence). **Boerhaave syndrome**: forceful vomiting ruptures the distal esophagus. **Mediastinitis**: saliva, bacteria, and gastric contents cause necrotizing infection. **Signs**: pain, crepitus, fever, and pneumomediastinum. **Treatment**: NPO, antibiotics, drainage, and repair.

### CC-general_ent-18.1 (concept check)

Stem: Six hours after rigid esophagoscopy for a fish bone, a patient has neck pain, fever, and crepitus. CT shows air tracking along the retropharyngeal space into the mediastinum. Why is infection so dangerous here?

- **Correct:** Leaks spread freely without a serosal barrier
- Distractor: The esophagus has a thick serosa that traps bacteria — _why wrong:_ The esophagus lacks a serosa, so leaks are not contained.
- Distractor: Saliva is sterile — _why wrong:_ Saliva carries a heavy bacterial load.
- Distractor: The mediastinum has no lymphatics — _why wrong:_ The issue is free spread along fascial planes, not lymphatics.

Explanation: Without a serosa, saliva and bacteria spread through the retropharyngeal and danger spaces into the mediastinum, causing rapidly progressive mediastinitis. Early NPO, broad antibiotics, drainage, and repair reduce mortality.

Pearl: Pain and crepitus after esophagoscopy = perforation until proven otherwise.

## T-general_ent-19 — Evidence Interpretation / Outcomes Research
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-19.overview**

Evidence interpretation (study design, bias, statistics, and clinical practice guidelines) lets clinicians evaluate literature and apply it. It is tested on boards and essential for practice.

**T-general_ent-19.physiology**

**Evidence hierarchy**: systematic reviews of randomized trials sit at the top, then RCTs, cohort studies, case-control studies, case series, and expert opinion. **Test characteristics**: sensitivity (true positive rate) and specificity (true negative rate) are properties of the test. **Predictive values**: positive and negative predictive values depend on disease prevalence. **Likelihood ratios**: combine sensitivity and specificity to update pretest probability.

**T-general_ent-19.pathophysiology**

**Bias**: selection bias, measurement bias, and confounding distort associations; randomization and blinding reduce them. **Prevalence effect**: in low-prevalence populations, even good tests produce many false positives. **Absolute vs relative risk**: relative risk reductions can exaggerate benefit; NNT equals 1 divided by absolute risk reduction. **Type I and type II errors**: false positives (alpha) and false negatives (beta, related to power). **Guidelines**: AAO-HNS CPGs grade evidence and strength of recommendation.

### CC-general_ent-19.1 (concept check)

Stem: A screening test for nasopharyngeal carcinoma has 95 percent sensitivity and 95 percent specificity. It is applied to a low-risk US population where prevalence is 1 in 10,000. Why will most positive results be false positives?

- **Correct:** Low prevalence lowers PPV
- Distractor: Sensitivity is too low to detect cancer — _why wrong:_ Sensitivity is high; the problem is the rarity of disease.
- Distractor: Specificity falls when prevalence is low — _why wrong:_ Specificity is a property of the test and does not change with prevalence.
- Distractor: The test was validated in the wrong country — _why wrong:_ Validation setting is not the core reason; the arithmetic of prevalence is.

Explanation: With 10,000 people tested, about 1 true case is found while 5 percent of 9,999 healthy people (about 500) test positive, so PPV is about 0.2 percent. Predictive values depend on prevalence; sensitivity and specificity do not.

Pearl: Rare disease + good test = mostly false positives.

## T-general_ent-20 — Geriatric Otolaryngology / Frailty
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-20.overview**

Older adults have presbycusis, presbyphonia, dysphagia, balance disorders, and higher surgical risk from frailty. Frailty assessment predicts outcomes better than age.

**T-general_ent-20.physiology**

**Declining physiologic reserve**: cardiopulmonary, renal, and muscle reserve fall with age, reducing tolerance of surgical stress. **Sensory aging**: hearing (presbycusis), vision, vestibular function, and proprioception decline together. **Swallowing aging (presbyphagia)**: slower swallow triggering and reduced pharyngeal strength. **Pharmacology**: altered drug metabolism and polypharmacy increase adverse effects.

**T-general_ent-20.pathophysiology**

**Frailty phenotype**: unintentional weight loss, weakness, exhaustion, slow gait, and low activity predict complications, delirium, and mortality better than age. **Postoperative delirium**: anesthesia, opioids, sleep disruption, and sensory deprivation precipitate it. **Aspiration**: presbyphagia and neurologic disease increase pneumonia risk. **Falls**: vestibular and sensory loss combine with medications to increase fall risk. **Hearing loss**: linked to social isolation and cognitive decline. **Care logic**: frailty screening, prehabilitation, and shared decision-making.

### CC-general_ent-20.1 (concept check)

Stem: An 84-year-old with slow gait, unintentional 6 kg weight loss, and weak grip is being considered for a long head and neck resection. Why is frailty assessment more useful than age alone?

- **Correct:** Frailty predicts complications
- Distractor: Age determines eligibility for surgery — _why wrong:_ Chronological age alone is a poor predictor of outcomes.
- Distractor: Frailty only predicts length of stay — _why wrong:_ Frailty predicts complications, delirium, and mortality too.
- Distractor: Frail patients always do better with surgery — _why wrong:_ Frailty increases surgical risk.

Explanation: Frailty reflects reduced physiologic reserve across systems. Frailty scores predict postoperative complications, delirium, discharge to care facilities, and mortality better than age, guiding shared decision-making and prehabilitation.

Pearl: Measure frailty, not just age.

## T-general_ent-21 — Grafts / Implants / Biomaterials in ENT
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-21.overview**

Autografts, allografts, xenografts, and alloplastic implants are used to reconstruct cartilage, bone, and soft tissue in otolaryngology. Choice balances biocompatibility, resorption, infection, and extrusion.

**T-general_ent-21.physiology**

**Graft take**: grafts survive by plasmatic imbibition, then inosculation and revascularization from the recipient bed. **Cartilage biology**: avascular, nourished by diffusion; chondrocytes survive transplantation if not crushed. **Bone healing**: osteoconduction (scaffold), osteoinduction (growth signals such as BMPs), and osteogenesis (living cells). **Foreign body response**: implants are encapsulated by fibrous tissue.

**T-general_ent-21.pathophysiology**

**Autografts**: lowest infection and rejection but donor morbidity. **Alloplasts**: silicone, porous polyethylene, and titanium; risk of infection and extrusion, especially in thin or irradiated tissue. **Resorption**: crushed cartilage and nonvascularized bone resorb. **Biofilms**: form on implants.

### CC-general_ent-21.1 (concept check)

Stem: One year after dorsal augmentation with a porous polyethylene implant, a patient with thin dorsal skin develops redness and then exposure of the implant. Why did it fail?

- **Correct:** Thin cover cannot protect an alloplast
- Distractor: Porous implants are rejected by antibodies — _why wrong:_ Immunologic rejection is not the usual mechanism of alloplast failure.
- Distractor: The implant resorbed and shifted — _why wrong:_ Porous polyethylene does not resorb.
- Distractor: The implant was too vascularized — _why wrong:_ Tissue ingrowth helps stability; inadequate coverage is the problem.

Explanation: Alloplastic implants depend on thick, well-vascularized soft tissue cover. Thin, scarred, or irradiated skin lets implants become exposed, colonized by biofilm, and extrude. Autologous cartilage tolerates thin coverage better.

Pearl: Alloplasts need generous, healthy coverage.

## T-general_ent-22 — Hemostasis / Coagulopathy / Antithrombotic Management in ENT
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-22.overview**

Perioperative hemostasis requires assessing bleeding risk, managing antithrombotics, and recognizing coagulopathy. Head and neck surgery has bleeding complications that can obstruct the airway.

**T-general_ent-22.physiology**

**Primary hemostasis**: von Willebrand factor tethers platelets to exposed collagen, and platelets aggregate via thromboxane A2 and ADP. **Secondary hemostasis**: the coagulation cascade converges on thrombin, which converts fibrinogen to fibrin. **Fibrinolysis**: plasmin breaks down clot; tranexamic acid inhibits this. **Mucosal surfaces**: the nose and pharynx have high fibrinolytic activity, which favors bleeding.

**T-general_ent-22.pathophysiology**

**Antiplatelets**: aspirin irreversibly inhibits COX-1; clopidogrel blocks P2Y12. **Anticoagulants**: warfarin (vitamin K antagonist), DOACs (factor Xa or thrombin inhibitors). **von Willebrand disease**: most common inherited bleeding disorder. **Bridging**: depends on thrombotic risk. **Reversal**: vitamin K, PCC, idarucizumab, and andexanet alfa.

### CC-general_ent-22.1 (concept check)

Stem: A 14-year-old girl with heavy menses had prolonged bleeding after a dental extraction and now needs tonsillectomy. Platelet count and PT are normal. Which inherited disorder should be tested first?

- **Correct:** von Willebrand disease
- Distractor: Hemophilia A — _why wrong:_ Hemophilia A is X-linked and rare in girls, and prolongs the aPTT.
- Distractor: Vitamin K deficiency — _why wrong:_ Vitamin K deficiency prolongs the PT.
- Distractor: Immune thrombocytopenia — _why wrong:_ The platelet count is normal.

Explanation: von Willebrand factor tethers platelets to exposed collagen. Deficiency causes mucocutaneous bleeding with a normal platelet count and PT. Desmopressin or factor replacement can be given perioperatively.

Pearl: Mucocutaneous bleeding history with normal counts = test for von Willebrand disease.

## T-general_ent-23 — Immunocompromised Host in Otolaryngology
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-23.overview**

Immunocompromised patients (transplant, chemotherapy, HIV, diabetes) face unusual and aggressive ENT infections and malignancies. Lower thresholds for imaging and biopsy are needed.

**T-general_ent-23.physiology**

**Innate immunity**: neutrophils and macrophages kill bacteria and fungi; neutropenia is the main risk for invasive fungal infection. **Cell-mediated immunity**: T cells control viruses (HSV, VZV, CMV), mycobacteria, and tumor surveillance. **Humoral immunity**: antibodies opsonize encapsulated bacteria. **Barriers**: intact mucosa and skin.

**T-general_ent-23.pathophysiology**

**Invasive fungal sinusitis**: neutropenia and DKA allow angioinvasive fungi. **Necrotizing otitis externa**: diabetic microangiopathy and neutrophil dysfunction. **Cutaneous SCC and lymphoma**: transplant immunosuppression impairs tumor surveillance. **Viral reactivation**: zoster and HSV cause severe mucositis and cranial neuropathies. **Atypical presentations**: blunted inflammatory signs delay diagnosis, so imaging and biopsy thresholds are lower.

### CC-general_ent-23.1 (concept check)

Stem: A liver transplant recipient on tacrolimus has 2 weeks of sinus pain and a black lesion on the middle turbinate. Why must this be treated differently than sinusitis in a healthy patient?

- **Correct:** Invasive fungal infection is much more likely
- Distractor: Transplant patients cannot receive antibiotics — _why wrong:_ Antibiotics are allowed but insufficient here.
- Distractor: Immunosuppression makes CT unreliable — _why wrong:_ CT remains useful.
- Distractor: Bacterial sinusitis is impossible in transplant patients — _why wrong:_ Bacterial sinusitis still occurs.

Explanation: Impaired neutrophil and T-cell immunity allows angioinvasive fungi. Black or pale insensate mucosa requires urgent biopsy, debridement, antifungals, and reducing immunosuppression.

Pearl: Immunocompromised + dark nasal mucosa = invasive fungal disease until proven otherwise.

## T-general_ent-24 — Laser / Energy Safety in Otolaryngology
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-24.overview**

Lasers and electrosurgical devices are common in airway and head and neck surgery, creating risks of airway fire, eye injury, and tissue damage. Safety protocols prevent catastrophic events.

**T-general_ent-24.physiology**

**Wavelength and chromophore**: CO2 laser (10,600 nm) is absorbed by water, KTP (532 nm) by hemoglobin, and Nd:YAG (1064 nm) penetrates deeply. **Thermal zones**: tissue is vaporized at the center, coagulated around it, and heated at the periphery. **Electrosurgery**: monopolar current passes through the patient to a return pad; bipolar current passes between tips. **Combustion**: requires fuel, oxidizer, and ignition.

**T-general_ent-24.pathophysiology**

**Fire triangle**: fuel (endotracheal tube, drapes), oxidizer (oxygen, nitrous oxide), and ignition. **Airway fire**: laser strikes an endotracheal tube in an oxygen-rich environment. **Prevention**: lowest oxygen concentration, laser-safe tubes, saline-filled cuffs. **Eye protection**: wavelength-specific goggles.

## T-general_ent-25 — Lemierre Syndrome
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-25.overview**

Lemierre syndrome is septic thrombophlebitis of the internal jugular vein after oropharyngeal infection, usually with Fusobacterium necrophorum. It causes septic pulmonary emboli and requires prolonged antibiotics.

**T-general_ent-25.physiology**

**Internal jugular vein**: drains the brain, face, and neck, running in the carotid sheath. **Parapharyngeal space**: lies just lateral to the tonsillar fossa and adjacent to the carotid sheath. **Venous drainage of the tonsils**: peritonsillar veins connect to the internal jugular system. **Pulmonary filter**: venous emboli lodge in the lungs.

**T-general_ent-25.pathophysiology**

**Spread**: pharyngitis or peritonsillar infection extends to the parapharyngeal space and causes septic thrombophlebitis of the internal jugular vein. **Fusobacterium necrophorum**: an anaerobe whose virulence factors promote platelet aggregation and thrombosis. **Septic emboli**: seed the lungs (cavitary nodules) and sometimes joints. **Presentation**: persistent fever and neck tenderness after a sore throat in a young adult. **Treatment**: prolonged antibiotics (often several weeks); anticoagulation is debated; drainage for abscesses.

### CC-general_ent-25.1 (concept check)

Stem: A 19-year-old has persistent fever and right neck tenderness 1 week after a sore throat. CT shows internal jugular vein thrombosis, and chest CT shows multiple cavitating nodules. Which organism is most likely?

- **Correct:** Fusobacterium necrophorum
- Distractor: Streptococcus pyogenes — _why wrong:_ Group A strep causes pharyngitis but is not the classic cause of septic jugular thrombophlebitis.
- Distractor: Staphylococcus aureus — _why wrong:_ S. aureus can cause septic emboli, but this syndrome is classically Fusobacterium.
- Distractor: Epstein-Barr virus — _why wrong:_ EBV causes mononucleosis, not septic thrombophlebitis with cavitating emboli.

Explanation: Pharyngeal infection spreads to the parapharyngeal space and causes septic thrombophlebitis of the internal jugular vein. Fusobacterium promotes platelet aggregation and thrombosis, seeding the lungs with septic emboli. Treatment is prolonged antibiotics.

Pearl: Sore throat, then neck tenderness and lung nodules = Lemierre syndrome.

## T-general_ent-26 — Ludwig Angina
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-26.overview**

Ludwig angina is rapidly spreading cellulitis of the bilateral submandibular, sublingual, and submental spaces, usually odontogenic. It threatens the airway by pushing the tongue up and back, and airway control comes first.

**T-general_ent-26.physiology**

**Mylohyoid muscle**: divides the sublingual space (above) from the submaxillary space (below). **Tooth roots**: second and third molar roots extend below the mylohyoid line, draining infection into the submaxillary space. **Floor of mouth**: confined by the mandible and hyoid, so swelling displaces the tongue. **Communication**: spaces communicate around the posterior mylohyoid.

**T-general_ent-26.pathophysiology**

**Odontogenic source**: infection from lower molars spreads into the submandibular spaces bilaterally. **Cellulitis more than abscess**: woody, indurated swelling without a discrete collection early. **Airway obstruction**: tongue elevation and posterior displacement and supraglottic edema. **Spread**: to parapharyngeal and retropharyngeal spaces and the mediastinum. **Management logic**: secure airway (awake fiberoptic intubation or awake tracheostomy), IV antibiotics, steroids in selected cases, and drainage plus tooth extraction.

### CC-general_ent-26.1 (concept check)

Stem: A 40-year-old with a lower second molar abscess has a board-like, tender submandibular and submental swelling, an elevated floor of mouth, and drooling. Why is the airway threatened?

- **Correct:** The tongue is pushed up and back
- Distractor: The vocal folds become paralyzed — _why wrong:_ Ludwig angina does not paralyze the vocal folds.
- Distractor: The trachea is compressed in the chest — _why wrong:_ The obstruction is in the oral cavity and pharynx.
- Distractor: Pus drains into the larynx — _why wrong:_ The danger is mechanical displacement and edema, not drainage.

Explanation: Second and third molar roots extend below the mylohyoid, so infection spreads into the bilateral submandibular spaces. The swelling, confined by the mandible, elevates and displaces the tongue posteriorly. Secure the airway (often awake) before anything else.

Pearl: Ludwig angina: airway first.

## T-general_ent-27 — Oral Manifestations of Systemic Disease
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-27.overview**

The oral cavity reflects systemic disease: vitamin deficiencies, autoimmune disease, infections, hematologic disorders, and medications. Recognizing patterns prompts systemic workup.

**T-general_ent-27.physiology**

**Oral mucosa turnover**: oral epithelium renews every 1-2 weeks, so nutritional deficiencies and drugs show early. **Saliva**: lubricates, buffers, and contains antimicrobial proteins. **Immune surveillance**: oral mucosa is constantly exposed to microbes. **Vascular supply**: rich mucosal vessels reflect systemic hematologic changes.

**T-general_ent-27.pathophysiology**

**Nutritional deficiencies**: B12, folate, and iron deficiency cause atrophic glossitis and angular cheilitis. **Autoimmune blistering disease**: pemphigus vulgaris (intraepithelial, desmoglein antibodies) and mucous membrane pemphigoid (subepithelial) cause erosions. **Lichen planus**: T-cell-mediated with reticular white striae. **Infections**: candidiasis with immunosuppression or xerostomia; herpes simplex. **Hematologic disease**: leukemia causes gingival infiltration and bleeding. **Medications**: phenytoin, cyclosporine, and calcium channel blockers cause gingival hyperplasia; bisphosphonates cause osteonecrosis.

### CC-general_ent-27.1 (concept check)

Stem: A 55-year-old has painful oral erosions that peel with minimal pressure (positive Nikolsky sign). Biopsy shows intraepithelial blisters with acantholysis. What is the diagnosis?

- **Correct:** Pemphigus vulgaris
- Distractor: Mucous membrane pemphigoid — _why wrong:_ Pemphigoid shows subepithelial blisters without acantholysis.
- Distractor: Oral lichen planus — _why wrong:_ Lichen planus shows lace-like white striae and band-like lymphocytes.
- Distractor: Recurrent aphthous ulcers — _why wrong:_ Aphthae are discrete ulcers without blistering or acantholysis.

Explanation: Antibodies against desmoglein 3 disrupt cell adhesion within the epithelium, causing acantholysis and fragile intraepithelial blisters. Oral lesions often precede skin lesions; systemic immunosuppression is required.

Pearl: Intraepithelial blisters with acantholysis = pemphigus.

## T-general_ent-28 — Pain Management in the Head & Neck Patient
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-28.overview**

Pain management in head and neck patients combines multimodal analgesia, neuropathic agents, and opioid stewardship. Post-tonsillectomy, cancer, and post-radiation pain each need tailored approaches.

**T-general_ent-28.physiology**

**Nociception**: tissue injury activates peripheral nociceptors that signal through trigeminal, glossopharyngeal, vagal, and cervical nerves. **Central processing**: the trigeminal nucleus caudalis and dorsal horn modulate pain. **Neuropathic pain**: arises from nerve injury or tumor invasion with abnormal firing. **Drug metabolism**: codeine and tramadol are activated by CYP2D6.

**T-general_ent-28.pathophysiology**

**Multimodal analgesia**: acetaminophen, NSAIDs, and local anesthetics reduce opioid needs. **Codeine and tramadol in children**: ultrarapid CYP2D6 metabolizers risk fatal respiratory depression; contraindicated after pediatric tonsillectomy. **Neuropathic pain**: gabapentinoids. **Opioid stewardship**: limit prescriptions.

### CC-general_ent-28.1 (concept check)

Stem: A 5-year-old with obstructive sleep apnea is being discharged after adenotonsillectomy. A family member asks why the surgeon will not prescribe the acetaminophen-codeine syrup that worked for an older sibling. What is the reason?

- **Correct:** Unpredictable morphine conversion
- Distractor: Codeine is too weak to control tonsil pain — _why wrong:_ Potency is not the reason; the risk is unpredictable morphine exposure.
- Distractor: Codeine increases post-tonsillectomy bleeding — _why wrong:_ Codeine does not increase hemorrhage risk; the danger is respiratory depression.
- Distractor: Codeine is poorly absorbed after surgery — _why wrong:_ Absorption is not the problem; metabolism is.

Explanation: CYP2D6 converts codeine to morphine. Ultrarapid metabolizers produce high morphine levels, and children with OSA are especially sensitive to respiratory depression, which led to deaths and an FDA contraindication. Scheduled acetaminophen and ibuprofen are standard.

Pearl: No codeine or tramadol after pediatric tonsillectomy.

## T-general_ent-29 — Penetrating and Blunt Neck Trauma
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-29.overview**

Penetrating and blunt neck trauma threatens the airway, vessels, aerodigestive tract, and nerves. Hard signs mandate surgery; modern practice favors a no-zone approach with CT angiography.

**T-general_ent-29.physiology**

**Neck zones**: zone I (clavicles to cricoid), zone II (cricoid to angle of mandible), zone III (angle to skull base). **Platysma**: penetration beyond it defines significant penetrating injury. **Compartments at risk**: vascular (carotid, jugular, vertebral), aerodigestive (larynx, trachea, pharynx, esophagus), and neural (vagus, phrenic, brachial plexus, spinal cord).

**T-general_ent-29.pathophysiology**

**Hard signs**: expanding or pulsatile hematoma, active bleeding, bruit, air bubbling, airway compromise, and neurologic deficit require operative exploration. **Soft signs**: dysphagia, hoarseness, subcutaneous emphysema, and stable hematoma prompt imaging. **No-zone approach**: stable patients are evaluated by CT angiography regardless of zone. **Blunt cerebrovascular injury**: carotid or vertebral dissection can cause delayed stroke. **Esophageal injury**: easily missed and causes mediastinitis.

### CC-general_ent-29.1 (concept check)

Stem: A stab wound to the left neck violates the platysma. The patient is stable, with no expanding hematoma, bleeding, stridor, or neurologic deficit. What is the modern initial evaluation?

- **Correct:** CT angiography of the neck
- Distractor: Mandatory neck exploration — _why wrong:_ Mandatory exploration is reserved for hard signs or instability.
- Distractor: Discharge with outpatient follow-up — _why wrong:_ Platysma violation requires evaluation for occult injuries.
- Distractor: Plain neck radiograph only — _why wrong:_ Plain films are inadequate for vascular and aerodigestive injury.

Explanation: The no-zone approach evaluates stable patients with CT angiography regardless of zone, reserving surgery for hard signs (expanding hematoma, pulsatile bleeding, air bubbling, airway compromise). Esophageal injury may need additional study.

Pearl: Stable penetrating neck trauma: CTA, not reflex exploration.

## T-general_ent-30 — Peritonsillar Abscess
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-30.overview**

Peritonsillar abscess is pus between the tonsillar capsule and the superior constrictor, the most common deep neck infection in young adults. It causes trismus, muffled voice, and uvular deviation, and is treated with drainage and antibiotics.

**T-general_ent-30.physiology**

**Peritonsillar space**: potential space between the tonsil capsule and the superior constrictor muscle. **Weber glands**: minor salivary glands in the supratonsillar space that drain to the tonsil surface. **Neighbors**: the pterygoid muscles (trismus) and parapharyngeal space lie laterally; the internal carotid is posterolateral. **Superior pole**: most abscesses form at the superior pole.

**T-general_ent-30.pathophysiology**

**Spread from tonsillitis**: infection extends through the tonsillar capsule into the peritonsillar space. **Weber gland theory**: obstruction and infection of Weber glands may explain abscess formation even without preceding tonsillitis. **Trismus**: inflammation irritates the medial pterygoid. **Hot potato voice**: palatal swelling alters resonance. **Uvular deviation**: displacement away from the abscess. **Microbiology**: Group A strep, Fusobacterium, and anaerobes. **Treatment logic**: needle aspiration or incision and drainage; quinsy tonsillectomy for recurrence or failure.

### CC-general_ent-30.1 (concept check)

Stem: A 22-year-old has severe unilateral sore throat, trismus, muffled voice, and a uvula deviated away from a bulging left soft palate. Why does she have trismus?

- **Correct:** Inflammation irritates the medial pterygoid
- Distractor: Infection spreads to the TMJ capsule — _why wrong:_ The TMJ is not involved in peritonsillar abscess.
- Distractor: The tongue is pushed against the palate — _why wrong:_ Tongue displacement occurs in Ludwig angina, not PTA trismus.
- Distractor: Pain reflexively closes the airway — _why wrong:_ Trismus is not an airway reflex.

Explanation: The peritonsillar space lies medial to the superior constrictor, which sits next to the medial pterygoid. Inflammation spreading laterally irritates the pterygoid, causing trismus. Drainage and antibiotics treat it.

Pearl: Trismus + uvular deviation = peritonsillar abscess until proven otherwise.

## T-general_ent-31 — Post-Tonsillectomy Hemorrhage
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-31.overview**

Post-tonsillectomy hemorrhage is primary (within 24 hours) or secondary (after 24 hours, typically days 5-10 when the eschar separates). It is the most common serious complication of tonsillectomy and can be fatal through airway compromise and hypovolemia, especially in small children.

**T-general_ent-31.physiology**

**Tonsillar blood supply**: mainly the tonsillar branch of the facial artery, plus the ascending pharyngeal, dorsal lingual, ascending palatine, and lesser palatine arteries; the paratonsillar (external palatine) vein drains it. **Tonsillar fossa**: the tonsil lies on the superior constrictor; the internal carotid lies about 2.5 cm posterolateral. **Wound healing by secondary intention**: a fibrinous exudate (white eschar) covers the fossa, then granulation tissue forms underneath. **Pediatric blood volume**: about 70-80 mL/kg, so a small child loses a large proportion of volume with modest bleeding. **Coagulation**: platelet plug and fibrin clot seal small vessels.

**T-general_ent-31.pathophysiology**

**Primary hemorrhage**: incomplete hemostasis or a slipped tie, often from a larger vessel at the lower pole. **Secondary hemorrhage**: separation of the eschar around days 5-10 exposes vessels in granulating tissue; dehydration, infection, and reduced oral intake contribute. **Swallowed blood**: children swallow blood and present with hematemesis or tachycardia before obvious bleeding, so hypotension is late. **Airway risk**: blood and clot can be aspirated, and induction of anesthesia in a bleeding child requires rapid sequence technique. **Coagulopathy**: undiagnosed von Willebrand disease or NSAID effects may contribute; ibuprofen is not associated with significant increased risk in modern evidence. **Management logic**: assess volume status, examine, remove clot, and control bleeding under anesthesia when bleeding is active or recurrent.

### CC-general_ent-31.1 (concept check)

Stem: A 5-year-old, 7 days after tonsillectomy, has spit up blood twice at home. In the ED she is pale with a heart rate of 150 and normal blood pressure, and a clot sits in the right fossa. Why is her normal blood pressure falsely reassuring?

- **Correct:** Children compensate until late hypovolemia
- Distractor: Tonsillar bleeding is always venous — _why wrong:_ Secondary bleeding can be arterial and brisk.
- Distractor: Swallowed blood does not count toward losses — _why wrong:_ Swallowed blood is real blood loss and hides the true volume lost.
- Distractor: Her clot proves the bleeding has stopped — _why wrong:_ A clot in the fossa often precedes a larger rebleed.

Explanation: Children maintain blood pressure through tachycardia and vasoconstriction until they have lost a large share of their small blood volume, so hypotension is a late sign. Secondary bleeds occur around days 5-10 as the eschar separates; she needs IV access, labs, and likely control in the OR.

Pearl: In a bleeding child, tachycardia is the warning; hypotension is the crash.

## T-general_ent-32 — Postoperative Neck Hematoma
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-32.overview**

Postoperative neck hematoma after thyroid, parathyroid, or neck surgery can rapidly compromise the airway. Immediate bedside wound opening is lifesaving when the airway is threatened.

**T-general_ent-32.physiology**

**Closed neck compartment**: the strap muscles and deep cervical fascia confine the central neck. **Venous and lymphatic drainage**: the larynx and pharynx depend on low-pressure venous and lymphatic outflow. **Airway structures**: the larynx and trachea are central.

**T-general_ent-32.pathophysiology**

**Venous and lymphatic obstruction**: hematoma compresses veins and lymphatics, causing laryngeal and pharyngeal edema; this, rather than direct tracheal compression, is the main mechanism of airway compromise. **Timing**: most occur within 6 hours, nearly all within 24 hours. **Risk factors**: hypertension, coughing or vomiting at emergence, anticoagulation, and large goiters. **Management**: SCOOP (skin exposure, cut sutures, open skin, open muscles, pack) at the bedside, then OR evacuation.

### CC-general_ent-32.1 (concept check)

Stem: Two hours after total thyroidectomy, a patient develops a tense, expanding neck swelling, stridor, and difficulty swallowing. What is the main mechanism of airway compromise?

- **Correct:** Venous and lymphatic outflow obstruction
- Distractor: Direct crushing of the cartilaginous trachea — _why wrong:_ The trachea resists compression; laryngeal and pharyngeal edema is the main mechanism.
- Distractor: Bilateral recurrent nerve paralysis from blood — _why wrong:_ Hematoma does not paralyze the vocal folds.
- Distractor: Aspiration of blood from the wound — _why wrong:_ The wound does not communicate with the airway.

Explanation: Blood in the closed central compartment compresses veins and lymphatics, causing rapidly progressive laryngeal and pharyngeal edema. Open the wound at the bedside (skin, sutures, strap muscles) to decompress, then return to the operating room.

Pearl: Post-thyroidectomy hematoma with stridor: open the neck now.

## T-general_ent-33 — Systemic / Granulomatous Disease Manifestations in ENT
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-33.overview**

Granulomatous and systemic diseases (GPA, sarcoidosis, EGPA, TB, syphilis, relapsing polychondritis, IgG4-related disease) often present in the head and neck. Biopsy and serology guide systemic therapy.

**T-general_ent-33.physiology**

**Granuloma formation**: macrophages aggregate and transform into epithelioid and giant cells in response to persistent antigens. **Small-vessel supply**: nasal mucosa, middle ear, and larynx have rich microvasculature.

**T-general_ent-33.pathophysiology**

**GPA**: ANCA (PR3) necrotizing vasculitis causes sinonasal crusting, saddle nose, otitis, subglottic stenosis. **Sarcoidosis**: noncaseating granulomas; parotid and facial nerve involvement (Heerfordt syndrome). **EGPA**: asthma, eosinophilia, and polyps. **TB**: caseating granulomas; scrofula. **IgG4-related disease**: fibroinflammatory enlargement of salivary glands.

### CC-general_ent-33.1 (concept check)

Stem: A 35-year-old has bilateral parotid enlargement, uveitis, fever, and facial nerve palsy. What is the diagnosis?

- **Correct:** Sarcoidosis (Heerfordt)
- Distractor: Sjögren syndrome — _why wrong:_ Sjögren causes gland enlargement and dryness but not facial palsy with uveitis.
- Distractor: Mumps parotitis — _why wrong:_ Mumps is acute viral parotitis without uveitis.
- Distractor: Parotid lymphoma — _why wrong:_ Lymphoma would not cause uveitis and fever in this pattern.

Explanation: Uveoparotid fever (Heerfordt syndrome) is a form of sarcoidosis with noncaseating granulomas involving parotid glands, uvea, and facial nerve.

Pearl: Parotid enlargement + uveitis + facial palsy = sarcoidosis.

## T-general_ent-34 — Tracheostomy Emergency
_source: pathophys_v470/general_ent_a.py_

**T-general_ent-34.overview**

Tracheostomy emergencies (decannulation, tube obstruction, bleeding) are a leading cause of preventable airway deaths. Response depends on whether the patient has a patent upper airway and how mature the tract is.

**T-general_ent-34.physiology**

**Tract maturation**: the stoma tract epithelializes over about 5-7 days, after which the tube can usually be replaced through it. **Upper airway status**: a laryngectomy patient has no connection between the mouth and trachea; a tracheostomy patient usually does. **Humidification**: the upper airway normally humidifies air; bypassing it dries secretions. **Cuff function**: an inflated cuff seals the trachea for ventilation and limits aspiration.

**T-general_ent-34.pathophysiology**

**Accidental decannulation in an immature tract**: tissue planes collapse, and blind reinsertion can create a false passage into the pretracheal space. **Obstruction**: dried mucus plugs the inner cannula, especially without humidification. **False passage**: inability to ventilate, subcutaneous emphysema, and loss of end-tidal CO2. **Tracheoinnominate fistula**: tube or cuff erosion into the innominate artery, typically 3 days to 6 weeks after placement, often preceded by a sentinel bleed; cuff overinflation and digital pressure temporize. **Management algorithm**: oxygenate via face and stoma, remove the inner cannula, pass a suction catheter, deflate the cuff, and remove the tube if needed; orally intubate if the upper airway is patent (not in laryngectomy).

### CC-general_ent-34.1 (concept check)

Stem: Four days after an open tracheostomy, a patient's tube dislodges during repositioning, and he is desaturating. The upper airway is patent. What is the safest first action?

- **Correct:** Oxygenate from above and orally intubate
- Distractor: Blindly reinsert the tracheostomy tube — _why wrong:_ An immature tract can collapse, so blind reinsertion risks a false passage into the pretracheal tissue.
- Distractor: Wait for the surgeon before any airway action — _why wrong:_ Hypoxia requires immediate airway management.
- Distractor: Give a sedative to reduce agitation — _why wrong:_ Sedation worsens respiratory drive without securing the airway.

Explanation: The tract is immature before about 5-7 days, so tissue planes collapse when the tube comes out. With a patent upper airway, oxygenate by face mask and stoma and intubate orally. Stay sutures help recover the tract if reinsertion is attempted.

Pearl: Immature tract dislodgement with patent upper airway: intubate from above.

## T-general_ent-35 — Wound Healing / Scar Biology in Head & Neck Surgery
_source: pathophys_v470/general_ent_b.py_

**T-general_ent-35.overview**

Wound healing in the head and neck is generally favorable due to rich blood supply, but radiation, malnutrition, diabetes, smoking, and hypothyroidism impair it. Understanding healing phases guides closure and scar management.

**T-general_ent-35.physiology**

**Hemostasis**: platelets form a plug and release growth factors. **Inflammation**: neutrophils then macrophages clear debris and orchestrate repair. **Proliferation**: fibroblasts lay down collagen III, angiogenesis, and epithelialization. **Remodeling**: collagen I replaces III over months; scars reach about 80 percent strength. **Oxygen dependence**: collagen synthesis requires oxygen.

**T-general_ent-35.pathophysiology**

**Radiation**: endarteritis and fibrosis impair healing. **Smoking**: vasoconstriction and carbon monoxide reduce oxygen delivery. **Malnutrition**: protein and vitamin C deficiency impair collagen. **Diabetes**: impaired immunity and microvascular disease. **Hypothyroidism**: increases fistula risk. **Steroids**: impair inflammation; vitamin A partly reverses.

### CC-general_ent-35.1 (concept check)

Stem: A patient who smokes a pack a day and had neck radiation 2 years ago develops wound breakdown and a fistula after salvage neck surgery. What single mechanism do both risk factors share?

- **Correct:** Reduced oxygen delivery to the wound
- Distractor: Excess collagen synthesis causing tension — _why wrong:_ Both factors impair, rather than increase, collagen synthesis.
- Distractor: An exaggerated inflammatory phase — _why wrong:_ Both blunt effective healing; neither speeds closure through inflammation.
- Distractor: Hypersensitivity to suture material — _why wrong:_ Suture allergy is rare and unrelated to smoking or radiation.

Explanation: Smoking causes vasoconstriction and carbon monoxide binding to hemoglobin; radiation causes obliterative endarteritis and fibrosis. Fibroblast collagen synthesis, angiogenesis, and neutrophil killing all depend on oxygen, so both impair healing; vascularized flaps help in irradiated beds.

Pearl: Wound healing needs oxygen: smoking and radiation both starve it.


---

# Concept checks on legacy topic names

### CC-facial_plastics-legacy.1 — NOE Fracture Mechanics

Stem: In an NOE fracture, why is the status of the bone fragment carrying the medial canthal tendon the key to classification and repair?

- **Correct:** The tendon position sets the intercanthal distance
- Distractor: The fragment contains the lacrimal gland — _why wrong:_ The lacrimal gland lies superolaterally in the orbit, not on the central fragment.
- Distractor: The fragment carries the optic nerve — _why wrong:_ The optic nerve passes through the optic canal, posterior in the orbit.
- Distractor: The fragment determines nasal tip projection — _why wrong:_ Tip projection depends on cartilage support, not the central fragment.

Explanation: The medial canthal tendon inserts on the central fragment. Markowitz types I and II keep the tendon on a fragment that can be plated; type III (tendon avulsed or fragment comminuted) needs transnasal canthopexy to correct telecanthus.

Pearl: NOE repair is about putting the medial canthus back where it belongs.

### CC-facial_plastics-legacy.2 — Frontal Sinus Fracture Decision Model

Stem: A patient has a minimally displaced posterior table frontal sinus fracture without CSF leak, and the outflow tract is patent on CT. What is the most reasonable initial management?

- **Correct:** Observation with imaging follow-up
- Distractor: Cranialization of the frontal sinus — _why wrong:_ Cranialization is reserved for severely comminuted posterior table fractures or persistent CSF leak.
- Distractor: Obliteration of the frontal sinus — _why wrong:_ Obliteration is used when outflow is irreparably blocked.
- Distractor: Immediate open reduction of the anterior table — _why wrong:_ The anterior table is not described as displaced.

Explanation: Management balances anterior table contour, posterior table displacement with CSF leak, and outflow patency. Minimally displaced fractures with a patent outflow tract and no leak can be observed with endoscopic and imaging follow-up.

Pearl: Patent outflow and no leak: observe.

### CC-facial_plastics-legacy.3 — Dynamic Facial Reanimation

Stem: A 30-year-old has had complete facial paralysis for 5 years after removal of a cerebellopontine angle tumor. EMG shows no fibrillation potentials or motor units in the facial muscles. Which option can restore a dynamic smile?

- **Correct:** Free functional gracilis transfer
- Distractor: Masseteric nerve transfer to the facial nerve — _why wrong:_ After about 2 years, native facial muscles are atrophied and cannot be reinnervated.
- Distractor: Primary facial nerve repair — _why wrong:_ Primary repair is for recent transection with available nerve ends.
- Distractor: Gold weight implant alone — _why wrong:_ A gold weight protects the eye but does not restore smile.

Explanation: Electrical silence means the native muscles have fibrosed. A free gracilis muscle brings new muscle, usually innervated by the masseteric nerve or a cross-facial graft, to restore dynamic smile.

Pearl: Long-standing paralysis with silent EMG: bring new muscle.

### CC-facial_plastics-legacy.4 — Static Facial Reanimation

Stem: A 75-year-old with permanent facial paralysis and poor overall health has an exposed cornea and a drooping oral commissure. Which approach best meets his goals with the least morbidity?

- **Correct:** Gold weight with static sling
- Distractor: Free gracilis transfer — _why wrong:_ Free muscle transfer requires a long operation and recovery.
- Distractor: Cross-facial nerve graft — _why wrong:_ This requires long nerve growth and two stages.
- Distractor: Masseteric nerve transfer — _why wrong:_ This requires viable muscle and is less suited to long-standing paralysis.

Explanation: Static procedures (gold or platinum weight, slings, brow lift) protect the eye and improve symmetry quickly and with less morbidity, appropriate when dynamic options are unsuitable.

Pearl: Eye protection first; static procedures fit frail patients.

### CC-sleep-legacy.5 — Palatal Surgery Selection for OSA

Stem: A 45-year-old with OSA, a BMI of 34, Friedman tongue position IV, and 1+ tonsils asks for palatal surgery to avoid CPAP. Why is isolated palatal surgery unlikely to succeed?

- **Correct:** Collapse is likely retrolingual
- Distractor: Small tonsils make palatal surgery unsafe — _why wrong:_ Tonsil size affects benefit, not safety.
- Distractor: Palatal surgery cannot be done above BMI 30 — _why wrong:_ There is no strict BMI cutoff, but higher BMI lowers success.
- Distractor: Friedman position IV means central apnea — _why wrong:_ Friedman position describes tongue and palate anatomy, not central events.

Explanation: Friedman stage III (high tongue position, small tonsils, higher BMI) predicts poor success with palatal surgery alone because collapse is largely retrolingual and multilevel. DISE and alternative therapies (oral appliance, HNS, MMA) are considered.

Pearl: Small tonsils + high tongue + obesity = palatal surgery alone will likely fail.
