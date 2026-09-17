"""Distractor-specific why-wrong repairs for Otology / Neurotology."""

WHY_WRONG_FIXES = {
    "v136_oto_01": [
        "Mastoidectomy is a surgical procedure for mastoid bone disease, not indicated for uncomplicated canal-confined otitis externa without extension beyond the canal or bony involvement.",
        "Correct.",
        "Oral steroids address inflammation but do not treat the underlying bacterial infection in the canal; topical antimicrobial therapy targeting the infection directly is the primary treatment needed.",
        "Untreated canal infection with edema and purulent debris will not resolve without intervention, and continuing water exposure/ear manipulation without precautions would worsen the condition.",
    ],
    "v136_oto_02": [
        "Correct.",
        "Symmetric, gradual, expected presbycusis pattern does not require routine imaging; CT would be reserved for asymmetric or otherwise atypical findings.",
        "There is no acute inflammatory or autoimmune process suggested here; steroids have no role in typical gradual presbycusis.",
        "This is factually incorrect and would deny beneficial treatment -- amplification and communication strategies do meaningfully improve function and quality of life in age-related hearing loss.",
    ],
    "v136_oto_03": [
        "Correct.",
        "Otosclerosis causes a conductive hearing loss pattern from stapes fixation; it does not produce absent OAEs with abnormal ABR neural synchrony, which reflects a neural/synaptic problem, not conductive pathology.",
        "Superior canal dehiscence causes a third-window conductive-type hearing pattern and vestibular symptoms, not the absent-OAE, abnormal-ABR pattern seen here.",
        "BPPV is a vestibular disorder causing positional vertigo, unrelated to newborn hearing screening results or ABR/OAE testing.",
    ],
    "v136_oto_04": [
        "Because central auditory pathways are bilaterally represented above the cochlear nuclei, a unilateral cortical lesion does not typically cause complete deafness in either ear; this describes a peripheral, not central, pattern.",
        "Conductive hearing loss results from external or middle-ear pathology, not a central cortical lesion.",
        "The vestibulo-ocular reflex is mediated by brainstem/peripheral vestibular pathways, not cortical auditory processing; a cortical lesion would not selectively impair this reflex.",
        "Correct.",
    ],
    "v136_oto_05": [
        "A cochlear implant user relies on the implant, not a hearing aid, for sound perception; increasing hearing-aid gain would not address abnormal electrode impedances or restore implant function.",
        "Treating for labyrinthitis without first testing the device ignores the objective finding of abnormal electrode impedances, which points toward a hardware problem.",
        "Cochlear implants can be surgically revised or replaced when hardware failure is confirmed; stating revision is never possible is factually incorrect.",
        "Correct.",
    ],
    "v136_oto_06": [
        "Drilling into the vestibule is unnecessary and destructive for standard cochlear implantation and would cause trauma to vestibular structures rather than achieving atraumatic scala-tympani placement.",
        "Correct.",
        "Intentionally disarticulating the ossicular chain serves no purpose in standard cochlear implant electrode insertion and would cause unnecessary conductive hearing damage.",
        "Tightly packing material around the electrode risks displacing the array or compromising its position rather than securing an atraumatic, stable placement.",
    ],
    "v136_oto_07": [
        "Correct.",
        "Stapedectomy addresses stapes fixation from otosclerosis, an entirely unrelated condition; it is not a required step for cochlear implantation in a malformed inner ear.",
        "The described anomaly involves the incomplete partition and cochlear aperture, inner-ear structures, not the external canal.",
        "This CT finding specifically signals increased anatomic risk (facial nerve variation, gusher risk); stating there is no additional surgical risk contradicts the clinical significance of this finding.",
    ],
    "v136_oto_08": [
        "Correct.",
        "Ossicular fusion is not a universal consequence of infancy and is unrelated to auditory deprivation or the rationale for early implantation.",
        "Lack of auditory stimulation does not cause cochlear infection; this describes an unrelated, incorrect mechanism.",
        "Hearing aids amplify sound to provide auditory input; they do not damage the auditory cortex.",
    ],
    "v136_oto_09": [
        "Autophony relieved by lying down is characteristic of patulous ETD, the opposite pattern from obstructive ETD.",
        "A tympanic membrane moving with respiration indicates an abnormally patent (patulous) Eustachian tube, not an obstructed one.",
        "Correct.",
        "Symptoms specifically triggered by exercise are characteristic of patulous ETD, not obstructive ETD.",
    ],
    "v136_oto_10": [
        "There is no inflammatory process here; this is a fixed congenital structural anomaly, and systemic steroids would have no effect on canal atresia or conductive hearing loss rehabilitation.",
        "Correct.",
        "A vestibular implant addresses balance disorders, not hearing rehabilitation; it is an entirely unrelated device for a different sensory system.",
        "An atretic (absent or closed) canal has no normal canal or tympanic membrane through which to place a tympanostomy tube; this is not anatomically feasible.",
    ],
    "v136_oto_11": [
        "Continuous, excessive sound protection can actually reinforce central auditory gain and worsen sound intolerance over time, the opposite of the graded, less-avoidant approach that helps.",
        "Stapedectomy addresses conductive hearing loss from stapes fixation; it has no role in treating hyperacusis, a central sound-tolerance processing disorder with a normal audiogram and exam here.",
        "Correct.",
        "Hyperacusis is a recognized clinical phenomenon that can coexist with migraine, anxiety, and tinnitus; dismissing all cases as malingering ignores a legitimate condition.",
    ],
    "v136_oto_12": [
        "Blind transcanal biopsy of a vascular jugular-foramen mass risks catastrophic hemorrhage without first understanding vascularity and anatomy.",
        "Jugular foramen masses have a broad differential (paraganglioma, schwannoma, meningioma, and others) distinct from vestibular schwannomas, which typically arise in the internal auditory canal/cerebellopontine angle.",
        "Correct.",
        "Proceeding to radical surgery without first assessing vascularity, cranial-nerve function, and growth pattern risks unnecessary morbidity and may bypass less invasive, equally effective options.",
    ],
    "v136_oto_13": [
        "Increasing traction on a nerve already showing signs of mechanical stress would worsen, not resolve, the concerning EMG activity and increases the risk of permanent facial nerve injury.",
        "Monitoring exists specifically to provide real-time warning of mechanical, thermal, or ischemic nerve stress that anatomy alone cannot detect; ignoring it defeats its entire safety purpose.",
        "Correct.",
        "Cutting the nerve to eliminate a warning signal destroys facial nerve function entirely, the exact outcome the monitoring is meant to help prevent; this is a drastic overreaction to a signal that calls for pausing and reassessing.",
    ],
    "v136_oto_14": [
        "Repeated local procedures without addressing the underlying systemic granulomatous disease activity will not durably resolve ear findings that are being driven by ongoing systemic inflammation.",
        "Otosclerosis is an isolated stapes fixation process; it does not explain the combination of serous otitis, progressive mixed hearing loss, and facial weakness in the context of a known systemic vasculitis.",
        "Correct.",
        "Coordinating with rheumatology is essential for controlling the systemic disease process driving the ear findings; avoiding this collaboration would leave the underlying, treatable disease process unaddressed.",
    ],
    "v136_oto_15": [
        "Correct.",
        "Tympanostomy tubes treat middle-ear effusion, an entirely different mechanism from stapes fixation; they would not improve conductive loss from otosclerosis.",
        "There is no infectious process described here; otosclerosis is not an infection, so antibiotics would have no effect on stapes fixation.",
        "Labyrinthectomy destroys vestibular (and residual hearing) function and is used for intractable vertigo, an entirely different problem; it would worsen this patient's hearing.",
    ],
    "v136_oto_16": [
        "Waiting until profound deafness develops forfeits the opportunity to detect early threshold shifts that could inform dose adjustments or alternative therapy before irreversible severe hearing loss occurs.",
        "Correct.",
        "Tympanostomy tubes treat middle-ear effusion; they have no role in addressing sensorineural ototoxic injury from cisplatin, which affects the cochlea directly.",
        "The new bilateral high-frequency tinnitus and hearing loss in the setting of cisplatin therapy is classic ototoxic sensorineural injury, not conductive.",
    ],
    "v136_oto_17": [
        "Canalith repositioning treats BPPV specifically; without positional nystagmus indicating canalithiasis, repeating this maneuver would not address PPPD, a different, functional vestibular disorder.",
        "Labyrinthectomy is a destructive procedure for confirmed ongoing peripheral vestibular pathology; PPPD is a functional, centrally-maintained disorder that testing shows is largely compensated, so destroying peripheral function would not help and could worsen symptoms.",
        "Correct.",
        "Prolonged inactivity and avoidance are part of the maladaptive pattern that maintains PPPD; strict bed rest would reinforce, not resolve, the disorder.",
    ],
    "v136_oto_18": [
        "Correct.",
        "Otitis externa is a canal-confined infection that does not produce an expansile petrous-apex lesion with restricted diffusion or sixth-nerve palsy.",
        "BPPV is a peripheral vestibular disorder causing positional vertigo, unrelated to a petrous-apex mass lesion or cranial nerve involvement.",
        "Tympanosclerosis is a middle-ear/tympanic-membrane scarring process; it does not produce an expansile petrous-apex lesion or cranial neuropathy.",
    ],
    "v136_oto_19": [
        "The carotid canal lies anteriorly and inferiorly in the temporal bone, unrelated to the facial recess dissection plane used to locate the vertical facial nerve during mastoidectomy.",
        "The cochlear aqueduct is a separate, deep structure related to CSF/perilymph communication, not a reliable surgical landmark for the vertical facial nerve.",
        "The tegmen forms the superior boundary of the middle ear/mastoid, a different plane from the facial nerve/chorda tympani relationship that specifically guides the facial recess approach.",
        "Correct.",
    ],
    "v136_oto_20": [
        "Mastoidectomy is an aggressive surgical procedure entirely disproportionate to a simple, dry, uncomplicated traumatic perforation, which typically heals with observation alone.",
        "Ototoxic drops risk further inner-ear injury if they pass through an open perforation into the middle ear; they are not appropriate for a perforation expected to heal spontaneously.",
        "Deliberately allowing water exposure risks introducing infection into the middle ear through the open perforation, the opposite of the dry-ear precautions needed to support healing.",
        "Correct.",
    ],
    "v136_oto_21": [
        "Prolonged vestibular suppressant use can actually impede the central compensation process needed for recovery from vestibular neuritis; they are meant for short-term acute symptom control, not chronic use.",
        "Strict bed rest and inactivity reinforce avoidance behavior and delay the central compensation that active movement and rehabilitation exercises are specifically designed to promote.",
        "Correct.",
        "The Epley maneuver treats BPPV specifically by repositioning displaced otoconia; without evidence of BPPV, repeating this maneuver would not address the vestibular hypofunction and avoidance behavior described here.",
    ],
    "v136_oto_22": [
        "Correct.",
        "Different vestibular tests intentionally sample different frequency ranges and structures; a discrepancy between them is expected and diagnostically meaningful, not evidence that one result is simply invalid.",
        "Caloric testing evaluates low-frequency horizontal semicircular canal function, not otolith function, which is assessed by different tests like VEMPs.",
        "The video head-impulse test evaluates the vestibulo-ocular reflex, not hearing; this statement misdescribes what vHIT measures.",
    ],
    "v141_oto_01": [
        "Correct.",
        "Chronic vestibular suppressants like meclizine do not correct the underlying mechanical problem (displaced otoconia) causing BPPV and can impede central compensation with prolonged use.",
        "Classic BPPV with a typical Dix-Hallpike response is a clinical diagnosis; routine imaging before treatment is unnecessary when the presentation is this characteristic.",
        "Labyrinthectomy is a destructive procedure reserved for intractable peripheral vestibular disease unresponsive to conservative treatment; it is vastly disproportionate to classic, treatable BPPV.",
    ],
    "v141_oto_02": [
        "Labyrinthectomy destroys residual hearing along with vestibular function; it is not the most hearing-preserving option when this patient still has useful hearing.",
        "Cochlear nerve section is a major neurosurgical procedure with its own risks and is not a universal escalation step; less invasive, hearing-preserving options should be tried first.",
        "This patient has ongoing disabling vertigo despite current therapy; declining any further treatment would leave a genuinely treatable symptom burden unaddressed.",
        "Correct.",
    ],
    "v141_oto_03": [
        "Correct.",
        "Immediate surgery is not mandatory for a small, minimally symptomatic tumor with good hearing; observation or radiation are also reasonable, less invasive options.",
        "Vestibular schwannomas are benign tumors; chemotherapy is not a standard or effective treatment for this tumor type.",
        "Even with observation as a reasonable initial strategy, serial monitoring is essential to detect growth that would change management; no follow-up would miss a growing tumor.",
    ],
    "v141_oto_04": [
        "This patient already has appropriately fitted hearing aids with poor benefit; simply increasing gain further would not overcome the poor speech recognition and could cause discomfort or distortion.",
        "Stapedectomy treats conductive hearing loss from stapes fixation; it has no role in bilateral sensorineural hearing loss, the mechanism described here.",
        "Cochlear implantation is a well-established, effective rehabilitation option for exactly this clinical picture; stating no rehabilitation is available is inaccurate.",
        "Correct.",
    ],
    "v141_oto_05": [
        "Correct.",
        "BPPV is an inner-ear positional vertigo disorder unrelated to mastoid infection, cranial nerve palsy, or retro-orbital pain.",
        "Otosclerosis causes isolated conductive hearing loss from stapes fixation; it does not explain lateral rectus palsy or retro-orbital pain in the setting of acute mastoiditis.",
        "Patulous Eustachian tube causes autophony from an abnormally open tube; it is entirely unrelated to mastoid infection spreading to the petrous apex.",
    ],
    "v141_oto_06": [
        "Treating persistent, recurrent clear otorrhea as ordinary serous otitis media without considering CSF leak risks missing a condition that carries meningitis risk and requires specific skull-base repair.",
        "Correct.",
        "Simply removing the tube without investigating the cause of recurrent clear drainage ignores a potentially serious CSF leak that will likely continue to drain and carries infection risk.",
        "Stapedectomy addresses stapes fixation from otosclerosis, an entirely unrelated condition with no connection to a tegmen defect or CSF leak.",
    ],
    "v142_oto_01": [
        "Correct.",
        "New facial weakness and persistent granulation at the bony-cartilaginous junction in a diabetic patient are red flags for skull-base extension; topical therapy alone is inadequate for a potentially invasive, life-threatening infection.",
        "Stapedectomy addresses stapes fixation from otosclerosis, an entirely unrelated condition; it has no role in treating an invasive skull-base infection.",
        "Facial weakness is not an expected finding in uncomplicated otitis externa; its presence here signals a serious complication that must be urgently addressed, not reassured away.",
    ],
    "v142_oto_02": [
        "Correct.",
        "Proceeding with a fenestration procedure designed to treat a fixed footplate, when the footplate is actually mobile, risks unnecessary inner-ear injury without addressing the true, different cause of the conductive hearing loss.",
        "Removing the incus does not address the actual underlying pathology, which needs to be reassessed first; this is a destructive step taken before understanding the true diagnosis.",
        "Labyrinthectomy destroys vestibular and residual hearing function and is used for intractable vertigo, an entirely disproportionate response to an unexpected intraoperative finding during stapes surgery.",
    ],
    "v142_oto_04": [
        "These structures define broader mastoidectomy boundaries but are not the specific landmarks that bound the facial recess itself, which is defined by the facial nerve, chorda tympani, and fossa incudis.",
        "The carotid artery, jugular bulb, and Eustachian tube are anteriorly/inferiorly located structures relevant to other aspects of temporal bone anatomy, not the specific boundaries of the facial recess.",
        "The superior semicircular canal, endolymphatic sac, and vestibular aqueduct are posterior/superior inner-ear-related structures, not the boundaries that define the facial recess opening into the middle ear.",
        "Correct.",
    ],
    "v143_oto_01": [
        "Uncomplicated diffuse otitis externa confined to the canal is a topical-treatment disease; oral antibiotics are reserved for extension beyond the canal or specific high-risk situations, not routine first-line therapy.",
        "There are no red flags (diabetes, cranial neuropathy) suggesting invasive disease; CT is unnecessary before treating straightforward, uncomplicated otitis externa.",
        "Correct.",
        "Mastoidectomy is a major surgical procedure for mastoid bone disease, entirely disproportionate to canal-confined, uncomplicated otitis externa.",
    ],
    "v143_oto_02": [
        "Sensorineural hearing loss shows elevated bone thresholds along with air thresholds; here bone thresholds are normal (10 dB) with elevated air thresholds, defining a conductive, not sensorineural, pattern.",
        "Correct.",
        "Auditory neuropathy typically shows a specific electrophysiologic pattern (present OAEs with abnormal ABR) rather than this straightforward conductive air-bone gap with a type B tympanogram, which points to a middle-ear mechanical problem.",
        "A 45 dB air-bone gap represents a clinically significant conductive hearing loss, not normal hearing.",
    ],
    "v143_oto_03": [
        "Forcing the electrode against resistance risks fracturing the cochlear structures or causing significant intracochlear trauma; the correct response to resistance is to stop and reassess, not push through.",
        "Widely opening the vestibule is unnecessary and destructive for standard scala-tympani electrode placement and would cause trauma to vestibular structures.",
        "Removing the stapes serves no purpose in standard cochlear implant electrode insertion through the round window and would cause unnecessary additional conductive damage.",
        "Correct.",
    ],
    "v143_oto_04": [
        "Correct.",
        "Performing stapes surgery without first confirming the diagnosis of superior canal dehiscence via imaging risks operating on the wrong condition and could worsen symptoms if the actual problem is a third-window syndrome.",
        "MRI brain does not adequately visualize the fine bony detail of the superior semicircular canal needed to confirm dehiscence; high-resolution CT reformatted in the canal plane is the specific imaging study required.",
        "There is no evidence of middle-ear infection here (normal middle-ear mechanics); this presentation is inconsistent with otitis media.",
    ],
    "v143_oto_05": [
        "Correct.",
        "Labyrinthectomy is a destructive procedure for confirmed unilateral peripheral vestibular disease; it is entirely inappropriate for vestibular migraine, a central, episodic, migraine-related disorder with normal hearing between attacks.",
        "Bacterial labyrinthitis is an infectious process typically with hearing loss and evidence of infection; it does not fit a pattern of recurrent episodic vertigo with migraine features and normal interictal hearing.",
        "Stapedectomy addresses conductive hearing loss from stapes fixation, an entirely unrelated condition with no role in treating episodic vertigo of migrainous origin.",
    ],
    "v144_oto_01": [
        "Correct.",
        "While age-related hearing loss is common, it still functionally impairs communication and quality of life; declining any treatment ignores effective rehabilitation options.",
        "Symmetric, typical presbycusis without red flags does not require imaging before discussing amplification; routine CT is not indicated solely for this presentation.",
        "There is no acute inflammatory process described; steroids have no role in typical gradual, symmetric age-related hearing loss.",
    ],
    "v144_oto_02": [
        "Correct.",
        "Cerumen impaction would typically cause absent OAEs due to conductive blockage, not the specific pattern of present OAEs with an absent/abnormal ABR that indicates a neural synchrony problem.",
        "Conductive otitis media would be expected to affect OAE testing as well (via the conductive pathway) rather than producing this specific dissociation between preserved OAE and disordered ABR.",
        "Otosclerosis causes a conductive hearing loss pattern from stapes fixation; it does not explain this specific neural pattern.",
    ],
    "v144_oto_03": [
        "The basal turn of the cochlea is stiff and narrow, tuned to encode high, not low, frequencies; a basal turn lesion would cause the opposite pattern from what this option describes.",
        "The cochlea is the hearing organ; a cochlear lesion affects hearing, not vestibular function, which is mediated by separate vestibular end organs.",
        "Correct.",
        "A cochlear lesion affects hearing perception, not speech production, which is a motor function unrelated to cochlear pathology.",
    ],
    "v144_oto_04": [
        "A slowly stable loss over decades describes a pattern more consistent with typical presbycusis, not the rapidly progressive, fluctuating course that supports an autoimmune inner-ear process.",
        "A single brief positional vertigo episode is characteristic of BPPV, an entirely different, benign mechanical vestibular disorder.",
        "Correct.",
        "This patient by definition has documented progressive bilateral SNHL; a normal audiogram would contradict the premise of hearing loss.",
    ],
    "v144_oto_05": [
        "Correct.",
        "Peripheral vestibular neuritis typically shows an abnormal head-impulse test; a normal head-impulse test combined with direction-changing nystagmus and severe ataxia is atypical for peripheral neuritis and instead suggests a central cause.",
        "BPPV causes brief, positional vertigo triggered by specific head movements, not continuous vertigo with severe truncal ataxia and direction-changing gaze-evoked nystagmus, which are central red flags.",
        "Ménière disease is diagnosed based on episodic vertigo with associated fluctuating hearing loss and aural fullness; nothing here confirms this diagnosis, and the concerning central findings should prompt urgent workup instead.",
    ],
    "v144_oto_06": [
        "Abnormal integrity testing points toward a device-related, not central neural, problem; assuming central decline and simply observing would miss a correctable hardware issue.",
        "Correct.",
        "Removing the implant without planning for potential reimplantation abandons the patient's hearing rehabilitation prematurely, before a structured workup has determined the appropriate next step.",
        "Ear drops treat external/middle-ear conditions and have no relevance to an internal cochlear implant device malfunction.",
    ],
    "v144_oto_07": [
        "This specific anatomy (incomplete partition, widened cochlear aperture) is a recognized risk factor for gusher and abnormal facial nerve course; stating there is no added concern ignores a real, well-described risk.",
        "Children with cochleovestibular malformations, including incomplete partition anomalies, can often still receive cochlear implants with appropriate surgical planning; stating implantation is impossible is inaccurate.",
        "The mastoid cortex is a superficial landmark unrelated to the specific inner-ear and facial-nerve anatomic risks posed by this malformation.",
        "Correct.",
    ],
    "v144_oto_08": [
        "Cochlear anatomic growth timing is not the reason early auditory access matters; the actual concern is central auditory cortical development, which depends on early meaningful auditory input.",
        "Hearing aids amplify sound but do not cure the underlying sensorineural hearing loss; this statement misrepresents what hearing aids actually do.",
        "Speech therapy can still provide benefit beyond infancy; stating it is ineffective after infancy overstates the graded, not binary, nature of auditory developmental windows.",
        "Correct.",
    ],
    "v144_oto_09": [
        "Correct.",
        "A normal exam during symptoms would argue against, not for, obstructive ETD, since obstructive ETD should produce objective findings that correlate with symptoms.",
        "A migraine history alone does not provide objective evidence of middle-ear pressure dysfunction; it would instead suggest considering migraine-related causes of aural symptoms.",
        "Autophony improving when supine is the classic pattern of patulous ETD (the opposite condition), not obstructive ETD.",
    ],
    "v144_oto_10": [
        "Bone-conduction technology is a well-established, effective rehabilitation option for exactly this scenario; stating no rehabilitation is possible is inaccurate.",
        "Correct.",
        "Cochlear implantation addresses sensorineural hearing loss with poor cochlear function; this patient has good bone-conduction thresholds and a conductive problem, making bone-conduction technology the appropriate first consideration.",
        "There is no inflammatory process described; steroids would not correct a structural/mechanical conductive pathway issue related to recurrent canal disease.",
    ],
    "v144_oto_11": [
        "Constant sound overprotection can reinforce central auditory gain and worsen sound intolerance over time, the opposite of the graded exposure approach that actually helps.",
        "Stapedectomy treats conductive hearing loss from stapes fixation; this patient has normal hearing thresholds, and hyperacusis is not addressed by ear surgery.",
        "Correct.",
        "Ménière disease involves episodic vertigo, fluctuating hearing loss, and aural fullness; treating this presentation as Ménière disease without further evaluation misapplies an unrelated diagnosis.",
    ],
    "v144_oto_12": [
        "Nausea commonly accompanies both labyrinthitis and vestibular neuritis as a nonspecific autonomic response to vertigo; it does not distinguish between the two conditions.",
        "Correct.",
        "Continuous vertigo occurs in both labyrinthitis and vestibular neuritis, since both produce an acute vestibular syndrome; it is not the distinguishing feature.",
        "Head-motion intolerance is a shared feature of both conditions related to vestibular hypofunction; it does not differentiate labyrinthitis from isolated vestibular neuritis.",
    ],
    "v144_oto_13": [
        "Immediate biopsy without first understanding vascularity and critical neurovascular relationships risks catastrophic hemorrhage or nerve injury.",
        "Lateral skull-base masses with multiple lower cranial neuropathies have a broad differential distinct from vestibular schwannomas, which typically cause different cranial nerve involvement; assuming this diagnosis could lead to an inappropriate treatment plan.",
        "Correct.",
        "Symptoms alone do not reveal the tumor's vascularity, exact compartment of origin, or relationship to critical vessels; imaging-based anatomic characterization is needed.",
    ],
    "v144_oto_14": [
        "Correct.",
        "A sudden increase in EMG activity is itself a warning sign of nerve stress, not proof of an intact, unstressed nerve; interpreting it as reassuring would miss an important safety signal.",
        "Monitoring is an adjunct to, not a replacement for, direct anatomic identification of the nerve; relying on monitoring alone would be an incomplete safety strategy.",
        "Sacrificing the nerve in response to a warning sign that calls for pausing and reassessing is a drastic overreaction that would cause the exact permanent facial paralysis the monitoring is meant to help prevent.",
    ],
    "v144_oto_15": [
        "Sudden SNHL is a sensorineural process typically without a hypercompliant tympanogram or the mechanical findings described here; this presentation is conductive, not sensorineural.",
        "Ménière disease involves episodic vertigo, fluctuating sensorineural hearing loss, and aural fullness; it does not produce a persistent conductive gap with hypercompliant tympanometry after trauma.",
        "Vestibular neuritis is a vestibular (balance) disorder without hearing loss or conductive findings; it does not fit a presentation of persistent conductive hearing loss.",
        "Correct.",
    ],
    "v144_oto_16": [
        "Correct.",
        "Treating each episode as isolated, uncomplicated otitis media without recognizing the underlying systemic granulomatous disease will likely lead to recurrent, refractory ear findings.",
        "Performing tympanoplasty during active, uncontrolled systemic inflammatory disease risks poor surgical outcomes and graft failure.",
        "Laboratory and rheumatologic evaluation is essential to identify and manage the systemic disease process driving the refractory otologic findings.",
    ],
    "v144_oto_17": [
        "Correct.",
        "There is no inflammatory process here; systemic steroids have no mechanism to reverse stapes fixation from otosclerosis.",
        "Canal-wall-down mastoidectomy is a procedure for chronic ear disease/cholesteatoma, an entirely different indication unrelated to stapes fixation.",
        "Effective treatment options (amplification, stapes surgery) exist and should be offered to a patient with disabling hearing loss; mandating observation regardless of disability denies beneficial treatment.",
    ],
    "v144_oto_18": [
        "High-frequency loss often precedes noticeable conversational hearing impairment; waiting until conversational hearing is affected means missing the earlier opportunity to detect threshold shifts.",
        "Reducing additional noise exposure during ototoxic therapy can help minimize cumulative auditory insult; stating noise protection has no role ignores this potential protective measure.",
        "Ototoxic hearing loss from cisplatin is often permanent, not always reversible; this statement is factually incorrect and could lead to false reassurance.",
        "Correct.",
    ],
    "v144_oto_19": [
        "Obstructive ETD produces negative middle-ear pressure and retraction, not the TM movement with respiration and improvement when supine seen here, which is the opposite pattern.",
        "Otosclerosis causes progressive conductive hearing loss from stapes fixation; it does not cause autophony of voice/breathing or TM movement with respiration.",
        "Acute labyrinthitis is an infectious/inflammatory inner-ear process typically with vertigo and hearing loss; it does not produce the positional autophony described here.",
        "Correct.",
    ],
    "v144_oto_20": [
        "Chronic vestibular suppressant use can impede central compensation and does not address the maladaptive visual/postural dependence that maintains PPPD.",
        "Canal plugging surgery treats specific mechanical vestibular conditions like intractable BPPV or superior canal dehiscence; it has no role in PPPD, a functional, centrally-mediated disorder.",
        "Correct.",
        "Strict bed rest reinforces avoidance and inactivity, part of the maladaptive pattern maintaining PPPD, rather than addressing it through active rehabilitation.",
    ],
    "v144_oto_21": [
        "Not all petrous apex lesions require surgery; some, like asymptomatic cholesterol granulomas, can be observed, while symptomatic or growing lesions may need drainage or resection.",
        "Biopsying through the carotid canal would risk catastrophic injury to the internal carotid artery; this is an unsafe approach to any petrous apex lesion.",
        "This presentation (chronic retro-orbital pain, diplopia, T1-hyperintense expansile lesion) is inconsistent with acute mastoiditis, an infectious process with a different clinical course and imaging appearance.",
        "Correct.",
    ],
    "v144_oto_22": [
        "Pulse-synchronous tinnitus has a distinct differential (vascular, structural, intracranial causes) from ordinary subjective tinnitus and specifically warrants evaluation.",
        "Oral steroids do not address the vascular or structural causes that typically underlie pulsatile tinnitus; empiric steroid treatment would not identify or treat the actual cause.",
        "Correct.",
        "Stapedectomy addresses conductive hearing loss from otosclerosis; it has no established role as an initial step in evaluating new unilateral pulsatile tinnitus with normal otoscopy.",
    ],
    "v144_oto_23": [
        "Correct.",
        "Most uncomplicated traumatic perforations heal spontaneously; performing tympanoplasty immediately in every case is an unnecessary surgical intervention when observation is often sufficient.",
        "Introducing hydrogen peroxide irrigation into an open perforation risks middle-ear irritation or ototoxic injury and works against the dry-ear precautions needed to support healing.",
        "There is no inflammatory or infectious indication described; systemic steroids have no established role in managing an uncomplicated traumatic perforation.",
    ],
    "v144_oto_24": [
        "A type As tympanogram (shallow compliance) with absent reflexes and a conductive air-bone gap indicates an abnormally stiff middle-ear system, not normal mechanics.",
        "Correct.",
        "Vestibular neuritis is a vestibular (balance) disorder without conductive hearing findings; it does not produce this tympanometric and audiometric pattern.",
        "Pure cochlear presbycusis produces a sensorineural pattern with normal tympanometry, not a conductive air-bone gap with an abnormal type As tympanogram.",
    ],
    "v144_oto_25": [
        "BPPV causes brief, positional vertigo triggered by specific movements, not the continuous 36-hour vertigo with unidirectional nystagmus and abnormal head impulse described here.",
        "Salt restriction is a management strategy for Ménière disease, not a diagnostic test; and this presentation lacks the hearing loss and episodic pattern that would suggest Ménière disease in the first place.",
        "Acoustic neuroma typically presents with a more gradual course, and this acute presentation with an otherwise normal exam does not indicate an emergency surgical tumor.",
        "Correct.",
    ],
    "v144_oto_26": [
        "Long-term suppressant use and activity restriction reinforce avoidance behavior and can impede the central compensation process that active rehabilitation is designed to promote.",
        "Cervical immobilization addresses neck-related issues, not vestibular compensation; it does not target the gaze-stability and balance mechanisms needed to overcome vestibular hypofunction-related avoidance.",
        "Correct.",
        "Middle-ear surgery addresses structural middle-ear problems; it has no role in promoting central vestibular compensation for hypofunction that persists after the acute injury has resolved.",
    ],
    "v144_oto_27": [
        "Pure-tone audiometry measures hearing thresholds, an auditory function, not otolith (balance) function, which is assessed by different tests like VEMPs.",
        "Tympanometry measures middle-ear compliance/pressure, an auditory/middle-ear function; it does not assess saccular (vestibular otolith) function, which requires cervical VEMP testing.",
        "Otoacoustic emissions measure cochlear outer hair cell function (a hearing test), not horizontal semicircular canal function, which is assessed by tests like calorics or vHIT.",
        "Correct.",
    ],
}


def apply_why_wrong_fix_otology_v1(data_module):
    """Overwrite why_wrong for the fixed ids. Returns count actually updated."""
    byid = {q.get("id"): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")}
    updated = 0
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        if len(new_why_wrong) != len(q.get("choices") or []):
            raise ValueError(
                f"{qid}: fix has {len(new_why_wrong)} entries but question has "
                f"{len(q.get('choices') or [])} choices"
            )
        q["why_wrong"] = new_why_wrong
        updated += 1
    if missing:
        print(f"why_wrong_fix_otology_v1: {len(missing)} ids not found: {missing}")
    return updated
