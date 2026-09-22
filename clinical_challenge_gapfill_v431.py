"""v43.1: Clinical Challenge coverage gap-fill for 24 topics that sat at <=1 question.

Requested 2026-09-22 (the "Yes" to the proposed 24-topic gap-fill): every topic below
had zero or one Clinical Challenge despite having full six-field curriculum content.
Adds 2 new questions to each of the 21 zero-coverage topics and 1 new question to each
of the 3 single-coverage topics (Gradenigo, Orbital Apex, Villaret -- already partially
covered from the v42.5 skull-base syndrome work), for 45 new questions total, bringing
every one of these topics to >=2 Clinical Challenges. Every question is grounded
directly in that topic's existing recognize/localize/workup/manage/operate/teach
content (re-read in full immediately before authoring) rather than new, unsourced
claims -- no new source_basis citations are needed since no curriculum-card content is
being added or changed, only new assessment items against already-sourced content.
"""

import re


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


CLINICAL_CHALLENGES_NEW = [
    # ---------------- Otology / Neurotology ----------------
    {
        "id": "v431-eac-exostoses-osteoma-01",
        "domain": "Otology / Neurotology",
        "topic": "EAC Exostoses / Osteoma (Canalplasty)",
        "stem": (
            "A competitive cold-water surfer has bilateral, multiple, smooth, broad-based bony prominences in the "
            "medial ear canals, found incidentally. The entire tympanic membrane is visible bilaterally, hearing "
            "is normal, and there is no history of trapped water, infection, or impaction. What is the most "
            "appropriate management?"
        ),
        "choices": [
            "Observation, with counseling on cold-water exposure reduction and protective earplugs/hood use",
            "Bilateral canalplasty/exostectomy now, before symptoms develop",
            "High-resolution CT temporal bone to rule out cholesteatoma",
            "Biopsy of the bony prominences to exclude neoplasm",
        ],
        "answer": 0,
        "explanation": (
            "An asymptomatic, patent, self-cleaning canal with a fully visible tympanic membrane does not need "
            "surgery -- observation with exposure-reduction counseling and protective gear is appropriate. Surgery "
            "is reserved for recurrent obstruction-related infections, symptomatic trapping/impaction, attributable "
            "hearing loss, or an unmonitorable TM/medial canal."
        ),
        "why_wrong": [
            "Correct.",
            "Prophylactic canalplasty is not justified by imaging or lesion appearance alone without symptoms or "
            "an access/surveillance problem.",
            "Smooth, broad-based, bilateral exostoses in a cold-water-exposure history are a classic pattern; CT is "
            "reserved for severe occlusion, suspected cholesteatoma/erosion, atypical tumor, or preoperative mapping "
            "-- not routine for a typical asymptomatic case.",
            "Classic bony exostoses do not require biopsy; biopsy is reserved for atypical, suspicious soft-tissue "
            "lesions.",
        ],
        "board_pearl": "Incidental smooth bilateral exostoses in a patent, dry, self-cleaning canal = observation, "
        "not prophylactic surgery.",
        "curveball": "How do exostoses and an EAC osteoma typically differ in presentation?",
        "curveball_answer": (
            "Exostoses are typically bilateral, multiple, and broad-based, associated with cold-water exposure "
            "(surfing/diving). An osteoma is usually a solitary, unilateral, discrete or pedunculated bony mass, "
            "often near a tympanosquamous or tympanomastoid suture -- these are typical patterns, not absolute "
            "diagnostic rules."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-eac-exostoses-osteoma-02",
        "domain": "Otology / Neurotology",
        "topic": "EAC Exostoses / Osteoma (Canalplasty)",
        "stem": (
            "A patient with severe symptomatic canal exostoses causing recurrent otitis externa and conductive "
            "hearing loss elects canalplasty. This is their only-hearing ear. Which statement about the "
            "osteotome-versus-drill technique choice is most accurate?"
        ),
        "choices": [
            "The drill is universally safer and should always be chosen for the only-hearing ear",
            "The osteotome is universally safer and should always be chosen for the only-hearing ear",
            "Published cohort data show real tradeoffs between techniques (e.g., higher TM perforation with "
            "osteotome, higher sensorineural hearing loss with drill in one systematic review), so neither is "
            "universally safer, and the small but consequential SNHL risk should be explicitly discussed",
            "Technique choice does not affect complication rates and can be based on surgeon preference alone",
        ],
        "answer": 2,
        "explanation": (
            "A 2023 systematic review of 1,788 ears found pooled TM perforation 5.3% (osteotome) vs. 3.8% (drill), "
            "sensorineural hearing loss 0.69% (osteotome) vs. 4.3% (drill), and restenosis 1.1% vs. 4.1%, "
            "respectively -- real tradeoffs, not a universal 'one is always safer' answer. For the only-hearing "
            "ear, the small but consequential risk of iatrogenic sensorineural hearing loss must be explicitly "
            "discussed regardless of technique chosen."
        ),
        "why_wrong": [
            "The drill is not universally safer -- it carried a higher pooled SNHL rate in the cited review.",
            "The osteotome is not universally safer -- it carried a higher pooled TM perforation rate in the "
            "cited review, despite lower pooled SNHL and postoperative stenosis rates.",
            "Correct.",
            "Technique choice is associated with different pooled complication profiles in cohort data, even "
            "though heterogeneity and nonrandomized design limit causal comparison.",
        ],
        "board_pearl": "Never teach restenosis, TM perforation, or SNHL after canalplasty as a single universal "
        "percentage -- cite the tradeoffs and individualize, especially for the only-hearing ear.",
        "curveball": "What intraoperative hazard is specific to posterior-inferior medial canal drilling?",
        "curveball_answer": (
            "The facial nerve's mastoid segment approaches the posterior-inferior medial canal wall and its course "
            "can be lateral to the annular plane; blind drilling there risks facial nerve injury. Anterior canal "
            "drilling risks TMJ exposure, and medial drilling risks the TM/ossicular chain."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-ramsay-hunt-01",
        "domain": "Otology / Neurotology",
        "topic": "Ramsay Hunt Syndrome (Herpes Zoster Oticus)",
        "stem": (
            "A patient presents with acute unilateral facial weakness and severe otalgia. No vesicles are visible "
            "on the pinna, ear canal, or oropharynx. Which statement is most accurate?"
        ),
        "choices": [
            "The absence of vesicles excludes Ramsay Hunt syndrome; this must be Bell palsy",
            "Absence of a visible rash does not exclude Ramsay Hunt syndrome (zoster sine herpete), and severe "
            "otalgia with facial palsy still warrants a careful search for vesicles and consideration of the "
            "diagnosis",
            "Vesicles always precede the facial palsy in Ramsay Hunt syndrome, so their absence now means they "
            "will never appear",
            "MRI is required in every case of facial palsy with otalgia before starting any treatment",
        ],
        "answer": 1,
        "explanation": (
            "Rash may follow the palsy or be absent entirely (zoster sine herpete). Ear pain plus palsy warrants a "
            "careful search for vesicles, but their absence does not exclude the diagnosis. The workup is clinical; "
            "MRI/electrodiagnostics are reserved for atypical, severe, or nonrecovering cases rather than being "
            "routine."
        ),
        "why_wrong": [
            "Absence of vesicles does not exclude Ramsay Hunt syndrome; zoster sine herpete is a recognized "
            "presentation.",
            "Correct.",
            "Vesicles can appear after the palsy, not only before, or may never become visible.",
            "MRI is reserved for atypical, severe, or nonrecovering presentations, not required routinely when the "
            "diagnosis is clinically evident.",
        ],
        "board_pearl": "Ramsay Hunt generally has a worse facial recovery prognosis than Bell palsy -- ear pain "
        "plus palsy should prompt a careful vesicle search even when none are initially visible.",
        "curveball": "Is facial nerve decompression indicated for Ramsay Hunt syndrome?",
        "curveball_answer": (
            "Facial nerve decompression is not routine because evidence is insufficient. Immediate priorities are "
            "corneal protection and early corticosteroid plus antiviral therapy; persistent deficits are managed "
            "later with exposure protection, rehabilitation, chemodenervation, or facial reanimation."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-ramsay-hunt-02",
        "domain": "Otology / Neurotology",
        "topic": "Ramsay Hunt Syndrome (Herpes Zoster Oticus)",
        "stem": "What is the underlying pathophysiology of Ramsay Hunt syndrome, and what associated symptoms can it explain?",
        "choices": [
            "Varicella-zoster reactivation in the geniculate ganglion inflaming the facial nerve in the fallopian "
            "canal, with adjacent vestibulocochlear nerve involvement explaining hearing loss, tinnitus, or vertigo",
            "A slowly growing schwannoma along the facial nerve causing gradual, non-painful weakness",
            "Autoimmune demyelination isolated to the facial nerve with no adjacent cranial nerve involvement possible",
            "Chronic otitis media eroding directly into the fallopian canal",
        ],
        "answer": 0,
        "explanation": (
            "Varicella-zoster reactivation in the geniculate ganglion inflames the facial nerve within the "
            "fallopian canal; its anatomic proximity to the vestibulocochlear nerve explains why hearing loss, "
            "tinnitus, or vertigo may coexist with the facial palsy."
        ),
        "why_wrong": [
            "Correct.",
            "A slowly growing schwannoma describes facial nerve schwannoma, a different diagnosis with a distinct, "
            "typically non-painful, progressive or fluctuating course rather than acute painful zoster reactivation.",
            "The geniculate ganglion's proximity to the vestibulocochlear nerve explains why audiovestibular "
            "symptoms commonly coexist -- adjacent-nerve involvement is expected, not excluded.",
            "The mechanism is viral reactivation, not otitis media eroding the fallopian canal.",
        ],
        "board_pearl": "Acute unilateral facial weakness with severe otalgia and vesicles (or a history suspicious "
        "for zoster sine herpete) localizes to geniculate-ganglion VZV reactivation, not a slowly progressive nerve "
        "tumor.",
        "curveball": "How would you document severity and eye-closure risk at initial evaluation?",
        "curveball_answer": (
            "Examine the ear and oropharynx, document House-Brackmann grade and eye closure, and obtain audiometry "
            "when hearing symptoms are present -- meticulous corneal protection should start immediately given the "
            "risk of incomplete eye closure."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-facial-nerve-schwannoma-01",
        "domain": "Otology / Neurotology",
        "topic": "Facial Nerve Schwannoma",
        "stem": (
            "A patient has a presumed Bell palsy that fails to recover over several months, with subtle recurrent "
            "fluctuation in facial weakness. What should prompt suspicion for facial nerve schwannoma, and what "
            "study is most useful?"
        ),
        "choices": [
            "Recurrent or non-recovering same-side facial palsy is reassuring and needs no further workup",
            "Recurrent same-side palsy or failure of presumed Bell palsy to recover should prompt imaging; contrast "
            "MRI best maps neural/soft-tissue extent, with temporal-bone CT to define fallopian-canal/ossicular "
            "involvement",
            "This presentation is diagnostic of Ramsay Hunt syndrome and needs only a skin exam",
            "Facial nerve schwannoma cannot cause fluctuating weakness, so imaging is unnecessary",
        ],
        "answer": 1,
        "explanation": (
            "Recurrent same-side palsy or failure of presumed Bell palsy to recover warrants imaging. Contrast MRI "
            "maps neural and soft-tissue extent; temporal-bone CT defines fallopian-canal and ossicular "
            "involvement. Smooth fallopian-canal enlargement and multisegment enhancement help distinguish "
            "schwannoma from other temporal-bone/CPA lesions."
        ),
        "why_wrong": [
            "Non-recovering or recurrent facial palsy is a recognized red flag, not a reassuring finding.",
            "Correct.",
            "Ramsay Hunt syndrome is an acute painful presentation typically with vesicles/otalgia, not a slowly "
            "progressive or recurrent, fluctuating course; imaging (not a skin exam) is the appropriate next step "
            "here.",
            "Facial nerve schwannoma classically causes slowly progressive, recurrent, or fluctuating weakness, "
            "sometimes discordant with tumor size.",
        ],
        "board_pearl": "Facial function discordant with tumor size, or facial weakness that fails to follow the "
        "expected Bell palsy recovery course, should trigger imaging for facial nerve schwannoma.",
        "curveball": "If facial function is currently good, does that favor surgical resection?",
        "curveball_answer": (
            "No -- intact function argues against reflexive excision, since resection often risks major facial "
            "deterioration. Small or slowly growing tumors with useful facial function are typically observed with "
            "serial exam, audiometry, and MRI; intervention (stereotactic radiation, decompression, nerve-sparing "
            "debulking, or resection with repair/grafting) is individualized by growth, symptoms, hearing, "
            "location, age, and goals -- counsel from present function, not tumor size alone."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-facial-nerve-schwannoma-02",
        "domain": "Otology / Neurotology",
        "topic": "Facial Nerve Schwannoma",
        "stem": "Which imaging finding helps distinguish a facial nerve schwannoma from other temporal-bone or cerebellopontine-angle lesions?",
        "choices": [
            "Smooth fallopian-canal enlargement with multisegment enhancement along the course of the facial nerve",
            "An isolated internal auditory canal mass that never involves the fallopian canal",
            "Focal bone erosion with exposed cartilage in the external auditory canal",
            "Opacification of only the mastoid air cells with no soft-tissue mass",
        ],
        "answer": 0,
        "explanation": (
            "Facial nerve schwannoma can arise along any facial-nerve segment; smooth fallopian-canal enlargement "
            "and multisegment enhancement (tracking the nerve's course) help distinguish it from other "
            "temporal-bone and CPA lesions that do not follow the nerve's path."
        ),
        "why_wrong": [
            "Correct.",
            "Facial nerve schwannoma is defined by its ability to arise along and enlarge any facial-nerve "
            "segment, including but not limited to the IAC, with fallopian-canal involvement being characteristic.",
            "Focal bone erosion with exposed cartilage in the EAC is characteristic of EAC cholesteatoma, a "
            "different differential.",
            "Isolated mastoid opacification without a soft-tissue mass following the nerve's course would not "
            "characterize a schwannoma.",
        ],
        "board_pearl": "A facial-nerve-course-following pattern of smooth canal enlargement and multisegment "
        "enhancement is the key imaging discriminator for facial nerve schwannoma.",
        "curveball": "What determines the choice of management when intervention is chosen?",
        "curveball_answer": (
            "Options -- decompression, nerve-sparing debulking in selected anatomy, radiosurgery, or resection with "
            "primary repair, grafting, or nerve transfer -- are individualized by growth, symptoms, hearing, "
            "tumor location, patient age, and goals, always weighing the facial-function tradeoff of intervention."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-ansd-01",
        "domain": "Otology / Neurotology",
        "topic": "Auditory Neuropathy Spectrum Disorder",
        "stem": (
            "An infant with a history of prematurity and hyperbilirubinemia has speech understanding that is "
            "disproportionately poor relative to behavioral audiometric thresholds. Testing shows a present "
            "cochlear microphonic with an absent auditory brainstem response. What is the diagnosis and underlying "
            "mechanism?"
        ),
        "choices": [
            "Sensorineural hearing loss from outer-hair-cell damage alone",
            "Auditory neuropathy spectrum disorder: outer-hair-cell function is preserved while inner-hair-cell, "
            "synaptic, or auditory-nerve transmission is dys-synchronous",
            "Conductive hearing loss from middle-ear effusion",
            "Normal auditory function with a technical testing artifact",
        ],
        "answer": 1,
        "explanation": (
            "This is the signature pattern of auditory neuropathy spectrum disorder (ANSD): a present cochlear "
            "microphonic and/or otoacoustic emissions (reflecting preserved outer-hair-cell function) with an "
            "absent or markedly abnormal ABR (reflecting dys-synchronous inner-hair-cell, synaptic, or "
            "auditory-nerve transmission). Prematurity, hyperbilirubinemia, neuropathy, and family history are "
            "recognized risk factors."
        ),
        "why_wrong": [
            "Outer-hair-cell function is preserved in ANSD, which is the opposite pattern from isolated "
            "outer-hair-cell sensorineural loss.",
            "Correct.",
            "A present cochlear microphonic with disproportionately poor speech understanding reflects a neural "
            "transmission problem, not a conductive middle-ear process.",
            "This is a recognized, reproducible diagnostic pattern, not an artifact -- OAEs may disappear over "
            "time, so serial testing matters.",
        ],
        "board_pearl": "ANSD's signature is preserved cochlear receptor activity (present OAE/cochlear microphonic) "
        "with disordered neural synchrony (absent/abnormal ABR) -- lesion site strongly affects rehabilitation "
        "prognosis.",
        "curveball": "Does a single audiogram predict whether this child will benefit from hearing aids?",
        "curveball_answer": (
            "No -- thresholds alone do not predict benefit. Management is early language access with individualized "
            "hearing-aid or remote-microphone trials and close functional monitoring; escalate based on functional "
            "speech-language progress, not a single audiogram."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-ansd-02",
        "domain": "Otology / Neurotology",
        "topic": "Auditory Neuropathy Spectrum Disorder",
        "stem": (
            "A child with confirmed ANSD has failed an adequate trial of appropriately fitted amplification with "
            "poor speech-language progress. The family and team are considering cochlear implantation. What should "
            "be confirmed first, and why?"
        ),
        "choices": [
            "Nothing further is needed; proceed directly to implantation since amplification failed",
            "Confirm cochlear-nerve integrity with MRI, because severe cochlear-nerve deficiency predicts limited "
            "CI benefit and may prompt auditory-brainstem-implant evaluation in selected centers",
            "Repeat the ABR only, since OAEs are not useful once ANSD is diagnosed",
            "Confirm normal outer-hair-cell function, since that is the main predictor of CI benefit in ANSD",
        ],
        "answer": 1,
        "explanation": (
            "Cochlear implantation should be considered when appropriately fitted amplification fails to support "
            "speech and language, but cochlear-nerve integrity should be confirmed first: severe cochlear-nerve "
            "deficiency predicts limited CI benefit and may prompt auditory-brainstem-implant evaluation in "
            "selected centers."
        ),
        "why_wrong": [
            "Cochlear-nerve integrity should be confirmed before proceeding, since severe deficiency changes the "
            "expected benefit and may redirect care toward ABI evaluation.",
            "Correct.",
            "OAEs remain relevant since they may disappear over time; the key confirmatory step for CI candidacy "
            "specifically is imaging of the cochlear nerves.",
            "Outer-hair-cell function is preserved in ANSD by definition and is not the limiting factor for CI "
            "benefit; cochlear-nerve status is the key predictor.",
        ],
        "board_pearl": "Before cochlear implantation in ANSD, confirm cochlear-nerve integrity by MRI -- severe "
        "nerve deficiency limits expected CI benefit and may warrant ABI evaluation instead.",
        "curveball": "What workup elements, beyond ABR/OAE, support the ANSD evaluation?",
        "curveball_answer": (
            "Behavioral audiology, speech perception testing, genetics evaluation, and MRI of the cochlear nerves, "
            "in addition to confirming the present cochlear microphonic/OAE with absent or markedly abnormal ABR."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-vernet-01",
        "domain": "Otology / Neurotology",
        "topic": "Vernet Syndrome (Jugular Foramen Syndrome)",
        "stem": (
            "A patient has ipsilateral loss of gag reflex and posterior-tongue taste, hoarseness with vocal-fold "
            "paralysis, dysphagia, and shoulder droop with weak head-turn to the opposite side. Tongue strength and "
            "protrusion are normal. Where does this lesion localize?"
        ),
        "choices": [
            "The hypoglossal canal alone",
            "The jugular foramen, affecting CN IX, X, and XI, which exit the skull base together, while CN XII "
            "exits separately and is spared",
            "The cavernous sinus",
            "The orbital apex",
        ],
        "answer": 1,
        "explanation": (
            "This is Vernet syndrome: CN IX (gag/taste), X (hoarseness/vocal-fold paralysis/dysphagia), and XI "
            "(trapezius/sternocleidomastoid weakness) exit together through the jugular foramen. CN XII is spared "
            "because it exits separately through the hypoglossal canal -- its involvement would instead define "
            "Collet-Sicard syndrome."
        ),
        "why_wrong": [
            "The hypoglossal canal carries CN XII, which is explicitly spared here (normal tongue strength).",
            "Correct.",
            "Cavernous sinus syndrome affects CN III, IV, VI, V1, V2, not the IX-XI combination described here.",
            "Orbital apex syndrome affects vision and CN II, III, IV, VI, V1 -- not the lower cranial nerves IX-XI.",
        ],
        "board_pearl": "Build the lower-cranial-nerve syndrome ladder: IX+X+XI at the jugular foramen = Vernet. Add "
        "XII (hypoglossal canal) = Collet-Sicard. Add Horner syndrome from retroparotid sympathetic-chain "
        "involvement = Villaret.",
        "curveball": "What is the most common cause, and what must be done before biopsy?",
        "curveball_answer": (
            "Typical causes are glomus jugulare paraganglioma, lower-cranial-nerve schwannoma, metastasis, or "
            "skull-base meningioma. Vascular imaging is mandatory before biopsying a suspected paraganglioma, given "
            "its hypervascularity."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-vernet-02",
        "domain": "Otology / Neurotology",
        "topic": "Vernet Syndrome (Jugular Foramen Syndrome)",
        "stem": (
            "An elderly, comorbid patient is found to have a small, slow-growing jugular foramen mass with "
            "preserved lower-cranial-nerve function. What is an appropriate initial management option, "
            "and why?"
        ),
        "choices": [
            "Immediate surgical resection regardless of symptoms, since any jugular foramen mass must be removed",
            "Observation is a reasonable option for small, asymptomatic, slow-growing lesions, especially in older "
            "or comorbid patients, since resection risks worsening existing lower-cranial-neuropathy",
            "Radiosurgery is contraindicated in Vernet syndrome",
            "No imaging or specialist referral is needed once the cranial nerve pattern is recognized",
        ],
        "answer": 1,
        "explanation": (
            "Management is decided between observation (favored for small, asymptomatic, slow-growing lesions, "
            "especially in older or comorbid patients, since resection risks worsening existing "
            "lower-cranial-neuropathy), stereotactic radiosurgery, or surgical resection, based on lesion type, "
            "growth, and symptom burden."
        ),
        "why_wrong": [
            "Reflexive resection is not indicated for every jugular foramen mass; observation is appropriate for "
            "selected small, asymptomatic, slow-growing lesions.",
            "Correct.",
            "Radiosurgery is one of the three options considered (alongside observation and surgery), not "
            "contraindicated.",
            "Contrast MRI/MRA/CTA of the skull base is needed to characterize the mass and vascularity, and "
            "multidisciplinary evaluation is standard.",
        ],
        "board_pearl": "Resection of a jugular foramen lesion can worsen existing lower-cranial-nerve deficits -- "
        "weigh that risk explicitly against observation or radiosurgery, especially in older or comorbid patients.",
        "curveball": "What perioperative issues must be planned for if resection is chosen?",
        "curveball_answer": (
            "Protect the remaining lower cranial nerves and the jugular bulb/sigmoid sinus, and plan for "
            "perioperative airway/aspiration management (possible vocal-fold medialization, feeding plan) since "
            "resection can worsen voice and swallow function."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-gradenigo-01",
        "domain": "Otology / Neurotology",
        "topic": "Gradenigo Syndrome (Petrous Apicitis)",
        "stem": (
            "A child recovering from acute otitis media develops otorrhea, retro-orbital pain in a V1 distribution, "
            "and new diplopia with inability to abduct one eye. What is the diagnosis and anatomic explanation?"
        ),
        "choices": [
            "Cavernous sinus syndrome, from direct cavernous sinus thrombosis",
            "Gradenigo syndrome: infection tracking from the middle ear/mastoid into the petrous apex compresses "
            "CN VI in Dorello canal, with adjacent trigeminal (V1) involvement",
            "Orbital apex syndrome, from invasive fungal sinusitis",
            "Isolated CN III palsy from uncal herniation",
        ],
        "answer": 1,
        "explanation": (
            "This is the classic Gradenigo triad: otorrhea/otitis media, V1-distribution facial pain, and isolated "
            "CN VI (abducens) palsy. CN VI travels through Dorello canal beneath the petroclinoid ligament "
            "immediately adjacent to the petrous apex, so petrous apicitis compresses/irritates it; adjacent "
            "trigeminal ganglion/Meckel cave involvement produces the facial pain."
        ),
        "why_wrong": [
            "Cavernous sinus syndrome would typically affect multiple cranial nerves (III, IV, VI, V1, V2 ± "
            "Horner), not an isolated CN VI palsy with this specific otogenic source.",
            "Correct.",
            "Orbital apex syndrome adds vision loss/CN II involvement and ophthalmoplegia from multiple nerves, "
            "which is not described here, and its classic trigger is invasive fungal disease in an "
            "immunocompromised/DKA patient, not a post-otitis picture.",
            "Isolated CN III palsy is not the pattern described, and uncal herniation is unrelated to this otogenic "
            "presentation.",
        ],
        "board_pearl": "Otorrhea + retro-orbital (V1) pain + isolated CN VI palsy after otitis media/mastoiditis = "
        "Gradenigo syndrome -- specifically the abducens nerve because Dorello canal is the anatomic bottleneck at "
        "the petrous apex, distinguishing it from orbital apex or cavernous sinus syndrome.",
        "curveball": "What is the initial management approach?",
        "curveball_answer": (
            "Start IV antibiotics targeting the causative otitis media/mastoiditis organism and obtain source "
            "control with myringotomy and tube placement for drainage and culture. A well-aerated petrous apex "
            "system may resolve with medical management and close monitoring; failure to improve, abscess, or "
            "significant apicitis warrants surgical drainage."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    # ---------------- Rhinology / Allergy / Skull Base ----------------
    {
        "id": "v431-empty-nose-syndrome-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Empty Nose Syndrome",
        "stem": (
            "A patient several years after aggressive turbinate resection reports a paradoxical sensation of nasal "
            "obstruction and suffocation despite a wide-open nasal airway on exam. What is the most appropriate "
            "initial approach?"
        ),
        "choices": [
            "Dismiss the symptoms as purely psychiatric since the airway is objectively open",
            "Validate the symptoms, begin humidification/saline/emollients, evaluate and coordinate treatment of "
            "sleep and mental-health comorbidity, and set realistic expectations while working up the diagnosis",
            "Proceed immediately to revision turbinate/lateral-wall augmentation surgery",
            "Order no further testing since a wide-open airway rules out empty nose syndrome",
        ],
        "answer": 1,
        "explanation": (
            "Empty nose syndrome (ENS) should be considered after turbinate surgery when paradoxical obstruction, "
            "suffocation sensation, dryness, or crusting occurs despite a visibly open airway. It is a multifactorial "
            "neurosensory/airflow disorder; initial management validates the symptoms, begins humidification/saline/"
            "emollients, and coordinates treatment of common sleep and mental-health comorbidity while excluding "
            "other contributors -- not dismissing the complaint or rushing to surgery."
        ),
        "why_wrong": [
            "Psychological comorbidity should be treated without dismissing the nasal symptoms -- ENS is a "
            "recognized, multifactorial diagnosis, not merely psychiatric.",
            "Correct.",
            "Surgery is reserved for selected patients with consistent symptoms and temporary cotton-test "
            "improvement; evidence and durability are variable, so it is not the first step.",
            "A wide nasal cavity does not prove adequate nasal function and does not rule out ENS -- that is the "
            "paradox that defines the syndrome.",
        ],
        "board_pearl": "A wide cavity does not prove adequate nasal function. Prevention favors mucosa-preserving "
        "turbinate surgery in the first place.",
        "curveball": "What workup tools support (though do not definitively confirm) the diagnosis?",
        "curveball_answer": (
            "Operative history, endoscopy, the ENS6Q questionnaire, mucosal assessment, and a carefully interpreted "
            "cotton test, while excluding inflammatory, structural, neurologic, sleep, and psychiatric contributors "
            "-- no single test is definitive."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-empty-nose-syndrome-02",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Empty Nose Syndrome",
        "stem": "What is the proposed underlying mechanism of empty nose syndrome, and what is the single most important prevention strategy?",
        "choices": [
            "Simple mechanical obstruction from scar tissue; prevention is avoiding any turbinate surgery entirely",
            "Loss of turbinate mucosa and airflow sensation with altered nasal aerodynamics, a multifactorial "
            "neurosensory and airflow disorder rather than fixed stenosis; prevention favors mucosa-preserving "
            "turbinate surgery",
            "An infectious process requiring long-term antibiotics for prevention",
            "A purely anatomic finding that always resolves spontaneously without intervention",
        ],
        "answer": 1,
        "explanation": (
            "Loss of turbinate mucosa and airflow sensation, plus altered nasal aerodynamics, are proposed "
            "contributors -- it is a multifactorial neurosensory and airflow disorder rather than fixed stenosis. "
            "Prevention favors mucosa-preserving turbinate surgery rather than aggressive resection."
        ),
        "why_wrong": [
            "ENS is not simple mechanical scar obstruction, and complete avoidance of turbinate surgery is not the "
            "recommended prevention strategy -- mucosa preservation is.",
            "Correct.",
            "ENS is not an infectious process and is not prevented or treated with antibiotics.",
            "ENS is a chronic, often distressing condition that does not reliably resolve spontaneously.",
        ],
        "board_pearl": "Prevention beats treatment for ENS: preserve turbinate mucosa during surgery rather than "
        "relying on later revision options, whose evidence and durability are variable.",
        "curveball": "If a patient has temporary symptom improvement with a cotton test, does that guarantee surgical success?",
        "curveball_answer": (
            "No -- selected patients with consistent symptoms and temporary cotton-test improvement may be "
            "considered for turbinate or lateral-wall augmentation, but evidence and durability are variable and "
            "revision requires careful consent."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-silent-sinus-syndrome-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Silent Sinus Syndrome",
        "stem": (
            "A patient presents with painless, progressive unilateral enophthalmos and hypoglobus, with no history "
            "of trauma and minimal sinonasal complaints. CT shows an opacified, contracted maxillary sinus with a "
            "retracted uncinate process and a depressed orbital floor. What is the diagnosis and mechanism?"
        ),
        "choices": [
            "Orbital blowout fracture from unrecognized trauma",
            "Silent sinus syndrome: chronic maxillary outflow obstruction produces negative pressure, maxillary "
            "atelectasis, and inferior bowing of the orbital floor, increasing orbital volume",
            "An expansile maxillary mucocele causing outward globe displacement",
            "Orbital cellulitis with abscess",
        ],
        "answer": 1,
        "explanation": (
            "This is silent sinus syndrome: chronic maxillary outflow obstruction causes negative intrasinus "
            "pressure, progressive maxillary sinus atelectasis (volume loss, not expansion), and inferior bowing of "
            "the orbital floor, increasing orbital volume and causing painless enophthalmos/hypoglobus without a "
            "trauma history."
        ),
        "why_wrong": [
            "No trauma history is present, and the imaging pattern (atelectatic, opacified sinus with retracted "
            "uncinate) is distinct from a blowout fracture.",
            "Correct.",
            "A mucocele is expansile and would increase sinus volume, not contract it -- silent sinus syndrome "
            "specifically shows sinus volume LOSS, the opposite pattern.",
            "There is no described history of infection, fever, or orbital inflammation consistent with cellulitis "
            "or abscess.",
        ],
        "board_pearl": "Unexplained painless enophthalmos is sometimes a sinus diagnosis, not a primary orbital or "
        "traumatic one -- distinguish silent sinus syndrome's volume LOSS from an expansile mucocele, neoplasm, or "
        "post-traumatic deformity on imaging.",
        "curveball": "What is the appropriate treatment sequence?",
        "curveball_answer": (
            "Endoscopic uncinectomy and maxillary antrostomy restore ventilation of the obstructed sinus; "
            "orbital-floor reconstruction may be performed simultaneously or staged depending on deformity, "
            "diplopia, severity, and expected remodeling after re-aeration. Medical therapy may address concurrent "
            "inflammation but does not reverse established atelectasis or orbital-volume change."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-silent-sinus-syndrome-02",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Silent Sinus Syndrome",
        "stem": "Why is silent sinus syndrome called 'silent,' and how does this affect the diagnostic approach?",
        "choices": [
            "Because patients are typically asymptomatic from a sinonasal standpoint, with the orbital finding "
            "(enophthalmos/hypoglobus) being the presenting complaint rather than sinus pain or congestion",
            "Because the diagnosis can only be made on a silent (unenhanced) MRI sequence",
            "Because it never causes any imaging abnormality",
            "Because it is asymptomatic and never requires treatment",
        ],
        "answer": 0,
        "explanation": (
            "The syndrome is 'silent' because it lacks prominent sinus symptoms -- the presenting complaint is "
            "typically the orbital finding (painless progressive enophthalmos or hypoglobus), which should raise "
            "concern for this diagnosis even without sinus pain or congestion."
        ),
        "why_wrong": [
            "Correct.",
            "The diagnosis relies on sinus/orbital CT findings (opacified, contracted maxillary sinus, retracted "
            "uncinate, depressed orbital floor), not a specific MRI sequence.",
            "The syndrome has a characteristic, reliably visible CT abnormality -- it is 'silent' clinically, not "
            "radiographically.",
            "Treatment (endoscopic sinus surgery ± orbital reconstruction) is indicated once the diagnosis is "
            "established; it is not left untreated simply because sinus symptoms are minimal.",
        ],
        "board_pearl": "Coordinate rhinology and ophthalmic evaluation whenever silent sinus syndrome is suspected "
        "-- the orbital finding, not a sinus complaint, is usually what brings the patient in.",
        "curveball": "How is this distinguished from a maxillary mucocele or neoplasm on imaging?",
        "curveball_answer": (
            "Silent sinus syndrome shows sinus volume LOSS (atelectasis, contraction) with a retracted uncinate, "
            "whereas a mucocele is expansile and neoplasm typically shows a mass with possible bone destruction -- "
            "distinguishing volume loss from expansile or destructive processes is central to the imaging workup."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-endoscopic-pituitary-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Endoscopic Pituitary / Anterior Skull Base Approach",
        "stem": (
            "During a planned endoscopic transsphenoidal approach to a sellar lesion with an expected high-flow CSF "
            "leak, what should be planned before dural entry?"
        ),
        "choices": [
            "Nothing specific; reconstruction can be improvised after the leak is identified",
            "Carotid localization and multilayer closure planning, including preserving or harvesting a "
            "vascularized nasoseptal flap when a high-flow leak is plausible",
            "Automatic conversion to an open craniotomy approach",
            "Deferring endocrinology involvement until after surgery",
        ],
        "answer": 1,
        "explanation": (
            "The endonasal corridor is bounded by the carotids and cavernous sinuses laterally, the optic apparatus "
            "superiorly, and the clivus posteriorly. Plan carotid localization and multilayer closure before dural "
            "entry, and preserve or harvest a vascularized nasoseptal flap when a high-flow leak is plausible -- "
            "durable CSF-leak prevention and carotid safety are part of surgical success, not an afterthought."
        ),
        "why_wrong": [
            "Reconstruction planning, including flap harvest, should be anticipated before dural entry, not "
            "improvised afterward.",
            "Correct.",
            "The endoscopic corridor is chosen specifically to avoid a craniotomy when appropriate for the lesion; "
            "conversion is not automatic.",
            "This is a team operation -- endocrinology involvement (optimizing endocrine deficits, pituitary "
            "testing) is part of preoperative planning, not deferred.",
        ],
        "board_pearl": "Success in endoscopic pituitary/skull-base surgery includes endocrine and visual outcomes, "
        "carotid safety, and durable CSF-leak prevention -- not merely tumor removal.",
        "curveball": "Who is responsible for which part of the operation?",
        "curveball_answer": (
            "The rhinologist creates the corridor and reconstruction while neurosurgery treats the lesion -- this "
            "is explicitly a team operation."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-endoscopic-pituitary-02",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Endoscopic Pituitary / Anterior Skull Base Approach",
        "stem": (
            "A patient is found to have an incidental, small, noncompressive, nonfunctioning sellar lesion. A "
            "separate patient has a large prolactinoma. What is the most appropriate initial management for each?"
        ),
        "choices": [
            "Immediate endoscopic resection for both lesions",
            "Observation for the appropriate incidental noncompressive lesion; disease-specific medical therapy "
            "(dopamine agonists) as first-line for most prolactinomas, optimizing endocrine deficits before any "
            "surgery",
            "Radiation therapy alone for both, without surgical or medical evaluation",
            "No further workup or follow-up is needed for either lesion",
        ],
        "answer": 1,
        "explanation": (
            "Not every lesion requires surgery. Appropriate incidental/noncompressive lesions can be observed, and "
            "disease-specific medical therapy such as dopamine agonists is used for most prolactinomas as first-line "
            "treatment; endocrine deficits should be optimized before any surgery is undertaken."
        ),
        "why_wrong": [
            "Not every sellar lesion requires resection -- prolactinomas in particular typically respond to medical "
            "therapy first.",
            "Correct.",
            "Radiation is not the default first-line approach for either scenario described; medical therapy and "
            "observation are appropriate here.",
            "Dedicated MRI, complete pituitary testing, formal visual assessment when indicated, and "
            "multidisciplinary review are part of standard workup and follow-up for sellar lesions.",
        ],
        "board_pearl": "Sellar lesions are not uniformly surgical -- prolactinomas are the classic example of a "
        "pituitary tumor managed medically first, and observation is appropriate for select incidental findings.",
        "curveball": "What symptoms might prompt evaluation of a sellar/skull-base lesion in the first place?",
        "curveball_answer": (
            "Endocrine excess or failure, visual-field loss, cranial neuropathy, headache, or an incidental imaging "
            "finding."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-orbital-apex-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Orbital Apex Syndrome",
        "stem": (
            "A patient with poorly controlled diabetes presents in diabetic ketoacidosis with facial pain, "
            "ophthalmoplegia, and new vision loss. Nasal endoscopy shows dusky, nonviable-appearing turbinate "
            "mucosa. What is the most appropriate next step?"
        ),
        "choices": [
            "Obtain outpatient MRI in 1-2 weeks once the patient's glucose is better controlled",
            "Immediate bedside biopsy of the nonviable mucosa for frozen section and fungal stain, with emergent "
            "correction of the underlying DKA, systemic antifungal therapy, and urgent surgical debridement for "
            "suspected invasive fungal sinusitis",
            "Reassurance and outpatient ophthalmology follow-up, since vision loss in DKA is usually self-limited",
            "Oral antibiotics only, with re-evaluation in 48-72 hours",
        ],
        "answer": 1,
        "explanation": (
            "In an immunocompromised or DKA patient with facial pain and eye findings, think invasive fungal "
            "sinusitis (mucormycosis or aspergillosis) until proven otherwise. This is an emergency: obtain "
            "immediate bedside nasal endoscopy with biopsy of any nonviable, dusky, or black-appearing mucosa for "
            "frozen section and fungal stain, and treat emergently with DKA correction, systemic antifungal "
            "therapy, and urgent surgical debridement. New vision loss is a surgical emergency, not an indication "
            "to wait for further imaging."
        ),
        "why_wrong": [
            "Delaying imaging and biopsy risks progression of a fulminant, life- and vision-threatening infection.",
            "Correct.",
            "Vision loss with ophthalmoplegia and V1 hypesthesia in this setting is not self-limited and demands "
            "emergent intervention.",
            "Oral antibiotics alone do not address suspected invasive fungal disease, which requires systemic "
            "antifungal therapy and surgical debridement.",
        ],
        "board_pearl": "Vision loss plus ophthalmoplegia plus V1 numbness localizes to the orbital apex, where the "
        "optic canal and superior orbital fissure converge -- this is the key discriminator from a pure superior "
        "orbital fissure or cavernous sinus syndrome.",
        "curveball": "How does orbital apex syndrome differ from superior orbital fissure syndrome and cavernous sinus syndrome anatomically?",
        "curveball_answer": (
            "Superior orbital fissure syndrome affects motility and sensory function (CN III, IV, VI, V1) with "
            "preserved vision, since the optic nerve runs through the separate optic canal. Cavernous sinus "
            "syndrome affects CN III, IV, VI, V1, V2 ± Horner, typically vision-sparing unless disease extends "
            "posteriorly. Orbital apex syndrome uniquely combines both compartments (optic canal + superior orbital "
            "fissure), so vision loss occurs alongside ophthalmoplegia."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-villaret-01",
        "domain": "Head & Neck Oncology",
        "topic": "Villaret Syndrome (Retroparotid Space Syndrome)",
        "stem": (
            "A patient has ipsilateral CN IX, X, XI, and XII palsies PLUS ptosis, miosis, and anhidrosis. Where "
            "does this lesion localize, and how does it differ from Collet-Sicard syndrome?"
        ),
        "choices": [
            "The jugular foramen alone, identical to Vernet syndrome",
            "The retroparotid (retrostyloid/poststyloid parapharyngeal) space, where the added Horner syndrome "
            "(sympathetic-chain injury) distinguishes Villaret from Collet-Sicard, which has the same IX-XII "
            "pattern without Horner syndrome",
            "The cavernous sinus",
            "The orbital apex",
        ],
        "answer": 1,
        "explanation": (
            "This is Villaret syndrome: Collet-Sicard syndrome (IX-XII) with the added finding of sympathetic-chain "
            "injury (Horner syndrome), which localizes the lesion to the retroparotid space -- containing the "
            "carotid sheath, cranial nerves IX-XII, and the cervical sympathetic chain -- rather than the jugular "
            "foramen or skull base alone."
        ),
        "why_wrong": [
            "Vernet syndrome involves only IX, X, and XI at the jugular foramen, with XII spared -- this patient "
            "has all four (IX-XII) plus Horner syndrome, which is neither Vernet nor jugular-foramen-only disease.",
            "Correct.",
            "Cavernous sinus syndrome affects CN III, IV, VI, V1, V2 ± Horner -- not the lower cranial nerves IX-XII "
            "described here.",
            "Orbital apex syndrome affects vision and CN II, III, IV, VI, V1, not the lower cranial nerve pattern "
            "described here.",
        ],
        "board_pearl": "Horner syndrome is the key discriminator that elevates a lower-cranial-nerve syndrome from "
        "Collet-Sicard to Villaret, because it means the sympathetic chain in the retroparotid space is also "
        "involved.",
        "curveball": "What must be done before needle biopsy of a suspected vascular lesion in this space?",
        "curveball_answer": (
            "Characterize vascularity with imaging before any needle biopsy of a suspected vascular lesion (e.g., "
            "vagal or sympathetic-chain schwannoma, paraganglioma), and counsel proactively for potential permanent "
            "multi-nerve deficits (voice, swallow, shoulder function, and oculosympathetic findings) if resection "
            "is planned."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    # ---------------- Head & Neck Oncology ----------------
    {
        "id": "v431-slnb-oral-cavity-01",
        "domain": "Head & Neck Oncology",
        "topic": "Sentinel Lymph Node Biopsy in Oral Cavity Cancer",
        "stem": (
            "Which patient is the most appropriate candidate for sentinel lymph node biopsy (SLNB) as a staging "
            "strategy for oral cavity squamous cell carcinoma?"
        ),
        "choices": [
            "A patient with a cT1-2, clinically node-negative (cN0) oral-cavity SCC evaluated within a validated "
            "multidisciplinary SLNB program",
            "A patient with an overtly clinically node-positive (cN+) neck",
            "A patient with a cT4 primary and multiple palpable nodes",
            "Any oral cavity SCC regardless of clinical stage or nodal status",
        ],
        "answer": 0,
        "explanation": (
            "SLNB is a staging option for selected early cT1-2 clinically node-negative oral-cavity SCC when "
            "performed within a validated multidisciplinary program; it is not used to stage an overtly "
            "node-positive neck."
        ),
        "why_wrong": [
            "Correct.",
            "SLNB is explicitly not used to stage an overtly node-positive neck.",
            "Advanced T-stage with palpable nodes is not the selected early cN0 population for whom SLNB is "
            "validated.",
            "SLNB has a specific, validated indication (early cT1-2 cN0) rather than universal applicability.",
        ],
        "board_pearl": "SLNB is staging, not primary-tumor treatment -- its safety depends on patient selection, "
        "mapping quality, pathology processing, and an experienced team.",
        "curveball": "What technical factor can complicate sentinel node localization specifically for floor-of-mouth primaries?",
        "curveball_answer": (
            "'Shine-through' from the injection site at the primary tumor can obscure or mimic sentinel node signal "
            "on lymphoscintigraphy for floor-of-mouth primaries, complicating localization."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-slnb-oral-cavity-02",
        "domain": "Head & Neck Oncology",
        "topic": "Sentinel Lymph Node Biopsy in Oral Cavity Cancer",
        "stem": (
            "A patient undergoes technically adequate SLNB for an early oral-cavity SCC, and the sentinel node is "
            "negative on step-sectioning and immunohistochemistry. What is the appropriate next step, and what is "
            "the alternative to SLNB when mapping expertise or pathology support is unavailable?"
        ),
        "choices": [
            "Proceed to elective neck dissection regardless of the negative SLNB result",
            "A negative, technically adequate SLNB can permit surveillance rather than further neck treatment; "
            "elective neck dissection remains a valid alternative to SLNB when mapping expertise, pathology "
            "support, or reliable follow-up is unavailable",
            "No further follow-up of any kind is needed once SLNB is negative",
            "SLNB findings do not affect management decisions either way",
        ],
        "answer": 1,
        "explanation": (
            "A negative, technically adequate SLNB can permit surveillance. Positive findings trigger pathology- "
            "and protocol-directed neck treatment and adjuvant decision-making rather than one automatic response "
            "for every deposit. Elective neck dissection remains a valid alternative to SLNB when mapping "
            "expertise, pathology support, or reliable follow-up is unavailable."
        ),
        "why_wrong": [
            "A technically adequate negative SLNB is meant to avoid unnecessary elective neck dissection, not "
            "trigger one regardless of result.",
            "Correct.",
            "Surveillance and continued follow-up are still required after a negative SLNB.",
            "SLNB findings directly guide subsequent neck management decisions.",
        ],
        "board_pearl": "SLNB's value depends on selection, mapping quality, pathology processing, and an "
        "experienced team -- elective neck dissection is the fallback when any of those elements is not reliably "
        "available.",
        "curveball": "How is a positive sentinel node result managed?",
        "curveball_answer": (
            "Positive findings trigger pathology- and protocol-directed neck treatment and adjuvant "
            "decision-making, individualized rather than following one automatic response for every nodal deposit."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    # ---------------- Thyroid / Parathyroid / Salivary ----------------
    {
        "id": "v431-subacute-thyroiditis-01",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "Subacute (de Quervain) Thyroiditis",
        "stem": (
            "A patient develops a painful, tender thyroid gland with fever and transient thyrotoxic symptoms two "
            "weeks after a viral-like illness. Radioactive iodine uptake is low. What is the diagnosis and best "
            "initial management?"
        ),
        "choices": [
            "Graves disease; start antithyroid drugs",
            "Subacute (de Quervain) granulomatous thyroiditis; treat pain with NSAIDs (corticosteroids for severe "
            "or refractory inflammation) and beta blockade for adrenergic symptoms, since antithyroid drugs do not "
            "help",
            "Hashimoto thyroiditis; start levothyroxine immediately",
            "Thyroid abscess; proceed directly to surgical drainage",
        ],
        "answer": 1,
        "explanation": (
            "Pain, high inflammatory markers, thyrotoxicosis, and LOW uptake form the classic pattern of subacute "
            "granulomatous thyroiditis -- this is destructive thyroiditis (inflammatory follicular disruption "
            "releasing stored hormone), not increased hormone synthesis, so antithyroid drugs do not help. Treat "
            "pain with NSAIDs, reserve corticosteroids for severe/refractory inflammation, and use beta blockade "
            "for adrenergic symptoms."
        ),
        "why_wrong": [
            "Graves disease characteristically shows HIGH radioactive iodine uptake, not low, and antithyroid "
            "drugs would not be expected to help a destructive process anyway.",
            "Correct.",
            "Hashimoto thyroiditis typically presents as a painless, firm, diffuse gland rather than an acutely "
            "painful, tender one following a viral illness.",
            "There is no description of a discrete abscess; surgery has no routine role in subacute thyroiditis "
            "unless the expected course fails or a persistent focal lesion/abscess/compressive progression develops.",
        ],
        "board_pearl": "Anticipate the thyrotoxic-to-hypothyroid-to-recovery sequence in subacute thyroiditis, and "
        "follow for the transient hypothyroid phase and uncommon permanent hypothyroidism.",
        "curveball": "When should surgery be reconsidered in a patient with presumed subacute thyroiditis?",
        "curveball_answer": (
            "There is no routine surgical role, but failure to follow the expected clinical course, a persistent "
            "focal lesion, concern for abscess, or compressive progression should reopen the diagnosis."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-hashimoto-thyroiditis-01",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "Hashimoto Thyroiditis",
        "stem": (
            "A patient with known Hashimoto thyroiditis and a diffusely heterogeneous gland on ultrasound is found "
            "to have a new dominant nodule with rapid growth. What is the most appropriate next step?"
        ),
        "choices": [
            "Attribute the finding to Hashimoto thyroiditis and continue routine antibody monitoring only",
            "Risk-stratify the focal finding on its own merits and evaluate urgently for lymphoma, often with core "
            "biopsy and flow/cytogenetic studies, since lymphoma is primarily treated nonsurgically",
            "Proceed directly to total thyroidectomy without further workup",
            "No imaging or biopsy is needed since diffuse heterogeneity alone is an FNA indication",
        ],
        "answer": 1,
        "explanation": (
            "Do not dismiss a dominant nodule or rapidly growing mass as 'just Hashimoto' -- risk-stratify the "
            "focal finding on its own merits. Rapid enlargement in a Hashimoto gland warrants urgent lymphoma "
            "evaluation, often with core biopsy and flow/cytogenetic studies, because lymphoma is primarily treated "
            "nonsurgically."
        ),
        "why_wrong": [
            "A new dominant, rapidly growing nodule should not be attributed to the background diagnosis without "
            "independent evaluation; repeatedly measuring antibodies is not the appropriate response to a new "
            "focal finding.",
            "Correct.",
            "Surgery is reserved for selected compressive goiter or independently suspicious disease -- rapid "
            "enlargement specifically should first prompt lymphoma evaluation (often nonsurgical), not "
            "thyroidectomy.",
            "Diffuse heterogeneity alone is not an FNA indication; a discrete, suspicious, or rapidly growing focal "
            "lesion is a different situation warranting targeted evaluation.",
        ],
        "board_pearl": "Rapid enlargement in a background of Hashimoto thyroiditis should trigger urgent lymphoma "
        "workup -- thyroid lymphoma is primarily a nonsurgical diagnosis and treatment, so core biopsy with "
        "flow/cytogenetics (not reflexive surgery) is the key next step.",
        "curveball": "What labs and imaging support the baseline diagnosis of Hashimoto thyroiditis?",
        "curveball_answer": (
            "TSH and free T4 define thyroid function; anti-TPO antibodies support the diagnosis. Ultrasound "
            "characterizes the gland or a true nodule, but diffuse heterogeneity alone is not an FNA indication."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-ebsln-injury-01",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "External Branch of the Superior Laryngeal Nerve Injury",
        "stem": (
            "A professional singer undergoes thyroidectomy. Postoperatively, vocal-fold motion is grossly normal on "
            "laryngoscopy, but the patient reports loss of high pitch, projection, and vocal endurance. What is the "
            "most likely diagnosis, and what confirmatory test is most specific when the result will change "
            "management?"
        ),
        "choices": [
            "Recurrent laryngeal nerve paralysis; confirm with videostroboscopy alone",
            "External branch of the superior laryngeal nerve (EBSLN) injury; cricothyroid laryngeal EMG is the "
            "most specific confirmatory test when it will change counseling or treatment",
            "Normal postoperative course; no further evaluation is needed since vocal-fold motion is normal",
            "Laryngopharyngeal reflux; start empiric PPI therapy",
        ],
        "answer": 1,
        "explanation": (
            "EBSLN injury should be suspected when there is loss of high pitch, projection, and vocal endurance "
            "with PRESERVED gross vocal-fold motion, especially in a professional voice user -- normal vocal-fold "
            "motion does not exclude laryngeal nerve injury. The EBSLN powers cricothyroid tension; injury changes "
            "pitch control without the classic finding of recurrent laryngeal nerve paralysis. Stroboscopy may show "
            "subtle asymmetry but is not diagnostic; cricothyroid laryngeal EMG is the most specific confirmatory "
            "test when the result will change counseling or treatment."
        ),
        "why_wrong": [
            "Recurrent laryngeal nerve paralysis would be expected to cause abnormal vocal-fold motion, which is "
            "not present here; stroboscopy alone is also not diagnostic for EBSLN injury.",
            "Correct.",
            "A normal 'gross' exam does not exclude EBSLN injury -- pitch, projection, and endurance complaints in "
            "a professional voice user after neck surgery warrant specific evaluation.",
            "The clinical picture (post-thyroidectomy voice change in a professional voice user with normal fold "
            "motion) points to EBSLN injury, not reflux, as the most likely explanation.",
        ],
        "board_pearl": "Normal vocal-fold motion does not exclude laryngeal nerve injury -- always ask about high "
        "notes, projection, fatigue, and occupational voice demands after thyroid/neck surgery.",
        "curveball": "How can EBSLN injury be prevented during thyroidectomy?",
        "curveball_answer": (
            "Prevention requires capsular upper-pole dissection, individual vessel control, and "
            "visual/monitoring-assisted nerve preservation when feasible, since the EBSLN courses variably near the "
            "superior thyroid pedicle."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-subacute-thyroiditis-02",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "Subacute (de Quervain) Thyroiditis",
        "stem": "What is the expected clinical course of subacute (de Quervain) thyroiditis over time?",
        "choices": [
            "A single, permanent hyperthyroid phase with no resolution",
            "A thyrotoxic phase (from destructive release of stored hormone), followed by a transient hypothyroid "
            "phase, followed by recovery -- with uncommon permanent hypothyroidism",
            "Immediate, permanent hypothyroidism from the first presentation",
            "No change in thyroid function at any point during the illness",
        ],
        "answer": 1,
        "explanation": (
            "Anticipate the thyrotoxic-to-hypothyroid-to-recovery sequence: inflammatory follicular disruption "
            "initially releases stored hormone (thyrotoxic phase), followed by a transient hypothyroid phase as "
            "stores are depleted, then recovery in most patients; permanent hypothyroidism is uncommon but should "
            "be monitored for."
        ),
        "why_wrong": [
            "The hyperthyroid phase is transient, driven by destructive release rather than increased synthesis, "
            "and is followed by a hypothyroid phase and recovery.",
            "Correct.",
            "The initial phase is thyrotoxic, not hypothyroid, reflecting release of preformed stored hormone.",
            "Thyroid function characteristically changes through a recognizable multiphase course.",
        ],
        "board_pearl": "Pain, high inflammatory markers, thyrotoxicosis, and low radioactive iodine uptake form the "
        "classic pattern; follow patients through the expected multiphase course.",
        "curveball": "What determines whether corticosteroids should be used instead of NSAIDs?",
        "curveball_answer": (
            "Corticosteroids are reserved for severe or refractory inflammation, with NSAIDs as first-line pain "
            "treatment; beta blockade addresses adrenergic thyrotoxic symptoms, and antithyroid drugs are not "
            "useful since this is destructive, not synthetic, thyrotoxicosis."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-hashimoto-thyroiditis-02",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "Hashimoto Thyroiditis",
        "stem": "What is the underlying pathophysiology of Hashimoto thyroiditis, and what workup best defines thyroid function and supports the diagnosis?",
        "choices": [
            "Acute bacterial infection of the thyroid; blood cultures confirm the diagnosis",
            "Chronic autoimmune lymphocytic injury progressively destroying follicles, producing goitrous or "
            "atrophic disease; TSH and free T4 define function, with anti-TPO antibodies supporting the diagnosis",
            "A destructive process triggered only by viral illness, identical to subacute thyroiditis",
            "A purely anatomic finding with no relevant laboratory correlate",
        ],
        "answer": 1,
        "explanation": (
            "Hashimoto thyroiditis is chronic autoimmune lymphocytic injury that progressively destroys thyroid "
            "follicles and may produce goitrous or atrophic disease. TSH and free T4 define function; anti-TPO "
            "antibodies support the diagnosis, though ultrasound is used to characterize a gland or true nodule "
            "rather than diffuse heterogeneity alone."
        ),
        "why_wrong": [
            "Hashimoto thyroiditis is autoimmune, not an acute bacterial infection; blood cultures are not relevant.",
            "Correct.",
            "Subacute thyroiditis follows a viral-like illness with a painful, tender gland; Hashimoto is a chronic "
            "autoimmune process with a distinct (usually painless) presentation.",
            "TSH, free T4, and anti-TPO antibodies are directly relevant laboratory correlates.",
        ],
        "board_pearl": "Use levothyroxine for overt hypothyroidism and individualize subclinical disease treatment; "
        "monitor clinically and evaluate new focal or rapid enlargement rather than repeatedly measuring antibodies.",
        "curveball": "When is surgery indicated in Hashimoto thyroiditis?",
        "curveball_answer": (
            "Surgery is reserved for selected compressive goiter or independently suspicious disease -- not for the "
            "diffuse autoimmune process itself."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-ebsln-injury-02",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "External Branch of the Superior Laryngeal Nerve Injury",
        "stem": "What is the appropriate management approach for a patient with confirmed isolated EBSLN injury after thyroidectomy?",
        "choices": [
            "A standard restorative nerve-repair operation exists and should be offered to every patient",
            "There is no standard restorative operation for isolated EBSLN injury; use observation and voice "
            "therapy for compensation, projection, and safe vocal loading, since recovery and functional impact vary",
            "Immediate revision thyroidectomy to explore and repair the nerve",
            "No treatment or counseling is useful; the patient should be told nothing can be done",
        ],
        "answer": 1,
        "explanation": (
            "No standard restorative operation exists for isolated EBSLN injury. Management is observation and "
            "voice therapy for compensation, projection, and safe vocal loading; recovery and functional impact "
            "vary between patients."
        ),
        "why_wrong": [
            "No standard restorative operation exists for this specific isolated nerve injury.",
            "Correct.",
            "Revision surgery is not the standard management approach for isolated EBSLN injury.",
            "Voice therapy offers real functional benefit through compensation strategies, so patients should be "
            "counseled and offered therapy rather than told nothing can be done.",
        ],
        "board_pearl": "Prevention (capsular upper-pole dissection, individual vessel control, and "
        "visual/monitoring-assisted nerve preservation) matters because there is no standard restorative operation "
        "once EBSLN injury has occurred.",
        "curveball": "What symptoms should specifically be asked about in a professional voice user after neck surgery?",
        "curveball_answer": (
            "Ask about high notes, projection, fatigue, and occupational voice demands -- normal vocal-fold motion "
            "does not exclude laryngeal nerve injury."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    # ---------------- Pediatric Otolaryngology ----------------
    {
        "id": "v431-pierre-robin-01",
        "domain": "Pediatric Otolaryngology",
        "topic": "Pierre Robin Sequence",
        "stem": (
            "A newborn has micrognathia, glossoptosis, and a U-shaped cleft palate with significant feeding "
            "difficulty and intermittent upper-airway obstruction. What is the underlying mechanism of the airway "
            "obstruction, and what is the first management priority?"
        ),
        "choices": [
            "Primary laryngeal obstruction from vocal fold immobility; priority is immediate tracheostomy",
            "Tongue-base (not primary laryngeal) obstruction from mandibular hypoplasia displacing the tongue "
            "posteriorly; priority is a multidisciplinary pathway addressing airway and nutrition first, using "
            "monitored positioning, feeding support, and nasopharyngeal airway or noninvasive support as needed",
            "Fixed subglottic stenosis; priority is balloon dilation",
            "This is a purely cosmetic finding with no airway implications",
        ],
        "answer": 1,
        "explanation": (
            "Mandibular hypoplasia displaces the tongue posteriorly, producing tongue-base (not primary laryngeal) "
            "obstruction, and may impede palatal fusion. Management follows a multidisciplinary pathway: "
            "specialist-directed monitored positioning, feeding support, and nasopharyngeal airway or noninvasive "
            "support when appropriate -- treat airway and nutrition first before addressing the palate."
        ),
        "why_wrong": [
            "The obstruction is tongue-base in origin, not primary laryngeal, and tracheostomy is reserved for "
            "persistent significant obstruction after evaluation, not an automatic first step.",
            "Correct.",
            "Pierre Robin sequence is not defined by fixed subglottic stenosis; its obstruction is tongue-base and "
            "positional/dynamic in nature.",
            "Severity ranges from feeding difficulty to life-threatening obstruction -- this is not a cosmetic-only "
            "finding.",
        ],
        "board_pearl": "Treat airway and nutrition first in Pierre Robin sequence -- quantify obstruction and "
        "identify multilevel/syndromic disease before choosing a tongue, mandible, or tracheostomy solution; "
        "palate repair follows airway and growth stabilization.",
        "curveball": "What surgical options exist for persistent significant obstruction, and how are they chosen?",
        "curveball_answer": (
            "Mandibular distraction, tongue-lip adhesion, or tracheostomy, selected by obstruction level, "
            "comorbidity, and institutional expertise -- isolated and syndromic (e.g., Stickler) forms of Pierre "
            "Robin sequence differ in prognosis and should be evaluated for based on phenotype and genetics."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-nasal-dermoid-01",
        "domain": "Pediatric Otolaryngology",
        "topic": "Nasal Dermoid Cyst",
        "stem": (
            "An infant has a congenital midline nasal dorsal pit with a tuft of hair and intermittent sebaceous "
            "drainage. What is the most appropriate next step, and what must be avoided?"
        ),
        "choices": [
            "Office biopsy of the pit to confirm the diagnosis before any imaging",
            "Image before biopsy -- MRI best evaluates intracranial/dural extension, with thin-cut CT added "
            "selectively for bony detail that changes operative planning; avoid blind probing or office biopsy",
            "Reassurance only, since midline nasal pits are never associated with intracranial extension",
            "Immediate excision in the office without any imaging",
        ],
        "answer": 1,
        "explanation": (
            "A congenital midline nasal dorsal pit, tract, mass, hair, or recurrent sebaceous drainage suggests a "
            "nasal dermoid and possible intracranial extension via the embryologic prenasal/foramen-cecum pathway. "
            "The board-level safety rule is image before incision: obtain MRI (best for intracranial/dural "
            "extension) and thin-cut CT selectively for bony detail; avoid blind probing or office biopsy, which "
            "risk violating an intracranial communication."
        ),
        "why_wrong": [
            "Blind probing or office biopsy should be avoided given the possibility of intracranial communication.",
            "Correct.",
            "A midline nasal mass carries real risk of intracranial extension and must be imaged, not simply "
            "reassured.",
            "Excision requires an approach matched to extent, planned only after imaging defines intracranial "
            "involvement -- not performed blindly in the office.",
        ],
        "board_pearl": "The board-level safety rule for a midline pediatric nasal mass is: image before incision, "
        "because it may communicate with the skull base.",
        "curveball": "What other diagnoses must be distinguished from a nasal dermoid on imaging?",
        "curveball_answer": (
            "Encephalocele and nasal glial heterotopia -- MRI and CT are used selectively for complementary "
            "questions (dural/intracranial extension versus bony detail) to make this distinction and guide "
            "operative planning."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-infantile-hemangioma-phace-01",
        "domain": "Pediatric Otolaryngology",
        "topic": "Infantile Hemangioma / PHACE Syndrome",
        "stem": (
            "An infant has a large, segmental facial hemangioma involving a significant portion of the face. What "
            "should this finding prompt, and what workup is appropriate before starting systemic treatment?"
        ),
        "choices": [
            "Nothing further; treat as a purely cosmetic focal lesion with observation only",
            "Concern for PHACE syndrome; obtain MRI/MRA of the head and neck, echocardiography/aortic-arch "
            "assessment, ophthalmologic examination, and multidisciplinary review before treatment decisions",
            "Immediate surgical excision without any additional workup",
            "Topical timolol alone, without any further evaluation, regardless of lesion size",
        ],
        "answer": 1,
        "explanation": (
            "A large segmental face or scalp infantile hemangioma raises concern for PHACE syndrome (posterior "
            "fossa, arterial, cardiac, eye, and ventral developmental anomalies) rather than representing only a "
            "cosmetic problem. For PHACE risk, obtain MRI/MRA of the head and neck, echocardiography/aortic-arch "
            "assessment, ophthalmologic examination, and multidisciplinary review before treatment decisions, since "
            "cerebrovascular/cardiac anatomy affects safe propranolol initiation and dosing."
        ),
        "why_wrong": [
            "A large segmental lesion is a recognized syndrome marker, not merely cosmetic, and needs evaluation "
            "before treatment.",
            "Correct.",
            "Surgery has a selected role (urgent focal compromise, residual deformity, ulceration, or lesions "
            "unsuitable for medication), not as the default first step, and workup should precede intervention.",
            "Topical timolol suits selected thin superficial lesions, not large segmental lesions with PHACE risk, "
            "which need cerebrovascular/cardiac evaluation before systemic treatment.",
        ],
        "board_pearl": "A large segmental facial hemangioma is a syndrome marker for PHACE -- oral propranolol is "
        "highly effective first-line systemic therapy for high-risk hemangiomas, but PHACE arterial disease changes "
        "pretreatment evaluation and dosing precautions.",
        "curveball": "How do infantile hemangiomas differ biologically from vascular malformations?",
        "curveball_answer": (
            "Infantile hemangiomas are GLUT-1-positive vascular TUMORS that appear in early infancy, proliferate, "
            "then involute, differing from vascular malformations, which are present fully formed at birth and do "
            "not follow this proliferation/involution biology."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-pierre-robin-02",
        "domain": "Pediatric Otolaryngology",
        "topic": "Pierre Robin Sequence",
        "stem": "What workup elements help quantify obstruction severity and identify multilevel or syndromic disease in a newborn with suspected Pierre Robin sequence?",
        "choices": [
            "None are needed; the diagnosis and severity are fully apparent from the facial appearance alone",
            "Assess breathing across sleep and feeding, growth, gas exchange/polysomnography when needed, "
            "swallowing, and airway level by endoscopy; evaluate for associated syndromes such as Stickler based "
            "on phenotype and genetics",
            "Only a chest X-ray is required",
            "Genetic testing alone, without any airway or feeding assessment",
        ],
        "answer": 1,
        "explanation": (
            "Assess breathing across sleep and feeding, growth, gas exchange/polysomnography when needed, "
            "swallowing, and airway level by endoscopy. Evaluate for associated syndromes such as Stickler based on "
            "phenotype and genetics -- isolated and syndromic forms differ in prognosis."
        ),
        "why_wrong": [
            "Facial appearance alone does not quantify functional obstruction severity or identify multilevel/"
            "syndromic disease.",
            "Correct.",
            "A chest X-ray alone does not assess upper-airway obstruction level, feeding, or syndromic features.",
            "Genetic testing is one part of a broader multidisciplinary assessment that must also include airway "
            "and feeding evaluation.",
        ],
        "board_pearl": "Quantify obstruction and identify multilevel/syndromic disease before choosing a tongue, "
        "mandible, or tracheostomy solution.",
        "curveball": "What safe-sleep principle applies to home management of these infants?",
        "curveball_answer": (
            "Home sleep plans must follow infant safe-sleep and specialty guidance rather than casual "
            "prone-position advice, even though positioning can be part of a specialist-directed monitored plan."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-nasal-dermoid-02",
        "domain": "Pediatric Otolaryngology",
        "topic": "Nasal Dermoid Cyst",
        "stem": "What is the definitive treatment for a confirmed nasal dermoid cyst and tract, and what special planning is needed if intracranial extension is suspected?",
        "choices": [
            "Observation only, since most nasal dermoids resolve spontaneously without infection or growth risk",
            "Excise the complete cyst and tract using an approach matched to extent; suspected intracranial disease "
            "requires skull-base/neurosurgical planning",
            "Office drainage of any acute infection is definitive treatment; no further surgery is needed",
            "Radiation therapy is first-line treatment",
        ],
        "answer": 1,
        "explanation": (
            "Excise the complete cyst and tract using an approach matched to extent; suspected intracranial disease "
            "requires skull-base/neurosurgical planning. Observation does not eliminate recurrent infection or "
            "growth risk."
        ),
        "why_wrong": [
            "Observation does not eliminate recurrent infection or growth risk; these lesions require definitive "
            "excision.",
            "Correct.",
            "Acute infection should be treated before definitive surgery when clinically safe, but drainage alone "
            "is not definitive treatment for the cyst and tract.",
            "Radiation therapy has no role in the management of a congenital nasal dermoid cyst.",
        ],
        "board_pearl": "Image before incision: a midline pediatric nasal mass may communicate with the skull base, "
        "so operative planning must account for possible intracranial extension.",
        "curveball": "If the patient presents with acute infection of the dermoid, what is the management sequence?",
        "curveball_answer": (
            "Treat acute infection before definitive surgery when clinically safe -- infection control comes first, "
            "followed by complete excision of the cyst and tract once the acute process has resolved."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-infantile-hemangioma-phace-02",
        "domain": "Pediatric Otolaryngology",
        "topic": "Infantile Hemangioma / PHACE Syndrome",
        "stem": "What is the first-line systemic therapy for a high-risk infantile hemangioma, and what precaution applies specifically in PHACE syndrome?",
        "choices": [
            "Surgical excision is first-line for all high-risk hemangiomas",
            "Oral propranolol is first-line systemic therapy for high-risk hemangiomas; in PHACE, assess "
            "cerebrovascular/cardiac anatomy and use individualized cautious initiation and titration",
            "Topical timolol is first-line for all hemangiomas regardless of size or depth",
            "No treatment is available for high-risk infantile hemangiomas",
        ],
        "answer": 1,
        "explanation": (
            "Oral propranolol is first-line systemic therapy for high-risk hemangiomas. In PHACE, assess "
            "cerebrovascular/cardiac anatomy and use individualized cautious initiation and titration, since "
            "arterial anomalies can affect safety. Topical timolol suits selected thin superficial lesions rather "
            "than high-risk disease."
        ),
        "why_wrong": [
            "Surgery has a selected role (urgent focal compromise, residual deformity, ulceration, or lesions "
            "unsuitable for medication), not as first-line therapy.",
            "Correct.",
            "Topical timolol is reserved for selected thin superficial lesions, not high-risk hemangiomas needing "
            "systemic therapy.",
            "Oral propranolol is a highly effective, well-established treatment option.",
        ],
        "board_pearl": "Propranolol is highly effective, but PHACE arterial disease changes pretreatment evaluation "
        "and dosing precautions -- cerebrovascular/cardiac workup comes before treatment in suspected PHACE.",
        "curveball": "What airway-specific consideration applies to hemangiomas that may involve the airway?",
        "curveball_answer": (
            "Airway disease requires direct airway assessment and coordinated control, in addition to any medical "
            "or surgical management of the cutaneous lesion."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    # ---------------- Laryngology / Voice / Swallowing ----------------
    {
        "id": "v431-lpr-01",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngopharyngeal Reflux (LPR)",
        "stem": (
            "A patient has chronic throat clearing, globus sensation, and mild posterior laryngeal erythema on "
            "exam, with no typical GERD symptoms. What is the most appropriate next step?"
        ),
        "choices": [
            "Diagnose LPR based on the posterior erythema alone and start indefinite high-dose PPI therapy",
            "Recognize that posterior erythema/edema alone cannot diagnose LPR and that this symptom cluster is "
            "nonspecific; for isolated extraesophageal symptoms without typical GERD, favor objective ambulatory "
            "reflux testing before prolonged PPI therapy",
            "Proceed directly to antireflux surgery",
            "Attribute the symptoms definitively to allergy without any further evaluation",
        ],
        "answer": 1,
        "explanation": (
            "Chronic hoarseness, throat clearing, globus, cough, or irritation may be reflux-associated, but this "
            "symptom cluster is nonspecific and commonly overlaps allergy, voice-use, sensory neuropathy, and other "
            "laryngeal disorders. Posterior erythema or edema alone cannot diagnose LPR. For isolated "
            "extraesophageal symptoms without typical GERD, favor objective ambulatory reflux testing before "
            "prolonged PPI therapy."
        ),
        "why_wrong": [
            "Posterior erythema alone is not diagnostic of LPR, and indefinite empiric PPI therapy without "
            "objective confirmation is not the recommended approach for isolated extraesophageal symptoms.",
            "Correct.",
            "Antireflux surgery is reserved for objectively proven reflux with appropriate symptom correlation and "
            "foregut evaluation, not unexplained throat symptoms alone.",
            "The symptom cluster is nonspecific and overlaps multiple etiologies (allergy, voice use, sensory "
            "neuropathy); competing causes and alarm features should be assessed rather than assuming one cause "
            "without evaluation.",
        ],
        "board_pearl": "Avoid turning nonspecific throat symptoms or erythema into a reflex diagnosis of LPR -- "
        "establish whether reflux is objectively or clinically plausible before committing to long-term acid "
        "suppression.",
        "curveball": "When is a time-limited PPI trial reasonable, and what should happen if it fails?",
        "curveball_answer": (
            "A time-limited PPI trial is reasonable when typical GERD symptoms coexist, but response is not "
            "diagnostic; stop escalation and reconsider the phenotype (competing causes) when treatment fails "
            "rather than continuing to increase acid suppression indefinitely."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-lpr-02",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngopharyngeal Reflux (LPR)",
        "stem": "What is a key limitation of using laryngoscopic findings alone to diagnose LPR?",
        "choices": [
            "There is no limitation; laryngoscopic erythema/edema is definitive for LPR",
            "No symptom or laryngoscopic sign uniquely localizes symptoms to reflux, so proximal refluxate exposure "
            "is a plausible mechanism but not a certain diagnosis from exam findings alone",
            "Laryngoscopy cannot be performed in patients with suspected LPR",
            "Laryngoscopic findings are only useful for diagnosing malignancy, never inflammatory conditions",
        ],
        "answer": 1,
        "explanation": (
            "Proximal refluxate exposure may injure pharyngolaryngeal mucosa, but no symptom or laryngoscopic sign "
            "uniquely localizes symptoms to reflux. Perform laryngeal examination and assess competing causes and "
            "alarm features, but recognize the nonspecificity of the exam findings themselves."
        ),
        "why_wrong": [
            "Erythema/edema are nonspecific and commonly seen in the absence of reflux, so they are not definitive.",
            "Correct.",
            "Laryngoscopy is a standard, appropriate part of the workup for suspected LPR.",
            "Laryngoscopy is broadly useful for assessing laryngeal pathology, including inflammatory findings, not "
            "solely malignancy.",
        ],
        "board_pearl": "No single symptom or laryngoscopic finding is diagnostic for LPR -- objective ambulatory "
        "reflux testing is favored over relying on exam appearance alone when symptoms are isolated and "
        "extraesophageal.",
        "curveball": "What other diagnoses commonly overlap with the LPR symptom cluster?",
        "curveball_answer": (
            "Allergy, voice-use disorders, sensory neuropathy, and other laryngeal disorders commonly overlap with "
            "the chronic hoarseness/throat-clearing/globus/cough symptom cluster attributed to LPR."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    # ---------------- Facial Plastics / Trauma ----------------
    {
        "id": "v431-laryngeal-fracture-01",
        "domain": "Facial Plastics / Trauma",
        "topic": "Laryngeal Fracture / External Laryngeal Trauma",
        "stem": (
            "A patient sustains a clothesline-type anterior neck injury and speaks calmly with only mild "
            "hoarseness in the emergency department. What is the most important principle in the initial "
            "evaluation?"
        ),
        "choices": [
            "Mild symptoms reliably rule out significant laryngeal injury, so no further evaluation is needed",
            "Symptom severity does NOT reliably grade structural injury -- a calmly speaking patient can still "
            "develop edema and obstruction over hours, so airway/breathing assessment and coordinated evaluation "
            "must proceed regardless of initial symptom mildness",
            "CT should be obtained first, before any airway assessment, in every case",
            "Blind rapid-sequence intubation is the safest first step in all suspected laryngeal trauma",
        ],
        "answer": 1,
        "explanation": (
            "Hoarseness is common but symptom severity does NOT reliably grade structural injury; a patient "
            "speaking calmly may develop edema and obstruction over hours. Airway, breathing, and circulation "
            "assessment with cervical-spine precautions and senior ENT/anesthesia/trauma support come first, and a "
            "normal-appearing external neck is not a rule-out test."
        ),
        "why_wrong": [
            "Mild initial symptoms do not exclude serious injury -- deterioration can occur over hours.",
            "Correct.",
            "Airway/breathing assessment with cervical-spine precautions comes before imaging; a threatened airway "
            "should not be imaged first, and stable patients are imaged only once safe.",
            "Routine blind rapid-sequence intubation across suspected severe disruption is specifically avoided, "
            "since it may create a false passage or complete separation.",
        ],
        "board_pearl": "Suspect after anterior neck trauma plus voice, breathing, or swallowing change; do "
        "airway/c-spine evaluation BEFORE CT. A normal-appearing external neck or calm speech is not a rule-out "
        "test.",
        "curveball": "What airway management approach is favored for a patient with a clearly unstable laryngeal framework?",
        "curveball_answer": (
            "Choice among controlled fiberoptic intubation with immediate surgical backup and awake/local "
            "tracheostomy depends on anatomy, stability, expertise, and associated injuries; with a clearly "
            "unstable framework or major separation, a controlled awake tracheostomy below the injury is often "
            "favored, securing a surgical airway below the injury when feasible."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-laryngeal-fracture-02",
        "domain": "Facial Plastics / Trauma",
        "topic": "Laryngeal Fracture / External Laryngeal Trauma",
        "stem": (
            "A patient has a Schaefer-Fuhrman group III laryngeal injury (massive edema, exposed cartilage, and "
            "vocal-fold immobility) on flexible laryngoscopy and CT. What is the recommended timing for operative "
            "repair, and what is a common misconception to avoid?"
        ),
        "choices": [
            "Repair should be delayed 3-10 days as the required standard, based on a published mean time to repair",
            "Expeditious repair is preferred when clinically feasible -- exploration within 24-48 hours (Pasha: "
            "ideally within 2-3 days after stabilization); a published mean of 5.6 days (range 3-10) reflects real "
            "practice variation, not a required or optimal delay",
            "No operative intervention is ever indicated for group III injuries",
            "Repair timing does not matter as long as it occurs within one year",
        ],
        "answer": 1,
        "explanation": (
            "Displaced fractures, exposed cartilage, large mucosal lacerations, and persistent immobility (group "
            "III-V) require prompt operative assessment/repair. Expeditious repair is preferred when clinically "
            "feasible: exploration within 24-48 hours, with Pasha describing repair ideally within 2-3 days after "
            "stabilization. A published mean of 5.6 days (range 3-10) must not be misread as a required delay -- "
            "this is a key teaching correction to avoid."
        ),
        "why_wrong": [
            "This misreads a published cohort mean/range as a mandated delay -- the actual recommendation favors "
            "early reconstruction when safe, often within 24-48 hours.",
            "Correct.",
            "Group III-V injuries with major mucosal/cartilage instability warrant early operative evaluation, not "
            "universal nonoperative management.",
            "Repair timing matters significantly -- delayed repair risks worse outcomes (stenosis, dysphonia, "
            "dysphagia); it is not timing-agnostic.",
        ],
        "board_pearl": "NEVER teach waiting 3-10 days as the optimal standard for laryngeal fracture repair -- "
        "early reconstruction when safe (often within 24-48 hours) is favored; this is a classic point of "
        "confusion to correct explicitly.",
        "curveball": "What late complications can result from malrepair or delayed repair?",
        "curveball_answer": (
            "Glottic/subglottic stenosis, web formation, dysphonia, dysphagia/aspiration, vocal-fold immobility, "
            "and decannulation failure -- restoring the anterior commissure and mucosal coverage properly is key to "
            "avoiding these."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-blepharoplasty-eyelid-01",
        "domain": "Facial Plastics / Trauma",
        "topic": "Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)",
        "stem": (
            "A patient presents with a 'droopy eyelid.' What is the most important first step before planning "
            "surgical correction?"
        ),
        "choices": [
            "Proceed directly to blepharoplasty skin excision for any droopy eyelid appearance",
            "Identify the failing layer and vector -- distinguishing dermatochalasis (skin excess) from true "
            "ptosis (levator/aponeurotic dysfunction), ectropion (outward, horizontal laxity), and entropion "
            "(inward) -- and assess ocular surface/lower-lid support, since neurogenic ptosis must not be mistaken "
            "for aging",
            "Assume all eyelid malposition in an older patient is due to aging skin excess",
            "Treat with botulinum toxin as definitive therapy for all eyelid malposition",
        ],
        "answer": 1,
        "explanation": (
            "'Droopy eyelid' is not one diagnosis. Skin excess (dermatochalasis), levator/aponeurotic dysfunction "
            "(true ptosis), horizontal laxity (ectropion), and anterior/posterior lamellar imbalance (entropion) "
            "are different defects requiring different repairs; neurogenic ptosis must not be mistaken for aging. "
            "Identify the failing layer and vector, and assess ocular surface and lower-lid support before removing "
            "tissue."
        ),
        "why_wrong": [
            "Reflexive skin excision without distinguishing the underlying defect risks treating the wrong problem "
            "and causing complications like lagophthalmos.",
            "Correct.",
            "Ptosis in particular can be neurogenic and should not be assumed to be simple age-related skin excess "
            "without evaluation.",
            "Botulinum toxin has only selected temporary uses; structural disease requires anatomic correction.",
        ],
        "board_pearl": "Identify the failing layer and vector before removing tissue -- measure margin-reflex "
        "distance and levator function, test lower-lid distraction/snap-back, and assess the ocular surface and dry "
        "eye before any procedure.",
        "curveball": "What complications must be specifically avoided during blepharoplasty and eyelid malposition surgery?",
        "curveball_answer": (
            "Overresection, lagophthalmos, ectropion, and retrobulbar hematoma -- blepharoplasty conservatively "
            "removes or repositions tissue, ptosis repair targets the levator/Müller mechanisms, lateral tarsal "
            "strip treats lax ectropion, and entropion repair corrects retractors and overriding."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-blepharoplasty-eyelid-02",
        "domain": "Facial Plastics / Trauma",
        "topic": "Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)",
        "stem": "What preoperative measurements and assessments are used to characterize eyelid malposition before planning surgery?",
        "choices": [
            "None are needed; visual inspection alone is sufficient",
            "Measure margin-reflex distance and levator function, test lower-lid distraction/snap-back, examine "
            "pupils and motility, assess ocular surface and dry eye, and obtain formal visual fields when "
            "documenting functional upper-lid obstruction",
            "Only intraocular pressure measurement is relevant",
            "A single photograph is sufficient for surgical planning",
        ],
        "answer": 1,
        "explanation": (
            "Measure margin-reflex distance and levator function, test lower-lid distraction/snap-back, examine "
            "pupils and motility, assess ocular surface and dry eye, and obtain formal visual fields when "
            "documenting functional upper-lid obstruction -- these define which layer/mechanism is failing and "
            "guide the specific repair chosen."
        ),
        "why_wrong": [
            "Visual inspection alone cannot distinguish dermatochalasis, true ptosis, ectropion, and entropion, "
            "which require different repairs.",
            "Correct.",
            "Intraocular pressure is not part of the standard eyelid-malposition workup described here.",
            "A single photograph does not substitute for functional measurements like margin-reflex distance and "
            "levator function.",
        ],
        "board_pearl": "Assess ocular surface and lower-lid support before removing tissue -- functional "
        "measurements, not appearance alone, should drive the surgical plan.",
        "curveball": "What conservative (nonsurgical) options can bridge mild eyelid malposition?",
        "curveball_answer": (
            "Lubrication and exposure protection can bridge mild malposition; botulinum toxin has selected "
            "temporary uses, but structural disease still requires anatomic correction."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-cervical-necrotizing-fasciitis-02",
        "domain": "General ENT / Emergencies",
        "topic": "Cervical Necrotizing Fasciitis",
        "stem": "What is the underlying pathophysiology of cervical necrotizing fasciitis, and what dangerous extension pattern should be anticipated?",
        "choices": [
            "A localized, monomicrobial abscess confined strictly to the neck with no risk of further spread",
            "Polymicrobial infection spreading along fascial planes with small-vessel thrombosis and necrosis; "
            "danger-space extension can produce descending necrotizing mediastinitis",
            "A purely viral process with no role for surgical intervention",
            "An autoimmune process unrelated to any preceding infection",
        ],
        "answer": 1,
        "explanation": (
            "Polymicrobial infection spreads along fascial planes, thromboses small vessels, and causes necrosis; "
            "danger-space extension can produce descending necrotizing mediastinitis, which is why thoracic "
            "extension requires an early thoracic-surgery drainage strategy."
        ),
        "why_wrong": [
            "This is a spreading, polymicrobial process, not a localized monomicrobial abscess -- it tracks along "
            "fascial planes and can extend well beyond the initial site.",
            "Correct.",
            "This is a bacterial (polymicrobial), not viral, process requiring urgent operative source control.",
            "It typically follows an odontogenic/pharyngeal infection rather than arising as an autoimmune process.",
        ],
        "board_pearl": "Danger-space extension can produce descending necrotizing mediastinitis -- thoracic "
        "extension requires an early thoracic-surgery drainage strategy, not neck debridement alone.",
        "curveball": "What supportive therapies accompany surgical debridement?",
        "curveball_answer": (
            "Secure the threatened airway, resuscitate, start broad aerobic/anaerobic coverage with "
            "toxin-suppressing therapy when indicated, and provide ICU support -- but antibiotics cannot replace "
            "debridement."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    # ---------------- General ENT / Emergencies ----------------
    {
        "id": "v431-penetrating-blunt-neck-trauma-01",
        "domain": "General ENT / Emergencies",
        "topic": "Penetrating and Blunt Neck Trauma",
        "stem": (
            "A hemodynamically stable patient has a penetrating neck wound with platysma violation but no hard "
            "signs of vascular, airway, or aerodigestive injury. What is the most appropriate evaluation strategy?"
        ),
        "choices": [
            "Mandatory surgical exploration of every Zone II wound with platysma violation",
            "Selective CTA-based evaluation and serial examination (a 'no-zone' pathway) based on mechanism and "
            "findings, rather than mandatory Zone-II exploration",
            "No imaging or further workup, since the patient is currently stable",
            "Immediate blind wound exploration and clamping of any visible vessel",
        ],
        "answer": 1,
        "explanation": (
            "Classic zones (I clavicle-to-cricoid, II cricoid-to-mandibular angle, III angle-to-skull base) "
            "describe exposure, but stable penetrating trauma is commonly evaluated with a selective no-zone "
            "pathway: stable selected patients undergo CTA based on mechanism and findings rather than mandatory "
            "Zone-II exploration."
        ),
        "why_wrong": [
            "Mandatory exploration of every Zone II wound has been superseded by selective, CTA-based evaluation "
            "for stable patients.",
            "Correct.",
            "A stable patient with platysma violation still requires evaluation (CTA and serial exams based on "
            "mechanism/findings); stability alone does not exclude significant injury.",
            "Blind clamping or probing of a neck wound is specifically avoided; hemorrhage is controlled with "
            "direct pressure and resuscitation, with definitive vascular control obtained in a controlled operative "
            "setting when needed.",
        ],
        "board_pearl": "Resuscitation plus hard-versus-soft signs first. Stable patients receive selective "
        "CTA/no-zone assessment; unstable hemorrhage demands immediate control.",
        "curveball": "Does a negative CTA definitively exclude an esophageal injury?",
        "curveball_answer": (
            "No -- CTA alone cannot exclude all esophageal injuries when trajectory, symptoms, air, or CT changes "
            "remain suspicious; add contrast evaluation and/or esophagoscopy in that setting."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-penetrating-blunt-neck-trauma-02",
        "domain": "General ENT / Emergencies",
        "topic": "Penetrating and Blunt Neck Trauma",
        "stem": "What are 'hard signs' of significant neck trauma that mandate immediate operative/endovascular management without routine imaging delay?",
        "choices": [
            "A nonexpanding hematoma and minor hemoptysis alone",
            "Active arterial bleeding, expanding hematoma, shock from neck injury, bruit/thrill, major airway "
            "compromise, air bubbling from the wound, or evolving focal neurologic deficit",
            "Mild dysphonia and subcutaneous emphysema alone",
            "Any visible external wound regardless of depth",
        ],
        "answer": 1,
        "explanation": (
            "Hard signs -- active arterial bleeding, expanding hematoma, shock from neck injury, bruit/thrill, "
            "major airway compromise, air bubbling from the wound, or evolving focal neurologic deficit -- mandate "
            "unstable patients or hard-sign patients proceed to immediate operative/endovascular management without "
            "routine imaging delay. Soft signs (nonexpanding hematoma, dysphonia, dysphagia, minor hemoptysis, or "
            "subcutaneous emphysema) instead prompt selective CTA-based workup."
        ),
        "why_wrong": [
            "A nonexpanding hematoma and minor hemoptysis are classified as soft signs, prompting selective "
            "workup rather than immediate operative management.",
            "Correct.",
            "Mild dysphonia and subcutaneous emphysema are soft signs, not hard signs.",
            "A superficial wound without platysma violation or the listed hard-sign findings does not by itself "
            "mandate immediate operative management.",
        ],
        "board_pearl": "Hard signs mandate immediate control; soft signs prompt selective CTA-based observation and "
        "serial examination -- know which category each finding belongs to.",
        "curveball": "What blunt-trauma-specific injury must be screened for based on mechanism/risk?",
        "curveball_answer": (
            "Occult carotid or vertebral artery dissection -- blunt cerebrovascular injury screening is "
            "mechanism/risk based, in addition to considering laryngotracheal disruption and pharyngoesophageal "
            "injury from blunt mechanisms."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-cervical-necrotizing-fasciitis-01",
        "domain": "General ENT / Emergencies",
        "topic": "Cervical Necrotizing Fasciitis",
        "stem": (
            "A patient develops rapidly progressive neck pain and swelling with systemic toxicity, pain out of "
            "proportion to exam findings, and skin duskiness after an odontogenic infection. CT shows no gas in the "
            "soft tissues. What is the most appropriate next step?"
        ),
        "choices": [
            "Rule out necrotizing fasciitis since there is no gas on CT, and continue antibiotics alone",
            "Recognize that gas may be absent on imaging and that this is a clinical diagnosis; secure the airway, "
            "resuscitate, start broad-spectrum coverage, and proceed immediately to wide operative debridement "
            "rather than waiting for a discrete abscess or reassuring scan",
            "Wait for a follow-up CT in 24 hours to reassess before considering surgery",
            "Treat with antibiotics alone until a discrete abscess forms",
        ],
        "answer": 1,
        "explanation": (
            "Cervical necrotizing fasciitis is a clinical diagnosis; gas may be absent on imaging. Rapidly "
            "progressive neck pain/swelling, systemic toxicity, pain out of proportion, skin duskiness, bullae, or "
            "crepitus after odontogenic/pharyngeal infection should trigger immediate concern. Secure the airway, "
            "resuscitate, start broad aerobic/anaerobic coverage, and proceed to immediate wide debridement to "
            "viable bleeding tissue -- antibiotics cannot replace debridement, and delay to operative source "
            "control is lethal."
        ),
        "why_wrong": [
            "Absence of gas on CT does not rule out necrotizing fasciitis, since it is a clinical diagnosis and gas "
            "may be absent.",
            "Correct.",
            "Waiting for repeat imaging delays life-saving operative source control, which should not be delayed "
            "for a 'reassuring' scan.",
            "Antibiotics alone cannot replace debridement; delay while awaiting abscess formation is dangerous.",
        ],
        "board_pearl": "Do not wait for a discrete abscess or reassuring scan -- rapid progression plus toxicity "
        "makes delay to operative source control lethal in cervical necrotizing fasciitis.",
        "curveball": "What operative principle governs the extent and follow-through of debridement?",
        "curveball_answer": (
            "Perform immediate wide debridement to viable bleeding tissue, drain all involved spaces, and plan "
            "serial re-exploration; thoracic extension (danger-space spread to descending necrotizing "
            "mediastinitis) requires an early thoracic-surgery drainage strategy."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v431-ear-nasal-foreign-body-01",
        "domain": "General ENT / Emergencies",
        "topic": "Ear and Nasal Foreign Body Removal",
        "stem": (
            "A toddler is found with a coin-like button battery lodged in the nasal cavity. What is the most "
            "appropriate management approach?"
        ),
        "choices": [
            "Schedule removal electively within the next few days since the child is otherwise asymptomatic",
            "Treat this as a tissue-destructive emergency requiring immediate removal, avoiding irrigation, with "
            "controlled microscopic/endoscopic removal under sedation or anesthesia if needed for a deep/impacted "
            "object or poor cooperation",
            "Attempt irrigation first to flush the battery out",
            "Obtain imaging before any attempt at removal, delaying intervention",
        ],
        "answer": 1,
        "explanation": (
            "Button batteries (and paired high-powered magnets) are tissue-destructive emergencies and must be "
            "removed immediately -- batteries generate alkaline electrical injury. Avoid irrigation for batteries. "
            "Proceed to controlled microscopic/endoscopic removal with sedation or anesthesia for batteries, "
            "deep/impacted objects, poor cooperation, adjacent critical structures, or failed attempts; imaging is "
            "selective and must not delay battery removal."
        ),
        "why_wrong": [
            "Battery removal must not be delayed -- it is a tissue-destructive emergency requiring immediate "
            "action, not elective scheduling.",
            "Correct.",
            "Irrigation is specifically avoided for batteries because of the risk of worsening electrical/chemical "
            "injury.",
            "Imaging must not delay battery removal, which is selective and secondary to prompt extraction.",
        ],
        "board_pearl": "Remove batteries and dangerous magnets immediately -- the safest first attempt is the best "
        "attempt, and technique should match object geometry.",
        "curveball": "How does the approach differ for a live insect in the ear canal?",
        "curveball_answer": (
            "Immobilize an aural insect with an appropriate agent only when tympanic-membrane integrity and "
            "material safety permit it, since live insects can abrade the canal -- this differs from the "
            "battery/magnet approach, which prioritizes immediate mechanical removal rather than immobilization "
            "first."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v431-ear-nasal-foreign-body-02",
        "domain": "General ENT / Emergencies",
        "topic": "Ear and Nasal Foreign Body Removal",
        "stem": "How should the technique for removing an ear or nasal foreign body be selected?",
        "choices": [
            "The same tool and technique should be used for every foreign body regardless of shape or material",
            "Choose the tool by shape and material: forceps for graspable objects, hook/curette or balloon behind "
            "smooth objects, suction when suitable, and positive pressure for selected nasal cases",
            "Repeated forceful attempts with the same instrument are preferred over changing technique",
            "General anesthesia is required for every foreign body removal regardless of cooperation or depth",
        ],
        "answer": 1,
        "explanation": (
            "Choose the tool by shape: forceps for graspable objects, hook/curette or balloon behind smooth "
            "objects, suction when suitable, and positive pressure for selected nasal cases. The safest first "
            "attempt is the best attempt -- match technique to object geometry and limit traumatic retries."
        ),
        "why_wrong": [
            "Technique should be matched to the object's shape and material, not applied uniformly.",
            "Correct.",
            "Repeated forceful attempts with an unsuitable instrument risk trauma and pushing the object deeper; "
            "traumatic retries should be limited.",
            "Sedation or anesthesia is reserved for batteries, deep/impacted objects, poor cooperation, adjacent "
            "critical structures, or failed attempts -- not required for every case.",
        ],
        "board_pearl": "The safest first attempt is the best attempt -- match technique to object geometry and "
        "re-examine afterward for injury or retained fragments.",
        "curveball": "What must always be done after successful removal?",
        "curveball_answer": (
            "Re-examine the ear or nose afterward for injury (e.g., canal trauma, tympanic membrane perforation) or "
            "retained fragments, since removal attempts themselves can cause trauma."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
]


def apply_clinical_challenge_gapfill_v431(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"challenges_added": []}

    topic_domains = {
        card.get("topic"): domain
        for domain, cards in modules.items()
        for card in cards
        if card.get("topic")
    }

    challenges = data_module.CLINICAL_CHALLENGES_V119
    existing_ids = {q.get("id") for q in challenges}
    for q in CLINICAL_CHALLENGES_NEW:
        if q["id"] in existing_ids:
            continue
        row = dict(q)
        canonical_domain = topic_domains.get(row["topic"])
        if canonical_domain is None:
            raise RuntimeError(f"v43.1: challenge topic missing from curriculum: {row['topic']}")
        row["concept_id"] = _v6_item_id(canonical_domain, row["topic"])
        challenges.append(row)
        existing_ids.add(row["id"])
        result["challenges_added"].append(row["id"])

    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in challenges if q.get("id")}

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result
