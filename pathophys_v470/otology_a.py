"""Otology / Neurotology (part A): mechanism-level teaching content."""

CONTENT = {
"Acute Otitis Externa": dict(
overview=(
"Acute otitis externa (AOE) is diffuse bacterial cellulitis of the external auditory canal skin, usually Pseudomonas aeruginosa or Staphylococcus aureus. "
"It matters because it is among the most common ear complaints, it is treated topically, and its look-alike in a diabetic or immunocompromised patient (necrotizing otitis externa) is a skull-base osteomyelitis."),
physiology=(
"**Canal structure**: the canal is about 2.5 cm long; the lateral one-third is cartilaginous and the medial two-thirds is bony. "
"**Lateral canal skin**: it is thick and carries hair follicles plus ceruminous and sebaceous glands. "
"**Medial canal skin**: over bone it is thin, tightly bound to periosteum, and has no adnexa, which is why swelling there is so painful. "
"**Cerumen is a barrier**: it is hydrophobic, mildly acidic (pH about 6), and contains lysozyme and long-chain fatty acids that inhibit bacterial growth. "
"**Self-cleaning**: canal epithelium migrates outward from the tympanic membrane, carrying keratin and cerumen laterally. "
"**Innervation**: sensory supply comes from V3 (auriculotemporal), CN X (Arnold nerve), CN VII and the great auricular nerve, which explains referred otalgia and the cough reflex with canal instrumentation."),
pathophysiology=(
"**Barrier breakdown starts it**: water exposure (\"swimmer's ear\"), cotton swabs, hearing-aid occlusion, or dermatitis remove cerumen and raise canal pH. "
"**Maceration**: moist, alkaline skin loses its acid mantle and stratum corneum integrity, letting Pseudomonas or Staphylococcus invade. "
"**Edema and pain**: inflammation of skin bound tightly to periosteum produces pain out of proportion to the visible findings, and tragal or pinna traction stretches the inflamed skin. "
"**Canal occlusion**: edema narrows the lumen, causing conductive hearing loss and blocking drops from reaching the medial canal (the reason for a wick). "
"**Spread**: cellulitis can extend to the pinna and periauricular tissues; in a diabetic or immunocompromised host, extension through the fissures of Santorini toward the skull base marks necrotizing otitis externa. "
"**Why topical therapy wins**: drops deliver local tissue concentrations about 1000 times higher than systemic therapy directly to the infected skin, so oral antibiotics add little unless infection extends beyond the canal."),
),

"Chronic Otitis Media / Cholesteatoma": dict(
overview=(
"Chronic otitis media is persistent middle-ear inflammation with or without a tympanic membrane perforation; cholesteatoma is keratinizing squamous epithelium trapped in the middle ear and mastoid. "
"Cholesteatoma matters because it is locally destructive (ossicles, labyrinth, facial nerve, tegmen) and is treated surgically."),
physiology=(
"**Middle-ear mucosa**: the middle ear and mastoid are lined by respiratory-type mucosa that clears secretions toward the Eustachian tube and exchanges gas with the blood. "
"**Pressure regulation**: the mucosa continuously absorbs nitrogen and oxygen, so middle-ear pressure would fall unless the Eustachian tube periodically opens (swallowing, yawning) to re-equalize it. "
"**Tympanic membrane layers**: lateral squamous epithelium, a middle fibrous layer, and medial mucosa; the pars flaccida lacks the organized fibrous layer, making it the weakest point. "
"**Epithelial migration**: TM squamous epithelium normally migrates centrifugally outward into the canal, so keratin never accumulates on the drum. "
"**Spaces at risk**: Prussak space (between pars flaccida and malleus neck) drains toward the epitympanum and aditus ad antrum; the sinus tympani and facial recess lie posterior and are hard to see surgically."),
pathophysiology=(
"**Retraction theory (primary acquired)**: chronic Eustachian tube dysfunction creates negative pressure that sucks the weak pars flaccida or posterior pars tensa inward into a retraction pocket. "
"**Trapping**: once the pocket deepens, migrating keratin can no longer clear and accumulates as a sac of desquamated keratin (the cholesteatoma matrix plus perimatrix). "
"**Secondary acquired**: squamous epithelium migrates through a marginal perforation or is implanted by trauma or surgery. "
"**Congenital**: an epithelial rest behind an intact drum, classically anterosuperior in a child with no history of otitis. "
"**Bone erosion**: the perimatrix releases inflammatory cytokines and osteoclast-activating factors (with pressure and infection), resorbing ossicles (incus long process first), the lateral semicircular canal (fistula), the fallopian canal, and the tegmen. "
"**Infection**: keratin debris is an ideal culture medium for Pseudomonas and anaerobes, so the classic symptom is painless, foul, recurrent otorrhea resistant to drops. "
"**Why surgery**: the matrix keeps producing keratin and does not involute, so medical therapy only quiets infection; removal (canal wall up or down) is the cure."),
),

"Sudden Sensorineural Hearing Loss": dict(
overview=(
"Sudden sensorineural hearing loss (SSNHL) is at least a 30 dB loss in three consecutive frequencies developing within 72 hours. "
"It is an otologic urgency: most cases are idiopathic, treatment works best early, and a small but important fraction hide a vestibular schwannoma or other retrocochlear cause."),
physiology=(
"**Cochlear transduction**: outer hair cells amplify basilar-membrane motion (the cochlear amplifier) and inner hair cells convert vibration into spiral ganglion firing. "
"**Endocochlear potential**: the stria vascularis pumps potassium into endolymph, generating a +80 mV potential that drives hair-cell transduction current; this is metabolically demanding. "
"**Blood supply**: the labyrinthine artery (usually from AICA) is an end artery with no collateral supply, so the cochlea is very sensitive to ischemia. "
"**Tonotopy**: the base encodes high frequencies and the apex low frequencies, which explains audiometric patterns such as low-frequency or flat losses."),
pathophysiology=(
"**Mostly idiopathic (about 90 percent per the AAO-HNS guideline)**: leading hypotheses are viral cochleitis, microvascular compromise, and immune-mediated injury; none is proven for an individual patient. "
"**Vascular theory**: the cochlea's end-artery supply and high metabolic demand mean brief ischemia can damage the stria and hair cells abruptly. "
"**Viral/inflammatory theory**: inflammation and cytokine release disrupt hair cells and strial function; this is the rationale for corticosteroids, which reduce cochlear inflammation and stabilize the stria. "
"**Membrane rupture**: rarely, a break between perilymph and endolymph (or a window leak) mixes potassium-rich fluid and depolarizes hair cells. "
"**Retrocochlear causes**: vestibular schwannoma can present as sudden loss through acute compression or vascular compromise of the cochlear nerve or artery, which is why MRI is part of the workup. "
"**Why timing matters**: steroid benefit is greatest in the first two weeks, and intratympanic steroid achieves far higher perilymph concentrations than oral dosing, making it the salvage route (within about 6 weeks of onset per the 2019 AAO-HNSF guideline); hyperbaric oxygen is a guideline option alongside steroids early or as salvage."),
),

"Otosclerosis / Stapes Fixation": dict(
overview=(
"Otosclerosis is abnormal remodeling of the otic capsule that most often fixes the stapes footplate, causing progressive conductive hearing loss in young adults. "
"It is a classic boards and OR topic because it is diagnosed by audiometry and reflexes and corrected by stapedotomy or amplification."),
physiology=(
"**Otic capsule**: the bony labyrinth is normally among the densest bone in the body and essentially does not remodel after childhood. "
"**Stapes footplate**: it sits in the oval window held by the annular ligament, which allows piston-like motion into the vestibule. "
"**Middle-ear impedance matching**: the area ratio of the tympanic membrane to the footplate (about 17:1) and the ossicular lever (about 1.3:1) recover roughly 25-30 dB that would otherwise be lost moving sound from air to inner-ear fluid. "
"**Acoustic reflex**: loud sound contracts the stapedius (CN VII), stiffening the chain; the reflex is measured as a change in compliance."),
pathophysiology=(
"**Abnormal remodeling**: foci of osteoclastic resorption (active, vascular \"otospongiosis\") are replaced by dense sclerotic bone (inactive otosclerosis). "
"**Site of predilection**: the fissula ante fenestram, just anterior to the oval window, is the classic first site, so the anterior footplate is fixed first. "
"**Conductive loss**: a fixed footplate cannot transmit sound energy into the vestibule, producing a progressive low-frequency-predominant air-bone gap. "
"**Carhart notch**: bone conduction dips at 2000 Hz because fixation removes the ossicular-chain resonance contribution to bone conduction; it is a mechanical artifact, not true cochlear loss, and improves after surgery. "
"**Reflexes absent**: the stapedius cannot move a fixed stapes, so acoustic reflexes are absent; early on an on-off pattern may appear. "
"**Cochlear otosclerosis**: foci involving the cochlear endosteum can release toxic enzymes that cause sensorineural loss. "
"**Risk factors**: autosomal dominant inheritance with incomplete penetrance, female predominance, worsening with pregnancy (hormonal influence), and measles virus association. "
"**Schwartze sign**: a reddish promontory blush reflects hypervascular active otospongiosis."),
),

"Vestibular Schwannoma": dict(
overview=(
"Vestibular schwannoma is a benign Schwann-cell tumor of the vestibular nerve in the internal auditory canal and cerebellopontine angle. "
"It is the classic cause of asymmetric sensorineural hearing loss and the prototype lateral skull-base tumor for observation, radiation, or microsurgery decisions."),
physiology=(
"**IAC anatomy**: the canal carries CN VII (anterosuperior), the cochlear nerve (anteroinferior), and the superior and inferior vestibular nerves (posterior), separated by the transverse crest and Bill's bar (\"7-up, Coke down\"). "
"**Obersteiner-Redlich zone**: the transition between central (oligodendrocyte) and peripheral (Schwann cell) myelin lies in the IAC, near where most schwannomas arise. "
"**Vascular supply**: the cochlea depends on the labyrinthine artery running with the nerves in the IAC. "
"**Central compensation**: the brainstem and cerebellum recalibrate continuously when one vestibular input slowly declines."),
pathophysiology=(
"**Genetics**: loss of the NF2 tumor-suppressor gene product (merlin) in Schwann cells removes contact inhibition; sporadic tumors are unilateral, while NF2 causes bilateral tumors. "
"**Hearing loss mechanism**: compression of the cochlear nerve, compromise of the labyrinthine artery, and biochemical changes in inner-ear fluid explain why hearing loss does not track tumor size. "
"**Why vertigo is uncommon**: slow vestibular loss is centrally compensated, so imbalance is more typical than vertigo. "
"**Growth pattern**: tumors expand within the IAC then into the CPA, where large tumors compress the brainstem, CN V (facial numbness, lost corneal reflex) and the fourth ventricle (hydrocephalus). "
"**Facial nerve tolerance**: CN VII is stretched and thinned around the tumor but motor function is usually preserved preoperatively; facial weakness at presentation suggests another diagnosis such as facial nerve schwannoma or malignancy. "
"**Retrocochlear signs**: ABR shows prolonged wave I-V interpeak latency, and word recognition is often worse than the pure-tone loss predicts."),
),

"Temporal Bone Anatomy": dict(
overview=(
"Temporal bone anatomy is the map behind every otologic diagnosis and operation, from reading a CT to drilling a mastoid safely. "
"Mastering it means knowing the landmarks that protect the facial nerve, labyrinth, sigmoid sinus, jugular bulb, carotid, and dura."),
physiology=(
"**Four parts**: squamous, mastoid, petrous, and tympanic (the styloid process is sometimes counted as a fifth). "
"**Facial nerve course**: labyrinthine segment (narrowest, no collaterals), geniculate ganglion (GSPN exits), tympanic segment above the oval window, second genu at the lateral canal, and mastoid segment to the stylomastoid foramen. "
"**Labyrinth**: cochlea (two and a half turns), vestibule (utricle and saccule), and three semicircular canals; the lateral canal is the key mastoid landmark. "
"**Middle-ear walls**: tegmen superiorly, jugular bulb inferiorly, carotid anteriorly, promontory and windows medially, aditus and pyramidal eminence posteriorly. "
"**Mastoid landmarks**: Macewen triangle overlies the antrum; the sinodural angle, digastric ridge (leads to stylomastoid foramen), and Trautmann triangle guide dissection. "
"**Pneumatization**: air cells develop from the antrum after birth, driven by middle-ear ventilation; poor ventilation leaves a sclerotic mastoid."),
pathophysiology=(
"**Why the labyrinthine segment matters**: it is the narrowest part of the fallopian canal, so inflammatory edema (Bell palsy) or fracture compression there causes ischemic nerve injury. "
"**Dehiscence**: the tympanic segment is partially dehiscent in about half of ears (55 percent in Cummings), which is why it is vulnerable during middle-ear surgery and cholesteatoma removal. "
"**Spread of disease follows anatomy**: infection travels through air-cell tracts to the petrous apex (Gradenigo), through the tegmen to the dura and temporal lobe, and to the dura around the sigmoid sinus (perisinus abscess), causing thrombophlebitis. "
"**Fracture patterns**: otic-capsule-violating fractures cross the labyrinth and cause SNHL and vertigo, while sparing fractures more often disrupt the ossicles and cause conductive loss. "
"**Third windows**: missing bone over the superior canal or other labyrinth segments creates abnormal fluid mechanics (superior canal dehiscence physiology)."),
),

"Audiogram Interpretation": dict(
overview=(
"The pure-tone audiogram, with speech testing, is the foundational test in otology: it classifies hearing loss as conductive, sensorineural, or mixed, and grades severity. "
"Every downstream decision (imaging, surgery, amplification, implantation) starts from reading it correctly, including masking."),
physiology=(
"**Air conduction**: sound through headphones tests the whole pathway: outer ear, middle ear, cochlea, and nerve. "
"**Bone conduction**: a vibrator on the mastoid stimulates the cochlea directly, largely bypassing the outer and middle ear. "
"**Air-bone gap**: the difference between air and bone thresholds represents conductive loss; a gap of 10 dB or more (with normal bone conduction) indicates a conductive component, while smaller gaps fall within test variability. "
"**Decibels HL**: 0 dB HL is average normal hearing at each frequency; normal adult thresholds are 25 dB HL or better. "
"**Interaural attenuation**: about 40 dB for supra-aural headphones and essentially 0 dB for bone conduction, so the non-test ear can hear the stimulus (crossover) unless masked. "
"**Speech testing**: the speech reception threshold should agree with the pure-tone average, and word recognition measures clarity, which reflects cochlear and neural function."),
pathophysiology=(
"**Conductive pattern**: normal bone conduction with elevated air conduction means sound is blocked before the cochlea (wax, effusion, perforation, fixation, discontinuity). "
"**Sensorineural pattern**: air and bone are equally elevated, meaning the cochlea or nerve is the problem. "
"**Characteristic shapes**: noise injury produces a 4 kHz notch with recovery at 8 kHz; presbycusis is bilateral, symmetric, and high-frequency sloping; Ménière disease classically starts as a fluctuating low-frequency loss. "
"**Retrocochlear warning signs**: asymmetry, unilateral tinnitus, or word recognition disproportionately poor for the pure-tone loss suggest a nerve problem and call for MRI. "
"**Masking dilemma**: with large bilateral conductive losses, masking noise loud enough to cover the non-test ear may itself cross over to the test ear, making thresholds uncertain. "
"**Pseudohypacusis**: an SRT much better than the pure-tone average, acoustic reflexes present at or within 5 dB of the admitted thresholds, or normal OAEs despite a claimed loss suggest a nonorganic loss."),
),

"Tympanometry / Acoustic Reflexes": dict(
overview=(
"Tympanometry measures how the tympanic membrane and middle ear accept sound energy as canal pressure changes; acoustic reflexes test the stapedius reflex arc. "
"Together they identify effusion, perforation, fixation, discontinuity, and some retrocochlear or facial nerve problems in minutes."),
physiology=(
"**Admittance**: a probe tone (226 Hz in adults) is played while canal pressure is swept; admittance peaks when canal pressure equals middle-ear pressure. "
"**Key measures**: peak pressure (middle-ear pressure), peak height (static admittance or compliance), and ear-canal volume. "
"**Reflex arc**: CN VIII to the cochlear nucleus, to both superior olivary complexes, to both facial motor nuclei, and out CN VII to the stapedius in both ears. "
"**Ipsilateral and contralateral reflexes**: stimulating one ear normally triggers the reflex in both ears, so the pattern of present and absent reflexes localizes the lesion. "
"**Infant probe tone**: a 1000 Hz probe is used under about 6 months because the infant canal wall is compliant and distorts 226 Hz results."),
pathophysiology=(
"**Type A**: normal peak and pressure. **Type As**: shallow peak from a stiff system such as otosclerosis or a thick drum. **Type Ad**: a very tall peak from a flaccid drum or ossicular discontinuity. "
"**Type B with normal volume**: no peak because fluid fills the middle ear (effusion) and the drum cannot move. "
"**Type B with large volume**: the probe measures the canal plus middle ear through a perforation or patent tube. "
"**Type B with small volume**: the probe is against wax or the canal wall. "
"**Type C**: negative peak pressure from Eustachian tube dysfunction and gas absorption. "
"**Reflex logic**: a conductive loss in the probe ear abolishes reflexes recorded there; a retrocochlear lesion abolishes reflexes when the affected ear is stimulated; a facial nerve lesion proximal to the stapedius abolishes reflexes recorded on that side. "
"**Reflex decay**: inability to sustain the reflex for 10 seconds at 10 dB above threshold suggests retrocochlear disease."),
),

"Eustachian Tube Dysfunction": dict(
overview=(
"Eustachian tube dysfunction (ETD) is failure of the tube to open (dilatory ETD) or close (patulous ETD) normally. "
"Dilatory ETD underlies otitis media with effusion, retraction pockets, and much acquired cholesteatoma, so it is a root cause in otology."),
physiology=(
"**Structure**: the tube runs about 36 mm in adults from the anterior middle ear to the nasopharynx; the lateral third is bony and the medial two-thirds cartilaginous. "
"**Default state**: the cartilaginous portion is normally closed, protecting the middle ear from nasopharyngeal pressure, secretions, and sound of one's own voice. "
"**Active opening**: the tensor veli palatini (CN V3) pulls the lateral cartilaginous wall open during swallowing and yawning; the levator veli palatini assists. "
"**Functions**: ventilation (equalizing pressure), protection, and clearance of middle-ear secretions by mucociliary transport. "
"**Children**: their tube is shorter, more horizontal, and less rigid, and the tensor is less efficient, so ETD and otitis media are much more common."),
pathophysiology=(
"**Gas absorption**: the middle-ear mucosa constantly absorbs gas; if the tube fails to open, pressure becomes negative. "
"**Negative pressure consequences**: retraction of the tympanic membrane, transudation of fluid (effusion), and mucosal edema. "
"**Causes of dilatory failure**: mucosal inflammation (allergy, infection, reflux), adenoid hypertrophy or mass, cleft palate (abnormal tensor insertion), and barotrauma. "
"**Barotrauma**: on airplane descent, external pressure rises faster than a closed tube can equalize, locking the tube shut and producing pain, effusion, or hemotympanum. "
"**Chronic sequelae**: long-standing negative pressure thins and retracts the drum (atelectasis, retraction pockets), which can evolve into cholesteatoma. "
"**Unilateral adult effusion**: always examine the nasopharynx, because a mass such as nasopharyngeal carcinoma can obstruct the tube."),
),

"Tympanic Membrane Perforation": dict(
overview=(
"A tympanic membrane perforation is a hole in the drum from infection, trauma, or prior tube placement. "
"Most traumatic perforations heal on their own; persistent ones cause conductive loss and recurrent otorrhea and are repaired by tympanoplasty."),
physiology=(
"**Layers**: lateral squamous epithelium, middle fibrous lamina propria (radial and circular fibers), and medial mucosa. "
"**Pars tensa vs flaccida**: the tensa has an organized fibrous layer and is anchored by the fibrous annulus; the flaccida is above the lateral process of the malleus and lacks organized fibers. "
"**Healing**: epithelium migrates across the defect from the edges, using a scaffold; the fibrous layer often does not regenerate fully, leaving a thin dimeric scar (epidermal and mucosal layers; the term monomeric is a misnomer). "
"**Sound transmission**: the drum collects sound over a large area and couples it to the malleus; it also shields the round window so sound reaches the two windows out of phase."),
pathophysiology=(
"**Conductive loss**: loss of surface area reduces the hydraulic ratio, and in large perforations sound reaching the round window directly can diminish the phase difference between the windows. "
"**Size, not location**: larger perforations cause greater loss; location matters little, contrary to the older posteroinferior teaching; loss over 40 dB suggests an additional ossicular problem. "
"**Why some fail to heal**: infection, large size, marginal location involving the annulus, and squamous epithelium turning in over the edge (preventing migration across the gap). "
"**Marginal perforations**: they involve the annulus and can allow squamous epithelium to migrate into the middle ear, causing secondary acquired cholesteatoma. "
"**Otorrhea**: an open middle ear is exposed to water and canal bacteria, leading to recurrent drainage. "
"**Traumatic perforations**: slap or blast injuries usually heal within weeks if kept dry; vertigo or sensorineural loss signals possible stapes subluxation or perilymph fistula."),
),

"Ossicular Discontinuity": dict(
overview=(
"Ossicular discontinuity is a break in the malleus-incus-stapes chain, most often erosion of the incus long process or a traumatic incudostapedial separation. "
"It produces a maximal conductive loss with an intact drum and is repaired by ossiculoplasty."),
physiology=(
"**Lever system**: the malleus handle and incus long process form a lever (about 1.3:1) that drives the stapes. "
"**Joints**: the incudomalleolar and incudostapedial joints are synovial; the incudostapedial joint is the most delicate link. "
"**Blood supply**: the incus long process and lenticular process have a tenuous end-arterial mucosal blood supply. "
"**Suspension**: ligaments and the tensor tympani and stapedius tendons hold the chain in place."),
pathophysiology=(
"**Maximal conductive loss**: with an intact drum and a broken chain, the drum shields the cochlea and transmits nothing, producing a gap up to about 60 dB, larger than a simple perforation. "
"**Erosion**: chronic otitis media and cholesteatoma erode the incus long process first because of its poor blood supply and inflammatory osteitis. "
"**Trauma**: temporal bone fractures and head injuries separate the incudostapedial joint or dislocate the incus. "
"**Tympanometry clue**: a disconnected, flaccid system produces a very high-compliance (Ad) tympanogram, the opposite of the stiff system in otosclerosis. "
"**Reflexes**: stapedius contraction cannot change drum compliance when the chain is broken, so reflexes recorded in that ear are absent."),
),

"Superior Canal Dehiscence": dict(
overview=(
"Superior canal dehiscence (SCD) is absent bone over the superior semicircular canal, creating a third mobile window into the inner ear. "
"It explains sound- or pressure-induced vertigo, autophony, and a conductive-appearing loss with normal middle-ear function."),
physiology=(
"**Two-window system**: normally the inner ear has only two mobile windows, the oval window (input) and round window (pressure release), so stapes motion drives fluid along the cochlea. "
"**Superior canal position**: it arches toward the middle cranial fossa floor and is covered by a thin bony layer under the temporal lobe dura. "
"**Canal stimulation**: semicircular canals sense angular acceleration through endolymph flow deflecting the cupula. "
"**Bone conduction physiology**: cochlear bone-conduction sensitivity depends partly on the impedance difference between the two windows."),
pathophysiology=(
"**Third window**: a dehiscence lets sound energy and pressure shunt away from the cochlea into the superior canal. "
"**Sound- and pressure-induced vertigo**: shunted energy moves endolymph in the canal, deflecting its cupula (Tullio phenomenon with sound, Hennebert sign with pressure), with eye movements in the plane of the superior canal. "
"**Air-bone gap with normal middle ear**: air conduction worsens because energy leaks away from the cochlea, while bone conduction improves (can be better than 0 dB) because the third window lowers inner-ear impedance on that side. "
"**Reflexes present**: unlike otosclerosis, the stapes moves normally, so acoustic reflexes are present, which is a key discriminator. "
"**Autophony**: patients hear their own voice, eye movements, footsteps, or pulse loudly through the bone-conduction pathway. "
"**VEMP changes**: cervical VEMP thresholds are abnormally low and ocular VEMP amplitudes are high because the third window increases vestibular sensitivity to sound."),
),

"Ménière Disease": dict(
overview=(
"Ménière disease is episodic vertigo lasting 20 minutes to 12 hours with fluctuating low-frequency sensorineural hearing loss, tinnitus, and aural fullness in the same ear. "
"Its pathologic hallmark is endolymphatic hydrops, and management escalates from diet and diuretics to intratympanic therapy and ablation."),
physiology=(
"**Two fluids**: endolymph (high potassium, low sodium) fills the membranous labyrinth; perilymph (high sodium, like CSF) surrounds it. "
"**Production and resorption**: the stria vascularis and vestibular dark cells secrete endolymph; the endolymphatic duct and sac are thought to regulate volume and resorb fluid. "
"**Reissner membrane**: it separates potassium-rich endolymph in the scala media from sodium-rich perilymph in the scala vestibuli. "
"**Apical sensitivity**: the cochlear apex is the most compliant region, so pressure changes affect low frequencies first."),
pathophysiology=(
"**Endolymphatic hydrops**: excess endolymph distends the cochlear duct and saccule, seen consistently on histopathology and gadolinium MRI. "
"**Why the low frequencies go first**: the compliant apex is distorted earliest by hydrops, producing low-frequency loss and fullness. "
"**Attack mechanism (rupture/leak theory)**: membranes may rupture or leak, mixing potassium-rich endolymph into perilymph, depolarizing hair cells and vestibular nerve fibers (initial excitation, then paralysis), then healing. "
"**Fluctuation and progression**: each attack can recover, but repeated episodes cause permanent hair-cell loss and a flattening hearing loss over years, with eventual burnout of vestibular function. "
"**Contributing factors**: endolymphatic sac hypoplasia, autoimmune and allergic factors, migraine overlap, and genetic predisposition; hydrops is necessary but not sufficient, since not all hydrops produces symptoms. "
"**Therapeutic logic**: salt restriction and diuretics aim to reduce endolymph volume; intratympanic gentamicin chemically ablates vestibular hair cells (type I more than type II; reduced endolymph secretion by dark cells is debated), while steroids are anti-inflammatory and hearing-sparing."),
),

"Vestibular Migraine": dict(
overview=(
"Vestibular migraine is recurrent vestibular symptoms (5 minutes to 72 hours) in a person with migraine, with migraine features during at least half of episodes. "
"It is one of the most common causes of recurrent vertigo and is often mistaken for Ménière disease."),
physiology=(
"**Shared circuits**: the trigeminal nociceptive system and vestibular nuclei are interconnected, and both project to the thalamus and cortex. "
"**Multisensory integration**: balance depends on integrating vestibular, visual, and proprioceptive signals in the vestibular nuclei, cerebellum, and cortex. "
"**Inner-ear vasculature**: the labyrinth is innervated by trigeminal fibers that can release vasoactive neuropeptides."),
pathophysiology=(
"**Central hyperexcitability**: migraine brains show altered cortical and brainstem excitability; cortical spreading depression and brainstem activation can involve vestibular pathways. "
"**Neurogenic inflammation**: trigeminal release of CGRP and substance P may alter inner-ear blood flow and sensory function, explaining occasional auditory symptoms. "
"**Variable presentation**: symptoms include spontaneous or positional vertigo, motion intolerance, and visual vertigo, with or without simultaneous headache. "
"**Why hearing is usually stable**: unlike Ménière disease, progressive low-frequency hearing loss is not expected; significant progressive loss should prompt reconsideration. "
"**Treatment rationale**: trigger management, sleep and stress regularity, and migraine preventives (tricyclics, beta-blockers, calcium-channel blockers, topiramate, CGRP pathway agents) reduce central excitability."),
),

"Vestibular Neuritis": dict(
overview=(
"Vestibular neuritis is acute, continuous vertigo lasting days from sudden unilateral loss of peripheral vestibular function, presumed viral. "
"The key bedside task is separating it from posterior-circulation stroke using HINTS."),
physiology=(
"**Tonic balance**: each vestibular nerve fires at a resting rate; the brain senses rotation from the difference between the two sides. "
"**Vestibulo-ocular reflex**: head rotation excites the ipsilateral horizontal canal and drives eye movement opposite the head to keep gaze stable. "
"**Nerve divisions**: the superior vestibular nerve supplies the superior and horizontal canals and utricle; the inferior nerve supplies the posterior canal and saccule. "
"**Central compensation**: the cerebellum and brainstem rebalance resting activity over days to weeks after a unilateral loss."),
pathophysiology=(
"**Unilateral loss creates false rotation**: when one nerve goes silent, the intact side's resting activity is interpreted as rotation toward it, causing vertigo and nystagmus beating away from the affected ear. "
"**Viral reactivation hypothesis**: herpes simplex type 1, found latent in human vestibular (Scarpa) ganglia, is thought to reactivate and inflame the nerve; this is supported by the literature rather than the core texts. "
"**Superior division predominance**: the superior nerve travels in a longer, narrower bony canal, so it is affected more often, sparing the posterior canal and saccule. "
"**Hearing spared**: the cochlear nerve is uninvolved; added hearing loss means labyrinthitis or a vascular (AICA) event. "
"**Head impulse test**: a rapid turn toward the affected side shows a corrective catch-up saccade because the VOR is lost; a normal head impulse in acute vertigo is worrisome for stroke. "
"**Compensation and steroids**: central compensation, accelerated by early vestibular rehabilitation, drives recovery; steroids may improve caloric recovery but not clearly long-term symptoms."),
),

"BPPV": dict(
overview=(
"Benign paroxysmal positional vertigo (BPPV) is brief vertigo triggered by head position change, caused by otoconia displaced into a semicircular canal. "
"It is the most common cause of peripheral vertigo and is cured at the bedside with canalith repositioning (Epley for posterior canal)."),
physiology=(
"**Otolith organs**: the utricle and saccule contain otoconia, calcium carbonate crystals embedded on a gelatinous membrane, that sense linear acceleration and gravity. "
"**Canals sense rotation**: each semicircular canal's cupula is normally the same density as endolymph, so it ignores gravity and responds only to angular acceleration. "
"**Canal geometry**: the posterior canal is the most dependent canal when upright and supine, so free debris settles there most often. "
"**Ewald laws**: eye movements occur in the plane of the stimulated canal; excitation of the posterior canal produces upbeating torsional nystagmus toward the affected ear."),
pathophysiology=(
"**Canalithiasis**: otoconia dislodged from the utricle (aging, head trauma, inner-ear disease, prolonged bed rest) float freely in the canal. "
"**Mechanism of vertigo**: when the head moves the canal into a gravity-dependent position, the debris falls and drags endolymph, deflecting the cupula. "
"**Latency and fatigue**: the clump takes a few seconds to start moving (latency), the response lasts under a minute, and repeated testing disperses particles (fatigability). "
"**Posterior canal (most common)**: Dix-Hallpike produces upbeating, torsional nystagmus toward the dependent ear. "
"**Horizontal canal**: supine roll test produces horizontal nystagmus; geotropic nystagmus suggests canalithiasis and apogeotropic suggests cupulolithiasis (debris stuck on the cupula, making it gravity sensitive). "
"**Repositioning logic**: the Epley maneuver rotates the head so debris travels around the canal and exits into the utricle, where it no longer stimulates the cupula."),
),

"Facial Paralysis": dict(
overview=(
"Facial paralysis is weakness of the muscles of facial expression from a CN VII lesion; Bell palsy (idiopathic, acute) is the most common cause but is a diagnosis of exclusion. "
"Management hinges on whether the lesion is central or peripheral, complete or incomplete, and what the cause is."),
physiology=(
"**Motor nucleus**: the upper face portion receives bilateral cortical input, while the lower face receives mainly contralateral input. "
"**Branches by segment**: GSPN at the geniculate (lacrimation), nerve to stapedius in the mastoid segment (stapedial reflex), and chorda tympani before the stylomastoid foramen (taste, submandibular/sublingual secretion). "
"**Labyrinthine segment**: the narrowest portion of the fallopian canal, at about 0.7 mm, with a thin vascular supply. "
"**Nerve injury grades (Sunderland/Seddon)**: neurapraxia (conduction block), axonotmesis (axon loss with intact sheath), and neurotmesis (complete transection). "
"**Electrophysiology**: after axonal loss, Wallerian degeneration makes the distal nerve inexcitable within 3-5 days, which is why ENoG is timed 3-14 days after onset."),
pathophysiology=(
"**Central vs peripheral**: a central (upper motor neuron) lesion spares the forehead because of bilateral cortical input; peripheral lesions paralyze the whole hemiface. "
"**Bell palsy mechanism**: presumed viral (HSV-1) reactivation causes nerve inflammation and edema; swelling within the tight labyrinthine segment produces compression, ischemia, and conduction block or degeneration. "
"**Why steroids early**: they reduce edema in the bony canal and improve complete recovery when started within 72 hours. "
"**Prognosis tracks injury degree**: neurapraxia recovers completely; axonal loss recovers slowly and incompletely, with risk of synkinesis from misdirected regenerating axons. "
"**ENoG logic**: more than 90 percent degeneration within 14 days of onset in complete paralysis predicts poor recovery and underlies the controversial middle fossa decompression. "
"**Topognosis**: whether tearing, stapedial reflex, and taste are affected in principle localizes the lesion relative to the GSPN, nerve to stapedius, and chorda tympani; in practice topognostic testing is unreliable because lesions are rarely discrete. "
"**Red flags against Bell**: slowly progressive weakness, recurrence on the same side, involvement of individual branches, or other cranial neuropathies suggest tumor."),
),

"Temporal Bone Fracture": dict(
overview=(
"Temporal bone fractures result from high-energy head trauma and threaten hearing, balance, the facial nerve, and the dura. "
"Modern classification by otic capsule involvement predicts complications better than the old longitudinal/transverse scheme."),
physiology=(
"**Otic capsule density**: the labyrinthine bone is very dense, so fractures often travel around it through weaker pneumatized bone. "
"**Neighbors at risk**: the facial nerve (especially perigeniculate region), ossicular chain, tegmen and dura, carotid canal, sigmoid sinus, and jugular bulb. "
"**Otic capsule healing**: it heals by fibrous union rather than bone, leaving a permanent path for infection to the meninges."),
pathophysiology=(
"**Otic capsule-sparing fractures** (most common, lateral blows): run through the squama and EAC, causing hemotympanum, TM tears, and conductive loss from ossicular disruption. "
"**Otic capsule-violating fractures** (occipital blows): cross the cochlea or vestibule, causing profound SNHL and vertigo and carry higher rates of facial paralysis and CSF leak. "
"**Facial nerve injury**: the perigeniculate area is most often injured, through edema, compression by bone fragments, or transection; immediate complete paralysis implies a severe injury, while delayed onset implies edema and a good prognosis. "
"**CSF leak**: tegmen and dural tears let CSF drain through the middle ear into the canal (otorrhea) or down the Eustachian tube (rhinorrhea); most close spontaneously within 7-10 days. "
"**Meningitis risk**: persistent communication and fibrous-only otic capsule healing create long-term meningitis risk, relevant to pneumococcal vaccination. "
"**Labyrinthine concussion and BPPV**: even without a fracture line, trauma can damage hair cells or dislodge otoconia."),
),

"Cochlear Implant Candidacy": dict(
overview=(
"Cochlear implants restore access to sound for people with severe-to-profound sensorineural loss who get limited benefit from well-fitted hearing aids. "
"Candidacy has expanded (single-sided deafness, asymmetric loss, younger children), so knowing the criteria and the anatomic and neural prerequisites matters."),
physiology=(
"**What the implant replaces**: lost hair cells; it electrically stimulates surviving spiral ganglion neurons directly. "
"**Tonotopy**: electrodes along the scala tympani stimulate base (high pitch) to apex (low pitch) neurons, mimicking place coding. "
"**Neural requirements**: a cochlear nerve must be present and the auditory pathway must be functional; an absent cochlear nerve is a contraindication (K.J. Lee) or at least a strong relative contraindication (Cummings), and an auditory brainstem implant is considered instead. "
"**Critical period**: the auditory cortex organizes around sound input in early childhood, so early implantation in congenitally deaf children produces better language outcomes."),
pathophysiology=(
"**Why aids fail**: once inner hair cells are lost, amplification produces distorted, unintelligible input; aided speech recognition scores therefore guide candidacy. "
"**Ossification after meningitis**: labyrinthitis ossificans can fill the scala tympani within weeks, making urgent imaging and early implantation important. "
"**Auditory deprivation**: long duration of deafness leads to neural degeneration and cortical reorganization by other senses, reducing outcomes, especially in prelingual adults implanted late. "
"**Anatomic barriers**: malformations (common cavity, incomplete partition), cochlear nerve deficiency, and ossification change electrode choice and expected benefit, and are mapped on CT and MRI. "
"**ANSD and CMV**: in auditory neuropathy spectrum disorder, implants can restore synchronous neural firing by bypassing a dysfunctional inner hair cell or synapse; children with congenital CMV (a sensorineural loss) also benefit, with outcomes similar to other etiologies unless neurodevelopmental comorbidity limits them."),
),

"Cochlear Implant Surgery": dict(
overview=(
"Cochlear implant surgery places an electrode array in the scala tympani through a mastoidectomy and facial recess approach. "
"The goals are complete atraumatic insertion, preserving residual hearing, and avoiding facial nerve injury, CSF gusher, and device extrusion."),
physiology=(
"**Facial recess**: the triangle bounded by the facial nerve (medially/posteriorly), the chorda tympani (laterally), and the incus buttress (superiorly) provides access to the round window. "
"**Round window niche**: it lies on the promontory, inferior to the oval window, and is often partly obscured by a bony overhang. "
"**Scala tympani**: the target chamber, below the basilar membrane, communicates with the round window membrane. "
"**Residual hearing**: surviving apical hair cells can be preserved for combined electric-acoustic stimulation if the basilar membrane is not damaged."),
pathophysiology=(
"**Insertion trauma**: forcing the array can translocate it from scala tympani into scala vestibuli, rupture the basilar membrane, and destroy residual hearing and neurons. "
"**Soft-surgery principles**: round window insertion, slow insertion, perioperative steroids, and lubrication reduce inflammation and fibrosis that destroy residual hearing. "
"**Gusher**: abnormal communication between the IAC and the cochlea (e.g., incomplete partition type III, X-linked) lets CSF pour out at cochleostomy. "
"**Meningitis risk**: implanted ears, especially with malformations and positioners in older devices, carry higher pneumococcal meningitis risk, so pneumococcal vaccination per CDC schedules is strongly recommended (Cummings notes it is not a formal requirement). "
"**Facial nerve stimulation**: current spread from electrodes near the labyrinthine segment can stimulate the facial nerve, especially with otosclerosis or malformations."),
),

"Tinnitus": dict(
overview=(
"Tinnitus is the perception of sound without an external source; most is subjective and linked to hearing loss. "
"The clinical job is to identify red flags (unilateral, pulsatile, objective) and then manage bothersome tinnitus with counseling, amplification, and CBT. The 2026 AAO-HNSF tinnitus guideline update adds a comprehensive audiologic evaluation for every patient, asking directly about self-harm, cochlear implant evaluation when hearing loss qualifies, and follow-up, and recommends against routine medications, supplements, or rTMS."),
physiology=(
"**Central gain**: the auditory system adjusts its sensitivity to match input; reduced cochlear input increases gain in the cochlear nucleus, inferior colliculus, and cortex. "
"**Spontaneous activity**: auditory neurons fire spontaneously even in silence, and the brain normally filters this out. "
"**Limbic and attention networks**: the amygdala, prefrontal cortex, and autonomic systems determine whether a sound is perceived as threatening or distressing."),
pathophysiology=(
"**Deafferentation model**: hair-cell or synaptic loss reduces input in a frequency region; central neurons increase gain and spontaneous synchronous firing, which is perceived as sound, often matching the hearing-loss frequency. "
"**Why distress varies**: limbic and attentional networks amplify perception and emotional response, explaining why CBT and counseling reduce bother without changing loudness. "
"**Somatic modulation**: neck and jaw inputs to the dorsal cochlear nucleus explain tinnitus changes with jaw clenching or neck movement (somatosensory tinnitus, now addressed in the 2026 guideline). **Why sound plus touch**: bimodal neuromodulation pairs sound with tongue or skin stimulation to exploit this auditory-somatosensory convergence and retrain central gain; the 2026 guideline discusses it as an emerging option. "
"**Pulsatile tinnitus**: a vascular sound reaching the cochlea (paraganglioma, dural AV fistula, sigmoid sinus diverticulum or dehiscence, idiopathic intracranial hypertension, carotid disease) and requires imaging. "
"**Objective tinnitus**: audible to the examiner, from vascular sources or muscle (palatal or middle-ear myoclonus). "
"**Unilateral tinnitus**: asymmetric neural pathology such as vestibular schwannoma must be excluded with MRI when accompanied by asymmetric hearing."),
),

"Hearing Aids and Bone-Conduction Devices": dict(
overview=(
"Hearing aids amplify sound for the cochlea, while bone-conduction devices bypass the outer and middle ear by vibrating the skull. "
"Matching the device to the type of loss, the ear canal, and the patient's goals is a core part of otology."),
physiology=(
"**Air-conduction aids**: a microphone, processor, and receiver deliver frequency-specific gain into the ear canal, with compression to keep loud sounds tolerable. "
"**Dynamic range**: sensorineural loss raises thresholds but not discomfort levels, narrowing the usable range (recruitment), so wide dynamic range compression is required. "
"**Bone conduction**: skull vibration stimulates both cochleae with very little interaural attenuation. "
"**CROS**: routes sound from a deaf ear to the better ear through a microphone on the deaf side."),
pathophysiology=(
"**Why conductive loss amplifies well**: the cochlea is healthy, so amplification restores clarity; bone-conduction devices are ideal when the canal cannot hold an aid (atresia, chronic drainage). "
"**Why severe SNHL amplifies poorly**: damaged inner hair cells and neurons distort sound, so loudness improves more than clarity, which pushes toward cochlear implants. "
"**Occlusion effect**: blocking the canal traps bone-conducted low-frequency sound, making one's own voice boomy; open fittings reduce it. "
"**Feedback**: sound leaking from the canal back to the microphone causes whistling, worsened by a loose fit or wax. "
"**Single-sided deafness**: a bone-anchored device or CROS transfers sound to the hearing ear but cannot restore binaural localization, whereas a cochlear implant can partially restore it. "
"**Untreated hearing loss**: it is associated with cognitive decline, social isolation, and falls, which is part of why amplification matters. **Access**: since 2022, FDA-regulated over-the-counter hearing aids serve adults with perceived mild-to-moderate loss, and the 2024 AAO-HNSF age-related hearing loss guideline recommends screening older adults and offering amplification."),
),

"Vestibular Test Battery": dict(
overview=(
"The vestibular test battery (VNG/ENG with calorics, rotary chair, video head impulse testing, and VEMPs) measures each part of the vestibular system across frequencies. "
"It localizes peripheral versus central dysfunction, identifies the affected side and organ, and documents compensation."),
physiology=(
"**Frequency coverage**: calorics test very low-frequency horizontal canal function, rotary chair tests low-to-mid frequencies, and head impulse testing tests high-frequency natural head movement. "
"**Calorics**: warm or cool irrigation creates a temperature gradient that moves endolymph convectively in the horizontal canal; warm water produces nystagmus toward the irrigated ear and cool water away (COWS). "
"**VEMPs**: loud sound stimulates otolith organs; cervical VEMP (saccule, inferior vestibular nerve) is recorded from the SCM and ocular VEMP (utricle, superior vestibular nerve) from the inferior oblique. "
"**Oculomotor testing**: saccades, pursuit, and optokinetic testing evaluate central pathways."),
pathophysiology=(
"**Unilateral weakness**: reduced caloric response (asymmetry over about 25 percent) indicates peripheral hypofunction on that side. "
"**Caloric-vHIT dissociation**: Ménière disease often shows reduced calorics with a normal head impulse, while vestibular neuritis abnormalities appear on both. "
"**Bilateral vestibulopathy**: reduced responses on both sides (ototoxicity) produce oscillopsia and imbalance, confirmed by rotary chair. "
"**Third-window physiology**: low cVEMP thresholds and high oVEMP amplitudes indicate superior canal dehiscence. "
"**Central signs**: abnormal pursuit, dysmetric saccades, direction-changing gaze-evoked nystagmus, or failure of fixation suppression point to brainstem or cerebellar lesions. "
"**Division localization**: an absent oVEMP with a normal cVEMP suggests superior vestibular nerve involvement, as in most vestibular neuritis."),
),

"Ototoxic / Noise-Induced Hearing Loss": dict(
overview=(
"Ototoxic hearing loss comes from drugs such as aminoglycosides and cisplatin; noise-induced loss comes from acoustic overexposure. "
"Both are largely preventable, typically start in the high frequencies, and require monitoring in at-risk patients."),
physiology=(
"**Outer hair cells are vulnerable**: they have high metabolic demand and are the first to fail with toxic or mechanical stress, beginning at the high-frequency base. "
"**Antioxidant defenses**: glutathione and related systems protect hair cells from reactive oxygen species. "
"**Ribbon synapses**: inner hair cells connect to auditory nerve fibers through glutamatergic synapses that can be injured independently of hair cells. "
"**Middle ear reflex**: the stapedius reflex dampens sustained loud low-frequency sound but is too slow to protect against impulse noise."),
pathophysiology=(
"**Aminoglycosides**: accumulate in hair cells, generate free radicals by forming iron complexes, and trigger apoptosis; gentamicin is more vestibulotoxic and amikacin more cochleotoxic. "
"**Mitochondrial susceptibility**: the m.1555A>G mitochondrial rRNA mutation makes ribosomes resemble bacterial ones, causing profound loss after a single aminoglycoside dose. "
"**Cisplatin**: produces reactive oxygen species in outer hair cells and the stria vascularis, causing dose-dependent, bilateral, permanent high-frequency loss; sodium thiosulfate given after cisplatin reduced hearing loss in children with localized hepatoblastoma (SIOPEL-6) and is now FDA-approved for this use. "
"**Loop diuretics**: inhibit the Na-K-2Cl transporter in the stria vascularis, reducing the endocochlear potential (usually reversible, but synergistic with aminoglycosides). "
"**Noise**: intense sound causes metabolic exhaustion and oxidative stress (temporary threshold shift), and with repeated exposure, permanent hair-cell loss maximal near 4 kHz (the notch). "
"**Acoustic trauma**: very loud impulse noise mechanically tears cochlear structures. "
"**Hidden hearing loss**: noise can destroy synapses before thresholds change, causing difficulty hearing in noise with a normal audiogram."),
),

"Autoimmune Inner Ear Disease": dict(
overview=(
"Autoimmune inner ear disease (AIED) is bilateral, asymmetric sensorineural loss progressing over weeks to months, often with vestibular symptoms, that responds to steroids. "
"It is one of the few treatable causes of progressive SNHL, so recognizing the tempo matters."),
physiology=(
"**Immune privilege**: the inner ear has a blood-labyrinth barrier, but the endolymphatic sac contains immune-competent cells and acts as its immunologic organ. "
"**Stria vascularis**: its vascular structure is a likely target for immune complex deposition and vasculitis. "
"**Steroid responsiveness**: glucocorticoid receptors are present in cochlear tissues, and steroids reduce inflammation there."),
pathophysiology=(
"**Immune-mediated injury**: autoantibodies and T cells target inner-ear antigens (e.g., heat shock protein 70 has been studied), with immune complex deposition and inflammation. "
"**Tempo is the clue**: faster than presbycusis and slower than sudden loss, typically progressing over weeks to months and often bilaterally. "
"**Primary vs secondary**: most AIED is primary (ear-limited); a minority is secondary to systemic autoimmune disease such as granulomatosis with polyangiitis, lupus, Cogan syndrome, rheumatoid arthritis, or relapsing polychondritis. "
"**Vestibular involvement**: similar immune injury of the vestibular end organs causes imbalance or episodic vertigo, overlapping with bilateral Ménière disease. "
"**Steroid response as diagnosis**: improvement with high-dose corticosteroids supports the diagnosis; steroid-sparing agents (methotrexate, biologics) are used for maintenance when steroid dependence develops."),
),

"CSF Otorrhea / Temporal Encephalocele": dict(
overview=(
"CSF otorrhea is CSF leaking into the middle ear and mastoid through a tegmen or posterior fossa defect, often with brain or meninges herniating (encephalocele). "
"It causes clear drainage or effusion and carries meningitis risk, so it is repaired surgically."),
physiology=(
"**Tegmen**: the thin bony roof of the mastoid and middle ear separates them from the middle cranial fossa dura and temporal lobe. "
"**CSF pressure**: normal opening pressure is about 10-15 cm H2O (spontaneous leaks often run 25-27 cm H2O) and transmits pulsatile force to the skull base. "
"**Arachnoid granulations**: aberrant granulations can erode skull-base bone over time."),
pathophysiology=(
"**Spontaneous leaks**: elevated intracranial pressure (often in obese patients with idiopathic intracranial hypertension physiology) gradually thins the tegmen, and arachnoid pits form multiple small defects. "
"**Herniation**: once bone is breached, dura and brain herniate into the mastoid or middle ear (encephalocele or meningoencephalocele), and CSF leaks. "
"**Clinical mimicry**: with an intact drum, CSF collects as an effusion and drains down the Eustachian tube, producing unilateral effusion or clear rhinorrhea; after tube placement it presents as persistent clear otorrhea. "
"**Acquired causes**: trauma, chronic ear disease, cholesteatoma erosion, and prior surgery. "
"**Meningitis risk**: a direct path from the nasopharynx and middle ear to the subarachnoid space allows bacterial spread, which is why repair is recommended. "
"**Recurrence**: untreated elevated ICP raises the risk of recurrence or new leaks after repair, so ICP management is part of care."),
),

"Necrotizing Otitis Externa": dict(
overview=(
"Necrotizing (malignant) otitis externa is an invasive infection of the external canal that spreads to the skull base, usually Pseudomonas in older diabetics or immunocompromised patients. "
"It causes severe pain, granulation tissue at the bony-cartilaginous junction, and cranial neuropathies, and requires prolonged systemic antibiotics."),
physiology=(
"**Fissures of Santorini**: natural gaps in the cartilaginous canal allow spread inferiorly toward the parotid and skull base. "
"**Bony-cartilaginous junction**: the classic site of granulation tissue and early invasion. "
"**Skull-base neighbors**: the stylomastoid foramen (CN VII) and jugular foramen (CN IX-XI), plus the hypoglossal canal (CN XII), lie close to the infection's route. "
"**Host defense**: neutrophil function and microvascular perfusion are essential to contain Pseudomonas."),
pathophysiology=(
"**Host susceptibility**: diabetic microangiopathy reduces tissue perfusion, and hyperglycemia impairs neutrophil chemotaxis and phagocytosis; immunosuppression and HIV play similar roles. "
"**Pseudomonas virulence**: exotoxins and proteases cause necrotizing vasculitis and tissue invasion. "
"**Spread**: infection extends from the canal floor through Santorini fissures and the tympanomastoid suture into the temporal bone and skull base, producing osteomyelitis. "
"**Cranial neuropathies**: CN VII is most often involved first at the stylomastoid foramen; spread medially affects CN IX-XII and can cause sigmoid or cavernous sinus thrombosis. "
"**Pain out of proportion**: periosteal and skull-base involvement explains deep, nocturnal pain. "
"**Fungal and resistant forms**: Aspergillus and resistant organisms occur, which is why cultures and biopsy guide therapy, along with exclusion of carcinoma."),
),
}
